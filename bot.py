from time import sleep
from selenium import webdriver
from secrets import username, password, nbr_likes


class tinderbot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.i = 0

    def login(self, nbr_likes):   
        self.driver.get("https://www.tinder.com")
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button').click()

        sleep(2)

        if len(self.driver.window_handles) == 2:
            self.driver.switch_to_window(self.driver.window_handles[1])
        else:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button').click()
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button').click()
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/button').click()
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[3]/button').click()
            sleep(2)
            self.driver.switch_to_window(self.driver.window_handles[1])
            

        sleep(2)
            

        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input').send_keys(username)
        sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]').click()

        sleep(5)

        self.driver.switch_to_window(self.driver.window_handles[0])

        sleep(5)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]').click()

        sleep(10)

        while self.i < nbr_likes:
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
            except Exception:
                try :
                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click()
                except Exception:
                    try:
                        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
                    except Exception:
                        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/a').click()
            sleep(3)
            self.i = self.i + 1
            print(self.i)

        
