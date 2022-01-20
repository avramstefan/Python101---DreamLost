import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from PIL import ImageTk, Image
import time
from playsound import playsound
import pygame
import winsound

pygame.init()
root = tk.Tk()
root.geometry('600x700')

start_button = "Start your adventure"
medieval_button = "Medieval Era"
cyber_button = "Cyberpunk Era"

medieval_1_1 = "Teleport yourself to a cyberpunk world"
medieval_1_2 = "Explore this world"
medieval_2_1 = "Find a tavern"
medieval_2_2 = "Go to event"
medieval_3_1 = "Order ale and deer meat"
medieval_3_2 = "Go back"
medieval_4_1 = "Join the lonely man"
medieval_4_2 = "Go to the cheerful group"
medieval_5_1 = "Next >"
medieval_6_1 = "Don't accept"
medieval_6_2 = "Go with her"
medieval_7_1 = "Next >"
medieval_8_1 = "You have another chance. Try again"
medieval_9_1 = "Find someone to tell you about the event"
medieval_9_2 = "Search for the mysterious young lady"
medieval_10_1 = "Try to leave"
medieval_10_2 = "Recover your soul through the power of love"
medieval_11_1 = "Finish your adventure"
medieval_12_1 = "Accept and go with him"
medieval_12_2 = "His words seem true,\n but you want to continue alone.\n Enroll yourself in the army"
medieval_13_1 = "Continue your path"
medieval_13_2 = "Help the child"
medieval_14_1 = "Enroll in the army"
medieval_14_2 = "Talk to the man"
medieval_15_1 = "Archer / Ranger"
medieval_15_2 = "Swordsman"
medieval_16_1 = "Accept and join the army beside him"
medieval_16_2 = "Don't accept. Go back"
medieval_17_1 = "I am from BlackRivers, your allies"
medieval_17_2 = "I am not from these lands"

cyber_1_1 = "Teleport yourself to a medieval world"
cyber_1_2 = "Enjoy this world and explore the city"
cyber_2_1 = "Go for recruitment"
cyber_2_2 = "Find a car"
cyber_3_1 = "Next >"
cyber_4_1 = "Continue your path"
cyber_4_2 = "Go with her"
cyber_5_1 = "You have another chance. Try again"
cyber_6_1 = "Find the portal"
cyber_6_2 = "Go in space"
cyber_7_1 = "Continue"
cyber_8_1 = "Finish your adventure"
cyber_9_1 = "Take the motorcycle"
cyber_9_2 = "Go with her"

cyber_choices_button = [cyber_1_1, cyber_1_2, # 0 1
                        cyber_2_1, cyber_2_2, # 2 3
                        cyber_3_1, # 4
                        cyber_4_1, cyber_4_2, # 5 6
                        cyber_5_1, # 7
                        cyber_6_1, cyber_6_2, # 8 9
                        cyber_7_1, # 10
                        cyber_8_1, # 11
                        cyber_9_1, cyber_9_2, # 12 13
                        
                        ]


medieval_choices_button = [medieval_1_1, medieval_1_2, # 0 1
                           medieval_2_1, medieval_2_2, # 2 3
                           medieval_3_1, medieval_3_2, # 4 5 - 5 does not exist
                           medieval_4_1, medieval_4_2, # 6 7
                           medieval_5_1, # 8
                           medieval_6_1, medieval_6_2, # 9 10
                           medieval_7_1, # 11
                           medieval_8_1, # 12
                           medieval_9_1, medieval_9_2, # 13 14
                           medieval_10_1, medieval_10_2, #15 16
                           medieval_11_1, # 17  EXIT MESSAGE
                           medieval_12_1, medieval_12_2, # 18 19
                           medieval_13_1, medieval_13_2, # 20 21
                           medieval_14_1, medieval_14_2, # 22 23
                           medieval_15_1, medieval_15_2, # 24 25
                           medieval_16_1, medieval_16_2, # 26 27
                           medieval_17_1, medieval_17_2, # 28 29
                           ]

Buttons = (start_button, medieval_button, cyber_button, cyber_choices_button, medieval_choices_button)

is_final = 1
is_sound = 1

def cyber_27(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_27 = tk.PhotoImage(file = "cyber_27_text.png")
    
    label = Label(image = cyber_27)
    label.image = cyber_27
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: exit(),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def cyber_26(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_26 = tk.PhotoImage(file = "cyber_26_text.png")
    
    label = Label(image = cyber_26)
    label.image = cyber_26
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_27(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_25(Buttons, label, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label.destroy()
    
    cyber_25 = tk.PhotoImage(file = "cyber_25_text.png")

    label = Label(image = cyber_25)
    label.image = cyber_25
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_26(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_24(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_24 = tk.PhotoImage(file = "cyber_24_text.png")
    
    label = Label(image = cyber_24)
    label.image = cyber_24
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][7], padx = 10,
                        pady = 5, fg = "white", bg = "dark red", command = lambda: era_choice(Buttons, 1,  label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 180, y = 30)

def cyber_23(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_23 = tk.PhotoImage(file = "cyber_23_text.png")
    
    label = Label(image = cyber_23)
    label.image = cyber_23
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_24(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_22(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_22 = tk.PhotoImage(file = "cyber_22_text.png")
    
    label = Label(image = cyber_22)
    label.image = cyber_22
    label.pack()

    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_23(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_21(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("doom.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)
    
    cyber_21 = tk.PhotoImage(file = "cyber_21_text.png")
    
    label = Label(image = cyber_21)
    label.image = cyber_21
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_22(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 30)

def cyber_20(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_20 = tk.PhotoImage(file = "cyber_20_text.png")
    
    label = Label(image = cyber_20)
    label.image = cyber_20
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][12], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_21(Buttons, label, button_1), # take the motorcycle
                        width = 30, height = 2)
    button_1.place( x = 40, y = 30)
        
    button_2 = tk.Button(root, text = Buttons[3][13], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_25(Buttons, label, button_1, button_2), # go with her
                        width = 30, height = 2)
    button_2.place( x = 320, y = 30)

def cyber_19(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_19 = tk.PhotoImage(file = "cyber_19_text.png")
    
    label = Label(image = cyber_19)
    label.image = cyber_19
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_20(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 30)

def cyber_18(Buttons, label, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label.destroy()
    
    cyber_18 = tk.PhotoImage(file = "cyber_18_text.png")

    label = Label(image = cyber_18)
    label.image = cyber_18
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_19(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_17(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_17 = tk.PhotoImage(file = "cyber_17_text.png")
    
    label = Label(image = cyber_17)
    label.image = cyber_17
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: exit(),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_16(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_16 = tk.PhotoImage(file = "cyber_16_text.png")
    
    label = Label(image = cyber_16)
    label.image = cyber_16
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_17(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_15(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_15 = tk.PhotoImage(file = "cyber_15_text.png")
    
    label = Label(image = cyber_15)
    label.image = cyber_15
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_16(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_14(Buttons, label, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label.destroy()
    
    cyber_14 = tk.PhotoImage(file = "cyber_14_text.png")

    label = Label(image = cyber_14)
    label.image = cyber_14
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_15(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)


def cyber_13(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_13 = tk.PhotoImage(file = "cyber_13_text.png")
    
    label = Label(image = cyber_13)
    label.image = cyber_13
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_1(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_12(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_12 = tk.PhotoImage(file = "cyber_12_text.png")
    
    label = Label(image = cyber_12)
    label.image = cyber_12
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_13(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_11(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_11 = tk.PhotoImage(file = "cyber_11_text.png")
    
    label = Label(image = cyber_11)
    label.image = cyber_11
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_12(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 30)

def cyber_10(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("doom.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)
    
    cyber_10 = tk.PhotoImage(file = "cyber_10_text.png")
    
    label = Label(image = cyber_10)
    label.image = cyber_10
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][8], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_11(Buttons, label, button_1), # find the portal
                        width = 30, height = 2)
    button_1.place( x = 40, y = 30)
        
    button_2 = tk.Button(root, text = Buttons[3][9], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_14(Buttons, label, button_1, button_2), # go in space
                        width = 30, height = 2)
    button_2.place( x = 320, y = 30)
    

def cyber_9(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_9 = tk.PhotoImage(file = "cyber_9_text.png")
    
    label = Label(image = cyber_9)
    label.image = cyber_9
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_10(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_8(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_8 = tk.PhotoImage(file = "cyber_8_text.png")
    
    label = Label(image = cyber_8)
    label.image = cyber_8
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_9(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_7(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_7 = tk.PhotoImage(file = "cyber_7_text.png")
    
    label = Label(image = cyber_7)
    label.image = cyber_7
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][7], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: era_choice(Buttons, 1,  label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 30)

def cyber_6(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_6 = tk.PhotoImage(file = "cyber_6_text.png")
    
    label = Label(image = cyber_6)
    label.image = cyber_6
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_7(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_5(Buttons, label, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label.destroy()
    
    cyber_5 = tk.PhotoImage(file = "cyber_5_text.png")

    label = Label(image = cyber_5)
    label.image = cyber_5
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_6(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_4(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_4 = tk.PhotoImage(file = "cyber_4_text.png")
    
    label = Label(image = cyber_4)
    label.image = cyber_4
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][5], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_8(Buttons, label, button_1), # continue your path
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)
        
    button_2 = tk.Button(root, text = Buttons[3][6], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_5(Buttons, label, button_1, button_2), # go with her
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)

def cyber_3(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    cyber_3 = tk.PhotoImage(file = "cyber_3_text.png")
    
    label = Label(image = cyber_3)
    label.image = cyber_3
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_4(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def cyber_2(Buttons, label, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label.destroy()
    
    cyber_2 = tk.PhotoImage(file = "cyber_2_text.png")

    label = Label(image = cyber_2)
    label.image = cyber_2
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][2], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_3(Buttons, label, button_1), # recruit
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)
        
    button_2 = tk.Button(root, text = Buttons[3][3], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_18(Buttons, label, button_1, button_2), # find a car
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)

def cyber_1(Buttons, label_2, button_a, button_b):

    button_a.destroy()
    button_b.destroy()
    label_2.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("cyber_sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)
    
    cyber_1 = tk.PhotoImage(file = "cyber_1_text.png")

    label = Label(image = cyber_1)
    label.image = cyber_1
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[3][0], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_1(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)
        
    button_2 = tk.Button(root, text = Buttons[3][1], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_2(Buttons, label, button_1, button_2),
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)

def medieval_59(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
    
    medieval_59 = tk.PhotoImage(file = "medieval_59_text.png")
    
    label = Label(image = medieval_59)
    label.image = medieval_59
    label.pack()
    
    button_garbage = tk.Button(root, text = "")
    
    button_1 = tk.Button(root, text = Buttons[4][22], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_40(Buttons, label, button_1, button_garbage),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_58(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_58 = tk.PhotoImage(file = "medieval_58_text.png")
    
    label = Label(image = medieval_58)
    label.image = medieval_58
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][12], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: era_choice(Buttons, 1,  label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_57(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_57 = tk.PhotoImage(file = "medieval_57_text.png")
    
    label = Label(image = medieval_57)
    label.image = medieval_57
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_58(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_56(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_56 = tk.PhotoImage(file = "medieval_56.png")
    
    label = Label(image = medieval_56)
    label.image = medieval_56
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_57(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_55(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_55 = tk.PhotoImage(file = "medieval_55_text.png")
    
    label = Label(image = medieval_55)
    label.image = medieval_55
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_56(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_54(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
    
    medieval_54 = tk.PhotoImage(file = "medieval_54_text.png")
    
    label = Label(image = medieval_54)
    label.image = medieval_54
    label.pack()

def medieval_53(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_53 = tk.PhotoImage(file = "medieval_53_text.png")
    
    label = Label(image = medieval_53)
    label.image = medieval_53
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][29], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_55(Buttons, label, button_2), #not from here
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][28], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_59(Buttons, label, button_1, button_2), #from BlackRivers
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_52(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_52 = tk.PhotoImage(file = "medieval_52_text.png")
    
    label = Label(image = medieval_52)
    label.image = medieval_52
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][17], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: exit(),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_51(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_51 = tk.PhotoImage(file = "medieval_51_text.png")
    
    label = Label(image = medieval_51)
    label.image = medieval_51
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_52(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 30)

def medieval_50(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("triple_h_the_game.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    
    medieval_50 = tk.PhotoImage(file = "medieval_50_text.png")
    
    label = Label(image = medieval_50)
    label.image = medieval_50
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_51(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_49(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_49 = tk.PhotoImage(file = "medieval_49_text.png")
    
    label = Label(image = medieval_49)
    label.image = medieval_49
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_50(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_48(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_48 = tk.PhotoImage(file = "medieval_44_text.png")
    
    label = Label(image = medieval_48)
    label.image = medieval_48
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_49(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_47(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_47 = tk.PhotoImage(file = "medieval_47_text.png")
    
    label = Label(image = medieval_47)
    label.image = medieval_47
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][12], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: era_choice(Buttons, 1,  label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_46(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_46 = tk.PhotoImage(file = "medieval_46.png")
    
    label = Label(image = medieval_46)
    label.image = medieval_46
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda:  medieval_47(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_45(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("pantera_walk.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    
    medieval_45 = tk.PhotoImage(file = "medieval_45_text.png")
    
    label = Label(image = medieval_45)
    label.image = medieval_45
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda:  medieval_46(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_44(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_44 = tk.PhotoImage(file = "medieval_44_text.png")
    
    label = Label(image = medieval_44)
    label.image = medieval_44
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda:  medieval_45(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_43(Buttons, label_copy, button):
    pass

def medieval_42(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_42 = tk.PhotoImage(file = "medieval_42_text.png")
    
    label = Label(image = medieval_42)
    label.image = medieval_42
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda:  medieval_44(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_41(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_41 = tk.PhotoImage(file = "medieval_41_text.png")
    
    label = Label(image = medieval_41)
    label.image = medieval_41
    label.pack()

def medieval_40(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_40 = tk.PhotoImage(file = "medieval_40_text.png")
    
    label = Label(image = medieval_40)
    label.image = medieval_40
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][25], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_48(Buttons, label, button_2), #swordsman
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][24], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_42(Buttons, label, button_1, button_2), #archer
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_39(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_39 = tk.PhotoImage(file = "medieval_39_text.png")
    
    label = Label(image = medieval_39)
    label.image = medieval_39
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][23], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_53(Buttons, label, button_2), #go to the emperor / talk to the man
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][22], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_40(Buttons, label, button_1, button_2), #enroll
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_38(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_38 = tk.PhotoImage(file = "medieval_38_text.png")
    
    label = Label(image = medieval_38)
    label.image = medieval_38
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][17], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: exit(),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_37(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_37 = tk.PhotoImage(file = "medieval_37.png")
    
    label = Label(image = medieval_37)
    label.image = medieval_37
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda:  medieval_38(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_36(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_36 = tk.PhotoImage(file = "medieval_36_text.png")
    
    label = Label(image = medieval_36)
    label.image = medieval_36
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda:  medieval_37(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)


def medieval_35(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_35 = tk.PhotoImage(file = "medieval_35_text.png")
    
    label = Label(image = medieval_35)
    label.image = medieval_35
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda:  medieval_36(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_34(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_34 = tk.PhotoImage(file = "medieval_34_text.png")
    
    label = Label(image = medieval_34)
    label.image = medieval_34
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][17], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: exit(),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_33(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_33 = tk.PhotoImage(file = "medieval_33.png")
    
    label = Label(image = medieval_33)
    label.image = medieval_33
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_34(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_32(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_29 = tk.PhotoImage(file = "medieval_32_text.png")
    
    label = Label(image = medieval_29)
    label.image = medieval_29
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_33(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)


def medieval_31(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("triple_h_the_game.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    
    medieval_29 = tk.PhotoImage(file = "medieval_31_text.png")
    
    label = Label(image = medieval_29)
    label.image = medieval_29
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_32(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_30(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("pantera_walk.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
     
    medieval_30 = tk.PhotoImage(file = "medieval_30_text.png")
    
    label = Label(image = medieval_30)
    label.image = medieval_30
    label.pack()
    
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_35(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_29(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_29 = tk.PhotoImage(file = "medieval_29_text.png")
    
    label = Label(image = medieval_29)
    label.image = medieval_29
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][21], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_31(Buttons, label, button_2), #help the child
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][20], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_30(Buttons, label, button_1, button_2), #leave the child
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_28(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_28 = tk.PhotoImage(file = "medieval_28_text.png")
    
    label = Label(image = medieval_28)
    label.image = medieval_28
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_29(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_27(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_27 = tk.PhotoImage(file = "medieval_27_text.png")
    
    label = Label(image = medieval_27)
    label.image = medieval_27
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_28(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_26(Buttons, label_copy, button):
    pass

def medieval_25(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_25 = tk.PhotoImage(file = "medieval_25_text.png")
    
    label = Label(image = medieval_25)
    label.image = medieval_25
    label.pack()
    
    button_garbage = tk.Button(root, text = "");
    
    button_2 = tk.Button(root, text = Buttons[4][19], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_40(Buttons, label, button_2, button), #go alone
                        width = 30, height = 2)
    button_2.place( x = 320, y = 30)
    
    button_1 = tk.Button(root, text = Buttons[4][18], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_27(Buttons, label, button_1, button_2), #go with the lonely man
                        width = 30, height = 2)
    button_1.place( x = 40, y = 30)

def medieval_24(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_24 = tk.PhotoImage(file = "medieval_24_text.png")
    
    label = Label(image = medieval_24)
    label.image = medieval_24
    label.pack()    
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_25(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    
def medieval_23(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_23 = tk.PhotoImage(file = "medieval_23_text.png")
    
    label = Label(image = medieval_23)
    label.image = medieval_23
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_24(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    
    
def medieval_22(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("murder_scream_sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    
    medieval_22 = tk.PhotoImage(file = "medieval_22_text.png")
    
    label = Label(image = medieval_22)
    label.image = medieval_22
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][12], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: era_choice(Buttons, 1,  label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_21(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_21 = tk.PhotoImage(file = "medieval_21_text.png")
    
    label = Label(image = medieval_21)
    label.image = medieval_21
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][17], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: exit(),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_20(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_20 = tk.PhotoImage(file = "medieval_20_text.png")
    
    label = Label(image = medieval_20)
    label.image = medieval_20
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_22(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_19(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_19 = tk.PhotoImage(file = "medieval_19_text.png")
    
    label = Label(image = medieval_19)
    label.image = medieval_19
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][16], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_21(Buttons, label, button_2), #recover soul
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][15], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_20(Buttons, label, button_1, button_2), #run
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_18(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_18 = tk.PhotoImage(file = "medieval_18_text.png")
    
    label = Label(image = medieval_18)
    label.image = medieval_18
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_19(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_17(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_17 = tk.PhotoImage(file = "medieval_17_text.png")
    
    label = Label(image = medieval_17)
    label.image = medieval_17
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_18(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_16(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_16 = tk.PhotoImage(file = "medieval_16_text.png")
    
    label = Label(image = medieval_16)
    label.image = medieval_16
    label.pack()

    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_17(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_15(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_15 = tk.PhotoImage(file = "medieval_15_text.png")
    
    label = Label(image = medieval_15)
    label.image = medieval_15
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_16(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    
def medieval_14(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_14 = tk.PhotoImage(file = "medieval_14.png")
    
    label = Label(image = medieval_14)
    label.image = medieval_14
    label.pack()

def medieval_13(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_13 = tk.PhotoImage(file = "medieval_13_text.png")
    
    label = Label(image = medieval_13)
    label.image = medieval_13
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][14], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_15(Buttons, label, button_2), #search for the lady
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][13], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_23(Buttons, label, button_1, button_2), #go in town
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_12(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("murder_scream_sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    
    medieval_11 = tk.PhotoImage(file = "medieval_12_text.png")
    
    label = Label(image = medieval_11)
    label.image = medieval_11
    label.pack()

    button_1 = tk.Button(root, text = Buttons[4][12], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: era_choice(Buttons, 1,  label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_11(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_11 = tk.PhotoImage(file = "medieval_11_text.png")
    
    label = Label(image = medieval_11)
    label.image = medieval_11
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_12(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_10(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_10 = tk.PhotoImage(file = "medieval_10_text.png")
    
    label = Label(image = medieval_10)
    label.image = medieval_10
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_13(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)
    

def medieval_9(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_9 = tk.PhotoImage(file = "medieval_9_text.png") #lady accept or no
    
    label = Label(image = medieval_9)
    label.image = medieval_9
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][10], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_11(Buttons, label, button_2),
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][9], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_10(Buttons, label, button_1, button_2),
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_8(Buttons, label_copy, button):

    button.destroy()
    label_copy.destroy()

    medieval_8 = tk.PhotoImage(file = "medieval_8_text.png")

    label = Label(image = medieval_8)
    label.image = medieval_8
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][8], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_9(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_7(Buttons, label_copy, button_a, button_b):
    
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy()
     
    medieval_7 = tk.PhotoImage(file = "medieval_7_text.png")
    
    label = Label(image = medieval_7)
    label.image = medieval_7
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][27], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_5(Buttons, label, button_2),
                        width = 30, height = 2)
    button_2.place( x = 320, y = 30)
    
    button_1 = tk.Button(root, text = Buttons[4][26], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_27(Buttons, label, button_1, button_2),
                        width = 30, height = 2)
    button_1.place( x = 40, y = 30)

def medieval_6(Buttons, label_copy, button):
    pass

def medieval_5(Buttons, label_copy, button):
     
    button.destroy()
    label_copy.destroy()
     
    medieval_5 = tk.PhotoImage(file = "medieval_5_text.png")
    
    label = Label(image = medieval_5)
    label.image = medieval_5
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][7], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_8(Buttons, label, button_2),
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][6], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_7(Buttons, label, button_1, button_2),
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)


def medieval_4(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_4 = tk.PhotoImage(file = "medieval_4_text.png")
    
    label = Label(image = medieval_4)
    label.image = medieval_4
    label.pack()
    
    button_1 = tk.Button(root, text = Buttons[4][11], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_39(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 170, y = 630)

def medieval_3(Buttons, label_copy, button_a, button_b):
   
    button_a.destroy()
    button_b.destroy()
    label_copy.destroy() 
   
    medieval_3 = tk.PhotoImage(file = "medieval_3_text.png")
    
    label = Label(image = medieval_3)
    label.image = medieval_3
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][5], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_2(Buttons, label, button_2),
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][4], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_5(Buttons, label, button_1),
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def medieval_2(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()
    
    medieval_2 = tk.PhotoImage(file = "medieval_2_text.png")
    
    label = Label(image = medieval_2)
    label.image = medieval_2
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][3], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_4(Buttons, label, button_2),
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][2], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_3(Buttons, label, button_1, button_2),
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)
    

def medieval_1(Buttons, label_copy, button):
    
    button.destroy()
    label_copy.destroy()

    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("medieval_sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)

    medieval_1 = tk.PhotoImage(file = "medieval_1_text.png")
    
    label = Label(image = medieval_1)
    label.image = medieval_1
    label.pack()
    
    button_2 = tk.Button(root, text = Buttons[4][1], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_2(Buttons, label, button_2),
                        width = 30, height = 2)
    button_2.place( x = 320, y = 630)
    
    button_1 = tk.Button(root, text = Buttons[4][0], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_1(Buttons, label, button_1, button_2),
                        width = 30, height = 2)
    button_1.place( x = 40, y = 630)

def era_choice(Buttons, is_final, BGlabel, button):
    
    button.destroy()
    BGlabel.destroy()
    
    if is_final == 1:
        winsound.PlaySound("start_sound_final.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)
    
    choose_era = tk.PhotoImage(file = "choose_era_text.png")

    label_2 = Label(image = choose_era)
    label_2.image =  choose_era
    label_2.pack()
    
    button_1 = tk.Button(root, text = Buttons[1], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: medieval_1(Buttons, label_2, button_1),
                        width = 20, height = 1)
    button_1.place( x = 40, y = 480)
        
    button_2 = tk.Button(root, text = Buttons[2], padx = 10,
                        pady = 5, fg = "white", bg = "black", command = lambda: cyber_1(Buttons, label_2, button_1, button_2),
                        width = 20, height = 1)
    button_2.place( x = 350, y = 480)

def start(Buttons, is_final):
      
    winsound.PlaySound("start_sound_final.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)
      
    first_page = tk.PhotoImage(file = "start_text.png")

    BGlabel = tk.Label(root, image = first_page)
    BGlabel.image = first_page
    BGlabel.pack()
    
    root.update()

    button = tk.Button(root, text = Buttons[0], padx = 10,
                       pady = 5, fg = "white", bg = "dark red", command = lambda: era_choice(Buttons, 0, BGlabel, button))
    button.place(x = 230, y = 320)
            

def exit():
    
    root.destroy()

start(Buttons, is_final)
root.mainloop()
