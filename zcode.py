import tkinter as tk
import tkinter.messagebox
import subprocess
import tkinter.font as tkfont
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from tkinter import filedialog as fd
import os
import getpass
import sys

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
clear()
print(f"Zcode - Kullanıcı: {getpass.getuser()}")

#Pencere
pencere=tk.Tk()
pencere.title("Zcode")
pencere.geometry("500x500")

def hakkinda():
	tkinter.messagebox.showinfo("Hakkında", "Zcode v1.0")
def ac():
	filename = fd.askopenfilename()
	if filename == "":
		pass
	else:
		with open(filename, "r", encoding="utf8") as file:
			file=file.read()
		ent.delete(1.0, "end")
		ent.insert(1.0, file)
	
def run():
	clear()
	ent_veri = ent.get(1.0, tk.END+"-1c")
	if ent_veri == "":
		tkinter.messagebox.showinfo("Hata", "Boş Kod çalıştırılamaz")
		status['text'] = "Hata"
	else:
            
                try:
                        exec(ent_veri)
                        status['text'] = "Başarılı"
                except BaseException as error:
                        status['text'] = "Hata"
                        tkinter.messagebox.showinfo("Hata", error)
                else:
                        pass
	"""if ent_veri == "":
		tkinter.messagebox.showinfo("Hata", "Boş Kod çalıştırılamaz")
		status['text'] = "Hata"
	else:
		status['text'] = "Komut çalıştırılıyor"
		try:
			exec(ent_veri)
		except BaseException as error:
			tkinter.messagebox.showinfo("Hata", error)
			status['text'] = "Hata"
		else:
			tkinter.messagebox.showinfo("Output", exec(ent_veri))
        """		
#Menu
menu = tk.Menu(pencere)
filemenu = tk.Menu(menu)
yardim = tk.Menu(menu)
#Dosya menüsü
filemenu.add_command(label="Dosya Aç", command=ac)
#Yardım menüsü
yardim.add_command(label="Hakkında", command=hakkinda)

menu.add_cascade(label="Dosya", menu=filemenu)
menu.add_cascade(label="Yardım", menu=yardim)

#kod
ent = tk.Text(pencere, width=500)
ent.pack(padx=50)
font = tkfont.Font(font=ent['font'])

cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}


cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}

ip.Percolator(ent).insertfilter(cdg)

#Tab
tab_size = font.measure('    ')
ent.config(tabs=tab_size)

#Statü
status = tk.Label(text="Başlatılmadı")
status.pack()

#Çalıştır
buton = tk.Button(text="Çalıştır", command=run)
buton.place(x=12, y=4400)
buton.pack()

#Config
pencere.config(menu=menu)
#Döngü
try:
	pencere.mainloop()
except:
	clear()
	sys.exit()
