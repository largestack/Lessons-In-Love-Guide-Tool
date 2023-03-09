# Missing
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day50&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 50

✅Event "[Rin: Window of the Waking Mind](./cafe15.md)" is completed (event=cafe15)



## Next events
* [Rin: Nothing Was Missing, Except Me](./cafe20.md)
* [Rin: Delirium](./rindorm20.md)

## Event properties
* ID: day50
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day50:
    scene dayfifty1
    with dissolve
    play music "sweetvermouth.mp3"

    "Another[school] day gets off to a relatively mild-mannered start."
    "I don’t feel like doing anything today, so I told the girls they can just do whatever it is they want."
    "Of course, Makoto was opposed to the idea and has, per usual, gone back to studying like the success-driven
    prefect she is."
    "Ami and Maya are chatting, Chika is on her phone, Futaba is reading..."
    "Ayane is...staring directly at me..."
    "Yup. Pretty much everything looks normal today."
    "Well, almost everything..."

    scene dayfifty2
    with dissolve

    s "Huh...Rin’s not here again..."

    "Normally, I wouldn’t think anything of it if one of the girls were to miss a class or two."
    "But Rin’s been starting to miss a lot lately. And I know she told me not to
    worry but I can’t help wondering if she’s really doing okay."
    "Maybe Futaba knows something?"

    s "Hey, Futaba..."

    scene dayfifty3
    with dissolve

    f "Sensei? Is something wrong?"
    f "You don’t normally visit me at my desk..."
    s "I was actually just wondering if you knew anything about why Rin’s been absent so much lately."

    scene dayfifty4
    with dissolve

    f "Are you worried about her?"
    s "Of course I am. Just like I’d be worried about you if you started going missing all the time."

    scene dayfifty5
    with dissolve

    f "Well, uhh...I mean, I kind of know...I just don’t know if she’d be happy with me telling you or not."

    scene dayfifty6
    with dissolve

    f "She’s, umm...Well, she’s not really in the best state of mind right now. That’s
    probably the easiest way to put it."

    "Huh...She {i}did{/i} say all that stuff about ‘thinking things she wasn’t
    supposed to,’ or however it was she put it."
    "I’m assuming that’s what Futaba is talking about here."

    s "Is there like...something wrong with her?"

    scene dayfifty7
    with dissolve

    f "Sensei! That’s a horrible way to word that question! Of course nothing’s wrong with her..."
    s "Oh, I didn’t mean anything bad by that. You’re right. It was poor phrasing."
    s "What I’m trying to ask is if she needs our help or medical help or anything like that."
    s "I don’t really know what to do in situations like these."

    scene dayfifty5
    with dissolve

    f "Well...I guess that can’t really be helped."
    f "I never really knew what to do until recently either. It’s not exactly something that[school] prepares you for."
    s "How long have you two known each other again?"

    scene dayfifty8
    with dissolve

    f "Oh jeez, I can’t even remember. I think since elementary[school]?"
    f "What I do remember is that she was the one to approach me first."

    scene dayfifty9
    with dissolve

    f "I wasn’t really the best at making friends, and I guess she just realized that before everyone else."

    "That definitely sounds like the Rin I know...Weirdly outgoing and always thinking about other people."

    if bonus == True:
        "After all, this is the same person who’s still actively trying to set me up with her roommate just because
        she thinks it will make both of us happy."
        "It’s weird thinking that she’s hiding some sort of other life behind all of that."
    else:
        "I hope she doesn't ever get hit by a plane. That would suck."

    scene dayfifty8
    with dissolve

    f "She wasn’t always like this, though..."

    scene dayfifty9
    with dissolve

    f "Well, I guess that’s not {i}entirely{/i} accurate."
    f "I guess it’s more of an ‘it’s never been that serious’ kind of thing..."

    scene dayfifty8
    with dissolve

    f "Normally, she gets better after a day or two. Sometimes even a few hours."

    scene dayfifty10
    with dissolve

    f "But..."

    "Futaba’s smile is suddenly wiped off of her face as she comes to terms with how unusual her current situation is."

    f "I feel like she’s barely even been getting out of bed lately..."
    f "I’m kind of worried about leaving her alone, actually..."
    s "You don’t think she’d do anything...stupid, do you?"

    scene dayfifty11
    with dissolve

    f "Not at all. She’d never do anything like that."
    f "She might be going through some stuff right now, but I know that deep down, she
    loves pretty much everyone and everything."
    s "I thought the same thing."
    s "I mean, obviously you know her much better than I do, but I’m pretty
    sure she’ll pull through whatever it is that’s going on."

    scene dayfifty8
    with dissolve

    if futaba_love > 9:
        f "I knew you’d agree with me there. That’s just the kind of person you are, Sensei..."
        f "You might try to hide it, but I can tell how much you care about all of us..."
        f "Plus, Rin’s been saying a lot of nice things about you lately."

        scene dayfifty12
        with dissolve

        f "I’m actually...kind of jealous she’s been seeing you so much...hahaha..."
        s "Really? What has she been saying?"

    else:
        f "I had a feeling you’d agree with me."
        f "Rin’s been saying nothing but nice things about you lately."
        s "Really? Like what?"

    scene dayfifty8
    with dissolve

    if bonus == True:
        f "Just things about how you’re really cool for your age and that you’re fun to be around...stuff like that."

        "Huh...I had no idea Rin would actually be talking about me to other people."
        "I mean, it {i}is{/i} her roommate, though, so I'm sure it just randomly came up in conversation once or twice."
        "I shouldn’t get too excited about that."

        s "Well that’s really nice of her. Whenever I make friends my age, I’ll be sure to tell them about her as well."
    else:
        f "Just things about how she thinks you'd look really cute if your eyes looked a little more normal."
        s "Wait, what's wrong with my eyes? No one has ever pointed that out before."
        f "They're just...all squiggly and stuff..."
        s "What?"
        s "Hold on. I will remove them."

    f "Heheh~ Are you sure that’s the best idea?"
    s "Actually, no. I’m sure that would be a horrible idea. "
    s "But either way, do you think there’s anything I can do for her?"

    scene dayfifty4
    with dissolve

    f "For Rin?"
    f "I mean...I don’t think she wants to see anyone right now but..."

    scene dayfifty8
    with dissolve

    f "Maybe you could try writing her a letter?"
    s "A letter?"
    f "Yeah. You know how powerful words can be. I’m sure that a nice letter or a present
    or something would make her feel a little better."
    f "I know it would for me, at least."
    s "Huh..."
    s "Yeah, I think I can do that. Hold on one sec."

    scene black
    with dissolve

    "I walk back to my desk and start scribbling down whatever words come to mind."
    "I finish within a matter of minutes. It’s actually surprisingly easy writing something like this for her."
    "Here’s hoping she likes it..."

    scene dayfifty8
    with dissolve

    f "Done already?"
    s "Yup. You’ve gotta promise not to read it, though, okay?"
    s "And let me know what she says once she sees it."
    f "I’m sure she’ll be able to let you know herself soon enough, Sensei."
    s "Even better. Thanks, Futaba."
    f "Of course. Thank {i}you{/i} for caring enough to ask, Sensei..."
    f "I’m sure that will mean a lot to her."

    scene black
    with dissolve
    stop music fadeout 3.0

    "The rest of the class carries on as normal..."

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ day50 = True
    jump afterschoolevent

label day54:
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
...
```