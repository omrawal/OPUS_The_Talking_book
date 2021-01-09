import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

def playbook(book_path,root):
    book = open(book_path,'rb')
    pdf_reader = PyPDF2.PdfFileReader(book)
    num_pages = pdf_reader.numPages
    play = pyttsx3.init()
    voices=play.getProperty('voices')
    play.setProperty('voice',voices[1].id)
    # print(play.getProperty('rate'))
    play.setProperty('rate', 150)
    print('Playing Audio Book')
    for num in range(0, num_pages):
        page = pdf_reader.getPage(num)
        data = page.extractText()
        play.say(data)
        play.runAndWait()
    messagebox.showinfo(title='Success!!',message='End of audiobook!!!')

root=tk.Tk()    
root.title("OPUS")
root.geometry("500x500")
lbs = tk.Label(root, text = "OPUS - The Talking Book", font=20)
lbs.place(x=180, y=5)
lbs1 = tk.Label(root, text = "Select any pdf file to read", font=10)
lbs1.place(x=50, y=50)

lbs_message = tk.Label(root, text = "Book:", font=10)
lbs_message.place(x=10, y=100)

message_entry=tk.Entry(root,font=10)
message_entry.place(x=150, y=100)

def browsefunc(ent):
    filename =askopenfilename(filetypes=([
                    ("PDF", ".pdf"),

                ]))
    ent.insert(tk.END, filename) # add this

file_browse_button=tk.Button(root,text="Browse",font=10,command=lambda:browsefunc(message_entry))
file_browse_button.place(x=400, y=90)

read_button=tk.Button(root,font=("times", 16),text="Listen",command=lambda:playbook(message_entry.get(),root))
read_button.place(x = 200, y = 200 )


root.mainloop()





