import warnings
import random
warnings.filterwarnings("ignore", category=DeprecationWarning) 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.calculator.net")

driver.maximize_window()
driver.find_element_by_xpath("//*[@id='contentout']/table/tbody/tr/td[3]/div[2]/a").click();
driver.find_element_by_xpath("//*[@id='content']/table[2]/tbody/tr/td/div[3]/a").click();

print (driver.title)
print (driver.current_url)

def WatiPrintCase(number1, number2,result, case):
	if case==1:
		return str(number1)+"% of"+str(number2)+" = "+str(result)
	if case==2:
		return str(result)+" is "+str(number1)+"%"+" of "+str(number2)+"."
	if case==3:
		return str(number1)+" is "+str(result)+"%"+" of "+str(number2)+"."

def unitCase(id1, id2, number1, number2, BtnXpath, result,case):
	ElementCpar1=driver.find_element_by_name(id1)
	ElementCpar2=driver.find_element_by_name(id2)
	ElementCpar1.send_keys(number1)
	ElementCpar2.send_keys(number2)

	driver.find_element_by_xpath(BtnXpath).click() 
	resultPage= driver.find_element_by_xpath("//*[@id='content']/p[2]")
	print (resultPage.text)

	Waitresult=WatiPrintCase(number1,number2,result,case)
	print(Waitresult)

	try:
		assert resultPage.text==Waitresult
	except Exception as e:
		print("ERROR, hay un problema")
	
	
	driver.find_element_by_name(id1).clear()

	driver.find_element_by_name(id2).clear()
	


def test_Aleatorio():
	#########Percentage Calculator in Common Phrases
	for i in range(10):
		alea1=random.randrange(1, 100,4)
		alea2=random.randrange(-1000, 1000,10)
		resultado=alea1/100 *alea2
		if int(resultado)== resultado:
			resultado=int(resultado)
		unitCase("c21par1","c21par2",alea1,alea2,"//*[@id='content']/table[2]/tbody/tr/td[2]/input[2]",resultado,2)

	'''for i in range(10):
		alea1=random.randrange(-1000, 1000,4)
		alea2=random.randrange(-1000, 1000,10)
		resultado=alea1/alea2*100
		if int(resultado)== resultado:
			resultado=int(resultado)
		unitCase("c21par1","c21par2",alea1,alea2,"//*[@id='content']/table[2]/tbody/tr/td[2]/input[2]",resultado,3)'''



test_Aleatorio()


