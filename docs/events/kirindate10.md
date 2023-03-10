# Politics! Pleasure! Ponies! (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kirin love greater than or equal to 10

* Event [Long and Hard](./kirindate5.md) (Kirin) is completed)



## Next events

None

## Event properties

* Id: kirindate10
* Group: Kirin
* Triggered by label: kirinafternoonhang
* Triggered by branch label: callafternoon
* Triggered by path: callafternoon->callkirinafternoon->kirinafternoonhang->kirindate10

## Official wiki page

[Politics! Pleasure! Ponies!](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindate10&go=Go) for more details.

## Event code

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirindate10:
    play sound "phonebeep.wav"

    "I tap on Kirin’s name in my phone and wait for her to answer."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene kirinmakeout1
    with dissolve
    play music "behindabathroom.mp3"

    "I wind up meeting Kirin at the Kanda apartment on account of all of the other...well, Kandas being out of the place."
    "Papa and Mama Kanda (Who I have yet to ever meet and hope I never will) are off at work while Karin is out doing soccer stuff with her friends or something along those lines."
    "Kirin wasn’t willing to provide many details over the phone."
    "It was just a lot of “I’m all alone. Come now,” mumbo-jumbo that, honestly, I’m more than okay with."
    "Good things happen when people get to be alone together."
    "I wonder what sort of good things will happen today?"

    ki "Hey, hey. Guess what?"
    s "What?"
    ki "We’re all alone~"
    s "I was actually just having a short inner-monologue about that."
    ki "Oh yeah? Say anything good to yourself? "
    ki "Anything fun?"
    s "Just that good things normally happen when two people are alone together."
    ki "Oooooh. I wonder what sort of good things will happen today?"
    s "That is literally how I ended the monologue."

    scene kirinmakeout2
    with dissolve

    ki "I know how your mind works. Mine is the same way."
    s "Sorry to break your heart but I still don’t think we’re connected that deeply."

    if bonus == True:
        ki "I know an easy way to change that~"
        s "You say that now, but I have a feeling you’re just going to back out again before anything happens."

        scene kirinmakeout3
        with dissolve

        ki "You really think that?"

        if kirinbeachhj == True:
            ki "I’ve literally let you cum on me before. Did that not earn me any points at all?"
            s "It earned you a few."
            ki "Well can I redeem them for a chance to get you to think I’m being serious right now?"
            s "I think you still need to earn a few more points for that type of reward."
            ki "I better start {i}grinding{/i} some then, huh?"
            s "I’m enticed by the way you said ‘grinding’ right there."

        else:
            s "Yeah. I’ve said it before and I’ll say it again."
            s "I have a hard time reading you."

            scene kirinmakeout1
            with dissolve

            ki "Well that’s a good thing, isn’t it? It makes me more exciting."
            s "It definitely makes you something."

    scene kirinmakeout1
    with dissolve

    ki "Hey, can I ask you a question?"
    s "Fine, yeah. Go ahead. It’s not like we’re doing anything el-"

    if bonus == True:
        jump kirindryx
    else:
        ki "If I ever catch a disease where my hair starts to turn into pasta, will you help me boil it so I can still do my twintails and stuff?"
        s "What?"
        ki "Yeah. Because pasta isn't that malleable when it's uncooked. And I'd feel weird about cooking a part of myself."
        ki "Also, how many ducks do you think there are?"
        s "Uhhhhhhhhhhhhhhhhhhhhhhhh..."
        ki "Have you ever worn a parachute before?"

        scene black
        with dissolve

        "I think Kirin may be having a psychotic episode, so I call an ambulance and wait with her until she is normal again."
        "She is very thankful and tries to hug me, but Karin shows up and the hug gets cancelled."
        "Maybe one day we will complete it."

        $ renpy.end_replay()
        $ kirin_love += 1
        $ kirindate10 = True
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "………"
        "……"
        "…"

        jump saturdaynight

label kirinhjrep:
    play sound "phonebeep.wav"

    "I tap on Kirin's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"
    play music "acoustic.mp3" fadein 10.0

    ki "Hihi~ Good afternoon, Sensei."
    ki "To what do I owe this pleasure?"

    if bonus == True:
        s "Help. I have an erection and don't know what to do about it."
    else:
        s "Help. I need a hug and I don't know what to do about it."

    ki "...Cool!"
    s "Want to hang out?"
    ki "Well, I mean...someone's gotta do something about it, don't they?"
    ki "I suppose I could free up some time for you in my {i}super busy{/i} schedule since you decided to ask {i}me{/i} for help."
    s "Thanks Kirin. You're a real life-saver."
    ki "Next time, you might wanna just text me, though."
    ki "What if I was with my family and had you on speakerphone?"

    if bonus == True:
        s "I highly recommend never putting me on speakerphone. Erections can strike at any minute."
        ki "Why do you need to verbally announce your erections? That's weird."
        ki "Just come over and I'll jerk you off or something."
    else:
        s "It is just a hug. We have nothing to hide."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump kirinhjrepx
    else:
        $ kirin_lust += 1
        stop music fadeout 5.0

        "{i}Kirin's lust has increased to [kirin_lust]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label kirinlust5:
...
```

## Code that triggers this event

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirinafternoonhang:
    if kirin_love >= 0 and kirindate1 == False:
        jump kirindate1
    if kirin_love >= 10 and kirindate5 == True and kirindate10 == False:
        jump kirindate10
...
```