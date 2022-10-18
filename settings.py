level_map = [
'X                        XX                                                                        ',
'X                      XX        X                                             X     X     XXXXXXXX',
'X       XXXX XXXX  XX                   XXXX XXXX  XXXX                X                          X',
'X   XX                    XX                                   X                                  X',
'XXX                           X                            X                                      X',
'X   XXX                      XX                                   X                               X',
'X       XXXXX   XX                      XXXX XXXX  XX                   XXXXXXXXXXXXX             X',
'X                    XX                                       X                     XX   XXX      X',
'X       P             XXXX               XXX     XX         XXX   X                         XX    X',
'X   XXXXXXX              XXX     XX        XXXXXXX                      XXX                      XX',
'X                                                                                                 X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

tile_size = 64
screen_width = 1280
screen_height = len(level_map) * tile_size

print(screen_width, screen_height)