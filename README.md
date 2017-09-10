# bundlewrap-vnstat

`bundlewrap-vnstat` installs and configures vnstat.
It will create the vnstat databases for all given interfaces.

The `main_interface` will be used when you execute `vnstat` without parameters.

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
