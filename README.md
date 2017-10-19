# python-import-sample

Imports are confusing and the examples are weak; so I am putting together a sample project with WORKING examples for python3.

## Sub Directory

No ```__init__.py``` required.
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

## Logging in Modules

The logging-test.py shows how to turn on logging for an app.
Example.py has a method for turning on class logging; more to come...not done with this yet.


## Unit Test Example

A quick test class has been created to confirm that imports will work with a test class.
Need to try putting the test in a folder and still being able to test a module in a nested directory.
I will create another project for python3 best practices in order to get my mind around abc, mixins, logging, file structure, and naming conventions.

### Confirm Using

```
python3 Test-SomeCls.py
```