# Thank You For Your Business (Maki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maki love greater than or equal to 15

* Event [Three Afloat On One Raft](./makiday351.md) (Maki) is completed)

* Event [Bad Kitty](./harukalust10.md) (Haruka) is completed)

* makibj equal to True (unknown variable)



## Next events

None

## Event properties

* Id: makidate15
* Group: Maki
* Triggered by label: pornshopmaki
* Triggered by branch label: pornshopmaki
* Triggered by path: pornshopmaki->makidate15

## Official wiki page

[Thank You For Your Business](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makidate15&go=Go) for more details.

## Event code

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label makidate15:
    scene makihhg1
    with dissolve
    play music "citylife.mp3"

    "I make my way into the porn shop only to be immediately assaulted by a hefty dose of deja vu."

    maki "Why am I doing this to myself? I don’t even like fishing."

    if bonus == True:
        maki "Besides, everyone knows that putting mini games into a porn game is the quickest way to get people to drop it."
        maki "Just let me fuck bitches. I wanna fuck bitches."
    else:
        maki "Besides, everyone knows that putting mini games into a porn game makes people quit even faster than blatantly censoring 100%% of its adult content."
        maki "Just let me HUG WOMEN. I wanna HUG WOMEN."

    s "Ahem."

    scene makihhg2
    with dissolve

    maki "…"
    s "…"
    maki "What?"
    s "Seems to me that you’re having a little trouble."

    if bonus == True:
        maki "I’m sorry, sir. We’re closed for the night because I apparently have to catch fish if I ever want to get laid."
    else:
        maki "I’m sorry, sir. We’re closed for the night because I apparently have to catch fish if I ever want to get hugged."

    s "You know, it wasn’t too long ago that I remember having a similar conversation with your daughter."

    if bonus == True:
        maki "Is Makoto making you fish in order to get into her pants? Because I’m pretty sure I taught her better than that."
    else:
        maki "Is Makoto making you fish?"

    s "What? No."

    if bonus == True:
        "Though, she did have to beg for a good amount of time."
        "But it’s not like I can say that to Maki."

    s "I just mean that she was playing this game the first time you and I met."

    scene makihhg3
    with dissolve

    maki "Aww. That makes this some sort of romantic reunion then, doesn’t it?"
    s "I don’t think there’s anything romantic about watching you catch fish in a porn shop."
    maki "And yet here we are."
    s "Why are you even playing it if you’re not having a good time?"

    scene makihhg4
    with dissolve

    if bonus == True:
        maki "Well, technically I’m {i}re{/i}playing it. I played a bit when it first came out, but Makoto had more sex than me so now I need to catch up."
        maki "Besides, she said they added more content and I want to see if I can bang the girl with the cat ears yet."
        s "Well I wish you the best of luck, Maki. "
        maki "Why are you making it sound like you’re about to leave? Come bang the cat girl with me."
    else:
        maki "Because that's what the script says I'm supposed to do."
        s "I see."

    mak "Ahem."

    scene makihhg2
    with dissolve

    maki "Oh, come on. What now?"
    s "It wasn’t me that time. "
    maki "If it wasn’t you then-"

    scene makihhg5
    with dissolve

    mak "…"
    maki "Oh. "
    maki "I thought you went out with Miku."

    scene makihhg6
    with dissolve

    mak "I thought {i}you{/i} were going to be working tonight."
    maki "I {i}am{/i} working. This is my job, sweetie."

    if bonus == True:
        jump makihhgx
    else:
        s "I was? Why?"
        maki "Because that's what the script says you have to do?"
        s "Ugh. Really? I wish they'd tell me these changes ahead of time."
        mak "Just shut up and leave, Sensei."
        s "You're so rude in the censored version."

        scene black
        with dissolve2

        "I go home and write an angry letter to the developer of Lessons in Love."

        $ renpy.end_replay()
        $ makidate15 = True
        $ maki_love += 1
        $ maki_lust += 3
        stop music fadeout 5.0

        "{i}Maki’s affection has increased to [maki_love]!{/i}"
        "{i}Maki’s lust has increased to [maki_lust]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makiinvite1:
...
```

## Code that triggers this event

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label pornshopmaki:
    if makiblock == True:
        "I don't really think I should visit Maki right now..."
        jump satnightmenu
    if maki_love >= 5 and makotodorm25 == True and makidate1 == True and bar25 == True and makidate5 == False:
        jump makidate5
    if maki_love >= 10 and christmas7 == True and makidate10 == False:
        jump makidate10
    if maki_love >= 15 and makiday351 == True and harukalust10 == True and makibj == True and makidate15 == False:
        jump makidate15
...
```