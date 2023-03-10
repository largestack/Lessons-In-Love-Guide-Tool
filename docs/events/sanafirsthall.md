# Nothing to Do (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Family Business](./firsttimebar.md) (Sana) is completed)



## Next events

* [Sana: Supermom](./bar10.md)

## Event properties

* Id: sanafirsthall
* Group: Sana
* Triggered by label: dormfriday
* Triggered by branch label: dorms
* Triggered by path: dorms->dormfriday->sanafirsthall

## Official wiki page

[Nothing to Do](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanafirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanafirsthall:
    scene sanahall1
    with dissolve

    s "Hey, Sana. Why are you just standing out here?"
    sa "Oh...umm...hi, Sensei..."

    scene sanahall2
    with dissolve

    sa "I don’t...really know..."
    sa "I just felt like...I was supposed to...for some reason..."
    s "Well, that's weird. But I guess I'm not really one to talk given my circumstances for being here."
    sa "What...kind of circumstances are-"
    s "Anyway, want to talk for a little while? Might help the two of us kill some time."
    s "Assuming you're not busy, of course. Which I doubt you are since you're kind of just...standing here."

    scene sanahall3
    with dissolve

    sa "Y-Yeah...I'm not doing anything..."
    sa "My mom is handling the bar to...give me time to study, but..."
    sa "Studying is kind of...really boring..."
    s "I can help you if you want. You might not know this, but I'm actually a teacher."
    sa "I had...no idea..."
    sa "I think I’ll...be okay, though..."
    sa "We can talk about something else instead...Something that doesn't make me want to fall asleep..."
    s "Sounds good. Maybe you can tell me a little about what your mom is like?"

    scene sanahall3r
    with dissolve

    sa "My...mom? Why do you want to know about her?..."
    s "Just wondering if that’s where you get any of your qualities from. The idea of an entire family of timid cyclops girls is quite amusing to me."
    sa "You...do know I...have a second eye...right?..."
    s "If you say so, Sana."
    sa "..."
    sa "Uhh...anyway..."

    scene sanahall4
    with dissolve

    sa "My mom and I...aren't really that much alike..."
    sa "I...do look like her, though..."

    "As much as I like Sana for her current appearance, I can't help but wonder what an aged up version would look like."
    "I'm sure I won't have to wonder for long, though. The two of us are bound to cross paths eventually."

    s "I’m guessing your mom's a lot more talkative than you are?"

    scene sanahall5
    with dissolve

    sa "That’s...{i}one{/i} way to put it..."
    sa "She’s...umm..."
    sa "Just...just go ahead and assume she's my...exact opposite..."

    scene sanahall4
    with dissolve

    sa "You’ll...find out whenever you meet her..."
    sa "Any way I describe her would...make her sound a lot worse than...she actually is..."
    s "That's...an interesting way to describe your mother. But I'll take your word for it."
    s "How are things with Ayane, then? I'm a little curious as to how you two ended up in the same dorm together."

    scene sanahall5r
    with dissolve

    sa "That just...kind of happened, I guess?"
    sa "I...don’t really have any friends other than her...And Ami and Maya were already together, so..."
    sa "Process of elimination?"
    s "That makes it sound incredibly depressing."

    scene sanahall6
    with dissolve

    sa "I know, but...it really isn't like that..."
    sa "We...actually {i}are{/i} good friends, so..."
    sa "You don't have to...feel bad for me or anything..."
    s "Great. Because that whole {i}sympathy{/i} thing isn't really one of my strong suits."

    scene sanahall4
    with dissolve

    sa "I'm not sure if...I understand what you mean by that, but...I like living with Ayane..."
    sa "She kind of...makes up for all of the things I'm lacking in..."
    sa "I just wish...she'd listen to...better music every once in a while..."

    "I guess there {i}is{/i} that whole saying about how opposites attract, so it's not bizarre to assume Ayane and Sana pair well together."
    "Lump the quietest girl together with the most talkative one and there's sure to be some sort of...dynamic there."
    "But to have both her best friend {i}and{/i} her mother be completely different from her?"
    "I feel like that could get...exhausting."

    s "Well, I’m happy {i}you're{/i} comfortable around her. That makes one of us."

    scene sanahall5r
    with dissolve

    sa "I know she...comes on strong...especially with you..."
    sa "But...I don't think you...have any reason to feel uncomfortable, Sensei..."
    s "We'll see about that, I guess."
    s "In the meantime, though, I'll let you get back to your compulsion to stand around the hall and neglect your education."
    sa "Oh...okay...I..."
    sa "I guess I'll...see you later, then?..."
    s "I'm sure you will. I plan on spending a lot of time in this hallway."
    sa "I..."
    sa "I'm not really sure how I...feel about that..."

    scene black
    with dissolve2

    "Sana and I talk for another minute or so before I leave the dorms and get on with my night."
    "She did mostly well this time, but I know that she's the type to get burned out by extensive conversations, so I figure it’s best to just leave her alone after a while."
    "As I step outside, I ponder what a fully adjusted and comfortable Sana Sakakibara would be like."
    "There's no way she can stay so reclusive forever, is there?"

    s "..."

    "I wonder how long it will be until I can see a new side of her?"
    "..."
    "I wonder if I'll like that one even more."

    $ renpy.end_replay()
    $ sanafirsthall = True
    $ sana_love += 1

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanahall:
    if chapthreeactive == True:
        scene sanasummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene sanahall7
        with dissolve
    else:
        scene sanahallwinter
        with dissolve

    sa "Um...Hello, Sensei..."
    s "Hey Sana. Are you free right now?"
    sa "Mhm. Did...you want to talk to me?"

    "Sana and I spend some time together outside of her room."
    "She tells me a few stories of how the bar has been as of late, and how she’s doing
    her best to try and engage more customers."
    "Of course, that comes with its own list of setbacks as well."
    "I’ll have to keep doing my best alongside her to make sure she gets the
    confidence she needs to run the place effectively."
    "The more time I spend with Sana, the more aware I become of how I really see her."
    "She’s definitely the outcast of the pack so far, and I want to keep protecting her for as long as I can..."

    scene black
    with dissolve

    $ sana_love += 1

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

                    ############################################
                    ##########        ROOM 1          ##########
                    ############################################

label chikadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if chika_love >= 5 and day == 1 and chikadorm5 == False:
                "I should probably wait until Yumi's not right there to hang out with Chika..."
                jump doorknock
            if chika_love >= 5 and day != 1 and day != 3 and firsttimemall == True and chikafirsthall == True and chikadorm5 == False:
                jump chikadorm5
            if chika_love >= 10 and mall10 == True and chikadorm5 == True and chikadorm10 == False:
                jump chikadorm10
            if chika_love >= 15 and chikadorm10 == True and chikadorm15 == False and day != 3 and day != 1:
                jump chikadorm15
            if chika_love >= 20 and mall15 == True and chikadorm20 == False:
                jump chikadorm20
            else:
                jump chikadormgen
        "Fingering" if chikadorm20 == True and bonus == True:
            jump chikafingerreplay
        "Handjob" if day139 == True and bonus == True:
            jump chikahjreplay
        "Hug" if chikadorm20 == True and bonus == False:
            jump chikafingerreplay
        "Hug Again" if day139 == True and bonus == False:
            jump chikahjreplay

label yumidorm:
    if yumi_love >= 5 and streets10 == True and yumidorm5 == False:
        jump yumidorm5
    if yumi_love >= 10 and yumidorm5 == True and yumidorm10 == False:
        jump yumidorm10
    elif yumi_love >= 5 and streets10 == False:
        play sound "knock.mp3"

        s "Hey Yumi, are you in there?"
        "..."
        "There's no answer."
        jump doorknock
    if yumi_love >= 15 and yumidorm10 == True and cafe20 == True and yumidorm15 == False:
        jump yumidorm15
    if yumi_love >= 20 and streets20 == True and yumidorm20 == False:
        jump yumidorm20
    if yumi_love >= 25 and streets25 == True and yumidorm25 == False:
        jump yumidorm25
    if yumi_love >= 30 and streets30 == True and yukidate1 == True and yumidorm30 == False:
        jump yumidorm30
    if yumi_love >= 35 and yumidorm30 == True and yumidorm35 == False:
        jump yumidorm35
    else:
        jump yumidormgen

label chikadormgen:
    play sound "knock.mp3"

    "..."
    c "Come in!"

    scene chikadormgen
    with fade

    "Chika and I spend our free time hanging out in her room."
    "We watch a few TV shows and I listen to her ramble on about how she's tired of working at the mall and
    wants to start a business or something."
    "But in order to start a business, you need money. And Chika seems to be using the money she earns on
    something else."
    "It gets late pretty quickly and the two of us decide that it would be best if I head back before Yumi gets home."

    scene black
    with dissolve
    $ chika_love += 1
    stop music fadeout 5.0

    "I can't help but feel a bit upset that we didn't get to spend more time together..."
    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumidormgen:
    play sound "knock.mp3"

    "..."
    y "Yeah? What do you want?"

    scene yumidormgen
    with fade

    "Yumi and I spend some time hanging out in her room together. Well...trying to, at least."
    "Apparently, even though we've been spending more time together as of late, she still absolutely hates my guts."
    "Does she have the right to do that? Yeah, I guess so. But that doesn't mean it isn't a bit of a let down."
    "I can't tell what it is, but I keep wanting to spend time with her. Maybe I have a thing for being belittled?"

    scene black
    with dissolve
    stop music fadeout 5.0

    "Eventually, and I mean less than twenty minutes later, she kicks me out of the room and I'm left to find something else to do..."

    $ yumi_love += 1

    "{i}Yumi's affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikadorm5:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label dormfriday:

    if chapthreeactive == True:
        scene summerdorm1fri
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene friwinter
        with dissolve
    else:
        scene dorm_friday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "This might be a good time to hang out with one of the girls."
    "It looks like Sana and Ami aren’t doing anything."
    "I could probably spend time with one of them if I want to."
    "What should I do?"

    menu fridaymenu:
        "Knock on a door":
            jump doorknock
        "Talk to Sana":
            if sanafirsthall == False and firsttimebar == True:
                jump sanafirsthall
...
```