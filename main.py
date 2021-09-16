from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from csv import DictReader
import random
import time
class Bot:
    def __init__(self) -> None:
        self.driver=webdriver.Chrome(executable_path=r"chromedriver.exe")
        self.driver.get(r"https://docs.google.com/forms/d/e/1FAIpQLSeN3XvP7AkYKZ_aEoDWh7Id2u-tVrOGgtJsVfGcyBimSlXjVg/viewform")
    def random_name(self):
        f=open("names.csv")
        random_name_list=[]
        names_list=DictReader(f)
        for i in names_list:
            names_dict=i
            for j in names_dict.values():
                random_name_list.append(j)
        random_name=random.choice(random_name_list)
        return random_name
    def fill_form(self):
        i=0
        while i<=30:
            WebDriverWait(self.driver,10000000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            name=self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            random_name=self.random_name()
            name.send_keys(str(random_name))
            self.driver.find_element_by_xpath('//*[@id="i9"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i28"]/div[3]/div').click()  
            self.driver.find_element_by_xpath('//*[@id="i44"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i63"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i76"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i76"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i95"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i108"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i124"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i140"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i153"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i163"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i173"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i186"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i202"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i221"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i231"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i244"]/div[3]/div').click()
            self.driver.find_element_by_xpath('//*[@id="i257"]/div[3]/div').click()
            submit_button=self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit_button.click()
            WebDriverWait(self.driver,1000000).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
            submit_another=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_another.click()
            WebDriverWait(self.driver,10000000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            i+=1
if __name__ == "__main__":
    bot=Bot()
    bot.fill_form()