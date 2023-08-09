# What is this?
This is a simple clone of the game [Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre)). I made this in under two hours because I had not make a Snake clone before and was bothered by not reaching that beginner coding milestone. I was also curious how I'd solve the problem of Snake's movement and growth logic by myself without external help. Now that I have made it I feel more at ease. This uses the same Grid class from my previous [Conway](https://github.com/ClementineAccount/ConwayPygame) project, also in PyGame.

Currently this only has movement and no collision detection or the fruit spawning. I might add that later but those features are not interesting to me and I had solved very [similar problems](https://github.com/ClementineAccount/ConwayPygame) grid collision and placement in the past. The main thing I was concerned with was 'growing' and 'movement' for a snake body and linked list. I was happy about the approach I took, keeping track of direction and updating the snake by a grid.

I didn't use any tutorials looking it up, but I did take a look at [Coding Train's version of Snake](https://thecodingtrain.com/challenges/3-snake-game) after I had written all the code here to compare the solution. 

I noticed that my idea of creating a 'swap' function to do movement for iteration is a little unusual, but I do like its simplicity (although am aware it has slightly more operations compared to a linear iteration with setting it using 'next'). I don't actually understand how Coding Train's version works. I did try it out into my code after the fact but it does not work at all for me.

# Future Plans

I probably won't bother much with this PyGame version of the Snake clone here, might add the fruit, collision and game loop state some other time. I also might experiment with different ways of setting a localized speed for the Snake character beyond ticks sets, but I do like not having to account for float rounding.

I intend to remake both this and Conway's in SDL2 so that I can create more class helper functions with the grid. I had flirted with the idea of creating a project that combines both Snake and Conway, reusing the same grid class I had made. Maybe I'd do both an SDL2 and Python version for practice though.


# How do I run it?

You'd need both Python and Pygame-ce installed.
Enter the following in the same directory as the script. You can move the snake around with the arrow keys

```
python .\main.py
```