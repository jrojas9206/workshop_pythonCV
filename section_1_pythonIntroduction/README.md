# 1. Introduction to Python :snake: and some clarifications 

## 1.1 Who developed Python :snake:? and why? 

The Python programming language was developed by Guido Van Rossum, in the late 80's [1]. The aim of this development was to create a successor to the ABC-programming language. The main characteristics for this new language were that it had to be intuitive, understandable, suitable for everyday tasks and open source [2]. The release to the public was made in 1991 and since then Python has evolved to become one of the most widely used programming languages. 

You will find that Python is flexible and that you can easily approach tasks related to web development, data science, machine learning, computer vision and more.

## 1.2 Some important information before we start coding

Before we start coding I would like to introduce you to: how looks the structure of a python project, what is a virtual environment and to the Python's :snake: package :package: administrator.

### 1.2.1 Classic structure of a python package

When you develop a Python project, you are free to choose the structure that suits you best. But before you start your project, I advise you to make a schema of how you want to call your scripts, check that the call is not in an infinite cycle, and in general you need to define a hierarchy for your project to avoid *import errors*. 

In the projects I have developed, I always try to follow the structure suggested by [python.org](https://packaging.python.org/en/latest/tutorials/packaging-projects/) with some little modifications. See the following schema. 

📦 Project's folder
 ┣ 📂app
 ┃ ┗ 📜app.py
 ┣ 📂src
 ┃ ┣ 📂Package
 ┃ ┃ ┣ 📜module.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📂test
 ┃ ┃ ┗ 📜test_module.py
 ┣ 📜.gitignore
 ┣ 📜pyproject.toml
 ┣ 📜README.md
 ┗ 📜requirements.txt

 In the scheme above, you will notice that the *src* folder contains the *tests* and *package name* subfolders. The *tests* folder will contain all your unit test scripts and other tests, and the *package* folder will contain all the core scripts with the desired functionality. 

 You will also have the *app* folder which contains your application for the dev and production environments, normally the scripts from there will make the call to your package. 

 From my point of view, this simple project architecture gives you stability and an implicit order to your developments. 

### 1.2.2 Virtual environment 

### 1.2.3 The python package administrator: PIP


## References 

1. Chun, Wesley. Core python programming. O'Reilly, 2001.
2. Python® – the language of today and Tomorrow. (n.d.). Retrieved from https://pythoninstitute.org/about-python 