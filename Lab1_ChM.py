import math
#Вариант №9
#задание №1
#19/12 = 1.58
#√12 = 3.46

X1 = 19/12
X2 = math.sqrt(12)

Y1 = 1.58
Y2 = 3.46

error1 = abs(X1 - Y1)
error2 = abs(X2 - Y2)
print("Вариант №9")
print("Задача №1")
if error1 < error2:
    print("Первое равенство точнее")
elif error1 > error2:
    print("Второе равенство точнее")
else:
    print("Равенства равны")

#////задание №2

def F1(num, unc):
    num_str = str(num - int(num))
    unc_str = str(unc)
    result = str(int(num))
    #print(num_str)

    for i in range(len(unc_str)-1):
        i +=1
        if num_str[i] == '.':
            result += '.'
        elif unc_str[i] == '0' :
            result += num_str[i]
        else:
            
            if int(num_str[i])>=5:
                result = result[:-1] +str(int(result[i])+1)
            break
    absolute0 = (num - float(result))
    return float(result), absolute0

num = 4.88445
unc = 0.00052

y0, y1 = F1(num, unc)
print("Задача №2")
print("Округленное число:", y0)
print("Абсолютная погрешность:", y1)
#///////задание №3
def F2(num):
    absolute =  10**(-len(str(num).split('.')[1]))# *0.5
    relative = absolute / num
    
    return absolute, relative

num = 4.633

absolute, relative = F2(num)
print("Задача №3")
print("Абсолютная погрешность:", absolute)
print("Относительная погрешность:", relative)
