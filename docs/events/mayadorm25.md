# FLAVOR BEAM!
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayadorm25&go=Go)



## Event preconditions
✅Maya love greater than or equal to 25

✅Event "[Maya: Watermelons and Violin](./shrine25.md)" is completed (event=shrine25)



## Next events
* [Main: The Value of Sharing](./halloween1.md)
* [Ami: Cute Girls and Stuff](./amisroom20.md)
* [Maya: What it Means to Be Destroyed](./mayadorm30.md)

## Event properties
* ID: mayadorm25
* Group: Maya
* Triggered by label: mayadorm
* Triggered by branch label: mayadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label mayadorm25:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "…"
    "I knock on Maya’s door and hope that, whenever she answers, I won’t be asked to carry anything across town again."
    "As much as I like spending time with her (For whatever reason that I actually do), I’m not the biggest fan of physical activity that doesn't result in my penis being submerged in a teenager."
    "But hey- Maybe Maya will be insatiably horny tonight and go against her better judgement to finally sleep with me."

    play sound "dooropen.mp3"
    scene flavorredux1
    with fade

    m "Oh, good. It's the last person I wanted to see."

    "Or maybe she won't and I'll just have to jerk off before going to sleep tonight."

    s "Hey, Maya. I just figured I'd stop by to see what you were doing tonight."
    m "..."
    m "Why? "
    s "Why not?"
    m "You’re not beginning to think we’re friends, are you?"
    m "I know that a lot of what I’ve been saying lately could be easily misinterpreted as us {i}getting closer,{/i} but I didn’t think you’d go this far."
    s "You know we don’t have to be friends to hang out, right?"
    m "Are you suggesting that we remain in each other’s company for the sole purpose of belittling one another?"
    s "Sure. Whatever works for you."

    scene flavorredux2
    with dissolve

    m "Hm...This may be a form of companionship I wouldn't outright reject."
    m "You have given me much to think about."

    scene flavorredux1
    with dissolve

    m "Please note that I am extremely exhausted tonight, though. And that I will very likely spend this time ranting about life or the world or something."
    s "Just to make sure, you {i}are{/i} the real Maya, right?"
    s "Because having you actually agree to spending time with me so shortly after that conversation about you being swapped with a {i}new{/i} Maya is very concerning."

    scene flavorredux3
    with dissolve

    m "Yes...I’m the normal Maya."
    m "Like I said, I’m just exhausted."
    m "As much as I like confusing you, doing it every single day can get really taxing after a while."
    s "Well, maybe there’s something I can do to help you re-"

    scene flavorredux1
    with dissolve

    m "Please don’t finish that sentence. Cleaning vomit out of this carpet is not a thing I want to be doing tonight."
    s "I’m honestly surprised you let me get as far into it as I did."
    m "As am I. I’m clearly off my game tonight."
    s "Then what do you suggest we do to get you back into it?"

    scene flavorredux4
    with dissolve

    m "Well, in a perfect world, I’d suggest that you leave me alone and I go out to eat by myself."
    m "But perfect worlds are clearly not something I have any experience with."
    s "So you’re suggesting that we go out to eat together?"
    m "I think what I’m suggesting is more along the lines of you following ten feet behind me and paying for my dinner."
    s "So kind of like that one time we went to the takoyaki truck?"
    m "Correct."
    s "..."
    s "This is just {i}another{/i} invitation to the takoyaki truck, isn't it?"

    scene flavorredux1
    with dissolve

    m "Incorrect."
    m "We’ll be going somewhere a little different tonight."
    s "Different?"
    m "You’ll see."
    m "But please hide your wallet, for where we're heading is very dangerous. Especially for people like you."
    s "I have many questions all of a sudden."
    m "Please keep them to yourself. Talking requires energy and I am scarcely low on that right now."

    scene black
    with dissolve2

    "Maya casually walks past me and I’m left with no choice but to follow her."
    "We move through the streets at a relatively brisk pace, which I imagine is only due to the fact that she’s hungry."
    "One thing I’ve noticed about her is that the only time she ever moves with any sense of urgency is when there is food involved."
    "And given that she likely won’t be paying for herself tonight, I can only imagine how excited she must be..."
    "………"
    "……"
    "…"

    scene mayamaid1
    with dissolve

    m "..."
    s "..."
    s "Maya, where did you bring me?"
    m "Hell."
    s "Hell is a lot...brighter than I expected it to be."
    m "You should see the other place."
    s "Is this a-"
    m "Maid cafe. Bingo."
    s "Why did you bring me to a maid cafe in the middle of the night?"
    s "And why are they even open this late?"

    scene mayamaid2
    with dissolve

    m "I didn’t bring you anywhere. You followed me here. Remember?"
    s "Well, since I followed you here, I assume you’re going to be paying for yourself then?"
    m "No. There is an admission fee for spending time with me. You may use that to cover tonight's bill."
    m "Also, I seem to have misplaced my wallet."
    m "Whatever will we do?"
    s "Okay, I'll pay for you. But-"
    m "Thank you for accepting my conditions without asking for anything in return. I appreciate it."
    s "..."

    "I sigh to myself and lean back in my chair, receiving the answer I more or less expected."
    "This is the first time I’ve been to a maid cafe since waking up in Kumon-mi. "
    "I didn’t even know one of these existed here, but I guess it makes sense given that virtually everything else seems to exist here as well."
    "I wonder why there are no other customers, though?"

    s "Is this...somewhere you come often?"

    scene mayamaid1
    with dissolve

    m "Lately, yes. "
    m "It’s surprisingly cheap for the sizable portions they give you."
    m "Plus, maids are cute."

    if bonus == True:
        m "But I’m sure you already know this given that all you think about are [young_girls]."
        s "Can you say “Maids are cute” again really quick? It was really out of character and I want to engrain it into my memory."
        m "I refuse."
    else:
        s "I refuse to weigh in on how I feel about them as it would imply that I see them as anything other than women just trying to make a decent living."

    scene mayamaid2
    with dissolve

    maid "Ah! You’re back! "
    maid "I must have missed you at the door, Princess Maya!"
    m "For the millionth time, just Maya is fine. "
    m "Being called a princess makes me nauseous."
    s "You’ll always be a princess to me."

    scene mayamaid3
    with dissolve

    m "I will destroy you."

    scene mayamaid4
    with dissolve

    maid "Oh! You brought a new customer this time! And he’s so handsome as well!"
    maid "Good evening, Master!"
    u "My name is Uta-chan and I’ll be taking {i}veeeeery{/i} good care of you today~!"

    scene mayamaid5
    with dissolve

    u "So if there’s {i}aaaaanything{/i} you need, feel free to let me know and I’ll do whatever I can to make your deepest desires come true!"
    m "You will immediately regret saying that to him."
    u "Your wish is my command while you’re inside this cafe, Master! Anything you want, you can have!"
    s "Please marry me."
    u "Awww! That's so, so sweet of you!"

    scene mayamaid6
    with dissolve

    u "But unfortunately, us maids are forbidden from marrying any of our guests. It's just one of the rules here, unfortunately."
    s "I will wait for you forever."

    scene mayamaid7
    with dissolve

    m "Can I order dinner now? Or do you want to hit on Uta-chan some more?"
    s "I’d like to hit on Uta-chan some more if that's okay."
    m "It's not."
    u "Sorry, Princess Maya. I was just so excited to see a new face that I almost lost myself for a second."
    u "But I’m here for {i}you{/i} now! So please tell Uta-chan how she can make your dreams come true tonight!"

    scene mayamaid8
    with dissolve

    m "Omurice and a black tea, and the freedom to go the rest of the night without being called a princess."
    u "But you {i}are{/i} a princess while you’re inside the cafe! And it’s my duty to make you feel more special than you’ve ever felt before."
    m "Call me a princess again and I am never coming back."

    scene mayamaid9
    with dissolve

    u "You’re more fun when you come by yourself."

    scene mayamaid10
    with dissolve

    u "You’ll keep on visiting me, though...Right, Master?"
    s "I will do anything you want me to do, Uta-chan."

    scene mayamaid11
    with dissolve

    u "Oh? {i}Anything,{/i} you say?"
    s "I will kill for you. All you have to do is ask."
    u "You don’t need to go that far, Master. As long as you’re happy, I can find it within myself to keep going on."
    u "And also, it would make me {i}super-duper{/i} happy if you’d buy an extra dessert or two~!"
    s "I will take one of everything you have."

    scene mayamaid12
    with dissolve

    u "E-Everything?!"
    m "Do you see now why I said this place was dangerous for people like you?"
    s "Shut up, Maya. I'm talking to Uta-chan."
    u "You’ve made me the happiest maid in the whole gosh-darn world, Master! Thank you so, so much!"
    u "Now, I’ll be back in a jiffy while I start getting stuff ready! But don’t miss me too much, okay?"

    scene mayamaid13
    with dissolve

    m "..."
    s "..."
    s "I already miss her."
    m "You’re disgusting."
    s "Hey, you’re the one who brought me to a maid cafe. You should know full-well how I’m going to act in a place like this."
    m "I knew it would be bad, but I didn’t think you’d propose within the first thirty seconds."
    s "And {i}I{/i} didn’t think I’d meet the girl of my dreams."

    scene mayamaid14
    with dissolve

    m "You {i}are{/i} aware that it’s all just an act, right?"
    m "She’s just trying to coax more money out of you."
    s "Of course I’m aware of that."
    s "No idiot goes into a maid cafe without knowing that they’re going to be swindled. That’s like half of the charm."
    m "So...you intend to just let her rob you?"
    s "If an undisclosed amount of desserts is the price to pay for a smile like that, I’ll buy them every day for the rest of my life."

    scene mayamaid15
    with dissolve

    m "I’m sure Ami would be thrilled to hear that."
    s "Ami can never know that we came here together."
    m "I have no intention of telling her that I willingly spent time with you, so that is fine by me."
    s "So, back to how cute you think maids are-"
    m "No. Not back to that."
    s "Have {i}you{/i} ever considered working in a place like this? Because I think you could pull off the outfit really well."

    scene mayamaid16
    with dissolve

    m "What part of “Not back to that” don’t you understand?"
    m "Of course I’ve never thought about working in a place like this."
    m "It’s annoying enough having to put on the shrine maiden dress every weekend. Putting on another, equally complicated uniform after that is far too much effort for me."
    s "But think about how cute you'd look."
    m "I am already cute. I don't need a costume to feel even more attractive."
    m "Plus, if I had to even think about talking to anyone the way these maids are forced to, I’d probably burst into flames."
    s "Do you want to try calling me Master once to test it out?"
    m "Do you want to jump off of a bridge?"

    scene mayamaid17
    with dissolve

    u "Hey! You be nice to him! That’s my Master you’re talking to!"

    "Uta-chan comes back to the table to drop off Maya’s food. I fall in love again in the process."

    scene mayamaid18
    with dissolve

    u "Master, I’m so {i}so{/i} sorry, but all of the desserts you ordered are gonna take a liiiiittle bit longer to prepare, okay?"
    u "The maid in the kitchen wasn’t expecting someone to be kind enough to order so many things, so she needs a teensy bit more time if that's okay."
    s "I will wait forever if I have to."

    scene mayamaid19
    with dissolve

    u "Aww, shucks...You're too kind to me already..."
    u "Keep saying things like that and I might just fall for you."
    m "I’m going to be sick."

    scene mayamaid20
    with dissolve

    u "Not if I cast a spell on your meal, you won’t!"
    m "Why do you always do this? I just want to eat."
    u "Because it’s my job, silly!"
    m "Please don't."

    scene mayamaid21
    with dissolve

    u "Happy days, happy nights, fill this meal with such delight~"
    u "Taste so sweet the girl will squeal...Uta-chan doth bless this meal!"
    m "Doth? Is this Shakespeare?"

    scene mayamaid22
    with hpunch

    u "FLAVOR BEEEEEEEAAAAAAAAAAM!!!!!!!!!"
    m "…"
    u "…"
    m "…"
    u "…"

    scene mayamaid23
    with dissolve

    m "Can I eat now?"

    scene mayamaid24
    with dissolve

    u "Of course!"
    u "Enjoy your meal, Princess!"

    scene mayamaid25
    with dissolve

    "Uta-chan disappears back into the kitchen and, once again, Maya and I are left on our own in the middle of a maid cafe."
    "That is not a sentence I ever expected to think."

    s "Do you think she’ll cast the flavor beam on each one of my desserts?"
    m "Most likely."
    m "She does it to the check as well."
    m "She uses the flavor beam on everything."
    s "She should cast it on you and see if it turns you into a more bright and cheerful person."
    m "She’s tried before."
    m "This is the result."
    s "Why do you keep coming here if you seem so annoyed by everything?"
    m "I already told you. Cheap food, large portions."
    m "You have seen me eat. You must understand how much of a blessing this is."
    s "Wouldn’t it make more sense to just...cook for yourself then? It would be cheaper, too."

    scene mayamaid26
    with dissolve

    m "Cooking...may be a weakness of mine."
    m "I have accepted this. Please do not torment me for it."
    s "I won’t torment you. I can’t cook either."
    s "We can just force Ami to cook for us for the rest of our lives."
    m "My only condition is that we eat in separate rooms."
    m "If you can agree to that, I will accept this proposition."
    s "I’ll draft the formal paperwork and have her sign it in the morning."
    m "Understood. It has been a pleasure doing business with you."

    scene black
    with dissolve2

    "Maya manages to finish her entire meal before Uta comes back with...way too many desserts."
    "After the flavor beam is cast on every one of them, Maya forces me to box them up so that she doesn’t have to stay and watch me eat everything in one sitting."
    "Obviously, I wouldn’t be able to do that even if I tried, so I wind up taking everything to go without much question."
    "We leave shortly after that..."
    "But part of me wishes that I could have stayed and talked to my future wife for a little while longer..."

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayadorm25 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amidorm20:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
        if maya_love >= 10 and day != 1 and day != 5 and mayadorm5 == True and mayadorm10 == False:
            jump mayadorm10
        if maya_love >= 15 and shrine15 == True and mayadorm15 == False:
            jump mayadorm15
        if maya_love >= 20 and shrine20 == True and yumidorm10 == True and mayadorm20 == False:
            jump mayadorm20
        if maya_love >= 25 and shrine25 == True and mayadorm25 == False:
            jump mayadorm25
...
```