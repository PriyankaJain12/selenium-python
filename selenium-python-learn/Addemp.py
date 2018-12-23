from selenium import webdriver

class Addemp:
	dr=webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
	dr.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/auth/login")
	Username=dr.find_element_by_id("txtUsername")
	Username.send_keys("admin")
	password=dr.find_element_by_id("txtPassword")
	password.send_keys("admin")
	login=dr.find_element_by_id("btnLogin")
	login.click()
	pim=dr.find_element_by_id("menu_pim_viewPimModule")
	pim.click()
	Addemp=dr.find_element_by_id("menu_pim_addEmployee")
	Addemp.click()
	firstname=dr.find_element_by_id("firstName")
	firstname.send_keys("Priya")
	LastName=dr.find_element_by_id("lastName")
	LastName.send_keys("Gupta")
	Save=dr.find_element_by_id("btnSave")
	Save.click()

