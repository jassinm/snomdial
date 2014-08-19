from distutils.core import setup
import py2app

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
        site_packages=True,
        includes=["phonenumbers"],
        packages=["snomdial"],
        plist=infoPlist,
    )),
)
