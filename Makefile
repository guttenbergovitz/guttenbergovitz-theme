SHELL := /bin/bash

.PHONY: help validate package.vscode zip.jetbrains-ui gen.iterm check.palette clean install

help:
	@echo "Guttenbergovitz Theme - Build, Validation & Install"
	@echo ""
	@echo "Validation:"
	@echo "  validate           - Validate color consistency across all themes"
	@echo "  check.palette      - Validate theme files use allowed palette"
	@echo ""
	@echo "Build:"
	@echo "  package.vscode     - Package VS Code theme (.vsix)"
	@echo "  zip.jetbrains-ui   - Zip JetBrains UI theme plugin"
	@echo "  gen.iterm          - Generate iTerm .itermcolors from palette"
	@echo ""
	@echo "Install:"
	@echo "  install            - Run interactive CLI installer for editors/terminals"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean              - Remove temporary build artifacts"

validate:
	@echo "Running consistency validation..."
	@python3 scripts/validate_consistency.py

package.vscode:
	cd vscode && npm install && npm run package

zip.jetbrains-ui:
	cp jetbrains/*.icls jetbrains/ui-theme/resources/
	cd jetbrains/ui-theme/resources && zip -r ../guttenbergovitz-ui-theme.jar .
	rm -f jetbrains/ui-theme/resources/*.icls
	@echo "Created: jetbrains/ui-theme/guttenbergovitz-ui-theme.jar"

gen.iterm:
	python3 scripts/generate_terminal_themes.py

check.palette:
	python3 scripts/check_palette.py

install:
	@python3 scripts/install_theme.py

clean:
	@find . -name "*.zip" -maxdepth 3 -print -delete
	@find . -name ".DS_Store" -print -delete
