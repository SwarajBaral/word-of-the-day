from selenium import webdriver as wb
from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _= system('clear')

esc = '\033[m'
cyan = "\033[1;32;36m"
green = "\033[1;32;40m"
#highlight = "\033[5;37;40m"

url = 'https://www.dictionary.com/e/word-of-the-day/'

options = wb.ChromeOptions()
options.headless = True
browser = wb.Chrome(executable_path='../ChromeDriver/chromedriver.exe', options=options)
browser.get(url)

word = browser.find_element_by_class_name("otd-item-headword__word")
pos = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[5]/div/p[1]/span/span")
desc = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[5]/div/p[2]")
origin = browser.find_element_by_class_name("wotd-item-origin__content")

clear()

print("The word of the day is : \n")
print(cyan + word.text + esc + ": " + green + pos.text + esc)
print("-------------------------------")
print(desc.text)
print("\n" + origin.text)

browser.close()
