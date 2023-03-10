# Couple's Discount (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 43

* Event [Something Darker](./amisroom10.md) (Ami) is completed)

* Event [No Romeo](./day24.md) (Main) is completed)



## Next events

* [Ami: Ode to a Marsh Warbler](./aminew2.md)

## Event properties

* Id: aminew1
* Group: Ami
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->aminew1

## Official wiki page

[Couple's Discount](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=aminew1&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label aminew1:
    scene aminewone1
    with fade
    play music "10c.mp3"

    a "And that’s exactly why I don’t think we should have gym class anymore."
    s "This breast envy of yours is really starting to get out of hand if you’re thinking of rebuilding the education system to cope with it."

    scene aminewone2
    with dissolve

    a "Breast envy is something that millions of girls struggle with every day, Sensei! We all know that it’s not just me who feels this way. Right, Maya?"
    m "Please don’t include neither me nor my breasts in any conversation our teacher is a part of. "
    m "In fact, please don’t include my breasts in {i}any{/i} conversation. Especially when I don’t feel the same sort of envy you do."

    "I somehow wind up walking  back from school with Ami and two other girls who could probably pass for residents of my home on a census test if things really came down to it."
    "Why I was forcibly dragged along when the smallest of the bunch seems to almost always stray from anything that I’m a part of, I’m not sure. "
    "But here we are, talking about breasts or the lack thereof on the way to..."
    "To..."

    s "Where exactly are we going again?"

    scene aminewone3
    with dissolve

    ay "Excellent question, future husband! We’re on our way to a cafe not far from here so we can take advantage of the couple’s discount they’re offering."
    a "We tried going as a trio last time but...things didn’t really work out the way I expected them to. "

    scene aminewone4
    with dissolve

    ay "It’s not a {i}trio,{/i} Ami. It’s called a {i}throuple.{/i} And the fact that the cafe would not offer us a discount proves that they are bad people who don’t care about inclusivity."
    a "Then...why are we going back exactly?"

    scene aminewone5
    with dissolve

    ay "Because we’re hungry and you kept looking at pictures of the parfaits they’ve been posting on Instagram all day saying, “Wow. I want to go there.”"
    ay "Oh. And we also have four people now."
    s "So, which one of you am I dating today?"
    ay "All of us. We are a quadrouple- a real type of thing that actually exists. And if the cafe doesn’t like that, they will be met with destruction."

    "As you can see, it’s a pretty normal day for me. "
    "I’m not sure how I’m going to deal with walking into a cafe for a couple’s discount with three girls who could pass for my daughters but I guess that’s a problem I’ll have to figure out how to handle later."
    "And, as much as I’d like to say that the cafe will probably just assume I’m their teacher, I can’t really see how that would be any better than a parent."
    "In fact, that would probably be even worse."
    "Honestly, I think I’m kind of screwed either way. But at least I also get to screw three girls in the process."
    "Just in the less fun way."

    scene aminewone6
    with dissolve

    a "Are you sure you’re okay with tagging along, Sensei? You...didn’t have anything else to do tonight?"
    s "Since when do you care about whether or not I’m free? Isn’t wanting to be with me every waking hour of the day like, half of your personality?"

    scene aminewone7
    with dissolve

    a "Is the other half being lovable and fun and nice and cute and kind and cute? And also cute?"
    s "No. It’s being annoying."

    scene aminewone8
    with dissolve

    a "Mm!"
    ay "Don’t worry, Ami! I think you’re all of those things. But I think you may have forgotten to mention your best quality which is, in my opinion, how cute you are."

    scene aminewone9
    with dissolve

    a "How come you can’t be more like Ayane?"
    s "I don’t really have the self-confidence to be hitting on myself all day long."
    a "Not that part. The part with how much she appreciates me and how she calls me cute even when I don’t have to tell her to."
    s "Probably because walking around school and talking to people about how cute my niece is would likely put me on some sort of list somewhere."
    m "I think that might be the most reasonable thing I’ve ever heard you say."
    ay "I’m not related to you, Sensei. You can call me cute as many times as you want and you won’t even have to worry about any lists since I am rich and can get you out of trouble if I have to."
    s "Is {i}that{/i} really what you want me to be, Ami? Are you sure?"
    ay "You’d think I’d be offended by getting called {i}that,{/i} but it really just made me super excited instead."

    scene aminewone10
    with dissolve

    m "Ew."
    a "Okay, so maybe {i}don’t{/i} be more like Ayane. But you are allowed to dote on me {i}a little{/i} bit, you know."
    a "Everybody already knows we’re close, so no one is going to put you on any list if you just remind them every once in a while that I am your entire world and that you are mine."
    ay "Ami’s right, Sensei. You should really cherish her more."
    a "See what I mean? If-"
    ay "Especially since you’ll be running away with me and never looking back as soon as I graduate. If you’re not nice to Ami now, how will she remember you when that happens?"

    scene aminewone11
    with dissolve

    a "Just go home if you’re going to say things like that, damn it!"

    scene black
    with dissolve2

    "Of course, Ayane doesn’t wind up going home since she is apparently the only one who remembers how to get to the cafe."
    "I highly doubt Ami is being serious when she says things like that anyway, though."
    "Even with how relentless Ayane’s flirting can be, it’s clear that she and Ami are extremely close and that it’s {i}probably{/i} just all in good fun."
    "Do I think Ami would cause physical harm to {i}someone else{/i} for doing what Ayane does? Absolutely."
    "At the bare minimum, I think she’d try."
    "But I think that, for whatever reason, Ayane gets a free pass."

    scene aminewone12
    with dissolve2

    "Eventually, we make it to what seems like less of a cafe and more of a hole in the wall that just happens to have a dessert menu."
    "It must be relatively new since there are still barely any decorations on the walls and the entire back half of the store is blocked off for some reason."
    "I can’t say I’m really looking forward to spending my night here on account of the entire menu being full of things I wouldn’t typically consume, but..."
    "At the very least, I have enabled the couple’s discount the girls were after."
    "Unless Ayane proceeds to ruin everything again by saying that we are a “quadrouple.”"

    barista "Welcome in! Table for four?"
    ay "Two tables for two, actually! We’re here for the couple’s discount."
    barista "Oh, sure! I take it you two girls are a couple then?"
    ay "We are!"
    m "I have never seen this girl in my life."

    scene aminewone13
    with dissolve

    ay "{i}Maya, what are you doing?{/i}"
    m "What? It’s only a 10%% discount. I’m going to be spending basically the same amount of money either way."
    ay "{i}Okay, but that’s not why we’re doing this, remember?{/i}"
    m "..."
    barista "Um..."
    ay "Just go along with it and {i}I’ll{/i} pay for you, okay?"

    scene aminewone14
    with dissolve

    m "I am in love with this woman."
    ay "Hahah...hah..."
    barista "Oh! Well...that would certainly make the two of you a couple then."
    barista "Follow me right this way. I’ll take you to a table in the back where you two won’t be interrupted."
    m "Good. I would not want someone to overhear me talking about all of the love that I have for this person."

    scene aminewone15
    with dissolve

    barista "And you two near the door, will you also be-"
    barista "Wait...I’m sorry, Sir. But you seem a little too old to be-"
    a "I consent to a romantic relationship with this man and am not being taken here against my will."
    s "..."
    barista "..."
    a "..."
    s "I’m her uncle and we don’t need the discount."

    scene aminewone16
    with dissolve

    a "Sensei, what the heck?! We were so close."
    s "It’s fine. I’m going to be paying anyway and a 10%% discount is not worth what little pride I have left."
    s "If it were 20%%, that would be a different story."
    barista "A...table near the window it is, then."
    barista "Please wait one moment."

    scene black
    with dissolve2

    "Ayane and Maya are taken to a table in the back to make out or something while Ami and I wait near the door for the barista-slash-waitress or whatever she is to return."
    "We’re seated shortly after and Ami, who apparently does not care at all about how much money I am willing to spend today, orders way too much food."
    "Surprisingly, it’s all taken over to us within five minutes- along with a complimentary pot of hot tea that I {i}will{/i} consume, unlike all of the other brightly colored desserts that have now joined us at the table."

    scene aminewone17
    with dissolve2

    a "You know, Sensei...I really wouldn’t have minded if you just decided to go along with the couples thing."
    a "I have done my research and know what I have to say to avoid getting you into trouble with anyone who does not understand the way we feel about one another."
    s "What way? We’re literally just related and haven’t done anything romantic together."
    a "Right, yeah. I obviously know that. But what I’m saying is that we {i}could{/i} and it would be okay because I’ve done my research."
    s "Is there something you’d like to admit to me, Ami? Like...perhaps something about your feelings for me?"

    scene aminewone18
    with dissolve

    a "Boy! This cake sure looks good, doesn’t it?!"
    s "..."
    a "I’m so glad that my uncle, who I’m not romantically involved with, is buying it for me today on this totally normal day of no importance whatsoever!"
    s "You should be glad. I’m spending probably an entire day’s worth of pay at this place for you."

    scene aminewone19
    with dissolve

    a "Yeah, but that’s your fault. You could have afforded another parfait if you just swallowed {i}what little is left of your pride{/i} and pretended to be in love with me."
    s "I’m not even going to eat {i}this{/i} parfait. Parfaits are not currency and mean nothing to me."
    a "Why would you even order it then?"
    s "Because the alternative would have been sitting here without any food. And there is nothing more disconcerting than an older man bringing a young girl to a cafe and just...watching her eat."

    scene aminewone20
    with dissolve

    a "Yeah...I guess it does sound kinda weird when I think of that happening with any other couple."

    scene aminewone21
    with dissolve

    a "But you and me are different, I think."
    a "I think that we look like the type of couple who could do pretty much anything normal couples do."
    a "Because even if we might seem mismatched on the outside at first...the way we feel about each other shines brighter than a sea of diamonds and cuts through the outside entirely."
    a "I think that anyone who takes a look at us...a {i}real{/i} look and not just a quick one...I think that anyone who does that will understand that what we have isn’t that abnormal at all."
    s "..."
    a "..."
    s "And I think you’re insane."

    scene aminewone22
    with dissolve

    a "Hahahah! Maybe I am!"

    scene aminewone23
    with dissolve

    a "But I know that if I were to change...and if I were to stop being as annoying as you say I am...that you’d change too."
    a "And that’s the last thing I want."
    a "I love you exactly the way you are, Sensei. Flaws and all."
    a "And I’m happy you came here with me today."

    scene aminewone24
    with dissolve

    a "Even if we didn’t manage to get the couple's discount."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene aminewone25
    with dissolve2

    ay "Say {i}aaaaahhh...{/i}my sweet, little princess."
    m "How dare you take advantage of my one and only weakness like this. You will rue the day, Ayane."

    scene aminewone26
    with dissolve

    ay "You say that, and yet I’ve already fed you an entire parfait. Don’t pretend you’re not enjoying this, Maya. Because if you weren’t, you wouldn’t keep opening your mouth for me."
    m "Please don’t say such revolting things while there is food on the table."
    ay "You really think it’s revolting?"

    scene aminewone27
    with dissolve

    m "Well..."
    m "Maybe not as revolting as it {i}could{/i} be..."
    ay "..."
    m "..."
    ay "When do you think he’ll remember it’s her birthday?"
    m "Hopefully soon. I even flat-out reminded him the other day."
    ay "Oh? When did that happen?"
    m "When he decided to be annoying and stop by the shrine for literally no reason other than to bother me."
    ay "..."
    m "I don’t get it at all. What do you two even see in him? He has literally zero good qualities."
    ay "Probably the same thing you do."

    scene aminewone28
    with dissolve

    m "Huh? Me?"
    m "Are you confusing me with someone else? Because I do everything I possibly can to stay {i}away{/i} from him."
    ay "I guess I’m confusing you with someone else then."
    m "..."
    ay "..."

    scene aminewone29
    with dissolve

    m "He’s not..."
    m "He’s not going to remember at all, is he?"
    ay "..."
    m "..."
    ay "There’s always next year."

    scene black
    with dissolve2

    "We stay at the cafe for a little over an hour before we decide to head home."
    "And, in case you were wondering, I did wind up eating the parfait."
    "It was just okay."

    $ renpy.end_replay()
    $ ami_love += 1
    $ aminew1 = True
    stop music fadeout 6.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label aminew2:
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
...
```