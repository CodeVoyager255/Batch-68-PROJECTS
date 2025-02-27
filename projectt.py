import tkinter as tk
from tkinter import messagebox

# Check for a winner by examining all winning combinations
def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                  [0, 4, 8], [2, 4, 6]]:           # Diagonals
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == 
            buttons[combo[2]]["text"] != ""):
            winner = True
            # Highlight winning combination
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

# Handle button clicks
def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:  # Only proceed if spot is empty and no winner
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:  # Toggle player only if no winner yet
            toggle_player()

# Switch between players
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Set up the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create 9 buttons in a 3x3 grid
buttons = [tk.Button(root, text="", font=("normal", 25), width=2, height=6, 
                     command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initialize game state
current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 20))
label.grid(row=3, column=0, columnspan=3)

# Start the game
root.mainloop()