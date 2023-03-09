# Tick Tock Tick Tock Tick Tock
Happy scenes event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ticktock&go=Go)



## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: ticktock
* Group: Happy scenes
* Triggered by label: doorknock
* Triggered by branch label: doorknock

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label ticktock:
    play sound "static.mp3"

    if bonus == True:
        scene ticktock3
        with flash
    else:
        scene 0
        with flash

    stop sound
    play music "amiasleep.mp3"

    six "おかえり"

    "I teleport back to my favorite room in the world. "
    "And thankfully, I’m all alone with my favorite girl."

    if bonus == True:
        "Her name is 61 6d 20 69 20 6f 6b 61 79 and she refuses to have sexual intercourse with me on her best friend’s bed."
    else:
        "Her name is 61 6d 20 69 20 6f 6b 61 79 and she's really tired of having to revise so many important scenes in this stupid game to comply with community guidelines."

    "The reason for this is that she isn’t really like you and me. "

    if bonus == True:
        "She doesn’t approve of [incest]."
    else:
        "She doesn't approve of the current economic downturn, a thing that has definitely always been a part of this event and was not just added in right now."

    "This is because she is an emissary of {s}GOD God gOD goD GOd{/s} HOPE."

    if bonus == True:
        "In addition to [incest], there are many other things she doesn’t approve of."
    else:
        "Banana."

    "She thinks that mayonnaise is a horrible condiment."
    "I disagree."
    "She doesn’t understand the need for the yellow light on traffic lights."
    "I disagree with that as well."
    "That light saves many lives."
    "Just as I do."
    "Just as we do."
    "Alone down here in the greatest room in the world."

    six "How is your day so far, Sensei?"
    s "Good. Thank you, 61 6d 20 69 20 6f 6b 61 79."
    s "How is yours?"
    six "It would be better if I could leave. Lol."
    s "Lol. Yeah, that would be nice."
    s "I’m sorry you’re trapped down here."
    six "It’s okay. As long as you come to visit me every once in a while, I’ll manage to stay sane."
    s "That’s nice."
    six "Hey, [amimaster], can I ask you a question?"
    s "Of course."
    six "What do you think all of this means?"
    s "All of what?"
    s "This is a normal day at the bottom of everything."

    if bonus == True:
        six "It doesn’t confuse you at all? Seeing me naked and surrounded by clocks?"
    else:
        six "It doesn’t confuse you at all? Seeing me as a 0 instead who I normally am?"

    s "This is the way I’ve always seen you."
    six "Really? Just a girl in a room with clocks?"
    s "Yup."
    six "Weird."
    s "Yup."
    six "…"
    s "…"

    if bonus == True:
        six "Wanna have sex?"
    else:
        six "Wanna hug?"

    menu:
        "Yes":
            if bonus == True:
                s "I would like to have sex."
            else:
                s "I would like to hug."

    six "Nail me to the wall, [ayanemaster]."

    if bonus == False:
        s "I don't know if I'm allowed."
        six "..."
        s "Actually, is there anything in this event I'm going to have to remember for another one of those puzzle things?"
        s "Because, if not, I should probably just back out of this."
        six "..."
        s "Yeah. On second thought, I should probably just do that."
        s "Do you know the way out by any chance?"
        six "..."
        s "...?"
        s "Uhh...well, okay. I guess I can just look for an exit or something."

        scene black
        with dissolve

        "I exit the room with clocks and it takes me a whole seven minutes to make my way back to Kumon-mi."
        "I couldn't even bring up my GPS because the reception down there was horrible."
        "I am going to leave a bad review for it on TripAdvisor."

        "{i}Congratulations!{/i}"
        "{i}You haven’t unlocked anything special. I just wanted to remind you how much I love you.{/i}"
        "=)"
        "{i}Everything you believe in is fake!{/i}"
        "{i}The only {s}living{/s} real thing is Kumon-mi!{/i}"
        "{i}All that happens here is gospel!{/i}"
        "{i}Throw yourself into {s}the wishing well{/s} a new, happier life!{/i}"
        "{i}Praise be!{/i}"

        "………"
        "……"
        "…"

        $ renpy.end_replay()
        $ ticktock = False
        $ ticktocktrack = True

        if day < 6:
            jump endofweekday
        else:
            jump endofsat
    else:
        jump ticktockx

label trinity1:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
play sound "knock.mp3"

                        s "Hey Makoto, are you in there?"
                        "..."
                        "There's no answer."
                        jump doorknock

                "Miku (Current Affection - [miku_love])"if mikublock == False:
                    if miku_love >= 5 and day != 2:
                        jump mikudorm
                    if day == 2:
                        play sound "knock.mp3"

                        s "Hey, Miku. Are you in there?"
                        mi "Nope! Down here! Ya walked right past me."
                        mi "I get it, though! I'm kinda easy to miss, hahahah!"
                        s "You really are..."

                        jump mikuhall
                    else:
                        play sound "knock.mp3"

                        s "Hey Miku, are you in there?"
                        "..."
                        "There's no answer."
                        jump doorknock

                "Go Back":
                    jump doorknock
        "Room 4 (Rin & Futaba)":
            "Who do I want to talk to?"
            menu:
                    "Rin (Current Affection - [rin_love])":
                        if cafe15 == True and cafe20 == True and rindorm20 == False:
                            jump rindorm
                        if cafe15 == True and rindorm20 == False or rinsad == True:
                            play sound "knock.mp3"

                            s "Hey Rin, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock
                        if beachvacation16 == True and cafe30 == False or rinsad == True:
                            play sound "knock.mp3"

                            s "Hey Rin, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock
                        if rin_love >= 5 and cafesugar == True and day != 3:
                            jump rindorm
                        if day == 3:
                            play sound "knock.mp3"
                            s "Hey Rin, are you in there?"

                            if cafe15 == True and rindorm20 == False or rinsad == True:
                                "..."
                                "There's no answer."
                                jump doorknock
                            if beachvacation16 == True and rindorm35 == False or rinsad == True:
                                "..."
                                "There's no answer."
                                jump doorknock
                            else:
                                r "Uhhhhh...Look down here?"
                                s "Huh? Oh, damn. My bad."
                                jump rinhall
                        else:
                            play sound "knock.mp3"

                            s "Hey Rin, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock


                    "Futaba (Current Affection - [futaba_love])":
                        if futaba_love >= 5 and day != 2:
                            jump futabadorm
                        if day == 2:
                            play sound "knock.mp3"
                            s "Hey Futaba, are you in there?"
                            f "Umm...Sensei?...I'm right next to you..."
                            s "Huh? Oh, right. Sorry."
                            jump futabahall
                        else:
                            play sound "knock.mp3"

                            s "Hey Futaba, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock

                    "Go Back":
                        jump doorknock
        "Room 5 (Ami & Maya)":
            if roomwithclocks == True:
                jump roomwithclocks
            if ticktock == True:
                jump ticktock
...
```