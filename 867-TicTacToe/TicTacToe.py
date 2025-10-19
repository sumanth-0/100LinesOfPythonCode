import tkinter as tk
from helper import check_winner, best_move
PLAYER = "X"
AI = "O"

root = tk.Tk()
root.title("Tic Tac Toe")

board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def on_click(i, j):
    if board[i][j] == "" and check_winner(board) is None:
        board[i][j] = PLAYER
        buttons[i][j]["text"] = PLAYER
        winner = check_winner(board)
        if winner:
            end_game(winner)
            return
        ai_move = best_move(board)
        if ai_move:
            x, y = ai_move
            board[x][y] = AI
            buttons[x][y]["text"] = AI
            winner = check_winner(board)
            if winner:
                end_game(winner)

def center_toplevel(toplevel_window):
    toplevel_window.update_idletasks() # Ensure dimensions are calculated

    window_width = toplevel_window.winfo_width()
    window_height = toplevel_window.winfo_height()

    screen_width = toplevel_window.winfo_screenwidth()
    screen_height = toplevel_window.winfo_screenheight()

    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    toplevel_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

def end_game(winner):
    popup = tk.Toplevel(root)
    center_toplevel(popup)
    popup.title("Tic Tac Toe")
    popup.geometry("250x100")
    popup.resizable(False, False)
    
    msg = "It's a Tie!" if winner == "Tie" else f"{winner} wins!"
    
    label = tk.Label(popup, text=msg, font=("Arial", 14))
    label.pack(pady=20)
    
    btn = tk.Button(popup, text="OK", command=root.destroy)
    btn.pack(pady=5)
    
    popup.transient(root)
    popup.grab_set()
    root.wait_window(popup)

for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                        command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

root.mainloop()
