# Behind a Bathroom, Under the Blazing Sun (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Extra French Fries](./beachvacation4.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation5
* Group: Main
* Triggered by label: beachvacation4
* Chain sources: beachvacation4
* Chain sources path: beachvacation4

## Official wiki page

[Behind a Bathroom, Under the Blazing Sun](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation5&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation5:
    scene kirinbeach1
    with dissolve
    play music "behindabathroom.mp3"

    s "Hah...That much should be fine."

    "A few minutes go by and I finally feel ready to put myself out in public again."

    if bonus == True:
        "You’d think that after spending so much time around these girls that my body would stop reacting to them in...certain ways, but it appears that this is very much not the case."
        "I should have asked Makoto to return the favor when the two of us were alone a little while ago."
        "It’s not like she’d ever say no to me, so this is pretty much entirely my fault and I shouldn't be blaming Miku and Kirin."
        "Even if they were a little over the top with some of their hand motions."
        "Particularly Kirin."
        "Oh well. Now that it’s all said and done with, I might as well get back to-"
    else:
        "Here's hoping I don't run into Kirin a-"

    scene kirinbeach2
    with dissolve

    ki "Whaaaat? Sensei? What are you doing over here?"
    ki "What a coincidence that the two of us just happened to run into each other again on such short notice."
    s "Did you follow me?"

    if bonus == True:
        ki "I wouldn’t have had to follow you if you didn’t run away."
        s "I wouldn’t have run away if you and Miku didn’t test my willpower as a man in broad daylight."
    else:
        ki "Yes. Because belly."
        s "Belly bad. Put it away."

    scene kirinbeach3
    with dissolve

    ki "You know you liked it."
    s "That’s exactly the issue."

    scene kirinbeach2
    with dissolve

    ki "So, you've gotta tell me."
    ki "Have you and Miku hooked up yet?"
    ki "Cause I’ve never seen her get that close to a guy before."

    if bonus == True:
        ki "So either she really admires you, or you deflowered her while I wasn’t paying attention."
        s "Why are you always under the assumption that I’m engaging in illicit relationships with my students?"

        scene kirinbeach4
        with dissolve

        ki "Well, uhh, for starters, you’ve already got a boner and I’ve only been here for a minute."
        s "Wait, what?"

        "I look down to find that my erection has returned with a vengeance. God damn this body."

        s "Well, erection aside, no. Miku and I have not “hooked up.”"
    else:
        s "Why are you always under the assumption that I’m engaging in illicit relationships with my students when all I have done is hug them?"
        ki "Beats me, man. Have you hugged Miku or not?"
        s "No."

    scene kirinbeach5
    with dissolve

    ki "Why not? She not your type or somethin’?"
    s "More like she’s not {i}the{/i} type to be doing something like that in general."

    scene kirinbeach2
    with dissolve

    if bonus == True:
        ki "Hey, you don’t know that. You’ve seen how hyper that girl gets. Maybe she needs a ride or two on the teacher to take her down a few notches."
    else:
        ki "Give me your lunch money, old man."

    s "Is there something you want, Kirin? I feel like I’m being mugged right now."

    scene kirinbeach6
    with dissolve

    ki "I’m just trying to fucking talk to you. Jeez."
    ki "You think I would have left one of my best friends and my sister behind to go hang out with some random guy?"
    s "Kind of, yeah."

    if bonus == True:
        ki "Well, you’re probably right about that. But still. It’s annoying that everyone else is getting to spend time with you when {i}I’m{/i} the one who literally offered herself up in exchange for..."
    else:
        ki "Well, you’re probably right about that. But still. I made you a pretty good offer in exchange for-"

    ki "What did I even ask for again?"
    s "Vouching for you if you ever decided to not show up to[school]."

    scene kirinbeach7
    with dissolve

    ki "Wow, was it really something that little? You sure lucked out on that deal, didn’t you?"
    s "Not like I’ve redeemed my end of it yet, though."

    scene kirinbeach8
    with dissolve

    ki "Hmm...That’s right. You haven’t."
    ki "..."
    s "...?"
    ki "Hold on a sec."

    scene kirinbeach1
    with dissolve

    "Kirin steps away from me and peers her head around the corner of the pavilion."
    "She scans the area for a moment before returning and sticking her tongue out at me."

    scene kirinbeach3
    with dissolve

    if bonus == True:
        jump kirinbeachhjx
    else:
        ki "I have to go do a thing."
        s "What? Already? But we just got here."
        ki "I got called into work."
        s "Where do you even work?"
        ki "I'm teaching inner city kids to read."
        s "Wow. Maybe you are a good person after all."
        ki "The censored version of Lessons in Love really gives both of us time to show our true colors, doesn't it?"
        s "The what?"
        ki "Bye!"
        s "Oh. Okay. See ya."

        scene black
        with dissolve

        "Kirin leaves and I frown because I miss her, but at least someone might learn how to read."

        $ renpy.end_replay()
        $ kirin_love += 1
        $ beachvacation5 = True
        $ kirinbeachhj = True
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump beachvacation6

label beachvacation6:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```