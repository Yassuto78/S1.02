from sage.all import *
import numpy as np #crée un alias pour numpy

def readFile(filename):
    x = []
    y = []
    with open(filename) as f:
        for line in f:
            tmp=line.split()
            x.append(float(tmp[0]))
            y.append(float(tmp[1]))
    return x,y

algorithmes_rapides =[{
    "name": "stdsort_vecteur1",
    "file": "../data/stdsort1.data",
    "color": "red"
    },
    {
    "name": "stdsort_vecteur2",
    "file": "../data/stdsort2.data",
    "color": "blue"
    },
    {
    "name": "stdsort_vecteur3",
    "file": "../data/stdsort3.data",
    "color": "green"
    },
    {
    "name": "stable_sort_vecteur1",
    "file": "../data/stable_sort1.data",
    "color": "purple"
    },
    { "name": "stable_sort_vecteur2",
    "file": "../data/stable_sort2.data",
    "color": "pink"
    },
    {"name": "stable_sort_vecteur3",
    "file": "../data/stable_sort3.data",
    "color": "gray"
    },
    {
    "name": "quicksort_vecteur1",
    "file": "../data/quicksort1.data",
    "color": "yellow"
    },
    {
    "name": "v2quicksort_vecteur1",
    "file": "../data/v2quicksort1.data",
    "color": "orange"
    },
    {
    "name": "v2quicksort_vecteur2",
    "file": "../data/v2quicksort2.data",
    "color": "gold"
    },
    {
    "name": "v2quicksort_vecteur3",
    "file": "../data/v2quicksort3.data",
    "color": "magenta"
    }
    ]
algorithmes_lents =[
    {"name": "selection_sort_vecteur1",
    "file": "../data/selection_sort1.data",
    "color": "yellow"
    },
    {"name": "selection_sort_vecteur2",
    "file": "../data/selection_sort2.data",
    "color": "blue"
    },
    {"name": "selection_sort_vecteur3",
    "file": "../data/selection_sort3.data",
    "color": "red"
    },
    {"name": "qsort_vecteur1",
    "file": "../data/qsort1.data",
    "color": "green"
    },
    {"name": "qsort_vecteur2",
    "file": "../data/qsort2.data",
    "color": "pink"
    },
    {"name": "qsort_vecteur3",
    "file": "../data/qsort3.data",
    "color": "purple"
    },
    {"name": "insertion_sort_vecteur1",
    "file": "../data/insertion_sort1.data",
    "color": "brown"
    },
    {"name": "insertion_sort_vecteur2",
    "file": "../data/insertion_sort2.data",
    "color": "gold"
    },
    {"name": "insertion_sort_vecteur3",
    "file": "../data/insertion_sort3.data",
    "color": "cyan"
    },
    {"name": "bubble_sort_vecteur1",
    "file": "../data/bubble_sort1.data",
    "color": "orange"
    },
    {"name": "bubble_sort_vecteur2",
    "file": "../data/bubble_sort2.data",
    "color": "magenta"
    },
    {"name": "bubble_sort_vecteur3",
    "file": "../data/bubble_sort3.data",
    "color": "gray"
    },
    {
    "name": "quicksort_vecteur2",
    "file": "../data/quicksort2.data",
    "color": "aqua"
    },
    {"name": "quicksort_vecteur3",
    "file": "../data/quicksort3.data",
    "color": "blanchedalmond"
    },
    ]
comparaisons = [
    {"titre": "algorithmes rapides",
    "tests": algorithmes_rapides,
    "output": "../data/algorithmes_rapides.png"
    },
    {"titre": "algorithmes lents",
    "tests": algorithmes_lents,
    "output": "../data/algorithmes_lents.png"
    }]
for ensemble in comparaisons:
    plot = Graphics()
    for test in ensemble["tests"]:
        x,y = readFile(test["file"])
        if len(x)==100:
            m = 5
        else:
            m = 1
        np_x = np.array(x)
        np_y = np.array(y)
        np_moy_x = np_x.reshape(-1,m).mean(axis=1)
        np_moy_y = np_y.reshape(-1,m).mean(axis=1)
        plot+= line(zip(np_moy_x,np_moy_y),rgbcolor=test["color"],legend_label=test["name"])
        #plot+=point(zip(x,y),rgbcolor=test["color"])
    plot.axes_labels_size(1)
    plot.axes_labels(['nombres elements x1000','temps execution (ms)'])
    plot.set_legend_options( loc='best')
    #plot.title(ensemble["titre"])
    plot += text(ensemble['titre'], (60,-1000), fontsize=12, color='black')
    plot.legend(True)
    plot.save(ensemble["output"],figsize =[Integer(10),Integer(5)])