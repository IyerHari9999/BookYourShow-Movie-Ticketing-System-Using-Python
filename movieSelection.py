import tkinter
import movieList
from PIL import ImageTk,Image

class insertPanel:
    #button:movie poster        title           cast
    PosterButton=None
    rootCanvas=None
    Movie=None
    row=0
    TitleText=None
    titleNcastFrame=None
    castText=None
    castButton=None
    titleButton=None
    posterHeight=10
    root=None
    emailID=""
    
    def __init__(self,root,Movie,row,emailID):
        self.emailID=emailID
        self.root=root
        self.Movie=Movie
        self.row=row
        self.setTitle(root)
        self.setCast(root)
        self.setPoster(root)

    def setTitle(self,root):
        if self.row%2==0:
            color="#fd91ba"
            fg="white"
        else:
            color="#ffd3e4"
            fg="#d34178"
        
        name=self.Movie.title
        name=name.upper()
        self.TitleText=tkinter.Label(root,text=name,font=("Bebas Neue",20),
                                         bg=color,fg=fg,)
        self.TitleText.place(x=15,y=50+self.row*90)

    def setCast(self,root):
        if self.row%2==0:
            color="#fd91ba"
        else:
            color="#ffd3e4"
        
        self.cText=tkinter.Label(root,text="CAST :",font=("century gothic bold",10),bg=color,fg="black")
        self.cText.place(x=15,y=50+self.row*90+30)
        self.castText=tkinter.Label(root,text=self.Movie.cast,font=("century gothic bold",10),bg=color,fg="black")
        self.castText.place(x=15,y=60+self.row*90+37)
        
    def setPoster(self,root):
        self.PosterButton=tkinter.Button(root,text="Watch Now",font=("Bebas Neue",14),
                                         bg="#d34178",fg="white",command=lambda:self.nextWindow())
        self.PosterButton.place(x=395,y=70+self.row*90)


    def nextWindow(self):
        import seat
        global Framelist
        self.root.destroy()
        print("Movie= ",self.Movie.title)
        #for ele in Framelist:
         #   ele.rootCanvas.pack_forget()
        seat.create(self.Movie.title,self.emailID)
Framelist = []

def create(emailID):
    row=1
    root=tkinter.Tk()
    root.geometry("500x600+432+50")
    root.title("BookYourShow",)
    root.iconbitmap(default='assets\icon.ico')
    img=Image.open("assets/bg2.jpg")
    photo=ImageTk.PhotoImage(img)
    bg=tkinter.Label(root,image=photo).place(x=-2,y=-2)
    MovieList = movieList.getMovieList()
    global Framelist
    for movie in MovieList:
        Framelist.append(insertPanel(root,movie,row,emailID))
        row+=1
    root.mainloop()
    
if __name__=='__main__':
    pass
