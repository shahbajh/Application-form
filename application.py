from tkinter import *

root = Tk()
root.geometry('600x600')
root.title("APPLICAION FORM")

class_0 = Label(root, text="ALGO FORM",width=20,font=("bold", 20))
class_0.place(x=90,y=53)


class_1 = Label(root, text="FullName",width=20,font=("bold", 10))
class_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

class_2 = Label(root, text="Email",width=20,font=("bold", 10))
class_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

class_3 = Label(root, text="MOBILE NO.",width=20,font=("bold", 10))
class_3.place(x=70,y=230)

entry_3 = Entry(root)
entry_3.place(x=240,y=230)



class_4 = Label(root, text="DATE OF BIRTH",width=20,font=("bold", 10))
class_4.place(x=70,y=280)


list1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=5)
c.set('date')
droplist.place(x=240,y=280)

list2 = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'];
c=StringVar()
droplist=OptionMenu(root,c, *list2)
droplist.config(width=5)
c.set('month')
droplist.place(x=300,y=280)


list3 = ['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'];
c=StringVar()
droplist=OptionMenu(root,c, *list3)
droplist.config(width=5)
c.set('year')
droplist.place(x=360,y=280)

Button(root, text='Submit',width=20,bg='GREEN',fg='WHITE').place(x=180,y=380)

root.mainloop()