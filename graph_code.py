import enum
from pyvis.network import Network
import grouping_code as gc
import random

net = Network()
data = [] #gc.main()

for num,node in enumerate(data):
    #Make node a random color for visual clarity
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]

    net.add_node(num, label='Person' + str(num),color=hex_number)

for person,node in enumerate(data):
    for index,entry in enumerate(node):
        net.add_edge(person,index,value=entry)




#net.show('nodes.html') >:(