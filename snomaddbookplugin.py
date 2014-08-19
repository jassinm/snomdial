from AddressBook import *
from AppKit import *
from snomdial import dial_with_snom
from config import HOST, USER, PWD, CCODE


class PySnomAddressBookDial(NSObject):
    def actionProperty(self):
        return kABPhoneProperty

    def titleForPerson_identifier_(self, person, identifier):
        return u"Dial with Snom"

    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return len(person.phone()) > 0

    def performActionForPerson_identifier_(self, person, identifier):
        phones = person.valueForProperty_(kABPhoneProperty)
        p = phones.valueAtIndex_(phones.indexForIdentifier_(identifier))
        dial_with_snom(HOST, USER, PWD, p, CCODE)
