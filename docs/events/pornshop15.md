# Fishing For Love
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=pornshop15&go=Go)



## Event preconditions
✅Makoto love greater than or equal to 15

✅Event "[Makoto: Egg Tooth](./makotonew3.md)" is completed (event=makotonew3)



## Next events
* [Makoto: Aftermath](./pornshop20.md)

## Event properties
* ID: pornshop15
* Group: Makoto
* Triggered by label: pornshop
* Triggered by branch label: pornshop

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label pornshop15:
    scene pornshophhg
    with dissolve
    play music "citylife.mp3"

    "I show up at the porn shop to find it in...slightly different condition than normal."
    "Previously, all of the posters covering the wall had seemed relatively low-resolution- like they were printed out on paper and just taped up or something."
    "But it looks like a whole plethora of new posters have been hung now. And they’re all advertising the same thing."
    "The fuck is {i}Hero's Harem Guild?{/i}"
    "…"
    "I take a look around to see if I can spot Makoto, but I-"

    mak "This...fucking...stupid...game..."
    s "…"
    s "Makoto? Where are you?"
    mak "Over here, bashing my head against a wall."
    mak "What do you want? "

    if bonus == True:
        s "Uhh...porn? Did you forget what you sell here?"
        mak "Go home and watch porn on your computer."
    else:
        s "I just wanted to spend time with my class representative and go over a varitey of new teaching techniques I am interested in attempting."
        mak "Go home and practice them with your accountant."

    scene makotohhg1
    with dissolve

    s "Nah, I think I’ll just watch whatever you’re-"
    s "…"
    s "Are you...fishing?"
    mak "What does it look like I’m doing, genius? Of course I’m fishing."
    s "Why?"
    mak "Some weird guy showed up an hour ago and just started hanging up all these weird posters for some video game he’s making."

    if bonus == True:
        jump makotohhgx
    else:
        s "Wow, neat! It looks really fun."
        s "Can you teach me how to play?"
        mak "Sure. Take a seat."

        scene black
        with dissolve

        "Makoto and I spend the next hour or so playing a fun fishing simulation game."
        "Also, I meet her mom. She seems like a completely normal woman and gives me her phone number so I can keep her updated on Makoto's progress in college."

        $ renpy.end_replay()
        $ makoto_love += 1
        $ pornshop15 = True
        $ makinumber = True
        stop music fadeout 8.0

        "{i}Congratulations! You now have Maki’s phone number.{/i}"
        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotolust5:
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
...
```