# Baby it's Cold Outside
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikalust10&go=Go)


Part of event chain [Bottled Dreams](./christmas5.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: chikalust10
* Group: Chika
* Triggered by label: chikalust10intro

## Event code
File: \game\script.rpy
Code:
```python
...
label chikalust10:
    scene chikalustten9
    with dissolve2

    c "Oh no. It looks like I was wrong and I am cold after all."
    c "I guess this means you have to keep me warm."
    s "You did this on purpose."
    c "Yes."
    c "I’m not really trying to hide that."
    s "Okay, good. Because you’d be doing a pretty horrible job if you were."
    c "Are you cold too, Sensei?"
    s "A bit. The shoulder you’re leaning up against is significantly warmer than the rest of my body."
    c "That probably means we should get closer then, huh?"

    if bonus == True:
        jump chikalust10x
    else:
        scene black
        with dissolve2
        stop music fadeout 10.0

        s "Asbolutely not. I am offended that you would even suggest such a thing."
        s "We can hug instead, though. That much is allowed."
        c "Yes. Please hug me, Sensei."

        "We hug."

        $ renpy.end_replay()
        $ chikalust10 = True
        $ chika_lust += 1

        "{i}Chika’s lust has increased to [chika_lust]!{/i}"
        "………"
        "……"
        "…"

        jump christmas6

label christmas6:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
"Opinions are best when they’re kept isolated, which is why I will continue to ignore my thoughts and let everyone else be happy instead."

    scene chikalustten1
    with dissolve2

    c "Oh, Sensei! I forgot to tell you."
    c "Chinami and I got you a present since you’re always going out of your way for us."
    c "It’s nothing big since we’re still kind of low on money, but we hope you like it anyway."
    s "Speaking of Chinami, are you really leaving her alone on Christmas?"
    s "That seems unlike you."

    scene chikalustten2
    with dissolve

    c "We watched some movies and stuff together earlier. She’s asleep right now."
    c "So I guess {i}technically{/i} she’s alone on Christmas, but she’ll probably never even realize it since we’ll be back before she even wakes up."
    s "Fair enough. "
    s "Can I ask you something else, though?"
    c "Sure. What’s up?"
    s "Why are we holding hands right now?"
    c "Because I won you. You are my prize."
    s "I’m no expert on spin the bottle, but I’m pretty sure the person who spins is the one who technically “wins.”"

    scene chikalustten3
    with dissolve

    c "Nope! I’m the winner. And if you’re not going to kiss me in front of everyone, the least you can do is hold my hand."
    s "Okay but if anyone sees us, you’re taking the blame."

    scene chikalustten4
    with dissolve

    c "Of course. I planned on that anyway. "

    "And I’m assuming she planned on “winning” as well considering she basically leapt in front of the bottle as it stopped spinning."
    "If it was even a little off to the side, I imagine she would have pushed Maya over as well."
    "But hey, at least it’s proof that her affinity for me is actually genuine. "
    "Which isn’t to insinuate that it’s not like that with the others."
    "But Chika really does feel like an actual girlfriend at times."
    "It’s weird."

    scene chikalustten5
    with dissolve

    c "Hmm...Do you think anyone would care if we snuck outside for a bit?"
    s "I don’t think anyone would even know."
    c "Even better~"
    s "Is it, though? It’s freezing out and all you’re wearing is...that."
    c "I’ll be fine if it’s only for a few minutes. Besides, if I get cold, you can just warm me up."
    c "I’ll take the blame for that if we’re caught as well, so don’t even worry about it."
    s "You seem unusually confident tonight."
    c "Probs because I got the present I wanted most."
    s "…"
    c "…"

    scene chikalustten6
    with dissolve

    c "I’m talking about this cute handbag I got for myself before I left work yesterday."
    c "You’re the present I wanted second-most, though. So don’t feel too bad."
    s "I hope to one day be as essential as an accessory to you."
    c "And I hope to one day {i}be{/i} an accessory to you. "

    scene chikalustten7
    with dissolve

    c "Wait. That makes it sound like I’m okay with being some sort of mistress."
    c "What I meant to say is I just want to stay with you for a really long time. Kay?"
    s "Are we going outside or what? The door is right in front of us."

    scene chikalustten8
    with dissolve

    c "How come you never say anything cute back to me?"

    scene black
    with dissolve2

    "Chika and I make our way outside and walk around the perimeter of the hotel, stopping at an old bench leaned up against the brick walls."
    "The grass is overgrown and the exterior, particularly in the back, doesn’t match the high expectations the inside set-"
    "But the girl next to me manages to offset any flaws on the outside of the hotel by just being so fucking cute."

    if chika_lust < 10:
        "Unfortunately, an employee from the hotel decided to go out for a smoke break and told us that we weren’t allowed to be back here."
        "We spent the rest of our very special twenty-minutes together arguing that there shouldn’t be a bench here if people aren’t allowed to sit on it."
        "The argument changes nothing and we hang our heads as we make our way back to the hotel room."
        "But even though nothing really came of the meeting, Chika and I still manage to become a little bit closer."
        "It wasn’t much, but I’m glad we got to spend some of Christmas together."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ chikalust10miss = True

        stop music fadeout 5.0
        jump christmas6

    else:
        jump chikalust10
...
```