# Assignments

This directory contains course and class assignments for distributed systems.

## Structure

Each assignment follows this naming convention:
```
assignment-N-topic-name/
```

Where:
- `N` = Assignment number (1, 2, 3, etc.)
- `topic-name` = Brief description of the topic

## Current Assignments

### Assignment 1: RPC Server
- **Folder**: `assignment-1-rpc-server/`
- **Description**: Implementation of a Remote Procedure Call (RPC) server with database backend
- **See**: `assignment-1-rpc-server/README.md`

## Adding New Assignments

1. Create a new folder: `assignment-N-topic-name/`
2. Create a `README.md` with project description
3. Add all project files (`.py`, tests, etc.)
4. Update this file with assignment info

Example:
```bash
mkdir assignment-2-consensus-algorithm
cd assignment-2-consensus-algorithm
# Add your files and README.md
```

## Templates

A typical assignment structure:
```
assignment-N-topic-name/
├── README.md
├── requirements.txt
├── main.py
├── module1.py
├── module2.py
└── tests/
    └── test_module1.py
```

---

Last Updated: January 18, 2026
