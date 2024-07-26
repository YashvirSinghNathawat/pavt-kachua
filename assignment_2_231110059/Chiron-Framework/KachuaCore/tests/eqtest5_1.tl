:out = 0
if(:x > 10)[
    :out = :out + :c1
]
else[
    :out = :out + :c5
]
if(:y > 10)[
    :out = :out + :c2
]
if(:y > 15)[
    :out = :out + :c4
]
:out = :out + :c3