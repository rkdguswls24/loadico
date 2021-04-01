import random


class dice:
    def __init__(self):
        pass
    def get_data(self,names):
        names = names.split(' ')
        if(len(names)>1):
            data=self.listshuffle(names)
            return data
        else:
            data=self.numshuffle(names)
            return data
    
    def numshuffle(self,names):
        num = int(names[0])
        num = random.randint(1,num)
        return str(num)

    def listshuffle(self,names):
        data=random.sample(names,1)
        return str(data)

# if __name__ == '__main__':
#     m = dice()
#     arr = input('enter:')
#     print(m.get_data(arr))
    
    
