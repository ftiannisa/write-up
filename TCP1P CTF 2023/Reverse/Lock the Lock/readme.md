# Lock the Lock

### Category: Reverse Engineering

###### author: Kisanak

Unlock the Unlocked

- [chall.pyc](/TCP1P%20CTF%202023/Reverse/Lock%20the%20Lock/chall.pyc)

## Solution:

#### 🔍 Decompile + outline

We're given a .pyc file so we have to decompile it. I use uncompyle6 to do the job

```sh
$ uncompyle6 chall.pyc > chall.py
```

Apparently, it's a GUI app where we have to input something 999 times and each time, `submit()` function will check our input:

- there's `check()` function to validate the input
- if the input is correct, it will add our input to the `validatedkey` list and increase our attempts
- if input is incorrect, it will clear the `validatedkey` list and restart our attempts
- we need `validatedkey` to decrypt the flag

So the goal is to "generate" the correct input 999 times (aka `validatedkey` list), but how?

#### 🔎 Recon

First, we have to analyze the source code deeper.

Here, we can see a list called `init` is initialized and then was shuffled three times. But notice that a seed value[^1] is set for the `random` function, which means we can recreate this and still get the same output.

```py
random.seed(199)
...
num = [i for i in range(1, 1001)]
init = num.copy()
random.shuffle(init)
random.shuffle(init)
random.shuffle(init)
```

Then, `initialization()` function is called to initialized 2 variables, `tr` and `troot`. Basically this function generate a binary tree data structure.

Another list called `target` is initialized and `troot.data` will be removed from `target`, then this final list will be used for the `check()` function I mentioned before.

```py
...
tr, troot = initialization()
target = init.copy()
target.remove(troot.data)
random.shuffle(target)
```

Now, back to the `check()`. As we see, it has 4 parameters:

- `state` is some kind of temporary variable to keep the current state/path (the tree's left node or right node)
- `root` is the binary tree instance
- `n` is our input
- `x` is the data used to validate our input aka an element from the `target` list

```py
# a simplified check()
def check(state, root, n, x):
    state = root
    for i in n:
        if i == '0':
            state = state.l
        else:
            if i == '1':
                state = state.r
        if state == None:
            print('Error invalid node! Resetting level...')
            return False
        if state.data == x:
            return True
    print('Wrong answer! Resetting level...')
    return False
```

So the function checks every single digit in our input. If the digit is '0', then it will turn to the left node. If the digit is '1', it will take the right node. If it finds the right data (aka the `x`) in the binary tree, it will return True, otherwise it will return False.

#### ✨ Solving.

Now we know how the `check()` function works. So in order to get the correct input, we need to find the path to the correct data and "convert" the path into a binary string.

```py
''' snippet of the search path algorithm '''
def searchNode(node, key, path=None):
    # get the path and convert it to binary string
    if path is None:
        path = ''

    if not node:
        return False

    if key < node.data:
        path += '0'     # '0' for left node
        return searchNode(node.l, key, path)
    if key > node.data:
        path += '1'     # '1' for right node
        return searchNode(node.r, key, path)
    else:
        return path
```

you can get the full script of my solver [here](/TCP1P%20CTF%202023/Reverse/Lock%20the%20Lock/lock.py)

## FLAG

<details>
  <summary></summary>
  
TCP1P{where_the_skies_are_blue_to_see_you_once_again}
</details>

<br>

🏷️tags: pyc, uncompyle6, binary tree

### References

- [Binary Tree Path Finder Algorithm](https://stackoverflow.com/questions/70839176/python-recursive-path-finder-for-binary-tree)

[^1]: [Python Random seed() Method](https://www.w3schools.com/python/ref_random_seed.asp)
