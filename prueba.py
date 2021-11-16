from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.calculator.net")

driver.maximize_window()
driver.find_element_by_xpath("//*[@id='contentout']/table/tbody/tr/td[3]/div[2]/a").click();
driver.find_element_by_xpath("//*[@id='content']/table[2]/tbody/tr/td/div[3]/a").click();

print (driver.title)
print (driver.current_url)

def unitCase(id1, id2, number1, number2, BtnXpath):
	ElementCpar1=driver.find_element_by_name(id1)
	ElementCpar2=driver.find_element_by_name(id2)
	ElementCpar1.send_keys(number1)
	ElementCpar2.send_keys(number2)
	driver.find_element_by_xpath(BtnXpath).click() 

	driver.execute_script("arguments[0].setAttribute('value','')", ElementCpar2)
	driver.execute_script("arguments[0].setAttribute('value','')", ElementCpar1)
	resultado= driver.find_element_by_xpath("//*[@id='content']/p[2]")

	print (resultado.text)

#unitCase("cpar1","cpar2",12,-200,"//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]")

unitCase("c21par1","c21par2",12,200,"//*[@id='content']/table[2]/tbody/tr/td[2]/input[2]")
unitCase("c21par1","c21par2",12,300,"//*[@id='content']/table[2]/tbody/tr/td[2]/input[2]")
unitCase("c21par1","c21par2",12,-100,"//*[@id='content']/table[2]/tbody/tr/td[2]/input[2]")
'''unitCase("cpar1","cpar2",12,200,"//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]")
unitCase("cpar1","cpar2",12,200,"//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]")
unitCase("cpar1","cpar2",12,200,"//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]")'''


#ElementCpar1=driver.find_element_by_name("cpar1")
#ElementCpar2=driver.find_element_by_name("cpar2")

#ElementCpar1.send_keys(10)
#ElementCpar2.send_keys(200)

#driver.find_element_by_xpath("//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]").click() 

#resultado= driver.find_element_by_xpath("//*[@id='content']/p[2]")

