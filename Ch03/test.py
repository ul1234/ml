from trees import *
from treePlotter import *


fr = open('lenses.txt')
lenses = [line.strip().split('\t') for line in fr.readlines()]
lenses_label = ['age', 'prescript', 'astigamic', 'tearRate']
lenses_tree = createTree(lenses, lenses_label)
print lenses_tree
storeTree(lenses_tree, 'tree.txt')

t = grabTree('tree.txt')
createPlot(t)
