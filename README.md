
# Connect 4 with Minimax and Alpha-Beta Pruning

This project is a console-based implementation of the classic Connect 4 game, featuring an AI opponent powered by the Minimax algorithm with [Alpha-Beta Pruning](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/?ref=shm). The game allows you to play against the computer, which uses this advanced algorithm to make optimal moves.

## Features
- **Console-based gameplay**: Enjoy Connect 4 directly in your terminal.
- **AI opponent**: Play against an AI that uses the Minimax algorithm with Alpha-Beta Pruning for optimal decision-making.
- **Efficient AI**: The Alpha-Beta Pruning optimizes the Minimax algorithm, reducing the number of nodes evaluated, and providing a quicker response time.

## Prerequisites

Before running the project, make sure you have [**Python**](https://www.python.org) installed. This project is compatible with Python 3.x.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/JPaulBR/Connect4
2. Navigate to the project directory:
    ```bash
   cd Connect4
3. Run the project
    ```bash
   python3  Connect4.py

## How it works
- **Minimax Algorithm**: The AI simulates all possible moves to find the best possible outcome for itself and the worst possible outcome for the opponent.
- **Alpha-Beta Pruning**: This optimization technique reduces the number of nodes the Minimax algorithm needs to evaluate by "pruning" branches that won’t affect the final decision.

## Code Example

Here's a snippet of the code that handles the AI's decision-making using the Minimax algorithm with Alpha-Beta Pruning:

```python
# The minMaxAlphaBeta pruning adapted to connect4
def minMaxAlphaBeta(boardCopy,depth,alpha,beta,currentPlayer):
    if IsFinishGame() or depth == 0:
        return calculateHeuristicPoints(boardCopy)
    if currentPlayer == AI:
        maxEval = -float('inf')
        for column in [0,1,2,3,4,5,6]:
            if not ifValidPosition(boardCopy,column):
                continue
            row = getBottom(boardCopy,column)
            boardCopy[row][column] = currentPlayer
            eval = minMaxAlphaBeta(boardCopy, depth - 1, alpha, beta, PLAYER)
            boardCopy[row][column] = EMPTY_SLOT
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for column in [0,1,2,3,4,5,6]:
            if not ifValidPosition(boardCopy,column):
                continue
            row = getBottom(boardCopy,column)
            boardCopy[row][column] = currentPlayer
            eval = minMaxAlphaBeta(boardCopy, depth - 1, alpha, beta, AI)
            boardCopy[row][column] = EMPTY_SLOT
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval