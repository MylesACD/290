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

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
master = Tk()
master.geometry("300x300")

g = Graph()
j = Graph()



print("graph has {} statements.".format(len(j)))


def selectFile():
    master.fileName = filedialog.askopenfilename(filetypes=(("turtle files", ".ttl"), ("All files", "*")))
    g.parse(master.fileName, format="turtle")
    print("done parsing")


def closeWindows():
    exit()


def visualize():
    n = 0
    for triple in g:
        if n < c:
            j.add(triple)
            n += 1
        else:
            break
    stream = io.StringIO()
    rdf2dot(j, stream, opts={display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    dg.write_svg("test" + str(c) + ".svg")
    url = "C:/Users/Myles/Documents/GitHub/290/test" +str(c) +".svg"
    webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)



def tripleCount():
    global c
    c = tkinter.simpledialog.askinteger("Data","How many triples do you want to read?")


output = Label(master, text="Simulation Visualizer")
output.pack()

button3 = Button(master, text="Select File", command=selectFile)
button3.pack()

button4 = Button(master, text="Triple Count", command=tripleCount)
button4.pack()

button = Button(master, text="Graph Data", command=visualize)
button.pack()

button2 = Button(master, text="Quit", command=closeWindows)
button2.pack()

mainloop()
