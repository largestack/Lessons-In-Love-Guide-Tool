# Walkthrough (Molly)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Molly love greater than or equal to 30

* Event [Lifejacket](./rindorm50special.md) (Rin) is completed)

* Day of week (Mon-Sun) is after Tuesday

* Day of week is a weekday



## Next events

* [Main: Girls in Spandex](./halloweentwo1.md)

## Event properties

* Id: mollydorm30
* Group: Molly
* Triggered by label: mollydorm
* Triggered by branch label: mollydorm
* Triggered by path: mollydorm->mollydorm30

## Official wiki page

[Walkthrough](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollydorm30&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm30:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait for her to answer, but can’t help but notice a surprisingly familiar sound being muted as I do so."

    mo "…"
    s "…"
    s "Molly?"
    mo "Oh, it’s just you, Sir. "
    mo "I suppose that’s fine, then."
    mo "You may enter."
    s "Uhh...okay."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I turn the knob and make my way into Molly’s room, noticing that the volume has been slightly raised, but is still on the low side."
    "Based on what I {i}can{/i} hear, however..."

    if bonus == True:
        jump mollypornx
    else:
        s "Are you playing Raid: Shadow Legends again?"
        mo "Yes, Sir! Only the most important mobile game of our generation!"

        "Molly and I play Raid: Shadow Legends for a few hours before we decide to go outside and talk about Raid: Shadow Legends there."

label restofmollyporn:
    if bonus == True:
        "Molly takes a moment to put her clothes back on, once again making me turn around so I can’t watch her, and I begin to wonder how far I’m off from getting to skip that barrier in the future."
        "I mean, I know Molly’s been a little more open about stuff like this than most of the other girls for quite some time now, but I feel like this rejection thing might just be making her spiral into perpetual apathy."
        "Or something like that."
        "I don’t really know- nor do I care, since I’m already reaping the benefits of her sudden sexual growth."
        "Or disinterest."
        "Again, I still don’t really know."
        "But that doesn’t matter right now."
    else:
        "I guess the outside part doesn't really matter, now that I think about it."

    scene mollyporn8
    with dissolve2
    play music "thesleepingcity.mp3"

    "What {i}does{/i} matter is that it’s fucking cold."

    if bonus == True:
        s "I’m starting to think that {i}I{/i} should have [masturbate]d before coming out here to raise my body heat."
        mo "Very funny, Sir."
        mo "Though, I will admit that I am not feeling the cold just yet. So perhaps your idea isn’t too bad in the grand scheme of things."

    s "So, is {i}that{/i} really all you’ve been doing lately?"

    scene mollyporn9
    with dissolve

    mo "Playing games?"
    s "Playing those kinds of games."
    s "If you’re doing it to the point where it’s not even fun anymore and just a means of killing time, I can think of a lot better ways to do that."
    mo "There are always {i}better{/i} ways to do anything, Sir. But it doesn’t mean that anyone will actually do them."

    scene mollyporn10
    with dissolve

    mo "Growing closer to someone inside of a setting where everything is make believe is better in every way than doing the same thing in real life."
    mo "You don’t have to leave your chair. You don’t have to worry about what anyone thinks of you. And you can also look up a walkthrough whenever you get stuck."
    mo "This realm does not have walkthroughs, Sir. You need to fail in order to figure out what to do next."
    mo "But failing is painful...and closes off certain paths to you for good."

    if bonus == True:
        mo "So, if I continue to avoid that, I’ll find nothing but success in love and...sex."
        mo "And I can also have a million girlfriends or boyfriends and none of them will get jealous of one another unless it's a major underlying theme of the games they appear in."
        s "Now, that definitely does sound like a plus. Except for the boyfriend thing. I don’t really need one of those."

        scene mollyporn11
        with dissolve

        mo "See? This way of living isn’t entirely bad!"
        mo "Just...it can be a little depressing when you take the time to actually {i}think{/i} about what’s happening."
    else:
        s "Are we still talking about Raid: Shadow Legends?"

    scene mollyporn12
    with dissolve

    mo "You know...after seeing what Rin did to herself...and what she said to me...I couldn’t help but tear myself up over it."

    if bonus == False:
        s "I guess not."

    mo "And even though I disagreed in the heat of the moment about...{i}choosing{/i} her...I think she may have been right."
    s "I don’t think anything Rin said that night was “right.” "
    s "It’s hard for someone to make any sort of argument while having their wounds held shut by someone else."
    mo "That part...I don’t disagree with."
    mo "What I {i}do{/i} agree with, though, is that I didn’t have to push things further."
    mo "I knew she didn't want me...but I tried to make her want me anyway."
    mo "I didn’t have to start moving away from 2D out of...curiosity or interest or whatever other foul magic may have caused me to do the things I did."
    mo "I could have stayed inside of the vessel that’s served as my escape for so long now."
    mo "I don’t {i}have{/i} to want someone real. But I did anyway."
    mo "And that was a choice."
    s "…"
    mo "…"

    scene mollyporn13
    with dissolve

    mo "It was a choice..."
    mo "The wrong choice."

    if bonus == True:
        jump endofmollyoutsidex
    else:
        s "..."
        mo "..."
        s "Okay, well you're weirding me out so...I'm gonna go."
        mo "Okay, see ya."

        scene black
        with dissolve

        "The conversation comes to an abrupt end, but I manage to escape without hugging Molly."
        "I don't really know why, but I feel like I might have to hug her eventually."
        "I hope the Irish are okay with that. I don't really know much about their culture."

        $ renpy.end_replay()
        $ molly_love += 1
        $ mollydorm30 = True
        stop music fadeout 5.0

        "{i}Molly’s affection has increased to [molly_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

                    ############################################
                    ##########        ROOM 7          ##########
                    ############################################

label utadorm:
    if uta_love >= 5 and utamaid5 == True and utadorm5 == False:
        jump utadorm5
    if uta_love >= 10 and utadorm5 == True and day != 2 and utadorm10 == False:
        jump utadorm10
    if uta_love >= 15 and day != 2 and utamaid10 == True and utadorm15 == False:
        jump utadorm15
    if uta_love >= 30 and utamaid25p2 == True and utadorm30 == False:
        jump utadorm30
    elif uta_love >= 5 and utamaid5 == False:
        "I should probably get to know Uta a little better before I see if she wants to hang out in her room."
        jump doorknock2
    else:
        jump utadormgen

label utadormgen:
    play sound "knock.mp3"

    u "Come on in!"

    scene utadormgen
    with fade

    "I walk into Uta's room to find her just lounging around and listening to music on her phone."
    "She hops off the bed and excitedly hurries over to me, almost slipping on a pair of pants near her end table."
    "Fortunately for her, I'm able to catch her before she winds up cracking her head open on the floor."
    "{i}Unfortunately{/i} for me, this gives her the opportunity to tease me for the next half hour about keeping my hands to myself."
    "I'm sure she's just kidding, but I still get the urge to let her fall next time."
    "Of course, I'd feel overwhelmingly guilty if she actually got hurt."
    "And I definitely wouldn't want it to impact her appearance in any way, so..."
    "I guess I can take one for the team and let her tease me for a while longer."
    "Even if I saved her life."

    scene black
    with dissolve

    "The night goes on with just as much quirky flirting as I expected when I came here, and I wouldn't trade a second of it for anything else."
    "Well, actually, I'd definitely trade it for the opportunity to have all of that flirting to come to fruition, but..."
    "I guess something like that just isn't in the cards for tonight."
    "Either way, I'm glad I got to spend some time with Uta."
    "I can feel the two of us growing closer every single day."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta's affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label utafirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm:
    if molly_love >= 5 and mollycafe1 == True and mollydorm5 == False:
        jump mollydorm5
    if molly_love >= 10 and mollydorm5 == True and mollycafe10 == True and mollydorm10 == False:
        jump mollydorm10
    if molly_love >= 15 and christmas7 == True and mollydorm15 == False:
        jump mollydorm15
    if molly_love >= 20 and mollycafe20 == True and mollydorm20 == False:
        jump mollydorm20
    if molly_love >= 30 and rindorm50special == True and day > 2 and day < 6 and mollydorm30 == False:
        jump mollydorm30
...
```