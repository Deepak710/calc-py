# calc-py

## This is a simple Calculator Program to illustrate the various functionalities of Python.

### To Run this file,
1. [Clone](https://github.com/Deepak710/calc-py.git)/[Download](https://github.com/Deepak710/calc-py/archive/master.zip) this repo
1. Make Sure you have [Python](https://www.python.org/downloads/) installed (above 3.x)
1. Run calc.py using the Python IDLE

### Features:
1. Can do calculations of **exactly** two numbers, either integers or floats
1. Supported calculations
	* Addition
	* Suntraction
	* Multiplication
	* Division
	* Remainder (Modulo)
	* Exponent
1. Can view history of calculations (stored in history.txt, created when you make your first calculation)
1. Can't manually edit input (or) history Text Area. *(History can be changed by manually editing history.txt, pls don't it might crash the program)*
1. Can be made into a package *(pls don't, it'll be a disgrace to all the existing packages)*
	* Navigate to the root directory (calc-py)
	* Open Command Prompt here
	* Run either/both the following commands:
		* **python setup.py sdist** - for source distribution
		* **python setup.py bdist_wininst** - for windows binary distribution
	* Run **python setup.py register** to register the package
	* Run **python setup.py sdist upload** to upload the package to [PyPI](https://pypi.org)
	* Now that it is in the community, anyone can use it by using the following command
		* **python setup.py install** - directly from source distribution files
		* **pip install calc-py** - install from [pip](https://pypi.org/project/pip/)
	* Use the function.py script by 
		```python

		from calc-py import function as f
		
		root = f.t.Tk()
		root.title("Calculator")
		root.geometry("120x175")
		app = f.MyApp(root)
		root.mainloop()
		```

### Versions:
* **0.0a1.dev1**
	* Initial Commit
	* Bugs
		1. Random wrong answers
		1. What bug could be more severe than this, that too in a _**CALCULATOR!!!**_

Contact Me:

[Telegram](https://web.telegram.org/#/im?p=@AzorAhoy)
