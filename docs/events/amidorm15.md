# Back Out in the Heat
Ami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidorm15&go=Go)



## Event preconditions
✅Ami love greater than or equal to 15

✅Event "[Ami: No One Can See Us](./amidorm10.md)" is completed (event=amidorm10)

✅Event "[Maya: Secrets Worth Keeping](./mayadorm5.md)" is completed (event=mayadorm5)



## Next events
* [Main: Size Matters](./day142.md)
* [Main: What's Done is Done](./beachvacation1.md)
* [Ami: Important Things](./amisroom15.md)

## Event properties
* ID: amidorm15
* Group: Ami
* Triggered by label: amidorm
* Triggered by branch label: amidorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label amidorm15:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    s "Ami, open up. I’m bored."
    a "Coming! One second, Sensei!"

    "I hear a few drawers slam shut from inside of Ami’s room and wonder what it is she could be doing there."
    "But before those thoughts go anywhere substantial, the tapping of footsteps racing to the door drags me back to reality."

    play sound "dooropen.mp3"
    scene backinheatredux1
    with fade

    a "Hi! Perfect timing."
    s "Perfect timing for what, exactly? Because if you're going to make me do something-"

    scene backinheatredux2
    with dissolve

    a "Of course I'm going to make you do something. That’s my job. "
    s "Your job is to cook and clean for me, not force me back into the world when I'm finally able to get away from it."

    scene backinheatredux3
    with dissolve

    a "Oh, stop. It's not like I'm asking you to do anything serious. I just need you to come grocery shopping with me so Maya stops complaining about not having anything to drink."
    s "Tell Maya to get her own drinks. She’s scarily independent. I'm sure she can manage."

    scene backinheatredux1
    with dissolve

    a "She’s also super lazy. And I’m kinda running out of stuff too, so I just figured I'd go for a walk and fix the problem on my own."
    a "Or at least that's what I {i}was{/i} going to do. But now you get to come with me."
    s "Is anything even open around here this late?"
    a "Mhm! There’s a corner store a few blocks away from here that’ll be open for another thirty minutes or so."
    a "It's good you showed up when you did, Sensei! You would have missed out on your chance otherwise."
    s "What is it with you two and getting me to carry stuff across town this late at night?"
    a "It’s not “across town” Sensei, it’s like two blocks-"

    scene backinheatredux4
    with dissolve

    a "Wait. What did you just say?"
    s "I said that you are lucky I'm feeling generous tonight. Because otherwise, I would not do this."
    a "..."
    s "..."

    scene backinheatredux5
    with dissolve

    a "Okay!"
    a "Let's get a move on, Sensei!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "And so the two of us make our way out of the dorms and into the street."
    "The hot summer air surrounds us, forcing us into a battle in which our respective resolves are tested as we are forced to walk another two blocks to our destination."
    "One of several things that Ami and I have in common is our mutual hate for extremely hot weather."
    "So the fact that we have gone out at night, when temperatures are expected to be a bit cooler, and things are still like {i}this?{/i}..."
    "Well, that's just fucking annoying."

    scene backinheatredux6
    with dissolve
    play music "comfort.mp3"

    a "Guuuuuuuuuuuhhhhhh..."
    s "Yeah. I feel that."
    a "Why does it have to be so...sticky and gross outside? "
    a "Whatever happened to cooler summer nights? And who was it that signed us up for this billion degree weather?"
    s "No clue. But I think you and I should probably have a word with them."

    scene backinheatredux7
    with dissolve

    a "Hey, [amimaster]..."
    a "What would you think about maybe going away somewhere soon?"
    s "I would think that there are multiple problems with that suggestion."
    a "Problems? Like what?"
    s "Problem A: We can’t leave Kumon-mi."
    a "Who said we have to leave Kumon-mi? What if it was something simple? Like...the beach? Or an onsen or something?"
    s "Problem B-"
    a "Can we just forget about {i}Problem B{/i} and start making plans already?"
    s "No. Because Problem B is that it’s still the middle of the[school] year. When would we even have time to go anywhere?"
    a "It can just be for the weekend or something! Like...maybe we could rent a shack near the beach and all hang out there for a night or two?"
    a "Don't you think it would be nice to get away, Sensei?"

    scene backinheatredux8
    with dissolve

    a "I know you hate this heat just as much as I do...So inside your head, you’re probably all like “Yaaaay water!” or “I finally get to see my [niece] in a swimsuit!” or something like that."
    s "I am thinking nothing of the sort."

    "I am."

    s "In fact, the only thing that's running through my head at the moment is that Maya is going to have to get her own damn groceries next time."
    s "Especially considering the fact that it looks like the store we're heading to is closing right now."

    scene backinheatredux9
    with dissolve

    a "Wait, what?! No! Wait for us, old lady! We'll be quick, I promise!"

    scene black
    with dissolve2

    "Ami grabs my wrist and drags me to the front of the store with her, forcing me to bow and ask for the old woman to open back up for a few minutes."
    "The woman obliges and I follow my [niece] as she fills a basket with an assortment of random items that I wind up not paying much attention to."
    "And before long-"
    "We’re back out in the heat."

    scene amiheat1
    with dissolve2

    a "Bleeeeeeeeeeeeh..."
    a "Who even invented weather in the first place? They’re stupid and I want them to know that."
    s "No one “invented” weather, Ami. That's not a thing I should have to tell you."

    scene amiheat2
    with dissolve

    a "I obviously know that, [amimaster]. I’m not an idiot."
    a "Sure, I might be bad at math and science and...umm...all of the other subjects we have. But I've got a pretty good head on my shoulders, Sensei."
    s "Then why are there leeks in your shopping bag? I don't remember them being on the list."

    scene amiheat3
    with dissolve

    a "Wait...yeah. Why {i}are{/i} there leeks in my shopping bag?"
    a "How the heck did those even get in there?"
    s "I know the answer."
    a "Then what-"
    s "I snuck them in while you weren’t looking."

    scene amiheat4
    with dissolve

    a "You...snuck leeks into my basket?"
    s "I did."
    a "{i}Why?{/i}"
    s "..."
    a "Sensei, what kind of weird practical joke is that?"
    s "I think it's less of a joke and more me simply being passively hilarious."

    if bonus == True:
        a "Your sense of humor is stupid. "
        s "Enjoy your leeks, Ami."
        a "..."
    else:
        s "Get leeked, bro."
        a "What does that even mean?"
        s "It will be funny for people from the future."
        a "????????????????"

    s "That aside, did you get everything else you needed?"

    scene amiheat5

    a "Mhm. Soda for me and bunch of random milk tea thingies for Maya."
    s "You’re stocking up on soda? I figured you'd be a little more conscious about your health."
    a "It’s fun to do things you know aren’t good for you every once in a while."

    if amifingered == True:
        scene amiheat6
        with dissolve

        a "But I’m sure you know all about that...don’t you, [amimaster]?"
        s "Are you really saying what I think you’re saying right now?"
        a "Maybe. What do you think I’m saying?"
        s "That you’ve found out about my secret girlfriend."
        a "That’s right, I-"

        scene amiheat7
        with hpunch

        a "Wait, what?! Who is it?! I’ll kill her! You’re mine!"
        s "I’m kidding, obviously."
        s "You're referencing how our relationship has progressed past the point of us being {i}just{/i} family. Right?"

        scene amiheat6
        with dissolve

        a "Heheh...look at us, Sensei...Keeping something so {i}naughty{/i} hidden from so many people."
        s "Are you really trying to seduce me on a park bench just fifty feet away from a woman who sold you leeks a few minutes ago?"

        scene amiheat7
        with dissolve

        a "I never wanted these leeks! You did this! This is your fault!"
        a "And also no! I’m just stating facts!"

    else:
        scene amiheat8
        with dissolve

        a "But...then again..."
        a "I guess you might not think so."
        s "…"

        "There’s a certain sadness in Ami’s voice that I think I understand."

        if bonus == True:
            "A type of longing that most could not possibly fathom, but one that makes absolute sense to her."
            "But..."
            "I can’t do that with her."
            "The two of us can't be anything more than this."
            "She’s been through enough already."
            "She doesn’t need the only person she has left in the world taking advantage of her, even {i}if{/i} he wants to."
            "Which I'm not saying he does."
            "We just..."
            "We can't be like that."
        else:
            "Probably because I, too, am a sad panda."

    s "…"
    a "…"
    s "Ami."

    scene amiheat9
    with dissolve

    a "Hm?"
    s "Let’s go on a vacation."

    scene amiheat10
    with dissolve

    a "Wait, really?! We can?! "
    a "I was only being half-serious when I suggested it before!"
    s "Oh. Well, if that’s the case-"
    a "No! No take-backs! You said vacation, so I’m getting a vacation whether you like it or not!"
    s "It will have to be somewhere close, obviously. We don't really have the time to go anywhere else."
    a "Well, yeah. Obviously. Not like we have much of a choice anyway."
    a "Do you really have enough money to get all of us a place to stay, though?"
    s "..."
    a "...?"
    s "All of us?"
    a "Yeah. I mean, Maya and Ayane are coming too, right?"
    a "And if it’s some place like the beach, we might as well just invite the rest of the class too and have a huge vacation trip for {i}everyone.{/i}"

    "And here I was thinking this was going to be a thing for just the two of us."

    if bonus == True:
        "Oh well, I guess. Not like I’m going to say no to hanging out with even more cute girls at once."
        "If anything, this is even better."
        "I just hope that having everyone in one place {i}outside{/i} of school doesn't lead to any sort of drama."
    else:
        "But I guess that would be kind of inappropriate. And I don't want her to get the wrong idea."

    s "Yeah...everyone can come."
    s "It’s summer, so you should {i}all{/i} be enjoying yourselves."

    scene amiheat12
    with dissolve

    a "So should you, Sensei."
    a "You’ve always got that...tired look in your eyes that makes it seem like you just want to take a break from life."
    a "Let's hope that a vacation is what you need to pick yourself back up."

    scene amiheat13
    with dissolve

    a "And if it’s not, I can always just give you a big hug instead. As many as you want."
    a "That would probably work, right [amimaster]?"
    s "Yeah...I guess."
    s "I think I’ll take the vacation instead, though."

    scene amiheat7
    with hpunch

    a "Be more excited about hugging your [niece], you jerk!"

    scene black
    with dissolve2

    "The heat persisted until I dropped Ami back off at the dorm."
    "It didn't let up until I was already halfway home."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amidorm15 = True
    stop music fadeout 6.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amimissionaryanim:
        play sound "knock.mp3"
        "..."

        a "Helloooo? Who's there?"
        s "Your [uncle]. Is Maya around right now?"
        a "Yeah, I'm right he-"
        a "Wait, Maya?"
        a "You mean you're not here to see me?"
        a "What the heck is this?"
        s "Of course I'm here to see you."
        a "But if you're here to see me, then why would you ask for-"
        a "Oh. I get it."
        s "So, are you going to let me in?"
        a "Depends~ What's in it for me?"
        s "You know exactly what's in it for you..."

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump amimissionaryanimx
        else:
            $ ami_lust += 1
            stop music fadeout 4.0

            s "A hug."

            "{i}Ami's lust has increased to [ami_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label amibjrep:
    play sound "knock.mp3"

    a "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        jump amibjrepx
    else:
        $ ami_lust += 1
        stop music fadeout 4.0

        "{i}Ami's lust has increased to [ami_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mayadorm20:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label amidorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ami_love >= 5 and amidorm5 == False and day == 1 or day == 5:
                play sound "knock.mp3"

                s "Hey, Ami. Are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            if ami_love >= 5 and day != 1 and day != 5 and amidorm5 == False:
                jump amidorm5
            if ami_love >= 10 and day > 5 and day60 == True and amidorm5 == True and amidorm10 == False and day24 == True and amisroom10 == True:
                jump amidorm10
            if ami_love >= 15 and amidorm10 == True and mayadorm5 == True and amidorm15 == False:
                jump amidorm15
...
```