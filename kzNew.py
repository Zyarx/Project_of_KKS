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
def num():

	#вводим пользовательское число
	num=int(input())

	#ограничение для числа and рекурсивная ловушка

	if 999<num<10000:
        	print("")
	elif num<999 or num>10000:
        	while num<999 or num>10000:
                	num=int(input())

	#переводим число в строку для проверки
	n=str(num)
	#начало второй рекурсивной ловушки
	if n[0]!=n[1]!=n[2]!=n[3] and n[1]!=n[0]!=n[2]!=n[3] and n[2]!=n[0]!=n[1]!=n[3] and n[3]!=n[0]!=n[1]!=n[2]:
       		 1+1
	elif n[0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3]  :
       		 while n[0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3] :
                	n=str(input())

	return n
#конец функции 


#начало функции топоры и тузы
def Ace_Axe(n,q):

	#Начало реализации правил игры
	#система работы топоров
	i=0
	c=0

	for i in range(4):
       		 if q[i]==n[i]:
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
                	if q[r]==n[g]:
                        	d=d+1
               		else :
                       		g=g+1

	d=d-c
	print ('Вы имеете'+' '+str(d)+' '+'Туза')
	#cистема работы тузов отлажена

	return c

#конец функии 

#функция самой игры 

def open(num,q):
	n=num()
	c=Ace_Axe(n,q)
	return c
#конец функции
c=open(num,q)
#условие цикличности
if c==4:
	print("OK")
elif c!=4 or c==0 :
	while c!=4 :
		c=open(num,q)
#Конец
