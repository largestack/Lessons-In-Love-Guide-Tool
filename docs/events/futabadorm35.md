# Overload
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabadorm35&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 35

✅Event "[Futaba: No, You](./library35.md)" is completed (event=library35)



## Next events
None

## Event properties
* ID: futabadorm35
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label futabadorm35:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Futaba’s door and wait to see if there’s a response."
    "She was still a little off the last time I checked the library, so I’m hoping that, at the very least, she’s awake tonight."

    f "Sensei? Is that you?"

    "Oh good. It appears that she is."

    s "Yup. Did my strong, manly knocking noise give it away?"
    f "It’s more the fact that just no one else ever knocks in general..."
    s "Does that mean I can come in?"

    if bonus == True:
        f "Am I allowed to put a bra on first?"
    else:
        f "Nope."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Sorry, Futaba. It was kind of hard to hear you out there."
    s "You said “Come in, it’s open,” right?"

    scene futabafingering1
    with dissolve
    play music "asobeatsex2.mp3"

    f "Well, I guess that answers that question."
    s "Oh, sorry. Did you need more time? I just couldn't seem to hear you from the hall."
    f "Right..."
    s "How are you feeling?"

    scene futabafingering2
    with dissolve

    f "Wow, you're just getting right down to it, aren't you?"
    s "At least I didn’t wake you up this time."

    scene futabafingering3
    with dissolve

    f "No. I guess you didn’t..."
    f "I’m still feeling a little out of it, but I’ll probably start getting better soon."
    f "Rin’s been really helpful. I feel like if I stay...sick any longer that she’ll wind up going crazy and quitting the cafe to be my full-time caretaker."
    s "Is whatever you have really that bad? I was under the impression you were just overworked."
    f "That’s the easiest way of putting it. Or at least the way that will make me feel less weird."
    f "So I’d be really thankful...if you could just leave it at that for now."
    s "Sure. It’s not really my business prying into your personal life anyway."

    scene futabafingering1
    with dissolve

    f "Then you might want to stop barging into my room without my permission as well..."
    s "Oh come on. You were going to let me in anyway. We both know that."

    scene futabafingering4
    with dissolve

    f "Obviously. But that doesn’t mean I’m not still embarrassed."

    if bonus == True:
        s "I’m surprised you have any embarrassment left in you after all of the things we’ve done."
        jump futabafingeringx
    else:
        s "Jesus isn't there anything else you know how to talk about omfg"
        f "Sorry, Sensei."
        s "I never should have come in here."
        f "I am sorry. Please do not go."
        s "I am going."
        s "Goodbye."

        scene black
        with dissolve
        play sound "dooropen.mp3"

        f "Sensei, wait."
        s "I can not believe this."

        "I walk home angrily and keep grunting to myself because of all of the anger. Ugh."

        s "Ugh."

        "I am so angry."

        $ renpy.end_replay()
        $ futabadorm35 = True
        $ futaba_love += 1
        stop music fadeout 5.0

        "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label rindorm40:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label futabadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if futaba_love >= 5 and futabafall == False and futabafirstvisit == False:
                "Please play Futaba's level 5 Library event to unlock the first dorm event!"
                jump doorknock
            if futaba_love >= 5 and futabafall == True and futabafirstvisit == False:
                jump futabafirstvisit
            if futaba_love >= 10 and futabadorm10 == False:
                jump futabadorm10
            if futaba_love >= 15 and library15 == True and futabanew1 == False:
                jump futabanew1
            if futaba_love >= 15 and futabanew2 == True and futabanew3 == False:
                jump futabanew3
            if futaba_love >= 15 and futabanew3 == True and futabadorm15 == False:
                jump futabadorm15
            if futaba_love >= 25 and day > 5 and bookdate == True and futabadorm25 == False:
                jump futabadorm25
            if futaba_love >= 30 and library30 == True and day != 3 and futabadorm30 == False:
                jump futabadorm30
            if futaba_love >= 35 and library35 == True and futabadorm35 == False:
                jump futabadorm35
...
```