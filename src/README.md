# Shared Utilities

Reusable utilities and common modules used across multiple projects.

## Structure

```
src/
├── common/                    # Common utilities
│   ├── __init__.py
│   ├── networking.py         # Network utilities
│   ├── logging.py            # Logging utilities
│   └── helpers.py            # Helper functions
└── utils/
    ├── __init__.py
    └── ...
```

## Usage

From your assignment/project, import shared utilities:

```python
import sys
sys.path.insert(0, '../../src')

from common.networking import create_socket
from common.logging import setup_logger
```

---

Last Updated: January 18, 2026
