forward 10
if (:a > 10)[
    :a = 20
    forward 30
    left 90
] else [
    :a = 30
    forward 60
    left 90
]
forward :a
