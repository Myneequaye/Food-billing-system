from tkinter import *
from tkinter import messagebox 
import time
import datetime
import random
import tkinter as tk
import sqlite3

root =Tk()
root.geometry("1350x720+0+0")
root.title("Alicious Food Billing System")
root.configure(background='thistle')

Tops = Frame(root,bg='thistle',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('Lato',35,'bold'),text='Alicious Food Billing System',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='thistle',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='thistle',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='thistle',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='thistle',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='thistle',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='thistle',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='thistle',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='thistle',bd=4,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='thistle',bd=4,relief=RIDGE)
Food_F.pack(side=RIGHT)

conn = sqlite3.connect('foodbilling.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Receipts (id INTEGER PRIMARY KEY, Bill_No TEXT);''') 
###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
Vat = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Sprite = StringVar()
E_Pepsi = StringVar()
E_Guinness = StringVar()
E_ClubBeer = StringVar()
E_Shandy = StringVar()
E_Fanta = StringVar()
E_CocaCola = StringVar()
E_Malt = StringVar()

E_Banku = StringVar()
E_JollofRice = StringVar()
E_FriedRice = StringVar()
E_Waakye = StringVar()
E_Fufu = StringVar()
E_Beans = StringVar()
E_TuoZaafi = StringVar()
E_OmoTuo = StringVar()

E_Sprite.set("0")
E_Pepsi.set("0")
E_Guinness.set("0")
E_ClubBeer.set("0")
E_Shandy.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_Malt.set("0")

E_Banku.set("0")
E_JollofRice.set("0")
E_FriedRice.set("0")
E_Waakye.set("0")
E_Fufu.set("0")
E_Beans.set("0")
E_TuoZaafi.set("0")
E_OmoTuo.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        pass

def Reset():

    Vat.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    # ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_Guinness.set("0")
    E_ClubBeer.set("0")
    E_Shandy.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_Malt.set("0")

    E_Banku.set("0")
    E_JollofRice.set("0")
    E_FriedRice.set("0")
    E_Waakye.set("0")
    E_Fufu.set("0")
    E_Beans.set("0")
    E_TuoZaafi.set("0")
    E_OmoTuo.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtSprite.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtGuinness.configure(state=DISABLED)
    txtClubBeer.configure(state=DISABLED)
    txtShandy.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtMalt.configure(state=DISABLED)
    txtBanku.configure(state=DISABLED)
    txtJollofRice.configure(state=DISABLED)
    txtFriedRice.configure(state=DISABLED)
    txtWaakye.configure(state=DISABLED)
    txtFufu.configure(state=DISABLED)
    txtBeans.configure(state=DISABLED)
    txtTuoZaafi.configure(state=DISABLED)
    txtOmoTuo.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Sprite.get())
    Item2=float(E_Pepsi.get())
    Item3=float(E_Guinness.get())
    Item4=float(E_ClubBeer.get())
    Item5=float(E_Shandy.get())
    Item6=float(E_Fanta.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_Malt.get())

    Item9=float(E_Banku.get())
    Item10=float(E_JollofRice.get())
    Item11=float(E_FriedRice.get())
    Item12=float(E_Waakye.get())
    Item13=float(E_Fufu.get())
    Item14=float(E_Beans.get())
    Item15=float(E_TuoZaafi.get())
    Item16=float(E_OmoTuo.get())

    PriceofDrinks =(Item1 + 0) + (Item2 + 0) + (Item3 + 0) + (Item4 + 0) + (Item5 + 0) + (Item6 + 0) + (Item7 + 0) + (Item8 + 0)

    PriceofFood =(Item9 + 0) + (Item10 + 0) + (Item11 + 0) + (Item12 + 0) + (Item13 + 0) + (Item14 + 0) + (Item15 + 0) + (Item16 + 0)



    DrinksPrice = "GHC",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "GHC",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
#Service charge
    # SC = "GHC",str('%.2f'%(1.59))
    # ServiceCharge.set(SC)

    SubTotalofITEMS = "GHC",str('%.2f'%(PriceofDrinks + PriceofFood + 0))
    SubTotal.set(SubTotalofITEMS)

    Tax = "GHC",str('%.2f'%((PriceofDrinks + PriceofFood) * 0.03))
    Vat.set(Tax)
    Tax = float(Tax[1])
    Tax = round(Tax,2)

    TT=((PriceofDrinks + PriceofFood + 0) )
    TC="GHC",str('%.2f'%(PriceofDrinks + PriceofFood + Tax ))
    TotalCost.set(TC)


def chkSprite():
    if(var1.get() == 1):
        txtSprite.configure(state = NORMAL)
        txtSprite.focus()
        txtSprite.delete('0',END)
        E_Sprite.set("")
    elif(var1.get() == 0):
        txtSprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chkPepsi():
    if(var2.get() == 1):
        txtPepsi.configure(state = NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0',END)
        E_Pepsi.set("")
    elif(var2.get() == 0):
        txtPepsi.configure(state = DISABLED)
        E_Pepsi.set("0")

def chk_Guinness():
    if(var3.get() == 1):
        txtGuinness.configure(state = NORMAL)
        txtGuinness.delete('0',END)
        txtGuinness.focus()
    elif(var3.get() == 0):
        txtGuinness.configure(state = DISABLED)
        E_Guinness.set("0")

def chk_ClubBeer():
    if(var4.get() == 1):
        txtClubBeer.configure(state = NORMAL)
        txtClubBeer.delete('0',END)
        txtClubBeer.focus()
    elif(var4.get() == 0):
        txtClubBeer.configure(state = DISABLED)
        E_ClubBeer.set("0")

def chk_Shandy():
    if(var5.get() == 1):
        txtShandy.configure(state = NORMAL)
        txtShandy.delete('0',END)
        txtShandy.focus()
    elif(var5.get() == 0):
        txtShandy.configure(state = DISABLED)
        E_Shandy.set("0")

def chk_Fanta():
    if(var6.get() == 1):
        txtFanta.configure(state = NORMAL)
        txtFanta.delete('0',END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state = DISABLED)
        E_Fanta.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_Malt():
    if(var8.get() == 1):
        txtMalt.configure(state = NORMAL)
        txtMalt.delete('0',END)
        txtMalt.focus()
    elif(var8.get() == 0):
        txtMalt.configure(state = DISABLED)
        E_Malt.set("0")

def chk_Banku():
    if(var9.get() == 1):
        txtBanku.configure(state = NORMAL)
        txtBanku.delete('0',END)
        txtBanku.focus()
    elif(var9.get() == 0):
        txtBanku.configure(state = DISABLED)
        E_Banku.set("0")

def chk_JollofRice():
    if(var10.get() == 1):
        txtJollofRice.configure(state = NORMAL)
        txtJollofRice.delete('0',END)
        txtJollofRice.focus()
    elif(var10.get() == 0):
        txtJollofRice.configure(state = DISABLED)
        E_JollofRice.set("0")

def chk_FriedRice():
    if(var11.get() == 1):
        txtFriedRice.configure(state = NORMAL)
        txtFriedRice.delete('0',END)
        txtFriedRice.focus()
    elif(var11.get() == 0):
        txtFriedRice.configure(state = DISABLED)
        E_FriedRice.set("0")

def chk_Waakye():
    if(var12.get() == 1):
        txtWaakye.configure(state = NORMAL)
        txtWaakye.delete('0',END)
        txtWaakye.focus()
    elif(var12.get() == 0):
        txtWaakye.configure(state = DISABLED)
        E_Waakye.set("0")

def chk_Fufu():
    if(var13.get() == 1):
        txtFufu.configure(state = NORMAL)
        txtFufu.delete('0',END)
        txtFufu.focus()
    elif(var13.get() == 0):
        txtFufu.configure(state = DISABLED)
        E_Fufu.set("0")

def chk_Beans():
    if(var14.get() == 1):
        txtBeans.configure(state = NORMAL)
        txtBeans.delete('0',END)
        txtBeans.focus()
    elif(var14.get() == 0):
        txtBeans.configure(state = DISABLED)
        E_Beans.set("0")

def chk_TuoZaafi():
    if(var15.get() == 1):
        txtTuoZaafi.configure(state = NORMAL)
        txtTuoZaafi.delete('0',END)
        txtTuoZaafi.focus()
    elif(var15.get() == 0):
        txtTuoZaafi.configure(state = DISABLED)
        E_TuoZaafi.set("0")

def chk_OmoTuo():
    if(var16.get() == 1):
        txtOmoTuo.configure(state = NORMAL)
        txtOmoTuo.delete('0',END)
        txtOmoTuo.focus()
    elif(var16.get() == 0):
        txtOmoTuo.configure(state = DISABLED)
        E_OmoTuo.set("0")

x=random.randint(10908,500876)
def Receipt():
    txtReceipt.delete("1.0",END)
    global x
    randomRef = str(x)
    Receipt_Ref.set("Bill No. "+ randomRef)
        
    txtReceipt.insert(END,'Receipt Ref:\t\t'+Receipt_Ref.get() +'\t\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Sprite:\t\t\t\t\t' + E_Sprite.get() +'\n')
    txtReceipt.insert(END,'Pepsi:\t\t\t\t\t'+ E_Pepsi.get()+'\n')
    txtReceipt.insert(END,'Guinness:\t\t\t\t\t'+ E_Guinness.get()+'\n')
    txtReceipt.insert(END,'Club Beer:\t\t\t\t\t'+ E_ClubBeer.get()+'\n')
    txtReceipt.insert(END,'Shandy:\t\t\t\t\t'+ E_Shandy.get()+'\n')
    txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+ E_Fanta.get()+'\n')
    txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ E_CocaCola.get()+'\n')
    txtReceipt.insert(END,'Malt:\t\t\t\t\t'+ E_Malt.get()+'\n')
    txtReceipt.insert(END,'Banku:\t\t\t\t\t'+ E_Banku.get()+'\n')
    txtReceipt.insert(END,'Jollof Rice:\t\t\t\t\t'+ E_JollofRice.get()+'\n')
    txtReceipt.insert(END,'Fried Rice:\t\t\t\t\t'+ E_FriedRice.get()+'\n')
    txtReceipt.insert(END,'Waakye:\t\t\t\t\t'+ E_Waakye.get()+'\n')
    txtReceipt.insert(END,'Fufu:\t\t\t\t\t'+ E_Fufu.get()+'\n')
    txtReceipt.insert(END,'Beans:\t\t\t\t\t'+ E_Beans.get()+'\n')
    txtReceipt.insert(END,'Tuo Zaafi:\t\t\t\t\t'+ E_TuoZaafi.get()+'\n')
    txtReceipt.insert(END,'Omo Tuo:\t\t\t\t\t'+ E_OmoTuo.get()+'\n')
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t'+ CostofDrinks.get()+'\n')
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSub Total:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'VAT:\t\t\t\t'+ Vat.get()+'\n')
    txtReceipt.insert(END,'Total Cost:\t\t\t\t'+str(TotalCost.get())+'\n')
  
        
 
############################Database###################################################


#########################################Drinks####################################################################
Sprite=Checkbutton(Drinks_F,text='Sprite\t\t\t',variable=var1,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chkSprite).grid(row=0,sticky=W)
Pepsi=Checkbutton(Drinks_F,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chkPepsi).grid(row=1,sticky=W)
Guinness=Checkbutton(Drinks_F,text='Guinness',variable=var3,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chk_Guinness).grid(row=2,sticky=W)
ClubBeer=Checkbutton(Drinks_F,text='Club Beer',variable=var4,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chk_ClubBeer).grid(row=3,sticky=W)
Shandy=Checkbutton(Drinks_F,text='Shandy',variable=var5,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chk_Shandy).grid(row=4,sticky=W)
Fanta=Checkbutton(Drinks_F,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chk_Fanta).grid(row=5,sticky=W)
CocaCola=Checkbutton(Drinks_F,text='Coca Cola',variable=var7,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chk_CocaCola).grid(row=6,sticky=W)
Malt=Checkbutton(Drinks_F,text='Malt',variable=var8,onvalue=1,offvalue=0,font=('Lato',16,'bold'),
                    bg='thistle',command=chk_Malt).grid(row=7,sticky=W)
##############################################Drink Entry###############################################################

txtSprite = Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=0,column=1)

txtPepsi = Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Pepsi)
txtPepsi.grid(row=1,column=1)

txtGuinness = Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Guinness)
txtGuinness.grid(row=2,column=1)

txtClubBeer= Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_ClubBeer)
txtClubBeer.grid(row=3,column=1)

txtShandy = Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Shandy)
txtShandy.grid(row=4,column=1)

txtFanta = Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Fanta)
txtFanta.grid(row=5,column=1)

txtCocaCola = Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtMalt = Entry(Drinks_F,font=('Lato',14,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Malt)
txtMalt.grid(row=7,column=1)
#############################################Foods######################################################################

Banku = Checkbutton(Food_F,text="Banku\t\t\t ",variable=var9,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_Banku).grid(row=0,sticky=W)
JollofRice = Checkbutton(Food_F,text="Jollof Rice",variable=var10,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_JollofRice).grid(row=1,sticky=W)
FriedRice = Checkbutton(Food_F,text="Fried Rice ",variable=var11,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_FriedRice).grid(row=2,sticky=W)
Waakye = Checkbutton(Food_F,text="Waakye ",variable=var12,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_Waakye).grid(row=3,sticky=W)
Fufu = Checkbutton(Food_F,text="Fufu ",variable=var13,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_Fufu).grid(row=4,sticky=W)
Beans = Checkbutton(Food_F,text="Beans ",variable=var14,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_Beans).grid(row=5,sticky=W)
TuoZaafi = Checkbutton(Food_F,text="Tuo Zaafi ",variable=var15,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_TuoZaafi).grid(row=6,sticky=W)
OmoTuo = Checkbutton(Food_F,text="Omo Tuo (Rice Balls) ",variable=var16,onvalue = 1, offvalue=0,
                        font=('Lato',16,'bold'),bg='thistle',command=chk_OmoTuo).grid(row=7,sticky=W)
################################################Entry Box For Cake##########################################################
txtBanku=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Banku)
txtBanku.grid(row=0,column=1)

txtJollofRice=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_JollofRice)
txtJollofRice.grid(row=1,column=1)

txtFriedRice=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_FriedRice)
txtFriedRice.grid(row=2,column=1)

txtWaakye=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Waakye)
txtWaakye.grid(row=3,column=1)

txtFufu=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Fufu)
txtFufu.grid(row=4,column=1)

txtBeans=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Beans)
txtBeans.grid(row=5,column=1)

txtTuoZaafi=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_TuoZaafi)
txtTuoZaafi.grid(row=6,column=1)

txtOmoTuo=Entry(Food_F,font=('Lato',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_OmoTuo)
txtOmoTuo.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofDrinks=Label(Cost_F,font=('Lato',14,'bold'),text='Cost of Drinks\t',bg='thistle',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('Lato',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('Lato',14,'bold'),text='Cost of Foods  ',bg='thistle',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('Lato',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblSubTotal=Label(Cost_F,font=('Lato',14,'bold'),text='Sub Total',bg='thistle',
                fg='black',justify=CENTER)
lblSubTotal.grid(row=2,column=0,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('Lato',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=2,column=1)

############################################################Payment information###################################################

lblVat=Label(Cost_F,font=('Lato',14,'bold'),text='\tVAT (3%)',bg='thistle',bd=7,
                fg='black',justify=CENTER)
lblVat.grid(row=0,column=2,sticky=W)
txtVat=Entry(Cost_F,bg='white',bd=7,font=('Lato',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=Vat)
txtVat.grid(row=0,column=3)

# lblSubTotal=Label(Cost_F,font=('Lato',14,'bold'),text='\tSub Total',bg='thistle',bd=7,
#                 fg='black',justify=CENTER)
# lblSubTotal.grid(row=1,column=2,sticky=W)
# txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('Lato',14,'bold'),
#                         insertwidth=2,justify=RIGHT,textvariable=SubTotal)
# txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('Lato',14,'bold'),text='\tTotal',bg='thistle',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=1,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('Lato',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=1,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('Lato',12,'bold'))
txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='Total',
                        bg='thistle',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='Receipt',
                        bg='thistle',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='Reset',
                        bg='thistle',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='Exit',
                        bg='thistle',command=iExit).grid(row=0,column=3)

###################################Calculator Display################################################################################




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################
txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('Lato',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='7',
                        bg='thistle',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='8',
                        bg='thistle',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='9',
                        bg='thistle',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='+',
                        bg='thistle',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='4',
                        bg='thistle',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='5',
                        bg='thistle',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='6',
                        bg='thistle',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='-',
                        bg='thistle',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='1',
                        bg='thistle',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='2',
                        bg='thistle',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='3',
                        bg='thistle',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='*',
                        bg='thistle',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='0',
                        bg='thistle',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='C',
                        bg='thistle',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='=',
                        bg='thistle',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('Lato',16,'bold'),width=4,text='/',
                        bg='thistle',command=lambda:btnClick('/')).grid(row=5,column=3)


cur.execute('''INSERT OR IGNORE INTO Receipts (Bill_No) 
VALUES (?)''',(x, ))
conn.commit()

root.mainloop()
