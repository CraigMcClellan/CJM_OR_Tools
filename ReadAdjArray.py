# This File Inputs an adjaceny list from a data file and returns a list of Singly Linked Lists
#Help from - http://pymotw.com/2/csv/ 
# The data must be in the form :
""" n,0; i1, j1; i2, j2; etc. """
#As of now this only works on arcs and doesn't work with costs and capacities

import csv # Comma Seperated Variable Module
from CJM_OR_Tools import *
from collections import defaultdict
"""
from collections import defaultdict
frequencies = defaultdict(int)
for word in wordlist:
    frequencies[word] += 1 """
#def class AdjArray(object):
        
       # def __init__(self):
                
        

def GetAdjArray(Filename_arg):   

        AdjArray_var = defaultdict(SinglyLinkedList) # For Each New Node Make Them a Singly Linked List

        MyFile = open(Filename_arg, "r")   # Open the file read only

        reader = csv.reader(MyFile) # This grabs the data using the comma seperated values function(?)

        for ParsedLine in reader: # Each row is a parsed list             
                if len(ParsedLine) == 2:                                        
                        AdjArray_var[ParsedLine[0]].AddItem(int(ParsedLine[1])) # .AddItem(HeadNode)
                elif len(ParsedLine) == 3:                        
                        AdjArray_var[ParsedLine[0]].AddItem(int(ParsedLine[1]), int(ParsedLine[2])) # .AddItem(HeadNode, EdgeCost)
                elif len(ParsedLine) == 4:
                        AdjArray_var[ParsedLine[0]].AddItem(int(ParsedLine[1]), int(ParsedLine[2]), int(Parsed[3])) # .AddItem(HeadNode, EdgeCost, UpperCapacity)
                else:                        
                        raise ValueError("Error Data Size in Data File Line: ", MyData.index[MyRow])

        return AdjArray_var

def main() :
        """
        Source = 1

        MyAdjArray = GetAdjArray("Network1.dat")
        
        print("\n")

        for MyNode in MyAdjArray.keys():             
                print("Node ", MyNode, ": ", end = " ")
                MyListItem = MyAdjArray[MyNode].GetListHead
                while not MyListItem is None:
                        print(MyListItem.HeadNode, end = " ")
                        MyListItem = MyListItem.NextItem        
                print("\n")
        """

        MyAdjArray = AdjacencyArray()

        MyAdjArray.GetAdjacencyArray("Network1.dat")

        MyAdjArray.aPrint()

        print("Count: ", MyAdjArray.Count)
                

        #Distance, Predecessor = SPA_Djikstra(Source, MyAdjArray)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])


