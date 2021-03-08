all: serve

serve:
	Rscript -e "blogdown::serve_site()"

build:
	Rscript -e "blogdown::build_site()"

deploy: build
	rsync -zrvce 'ssh -p 18765' public/ u525-8pjzevoxexom@sm32.siteground.biz:~/www/stuartlee.org/public_html


clean:
	rm -rf public
	rm -rf blogdown
