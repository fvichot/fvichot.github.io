ifndef VERBOSE
.SILENT:
endif

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    CHROME_APP = chromium
endif
ifeq ($(UNAME_S),Darwin)
    CHROME_APP = /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome
endif

include ~/.cloudflare_rc

TO_PDF = $(CHROME_APP) --headless --disable-gpu --content-shell-host-window-size=1200x1024 \
         --print-to-pdf=

FILES = cv_en_florian_vichot.html cv_fr_florian_vichot.html
FILES_PDFS = $(FILES:%.html=pdf/%.pdf)
TEMPLATE = templates/cv_html.tmpl

all: $(FILES_PDFS) $(FILES)

%.html: confs/%.toml $(TEMPLATE) css/all.css css/bootstrap.css css/font-awesome.css
	scripts/render_toml.py -t $(TEMPLATE) $< $@
	echo Generated $@

pdf/%.pdf: %.html
	mkdir -p pdf
	$(TO_PDF)$@ file://$(PWD)/$< 2>/dev/null
	echo Generated $@

purge:
	curl -s -X DELETE "https://api.cloudflare.com/client/v4/zones/$(zone)/purge_cache" \
         -H "X-Auth-Email: $(user)" \
         -H "X-Auth-Key: $(key)" \
         -H "Content-Type: application/json" \
         --data '{"purge_everything":true}' >/dev/null \
         && echo "Cloudflare cache purged!"
