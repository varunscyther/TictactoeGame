"""
Tic Tac Toe is one of the fun game played widely across the world.
This game is developed using tkinter package - on of the standard python interface for GUI tool kit
- https://docs.python.org/3/library/tkinter.html#module-tkinter

This game allows two user to play at same time and based on the game rules either player can win or game
could result in toi a tie.

Also under this game, following option are provided i.e

- Game rules instruction
- Strategy to win the game
- Option to reset the game
- Any time players can exit from an game
"""

from tkinter import *
from tkinter import messagebox

global b1, b2, b3, b4, b5, b6, b7, b8, b9, winner, clickCounter, buttonClicked

'''Function to build game menus'''


def build_menu():
    game_menu = Menu(window)
    window.config(menu=game_menu)
    build_option_menu(game_menu)


"""
Function to build different game menu options
Different menu options :
a.  Games Rules
b.  How to Win
c.  Restart Game
d.  Exit Game
"""


def build_option_menu(game_menu):
    options = Menu(game_menu, tearoff=False)
    game_menu.add_cascade(label="Menu Options", menu=options)
    # Menu option to explain the different games rules
    options.add_command(label="Game Rules", command=game_rules)
    # Menu option to help players to strategies the probabilities of winning game
    options.add_command(label="How to Win", command=how_to_win)
    # Menu option to restart the game
    options.add_command(label="Restart Game", command=setup)
    # Menu option to exit the game
    options.add_command(label="Exit Game", command=exit_game)


'''Function to build the option for instructing game rules'''


def game_rules():
    messagebox.showinfo("Instructions", " - The game will be  played on a grid of 3 squares by 3 squares.\n"
                                        "- There will be two players 'X' and 'O' .\n"
                                        "- Players can take turns by clicking on available option.\n"
                                        "- The first player to get 3 of his/her marks in a row (up, down, across, "
                                        "or diagonally) is the winner.\n"
                                        "- When all 9 squares are full, the game is over. If no player has 3 marks in "
                                        "a row, the game ends in a tie")


'''Function to build the option for helping using to strategics the probabilities of winning game '''


def how_to_win():
    messagebox.showinfo("How to Win", "- To beat the other player (or at least tie), you need to make use of a little "
                                      "bit of strategy.\n"
                                      "- Strategy means figuring out what you need to do to win.\n"
                                      "- Part of your strategy is trying to figure out how to get three 'X's in a "
                                      "row.\n "
                                      "- The other part is trying to figure out how to stop the other player from "
                                      "getting three 'O's in a row.\n "
                                      "- After you put an 'X' in a square, you start looking ahead. Where's the best "
                                      "place for your next 'X' ?\n "
                                      "- You look at the empty squares and decide which ones are good choices which "
                                      "ones might let you make three 'X's in a row.\n"
                                      "- You also have to watch where the other player puts its 'O'. That could change "
                                      "what you do next.\n "
                                      "- If the other player gets two 'O's in a row, you have to put your next 'X' in "
                                      "the last empty square in that row, or the other player will win.\n "
                                      "- You are forced to play in a particular square or lose the game.\n"
                                      "- If you always pay attention and look ahead, you'll never lose a game of "
                                      "Tic Tac Toe. You may not win, but at least you'll tie.")


"""
Function to build the initial set up for the game in case of fresh or restart
- Configuring the grid
- Defining the buttons with text, font, height, width, colour and on click function
"""


def setup():
    global buttonClicked, clickCounter, window
    # X will start the game so clicked will be true
    buttonClicked = True
    # At the start of this game the click counter will initialize to 0.
    # This is needed for deciding the allowed number of maximum changes players can take in total in case of tie.
    clickCounter = 0

    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    b1 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b1))
    b2 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b2))
    b3 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b3))

    b4 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b4))
    b5 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b5))
    b6 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b6))

    b7 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b7))
    b8 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b8))
    b9 = Button(window, text=" ", font=("Times", 25), height=5, width=10,
                bg="SystemButtonFace", fg="blue", command=lambda: button_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


'''Function to option to exit the game'''


def exit_game():
    window.destroy()



"""
Function to handle the button click event 
- Game implicitly consider that first player will start with 'X' option and in that case button is clicked
- For other player, the option is 'O' and the button clicked will be considered as "False"
- Set that text of the button based on player selection
- Increment the counter holding number of clicks information so that ties case can be verified
- Then check for winner
    - Whether player with option 'X' is winner or
    - Whether player with option 'O' is winner or 
    - Whether it's an tie
- Also handle one case in which if an player try to select option which is already selected by other player then alert
 prompt an alert informing to choose another option
"""


def button_click(button):
    global buttonClicked, clickCounter

    if button["text"] == " " and buttonClicked is True:
        button["text"] = "X"
        buttonClicked = False
        clickCounter += 1
        check_if_x_is_winner()
        check_if_o_is_winner()
        check_for_tie()

    elif button["text"] == " " and buttonClicked is False:
        button["text"] = "O"
        buttonClicked = True
        clickCounter += 1
        check_if_x_is_winner()
        check_if_o_is_winner()
        check_for_tie()

    else:
        messagebox.showerror("Tic Tac Toe", "This option is already selected\nPick other available option....")


"""
Function to check whether player with option 'X' is an winner or not
- There are 8 probabilities which can lead player to win the game i.e. 
  To get 3 marks in a row (up, down, across, or diagonally)
- Highlight background of winning row in red if player with option 'X' wins
- Set the winner flag to "True" so that nested function should know that game is already won
- Prompt an congratulation messages to both the players to indicate who wins the game
- After winning, the grid needs to be disabled to restrict the player fo further selection as game ends  
"""


def check_if_x_is_winner():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(highlightbackground="red")
        b2.config(highlightbackground="red")
        b3.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(highlightbackground="red")
        b4.config(highlightbackground="red")
        b7.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(highlightbackground="red")
        b5.config(highlightbackground="red")
        b6.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(highlightbackground="red")
        b8.config(highlightbackground="red")
        b9.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(highlightbackground="red")
        b5.config(highlightbackground="red")
        b8.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(highlightbackground="red")
        b6.config(highlightbackground="red")
        b9.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(highlightbackground="red")
        b5.config(highlightbackground="red")
        b9.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(highlightbackground="red")
        b5.config(highlightbackground="red")
        b7.config(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is X. Sorry O better luck next time.")
        disable_all_buttons()


"""
Function to check whether player with option 'O' is an winner or not
- There are 8 probabilities which can lead player to win the game i.e. 
  To get 3 marks in a row (up, down, across, or diagonally)
- Highlight background of winning row in yellow if player with option 'O' wins
- Set the winner flag to "True" so that nested function should know that game is already won
- Prompt an congratulation messages to both the players to indicate who wins the game
- After winning, the grid needs to be disabled to restrict the player fo further selection as game ends  
"""


def check_if_o_is_winner():
    global winner

    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(highlightbackground="yellow")
        b2.config(highlightbackground="yellow")
        b3.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time.")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(highlightbackground="yellow")
        b4.config(highlightbackground="yellow")
        b7.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time.")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(highlightbackground="yellow")
        b5.config(highlightbackground="yellow")
        b6.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time.")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(highlightbackground="yellow")
        b8.config(highlightbackground="yellow")
        b9.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time.")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(highlightbackground="yellow")
        b5.config(highlightbackground="yellow")
        b8.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(highlightbackground="yellow")
        b6.config(highlightbackground="yellow")
        b9.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(highlightbackground="yellow")
        b5.config(highlightbackground="yellow")
        b9.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(highlightbackground="yellow")
        b5.config(highlightbackground="yellow")
        b7.config(highlightbackground="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation, Winner of this game is O. Sorry X better luck next time")
        disable_all_buttons()


"""
Function to check whether the game is tied or not
- So if the players click counter incremented to 9 and there is no winner
as winner flag is still "False" 
- Then disable the grid so that players are restricted to select any option further
- Sow info to both the players to indicate the game is tied.
"""


def check_for_tie():
    global clickCounter

    if clickCounter == 9 and winner is False:
        disable_all_buttons()
        messagebox.showinfo("Tic Tac Toe",
                            "Ohh ... it's an tie, unfortunately no body wins. Please restart game to play.")


'''Function to disable all the buttons available on grid'''


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


window = Tk()
window.title('Fun Game - Tic Tac Toe')
setup()
build_menu()
window.mainloop()
