# Condoms in the Sand
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotowinterbeach1&go=Go)



## Event preconditions
❌makotobeachticket equal to True (unknown variable)

✅Day of week is Saturday

✅Event "[Miku: Loxonin](./soccer35.md)" is completed (event=soccer35)

✅Event "[Maya: A Place That Can Only Exist in Our Minds](./mayadorm35.md)" is completed (event=mayadorm35)

❌makotonumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: makotowinterbeach1
* Group: Makoto
* Triggered by label: callmakotoafternoon
* Triggered by branch label: callafternoon

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label makotowinterbeach1:
    play sound "phonebeep.wav"

    "I tap on Makoto’s name in my phone and wait for her to answer."
    "It’s been a little while since she asked me if I’d accompany her to the beach and...what better time to do that than a random afternoon in the middle of winter?"
    "Yes, the idea of the two of us going {i}there{/i} when it’s obvious she just wants to be alone with me rather than scope out a venue she’s already familiar with is a little...abnormal."
    "But I’m not going to throw away a vacation opportunity with a cute girl just because the conditions aren’t perfect."

    if bonus == True:
        "Besides, I’m sure we’ll find some way to keep warm in no time at all..."
        "I'm talking about sex."
        "That was a sex joke."

    play sound "phonebeep.wav"
    play music "acoustic.mp3"

    mak "Hello?"
    s "Hey, Makoto. What are you up to right now?"
    mak "Right now? I’m just...hanging around. Why do you ask?"
    s "Is now a good time to go on that beach trip?"
    mak "Uhh...no. Not really. "
    mak "Can you hold on one second, please?"
    s "Huh? Uhh, yeah. I guess that’s fine."
    mak "Thanks. I’ll be back in a second."

    "I hear Makoto put the phone down and start talking to someone (Probably her mom) about something I can’t really make out over the sound of a television in the background."
    "I remain on the line for several minutes and begin to lose my patience."
    "But just as I’m about to hang up and find something else to do, I hear her coming back."

    mak "Yeah. We can go now. But...I want to meet {i}there{/i} if that’s okay."
    s "Why? "
    s "If this is about you throwing me a surprise party, I don’t want one."
    mak "Why on earth would I throw you a surprise party? That’s obviously not what’s happening."
    s "Well then what is it exactly?"
    mak "That...will probably be easier to explain once we’re there. "
    mak "It’s already starting to get late, though. So if we’re doing this, get ready now and meet me at the beach in one hour."
    mak "Okay?"
    s "...Yeah. "
    s "I’ll see you there."

    play sound "phonebeep.wav"

    if bonus == True:
        "I hang up the phone and begin to gather a few of my things to prepare for an overnight trip full of debauchery and...probably smart people stuff."
        "I don’t know. Makoto will probably want to take a break between orgasms to brush up on encyclopedic knowledge or something like that."
    else:
        "I hang up the phone and start packing my jammies. I'm so excited to go on a trip with one of my best buddies."

    scene wintersky
    with dissolve2

    "I send Ami a message telling her I won’t be around tonight and then promptly turn my phone off to avoid the barrage of messages she is sure to send me in response."
    "But it’s better off that she doesn’t know where I’ll be."
    "Especially since I’m going to be there with one of her least favorite people in the entire world."
    "But hey, that’s just how things are sometimes. And I don’t really want to think about it right now."

    if bonus == True:
        "I just want to make it to the inn, kick my shoes off, and ruthlessly plow my class rep until she can no longer walk."
    else:
        "I just want to drink pina coladas in my jam-jams."

    "This is going to be a good weekend."
    "………"
    "……"
    "…"

    scene makotobeachintro1
    with fade

    "I make it to the beach in just under an hour to find Makoto waiting near the spot where we set up camp for our last class trip."

    if mayadorm35 == True:
        "A barrage of memories (The kind I won’t black out for remembering) come rushing back into my head, likely avoiding a collision with Makoto’s."
    else:
        "A barrage of memories come rushing back into my head, likely avoiding a collision with Makoto’s."

    "Probably, at least."
    "I’m not really sure how her brain would rationalize the thought of an earlier class trip when this is still her first[school] year with me as her teacher."
    "I’m not concerned with that right now, though."
    "What I am concerned with is-"

    if bonus == True:
        mak "I want to let you know in advance that we will not be having sex this weekend."
    else:
        mak "I want to let you know in advance that I have a strict rule against pina coladas."

    s "…"
    mak "Thank you for understanding."
    s "…"
    s "I wonder if the bus has left yet."

    scene makotobeachintro2
    with dissolve

    if bonus == True:
        mak "You’ve been here for thirty seconds...Surely you’re able to go at least another several hours without getting an erection."
        s "Ha. Funny joke, Makoto."
        mak "Sensei, I’m being serious."
        mak "I feel like the only times I see you, I’m either taking your pants off or doing your paperwork."
        s "I see no problem with this."
        mak "The {i}problem{/i} is that I want to actually relax tonight."
        s "Are you implying that you don’t find sex relaxing, class rep?"
    else:
        mak "It did."
        s "But my jam-jams! I need a coconut drink to complete my comfiness ritual!"

    scene makotobeachintro3
    with dissolve

    if bonus == True:
        mak "I can assure you that having sex with someone of your size is anything but {i}relaxing{/i}, but that is beside the point."
        mak "The truth is that there’s something I’d like to discuss with you this weekend."
        mak "And we wouldn’t even be able to have sex anyway."
        s "Why not?"
        mak "It’s complicated."
        s "Girl problems?"
        mak "Sure. That’s one way to word it."
        mak "You’ll see soon enough."
        s "Wait, what?"

        scene makotobeachintro4
        with dissolve

        mak "Don’t worry about it."
        mak "The fact is, you’re here with me now. And the last bus of the day just drove off while I had you distracted, so there is no longer an escape."
        s "You should have told me about this whole no sex thing before I came here."
        mak "You wouldn’t have come at all if I had done that."
        s "True. But look, I even made special preparations just for you."
    else:
        mak "I can assure you that we can still have fun without your silly coconut drinks."

    "I empty out the contents of my suitcase onto the sand, showing Makoto how much I care about her."

    scene makotobeachintro5
    with dissolve

    mak "Sensei..."
    mak "Did..."

    if bonus == True:
        mak "Did you {i}only{/i} pack condoms for this trip?..."
        s "Anything for you, Makoto."
        mak "Why are there only three of them, though?..."
        s "I figured that you’d be so into it after the third condom that I could convince you to just keep going without one."

        scene makotobeachintro6
        with dissolve

        mak "I like to think I have a little more self-control than that."
        s "Says the girl who basically blackmailed me into taking her virginity at a Halloween party."
        mak "…"
        mak "Yeah, I did kind of do that."

        scene makotobeachintro7
        with dissolve

        mak "But that’s in the past! This weekend, I want to actually talk to you about something."
        mak "And we’re not going to be able to talk if our clothes are off."
        s "I mean...we {i}could{/i}, but-"
        mak "No."
        mak "I want you to treat me like a human being this weekend. I let you push me around far too often."
        s "Wait, like the {i}whole{/i} weekend? Not just for an hour or two?"
        mak "The whole weekend."
        mak "Or...I guess technically just until tomorrow, since we'll only be here for one night."
        s "Ugh..."
        mak "Listen, I understand that you like to joke around, but there is only so much that I can take before it starts getting to me."

        scene makotobeachintro8
        with dissolve

        mak "So, with that out of the way, are you excited to spend some time with Makoto Miyamura not as your sex slave or class president, but as a girl who puts you on a much higher pedestal than you deserve?"
        s "…"

        "I understand where Makoto’s coming from."
        "I obviously know that I’ve been using her for my own personal gain, but why in the world would I {i}not{/i} do that when she’s made it so ridiculously easy?"
        "I bet you’re thinking “because of common decency” or something along those lines, right?"
        "I’m sure that sort of thought process will take you very far in life."
        "Be sure to call and tell me all about it while you’re sulking in the darkest corner of your bedroom and I’m sitting on a throne of naked [teenager]s with a glass of white wine in my hand."
        "And I don’t even like white wine."
        "That’s how far apart you and I are."
        "If something that I want is offered to me, I take it."
        "If something that I desire is within reach, I reach for it."
        "You just wait and watch things drift further and further away."
        "That’s no good at all."
        "Sure, there’s also a chance that this is misplaced narration and that you, too, wrap your fingers around anything offered to you-"
        "Even when those things are dripping with so many negative connotations that it’s no different from gripping your own cock after putting it somewhere it doesn’t belong."
        "And if you are that person, then I like you."
        "Hell, even if you {i}aren’t{/i} that person, I like you."
        "Just for this weekend, though."
        "Because even someone like me understands that you can only push a person so far before they can no longer give you anything."
        "And a relationship becomes meaningless once you have nothing to gain from it."

        s "Fine. I won’t take advantage of you this weekend."
        s "But you’re going to owe me."

        scene makotobeachintro9
        with dissolve

        mak "Starting your marathon of niceties with a quid pro quo isn’t exactly the best first step, but I guess I’ll take what I can get."

        "So will I."

        scene makotobeachintro1
        with dissolve
    else:
        mak "Did you bring your {i}nice{/i} pajamas for this?"
        s "This was a very special weekend for me and now it is ruined."
        mak "Wow."

    mak "Should we start heading to the inn, then?"

    if bonus == False:
        "She doesn't care about me at all, does she?"

    mak "I already spoke with the front desk and secured a room. They just need your credit card information or they’re going to kick us out come dinner time."
    s "Wait, you got the room already? I’m surprised they let you book it without putting any money down."
    mak "It’s not like many people visit this time of year, so I’m pretty sure they were willing to go above and beyond to accommodate us given the circumstances."
    mak "Also, it’s far too cold near the water to have just waited out here for you to arrive."
    mak "So, at the risk of being any {i}less{/i} direct, I will now say, “Sensei, please walk back to the inn with me before I freeze to death.”"
    s "Fine, fine..."
    s "Let’s go."

    if bonus == True:
        s "Don’t come crying to me when you get horny and I’m not allowed to have sex with you, though."
        mak "Unlike you, I’m quite good at exhibiting self control."
        mak "Now, pick up your condoms and let’s get a move on."

        "I look down at the sand and notice how the soft ocean breeze has managed to lightly bury the condoms I bought just for tonight."
    else:
        "I look down at the sand and notice how the soft ocean breeze has managed to lightly bury my jammies."

    scene makotobeachintro9
    with dissolve

    s "…"
    mak "Uhh..."
    mak "Why are you just staring at them?..."
    s "Because they’re already gone, Makoto."

    if bonus == True:
        s "Gone like condoms in the sand."
        mak "…"
        mak "I think you’re looking for the phrase, “Dust in the wind.”"

    scene black
    with dissolve2

    mak "And now you’re just walking away like you said something really cool."

    "I gaze up at the sky."
    "It looks like it’s about to rain."
    "A large wave crashes against the beach."

    if bonus == True:
        "And comes to steal away the condoms in the sand..."
    else:
        "It makes a noise like {i}pchhhhhhhhhhhhhh!!!!!{/i}"

    scene makotobeachintro10
    with dissolve

    if bonus == True:
        mak "Wow. You’re, uhh...really not handling this abstinent weekend plan well, are you?"
        s "I’ll be fine. The idea of a vacation without sex seems strange to me, though."
        mak "If it’s any consolation, it’s much less of me not wanting to and a whole lot of us just...not being able to."
        s "Right. Because of girl problems."
        mak "Something like that."
        mak "But even if we were to do those sorts of things together, it wouldn’t change how I’d still see this as the perfect opportunity for you to be nice to me for once."
        mak "It’s rather bothersome watching you treat Ami like an angel and leaving {i}me{/i}, Makoto Miyamura, like I’m some sort of-"

        scene makotobeachintro11
        with dissolve

        s "Condom in the sand?"
        mak "Can you please stop saying that? It’s one of the worst analogies I’ve ever heard."
        s "Oh, come on. It’s not {i}that{/i} bad."
        mak "..."
        mak "Fine. Maybe it’s not the worst, but it’s still unsuitable as a description for our...strange dynamic with one another."

        scene makotobeachintro12
        with dissolve

        s "It {i}is{/i} kind of strange, isn’t it?"
        s "If I were you, I would have stopped doing my bidding a long time ago."
        s "What’s the point of keeping it up if you’re not enjoying it?"
        mak "Hope, I suppose."
        mak "Hope that one day you’ll realize how harsh you've been...and start treating me with the respect I deserve rather than the respect you can be bothered to hand out."

        scene makotobeachintro13
        with dissolve

    mak "I really shouldn’t...but I look up to you a lot, Sensei."
    mak "But I don’t want to keep looking up because that means you’ll always be looking down."
    mak "And if we’re not on equal footing, neither of us will ever {i}really{/i} be happy."
    s "Are you not happy, Makoto?"

    scene makotobeachintro14
    with dissolve

    mak "…"
    s "…"
    mak "I’m fine."
    mak "Just not very good at explaining myself, apparently."
    mak "But I have an entire weekend to do that, so..."
    mak "I hope you don’t mind me being extremely intrusive and making the most of the short time we have left together."

    scene black
    with dissolve2

    "She says, as if she’s dying."
    "We’re all dying, though."
    "It’s not just her."
    "We make it to the inn and I accompany Makoto to the front desk."
    "There’s apparently a discount on rooms due to this being the offseason, and it’s actually a pretty good deal for the type of place this is."
    "So good that I probably wouldn’t even mind coming back before summer starts, which is saying a lot given my tendency to pinch pennies."
    "Regardless, I pay the clerk and Makoto points me in the direction of our room, tugging on my sleeve to get me to follow her."
    "I oblige."

    if bonus == True:
        "And our weekend of...apparently no debauchery at all finally begins."

    $ renpy.end_replay()
    $ makotowinterbeach1 = True
    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

label makotowinterbeach2:
...
```

## Code that triggers this event
File: \game\MakotoEvents.rpy
Code:
```python
...
label callmakotoafternoon:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump callafternoon
    if chapthreeactive == True:
        jump makotosummer2poolgen
    if christmas7 == False:
        play sound "phonebeep.wav"

        "I tap on Makoto's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callafternoon

    if makotobeachticket == True and day == 6 and soccer35 == True and mayadorm35 == True:
        jump makotowinterbeach1
...
```