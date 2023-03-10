# Outside of Everything (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 26



## Next events

None

## Event properties

* Id: day26
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day26

## Official wiki page

[Outside of Everything](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day26&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day26:
    scene hall_noon
    with dissolve
    play music "normalday.mp3"

    "I make my way back to the classroom after a quick trip to the teacher's lounge because, for some reason (Likely in regard to my new teaching methods), Makoto wants to speak with me."
    "I was under the impression that she'd already gotten used to these methods on account of her distinct lack of complaints lately, but I guess...too much was too much. Or something."
    "I have no idea. I just hope she doesn't expect me to change because- let's face it. I am {i}not{/i} cut out to be the teacher she wants me to be."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "I sigh to myself and make my way into the classroom, not really knowing what to expect."
    "........."
    "......"
    "..."

    scene makalone1
    with dissolve2

    mak "Okay...You can do this, Makoto. You are strong...and admirable...and...at least not {i}entirely{/i} unattractive."
    mak "Yeah...yeah! What's the worst that could happen?"
    mak "I mean...you {i}could{/i} get rejected by the man you admire more than anyone else...or he {i}could{/i} think you're a creep for even considering something like this, but..."

    if firsttimepornshop == True:
        if bonus == True:
            mak "But it’s not like he’s all that innocent, either!"
            mak "In fact, he’s even worse! Just...waltzing into a porn shop in the middle of the night! Just how much of a pervert is he?!"
            mak "But...then again...it's not like I'm {i}not{/i} into that sort of thing. I just...I..."
            mak "Mm!"
        else:
            mak "But you {i}both{/i} wear glasses, so truly there must be some sort of deeper connection! We are comrades!"
    else:
        if bonus == True:
            mak "No...No! Sensei would never think I would have ulterior motives. He knows me better than that."
            mak "P-Plus! It’s not like they’re even {i}motives{/i} to begin with...this is just...to help me understand him better! Yeah!"
            mak "…"
            mak "Ugh..."
        else:
            mak "But you {i}both{/i} wear glasses, so truly there must be some sort of deeper connection! We are comrades!"

    "Interesting. It seems as if I'm not going to get yelled at at all and that, instead, I’ve stumbled into some sort of soliloquy."
    "That said, I should probably snap Makoto out of it before she reveals a little too much and winds up regretting something."

    s "Hey."

    scene makalone2
    with dissolve

    mak "Great...now I'm even hearing his voice. Could this day get any worse?"
    s "..."
    mak "..."
    s "I've been trying to reach you about your car's extended warranty."

    scene makalone2r
    with dissolve

    mak "..."
    s "..."
    mak "You're actually there, aren't you?"
    s "Yup."

    scene black
    with dissolve

    "Makoto slaps her cheeks to force herself back into her default setting of being a knowledge robot before turning around to meet me..."

    scene makalone3
    with dissolve

    mak "How much of that did you hear, exactly?"
    s "For the sake of preserving your mental health, none of it."
    mak "And for the sake that doesn't care at all about my mental health?"
    s "Enough to know you love me."

    scene makalone4
    with dissolve

    mak "L-Love?! No one said anything about love!"
    mak "Forget I even asked for the truth and just...go back to pretending you didn't hear anything! It'll make what I'm about to say significantly easier for me!"
    s "Really? Because I feel like a confession would be easier {i}if{/i} we both know what we're walking into."

    scene makalone5
    with dissolve

    mak "This...isn't a confession, though."
    s "It's not?"
    mak "Of course not...don't be ridiculous."
    mak "That sort of thing between a teacher and a student? Let alone {i}us?{/i} No...No, that would never work."
    s "Then what-"
    mak "Do you...remember what happened in your office the other day?"

    if bonus == True:
        s "You mean the massage?"
    else:
        s "You mean when we went to Hogwarts and you had to drop out of the sorting procedure?"

    mak "Y...Yeah."
    mak "Well...I’ve been thinking about that a lot since then and-"
    s "Name the time and place and we can do it again whenever you want."

    scene makalone6
    with dissolve

    mak "That's just the thing! I don't {i}want{/i} to do it again!"
    mak "My inability to get it off of my mind doesn't have anything to do with some...unquenchable thirst for more!"
    mak "The reason I can’t stop thinking about it is because of how absurdly inappropriate it was for {i}both{/i} of us to be a part of something like that!"
    mak "If...If any of the other girls knew what happened in there...I don’t even want to know what they would think about me."

    scene makalone5
    with dissolve

    mak "I'm already seen as a bit of a teacher's pet...so I need to be very careful when it comes to things like this, Sensei."
    s "So, just...don't touch you from now on? Is that what you're asking?"

    scene makalone7
    with dissolve

    mak "Precisely. It’s not only inappropriate, but entirely immoral given our relationship."
    s "If that's what you want, sure."
    s "I'm not really sure if I think any of what you said warrants walking away from something you were clearly interested in, though."

    scene makalone8
    with dissolve

    mak "My {i}interest{/i} in it is beside the point, Sensei! I was very obviously enjoying myself! Perhaps even {i}too{/i} much!"
    mak "I'm sure this is no surprise to you, but no one has ever touched-"
    s "I'm going to cut you off right there because this is definitely not something you should be yelling in a classroom."

    scene makalone5
    with dissolve
    stop music fadeout 15.0

    mak "Ugh...Look what you’re making me say. Now I’m even more worked up."
    s "I’m not making you say anything. You just started yelling after {i}I{/i} said something that made too much sense."

    scene makalone7
    with dissolve

    mak "Well, whatever the case...I don’t think it’s something we should be doing on[school] grounds anymore."
    s "You realize that implies that it would be fine {i}off{/i} of school grounds, right?"

    "Makoto breathes in deeply and holds the air inside of her for what feels like a full minute."
    "The sound of footsteps and chatter from outside of the classroom bleeds in through the thin walls and reinforces the notion in the back of my head that {i}all{/i} of this is wrong."
    "And what I'm sure is about to come next is perhaps the most {i}wrong{/i} of all."

    scene makalone10
    with dissolve
    play music "love.mp3"

    mak "That's...actually part of what I wanted to talk to you about."
    s "..."

    scene makalone11
    with dissolve

    mak "I...Umm..."
    mak "Again, this is not a confession..."
    mak "But there's been something I've been very interested in for quite a while now and..."

    scene makalone11r
    with dissolve

    mak "And that {i}thing{/i} just so happens to be you."

    if bonus == False:
        s "Does this still involve witchcraft and wizardry or-"

    mak "Again, this is not a confession."
    s "Each time you say that just makes it sound {i}more{/i} like a confession, Makoto."
    mak "I...know this might sound stupid since I’m still [young]and shouldn’t even be worrying about this kind of stuff yet, but..."

    scene makalone11
    with dissolve

    mak "I just want to try seeing what it’s like {i}not{/i} worrying about[school] and...work all the time."
    mak "I want to lay down some nights and think ‘Wow. Today was a really good day.’"

    scene makalone12
    with dissolve

    mak "And I guess I...never really get that."
    mak "Every day is the same thing. Over and over and over. It's like...I'm stuck in a loop or something."
    s "I get that. But what do you want me to do about it?"

    scene makalone13
    with dissolve

    mak "Huh?"
    s "How am I supposed to help? What can I do to help you not feel like you're...stuck in a loop or whatever?"
    mak "You don’t have to do anything different, really...And I say that knowing that your personality could do a complete 180 again any day now."

    scene makalone14
    with dissolve

    mak "You’ve...changed a lot over the last few weeks...And I’m not saying that’s a bad thing."
    mak "I’ve always admired you for your intellect and your dedication, but you’ve always seemed a little...closed-off."
    mak "Which is why it was always hard for me to tell you how I feel."
    mak "But...you’ve seemed more open lately. And I’m less worried about things like that now."
    mak "And it got me thinking-"
    mak "If {i}you{/i} can change your mindset and start changing yourself...why can't I?"

    scene makalone15
    with dissolve

    mak "So...here’s where you come in."
    mak "Every once in a while, and I don’t care when...I’d like to see you {i}outside{/i} of[school]."
    s "Ahh. So it's not a confession, but you {i}are{/i} asking me on a date. Is that right?"
    mak "No. That's not right at all."

    "Teenagers are exhausting."

    mak "What I'm looking for could be something as simple as just...going for a walk. Or going out for coffee."
    s "So-"
    mak "Stop it. It's not a date."
    mak "You just seem to know a lot about what it means to live a fulfilling life...so I want to learn more about that from you. Firsthand, without worrying about school getting in the way."

    "A fulfilling life, huh?"
    "Is that really what this is?"
    "Taking control of someone else’s body?"
    "Stepping in and single-handedly dismantling everything they built?"
    "Is this really what it means to be fulfilled?"

    s "I'm not sure how much you're planning on learning, but if it means hanging out with you outside of school...sure."
    s "That's fine by me."

    scene makalone16
    with dissolve

    mak "Heheh..."
    mak "I'm glad we were able to reach an understanding then. I promise I'll try not to bother you too much."
    s "I'm already getting used to being bothered by pretty much everyone, so don't worry too much about that."
    mak "Is it really that bothersome having to watch over a handful of teenage girls?"
    s "You'd be surprised."
    mak "Heheh...you're right. I think I would."
    mak "But perhaps learning how to deal with {i}that{/i} is just one more thing you can teach me during our time together."
    mak "It's bound to come in handy some day, I'm sure..."

    scene black
    with dissolve2

    "Makoto and I spend the rest of afternoon straightening up the classroom before ultimately separating."
    "And while the air was heavy upon entering the classroom a few minutes ago, it's gone back to normal now and the two of us are able to breathe easy again."
    "As we leave the building and fade out of each other's field of vision, something crosses my mind."
    "What if I'm {i}not{/i} able to help Makoto escape from the life she’s grown so tired of?"
    "What happens then?"
    "…"
    "I guess there's only one way to find out."
    "Here's hoping I don't have to."
    "And here's hoping I make a suitable raft for her to float away on."

    $ renpy.end_replay()
    $ makoto_love += 1
    $ day26 = True

    "{i}Makoto's affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    jump afterschoolevent

label day28:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

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
...
```