# bundlewrap-centos-vnstat

`bundlewrap-centos-vnstat` installs and configures vnstat.
It will create the vnstat databases for all given interfaces.

The `main_interface` will be used when you execute `vnstat` without parameters.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| CentOS 7    | `[x]` |
| Fedora 24   | `[x]` |
| RHEL 7      | `[x]` |
| Fedberry 23 | `[ ]` |

## Requirements

* Bundles:
  * [epel](https://github.com/rullmann/bundlewrap-centos-epel)
    * Required for RHEL and CentOS, but not Fedora

## Metadata

    'metadata': {
        'interfaces': {
            'eth0': {
                'ip_address': '172.16.16.42',
            },
            'tun0': {
                'ip_address': '10.10.10.42',
            },
        },
        'main_interface': 'eth0',
    }