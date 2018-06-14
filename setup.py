import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("Chess.py")]

cx_Freeze.setup(
    name="Chess",
    options={"build_exe":{"packages":["pygame", "math", "copy"], "include_files":["black_bishop.png",

                                                                  "black_king.png",
                                                                  "black_knight.png",
                                                                  "black_pawn.png",
                                                                  "black_queen.png",
                                                                  "black_rook.png",
                                                                  "chess field.png",
                                                                  "white_bishop.png",
                                                                  "white_king.png",
                                                                  "white_knight.png",
                                                                  "white_pawn.png",
                                                                  "white_queen.png",
                                                                  "white_rook.png" ]}},
    description="-__-",
    executables=executables,
    version="1.0.0"



)