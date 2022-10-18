level_map = [
'X                                C                                                              C X',
'X        C          C  XX        X       C                                     X     X     XXXXXXXX',
'X       XXXX XXXX  XX                   XXXX XXXX  XXXX                X                          X',
'X   XX                    XX                                   X                                  X',
'XXX                          CX                            X                                      X',
'X   XXX  C                   XX                                   X           C                   X',
'X       XXXXX   XX                      XXXX XXXX  XX                   XXXXXXXXXXXXX             X',
'X                    XX C                                     X                     XX   XXX      X',
'X   C   P             XXXX               XXX     XX         XXX   X      C                  XX    X',
'X   XXXXXXX              XXX     XX        XXXXXXX                      XXX                      XX',
'X             C                                                                       C           X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

tile_size = 64
screen_width = 1280
screen_height = len(level_map) * tile_size

print(screen_width, screen_height)