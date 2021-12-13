import tkinter as tk


SQUARE_DIM = 120
BOARD_DIM = SQUARE_DIM*8
TEXT_SIZE = 28
HAVE_DRAWN = False


global images
images = {}


def ranges(val):
    return range(val - SQUARE_DIM//2, val + SQUARE_DIM//2)
def move_piece(piece_x, piece_y, piece_name, x, y):
    if x <= 0:
        x = 1
    if x>= BOARD_DIM + 4*SQUARE_DIM:
        x = BOARD_DIM + 4*SQUARE_DIM - 1
    if y <= 0:
        y = 1
    if y>= BOARD_DIM:
        y = BOARD_DIM - 1
    piece_x.set(x)
    piece_y.set(y)
    chess_board.coords(piece_name, x, y)
def flytt(event):
    x, y = event.x, event.y
    if moving.get() == "TårnQH":
        move_piece(rookQ_W_x, rookQ_W_y, whiteRookQ_move, x, y)
    elif moving.get() == "TårnQB":
        move_piece(rookQ_B_x, rookQ_B_y, blackRookQ_move, x, y)
    elif moving.get() == "TårnKH":
        move_piece(rookK_W_x, rookK_W_y, whiteRookK_move, x, y)
    elif moving.get() == "TårnKB":
        move_piece(rookK_B_x, rookK_B_y, blackRookK_move, x, y)
    elif moving.get() == "DronningB":
        move_piece(queen_B_x, queen_B_y, blackQueen_move, x, y)
    elif moving.get() == "DronningH":
        move_piece(queen_W_x, queen_W_y, whiteQueen_move, x, y)
    elif moving.get() == "KongeB":
        move_piece(king_B_x, king_B_y, blackKing_move, x, y)
    elif moving.get() == "KongeH":
        move_piece(king_W_x, king_W_y, whiteKing_move, x, y)
    elif moving.get() == "HestQH":
        move_piece(knightQ_W_x, knightQ_W_y, whiteKnightQ_move, x, y)
    elif moving.get() == "HestQB":
        move_piece(knightQ_B_x, knightQ_B_y, blackKnightQ_move, x, y)
    elif moving.get() == "HestKH":
        move_piece(knightK_W_x, knightK_W_y, whiteKnightK_move, x, y)
    elif moving.get() == "HestKB":
        move_piece(knightK_B_x, knightK_B_y, blackKnightK_move, x, y)
    elif moving.get() == "LøperQH":
        move_piece(bishopQ_W_x, bishopQ_W_y, whiteBishopQ_move, x, y)
    elif moving.get() == "LøperQB":
        move_piece(bishopQ_B_x, bishopQ_B_y, blackBishopQ_move, x, y)
    elif moving.get() == "LøperKH":
        move_piece(bishopK_W_x, bishopK_W_y, whiteBishopK_move, x, y)
    elif moving.get() == "LøperKB":
        move_piece(bishopK_B_x, bishopK_B_y, blackBishopK_move, x, y)
    elif moving.get() == "Bonde1":
        move_piece(pawn1_x, pawn1_y, pawn1_move, x, y)
    elif moving.get() == "Bonde2":
        move_piece(pawn2_x, pawn2_y, pawn2_move, x, y)
    elif moving.get() == "Bonde3":
        move_piece(pawn3_x, pawn3_y, pawn3_move, x, y)
    elif moving.get() == "Bonde4":
        move_piece(pawn4_x, pawn4_y, pawn4_move, x, y)
    elif moving.get() == "Bonde5":
        move_piece(pawn5_x, pawn5_y, pawn5_move, x, y)
    elif moving.get() == "Bonde6":
        move_piece(pawn6_x, pawn6_y, pawn6_move, x, y)
    elif moving.get() == "Bonde7":
        move_piece(pawn7_x, pawn7_y, pawn7_move, x, y)
    elif moving.get() == "Bonde8":
        move_piece(pawn8_x, pawn8_y, pawn8_move, x, y)

    elif moving.get() == "Bonde9":
        move_piece(pawn9_x, pawn9_y, pawn9_move, x, y)
    elif moving.get() == "Bonde10":
        move_piece(pawn10_x, pawn10_y, pawn10_move, x, y)
    elif moving.get() == "Bonde11":
        move_piece(pawn11_x, pawn11_y, pawn11_move, x, y)
    elif moving.get() == "Bonde12":
        move_piece(pawn12_x, pawn12_y, pawn12_move, x, y)
    elif moving.get() == "Bonde13":
        move_piece(pawn13_x, pawn13_y, pawn13_move, x, y)
    elif moving.get() == "Bonde14":
        move_piece(pawn14_x, pawn14_y, pawn14_move, x, y)
    elif moving.get() == "Bonde15":
        move_piece(pawn15_x, pawn15_y, pawn15_move, x, y)
    elif moving.get() == "Bonde16":
        move_piece(pawn16_x, pawn16_y, pawn16_move, x, y)
    else:
        if x in ranges(rookQ_W_x.get()) and y in ranges(rookQ_W_y.get()):
            moving.set('TårnQH')
            move_piece(rookQ_W_x, rookQ_W_y, whiteRookQ_move, x, y)
        elif x in ranges(rookQ_B_x.get()) and y in ranges(rookQ_B_y.get()):
            moving.set('TårnQB')
            move_piece(rookQ_B_x, rookQ_B_y, blackRookQ_move, x, y)
        elif x in ranges(rookK_W_x.get()) and y in ranges(rookK_W_y.get()):
            moving.set('TårnKH')
            move_piece(rookK_W_x, rookK_W_y, whiteRookK_move, x, y)
        elif x in ranges(rookK_B_x.get()) and y in ranges(rookK_B_y.get()):
            moving.set('TårnKB')
            move_piece(rookK_B_x, rookK_B_y, blackRookK_move, x, y)
        elif x in ranges(queen_B_x.get()) and y in ranges(queen_B_y.get()):
            moving.set('DronningB')
            move_piece(queen_B_x, queen_B_y, blackQueen_move, x, y)
        elif x in ranges(queen_W_x.get()) and y in ranges(queen_W_y.get()):
            moving.set('DronningH')
            move_piece(queen_W_x, queen_W_y, whiteQueen_move, x, y)
        elif x in ranges(king_B_x.get()) and y in ranges(king_B_y.get()):
            moving.set('KongeB')
            move_piece(king_B_x, king_B_y, blackKing_move, x, y)
        elif x in ranges(king_W_x.get()) and y in ranges(king_W_y.get()):
            moving.set('KongeH')
            move_piece(king_W_x, king_W_y, whiteKing_move, x, y)
        elif x in ranges(knightQ_W_x.get()) and y in ranges(knightQ_W_y.get()):
            moving.set('HestQH')
            move_piece(knightQ_W_x, knightQ_W_y, whiteKnightQ_move, x, y)
        elif x in ranges(knightQ_B_x.get()) and y in ranges(knightQ_B_y.get()):
            moving.set('HestQB')
            move_piece(knightQ_B_x, knightQ_B_y, blackKnightQ_move, x, y)
        elif x in ranges(knightK_W_x.get()) and y in ranges(knightK_W_y.get()):
            moving.set('HestKH')
            move_piece(knightK_W_x, knightK_W_y, whiteKnightK_move, x, y)
        elif x in ranges(knightK_B_x.get()) and y in ranges(knightK_B_y.get()):
            moving.set('HestKB')
            move_piece(knightK_B_x, knightK_B_y, blackKnightK_move, x, y)
        elif x in ranges(bishopQ_W_x.get()) and y in ranges(bishopQ_W_y.get()):
            moving.set('LøperQH')
            move_piece(bishopQ_W_x, bishopQ_W_y, whiteBishopQ_move, x, y)
        elif x in ranges(bishopQ_B_x.get()) and y in ranges(bishopQ_B_y.get()):
            moving.set('LøperQB')
            move_piece(bishopQ_B_x, bishopQ_B_y, blackBishopQ_move, x, y)
        elif x in ranges(bishopK_W_x.get()) and y in ranges(bishopK_W_y.get()):
            moving.set('LøperKH')
            move_piece(bishopK_W_x, bishopK_W_y, whiteBishopK_move, x, y)
        elif x in ranges(bishopK_B_x.get()) and y in ranges(bishopK_B_y.get()):
            moving.set('LøperKB')
            move_piece(bishopK_B_x, bishopK_B_y, blackBishopK_move, x, y)
        elif x in ranges(pawn1_x.get()) and y in ranges(pawn1_y.get()):
            moving.set('Bonde1')
            move_piece(pawn1_x, pawn1_y, pawn1_move, x, y)
        elif x in ranges(pawn2_x.get()) and y in ranges(pawn2_y.get()):
            moving.set('Bonde2')
            move_piece(pawn2_x, pawn2_y, pawn2_move, x, y)
        elif x in ranges(pawn3_x.get()) and y in ranges(pawn3_y.get()):
            moving.set('Bonde3')
            move_piece(pawn3_x, pawn3_y, pawn3_move, x, y)
        elif x in ranges(pawn4_x.get()) and y in ranges(pawn4_y.get()):
            moving.set('Bonde4')
            move_piece(pawn4_x, pawn4_y, pawn4_move, x, y)
        elif x in ranges(pawn5_x.get()) and y in ranges(pawn5_y.get()):
            moving.set('Bonde5')
            move_piece(pawn5_x, pawn5_y, pawn5_move, x, y)
        elif x in ranges(pawn6_x.get()) and y in ranges(pawn6_y.get()):
            moving.set('Bonde6')
            move_piece(pawn6_x, pawn6_y, pawn6_move, x, y)
        elif x in ranges(pawn7_x.get()) and y in ranges(pawn7_y.get()):
            moving.set('Bonde7')
            move_piece(pawn7_x, pawn7_y, pawn7_move, x, y)
        elif x in ranges(pawn8_x.get()) and y in ranges(pawn8_y.get()):
            moving.set('Bonde8')
            move_piece(pawn8_x, pawn8_y, pawn8_move, x, y)
        elif x in ranges(pawn9_x.get()) and y in ranges(pawn9_y.get()):
            moving.set('Bonde9')
            move_piece(pawn9_x, pawn9_y, pawn9_move, x, y)
        elif x in ranges(pawn10_x.get()) and y in ranges(pawn10_y.get()):
            moving.set('Bonde10')
            move_piece(pawn10_x, pawn10_y, pawn10_move, x, y)
        elif x in ranges(pawn11_x.get()) and y in ranges(pawn11_y.get()):
            moving.set('Bonde11')
            move_piece(pawn11_x, pawn11_y, pawn11_move, x, y)
        elif x in ranges(pawn12_x.get()) and y in ranges(pawn12_y.get()):
            moving.set('Bonde12')
            move_piece(pawn12_x, pawn12_y, pawn12_move, x, y)
        elif x in ranges(pawn13_x.get()) and y in ranges(pawn13_y.get()):
            moving.set('Bonde13')
            move_piece(pawn13_x, pawn13_y, pawn13_move, x, y)
        elif x in ranges(pawn14_x.get()) and y in ranges(pawn14_y.get()):
            moving.set('Bonde14')
            move_piece(pawn14_x, pawn14_y, pawn14_move, x, y)
        elif x in ranges(pawn15_x.get()) and y in ranges(pawn15_y.get()):
            moving.set('Bonde15')
            move_piece(pawn15_x, pawn15_y, pawn15_move, x, y)
        elif x in ranges(pawn16_x.get()) and y in ranges(pawn16_y.get()):
            moving.set('Bonde16')
            move_piece(pawn16_x, pawn16_y, pawn16_move, x, y)
            
            
def place_piece(piece_x, piece_y, piece_name):
    x = piece_x.get()
    y = piece_y.get()
    x = (x//SQUARE_DIM)*SQUARE_DIM + SQUARE_DIM//2
    y = (y//SQUARE_DIM)*SQUARE_DIM + SQUARE_DIM//2
    piece_x.set(x)
    piece_y.set(y)
    chess_board.coords(piece_name, x, y)
    
def plasser(event):
    if moving.get() == "TårnQH":
        place_piece(rookQ_W_x, rookQ_W_y, whiteRookQ_move)
    elif moving.get() == "TårnQB":
        place_piece(rookQ_B_x, rookQ_B_y, blackRookQ_move)
    elif moving.get() == "DronningB":
        place_piece(queen_B_x, queen_B_y, blackQueen_move)
    elif moving.get() == "DronningH":
        place_piece(queen_W_x, queen_W_y, whiteQueen_move)
    elif moving.get() == "KongeB":
        place_piece(king_B_x, king_B_y, blackKing_move)
    elif moving.get() == "KongeH":
        place_piece(king_W_x, king_W_y, whiteKing_move)
    elif moving.get() == "TårnKH":
        place_piece(rookK_W_x, rookK_W_y, whiteRookK_move)
    elif moving.get() == "TårnKB":
        place_piece(rookK_B_x, rookK_B_y, blackRookK_move)
    elif moving.get() == "HestQH":
        place_piece(knightQ_W_x, knightQ_W_y, whiteKnightQ_move)
    elif moving.get() == "HestQB":
        place_piece(knightQ_B_x, knightQ_B_y, blackKnightQ_move)
    elif moving.get() == "HestKH":
        place_piece(knightK_W_x, knightK_W_y, whiteKnightK_move)
    elif moving.get() == "HestKB":
        place_piece(knightK_B_x, knightK_B_y, blackKnightK_move)
    elif moving.get() == "LøperQH":
        place_piece(bishopQ_W_x, bishopQ_W_y, whiteBishopQ_move)
    elif moving.get() == "LøperQB":
        place_piece(bishopQ_B_x, bishopQ_B_y, blackBishopQ_move)
    elif moving.get() == "LøperKH":
        place_piece(bishopK_W_x, bishopK_W_y, whiteBishopK_move)
    elif moving.get() == "LøperKB":
        place_piece(bishopK_B_x, bishopK_B_y, blackBishopK_move)
    elif moving.get() == "Bonde1":
        place_piece(pawn1_x, pawn1_y, pawn1_move)
    elif moving.get() == "Bonde2":
        place_piece(pawn2_x, pawn2_y, pawn2_move)
    elif moving.get() == "Bonde3":
        place_piece(pawn3_x, pawn3_y, pawn3_move)
    elif moving.get() == "Bonde4":
        place_piece(pawn4_x, pawn4_y, pawn4_move)
    elif moving.get() == "Bonde5":
        place_piece(pawn5_x, pawn5_y, pawn5_move)
    elif moving.get() == "Bonde6":
        place_piece(pawn6_x, pawn6_y, pawn6_move)
    elif moving.get() == "Bonde7":
        place_piece(pawn7_x, pawn7_y, pawn7_move)
    elif moving.get() == "Bonde8":
        place_piece(pawn8_x, pawn8_y, pawn8_move)
    elif moving.get() == "Bonde9":
        place_piece(pawn9_x, pawn9_y, pawn9_move)
    elif moving.get() == "Bonde10":
        place_piece(pawn10_x, pawn10_y, pawn10_move)
    elif moving.get() == "Bonde11":
        place_piece(pawn11_x, pawn11_y, pawn11_move)
    elif moving.get() == "Bonde12":
        place_piece(pawn12_x, pawn12_y, pawn12_move)
    elif moving.get() == "Bonde13":
        place_piece(pawn13_x, pawn13_y, pawn13_move)
    elif moving.get() == "Bonde14":
        place_piece(pawn14_x, pawn14_y, pawn14_move)
    elif moving.get() == "Bonde15":
        place_piece(pawn15_x, pawn15_y, pawn15_move)
    elif moving.get() == "Bonde16":
        place_piece(pawn16_x, pawn16_y, pawn16_move)
    moving.set('')

root = tk.Tk()
moving = tk.StringVar()

chess_board = tk.Canvas(root, width = BOARD_DIM + 4*SQUARE_DIM, height = BOARD_DIM)
chess_board.grid(row = 1, column = 1)
i, j = 1, 1
for x in range(0, BOARD_DIM, SQUARE_DIM):
    for y in range(0, BOARD_DIM, SQUARE_DIM):
        if i%2 != 0 and j%2 != 0:
            chess_board.create_rectangle(x, y, x + SQUARE_DIM, y + SQUARE_DIM, fill = "gray99")
        elif i%2 != 0 and j%2 == 0:
            chess_board.create_rectangle(x, y, x + SQUARE_DIM, y + SQUARE_DIM, fill = "gray40")
        elif i%2 == 0 and j%2 != 0:
            chess_board.create_rectangle(x, y, x + SQUARE_DIM, y + SQUARE_DIM, fill = "gray40")
        elif i%2 == 0 and j%2 == 0:
            chess_board.create_rectangle(x, y, x + SQUARE_DIM, y + SQUARE_DIM, fill = "gray99")
        j += 1
    i += 1

coord_y = tk.Canvas(root, width = SQUARE_DIM/4, height = BOARD_DIM)
coord_y.grid(row = 1, column = 0)
num = 8
for y in range(0, BOARD_DIM, SQUARE_DIM):
    coord_y.create_text(SQUARE_DIM/8, y + SQUARE_DIM/2, text = num, font = ("Courier", TEXT_SIZE), anchor = "center")
    num += -1
text = "abcdefgh"
num = 0
coord_x = tk.Canvas(root, width = BOARD_DIM, height = SQUARE_DIM/4)
coord_x.grid(row = 2, column = 1, sticky = "w")
for x in range(0, BOARD_DIM, SQUARE_DIM):
    letter = text[num]
    num += 1
    coord_x.create_text(x + SQUARE_DIM/2, SQUARE_DIM/8, text = letter, font = ("Courier", TEXT_SIZE), anchor = "center")


#Tårn:
rookQ_B_x, rookQ_B_y = tk.IntVar(), tk.IntVar()
rookQ_B_x.set(SQUARE_DIM//2)
rookQ_B_y.set(SQUARE_DIM//2)
rookQ_W_x, rookQ_W_y = tk.IntVar(), tk.IntVar()
rookQ_W_x.set(SQUARE_DIM//2)
rookQ_W_y.set(BOARD_DIM - SQUARE_DIM//2)
rookK_B_x, rookK_B_y = tk.IntVar(), tk.IntVar()
rookK_B_x.set(7*SQUARE_DIM + SQUARE_DIM//2)
rookK_B_y.set(SQUARE_DIM//2)
rookK_W_x, rookK_W_y = tk.IntVar(), tk.IntVar()
rookK_W_x.set(7*SQUARE_DIM + SQUARE_DIM//2)
rookK_W_y.set(BOARD_DIM - SQUARE_DIM//2)
blackRook = "Images/tb.png"
images[blackRook] = tk.PhotoImage(file = blackRook)
blackRookQ_move = chess_board.create_image((rookQ_B_x.get(), rookQ_B_y.get()), image = images[blackRook], anchor = "center")
blackRookK_move = chess_board.create_image((rookK_B_x.get(), rookK_B_y.get()), image = images[blackRook], anchor = "center")
whiteRook= "Images/th.png"
images[whiteRook] = tk.PhotoImage(file = whiteRook)
whiteRookQ_move = chess_board.create_image((rookQ_W_x.get(), rookQ_W_y.get()), image = images[whiteRook], anchor = "center")
whiteRookK_move = chess_board.create_image((rookK_W_x.get(), rookK_W_y.get()), image = images[whiteRook], anchor = "center")


#Dronning:
queen_B_x, queen_B_y = tk.IntVar(), tk.IntVar()
queen_B_x.set(3*SQUARE_DIM + SQUARE_DIM//2)
queen_B_y.set(SQUARE_DIM//2)
queen_W_x, queen_W_y = tk.IntVar(), tk.IntVar()
queen_W_x.set(3*SQUARE_DIM + SQUARE_DIM//2)
queen_W_y.set(BOARD_DIM - SQUARE_DIM//2)
blackQueen = "Images/qb.png"
images[blackQueen] = tk.PhotoImage(file = blackQueen)
blackQueen_move = chess_board.create_image((queen_B_x.get(), queen_B_y.get()), image = images[blackQueen], anchor = "center")
whiteQueen = "Images/qh.png"
images[whiteQueen] = tk.PhotoImage(file = whiteQueen)
whiteQueen_move = chess_board.create_image((queen_W_x.get(), queen_W_y.get()), image = images[whiteQueen], anchor = "center")


#Konge:
king_B_x, king_B_y = tk.IntVar(), tk.IntVar()
king_B_x.set(4*SQUARE_DIM + SQUARE_DIM//2)
king_B_y.set(SQUARE_DIM//2)
king_W_x, king_W_y = tk.IntVar(), tk.IntVar()
king_W_x.set(4*SQUARE_DIM + SQUARE_DIM//2)
king_W_y.set(BOARD_DIM - SQUARE_DIM//2)
blackKing = "Images/kb.png"
images[blackKing] = tk.PhotoImage(file = blackKing)
blackKing_move = chess_board.create_image((king_B_x.get(), king_B_y.get()), image = images[blackKing], anchor = "center")
whiteKing = "Images/kh.png"
images[whiteKing] = tk.PhotoImage(file = whiteKing)
whiteKing_move = chess_board.create_image((king_W_x.get(), king_W_y.get()), image = images[whiteKing], anchor = "center")


#Hest:
knightQ_B_x, knightQ_B_y = tk.IntVar(), tk.IntVar()
knightQ_B_x.set(SQUARE_DIM + SQUARE_DIM//2)
knightQ_B_y.set(SQUARE_DIM//2)
knightQ_W_x, knightQ_W_y = tk.IntVar(), tk.IntVar()
knightQ_W_x.set(SQUARE_DIM + SQUARE_DIM//2)
knightQ_W_y.set(BOARD_DIM - SQUARE_DIM//2)
knightK_B_x, knightK_B_y = tk.IntVar(), tk.IntVar()
knightK_B_x.set(6*SQUARE_DIM + SQUARE_DIM//2)
knightK_B_y.set(SQUARE_DIM//2)
knightK_W_x, knightK_W_y = tk.IntVar(), tk.IntVar()
knightK_W_x.set(6*SQUARE_DIM + SQUARE_DIM//2)
knightK_W_y.set(BOARD_DIM - SQUARE_DIM//2)
blackKnight = "Images/hb.png"
images[blackKnight] = tk.PhotoImage(file = blackKnight)
blackKnightQ_move = chess_board.create_image((knightQ_B_x.get(), knightQ_B_y.get()), image = images[blackKnight], anchor = "center")
blackKnightK_move = chess_board.create_image((knightK_B_x.get(), knightK_B_y.get()), image = images[blackKnight], anchor = "center")
whiteKnight = "Images/hh.png"
images[whiteKnight] = tk.PhotoImage(file = whiteKnight)
whiteKnightQ_move = chess_board.create_image((knightQ_W_x.get(), knightQ_W_y.get()), image = images[whiteKnight], anchor = "center")
whiteKnightK_move = chess_board.create_image((knightK_W_x.get(), knightK_W_y.get()), image = images[whiteKnight], anchor = "center")

#Løper:
bishopQ_B_x, bishopQ_B_y = tk.IntVar(), tk.IntVar()
bishopQ_B_x.set( 2*SQUARE_DIM + SQUARE_DIM//2)
bishopQ_B_y.set(SQUARE_DIM//2)
bishopQ_W_x, bishopQ_W_y = tk.IntVar(), tk.IntVar()
bishopQ_W_x.set( 2*SQUARE_DIM + SQUARE_DIM//2)
bishopQ_W_y.set(BOARD_DIM - SQUARE_DIM//2)
bishopK_B_x, bishopK_B_y = tk.IntVar(), tk.IntVar()
bishopK_B_x.set(5*SQUARE_DIM + SQUARE_DIM//2)
bishopK_B_y.set(SQUARE_DIM//2)
bishopK_W_x, bishopK_W_y = tk.IntVar(), tk.IntVar()
bishopK_W_x.set(5*SQUARE_DIM + SQUARE_DIM//2)
bishopK_W_y.set(BOARD_DIM - SQUARE_DIM//2)
blackBishop = "Images/lb.png"
images[blackBishop] = tk.PhotoImage(file = blackBishop)
blackBishopQ_move = chess_board.create_image((bishopQ_B_x.get(), bishopQ_B_y.get()), image = images[blackBishop], anchor = "center")
blackBishopK_move = chess_board.create_image((bishopK_B_x.get(), bishopK_B_y.get()), image = images[blackBishop], anchor = "center")
whiteBishop = "Images/lh.png"
images[whiteBishop] = tk.PhotoImage(file = whiteBishop)
whiteBishopQ_move = chess_board.create_image((bishopQ_W_x.get(), bishopQ_W_y.get()), image = images[whiteBishop], anchor = "center")
whiteBishopK_move = chess_board.create_image((bishopK_W_x.get(), bishopK_W_y.get()), image = images[whiteBishop], anchor = "center")


#Bøndene
blackPawn1 = "Images/bb.png"
images[blackPawn1] = tk.PhotoImage(file = blackPawn1)
blackPawn2 = "Images/bb.png"
images[blackPawn2] = tk.PhotoImage(file = blackPawn2)
blackPawn3 = "Images/bb.png"
images[blackPawn3] = tk.PhotoImage(file = blackPawn3)
blackPawn4 = "Images/bb.png"
images[blackPawn4] = tk.PhotoImage(file = blackPawn4)
blackPawn5 = "Images/bb.png"
images[blackPawn5] = tk.PhotoImage(file = blackPawn5)
blackPawn6 = "Images/bb.png"
images[blackPawn6] = tk.PhotoImage(file = blackPawn6)
blackPawn7 = "Images/bb.png"
images[blackPawn7] = tk.PhotoImage(file = blackPawn7)
blackPawn8 = "Images/bb.png"
images[blackPawn8] = tk.PhotoImage(file = blackPawn8)
whitePawn = "Images/bh.png"
images[whitePawn] = tk.PhotoImage(file = whitePawn)

#Bonde 1:
pawn1_x, pawn1_y = tk.IntVar(), tk.IntVar()
pawn1_x.set(SQUARE_DIM//2)
pawn1_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn1_move = chess_board.create_image((pawn1_x.get(), pawn1_y.get()), image = images[blackPawn1], anchor = "center")

#Bonde 2:
pawn2_x, pawn2_y = tk.IntVar(), tk.IntVar()
pawn2_x.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn2_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn2_move = chess_board.create_image((pawn2_x.get(), pawn2_y.get()), image = images[blackPawn2], anchor = "center")

#Bonde 3:
pawn3_x, pawn3_y = tk.IntVar(), tk.IntVar()
pawn3_x.set(SQUARE_DIM//2 + 2*SQUARE_DIM)
pawn3_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn3_move = chess_board.create_image((pawn3_x.get(), pawn3_y.get()), image = images[blackPawn3], anchor = "center")

#Bonde 4:
pawn4_x, pawn4_y = tk.IntVar(), tk.IntVar()
pawn4_x.set(SQUARE_DIM//2 + 3*SQUARE_DIM)
pawn4_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn4_move = chess_board.create_image((pawn4_x.get(), pawn4_y.get()), image = images[blackPawn4], anchor = "center")

#Bonde 5:
pawn5_x, pawn5_y = tk.IntVar(), tk.IntVar()
pawn5_x.set(SQUARE_DIM//2 + 4*SQUARE_DIM)
pawn5_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn5_move = chess_board.create_image((pawn5_x.get(), pawn5_y.get()), image = images[blackPawn5], anchor = "center")

#Bonde 6:
pawn6_x, pawn6_y = tk.IntVar(), tk.IntVar()
pawn6_x.set(SQUARE_DIM//2 + 5*SQUARE_DIM)
pawn6_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn6_move = chess_board.create_image((pawn6_x.get(), pawn6_y.get()), image = images[blackPawn6], anchor = "center")

#Bonde 7:
pawn7_x, pawn7_y = tk.IntVar(), tk.IntVar()
pawn7_x.set(SQUARE_DIM//2 + 6*SQUARE_DIM)
pawn7_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn7_move = chess_board.create_image((pawn7_x.get(), pawn7_y.get()), image = images[blackPawn7], anchor = "center")

#Bonde 8:
pawn8_x, pawn8_y = tk.IntVar(), tk.IntVar()
pawn8_x.set(SQUARE_DIM//2 + 7*SQUARE_DIM)
pawn8_y.set(SQUARE_DIM//2 + SQUARE_DIM)
pawn8_move = chess_board.create_image((pawn8_x.get(), pawn8_y.get()), image = images[blackPawn8], anchor = "center")

#Bonde 9:
pawn9_x, pawn9_y = tk.IntVar(), tk.IntVar()
pawn9_x.set(SQUARE_DIM//2 + 0*SQUARE_DIM)
pawn9_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn9_move = chess_board.create_image((pawn9_x.get(), pawn9_y.get()), image = images[whitePawn], anchor = "center")

#Bonde 10:
pawn10_x, pawn10_y = tk.IntVar(), tk.IntVar()
pawn10_x.set(SQUARE_DIM//2 + 1*SQUARE_DIM)
pawn10_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn10_move = chess_board.create_image((pawn10_x.get(), pawn10_y.get()), image = images[whitePawn], anchor = "center")

#Bonde 11:
pawn11_x, pawn11_y = tk.IntVar(), tk.IntVar()
pawn11_x.set(SQUARE_DIM//2 + 2*SQUARE_DIM)
pawn11_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn11_move = chess_board.create_image((pawn11_x.get(), pawn11_y.get()), image = images[whitePawn], anchor = "center")

#Bonde 12:
pawn12_x, pawn12_y = tk.IntVar(), tk.IntVar()
pawn12_x.set(SQUARE_DIM//2 + 3*SQUARE_DIM)
pawn12_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn12_move = chess_board.create_image((pawn12_x.get(), pawn12_y.get()), image = images[whitePawn], anchor = "center")

#Bonde 13:
pawn13_x, pawn13_y = tk.IntVar(), tk.IntVar()
pawn13_x.set(SQUARE_DIM//2 + 4*SQUARE_DIM)
pawn13_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn13_move = chess_board.create_image((pawn13_x.get(), pawn13_y.get()), image = images[whitePawn], anchor = "center")

#Bonde 14:
pawn14_x, pawn14_y = tk.IntVar(), tk.IntVar()
pawn14_x.set(SQUARE_DIM//2 + 5*SQUARE_DIM)
pawn14_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn14_move = chess_board.create_image((pawn14_x.get(), pawn14_y.get()), image = images[whitePawn], anchor = "center")


#Bonde 15:
pawn15_x, pawn15_y = tk.IntVar(), tk.IntVar()
pawn15_x.set(SQUARE_DIM//2 + 6*SQUARE_DIM)
pawn15_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn15_move = chess_board.create_image((pawn15_x.get(), pawn15_y.get()), image = images[whitePawn], anchor = "center")

#Bonde 16:
pawn16_x, pawn16_y = tk.IntVar(), tk.IntVar()
pawn16_x.set(SQUARE_DIM//2 + 7*SQUARE_DIM)
pawn16_y.set(BOARD_DIM - SQUARE_DIM//2 - SQUARE_DIM)
pawn16_move = chess_board.create_image((pawn16_x.get(), pawn16_y.get()), image = images[whitePawn], anchor = "center")




root.bind("<B1-Motion>", flytt)
root.bind("<ButtonRelease-1>", plasser)
root.mainloop()
