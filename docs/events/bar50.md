# Melatonin
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar50&go=Go)



## Event preconditions
✅Sana love greater than or equal to 50

✅Event "[Main: Food Groups](./day351.md)" is completed (event=day351)

✅sarasex equal to True (unknown variable)

✅Event "[Sana: Mine](./sanadorm50.md)" is completed (event=sanadorm50)

✅bar50miss equal to False (unknown variable)



## Next events
None

## Event properties
* ID: bar50
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label bar50:
    scene funnydildoscene1
    with dissolve
    play music "calmbar.mp3"

    "I make my way over to the bar to hang out with Sana for a bit."
    "She’s cleaning off the counter when I arrive...which, thanks to my above average deductive reasoning, I know means there were likely {i}real{/i} customers tonight."
    "Could it be that handing out a few fliers and hiring an ex Yakuza wife actually increased business somehow?"

    s "You certainly look happy tonight."
    sa "Do I?"
    s "Unless you’re smiling for no apparent reason. "
    s "If that's the case, allow me to change that last sentence to, “You certainly look menacing tonight.”"

    scene funnydildoscene2
    with dissolve

    sa "I...think happy is closer to the right answer."
    s "But not {i}entirely{/i} the right answer."

    scene funnydildoscene3
    with dissolve

    sa "I think that maybe...relieved is the word you’re looking for."
    sa "It’s been a while since we had actual customers."
    sa "Even those two old ladies who used to hang out in the back of the room stopped showing up a while ago."

    scene funnydildoscene1
    with dissolve

    sa "But...tonight, we had a handful of people that I’ve never even seen before."
    s "And how many of them ordered drinks that you didn’t have the ingredients for?"
    sa "…"

    scene funnydildoscene4
    with dissolve

    sa "Um..."
    sa "All of them..."

    scene funnydildoscene1
    with dissolve

    sa "But...they were understanding when I told them we could only serve beer and wine for the night."
    sa "And...now I guess I have...more ammunition in...getting my mom to order actual liquor."
    s "Does Sara even have the money to get actual liquor?"
    sar "Does Sara what now?"

    scene funnydildoscene5
    with fade

    "Sara and Yuki come out of the back room and make their way over to Sana and me."
    "Sara stands defiantly behind the counter and Yuki-"
    "Well...Yuki just stands, I guess."

    yu "Yo."
    sar "Good evening, Sensei. "
    sar "Now, what were you saying about having enough money to buy {i}actual{/i} liquor?"
    s "Oh. I was just asking if you had enough money to buy actual liquor."
    yu "Reasonable question."

    scene funnydildoscene6
    with dissolve

    sar "Hmph."
    sar "I do recall a time where that may have been a worry of mine."
    sar "But I’ll have you know that the one and only Sakaki-Bar-A is back on top."
    s "Please tell me the name of this place isn’t actually the “Sakaki-Bar-A.”"

    scene funnydildoscene7
    with dissolve

    sar "Wait, you really didn’t know that?"
    sar "You’ve been coming here for how long now?"
    s "Good question, Sara. Why don't you answer it for me?"

    scene funnydildoscene8
    with dissolve

    sa "Um...I know we...had a good night, but...I don’t think we should let {i}one{/i} good night go to our heads..."
    sa "We...still have a lot of work to do..."
    sar "I know, I know. "
    sar "But, since all three of us did wonderfully tonight, I was thinking that maybe we could all go out for a little celebration."
    s "Okay. Guess I’ll just go fuck myself then."

    scene funnydildoscene9
    with dissolve

    sar "Okay, the {i}four{/i} of us can go out for a little celebration."
    s "Is that really the best course of action?"
    sar "Why wouldn’t it be?"
    s "I mean, I take it that you finally generated some sort of profit tonight. It would be a bit of a shame to just blow that all on a post work celebration, wouldn’t it?"
    sa "Sensei is...actually giving good advice for a change..."
    s "Hey, what happened to all of that stuff about how I helped you face your fear of people and pasta?"

    scene funnydildoscene10
    with dissolve

    sa "Guh..."
    sar "It’s not like I was planning on going out to some fancy restaurant or anything..."
    sar "Yuki told me about some place she normally goes to in the old district, so I was thinking that maybe we could all grab dinner there before heading home."
    s "Tojo Ramen?"
    yu "You know it."

    scene funnydildoscene11
    with dissolve

    sa "The old district is...a little too far for me, I think..."
    sa "I’m...kind of tired from working all night and...I don’t even think the buses are running right now..."

    scene funnydildoscene12
    with dissolve

    sar "But we were all gonna ride on Yuki’s motorcycle together and it was gonna be fuuuuun..."
    sa "I...don’t even know if that’s legal?..."
    yu "It’s not, but no one’s gonna fuckin’ care."
    s "And I’m assuming I’d just be walking."

    scene funnydildoscene13
    with dissolve

    sar "Of course not! You’d be riding with us!"
    s "Four people on one motorcycle? I’ll pass."
    yu "You passed when it was just two as well, ya fuckin' pussy."
    s "Yuki, come on. Not in front of one of my students."
    sa "It’s okay, Sensei...I’m...a little afraid of motorcycles as well..."
    s "I’m not-"
    sar "Yeah, yeah. We all know how brave and strong you are."
    s "Sara, not you too. You’re supposed to always be on my side."

    scene funnydildoscene14
    with dissolve

    sar "Put a ring on it and maybe I will be~"
    sa "…"
    s "Pass."

    scene funnydildoscene15
    with dissolve

    sar "At least hesitate a little, jerk!"
    yu "Brutal."
    sa "Um...if Sensei and I...both don’t really want to go..."
    sa "I guess we could stay here and...close up..."
    s "As long as I don’t have to actually do anything."
    sa "I’ve...already handled most of it, so..."

    scene funnydildoscene16
    with dissolve

    sar "You’re really sure you don’t want to come, Sana?"
    sar "It’s been a while since the two of us have gone out to dinner together."
    sa "We could always go another time. I just...don’t really want to right now..."
    sar "If...that’s what you really want...okay..."

    scene funnydildoscene17
    with dissolve

    sar "I’m leaving her in your hands then, got it?"

    if bonus == True:
        sar "It will be good practice for when you decide to settle down with me and become Sana’s new daddy."
        s "I really wish all of you mothers would stop trying to get me to be your daughter’s new father."
    else:
        s "Leave her in Yuki's hands. She is in a gang that kills people."

    scene funnydildoscene18
    with dissolve

    if bonus == True:
        yu "Yo! Don’t fuckin’ lump me in with that shit. I ain’t ever asked for that."
    else:
        yu "Yo! Don’t fuckin’ lump me in with that shit. I ain’t ever killed anybody!"

    s "Not {i}yet{/i} you haven’t."
    yu "Ain’t gonna fuckin’ happen, man. Quit while you’re ahead."
    s "How am I-"
    sar "As much as I’d love to hang around and listen to you two “not flirt” with each other, I’d also love to eat before it’s time for me to pass out for the night."

    scene funnydildoscene19
    with dissolve

    yu "You good to go then?"
    yu "Should probably put on a jacket if you don’t wanna get cold. Body heat’s not good for shit when you’ve got the wind blowin’ right at you."
    sar "It’s near the door. I’m ready whenever."

    scene funnydildoscene20
    with dissolve

    sar "Be good."
    sa "Uhh...okay?"
    yu "Night, man. See you around or whatever."

    scene funnydildoscene21
    with dissolve

    "Sara and Yuki make their way out of the store, leaving Sana and me alone in the bar for what I imagine is the millionth time."
    "Tonight feels a little different, though."
    "For one, it’s the first time I’ve ever had to watch her really clean anything."
    "But not only that, we’re still coming off of a relatively awkward and uncomfortable exchange about her brother that I really hope doesn’t come up again any time soon."

    scene funnydildoscene22
    with dissolve

    sa "So...I guess it’s just us again..."
    s "I guess it is."
    s "What else do you have to do before we can get out of here?"
    sa "Are we...going somewhere?"
    sa "Because I wasn’t really lying about being tired..."
    s "Well, if you’re closing, there’s not really any point in hanging around, is there?"
    s "I figured I’d just walk you back to the dorm or something like-"

    "I inadvertently pause when I remember an important detail about the thing I literally {i}just{/i} thought about {i}not{/i} thinking about."
    "If her brother was killed while walking home, is something like that some sort of trigger for her?"
    "Is the sheer idea of walking home enough to evoke the same negative memories a lock of hair can?"
    "These are the things I’m forced to think about for her sake now."
    "All because she wanted to make something of hers mine."

    sa "...Sensei?"
    s "Oh, sorry."
    s "I just figured we’d walk back to the dorm or something."

    "It wouldn’t be the first time anyway."
    "I’m likely just overthinking things at this point."

    scene funnydildoscene23
    with dissolve

    sa "Sure..."
    sa "I’m just going to run up to my mom’s room to grab a few DVDs before we leave..."
    sa "Ayane’s been looking for a lot of...lighthearted romantic comedies lately and...I’m pretty sure my mom has a ton of those..."
    s "Don’t you need to finish cleaning first?"
    sa "I think it’s...clean enough, right?"
    sa "It’s not like we were...{i}extremely{/i} busy..."
    sa "Just...busier than normal..."
    s "Hey, you’re the employee. I’m just some guy who hangs out here and talks to you every once in a while."

    scene funnydildoscene24
    with dissolve

    sa "Then...in that case...wait here."
    sa "I’ll be right back."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Sana tosses the rag she’d been using to wipe down the counter into a large blue bin and quietly makes her way up the stairs."
    "I scan the room to see if maybe she missed a chair to push in or something like that. "
    "I don’t really know how nice this place is supposed to look when it closes."
    "And it’s not like I’d actually {i}help{/i} either since I’m not being paid."
    "But I could at least tell her about it when she comes back..."
    "………"
    "……"
    "…"
    "{i}Ten minutes later...{/i}"

    scene barnight
    with dissolve2

    s "…"

    "Sana still hasn’t come downstairs."
    "I was hoping things wouldn’t come to this as I am {i}also{/i} tired and really don’t want to summon the energy to go up there."
    "But I guess a real concern with her is that if a dresser fell down or something like that, she could be stuck beneath it for life."
    "I will save you, Sana."
    "Granted, I probably would have heard something if a dresser fell down or..."

    s "…"

    "Ugh."
    "Fuck it."
    "I sigh to myself and tap into my energy reserves and head for the stairs."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    if bonus == True:
        jump funnydildox
    else:
        "I go upstairs and Sana yells at me for not thinking she would be able to defeat a dresser in melee combat."
        "It is a very intense situation for the two of us and she cries a lot because of all of the dressers that have previously defeated her."
        "I think it is dumb that she would yell at me for her own weakness and tell her that her mom could probably defeat one."
        "Sana hates that even more and forces me to go home."
        "Dang it."

        $ renpy.end_replay()
        $ sana_love += 1
        $ bar50 = True
        stop music fadeout 5.0

        "{i}Sana’s affection has increased to [sana_love]!{/i}"
        "{i}Sana has defeated a dresser!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label bar55:
...
```

## Code that triggers this event
File: \game\SanaEvents.rpy
Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
    if sana_love >= 15 and bar10 == True and bar15 == False:
        jump bar15
    if sana_love >= 20 and day65 == True and bar15 == True and amisroom5 == True and bar20 == False:
        jump bar20
    if sana_love >= 25 and sanadorm20 == True and makidate1 == True and bar25 == False:
        jump bar25
    if sana_love >= 30 and sanadorm25 == True and day120 == True and bar30 == False:
        jump bar30
    if sana_love >= 35 and utamaid5 == True and christmas7 == True and bar35 == False:
        jump bar35
    if sana_love >= 40 and sanadorm35 == True and bar40 == False:
        jump bar40
    if sana_love >= 45 and thirdreset3 == True and futabadorm45 == True and bar45 == False:
        jump bar45
    if sana_love >= 50 and day351 == True and sarasex == True and sanadorm50 == True and bar50miss == False and bar50 == False:
        jump bar50
...
```