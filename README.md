# WordBlitz Greek Bot
 
> A simple python script that tries all the possible words in Greek at the
WordBlitz game on Facebook.

>The current best working version is v2. (I plan to add OCR in v3) 

>My at the time girlfriend destroyed me at this game so i did what every
rational man would do and created a python script to play for me.

## WordBlitz Description

---

WordBlitz is a game where an 4x4 array is given to you with random letters.
You have to swipe and link adjacent letters to form a word. You can try as 
many words as you want, in every direction: left, right, up, down or 
diagonal. Each letter contained inside the word you formed is worth a certain 
amount of points. Your goal is to acquire more points than your oponent.


## Scripts Description

---

The way the script works is actually pretty simple, it's not the most
efficient one, but it works fine. The board will always be 4x4 so i create a
paths.txt file with all the possible combinations of swipes. 

`CREATE_PATHS.py` The adjacent matrix represents the 16 letters of the board.
You can only connect a letter with an another letter if they are adjacent so
if the letters are adjacent the value in the matrix is "1" if not "0". For
every board position i find every possible path and store it in paths.txt. I
do it for paths of length less than 10 so i don't get a massive output.

`wordlist.txt` Contains A LOT of Greek words that the python script is gonna 
compare one by one later on to check if they are a valid word on the game 
board. I deleted all small and massive words to save time. Theorytically this 
can be an English wordlist too.

`gamev2.py` Where the magic happens. The script contains my screen's 
positions of all the letters location. When run it asks the user to put in 
the letters on the board (ex. 'ΤΑΙΒΚΛΥΑΕΟΜΨΥΑΡΑ') and then goes to paths.txt, 
takes the top path and creates a temp word based on the path. Then goes to 
wordlist.txt and checks if the temp word created is a valid Greek word. If 
yes it moves the cursor to the predefined screen positions and continues with 
the paths. The script ends after 85 seconds of runtime (each round lasts 60 
seconds). 

I tried adding ocr to the script so the user doesn't have to put manually the 
letters and image recognition so it can detect the correct screen positions 
automatically. I plan to continue working twowards those goals. If you want 
to help you are welcome to :D

## How To Run

---

For the gameV2:

1. Download gamev2.py, wordlist.txt, paths.txt or clone the repo.
```
    https://github.com/GRxeno/WordBlitzGreekBot.git
```
2. Install pyautogui. 
```
    python -m pip install pyautogui 
```
3. Change each letters board screen position to yours screen position 
(You can use pyautogui to find the correct values).
```	
dictionary = {'0':(x0, y0), '1':(x1, y1), ...,'15':(x15, y15) }
```
4. Run the python script and when asked put the letters like that: 
(ex. 'ΤΑΙΒΚΛΥΑΕΟΜΨΥΑΡΑ'). 

## Future Improvements

---

+ Add OCR to detect the letters automatically.
+ Add image recognition to detect the correct screen cords.
+ Add English wordlist and auto detect languege.