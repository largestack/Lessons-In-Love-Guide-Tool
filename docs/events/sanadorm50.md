# Mine (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 50

* Event [The Complete Absence of Everything](./sanadorm45.md) (Sana) is completed)

* Event [Sweet Vermouth](./bar45.md) (Sana) is completed)



## Next events

* [Sana: Melatonin](./bar50.md)
* [Main: Good Morning](./secondbeach1.md)

## Event properties

* Id: sanadorm50
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm
* Triggered by path: sanadorm->sanadorm50

## Official wiki page

[Mine](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm50&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanadorm50:
    play sound "knock.mp3"

    "I knock on Sana’s door and wait for her to answer. "
    "I can hear what sounds like loud gunfire from inside of the room so either Sana is playing a video game or in grave danger right now."

    play sound "knock.mp3"

    "I knock again to confirm that Sana is not involved in a real gunfight."

    sa "One...second..."

    "The gunfire ceases after several seconds and Sana either pauses her game or dies."
    "I guess I won’t know the real answer until she lets me in."
    "Which she wouldn’t be able to do if she was dead."

    sa "Okay...you can come in now..."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    stop music fadeout 10.0

    "As it turns out, Sana has either won the gunfight or-"
    "Actually, for the sake of moving things along, I’m going to assume there was no gunfight at all and that it really was just a video game."
    "Some might say this is a fair assumption considering Sana has been known to waste away her time with those."
    "However, that doesn’t mean she isn’t secretly hiding an alternate life as a criminal or something along those lines."
    "In fact, there are countless situations where people will go on killing sprees only to have all of the people who knew them while they {i}weren’t{/i} killing people proclaim how normal said killer was."
    "I could very well be one of those people."
    "The normal ones, I mean."
    "I’d never hurt a fly."

    scene sanasnotacyclops1
    with dissolve2
    play music "love.mp3"

    sa "Um...hey..."
    s "…"

    "It appears that there may have been a gunfight after all, as Sana is nowhere to be found."

    s "Sorry. I think I have the wrong room."
    sa "Because my hair isn’t covering my eyes?..."
    s "...Sana?"
    sa "Sensei...you’ve seen me like this before..."
    sa "Your...fake surprise is getting a little old."
    s "It’s not fake. I was actually just inner monologuing about how you lost in a gunfight."

    scene sanasnotacyclops2
    with dissolve

    sa "Gunfight?..."
    sa "Oh, you must be talking about the game I was playing."

    scene sanasnotacyclops3
    with dissolve

    sa "I’m...still not great at games like that...so I was spending the night practicing so...I don’t look really bad the next time I play with Rin..."
    s "Well I’m glad to see that you’re trying to improve yourself in ways beyond just speaking, but I think there might be better areas to improve in than how well you can shoot virtual stuff."

    scene sanasnotacyclops4
    with dissolve

    sa "Probably. But...I don’t think I’d have as much fun using my free time on things like that..."
    sa "Besides, for all you know...you could really like stuff like that too, Sensei."
    sa "What if...you’re secretly really good at shooters and you just...don’t know it yet?"
    s "That’s not even something I’d {i}want{/i} to be good at."
    sa "Why not? Don’t you want to impress girls?"
    s "Since when is that a thing girls are impressed by?"
    sa "I know {i}I’d{/i} be impressed. Rin too."
    sa "And Molly. And probably even Ami and Ayane."
    sa "Though...I don’t think it’s really possible for you to be any cooler in their books than you already are."
    sa "But...what I’m saying is...that it’s nice finding people who are...good at the things you’re interested in..."

    scene sanasnotacyclops5
    with dissolve

    sa "And...also that I could maybe use someone to practice against since...the AI in this game isn’t very good..."
    s "Ahh. So it was all just one big ploy to get me to play with you. "

    scene sanasnotacyclops6
    with dissolve

    sa "Maybe."
    s "Are you actually winking at me right now?"

    scene sanasnotacyclops7
    with dissolve

    sa "I’ve winked at you before, too...you just weren’t able to see it."
    s "You know, I’ve been fortunate...or {i}unfortunate{/i} based on how you look at things a very fair amount of times over the last...school year-"
    s "But I think that this plot twist might be the most surprising one yet."
    sa "Heheh...yeah..."
    sa "It’s kind of hard to believe with how I started out...huh?"
    s "I mean, you’re not {i}that{/i} different from how you started out."
    s "You just talk a little more and have an extra eye now."

    scene sanasnotacyclops8
    with dissolve

    sa "Just...for tonight..."
    sa "I still like my hair better the other way...I just...also know it can be a bit of a handicap for games that require your full attention."

    scene sanasnotacyclops9
    with dissolve

    sa "But...yeah..."
    sa "I’m...definitely not the same person I was when we met all that..."

    scene sanasnotacyclops10
    with dissolve

    sa "...time ago?"
    s "…"
    sa "How..."
    sa "How long have we known each other again?..."
    sa "Because...the[school] year isn’t even halfway over and..."
    s "…"
    sa "…"

    "I pause for a moment to see where this train of thought takes Sana."
    "Of course, for me, it’s been much longer than just half a[school] year."
    "Counting the other iterations of myself (Which apparently sucked even more than me for the most part), {i}I’ve{/i} likely gone through this hundreds, if not thousands of times."
    "How interesting would things be if someone like her caught onto what’s happening as well?"
    "That it’s been longer than half a[school] year."
    "That we’ve crammed three nearly full ones into the space of one and, if things go according to plan, are going to cram many, many more."
    "…"
    "I say, as if I actually have a plan."
    "If I had a plan, I wouldn’t be simply waiting to see where the train stops."
    "I’d be helping her get on board or...selling her a ticket or..."
    "Doing anything but watching."
    "Watching and waiting for her to uncover the secrets of the universe while both myself and Maya have no idea what those secrets even are."
    "I think."
    "Frankly, she might know and is just deciding against telling me about it."

    sa "…"
    s "…"
    sa "…"
    s "…"
    sa "…"
    s "…"

    play sound "static.mp3"
    scene sanasnotacyclops11 with flash
    stop sound

    sa "It’s funny how time can slip away from us, isn’t it?"
    s "Yeah. It’s almost like-"

    scene sanasnotacyclops12
    with dissolve

    s "...huh?"
    sa "It’s almost like one minute...you’re doing one thing...and the next minute...you...don’t even remember what that thing was."
    s "…"

    "How long have we been playing this for?"
    "And, better question, how did Sana manage to convince me to play a video game in the first place?"

    scene sanasnotacyclops13
    with dissolve

    s "…"
    sa "…"
    sa "What?"
    sa "Are you...upset at me for...killing you so many times?"
    s "Not really. "
    s "I just think I’m feeling the effects of that whole “time slipping away” thing as we speak."
    sa "That tends to happen to me when I play games as well..."
    sa "But it’s not like it doesn’t happen in...different ways, too."
    s "Is this you admitting that you’re finally in love with me?"

    scene sanasnotacyclops14
    with dissolve

    sa "Wh...What?...No...of course not...."
    sa "It’s true that we’re...a lot closer now than before, but...it’s not anything like that...."
    s "I know that. I was just messing around."

    "Damn it."

    s "Though, it’s hard to ever really recall a time where we’ve been this close before."

    scene sanasnotacyclops15
    with dissolve

    sa "That’s...closer to what I was getting at..."
    sa "When we first met {s}so, so long ago{/s} at the beginning of the[school] year, I never would have imagined...sitting on my bed in the dark with you..."
    sa "But now...I can do it without even feeling a little uncomfortable..."
    s "You should feel at least {i}slightly{/i} uncomfortable, I think."

    scene sanasnotacyclops16
    with dissolve

    sa "Why is that?"
    sa "Because you’re my teacher and I’m your student?"

    if bonus == True:
        s "That’s a very roundabout way of putting it and doesn’t really touch on the dramatic disparity between our ages and sizes."
    else:
        s "And you are also a health inspector."

    sa "Aren’t we friends before that, though?"
    sa "Doesn’t that take priority?"

    "I try my best to play whatever game the two of us are playing, but...as expected, I’m not very good."
    "I {i}am{/i} doing much better than I imagined I would with zero experience, though."
    "And...I’m already somehow familiar with what all of the buttons do."
    "Kind of like I’m coasting off of muscle memory despite a complete lack of {i}mental{/i} memory."

    s "I guess the whole friendship thing takes priority."
    s "I mean, it doesn’t really matter to me either way."
    s "To be completely honest, I don’t really view {i}any{/i} of you girls as friends."

    scene sanasnotacyclops17
    with dissolve

    sa "You...don’t?"
    s "Not really. No."
    sa "…"
    sa "Then...what do you view us as?..."
    s "Hm."
    s "That’s a complicated question."
    sa "I don’t mind if there’s a...complicated answer..."
    s "What about an answer so simple that it just {i}seems{/i} complicated?"
    sa "I...don’t know..."
    sa "I just...really thought we were friends...this whole time..."
    s "I’m going to kill you if you don’t pay attention."

    scene sanasnotacyclops18
    with dissolve

    sa "What?!"
    s "In the game."

    scene sanasnotacyclops19
    with dissolve

    sa "O-Oh...yeah...sorry..."
    s "There’s not really any one word I’d use to describe the relationship I have with all of you girls."
    s "You’re not friends or lovers or family or any other blanket term I can just toss all of you under."
    s "I treat every one of you differently and wouldn’t feel right simply calling you one thing or another."

    if bonus == True:
        s "We can be friendly and not be friends. Just like we can be intimate and not be lovers."
    else:
        s "We can be friendly and not be friends. Just like we can be on a water polo team together and not know how to swim."
        sa "..."

    sa "I...don’t really want-"
    s "But at the end of the day, I’m just me and you’re just you. And Ayane is just Ayane and Ami is just Ami."
    s "Labels are dumb."
    sa "…"
    sa "So...am I still allowed to call you my friend?"
    s "Call me whatever you want. I don’t care."
    s "Just don’t ask me how I see you, because it’s not a question that’s easy for me to answer."

    scene sanasnotacyclops20
    with dissolve

    sa "That’s fine..."
    sa "There are plenty of questions I find hard to answer, after all...and you’ve never pushed me to actually answer any of them..."
    s "That’s because your life is your life and your secrets are your secrets."
    s "I don’t need to know things you don’t want me to know."

    scene sanasnotacyclops21
    with dissolve

    s "But in the event that you ever want to tell me-"
    sa "…"
    s "…"
    s "What?"
    sa "…"
    s "Sana?"

    scene sanasnotacyclops22
    with dissolve

    sa "It’s been several years since my brother died now."
    sa "But, somehow, it feels a lot longer."
    sa "I keep a lock of his hair in a box on the table behind you."
    sa "My mom has one too. "
    sa "She used to smell it before going to bed every night...and then cry into her pillow thinking I couldn’t hear her from down the hall."
    sa "I did."
    sa "I always did."
    sa "And for a long time, that would make me cry too."
    sa "But now, I can barely even open the box anymore because it just reminds me of what actually happened to him."
    s "…"
    sa "…"
    sa "You should ask me what happened to him."
    s "What are you-"
    sa "Making my secrets your secrets."
    sa "Telling you the things I want you to know before I change my mind and don’t want you to know them."
    sa "I don’t want to just be {i}Sana{/i} to you anymore."
    sa "I want to be your friend."
    sa "Having you just see me as {i}me{/i}...isn't enough to make me feel the way I want to feel."
    s "I don’t really know how you want to feel, but I can’t just ask you what happened when-"

    scene sanasnotacyclops23
    with dissolve

    sa "I'll just tell you, then."
    sa "He was killed."
    sa "Stabbed to death on his way home from a friend’s house one night."
    sa "He was younger than I am now when it happened."
    sa "We never even found out who did it."
    sa "Now...{i}that’s{/i} what I think of every time I open the box."
    sa "That time...really does slip away faster than we expect it to..."
    sa "But no amount of time can fix certain things once they break beyond recognition."
    sa "So you’re forced to let it slip even more."

    scene sanasnotacyclops24
    with dissolve

    s "…"
    sa "He used to play games like this, you know. The same way we are now."
    sa "And whenever he got me to play with him, he’d always take it easy on me."
    sa "So...I’ve been taking it easy on you tonight. Trying to set the example he made for me."
    sa "But..."
    sa "I’m still going to kill you if you don’t pay attention."
    s "…"
    sa "…"

    scene sanasnotacyclops25
    with dissolve

    "I do what I do best and ignore it all."
    "But, in my defense, that’s what anyone would do in this situation."
    "Isn’t it?"
    "Who picks a time like this to come out and admit something as tragic as that?"
    "I guess it’s possible that she’s been wanting me to ask for a while..."
    "And I guess it’s also possible that she was desperate for me to know this side of her."
    "Because, as she said, she {i}wants{/i} to be seen as something more than just herself."
    "But to think that none of this would have happened if I’d just given her what she wanted from the start instead of being desperate to hear the sound of my own voice."
    "She’s crying because of me."

    s "…"
    sa "…"

    "No. "
    "She’s not crying because of me."
    "She’s crying because she’s subjected herself to a barrage of unhappy memories in exchange for momentary sympathy and a need to be {i}seen.{/i}"
    "But I already saw her."
    "And I’ll continue to see her each and every day."
    "I just happen to know a little more now."
    "I know a little more about a thing I didn’t want to know in the first place."
    "And now {i}I{/i} have to adapt."

    s "Thank you for telling me that."

    "And I thank her anyway."
    "Why?"
    "Why must my mouth once again betray the device that directs it?"

    if bonus == True:
        "Why must I act in opposition to myself when all I {i}really{/i} want is to remove her clothes and help her forget the only way I know how?"

    scene black

    "Everything goes dark."
    "For you, at least."
    "I can still see everything."
    "I just don’t want you to see anymore."
    "Not until the two of us return to normal."
    "Not until what is hers is no longer mine."

    "{i}You sit in silence and kill each other for the next hour!{/i}"

    $ renpy.end_replay()
    $ sana_love += 1
    $ sanadorm50 = True
    stop music fadeout 10.0

    if sarasex == False:
        $ bar50miss = True

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

                    ############################################
                    ##########        ROOM 3          ##########
                    ############################################

label makotodorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if makoto_love >= 5 and firsttimepornshop == True and makotofirsthall == True and makotodorm5 == False:
                jump makotodorm5
            if makoto_love >= 20 and day != 2 and makidate1 == True and pornshop20 == True and makotodorm20 == False:
                jump makotodorm20
            if makoto_love >= 25 and makotofirsthall == True and pornshop25 == True and trinity3track == True and mikudorm30 == True and makotodorm25 == False:
                jump makotodorm25
            if makotodorm25 == True and hoorayanotherreset == False:
                play sound "knock.mp3"

                s "Hey Makoto, are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            else:
                jump makotodormgen
        "Handjob" if makotonew3 == True and bonus == True:
            if makotodorm25 == True and hoorayanotherreset == False:
                play sound "knock.mp3"

                s "Hey Makoto, are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            else:
                jump makotohjreplay
        "Have Sex (Missionary)" if pornshop20 == True and bonus == True:
            if makotodorm25 == True and hoorayanotherreset == False:
                play sound "knock.mp3"

                s "Hey Makoto, are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            else:
                jump makotomissreplay

label mikudorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if miku_love >= 5 and firsttimesoccerfield == True and mikudorm5 == False:
                jump mikudorm5
            if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
                jump mikudorm10
            if miku_love >= 15 and mikudorm10 == True and mikudorm15 == False:
                jump mikudorm15
            if miku_love >= 25 and soccer25 == True and mikudorm25 == False:
                jump mikudorm25
            if miku_love >= 30 and soccer30 == True and day != 4 and trinity3track == True and mikudorm30 == False:
                jump mikudorm30
            if miku_love >= 35 and makotowinterbeach4 == True and day != 4 and mikudorm35 == False:
                jump mikudorm35
            if miku_love >= 35 and mikudorm35 == True and day != 4 and mikudorm40 == False:
                jump mikudorm40
            if miku_love >= 45 and christmastwo20 == True and day != 4 and mikudorm45 == False:
                jump mikudorm45
            else:
                jump mikudormgen
        "Fingering" if mikudorm50 == True:
                jump mikudormfingeranim

label makotodormgen:
    play sound "knock.mp3"

    s "Hey, Makoto. Are you free right now?"
    mak "Sensei? Of course. Come on in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

    scene makotodormgen
    with dissolve

    "Makoto invites me in and tries to lecture me on the importance of whatever weird subject she's studying tonight."

    if bonus == True:
        "I get fed up after several minutes and wind up telling her that I won't recommend her to a good[school] unless she chills out."
        "She obliges and we get on to talking about work and how stressed she is having to balance[school] with...porn."
        "It sounds weird to say it like that, but it's clear to see that she actually is getting a little run-down as the days go by."
    else:
        "I swear, sometimes it's like this girl doesn't realize {i}I{/i} am the teacher. I should be lecturing {i}her.{/i}"

    scene black
    with dissolve

    "Eventually, it comes time for me to go as she has yet another late shift at her parents' shop."
    "I walk her to the bus stop and the two of us say our goodbyes."
    "I really do hope that she's able to find time to relax soon..."

    $ makoto_love += 1
    stop music fadeout 3.0

    "{i}Makoto's affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikudormgen:
    play sound "knock.mp3"

    s "Hey, Miku. What are you doing right now?"
    mi "A whole lotta nothin'! Come talk to me about stuff!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

    scene mikudormgen
    with dissolve

    "Miku lets me into the room and the two of us proceed to 'talk about stuff.'"
    if chapthree8 == False:
        "We go through the usual routine of her rambling on about soccer and other drama that has been going on with the team while I..."
    else:
        "We go through the usual routine of her rambling on about swimming and other drama that has been going on with the team while I..."

    "Well, I just do my best to keep up...which is a lot harder than you might expect."
    "Miku is like a ball of lightning constantly ricocheting off of everything in its path."
    "And don't get me wrong, I like being a lightning rod just as much as any guy would, but-"
    "Well, let's just say I wouldn't mind if she slowed down every once in a while."

    scene black
    with dissolve

    "We wind up playing some card game that Miku made up for a couple hours until Makoto tells her she's on the way home."
    "Strange...it feels like I just got here. It's crazy how quickly time flies when I'm with Miku."
    "But, yet again, it might just be that time is trying to catch up to her..."

    $ miku_love += 1
    stop music fadeout 3.0

    "{i}Miku's affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotodorm5:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
    if sana_love >= 15 and sanadorm15 == False:
        jump sanadorm15
    if sana_love >= 20 and bar20 == True and sanadorm20 == False:
        jump sanadorm20
    if sana_love >= 25 and bar25 == True and beachvacation16 == True and sanadorm25 == False:
        jump sanadorm25
    if sana_love >= 30 and bar30 == True and day != 4 and sanadorm30 == False:
        jump sanadorm30
    if sana_love >= 35 and bar35 == True and day != 4 and sanadorm35 == False:
        jump sanadorm35
    if sana_love >= 45 and thirdreset3 == True and day != 4 and sanadorm45 == False:
        jump sanadorm45
    if sana_love >= 50 and sanadorm45 == True and bar45 == True and sanadorm50 == False:
        jump sanadorm50
...
```