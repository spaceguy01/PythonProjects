from selenium import webdriver

"""Scrapes the Main titles and Sub-titles of subjects for
Udemy: Automate The Boring Stuff course"""

driver = webdriver.Chrome()

url = 'https://www.udemy.com/automate/'

driver.get(url)


"""Clicking on tab to show all the subjects"""

driver.find_element_by_class_name("js-load-more").click()

titles = driver.find_elements_by_class_name("lecture-title-text")


"""Returning Scraped Data"""

print ("\nThe Main Titles are as follows:\n")
for each in titles:
    print (each.text)

print ("--"*40)
print ('\n')

subtitles = driver.find_elements_by_class_name("title")

print ("\nThe Sub-Titles are as follows: \n\n")

for each in subtitles:
    print (each.get_attribute('textContent').strip())
