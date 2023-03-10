# Rising of the Tide (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Makoto love greater than or equal to 10

* Event [Walk in the Park](./day38.md) (Main) is completed)



## Next events

* [Makoto: Frogger](./makotonew1.md)

## Event properties

* Id: pornshop10
* Group: Makoto
* Triggered by label: pornshop
* Triggered by branch label: pornshop
* Triggered by path: pornshop->pornshop10

## Official wiki page

[Rising of the Tide](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=pornshop10&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label pornshop10:
    scene pornshop10
    with dissolve2
    play music "citylife.mp3"

    mak "Oh dear lord, it never ends."
    s "Oh, come on. Since when is it a crime to spend time with my favorite student?"
    mak "‘Spending time’ together isn’t exactly the issue..."

    "Once again, I find myself at the porn shop with Makoto. And once again, she is not happy to see me."
    "But I guess not many people {i}would{/i} be happy to see their teacher at a porn shop."
    "Unless you're surveying my class."
    "If that's the case, probably half of them would."
    "But obviously, Makoto is not one of them."

    s "Hey..."
    mak "What? Why are you saying {i}hey{/i} like that?"
    s "Is there anything I can do to help increase business here?"
    s "I've been coming here for a little while now and I've yet to actually see any other customers."
    s "And I can't imagine the lack of men has been doing any favors for your family financially."

    if bonus == True:
        jump makotoporn10x
    else:
        mak "Why, yes. There are many things you can do to help."
        mak "Grab a chair and let's talk business."

        scene black
        with dissolve

        "Makoto breaks down the numbers for me and it appears that the lack of males really did make a dramatic impact on her family's store."
        "Together, she and I come up with a new business plan to attract more female customers that we are going to pitch to her mother after purchasing fancy suits."
        "Everyone knows that sales pitches go better when there are suits involved."

        s "I want mine to be purple."
        mak "You can't wear a purple suit. It is bad luck."
        s "I am sorry. Forgive me."

        "I did not know this."

        $ renpy.end_replay()
        $ pornshop10 = True
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

label pornshop15:
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
...
```