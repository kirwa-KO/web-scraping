from tkinter import *

first_number = 0.0

root = Tk()

root.title("Thala Calculate:")

e = Entry(root)

e.grid(row=0, column=0, columnspan=4)

def	numberClicked(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, current + str(number))

def clickAdd():
	global first_number
	first_number = float(e.get())
	e.delete(0, END)
	global math
	math = "+"

def clickSub():
	global first_number
	first_number = float(e.get())
	e.delete(0, END)
	global math
	math = "-"

def clickMul():
	global first_number
	first_number = float(e.get())
	e.delete(0, END)
	global math
	math = "*"

def clickDiv():
	global first_number
	first_number = float(e.get())
	e.delete(0, END)
	global math
	math = "/"

def clearClick():
	e.delete(0, END)

def removeZeroFromFloatIfLeadingZeroAfterDot(number):
    if number % 1 == 0:
        return int(number);
    return number

def equalClicked():
	second_number = float(e.get())
	e.delete(0, END)
	if (math == '+'):
		e.insert(0, removeZeroFromFloatIfLeadingZeroAfterDot(first_number + second_number))
	elif (math == '-'):
		e.insert(0, removeZeroFromFloatIfLeadingZeroAfterDot(first_number - second_number))
	elif (math == '*'):
		e.insert(0, removeZeroFromFloatIfLeadingZeroAfterDot(first_number * second_number))
	else:
		e.insert(0, removeZeroFromFloatIfLeadingZeroAfterDot(first_number / second_number))

# Numberrs Button

button_0 = Button(root, text="0", command=lambda: numberClicked('0'))
button_1 = Button(root, text="1", command=lambda: numberClicked('1'))
button_2 = Button(root, text="2", command=lambda: numberClicked('2'))
button_3 = Button(root, text="3", command=lambda: numberClicked('3'))
button_4 = Button(root, text="4", command=lambda: numberClicked('4'))
button_5 = Button(root, text="5", command=lambda: numberClicked('5'))
button_6 = Button(root, text="6", command=lambda: numberClicked('6'))
button_7 = Button(root, text="7", command=lambda: numberClicked('7'))
button_8 = Button(root, text="8", command=lambda: numberClicked('8'))
button_9 = Button(root, text="9", command=lambda: numberClicked('9'))

# operation buttons

button_add = Button(root, text='+', command=clickAdd)
button_sub = Button(root, text='-', command=clickSub)
button_mul = Button(root, text='*', command=clickMul)
button_div = Button(root, text='/', command=clickDiv)

# buttons for dot, clear and equal

button_dot = Button(root, text='.', command=lambda: numberClicked('.'))
button_equal = Button(root, text='=', command=equalClicked)
button_clear = Button(root, text='CE', command=clearClick)

# place buttons on the screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_0.grid(row=4, column=0, columnspan=2, ipadx=23)
button_dot.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=5, column=0, columnspan=2, ipadx=23)
button_equal.grid(row=5, column=2, columnspan=2, ipadx=23)

root.mainloop()