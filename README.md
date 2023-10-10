# ALX-Holberton B&B - AirBnB Clone

![ALX-Holberton B&B](https://user-images.githubusercontent.com/88311316/151070609-19608294-829e-408b-b2b3-5d1f2873f1e3.png)

## Project Description
ALX-Holberton B&B is the culmination of four months of intensive study at the ALX-Holberton School, where I've been learning the ropes of full-stack software engineering. This project aims to replicate the functionality of the Airbnb website using my own server. The final version of this project will include:

1. A command-line interpreter for data manipulation without a visual interface (for development and debugging).
2. A website (front-end) with both static and dynamic features.
3. A comprehensive database to manage backend functionalities.
4. An API to facilitate communication between the front-end and back-end of the system.
5. A review of general software engineering concepts.

As you navigate through this codebase, it's essential to keep in mind the following key concepts covered during this project:

- Creating a Python package
- Developing a command-line interpreter in Python using the `cmd` module
- Implementing unit testing in a large project
- Serializing and deserializing classes
- Working with JSON files for data storage
- Managing datetime
- Understanding UUIDs
- Utilizing `*args` and `**kwargs` in Python functions
- Handling named arguments in functions

## Environment

The development environment for this project used Ubuntu 14.04LTS and Python 3.4.3.

### Additional Information

For more information about Python versions and documentation, you can visit [python.org](https://www.python.org/).

## Requirements

To contribute or work with this project, you should have knowledge of Python 3, experience with command-line interpreters, and access to a computer running Ubuntu 14.04. Make sure you have Python 3 and a PEP 8 style checker installed.

## Repository Contents

This repository contains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Provides information about the authors of the project |
|[base_model.py](./models/base_model.py) | Defines the BaseModel class (parent class) and its methods |
|[user.py](./models/user.py) | Defines the User subclass |
|[amenity.py](./models/amenity.py) | Defines the Amenity subclass |
|[city.py](./models/city.py)| Defines the City subclass |
|[place.py](./models/place.py)| Defines the Place subclass |
|[review.py](./models/review.py) | Defines the Review subclass |
|[state.py](./models/state.py) | Defines the State subclass |
|[file_storage.py](./models/engine/file_storage.py) | Handles the creation of new class instances, serialization, and deserialization of data |
|[console.py](./console.py) | Allows for the creation of objects, retrieval of objects from files, manipulation of objects, updating of object attributes, and destruction of objects |
|[test_base_model.py](./tests/test_models/test_base_model.py) | Contains unit tests for the BaseModel class |
|[test_user.py](./tests/test_models/test_user.py) | Contains unit tests for the User class |
|[test_amenity.py](./tests/test_models/test_amenity.py) | Contains unit tests for the Amenity class |
|[test_city.py](./tests/test_models/test_city.py) | Contains unit tests for the City class |
|[test_place.py](./tests/test_models/test_place.py) | Contains unit tests for the Place class |
|[test_review.py](./tests/test_models/test_review.py) | Contains unit tests for the Review class |
|[test_state.py](./tests/test_models/test_state.py) | Contains unit tests for the State class |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | Contains unit tests for the file_storage module |
|[test_console.py](./tests/test_console.py) | Contains unit tests for the console.py file |

## Installation

To get started, clone this repository and run the console.py file:

```bash
$ git clone https://github.com/------/AirBnB_clone.git
$ ./console.py

Usage
Command-Line Methods
The following methods are available for use in the command-line interpreter:

- `create`: Creates an object of a given class.
- `show`: Prints the string representation of an instance based on the class name and ID.
- `all`: Prints all string representations of instances, based on the class name (or not).
- `update`: Updates an instance based on the class name and ID by adding or updating attributes (saves changes into the JSON file).
- `destroy`: Deletes an instance based on the class name and ID (saves changes into the JSON file).
- `count`: Retrieves the number of instances of a class.
- `help`: Provides information about a specific command.
- `quit` or `EOF`: Exits the program.

---

0x00. AirBnB Clone - The console

## Table of Contents
1. Introduction
2. Environment
3. Installation
4. Testing
5. Usage
6. Authors

### 1. Introduction
The ALX-Holberton B&B is a team project aimed at building a clone of the AirBnB website. The console component serves as a command interpreter to manage object abstractions and how they are stored.

#### 1.1 Features
The console is responsible for performing the following tasks:

- Creating new objects.
- Retrieving objects from a file.
- Performing operations on objects.
- Deleting objects.

#### 1.2 Storage
All classes are managed by the Storage engine using the FileStorage class.

### 2. Environment
- Operating System: Ubuntu 20.04 LTS
- Python Version: 3.8.3
- Editors: VIM 8.1.2269, VSCode 1.6.1, Atom 1.58.0
- Version Control: Git 2.25.1

### 3. Installation
Clone the repository and change to the AirBnb directory, then run the following command:

```bash
./console.py

3.1 Execution
Interactive mode:

$ ./console.py
(hbnb)

Non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

Testing
All tests are defined in the tests folder.
4.1 Documentation
Modules: python3 -c 'print(__import__("my_module").__doc__)'
Classes: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
Functions (inside and outside a class): python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

4.2 Python Unit Tests
Testing Framework: unittest module
File Extension: .py
Test Files and Folders: Start with test_
Organization: For models/base.py, unit tests are in tests/test_models/test_base.py
Execution Command: python3 -m unittest discover tests
Or: python3 -m unittest tests/test_models/test_base.py

4.3 Running Tests
Run tests in interactive mode:

echo "python3 -m unittest discover tests" | bash

Run tests in non-interactive mode:
python3 -m unittest discover tests

Usage
5.1 Getting Started
Start the console in interactive mode:

$ ./console.py
(hbnb)

Use the help command to see the available commands:

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)

Quit the console:
(hbnb) quit
$


5.2 Available Commands
create: Create a new instance of a given class.
show: Display the string representation of an instance based on the class name and ID.
destroy: Delete an instance based on the class name and ID.
all: Print the string representations of all instances based on the class name (or not).
count: Retrieve the number of instances of a class.
update: Update an instance based on the class name and ID by adding or updating an attribute (saves the change into the JSON file).
help: Get information about a specific command.
quit or EOF: Exit the program.

Authors
Olutayo Victor, Ogunlade
GitHub: https://github.com/Olutayo0910
LinkedIn: www.linkedin.com/in/olutayo-victor-ogunlade-cpca-5644261a5
E-mail: olutayoogunlade2022@gmail.com
Adeoti Babatunde
