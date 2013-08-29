echo:
	@echo "\n============================"
	@echo "Styling and profiling"
	@echo "============================\n"
	@say "building your stylesheet"
	@mkdir -p ny-py/static/css
	@lessc --compress --verbose ny-py/design/less/style.less ny-py/static/css/style.min.css
	@lessc --compress --verbose ny-py/design/less/landing.less ny-py/static/css/landing.min.css
	@say "has finished successfully"
	@echo "\n==========================="
	@echo "Booyah"
	@echo "===========================\n"

clean:
	rm -r ny-py/static/css

css: css/*.css

css/*.css: less/*.less
	@echo "\n============================"
	@echo "Styling and profiling"
	@echo "============================\n"
	@say "building your stylesheet"
	@mkdir -p ny-py/static/css
	@lessc --compress --verbose ny-py/design/less/style.less ny-py/static/css/style.min.css
	@lessc --compress --verbose ny-py/design/less/landing.less ny-py/static/css/landing.min.css
	@say "has finished successfully"
	@echo "\n==========================="
	@echo "Booyah"
	@echo "===========================\n"

watch:
	echo "Watching less files..."; \
	watchr -e "watch('less/.*\.less') { system 'make css' }"

.PHONY:
	css watch