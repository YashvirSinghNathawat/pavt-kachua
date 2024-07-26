:out = 0
if(:x > 10)[
    :out = :out + 2
]
else[
    :out = :out + 10
]
if(:y > 10)[
    :out = :out + 3
    
    if(:y > 15)[
    :out = :out + 5
    ]
]
:out = :out + 1