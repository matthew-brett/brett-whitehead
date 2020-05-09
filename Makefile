PDSITE=./.pdsite/bin/pdsite
BUILD_DIR=.html

build:
	$(PDSITE) build

gh-pages: build
	sh .push-gh-pages/push-gh-pages.sh $(BUILD_DIR)
