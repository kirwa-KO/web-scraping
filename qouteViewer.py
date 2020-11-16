from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Qoute Viewer")

image_0 = ImageTk.PhotoImage(Image.open("qoutes/image0.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_1 = ImageTk.PhotoImage(Image.open("qoutes/image1.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_2 = ImageTk.PhotoImage(Image.open("qoutes/image2.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_3 = ImageTk.PhotoImage(Image.open("qoutes/image3.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_4 = ImageTk.PhotoImage(Image.open("qoutes/image4.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_5 = ImageTk.PhotoImage(Image.open("qoutes/image5.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_6 = ImageTk.PhotoImage(Image.open("qoutes/image6.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_7 = ImageTk.PhotoImage(Image.open("qoutes/image7.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_8 = ImageTk.PhotoImage(Image.open("qoutes/image8.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_9 = ImageTk.PhotoImage(Image.open("qoutes/image9.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_10 = ImageTk.PhotoImage(Image.open("qoutes/image10.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_11 = ImageTk.PhotoImage(Image.open("qoutes/image11.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_12 = ImageTk.PhotoImage(Image.open("qoutes/image12.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_13 = ImageTk.PhotoImage(Image.open("qoutes/image13.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_14 = ImageTk.PhotoImage(Image.open("qoutes/image14.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_15 = ImageTk.PhotoImage(Image.open("qoutes/image15.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_16 = ImageTk.PhotoImage(Image.open("qoutes/image16.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_17 = ImageTk.PhotoImage(Image.open("qoutes/image17.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_18 = ImageTk.PhotoImage(Image.open("qoutes/image18.jpg").resize((1920, 1080), Image.ANTIALIAS))
image_19 = ImageTk.PhotoImage(Image.open("qoutes/image19.jpg").resize((1920, 1080), Image.ANTIALIAS))


# you need to add images variable to this list
allImages = [ image_0, image_1, image_2, image_3, image_4,
             image_5, image_6, image_7, image_8, image_9,
             image_10, image_11, image_12, image_13, image_14,
             image_15, image_16, image_17, image_18, image_19 ]

# allImages = [ image_0, image_1 ]

myLabelForImg = Label(image=allImages[0])
indexOfImg = 0

myLabelForImg.grid(row=0, column=0, columnspan=3)
nextBtn = Button(root, text=">>", command=lambda: clickNextBtn(indexOfImg + 1))
prevBtn = Button(root, text="<<", command=lambda: clickPrevBtn(indexOfImg - 1))
quitBtn = Button(root, text="Quit..!!", command=root.quit)

statusBar = Label(root, text="Qoute 1 of " + str(len(allImages)), bd=1, relief=SUNKEN, anchor=E)


def	clickNextBtn(number):
	global indexOfImg
	global myLabelForImg
	global nextBtn
	global allImages
	global statusBar
	if number == len(allImages):
		nextBtn = Button(root, text=">>", state=DISABLED)
		return
	myLabelForImg.grid_forget()
	myLabelForImg = Label(image=allImages[number])
	myLabelForImg.grid(row=0, column=0, columnspan=3)
	indexOfImg += 1
	statusBar = Label(root, text="Qoute " + str(number + 1) + " of " + str(len(allImages)), bd=1, relief=SUNKEN, anchor=E)
	statusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)


def	clickPrevBtn(number):
	global indexOfImg
	global myLabelForImg
	global prevBtn
	global allImages
	global statusBar
	if number < 0:
		prevBtn = Button(root, text="<<", state=DISABLED)
		return
	myLabelForImg.grid_forget()
	myLabelForImg = Label(image=allImages[number])
	myLabelForImg.grid(row=0, column=0, columnspan=3)
	indexOfImg -= 1
	statusBar = Label(root, text="Qoute " + str(number + 1) + " of " + str(len(allImages)), bd=1, relief=SUNKEN, anchor=E)
	statusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)



prevBtn.grid(row=1, column=0)
quitBtn.grid(row=1, column=1)
nextBtn.grid(row=1, column=2)
statusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()