import requests
import re
from bs4 import BeautifulSoup
import string

class mari:
    def __init__(self):
        self.amount = 0 # 초기 시세 입력값
        
        
    
    def set_data(self,amount):
        url = "https://lostark.game.onstove.com/Shop#mari" #마리상점 주소
        res = requests.get(url)
        res.raise_for_status()     # 주소 연결 확인
        soup = BeautifulSoup(res.text,"lxml")
        #self.list_item = soup.find("ul",attrs={"class":"list-items"}) # 리스트 아이템 T3 탭
        self.list_item = soup.find("div",attrs={"id":"lui-tab1-1"})
        self.list_item = self.list_item.find("ul",attrs={"class":"list-items"})
        self.items = self.list_item.find_all("div",attrs={"class":"wrapper"})
        

        #T2 items
        self.list_item2 = soup.find("div",attrs={"id":"lui-tab1-2"})
        self.list_item2= self.list_item2.find("ul",attrs={"class":"list-items"})
        self.items2 = self.list_item2.find_all("div",attrs={"class":"wrapper"})

        
        amount = int(amount)
        self.amount = float(amount/95) # 초기 시세 입력값
        self.amount = round(self.amount,2) 
        
        

    def print_data(self,items):
        
        #print("1크리당 {}골드/".format(self.amount) )
        list1="1크리당 {}골드/\n".format(self.amount)
        
        #불러온 아이템당 
        for item in items:
            
            item_name = item.find("span",attrs={"class":"item-name"}).get_text()
            #print(item_name)
            item_amount = item.find("span",attrs={"class":"amount"}).get_text()     #아이템 크리스탈 금액
            item_cnt = re.findall("\d+",item_name[-8:])                             #아이템 수량
            #print(item_cnt)

            if not item_cnt:
                item_cnt = '1'
            else:
                item_cnt = ''.join(item_cnt)

            #총 골드 량 = 총 크리스탈 갯수 * 1크리당 골드
            self.item_total = (int(item_amount)*self.amount)             
            # print(self.item_total)
            # print(item_cnt)
            #개당 골드량 = 총 골드 량 / 아이템 갯수
            amount_per = self.item_total/int(item_cnt)

            p= re.compile("석 결정+")
            m = p.search(item_name)
            #print(m)
            
            if m:
                str1= str("{0:<25}/  ".format(item_name) + " {} 크리스탈 /  ".format(item_amount)+\
                " {:.2f} 골드 /  ".format(self.item_total)+" 10 개당 {:.2f} 골드\n".format(amount_per*10))
            else:
                str1= str("{0:<25}/  ".format(item_name) + " {} 크리스탈 /  ".format(item_amount)+\
                    " {:.2f} 골드 /  ".format(self.item_total)+" 개당 {:.2f} 골드\n".format(amount_per))
            
            list1 = list1+str1
            # print("{0:<20}/  ".format(item_name),end='')
            # print(" {}크리스탈/  ".format(item_amount),end='')
            # print(" {:.2f}골드/  ".format(self.item_total),end='')
            # print(" 개당{}골드".format(amount_per))

        return list1

    def get_data(self):
        content =("T3\n"+
        self.print_data(self.items)+
        "\nT2\n"+
        self.print_data(self.items2))
        return content
        # print("T3")
        # print(self.print_data(self.items))
        # print("T2")
        # print(self.print_data(self.items2))

    




# a = mari()
# try:
#     a.set_data(1000)
#     print(a.get_data())
# except Exception as e:
#     print(e)
#     print("골드를 입력하세요\n사용예) !마리 1000")



