import pyautogui as pg
import time

def pos():
	print(pg.position())
	
def screenshot():
	
	letters = [(212,341), (289,341), (366,341), (442,341),
		   (212,419), (289,419), (366,419), (442,419),
		   (212,496), (289,496), (366,496), (442,496), 
		   (212,572), (289,572), (366,572), (442,572)]
	
	id = 0	
	for l in letters:
		pg.screenshot('screenshots\screenshot%s.png' % str(id), region=(l[0], l[1], 30, 30))
		id += 1
	
def find_letters():

	start_time = time.time()

	letters = [(212,341), (289,341), (366,341), (442,341),
		   (212,419), (289,419), (366,419), (442,419),
		   (212,496), (289,496), (366,496), (442,496), 
		   (212,572), (289,572), (366,572), (442,572)]

	cross = {1:'Α', 2:'Β', 3:'Γ', 4:'Δ', 5:'Ε', 6:'Ζ', 
			 7:'Η', 8:'Θ', 9:'Ι', 10:'Κ', 11:'Λ', 12:'Μ', 
			 13:'Ν', 14:'Ξ', 15:'Ο', 16:'Π', 17:'Ρ', 18:'Σ', 
			 19:'Τ', 20:'Υ', 21:'Φ', 22:'Χ', 23:'Ψ', 24:'Ω'}

	word = ''	
	for letter in letters:
		for i in range(1,25):
			tried = pg.locateOnScreen('letters\letter%s.jpg' % str(i),grayscale=True,region=(letter[0], letter[1], 30, 30))
			if (tried != None):
				word += cross.get(i)
				break
	print("--- %.3f seconds ---" % (time.time() - start_time))
	print(word)
	
find_letters()
