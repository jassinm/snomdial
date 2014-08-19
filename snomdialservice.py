import objc
from Foundation import *
from AppKit import *
import objc
from snomdial import dial_with_snom

HOST = ""
USER = ""
PWD = ""
CCODE = "US"


def serviceSelector(fn):
    # this is the signature of service selectors
    return objc.selector(fn, signature="v@:@@o^@")


def ERROR(s):
    # NSLog(u"ERROR: %s", s)
    return s


class SnomDialService(NSObject):
    @serviceSelector
    def doSnomDialService_userData_error_(self, pboard, data, error):
        # NSLog(u"doOpenFileService_userData_error_(%s, %s)", pboard, data)
        try:
            types = pboard.types()
            pboardString = None
            if NSStringPboardType in types:
                pboardString = pboard.stringForType_(NSStringPboardType)
            if pboardString is None:
                return ERROR(NSLocalizedString(
                    "Error: Pasteboard doesn't contain a string.",
                    "Pasteboard couldn't give string."
                ))
            # NSLog(u"******** : %s" % pboardString)
            dial_with_snom(HOST, USER, PWD, pboardString, CCODE)

            # if not NSWorkspace.sharedWorkspace().openFile_(pboardString):
            #     return ERROR(NSLocalizedString(
            #         "Error: Couldn't open file %s.",
            #         "Couldn't perform service operation for file %s."
            #     ) % pboardString)

            return ERROR(None)
        except:
            import traceback
            traceback.print_exc()
            return ERROR(u'Exception, see traceback')
