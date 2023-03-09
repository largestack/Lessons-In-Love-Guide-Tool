# Normal Office Visit
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day56&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 56

✅Event "[Maya: Different Worlds](./shrine5.md)" is completed (event=shrine5)



## Next events
* [Ami: Ode to a Marsh Warbler](./aminew2.md)

## Event properties
* ID: day56
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day56:
    scene mayaoffice0
    with dissolve
    play music "phantomthief.mp3" fadein 3.0

    "And so begins another lonely day in the office."
    "Upon thinking more about it, this whole ‘guidance counselor’ thing doesn’t really make sense to me, to be honest."
    "Most days, I just find myself sitting here for an hour or two before calling it quits and going home."
    "Sure, there are rare occasions where someone will actually stop by...but I think only {i}one{/i} of those occasions has actually involved counseling so far."
    "Two, maybe- if you count being blown off by Yumi as counseling. Which I do not."

    play sound "knock.mp3"

    "…"

    if bonus == True:
        "Welp, it looks like someone else is here to take advantage of both my office hours and a position I am absolutely not qualified for."
    else:
        "=D"

    s "Come in."

    play sound "dooropen.mp3"
    show mayaoffice1
    with dissolve

    s "..."

    "And...it looks like it's someone entirely unexpected."

    if bonus == True:
        s "Huh..."
        m "What do you mean “Huh?” Am I not allowed to use this office for the same unintended purposes everyone else uses it for?"
        s "That depends on whether or not you are here for a shoulder massage."

        scene mayaoffice1r
        with dissolve

        m "What? Ew. No."
        m "Is that seriously what you've been using this place for?"
        s "...No."
        m "You're disgusting..."
    else:
        m "Yo."

    s "So, what brings you here today, Maya?"
    s "It’s not often you actually come to see me. In fact, I’m pretty sure that this is the first time this has ever happened."

    scene mayaoffice1
    with dissolve

    m "That is correct. And don't take my arrival here as some sort of omen for things to come. I would like to clarify first and foremost that I absolutely do not want to be here right now."
    s "Well, that's a good start to this conversation."
    m "The fact of the matter is, if I {i}didn’t{/i} remind you of something soon, horrible things would likely follow."
    s "That’s...ominous."
    m "What is truly ominous is your existence and all of the horrible things that occur because of it."
    m "So, how is this new world treating you?"
    s "You mean the world that I have been in forever?"
    m "No. I mean the one that you continuously deny that you’ve been reborn into even though we both know that is not the case."
    s "I'm just going to assume you mean the world I've been in forever- which has been pretty good so far, I guess."
    m "Nothing strange has happened?"

    if roomwithtrack == True:
        s "Well...I wouldn’t say that."

        scene mayaoffice2
        with dissolve

        m "Please clarify."
        s "Well, I think I’ve been having some strange dreams lately."
        m "You think?"
        s "Well...they {i}feel{/i} like dreams, But I’m not really sure if that's what they are or not."
        m "Dreams of what, exactly?"
        s "That...is kind of hard to explain."
        m "Can you try? I'm actually curious now."
        s "Well, I am completely aware of how insane this will make me sound...but do you know anything about a...sort of..."
        s "Room with clocks?"

        scene mayaoffice1
        with dissolve

        m "There are many rooms with clocks in them. I’m not sure which one you’re talking about."
        s "No, like...one room with way too many clocks."
        m "…"
        s "…"

        scene mayaoffice3
        with dissolve

        m "Were they like...different kinds of clocks or something?..."
        m "Because I'm really confused about why something that unremarkable would be the first thing you go to in order to quantify how strange this world is."
        s "There was other stuff that happened in the dream. It's all...blurry for the most part. But I remember seeing someone who looked {i}a lot{/i} like you there."

        scene mayaoffice4
        with dissolve

        m "Oh. Wonderful. So it was {i}that{/i} type of dream."

        if bonus == True:
            s "It really wasn't. In fact, I will confirm right now that I didn't even {i}touch{/i} dream-Maya."
            m "Do you...want a medal for that or something?"
            s "No. But some acknowledgement that I'm not as bad as you say I am would be nice."
            m "Are you forgetting the part roughly one minute ago where you admitted to molesting a girl in this very office?"
            s "Massage. Not molest."
            m "Sorry, how old are you again?"
            s "I honestly don't know."
            m "Then I will answer for you- old enough for there to be no difference between {i}massage{/i} and {i}molest.{/i} Now, can we please get back to the aspects of your dream that don't involve touching me?"

            "There is no winning with this girl."

            s "Fine. What else do you want to know?"
        else:
            s "Hug her? Absolutely not. I am a very polite boy in my dreams."

        scene mayaoffice1
        with dissolve

        m "To start, are there any other important details you remember about this dream? Or was it just...clocks and me?"
        s "The thing is I don't even know if it {i}was{/i} you. She was identical, but I...remember her acting very...different from how you typically act."
        m "How depressing that you must resort to dreams of me being nice to you since it will never happen in real life."
        s "Okay, you know what? I don't think I'm going to talk about that dream anymore since it was clearly just some...ridiculous and random REM-induced brain voyage."
        m "That's probably a good call. But that aside, has anything {i}else{/i} strange happened?"

        if letterttrack == True:
            s "One more thing. But it's going to make me sound strange again."
            m "I can assure you I am quite used to that by now."
            s "Then...how do you feel about the letter T?"
            m "..."
            s "..."

            scene mayaoffice3
            with dissolve

            m "What?"
            s "Told you."
            m "What does the letter T have to do with anything? Is that...some sort of code?"
            s "No. Well, at least I don’t think it is."
            s "I’m not really sure."
            s "I just vaguely remember something about that letter recently. But I feel like it's...a memory I'm not really supposed to have? Does that make any sense?"
            m "Not really..."
            m "Besides, what relevancy would that have to me? Asking me how I feel implies that I have something to do with this, doesn't it?"
            s "Dream-Maya was there again."
            m "Is she just in all of your dreams now? Because that is quite sickening and does not make me feel very safe."
            s "I wouldn’t worry too much about it...It's probably just more meaningless brain vomit."

            scene mayaoffice4
            with dissolve

            m "I sincerely hope that is true for the sake of both of us."
            m "So, did anything else happen? Or is that it?"

    s "Uhh...No? I don’t think so at least?"
    s "What about with you? We’re in the counseling room. So if you have any issues, this is the best place to air them out."

    scene mayaoffice3
    with dissolve

    m "Yeah...I can promise you that if I {i}did{/i} have any issues, you’d be one of the last people I'd go to for help."
    s "{i}One of?{/i} So I’m not in last place?"

    scene mayaoffice1
    with dissolve

    m "Second to last. I wouldn’t celebrate just yet."
    s "Well...who is last then?"
    m "That would have to be God."
    s "Aren’t you a shrine maiden?"
    m "Only because I have to be."
    s "You...{i}have{/i} to be a shrine maiden?"
    m "It's very complicated. You wouldn't understand."
    s "Then I think you’re going to have to tell me more about it."
    m "Please don’t tell me what I {i}have{/i} to do. That sort of methodology might work on Ami and Ayane, but not me."
    s "I didn’t mean that you literally {i}have{/i} to...I’m just curious."
    m "Well, I am very sorry, but this is one of many cases in life where you'll just have to remain curious."

    scene mayaoffice4r
    with dissolve

    m "For now, though...let me get to the real reason I’m here."
    s "Oh, right. You said you wanted to remind me of something, correct?"
    m "Correct, but before I remind you, there is something I would like to ask. And I’d appreciate it if you would answer as honestly as possible."
    s "Oh...uhh, sure. What’s up?"

    scene mayaoffice1
    with dissolve

    m "Are you happy here?"
    s "You mean...Kumon-mi?"
    m "More or less."

    "Why exactly would Maya care about something as trivial as my happiness?"
    "This isn't some sort of trick question, is it?"

    s "..."
    m "..."

    "Regardless...she {i}did{/i} ask me to answer as honestly as possible..."
    "So..."

    menu:
        "I am happy here":
            s "I guess so. Kumon-mi is pretty nice."

            if bonus == True:
                s "Plus, this is probably the closest I’ll ever get to having a harem, so that's a plus."

                scene mayaoffice3
                with dissolve

                m "And there you go immediately ruining everything."
                m "Do you really think you’ll be able to romance {i}everyone{/i} without some form of consequence?"
                s "If I am very careful? Probably."

                scene mayaoffice4
                with dissolve

                m "Well...I have no intention of trying to stop you."
                m "Just know that I think you're absolutely disgusting and would be better off locked up in some room far, far away from teenage girls for the rest of your life."
                s "If that ever happens, will you at least come by to feed me every now and then?"
                m "No. I will leave you there to starve."
                s "I'd say something like “Remind me to not get on your bad side,” but I'm pretty sure I've been there from the start, so..."
            else:
                m "Cool. Just wanted to make sure."

        "{s}I am miserable{/s} {b}INCORRECT ANSWER. IGNORE ME.{/b}":
            stop music
            play music "sweetvermouth.mp3"
            play sound "static.mp3"
            scene happy1 with flash
            scene helpme with flash
            scene happy2 with flash
            scene helpme with flash
            scene happy3 with flash
            scene helpme with flash
            scene happy4 with flash
            scene helpme with flash
            scene happy5 with flash
            scene helpme with flash
            scene happy6 with flash
            scene helpme with flash
            scene happy7 with flash
            scene helpme with flash
            scene happy8 with flash
            scene helpme with flash
            scene happy9 with flash
            scene mayaoffice5 with flash
            stop sound

            s "I feel great!"
            m "{b}YOU WOULD FEEL BETTER INSIDE OF ME.{/b}"

            play sound "static.mp3"
            scene 2 with flash
            scene helpme with flash
            scene 3 with flash
            scene helpme with flash
            scene 2 with flash
            scene helpme with flash
            scene 3 with flash
            scene mayaoffice5r with flash
            stop sound
            $ renpy.pause(10, hard=True)
            play sound "static.mp3"
            scene happy3
            with flash
            stop sound
            stop music
            scene mayaoffice1
            play music "phantomthief.mp3"

            m "I see."
            m "Well that’s good at least."
            s "It sure is."

    scene mayaoffice4r
    with dissolve

    m "Well, now that that’s out of the way, I guess I’ll cut to the chase."
    m "Something important is going to happen with Ami soon."
    s "Important? What do you mean?"
    m "I mean that something she cares very much about is going to happen soon."
    m "And it’s something {i}you{/i} care about too."
    s "Do you mean me? Or {i}me{/i}?"
    m "It doesn’t make a difference. I dislike both versions of you equally."
    s "That's unfortunate. I was just starting to think we were friends."

    scene mayaoffice6
    with dissolve

    m "Quit joking around for a moment...I’m serious."
    m "If you so much as even {i}upset{/i} Ami, I swear on everything in this world that I will destroy you."
    s "That's fine. It's not like I'm actively trying to hurt her or anything. But...what’s this allegedly important thing that's going to happen?"
    s "How can I be prepared for it if I don't know what it is?"

    scene mayaoffice4
    with dissolve
    stop music fadeout 10.0

    m "You’ll know when the time comes."
    s "How can you be so sure of that?"
    m "I just am."
    m "Now, if you’ll excuse me...I would like to go eat pizza with my friends."
    s "Oh. Uhh...sure. You’re-"
    m "Thank you and goodbye."

    play sound "dooropen.mp3"
    scene black
    with dissolve

    m "Oh...and one more thing."

    "Maya calls out to me from the hall before closing the door."

    m "Not everything is always as it seems."
    m "I'd ask that you remember that."
    s "…"

    "Maya closes the door and I’m left confused and alone."
    "As such, I decide to pack up and leave the office a little early today."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ day56 = True

    jump afterschoolevent

label day60:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
...
```