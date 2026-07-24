# Requirements

## Shared Dependencies

Add project-specific dependencies to the `requirements.txt` file in each assignment/project/lab folder.

The shared dependencies for distributed systems projects live in the root
`requirements.txt` (networking uses `asyncio`/`socket` from the standard
library, so nothing to install there):

```
# Testing
pytest>=8.4.2
pytest-asyncio>=1.2.0

# Code Quality
pylint>=3.3.9
black>=25.11.0
flake8>=7.3.0

# Utilities
requests>=2.32.5
numpy>=2.0.2
```

Versions are pinned to the latest release of each package that still
supports Python 3.9, since that's the oldest interpreter in the CI test
matrix (`.github/workflows/python-tests.yml`, `python-package.yml`).

## Installation

```bash
# Install shared dependencies (if any)
pip install -r requirements.txt

# Install project-specific dependencies
cd assignments/assignment-1-rpc-server
pip install -r requirements.txt
```

---

Last Updated: 2026-07-24
