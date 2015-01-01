from collections import defaultdict
import csv # Comma Seperated Variable Module

"""     
        Updates:
                12/28/2014 - Singly Linked List - Completed and tested, planning on adding Lower Capacity Functionality at a later date
                12/31/2014 - Added Singly Linked Queue Item and Singly Linked Queue, not tested yet, Added Adjacency Array Class

"""

#----------------------------------------------- Classes -----------------------------------------------

# SinglyLinkedListItem Class 
"""     This is a class for a Singly Linked List Item  data structure.  
        It is initialized by OPTIONALLY passing the Head Node, Edge/Arc Cost, the UpperCapacity of the Edge/Arc,
        and the Next List Item.  It is modified code from "VBA Developer's Handbook, 2nd Edition" by Ken Getz 
        and Mike Gilbert, Sybex, 2001. This code was given to me by Professor Steven Charbonneau for the course OR 643
        Network Optimization.  It is adapted from the VBA code for that course. 

        Also used these websites to understand SLLIs in Python :
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
        http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
        http://www.dreamincode.net/forums/topic/211480-python-singly-linked-lists/

        Attributes:        
        .HeadNode = Head Node, the node or list item flow pushed across this arc is directed to; default = None
        .ArcCost = Edge/Arc Cost, this is the cost or impact of pushing flow across this edge/arc; default = None 
        .UpperCapacity = The maximum amount of flow that can be pushed across this edge/arc; default = None
        .NextItem = The List Item or Node that follows this particular node; default  = None       
        
        Methods:
        .SetNextItem - This method allows for the update of the NextItem attribute       

        
"""      
class SinglyLinkedListItem(object):

        def __init__(self, slli_HeadNode = None, slli_ArcCost = None, slli_UpperCapacity = None,  slli_NextItem = None):
                self.HeadNode = slli_HeadNode
                self.ArcCost = slli_ArcCost
                self.UpperCapacity = slli_UpperCapacity
                self.NextItem = slli_NextItem              
        
        def SetNextItem(self, slli_tempHdNode):
                self.NextItem = slli_tempHdNode

        def __Terminate__(self):
                self.NextItem = None 

# SinglyLinkedList Class 
"""     This is a class for a Singly Linked List data structure. It is initialized with no parameters.
        It is modified code from "VBA Developer's Handbook, 2nd Edition" by Ken Getz and Mike Gilbert, 
        Sybex, 2001. This code was given to me by Professor Steven Charbonneau for the course OR 643
        Network Optimization.  It is adapted from the VBA code for that course. 

        Also used these websites to understand SLLs in Python :
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
        http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
        http://www.dreamincode.net/forums/topic/211480-python-singly-linked-lists/

        Attributes:
        .GetListHead - This returns the Singly Linked List Item that is in front of the list
        .Count - The number of Singly Linked List Items in the list

        Methods:
        .IsEmpty - Returns True if no Singly Linked List Items are in the List; False if a Singly Linked List 
                   Item exists in the List
        .AddItem - This method is used to add/create a Singly Linked List Item to/in the the List.  
                   Use:
                        SinglyLinkedListObject.AddItem(EndNode, EdgeCost (Optional), UpperCapacity (Optional), SortTerm (Optional), SortOrder (Optional))
                        Where:
                                EndNode - Head Node, the node or list item flow pushed across this arc is directed to
                                EdgeCost - Edge/Arc Cost, this is the cost or impact of pushing flow across this edge/arc; default = 0 
                                UpperCapacity - The maximum amount of flow that can be pushed across this edge/arc; default = None
                                SortTerm - An indicator of which term we are sorting on
                                                0 = No Sort (not currently used)
                                                1 = Sort on EndNode (Default value)
                                                2 = Sort on EdgeCost
                                SortOrder - An indicator of which way we want to sort the data
                                                "Asc" = Ascending Order (Default Value)
                                                "Desc" = Descending Order
        .Delete - This Method is used to delete a Singly Linked List Item from the List. Returns error if Item is not in the List.
                Use:
                SinglyLinkedListObject.Delete(EndNode)
                Where:
                        EndNode - Head Node, the node or list item flow pushed across this arc is directed to

        Updates:
        12/28/2014 - Completed and tested, planning on adding Lower Capacity Functionality at a later date
"""
class SinglyLinkedList(object): 
      
        def __init__(self):       
                
                self.GetListHead = None
                self.Count = 0         

        def IsEmpty(self):     
                if self.GetListHead.HeadNode is None:
                        return True   
                else:
                        return False  

        def AddItem(self, _EndNode, _EdgeCost = 0, _UpperCapacity = None, _SortTerm = 1, _SortOrder = 'Asc'):                              
                
                _liNew = SinglyLinkedListItem( _EndNode, _EdgeCost, _UpperCapacity)

                _liPrevious = None

                if self.GetListHead == None:                        
                        self.GetListHead = _liNew
                else:
                        _liCurrent = self.GetListHead 
                        if _SortTerm == 0:                        
                                while not _liCurrent is None:
                                        _liPrevious = _liCurrent
                                        _liCurrent = _liCurrent.NextItem                         
                        elif _SortTerm == 1: 
                                if _SortOrder == "Asc":
                                        while not _liCurrent is None:
                                                if _liNew.HeadNode > _liCurrent.HeadNode:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break 
                                else:
                                        while not _liCurrent is None:
                                                if _liNew.HeadNode < _liCurrent.HeadNode:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break  
                        elif _SortTerm == 2:
                                if _SortOrder == "Asc":
                                        while not _liCurrent is None:
                                                if _liNew.ArcCost > _liCurrent.ArcCost:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break 
                                else:
                                        while not _liCurrent is None:
                                                if _liNew.ArcCost < _liCurrent.ArcCost:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break 
                        if _liPrevious == None:
                                _liNew.SetNextItem(self.GetListHead)
                                self.GetListHead = _liNew
                        else:                        
                                _liNew.SetNextItem(_liCurrent)
                                _liPrevious.SetNextItem(_liNew)

                self.Count += 1    
        
        def Delete(self, _TargetedNode):              

                #initialize the variables we will be using
                _liPrevious = None
                _liCurrent = self.GetListHead

                #iterate through the list until we reach the end
                while not _liCurrent is None:
                        if _liCurrent.HeadNode == _TargetedNode:
                                if not _liPrevious is None:
                                        _liPrevious.NextItem = _liCurrent.NextItem
                                else:
                                        self.GetListHead = _liCurrent.NextItem
                                self.Count -= 1                                   
                                break
                        elif _liCurrent is None:
                                raise ValueError("Node not present in Singly Linked List")
                                break
                        else:
                                _liPrevious = _liCurrent
                                _liCurrent = _liCurrent.NextItem  

# SinglyLinkedQueueItem Class
"""     This is a class for a Singly Linked Queue Item (aka Node) data structure.  
        It is initialized by OPTIONALLY passing a Singly Linked Queue Item Node, an Optional Label, 
        and an optional Next List Item.  It is modified code from "VBA Developer's Handbook, 2nd Edition" by Ken Getz 
        and Mike Gilbert, Sybex, 2001. This code was given to me by Professor Steven Charbonneau for the course OR 643
        Network Optimization.  It is adapted by me from the VBA code for that course. 

        Attributes:
                .Node - Singly Linked Queue Item 
                .Label - Optional Data variable; Various Uses but mainly for labeling queue items for Network Modeling
                .NextItem - Pointer to the Next Singly Linked Queue Item 

        Methods:
                .SetNextItem - Method to set a Queue Item's .NextItem attribute
                .SetLabel - Method to set a Queue Items's .Label attribute
"""

class SinglyLinkedQueueItem(object):

        def __init__(self, slqi_Node = None, slqi_Label = None, slqi_NextItem = None):
                self.Node = slqi_Node
                self.Label = slqi_Label 
                self.NextItem = slqi_NextItem             
        
        def SetNextItem(self, slqi_tempHdNode):
                self.NextItem = slqi_tempHdNode

        def SetLabel(self, slqi_tempLabel):
                self.Label = slqi_tempLabel

        def __Terminate__(self):
                self.NextItem = None 

# SinglyLinkedQueue Class
"""      
        This queue class is adapted from VBA code from the course OR 643 Network Optimization. 
        It is a minor modification From 'the "VBA Developer's Handbook, 2nd Edition"
        by Ken Getz and Mike Gilbert  Copyright 2001; Sybex, Inc. All rights reserved. The VBA code 
        was given to me by Professor Steven Charbonneau. It is adapted by me from the VBA code for that course. 

        Attributes:
                .qFront - Pointer to the Queue Item at the front of the queue 
                .qRear - Pointer to the Queue Item at the rear of the queue
                .qCount - Counter that tracks the number of Queue Items in the Queue

        Methods:
                .IsEmpty - Returns boolean True if the Queue is empty and false if it contains a Queue Item
                .Remove - Deletes the Queue Item at the front of the Queue and returns it
                .Add - Adds a Queue Item to a Queue
                        Use:
                                SinglyLinkedQueueObject.Add(Node_Label, Optional Data_Label) 
                                Where:
                                        Node_Label - Integer Node abel
                                        Data_Label - Optional Data Label; Mainly used for labeling nodes in Network
                                                     Optimization Algorithms
          
"""
class SinglyLinkedQueue(object):

        def __init__(self):
                self.qFront = None # Pointer to the front of the queue where items are removed
                self.qRear = None  # Pointer to the rear of the queue where items are added
                self.qCount = 0 # C

        def IsEmpty(self):
                if not self.qFront is None:
                        return False
                elif not self.qRear is None:
                        return False
                else:
                        return True
        
        def Remove(self):
                if self.IsEmpty: # If the queue is empty return None
                        __TempPointer =  None
                else: 
                        __TempPointer = self.qFront
                        if self.qFront is self.qRear: # If there is only one item
                                self.qFront = None
                                self.qRear = None
                        else: # If more than one item
                                self.qFront = self.qFront.NextItem
                self.qCount -= 1
                return __TempPointer    

        def Add( _EndNode, Data_Label = None):
        
                qNew = SinglyLinkedQueueItem( _EndNode, Data_Label) # Create new Queue Item

                if self.IsEmpty: 
                        self.qFront = qNew
                        self.qRear = qNew
                else:
                        self.qRear.SetNextItem(qNew)
                        self.qRear = qNew

                self.qCount += 1

        def __Terminate__(self):
                self.qFront = None
                self.qRear = None
                        
# Adjacency Array Class
"""     
        This is an attempt at making an Adjacency Array class. I call it an Adjacency Array
        because of convention but really my implementation is a Dict of Singly Linked Lists.
        Since the nodes names can be anything it doesn't matter if they are strings. The Tail nodes
        can be dict keys as well.

        Attributes:
                .data - Where the actual adjacency data is stored
                .Count - Returns number of nodes in the network

        Methods:
                .GetAdjacencyArray - Loads the data from a Comma Seperated Value (csv) file into the .data attribute
                        Use:
                                AdjacencyArrayObject.GetAdjacencyArray(filename_arg)
                                Where:
                                        filename_arg - comma seperated data file
                .aPrint - Prints the Adjacency Array 
                        Use:
                                AdjacencyArrayObject.aPrint()                         
      
"""    

class AdjacencyArray(object):     
        
        def __init__(self):
                
                self.data = None

                self.Count = 0

        def GetAdjacencyArray(self, Filename_arg):   

                AdjArray_var = defaultdict(SinglyLinkedList) # For Each New Node Make Them a Singly Linked List

                MyFile = open(Filename_arg, "r")   # Open the file read only

                reader = csv.reader(MyFile) # This grabs the data using the comma seperated values function(?)

                for ParsedLine in reader: # Each row is a parsed list             
                        if len(ParsedLine) == 2:                                        
                                AdjArray_var[ParsedLine[0]].AddItem(ParsedLine[1]) # .AddItem(HeadNode)
                        elif len(ParsedLine) == 3:                        
                                AdjArray_var[ParsedLine[0]].AddItem(ParsedLine[1], int(ParsedLine[2])) # .AddItem(HeadNode, EdgeCost)
                        elif len(ParsedLine) == 4:
                                AdjArray_var[ParsedLine[0]].AddItem(ParsedLine[1], int(ParsedLine[2]), int(Parsed[3])) # .AddItem(HeadNode, EdgeCost, UpperCapacity)
                        else:                        
                                raise ValueError("Error Data Size in Data File Line: ", MyData.index[MyRow])

                self.data = AdjArray_var   

                self.Count = len(AdjArray_var)  

        def aPrint(self):

                MyAdjArray = self.data

                for MyNode in MyAdjArray.keys():             
                        print("Node ", MyNode, ": ", end = " ")
                        MyListItem = MyAdjArray[MyNode].GetListHead
                        while not MyListItem is None:
                                print(MyListItem.HeadNode, end = " ")
                                MyListItem = MyListItem.NextItem        
                        print("\n")          

#----------------------------------------------- Functions ----------------------------------------------- 

# Djikstra's Shortest Path Algorithm using lists
"""    
         Implementation of Djikstra's Shortest Path Algorithm to find the shortest path
        from a Source Node to all other nodes in a network.  This is the most least efficient
        implementation using only Lists """

def SPA_Djikstra(SourceNode_arg, AdjArray_arg):

        # Initializations 
        InfDist = 32000         #This is a VLN (Very Large Number) distance used to set the initial distances of each node; 
                                #It is 32k because of the size limitation of integers 
        
        DistArray_arg = [[InfDist] for nodes in AdjArray_arg.keys()]   # Distance(i) = VLN for all i in N
        PredArray_arg = [[-1] for nodes in AdjArray_arg.keys()]        # Pred(i) = -1 for all i in N   
        S = SinglyLinkedList()   # S = {} 
        S_Prime = SinglyLinkedList()                                                               
        for nodes in AdjArray_arg.keys():  # S' = N              
                S_Prime.AddItem(nodes)

        #S_Prime = [int(i) for i in S_Prime]
        
        DistArray_arg[SourceNode_arg] = 0       # Distance(Source) = 0
        PredArray_arg[SourceNode_arg] = 0       # Predecessor(Source) = 0
               
        while S.Count < AdjArray_arg.Count:       # Main Loop
                i = 0 
                # Find the smallest Distance in S'
                MyListItem = S_Prime.GetListHead
                MyMinItem = MyListItem
                while i <= S_Prime.Count:
                        if DistArray_arg[MyListItem.HeadNode] < DistArray_arg[MyMinItem.HeadNode]:
                                MyMinItem = MyListItem
                        i += 1
                        MyListItem = S_Prime.NextItem         
                print(MyMinItem)
                                
                
        return DistArray_arg, PredArray_arg    

         
 
