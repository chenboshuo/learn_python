# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Set theory
# A set is a collection of unique objects.

# A basic use is removing duplication:
l = ['a','a','b']
l

set(l)

list(set(l))

# ## 集合运算

# `A|B` returns $ A \cup B$

A = set([1,2,3])
B = set([  2,3,4])
A|B

# `A&B` returns $A \cap B$

A & B

# $$ A \setminus B = A - B = \{ x | x \in A, x \notin B \} $$

A - B

# $$ A \Delta B = \{ x | x\in A \oplus x \in B \} $$
# `A ^ B` returns $A \Delta B$

A ^ B

# `x in A` returns $x \in A$

1 in A

# `A <= B` returns $ A \subseteq B$ 

A <= B

set([3,4]) <= B


