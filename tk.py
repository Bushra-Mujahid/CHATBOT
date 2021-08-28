from tkinter import *

root=Tk()

def send():
    send="You => "+e.get()
    txt.insert(END, "\n"+send)
    if(e.get()=="Hello"):
        txt.insert(END, "\n" + "Bot => Hi")
    elif (e.get() == "Hi"):
        txt.insert(END, "\n" + "Bot => hello")
    elif (e.get() == "hello"):
        txt.insert(END, "\n" + "Bot => hi")
    elif (e.get() == "hi"):
        txt.insert(END, "\n" + "Bot => Hello")
    elif (e.get() == "What is your name?"):
        txt.insert(END, "\n" + "Bot => ChatCommunicator")
    elif (e.get() == "Who made you?"):
        txt.insert(END, "\n" + "Bot => Bushra Mujahid")
    elif (e.get() == "How are you?"):
        txt.insert(END, "\n" + "Bot => Fine and you?")
    elif (e.get() == "Fine"):
        txt.insert(END, "\n" + "Bot => Nice to hear")
    elif (e.get() == "What is Chatbot?"):
        txt.insert(END, "\n" + "Bot => A Chatbot is a program, stimulates a conversation between a user and a computer. ")
    elif (e.get() == "please can you say me, what are the requirements to create you?"):
        txt.insert(END, "\n" + "Bot => I have been created with  Python and tkinter .")
    elif (e.get() == "How chatbot works?"):
        txt.insert(END, "\n" + "Bot => firstly, it takes the input, then processes it by matching the request with its response and displays the output.")
    else:
        txt.insert(END, "\n" + "Bot => Sorry I did'nt get it.")

    e.delete(0,END)
txt=Text(root, bg="black", foreground="#00ffff")
txt.grid(row=0, column=0, columnspan=2)

e=Entry(root, width=100)

main_menu = Menu(root)

# Create the submenu
file_menu = Menu(root)

# Add commands to submenu
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)

#Add the rest of the menu options to the main menu
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

send=Button(root, text="Send", command=send, foreground="#00ffff", bg="black",font=("Arial", 12)).grid(row=1,column=1)
e.grid(row=1, column=0)

root.title("CHATBOT")

root.mainloop()