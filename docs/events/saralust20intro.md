# Engulfed (Sara)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Tokimeki Labyrinth](./christmastwo6.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: saralust20intro
* Group: Sara
* Triggered by label: christmastwo6
* Chain sources: christmastwo6
* Chain sources path: christmastwo6

## Official wiki page

[Engulfed](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=saralust20intro&go=Go) for more details.

## Event code

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label saralust20intro:
    if sara_lust >= 20 and haruka_lust >= 20 and bonus == True:
        jump saralust20x
    elif sara_lust >= 20 and haruka_lust >= 20 and bonus == False:
        "As requested of me last night, I make my way over to Sara’s unnamed bar to help her decorate the place."
        "We have a very good time up until I get tangled up in tinsel and the fire department has to come and get me out."
        "I can be such a klutz sometimes."

        $ renpy.end_replay()
        $ haruka_lust += 1
        $ sara_lust += 3
        $ saralust20 = True
        stop music fadeout 5.0

        "{i}Sara’s lust has increased to [sara_lust]!{/i}"
        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo7
    else:
        "As requested of me last night, I make my way over to Sara’s unnamed bar to help her decorate the place."
        "And while I initially thought that might be code language for something a bit more entertaining, I quickly discovered that was not the case at all."
        "As it turns out, Sara's [[allegedly] hosting a pretty decently sized Christmas party tonight and needs all of the help she can get setting the place up."
        "With Haruka's assistance in addition to what little I had to offer, we're able to get everything done in a little over an hour and I'm free to get on with the rest of my day."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ saralust20skip = True
        stop music fadeout 5.0

        jump christmastwo7
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
with fade

    "{i}Several minutes later...{/i}"

    play sound "dooropen.mp3"
    scene christmashome37
    with dissolve

    f "Hah...sorry about that. The conversation lasted a little longer than expected."

    scene christmashome38
    with dissolve

    f "So, what time tomorrow were we..."
    r "Mm~ Mmn...Otoha..."
    o "Chu...mnf...mm~"
    f "..."

    scene christmashome39
    with dissolve

    f "{i}*Ahem*{/i}"
    f "Oh no. I seem to have forgotten to call my aunt as well. Please excuse me for...a longer amount of time."

    play sound "dooropen.mp3"
    scene christmashome36
    with dissolve

    r "Ahm...mmm...mm!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene christmashome40
    with dissolve2

    a "WAAAAAAAAH! NIKI! YOU’RE THE ONLY PERSON WHO UNDERSTANDS ME!"
    sa "I...um..."
    sa "Didn’t really like the song, but...I’m happy you...found someone you like so much..."

    scene christmashome41
    with dissolve

    m "So, now that you’ve been forced to sit through whatever that was, are you still calling it a night?"
    ay "Are you trying to get him to stay up later because you’ll {i}miss{/i} him, Maya?"
    m "No. I’m just smart enough to know that once he’s out of the picture, everyone else will inevitably want to go to sleep as well. And I am very tired."
    s "Or maybe...you’re just actually excited for the Christmas party tomorrow and don’t want to wait any longer."

    scene christmashome42
    with dissolve

    m "Yup. You got me. Goodnight, everyone. I am so excited to be packed into a small, hot room with nineteen other girls tomorrow night."

    scene black
    with dissolve2

    "Not seeing much reason to stay awake, I also decide to head to bed."

    if bonus == True:
        "This time, however, I decide to lock my door so Ayane can’t mount me in the middle of the night."
        "I’m not really sure how tomorrow’s party will compare to last year’s (If...you can even call it {i}last{/i} year? How does that work exactly?) but, if there is anything I {i}do{/i} know...it’s that it’s going to be lively."
        "The class size has nearly doubled and, unless we have some new venue planned out that I haven’t heard of, I think it’s pretty safe to assume that chaos will ensue and..."

        s "...Fuck."

        "I forgot to buy Miku a Christmas present..."

        s "..."

        "Oh well."
        "I’ll just buy one on the way back from Sara’s tomorrow."
    else:
        "I sure hope Santa Claus brings me lots of presents tomorrow."

    $ renpy.end_replay()
    $ christmastwo6 = True
    $ ayane_love += 1
    $ ami_love += 1
    $ sana_love += 1
    $ maya_love += 1
    stop music fadeout 7.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 6
    hide friday onlayer date
    show saturday onlayer date

    jump saralust20intro
...
```