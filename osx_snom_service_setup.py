from distutils.core import setup
import py2app

plist = dict(
    CFBundleIdentifier=u'net.sf.pyobjc.PyObjCSnomDialService',
    CFBundleName=u'PyObjCSnomDialService',
    LSBackgroundOnly=1,
    NSServices=[
        dict(
            NSMenuItem=dict(
                default=u'Dial With Snom',
            ),
            NSMessage=u'doSnomDialService',
            NSPortName=u'PyObjCSnomDialService',
            NSSendTypes=[
                u'NSStringPboardType',
            ],
        ),
    ],
)


setup(
    name='SnomDial Service',
    app=["osx_snom_service.py"],
    options=dict(py2app=dict(plist=plist,
                             packages=["snomdial"])),
)
