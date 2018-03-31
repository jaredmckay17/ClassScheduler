# ClassScheduler
This Python program reads in a JSON file with course names and associated with a list of prerequisite courses and prints a course schedule based off the following conditions:

- All of the courses provided in the JSON file will be output to standard output. 
- Courses with prerequisite courses must appear in standard output after those prequisite courses (essentially creating a 'schedule' of how courses should be taken for a student).

## How to Use
The Python file itself is invoked by a Bash script provided aptly named 'scheduler' and by passing a JSON file as a parameter to that Bash script in the following format:

- Each object in the JSON file has these keys: 
    - name (type string, must be provided and cannot be None) 
    - pre-requisites (list of strings, must be provided and cannot be None but can be an empty list)

The output of the Bash script execution (with the input parameter of the JSON file) will be similar to the following output:

```
Algebra 1
Geometry
Algebra 2
Pre Calculus
Physics
Linear Algebra
```

## Design Explanation
The Python file will initiate execution by moving through the following sections sequentially: 
### JSON Input File 'Processing' Stage 
First, the JSON library is used to attempt to load the JSON file into a Python object which is then converted into a Python dictonary of key value pairs. These key value pairs are the name of the course as the key and the courses's prerequisites (if any) as the value. Once this is completed with correct error handling in the code, we can safely assume that the JSON format is in the correct format for the next section. As a note here, there are many way to correctly 'massage' data into the formats needed (such as checking for alphabetic characters only, char length of strings for names, checking to ensure for no duplicates of the same data, etc.) but in terms of time and lack of interviewer colloboration, I'm making the assumption that if the value is None (name or prerequisites) this will suffice for the check for this implementation. 
### Topological Sort / Depth First Search by Recursion
In terms of class scheduling, it is found that prerequisites for courses (or the key value pair relationship) follows the behavior of a Directed Acyclic Graph. In terms of an educational software system, this would allow the software for students to register for courses and model those course subjects as "nodes" to be sure that the student has taken a prerequisite course before registering for a certain course. The connections between the nodes have a direction (i.e. pre-Algebra before Algebra 1) and they are 'non-circular' in nature, so we can utilize topological sort via depth-first search in our graph. The graph is the dictionary of key value pairs, with the value (list of prerequisites) being the nodes connnected to the current course node, or the key.

- We utilize topological sort by passing in the graph dictionary to the topological sort method that contains the visited nodes set. We create a 'reverse' post-order list that will contain the course order needed to print off at the conclusion of the program. We loop through the keys of the graph dicitonary (the course name of the current node) and if that node name is not in the visited nodes set, then we call the depth-first search on that. This depth-first search method will then add the current node into the visited nodes set if it is not already in the visited nodes set, and then recursively call itself if prerequisites are present. At the conclusion of each these depth-search calls, we then append the start node that we are currently on in the 'reverse' post-order list. This ordering is what is printed out to standard output line by line and follows the standard utilization of depth-first search. 

### Print Final Course Schedule
The final course schedule contained within the 'reverse' post-order list is outputted to standard output line by line. 

## Performance
The processing of the 'graph dictionary' is described as where each node maintains a 'list' of all its adjacent edges. For each node, its neighbors are found by traversing this 'list' once in linear time. So, the sum of the sizes of the routes of all the nodes is E, where E is the total number of edges. The complexity of the depth-first search in this implementation is in O(N) (number of nodes) + O(E) = O(N + E). This is called from the original topological sort method which also runs in linear time, so negating what is not needed shows that the overall performance is within linear time of O(N + E). 


