WORKDIR=build
ANTLR_VERSION=4.10
ANTLR_JAR=antlr-$(ANTLR_VERSION)-complete.jar

PROJECT=grammars-v4
GITHUB_URL=git@github.com:facetoe/$(PROJECT).git
UPSTREAM_GITHUB_URL=git@github.com:antlr/$(PROJECT).git
GRAMMAR_COMMIT=42775341e4138ce572e48aaec8671d12c98171e2

$(WORKDIR)/$(ANTLR_JAR):
	mkdir -p $(WORKDIR)
	curl https://www.antlr.org/download/$(ANTLR_JAR) -o $(WORKDIR)/$(ANTLR_JAR)

$(WORKDIR)/$(PROJECT):
	git clone $(GITHUB_URL) $(WORKDIR)/$(PROJECT)
	cd $(WORKDIR)/$(PROJECT); \
		git remote add upstream $(UPSTREAM_GITHUB_URL); \
		git fetch upstream; \
		git merge upstream/master; \
		git cherry-pick "$(GRAMMAR_COMMIT)"

generate-parser: $(WORKDIR)/$(ANTLR_JAR) $(WORKDIR)/$(PROJECT)
	(cd $(WORKDIR)/$(PROJECT)/promql && java -jar $(CURDIR)/$(WORKDIR)/$(ANTLR_JAR) -Dlanguage=Python3 PromQLLexer.g4 -visitor -o $(CURDIR)/promformat/parser)
	(cd $(WORKDIR)/$(PROJECT)/promql && java -jar $(CURDIR)/$(WORKDIR)/$(ANTLR_JAR) -Dlanguage=Python3 PromQLParser.g4 -visitor -o $(CURDIR)/promformat/parser)

clean:
	rm -rf $(WORKDIR)

test:
	PYTHONPATH=. pytest-3 tests/

reformat:
	black promformat tests
