ifndef VERBOSE
.SILENT:
endif

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    TO_PDF = chromium --headless --disable-gpu --content-shell-host-window-size=1200x1024 \
                      --print-to-pdf=$@ file://$(PWD)/$<
endif
ifeq ($(UNAME_S),Darwin)
#    CHROME_APP := /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome
    CHROME_APP := /Applications/Chromium.app/Contents/MacOS/Chromium
#    TO_PDF = $(CHROME_APP) --headless --disable-gpu --content-shell-host-window-size=1200x1024 \
                           # --print-to-pdf=$@ $<
    TO_PDF = wkhtmltopdf --dpi 330 --print-media-type $< $@
endif

include ~/.cloudflare_rc

FILES = cv_en_florian_vichot.html cv_fr_florian_vichot.html
FILES_PDFS = $(FILES:%.html=pdf/%.pdf)
# TEMPLATE = templates/cv_html.tmpl
TEMPLATE = templates/oz_cv_html.tmpl

all: $(FILES_PDFS) $(FILES)

%.html: confs/%.toml $(TEMPLATE) css/all.css css/bootstrap.css css/font-awesome.css scripts/render_toml.py Makefile
	scripts/render_toml.py -t $(TEMPLATE) $< $@
	echo Generated $@

pdf/%.pdf: %.html Makefile
	mkdir -p pdf
	$(TO_PDF)
	echo Generated $@

# For some reason, purge_everything doesn't work, so purge each page...
purge:
	curl -s -X DELETE "https://api.cloudflare.com/client/v4/zones/$(zone)/purge_cache" \
         -H "X-Auth-Email: $(user)" \
         -H "X-Auth-Key: $(key)" \
         -H "Content-Type: application/json" \
         --data '{"files":['\
'"http://flo.click/resume/cv_en_florian_vichot.html",'\
'"http://flo.click/resume/cv_fr_florian_vichot.html",'\
'"http://flo.click/resume/css/all.css"'\
']}' > /dev/null \
         && echo "Cloudflare cache purged!"
