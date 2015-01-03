from CJM_OR_Tools import *

# Program Runs Stuff

def main():
        

        XArray = AdjacencyArray()

        XArray.GetAdjacencyArray('Network2.dat')

        #XArray.aPrint()

        #print("Count :=", XArray.Count)

        print("\n \n")

        MySourceNode = "8"

        Dist_Array, Pred_Array = SPA_Djikstra(MySourceNode, XArray)

        print("----------- Results ---------- \n \n")
        for node in XArray.data.keys():
                print("From Node ", MySourceNode," to Node(", node, ") - Dist:", Dist_Array[node]," Pred:", Pred_Array[node])

        """        
        X = SinglyLinkedList()

        X.AddItem("1")
        
        X.AddItem("2")

        X.AddItem("3")

        X.sPrint()
        print("lsthead: ", X.GetListHead.HeadNode)

        X.Delete("1")

        X.sPrint()
        print("lsthead: ", X.GetListHead.HeadNode)
        """
                

        


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])
