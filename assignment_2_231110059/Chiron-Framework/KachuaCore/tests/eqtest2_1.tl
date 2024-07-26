:y = :x
if (:x <= 60) [
    if (:x >= 14)[
        :y = :y + :c1
   ]
]
if (:x >=0 )[
    if(:x <= 100)[
    :y = :y + :c2
    ]
    else[
        :y = :y + :c2
    ]
]
else[
    if(:x<100)[
        :y = :y + :c4
    ]
]
:y = :y + :c3