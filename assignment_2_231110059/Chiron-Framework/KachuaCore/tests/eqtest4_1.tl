:z = :x + :c3
if(:x <= 42)[
    if(:y <= 42)[
        :z = :z + :c1
    ] else [
        :z = :z + :c2
    ]
]
else[
    if(:y <= 42)[
        :z = :z + :c4
    ] else [
        :z = :z + :c5
    ]
]
:z = :z + :c6