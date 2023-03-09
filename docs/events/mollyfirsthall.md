# The Cult of Molly
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollyfirsthall&go=Go)



## Event preconditions
✅Event "[Main: Lifting the Curse](./day154.md)" is completed (event=day154)



## Next events
None

## Event properties
* ID: mollyfirsthall
* Group: Molly
* Triggered by label: dorm2monday
* Triggered by branch label: dorm2monday

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label mollyfirsthall:
    scene mollyhall1
    with dissolve

    s "Hey, Molly. What are you up to?"
    mo "Afternoon, Sir! "
    mo "I decided to be adventurous this fine evening and journey outside of my room."
    s "Oh, really? Are you going somewhere?"
    mo "Negative, Sir. This is as far as I am willing to go."
    mo "In order to break the NEET mold, I must stand in this very hallway for at least an hour once a week."
    mo "What a coincidence that you just happened to show up on that very day!"
    s "I mean, I show up on other days too. I don’t think it’s that strange of a coincidence."

    scene mollyhall2
    with dissolve

    mo "Tell me, Sir. Do you believe in fate?"
    s "I feel like I’ve answered this question for someone else before."
    mo "I believe, Sir. I believe we were fated to meet in this very hallway."
    mo "This is a gift from the Heavens above! Or the Hells below! Whichever you believe in!"
    s "And if we don’t believe in either?"
    mo "Then find something to believe in!"
    mo "Or better yet, believe in me!"
    mo "Oh! Even better than that-"
    mo "Believe in the me that believes in you!"
    s "Molly, what the fuck are you even talking about?"

    scene mollyhall3
    with dissolve

    mo "I JUST SHOTGUNNED A MONSTER AND I’M READY TO KICK ASS! LET’S GO!"
    s "If you’re going to ask someone to believe in {i}you{/i} instead of heaven or hell, you’re going to need better reasoning than “I just shotgunned a monster.”"

    scene mollyhall2
    with dissolve

    mo "Let’s face it, Sir. You’ll believe in Molly MacCormack whether she gives you a good reason or not."
    s "And why is that?"

    scene mollyhall4
    with dissolve

    mo "Because cute girls are more powerful than God! Especially ones with green thigh-high’s named Molly!"
    mo "And as further proof, I’ll have you know that I {i}killed{/i} several gods just earlier today in a video game I was playing."
    mo "So if that’s not enough reason for you to worship me, I don’t know what is."
    s "Are you...starting a cult or something?"

    scene mollyhall5
    with dissolve

    mo "Yeah. But it’s a totally wholesome one and I’m not going to ask you to pray or donate or anything."
    mo "We can just hang out, eat junk food, and watch movies."
    s "That...actually sounds like a pretty sweet deal."
    mo "The sweetest deal, Sir."
    s "And where can I sign up for this so-called “Cult of Molly?”"

    scene mollyhall4
    with dissolve

    mo "All I need is eight ounces of your blood. That is enough to perform the ritual."

    scene mollyhall5
    with dissolve

    mo "I’ll also need you to sign a few papers."
    mo "I like to keep things organized, Sir. And without proper documentation for each and every member, things are bound to get wild."
    mo "Just look at Christianity, Sir. There are like ten different kinds now. Would that really have happened if everyone had to sign a form?"
    s "Uhh...Probably?"

    scene mollyhall2
    with dissolve

    mo "Nonsense! Malarky! "
    mo "Real religion is like a gym membership. You sign up ‘cause you think it’s cool and then wind up forgetting about it and ultimately stop caring altogether."
    mo "The Cult of Molly, though...That’s where things become different."

    scene mollyhall4
    with dissolve

    mo "Together, we’ll usher in the end of times! The last of days! The...ending of...stuff!"
    s "You need to chill out with the energy drinks, Molly. Your enthusiasm is going to tear this place down."

    scene mollyhall3
    with dissolve

    mo "Let it burn for all I care! I’ll move in with you and Ami!"
    s "You two would have to sleep in the same bed."

    scene mollyhall6
    with dissolve

    mo "I hope she likes cuddling, Sir. I tend to grab onto things when I sleep, you see."
    mo "It’s a habit I’ve had since birth. "
    mo "I think it’s because I’m so full of love that it possesses me in my sleep."
    mo "It's either that or a demon."
    mo "It could be either one, Sir."
    s "That’s nice, Molly."

    play sound "texttone.wav"
    scene mollyhall7
    with hpunch

    mo "Gah!"

    "Molly’s cell phone suddenly rings from inside of her pocket, causing her to jump up in surprise."

    scene mollyhall8
    with dissolve
    play sound "phonebeep.wav"

    mo "Who the heck is textin’ me at this time of night? Don’t they know that the latest update is supposed to drop in-"

    scene mollyhall9
    with dissolve

    mo "AH! RIGHT NOW! "

    scene mollyhall10
    with dissolve

    mo "Sir...I apologize for cutting this meeting short, but it appears that I have prior engagements."
    s "Go play your game, Molly. I’ll just find something else to do."
    mo "Roger. Please feel free to visit me again soon, though!"
    mo "Preferably on a day where I don’t have games to play!"

    scene mollyhall11
    with dissolve

    s "…"
    s "How am I supposed to know when that is?"

    scene black
    with dissolve

    "I wind up walking around the area surrounding the dorms for a few minutes afterward, hoping to bump into another familiar face. "
    "Unfortunately, I don’t find anything and am forced to go home early..."
    "Oh well, I guess."
    "At least Molly’s probably having a good night."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollyfirsthall = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyofirsthall:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label dorm2monday:
    if chapthreeactive == True:
        scene summerdorm2mon
        with dissolve
    elif mollysad == True and chapthreeactive == False:
        scene monwinter2nomolly
        with dissolve
    elif day288 == True and mollysad == False and chapthreeactive == False:
        scene monwinter2otoha
        with dissolve
    elif christmas7 == True and day288 == False and chapthreeactive == False:
        scene monwinter2
        with dissolve
    else:
        scene dorm2_monday
        with dissolve


    if mollysad == True:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Otoha isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"
        jump monday2menu
    elif day288 == True and mollysad == False:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Molly and Otoha aren't doing anything."
        "I could probably spend time with one of them if I want to."
        "What should I do?"
        jump monday2menu
    else:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Molly isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"
        jump monday2menu

    menu monday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Molly" if mollysad == False:
            if mollyfirsthall == False:
                jump mollyfirsthall
...
```