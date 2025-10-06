# Plan Refaktoringu Guttenbergovitz Theme

## Analiza Obecnego Stanu

### Baza Referencyjna: VSCode Theme
Zgodnie z wymogami projektu, temat VSCode (`vscode/themes/guttenbergovitz-color-theme.json`) jest bazą kolorystyczną dla wszystkich innych implementacji.

### Aktualny Stan Spójności

#### ✅ Implementacje w pełni spójne:
- **Neovim** (`lua/guttenbergovitz/init.lua`) - 100% zgodność
- **Vim** (`vim/colors/guttenbergovitz.vim`) - 100% zgodność
- **Helix** (`helix/guttenbergovitz.toml`) - 99% zgodność (brakuje tylko `border`)

#### ⚠️ Implementacje wymagające aktualizacji:
- **Kitty** - brakuje kolorów akcentowych i UI (9 niezgodności)
- **Warp** - brakuje kolorów akcentowych i UI (9 niezgodności)
- **Ghostty** - brakuje kolorów akcentowych i UI (9 niezgodności)
- **Zed** - brakuje niektórych kolorów podstawowych (9 niezgodności)

### Identyfikacja Problemów

#### 1. Brak Centralnego Źródła Prawdy
Pomimo istnienia `palette.json`, nie jest on konsekwentnie wykorzystywany przez wszystkie implementacje. Każda platforma definiuje kolory niezależnie, co prowadzi do:
- Duplikacji definicji kolorów
- Rozbieżności między implementacjami
- Trudności w synchronizacji zmian

#### 2. Niekompletne Implementacje Terminali
Terminale (Kitty, Warp, Ghostty) definiują tylko:
- Kolory podstawowe (background, foreground)
- Kolory ANSI (0-15)
- Brakuje im kolorów akcentowych używanych w syntaxie

#### 3. Niezgodność `palette.json` z VSCode
Plik `palette.json` zawiera pełną paletę, ale jego struktura nie jest w 100% zgodna z faktycznymi wartościami używanymi w VSCode theme.

## Proponowane Rozwiązanie

### Faza 1: Zunifikowanie Źródła Prawdy

#### A. Aktualizacja `palette.json`
Przekształcić `palette.json` w **jedyne źródło prawdy** dla wszystkich kolorów:

```json
{
  "meta": {
    "name": "Guttenbergovitz",
    "version": "2.0.0",
    "reference": "VSCode theme"
  },
  "dark": {
    "base": {
      "bg": "#232326",
      "bg_dark": "#1d1d20",
      "bg_light": "#2a2a2d",
      "fg": "#d4be98",
      "fg_dim": "#7c7c7c"
    },
    "accents": {
      "red": "#a96b69",
      "green": "#89a87d",
      "yellow": "#d6b986",
      "orange": "#d79969",
      "purple": "#b194a3",
      "cyan": "#89b4ac",
      "blue": "#7a9ec2"
    },
    "ui": {
      "border": "#3a3a3d",
      "selection": "#3a3a3d",
      "line_highlight": "#2a2a2d",
      "cursor": "#d4be98"
    },
    "semantic": {
      "keyword": "#a96b69",
      "function": "#d79969",
      "string": "#89a87d",
      "type": "#d6b986",
      "variable": "#d4be98",
      "comment": "#7c7c7c",
      "operator": "#a96b69",
      "constant": "#d6b986",
      "punctuation": "#d4be98"
    },
    "terminal": {
      "ansi": {
        "black": "#1d1d20",
        "red": "#a96b69",
        "green": "#89a87d",
        "yellow": "#d6b986",
        "blue": "#d79969",
        "magenta": "#a96b69",
        "cyan": "#89a87d",
        "white": "#d4be98"
      },
      "ansi_bright": {
        "black": "#7c7c7c",
        "red": "#a96b69",
        "green": "#89a87d",
        "yellow": "#d6b986",
        "blue": "#d79969",
        "magenta": "#a96b69",
        "cyan": "#89a87d",
        "white": "#d4be98"
      }
    },
    "status": {
      "error": "#cc6666",
      "warning": "#de935f",
      "info": "#81a2be",
      "hint": "#9cc5c0",
      "success": "#b5bd68"
    }
  },
  "light": {
    // ... odpowiedniki dla jasnego motywu
  }
}
```

#### B. Skrypty Generujące
Stworzyć skrypty w `scripts/` do automatycznego generowania tematów:

1. **`scripts/generate_all.py`** - master script generujący wszystkie tematy
2. **`scripts/generators/`** - dedykowane generatory dla każdej platformy:
   - `vscode_generator.py`
   - `neovim_generator.py`
   - `helix_generator.py`
   - `kitty_generator.py`
   - `warp_generator.py`
   - `ghostty_generator.py`
   - `zed_generator.py`
   - `vim_generator.py`
   - `jetbrains_generator.py`
   - `iterm_generator.py`

### Faza 2: Implementacja Per-Platform

#### Priorytety (według liczby niezgodności):

1. **Zed** (9 issues) - edytor z największymi brakami
2. **Kitty/Warp/Ghostty** (po 9 issues) - terminale wymagają rozszerzenia
3. **Helix** (1 issue) - tylko drobne uzupełnienie

### Faza 3: Automatyzacja i CI/CD

#### A. Pre-commit Hooks
```bash
# Walidacja spójności przed committem
scripts/validate_consistency.py
```

#### B. GitHub Actions
```yaml
# .github/workflows/validate-themes.yml
- Sprawdzanie spójności kolorów
- Automatyczne generowanie tematów z palette.json
- Testy wizualne (screenshots)
```

### Faza 4: Dokumentacja

#### A. Dla Developerów
```markdown
# CONTRIBUTING.md
## Zmiana kolorów
1. Edytuj tylko `palette.json`
2. Uruchom `make generate`
3. Sprawdź `make validate`
4. Commit wszystkich zmian
```

#### B. Dla Użytkowników
```markdown
# README.md
## Gwarancja Spójności
Wszystkie implementacje są automatycznie generowane z jednego źródła,
gwarantując identyczne kolory na wszystkich platformach.
```

## Plan Implementacji

### Krok 1: Przygotowanie Infrastruktury
- [ ] Aktualizacja `palette.json` do pełnej wersji referencyjnej
- [ ] Stworzenie struktury `scripts/generators/`
- [ ] Implementacja base generator class

### Krok 2: Migracja Wysokopriorytetowych Platform
- [ ] Zed - pełna regeneracja z palette.json
- [ ] Kitty - dodanie kolorów semantycznych jako komentarze
- [ ] Warp - rozszerzenie o pełną paletę
- [ ] Ghostty - harmonizacja z VSCode

### Krok 3: Dopracowanie Pozostałych
- [ ] Helix - dodanie `border` color
- [ ] Weryfikacja Neovim/Vim - upewnienie się że są zsynchronizowane

### Krok 4: Automatyzacja
- [ ] Implementacja `make generate`
- [ ] Implementacja `make validate`
- [ ] Setup GitHub Actions
- [ ] Pre-commit hooks

### Krok 5: Dokumentacja i Testy
- [ ] Aktualizacja CLAUDE.md
- [ ] Rozszerzenie README.md
- [ ] Stworzenie CONTRIBUTING.md
- [ ] Testy wizualne

## Korzyści z Refaktoringu

### Dla Maintainerów
1. **Jednolite źródło zmian** - edycja tylko `palette.json`
2. **Automatyzacja** - brak ręcznej synchronizacji
3. **Walidacja** - automatyczne wykrywanie niezgodności
4. **Wersjonowanie** - łatwe śledzenie zmian kolorów

### Dla Użytkowników
1. **Spójność** - identyczne kolory na wszystkich platformach
2. **Przewidywalność** - ta sama estetyka wszędzie
3. **Jakość** - mniej błędów, lepsza konsystencja

### Dla Projektu
1. **Profesjonalizm** - uporządkowana struktura
2. **Skalowalność** - łatwe dodawanie nowych platform
3. **Maintainability** - prostsze w utrzymaniu
4. **Trust** - użytkownicy mogą zaufać spójności

## Backward Compatibility

### Zachowanie Kompatybilności
- Wszystkie istniejące instalacje będą działać bez zmian
- Struktura plików pozostaje niezmieniona
- Tylko wartości kolorów są harmonizowane

### Breaking Changes
- **Żadnych** - to jest harmonizacja, nie przepisanie
- Kolory mogą się nieznacznie zmienić w niektórych implementacjach
- Dokumentować zmiany w CHANGELOG.md

## Timeline

- **Tydzień 1**: Przygotowanie infrastruktury (Kroki 1-2)
- **Tydzień 2**: Migracja platform (Krok 3)
- **Tydzień 3**: Automatyzacja (Krok 4)
- **Tydzień 4**: Dokumentacja i testy (Krok 5)
- **Tydzień 5**: Review, fixes, release

## Metryki Sukcesu

1. ✅ Wszystkie implementacje mają 100% zgodność z VSCode
2. ✅ `make validate` przechodzi bez błędów
3. ✅ Każda zmiana koloru wymaga edycji tylko 1 pliku
4. ✅ CI/CD automatycznie wykrywa niezgodności
5. ✅ Dokumentacja jasno opisuje proces zmian

## Ryzyka i Mitygacja

### Ryzyko 1: Zmiany w istniejących kolorach
**Mitygacja**: Dokładna dokumentacja wszystkich zmian, wersjonowanie semantyczne

### Ryzyko 2: Złamanie workflow użytkowników
**Mitygacja**: Zachowanie struktury plików, tylko wartości się zmieniają

### Ryzyko 3: Complexity w scripts
**Mitygacja**: Dobra dokumentacja, testy, code review

## Następne Kroki

1. **Review tego planu** z zespołem/maintainerem
2. **Decyzja**: full refactor vs incrementalne zmiany
3. **Implementacja** według wybranego podejścia
4. **Testing** na różnych platformach
5. **Release** z pełną dokumentacją zmian
