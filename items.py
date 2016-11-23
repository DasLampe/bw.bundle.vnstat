pkg_dnf = {
    'vnstat': {},
}

svc_systemd = {
    'vnstat': {
        'enabled': True,
        'needs': [
            "pkg_dnf:vnstat",
        ],
    },
}

actions = {}

files = {
    '/etc/sysconfig/vnstat': {
        'source': "sysconfig_vnstat",
        'owner': "root",
        'mode': "0644",
        'content_type': "mako",
        'needs': [
            "pkg_dnf:vnstat",
        ],
        'triggers': [
            "svc_systemd:vnstat:restart",
        ],
    },
    '/etc/vnstat.conf': {
        'source': "vnstat.conf",
        'owner': "root",
        'mode': "0644",
        'content_type': "mako",
        'needs': [
            "pkg_dnf:vnstat",
        ],
        'triggers': [
            "svc_systemd:vnstat:restart",
        ],
    },
}

directories = {
    "/var/lib/vnstat": {
        "mode": "6755",
        "owner": "vnstat",
        "group": "vnstat",
        'needs': [
            "pkg_dnf:vnstat",
        ],
    },
}

for interface in node.metadata['interfaces']:
    actions['vnstat_create_database_{}'.format(interface)] = {
        'command': "vnstat -u -i {}".format(interface),
        'unless': "test -f /var/lib/vnstat/{}".format(interface),
        'cascade_skip': False,
        'needs': [
            "pkg_dnf:vnstat",
        ],
        'triggers': [
            "svc_systemd:vnstat:restart",
        ],
    }
