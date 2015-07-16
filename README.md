# Python Algorithms Test
My solutions to these problems can be found in the files: **_print_depth.py_** and **_least_common_ancestor.py_**.

**NOTE**: Discussions about my answers can be found in the comment block at the top of each Python file.
### 1) Write following function body. A nested dictionary is passed as parameter. You need to print all keys with their depth.
Sample Input:
```python
a = { “key1”: 1,
      “key2”: { “key3”: 1,
                “key4”: { “key5”: 4
                        }
              }
    }
```
Sample Output:

```
key1 1
key2 1
key3 2
key4 2
key5 3
```

```python
def print_depth(data):
    # Write function body
```

You may write additional functions.

###2) Write following function body. 2 Nodes are passed as parameters. You need to find their Least Common Ancestor and print its value. Node structure are as follows:

```python
class Node{
    value;
    parent;
}
```
![Image](https://github.com/dhaggerty88/revel_python_test/blob/master/img/Capture.PNG)

Ancestor Definition:

1) Any node falls under parent chain till root node.
2) A node is ancestor of itself.

For example: if we consider Node 7 it’s ancestors will be 1, 3, and 7. All nodes values are unique for this tree.
You function needs to find least common ancestor (closest common ancestor).

```python
def lca(node1, node2):
    # Write function body
```

You may write additional functions.
