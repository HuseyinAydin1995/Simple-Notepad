from tkinter import *
from tkinter.ttk import *
from tkinter  import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText

def fileActions(value):
	if value == 'New':
		if len(notepad.get('1.0', END+'-1c'))>0:
			if messagebox.askyesno("Notepad", "Do you want to save changes?"):
				fileActions("Save")
			else:
				notepad.delete(0.0, END)
		window.title("Simple Notepad"),
	elif value == 'Open':
		try:
			fileDialog = filedialog.askopenfile(parent = window, mode = 'r')
			t = fileDialog.read()
			notepad.delete(0.0, END)
			notepad.insert(0.0, t)
		except:
			print("File cannot be opened!")
	elif value == 'Save':
		fileDialog = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
		if fileDialog!= None:
			data = notepad.get('1.0', END)
			try:
				fileDialog.write(data)
			except:
				messagebox.showerror(title="Error", message = "File cannot be saved!"),
	elif value == 'Save As':
		fileDialog = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
		t = notepad.get(0.0, END)
		try:
			fileDialog.write(t.rstrip())
		except:
			messagebox.showerror(title="Error", message = "File cannot be saved!")


def specialActions(value,index=0):
    if index == 0:
        notepad.event_generate("<<"+value+">>")
    else:
        if value == "Click":
            notepad.tag_config('Found',background=currentTheme[2],foreground=currentTheme[3])
        elif value == "Exit":
            if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
                window.destroy()

def changeTheme(value):
	if value == "Default":
		currentTheme = ["white","black","white","black"]
	elif value == "Night":
		currentTheme = ["#0c1445","#747484","white","black"]
	elif value == "Dark":
		currentTheme = ["#000000","#ffffff","white","black"]
	notepad.configure(bg=currentTheme[0],fg=currentTheme[1])
window = Tk()
window.iconphoto(False,PhotoImage(file = "icon.png"))
window.title('Simple Notepad')
window.resizable(0, 0)
window.configure(background="green")
currentTheme = ["white","black","white","black"]
notepadDimensions = [90,30]
notepad = ScrolledText(window,width = notepadDimensions[0],height = notepadDimensions[1],bg=currentTheme[0], fg=currentTheme[1])

notepadMenu = Menu(window)
window.configure(menu=notepadMenu)


fileMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)
fileMenu.add_command(label="New", command = lambda:fileActions("New"))
fileMenu.add_command(label="Open", command = lambda:fileActions("Open"))
fileMenu.add_command(label="Save", command = lambda:fileActions("Save"))
fileMenu.add_command(label="Save As", command = lambda:fileActions("Save As"))
fileMenu.add_command(label="Exit", command = lambda:fileActions("Exit"))

editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)
editMenu.add_command(label="Cut", command = lambda:specialActions("Cut"))
editMenu.add_command(label="Copy", command = lambda:specialActions("Copy"))
editMenu.add_command(label="Paste", command = lambda:specialActions("Paste"))
editMenu.add_command(label="Clear", command = lambda:specialActions("Clear"))
editMenu.add_command(label="Select All", command = lambda:specialActions("SelectAll"))

themeMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Theme', menu = themeMenu)
themeMenu.add_command(label="Default", command = lambda:changeTheme("Default"))
themeMenu.add_command(label="Night", command = lambda:changeTheme("Night"))
themeMenu.add_command(label="Dark", command = lambda:changeTheme("Dark"))

about = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='About', menu = about)
about.add_command(label='About',command = lambda:messagebox.showinfo("Simple Notepad", "Simple Notepad\nCreated by Hüseyin AYDIN"))

notepad.pack()
window.mainloop()