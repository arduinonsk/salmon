#!/usr/bin/env python
#-*-coding=utf-8-*-

# импортируем библиотеку Arduino
from pyavrutils import Arduino
# выбираем компилятор
cc = Arduino()
# пишем скетч Arduino без лососей
codebegin = 'void setup(){Serial.begin(19200);}void loop(){Serial.println("'
codeend = '");}'
# задаем количество лососей
n = 0
# бесконечный цикл
while(1):
	# добавляем одного лосося и складываем всех лососей в строку
	n+=1
	salmons = ''
	for salmon in range(n):
		salmons += 'salmon'
	# встраиваем лососей в скетч 
	code = codebegin + salmons + codeend
	# компилируем скетч
	cc.build(code)
	# получаем объем занятой RAM в процентах
	ramused = str(cc.size()).split(' ')[6]
	# печатаем количество лососей и объем занятой RAM на печать
	print "salmon count:", n, "| RAM used:", ramused
	# если памяти занято больше 100% - выходим
	if float(ramused[:-1]) > 100: break
# печатаем сколько лососей влезло в RAM
print "Your RAM if full of salmon. There are", n-1, "salmons fit."
