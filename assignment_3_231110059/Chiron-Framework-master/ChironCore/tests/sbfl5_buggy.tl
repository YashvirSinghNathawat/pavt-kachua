pendown
if :x > 0 [
	if :y > 0 [
		if :z > 0 [
			backward 30
            right 90
            forward 30
		]
		else [
            forward 30
            left 90
            backward 30         
            
            ]
	]
	else [
        backward 10
        left 45
        forward 20   
    ]
]
else [
    if :y > 0 [
		if :z > 0 [
			 forward 30
            left 90
            backward 30
		]
		else [
            backward 100
            left 45
            forward 100         
            
            ]
	]
	else [
        forward 100
        left 90
        backward 90   
    ]
]

