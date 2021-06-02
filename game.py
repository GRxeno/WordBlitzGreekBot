import time

try:
    import pyautogui as pg
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
finally:
    import pyautogui as pg

adj_matrix = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
			[1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
			[1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
			[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
			[0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0], 
			[0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
			[0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0], 
			[0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0], 
			[0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1], 
			[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1], 
			[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1], 
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]]			  
			  
def move(directions):
	
	dictionary = {0:(225, 350), 1:(300, 350), 2:(375, 350), 3:(450, 350),
				  4:(225, 425), 5:(300, 425), 6:(375, 425), 7:(450, 425),
				  8:(225, 500), 9:(300, 500), 10:(375, 500), 11:(450, 500),
				  12:(225, 575), 13:(300, 575), 14:(375, 575), 15:(450, 575)}
	
	first_wh = dictionary.get(directions[0]) 
	pg.moveTo(first_wh[0], first_wh[1], 0.1)
	pg.mouseDown()
	for pos in directions:
		wh = dictionary.get(pos)
		pg.moveTo(wh[0], wh[1], 0.1)
	pg.mouseUp()
	time.sleep(0.2)

def printAllPathsUtil(current, destination, visited, path): 
	
	visited[current]= True
	path.append(current) 

	if current == destination: 
		word = ''
		if (len(path) > 4):
			for j in path:
				word += board.get(j)
		if word in dictionary and word not in all_words:
			all_words.add(word)
			print(word)
			move(path)
	else: 
		for i in range(0, 16): 
			if (adj_matrix[current][i] == 1) and (visited[i] == False) and (len(path) < 9):
				printAllPathsUtil(i, destination, visited, path) 
				   
	path.pop() 
	visited[current]= False


def printAllPaths(source, destination): 
	visited = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
	path = [] 
	printAllPathsUtil(source, destination, visited, path) 
		
def create_board(input):
	board = {0:input[0], 1:input[1], 2:input[2], 3:input[3],
	              4:input[4], 5:input[5], 6:input[6], 7:input[7],
				  8:input[8], 9:input[9], 10:input[10], 11:input[11],
				  12:input[12], 13:input[13], 14:input[14], 15:input[15]}
	return board

		
start_time = time.time()	
f = open('output.txt', 'r', encoding="utf8")
dictionary = set(f.read().splitlines())	

input = 'ΤΑΙΒΚΛΥΑΕΟΜΨΥΑΡΑ'
#input = 'ΠΑΣΕΣΣΧΤΟΩΑΡΣΛΚΟ'
#input = input("Enter letters: " )

board = create_board(input)
all_words = set()

for i in range(0,16):
	for j in range(0,16):
		printAllPaths(i, j)
print(len(all_words))
print("--- %s seconds ---" % (time.time() - start_time))