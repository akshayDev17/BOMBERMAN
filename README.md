# Basic Information:

This is a basic simulation of the famous game Bomberman, available on the console NES64(Nintendo) given to me as my college assignment.



## Setup of the game:

* Clone the repository.

  ```bash
  git clone https://github.com/akshayDev17/BOMBERMAN.git
  ```

* Go inside the directory named new.

  ```bash
  cd new
  ```

* Run the Bomber.py file.

  ```bash
  python Bomber.py
  ```



## Instructions regarding movement of the character:

* W  -  move up
* S  -  move down
* A  -  move left
* D  -  move right



## Details regarding the game:

* The game is bounded by walls which are indestructible.
* It also has bricks, 2*4 dimensions, which can be destroyed by bombs.
* B  -  bomb plant.


* Enemies are spawned randomly.
* The player has 5 lives in total.
* The player can plant only 1 bomb at a time.
* If the bomb breaks a brick tile, the player is rewarded with 20 points.
* If an enemy/enemies is/are killed by a bomb, for each enemy killed the player is rewarded with 100 points.
* The player dies by :
  *  Hitting the enemy.
  * Caught in the bomb radius.
* On death of the player, the round is reinitialized, and the score of previous round is recorded.
* If all lives are consumed, or the player hits the *Quit Button Q* , the game is exited from, and the scores of individual rounds are displayed.