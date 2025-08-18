SHELL := /bin/bash

.PHONY: help package.vscode zip.jetbrains-ui gen.iterm check.palette clean

help:
	@echo "Targets:"
	@echo "  package.vscode     - Package VS Code theme (.vsix)"
	@echo "  zip.jetbrains-ui   - Zip JetBrains UI theme plugin"
	@echo "  gen.iterm          - Generate iTerm .itermcolors from palette"
	@echo "  check.palette      - Validate theme files use allowed palette"
	@echo "  clean              - Remove temporary build artifacts"

package.vscode:
	cd vscode && npm install && npm run package

zip.jetbrains-ui:
	cd jetbrains/ui-theme/resources && zip -r ../guttenbergovitz-ui-theme.zip .
	@echo "Created: jetbrains/ui-theme/guttenbergovitz-ui-theme.zip"

gen.iterm:
	python3 scripts/gen_itermcolors.py

check.palette:
	python3 scripts/check_palette.py

clean:
	@find . -name "*.zip" -maxdepth 3 -print -delete
	@find . -name ".DS_Store" -print -delete
