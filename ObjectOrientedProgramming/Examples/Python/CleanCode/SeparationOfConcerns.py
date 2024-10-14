import string


class Gui(Observable):
    grid_rows = [8, 7, 6, 5, 4, 3, 2, 1]

    def onKeyPress(self, event):
        # on ESC exit App
        if event.keycode == 27:
            self.exitGUI()

    def exitGUI(self):
        self.window.destroy()

    def new_game(self):
        self._notify('gui_start_new_game')

    def initBoard(self):
        # list A - H
        alphaList = list(string.ascii_uppercase)[:10]
        rowList = list(range(10))
        colList = list(range(10))
        colRevList = list(reversed(colList))

        print(colList[1])
        print(colRevList[1])

        for r in rowList:
            if r == 0 or r == 9:
                for c in colList:
                    if c == 0 or c == 9:
                        self.createLable(r, c, "", False)
                    else:
                        t = alphaList[c - 1]
                        self.createLable(r, c, f"{t}", False)
            else:
                for c in colList:
                    cr = colRevList[r]
                    if c == 0 or c == 9:
                        self.createLable(r, c, f"{cr}", False)
                    else:
                        t = alphaList[c - 1]
                        self.createLable(r, c, f"{t}{cr}")

    def button_pressed(self, col, row):
        col -= 1
        row = abs(8 - row)  # Return the absolute value of a number
        self._notify('gui_board_input', [col, row])

    def update_board(self, data):
        is_white = False
        for col_index, board_col in enumerate(data):
            for row_index, field in enumerate(board_col):
                for b in self.button_list:
                    col = col_index + 1
                    row = 8 - row_index
                    button = b[2]
                    if col == b[0] and row == b[1]:
                        if field.piece is not None:
                            img_path = field.piece.get_img_path()
                            img = tk.PhotoImage(file=img_path)
                            r_img = img.subsample(3, 3)
                            self.button_img_list.append(r_img)
                            button.configure(image=r_img)
                        else:
                            button.configure(image="")

                        # clickable
                        if field.clickable:
                            button.configure(state="normal")
                        else:
                            button.configure(state="disable")
                        # highlight
                        if field.highlighted:
                            bg_color = "#ffff00"
                        elif is_white:
                            bg_color = "#FECE9E"
                        else:
                            bg_color = "#D38B41"
                        button.configure(bg=bg_color)
                # creat checkerboard muster
                is_white = not is_white
            is_white = not is_white