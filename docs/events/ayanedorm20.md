# Still Young (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 20

* Event [Endless Torment](./dojo20.md) (Ayane) is completed)

* Event [Less Like the Vulture](./ayanedorm10.md) (Ayane) is completed)

* Event [Shaking The Tree](./sanadorm15.md) (Sana) is completed)

* Day of week is Saturday



## Next events

* [Ayane: Regularly Scheduled Programming](./dojo25.md)

## Event properties

* Id: ayanedorm20
* Group: Ayane
* Triggered by label: ayanedorm
* Triggered by branch label: ayanedorm20
* Triggered by path: ayanedorm20

## Official wiki page

[Still Young](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanedorm20&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm20:
    play sound "knock.mp3"

    "I knock on Ayane's door and wait for-"

    play sound "dooropen.mp3"
    stop music fadeout 3.0

    "…"

    ay "Come in."
    s "…"
    ay "…"
    s "Okay."

    scene black
    with dissolve2

    "Ayane opens the door less than two seconds after I knock which, in itself, isn't something to write home about."
    "In fact, one out of every three visits here normally starts the same exact way."
    "This time is different, though."
    "This time, there is no excitement."
    "There's no rush to get as close to me as possible- nor energized advances or the hastened removal of our clothing."
    "Just a door that was opened a little too quickly-"
    "And the mess of a girl who was waiting behind it."
    "........."
    "......"
    "..."

    scene ayanecancrytoo1
    with dissolve2
    play music "closeto.mp3"

    ay "…"
    s "…"

    scene ayanecancrytoo2
    with dissolve

    ay "Yeah...I know."
    ay "I look really ugly right now and I’m sorry you have to see me like this..."
    s "Why?"
    ay "Because I shouldn't be dragging you into-"
    s "No, I mean why are you apologizing?"

    scene ayanecancrytoo1

    if bonus == True:
        ay "Well...because you're going to have sex with me."
    else:
        ay "Because we are going to do the hug thing."

    s "..."
    ay "And I...look like {i}this...{/i}"
    s "..."

    scene ayanecancrytoo2
    with dissolve

    ay "You...{i}are{/i} going to have sex with me...right?..."
    s "In this condition? Are you kidding?"
    ay "What condition? I'm fine."
    s "You're not fine, Ayane. Something is very obviously wrong. How long have you been crying? Your eyes are nearly swollen shut."

    scene ayanecancrytoo3
    with dissolve

    ay "Do we really have to do this?"
    s "Yes, we do. Talk to me."
    ay "I don’t want to."
    s "That’s not fair and you know it."
    s "You can’t just keep hiding your-"

    if bonus == True:
        ay "I’m pregnant."
    else:
        ay "I don't actually like the third season of Seinfeld."

    s "…"
    ay "…"
    s "What did you just say?..."

    if bonus == False:
        ay "I lied."
        ay "It's one of the worst seasons."
        s "..."
        ay "..."

    scene ayanecancrytoo4
    with dissolve

    ay "Just kidding~"
    ay "Hahahaha...hah..."
    ay "That...lightened up the mood a little though, right?"
    s "..."
    ay "...Sensei?"
    s "Do you really think that's funny?"

    "I feel nauseous- like my stomach is eating itself from the inside out and my heart is being pounded by a jackhammer."

    scene ayanecancrytoo5
    with dissolve

    ay "Sorry..."
    ay "I know that was kind of messed up..."
    s "Kind of? Are you kidding?"
    s "That's one of the absolute worst things that could possibly happen."
    ay "..."
    ay "Would it...really be that bad, though?..."

    if bonus == True:
        s "Would what be that bad? Getting you pregnant?"
        ay "Yeah..."
        ay "Don’t you want to be a daddy?"
        s "You haven't even finished high school yet. Listen to yourself."
        ay "I can drop out. I have money."
        ay "I think I'd make a good mom."
        ay "We could raise a baby without any problems at all..."
    else:
        s "Would what be that bad? Talking shit on the third season of Seinfeld?"
        ay "Yeah...Like what if-"
        s "Ayane, don't. It will only make things worse."

    scene ayanecancrytoo6
    with dissolve

    if bonus == True:
        ay "It'd be...a wonderful life...where neither of us would have to hide our feelings anymore."
        s "Is {i}that{/i} what this is about?"
        s "Are you really that torn up about keeping our relationship a secret? Because if this is a byproduct of that-"
        ay "No. I’m fine with keeping our relationship a secret, Sensei. I expected as much once we started getting more serious, and I have no intention of putting that in any real danger."
        ay "I’ll admit that I’d be more than happy to tell the entire world if you wanted to, but that’s not why I'm crying."
        s "Then why are you crying? I can’t help you if you won’t tell me anything."
    else:
        ay "George Costanza..."
        s "Ayane, why are you doing this?"

    scene ayanecancrytoo7
    with dissolve

    ay "Because..."
    ay "Because you’re all I have."
    ay "And yeah, I’m sure that makes me sound crazy and that you probably think I’m some sort of...psychopath who’s going to kill anyone for trying to get close to you-"
    ay "But I couldn’t care less about that."
    ay "I couldn’t care less about any of them."
    ay "I am addicted to you."

    scene ayanecancrytoo8
    with dissolve

    ay "And it’s your fault, too, you know!"
    ay "It’s your fault for being so nice to me all the time."
    ay "It's your fault that I fell in love."
    s "It’s not {i}my{/i} fault that you feel this way. Don’t try to pin this on me."

    scene ayanecancrytoo9
    with dissolve

    ay "...Huh?"
    s "That...sounded a little more harsh than I wanted it to. I didn't mean it like that."
    s "What I’m trying to say is that maybe you’ve only gotten this attached to me because you were desperate to. "
    s "Maybe you only feel this way because you think I'm ready to just accept all of the parts of you that aren't perfect."
    ay "Wait...are you...saying that you...{i}don’t{/i} accept those parts of me?..."
    s "Most of them I don't have any issue with at all. I love how chaotic and unpredictable you can be."
    s "But it’s not even remotely fair for you to just keep all of {i}this{/i} inside and then just let it out whenever it’s convenient for you."
    ay "That’s...not what I’m doing..."
    s "Then what are you doing, Ayane? Talk to me."

    scene ayanecancrytoo10
    with dissolve

    "Ayane’s eyes move away from me and navigate to the opposite side of the room."
    "It’s clear that she’s not used to being on her back foot like this, but I'm not really sure what she was expecting when she let me inside."
    "I know she’s not consciously trying to take advantage of me, but I need to show her that I’m not just some tool she can use to make herself feel whole."

    s "..."

    "I think long and hard about that last sentence in the midst of a conversational gap, but decide to break the silence on my own when I see where my thoughts are headed."

    s "Where did this all come from? It's just so...random."
    ay "What do you mean?..."
    ay "It's not like this has never happened before..."
    s "…"

    scene ayanecancrytoo11
    with dissolve

    ay "Do you remember the first time I broke down in front of you?"
    s "…"

    "Right."
    "Ayane and I go back much further than the time I’ve spent with her here."
    "There are years worth of memories stored somewhere inside of this body attempting to revolve around her only to be forced away by a foreign source of gravity."
    "None of them belong to me, and yet I wish to access them regardless."
    "Nearly all of the memories I possess are little things like play-fighting at the dojo or brainstorming names for the children we’ll never have."
    "There are some bigger ones in the mix, sure. But I can't recollect them without having to force away an erection."
    "I don’t deserve any of this."
    "But I want it regardless."
    "I want to remember what I was never there for."
    "I want to see it as if I was."

    s "..."
    ay "You don’t, do you?"
    s "..."

    scene ayanecancrytoo12
    with dissolve

    ay "It’s fine....Of course you wouldn’t remember something as silly as that."
    ay "But I remember it vividly. It was probably the moment I fell in love with you."
    s "I’d love to hear it..."

    scene ayanecancrytoo13
    with dissolve

    ay "I had just turned eleven...and my mom had moved out a few weeks earlier."
    ay "I came over to your house to play with Ami and we were watching some old gameshow on TV."

    scene ayanecancrytoo14
    with dissolve

    ay "You were cooking us dinner...or at least {i}trying{/i} to..."

    scene ayanecancrytoo15
    with dissolve

    ay "But, then..."
    ay "When you finally finished...you brought over this...{i}huge{/i} plate of super-burnt fried chicken, and I just..."
    ay "I lost it."
    ay "I started crying like a...fucking baby out of nowhere and you and Ami had no idea what to do."

    scene ayanecancrytoo16
    with dissolve

    ay "And so you put the chicken down right there on the floor...and you wrapped your arms around me..."
    ay "I can still remember how large they felt..."
    ay "And you told me...you told me that everything would be okay. And that you would always be there for me."
    ay "Then Ami started crying too because she was confused. And so she joined in and it was just this big, tight group-hug."
    ay "You never asked me any questions about {i}why{/i} I was crying, but it was because your poor attempt at making fried chicken reminded me of my mom."
    ay "And how, before we had any money, we'd eat frozen food all the time."
    ay "My mom was never good at cooking. It was always my dad’s job."

    scene ayanecancrytoo17
    with dissolve

    ay "But now?..."
    ay "My dad won’t even look at me anymore..."
    ay "And I haven’t talked to my mom in years..."
    ay "And I know I’m dumping a lot on you out of nowhere right now, but when you stand there and look at me like that, I can’t help it!"
    ay "Yes, I have friends. And yes, they’re all very nice. But no one looks after me anymore!"

    scene ayanecancrytoo18
    with dissolve

    if bonus == True:
        ay "And..."
        ay "And I’m still young!"
        ay "I still need to be looked after!"
        ay "I'm not {i}ready{/i} to do everything on my own yet!"
        ay "I can only be so strong, Sensei! I need help! I need help with all sorts of things!"
        ay "How am I supposed to keep myself together when I'm cracking a little more each day?!"
        s "…"
    else:
        ay "And...And I’m still young, but old enough to legally consent! And I do not need to be looked after, but would appreciate the sentiment!"
        s "Okay."

    "It all suddenly clicks."
    "Ayane isn’t just obsessed with me because she’s in love with me."
    "She needs a father figure in her life now that hers has left her behind."
    "She chose me."
    "And I've been too preoccupied with trying to stick my dick inside of her to realize that."
    "It all suddenly clicks."

    scene ayanecancrytoo19
    with dissolve

    ay "So...yeah. That’s why I was crying. Normal Ayane-stuff."
    ay "I just...miss you a lot."
    ay "Do you want to move into my dorm room, too? Is that allowed?"
    s "I don’t think the[school] would like that very much, Ayane."

    scene ayanecancrytoo20
    with dissolve

    ay "What if we dressed you up like a girl and made you wear baggy clothes to hide all of your muscles? Would that work?"
    s "I have a feeling that wouldn’t work either."
    ay "Ugh. Today just keeps getting worse."
    s "Would it be good enough to just keep coming here and spending time with you whenever possible?"
    ay "Good enough? No. But I'll accept it."
    ay "You should just delete all of the plans in your calendar for the next year and come here every day from now on. I kind of need you."

    "I try to smile at Ayane and forget to tell her that, in a weird way, I think I need her too."
    "Sure, I already have Ami as what I'd probably call the central figure of importance in my life, but who says I can’t have two?"
    "Ayane needs a guardian just as much as she does."
    "And even if the two of us aren’t related, I can’t just {i}not{/i} want to take care of Ayane after hearing all of that."
    "I'm a horrible person, yes. But I’m not heartless."
    "I need someone like Ayane to remind me of that from time to time."

    s "Well, I can’t guarantee I'll come every day...But, like I said, I’ll come as much as I can."

    scene ayanecancrytoo21
    with dissolve

    ay "Then...if you’re not going to come here every day, can you at least..."
    ay "Spend the night?..."
    s "Isn’t Sana going to be home any minute now?"
    ay "So? It’s just Sana. She’s not going to tell anybody."

    "I don’t think that’s really the issue here..."

    s "Ayane...I don’t know if that’s a good idea."

    scene ayanecancrytoo22
    with dissolve

    if bonus == True:
        ay "Please, [ayanemaster]? I know I'm ugly right now, but you can have sex with me under the covers if you want."
        s "I’m not going to have sex with you when you look like you’ve just come back from a funeral."
        ay "Okay, no sex. But please just sleep next to me tonight and I’ll never ask you for another favor again."
        s "I somehow doubt you'd even be able to make it through the rest of the night without asking for another favor."

        "Sana will be home soon...but I feel like leaving Ayane behind might just wind up hurting her even more..."
    else:
        ay "It is."
        s "Drat. That is a solid argument."

    "What should I do?"

    menu:
        "Spend the night":
            s "...Okay."
            s "I’ll spend the night."

            if bonus == True:
                scene ayanecancrytoo25
                with dissolve

                ay "Really?! You will?"
                s "Yes. But no [molesting] me under the blanket, got it?"
                ay "Is it really molesting if both of us enjoy it?"
                s "I am not answering that question right now."
                ay "Fine! I’ll just be the little spoon so you don’t have to worry about me trying to grab your penis while you're not paying attention."
                s "Uhh...Thank you?"

            scene black
            with dissolve2

            "………"
            "……"
            "…"

            if bonus == True:
                scene ayanecancrytoo26
                with dissolve2

                "Ayane falls asleep mere moments after getting into bed."
                "Part of me thinks about leaving while I have the chance, but I decide against it on the off chance that she wakes up in the middle of the night for another episode."
                "She really does need me right now, and I can't hold that against her."
                "And even though we’re bound to be discovered any moment-"
                "I won’t regret this decision."
                "I'm sure Sana will understand."

                scene black
                with dissolve2

                "………"
                "……"
                "…"

                play sound "dooropen.mp3"

                sa "I’m home..."

                scene ayanecancrytoo27
                with dissolve2

                sa "…"
                sa "What?..."
                sa "What...is this?..."

                scene ayanecancrytoo28
                with fade

                sa "What are you doing?..."

                "I managed to stay awake long enough for Sana to get back because I felt like not having the chance to explain this would have made it ten times worse."

                s "Sana, this is absolutely not what it looks like."
                sa "Why are you...in Ayane’s bed?..."
                s "She wasn’t feeling well."

                scene ayanecancrytoo29
                with dissolve

                sa "What?..."
                sa "What’s...wrong with her?..."
                sa "And...how does sleeping next to her fix it?..."
                sa "I’m...I’m really confused..."
                s "I don’t blame you. It’s a weird situation."
                s "She's just been feeling a little down because of...family stuff, I guess."
                sa "Oh..."

                scene ayanecancrytoo30
                with dissolve

                sa "{i}Oh...{/i}"
                sa "So you just..."
                sa "Didn’t want her to be alone..."
                s "Right."
                sa "And..."

                scene ayanecancrytoo31
                with dissolve

                sa "And...nothing else...happened?"
                s "Nothing at all."

                scene ayanecancrytoo32
                with dissolve

                sa "If...If you say so..."
                sa "I guess...this was bound to happen anyway..."
                sa "Of course you wouldn't just...leave her alone..."
                s "..."

                scene ayanecancrytoo33
                with dissolve

                sa "She looks like...she was crying a lot..."
                s "Yeah. I’ve never seen her like that before."
                sa "Poor thing...She must be exhausted..."
                s "I'm sure she is. And I'm sure you are too since you're just now getting back from work."

                scene ayanecancrytoo34
                with dissolve

                sa "I am..."
                sa "I...don't know if I'll be able to get much sleep now, though..."
                s "Just pretend I'm not here and I'm sure you'll be fine."
                sa "..."
                sa "I...don't think that will work very well..."
                s "You won't know until you try."
                sa "..."
                sa "Um..."
                sa "Can you at least...turn around so I can put on my pajamas?..."
                s "..."
                s "{i}Just pretend I'm not here and I'm sure you'll be fine.{/i}"

                scene black
                with dissolve2

                "I relutctantly keep my eyes closed while Sana gets dressed because this really isn't the time to be letting my mind wander."
                "Keeping my eyes open would also trigger a chain of events that would not be very ideal right now in my current role as the big spoon."
                "..."
                "What?"
                "I’m only human."
                "It’s impossible to avoid thoughts like this- the same way it’s impossible to avoid things like loneliness or fear."
                "We all bear witness to life's littlest atrocities. And sometimes, we may feel the need to lean on someone else for help."
                "So whether it be missing your family-"
                "Or feeling unwanted-"
                "Or falling in love with a best friend’s uncle-"
                "There is always a tomorrow."
                "Just sometimes-"
                "It’s a little harder to get there."

            $ renpy.end_replay()
            $ ayane_love += 5
            $ ayanesleepover = True
            $ ayanedorm20 = True
            stop music fadeout 5.0

            "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
            "........."
            "......"
            "..."

            $ totaldays += 1
            $ day += 1
            if day == 7:
                hide saturday onlayer date
                show sunday onlayer date
            else:
                "ERROR ADVANCING TO SUNDAY"

            "{i}[totaldays] Days have passed...{/i}"

            scene room2
            with dissolve2

            "Ayane and Sana are both gone when I wake up."
            "There is a letter next to the bed that just says 'Thank you.'"
            "..."
            "I guess I should figure out what I want to do today."

            menu:
                "Go somewhere":
                    "Where should I go?"
                    menu:
                        "Koi Cafe":
                            jump cafe
                        "Library":
                            jump library
                        "Soccer field":
                            if soccer20 == True:
                                "Who do I want to spend time with?"
                                menu:
                                    "Miku":
                                        jump soccerfield
                                    "Karin":
                                        jump soccerfieldkarin
                                    "Kirin":
                                        jump soccerfieldkirin
                            else:
                                jump soccerfield
                        "Ami's Room":
                            jump amisroom
                        "=D" if swimming == True:
                            jump swimming

        "Go home":
            s "I’m sorry, Ayane...But I really should get going."

            scene ayanecancrytoo23
            with dissolve

            ay "Really?...Even when I promised to be good?"

            if bonus == True:
                s "It doesn’t have anything to do with you being good or not. I just can’t let another student see me sleeping in a bed with you."
                ay "Well...what if you slept on the floor? Would that be okay?"
                ay "Wait, no! What if {i}I{/i} slept on the floor? You’d stay then, right?"
                s "Ayane...I’m not going to make you sleep on the floor of your own room."
                ay "Can I...at least talk to you on the phone while you walk home? I don’t want you to leave yet. I’m still sad."
                s "If that's what you want, sure."
                s "You can call me whenever you want."

                scene ayanecancrytoo24
                with dissolve

                ay "That's not true. If I called you whenever I wanted, you’d never be able to put down the phone."
                s "Fair. You can definitely call me tonight, though."

                scene ayanecancrytoo22

                ay "Okay...Then...I’ll call you as soon as you leave."
                s "Works for me. And sorry I couldn’t spend the night tonight. But maybe some other time."
                ay "Yeah..."
                ay "Maybe some other time."
                ay "I love you, [ayanemaster]. You don’t have to say it back."
            else:
                s "This is inappropriate and I will not be lured in by your siren song."
                ay "Sensei nooooooooooooooooooooo!"

            scene black
            with dissolve2

            "I walk up to Ayane to say goodbye and she wraps her arms around me, but doesn’t squeeze with the same amount of enthusiasm she normally does."

            play sound "dooropen.mp3"
            "…"

            "I leave the room and receive a phone call before I even get back to the street."
            "Ayane falls asleep mid-conversation less than five minutes later."
            "It never ceases to amaze me how tired you can get from crying."

            $ renpy.end_replay()
            $ ayane_love += 1
            $ ayanedorm20 = True
            $ ayanesleepover = False
            stop music fadeout 5.0

            "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label sanadorm25:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ayane_love >= 5 and ayanedorm5 == False:
                jump ayanedorm5
            if ayane_love >= 15 and ayanedorm10 == True and ayanedorm15 == False:
                jump ayanedorm15
            if ayane_love >= 20 and dojo20 == True and ayanedorm10 == True and sanadorm15 == True and day == 6 and ayanedorm20 == False:
                jump ayanedorm20
...
```