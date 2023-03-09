# Micropenis
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumifirsthall&go=Go)



## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: yumifirsthall
* Group: Yumi
* Triggered by label: dormmonday
* Triggered by branch label: dorms

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label yumifirsthall:
    scene yumihall1
    with dissolve

    s "Hey Yumi. What are you up to?"
    y "Oh, fuck no. Don't just walk up to me in the hall of the {i}girls'{/i} dorm and act like you fuckin' own the place."
    s "All I did was say hi."
    y "Which is a billion times more than you're allowed to say, douchenozzle."
    y "There is absolutely no fucking way you are allowed over here. I don't believe it for even a second."
    y "Who's on the hit list today? Class prez? Fat-aba?"
    s "I was actually kind of hoping the two of us could hang out."

    scene yumihall2
    with dissolve

    y "And I was actually kind of hoping I'd be able to stand in the hall of the building I fucking {i}live{/i} in without worrying about some predator trying to sneak into my room."
    y "Get the fuck out of here. Now."
    s "I'm starting to think you don't want to be around me tonight."

    scene yumihall3
    with dissolve

    y "Oh my fucking God. It's like talking to a brick wall- just the brick wall has a micropenis that gets hard every time it sees a pair of tits."
    s "Your analogy game needs some work, Yumi."

    scene yumihall4
    with dissolve

    y "My {i}what?{/i} This that new teaching strategy I've been hearin' about?"
    y "You coming to our rooms to lecture us now since you're too busy sniffing our fucking gym clothes in the locker room during school hours."
    s "To my dismay and your fortune, I can assure you here and now that I don't have access to that room."

    scene yumihall5
    with dissolve

    y "Finally, some good fucking news."
    s "So, what do you want to do? Go for a walk? Give me a tour of your dorm room?"

    scene yumihall6
    with dissolve

    y "You mean right now? I don't know. Blowin' my brains out sounds pretty fuckin' appealing."
    s "We're not hanging out tonight, are we?"

    scene yumihall7
    with dissolve

    y "Of fucking course not! Now get the hell out of here and never come back!"

    play sound "dooropen.mp3"
    scene yumihall0
    with dissolve

    "Yumi disappears into her dorm room, which I don't really blame her for since I definitely {i}shouldn't{/i} be here."
    "But hey, if no one is going to stop me, I'm going to keep on coming."
    "It's not like there's much else to do at night anyway."
    "For now, though, I guess I'll head back home."
    "Yumi can only avoid me for so long..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ yumi_love += 1
    $ yumifirsthall = True

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumihall:
    if chapthreeactive == True:
        scene yumisummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene yumihall2
        with dissolve
    else:
        scene yumihallwinter
        with dissolve

    s "Hey Yumi."
    y "Oh god damnit, not this shit again."

    "I try talking to Yumi for as long as she’ll allow me to
    before she retreats back to the safety of her room yet again."
    "I swear I’ll get this girl to like me eventually..."

    scene black
    with dissolve

    $ yumi_love += 1

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayafirsthall:
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
...
```