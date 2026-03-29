from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("GUVI Notepad")
    file=None
    textArea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file=="":
            file=None
        else:
            # Save as a new file
            f = open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) +" - Notepad")
            print("File Saved")

    else:
        # Save the file
        f=open(file,"w")
        f.write(textArea.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by GUVI")

if __name__ =="__main__":
    root=Tk()
    
    root.title("GUVI Notepad")
    root.geometry("600x854")

# Adding TextArea 
textArea=Text(root,bg="white",font="lucida 13")
file=None
textArea.pack(expand=True,fill=BOTH)

# Creating Menu bar
MenuBar= Menu(root)

# File Menu Starts
FileMenu= Menu(MenuBar,tearoff=0)

# To open new file
FileMenu.add_command(label="New",command=newfile)

# To open already existing file
FileMenu.add_command(label="Open",command=openfile)

# To save the current file
FileMenu.add_command(label="Save",command=savefile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quitApp)
MenuBar.add_cascade(label="File",menu=FileMenu)
# File Menu ends



# Edit Menu Starts

EditMenu = Menu(MenuBar, tearoff=0)

# To give a feature of cut, copy and paste
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)

MenuBar.add_cascade(label="Edit",menu=EditMenu)

# Help Menu Starts
HelpMenu= Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label="About Notepad",command=about)
MenuBar.add_cascade(label="Help",menu=HelpMenu)

# Help Menu Ends
root.config(menu=MenuBar)

# Adding Scrollbar
Scroll=Scrollbar(textArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=Scroll.set)


root.mainloop()


# Completed.
