from selenium import webdriver
driver = webdriver.Chrome()

city = str(input("Enter the name of the city: ")).replace(' ','-')

driver.get('https://www.weather-forecast.com/locations/'+city+"/forecasts/latest")


print('-'*60)
print (driver.find_elements_by_class_name("b-forecast__table-description-title")[0].text)
print (driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
print ('-'*60)

print (driver.find_elements_by_class_name("b-forecast__table-description-title")[1].text)
print (driver.find_elements_by_class_name("b-forecast__table-description-content")[1].text)
print ('-'*60)
print (driver.find_elements_by_class_name("b-forecast__table-description-title")[2].text)
print (driver.find_elements_by_class_name("b-forecast__table-description-content")[2].text)
print ('-'*60)
