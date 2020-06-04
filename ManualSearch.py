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

#Generate GUI window
master = Tk()
master.geometry("300x300")

g = Graph()
j = Graph()

#Opens file explorer so user can select turtle file to parse from any path. Parses the entire file into a holder graph g
def selectFile():
    master.fileName = filedialog.askopenfilename(filetypes=(("turtle files", ".ttl"), ("All files", "*")))
    g.parse(master.fileName, format="turtle")
    print("done parsing")

#exit the application
def closeWindows():
    exit()


def visualize():
    j=Graph()
    l=0
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

    # #add any triples from g where the current objects in j are subjects
    # for s, p, o in j.triples((None, None, None)):
    #         for q, w, e in g.triples((o, None, None)):
    #             if s is not e:
    #                 j.add((q, w, e))

    #creates the graph visually and saves it as an svg file
    stream = io.StringIO()
    rdf2dot(j, stream, opts={display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    dg.write_svg("graph" + str(c) + ".svg")
    #once complete the graph is automatically opened in chrome
    url = "C:/Users/Myles/Documents/GitHub/290/graph" +str(c) +".svg"
    webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)



def subjectNumber():
    global c
    c = tkinter.simpledialog.askinteger("Data","Which subject do you want select")


output = Label(master, text="Simulation Visualizer")
output.pack()

button3 = Button(master, text="Select File", command=selectFile)
button3.pack()

button4 = Button(master, text="subjectNumber", command=subjectNumber)
button4.pack()

button = Button(master, text="Graph Data", command=visualize)
button.pack()

button2 = Button(master, text="Quit", command=closeWindows)
button2.pack()

mainloop()
