from distutils.core import setup

infoPlist = dict(
    CFBundleName='PySnomAddressBookDial',
    CFBundleGetInfoString='Snom dial plugin for AddressBook',
    CFBundleVersion='0.1',
    CFBundleShortVersionString='0.1',
    NSPrincipalClass='PySnomAddressBookDial',
)

setup(
    name='PyAddressLabel',
    plugin=['snomaddbookplugin.py'],
    data_files=[],
    options=dict(py2app=dict(
        extension=".bundle",
        packages=["snomdial"],
        plist=infoPlist,
    )),
)
