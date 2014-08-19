init:
	sudo /usr/bin/easy_install phonenumbers
	/usr/bin/python -c 'from phonenumbers import PhoneMetadata; PhoneMetadata.load_all()'

configure:
	rm -f config.py
	@echo "HOST = \"\"\nUSER = \"\"\nPWD =\"\"\nCCODE = \"\"" >> config.py
	@read -p "Enter snom host ip:" SNOMHOST; \
	sed  -i '' 's/^HOST.*/HOST="'$$SNOMHOST'"/' ./config.py
	@read -p "Enter snom user:" SNOMUSER; \
	sed  -i '' 's/^USER.*/USER="'$$SNOMUSER'"/' ./config.py
	@read -p "Enter snom password:" SNOMPWD; \
	sed  -i '' 's/^PWD.*/PWD="'$$SNOMPWD'"/' ./config.py
	@read -p "Enter country code:" CCODE; \
	sed  -i '' 's/^CCODE.*/CCODE="'$$CCODE'"/' ./config.py



install: init
	/usr/bin/python setup.py install
	/usr/bin/python osx_addrbook_snomdial_setup.py py2app
	mv ./dist/PySnomAddressBookDial.bundle ~/Library/Address\ Book\ Plug-Ins/
	/usr/bin/python osx_snom_service_setup.py py2app --site-packages
