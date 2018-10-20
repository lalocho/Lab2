class Node(object):
 item = -1
 next = None
 def __init__(self, item, next):
    self.item = item
    self.next = next
# create a method that will load both of the .txt files and that creates a single linked list out of them
def getIDs(filename1,filename2):
    """ 
    Gets the ID's from both of the files and returns a linked list that contains all of them

    Parameters:
        filename1: name of the first file that contains ID's
        filename2: name of the second file that contains ID's
    Returns :
        Returns the first node of the created linked list that contains all of the ID's
        from both of the files
    """
    root = None
    with open(filename1)as file:
        for line in file:
            value = int(line)
            root = Node(value,root)
    with open(filename2)as file:
        for line in file:
            value = int(line)
            root = Node(value,root)
    return root

def Sol1 (root):
    """
    Travels through a linked list and Checks to see if there are any duplicate values
    This is done using nested while loops. If any duplicate values are found a message
    is printed indicating so.

    Parameters:
        root: root of the linked list to be sorted.
    Returns :
        returns nothing
    """
     helper = root.next
     while root.next is not None: 
        while helper is not None:
            if helper.item == root.item:
                print(helper.item," has a duplicate")
            helper = helper.next
        root =root.next
        helper = root.next

def Sol2 (root):
    """

    Firstly the linked list provided is sorted using bubble sort
    After having been sorted Each item in the table is compared
    to the next item in the table if they are equal then a message
    is printed to indicate that there exist more than one node with
    that particulare value

    Parameters:
        root: root of the linked list
    Return:
        returns nothing
    """ 
    swaps =  0
    Leading = root.next
    Laging = root
    while swaps is not -1:  
        while Leading is not None:
            if Laging.item > Leading.item:
                Laging.item,Leading.item = Leading.item, Laging.item
                swaps+=1
            Leading = Leading.next
            Laging = Laging.next
        if swaps > 0:
            Leading = root.next
            Laging = root
            swaps = 0
        else:
            swaps = -1
    Leading = root
    while Leading.next is not None:
        if Leading.item == Leading.next.item:
            print(Leading.item," has a duplicate")
        Leading = Leading.next 



def Merge(a,b):
    """
    Takes two sorted linked lists and merges them into a single sorted linked list

    Parameters:
        a: first sorted linked list
        b: second sorted linked list
    Returns:
        Pointerlist: sorted linked list that contains all the elements in linked list a and b
    """
    PointerA = a
    PointerB = b
    Pointerlist = None
    while PointerA is not None and PointerB is not None:
        if PointerA.item <= PointerB.item:
            Pointerlist = Node(PointerA.item,Pointerlist)
            PointerA = PointerA.next
        else:
            Pointerlist = Node(PointerB.item,Pointerlist)
            PointerB = PointerB.next
    if PointerA is None:
        while PointerB is not None:
            Pointerlist = Node(PointerB.item,Pointerlist)
            PointerB = PointerB.next
    if PointerB is None:
        while PointerA is not None:
            Pointerlist = Node(PointerA.item,Pointerlist)
            PointerA = PointerA.next
    return Pointerlist
       
def Mergesort(root):
    """
    Sorts a linked list using mergesort algorithm
    
    Parameters:
        root: root of linked list
    Returns:
        sortedList: first node of a sorted linked list
    """
    if root is None or root.next is None :
        return root
    Head = root 
    Lagging = Head
    Leading = Head
    while  Leading.next.next is not None:
        Lagging = Lagging.next
        Leading = Leading.next.next
        if Leading is None or Leading.next is None : 
            break
#        if Leading is not None: 
#            Leading = Leading.next
    Rightmiddle = Lagging.next
 #   middle = MiddleLL(Head)
 #   Rightmiddle = middle.next
#    while Head is not None:
#        print(Head.item)
#        Head = Head.next
    Lagging.next = None
    LeftHalf = Mergesort(Head)
    RightHalf = Mergesort(Rightmiddle)
    sortedlist = Merge(LeftHalf, RightHalf)
    return sortedlist

def Sol3(root):
    """
    Sorts linked list through recursive mergesort. Then Traverses linked list and
    compares current item with next item and if they match a message is printed
    to indicate so.

    Parameters:
        root: root of linked list
    Return:
        returns nothing
    """
    Sortedlist =Mergesort(root)
    Leading = Sortedlist
    while Leading.next is not None:
        print(Leading.item)
        if Leading.item == Leading.next.item:
            print(Leading.item," has a duplicate")
        Leading = Leading.next    


def GetMax(root):
    """ 
    Returns the max value found in a linked List

    Parameters:
        root: Root of a linked list
    Returns:
        max: largest integer value found in the linked list
    """

    max = root.item
    while root!= None:
        if max < root.item:
            max = root.item
        root = root.next
    return max

def Sol4(root):
    """
    Creates a list "seen" that is 1 larger than the largest element found in the given linked list
    The initial value found in all members of the list is false. The given linked list is
    traversed and if the current item in the list has not been seen before(seen[current item ] ==false)
    then seen[current item] is updated to true. If however the item has been seen then a message is printed
    to indicate so.

    Parameters:
        root: root of a linked list
    Returns:
        returns nothing
    """
    m = GetMax(root)
    seen = [False]*(m+1)
    helper = root
    while helper is not None:
        if seen[helper.item] == True:
            print(helper.item," has a duplicate")
        else:
            seen[helper.item] = True
        helper = helper.next
    
file_name1 = str(input("Enter the name of the first file that contains ID's: ")) # activision.txt
file_name2 = str(input("Enter the name of the second file that contains ID's: ")) # vivendi.txt
root = getIDs(file_name1,file_name2)
#Sol1(root)
#Sol2(root)
#Sol3(root)
Sol4(root)
