define instructor = Character("Sergeant Boom", color="#FFFFFF")
define system = Character("SYSTEM", color="#858BFF")

image gate:
    "images/bg_gate.png"
    zoom 1.5

image hall:
    "images/bg_training_hall.png"
    zoom 1.5

image terminal:
    "images/bg_terminal_room.png"
    zoom 1.5

image q_show:
    "images/question_show.png"
    zoom 1.8

image q_fail:
    "images/question_fail.png"
    zoom 1.5

image q_ok:
    "images/question_ok.png"
    zoom 3

image flashbang = "images/flashbang.jpg"

default attempts = 0
default badge_code = 17

init python:
    if not hasattr(persistent, "fail_count") or persistent.fail_count is None:
        persistent.fail_count = 0


label start:

    $ persistent.fail_count += 1

    scene black

    "Night. A military base."

    instructor "Who are you?"

    if persistent.fail_count >= 2:
        system "You were here before..."

    jump gate_entry


label gate_entry:

    scene gate

    instructor "Why are you here?"

    menu:
        "Request entry":
            jump gate_pass
        "Stay silent":
            jump flashbang
        "Force entry":
            jump flashbang


label gate_pass:

    instructor "Okay."
    instructor "Go to security check."

    jump quadratic_mission


label quadratic_mission:

    $ attempts = 0

    scene q_show

    system "LOCK ACTIVE."
    system "CODE: x² - 5x + 6 = 0"

    instructor "Find the code."

    jump quad_menu


label quad_menu:

    menu:
        "2, 3":
            jump quad_correct
        "1, 6":
            jump quad_wrong
        "-2, -3":
            jump quad_wrong
        "0, 5":
            jump quad_wrong


label quad_wrong:

    $ attempts += 1

    scene q_fail

    if attempts == 1:
        system "WRONG."
        instructor "Try again."
        instructor "Hint: multiply = 6, add = -5"
        jump quad_menu
    else:
        jump flashbang


label quad_correct:

    scene q_ok
    system "ACCESS OK."

    pause 1.0

    jump memory_intro


label memory_intro:

    scene hall

    system "Your ID is 17."
    instructor "Remember it."

    jump scenario_1


label scenario_1:

    instructor "You hear a sound behind you."

    menu:
        "Check it":
            jump scenario1_pass
        "Ignore":
            jump flashbang
        "Run":
            jump flashbang


label scenario1_pass:

    instructor "Good."

    jump memory_test


label memory_test:

    system "Enter your ID."

    menu:
        "17":
            jump memory_correct
        "71":
            jump flashbang
        "10":
            jump flashbang
        "21":
            jump flashbang


label memory_correct:

    system "OK."

    jump pattern_mission


label pattern_mission:

    system "Find next number."
    "2, 4, 8, 16, ?"

    menu:
        "32":
            jump pattern_pass
        "24":
            jump flashbang
        "20":
            jump flashbang
        "18":
            jump flashbang


label pattern_pass:

    system "Correct."

    jump scenario_2


label scenario_2:

    instructor "Your teammate is hurt."

    menu:
        "Help":
            jump flashbang
        "Finish mission":
            jump scenario2_pass
        "Call backup":
            jump flashbang


label scenario2_pass:

    instructor "Good choice."

    jump reaction_test


label reaction_test:

    system "QUICK TEST."
    system "Choose fast."

    menu:
        "Press button NOW":
            jump reaction_pass
        "Wait":
            jump flashbang
        "Look around":
            jump flashbang


label reaction_pass:

    system "Fast enough."

    jump quadratic_2


label quadratic_2:

    $ attempts = 0

    scene q_show

    system "LOCK 2 ACTIVE."
    system "CODE: x² - 7x + 10 = 0"

    instructor "Find the code."

    jump quad2_menu


label quad2_menu:

    menu:
        "2, 5":
            jump quad2_correct
        "1, 10":
            jump quad2_wrong
        "3, 4":
            jump quad2_wrong
        "0, 7":
            jump quad2_wrong


label quad2_wrong:

    $ attempts += 1

    scene q_fail

    if attempts == 1:
        system "WRONG."
        instructor "Hint: multiply = 10, add = -7"
        jump quad2_menu
    else:
        jump flashbang


label quad2_correct:

    scene q_ok
    system "ACCESS OK."

    pause 1.0

    jump final_code


label final_code:

    system "FINAL LOCK."
    instructor "Combine ID and first code."

    menu:
        "1723":
            jump final_pass
        "2317":
            jump flashbang
        "1700":
            jump flashbang
        "9999":
            jump flashbang


label final_pass:

    jump terminal_room


label terminal_room:

    scene terminal

    system "Loading..."

    if persistent.fail_count >= 3:
        system "You failed before..."

    instructor "Ignore that."

    menu:
        "Listen to instructor":
            jump bad_ending
        "Check system":
            jump truth_route


label truth_route:

    system "This is a loop."
    system "Flashbang resets you."

    if persistent.fail_count >= 5:
        system "You remember everything now..."

        menu:
            "Break the system":
                jump secret_ending
            "Escape normally":
                jump good_ending
    else:
        menu:
            "Accept":
                jump good_ending
            "Deny":
                jump flashbang


label flashbang:

    scene white
    pause 0.1
    scene black
    pause 0.1

    show flashbang

    "FLASHBANG"

    pause 0.3

    hide flashbang
    scene black

    instructor "You failed."

    menu:
        "Restart":
            jump start
        "Quit":
            return


label good_ending:

    system "Loop ended."

    "You leave the facility."

    "ENDING: ESCAPED"

    return


label bad_ending:

    scene black

    instructor "You follow orders."

    system "Memory wipe starting..."

    show flashbang

    "FLASHBANG"

    pause 0.5

    "You forgot everything."

    "ENDING: STILL TRAPPED"

    return


label secret_ending:

    scene black

    system "Override accepted."

    system "Shutting down training..."

    "The world breaks apart."

    "Nothing is real."

    "You were the test."

    "ENDING: SYSTEM BROKEN"

    return