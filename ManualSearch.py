import rdflib
from rdflib import Graph
import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

g = Graph()
j = Graph()
n=0
g.parse("SugarScape.ttl", format="turtle")
    # loop through each triple in the graph (subj, pred, obj)


    #"vDist_read#id=baed4b73-b7b6-4f01-a7be-60d567c76641")

    # if subj == 'file:///C:/Users/Myles/PycharmProjects/untitled/vDist_read#id=baed4b73-b7b6-4f01-a7be-60d567c76641':
    #     j.add([subj,pred,obj])

for triple in g:
     if n==15000:
         j.add(triple)
         n=0
     else:
         n+=1

print("graph has {} statements.".format(len(j)))




def visualize(g):

    stream = io.StringIO()
    rdf2dot(g, stream, opts = {display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    dg.write_svg("test.svg")

visualize(j)
