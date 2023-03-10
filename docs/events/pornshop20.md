# Aftermath (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Makoto love greater than or equal to 20

* Event [Kadrillionbilliontrillion](./halloween14.md) (Main) is completed)

* Event [Fishing For Love](./pornshop15.md) (Makoto) is completed)



## Next events

* [Makoto: Residual Sadness](./makotodorm20.md)

## Event properties

* Id: pornshop20
* Group: Makoto
* Triggered by label: pornshop
* Triggered by branch label: pornshop
* Triggered by path: pornshop->pornshop20

## Official wiki page

[Aftermath](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=pornshop20&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label pornshop20:
    scene makotomakidildo1
    with dissolve
    play music "citylife.mp3"

    "I arrive at the porn shop to find a less-than-happy Makoto standing still at the counter and already hating the fact that I am, yet again, visiting her at work."

    if bonus == True:
        "You’d think that after taking her virginity she’d be a lot more accepting of my degenerate side, but I guess she’s still just normal, old Makoto after all."

    mak "Whaaaaaaaaaaaaat? Why are you here?"

    if bonus == True:
        mak "Let me sell porn in peace."
        s "I can’t get enough of you, Makoto. Staying away is impossible."

        scene makotomakidildo2
        with dissolve

        mak "As if I’d believe that from the same guy who routinely calls girls into his office to do God-knows-what to them."
        s "It’s called counseling. And that sour attitude of yours makes me think it might be time for you to receive some. "
        mak "Right, right. I’m sure that would be a great conversation with Mother."
        mak "Hey, Mom? I need counseling now."
        mak "{i}Why, dear? What’s wrong?{/i}"
        mak "I’m not excited enough about selling anal gangbang videos to my teacher. I must be rehabilitated."
        s "To be fair, your mother always seems very excited about the concept of anal gangbang videos."
    else:
        s "I was lonely. I just needed to be held."
        mak "I do not want to hold you."
        s "Your mom would hold me if I asked her to."

    scene makotomakidildo3
    with dissolve

    mak "My mom is a fucking creep! She doesn’t count!"
    maki "I can hear you, Makoto!"

    scene makotomakidildo4
    with dissolve

    mak "Shut up, Mom! "
    maki "I love you, sweetie!"
    s "You two are so cute together."

    scene makotomakidildo5
    with dissolve

    mak "You are the bane of my existence."
    s "Wow. And to think you’d say something like that after all of the precious memories we made during the Halloween party."

    scene makotomakidildo6
    with dissolve

    mak "Those memories were made with fun-Makoto. Business-Makoto is currently in charge, thank you very much."

    if bonus == True:
        mak "And also, please don’t speak any further about the memories we made while my mother is right around the corner re-stocking vibrators."
        s "I’m honestly surprised you sell enough of those to warrant re-stocking them."

        scene makotomakidildo7
        with dissolve

        mak "Well, you know. It’s getting close to Christmas and the historic lack of men means a lot of women buying presents for one another."
        s "Right. And what better present than the gift of an orgasm?"
        mak "Right..."

        scene makotomakidildo8
        with dissolve

        mak "Wait! Not right! There are a lot of better presents out there!"
        mak "Like...golf clubs! Or a trip to the zoo!"
        s "Or this."

        scene makotomakidildo9
        with dissolve

        "I reach behind me and manage to grab hold of a display-dildo sitting on top of a shelf, placing it directly into Makoto’s hand."
        "She angrily looks over it, likely pondering the kindest way to remove me from the store without her mother getting mad at her for turning away a real-live customer."
    else:
        s "If that is what you think is best, I will cease conversation and simply purchase this item right here."

        scene black
        with dissolve

    s "One Christmas present, please."

    if bonus == True:
        scene makotomakidildo10
        with dissolve

    mak "Would you like it gift-wrapped, sir?"

    if bonus == True:
        jump makotomakidildox
    else:
        s "Yes, please. It is for my accountant."
        mak "Why are you purchasing a roll of duct tape for you- oh. Right."
        s "I am in trouble, Makoto."
        mak "..."
        s "Please help me."

        $ renpy.end_replay()
        $ pornshop20 = True
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

label pornshop25:
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
...
```