# Requirements

## Shared Dependencies

Add project-specific dependencies to the `requirements.txt` file in each assignment/project/lab folder.

The shared dependencies for distributed systems projects live in the root
`requirements.txt` (networking uses `asyncio`/`socket` from the standard
library, so nothing to install there):

```
# Testing
pytest>=9.1.1
pytest-asyncio>=1.4.0

# Code Quality
pylint>=4.0.6
black>=26.5.1
flake8>=7.3.0

# Utilities
requests>=2.34.2
numpy>=2.5.1  # For numerical computations if needed
```

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
