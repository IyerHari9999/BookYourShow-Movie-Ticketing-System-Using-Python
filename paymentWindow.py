import tkinter
from PIL import ImageTk, Image

if __name__ != '__main__':
    class Payment:
        CVVText = None
        enterCardInfoText = None
        dashTextBox = []

        enterCardNumberText = None
        baitText = None
        enterCVVText = None
        cardNumberText = None
        submitButton = None

        title = ""
        selectedSeatList = []

        emailID = ""

        parentWindow=None
        def __init__(self, root, title, selectedSeatList, emailID):
            self.parentWindow=root
            self.title = title
            self.selectedSeatList = selectedSeatList
            self.emailID = emailID

            self.cardNumberText = tkinter.Entry(root, width=30, font=("", 15))
            self.cardNumberText.place(x=19, y=260)

            # CVV text
            self.CVVText = tkinter.Entry(root, width=6, show="•", font=("arial black", 15))
            self.CVVText.place(x=19, y=330)

            self.submitButton = tkinter.Button(root, text='Submit', width=10, font=("Bebas Neue", 15),
                                               bg="#d34178", fg="white")
            self.submitButton.config(command=lambda: self.retreiveText(root))
            self.submitButton.place(x=380, y=335)

        def retreiveText(self, root):

            cvv = self.CVVText.get()
            no = self.cardNumberText.get()

            if len(cvv) == 3:
                root.destroy()
                import sendMail
                sendMail.sendMsg(self.title, self.selectedSeatList, self.emailID, seatListText)
                import confirmationScreen

                confirmationScreen.create(self.title, self.selectedSeatList)

            else:
                self.invalidText = tkinter.Label(root, font=("calibri bold", 11), bg="#ffd3e4", fg="red",
                                                 text='Please re-check your card number or cvv details')
                self.invalidText.place(x=18, y=365)


    seatListText = ""


    def create(title, selectedSeatList, emailID, seatText):
        global seatListText
        seatListText = seatText

        root = tkinter.Tk()

        root.geometry("500x400+432+150")
        root.title("BookYourShow", )
        root.iconbitmap(default='assets\icon.ico')
        img = Image.open("assets/bg4.jpg")
        photo = ImageTk.PhotoImage(img)
        bg = tkinter.Label(root, image=photo).place(x=-2, y=-2)
        Payment(root, title, selectedSeatList, emailID)
        root.mainloop()


