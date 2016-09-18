pkg_yum = {
    'vnstat': {},
}

svc_systemd = {
    'vnstat': {
        'enabled': True,
        'needs': [
            "pkg_yum:vnstat",
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
            "pkg_yum:vnstat",
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
            "pkg_yum:vnstat",
        ],
        'triggers': [
            "svc_systemd:vnstat:restart",
        ],
    },
}

for interface in node.metadata['interfaces']:
    actions['vnstat_create_database_{}'.format(interface)] = {
        'command': "vnstat -u -i {}".format(interface),
        'unless': "test -f /var/lib/vnstat/{}".format(interface),
        'cascade_skip': False,
        'needs': [
            "pkg_yum:vnstat",
        ],
        'triggers': [
            "svc_systemd:vnstat:restart",
        ],
    }
