#Spinkoins
#область работы карины

#подключение функции рандома
import random

#задаем рандомное число для отгадывания
random_num=random.randint(1000,9999)
#переводим рандомное число в строку для проверки
q=str(random_num)
#начало рекурсивной ловушки для рандомного числа
if q[0]!=q[1]!=q[2]!=q[3] and q[1]!=q[0]!=q[2]!=q[3] and q[2]!=q[0]!=q[1]!=q[3] and q[3]!=q[0]!=q[1]!=q[2]:
        1+1
elif q[0]==q[1] or q[0]==q[2] or q[0]==q[3] or q[1]==q[2] or q[1]==q[3] or q[2]==q[3]  :
        while q[0]==q[1] or q[0]==q[2] or q[0]==q[3] or q[1]==q[2] or q[1]==q[3] or q[2]==q[3] :
                q=str(random.randint(1000,9999))

#конец ловушки

print(q)

#начало функции по вводу пользовательского числа
def number():
	#вводим пользовательское число
	num=str(input())
	#ограничение для числа and рекурсивная ловушка
	l=len(num)
	if l==4 and num[0]!=num[1]!=num[2]!=num[3]:
             print("Ok")
	else :
		while l!=4 or num[0]==num[1] or num[0]==num[2] or num[0]==num[3] or num[1]==num[2] or num[1]==num[3] or num[2]==num[3]:
			print("ошибка")
			num=str(input())
			l=len(num)
			print(num)
	return num
#конец функции 


#начало функции топоры и тузы
def Ace_Axe(num,q):

	#Начало реализации правил игры
	#система работы топоров
	i=0
	c=0

	for i in range(4):
       		 if q[i]==num[i]:
                	c=c+1
       		 else :
                	i=i+1
	
	print ('Вы имеете'+' '+str(c)+' '+'Топора')
	#cистема работы топоров отлажена
	
	#система работы тузов	
	r=0
	g=0
	d=0

	for r in range(4):
        	for g in range(4):
                	if q[r]==num[g]:
                        	d=d+1
               		else :
                       		g=g+1

	d=d-c
	print ('Вы имеете'+' '+str(d)+' '+'Туза')
	#cистема работы тузов отлажена
	return c

#конец функии 

#функция самой игры 

def open(number,q):
	num=number()
	c=Ace_Axe(num,q)
	return c
#конец функции
c=open(number,q)
#условие цикличности
if c==4:
	print("OK")
elif c!=4 or c==0 :
	while c!=4 :
		c=open(number,q)
#Конец
