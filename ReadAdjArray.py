# This File Inputs an adjaceny list from a file and returns a list of lists
# The data must be in the form :
""" n,0; i1, j1; i2, j2; etc. """
#As of now this only works on arcs and doesn't work with costs and capacities

#import sys
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
                
def Djikstra_CJM(SourceNode_arg, AdjArray_arg):
        """     Implementation of Djikstra's Shortest Path Algorithm to find the shortest path
                from a Source Node to all other nodes in a network.  This is the most least efficient
                implementation using only Lists"""

        # Initializations 
        InfDist = 32000         #This is a VLN (Very Large Number) distance used to set the initial distances of each node; 
                                #It is 32k because of the size limitation of integers 
        DistArray_arg = [[InfDist] for i in range(len(AdjArray_arg))]   # Distance(i) = VLN for all i in N
        PredArray_arg = [[-1] for i in range(len(AdjArray_arg))]        # Pred(i) = -1 for all i in N   
        S = gList()        
        S_Prime = gList()                                                         # S = {}        
        for i in range(len(AdjArray_arg)):               # S' = N
                S_Prime.AddItem(i)

        #S_Prime = [int(i) for i in S_Prime]
        
        DistArray_arg[SourceNode_arg] = 0       # Distance(Source) = 0
        PredArray_arg[SourceNode_arg] = 0       # Predecessor(Source) = 0
               
        while S.Count < len(AdjArray_arg):       # Main Loop
                i = 0 
                # Find the smallest Distance in S'
                MyListItem = S_Prime.GetListHead
                MyMinItem = MyListItem
                while i <= len(S_Prime):
                        if DistArray_arg[MyListItem.HeadNode] < DistArray_arg[MyMinItem.HeadNode]:
                                MyMinItem = MyListItem
                        i += 1
                        MyListItem = S_Prime[i]          
                print(MyMinItem)
                                
                
        return DistArray_arg, PredArray_arg
        

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

        Distance, Predecessor = Djikstra_CJM(Source,MyAdjArray)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])


