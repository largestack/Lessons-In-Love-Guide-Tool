# The 'S' Word (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 70

* Event [Supermom](./bar10.md) (Sana) is completed)



## Next events

* [Main: Weight Limit](./day72.md)

## Event properties

* Id: day70
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day70

## Official wiki page

[The 'S' Word](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day70&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day70:
    scene hall_noon
    with dissolve
    play music "10c.mp3"

    "Instead of going to the cafeteria for lunch today, I have decided to wander the halls of the school instead."
    "Apparently, Ayane finally told Ami about that cooking competition she thought up a few weeks ago and Ami’s been cooking up a storm ever since."
    "I think I had somewhere around six types of bacon this morning."
    "And while that isn't exactly a {i}problem,{/i} I would like to make it known that I wasn't even aware that many types existed."
    "Anyway, as you may have guessed, I'm not very hungry."
    "And considering that I probably won’t {i}be{/i} hungry for the next year, I might as well...kill some time in the library while I wait for everyone to finish eating."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "………"
    "……"
    "…"

    scene sanalib1
    with dissolve2

    sa "Oh...S-Sensei..."
    sa "Good afternoon..."
    s "Sana? What are you doing in here? I figured you'd be in the cafeteria right now."

    scene sanalib2
    with dissolve

    sa "I...had a big breakfast and I’m...kind of worried about the tests coming up, so..."
    s "Tests? What tests?"

    scene sanalib1
    with dissolve

    sa "The...standardized tests that everyone has to take..."
    s "Again? I feel like we just had those."
    sa "Um...I guess...we missed one?...I don't really know how this works..."
    s "That makes two of us, Sana."
    sa "I...feel like that's a thing you should probably-"
    s "So, what are you studying? Anything I can help with?"

    scene sanalib3
    with dissolve

    sa "Umm...I was going to focus on history today..."
    s "Oh, okay. So that’s a no then."
    sa "Yeah...I figured..."
    s "If you want to talk about biology, though, I'd be more than happy to focus on that."
    s "Just don't ask me about mitochondria and inadvertently force me into the bathroom with another girl."
    sa "Umm...what?"
    s "Nothing. Just forget I even said that."
    sa "I...don't know what you're talking about and...biology won't be on the test...but thank you."
    s "Anyway, if these tests are coming up so soon, how come you're the only one studying? What happened to Ayane?"

    scene sanalib4
    with dissolve

    sa "Ayane...doesn’t like missing lunch..."
    s "Why not study in the cafeteria then?"
    sa "It’s too loud in there..."
    sa "I...have a hard time focusing in places like that..."
    sa "When more than one thing is happening at a time, I...kind of...lose track of everything..."

    "I feel like that isn’t exactly a great trait for a bartender to have."

    s "I can leave if you want. I'm not trying to distract you or anything."

    scene sanalib6
    with dissolve

    sa "No...it’s okay..."
    sa "I...actually had something I...wanted to ask you about anyway."
    s "Oh? And what's that?"
    sa "Just..."

    scene sanalib7
    with dissolve

    sa "Is it...really okay for me to come to your house?..."
    s "You mean for the cooking thing?"
    sa "Y-Yeah...Are you sure I won’t be...you know...intruding?"
    s "Absolutely. I mean, I'm not sure if Ami knows you're coming yet, but the way I look at it is that you’ll help make the competition fair."

    scene sanalib1
    with dissolve

    sa "Fair?...Me?...How?..."
    s "Well, Ami’s my [niece] and I eat her food pretty much every day. So it's hard to say I'm an impartial judge, do you know what I mean?"
    s "So, if you come over and be a judge as well, that’ll make things more balanced."
    sa "But...what if we vote for different things? We’d have a tie if there are only two of us..."
    s "Don’t worry about that. I actually have a third judge in mind already. I’m just...probably going to need Ami’s help to get her to come over."
    sa "I see..."
    sa "Well...as long as you’re okay with it...I’d be happy to come over."

    scene sanalib7
    with dissolve

    sa "I’ve...never really been anywhere other than my mom's and Ayane's, though...so...I'm sorry if I act kind of nervous..."
    s "I'm pretty sure nervous is just your default setting. Plus, Ami and Ayane will both be there to support you in case you start...losing track of stuff or whatever your problem was."
    s "This is just one more step in the plan to get you social."
    sa "Have I...been doing okay with that lately?"
    sa "I don’t feel any different...and I don’t want you to think I’m wasting your time."
    s "Well...it’s true that you haven’t really warmed up to other people yet."
    s "And I think you might now be traumatized when it comes to spaghetti-"

    scene sanalib8
    with dissolve

    sa "Ngh!"
    s "Okay, so you’re {i}definitely{/i} traumatized when it comes to spaghetti."

    scene sanalib9
    with dissolve

    sa "I’m just...not cut out to be a bartender, am I?"
    s "Don’t say that. You just need a little more time to settle into things. Do you think I was always as great at teaching as I am now?"
    sa "I...actually figured you...used to be better and...you're just checked out now or something..."
    s "Wow. Did you actually just snap back at me?"

    scene sanalib10
    with dissolve

    "Sana shakes her head and thinks quietly to herself for a moment - likely about how to not ‘hurt my feelings.’"
    "Obviously, I know I’m not a great teacher- so nothing she says is going to harm me at all."
    "In fact, while we're on the topic, I’m probably the worst teacher to ever walk the face of the earth."
    "But at least no one’s failed or been kicked out of[school] yet."
    "Granted, Yumi would probably be expelled if I actually turned in the accurate attendance sheets, but still..."
    "As far as the statistics are concerned, I’m a perfectly acceptable teacher as long as everyone manages to do okay on their standardized tests."

    scene sanalib11
    with dissolve

    sa "I...think you’re a good teacher, Sensei..."
    sa "I wasn't...snapping back at you..."
    s "Wait...you do? Why?"
    sa "Because...you talk to me..."
    sa "And you go out of your way to spend time with me when I need extra help..."
    sa "You...might not be very good at some subjects...but...that’s what the Internet is for."
    sa "Anything you don’t know...I can just look up on the computer."
    s "That’s the spirit. Computers will have taken all teaching positions by the year 2050 anyway. I’m just ahead of the trend."

    scene sanalib7
    with dissolve

    sa "Umm...r-right..."
    sa "Well...as long as you can stay our teacher for the next couple years..."
    s "Sorry to cut you off, but I'm pretty sure it doesn't work that way."

    scene sanalib1
    with dissolve

    sa "...Huh? What do you mean?..."
    s "Well...this school might work a little differently, but I'm pretty sure that once a new school year begins, you'll be getting a {i}new{/i} teacher."
    s "It's not predetermined that I'm going to have you for all three years or anything like that."
    sa "..."
    s "..."

    scene sanalib12
    with hpunch

    sa "Wh...what?!"
    sa "But..."

    "Maybe I should have just...let her find out on her own instead of preemptively breaking her heart?"

    sa "But..."
    sa "But I..."

    scene sanalib13
    with dissolve

    sa "I don’t want a different teacher..."
    sa "You’re the...only one who’s ever...been able to help me."
    s "Hey, you don’t have to cry-"

    scene sanalib12
    with dissolve

    sa "I’m not crying! There’s something in my eye!"
    s "But there are tears in both of them."
    sa "H-how do you know?! You can’t even see the other one!"
    s "Just a feeling, I guess."

    scene sanalib13
    with dissolve

    sa "Can you...see if they’ll maybe...make an exception for you?"
    s "I mean...I’m not exactly on the best terms with any of the staff members...but I can try?"

    if bonus == True:
        s "If it were up to me, I’d stay teaching you girls all the way through college. Meeting new people is too much of a pain."

        "Starting over sounds like it would be a bit of a slog as well and I'm already pretty far along with most of this class, I feel."
    else:
        s "Despite being an employee here, several of this college's practice still confuse me. But, if at all possible, I would like to teach you for as long as I can."
        s "For the rest of eternity even."

        "I smile to myself knowing that I will be doing just that."

    scene sanalib14
    with dissolve

    sa "You promise?..."
    s "I...will do my best. But I obviously can't make any promises."
    sa "…"
    s "…"

    scene sanalib15
    with dissolve

    sa "{i}*Sniff...*{/i}"

    "Sana uses the sleeve of her sweatshirt to wipe away the tears that have accumulated over the last few minutes."
    "It’s...pleasantly surprising to see her react like this to the idea of me not being her teacher anymore."
    "There’s gotta be more to it than just the fear of actually having to do[school]work again, right?"

    scene sanalib16
    with dissolve

    sa "…"
    sa "Um..."
    sa "I definitely wasn’t crying..."
    sa "I just..."
    sa "I definitely wasn’t crying."
    s "Right. Just like you weren’t crying during the spaghetti incident."

    scene sanalib12
    with dissolve

    sa "Stop saying the ‘S’ word!!!"

    scene black
    with dissolve2

    "Sana took another few minutes to collect herself before realizing that all of the extra time she set aside to study had vanished."
    "How much of that is my fault, you ask?"
    "All of it."
    "But I’m still glad that the two of us got to spend some time alone together."
    "There just haven't been many opportunities for that inside of school due to the...type of person she is."
    "I'm sure a day will come where that will no longer be the case, though."
    "So here's hoping that coming to my house and judging a cooking competition will somehow, in what would have to be an extremely roundabout way, serve as her gateway to a life full of friends."

    $ renpy.end_replay()
    $ day70 = True
    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    jump afterschoolevent

label day72:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
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
...
```