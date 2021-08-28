#Python - Addition of Matrix Function 
"Computer Programming Tutor, May 20,2021"

def addM(a,b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        res.append(row)
    return res

a = [[2],[3],
   [3],[3]
    ]

b = [[1],[1],
   [2],[2]
    ]

print(addM(a,b))
x = [[1],[1],
     [2],[2]
    ]
y = [[1],[1],
     [1],[1]
    ]

print(addM(x,y))
