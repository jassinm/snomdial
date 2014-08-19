init:
	sudo /usr/bin/easy_install phonenumbers

configure:
	@read -p "Enter snom host ip:" SNOMHOST; \
	sed  -i '' 's/^HOST.*/HOST="'$$SNOMHOST'"/' ./snomaddbookplugin.py
	@read -p "Enter snom user:" SNOMUSER; \
	sed  -i '' 's/^USER.*/USER="'$$SNOMUSER'"/' ./snomaddbookplugin.py
	@read -p "Enter snom password:" SNOMPWD; \
	sed  -i '' 's/^USER.*/USER="'$$SNOMPWD'"/' ./snomaddbookplugin.py
	@read -p "Enter country code:" CCODE; \
	sed  -i '' 's/^CCODE.*/CCODE="'$$CCODE'"/' ./snomaddbookplugin.py



install: init configure
	/usr/bin/python setup.py install
	/usr/bin/python pluginsetup.py py2app
	mv ./dist/PySnomAddressBookDial.bundle ~/Library/Address\ Book\ Plug-Ins/
