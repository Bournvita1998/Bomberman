Bomberman game can be run by using python
i.e. python bomberman.py

Basic Controls :--

   Function     key
1)Move left 	a
2)Move right	d
3)Move up   	w
4)Move down 	s
5)Drop bomb 	b

It is a simple game where bomberman can be run by the user whereas enemies move randomly on the board. Both of them cannot walk through walls or bricks. Bomberman can drop a bomb which destroys bricks and enemies around it's four direction and the place of bomb itself after 3 frames .

--'/' represents the bricks
--'B' represents Bomberman
--'[^^]'
--' ][ ' represents Enemy
--'#' represents the fire of explosion
--'X' The walls

It is implemented using OOP's Principles

Modularity:-
Code has been divided into several modules , which altogether run as if it were a single file code

bomberman.py :- It conatains the code for running the game and some other things
movement.py  :- It conatains the code for movement of bomberman
gameplay.py  :- It conatains the code for printing the updated Matrix.
AlarmException.py and getchunix.py :- It contains the code for getting char from keyboard without interupt

Inheritance:-
The Movement inherit Gameplay class
and Bomberman inherit Gameplay and Movement classes

Polymorphism:-
We have an abstract class Gameplay which contains printboard()

The functions listed above work according to the object which called it , i.e the functions work differently

Encapsultion:-
The printboard method is private to its class
