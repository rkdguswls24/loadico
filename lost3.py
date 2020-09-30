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
        res = requests.get(url+self.name)
        res.raise_for_status()
        soup = BeautifulSoup(res.text,"lxml")

        contents = soup.find("div",attrs={"class":"profile-ability-basic"})
        self.content = contents.find_all("span")
        
    def get_data(self):
        str1 = ("공격력: "+self.content[1].get_text())
        return str1

# b = spec()
# b.set_name("동네봉")
# print(b.get_data())