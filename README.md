# Python Learning Notes

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📚 Introduction

A comprehensive Python learning guide covering core concepts from beginner to intermediate level, with detailed comments and runnable code examples.

## 📋 Table of Contents

| Chapter | Topic | Content |
|---------|-------|---------|
| 1 | Loops | for, while, range(), enumerate() |
| 2 | Control Statements | pass, continue, break comparison |
| 3 | Data Structures | list, tuple, dict, set |
| 4 | Set Operations | intersection, union, difference, symmetric difference |
| 5 | Functions | *args, **kwargs, lambda, decorators |
| 6 | Memory Management | iterators, shallow copy, deep copy |
| 7 | File Operations | text, CSV, JSON |
| 8 | Exception Handling | try/except/finally |
| 9 | Module Imports | standard library usage |
| 10 | Recursion | factorial, Fibonacci |

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/hahAI111/python-dataengineer-tutorials.git

# Enter the directory
cd python-dataengineer-tutorials

# Run the learning notes
python python_learning_notes.py
```

## 📝 Key Concepts Preview

### Control Statements Comparison

| Keyword | Function | Loop Continues? |
|---------|----------|-----------------|
| `pass` | Placeholder, does nothing | ✅ Yes |
| `continue` | Skip current iteration | ✅ Next iteration |
| `break` | Exit loop | ❌ Exit |

### Data Structures Comparison

| Type | Mutable | Ordered | Duplicates | Syntax |
|------|---------|---------|------------|--------|
| list | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| tuple | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| set | ✅ | ❌ | ❌ | `{1, 2, 3}` |
| dict | ✅ | ✅ | Unique keys | `{"a": 1}` |

### Shallow Copy vs Deep Copy

| Operation | Syntax | New Object? | Nested Independent? |
|-----------|--------|-------------|---------------------|
| Assignment | `b = a` | ❌ | ❌ |
| Shallow Copy | `b = a.copy()` | ✅ | ❌ |
| Deep Copy | `b = copy.deepcopy(a)` | ✅ | ✅ |

## 📂 File Structure

```
python-dataengineer-tutorials/
├── README.md                    # Project documentation
├── python_learning_notes.py     # Main learning notes file
└── LICENSE                      # License
```

## 🎯 Target Audience

- Python beginners
- Developers who need to review Python fundamentals
- Students preparing for Python interviews

## 📖 Usage Tips

1. **Learn step by step**: Run code in order, understand each concept
2. **Hands-on practice**: Modify code parameters, observe output changes
3. **Take notes**: Add your own understanding to the comments
4. **Practice**: Try writing similar code yourself

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📜 License

MIT License - Free to use and modify
