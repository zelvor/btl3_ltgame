level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                                                                                                 X',
'X                                                                                                 X',
'X                                                                                                 X',
'X C             S          C                                C                                  C  X',
'XXX            XXX    X   XXX      XXX      XXX     XX     XXX                                 XXXX',
'X      XX                                                            XXX               XX         X',
'X                                                                                   X           C X',
'X                                               C      C                       XX                 X',
'X                                              XXX    XXX                XX                       X',
'X   S   P J               C             J   XXXX        XXXX        XX            S               X',
'X   XXXXXXX                            XXXXXX       X      XXXXX              XXXXXXX             X',
'X             C                                                                       C           X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

tile_size = 64
screen_width = 1280
screen_height = len(level_map) * tile_size + 64

print(screen_width, screen_height)