BUILD_DIR=public

build-gh-pages: clean
	hugo -D --baseURL="https://matthew-brett.github.io/miles-bell"

gh-pages: build-gh-pages
	ghp-import -n $(BUILD_DIR) -p -f

clean:
	rm -rf $(BUILD_DIR)
