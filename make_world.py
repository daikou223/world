import random
world_size = 30
world_data = [[0]*world_size for _ in range(world_size)]
sec_data = [[random.randint(0,9) for _ in range(world_size)] for _ in  range(world_size)]
for _ in range(25):
	for height in range(1,world_size-1):
		for width in range(1,world_size-1):
			if world_data[height][width+1] + \
			world_data[height][width-1] + \
			world_data[height+1][width] + \
			world_data[height-1][width] >= random.randint(0,40) and \
			world_data[height][width] < 9:
				world_data[height][width] += 1
cullent_x = random.randint(1,world_size-2)
cullent_y = random.randint(1,world_size-2)
while world_data[cullent_x][cullend_y] == 0:
	cullent_x = random.randint(1,world_size-2)
	cullent_y = random.randint(1,world_size-2)
with open("world.txt","w") as text:
	text.write(str(world_size))
	text.write("\n")
	for height in range(world_size):
		text.write(" ".join(map(str,world_data[height])))
		text.write("\n")
	for height in range(world_size):
		text.write(" ".join(map(str,sec_data[height])))
		text.write("\n")
	text.write(str(cullent_x)+" "+str(cullent_y))
	
			