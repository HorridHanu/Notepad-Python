

########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # MAKING THE SCREEN OF NOTEPAD!     ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################



          #Define Datetime Funuction!

from datetime import datetime
now=datetime.now()
Time=now.strftime("%H:%M")
Date=now.strftime("%D")
def time_now():
    print(f"{Time}  {Date}")


          #Define Function For Cammand!

def fun():
    print("yes work! \n"
        "PLEASE CHECK NEXT VERSION ON  ->Github.com/HorridHanu<- .")


from tkinter import *
root=Tk()
root.geometry("700x400")
root.title("Untitled-Notpad")
root.bell()                  #used to bell on openin



          #Main Menu!
mainmenu=Menu(root)


          # Submenu File!
m1=Menu(mainmenu ,tearoff = 0)
m1.add_command(label="New            Ctrl+N", command=fun)
m1.add_command(label="Open..        Ctrl+O", command=fun)
m1.add_command(label="save            Ctrl+s", command=fun)
m1.add_command(label="Save as", command=fun)
m1.add_separator()
m1.add_command(label="Page setup", command=fun)
m1.add_command(label="Print           Ctrl+P", command=fun)
m1.add_separator()
m1.add_command(label="Exit", command=exit)        #exit has pre-function to exit!
mainmenu.add_cascade(label="File", menu=m1)


          #Submenu Edit!
m2 = Menu(mainmenu ,tearoff = 0)
m2.add_command(label="Undo            Ctrl+Z", command=fun)
m2.add_separator()
m2.add_command(label="Cut               Ctrl+X", command=fun)
m2.add_command(label="Copy            Ctrl+C", command=fun)
m2.add_command(label="Paste            Ctrl+V", command=fun)
m2.add_command(label="Delete               Del", command=fun)
m2.add_separator()
m2.add_command(label="Find             Ctrl+F", command=fun)
m2.add_command(label="Find Next            F3", command=fun)
m2.add_command(label="Replace        Ctrl+H", command=fun)
m2.add_command(label="Go To           Ctrl+G", command=fun)
m2.add_separator()
m2.add_command(label="Select          Ctrl+A",command=fun)
m2.add_command(label="Time/Date         F5",command=time_now)
mainmenu.add_cascade(label="Edit", menu=m2)


          #Submenu Format
m3 = Menu(mainmenu ,tearoff = 0)
m3.add_command(label="WordWrap", command=fun)
m3.add_command(label="font..", command=fun)
mainmenu.add_cascade(label="Format", menu=m3)


          #Submenu Veiw
m4 =Menu(mainmenu ,tearoff = 0)
m4.add_command(label="Status Bar", command=fun)
mainmenu.add_cascade(label="View", menu=m4)


          #Submenu View Help
m5=Menu(mainmenu ,tearoff = 0)
m5.add_command(label="View Help", command=fun)
m5.add_separator()
m5.add_command(label="About Notepad", command=fun)
mainmenu.add_cascade(label="Help", menu=m5)


root.config(menu=mainmenu)


root.mainloop()
########################################################################################
########################################################################################