# This File Inputs an adjaceny list from a file and returns a list of lists
# The data must be in the form :
""" n,0; i1, j1; i2, j2; etc. """
#As of now this only works on arcs and doesn't work with costs and capacities

import sys
#sys.path.append('\Users\Craig\Documents\Python\MyProgs')#'/ufs/guido/lib/python')
#PYTHONPATH=$PYTHONPATH:C:\Users\Craig\Documents\Python\MyProgs
import CJM_OR_Tools

def GetAdjArray(NodeCount_arg, Filename_arg):

        Flag_var = -1

        # Initializing Adjaceny Array
        AdjArray_arg = [[Flag_var] for i in range(NodeCount_arg + 1)]    

        with open(Filename_arg, "r") as MyFile:         # This is similar to the VBA with for files  
          
                # Reading in data and building the adjacency array 
                AllData = MyFile.readlines()      
        
        for MyLine in AllData: 
                ReadStuff = MyLine.split(",")         
                i = int(ReadStuff[0])        
                j = int(ReadStuff[1]) 
                if AdjArray_arg[i].count(Flag_var) > 0: # If it is empty
                        AdjArray_arg[i].append(j)                        
                        AdjArray_arg[i].remove(Flag_var) 
                        #AdjArray_arg[i] = j
                else:                         
                        AdjArray_arg[i].append(j)   # If it isn't empty add arc to the end  

        return AdjArray_arg    

def main() :

        NodeCount = 9
        Source = 1

        MyAdjArray = GetAdjArray(NodeCount, "Network1.dat")
        
        index = 0 
        print("")
        for nodes in MyAdjArray:   
                if index != 0:              
                        print("Node %d :" % index, end = " ")
                        for arc in range(len(MyAdjArray[index])):
                                print(MyAdjArray[index][arc], end = " ")
                        print("\n")      
                index += 1

        Distance, Predecessor = SPA_Djikstra(Source, MyAdjArray)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])


