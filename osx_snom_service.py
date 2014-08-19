from AppKit import *
from Foundation import *
from snomdialservice import *
from PyObjCTools import AppHelper


def main():
    # NSLog(u"main()")
    serviceProvider = SnomDialService.alloc().init()
    # NSLog(u"serviceProvider = %s", serviceProvider)
    NSRegisterServicesProvider(serviceProvider, u"PyObjCSnomDialService")
    # NSLog(u"registered as PyObjCSimpleService")
    AppHelper.runConsoleEventLoop()


if __name__ == '__main__':
    main()
