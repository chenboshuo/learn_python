---
jupyter:
  jupytext:
    formats: ipynb,py:light,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

## Deques and Other Queues
The `.append` and `.pop` methods make a list usable as a stack or queue (if you use `.append` and `pop(0)`, you get LIFO behavior).
But inserting and removing from the left of a list(the 0-index end) is costly because the entire list must be shifted.

The class `collection.deque` is a thread-safe double-ended queue designed for fast inserting and removing from both ends.
It is also the way to go if you need to keep a list of "last seen items" or something like that that
