# How to use it

Execute game.py.

It needs opencv-python, pygame and numpy. Other libraries should already be installed with python

Four notes will appear when the game is opened, and a piano will also appear under them. The notes need to be played on the piano, if a wrong note is played, its respective key will light up in red, if the correct one is played it will light up in green and play its sound. The music sheet is read from left to right, and when a correct note is played it goes on to the next one. When all the notes on the current sheet are played a new random set of notes will appear on the music sheet.

# Example

https://github.com/XaviMV/piano-practice/assets/70759474/ebdf8509-1dab-4760-8320-41f0d690bd3b

# Improvements

Every time a key in the piano lights up in green or red it only does so for 1 single frame, so sometimes it is difficult to see. It could be changed so that the period during which it changes color increases (to maybe 0.5 or 0.25 seconds). It could also progressively lose its red/green color, so that after being pressed it becomes a saturated red/green and progressively goes back to being black/white.
