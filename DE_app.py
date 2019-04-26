from tkinter import filedialog
from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Differential Expression Analysis Pipeline Application")

pathlabel = Label(root)
pathlabel.place(x=350,y=150)


def browsefunc():
	filename = filedialog.askopenfilenames()
	pathlabel.config(text=filename)

label_0 = Label(root, text = "Please select your sequence reads",width=50,font=("bold", 10))
label_0.place(x=20,y=130)
browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.place(x=350,y=130)

label_1 = Label(root, text="Quality Control",width=50,font=("bold", 10))
label_1.place(x=20,y=180)
var1 = IntVar()
Checkbutton(root, text="fastQC", variable=var1).place(x=350,y=180)
var2 = IntVar()
Checkbutton(root, text="multiQC", variable=var2).place(x=420,y=180)
print(var1.get())
print(var2.get())

label_2 = Label(root, text="Select your reference",width=50,font=("bold", 10))
label_2.place(x=20,y=230)
list1 = ["De Novo Reference Transcriptome","Model Organism Reference Transcriptome"];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=50)
c.set(list1[0]) 
droplist.place(x=350,y=230)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=450)

root.mainloop()