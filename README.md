# DisjointSet
-python version used: v2.6.6
-OS: RHEL 6.6
-This Program implements 'add' and 'remove' function to add/remove disjoint integer set to a list of such disjoint sets.
-To test the program from from linux shell:
  $python disjoint.py

-To verify add/remove function, append following calls at end of file: disjoint.py
add(x,y), to add [x, y] to the disjoint sets, where x and y are integers
remove(x,y), to remove [x, y] from the disjoint sets, where x and y are integers

- Some sample calls are already added for:
Start: []
Call: add(1, 5) => [[1, 5]]
Call: remove(2, 3) => [[1, 2], [3, 5]]
Call: add(6, 8) => [[1, 2], [3, 5], [6, 8]]
Call: remove(4, 7) => [[1, 2], [3, 4], [7, 8]]
Call: add(2, 7) => [[1, 8]]

