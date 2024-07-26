repeat 4[
            forward 40
            right 89
            backward 11
            if(:y >= 99)[
                backward 99
                left 78
                forward 19
            ]
            else[
                pendown
                forward 15
            ]
]
if :x==20[
    forward 10
]
else [
    pendown
    forward 15
    forward 15
]
if(:x <= :y)[
    if :x == 0[
        if :y==0 [
            forward 40
        ] else [
            backward 30
            pendown
            forward 15
            forward 15
        ]
    ]
    else[
        if :y==0[
            forward 20
        ] else [
            pendown
            forward 15
            forward 15
        ]

    ]
]