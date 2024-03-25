# Part-1

Let's make Git in Python! You should already know Git basics to follow along. If you're new to Git, try using it first, then come back here.

## Why learn Git internals?

For everyday tools like Firefox or Vim, we often don't need to know how they work internally. Similarly, when using Git for basic tasks like tracking code history with commands like **git add**, **git commit**, and **git push**, understanding internals isn't crucial. However, as you collaborate with others on multiple branches, advanced features like _rebase_ or _force push_ can get confusing without understanding Git's internals. To effectively navigate these situations, it's more valuable to grasp Git's underlying workings than to memorize advanced commands. This understanding helps solve complex collaborative coding issues.

## Introducing: μgit

**μgit**, or **ugit**, is a simplified version of Git, focused on simplicity and educational value. While not identical to Git, it shares its key concepts like _commits_, _branches_, the _index_, _merges_, and _remotes_. ugit omits certain features like object compression, file mode, and commit time to reduce complexity. The journey presents incremental code changes, starting with a basic Python application that prints "hello world". The setup includes a setup.py file for the ugit executable, which calls the main() function in cli.py. To follow along and experiment, it's recommended to download or type the source code. Installing ugit in development mode allows immediate editing and running of the source.

Step 1: creating new env

```
$ python3 -m venv ugit-env
$ .\ugit-env\Scripts\activate
```

Step 2: install ugit

```
$ python3 setup.py develop
```

Step 3: executing ugit

```
$ ugit
```

## Hash-objects

In Git's lingo, this feature is called _the object database_. It allows us to store and retrieve arbitrary blobs(Binary Large Objects), which are called _objects_. As far as the Object Database is concerned, the content of the object doesn't have any meaning (just like a filesystem doesn't care about the internal structure of a file).

```
$ ugit hash-object
```

The **hash-object** command, which stores a file in the _.ugit_ directory for later retrieval. This command mirrors Git's _object database_ to save and retrieve arbitrary blobs(Binary Large Objects).

Objects are referenced using their hash. If you're unfamiliar with hashes and hash functions, I recommend pausing to read about them. In essence, a hash function generates a fixed-length _fingerprint_ from arbitrary-length data. Hash functions like SHA-1 ensure that different data typically produce different fingerprints, a principle Git relies on.

```
$ echo -n this is cool | sha1sum
60f51187e76a9de0ff3df31f051bde04da2da891

$ echo -n this is cooler | sha1sum
f3c953b792f9ab39d1be0bdab7ab5f8350593004
```

When hashing phrases like "this is cool" and "this is cooler," even small differences yield completely different hashes.

In the **hash-object** command:

1. Obtain the file path to store.
2. Read the file's content.
3. Hash the content using SHA-1.
4. Save the file under _.ugit/objects/{SHA-1 hash}_.

This storage method is called _content-addressable storage_. The address used to find a blob is based on its content, unlike _name-addressable storage_ (e.g., typical filesystems). Content-addressable storage simplifies data synchronization between repositories, ensuring objects with the same OID are identical. Additionally, different objects have different OIDs, preventing naming clashes.

```
$ git cat-object
```

The **cat-file** command is the counterpart to **hash-object.** It retrieves and prints an object based on its OID, reading the file located at _.ugit/objects/{OID}_.

```
$ cd /tmp/new
$ ugit init
Initialized empty ugit repository in /tmp/new/.ugit
$ echo some file > bla
$ ugit hash-object bla
0e08b5e8c10abc3e455b75286ba4a1fbd56e18a5
$ ugit cat-file 0e08b5e8c10abc3e455b75286ba4a1fbd56e18a5
some file
```

Notably, the original filename (e.g., "bla") isn't preserved during this process. The object database focuses solely on storing bytes for future retrieval, irrespective of the filename.

Each object also has a type tag prepended to it, followed by a null byte. This helps ensure objects are used correctly in different contexts. By default, the type is _blob_, indicating a collection of bytes without specific meaning. When reading the file later, we'll extract and verify the type.

## Write-Tree:

The **write-tree** command, which saves the current working directory to the object database. Similar to **hash-object,** **write-tree** assigns an OID after execution, allowing retrieval of the directory later.
In Git terminology, a _tree_ represents a directory.

```
ugit write-tree
```

We also have a separate is_ignored() function. This way if we have any file (for example, .ugit) we want to ignore later we have one place to change.

However, till part-1 write-tree results in separate OIDs for each file, which isn't very practical. Additionally, filenames are not stored in the object database; they are merely printed and then discarded. We fill fix it in the next part

## Files

### ugit/cli.py

- Contains the arg parser to implement sub-commands
- To initialize a new empty repository

```
ugit init
```

- Information about the new repository will be stored in **.ugit** to avoid clashes with **.git**

### ugit/data.py

- Manages data flow into/out-from **.ugit**

### ugit/base.py

- This module will contain the fundamental higher-level logic of ugit. For example, It will utilize the object database implemented in data.py to create higher-level structures for storing directories and other data.
