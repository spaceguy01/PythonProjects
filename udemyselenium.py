from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.udemy.com/selenium-webdriver-with-python3/'

driver.get(url)

driver.find_element_by_class_name("js-load-more").click()

titles = driver.find_elements_by_class_name("lecture-title-text")

print ("\nThe Main Titles are as follows: \n\n")
for each in titles:
    print (each.text)

print ("--"*60)
print ('\n\n')

subtitles = driver.find_elements_by_class_name("title")

print ("\nThe Sub-Titles are as follows: \n\n")

for each in subtitles:
    print (each.get_attribute('textContent').strip())
