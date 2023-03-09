# Out With the Old
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanelust20&go=Go)


Part of event chain [Room to Grow](./christmastwo3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: ayanelust20
* Group: Ayane
* Triggered by label: christmastwo3

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label ayanelust20:
    scene ayaneofficebang1
    with dissolve2
    play music "asobeatsex4.mp3"

    "Ayane and I retreat to my office because, well, where else would we go during school hours?"

    if bonus == True:
        "Well...apart from the nurse’s office, which we've already made out in once before."
        "But- wait, isn’t the nurse absent on Fridays? We really could have just gone there after all."
        "Assuming that there is going to be sex, of course. For all I know, this really {i}could{/i} just be about giving me a sneak peek of something."
        "But when Ayane and I are alone, the chances are that one of us is probably going to want to get a little closer."
        "And by {i}one{/i} of us, I really mean {i}both{/i} of us."
        "We are very...horny people."
        "Destructively horny, if you will."

        if ayanelust10 == True:
            "But I probably don’t have to remind you of that on account of the entire Kirin situation."

    ay "Are you ready to have your mind blown, Sensei?"

    if bonus == True:
        jump ayanelust20x
    else:
        s "Yes, but please be gentle."

        scene black
        with dissolve2

        "Ayane spends the next ten minutes showing me the mech suit she has been working on, which she will soon reveal to the class before beginning her quest for world domination."
        "Unfortunately, the mech suit falls apart shortly after she gets inside because it was held together tomato paste."
        "This will teach her not to use cooking ingredients on heavy machinery in the future."
        "Ayane cries a lot, which makes me cry too."
        "Eventually, we stop crying and hug each other. Then we leave."

        $ renpy.end_replay()
        $ ayane_lust += 1
        $ ayanelust20 = True
        stop music fadeout 5.0

        "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo4

label ayanenew1:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
scene imaniclassintro25
    with dissolve

    m "I feel as though I may be forced to actually learn something for the first time in a very, very long time. And I worry that my hands may no longer remember how to hold a pencil for any tests assigned to us."
    s "Well, you sure knew how to hold one when you filled a fake journal with information on yourself and all of your-"

    scene imaniclassintro24
    with dissolve

    m "I’m leaving now. I’ll see you later tonight."
    s "Wait, tonight?"
    m "I’m sleeping over for the mini Christmas party we’re having at your house."
    s "How do you know about all of these things without secret knowledge from the future?"

    if bonus == True:
        m "Because I talk to people about things other than just sex and boobies."
    else:
        m "Because I talk to people about things other than hugs."

    m "Anyway, bye."
    m "Make sure that whatever present you decide to buy for the person unfortunate enough to be assigned to you isn’t one that will get immediately tossed into the trash."
    s "Thanks, Maya. I’ll make sure to pick up a separate present for you too and-"

    scene imaniclassintro26
    with dissolve
    play sound "slidedoor.mp3"

    s "Okay. Good talk."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene imaniclassintro27
    with dissolve2

    "Huh."
    "Well, at least it’s not Maya this time."
    "But what the hell am I supposed to buy for Miku?"
    "I don’t think it’ll be {i}too{/i} hard since I know she likes...soccer and...running and stuff- but neither of those things sound like they’d make particularly exciting gifts."
    "Oh well."
    "I’ll probably just wait until the last minute and choose whatever I can find."
    "Or, if I’m really struggling, just get her a gift card or something."
    "I don’t care what anyone says about how gift cards are {i}impersonal{/i} or bad gifts or anything."
    "Nothing says “I care about you” more than trusting someone with the free will to make their own decisions rather than making one for them, in my opinion."
    "But, this is clearly no time for an inner debate like that since I’m now acutely aware that someone {i}else{/i} is standing in front of my desk."

    if ayane_lust >= 20:
        scene imaniclassintro28
        with fade

        ay "Surprise Ayane visit! Time to love me!"
        s "You need to stop skipping gym class to come and see me. People are going to realize what your game is."

        scene imaniclassintro29
        with dissolve

        if bonus == True:
            ay "Everyone’s known my game since the start, Sensei! I’m like the Ami that people won’t think is weird for liking you so much since you and me aren’t {i}actually{/i} related."
        else:
            ay "Everyone’s known my game since the start, Sensei! Some people have already started lending me bones!"

        s "So, what’s up then? If this is about the Secret Santa thing, Maya just reminded me."

        scene imaniclassintro30
        with dissolve
        stop music fadeout 25.0

        ay "Well...it’s not about that. But it is {i}kind of{/i} a present, I guess?"
        ay "I just wanted to give you a sneak peek of something so I could get your thoughts on it before everyone else sees it."

        scene imaniclassintro31
        with dissolve

        ay "Plus, we haven’t really been spending any time in school {i}alone{/i} lately and...yeah."
        s "It’s kind of hard to find alone time when I’m surrounded by an ever-increasing number of girls."
        s "So, what is it you wanted to show me?"

        scene imaniclassintro32
        with dissolve

        ay "Well, I’m not going to just {i}tell{/i} you! That would ruin the surprise!"
        ay "You’ll have to follow me if you want to see it!"
        s "Then...lead the way, I guess?"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ christmastwo3 = True

        jump ayanelust20
...
```