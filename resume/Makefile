TO_PDF = /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
         --headless --disable-gpu --content-shell-host-window-size=1200x1024 \
         --print-to-pdf=output.pdf
include ~/.cloudflare_rc

ifndef VERBOSE
.SILENT:
endif

.PHONY: css pdfs html

all: pdfs html css

css: css/all.css css/bootstrap.css css/font-awesome.css

pdfs: pdf/cv_en_florian_vichot.pdf pdf/cv_fr_florian_vichot.pdf

html: cv_en_florian_vichot.html cv_fr_florian_vichot.html

pdf/%.pdf: %.html
	$(TO_PDF) file://$(PWD)/$<
	mkdir -p pdf
	mv output.pdf $@

purge:
	curl -s -X DELETE "https://api.cloudflare.com/client/v4/zones/$(zone)/purge_cache" \
         -H "X-Auth-Email: $(user)" \
         -H "X-Auth-Key: $(key)" \
         -H "Content-Type: application/json" \
         --data '{"purge_everything":true}' >/dev/null \
         && echo "Cloudflare cache purged!"
