### Assignment 2: Search
#### Due 3/4 at the start of class. 

For the written portion of the assignment, please include a PDF in your repo.

I've provided some starter code for you for this assignment; you are welcome to modify or extend it as needed to make it work better for your purposes.


1. (20 points) Fill in the following table. (you're more than welcome to recreate this in a separate document)


   
| Algorithm  | Time Complexity  | Space Complexity  | Complete?  | Optimal?  |
|---|---|---|---|---|
| BFS  |   |   |   |   |
| UCS  |   |   |   |   |
| DFS   |   |   |   |   |
| DLS  |   |   |   |   |
| IDS |    |   |   |   |
|A*  |    |    |   |   |


2. (15 points) Search. I've provided an example class for you for solving the Fox and Chickens problem. Using the FoxAndChickensState as an example, 
   create an EightPuzzleState, with isGoal, successor, and any other helper functions you think are necessary. You may choose how to represent the grid. Test it with the included BFS implementation.
   
3. (10 points) Add a closed list to the BFS function. (consider using a dictionary)

4. (10 points) Using the BFS function as a template, implement DFS, depth-limited search,
and iterative deepening depth-first search.
   
5. (15 points) Implement A* for the 8-puzzle, using Manhattan distance as a heuristic. You will probably want to use the heapq module for your priority queue.

7. (10 points) Run each of your functions on the 8-puzzle, and measure the number of states generated. Prepare a table showing your results.

6. (20 points). I've provided a TicTacToeState class. Using this, complete the implementation of the minimax algorithm for two-player search. Add a wrapper around this that allows a person to play tic-tac-toe against the computer.

7. (686 students only). 
In the late 90s, Deep Blue shocked the world by becoming the first computer to beat a human grandmaster, Garry Kasparov.
   [This paper](https://pdf.sciencedirectassets.com/271585/1-s2.0-S0004370200X00847/1-s2.0-S0004370201001291/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLWVhc3QtMSJHMEUCIQCHv6f1SKION447Zy%2B%2Fjj7ZZK51qungm5kN%2F0y2yhsurAIgE%2FbNHZZ6By25D%2BImBUVaq%2BUKDf%2B7Uqa9L8a7t9nrUa4qtAMIZBADGgwwNTkwMDM1NDY4NjUiDDBGodLKiULNC6ZDmiqRAy8Ti2ThK2XwJtoOgN0IXF%2FXgLkg18X%2FaMHYsu6qjqyrg0M4y02n1A26mGFxoJwg1%2Fg0Ls5lZiD1VoyjpQlAoYpJ9tscxkeXrAqFdG1NAY%2B7B9piqse3MvUhK3syw5E%2FM60Xh%2FrBllp4OYC2%2FzLGLHXk2cmE%2BxB0eKkGn1BQ6PRQ81g1kod5w8JHqqgwETX8hJhuc68lXyyQVgTmCf5zwoU79N4ns3rK3sUxRwdCSQjOI4FDHUB4G1gFrmMcYohopvHzhNul8R9h6CzYqJpA2WWEptxr%2FSaYcwJWoO01KFmKEdRW0uGPPEvR3ZRac3wGlZGGFVSJUmOTPxd05n%2BH2oFU3hZ2Rzis0cRIP2zGn5xuRVMA%2Fr%2F22kHUZ3ufN%2FEkBVBH4UW16jMKRB8MH2k6Bj0LuLV7G%2Bdwo%2BjvSJI6H9%2FOPuOFZkQgwf2PRNqgu7fdgu5pg%2BL%2FkrpIuBKVDy6KwZmrH0r9NrkGaCjsYMU5xwgLzsLl0ie2bEphPRgs7uT0KTaaPUESztHqyHqwPPBoTXbVMKvPtYEGOusBCxNCzDJkUlyCq0Gl7RqKSM%2BZqQN9BiC4ZAIFFTRsiGlFv7ctOeI8y98SwdwP%2FDBOb1JxTOUmMG5YVrf184WvyWrIAMYO9PbIqdXMZMyR%2B%2BHXurj0q25Ze48eUc9KIQS7Yxbmkq5A5dHYXlCXN6lMhCnH6RAiyf%2Bp6%2FHLYNO7DW6th6O9GBgbV72%2Boq1nOQAEvTJL6teDz%2Fv8ppaRiYW%2B5dMmbBbeXIBGK4hLBJml71fKDSbirx6z0JAFQS1EzO56bVlbTyIvzKGG%2BgdlI1HHSypoaqOmqa4UO09yLCluDDoG4MMC%2FMaQEpusoQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210217T194502Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYTXOLMFNW%2F20210217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a1ea154dc26b7f6bf55b78d2558066ea4c89243537c19854e4c8c0264e98e017&hash=9759e9a487197b114f2285cc3be7d68f70fddd5b5be56c5c1dd01eac3bc91a77&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0004370201001291&tid=spdf-8d7dcfe8-5cff-4e07-b20e-7d7992c76c45&sid=54f296356b581744646ab6348b72ed4150ebgxrqa&type=client)
   describes how Deep Blue was constructed - it took advantage of specialized hardware, along with hand-crafted heuristics and 
   many optimizations of the alpha-beta pruning technique we've learned about.
   
20 years later, the Google team has re-revolutionized game search with the development of AlphaZero, which is described [here](https://science.sciencemag.org/content/sci/362/6419/1140.full.pdf).

AlphaZero uses a very different approach - specifically, a deep neural network is used to learn heuristic functions through self-play. (We'll look at reinforcement learning later in the semester).
This allows the program to learn to play any game, as long as it knows the state space, how to win, and the legal actions.

These articles are both pretty dense, and I don't expect you to grasp every nuance.

a) What were the engineering advances that led to Deep Blue's success? Which of them can be transferred to other problems, and which are specific to chess?

b) AlphaZero is compared to a number of modern game-playing programs, such as StockFish, which work similarly to Deep Blue. The Science paper shows that AlphaZero is able to defeat StockFish even when it is given only 1/100 of the computing time. Why is that? Please frame your answer in terms of search and the number of nodes evaluated.

