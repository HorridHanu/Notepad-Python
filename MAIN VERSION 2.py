

########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # NOTEPAD COPY MAIN!                ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################



          #Define Functions For Cammand!


def fun():
    print("yes work! \n"
        "PLEASE CHECK NEXT VERSION ON  ->Github.com/HorridHanu<- .")

    # Define function for Files!
    # Define function for Newfile!
import os.path
import os
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


    # function for openfile!
from tkinter.filedialog import askopenfilename, asksaveasfilename
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                               ("Text Documents",
                                                               " *.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f= open(file, "r")
        text.insert(1.0, f.read())
        f.close()


    # function for savefile!
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',
                                 filetypes=[("All Files", ".txt"),
                                           ("Text Documents", ".txt")])
        if file =="":
            file =None
        else:
            #save the file!
            root.title(os.path.basename(file) + " - Notepad")
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            # print("file save")


    else:
        # save the file!
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()



    # Define function for Edits!
    # function for cut!
def cut():
    text.event_generate(("<<Cut>>"))


    # function for copy!
def copy():
    text.event_generate(("<<Copy>>"))


    # function for paste!
def paste():
    text.event_generate(("<<Paste>>"))


    # function for delete!
def delete():
    text.delete(1.0, END)



    # Define functions for ABOUT!
    # import the message box as tmsg
import tkinter.messagebox as tmsg


    # function for help!
def help():
    # print("I will help you!")
    # showinfo help to show a messsage !
    tmsg.showinfo("Help", "Tell Us Whats happen?\nContact Us On ->Github.com/HorridHanu<-")
    # print(a) return value (ok)


    # function for rate!
def rate():
    # askquestion help to to ask question in yes or no
    a= tmsg.askquestion("Rate us!", " Was Your Experince Good?")
    # print(a) return value is yes no or!
    if a == 'yes':
        msg = "Thanks Sir Please Rate Us On Appstore!"
    else:
        msg = "Tell Us Whats happen?\nContact Us On ->Github.com/HorridHanu<-"
    tmsg.showinfo("Experince..", msg)


    # function for joining!
def join_us():
    ans = tmsg.askquestion("Join", "Would You Join Us On Github")
    # print(ans)
    if ans =="no":
        msg = "Without Joining You Cann't Get Next Update!"
    else:
        msg ="Go To ->Github.com/HorridHanu<- \n For More Update And Versions...."
    tmsg.showwarning("Warning", msg)


    # define function for about!
def about():
    tmsg.showerror("About", "Notepad By Hanu.. \nVersion 2.0.."
                            "\nCopy Right 2021 Hanu Corporation. "
                            "All Right Reserved!"
                            " For All OS {Windows}, {Linux}, {MacOS}"
                            " User Interface Are Protected By Trademark"
                            " And Other Pendings"
                            " Or Existing Intellecutal Property Right In "
                            " United State And Other Countries.")





    #BASIC TKINTER SETUP!
from tkinter import *
root=Tk()
root.geometry("700x390")
root.title("Untitled - Notpad")
root.bell()              #used to bell on opening!
# root.iconphoto("1.ICON.png")





    # STATUS BAR!
statusbar = StringVar()
statusbar.set(" Be Happy....")
sbar = Label(root, textvariable=statusbar, relief=SUNKEN, anchor="w").pack(fill=X, side=BOTTOM)

    # DEFINE FUNCTION FOR STATUS BAR!
def status_bar():
    statusbar.set(" Font Lucida, Size 19 And You Are Working Be Happy.....")


    # define function for font!
def font():
    statusbar.set(" Font Is Lucida And Size Is 17......")

    # define function for time!
    # IMPORT Datetime MODULE!
from datetime import datetime
now = datetime.now()
Time = now.strftime("%H:%M")
Date = now.strftime("%D")

def time_now():
    statusbar.set(f"{Time}  {Date}")




    # SCROLLBAR AND TEXT AREA!
    # scrollbar using Scroll widget!
sb = Scrollbar(root)
sb.pack(fill=Y, side=RIGHT)

    # Text area using text widget and connect with scroll bar!
text = Text(root, font="lucida 17", yscrollcommand=sb.set)
# for taking the full geometry
text.pack(fill=BOTH, expand=True)
file = None
sb.config(command=text.yview)



    #Main Menu!
mainmenu=Menu(root)


    # Submenu File!
m1 = Menu(mainmenu, tearoff=0)
m1.add_separator()
# to new file
m1.add_command(label="New            Ctrl+N", command=newfile)
# m1.add_separator()
# to open existing file
m1.add_command(label="Open..        Ctrl+O", command=openfile)
# m1.add_separator()
# to save current file
m1.add_command(label="save            Ctrl+s", command=savefile)
m1.add_separator()
# to print
m1.add_command(label="Print           Ctrl+P", command=fun)
# to Exit!
m1.add_separator()
m1.add_command(label="Exit", command=exit)      #exit has pre-function to exit!
mainmenu.add_cascade(label="File", menu=m1)
# file menu END


          #Submenu Edit!
m2 = Menu(mainmenu, tearoff = 0)
m2.add_separator()
# to cut
m2.add_command(label="Cut               Ctrl+X", command=cut)
# to copy
m2.add_command(label="Copy            Ctrl+C", command=copy)
# to paste
m2.add_command(label="Paste            Ctrl+V", command=paste)
m2.add_separator()
# to delete
m2.add_command(label="Delete               Del", command=delete)
m2.add_separator()
m2.add_command(label="Select          Ctrl+A",command=fun)
# to time
m2.add_command(label="Time/Date         F5",command=time_now)
mainmenu.add_cascade(label="Edit", menu=m2)
# edit menu END


          #Submenu Format
m3 = Menu(mainmenu, tearoff = 0)
m3.add_separator()
m3.add_command(label="WordWrap", command=fun)
# to font
m3.add_command(label="font..", command=font)
mainmenu.add_cascade(label="Format", menu=m3)


          #Submenu Veiw
m4 = Menu(mainmenu, tearoff=0)
m4.add_separator()
# to view statusbar
m4.add_command(label="Status Bar", command=status_bar)
mainmenu.add_cascade(label="View", menu=m4)


          #Submenu View Help
m5=Menu(mainmenu, tearoff = 0)
m5.add_separator()
# to view help
m5.add_command(label="View Help", command=help)
m5.add_separator()
# m5.add_separator()
# m5.add_separator()
# to rate
m5.add_command(label="Rate us!", command=rate)
# m5.add_separator()
# to join
m5.add_command(label="Join us!", command=join_us)
m5.add_separator()
m5.add_separator()
# about
m5.add_command(label="About Notepad", command=about)
mainmenu.add_cascade(label="Help", menu=m5)
# View help menu END

root.config(menu=mainmenu)    #configure the mainmenu as menu


root.mainloop()
########################################################################################
########################################################################################