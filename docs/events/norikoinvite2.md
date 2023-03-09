# Beginnings. Endings. Things in Between.
Noriko event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikoinvite2&go=Go)


Part of event chain [New Shoes](./norikoinvite1.md)

## Event preconditions
✅Event "[Noriko: Kind Of, Yes. Kind Of, No.](./norikodorm10.md)" is completed (event=norikodorm10)



## Next events
* [Maya: What it Means to Be Destroyed](./mayadorm30.md)

## Event properties
* ID: norikoinvite2
* Group: Noriko
* Triggered by label: norikoinvite1

## Event code
File: \game\NorikoEvents.rpy
Code:
```python
...
label norikoinvite2:
    scene norikofirstinvptwo1
    with dissolve

    s "Hah..."

    "I’ve lived here for how long now and I’m {i}just{/i} finding out there’s a spare key?"
    "I guess it makes locking this door pointless, but I might as well do {i}something{/i} while Noriko composes herself."
    "As soon as we heard the door close, she sprinted out of Ami’s room and ran off, presumably to the bathroom, saying that she needed a minute and will be gone before I know it."
    "Frankly, I feel like this entire situation is a little over the top."
    "I still have no idea what happened between her and Maya, but I at least hope it was something {i}big{/i} if simply being found inside of my house is enough to worry everyone."

    scene black
    with dissolve

    "I make my way back to my room and-"

    play sound "static.mp3"
    scene happy9
    with flash
    scene happy8
    with flash
    scene happy7
    with flash
    scene whythesky
    with flash
    stop sound

    "(sədn)"
    "I make my way back to the sky instead of my room."
    "It’s much brighter up here than it will ever be inside of that prison."
    "But, if you really think about it, isn’t the sky a prison too?"
    "A prison is something you are forced to live in or around or on top of or below, and the sky is at least half of those things."
    "Think back to when you were young."
    "Picture yourself in the backseat of a car, looking out of the window as your parents drive down the highway."
    "If you didn’t have parents, think of a bus."
    "When you looked up at the sky, half concealed by deceivingly tall trees in surrounding forests-"
    "Did you ever think the clouds were following you?"
    "You’d drive and drive and drive...but the clouds would never go away."
    "And you were too young to understand science or spatial reasoning (If that even counts clouds as objects and not something entirely unrelated), so you didn’t even bother considering that-"
    "Well, they’re {i}not{/i} actually following you."
    "But they {i}are{/i} following you."
    "The sky follows you!"
    "The world follows you!"
    "You can not escape!"
    "You can not leave!"
    "Fall deeper into the wishing well!"

    play sound "static.mp3"
    scene norikofirstinvptwo2
    with flash
    stop sound

    s "…"

    "I find myself back in my room, but I don’t remember walking here."
    "That seems to be happening a lot lately."
    "I’ll be just minding my own business, following a particularly slow or decrepit train of thought when-"

    if bonus == True:
        jump norikofirstinvx
    else:
        scene black
        stop music

        "Noriko runs into the bedroom with a tray of Totino's pizza rolls and the two of us have a pizza roll party."

        $ renpy.end_replay()
        $ noriko_love += 1
        $ norikoinvite2 = True
        stop music fadeout 10.0

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label norikospecial20:
...
```

## Code that triggers this event
File: \game\NorikoEvents.rpy
Code:
```python
...
scene norikofirstvisit35
    with dissolve

    m "You’re weird."
    a "Yeah. I guess I...am kind of weird."
    m "No, like you’re acting weird."
    m "What’s going on?"
    m "Is everything okay?"

    scene norikofirstvisit36
    with dissolve

    m "Is Sensei-"

    scene norikofirstvisit37
    with hpunch

    a "Taking a nap!"
    a "We got karaage on the way home and...his was raw and he’s...having stomach problems."
    a "And that’s...actually why I was about to leave."
    m "You’re not going to stay here and take care of him?"
    a "I...need to go buy medicine!"
    m "I should have some in my bag if-"
    a "He only likes medicine from brand new bottles!"
    m "…"

    scene norikofirstvisit38
    with dissolve

    m "What?"
    a "Y-Yeah..."
    a "So...how about the two of us go for a walk and then just...come right back."
    m "But my legs are so tired from-"

    scene norikofirstvisit39
    with dissolve

    a "I’ll buy you something watermelon flavored~"
    m "My legs suddenly feel a lot better."
    a "Great! Then...let’s get going, shall we?"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene norikofirstvisit40
    with dissolve2

    m "…"
    a "…"
    a "Maya? What’s up?"
    a "We’ve gotta get a move on before-"
    m "Did you get new shoes?"
    a "Um...y-yeah..."
    a "Sensei just got them for me...but they’re a little too big."
    a "So we have to...take them back..."
    m "…"
    a "…"

    scene norikofirstvisit41
    with fade

    m "…"
    a "…"
    m "…"
    a "…"
    a "Maya?"

    scene norikofirstvisit42
    with dissolve2

    m "They’re nice."
    a "Th-thanks..."
    a "But I won’t be keeping them, so..."

    scene norikofirstvisit43
    with dissolve

    m "Yeah."
    m "I wouldn't expect you to."
    a "..."
    m "Let’s go."
    m "I’m hungry."
    a "…"
    a "Okay..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ norikoinvite1 = True
    jump norikoinvite2
...
```