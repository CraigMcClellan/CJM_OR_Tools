from CJM_OR_Tools import *

# Program Runs Stuff

def main():

        XArray = AdjacencyArray()

        XArray.GetAdjacencyArray('Network1.dat')

        XArray.aPrint()

        print("Count :=", XArray.Count)

        print("\n \n")

        SourceNode = "1"

        Dist_Array, Pred_Array = SPA_Djikstra(SourceNode, XArray)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])
