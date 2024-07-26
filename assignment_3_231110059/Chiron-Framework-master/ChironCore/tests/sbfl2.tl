pendown
if :x > 0 [
	if :y > 0 [
		if :z > 0[

			backward 20
			left 20
		
		] else [backward 10]
		
	] else [backward 10]

] else [backward 10]
if :p > 0 [
	forward 100
]
else[
	backward 20
]