if(:x <= -80)[
    if(:y >= 89)[
        backward 99
    ]
    else [
        if(:z > 250)[
            backward 100
        ]
        if(:z < 0)[
            left 100
        ]
    ]
]

pendown
repeat 2 [
    forward 10
    if :z < 50 [
	        if :p < 50 [
		        right 39
                forward 20
	        ]
	        else [
		        left 46
                forward 3
	        ]
    ] 
]

if(:x == 0)[
    backward 100
]

pendown

:e = 25

if(:y <= 89)[
    backward 20
]

if(:x > -100 && :y <= 0)[
    forward 20
    :e = 0
    right 50
    goto(20, -19)
    if(:y < -5)[
        right 30
        forward 5
        left 30
    ]
]

if(:x >= 0 && :y > 39)[
    backward 8
    right 20
    left 134
    goto(10, 9)
    if(:y > 5)[
        right 60
        backward 8
        left 60
    ]
]

else[
    backward 19
    :e = :e * 90    
    if :z < 50 [
	        if :p < 50 [
		        right 39
                forward 20
	        ]
	        else [
		        left 46
                forward 3
	        ]
    ] 
    goto(5, 9)
    backward 9
    goto(-10, 8)
    if(:y > 5)[
        right 60
        backward 8
        left 60
    ]
]

pendown

:e = 25

if(:x >= -219)[
    backward 9
]



if(:x >= 0 && :y > 90)[
    backward 9
    right 90
    forward 7
    left 134
    goto(10, -9)
    if(:x > 5)[
        right 60
        backward 8
        left 60
    ]
]

else[
    :e = :e * 90    
    right 90
    goto(5, 5)
    backward 39
    right 90
    left 134
    goto(-10, 8)
    if(:x > 5)[
        right 60
        backward 8
        left 60
    ]
]
if(:x > 40 && :y <= -70)[
    forward 20
    :e = 0
    if :z < 50 [
	        if :p < 50 [
		        right 39
                forward 20
	        ]
	        else [
		        left 46
                forward 3
	        ]
    ] 
    forward 70
    if(:x < 40)[
        right 45
        forward 8
        left 45
    ]
]