PDSITE=./.pdsite/bin/pdsite
BUILD_DIR=.html
SCRIPTS=.scripts

build:
	rm -rf $(BUILD_DIR)
	$(PDSITE) build

gh-pages: build
	ghp-import -n $(BUILD_DIR) -p -f
