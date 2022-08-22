WORKDIR=build
ANTLR_VERSION=4.10
ANTLR_JAR=antlr-$(ANTLR_VERSION)-complete.jar


# When https://github.com/antlr/grammars-v4/pull/2484 is merged can use grammar from official project
#GITHUB_URL=git@github.com:antlr/$(PROJECT).git
PROJECT=grammars-v4
GITHUB_URL=git@github.com:facetoe/$(PROJECT).git
GRAMMAR_COMMIT=42775341e4138ce572e48aaec8671d12c98171e2

$(WORKDIR)/$(ANTLR_JAR):
	mkdir -p $(WORKDIR)
	curl https://www.antlr.org/download/$(ANTLR_JAR) -o $(WORKDIR)/$(ANTLR_JAR)

$(WORKDIR)/$(PROJECT):
	git clone $(GITHUB_URL) $(WORKDIR)/$(PROJECT)

generate-parser: $(WORKDIR)/$(ANTLR_JAR) $(WORKDIR)/$(PROJECT)
	git -C $(WORKDIR)/$(PROJECT) reset --hard "$(GRAMMAR_COMMIT)"
	(cd $(WORKDIR)/$(PROJECT)/promql && java -jar $(CURDIR)/$(WORKDIR)/$(ANTLR_JAR) -Dlanguage=Python3 PromQLLexer.g4 -visitor -o $(CURDIR)/promformat/parser)
	(cd $(WORKDIR)/$(PROJECT)/promql && java -jar $(CURDIR)/$(WORKDIR)/$(ANTLR_JAR) -Dlanguage=Python3 PromQLParser.g4 -visitor -o $(CURDIR)/promformat/parser)

clean:
	rm -rf $(WORKDIR)

test:
	PYTHONPATH=. pytest-3 tests/

reformat:
	black promformat tests
