# Temporary Bliss
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindorm25&go=Go)



## Event preconditions
✅Kirin love greater than or equal to 25

✅Event "[Noriko: Loxosceles Reclusa](./norikodorm25.md)" is completed (event=norikodorm25)

✅Day of week is not Wednesday



## Next events
* [Chika: In Search of Summer](./chikaspecial40.md)
* [Kirin: Four Hand Massage](./kirinsoccer25.md)
* [Yuki: Opposite Directions](./yukidate10.md)

## Event properties
* ID: kirindorm25
* Group: Kirin
* Triggered by label: kirindorm
* Triggered by branch label: doorknock2

## Event code
File: \game\KirinEvents.rpy
Code:
```python
...
label kirindorm25:
    play sound "knock.mp3"

    "I knock on Kirin’s door and wait for her to answer."
    "Typically around this time of night, I’d be able to hear the TV on full blast or the unintelligible, angsty yelps of music Noriko has on."
    "However, tonight looks to be a slow one for the girls of dorm 10. "

    if bonus == True:
        "Either that or Kirin is just masturbating, which, all things considered, is an equally probable scenario when compared to the other things I listed."

    ki "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        "Ready for things to get “intense” if my final prediction is true, I bring my fingers to my zipper for easier access when Kirin demands control over my penis."
        "I am prepared, Kirin. "
        "Bring on the sex."
    else:
        "I do a cool spin move before walking into the room because I want to get the dancing out of my system first."

    scene kirinreading1
    with dissolve

    ki "Yo."
    s "Hey."

    if bonus == True:
        "So, it appears that my prediction was not entirely incorrect, but not entirely {i}correct{/i} either seeing as she’s just...casually reading an adult magazine like it’s the news section of the paper."
        "I hesitantly loosen my grip on my zipper as the probability of fucking her becomes unclear."
    else:
        "I do another spin move but Kirin is not impressed."

    if kirinkill == True:
        ki "Looking for Noriko?"
        s "Looking for you, actually."
        ki "Even after voting to kill me over her and Chika? "
        s "Oh, come on. Are you still upset about that?"
        ki "No. I love being murdered. It does wonders for my self esteem."
        s "Kirin, I formally apologize for killing you. "
        s "And, if it will make you feel any better, I will allow you to ride on top tonight."

        scene kirinreading2
        with dissolve

        ki "Golly gee, Sensei! On top? You really think I can do it?!"
        s "I think you can do {i}anything{/i} if you believe in yourself, Kirin."

        scene kirinreading1
        with dissolve

        ki "Get bent. I don’t want to have sex tonight."

        "Oh no. I think I broke Kirin."

    else:
        scene kirinreading3
        with dissolve

        if bonus == True:
            ki "What are you doing? Were you just holding your zipper?"
            s "What? No. Of course not."
            s "Why would I, an upstanding citizen and reliable teacher, come into this dorm room under the assumption that we were going to have sex?"
            ki "Probably becauuuuse...that’s...what we do?"

            "I tighten my grip on the zipper again, waiting for the signal that it’s go-time."

            ki "Well, correction. That’s what we {i}normally{/i} do. I’m too tired tonight."

            "The grip loosens again. This is getting exhausting."

            ki "But if you want to jerk off in mine or Noriko’s underwear, you can go pick up our laundry from downstairs. I’ll take losing one pair as the cost for not having to carry everything up here myself."
        else:
            ki "What was the spin move for?"
            s "What spin move? I don't know what you're talking about."

    if bonus == True:
        jump kirinpornox
    else:
        ki "If you're going to just keep doing that, get out. I'm busy."
        s "Whatcha reading, buddy?"

        "I do another spin. It is my best one yet."

        ki "..."
        s "What is wrong?"

        "More spins."

        scene black
        with dissolve

        ki "Okay. You're done."

        "Kirin gets off the bed and grabs me by the scruff of my neck like I am kitten."
        "It is equal parts comforting and scary, but then she throws me out of the room and I decide that it was {i}mostly{/i} scary."
        "I do another spin move on my way out of the dorm."
        "I am so cool and Kirin is a loser for not seeing that."

        $ renpy.end_replay()
        $ kirindorm25 = True
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

label kirinsoccer25:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
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
    if kirin_love >= 25 and norikodorm25 == True and day != 3 and kirindorm25 == False:
        jump kirindorm25
...
```