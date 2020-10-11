from math import *
import random
a=dict()
dict={	
	1: ['y','n',38],
	2:['n','n'],
	3:['n','n'],
	4:['y','n',14],
	5:['n','n'],
	6:['n','n'],
	7:['n','n'],
	8:['y','n',30],
	9:['n','n'],
	10:['n','n'],
	11:['n','n'],
	12:['n','n'],
	13:['n','n'],
	14:['n','n'],
	15:['n','n'],
	16:['n','n'],
	17:['n','n'],
	18:['n','n'],
	19:['n','n'],
	20:['n','n'],
	21:['y','n',42],
	22:['n','n'],
	23:['n','n'],
	24:['n','n'],
	25:['n','n'],
	26:['n','n'],
	27:['n','n'],
	28:['n','n'],
	29:['n','n'],
	30:['n','n'],
	31:['n','n'],
	32:['n','y',0,10],
	33:['n','n'],
	34:['n','n'],
	35:['n','n'],
	36:['n','y',0,6],
	37:['n','n'],
	38:['n','n'],
	39:['n','n'],
	40:['n','n'],
	41:['n','n'],
	42:['n','n'],
	43:['n','n'],
	44:['n','n'],
	45:['n','n'],
	46:['n','n'],
	47:['n','n'],
	48:['n','y',0,26],
	49:['n','n'],
	50:['y','n',67],
	51:['n','n'],
	52:['n','n'],
	53:['n','n'],
	54:['n','n'],
	55:['n','n'],
	56:['n','n'],
	57:['n','n'],
	58:['n','n'],
	59:['n','n'],
	60:['n','n'],
	61:['n','n'],
	62:['n','y',0,18],
	63:['n','n'],
	64:['n','n'],
	65:['n','n'],
	66:['n','n'],
	67:['n','n'],
	68:['n','n'],
	69:['n','n'],
	70:['n','n'],
	71:['y','n',92],
	72:['n','n'],
	73:['n','n'],
	74:['n','n'],
	75:['n','n'],
	76:['n','n'],
	77:['n','n'],
	78:['n','n'],
	79:['n','n'],
	80:['y','n',99],
	81:['n','n'],
	82:['n','n'],
	83:['n','n'],
	84:['n','n'],
	85:['n','n'],
	86:['n','n'],
	87:['n','n'],
	88:['n','y',0,24],
	89:['n','n'],
	90:['n','n'],
	91:['n','n'],
	92:['n','n'],
	93:['n','n'],
	94:['n','n'],
	95:['n','y',0,56],
	96:['n','n'],
	97:['n','y',0,78],
	98:['n','n'],
	99:['n','n'],
	100:['n','n']
}
print("\n")
print("                                                           Ladders: ")
print("\n")
for key in dict:
	if(dict[key][0]=='y'):
		print("                                             "+str(key)+"  ---------- LADDER ---------->>>  "+str(dict[key][2]))
		print()
print("\n")
print("\n")
print("                                                           Snakes: ")
print("\n")
for key in dict:
	if(dict[key][1]=='y'):
		print("                                             "+str(key)+"  ---------- SNAKE ---------->>>  "+str(dict[key][3]))
		print()
n=int(input("Enter the number of players: "))
b=0
for i in range(n):
	s=str(input("Enter the name of player "+str(i+1)+" "))
	a[i]=[s,0]
def fun(a,dict,n):
	for key in a.copy():
		print(a[key][0],end=" ")
		c=str(input("Roll the dice: "))
		z=random.randrange(1,7,1)
		a[key][1]+=z
		if(a[key][1]<100):
			print(a[key][0]," reached ",a[key][1],end="\n")
			if(dict[a[key][1]][1]=='y'):
				a[key][1]=dict[a[key][1]][3]
				print(a[key][0]," reached ",a[key][1]," by snake",end="\n")
			elif(dict[a[key][1]][0]=='y'):
				a[key][1]=dict[a[key][1]][2]
				print("Woohoo ",a[key][0]," reached ",a[key][1]," by ladder",end="\n")
		elif(a[key][1]==100):
			global k
			print(a[key][0]," reached ",a[key][1],end="\n")
			print("Player ",a[key][0]," has won rank ",k,end="\n")
			k+=1
			a.pop(key)
		else:
			a[key][1]-=z

	if(k!=n+1):
		fun(a,dict,n)
k=1
fun(a,dict,n)

