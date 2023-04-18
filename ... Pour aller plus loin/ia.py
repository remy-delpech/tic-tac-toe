def Ia(board, signe):
    # Define the maximizer and minimizer players
    if signe == "X":
        max_player = "X"
        min_player = "O"
    else:
        max_player = "O"
        min_player = "X"

    # Define the utility function
    def utility(board):
        # Check if the game is over
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                if board[i][0] == max_player:
                    return 1
                else:
                    return -1
            if board[0][i] == board[1][i] == board[2][i] != "":
                if board[0][i] == max_player:
                    return 1
                else:
                    return -1
        if board[0][0] == board[1][1] == board[2][2] != "":
            if board[0][0] == max_player:
                return 1
            else:
                return -1
        if board[0][2] == board[1][1] == board[2][0] != "":
            if board[0][2] == max_player:
                return 1
            else:
                return -1
        # Check if the game is a tie
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    return None
        return 0

    # Define the minimax algorithm
    def minimax(board, player):
        # Check if the game is over
        score = utility(board)
        if score is not None:
            return score

        # Find the best move for the current player
        if player == max_player:
            best_score = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = max_player
                        score = minimax(board, min_player)
                        board[i][j] = ""
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = min_player
                        score = minimax(board, max_player)
                        board[i][j] = ""
                        best_score = min(best_score, score)
            return best_score

    # Find the best move for the AI player using the minimax algorithm
    best_score = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = max_player
                score = minimax(board, min_player)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = i * 3 + j
    if best_move is not None:
        return best_move
    else:
        return False