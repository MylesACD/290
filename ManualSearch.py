import tkinter
from tkinter import filedialog
from rdflib import Graph
from tkinter import *
from tkinter import simpledialog
import io
import pydotplus
from IPython.display import display
from rdflib.tools.rdf2dot import rdf2dot
import os
import webbrowser
import pathlib
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#Generate GUI window
master = Tk()
master.geometry("300x300")

g = Graph()
j = Graph()

#Opens file explorer so user can select turtle file to parse from any path. Parses the entire file into a holder graph g
def selectFile():
    try:
        master.fileName = filedialog.askopenfilename(filetypes=(("turtle files", ".ttl"), ("All files", "*")))
        print("Parsing file please wait")
        g.parse(master.fileName, format="turtle")
        print("done parsing")
    except:
        print("Invalid file selection, parsing incomplete")

#exit the application
def closeWindows():
    os.system("TASKKILL /F /IM ManualSearch.exe")
    exit()


def visualize():
    try:
        j=Graph()
        l=0
        #iterate through g until the subject number specified by user is found
        for s in g.subjects():
            if l == c:
                selectedR = s
                break
            l+=1
        #add all triples in g that have the selected resource as their subject and add to j
        for s, p, o in g.triples((selectedR, None, None)):
            j.add((s, p, o))
        #add all triples in g that have the selected resource as their object and add to j
        for s, p, o in g.triples((None, None,selectedR)):
            #check if  this relationship is already detailed in j
            if not j.__contains__((None, None, s)):
                j.add((s, p, o))

        #creates the graph visually and saves it as an svg file
        stream = io.StringIO()
        rdf2dot(j, stream, opts={display})
        dg = pydotplus.graph_from_dot_data(stream.getvalue())
        dg.write_svg("graph"+str(c)+".svg")
        print("Graph saved")
        #once complete the graph is automatically opened in chrome
        url = str(pathlib.Path().absolute())+"/graph" +str(c) +".svg"
        webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    except:
        print("unable to create graph")


def subjectNumber():
    global c
    c = tkinter.simpledialog.askinteger("Data","Which subject do you want select")


output = Label(master, text="Simulation Visualizer")
output.pack()

button3 = Button(master, text="Select File", command=selectFile)
button3.pack()

button4 = Button(master, text="Subject Number", command=subjectNumber)
button4.pack()

button = Button(master, text="Graph Data", command=visualize)
button.pack()

button2 = Button(master, text="Quit", command=closeWindows)
button2.pack()

mainloop()
