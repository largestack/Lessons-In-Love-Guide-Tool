# Reverse Cowgirl (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Die For What You Believe In](./beachvacation11.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation12
* Group: Main
* Triggered by label: beachvacation11
* Chain sources: beachvacation11
* Chain sources path: beachvacation11

## Official wiki page

[Reverse Cowgirl](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation12&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation12:
    scene sunbathing1
    with dissolve
    play music "normalday.mp3"

    s "Hello, ladies."
    mi "You sound kinda creepy when ya just walk up to a group of half-naked girls and say “Hey, ladies,” Sensei."

    if bonus == True:
        s "Not being creepy isn’t really a strong suit of mine."
        c "Aww, come on. You’re not that bad."

        "I stumble upon Chika, Tsuneyo, and Miku laying out on a blanket once the afternoon rolls around."
        "And, in case you were wondering, no. Maya didn’t actually die during the watermelon incident."
        "Thankfully, Karin was able to hold back and only used a fraction of her true power. "
        "So Maya got off without any internal bleeding whatsoever."
        "What a joyous occasion. "
    else:
        s "Yeah. That was not my best greeting. I apologize."

    t "You."
    s "Hi, Tsuneyo."

    scene sunbathing2
    with dissolve

    t "Ah-"

    scene sunbathing1
    with dissolve

    t "Wait, no. Stop that."
    t "I am mad at you."
    s "Why? I haven’t even really seen you since yesterday and-"
    s "Oh. "
    s "Yeah, I probably know what this is about."

    scene sunbathing3
    with dissolve

    mi "Sneaky move havin’ us girls do yer’ dirty work for ya. Karin almost died."
    s "Is {i}that{/i} why she was passed out in her breakfast when I made it to the beach this morning?"
    mi "Yup! Ruined a perfectly good dish and Ayane had to go buy her another one."
    s "Oh. Well then no one lost except for Ayane’s dad. This seems fine to me."

    scene sunbathing4
    with dissolve

    t "Wrong. I lost."
    t "I learned things today that I was not ready to learn."
    s "To be fair, these are things you probably should have learned about a while ago."
    t "Fuck you."
    c "Yeah...Think I’m gonna go out on a limb and side with Tsuneyo here, Sensei. "

    if bonus == True:
        c "It’s probably for the best if you just...don’t talk about masturbation or sex or anything like that with her. "
        c "I don’t think she’s prepared for that kinda stuff yet."

        scene sunbathing5
        with dissolve

        mi "Yeah. Not everyone here’s as mature as Chika and me, Sensei. Some people just take a little longer to develop. Like noodle-girl!"
        s "Wow, Miku. I had no idea you were ready to talk about stuff like that."
        mi "Whaddya mean? I’m ready to talk about anythin’ ya throw at me. Just name it."
        s "Any thoughts on reverse cowgirl?"
    else:
        c "There's a time and a place to teach language arts and the beach really isn't one of those places."
        s "Can I at least ask her if she's more interested in learning about it now that she's beginning to understand the basics?"

    scene sunbathing6
    with dissolve

    c "Sensei! What do you think you’re asking her?!"

    if bonus == True:
        jump cowboyx
    else:
        s "If she's more interested in learning about it now that she's beginning to understand the basics."
        t "Perhaps it is for the best if you just leave now."
        s "You know, I really think it might be all of you who are overreacting this time and that I didn't really do anything wrong."
        s "I understand that the point of vacation is to get {i}away{/i} from learning for a moment, but-"
        mi "You heard the woman, Sensei! Be gone!"
        mi "And take yer friggin' textbooks and ancient languages with ya when ya go!"

        scene black
        with dissolve2

        s "I understand. I am very sorry for doing something that was apparently so wrong."
        s "I will use this opportunity to {i}not{/i} study where this disconnect comes from and simply employ better common sense to ensure that it does not happen again in the future."
        t "And stay out, peasant."

        $ renpy.end_replay()
        $ beachvacation12 = True
        $ chika_love += 1
        $ tsuneyo_love += 1
        $ miku_love += 1
        stop music fadeout 5.0

        "{i}Your affection with Chika, Tsuneyo, and Miku has increased by 1!{/i}"
        "………"
        "……"
        "…"

        if ayane_lust >= 10:
            jump ayanelust10
        else:
            jump ayanelust10skip

label ayanelust10:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```