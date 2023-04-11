import random
import webbrowser as wb
input("Press Enter To Start: ")
choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while True:
    AS = random.randint(1000, 9999)
    main1 = random.choice(choice)
    main2 = random.choice(choice)
    wb.open(f"https://prnt.sc/{main1}{main2}{AS}")
    main2 = input("Press Enter For Next Picture And Exit To Go Back: ")