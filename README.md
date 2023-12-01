# How to use it

Execute game.py.

It needs opencv-python, pygame and numpy. Other libraries should already be installed with python

When the game is opened three notes will appear, below them a piano will also appear. The notes need to be played on the piano, if a wrong note is played it will light up in red, if the correct one is played it will light up in green and play its respective sound. The music sheet is read from left to right, and when a correct note is played it goes on to the next one. When all the notes on the current sheet are played a new random music sheet will be generated and the process repeats itself.

# Example

With this following example, the note that needs to be played is the first one strating from the left.

![image](https://github.com/XaviMV/piano-practice/assets/70759474/3e6fc40f-d1b3-444b-80fe-abfea58f0eb7)

When the incorrect note is played, it lights up in red

![image](https://github.com/XaviMV/piano-practice/assets/70759474/872b0f5b-7ce9-4681-a6f0-c77988bda69b)

When the correct note is played it lights up in green and plays its sound

![image](https://github.com/XaviMV/piano-practice/assets/70759474/01a948b0-8300-4f4b-83a9-3924b3eb7a99)


# Improvemetns

Right now flat and sharp notes are not implemented (the black keys in the piano)

Every music sheet has exactly 3 notes every time, this could be changed to have a variable amount

Every time a key in the piano lights up in green or red it only does so for 1 single frame, so sometimes it is difficult to see. It could be changed so that the period during which it changes color increases (to maybe 0.5 or 0.25 seconds). It could also progressively lose its red/green color, so that after being pressed it becomes a saturated red/green and progressively goes back to being black/white.
