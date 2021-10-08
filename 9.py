def plo():
	if S>=(2*K+2*R)**2:
		print ("сцену вписать можно")
	else:
		print ("сцену вписать нельзя")
try: 
	print ("введите площадь зала")
	S=int(input())
	print ("введите радиус сцены")
	R=int(input())
	print ("введите растояние от сцены до стены")
	K=int(input())
except ValueError:
	print ("введены некоректные данные")
	exit()
plo()

