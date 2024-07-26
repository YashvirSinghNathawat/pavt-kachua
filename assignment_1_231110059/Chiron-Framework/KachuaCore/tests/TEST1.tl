if :x < -10 [
	if :y < 90 [
		right 39
	]
	else [
		left 46
	]
] else [
	if :y > -36 [
		right 76
	]
	else [
		left 90
	]
	if :z < 59 [
		right 31
		if :p < 90 [
			right 39
		] else [
			left 31
		]
	]
]
