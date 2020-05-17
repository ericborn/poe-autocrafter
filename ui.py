# -*- coding: utf-8 -*-
"""
Created on Sun May 17

UI for the POE autocrafter

@author: Eric
"""
import tkinter as tk

# on change dropdown value
def change_dropdown(*args):
    print(dropdown_button.get())

# initalize window
root = tk.Tk() 

# change title
root.title('POE AutoCrafter')

# Add a grid
mainframe = tk.Frame(root)
mainframe.grid(column=0,row=0, sticky=(tk.N, tk.W, tk.E, tk.S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# number of rolls box
tk.Label(root, text='Number of rolls')#.grid(row=0)
roll_input = tk.Entry(root)
#roll_input.grid(row=0, column=1)

# create a Tkinter variable to store the dropdown button
dropdown_button = tk.StringVar(root)

mod_list = ['Cold Resistance', 'Lightning Resistance', 'Fire Resistance',
            'Chaos Resistance', 'Movement Speed', 'Elusive', 'Tailwind', 
            'To Intelligence', 'To Strength', 'To Dexterity', 'Vitality Skill']

dropdown_button.set(mod_list[0])

popupMenu = tk.OptionMenu(mainframe, dropdown_button, *mod_list)
tk.Label(mainframe, text="Choose a mod to roll").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# create exit button
exit_button = tk.Button(root, text='Quit', width=10, command=root.destroy)
#start_button_widget = tk.Button(window, text='Start Crafting', width=20)

# draw the exit button
exit_button.pack()

# link function to change dropdown
dropdown_button.trace('w', change_dropdown)

# call window
root.mainloop()