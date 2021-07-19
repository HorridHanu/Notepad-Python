




######################################################################################################################################
######################################################################################################################################
## # CODE LANGUAGE IS PYHTON!                                                        ##      ##                                     ##
## # DATE: 18-JULY-2021                                                              ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                                                                   ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!                                                   ##########    #######   ##     ##   ##     ##  ##
## # NOTEPAD COPY MAIN!                                                              ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                                                                  ##      ##    #######   ##     ##   #########  ##
######################################################################################################################################
######################################################################################################################################





    # Basic import statement
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font, colorchooser
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


    # Basic setup
root = Tk()
root.geometry("700x500")
root.title("Untitled - Notepad")



    # Main Menu!
mainmenu=Menu(root)

    # icons of file Menu
new_icon = tkinter.PhotoImage(file='icon/new.png')
open_icon = tkinter.PhotoImage(file='icon/open.png')
save_icon = tkinter.PhotoImage(file='icon/save.png')
save_as_icon = tkinter.PhotoImage(file='icon/save as.png')
exit_icon = tkinter.PhotoImage(file='icon/exit.png')


    # define function for file menu


    # For new file!
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


    # To open file
def openfile():
    global file
    file = askopenfilename(defaultextension="*.txt", filetypes=[("All Files", "*.*"),
                                                                ("Text Doucments", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()


    # To save file
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt"
                             , filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()


    # To save_as the file
def save_as():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()




text_url = " "
def Exit(event = None):
    global text_change
    global text_url
    try:
        if text_change:
            mbox = tmsg.askyesnocancel("Warning","Do you want to save Untitled File" )
            if mbox is True:
                if text_url:
                    content = text.get(1.0, END)
                    with open(text_url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        root.destroy()
                else:
                    content2 = str(text.get(1.0, END))
                    text_url = asksaveasfilename(mode="w", defaultextension=".txt",
                                 filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
                    text_url.write(content2)
                    text_url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return


    # Submenu of file!
m1 = Menu(mainmenu, tearoff=0)
m1.add_separator()

    # to new file!
m1.add_command(label="New", image=new_icon, compound=tkinter.LEFT, accelerator="ctrl+N", command=newfile)

    # to open existing file!
m1.add_command(label="Open...", image=open_icon, compound=tkinter.LEFT, accelerator="ctrl+O", command=openfile)

    # to save current file!
m1.add_separator()
m1.add_command(label="Save", image=save_icon, compound=tkinter.LEFT, accelerator="ctrl+S", command=savefile)

    # to save as!
m1.add_command(label="Save as...", image=save_as_icon, compound=tkinter.LEFT, command=save_as)
m1.add_separator()

    # to Exit!
m1.add_command(label="Exit", image=exit_icon, compound=tkinter.LEFT, command=Exit)      #exit has pre-function to exit!

mainmenu.add_cascade(label="File", menu=m1)




    # Submenu of edit


    # Icons of edit menu

cut_icon = tkinter.PhotoImage(file='icon/cut.png')
copy_icon = tkinter.PhotoImage(file='icon/copy.png')
paste_icon = tkinter.PhotoImage(file='icon/paste.png')
del_icon = tkinter.PhotoImage(file='icon/delete.png')
find_icon = tkinter.PhotoImage(file='icon/find.png')


    #Functions for Edit!


    # To cut the text
def cut():
    text.event_generate("<<Cut>>")


    # To copy the text
def copy():
    text.event_generate("<<Copy>>")


    # To paste the copied text
def paste():
    text.event_generate("<<Paste>>")


    # To delete the text
def delete():
    text.delete(1.0, END)


    # To find the text
def find():


    #define function for find


    def find_fun(event=None):
        word = find_input.get()
        text.tag_remove("match", "1.0", END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text.search(word, start_pos, stopindex=tkinter.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text.tag_config('match', foreground='red', background='yellow')


    #define function for replace


    def replace_fun():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text.get(1.0, END)
        new_content = content.replace(word, replace_text)
        text.delete(1.0, END)
        text.insert(1.0, new_content)



    # Basic setup for find window
    findpop = Tk()
    findpop.geometry("300x130")
    findpop.resizable(0, 0)
    findpop.title("Find Word..")
    findpop.config(bg="white")


    #frame
    find_frame = ttk.Label(findpop)


    #Label
    text_find = ttk.Label(find_frame, text="Find:")
    text_replace = ttk.Label(find_frame, text="Replace:")


    #Entry
    find_input = Entry(find_frame, width=30, fg="Grey", bg="black")
    replace_input = Entry(find_frame, width=30, fg="Grey", bg="black")


    #Button
    find_button = ttk.Button(find_frame, text="Find",command=find_fun)
    replace_button = ttk.Button(find_frame, text="Replace", command=replace_fun)


    #Grid Frame
    find_frame.pack(pady=20, side=TOP)


    #Grid Label
    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)


    #Grid Entry
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)


    #Grid Button
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    findpop.mainloop()


    # Submenu of edit
m2 = Menu(mainmenu, tearoff=0)
m2.add_separator()

    # to cut
m2.add_command(label="Cut", image=cut_icon, compound=tkinter.LEFT, accelerator="ctrl+X", command=cut)

    # to copy
m2.add_command(label="Copy", image=copy_icon, compound=tkinter.LEFT, accelerator="ctrl+C", command=copy)

    # to paste
m2.add_command(label="Paste", image=paste_icon, compound=tkinter.LEFT, accelerator="ctrl+V", command=paste)
m2.add_separator()

    # to delete
m2.add_command(label="Delete", image=del_icon, compound=tkinter.LEFT, command=delete)
m2.add_separator()

    # to find
m2.add_command(label="Find", image=find_icon, compound=tkinter.LEFT, accelerator="ctrl+F", command=find)

mainmenu.add_cascade(label="Edit", menu=m2)



    # Submenu of veiw


    # Icons for View

tool_bar_icon = tkinter.PhotoImage(file="icon/toolbar.png")
status_bar_icon = tkinter.PhotoImage(file="icon/status.png")



    #Status_bar
statusbar = ttk.Label(text="Be Happy....")
statusbar.pack(side=BOTTOM, fill=X, padx=10)
text_change = False

    # initailiizng the value
    # for statusbar
show_statusbar = tkinter.BooleanVar()
show_statusbar.set(True)

    # for toolbar
show_toolbar = tkinter.BooleanVar()
show_toolbar.set(True)


    # define function for hide toolbar
def hide_tool_bar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar = False
    else:
        text.pack_forget()
        statusbar.pack_forget()
        tool_bar_label.pack(side=TOP, fill=X)
        text.pack(expand=True, fill=BOTH, padx=4, pady=4)
        statusbar.pack(side=BOTTOM, fill=X, padx=10)
        show_toolbar = True


    # define function for hide statusbar
def hide_status_bar():
    global show_statusbar
    if show_statusbar:
        statusbar.pack_forget()
        show_statusbar = False
    else:
        statusbar.pack(side=BOTTOM, fill=X, padx=10)
        show_statusbar = True


m3 = Menu(mainmenu, tearoff=0)
m3.add_separator()

    # to view toolbar
m3.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0, image=tool_bar_icon, compound=tkinter.LEFT, command=hide_tool_bar)
mainmenu.add_cascade(label="View", menu=m3)

    # to view statusbar
m3.add_separator()
m3.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0, image=tool_bar_icon, compound=tkinter.LEFT, command=hide_status_bar)




    # Submenu Theme

    # Icons for Theme


default_icon = tkinter.PhotoImage(file='icon/default.png')
light_icon = tkinter.PhotoImage(file='icon/light.png')
dark_icon = tkinter.PhotoImage(file='icon/dark.png')
red_icon = tkinter.PhotoImage(file='icon/red.png')
nightblue_icon = tkinter.PhotoImage(file='icon/night blue.png')
monokai_icon = tkinter.PhotoImage(file='icon/monokai.png')



    # Define function for Theme


    # for default theme
def default():
    global text
    text.config(fg='#000000', bg='#ffffff')


    # for light theme
def light():
    global text
    text.config(fg='#474747', bg='#e0e0e0')


    # for dark theme
def dark():
    global text
    text.config(fg='#c4c4c4', bg='#2d2d2d')


    # for red theme
def red():
    global text
    text.config(fg='#2d2d2d', bg='#ffe8e8')


    # for night blue theme
def night_blue():
    global text
    text.config(fg='#ededed', bg='#6b9dc2')


    # for monokai theme
def monokai():
    global text
    text.config(fg='#d3b774', bg='#6b9dc2')

m4 = Menu(mainmenu, tearoff=0)
m4.add_separator()

    # To default theme

m4.add_command(label="Default", compound=tkinter.LEFT, image=default_icon, command=default)
m4.add_separator()

    # To light theme
m4.add_command(label="Light", compound=tkinter.LEFT, image=light_icon, command=light)

    # To dark theme
m4.add_command(label="Dark", compound=tkinter.LEFT, image=dark_icon, command=dark)
m4.add_separator()

    # To red theme
m4.add_command(label="Red", compound=tkinter.LEFT, image=red_icon, command=red)

    # To night blue Theme
m4.add_command(label="Night Blue", compound=tkinter.LEFT, image=nightblue_icon,command=night_blue)

    # To monokai theme
m4.add_command(label="Monokai", compound=tkinter.LEFT, image=monokai_icon, command=monokai)

mainmenu.add_cascade(label="Theme", menu=m4)




    # Submenu View Help

    #icons for help

help_icon = PhotoImage(file='icon/help.png')
rate_icon = PhotoImage(file='icon/rate.png')
join_icon = PhotoImage(file='icon/join.png')
about_icon = PhotoImage(file='icon/about.png')


    # function for help
def help():
    # showwaring help to show a messsage !
    tmsg.showwarning("Help...", "Tell Us Whats happen? \nContact Us On ->Github.com/HorridHanu<-"
                          "\n or +1(204) 514 4737")




    # function for rate!
def rate():
    # askquestion help to to ask question in yes or no
    a= tmsg.askquestion("Rate us...", " Was Your Experince Good?")
    # print(a) return value is yes no or!
    if a == 'yes':
        msg = "Thanks Please Rate Us On Appstore!"
    else:
        msg = "Tell Us Whats happen?\nContact Us On ->Github.com/HorridHanu<-" \
              "\n or +1(204) 514 4737"
    tmsg.showerror("Experince...", msg)



    # function for joining!
def join_us():
    ans = tmsg.askquestion("Join...", "Would You Join Us On Github")
    # print(ans)
    if ans =="no":
        msg = "Without Joining You Can't Get Next Update!"
    else:
        msg ="Go To ->Github.com/HorridHanu<- \n For More Update And Versions...."
    tmsg.showwarning("Warning...", msg)



    # define function for about!
def about():
    # statusbar.set("About")
    tmsg.showerror("About...", "Notepad By Hanu.. \nVersion 3.0.."
                            "\nCopy Right 2021 Hanu Corporation. "
                            "All Right Reserved!"
                            " For All OS {Windows}, {Linux}, {MacOS}"
                            " User Interface Are Protected By Trademark"
                            " And Other Pendings"
                            " Or Existing Intellecutal Property Right In "
                            " United State And Other Countries.")


    # submenu Help
m5 = Menu(mainmenu, tearoff=0)
m5.add_separator()

    # to view help
m5.add_command(label="View Help", command=help, image=help_icon, compound=tkinter.LEFT)
m5.add_separator()

    # to rate
m5.add_command(label="Rate us!", command=rate, image=rate_icon, compound=tkinter.LEFT)

    # to join
m5.add_command(label="Join us!", command=join_us, image=join_icon, compound=tkinter.LEFT)
m5.add_separator()

    # about
m5.add_command(label="About Notepad", command=about, image=about_icon, compound=tkinter.LEFT)
mainmenu.add_cascade(label="Help", menu=m5)



root.config(menu=mainmenu)    #configure the mainmenu as menu






    #tool bar
tool_bar_label = Label(root)
tool_bar_label.pack(side=TOP, fill=X)



    # font family
fonts = tkinter.font.families()
font_family = StringVar()
font_box = ttk.Combobox(tool_bar_label, textvariable=font_family, state='readonly')
font_box["values"] = fonts
font_box.current(fonts.index("Arial"))
font_box.grid(row=0, column=0, padx=10, pady=5)

    # size
size_family = IntVar()
font_size = ttk.Combobox(tool_bar_label, width=20, textvariable=size_family, state='readonly')
font_size["values"] = tuple(range(8, 74, 2))
font_size.current(20)
font_size.grid(row=0, column=1, padx=10, pady=5)

    # set initial font and font size
font_now = "Arial"
font_size_now = 20


    # function for change font
def change_font(root):
    global font_now
    font_now = font_family.get()
    text.config(font=(font_now, font_size_now))

font_box.bind("<<ComboboxSelected>>", change_font)


    # define function for change size
def change_size(root):
    global font_size_now   
    font_size_now = size_family.get()
    text.config(font=(font_now, font_size_now))

font_size.bind("<<ComboboxSelected>>", change_size)


    # bold button
    # icon bold button
bold_icon = tkinter.PhotoImage(file='icon/bold.png')
boldbtn = Button(tool_bar_label, image=bold_icon)
boldbtn.grid(row=0, column=2, padx=5)

    # define function for bold
def bold():
     text_get = font.Font(font=text["font"])
     if text_get.actual()["weight"] == "normal":
         text.config(font=(font_now, font_size_now, "bold"))
     if text_get.actual()["weight"] == "bold":
         text.config(font=(font_now, font_size_now, "normal"))
boldbtn.config(command=bold)




    # Italic button
    # icon italic button
italic_icon = tkinter.PhotoImage(file='icon/italic.png')
italicbtn = Button(tool_bar_label, image=italic_icon)
italicbtn.grid(row=0, column=3, padx=5)

    # define function for bold
def Italic():
    text_get = font.Font(font=text["font"])
    if text_get.actual()["slant"] == "roman":
        text.config(font=(font_now, font_size_now, "italic"))
    if text_get.actual()["slant"] == "italic":
        text.config(font=(font_now, font_size_now, "roman"))
italicbtn.config(command=Italic)




    # Underline button
    # icon Underline button
under_line_icon = tkinter.PhotoImage(file='icon/underline.png')
underlinebtn = Button(tool_bar_label, image=under_line_icon)
underlinebtn.grid(row=0, column=4, padx=5)

    # define funcions for Underline
def Underline():
    text_get = font.Font(font=text["font"])
    if text_get.actual()["underline"] == 0:
        text.config(font=(font_now, font_size_now, "underline"))
    if text_get.actual()["underline"] == 1:
        text.config(font=(font_now, font_size_now, "normal"))
underlinebtn.config(command = Underline)




    # font choose button
    # icon font choose button
font_color_icon = tkinter.PhotoImage(file='icon/font color.png')
fontcolorbtn = Button(tool_bar_label, image=font_color_icon)
fontcolorbtn.grid(row=0, column=5, padx=5)

    # define funcions for font color chooser
def fontcolor():
    color = colorchooser.askcolor()
    text.config(fg=color[1])
fontcolorbtn.config(command=fontcolor)




    # aling left button
    # icon aling left button
align_left_icon = tkinter.PhotoImage(file='icon/left.png')
alignleftbtn = Button(tool_bar_label, image=align_left_icon)
alignleftbtn.grid(row=0, column=6, padx=2)


    # define funcions for aling left button
def aling_left():
    text_get = text.get(1.0, END)
    text.tag_config("left", justify=tkinter.LEFT)
    text.delete(1.0, END)
    text.insert(INSERT,text_get, "left")
alignleftbtn.config(command=aling_left)





    # aling center button
    # icon aling center button
align_center_icon = tkinter.PhotoImage(file='icon/centre.png')
aligncenterbtn = Button(tool_bar_label, image=align_center_icon)
aligncenterbtn.grid(row=0, column=7, padx=2)


    # define funcions for aling center button
def aling_center():
    text_get = text.get(1.0, END)
    text.tag_config("center", justify=tkinter.CENTER)
    text.delete(1.0, END)
    text.insert(INSERT,text_get, "center")
aligncenterbtn.config(command=aling_center)




    # aling right button
    # icon aling right button
align_right_icon = tkinter.PhotoImage(file='icon/right.png')
alignrightbtn = Button(tool_bar_label, image=align_right_icon)
alignrightbtn.grid(row=0, column=8, padx=2)


    # define funcions for aling right button
def aling_right():
    text_get = text.get(1.0, END)
    text.tag_config("right", justify=tkinter.RIGHT)
    text.delete(1.0, END)
    text.insert(INSERT,text_get, "right")
alignrightbtn.config(command=aling_right)





    #Scroll Bar
sb = Scrollbar(root)
sb.pack(fill=Y, side=RIGHT)




    #Text
text = Text(root, yscrollcommand=sb.set)
text.config(wrap="word", relief=FLAT)
text.pack(expand=True, fill=BOTH, padx=4, pady=4)
file = None
sb.config(command=text.yview)





    #Counting the word and character in Statusbar
def Count(event=None):
    global text
    if text.edit_modified():
        text_change = True
        word = len(text.get(1.0, "end-1c").split())
        char = len(text.get(1.0, "end-1c").replace(" ", ""))
        statusbar.config(text=f"char:{char} word:{word}")
    text.edit_modified(False)
text.bind("<<Modified>>", Count)







root.mainloop()

######################################################################################################################################
######################################################################################################################################
                                                                                                                                    ##
###########                                                                                                                         ##
##                                                                                                                                  ##
##               ##                     ##                                                                                          ##
#########        ##########             ##                                                                                          ##
#########        ##########      #########                                                                                          ##
##               ##      ##      ##     ##                                                                                          ##
##               ##      ##      ##     ##                                                                                          ##
###########      ##      ##      #########  ## ## ##                                                                                ##
                                                                                                                                    ##
######################################################################################################################################
######################################################################################################################################
