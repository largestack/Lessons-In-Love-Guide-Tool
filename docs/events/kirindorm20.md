# Terms & Conditions (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kirin love greater than or equal to 20

* Event [Bye Bye, Boner](./kirindorm15.md) (Kirin) is completed)

* Day of week is not Wednesday



## Next events

* [Kirin: All That is Contaminated](./kirindate25.md)
* [Main: Operation: Firestarter](./day318.md)
* [Noriko: Kind Of, Yes. Kind Of, No.](./norikodorm10.md)

## Event properties

* Id: kirindorm20
* Group: Kirin
* Triggered by label: kirindorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->kirindorm->kirindorm20

## Official wiki page

[Terms & Conditions](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindorm20&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label kirindorm20:
    play sound "knock.mp3"

    "I knock on Kirin’s door, waiting to see if she’s around tonight."
    "And, I guess I’m waiting to see if Noriko is around as well in a sense, given that she’s here pretty much every time Kirin is."

    if bonus == True:
        "If so, could this finally be the night of the fated threesome?"
        "Will my dreams finally come true?"

    ki "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I walk into the room to find things rather quiet."
    "And, within a matter of seconds, dreams die."

    scene kirinalmostsex1
    with dissolve

    s "Fuck."
    ki "Shit."
    ki "Why are we cursing?"
    s "Just coming to terms with something."
    ki "Looking for Noriko?"
    s "Not exactly. I’m fine with just hanging out with you."

    scene kirinalmostsex2
    with dissolve

    ki "Oh good. I’m glad you’re {i}fine{/i} with it."
    s "You know what I mean."
    ki "I’d still prefer to hear you say it out loud."
    s "I am here to spend time with Kirin Kanda and no one else but her."
    ki "Now say it more believably."
    s "Don’t push it. There are over ten other girls in this building that I can go hang out with instead right now."

    if bonus == True:
        ki "Mhm. But you’re in {i}my{/i} room. So I take it that means you either need something from me or you want to take my clothes off."
        s "Are you implying I wouldn’t come here to just talk?"
        ki "We both know that sex is better than talking."
        s "Correct me if I’m wrong, but you’re still a virgin. So you don’t technically {i}know{/i} that."
        ki "That’s right. I’m an innocent little girl who just dreams of being pinned down and ravaged by her teacher."
    else:
        ki "True. But how many more of them have the third season of Seinfeld on DVD?"
        s "Are we really bringing that up again? That was so long ago."
        ki "Just like the tragic volcano that destroyed Pompeii."

    ki "I guess we can talk about that?"
    s "Perfect. That’s one of my favorite topics."
    ki "It’s one of mine as well. "
    ki "In fact, I think I’ll skip out on my other obligations for tonight just so we can experience this wonderful conversation together."

    if bonus == True:
        jump kirinalmostx
    else:
        s "Awesome."

        scene black
        with dissolve

        "Kirin and I spend the rest of the night talking about Pompeii."
        "It is very sad."
        "But that's okay because she has the third season of Seinfeld on DVD and the passable humor of that is enough to quell some of the sadness."
        "George Constanza sure is a hoot."

        $ renpy.end_replay()
        $ kirindorm20 = True
        $ kirin_love += 1
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label norikodorm5:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label kirindorm:
    if kirin_love >= 10 and day271 == True and day != 3 and utadorm5 == True and iodorm5 == True and kirindorm10 == False:
        jump kirindorm10
    if kirin_love >= 15 and kirinsoccer20 == True and day != 3 and kirindorm15 == False:
        jump kirindorm15
    if kirin_love >= 20 and kirindorm15 == True and day != 3 and kirindorm20 == False:
        jump kirindorm20
...
```