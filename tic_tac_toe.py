import tkinter as tk
import random


def player_move(row, col):
    if buttons[row][col]["text"] == "X" or buttons[row][col]["text"] == "O":
        check_winner()
    else:
        buttons[row][col].config(text="X")

        if not check_winner():
            computer_move()


def computer_move():
    available_buttons = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if buttons[r][c]["text"] not in ["X", "O"]
    ]

    if available_buttons:
        random_row, random_col = random.choice(available_buttons)
        buttons[random_row][random_col].config(text="O")
        check_winner()


def on_restart():
    global player_score, computer_score
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="lightGray")

    player_score = 0
    computer_score = 0
    score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
    win_label.config(text="")


def check_winner():
    global player_score, computer_score
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            == "X"
        ):
            win_label.config(text="Player wins!!")
            player_score += 1
            score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for col in range(3):
        if (
            buttons[0][col]["text"]
            == buttons[1][col]["text"]
            == buttons[2][col]["text"]
            == "X"
        ):
            win_label.config(text="Player wins!!")
            player_score += 1
            score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == "X":
        win_label.config(text="Player wins!!")
        player_score += 1
        score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == "X":
        win_label.config(text="Player wins!!")
        player_score += 1
        score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            == "O"
        ):
            win_label.config(text="Computer wins!")
            computer_score += 1
            score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
            for col in range(3):
                buttons[row][col].config(bg="red")
            return True

    for col in range(3):
        if (
            buttons[0][col]["text"]
            == buttons[1][col]["text"]
            == buttons[2][col]["text"]
            == "O"
        ):
            win_label.config(text="Computer wins!")
            computer_score += 1
            score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
            for row in range(3):
                buttons[row][col].config(bg="red")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == "O":
        win_label.config(text="Computer wins!")
        computer_score += 1
        score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
        for i in range(3):
            buttons[i][i].config(bg="red")
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == "O":
        win_label.config(text="Computer wins!")
        computer_score += 1
        score_label.config(text=f"You: {player_score}   Computer: {computer_score}")
        for i in range(3):
            buttons[i][2 - i].config(bg="red")
        return True

    # Check for a tie
    if all(button["text"] in ["X", "O"] for row in buttons for button in row):
        win_label.config(text="It's a Tie!")
        for row in buttons:
            for button in row:
                button.config(bg="yellow")
        return True

    return False


window = tk.Tk()
window.title("Tic-Tac-Toe Almdrasa")

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

score_frame.rowconfigure(0, weight=1)
score_frame.columnconfigure(0, weight=1)
game_frame.rowconfigure(0, weight=1)
game_frame.columnconfigure(0, weight=1)

player_score = 0
computer_score = 0
score_label.config(text=f"You: {player_score}   Computer: {computer_score}")


window.mainloop()
