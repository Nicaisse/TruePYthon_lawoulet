from lawoulet import *
import keyboard




while True:
    play_game()
    restart=input("pressez k pour stopper et autre touche pour continuer :").lower()
    if restart=="k":
        exit()