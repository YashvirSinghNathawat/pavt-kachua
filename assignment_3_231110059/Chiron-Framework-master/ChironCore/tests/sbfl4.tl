if :x < 100 [
	if :y < 100 [
		right 39
        if :z < 50 [
	        if :p < 50 [
		        right 39
                forward 20
	        ]
	        else [
		        left 46
                forward 3
	        ]
    ] 
	]
	else [
		left 46
        forward 3
	]
]
else [
    if :y < 100 [
		right 39
        if :z < 50 [
	        if :p < 50 [
		        right 39
                forward 20
	        ]
	        else [
		        left 46
                forward 30
	        ]
    ] 
	]
	else [
		left 46
        forward 30
	]
]