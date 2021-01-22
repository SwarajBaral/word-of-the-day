# word-of-the-day
A python script that scrapes [Dictionary](https://www.dictionary.com/) to display the word of the day, its meaning and its description in the terminal. Can be added to bashrc to run it everytime you open cmd or terminal.

## Getting Started
### Packages
-Selenium - to be used as Selenium webdriver.
To install the required packages for this script. Navigate to the repository on your local machine run the following command in the terminal.
```python3
$ pip install -r requirements.txt
```
### Usage
To run the script
```python3
$ python wotd.py
```
## Built with
Python 3.8.3rc1

## Author
Swaraj Baral - *Student*

---
**NOTE**
: The script wont work if correct browser driver path isn't provided. The webdriver has to be chosen according to the user's web browser and browser version.
- To use a different web browser or a different version of a browser. 
  1. Download the latest version of preferred browser
  2. Change the executable_path = ' ' paramete. Set it to the location of your driver.
---
