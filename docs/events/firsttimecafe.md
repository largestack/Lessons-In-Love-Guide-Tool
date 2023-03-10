# Guinea Pig (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 0



## Next events

None

## Event properties

* Id: firsttimecafe
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe
* Triggered by path: cafe->firsttimecafe

## Official wiki page

[Guinea Pig](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimecafe&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label firsttimecafe:
    play music "cafe.mp3" fadein 2.0
    scene cafe_day
    with dissolve

    "I decide to stop by the cafe after refusing breakfast from Ami a good four or five times."
    "It's nothing against her cooking. In fact, it kind of feels like Ami's carefully tailored her abilities to the best of my liking."
    "I just feel compelled to get out and actually do things every once in a while."
    "Or at least trick myself into thinking that I'm doing things when, in all actuality, I'm just roaming around in hopes of more easily bridging the first half of the day to the second."
    "Regardless, I am at the cafe now. And so I must do what is customary for any cafe-goer-"
    "Hit on the barista."

    q "Next customer!"

    scene cafe1
    with fade

    r "What can I get y-"

    scene cafe2
    with dissolve

    r "Wait, Sensei? I almost didn’t recognize you on account of the normal clothes and slightly threatening aura."
    s "Threatening aura?"
    r "Slightly threatening. Like a bear, but if the bear was asleep or missing both of its hind legs."
    s "Good. That's pretty close to what I was going for so I'm glad the change of clothes helped."

    scene cafe1
    with dissolve

    r "Weird seeing you drop by, though. Didn't take you for much of a coffee drinker."
    r "So, what can I get you?"
    s "I'll take, uhh..."

    menu:
        "Black coffee":
            s "Just a large coffee please."
            s "Unless you're going to force me to use whatever the Italian word for large is."
            s "If that's the case, I'll just leave with nothing."

            scene cafe3
            with dissolve

            r "No one actually {i}forces{/i} anyone to use those sizes, dude. They're more of a quirky suggestion than a flat out rule."
            r "Forcing people to say {i}Venti{/i} and {i}Grande{/i} and stuff is more like a...fun little movie thingy."
            r "But anyway, what do you take in your coffee? Milk? Sugar?"
            s "Just black, please."

            scene cafe2
            with dissolve

            r "Woah, really? You're not just trying to upgrade your slightly threatening aura to full on threatening, are you? Cause I wasn't trying to wake the bear."
            s "Nope. That's just how I drink coffee."
            r "And you're not just trying to make things easy for me either?"

            scene cafe4
            with dissolve

            r "Because I’ll have you know I’m pretty great when it comes to this barista stuff."
            r "Humble brag, but I can kind of run circles around the rest of the staff here."
            s "Impressive, but no. I really do just drink my coffee black."
            r "If you say so. At least it’ll be easy to remember your order."
            s "Who says I’m coming back? You still have a chance to blow this."

            scene cafe2
            with dissolve

            r "How could anyone mess up a black coffee? You just...pour it into a cup."
            s "Honestly, you would be surprised."

            scene cafe4
            with dissolve

            r "Guess I'll just have to take your word for it."
            r "Total's 200 yen, Sensei."
            s "Is that before or after my teacher discount?"
            r "Oh, sorry. My b."
            r "New total is 500 yen, Sensei."
            s "Wait, why did the total go up?"
            r "Probs cause I used my employee discount on you. But hey, if you want to feel cool and use the teacher one instead, be my guest."
            s "No, I think I'm fine with being an employee for the length of this transaction. Thanks, Rin."
            r "I gotchoo, pal."
            r "Now go grab a seat and I'll bring your coffee right over."
            jump chosedrink

        "(Copyrighted frozen beverage)":
            s "I’ll take one (copyrighted frozen beverage) please."

            scene cafe3
            with dissolve

            r "Gotcha. One (copyrighted frozen beverage) coming right up!"

            scene cafe2
            with dissolve

            r "I’m surprised, though. Ordering a feminine drink like that really makes your slightly threatening aura even {i}less{/i} threatening."
            r "Now, it's like you're an unconscious bear without any legs at all."
            s "Not only girls can enjoy (copyrighted frozen beverages), you know."
            s "Sometimes, even a manly man like me likes to kick back and relax with a nice, cold (copyrighted frozen beverage)."

            scene cafe3
            with dissolve

            r "Right, right. I guess you were just so masculine that I expected you to order a bowl of nails and beard oil."
            s "I have no use for beard oil without a beard."
            r "You still want the nails, then?"
            s "Extra nails, actually. Thank you for asking."
            r "Damn, you're actually pretty good at this barista banter, Sensei. Most people would've said something really awkward or lame by now and here you are about to eat nails for me."
            r "I admire your dedication."
            s "So, what do I owe you?"
            r "Total is 600 yen. You can just leave your money on the counter and go take a seat. I'll bring it over when it's ready."
            jump chosedrink

        "Tacos":
            s "I’ll have the tacos, please."

            scene cafe6
            with dissolve

            r "The what?"
            s "Tacos. The small, tortilla shell filled with meat and other various ingredients."
            r "Have...Have you ever been to a cafe before? Or are you just guessing what's on the menu? Because all the stuff we have is listed right above-"
            s "It's tacos or nothing, Rin."
            r "Sensei, we don't sell tacos here."
            s "Then why was I even given this option? That doesn't make any sense."
            r "What option? What are you talking about?"
            s "Forget it. I'll just have a black coffee instead."

            scene cafe2
            with dissolve

            r "Woah, really? You're not just trying to upgrade your slightly threatening aura to full on threatening, are you? Cause I wasn't trying to wake the bear."
            s "Nope. That's just how I drink coffee."
            r "And you're not just trying to make things easy for me either?"

            scene cafe4
            with dissolve

            r "Because I’ll have you know I’m pretty great when it comes to this barista stuff."
            r "Humble brag, but I can kind of run circles around the rest of the staff here."
            s "Impressive, but no. I really do just drink my coffee black."
            r "If you say so. At least it’ll be easy to remember your order."
            s "Who says I’m coming back? You still have a chance to blow this."

            scene cafe2
            with dissolve

            r "How could anyone mess up a black coffee? You just...pour it into a cup."
            s "Honestly, you would be surprised."

            scene cafe4
            with dissolve

            r "Guess I'll just have to take your word for it."
            r "Total's 200 yen, Sensei."
            s "Is that before or after my teacher discount?"
            r "Oh, sorry. My b."
            r "New total is 500 yen, Sensei."
            s "Wait, why did the total go up?"
            r "Probs cause I used my employee discount on you. But hey, if you want to feel cool and use the teacher one instead, be my guest."
            s "No, I think I'm fine with being an employee for the length of this transaction. Thanks, Rin."
            r "I gotchoo, pal."
            r "Now go grab a seat and I'll bring your coffee right over."
            jump chosedrink

label chosedrink:
    scene black
    with dissolve

    "I reach into my pocket for a few coins and place them directly into a tray on the counter before heading back over to find somewhere to sit."
    "Or, at least that's what I {i}would{/i} be doing if I actually intended to hang around, which I most certainly do not."
    "Should I have informed Rin of this at the time of placing my order? Maybe. But she also should have asked."
    "So now there is not much to do apart from standing awkwardly in the middle of the cafe and waiting for her to return..."
    "........."
    "......"
    "..."

    scene cafe7
    with dissolve

    r "Yo, why are you being such a sketchball? I told you to go find a seat."
    s "I meant to order my drink to-go."
    r "You know you...can still sit down if you order something to-go, right? Then just...get up once it's ready?"
    s "Or I could remain standing and make everyone here equally uncomfortable."
    r "I mean...{i}I guess?{/i}"
    s "So, do you have my drink?"

    scene cafe8
    with dissolve

    r "Yup! Got it right here."

    "Rin hands me my order and smiles at me in what seems to be anticipation, constantly shifting her gaze from me to the drink I'm holding."

    s "…"
    r "…"
    s "Are you going to watch me drink it?..."

    scene cafe9
    with dissolve

    r "Ah- sorry! I was just curious about whether you’d like it or not."
    s "I mean, I did order it. I wouldn't have bought something if I wasn't sure I'd like it."

    "Wanting to appease Rin and quell how uncomfortable this is beginning to make me, I bring the beverage to my mouth and-"

    s "..."
    r "So? Good?"
    s "I mean...yeah. But..."
    r "But what? Tell me."
    s "Rin, this isn't even close to what I ordered."

    scene cafe10
    with dissolve

    r "No. I suppose it is not."
    s "..."
    r "..."
    s "Well, is there an explanation for that? Or..."

    scene cafe11
    with dissolve

    r "Oh, I guess. Though, it's less of an explanation and more of just me using you as a guinea pig."
    r "You see, that's a custom recipe of mine. And I’ve been trying to get my manager to add it to the menu, but she’s been all like, “No way! You can't just change the menu, Rin!”"
    r "So, I figured if I was able to actually get some more people on my side, I might be able to persuade her."
    s "I see..."
    r "So, now that you've tried it and liked it, I'm going to need you to write on one of her comment cards that I'm the best barista ever and that she should listen to me more."
    s "I'm not sure if I can, in good faith, call you the best barista ever when you didn't even bring me my actual order."

    scene cafe12
    with dissolve

    r "I swear I was going to right after you tried this one!"
    r "Here, I'll even go get it right now. I just-"
    s "It's fine, Rin. I'll just keep whatever this is instead."
    s "It really {i}is{/i} good."

    scene cafe13
    with dissolve

    r "You...You really think that? And you're not just lying to me because it's customary to flirt with your barista?"
    s "I really think that. I'm going to need one of those comment card things if I'm going to recommend it to your manager, though."

    scene cafe14
    with dissolve

    r "Yeah! Totally! I'll go get one right now!"
    r "Just hang tight, okay?! I'll be right back!"

    scene black
    with dissolve2

    "Rin quickly dashes to the counter to grab me a card and I wind up having to sit down after all."
    "Unfortunately, a wave of customers all decide to show up at once and I'm unable to continue talking to her once I have my comment written."
    "Not knowing how long it will be until she's free again, I wait for a moment where she's distracted and place the card down on the counter before leaving."
    "And as I step out into the street with an indiscernible beverage in my hand, I come to realize something."
    "It's that I am now only slightly more than a lab rat."
    "And that the future of my beverage choice hangs in great jeopardy at the hands of a single teenager."

    scene black
    with dissolve

    $ renpy.end_replay()
    $ firsttimecafe = True
    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdayafternoon

label cafe2to4:
    scene cafe_day
    with dissolve
    play music "cafe.mp3" fadein 2.0

    "I head to the cafe to grab a quick cup of coffee and a bite to eat."
    "Rin remembers my order from last time, but still decides to make me some super secret mystery-concoction instead."
    "Even though I have no idea what’s in it, it tastes great...And it makes her happy knowing that I like it."
    "I hang out for the next couple hours playing games on my phone before deciding to get on with the rest of my day."

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0

    scene black
    with dissolve

    "........."
    "......"
    "..."
    jump saturdayafternoon

label cafesugar:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
...
```