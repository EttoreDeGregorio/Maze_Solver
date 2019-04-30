'''
0 -> unvisited node
1 -> wall
2 -> visited node
9 -> finish
'''

#start --> 1, 1
maze_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#start --> 3, 0
maze_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 9],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#start --> 1, 2
maze_3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 9, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]