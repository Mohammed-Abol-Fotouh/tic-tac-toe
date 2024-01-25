import tkinter as tk
import random


def player_move(row, col):
    """
    Handles player's move when a button is clicked.
    Checks if the button is available, updates the button with "X",
    and triggers the computer's move if the game is still ongoing.
    """
    if buttons[row][col]["text"] == "X" or buttons[row][col]["text"] == "O":
        # Ignore if the button is already marked
        check_winner()
    else:
        # Mark the button with "X"
        buttons[row][col].config(text="X")
        # Check if the player has won or if it's a tie
        if not check_winner():
            # Proceed with the computer's move
            computer_move()


def computer_move():
    """
    Handles the computer's move.
    Chooses a random available button and marks it with "O".
    Checks if the computer has won or if it's a tie.
    """
    # Create a list of all buttons that don't have text "X" or "O"
    available_buttons = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if buttons[r][c]["text"] not in ["X", "O"]
    ]

    # Check if there are available buttons
    if available_buttons:
        # Choose a random button from the list
        random_row, random_col = random.choice(available_buttons)
        buttons[random_row][random_col].config(text="O")
        # Check if the computer has won or if it's a tie
        check_winner()


def on_restart():
    """
    Restarts the game by resetting button texts and colors.
    Also resets the player and computer scores.
    """
    global player_score, computer_score
    for row in range(3):
        for col in range(3):
            # Reset button text and color
            buttons[row][col].config(text="", bg="lightGray")

    # Reset scores and update labels
    player_score = 0
    computer_score = 0
    score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
    win_label.config(text="")


def check_winner():
    """
    Checks for a winner or a tie after each move.
    Updates the score, highlights the winning combination, and handles ties.
    """
    global player_score, computer_score

    # Check for a win in rows (horizontal) and columns (vertical)
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            == "X"
        ):
            # Player wins
            update_winner("Player", row, 0, row, 1, row, 2)
            return True

    for col in range(3):
        if (
            buttons[0][col]["text"]
            == buttons[1][col]["text"]
            == buttons[2][col]["text"]
            == "X"
        ):
            # Player wins
            update_winner("Player", 0, col, 1, col, 2, col)
            return True

    # Check for a win in diagonal (from top-left to bottom-right)
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == "X":
        # Player wins
        update_winner("Player", 0, 0, 1, 1, 2, 2)
        return True

    # Check for a win in diagonal (from top-right to bottom-left)
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == "X":
        # Player wins
        update_winner("Player", 0, 2, 1, 1, 2, 0)
        return True

    # Check for a win in rows with "O"
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            == "O"
        ):
            # Computer wins
            update_winner("Computer", row, 0, row, 1, row, 2)
            return True

    # Check for a win in columns with "O"
    for col in range(3):
        if (
            buttons[0][col]["text"]
            == buttons[1][col]["text"]
            == buttons[2][col]["text"]
            == "O"
        ):
            # Computer wins
            update_winner("Computer", 0, col, 1, col, 2, col)
            return True

    # Check for a win in diagonal (from top-left to bottom-right) with "O"
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == "O":
        # Computer wins
        update_winner("Computer", 0, 0, 1, 1, 2, 2)
        return True

    # Check for a win in diagonal (from top-right to bottom-left) with "O"
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == "O":
        # Computer wins
        update_winner("Computer", 0, 2, 1, 1, 2, 0)
        return True

    # Check for a tie
    if all(button["text"] in ["X", "O"] for row in buttons for button in row):
        # It's a Tie!
        update_winner("Tie")
        return True

    return False


def update_winner(winner, *args):
    """
    Updates the winner label, scores, and highlights the winning combination.
    """
    global player_score, computer_score
    if winner == "Player":
        win_label.config(text="Player wins!!")
        player_score += 1
        score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
    elif winner == "Computer":
        win_label.config(text="Computer wins!")
        computer_score += 1
        score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
    elif winner == "Tie":
        win_label.config(text="It's a Tie!")
        for row in buttons:
            for button in row:
                button.config(bg="yellow")
    else:
        win_label.config(text="")

    # Highlight the winning combination
    for idx in range(0, len(args), 2):
        row, col = args[idx], args[idx + 1]
        buttons[row][col].config(bg="red" if winner == "Computer" else "green")


# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe Almdrasa")

# Configure row and column weights for the window
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Score frame
score_frame = tk.Frame(window)
score_label = tk.Label(score_frame, text="You: 0   Computer: 0", font={"Helvetica", 16})
win_label = tk.Label(score_frame, text="", font={"Helvetica", 16})
restart_btn = tk.Button(score_frame, text="Restart", command=on_restart)

# Game frame
game_frame = tk.Frame(window)
buttons = [[None for _ in range(3)] for _ in range(3)]  # 2D list to store buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(
            game_frame,
            text="",
            width=10,
            height=3,
            border=2,
            command=lambda r=row, c=col: player_move(r, c),
        )
        buttons[row][col].grid(row=row, column=col)

# Grid placement and configuration
score_frame.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
game_frame.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

score_label.grid(column=0, row=0, padx=5, pady=5, columnspan=2, rowspan=2)
win_label.grid(column=0, row=2, padx=5, pady=5, columnspan=2, rowspan=2)
restart_btn.grid(column=0, row=4, padx=5, pady=5, columnspan=2, rowspan=2)

# Configure row and column weights for the frames
score_frame.rowconfigure(0, weight=1)
score_frame.columnconfigure(0, weight=1)
game_frame.rowconfigure(0, weight=1)
game_frame.columnconfigure(0, weight=1)

# Initialize scores
player_score = 0
computer_score = 0
score_label.config(text=f"You: {player_score}   Computer: {computer_score}")

# Run the main loop
window.mainloop()
