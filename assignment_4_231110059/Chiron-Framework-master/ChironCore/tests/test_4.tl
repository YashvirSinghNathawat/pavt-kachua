if(:a >= 20)[
    if(:b <= 10)[
        forward 20
        right 90
    ]
    else[
        backward 60
        right 90
    ]
    backward 50
    left 90
]
else[
    if(:b > 10)[
        forward 20
        left 90
    ]
    else[
        forward 10
        left 90
    ]
    right 90
    
]