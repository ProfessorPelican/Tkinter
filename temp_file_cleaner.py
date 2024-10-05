import os
import shutil
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import tkinter.messagebox

class MainApplication(ttk.Frame):
    '''Main GUI for *.tmp file clearing application.
    Moves *.tmp files from a selected source folder to a selected
    destination folder.'''
    def __init__(self, master):
        self.master = master
        ttk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()
   
    def configure_gui(self):
       self.master.title('')
       self.master.iconbitmap('')
       self.set_app_style()
       self.style.theme_use("st_app_new")
       self.master.resizable(False, False)
    
    def create_widgets(self):
       self.create_master_window()
    
    def create_master_window(self):
        '''Creates the widgets on the master frame (excluding menus).'''
        title = 'TMP File Cleaner (moves tmp files)'
        self.title_lbl = ttk.Label(self.master, width=75, anchor='center',
                                   text=title).grid(row=1, column=0, columnspan = 2)
        self.spacer_lbl1 = ttk.Label(self.master, width=75, anchor='center',
                                    text='').grid(row=2, column=0, columnspan = 2)
        self.run_main_btn = ttk.Button(self.master, text='Run TMP File Cleaner',
                                       command=self.run_tmp_cleaner).grid(row=3, column=0, columnspan = 2)
        self.spacer_lbl2 = ttk.Label(self.master, width=75, anchor='center',
                                    text='').grid(row=4, column=0, columnspan = 2)
        
        self.source_folder_txt = tk.StringVar()
        self.lbl1 = ttk.Label(self.master,
                              text='source root folder (incl subfolders) with tmp files:').grid(row=5, column=0,
                                                                                           sticky='W', columnspan=2)
        self.source_folder_entry = ttk.Entry(self.master, width=75, textvariable=self.source_folder_txt).grid(row=6, 
                                                                                                   column=0)
        self.btn1 = ttk.Button(self.master, text='Browse', command=self.select_source_folder).grid(row=6, column=1)
        
        self.sep1 = ttk.Label(self.master).grid(row=7, column=0, columnspan = 2)
        
        self.destination_folder_txt = tk.StringVar()
        self.lbl2 = ttk.Label(self.master,
                             text='destination folder for tmp files:').grid(row=8, column=0,
                                                                             sticky='W', columnspan = 2)
        self.destination_folder_entry = ttk.Entry(self.master, width=75, 
                                            textvariable=self.destination_folder_txt).grid(row=9, column=0)
        self.btn2 = ttk.Button(self.master, text='Browse', command=self.select_destination_folder).grid(row=9, column=1)

    def select_source_folder(self):
        '''Selects file name and sets related input path variable in the 
        config file and in the related entry box.'''
        folder = tkinter.filedialog.askdirectory(initialdir = os.getcwd()) + '/'
        self.source_folder_txt.set(folder)

    def select_destination_folder(self):
        '''Selects file name and sets related input path variable in the 
        config file and in the related entry box.'''
        folder = tkinter.filedialog.askdirectory(initialdir = os.getcwd()) + '/'
        self.destination_folder_txt.set(folder)

    def run_tmp_cleaner(self):
        '''Moves temp files in a given source folder to a given destination
        folder (*.tmp).  Needed since many of these are created by the system.'''
        if self.source_folder_txt.get() == '' or self.destination_folder_txt.get() == '':
            tkinter.messagebox.showinfo(self.master, 'Please select both source and destination folders.')
            return
        
        try:
            for dirpath, subdirs, files in os.walk(self.source_folder_txt.get()):
                for file in files:
                    if str.lower(file)[-3:] == 'tmp':
                        shutil.move(os.path.join(dirpath, file),
                                    os.path.join(self.destination_folder_txt.get(), file))
            tkinter.messagebox.showinfo(self.master, 'TMP cleaner is complete.')
        except:
            tkinter.messagebox.showinfo(self.master, 'ERROR: Please ensure file paths are correct.')

    def set_app_style(self):
        self.style = ttk.Style()
        self.style.theme_create( "st_app_new", parent="alt", settings={
            ".":             {"configure": {"background"      : 'gray40,',
                                            "foreground"      : 'gray80',
                                            "relief"          : "flat",
                                            "highlightcolor"  : 'green2'}},
    
            "TLabel":        {"configure": {"foreground"      : 'green2',
                                            "padding"         : 10,
                                            "font"            : ("Calibri", 12)}},
    
            "TNotebook":     {"configure": {"padding"         : 5}},
            "TNotebook.Tab": {"configure": {"padding"         : [25, 5], 
                                            "foreground"      : "white"},
                                "map"      : {"background"      : [("selected", 'gray55')],
                                            "expand"          : [("selected", [1, 1, 1, 0])]}},
    
            "TCombobox":     {"configure": {"selectbackground": 'gray40',
                                            "fieldbackground" : "white",
                                            "background"      : 'gray80',
                                            "foreground"      : "black"}},
    
            "TButton":       {"configure": {"font"            :("Calibri", 13, 'bold'),
                                            "background"      : "black",
                                            "foreground"      : 'green2'},
                                "map"      : {"background"      : [("active", 'green2')],
                                            "foreground"      : [("active", 'black')]}},
                
            "TEntry":        {"configure": {"foreground"      : "black"}},
            "Horizontal.TProgressbar":{"configure": {"background": 'gray55'}}
        })

if __name__ == '__main__':
    root = tk.Tk()
    main_app =  MainApplication(root)
    root.mainloop()
    
