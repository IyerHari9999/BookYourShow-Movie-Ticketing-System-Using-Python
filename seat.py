import tkinter
from PIL import ImageTk, Image

if __name__!='__main__':
    
    ButtonList=[]
    remainingSeats=1
    selectedSeatList=[]
    rowNumber=0

    def toggle(toggle_btn):
        global remainingSeats
        global selectedSeatList
        global root
        if toggle_btn.config('relief')[-1] == 'sunken':
            toggle_btn.config(relief="raised")
            remainingSeats+=1
            insertRemainingText(root,remainingSeats)
            #remove button from selected list
            for button in selectedSeatList:
                if button==toggle_btn:
                    selectedSeatList.remove(button)
            print(selectedSeatList)
            print("deselected")
            insertAmountText(root)
        else:
            if remainingSeats>0:
                toggle_btn.config(relief="sunken")
                remainingSeats-=1
                insertRemainingText(root,remainingSeats)
                selectedSeatList.append(toggle_btn)
                print(selectedSeatList)
                print("selected")
                insertAmountText(root)

    def insertButton(root):     #frame
        global priceList
        global ButtonList
        global rowNumber
        global basePrice
        for i in range(5):
            if i==0:
                color="#ef79a5"
            elif i==1:
                color="#d65988"
            elif i==2:
                color="#c74475"
            elif i==3:
                color="#b42c60"
            elif i==4:
                color="#9f184b"
            ButtonRow=[]
            for j in range(5):
                ButtonRow.append(tkinter.Button(root,width=6,height=2,text=str(chr(i+65))+str(j+1),font=("Bebas Neue",15),
                                                bg=color
                                                ,command=lambda row=i,column=j:seatSelected(row,column),relief="raised"))
                ButtonRow[-1].place(x=100+j*70,y=130+i*75)
            priceList.append(basePrice+(7-i)*10)
            
            #rowPrice=tkinter.Label(root,text="COST:"+str(priceList[-1]))
            #rowPrice.place(x=420,y=117+i*75)

            ButtonList.append(ButtonRow)
            rowNumber+=10
            #tkinter.Button(root).pack()
    def seatSelected(i,j):
        print(i,j)
        global remainingSeats
        toggle(ButtonList[i][j])

    def insertRemainingText(root,remainingSeats):
        global rowNumber
        textbox = tkinter.Label(root,text=str(remainingSeats),bg="white",fg="#c22560",font=("arial black",16))
        textbox.place(x=503,y=290)

    def submitClicked(root,title,emailID):
        global remainingSeats
        global selectedSeatList
        seatListText=[]
        print("remainig seats= ",remainingSeats)
        if remainingSeats==0:
            ##
            print("Selected Seats= ")
            for seat in selectedSeatList:
                s=seat['text']
                seatListText.append(s)
            print("\nSuccess")
            import paymentWindow
            root.destroy()
            paymentWindow.create(title,selectedSeatList,emailID,seatListText)
            
    def insertSubmitButton(root,title,emailID):
        global rowNumber
        global remainingSeats
        global selectedSeatList

        submitButtton=tkinter.Button(root,text='Submit',width=41,height=1,font=("Bebas Neue",15),bg="#d34178",fg="white",
                                     command=lambda:submitClicked(root,title,emailID))
        submitButtton.place(x=101,y=510)

    def setRemainingText():
        global remainingSeats
        global optionsMenu
        global selectedSeatList
        global root
        print("insdie")

        print(type(optionsMenu))
        maxNumberOfSeats=int(optionsMenu['text'])
        print("Mx= ",maxNumberOfSeats)
        print("selected= ",len(selectedSeatList))
        remainingSeats=maxNumberOfSeats-len(selectedSeatList)
        insertRemainingText(root,remainingSeats)
        #insertAmountText(root)

    def insertOptionsMenu(root):
        options=[int(x) for x in range(1,6)]
        variable=tkinter.StringVar(root)
        variable.set(options[0])
        menu=tkinter.OptionMenu(root,variable,*options,
                                command=lambda a:setRemainingText())
        menu.place(x=480,y=200)
        return menu

    def insertAmountText(root):
        global selectedSeatList
        global costPerTicket
        global tax
        global priceList

        totalCost=0
        for seat in selectedSeatList:
            totalCost=totalCost+priceList[ord(seat['text'][0])-65]
        totalCost=str(totalCost+tax*totalCost)
        print("total Cost= ",totalCost)

        amountText=tkinter.Label(root,width=3,text=totalCost,bg="white",fg="#c22560",font=("arial black",19))
        amountText.place(x=500,y=423)

    basePrice=100
    costPerTicket=200
    tax=0
    optionsMenu=None
    priceList=[]
    
    def create(title,emailID):

        global root
        root = tkinter.Tk()
        root.geometry("700x600+330+50")
        root.title("BookYourShow",)
        root.iconbitmap(default='assets\icon.ico')
        img=Image.open("assets/bg3.jpg")
        photo=ImageTk.PhotoImage(img)
        bg=tkinter.Label(root,image=photo).place(x=-2,y=-2)
        global remainingSeats
        global optionsMenu
        optionsMenu=insertOptionsMenu(root)
        print("here")
        insertRemainingText(root,remainingSeats)
        insertButton(root)
        insertAmountText(root)
        insertSubmitButton(root,title,emailID)
        root.mainloop()
