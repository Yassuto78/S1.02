from sage.all import *
def readFile(filename):
    x = []
    y = []
    with open(filename) as f:
        for line in f:
            tmp=line.split()
            x.append(float(tmp[0])/1000)
            y.append(float(tmp[1]))
    return x,y

test1_comparaison =[{
    "name": "stdsort",
    "file": "../data/stdsort1.data",
    "color": "red"
    },
    {
    "name": "stable_sort",
    "file": "../data/stable_sort1.data",
    "color": "blue"
    }]
test2_comparaison =[{
    "name": "stdsort",
    "file": "../data/stdsort2.data",
    "color": "red"
    },
    {
    "name": "stable_sort",
    "file": "../data/stable_sort2.data",
    "color": "blue"
    }]
tests_std_sort=[{
    "name": "test1",
    "file": "../data/stdsort1.data",
    "color": "red"
    },
    {
    "name": "test2",
    "file": "../data/stdsort2.data",
    "color": "blue"
    },
    {
    "name": "test3",
    "file": "../data/stdsort3.data",
    "color": "yellow"
    }]
tests_std_stable_sort=[{
    "name": "test1",
    "file": "../data/stable_sort1.data",
    "color": "red"
    },
    {
    "name": "test2",
    "file": "../data/stable_sort2.data",
    "color": "blue"
    },
    {
    "name": "test3",
    "file": "../data/stable_sort3.data",
    "color": "yellow"
    }]
ensemble_tests = [
    {
    "titre": "comparaison des performances de std::sort",
    "tests": tests_std_sort,
    "output": "../data/stdsort.png"
    },
    {
    "titre": "comparaison des performances de std::stable_sort",
    "tests" : tests_std_stable_sort,
    "output": "../data/stable_sort.png"
    },
    {
    "titre": "comparaison des performances des differents algorithmes lors du test1",
    "tests": test1_comparaison,
    "output": "../data/comaparaison_test1.png"
    },
    {
    "titre": "comparaison des performances des differents algorithmes lors du test2",
    "tests": test2_comparaison,
    "output": "../data/comaparaison_test2.png"
    }]
for ensemble in ensemble_tests:
    plot = Graphics()
    for test in ensemble["tests"]:
        x,y = readFile(test["file"])
        plot+= line(zip(x,y),rgbcolor=test["color"])+point(zip(x,y),rgbcolor=test["color"])
    plot.save(ensemble["output"])