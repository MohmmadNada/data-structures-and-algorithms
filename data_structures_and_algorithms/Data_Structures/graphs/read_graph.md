# Graphs
<!-- Short summary or background information -->
A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.


## Challenge
<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:
add node
add edge
get nodes
get neighbors
size

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
all of methods work with Efficiency O(1)

## API
<!-- Description of each method publicly available in your Graph -->
Classes : 
1. Vertix : container with value 
   1. have str return value 
2. Edges : link between the vertices 
3. Graph :
   1.  init => dict  .
   2.  add_vertix(value ) : add new vertix to graph
   3.  add_adge (from , to ): Adds a new edge between two vertices, and check if the nodes exist in the graph
   4. get_vertix : returns all of the nodes in the graph as a collection list
   5. get_neighbors(sourceVertix):Returns a collection of edges connected to the given node
   6. size:Returns the total number of nodes
