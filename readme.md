# Part-1
Let's make Git in Python! You should already know Git basics to follow along. If you're new to Git, try using it first, then come back here.

## Why learn Git internals?
For everyday tools like Firefox or Vim, we often don't need to know how they work internally. Similarly, when using Git for basic tasks like tracking code history with commands like **git add**, **git commit**, and **git push**, understanding internals isn't crucial. However, as you collaborate with others on multiple branches, advanced features like *rebase* or *force push* can get confusing without understanding Git's internals. To effectively navigate these situations, it's more valuable to grasp Git's underlying workings than to memorize advanced commands. This understanding helps solve complex collaborative coding issues.

## Introducing: μgit
**μgit**, or **ugit**, is a simplified version of Git, focused on simplicity and educational value. While not identical to Git, it shares its key concepts like *commits*, *branches*, the *index*, *merges*, and *remotes*. ugit omits certain features like object compression, file mode, and commit time to reduce complexity. The journey presents incremental code changes, starting with a basic Python application that prints "hello world". The setup includes a setup.py file for the ugit executable, which calls the main() function in cli.py. To follow along and experiment, it's recommended to download or type the source code. Installing ugit in development mode allows immediate editing and running of the source.


Step 1: creating new env
```
python3 -m venv ugit
.\ugit-env\Scripts\activate
```
Step 2: install ugit
```
python3 setup.py develop
```
Step 3: executing ugit
```
ugit
```
