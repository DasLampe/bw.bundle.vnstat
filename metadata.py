@metadata_processor
def add_apt_packages(metadata):
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        metadata['apt']['packages']['vnstat'] = {'installed': True}

    return metadata, DONE

def add_vnstat_user(metadata):
    if node.has_bundle("users"):
        metadata['users']['vnstat'] = {}