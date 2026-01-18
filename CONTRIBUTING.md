# Contributing Guidelines

## Adding New Work

### Naming Conventions

- **Assignments**: `assignments/assignment-N-topic-name/`
- **Projects**: `projects/project-N-topic-name/`
- **Labs**: `labs/lab-N-topic-name/`

### Required Files

Each assignment/project/lab should include:

1. **README.md** - Project description, instructions, and setup
2. **requirements.txt** - Python dependencies (if any)
3. **Source code** - Well-organized `.py` files
4. **Tests** - `tests/` folder with test files (optional but recommended)

### File Organization

```
your-project/
├── README.md
├── requirements.txt
├── main.py
├── module1.py
├── module2.py
└── tests/
    ├── __init__.py
    └── test_module1.py
```

### Documentation

- Add clear docstrings to your code
- Include comments for complex logic
- Provide examples in README.md
- Document any dependencies

### Code Style

- Follow PEP 8 conventions
- Use meaningful variable and function names
- Keep functions small and focused
- Add type hints where appropriate

### Git Workflow

1. Keep each project self-contained
2. Don't modify other projects' files
3. Update relevant README.md files when adding new work
4. Commit messages should be clear and descriptive

### Sharing Code

For code used across multiple projects:

1. Move it to `src/common/` or `src/utils/`
2. Add `__init__.py` files to make modules importable
3. Update the `src/README.md` with usage instructions
4. Document the shared module

---

**Questions?** Check the main [README.md](../README.md)
