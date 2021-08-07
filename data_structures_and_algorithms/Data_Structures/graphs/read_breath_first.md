
# Challenge Summary
<!-- Description of the challenge -->
Write the following method for the Graph class:

breadth first
Arguments: Node
Return: A collection of nodes in the order they were visited.
Display the collection
## Whiteboard Process
<!-- Embedded whiteboard image -->
![IMAGE1](/img/CC36/Capture.PNG)
![IMAGE1](/img/CC36/Capture2.PNG)
![IMAGE1](/img/CC36/Capture3.PNG)
![IMAGE1](/img/CC36/Capture4.PNG)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time : O-n*n
Space : O -n
## Solution
<!-- Show how to run your code, and examples of it in action -->
core code
```
def BreadthFirst(self,startVertix):
        
        if  startVertix not in self.adjacency_list :
            raise KeyError('The vertix is not in Graph ')
        nodes = []
        breadth = Queue()
        visited= set()
        breadth.enqueue(startVertix)
        visited.add(startVertix)
        while breadth.front != None:
            parentVertix=breadth.dequeue()
            nodes.append(parentVertix) 
            childVertices= self.adjacency_list[parentVertix]
            for child in childVertices:
                childVertix=list(child.keys())[0]
                if childVertix not in visited:
                    visited.add(childVertix)
                    breadth.enqueue(childVertix)
        return nodes
```
[code](./graph.py)
> Note : the test for this Code Challenge under line 70 
[test](./test_graph.py)
