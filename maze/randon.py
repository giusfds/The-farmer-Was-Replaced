DIRECTION = [North, South, West, East]
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
clear()

for i in range(0,1,0):
	till()
	plant(BUSH)
	while get_entity_type() == BUSH:
		use_item(FERTILIZER)
	while not measure():
		move(DIRECTION[random()*4])
	harvest()