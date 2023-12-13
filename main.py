import time
import threading
import string
import random
import sys
resp_over = False
watch = False
letters = string.ascii_lowercase
boots = False
storage_stolen = False

timerer = 720


def resp_go():
    global resp_over
    global resp_score
    resp_score = 0
    while resp_over == False:
            if boots == True:
                r_str = (''.join(random.choice(letters) for i in range(1)))
                print(r_str)
                resp_start = time.time()
                re_str = input("Go! \n")
                if re_str == r_str.upper() and time.time() - resp_start < 2:
                        print("Good job.")
                        resp_score += 2
                        r_str = (''.join(random.choice(letters) for i in range(1)))
        
                else:
                        print("You get electrocuted, game over.")
                        exit()
            if boots == False:
                r_str = (''.join(random.choice(letters) for i in range(1)))
                print(r_str)
                resp_start = time.time()
                re_str = input("Go! \n")
                if re_str == r_str.upper() and time.time() - resp_start < 1:
                        print("Good job.")
                        resp_score += 1
                        r_str = (''.join(random.choice(letters) for i in range(1)))
        
                else:
                        print("You get electrocuted, game over.")
                        exit()
                        
                        


def resp_time():
    global resp_over
    global timerer
    time.sleep(10)
    print("Stop!")
    resp_over = True
    timerer = timerer + (resp_score * 10)
    plyr.room()


def countdown():
    global timerer
    for x in range(720):
        timerer = timerer - 1
        time.sleep(1)
        while timerer == 0:
            print("Game Over.")
            exit()


countdownThread = threading.Thread(target=countdown)
countdownThread.start()


class gameState:
    #Regular method
    def __init__(self, room, tm, depth):
        self.room = room
        self.timerer = tm
        self.depth = depth
        self.gui = "You are in the " + room + "room with", tm, "seconds left, at a", depth + " depth"


def gui(self):
    print(self.gui)


if timerer == 0:
    exit()

plyr = gameState("accomRoom", timerer, "low")


def start():
    global watch
    plyr.room = start
    watch_picked = input(
        "Your eyelids are almost frozen shut, the cold weakens your movement. You see a corpse on the floor; half submerged in water with a watch attached to its wrist. \033[1;31;50m Will you take the watch yes or no? \033[0;39;50m"
    )
    watchPicked = watch_picked.lower()
    if watchPicked == "yes":
        print(
            "\nYou succesfully steal from a corpse. \n\033[1;31;50mSay \"time\" to tell the time.  \033[0;39;50m"
        )
        watch = True
        accomRoom()
    if watchPicked == "no":
        print("\nStealing from the dead does seem like a bad idea.")
        watch = False
        accomRoom()

    time.sleep(10)


def accomRoom():
    plyr.room = accomRoom
    accom_choice = input(
        "\nThere are doors to the left and right of you and a ladder on the wall leading up to a hatch. Will you climb the \033[1;31;50mladder\033[0;39;50m go through the\033[1;31;50m left\033[0;39;50m door or go through the\033[1;31;50m right\033[0;39;50m door?"
    )
    accomChoice = accom_choice.lower()
    if accomChoice == "ladder":
        pass
    if accomChoice == "left":
        auxRoom()
    if accomChoice == "right":
        storage_room()
    if accomChoice == "time" and watch == True:
        print(timerer)
        plyr.room()


def auxRoom():
    aux_choice = input(
        "\nThrough the closed door you could see the room is partly flooded, with exposed wire from the ceiling creating sparks. It's probably not a good idea to go in there. Go \033[1;31;50mback\033[0;39;50m or Go \033[1;31;50min\033[0;39;50m?"
    )

    auxChoice = aux_choice.lower()

    if auxChoice == "back":
        accomRoom()
    if auxChoice == "in":
        respGame()


def respGame():
    if boots == False:
        resp_ready = input(
                "\nWalk carefully through the water and repair the equipment. Respond to the letter given by typing the capitilized version within 1 second. \nAre you ready, \033[1;31;50myes\033[0;39;50m or \033[1;31;50mno\033[0;39;50m? "
    )
    if boots == True:
            resp_ready = input(
                "\nWalk carefully through the water and repair the equipment. Respond to the letter given by typing the capitilized version within 2 seconds. \nAre you ready, \033[1;31;50myes\033[0;39;50m or \033[1;31;50mno\033[0;39;50m? ")

    respReady = resp_ready.lower()
    if respReady == "yes":
        rsp_g = threading.Thread(target=resp_go)
        rsp_t = threading.Thread(target=resp_time)
        rsp_g.start()
        rsp_t.start()
    if respReady == "no":
        resp_back = input(
            "Would you like to go back, \033[1;31;50myes\033[0;39;50m or \033[1;31;50mno\033[0;39;50m? "
        )
        respBack = resp_back.lower()
        if respBack == "yes":
            accomRoom()
        if respBack == "no":
            auxRoom()


def storage_room():
        global storage_stolen
        global boots
        if storage_stolen == False:
            storage_Choice = input("\nThe belongings of your fellow crewmates are scattered across the floor. You see a pair of \033[1;32;50mrubber\033[0;39;50m boots, take them, \033[1;31;50myes\033[0;39;50m or \033[1;31;50mno\033[0;39;50m? They could be quite useful.")
            storage_choice = storage_Choice.lower()
            if storage_choice == "yes" and watch == True:
                    print("\nYou've got quite a nasty habit of stealing.")
                    boots = True
                    storage_stolen = True
                    accomRoom()
            if storage_choice == "yes" and watch == False:
                    print("\nYou take the rubber boots and wear them proudly.")
                    boots = True
                    storage_stolen = True
                    accomRoom()
            if storage_choice == "no" and watch == False:
                    print("\nYour feet are sad, but your soul is pure.")
                    boots = False
                    storage_stolen = True
                    accomRoom()
            if storage_choice == "no" and watch == True:
                    print("\nYour feet are surprised, they might die of shock.")
                    boots = False
                    storage_stolen = True
                    accomRoom()
        if storage_stolen == True:
            print("You can't do anything here anymore.")
            accomRoom()
        
       

#def u_hall():
    #u_hall_Choice = input("You climb up the ladder and reach a door on your \033[1;31;50left\033[0;39;50m and \033[1;31;50right\033[0;39;50m and a a \033[1;31;50hatch\033[0;39;50m straight infront of you.")
    #u_hall_choice = u_hall_Choice.lower()
    #if u_hall_choice = "left":



start()


