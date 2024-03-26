# Part 2

### Write Tree and Read Tree

To save a collection of separate files into a single object that represents a directory. Our idea is that we will create one additional object that collects all the data necessary to store a complete directory. For example, if we have a directory with two files:

```
$ ls
cats.txt    dogs.txt
```

And we want to save the directory, we will first put the individual files into the object database:

```
$ ugit hash-object cats.txt
91a7b14a584645c7b995100223e65f8a5a33b707
$ ugit hash-object dogs.txt
fa958e0dd2203e9ad56853a3f51e5945dad317a4
```

And then create a "tree" object that has the content of:

```
91a7b14a584645c7b995100223e65f8a5a33b707 cats.txt
fa958e0dd2203e9ad56853a3f51e5945dad317a4 dogs.txt
```

And we have put this tree object into the object database as well. Then the OID of the tree object will actually represent the entire directory! How? Because we can first retrieve the tree object by its OID, then see all the files it contains (their names and OIDs) and then read all the OIDs of the files to get their actual content. In case of directory the object will look something like this:

```
blob 91a7b14a584645c7b995100223e65f8a5a33b707 cats.txt
blob fa958e0dd2203e9ad56853a3f51e5945dad317a4 dogs.txt
tree 53891a3c27b17e0f8fd96c058f968d19e340428d other
```

So, we have added a type to each entry so that we know if it's a file or a directory.

**write-tree:** Command to write Tree
**read-tree:** Command to read Tree

### Commit

This is another object type, _commit_, which will be stored in the object database. Commit type will have metadata about the commit. Example,

```
tree 5e550586c91fce59e0006799e0d46b3948f05693
parent bd0de093f1a0f90f54913d694a11cccf450bd990
author Arun Kothari
time 2019-09-14T09:31:09+00:00

This is the commit message!
```

**tag** will let you tag name (NO OIDs anymore) with commit, so we can refer it using that easy to remember string.

### Checkout

The **ugit checkout** command, when given a commit OID, populates the working directory with the content of that commit and moves HEAD to point to it.

```
$ ugit commit
d8d43b0e3a21df0c845e185d08be8e4028787069
$ ugit tag my-cool-commit d8d43b0e3a21df0c845e185d08be8e4028787069
```

For checking out later

```
$ ugit checkout my-cool-commit
        or
$ ugit checkout d8d43b0e3a21df0c845e185d08be8e4028787069
```
