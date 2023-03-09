# Cleaning Duty
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day36&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 36

✅Event "[Main: Operation: Fallen Angel](./day16.md)" is completed (event=day16)

✅Event "[Sana: The Bare Minimum](./bar5.md)" is completed (event=bar5)



## Next events
* [Main: Walk in the Park](./day38.md)

## Event properties
* ID: day36
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day36:
    scene threesix1
    with dissolve
    play music "normalday.mp3"

    "School is over for the day and, in place of my typical counseling hours, I have been summoned to the staff room to..."
    "I don't know, actually."
    "I was definitely asked to do {i}something,{/i} but...I didn't really understand what was being asked. So I'm kind of just hoping it's nothing important and that no one notices."
    "That's pretty much no different from what I always do, though."
    "I've been here for a little over a month and I still haven’t gotten the hang of the more...clerical side of things."
    "And it's not like I can ask for help either when this is something everyone just assumes I know already."
    "But hey, at least my students seem to like me. And I'm a lot more interested in appealing to them than anyone my age."
    "Disgusting, yes. I know."

    play sound "slidedoor.mp3"

    mi "Sensei! We need help!"

    scene threesix2
    with dissolve

    "Miku and Sana suddenly appear before me. How they knew I was here? I have no idea."

    s "Okay...And what do you need help with? I'm not counseling today."
    mi "I am very bad at cleaning!"
    s "I'm going to need a little more than that, Miku."
    mi "Fine, jeez!"
    mi "Sana and I are on cleaning duty today, but neither of us have any idea where any of the cleaning stuff is!"
    mi "Or...at least I think Sana doesn't have any idea."
    mi "Honestly, I haven't been able to hear anything she's said since she's so quiet and stuff and I feel weird about askin' her to talk louder."
    s "Well, you certainly don't feel weird about admitting that to me right in front of her."
    mi "My brain doesn't work the way most brains do, okay?!"
    sa "I...really don’t know where anything is either..."
    sa "And...umm...I'll try to talk a little...louder..."
    s "Okay, so we've identified the problem. But what exactly do you want me to do about it?"
    mi "Anything! Just help!"
    s "I don't know where any of that stuff is either, though."

    "In fact, I barely know where anything in this[school] is and I’ve been here for over a month now."

    scene threesix3
    with dissolve

    mi "What?! So we're doomed?!"
    s "Yeah, I guess so."

    scene threesix4
    with dissolve

    mi "AHHHH!! I’M NEVER GONNA MAKE IT TO SOCCER PRACTICE AT THIS RATE!"
    sa "I...ummm...tried telling you earlier but...I can try to do it on my own if...it will help you show up on time..."
    sa "I just...have to find everything first..."

    scene threesix6
    with dissolve

    mi "Ugh...thanks, Sana. But I ain't gonna make you do somethin' like that. I'd rather just miss practice at that rate."
    mi "Besides, Makoto says I’ve gotta start learnin’ responsibility and stuff and that cleanin' is a big part of that."
    mi "I just didn't expect it to be so much of a puzzle."

    "To be fair, it's not really {i}supposed{/i} to be..."

    scene threesix7
    with dissolve

    mi "I've just gotta face it, I guess...There’s no hope for me in this world..."
    mi "I’m going to have to join the space war..."
    s "No one’s joining the space war, Miku. Everything will be okay."
    s "Why don’t you and Sana just...go look for an actual teacher or something?"

    scene threesix8
    with dissolve

    sa "Actual teacher?..."
    sa "Are you not...a real teacher, Sensei?..."

    if bonus == True:
        "Correct, Sana. I'm just some guy who was reincarnated into the body of a teacher and is now using that as a tool to get {i}closer{/i} to you and everyone else."
    else:
        s "Of course I am a real teacher."

    s "I just meant...find someone who actually knows where stuff is."
    s "What about the teacher in the class next to ours? Miss...Watabe or something?"
    s "That’s a name I'm pretty sure I’ve heard mentioned before. She might know where stuff is."

    scene threesix9
    with dissolve

    mi "No way, Sensei...That teacher gives me the creeps."
    mi "And her room always smells like...candles or something."
    s "You know, I'm really starting to think we should just let Sana field this on her own."

    scene threesix10
    with dissolve

    sa "That's fine...I can just text my mom and tell her I'll be late for work..."
    s "..."

    "Is it really okay to be scheduling cleaning duty for people who almost always have something to do after school?"

    s "Okay, whatever. I'll come look for a janitor's closet with you two. But only because I really don't remember what I was supposed to be doing in here."

    scene threesix11
    with dissolve

    mi "Heck yeah! That’s the Sensei I know and love! I knew you’d come in clutch for your old pal, Miku!"
    s "Just...don't expect me to do any actual cleaning once we track the supplies down. I draw the line there."
    mi "Deal! Now, let's hurry the heck up and get this show on the road before the rest of the team tracks me down and breaks my kneecaps for bein' late!"

    play sound "slidedoor.mp3"
    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene newcleaning1
    with dissolve

    mi "Thanks again, Sensei! As a special reward, I’ll let you sit front row at our next soccer game!"
    s "I was unaware that I wasn’t already allowed to do that."
    sa "And...umm...I'll save you a...front row seat at the bar..."
    s "You have one row of seats."

    scene newcleaning2
    with dissolve

    mi "Oh, come on Sana! You can do better than that! Give the man somethin' he really wants!"
    sa "But...I don't really know what...Sensei would want..."

    "Good."

    mi "At least try usin' your outside voice if you're not gonna be forkin' over a decent reward! School's over! We don't gotta be quiet anymore! We're free!"
    sa "I...don't think I have an...outside voice..."
    s "That's not true. I heard your outside voice loud and clear during your little act with Ayane during gym a while ago."

    scene newcleaning3
    with dissolve

    sa "That...was for a mission..."
    sa "It was a...special exception..."
    mi "You went on a mission and didn’t even call your lifelong friend, Miku?!"
    mi "Am I not good enough for you anymore?! Is that how things are gonna be, Sana?!"
    s "Lifelong? You two have known each other that long?"

    scene newcleaning4
    with dissolve

    mi "You know it! Sana and I go all the way back to first grade! And, if you combine both of us, we've probably grown a whole foot since then!"
    s "That is...really not that much."
    mi "Well, we can't all be ten foot tall monsters like you, Sensei."
    mi "Sana and I were actually the two shortest girls throughout our entire school careers before high school came and Maya took my spot as the #2."
    s "Is she really shorter than you?"
    mi "Yeah, but she acts tall so nobody ever notices."
    mi "But apart from her, nothing else has really changed! We're still the same girls we've always been!"
    sa "I...don't know if I'd...really say that we were friends, though..."
    sa "We...only talked a couple times..."

    scene newcleaning5
    with dissolve

    mi "Yeah, but that’s just cause we hung out with different people! I was always with my soccer team back then and you were..."
    mi "You were...uhh..."
    mi "Huh. Who {i}did{/i} you hang out with back then, Sana? I remember there bein' somebody, but I can't put my finger on-"

    scene newcleaning6
    with dissolve

    sa "Oh...umm...look..."
    sa "Could...{i}that{/i} be the...janitor's closet?..."
    mi "What?! Was it seriously right there this whole time! But we walked past that like four times on our own!"

    "The three of us come to a stop at the end of the hallway in front of a room that is {i}clearly{/i} labeled as the custodial closet-"
    "But the even more convenient part is that it's already cracked open so I don't have to break the news of not having a key to them."

    mi "Come on, Sana! You can tell me more about your friends back then while we're cleanin' the chalkboard."
    sa "Can we...maybe talk about...umm...anything else?..."

    scene newcleaning7
    with dissolve

    mi "Sensei! Thanks again for your help today!"
    mi "I know you mentioned not wantin' to actually help with the cleanin' part, but if you change your mind-"
    s "Nope. I’m good. Thanks, though."
    mi "You sure? Might give ya a good chance to write dirty words on the board since we're just gonna erase the whole thing anyway."
    s "Still good. Not cleaning. But thanks."
    mi "Well, hey! You know where we'll be if ya want some more of us! And you know where I'll be afterward if ya want some more of {i}me!{/i}"
    s "Carefree suggestions like that are going to get you in trouble one day, Miku."
    mi "Probably! But Makoto makes me carry pepper spray around, so I'll be okay."
    sa "Th...Thank you...Sensei..."
    sa "You can...umm...come visit me again if..."
    sa "Uhh..."
    sa "You...want alcohol..."
    s "..."
    sa "..."
    s "Thank you, Sana. That's very considerate of you."

    scene black
    with dissolve2

    "The two of them disappear into the closet and I can instantly hear a mountain of supplies toppling to the ground as one of them manages to destroy the room in record time."
    "I doubt I'd be wrong in assuming it's Miku."
    "Either way, not wanting to get involved any further, I return to the office and..."
    "Try to remember whatever it is I'm supposed to be doing in there."

    $ renpy.end_replay()
    $ day36 = True
    $ miku_love += 1
    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Miku's affection has increased to [miku_love]!{/i}"
    "{i}Sana's affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    jump afterschoolevent

label day38:
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
...
```