# Python 学习笔记 (Python Learning Notes)

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📚 简介

这是一份完整的 Python 基础学习笔记，包含了从入门到进阶的核心概念，配有详细的中文注释和可运行的代码示例。

## 📋 目录

| 章节 | 主题 | 内容 |
|------|------|------|
| 1 | 循环结构 | for, while, range(), enumerate() |
| 2 | 控制语句 | pass, continue, break 对比 |
| 3 | 数据结构 | list, tuple, dict, set |
| 4 | 集合操作 | 交集、并集、差集、对称差集 |
| 5 | 函数 | *args, **kwargs, lambda, 装饰器 |
| 6 | 内存管理 | 迭代器、浅拷贝、深拷贝 |
| 7 | 文件操作 | 文本、CSV、JSON |
| 8 | 异常处理 | try/except/finally |
| 9 | 模块导入 | 标准库使用 |
| 10 | 递归 | 阶乘、斐波那契 |

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/your-username/python-learning-notes.git

# 进入目录
cd python-learning-notes

# 运行学习笔记
python python_learning_notes.py
```

## 📝 核心知识点预览

### 控制语句对比

| 关键字 | 作用 | 循环继续? |
|--------|------|-----------|
| `pass` | 占位符，什么都不做 | ✅ 继续 |
| `continue` | 跳过本次迭代 | ✅ 下一次 |
| `break` | 退出循环 | ❌ 退出 |

### 数据结构对比

| 类型 | 可变 | 有序 | 可重复 | 语法 |
|------|------|------|--------|------|
| list | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| tuple | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| set | ✅ | ❌ | ❌ | `{1, 2, 3}` |
| dict | ✅ | ✅ | key不重复 | `{"a": 1}` |

### 浅拷贝 vs 深拷贝

| 操作 | 语法 | 新对象? | 嵌套独立? |
|------|------|---------|-----------|
| 赋值 | `b = a` | ❌ | ❌ |
| 浅拷贝 | `b = a.copy()` | ✅ | ❌ |
| 深拷贝 | `b = copy.deepcopy(a)` | ✅ | ✅ |

## 📂 文件结构

```
python-learning-notes/
├── README.md                    # 项目说明
├── python_learning_notes.py     # 主学习笔记文件
└── LICENSE                      # 许可证
```

## 🎯 适合人群

- Python 初学者
- 需要复习 Python 基础的开发者
- 准备 Python 面试的同学

## 📖 使用建议

1. **逐章学习**: 按顺序运行代码，理解每个概念
2. **动手实践**: 修改代码参数，观察输出变化
3. **做笔记**: 将自己的理解添加到注释中
4. **练习**: 尝试编写类似的代码

## 🤝 贡献

欢迎 Issue 和 Pull Request！

## 📜 License

MIT License - 自由使用和修改
