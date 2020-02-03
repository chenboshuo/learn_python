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

# Set theory
A set is a collection of unique objects.

```python
# A basic use is removing duplication:
l = ['a','a','b']
l
```

```python
set(l)
```

```python
list(set(l))
```

## 集合运算


`A|B` returns $ A \cup B$

```python
A = set([1,2,3])
B = set([  2,3,4])
A|B
```

`A&B` returns $A \cap B$

```python
A & B
```

$$ A \setminus B = A - B = \{ x | x \in A, x \notin B \} $$

```python
A - B
```

$$ A \Delta B = \{ x | x\in A \oplus x \in B \} $$
`A ^ B` returns $A \Delta B$

```python
A ^ B
```

`x in A` returns $x \in A$

```python
1 in A
```

`A <= B` returns $ A \subseteq B$ 

```python
A <= B
```

```python
set([3,4]) <= B
```

```python

```
