import requests
import re
from bs4 import BeautifulSoup





# for stat in content:
#     print(stat.get_text())


class spec:
    def __init__(self):
        pass
    
    def set_name(self,name):
        self.name = name
        url = "https://lostark.game.onstove.com/Profile/Character/"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
        res = requests.get(url+self.name,headers=headers,verify=False)
        res.raise_for_status()
        soup = BeautifulSoup(res.text,"lxml")

        contents = soup.find("div",attrs={"class":"profile-ability-basic"})
        self.content = contents.find_all("span")
        self.realspec = soup.find("div",attrs={"class":"profile-ability-tooltip"})
        #print(self.realspec.get_text())
        
    def get_data(self):
        str1 = ("공격력: "+self.content[1].get_text()+""+self.realspec.get_text())
        return str1

# b = spec()
# b.set_name("찌크릿가든")
# print(b.get_data())
