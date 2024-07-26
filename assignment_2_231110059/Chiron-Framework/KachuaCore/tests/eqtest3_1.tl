:g = 0
if(:x > 10)[
    :g = :g + :x +  :c2
]
else[
    :g = :g + :x +  :c3
]
if(:y > 10)[
    :g = :g + :x + :c4
]
else[
    :g = :g + :x + :c1
]
:g = :g + :x + :c5
