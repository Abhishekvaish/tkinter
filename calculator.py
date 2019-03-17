## making a calculator using python-tkinter
from tkinter import *
from tkinter import messagebox

calculator=Tk()
#calculator.geometry("335x350+150+150")
calculator.title("@bh!$hek_Calculator")
calculator.resizable(width=False,height=False)


def set(number):
	global operands
	operands=operands+str(number)
	text.set(operands)

def clr():
	global operands
	operands=""
	text.set(operands)
def bks():
	global operands
	operands=operands[:len(operands)-1]
	text.set(operands)
def eql():
	global operands
	nop=""
	for i in operands:
		if i=="x":
			nop+="*"
		else:
			nop+=i
	try:
		sum=str(eval(nop))
	except:
		messagebox.showerror("@bh!$hek_Calculator","could not calculate")
	text.set(sum)
	operands=""
	
def buttons(i,r,c):
	Button(calculator,padx=13,pady=13,bd=8,font=("arial",20,"bold"),text=str(i),command=lambda:set(i)).grid(row=r,column=c)

text=StringVar()
operands=""
display=Entry(calculator,font=("arial",20,"bold"),bd=15,bg="light blue",justify="right",textvariable=text)
display.grid(columnspan=4)

buttons	(7,1,0)
buttons(8,1,1)
buttons(9,1,2)
Button(calculator,padx=8,pady=13,bd=8,font=("arial",15,"bold"),bg="red",text="OFF",command=calculator.quit).grid(row=1,column=3)

buttons	(4,2,0)
buttons(5,2,1)
buttons(6,2,2)
Button(calculator,padx=8,pady=13,bd=8,font=("arial",20,"bold"),text="⌫",command=bks).grid(row=2,column=3)

buttons	(1,3,0)
buttons(2,3,1)
buttons(3,3,2)
buttons('+',3,3)


Button(calculator,padx=13,pady=13,bd=8,font=("arial",20,"bold"),text="c",command=clr).grid(row=4,column=0)
buttons(0,4,1)
buttons("-",4,2)
buttons('x',4,3)

buttons("00",5,0)
buttons(".",5,1)
buttons('/',5,2)
Button(calculator,padx=13,pady=13,bd=8,font=("arial",20,"bold"),text="=",command=eql).grid(row=5,column=3)

calculator.mainloop()
