level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                                   J                               J                            CX',
'X                                   X                               X                            XX',
'X                                                                                                 X',
'X J                        C       M     M                  C                                  C  X',
'XXX            XXX   XX   XXXX     XXXXXXXXXXXX     XXX    XXX                                 XXXX',
'X      XXXX                                                     XX   XXX               XX         X',
'X                                                                                   X           C X',
'X                           C                               X                XXX                  X',
'X                                X             XX     XXX                X                 X      X',
'X P                     X        X X        XXXX   X                     XX   M        X          X',
'XXX                 X   X        X     XXXXXX                                 XXXXXXX             X',
'XM  CCCCCCC       M        M    SXM                    M                M             M          SX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

tile_size = 64
screen_width = 1280
screen_height = len(level_map) * tile_size + 64

print(screen_width, screen_height)