# CLAUDE.md

This file provides guidance for AI assistants (Claude and others) working with this repository.

## Repository Overview

**a_first_repo** is a beginner-level Python project demonstrating basic GitHub workflow and data processing with pandas. It was created as a first GitHub repository to explore version control, branching, and pull requests.

## Codebase Structure

```
a_first_repo/
├── README.md        # Brief project description
├── CLAUDE.md        # This file — AI assistant guidance
└── testchild.py     # Python data processing script using pandas
```

### Files

- **`testchild.py`**: A simple pandas script that creates a small student-scores dataset, computes the mean score, and prints the results to stdout. No classes, no functions — top-level procedural code only.
- **`README.md`**: Minimal project description (title + one-line summary).

## Technology Stack

| Component | Details |
|-----------|---------|
| Language  | Python 3.6+ (uses f-strings) |
| Libraries | `pandas` |
| Version control | Git / GitHub |

No virtual-environment, `requirements.txt`, `setup.py`, or lockfile is present in the repository. To run the script, `pandas` must be installed manually:

```bash
pip install pandas
python testchild.py
```

## Development Workflow

The project follows a simple **GitHub Flow**:

1. Create a feature branch off `master`.
2. Make changes and commit to the feature branch.
3. Open a Pull Request targeting `master`.
4. Merge after review.

Branch naming observed in history: descriptive short names (e.g. `Child-Branch`).

### Running the script

```bash
python testchild.py
```

Expected output:
```
Scores dataset:
      Name  Score
0    Alice     85
1      Bob     92
2  Charlie     78
3    Diana     90

Average score: 86.25
```

## Conventions

- **Python style**: Plain procedural scripts; no classes, no functions wrapping top-level logic, no type annotations.
- **Variable names**: Clear, lowercase with underscores (`average`, `df`, `data`).
- **String formatting**: f-strings preferred over `%`-formatting or `.format()`.
- **No error handling**: Scripts assume a clean environment; no try/except blocks are used.
- **Commit messages**: Short, descriptive, imperative mood (e.g. `Create testchild.py`).

## Testing

There is currently **no test suite**. No `pytest`, `unittest`, or other testing framework is configured. If adding tests in future, `pytest` is the recommended approach for Python projects of this size.

## CI/CD

No CI/CD pipeline exists at this time (no `.github/workflows/`, no other pipeline configs).

## Notes for AI Assistants

- This is a learning/sandbox repository. Keep suggestions simple and beginner-friendly.
- Do not introduce complex abstractions, frameworks, or patterns unless explicitly requested.
- When adding new Python scripts, follow the same flat, procedural style seen in `testchild.py` unless the user asks for something different.
- If the user asks to add dependencies, remind them to also create a `requirements.txt` so others can reproduce the environment.
- There is no linter or formatter configured; avoid silently reformatting existing code.
