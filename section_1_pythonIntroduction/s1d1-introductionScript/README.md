# Hello world from Python!

The Hello World program is usually the first program any programmer writes. It is basically a program that prints the phrase "Hello World!" to the terminal. To do this, you just need the following line of code in your python script or python terminal.

```python
# Code 1. 
print('Hello world!')
```

In section 1 you will learn how to create a Python script and set the previous line of code. And in section 2 you will find the different ways to execute Python code. 

# 1. Creating a python script

The instructions you will find here are for VSCode, if you are working with another IDE (Integrated Development Environment) the steps or paths will probably be a bit different. 
<figure>
    <img src='https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png'/>
    <figcaption><b>Figure 1.</b> Screenshot of VSCode. Figure taken from <a href=''>Visual Studio Code</a>.
    </figcaption>
</figure>


I assume that you already open VSCode, be attentive to Figure 1, and follow the next steps:

- In the editor bar go to **'File>Open Folder'** and select the repository folder.
- In the activity bar select the **Explorer**. Next, do right click on the folder **s1d1-introductionSctipt** and select the option **New File** and write the name of our python script **myHelloWorld.py**. Next click enter and the python file will be automatically opened. 
-  Inside the file, write the code shown in Code 1. Next, go to **'File>Save'**.
- Read the next section to learn how to run the Python script.
 

## 2. Executing python code

The Python code can be executed in two ways. **Firstly**, you can create a Python script, which is basically a plain text file with a *.py* extension (Steps done in the previous section). Write your Python code inside and then execute it by calling *python* from your terminal/powershell. In VSCode you go to Editor Bar **'Terminal>New Terminal'** and execute 1 by 1 the following lines of code.  

```bash 
# Command 1 - Changing to the directory were the python script is located
cd section_1_pythonIntroduction/s1d1-introductionScript/
```

```python
# Command 2 - Execting a python script from terminal/powershell
python helloWorld.py
```


**Second**, you can open your Python terminal, type or copy and paste your code there, and see each line of code executed one at a time. 

To open your Python terminal, type the word *python* or *python3* into your terminal. You will see a message similar to the following

```bash

Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.
 
>>>
```

after the symbol '>>>' you can write and execute your code. 

```python
>>> print('Hello world!') # Press enter to execute the line of code
Hello world!
>>>
```

## What next ?

- [Variable and datastructures](https://github.com/jrojas9206/workshop_pythonCV/tree/main/section_1_pythonIntroduction/s1d2-variablesAndDataStructures)

**Updated 23.10.2024**