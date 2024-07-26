:z = :x + 10
if(:x <= 42)[
    if(:y <= 42)[
        :z = :z + 20
    ] else [
        :z = :z + 30
    ]
]
else[
    if(:y <= 42)[
        :z = :z + 40
    ] else [
        :z = :z + 50
    ]
]
:z = :z + 60