

########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # MESSAGE BOXES!                    ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################


             #IMPORT MESSAGE BOX!
import tkinter.messagebox as tmsg


             #Define Functions For Cammand!


             # FOR JOINNING
def join_us():
    ans = tmsg.askquestion("Join", "Would You Join Us On Github")                                           # FOR ASK QUESTION  USING tmsg.askquestion
    # print(a) return value is yes no or!
    if ans =="no":
        msg = "Without Joining You Cann't Get Next Update!"
    else:
        msg ="Go To ->Github.com/HorridHanu<- \n For More Update And Versions...."
    tmsg.showwarning("Warning",msg)                                                                          # for showing warning use tmsg.showwarning


def help():
    # print("I will help you!")
    # showinfo help to show a messsage !
    a= tmsg.showinfo("Help", "Tell Us Whats happen?\nContact Us On ->Github.com/HorridHanu<-")               # for showing INFO use tmsg.showinfo
    # print(a), return value (ok)

def rate():
    # askquestion help to to ask question in yes or no
    a= tmsg.askquestion("Rate us!", " Was Your Experince Good?")                                             # FOR ASK QUESTION  USING tmsg.askquestion
    # print(a) return value is yes no or!
    if a == 'yes':
        msg = "Thanks Sir Please Rate Us On Appstore!"
    else:
        msg= "Tell Us Whats happen?\nContact Us On ->Github.com/HorridHanu<-"
    tmsg.showinfo("Experince..", msg)

def about():
    tmsg.showerror("About", "Hanu Notepad\nVersion 2.0"                                                      
                            "\nCopy Right 2021 Hanu Corporation. "
                            "All Right Reserved!"
                            " For All OS {Windows}, {Linux}, {MacOS}"
                            " User Interface Are Protected By Trademark"
                            " And Other Pendings"
                            " Or Existing Intellecutal Property Right In "
                            " United State And Other Countries.")

          #IMPORT TKINTER MODULE!
from tkinter import *
root=Tk()
root.geometry("700x300")
root.title("Message_Box")
root.bell()                                                                                                  #used to bell on openin


          #Main Menu!
mainmenu=Menu(root)



          #Submenu {VEIW HELP}
m5=Menu(mainmenu,tearoff = 0)
m5.add_command(label="View Help", command=help)
m5.add_separator()
# m5.add_separator()
# m5.add_separator()
m5.add_command(label="Rate us!", command=rate)
# m5.add_separator()
m5.add_command(label="Join us!", command=join_us)
m5.add_separator()
m5.add_separator()
m5.add_command(label="About Notepad", command=about)


mainmenu.add_cascade(label="Help", menu=m5)


root.config(menu=mainmenu)


root.mainloop()
########################################################################################
########################################################################################