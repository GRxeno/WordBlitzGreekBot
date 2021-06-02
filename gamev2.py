import time
import pyautogui as pg


def create_board(input):
	board = {'0':input[0], '1':input[1], '2':input[2], '3':input[3],
	        '4':input[4], '5':input[5], '6':input[6], '7':input[7],
			'8':input[8], '9':input[9], '10':input[10], '11':input[11],
			'12':input[12], '13':input[13], '14':input[14], '15':input[15]}
	return board

def move(directions):
	
	dictionary = {'0':(400, 690), '1':(550, 690), '2':(700, 690), '3':(850, 690),
				  '4':(400, 840), '5':(550, 840), '6':(700, 840), '7':(850, 840),
				  '8':(400, 980), '9':(550, 980), '10':(700, 980), '11':(850, 980),
				  '12':(400, 1130),'13':(550, 1130),'14':(700, 1130),'15':(850, 1130) }
	
	first_wh = dictionary.get(directions[0]) 
	pg.moveTo(first_wh[0], first_wh[1], 0.1)
	pg.mouseDown()
	for pos in directions:
		wh = dictionary.get(pos)
		pg.moveTo(wh[0], wh[1], 0.1)
	pg.mouseUp()
	time.sleep(0.2)

if __name__ == "__main__" :
	Openfile = open('paths.txt', 'r', encoding='utf-8')
	f = open('wordlist.txt', 'r', encoding="utf8")
	dictionary = set(f.read().splitlines())	

	#input = 'ΤΑΙΒΚΛΥΑΕΟΜΨΥΑΡΑ'
	#input = 'ΠΑΣΕΣΣΧΤΟΩΑΡΣΛΚΟ'
	input = input("Enter letters: " )

	board = create_board(input)
	all_words = set()

	start_time = time.time()
	for line in Openfile:
		if (time.time() - start_time) < 85:
			line = line[:-2]
			path = line.split(',')
			word = ''
			for j in path:
				word += board.get(j)
			if word in dictionary and word not in all_words:
				all_words.add(word)
				print(word)
				move(path)
			

			
	print("--- %d words tried ---" % len(all_words))
	print("--- %.3f seconds ---" % (time.time() - start_time))
	f.close()
	Openfile.close()