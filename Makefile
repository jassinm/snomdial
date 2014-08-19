init:
	sudo /usr/bin/easy_install phonenumbers

configure:
	@read -p "Enter snom host ip:" SNOMHOST; \
	sed  -i '' 's/^HOST.*/HOST="'$$SNOMHOST'"/' ./snomaddbookplugin.py
	sed  -i '' 's/^HOST.*/HOST="'$$SNOMHOST'"/' ./snomdialservice.py
	@read -p "Enter snom user:" SNOMUSER; \
	sed  -i '' 's/^USER.*/USER="'$$SNOMUSER'"/' ./snomaddbookplugin.py
	sed  -i '' 's/^USER.*/USER="'$$SNOMUSER'"/' ./snomdialservice.py
	@read -p "Enter snom password:" SNOMPWD; \
	sed  -i '' 's/^PWD.*/PWD="'$$SNOMPWD'"/' ./snomaddbookplugin.py
	sed  -i '' 's/^PWD.*/PWD="'$$SNOMPWD'"/' ./snomdialservice.py
	@read -p "Enter country code:" CCODE; \
	sed  -i '' 's/^CCODE.*/CCODE="'$$CCODE'"/' ./snomaddbookplugin.py
	sed  -i '' 's/^CCODE.*/CCODE="'$$CCODE'"/' ./snomdialservice.py



install: init configure
	/usr/bin/python setup.py install
	/usr/bin/python osx_addrbook_snomdial_setup.py py2app
	mv ./dist/PySnomAddressBookDial.bundle ~/Library/Address\ Book\ Plug-Ins/
	/usr/bin/python osx_snom_service_setup.py py2app --site-packages
