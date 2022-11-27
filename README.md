# AirBnB Clone: Console and Class Tests
This repository is for the purpose of collaborating on building test suites for the afore-mentioned AirBnB project. And so, this README aims to lay foundational guidelines to facilitate collaboration.

## Repository Structure
This repository shall mainly contain directories at the topmost level. Each directory shall contain test, and other, files relating to the different parts of the AirBnB clone project. The directories include:
- **AirBnB_console**

   This directory will contain tests for the first part of the project - the console. The tests here will be based on classes (and their attributes and methods), which are defined in separate files. The test files are thus going to be based on the different classes, with each test file containing tests for only one class. For EVERY assert method called to test a condition, there must be a corresponding comment made describing the test purpose. This comment should appear on a separate line before the assert method call, and follow the following syntax:

   `# T<classPrefix>-<attributePrefix>: <comment>`

   where `<classPrefix>` is class prefix in upper-case; `<attributePrefix>` is the attribute or method prefix in uppercase, and `<comment>` is the body of the comment. The prefixes are defined in the section below. For example, to start a comment for an assert call you are about to make to test the `save()` method of the BaseModel class, you would start like so:

   `# TBASE-SV: ...`

   This can be read as: you are writing a test [T] for the BaseModel class [BASE], on the save() method [SV]. This syntax will enable the repo maintainer to easily extract the comments for separate documentation.

   It is highly encouraged that, apart from writing the comments on a new line before the assert line, you leave a blank line before the comment line. See the `test_base_model.py` file, in the AirBnB_console directory for practical examples to follow.

## Prefixes
*class* BaseModel (prefix: BASE)
| Attribute/method | Prefix |
| ---------------- | ------ |
| id               | ID     |
| updated_at       | UA     |
| created_at       | CA     |
| save()           | SV     |
| to_dict()        | TD     |
| str()            | SR     |



*class* User (prefix: USER)
| Attribute/method | Prefix |
| ---------------- | ------ |
| email            | EM     |
| password         | PW     |
| first_name       | FN     |
| last_name        | LN     |



*class* State (prefix: STAT)
| Attribute/method | Prefix |
| ---------------- | ------ |
| name		   | NM     |



*class* City (prefix: CITY)
| Attribute/method | Prefix |
| ---------------- | ------ |
| state_id	   | SI     |
| name		   | NM     |



*class* Amenity (prefix: AMEN)
| Attribute/method | Prefix |
| ---------------- | ------ |
| name		   | NM     |



*class* Place (prefix: PLAC)
| Attribute/method | Prefix |
| ---------------- | ------ |
| city_id	   | CI     |
| user_id	   | UI     |
| name		   | NM     |
| description	   | DS     |
| number_rooms	   | NR     |
| number_bathrooms | NB     |
| max_guest	   | MG     |
| price_by_night   | PN     |
| latitude	   | LA     |
| longitude	   | LO     |
| amenity_ids	   | AI     |



*class* Review (prefix: REVI)
| Attribute/method | Prefix |
| ---------------- | ------ |
| place_id	   | PI     |
| user_id	   | UI     |
| text		   | TX     |



*class* FileStorage (prefix: FILE)
| Attribute/method | Prefix |
| ---------------- | ------ |
| all()		   | AL     |
| new()		   | NW     |
| save()	   | SV     |
| reload()	   | RL     |
| storage	   | SG     |


## Workflow Overview
In this section, an attempt will be made to summarize the basic flow, from editing a test file to issuing a pull request, for a hypothetical collaborator A (hereafter referred to as collab_A).

Every collaborator should create a branch from `main` whenever they want to modify a test file. So, whenever collab_A wants to add one or more tests to a test file, collab_A should:
1. create a branch from `main`;
2. read the documentation in the `test_doc.txt` file to know what tests are already available;
3. add tests as they want to, in the respective delimited sections (i.e. sections for method and attribute tests). Template test files are already available initialized with the respective sections. These are the files where all tests will be written. to test for a method or attribute, simply prefix `test_` to the method or attribute name and use that as the name of the test method. E.g. to write a test method for the `number_rooms` attribute of the `Place` class, the method header would look like so: `def test_number_rooms(self, ...)`;
4. for every test (i.e. for every assert method called), add a comment summarizing the purpose of the test in the prescribed format. So each comment starts on a separate line with something like `# TUSER-EM: ...` or `# TAMEN-PI: ...`;
5. ensure their test works;
6. after being done with adding tests and associated comments, and testing their new tests, push to their branch;
7. issue a pull request.

Please take care not to merge with `main` yourself - a pull request MUST be issued. Also, once your branch is merged it will be deleted from remote. Ensure to delete your local copy too. The next time you need to modify test files, you have to create a new branch (which can have the same name as previous deleted branch). This is meant to enable you get the latest copy of the test files from `main`.
