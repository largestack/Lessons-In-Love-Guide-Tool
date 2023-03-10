# Semblance of a Soul (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 230

* Makoto lust greater than or equal to 10

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

None

## Event properties

* Id: makotolust10
* Group: Makoto
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->makotolust10

## Official wiki page

[Semblance of a Soul](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotolust10&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label makotolust10:
    scene makotolustten1
    with dissolve2
    play music "asobeatsex3.mp3"

    mak "Hah..."
    mak "Finally."
    mak "I swear, Sensei, it’s like you don’t even work here sometimes."
    s "Sometimes? I feel like I’ve made it very apparent that I literally never work here."

    scene makotolustten2
    with dissolve

    mak "Correct. Though, I guess it might be hard to discern the sarcasm in my voice when I’m this exhausted."

    "Makoto and I are in my office after a long day of[school] in which we were tasked to do some...I don’t even know."
    "A thing, I guess."
    "One of the other teachers came into my room at the end of the day and started rattling off a bunch of stuff I didn’t understand, so Makoto was kind enough to step in and offer her assistance."
    "Originally, the gameplan was for her to stop by after class ended for the day and just do it all for me, but..."
    "Well, she apparently decided that we needed to clean my office afterward as well since I haven’t bothered tidying up in...ever."

    if bonus == True:
        jump makotolusttenx
    else:
        mak "I hope you are ready to clean."
        s "Noooooooooooooooooooooooooooooooo! You can't make me."
        mak "Sensei. Don't you dare throw a temper tantrum!"
        s "I don't wanna clean! I am the protagonist!"

        scene black
        with dissolve2

        "Makoto manages to make me clean because that's what the script says I'm supposed to do."
        "I hate it and the event ends way too quickly without anything fun happening."

        $ renpy.end_replay()
        $ makotolust10 = True
        $ makoto_lust += 1
        stop music fadeout 5.0

        "{i}Makoto’s lust has increased to [makoto_lust] because she really likes cleaning.{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotowinterbeach1:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
    if totaldays >= 85 and streets10 == True and day85 == False:
        jump day85
    if totaldays >= 86 and futaba_lust >= 5 and day == 5 and day86 == False:
        jump day86
    if totaldays >= 89 and day65 == True and day89 == False:
        jump day89
    if totaldays >= 91 and day63 == True and day65 == True and day91 == False:
        jump day91
    if totaldays >= 96 and day == 1 and shrine15 == True and ayanenew1 == True and day96 == False:
        jump day96
    if totaldays >= 98 and ami_lust >= 5 and day98 == False:
        jump day98
    if totaldays >= 103 and day102 == True and day103 == False:
        jump day103
    if totaldays >= 110 and day103 == True and day110 == False:
        jump day110
    if totaldays >= 114 and day103 == True and bar20 == True and day114 == False:
        jump day114
    if totaldays >= 120 and day103 == True and day91 == True and day120 == False:
        jump day120
    if totaldays >= 121 and day85 == True and day103 == True and day121 == False:
        jump day121
    if totaldays >= 126 and day103 == True and streets15 == True and chikadorm15 == True and day126 == False:
        jump day126
    if totaldays >= 128 and day103 == True and day126 == True and day == 5 and day128 == False:
        jump day128
    if totaldays >= 138 and day103 == True and day130 == True and day85 == True and day138 == False:
        jump day138
    if totaldays >= 139 and chika_lust >= 5 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False or chikadorm20 == True and mall20 == True and chika_lust >= 10 and day139 == False:
        jump day139
    if totaldays >= 140 and day138 == True and day140 == False:
        jump day140
    if totaldays >= 142 and amidorm15 == True and day140 == True and day142 == False:
        jump day142
    if totaldays >= 144 and day128 == True and day142 == True and day144 == False:
        jump day144
    if totaldays >= 150 and day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False:
        jump day150
    if totaldays >= 153 and day150 == True and day153 == False:
        jump day153
    if totaldays >= 154 and day153 == True and day154 == False:
        jump day154
    if (totaldays >= 200 and day == 5 and beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True
    and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and halloween1 == False):
        jump halloween1
    if totaldays >= 214 and makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day == 1 and day214 == False:
        jump day214
    if totaldays >= 215 and day214 == True and day == 2 and day215 == False:
        jump day215
    if totaldays >= 216 and day215 == True and day == 3 and day216 == False:
        jump day216
    if totaldays >= 217 and day216 == True and day == 4 and day217 == False:
        jump day217
    if totaldays >= 218 and day217 == True and day == 5 and day218 == False:
        jump day218
    if totaldays >= 230 and makoto_lust >= 10 and christmas7 == True and makotolust10 == False:
        jump makotolust10
...
```