import random
num=random.randint(1,20)
print(num)
玩次數=0
數字=input('請猜數字1~20:')
玩次數=玩次數+1
數字=int(數字)
while 玩次數<=5:
     if num==數字:
        print('答對了，你玩了',玩次數,'次')
        玩次數=999
     elif 玩次數==5 and 數字!=num :
        print('繼續挑戰! 答案是:',num)
        玩次數=999
     else:
         if 數字>num:
             print('太大了')
             
         elif 數字<num:
             print('太小了')
         print('還剩:',5-玩次數,'次')
         數字=input('再猜一次:')
         玩次數=玩次數+1
         數字=int(數字)
    


