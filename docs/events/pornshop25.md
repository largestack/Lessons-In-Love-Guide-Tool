# Service Charge (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Makoto love greater than or equal to 20

* Event [Residual Sadness](./makotodorm20.md) (Makoto) is completed)



## Next events

* [Makoto: Bluejay](./makotodorm25.md)

## Event properties

* Id: pornshop25
* Group: Makoto
* Triggered by label: pornshop
* Triggered by branch label: pornshop
* Triggered by path: pornshop->pornshop25

## Official wiki page

[Service Charge](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=pornshop25&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label pornshop25:
    scene makotoona1
    with dissolve
    play music "citylife.mp3"

    "I decide to spend the night hanging out at the porn shop with Makoto."
    "{i}She{/i} decides not to play along or have fun with me because business-Makoto is a fucking loser."

    mak "For the last time, can you put that thing down?"
    mak "If you’re not going to buy it, you shouldn’t be messing around with it."
    s "I’ve tried buying it four times now and each time you’ve turned me away."

    if bonus == True:
        jump makotoonax
    else:
        mak "Yes, because that is not an item {i}we{/i} sell. It is something from the store next door to us."
        s "You mean to tell me that this limited edition Turboman action figure actually comes from the toy shop next door and not this business?"
        mak "For the tenth time, yes. Go bring it back."
        s "But my son needs it in time for Christmas."
        mak "You don't even have a son."
        s "And you never will either with that attitude."
        mak "That's it. I'm calling the cops."

        scene black
        with dissolve

        s "Turboman, blasting off!"

        "I make wooshing noises and wiggle the action figure around in the air on my way out of the store."
        "I don't know if Turboman can actually fly or not, but I'm going to pretend he can if he can't because I think that makes him sound more turbo."

        $ renpy.end_replay()
        $ pornshop25 = True
        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotoinvitefinger:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump makotoinvitefingerx
    else:
        $ makoto_lust += 3
        stop music fadeout 5.0

        "{i}Makoto's lust has increased to [makoto_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotolust10:
...
```

## Code that triggers this event

File: (install folder)\game\MakotoEvents.rpy

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
    if makoto_love >= 20 and halloween14 == True and pornshop15 == True and pornshop20 == False:
        jump pornshop20
    if makoto_love >= 20 and makotodorm20 == True and pornshop25 == False:
        jump pornshop25
...
```