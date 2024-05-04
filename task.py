def number(number):
    for num in number:
        if num%5==0:
            if num>150:
                continue
            elif num>500:
                break
            else:
                print(num)
                
ex=[]
for i in range(1,6):
    num=input('enter number in list:')
    num=int(num)
    ex.append(num)
    
    print(number(ex))