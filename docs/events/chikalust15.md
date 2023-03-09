# The Princess & The Pauper
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikalust15&go=Go)


Part of event chain [Post-Game Celebration!](./dormwar16.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: chikalust15
* Group: Chika
* Triggered by label: dormwar16

## Event code
File: \game\ChikaEvents.rpy
Code:
```python
...
label chikalust15:
    play sound "dooropen.mp3"
    scene goodmorningio1
    with dissolve

    "I collapse into bed after being dropped off at the hotel by Maki."
    "I was hoping that by sticking around for so long and watching so many girls get intoxicated, that one of them might let their judgment slip and make my night a bit more interesting."
    "But here I lay, in the same clothes I slept in last night, completely alone. "

    s "…"

    "The bed smells like Io."
    "She probably slept here for a few hours after I left this morning."
    "I wonder if she’ll come again tonight."

    play sound "knock.mp3"

    "I imagine the sound of her knocking, worried that one of the other girls might be rounding the corner at that moment."
    "She’d peer over her shoulder every few seconds while I make my way to the door- an explanation or excuse already prepared in the event of being caught."
    "An explanation that she’d probably throw away the second she's confronted."
    "What an adorable coward she is."
    "It would be nice if she came tonight."

    play sound "knock.mp3"

    s "…"

    "Perhaps I wasn’t imagining anything at all?"

    scene black
    with dissolve

    "I get off the bed and make my way over to the door."
    "It appears I won’t have to be alone after all."

    scene chikatoukafun1
    with dissolve
    play music "asobeatsex2.mp3"

    c "{i}*Hic*{/i} Hiiiiiiiiiiiii~"
    s "You...can still walk?"
    c "Can’t...{i}*hic*{/i}...get rid of me...that...eashilyyy..."
    to "My face...feels...{i}*hic*{/i}...rather strange..."

    "Welp, there is absolutely no way that at least one of them won’t be regretting this in the morning."

    c "Whatcha...doin’ Sensei?..."
    c "We weren’t...{i}*hic*{/i}...finished hangin' out yet..."
    s "Really, how did you two even get over here? You could barely walk when we left the bar."
    c "It’s the...{i}*hic*{/i}...power of love, Sensei!"
    c "Now...let’s...{i}*hic*{/i}...make out..."
    s "And was Touka brought here by the power of love as well?"
    to "Love..."
    to "Love sounds...lovely..."
    c "Touka’shhh...fine..."
    c "We were just {i}*hic*{/i}...talking about our...dates with you..."

    if bonus == True:
        jump chikatoukax
    else:
        scene black
        with dissolve

        s "This is no time for tomfoolery. I must nurse the two of you inebriated women back to health."

        "I take it upon myself to make some coffee for the girls and sit with them until they are sober enough to return to their rooms."
        "But, for some strange reason, I feel compelled to choose one of them as the winner of being drunk."

        menu:
            "Chika wins":
                $ dorm1warpoints += 1
                $ chikalingeriewin = True

                "Chika is clearly the better drunk."
                "I am glad I was able to swiftly reach a decision."
            "Touka wins":
                $ dorm2warpoints += 1
                $ toukalingeriewin = True

                "Touka is clearly the better drunk."
                "I am glad I was able to swiftly reach a decision."

        stop music fadeout 5.0
        $ renpy.end_replay()
        $ chikalust15 = True
        $ chika_lust += 1

        "{i}Chika's lust has increased to [chika_lust]!{/i}"
        "………"
        "……"
        "…"

        $ totaldays += 1
        $ day -= 6
        if day == 1:
            hide sunday onlayer date
            show monday onlayer date
        else:
            "ERROR ADVANCING DAYS"

        "[totaldays] Days have passed..."

        jump dormwar17

label chikainvitemissionary:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump chikainvitemissionaryx
    else:
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika's lust has increased to [chika_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label chikaspecial40:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
u "Okay, but I’m closin’ my eyes the second you start touching her unconscious body in inappropriate places."
    else:
        u "Okay, but I’m closin’ my eyes the second you two start hidin' the soup so I don't know where to look for it!"

    mak "Hah..."
    mak "I’m so tired..."

    scene postfashion44
    with fade

    c "Come on! Live a little! Just one!"
    y "The fuck do you gain from me drinking? I have to watch your sister tonight."
    c "Yumi, it’s one beer. It’s not going to affect whether or not you’re able to babysit."
    c "There are adults everywhere, too. Nothing bad is going to happen, really."
    to "Oh my. I’ve heard about this. But to think I’d go from being a loner to experiencing “peer pressure” in less than a week is quite jarring."

    scene postfashion45
    with dissolve

    c "Touka~ Let’s have fun!"
    c "I’ve been wanting to hang out with you since you transferred in and we haven’t really gotten a chance yet."
    c "Isn’t now like, the best possible time?"
    to "I...suppose it’s as good a time as any, but I don’t quite understand the need for alcohol."
    to "And I normally begin to feel...impaired after just a glass of wine, so..."
    c "I wanna see drunk Touka!"
    c "You’re always so formal all the time. What if you’re like, super exciting when you’re drunk?"
    to "Exciting {i}how{/i}?..."
    c "Idunno. Like, maybe you start singing or dancing or get really mean and start trying to fight people."
    to "Fight people?..."
    to "Well...you do spend most of your time with Yumi...so I suppose you just...enjoy hanging out with those types of people..."

    scene postfashion46
    with dissolve

    y "The fuck you mean by {i}those{/i} types of people?"
    to "I...I meant no offense!"
    to "I’m just acknowledging Chika’s affinity for...more masculine women!"
    y "You saying I have a fuckin’ dick?"
    c "Yay! Bonding!"
    c "Now hurry up and take these beers so I don’t have to stand around holding them all night!"
    s "Hey, everyone. What’s going on over here?"

    scene postfashion47
    with dissolve

    c "Sensei! You’ll drink with me, won’t you?"
    c "These two are being total buzzkills."
    s "I didn’t even know you liked drinking, Chika."
    c "Well...I don’t, really. "
    c "But...when in Rome, you know?"
    c "We just finished battling it out with one another, so it makes sense for everybody to kick back and relax for a little while."
    c "Besides, if I get really drunk, no one will hold it against me if I start getting all up in your business! And I can just blame it on the alcohol if they do!"
    s "I see that you’ve completely and rationally thought all of this through, then."
    to "Sensei...what do you think I should do in this situation?"
    s "Me?"
    to "I’m supposed to look toward you for guidance, and I do not have much experience with peer pressure."
    y "Looking to this guy for guidance probably ain’t the best idea, Tamako."
    to "Touka."
    s "You tell her, Tsuneyo."

    scene postfashion48
    with dissolve

    to "That is a completely different girl!"

    if chika_lust >= 15:
        s "I think you should go for it, Touka. "
        s "It’s not every day you get a chance to feel like a normal [high_school]er. And your mother {i}is{/i} right over there in the event that you get too hammered."

        scene postfashion49
        with dissolve

        to "Well...I suppose it is true that my mother would not intentionally put me in harm’s way."
        to "So perhaps I am just misinterpreting the concept of peer pressure and...just finally being included in something."
        s "Well, there you go. Enjoy your youth."
        c "You gonna do it with me, Touka?"

        scene postfashion50
        with dissolve

        to "What the heck. Why not?"
        to "What’s the worst that could possibly happen?"

        scene black
        with dissolve2
        stop music fadeout 20.0

        "I stay with Chika and Touka a little while longer as they “enjoy their youth” together."
        "Of course, Yumi does not join in on the fun and, instead, heads back to the Chosokabe apartment to watch after Chinami."
        "Apparently, the two of them let her spend the night at the apartment alone last night. But doing that two nights in a row is cause for concern."
        "Either way, Chika and Touka proceed to drink."
        "And drink."
        "And drink."
        "And soon enough, the two of them can barely even walk and Maki has to drive them back to the hotel."
        "I catch a ride as well, since basically everyone else has already left and..."
        "Well, I’m just really tired of walking..."

        $ renpy.end_replay()
        $ dormwar16 = True
        jump chikalust15
...
```