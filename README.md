# AirBnB Clone: Console and Class Tests
This repository is for the purpose of collaborating on building test suites for the afore-mentioned AirBnB project. And so, this README aims to lay foundational guidelines to facilitate collaboration.

## Repository Structure
This repository shall mainly contain directories at the topmost level. Each directory shall contain test, and other, files relating to the different parts of the AirBnB clone project. The directories include:
- **AirBnB_console**

   The tests here will be based on classes (and their attributes and methods), which are defined in separate files. The test files are thus going to be based on the different classes, with each test file containing tests for only one class. For every assert method called to test a condition, there must be a corresponding comment made describing the test purpose. This comment should appear on a separate line before the assert method call, and follow the following syntax:

   `# T<classPrefix>-<attributePrefix>: <comment>`

   where <classPrefix> is class prefix in upper-case; <attributePrefix> is the attribute or method prefix in uppercase, and <comment> is the body of the comment. The prefixes are defined in the section below. For example, to start a comment for an assert call you are about to make to test the `save()` method of the BaseModel class, you would start like so:

   `# TBASE-SV: ...`

   This can be read as: you are writing a test [T] for the BaseModel class [BASE], on the save() method [SV]. This syntax will enable the repo maintainer to easily extract the comments for separate documentation.

## Prefixes
BaseModel (prefix: BASE)
| Attribute/method | Prefix |
| ---------------- | ------ |
| id               | ID     |
| updated_at       | UA     |
| created_at       | CA     |
| save()           | SV     |
| to_dict()        | TD     |
| str()            | SR     |
