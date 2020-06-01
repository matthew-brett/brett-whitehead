BUILD_DIR=public

gh-pages: build-gh-pages
	ghp-import -n $(BUILD_DIR) -p -f

serve:
	hugo server -D

build-gh-pages: clean
	hugo -D --baseURL="https://matthew-brett.github.io/brett-whitehead"

clean:
	rm -rf $(BUILD_DIR)
