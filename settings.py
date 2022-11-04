level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X       C                           C                               C                            CX',
'X       XXX                         X                               X                            XX',
'X                                                                                                 X',
'X J                        C       M     M J                CJ                               J C  X',
'XXX            XXX   XX   XXXX     XXXXXXXXXXXX     XXX    XXX                  S       C    XXXXXX',
'X      XXXX                                                     XX   XXX        XX     XX         X',
'X                                                                                   X             X',
'X                           C                               X                 XX                  X',
'X                           X    X             XX     XXX              X                   X      X',
'X P                     X        X X        XXXX   X                   XXXX   M        X          X',
'XXX     XXXX  XXX   X   X        X     XXXXXX                                 XXXXXXX             X',
'XM    X           M   S    M      M                    M       S        M             M           X',
'XXXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

tile_size = 64
screen_width = 1280
screen_height = len(level_map) * tile_size + 64

print(screen_width, screen_height)