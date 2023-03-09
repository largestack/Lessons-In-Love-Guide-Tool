# Parasite
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day83&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 83

✅Event "[Miku: You and Me and the Night](./mikudorm10.md)" is completed (event=mikudorm10)



## Next events
* [Miku: Hormones Running Wild](./soccer15.md)

## Event properties
* ID: day83
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day83:
    scene kirinoff0
    with dissolve
    play music "phantomthief.mp3"

    "And so another boring shift of sitting in the office and waiting for someone to show up begins."
    "Most of the girls have either gone home or headed elsewhere to study
    by now, but I’m still obligated to hang around in the event that {i}one{/i} of them didn’t."
    "Honestly, it’s a pain."
    "I get that people have problems and all that, but I really wish they’d
    have them at more convenient times of the day."
    "I don’t want to stay here any longer than they have to. I have...stuff to do."
    "But..."
    "I guess that “stuff” is just hanging around [teenage]girls anyway so, as long as someone
    actually shows up, I guess it doesn’t make much of a difference."
    "Of course, that isn’t always the case, though..."

    play sound "knock.mp3"

    q "Helloooo? Anyone in there?"

    "Huh...That’s not a voice I recognize."
    "Maybe it’s a girl from one of the other classes looking for her teacher?"
    "Or, better yet, maybe it's a cute new transfer student who’s gotten lost and is looking for someone to guide her around the campus?"

    q "Huh...Guess no one is here after all."
    s "Wait, no. I’m here. You can come in."

    "I call out to who I hope is a transfer student and wait for her to enter the room."

    play sound "dooropen.mp3"

    "…"

    scene kirinoff1
    with dissolve

    ki "Hiya~ Nice office you’ve got here, Sensei."
    s "...Karin?"

    "Or...at least that’s what I think her name is?"
    "I know she’s one of the girls on Miku’s soccer team but it’s not like I had
    the best opportunity to actually {i}talk{/i} to her last time we were near each other."

    scene kirinoff2
    with dissolve

    ki "Uhh, no...I’m Kirin. Karin is my older sister."

    scene kirinoff3
    with dissolve

    ki "But...I guess I can let you off the hook since this is our first time actually talking."
    ki "Our names are pretty close anyway, so it’s whatever."
    s "Right, right. Well, I’m sorry either way. It won’t happen again."

    scene kirinoff1
    with dissolve

    ki "Good. I’m going to hold you to that."
    s "So, {i}Kirin{/i}, what brings you here today?"

    scene kirinoff4
    with dissolve

    ki "Hmm...I don’t know. Boredom, I guess?"

    scene kirinoff5
    with dissolve

    ki "I’ve never been in any of the counseling offices before, and my teacher is kind of a bitch sooo...I figured I’d come visit yours."
    ki "That’s okay, right? It doesn’t look like you’re doing anything."
    s "What do you mean? I’m clearly very busy."
    ki "Yes, yes. Of course you are. I can tell how much of a burden my presence must be, but I humbly ask you to let me hang out here for a little while."
    s "I mean, I’m fine with it, but why {i}here{/i}? Don’t you need to be studying or something?"
    ki "Studying is boring. I want to do something fun."
    s "Normally people don’t come to the counseling room in search of fun."

    scene kirinoff6
    with dissolve

    if bonus == True:
        ki "Really? Cause I could have sworn I heard these weird moaning sounds the last few times I’ve walked by."
    else:
        ki "Really? Cause I could have sworn I heard you listening Sandstorm by Darude on repeat that last few times I've walked by."

    s "…"
    s "Uhh..."

    scene kirinoff7
    with dissolve

    ki "It’s okay. You don’t need to hide anything from me. You can do whatever you want in here."
    ki "It’s your office, after all."

    if bonus == True:
        ki "If you want to use it to have sex with your students, that’s totally cool. I won’t tell on you."
    else:
        ki "If you want to use it to listen to Sandstorm, that’s totally cool. I won’t tell on you."

    s "This is...not at all how I expected our first conversation to go."

    scene kirinoff5
    with dissolve

    ki "Hmm...No, I guess it’s probably not."
    s "You’re really not going to tell anyone?"
    ki "Nahh. It’s more fun being in on secrets than exposing them."

    if bonus == True:
        scene kirinoff4
        with dissolve

        ki "You should probably try and convince the girls to keep it down, though. If anyone else walked by, you would probably get in a lot of trouble."

        "Did...anything like that ever even happen in here, though?"
        "And how would Kirin have even heard it if it did?"
        "What sort of reason would she have ever had to come over here?"

    s "Hey...can I ask you something?"

    scene kirinoff6
    with dissolve

    if bonus == True:
        ki "Whaaaat, you want {i}me{/i} to engage in a secret relationship with you as well?"
        ki "Sensei! I’m shocked! We’ve barely even met and you’re already looking at me like a vulture looks at a dead rabbit."
    else:
        ki "What's that? You want to see my old Sandstorm dance routine?"
        ki "Well, I mean...if that's what you really want..."

    s "I was just going to ask you about your hearing..."

    scene kirinoff2
    with dissolve

    ki "My...{i}hearing{/i}?"
    ki "That’s so boring. Talk about something more fun."
    s "Fun isn’t really my strong suit. But if you want to stand here and continue flirting for a while, I seem to have gotten pretty good at that as of late."

    scene kirinoff6
    with dissolve

    ki "Is that what it is? I’ve been wondering why everyone’s been going crazy about you."
    ki "Even Miku won’t shut up about you and she’s never even mentioned a boy before."
    s "Ahh, okay. I see what’s going on here."
    s "You’re not here to kill time. You’re just checking in to see what it is about me that’s making everyone fall for me, right?"

    scene kirinoff4
    with dissolve

    ki "Hmm...Well, I guess that’s one of the reasons."
    ki "You could just be one of those guys that’s destined to lead a harem from the get-go, but...I still think it
    might be something a little more than that."

    if bonus == False:
        s "Ew, harems are gross. I just want to teach."

    s "Wait, roll back for a second. {i}One{/i} of the reasons? How many are there? What do you want from me?"

    scene kirinoff7
    with dissolve

    ki "Relax...It's just one more reason. And it’s a pretty simple one, too."
    s "...Okay?"
    ki "Basically, I just need you to do something for me."
    s "And why exactly would I do anything for you? You’re not even one of my students."

    if bonus == True:
        ki "No, but I’m cute and I’ll probably have sex with you if you play your cards right."
    else:
        ki "No, but I’m cute and I’ll probably give you a shoulder rub if you play your cards right."

    s "Well, when you put it that way..."
    s "What do you need?"

    scene kirinoff8
    with dissolve

    ki "Geez...boys really {i}are{/i} easy, aren’t they?"
    s "What you said can not be taken back. I hope you’re aware of that."

    scene kirinoff9
    with dissolve

    ki "Yeah, yeah. I know. I won’t take anything back."
    ki "Besides, the favor I need today is pretty standard anyway."
    s "And what is this favor, Kirin?"

    scene kirinoff1
    with dissolve

    ki "I need you to vouch for me whenever I don’t come to[school]."
    ki "This place is boring and I don’t want to come anymore."

    if bonus == True:
        s "You think I’d risk losing my job for the chance of having sex with you?"
    else:
        s "You think I'd risk losing my job for a shoulder rub?"

    ki "Yes. But, because I’m so nice, I’m willing to offer something else for today and today only."
    s "...I’m listening."

    if bonus == True:
        jump kirinofficex
    else:
        scene black
        with dissolve

        "Kirin looks over her shoulder to make sure the door is closed before retrieving a suitcase from under the table (No idea when she put it there) and sliding it across the desk to me."

        ki "This is one billion US dollars."
        s "My god..."
        ki "Do we have a deal?"
        s "How did you fit it all in one suitcase?"
        ki "That's a question for another day. Are you in or are you out?"
        s "The shoulder rub probably would have been enough, you know."
        ki "I don't have all day, boss."
        s "Fine. I'm in."

        "I don't know what I just signed up for, but I'm not about to turn down-"

        s "Hey, wait a minute. This is just the third season of Seinfeld on DVD."
        ki "Is it?"
        s "Yes. See? It says {i}Seinfeld Season 3{/i} right there on the cover."
        ki "Hmmmmmmmmmmmmmmmmmmm..."
        s "What's your game here, Kirin?"
        ki "Hmmmmmmmmmmmmmmm..."
        s ".........???????????????????"
        ki "Bye Sensei!"

        play sound "dooropen.mp3"

        s "Wtf"

        $ renpy.end_replay()
        $ day83 = True
        stop music fadeout 3.0

        "………"
        "……"
        "…"

        jump afterschoolevent

label day85:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
...
```