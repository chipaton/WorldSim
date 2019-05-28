import sys
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import time


#initial values
population = 7500000000.0
maxPopulation = 10000000000.0
veganPercent = .25
year = 2019
start = True

def increase_population():
    global population
    population = population * 1.07

def thanos():
    global population
    population = population/2.0
#loop
while start == True:
    while population < maxPopulation:
        increase_population()
        time.sleep(5)
#create gui
window = Tk()
window.title("WorldSim")
window.geometry('1600x900')

#statistics
statLabel = Label(window, text = "Statistics", font = ("Arial Bold", 15))
statLabel.grid(column = 0, row = 0)
popLabel = Label(window, text = "Population: " + str(int(population)), font = ("Arial", 10))
popLabel.grid(column = 0, row = 1)
yearLabel = Label(window, text = "Year: " + str(year), font = ("Arial", 10))
yearLabel.grid(column = 0, row = 2)
#population bar
style = ttk.Style()
style.theme_use('default')
if population > 9000000000:
    style.configure("red4.Horizontal.TProgressbar", background='red4')
    bar = Progressbar(window, length=800, style='red4.Horizontal.TProgressbar')
elif population > 8000000000:
    style.configure("red2.Horizontal.TProgressbar", background='red2')
    bar = Progressbar(window, length=800, style='red2.Horizontal.TProgressbar')
elif population > 6000000000:
    style.configure("DarkOrange1.Horizontal.TProgressbar", background='DarkOrange1')
    bar = Progressbar(window, length=800, style='DarkOrange1.Horizontal.TProgressbar')
elif population > 4000000000:
    style.configure("forest green.Horizontal.TProgressbar", background='forest green')
    bar = Progressbar(window, length=800, style='forest green.Horizontal.TProgressbar')
else:
    style.configure("lawn green.Horizontal.TProgressbar", background='lawn green')
    bar = Progressbar(window, length=800, style='lawn green.Horizontal.TProgressbar')
bar['value'] = int((population/maxPopulation) * 100.0)
bar.grid(column=1, row=0)
window.mainloop()






