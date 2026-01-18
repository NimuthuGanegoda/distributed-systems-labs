# Distributed Systems Labs & Projects

A comprehensive repository for distributed systems assignments, labs, and personal projects.

## 📁 Directory Structure

```
distributed-systems-labs/
├── assignments/                    # Course/class assignments
│   ├── assignment-1-rpc-server/   # RPC Server with Database
│   ├── assignment-2-xxx/          # Add more assignments here
│   └── README.md
├── projects/                       # Personal projects & experiments
│   ├── project-1-xxx/
│   └── README.md
├── labs/                           # Lab exercises & practice
│   ├── lab-1-xxx/
│   └── README.md
├── src/                            # Shared source code & utilities
│   └── common/                     # Common utilities, helpers
├── tests/                          # Shared tests
│   └── shared/                     # Shared test utilities
├── docs/                           # Shared documentation
│   ├── architecture/
│   ├── concepts/
│   └── README.md
├── .gitignore                      # Git ignore rules
├── README.md
├── requirements.txt                # Project dependencies
├── setup.py                        # Package setup (optional)
└── CONTRIBUTING.md                 # Contribution guidelines
```

## 🚀 Quick Start

### Run Assignment 1 (RPC Server)
```bash
cd assignments/assignment-1-rpc-server
python main.py
```

### Add a New Assignment
```bash
mkdir assignments/assignment-2-your-name
cd assignments/assignment-2-your-name
# Add your project files
```

### Add a Personal Project
```bash
mkdir projects/project-1-your-name
cd projects/project-1-your-name
# Add your project files
```

### Add a Lab Exercise
```bash
mkdir labs/lab-1-your-name
cd labs/lab-1-your-name
# Add your lab files
```

## 📋 Categories

### Assignments (`assignments/`)
- Course or class assignments
- Graded work
- Structured problems with requirements
- Format: `assignment-N-topic-name/`

### Projects (`projects/`)
- Personal projects
- Experimental implementations
- Open-ended explorations
- Format: `project-N-topic-name/`

### Labs (`labs/`)
- Lab exercises from courses
- Practice problems
- Guided tutorials
- Format: `lab-N-topic-name/`

### Shared Code (`src/`)
- Utilities and helpers used across multiple projects
- Common patterns and implementations
- Reusable components

### Documentation (`docs/`)
- Architecture documentation
- Distributed systems concepts
- Algorithm explanations
- Design patterns

## 🔧 Setup

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Python Path
If using shared utilities from `src/`:
```python
import sys
sys.path.insert(0, '/path/to/distributed-systems-labs/src')
```

## 📝 Project Template

Each assignment/project should have:
- `README.md` - Overview and instructions
- `requirements.txt` - Project-specific dependencies
- Source files (.py)
- Test files (if applicable)

Example:
```
assignment-N-topic/
├── README.md
├── requirements.txt
├── main.py
├── module1.py
├── module2.py
└── tests/
    └── test_module1.py
```

## 🎯 Topics Covered

- RPC (Remote Procedure Call)
- Client-Server Architecture
- Database Systems
- Network Programming
- Concurrency & Threading
- Consensus Algorithms
- Distributed Transactions
- Message Passing
- And more...

## 📚 Resources

- Each assignment/project has its own README with specific details
- See `docs/` folder for architectural discussions
- Check individual project READMEs for implementation details

## 🤝 Contributing

Follow the structure above when adding new work. Keep projects organized and self-contained.

---

**Last Updated**: January 18, 2026
