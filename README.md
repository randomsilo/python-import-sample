# python-import-sample

Imports are confusing and the examples are weak; so I am putting together a sample project with WORKING examples for python3.

## Sub Directory

No __init__.py required.
The syntax is :
```
from SubDirectoryname import FilenameWithoutDotPy

instance = FilenameWithoutDotPy.MyClassName()
```

### Confirm Using

```
python3 subdir-test.py
```

## Nested Sub Directories and Inheritence

Take a look at the files under libproj.
I created an abstract base class that has implemented methods and methods to be implemented by the sub class.