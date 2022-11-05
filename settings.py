level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X       C                           C                               C                             X',
'X       XXX                         X                               X                            XX',
'X                                                                                                 X',
'X J                        C       M     M J                CJ                               J C  X',
'XXX      H     XXX   XX   XXXX     XXXXXXXXXXXX     XXX    XXX       H          S       C    XXXXXX',
'X      XXXX                                                     XX   XXXXXX     XX     XX         X',
'X                                                                                   X             X',
'X                           C                               X                 XX                  X',
'X                           X    X             XX     XXX                          X       X      X',
'X P      H              X        X X   H    XXXX   X                          M    C   X          X',
'XXX     XXXX  XXX   X   X        X     XXXXXX                                 XXXXXXX             X',
'XM    X           M   S    M      M              H     M   C   S        M             M           X',
'XXXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

tile_size = 64
screen_width = 1280
screen_height = len(level_map) * tile_size + 64

print(screen_width, screen_height)