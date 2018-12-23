from selenium import webdriver

class LoginTest:
	dr=webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
	dr.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/auth/login")
	Username=dr.find_element_by_id("txtUsername")
	Username.send_keys("admin")
	password=dr.find_element_by_id("txtPassword")
	password.send_keys("admin")
	login=dr.find_element_by_id("btnLogin")
	login.click()