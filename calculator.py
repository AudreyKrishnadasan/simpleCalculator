from tkinter import*

root = Tk()
root.title("Simple Calculator")


e = Entry(root,width=35, borderwidth =5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter your name:") #default text in the box

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	global num1
	global math
	math = "addition"
	num1 = int(e.get())
	e.delete(0, END)

def button_equal():
	numNext = int(e.get())
	e.delete(0, END)

	if math == "addition":
		e.insert(0, num1 + numNext)

	if math == "subtraction":
		e.insert(0, num1 - numNext)

	if math == "multiplication":
		e.insert(0, num1 * numNext)

	if math == "division":
		e.insert(0, num1 / numNext)


def button_subtract():
	global num1
	global math
	math = "subtraction"
	num1 = int(e.get())
	e.delete(0, END)

def button_multiply():
	global num1
	global math
	math = "multiplication"
	num1 = int(e.get())
	e.delete(0, END)

def button_divide():
	global num1
	global math
	math = "division"
	num1 = int(e.get())
	e.delete(0, END)


button1 = Button(root,text="1", padx=40, pady=20,command= lambda: button_click(1))
button2 = Button(root,text="2", padx=40, pady=20,command= lambda: button_click(2))
button3 = Button(root,text="3", padx=40, pady=20,command= lambda: button_click(3))
button4 = Button(root,text="4", padx=40, pady=20,command= lambda: button_click(4))
button5 = Button(root,text="5", padx=40, pady=20,command= lambda: button_click(5))
button6 = Button(root,text="6", padx=40, pady=20,command= lambda: button_click(6))
button7 = Button(root,text="7", padx=40, pady=20,command= lambda: button_click(7))
button8 = Button(root,text="8", padx=40, pady=20,command= lambda: button_click(8))
button9 = Button(root,text="9", padx=40, pady=20,command= lambda: button_click(9))
button0 = Button(root,text="0", padx=40, pady=20,command= lambda: button_click(0))

buttonClear = Button(root,text="clear", padx=91, pady=20,command= button_clear)
buttonAdd = Button(root,text="+", padx=39, pady=20,command= button_add)
buttonEqual = Button(root,text="=", padx=101, pady=20,command= button_equal)

buttonSubtract = Button(root,text="-", padx=40, pady=20,command= button_subtract)
buttonMultiply = Button(root,text="*", padx=42, pady=20,command= button_multiply)
buttonDivide = Button(root,text="/", padx=42, pady=20,command= button_divide)

#put buttons on screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1,columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1,columnspan=2)

buttonSubtract.grid(row=6, column = 0)
buttonMultiply.grid(row=6, column = 1)
buttonDivide.grid(row=6, column = 2)



#fg= foreground/text color
#bg = background color 

root.mainloop()