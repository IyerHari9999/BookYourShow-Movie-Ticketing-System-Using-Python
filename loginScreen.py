import tkinter
from PIL import ImageTk, Image

class LoginScreen:
    Frame=None
    UsernameTextBox=None
    PasswordTextBox=None
    SubmitButton=None
    ButtonHeight=1
    ButtonWidth=50
    TextBoxHeight=1
    TextBoxWidth=19
    Font=("berlin sans fb",17)
    root=None
    invalidText=None
    emailID=""
    def __init__(self,root):
        
        self.UsernameTextBox=tkinter.Text(root,width=self.TextBoxWidth,height=self.TextBoxHeight,font=self.Font)
        self.PasswordTextBox = tkinter.Entry(root,show="•",width=19,font=self.Font)
        self.invalidText=tkinter.Text()
        self.UsernameTextBox.place(x=200,y=244)
        self.PasswordTextBox.place(x=200,y=287)

        self.SubmitButton=tkinter.Button(root,text='Submit',width=self.ButtonWidth,height=self.ButtonHeight,font=("Bebas Neue",15),
                                         bg="#d34178",fg="white",command=lambda:self.__credentailValidator(root))
        self.SubmitButton.place(x=45,y=350)

    #check for credentials: next screen if corect else invalid. called when submit clicked
    def __credentailValidator(self,root):
        correctUsername='hariharanr1000@gmail.com'
        correctPass='12345'

        inputUsername = self.UsernameTextBox.get("1.0", tkinter.END).strip()
        inputPass = self.PasswordTextBox.get().strip()

        self.invalidText.pack_forget()

        print("ipUsr=",inputUsername)
        print("ipPass=",inputPass)
        if correctUsername==inputUsername and correctPass==inputPass:
            print("Success")
            self.__validCredentails(root)
        else:
            print("Fail")
            self.__invalidCredentials()

    def __invalidCredentials(self):
        self.invalidText=tkinter.Label(root,font=("calibri bold",11),bg="#ffd3e4",fg="red",
                                       text='You have entered invalid username or password, please try again')
        self.invalidText.place(x=45,y=324)

    def __validCredentails(self,root):
        root.destroy()
        self.emailID='hariharanr1000@gmail.com'
        import movieSelection
        canvas=movieSelection.create(self.emailID)

    #def CreateNewAcc(self):

root=tkinter.Tk()

root.geometry("500x400+432+150")
root.title("BookYourShow",)
root.iconbitmap(default='assets\icon.ico')
img=Image.open("assets/bg1.jpg")
photo=ImageTk.PhotoImage(img)
bg=tkinter.Label(root,image=photo).place(x=-2,y=-2)
screen=LoginScreen(root)
root.mainloop()
