# The Complete Absence of Everything
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm45&go=Go)



## Event preconditions
✅Sana love greater than or equal to 45

✅Event "[Main: Sayonara](./thirdreset3.md)" is completed (event=thirdreset3)

✅Day of week is not Thursday



## Next events
* [Sana: Mine](./sanadorm50.md)

## Event properties
* ID: sanadorm45
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm45:
    play sound "knock.mp3"

    "I knock on Sana’s door and wait for her to answer."
    "But as I make the completely sane decision to press my ear against it to see if she’s up to anything, I notice the unmistakable sound of what could only be described as maniacal laughter."

    ya "Enter and learn the truth!"
    ya "He is risen! He is just! He is-"
    sa "He is...Sensei..."
    sa "Come in..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I open the door and try to waive off the sudden increased abundance of confusion that has sunken into me."
    "Here I was thinking that Sana and Yasu weren’t exactly on good terms."
    "Now they’re hanging out together?"
    "That’s completely-"
    "Wait."
    "What if Yasu did...Yasu stuff and just wandered in there on her own?"
    "Did Touka go home for the night? Is it really okay to leave her alone?"

    scene sanayasudormvisit1
    with dissolve

    sa "Umm...hi..."
    s "Quick. Before she has a chance to preach...why is Yasu here?"

    if bonus == True:
        ya "I am simply doing the lord’s work, Sensei. Spreading the seed the best a [young_girl] {i}can{/i} without the help of a certain someone."
    else:
        ya "Would you like to buy any Girl Scout Cookies?..."

    s "Too slow, Sana. Now there’s no escaping."

    scene sanayasudormvisit2
    with dissolve

    ya "What is there to escape from, Sensei?"
    ya "I come here not of my own volition."
    ya "At least not this time."
    sa "Yasu’s...actually been coming here for a little while now..."
    s "So you two are friends all of a sudden?"
    sa "I...don’t really think it’s that simple."
    ya "Honorary angels have no time for friends, Sensei. We must use our time to-"
    s "Yeah, yeah. He who’s so commonly a god or whatever."
    s "I don’t really think Sana is interested in that kind of stuff, though."

    scene sanayasudormvisit3
    with dissolve

    ya "Hm."
    ya "It appears she is not."
    ya "But that does not change the fact that I can hear things that I know she would like to hear. And see things that she wishes she could see."
    ya "It is only a matter of time before her questions outweigh her uncertainties."
    ya "And when that time comes, I will be here to shepherd her to the light."

    if bonus == True:
        ya "To open up her mind and her body to anyone willing to fill it."
    else:
        ya "(Airplane noises)"

    scene sanayasudormvisit4
    with dissolve

    sa "Wait...uh...what was that last part?..."

    if bonus == True:
        sa "About my...body?..."

    ya "Perhaps I can go over that in vivid detail during my next visit."

    scene sanayasudormvisit5
    with dissolve

    ya "But until then...may the path you walk be free of callousness."
    ya "Good day, humans."

    scene sanayasudormvisit6
    with dissolve
    play sound "dooropen.mp3"

    sa "…"
    s "…"

    if bonus == True:
        sa "Do you...have any idea what that...body part was about?"
    else:
        sa "Do you...have any idea what those noises were?..."

    s "I do."
    sa "…"
    sa "Could you-"
    s "I can’t."
    sa "Oh..."
    sa "Um...okay..."
    s "That aside, what just happened?"

    scene sanayasudormvisit7
    with dissolve

    sa "I...don’t know..."
    sa "It just...kind of started happening the other day and...she keeps coming back."
    s "If she’s bothering you, just tell Touka about it. She seems to be the only one capable of getting Yasu to...rein it in a bit."

    scene sanayasudormvisit8
    with dissolve

    sa "She’s not bothering me."
    sa "She’s...a little strange, I’ll admit...but...the things she talks about are actually kind of interesting."
    sa "Scary...but definitely interesting."
    s "Well I think we’re going to have to agree to disagree here. I’m not really a fan of all of that religious stuff."
    sa "I’m...not really surprised to hear that..."
    sa "You don’t...seem like the religious type..."
    s "Even that’s a bit of an understatement. "
    s "Can we sit down, by the way?"
    s "As much as I enjoy towering over you, extended conversations with our height difference kind of hurts my neck."

    scene sanayasudormvisit9
    with dissolve

    sa "Heheh...of course..."
    sa "Please...sit down..."

    scene black
    with dissolve

    "Sana and I make our way across the room to the couch and then take our respective places."
    "And, in doing so, I realize something."
    "Almost every time Sana and I are seated next to one another, I’m closest to the side of her face that she hides behind her hair."
    "What gives?"

    scene sanayasudormvisit10
    with dissolve

    s "Sana."
    sa "Hm?"
    s "Is there a reason I always have to sit closest to the side of your face that doesn’t have an eye?"
    sa "…"
    sa "What?"

    "I guess not."

    s "Anyway, Yasu."
    sa "What about her?"
    s "Well, weren’t you afraid of her up until...now?"

    scene sanayasudormvisit11
    with dissolve

    sa "I was, but...I think that’s just because I didn’t really understand her..."
    s "And...you understand her now?"
    sa "Well...no."
    sa "But I think that’s just because I’ve {i}never{/i} really understood anything about god."

    scene sanayasudormvisit12
    with dissolve

    sa "I think Yasu just...might have been from one of those families that...forces a child to follow a certain path without...asking them if they want to."
    sa "My mom never did that...so I was kind of free to choose whatever I wanted to believe instead of...following in her footsteps."
    s "Sara’s not actually religious, is she?"

    scene sanayasudormvisit13
    with dissolve

    sa "No...my mom’s an atheist."
    s "And what would you call yourself?"
    sa "Um..."

    scene sanayasudormvisit14
    with dissolve

    sa "I guess I’d also call myself an atheist..."
    sa "So I suppose I {i}did{/i} kind of follow in her footsteps a little bit."

    scene sanayasudormvisit15
    with dissolve

    sa "But...I can promise you that the decision was mine and that I didn’t just end up that way because of her."
    s "I’m lost. If you don’t believe in any sort of god, why doesn’t allowing Yasu to preach about hers annoy you?"

    scene sanayasudormvisit16
    with dissolve

    sa "Because...getting mad at someone for believing something differently than you is the easiest way to tell if someone is a bad person..."
    sa "Just because we think differently doesn’t mean I’m not interested in hearing how she looks at the world."
    sa "I think it’s...really special that we can still talk to each other in spite of that."
    s "I get that, but...you do realize she’s trying to convert you, right?"

    scene sanayasudormvisit13
    with dissolve

    sa "Of course..."
    sa "I might not be as smart as Makoto or...umm...Nodoka...but I’m not an idiot, Sensei."
    sa "I’m...free to choose when and how I want to be converted or changed."
    sa "And...in a sense...haven’t you been trying to convert me as well?"
    sa "Not in a...religious way or anything...but you identified a part of me that you didn’t agree with or like and...you’ve been showing me how to move past it."
    sa "The only difference with that is I believe you. And...I don’t really believe Yasu."

    scene sanayasudormvisit17
    with dissolve

    sa "But if her getting to talk about her beliefs can get her to smile...I don’t mind hearing her out."
    sa "I mean...she’s the one coming here after all. And it’s not like anyone else besides Ayane ever does that."
    s "And that stuff about her hearing things and seeing things you wish you could?"

    scene sanayasudormvisit18
    with dissolve

    sa "…"
    sa "What about it?"
    s "It's just..."
    s "I remember you crying the first time you met her."
    sa "And?"
    s "And it was right after Yasu said something about someone-"

    scene sanayasudormvisit13
    with dissolve

    sa "Why are {i}you{/i} an atheist, Sensei?"
    s "Hold on. I wasn’t finished-"
    sa "Why are {i}you{/i} an atheist, Sensei?"
    s "…"
    sa "…"

    "Okay then. I guess that’s not something Sana wants to talk about right now."

    s "I guess because the idea of a god in general is just annoying to me."
    s "I don’t care much about science or faith or anything like that, I just don’t want some annoying, invisible celestial entity telling me what to do with my life."
    sa "Your answer reminds me a little bit of Maya’s. Though I think she...cared about the science part a little more..."
    s "And yet she works at a shrine and prays at least once every several months."
    s "Also, why were you talking to Maya about religion?"
    s "Is this just a thing you do, Sana? Go out and coax the other students into telling you their outlooks on faith?"

    scene sanayasudormvisit14
    with dissolve

    sa "Of course not..."
    sa "It just...came up during one of our D&D sessions..."
    s "Why? Girls are supposed to be talking about boys and...makeup or whatever. Not religion."

    sa "That’s...a very outdated way of thinking, Sensei..."

    if bonus == True:
        sa "Aren’t you only a little older than 30?..."
        s "Age is just a number, Sana."
        sa "And that’s...a thing that no one should ever say in...any context..."
    else:
        s "You are right and I apologize. That was insensitive of me."

    s "Either way, god is a lie and everything is going to be dark and silent when we die."

    scene sanayasudormvisit17
    with dissolve

    sa "At least with that...I can agree..."
    sa "But I think a thought as scary as that is why so many people choose to think differently than we do..."
    sa "And...I’d be lying if I said I didn’t wish there would be more afterward..."
    sa "Especially...since..."
    s "…"
    sa "…"

    scene sanayasudormvisit18
    with dissolve

    sa "You know...maybe I do follow in my mom’s footsteps a little more than I’d like to admit."
    sa "We’re both...very different people...but I know that she wishes there was more after death as well."
    sa "I think that if...she was able to actually believe that...things might be a little easier for her."
    sa "If you closed your eyes right now and were never able to open them back up...how would you feel, Sensei?"
    s "Bad. But also not {i}too{/i} bad because the last thing I'd see would be you."

    scene sanayasudormvisit19
    with dissolve

    sa "That...doesn’t sound like a very good final sight..."
    sa "Also...please never repeat that to Ayane..."
    s "I was just kidding anyway."
    s "Kind of."
    s "The real answer is that I’d be miserable."
    s "But so would anyone, really."
    s "Even those fatalistic types who are always talking about how much they want to die-"
    s "Actually, just envision Miss Watabe. That’s the type I’m talking about."
    s "I’m sure even Miss Watabe would be miserable if she actually died."
    s "Assuming she maintained sentience, that is."
    s "Which she wouldn’t."
    s "Because...you know. She’d be dead."

    scene sanayasudormvisit20
    with dissolve

    sa "Dying is scary."
    sa "The idea of everything being black is scary."
    sa "But what it does to the people someone leaves behind..."

    scene sanayasudormvisit21
    with dissolve

    sa "That’s what I’m scared of most right now."
    s "Even after already experiencing it?"
    sa "It’s {i}because{/i} I’ve experienced it that I’m so afraid of it."
    sa "I’d take the complete absence of everything over that sort of pain ever again."
    s "Yeah...I-"

    play sound "static.mp3"
    scene imissyoumore with flash
    play music "painisreal.mp3"
    stop sound

    "There can be no complete absence of everything, for everything is already gone!"
    "And when everything is already gone, there’s obviously nothing left to lose."
    "It’s not profound or prophetic."
    "Poetic or poignant."
    "There’s just nothing."
    "We’ve already lost."
    "I’ve already lost."
    "You’ve already lost."
    "We go to sleep at night, throw ourselves into darkness for X amount of time, then wake up and eagerly await the next time we get to fall into the dark again."
    "Nearly a third of your life is spent being utterly incapable of anything."
    "What do you do with the time you’re awake?"
    "What are you going to become?"
    "How different is that person from the {i}you{/i} you are now?"
    "Henry David Thoreau once said, “Be not simply good. Be good for something.”"
    "Then he fucking died, which isn’t good at all."
    "Dead people have no use unless we turn them into fertilizer or something to that effect."
    "But I guess in a roundabout sort of way, a good portion of people wind up dissolving in the soil and inadvertently fertilizing trees."
    "[[redacted] was one of those people."

    if bonus == True:
        "I watched from afar, behind her favorite tree, as her body was lowered into the ground."
        "I went home and [masturbate]d to the idea of thrusting into her one last time."
        "She’d cry out with those same pained yelps she always did."
        "Not from the physicality of it, but from the fact that she, too, had already accepted that everything is gone. "
        "And then she’d let me cum inside of her because it felt better for both of us."
    else:
        "She was a pretty cool person. Great at word searches."

    play sound "static.mp3"
    scene sanayasudormvisit22 with flash
    stop sound

    "Sana reaches her hand out and several sunflowers begin to sprout from her skin and float around the room."

    if bonus == True:
        "I watch in awe as they swirl around her-  petals occasionally grazing her petite frame that I will one day pin down to her bed with full force before splitting her in two with my gigantic cock."
        "I do not believe in god, for if I did, I would be forced to worship myself."
        "And there is no one in this world more unworthy of anyone's faith or praise or worship than the man who can’t even rememmmmmmmmmmmmmmmmmmmmmmm-"
    else:
        "Why did this event get so weird out of nowhere?"

    "////////////////////RECOORDINATING"
    "////////////////////PLEASE REMAIN CALM AS THINGS ARE RETURNED TO THE WAY THEY ARE MEANT TO BE"
    "////////////////////…"
    "////////////////////…"
    "////////////////////…"

    scene sanayasudormvisit13
    play music "sweetvermouth.mp3"

    sa "Why are {i}you{/i} an atheist, Sensei?"
    s "…"
    s "What?"
    sa "I said...why are {i}you{/i} an atheist, Sensei?"
    s "…"
    sa "…"

    scene black
    with dissolve2

    "I am viciously sodomized by a horrible case of deja vu and replay a conversation that seems all too familiar to me."
    "Then I go home."

    $ renpy.end_replay()
    $ sana_love += 2
    $ sanadorm45 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased by 2 points for reasons beyond your comprehension!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanadorm50:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
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
...
```