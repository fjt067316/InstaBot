from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Josh\PycharmProjects\WebScraper\chromedriver.exe")

driver.get('https://instagram.com/accounts/login/')
#insta needs time to import forms after loading webpage bc they don't hard code it in
time.sleep(1)
username = driver.find_element_by_name('username')
passwd = driver.find_element_by_name('password')
#username = driver.find_elements_by_xpath('//input[@name="username"]')
#passwd = driver.find_elements_by_xpath('//input[@name="password"]')
print(username)

#username.clear()
username.send_keys('') # enter your login
#passwd.clear()
passwd.send_keys('') # enter your login

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

#we're logged in now time to follow people and put them in a list and after a few days unfollow them :)
#where #lit is I could create a dictionary and have the bot cycle through #'s
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('#nice')
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
time.sleep(2)

i = 1
a = 1
driver.execute_script("window.scrollTo(0,1300)")

while a < 200:
    if i > 3:
        i = 1
        a += 1
        driver.execute_script("window.scrollTo(0,1700)")

#click on post after scrolling
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[%s]/div[%s]/a/div[1]/div[2]' % (a, i)).click()
    # click on follow
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
    # when 'x' button is available after follow button it means they are already followed so click 'unfollow'
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
    except:
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
        driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
#click the x to go back
 #       driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()

    i += 1


