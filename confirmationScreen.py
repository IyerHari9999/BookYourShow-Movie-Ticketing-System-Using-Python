import tkinter
from PIL import ImageTk, Image
if True:
    class ConfirmationScreen:
        rootCanvas=None
        successText=None
        successString=""
        mailText=None
        mailString=""
        finishButton=None
        title=""
        selectedSeatList=""
        def __init__(self,root,title,selectedSeatList):    #canvas
            self.title=title
            self.selectedSeatList=selectedSeatList
            self.finishButton=tkinter.Button(root,width=49,height=1,font=("Bebas Neue",15),bg="#d34178",fg="white",
                                             command=lambda:self.finishclicked(root),text="Finish")
            self.finishButton.place(x=50,y=335)

        def finishclicked(self,root):
            root.destroy()

    def create(title,selectedSeatList):
        print("confirmition screen")
        print('seats= ')
        print(type(selectedSeatList[0]))
        #for ele in selectedSeatList:
         #   print(ele['text'],end=" ")
        root=tkinter.Tk()
        root.geometry("500x400+432+150")
        root.title("BookYourShow",)
        root.iconbitmap(default='assets\icon.ico')
        img=Image.open("assets/bg5.jpg")
        photo=ImageTk.PhotoImage(img)
        bg=tkinter.Label(root,image=photo).place(x=-2,y=-2)
        ConfirmationScreen(root,title,selectedSeatList)
        root.mainloop()
