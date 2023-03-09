# Quid Pro Quo
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotolust5&go=Go)



## Event preconditions
✅Makoto lust greater than or equal to 5

✅Event "[Makoto: Egg Tooth](./makotonew3.md)" is completed (event=makotonew3)



## Next events
* [Makoto: Declaration of War](./makotoinvite1.md)
* [Makoto: Studious Teen Virgin](./makotoinvite2.md)

## Event properties
* ID: makotolust5
* Group: Makoto
* Triggered by label: pornshop
* Triggered by branch label: pornshop

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label makotolust5:
    scene black
    with dissolve
    "………"
    "……"
    "…"
    scene makotofirstlust1
    with dissolve
    play music "citylife.mp3"

    mak "Why are we in the back room already? How did I get here?"
    mak "There wasn’t even an opening to this event."

    if bonus == True:
        jump makotolust5x
    else:
        s "There won't be an ending either."
        mak "What? Why not?"
        s "Patreon doesn't want this scene in the game."
        mak "Oh. Well, I guess that takes a load off my back since I won't feel pressured to hug you anymore."
        s "I never want you to feel pressured about anything, Makoto. I am nice."
        mak "You're okay."
        s "Wow."

        scene black
        with dissolve

        "If that's how Makoto really feels about me, I don't even want to be here anymore."

        s "Goodbye, Makoto. Enjoy your weirdly lit backroom thing."
        mak "Bye, Sensei. Thank you for being a responsible man who does not want to distract me while I am at work."
        s "Tell your mother I said hello."
        mak "But she hasn't even shown up in the game yet."
        s "I know, but I saw her character profile and she looks cute."
        mak "Okay. I will tell her."

        $ renpy.end_replay()
        $ makoto_lust += 1
        $ makotolust5 = True
        stop music fadeout 5.0

        "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotoinvite1:
...
```

## Code that triggers this event
File: \game\MakotoEvents.rpy
Code:
```python
...
label pornshop:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump satnightmenu
    if makoto_love >= 0 and firsttimepornshop == False:
        jump firsttimepornshop
    if makoto_love >= 5 and pornshop5 == False:
        jump pornshop5
    if makoto_love >= 10 and day38 == True and pornshop10 == False:
        jump pornshop10
    if makoto_love >= 15 and makotonew1 == True and makotodorm5 == True and makotonew2 == False:
        jump makotonew2
    if makoto_love >= 20 and makotonew2 == True and day > 4 and day < 7 and makotonew3 == False:
        jump makotonew3
    if makoto_love >= 15 and makotonew3 == True and pornshop15 == False:
        jump pornshop15
    if makoto_lust >= 5 and makotonew3 == True and makotolust5 == False:
        jump makotolust5
...
```