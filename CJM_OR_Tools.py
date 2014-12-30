#----------------------------------------------- Classes -----------------------------------------------

# SinglyLinkedListItem Class 
"""     This is a class for a Singly Linked List Item (aka Node) data structure.  
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

        Updates:
        12/28/2014 - Completed and tested, planning on adding Lower Capacity Functionality at a later date
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
        Option Explicit
'This queue class is a minor modification From
'the "VBA Developer's Handbook, 2nd Edition"
' by Ken Getz and Mike Gilbert
' Copyright 2001; Sybex, Inc. All rights reserved.

' Queue class.

'Initialize the objects we need to make the queue work
Private qFront As QueueItem 'create the front of the queue (where things are removed)
Private qRear As QueueItem  'create the back of the queue (where things are added)
Private qCount As Integer

'Call this sub when adding a new item to the queue.  This routine takes two arguments
'Node: an integer variable that represents the node we are looking for
'Label: a variant variable that accepts any type of argument.  This might be a text or number
Public Sub Add(Node As Integer, Optional Label As Variant = Null)
    Dim qNew As QueueItem
    Set qNew = New QueueItem
    
    qNew.Node = Node    'assign the node value to the queue item
    qNew.Label = Label  'assign the label value to the queue item
    
    'If the queue is empty, need to make sure we poit both the front and the rear of the queue to itself
    If IsEmpty Then     'call the function that determines if the queue is empty
        Set qFront = qNew   'point the front of the queue to the item we just added
        Set qRear = qNew    'point the rear of the queue to the item we just added
    Else    'There are other items in the queue, put the new item in the back
        Set qRear.NextItem = qNew   'point the previous last item to the new item
        Set qRear = qNew            'make the new item the back of the queue
    End If
    qCount = qCount + 1
    
End Sub

'Sometimes you may just want to see what is at the front of the queue without removing it.
'This function allows you to do that.  It lets you look at the front element in the queue.
'It returns nothing if the queue is empty
Public Property Get QueueFront() As QueueItem
    If IsEmpty Then 'make sure the queue is not empty
        Set QueueFront = Nothing  'if it is, then set the function value equal to nothing
    Else    'it isn't empty
        Set QueueFront = qFront   'set the function value equal to the front of the queue
    End If
End Property


'This function removes the front of the queue and returns the actual queueitem so you can use its components
'it is not required to recieve the return of the queue when you remove it.
Public Function Remove() As QueueItem
    
    'Check to see if the item is empty, if it is, then return a nothing value
    If IsEmpty Then
        Set Remove = Nothing
    Else    'The queue is not empty
        Set Remove = qFront 'assign the queue item pointer to the function
        'check to make sure we are not removing the only item in the queue
        If qFront Is qRear Then 'if so then do the following
            Set qFront = Nothing    'point the front to nothing
            Set qRear = Nothing     'point the back to nothing
        Else    'it isn't the only item
            Set qFront = qFront.NextItem    'make next item the front of the queue
                                            'this is where/how the first item in the queue gets removed
        End If
        qCount = qCount - 1
    End If
End Function

'This is a property of a queue.  It returns true if the queue is empty
Property Get IsEmpty() As Boolean
    'If both q front and rear are empty, this line evaluates to true
    IsEmpty = ((qFront Is Nothing) And (qRear Is Nothing))
End Property

Private Sub Class_Initialize()
    ' Make the queue appear empty.
    Set qFront = Nothing
    Set qRear = Nothing
End Sub

Private Sub Class_Terminate()
    ' Release memory used by the queue.
    Set qFront = Nothing
    Set qRear = Nothing
End Sub

'This is a property that tells you how many elements are in the queue.  This is convenient
'in that you don't have to iterate across the entire queue to find the answer, it keeps count
'dont know if this will ever find any use.  The state of most interest is when it is empty
'and we already have a property for that.
Public Property Get Count() As Integer
    'Assign the value of deqCount to the property
    Count = qCount
End Property
"""
def SinglyLinkedQueue(object):

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
                self.qCount -=
                return __TempPointer    

        def Add( _EndNode, Data_Label = None)
        
                qNew = SinglyLinkedQueueItem() 

Public Sub Add(Node As Integer, Optional Label As Variant = Null)
    Dim qNew As QueueItem
    Set qNew = New QueueItem
    
    qNew.Node = Node    'assign the node value to the queue item
    qNew.Label = Label  'assign the label value to the queue item
    
    'If the queue is empty, need to make sure we poit both the front and the rear of the queue to itself
    If IsEmpty Then     'call the function that determines if the queue is empty
        Set qFront = qNew   'point the front of the queue to the item we just added
        Set qRear = qNew    'point the rear of the queue to the item we just added
    Else    'There are other items in the queue, put the new item in the back
        Set qRear.NextItem = qNew   'point the previous last item to the new item
        Set qRear = qNew            'make the new item the back of the queue
    End If
    qCount = qCount + 1
    
End Sub 
     
                        
                

#----------------------------------------------- Functions ----------------------------------------------- 

def SPA_Djikstra(SourceNode_arg, AdjArray_arg):
        """     Implementation of Djikstra's Shortest Path Algorithm to find the shortest path
                from a Source Node to all other nodes in a network.  This is the most least efficient
                implementation using only Lists"""

        # Initializations 
        InfDist = 32000         #This is a VLN (Very Large Number) distance used to set the initial distances of each node; 
                                #It is 32k because of the size limitation of integers 
        DistArray_arg = [[InfDist] for i in range(len(AdjArray_arg))]   # Distance(i) = VLN for all i in N
        PredArray_arg = [[-1] for i in range(len(AdjArray_arg))]        # Pred(i) = -1 for all i in N   
        S = SinglyLinkedList()   # S = {} 
        S_Prime = SinglyLinkedList()                                                               
        for i in range(len(AdjArray_arg)):  # S' = N              
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

         

def main():

        x = SinglyLinkedList()

        x.AddItem(1, 32,None,2)

        x.AddItem(2, 15,None,2)

        x.AddItem(3, 23,None,2)

        y = x.GetListHead

        while not y is None:

                print("Node: ", y.HeadNode, "\n")
        
                y = y.NextItem

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()           
