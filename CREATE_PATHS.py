

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
			  

def printAllPathsUtil(current, destination, visited, path): 
	
	visited[current]= True
	path.append(current) 

	if current == destination: 
		if (len(path) > 4):
			for p in path:
				saveFile.write('%s,' % str(p))
			saveFile.write('\n')
	else: 
		for i in range(0, 16): 
			if (adj_matrix[current][i] == 1) and (visited[i] == False) and (len(path) < 10):
				printAllPathsUtil(i, destination, visited, path) 
				   
	path.pop() 
	visited[current]= False


def printAllPaths(source, destination): 
	visited = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
	path = [] 
	printAllPathsUtil(source, destination, visited, path) 


saveFile = open('paths.txt', 'w', encoding='utf-8')

for i in range(0,16):
	for j in range(0,16):
		printAllPaths(i, j)
		
saveFile.close()