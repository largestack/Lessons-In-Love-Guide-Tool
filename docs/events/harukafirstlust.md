# The Need to be Hurt
Haruka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukafirstlust&go=Go)



## Event preconditions
✅Haruka love greater than or equal to 5

❌Haruka lust greater than or equal to 5

✅Event "[Haruka: Drunk Again](./harukadate1.md)" is completed (event=harukadate1)



## Next events
None

## Event properties
* ID: harukafirstlust
* Group: Haruka
* Triggered by label: harukacafe
* Triggered by branch label: saturdaymorning

## Event code
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukafirstlust:
    scene cafe_day
    with dissolve
    play music "cafe.mp3"

    "I show up at the cafe to check in on Haruka and see what she’s up to."
    "Given that this is her business, I’d imagine the answer to that would be “working,” but the cafe is unusually dead this morning for some reason."
    "In fact, I don’t even see Rin behind the counter, which is borderline absurd to me given that she’s here virtually every weekend ever."
    "I wonder if something is going on?"

    h "Hey! Come hang out with me, loser."
    s "…"

    scene harukafirstlust1
    with dissolve

    s "Loser? Really?"
    s "How old are you?"
    h "Old enough!"

    scene harukafirstlust2
    with dissolve

    h "What are you up to today?"
    s "Uhh, just normal cafe stuff I guess. Where is everybody?"
    h "Beats me. Probably sleeping in for the holiday or something."
    s "Holiday?"
    h "Yeah. It’s Kumon-mi Day. "
    s "What the fuck is Kumon-mi Day?"

    scene harukafirstlust3
    with dissolve

    h "Beats me. I can tell you it’s definitely not just some convenient plot device inserted into this scene to justify creating an opportunity where the two of us are alone, though."
    s "Of course it’s not. That would just be lazy writing."

    scene harukafirstlust1
    with dissolve

    h "Heheh~ You got that right."
    s "If it’s a holiday, why even bother opening, though? You don’t even have Rin working today."

    scene harukafirstlust4
    with dissolve

    h "Really, dude? We get to hang out alone in this nice, air-conditioned cafe and you’re going to complain about my part-timer not being here?"
    s "I’m not complaining. I just feel like this completely disrupts the chain of events my life has begun to follow."
    s "I don’t like change."
    h "Yeah...I guess I can agree with that."

    scene harukafirstlust2
    with dissolve

    h "Rin’s fine, though. I sent her home early."
    s "It must suck coming all the way here just to get sent home early."
    h "Naaaah. She seemed tired anyway so I’m sure she’s fine with it."

    scene harukafirstlust1
    with dissolve

    h "Plus, if a million people just decide to show up out of nowhere, I could always force you to help me instead."
    s "Yeah, I’m not sure how that would work out. I don’t even remember the names of your sizes."

    scene harukafirstlust2
    with dissolve

    h "Ehh, I’m sure you won’t have to worry about that. I honestly might just close up anyway."
    h "At least until the afternoon or night or something when things start to pick up again. "
    h "A day off might not hurt every once in a while and I guess a holiday is as good an excuse as any. "

    scene harukafirstlust1
    with dissolve

    h "Plus, then I’d get to make you hang out with me. "
    s "You are aware you can’t {i}make{/i} me do anything, right?"

    scene harukafirstlust5
    with dissolve

    h "Oh I can {i}make{/i} you do plenty of things, Sensei~"
    s "..."
    s "Are you seducing me right now?"
    h "What? Seducing you? At my own workplace? How dare you accuse me of something so outrageous."
    s "So you’re not, then?"

    scene harukafirstlust6
    with dissolve

    h "Well..."

    "Haruka pauses and directs her attention to the barren streets outside of the cafe."
    "Nothing or no one can be seen passing by. No cars, no pedestrians, not even an occasional leaf or plastic cup-lid or anything."

    if bonus == True:
        jump harukabathroomx
    else:
        scene black
        with dissolve

        h "Nah. I'm just fuckin' around."
        s "Hahaha. You're so crazy, Haruka."

        "The two of us proceed to celebrate Kumon-mi Day by filling our hands with as many coffee beans as we can and then throwing them into the air and trying to run under them."
        "The tradition dates back to the origins of the city and fills my eyes with tears as I attempt to recollect all of my past lives and all of my past celebrations."
        "Then Haruka interrupts me and is all like {i}When do you wanna put our shoes back on?{/i} and I say {i}never{/i} and then leave."
        "Also, we hug."

        $ renpy.end_replay()
        $ haruka_lust += 1
        $ haruka_love += 3
        $ harukafirstlust = True

        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
        "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
        "………"
        "……"
        "…"

        jump saturdayafternoon

label harukacafedogrep:
        scene black
        with dissolve
        play music "cafe.mp3" fadein 3.0

        "I head to the cafe to see what Haruka is up to and find her at a table near the window filing through some paperwork."

        h "Oh, hey! What are you up-"

        if bonus == True:
            s "Let's have sex."
        else:
            s "Let's hug."

        h "...What?"
        h "Right now?"
        h "But it's the middle of breakfast."
        s "I don't care."
        h "Um...Uhh..."

        "Haruka looks over to the counter to find Rin sifting through a few syrup bottles and not paying much attention to the store."

        h "...Okay. But we need to be quick."

        "........."
        "......"
        "..."

        if bonus == True:
            jump harukacafedogrepx
        else:
            $ haruka_lust += 1
            stop music fadeout 4.0

            "{i}Haruka's lust has increased to [haruka_lust]!{/i}"
            "........."
            "......"
            "..."

            jump saturdayafternoon

label harukadate10:
...
```

## Code that triggers this event
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukacafe:
    if haruka_love >= 5 and haruka_lust >= 5 and harukafirstlust == False:
        jump harukafirstlust
...
```