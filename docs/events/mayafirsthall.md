# Mondays
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayafirsthall&go=Go)



## Event preconditions
✅Event "[Maya: A New Beginning](./firsttimeshrine.md)" is completed (event=firsttimeshrine)



## Next events
None

## Event properties
* ID: mayafirsthall
* Group: Maya
* Triggered by label: dormmonday
* Triggered by branch label: dorms

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label mayafirsthall:
    if _in_replay:
        play music "sweetvermouth.mp3"

    scene mayahall1
    with fade

    s "Hey, Maya. What are you up to?"
    m "What makes you think it’s okay to just approach me in the hallway?"
    s "The...fact that I am also in the hallway? And that we know each other. And that it is customary to greet the people you know."
    m "Do you know Yumi as well?"
    s "I do."

    scene mayahall2
    with dissolve

    m "Excellent. Go bother her instead, then. As you can see, I am in the middle of something very important."
    s "Are you? Because it looks to me like you’re just trying to open the door."
    m "I’m not {i}just{/i} trying to open the door. I’m attempting to escape from a man who would likely attempt to sodomize me if we were alone in the hallway right now."
    s "How come the two people who hate me the most had to choose today to hang out in the hall?"

    scene mayahall1
    with dissolve

    m "Mondays, am I right?"
    s "Distaste for Mondays aside, what are you actually up to?"

    scene mayahall3
    with dissolve

    m "Why does it matter? It’s not like I’m planning on including you."
    s "You’re kind of including me now by just responding to me."

    scene mayahall4
    with dissolve

    m "I see."
    m "Farewell."
    s "Maya, wait."

    scene mayahall5
    with dissolve

    m "{i}Why?{/i} Am I seriously not even allowed to retreat into my own room without you attempting to get involved? "
    s "I mean, I don’t plan on physically restraining you or anything. But would it kill you to converse with me for like, five minutes?"
    m "That depends entirely on what we’d talk about. I’m sure there are plenty of conversation topics that would put an end to both of us in a matter of seconds."
    s "I highly doubt that’s-"
    m "You’re not even supposed to be here. You know that, right? This is a dorm for {i}girls.{/i} "
    m "How are we supposed to feel safe at night if you’re standing outside of our doors, pressing your face against them and listening in on our conversations?"
    s "Just talk quieter if you’re worried about me listening in."

    scene mayahall6
    with dissolve

    m "So it falls on {i}us{/i} to traipse around your wrongdoings? Are you {i}that{/i} opposed to even the faintest trace of dignity?"
    s "How about this? You hang out with me for the rest of the night and I promise to never press my face against your door without permission."

    scene mayahall7
    with dissolve

    m "Counter-offer: How about you walk yourself off the nearest bridge and never set foot in this hallway again?"
    s "Only if you walk off with me."
    m "This...constant need to flirt with me will only make me hate you more, you know."
    s "I actually figured you already hated me as much as possible. So it’s good knowing I’ve still got some time left to talk to you like this before we’re done for good."
    s "Anyway, do you come here often? I like your bell."
    m "..."
    s "If you have some time, would you maybe want to go out for dinner or something?"
    m "Do not tempt me with free food. Not with that disgusting look on your face."
    s "I think this is just how I look."
    m "It is. And it’s disgusting. Go away and never look at me again."
    s "Can you at least ask Ami to come out if you’re going to take that much exception to my existence?"

    scene mayahall8
    with dissolve

    m "Ami isn’t home at the moment. May I take a message?"
    s "Sure. Tell her-"
    m "Sorry. This person’s voice mailbox is currently full. Please hang up and try again."
    s "..."
    m "..."

    scene mayahall7
    with dissolve

    m "I am going back into my room now."
    m "Do not attempt to follow me, and do not tell anyone that the two of us even {i}spoke{/i} tonight."
    s "Standing here and letting you hurl insults at me isn’t exactly {i}speaking.{/i}"
    m "Then you should have no problem doing exactly as I told you just now. "
    s "..."

    scene mayahall2
    with dissolve

    m "Goodbye."
    s "..."

    scene mayahall0
    with dissolve
    play sound "dooropen.mp3"

    s "..."

    scene black
    with dissolve2

    "Well..."
    "You can’t say I didn’t try."

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayafirsthall = True
    stop music fadeout 5.0

    "{i}Maya’s affection has somehow increased to [maya_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayahall:
    if chapthreeactive == True:
        scene mayasummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene mayahall1
        with dissolve
    else:
        scene mayahallwinter1
        with dissolve

    s "Hey there, stranger. Come here often?"
    m "…"
    s "…"
    m "Oh, sorry. Were you talking to me?"
    s "Yeah. I was wondering if-"
    m "No thanks."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Maya heads back inside without giving me an opportunity to spend time with her."
    "But, for some strange reason, I still feel as if she likes me a little more."

    $ maya_love += 1

    "{i}Maya’s affection level has increased to [maya_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikufirsthall:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label dormmonday:
    if chapthreeactive == True and yumiblock == False:
        scene summerdorm1mon
        with dissolve
    elif chapthreeactive == True and yumiblock == True:
        scene dormmonyumigone
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene monwinter
        with dissolve
    else:
        scene dorm_monday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "What should I do?"

    menu mondaymenu:
        "Knock on a door":
            jump doorknock
        "Talk to Yumi" if yumiblock == False:
            if yumifirsthall == False:
                jump yumifirsthall
            else:
                jump yumihall
        "Talk to Maya":
            if mayafirsthall == False and firsttimeshrine == True:
                jump mayafirsthall
...
```