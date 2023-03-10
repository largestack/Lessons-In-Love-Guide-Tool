# Die For What You Believe In (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Where Puppies Roam Free](./beachvacation10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation11
* Group: Main
* Triggered by label: beachvacation10
* Chain sources: beachvacation10
* Chain sources path: beachvacation10

## Official wiki page

[Die For What You Believe In](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation11&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation11:
    scene mollymaya1
    with dissolve
    play music "justbehappy.mp3" fadein 4.0

    mo "Well, well, well! Glad you decided to join us, Sir!"
    m "Yes. Very glad. Hooray."

    "I find Molly and Maya hiding from the sun under a slew of parasols on my way down the beach."

    s "When you said you were bringing multiple umbrellas, I didn’t really believe you. "

    scene mollymaya2
    with dissolve

    mo "Well, you should have! Without constant protection from the sun, I’m as good as dead. "
    mo "I don’t know how you Japanese people handle these harsh Summers so well. I feel like I’m being tossed into the depths of Orodruin every time I step outside."
    s "I have no idea what that is."
    mo "Then you have much to learn! Perhaps the two of us should retreat back to the inn and have ourselves a Lord of the Rings marathon? Aye, Supreme Overlord?"
    s "You’re just trying to escape from the outdoors again, aren’t you?"

    scene mollymaya3
    with dissolve

    mo "Guh...I had no idea you could read minds as well..."
    mo "This is concerning for a number of reasons."
    s "That aside...how are you, Maya? I didn’t really see you at all yesterday once we got to the beach."
    m "Correct. I was beginning to think my plan of avoiding you was going to keep up for the full 48 hours."
    m "I regret to see that this is very much not the case."
    s "Thanks. I missed you too."
    m "Please go away."

    scene mollymaya4
    with dissolve

    mo "Are you two like arch nemeses or something? I haven’t really been around long but every interaction you’ve had together since I joined the class has been pretty toxic."
    mo "Even thought about reporting you to the GMs on one or more occasions for gameplay sabotage."
    m "This isn’t a game. This is real life."

    scene mollymaya5
    with dissolve

    mo "What do you know, Maya?!"
    m "A little too much, I’m afraid."
    mo "Well, it’s a game to me. And it’s a game to the Supreme Overlord as well."
    s "I don’t even know what we’re talking about right now."

    scene mollymaya6
    with dissolve

    m "Strange. It appears as if we might actually be on the same page for once. "
    m "Though, I suppose that makes sense given that Molly is perhaps the only person I know who is more delusional than you."

    scene mollymaya1
    with dissolve

    mo "Did ya hear that, Sir? We’re brothers in arms. Fellow degenerates."
    mo "Who cares if the world doesn’t understand how you and I look at it? As long as we’re leveling up our stats with everybody, I’m sure we’ll survive."
    s "Molly, why did you come here again? You’re really not suited for the outdoor world."

    scene mollymaya7
    with dissolve

    mo "Well, it was to play D&D. But now that that’s over I’m kinda just floatin’ out in the Twisting Nether until the next time we all meet up."
    s "Oh, are you guys not playing again tonight?"
    m "We are not. "
    m "Ayane’s character died so she needs time to prepare a new one."
    mo "There’s the issue with Futaba as well."
    mo "She wasn’t able to play last night and I heard that she went back to the dorm this morning."
    s "Wait, really? How come?"
    m "She said she wasn’t feeling well. "
    m "I imagine it’s because of the heat."
    m "It won’t be an issue soon, though. "

    scene mollymaya8
    with dissolve

    mo "That’s right, Sir. {i}Winter is coming{/i}."
    s "Why did you say that so menacingly?"

    scene mollymaya9
    with dissolve

    mo "Oh my God! You really don’t know anything, do you? What do you even do for fun?!"

    if bonus == True:
        m "He peeks on [young_girls] while they’re getting changed."
        mo "I mean, so do I, but it’s normally in the form of a game. You know there are much easier ways to do that, don’t you?"
    else:
        m "He used to hang out with me."
        s "I did?"
        m "Yes. I mean whoops. Who said that?"
        mo "If that's true, it sure beats romancing virtual girls in virtual spaces like I do all day."
        mo "Thankfully, I am not alone and there are many others just like me."

    s "Oh please. As if anyone would be attracted to girls in a video game. That just doesn’t even make sense."

    scene mollymaya3
    with dissolve

    mo "I’m just going to pretend I didn’t hear that...You two carry on with your normie conversation while I lay here and innervate myself."
    s "Try to do things like that in private, Molly."

    scene mollymaya10
    with dissolve

    mo "It‘s a spell to restore my mana and it’s very wholesome!"
    mo "I might be a degenerate but even I wouldn’t stoop to doing {i}that{/i} surrounded by a crowd of my friends!"
    mo "My lust level is nowhere near high enough!"

    scene mollymaya13
    with dissolve

    mo "Now if you’ll excuse me-"
    mo "Bzzzzzzzzzzz..."
    m "… "
    s "…"
    s "What is she doing?"
    m "Innervating."
    s "Does she really need to make those noises, though?"
    m "Does she really need to do 90%% of the things that she does?"
    s "Good point."

    "I take a few steps toward the towel the two of them are sitting on and begin to crouch down."

    s "Can I take a seat? I’m getting a little tired of-"

    scene mollymaya11
    with dissolve

    m "No thank you."
    s "But there’s plenty of room."
    m "I said no thank you."
    m "I’m afraid you might accidentally touch me. "
    s "Would that really be so bad?"

    scene mollymaya12
    with dissolve

    if bonus == True:
        m "I fear that my skin would melt off if you even thought about touching me."
        s "Your skin would have probably melted off by now because it’s pretty unfeasible to think that I haven’t imagined touching you at some point."
    else:
        m "I'm afraid it might cause me to fall in love with you all over again."
        s "????????????"
        m "Oh. Crap. I have to keep up the facade."

    scene mollymaya13
    with dissolve

    m "You’re disgusting."
    s "How many times is that now? Four? Five?"
    m "Not enough to get the point across, apparently."
    m "Why are you even here?"
    m "And where is Ami?"

    if bonus == True:
        m "She seemed to take her time waking you up this morning, so I can only imagine what that must mean."

        if amilust10 == True:
            s "…"
            m "…"

            "Wait..."
            "Does Maya know about {i}that{/i}?"
            "I know her and Ami are best friends, but I didn’t think she’d go as far as telling her friend that she’s engaged in [incest] with her [uncle]."
            "That just seems like a horrible idea in every sense of the word."
            "But...then again...Maya has been known to understand a little more than she’s supposed to at times."
            "This is incredibly worrying."

            s "I have no idea what you’re talking about."
            m "Apologies. Of course you don’t."

        else:
            s "I have no idea what you’re talking about. All she did was wake me up and walk down here with me."
            m "Really?"
            s "Really."
            m "…"
            m "Interesting."
    else:
        s "I think I saw her floating away earlier."

    scene mollymaya14
    with dissolve

    mo "Oooookay. I’m tired of not being involved anymore. Molly MacCormack has joined the battle."
    s "Welcome back Molly. How was your intervention?"
    mo "{i}Innervation{/i}, Sir. You need to memorize your spells or you’ll never make it into the raid group."
    s "Is that a thing I even want to be a part of?"

    scene mollymaya16
    with dissolve

    mo "Of course! It’s only the peak of the endgame experience!"

    if bonus == True:
        mo "The only thing better than getting a well-rounded raid group is checking the tags and not seeing anything about vore."
        s "How do you know all of these strange words?"
        s "Am I really getting that old?"
    else:
        mo "The only thing better than getting a well-rounded raid group is a balanced breakfast."
        s "I agree, Molly. But I'm basically an old man now and my taste buds are slowly beginning to dwindle."

    scene mollymaya17
    with dissolve

    m "Yes. I’ve been telling you that since you first showed up at the shrine."

    if bonus == True:
        m "You’re disturbingly old. So much so that I don’t understand how you haven’t been arrested for hanging around us in public yet."
    else:
        m "You need to get a new tongue."
        m "Here, borrow mine."

    s "Wow, you’re really firing on all cylinders today. Aren’t you, Maya?"
    m "You’re ruining my vacation."
    s "All you’re doing is sitting on a towel. That’s not really high quality vacation material."
    m "And sleeping until almost noon and having your [niece] come to wake you up is?"

    scene mollymaya18
    with dissolve

    if bonus == True:
        mo "That doesn’t sound all that bad to me. I’m sure I’ve even read through a few pretty...{i}interesting{/i} scenes that have started that way."
    else:
        mo "You know, I really just don't see the point of accountants when we'll all be using Dogecoin in a few years."

    m "Why do girls like you exist?"

    scene mollymaya19
    with dissolve

    mo "Why do {i}any{/i} of us exist, Maya?"
    mo "What is life if not an excuse to feel pain? To grow old and die. "
    mo "It’s how the universe was designed. We’re all creatures just struggling to find our purpose before our time runs out."
    m "…"
    mo "…"
    m "Is that supposed to be me?"
    s "It was pretty spot on, to tell you the truth."
    m "It was not. She didn’t even get my face right."

    scene mollymaya20
    with dissolve

    mo "Please leave me alone, Sensei. I can not enjoy my vacation with you standing so close to me."
    mo "Make yourself useful and fetch me a watermelon before I fade away into nothingness."

    scene mollymaya21
    with dissolve

    m "This isn’t funny."
    mo "Like my Maya impression, Sensei? It’s pretty good, right?"
    mo "That was my first time tryin’ the whole ‘expressionless’ face thing. Did it look okay?"
    s "It was perfect. I actually thought you {i}were{/i} Maya for a second."

    scene mollymaya22
    with dissolve

    m "You’re not funny either. "
    m "That impression was nothing like me."
    s "Why don’t you give us your best Molly impression then, Maya?"
    m "I’d rather die."
    mo "Urrheak here is just jealous that my personality can’t be so easily mimicked. "

    scene mollymaya23
    with dissolve

    m "Your personality can be mimicked by any prepubescent boy in Japan. You aren’t as unique as you think."
    mo "Do you hear something, Sir? The wind is certainly loud today."
    m "It’s not even windy."
    s "I don’t hear anything at all. "
    s "In fact, have you seen Maya around? I’m starting to worry that she might have gotten lost or something."

    scene mollymaya24
    with dissolve

    mo "Maya?"
    mo "I’ve..."
    mo "I’ve never even heard that name before..."
    s "Wait a minute...neither have I."
    m "This isn’t funny."
    m "You’re disgusting {i}and{/i} immature."

    scene mollymaya25
    with dissolve

    m "In fact, it’s almost unnerving how-"

    scene mollymaya26
    with dissolve

    m "Wait..."
    m "What are they doing over there?"

    "Something off in the distance catches Maya’s attention."
    "Molly and I both follow her gaze to figure out what it might be..."

    scene mollymaya27
    with dissolve

    ka "Hah..."
    a "You can do it, Karin! We believe in you!"
    mi "Yeah! You show that melon who’s boss! "
    ka "Okay but...I don’t really know how hard to swing the bat..."
    ka "Don’t we have anything a little less...well, hard?"
    mi "If it ain’t hard there’s no way you’ll kill the melon!"
    mi "Just give it a good ole whack and show it that you’re co-captain of the soccer team for a reason!"
    a "Yeah! Even though you don’t really need a bat for soccer and...being the co-captain isn’t really based on strength!"
    mi "Yeah! What Ami said!"
    ka "Okay...but I doubt I’ll get it on the first try."

    scene mollymaya28
    with dissolve

    m "Oh no...No..."
    m "This can’t be happening."
    m "I have to go!"

    scene mollymaya29
    with dissolve

    "Maya suddenly takes off toward Karin and Molly is left with an expectedly confused look on her face."

    mo "The Hell was that about, Sir?"
    s "I guess you don’t know."
    mo "Know what? What’s going on?"
    s "Maya has a...unique affinity for watermelons."
    s "It’s actually kind of strange. It’s not even that good of a fruit."
    mo "It’s really not. It just tastes like...water. And melon."
    s "I agree. But, well-"
    s "Well I guess you’ll see for yourself."

    scene mollymaya30
    with dissolve

    a "Oh, crap! I forgot all about Maya!"
    a "Karin! Abort mission! Don’t kill the watermelon!"

    scene mollymaya31
    with dissolve

    ka "Thank you for the concern, Ami. But it’s really okay. I’ll figure out a way to make the bat work."
    ka "Sure, I would have preferred maybe a large stick or something like that but...this will do."
    ka "This will do nicely."
    ka "This melon will die."

    scene mollymaya32
    with dissolve

    a "No, you don’t understand! If you blow up the watermelon, Maya will get really upset!"
    a "They need to be cut into perfect wedges or else she gets super cranky."
    mi "Wow. Maya’s actually kinda fast. "
    mi "Think she’ll make it in time?"

    scene mollymaya33
    with dissolve

    a "Of course she’ll make it in time! A melon is involved!"
    ka "Okay! Here I go!"

    scene mollymaya34
    with dissolve

    a "AHHHH! I CAN’T WATCH!"

    scene mollymaya35
    with fade

    ka "The melon is here. I can sense it."

    "Karin miraculously makes her way over to the watermelon and kneels down in front of it."
    "Maya gets closer with each passing second, but who’s to say if she’ll make it in time?"
    "Karin could strike at any moment."
    "And with a figure like that I can imagine it would send the watermelon flying into a million tiny bits."

    a "KARIN! YOU DON’T HAVE TO DO THIS!"
    ka "It’s okay Ami...Everything is going to be okay..."
    a "NO, LIKE, YOU LITERALLY DON’T HAVE TO DO THIS. WE CAN JUST EAT IT LIKE NORMAL."
    ka "A mission is a mission..."

    scene mollymaya36
    with dissolve

    ka "God...forgive me!"

    scene black
    with dissolve

    "In the very last second-"
    "Just before the watermelon’s demise."
    "An angel appears."
    "..."
    "And the bat immediately connects with her."

    scene mollymaya37
    with dissolve

    ka "Ahhh! Oh my God! I-I’m so sorry! I had no idea you were there!"
    a "THAT’S WHAT I WAS TRYING TO TELL YOU!"
    m "I...regret nothing..."
    m "Let this...be a lesson...on the..."
    m "Hah..."
    ka "On the what?! Tell me your dying wish and I’ll devote my life to making it come true!"
    m "Let this be a lesson on the..."

    scene mollymaya38
    with dissolve

    m "The proper treatment...of watermelons..."

    scene black
    with dissolve2

    "They were strange dying words, but they did their job."
    "Karin spent the rest of her life wandering the world and educating youths in urban areas about how to properly treat watermelons."
    "She continuously had to relocate, though, because local law enforcement kept putting out bulletins about a deranged woman entering[school]s and lecturing students about fruit."
    "Maya died shortly after the incident."
    "We spread her ashes over her favorite melon farm."

    scene sky
    with dissolve

    "And me?"
    "I bet you’re wondering what I did."
    "But this isn’t my story."
    "It’s yours."
    "So what will you do?"
    "Will you die for what you believe in?"
    "Or will you be the one bearing the {s}baseball bat{/s} axe?"

    $ renpy.end_replay()
    $ beachvacation11 = True
    $ maya_love += 1
    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

label beachvacation12:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```