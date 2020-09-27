import requests
import re
from bs4 import BeautifulSoup
import string

class mari:
    def __init__(self):
        self.amount = 0 # 초기 시세 입력값
        
        url = "https://lostark.game.onstove.com/Shop#mari" #마리상점 주소
        res = requests.get(url)
        res.raise_for_status()      # 주소 연결 확인
        soup = BeautifulSoup(res.text,"lxml")
        self.list_item = soup.find("ul",attrs={"class":"list-items"}) # 리스트 아이템 T3 탭
        self.items = self.list_item.find_all("div",attrs={"class":"wrapper"})
    
    def set_data(self,amount):
        amount = int(amount)
        self.amount = float(amount/95) # 초기 시세 입력값
        self.amount = round(self.amount,2) 
        

    def print_data(self):

        #print("1크리당 {}골드/".format(self.amount) )
        self.list1="1크리당 {}골드/\n".format(self.amount)
        
        #불러온 아이템당 
        for item in self.items:
            
            item_name = item.find("span",attrs={"class":"item-name"}).get_text()
            item_amount = item.find("span",attrs={"class":"amount"}).get_text()
            item_cnt = re.findall("\d+",item_name[-5:])

            if not item_cnt:
                item_cnt = ['1']
            

            #총 골드 량 = 총 크리스탈 갯수 * 1크리당 골드
            self.item_total = round(int(item_amount)*self.amount,2)
            
            #개당 골드량 = 총 골드 량 / 아이템 갯수
            amount_per = round(self.item_total/int(item_cnt[0]),2)

            
            str1= str("{0:<25}/  ".format(item_name) + " {} 크리스탈/  ".format(item_amount)+\
                " {:.2f} 골드/  ".format(self.item_total)+" 개당 {} 골드\n".format(amount_per))
            
            self.list1 = self.list1+str1
            # print("{0:<20}/  ".format(item_name),end='')
            # print(" {}크리스탈/  ".format(item_amount),end='')
            # print(" {:.2f}골드/  ".format(self.item_total),end='')
            # print(" 개당{}골드".format(amount_per))

            
        return self.list1    
    
    






