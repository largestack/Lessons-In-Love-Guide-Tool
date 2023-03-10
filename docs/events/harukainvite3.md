# Unfiltered Tap Water (Haruka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Sober-ish](./harukadate20.md) (Haruka) is completed)

* harukasex equal to True (unknown variable)

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

None

## Event properties

* Id: harukainvite3
* Group: Haruka
* Triggered by label: harukainvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->harukainvite->harukainvite3

## Official wiki page

[Unfiltered Tap Water](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukainvite3&go=Go) for more details.

## Event code

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label harukainvite3:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "Ami told me earlier today that she wouldn’t be around, so I figure now is as good a time as any to bring someone over."

    if bonus == True:
        "Plus, Haruka and I never got to do anything fun after our bar hopping adventure, so I would like to make up for lost {i}intimate time{/i} if at all possible."
        "And while I agree with all of that stuff she recently said about how it's nice to hang out without any of the more physical parts of our relationship getting in the way..."
        "The physical stuff is still my favorite part."
        "And it’s the only reason this relationship exists in the first place, so..."
        "Yeah, I’m pretty sure you’re able to guess what’s on my mind today."

    play sound "phonebeep.wav"

    h "Hey! What’s up?"
    s "Not much. Are you still at work?"
    h "Nope! It was actually kind of dead today, so I let the rest of the staff take over."
    h "Rin’s there tonight as well, so-"
    s "You should come over."
    h "I should?"
    s "You should."
    h "Huh."
    h "Well, then I guess I should."
    h "Am I just meeting you there or am I coming in?"
    s "Coming in, preferably. "
    h "Is your [niece] around?"
    s "She is not."
    h "I see, I see."
    h "Okay. Yeah, I’ll head over now."
    s "Sounds good. See you soon, Haruka."
    h "Yup! See you soon."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone as soon as the plans are set in stone and begin the journey back."
    "The tone of Haruka’s voice carried a bit of disappointment when she found out we weren’t just meeting up and that she was coming in-"
    "But I’m sure that tone will change within a very short amount of time."
    "It always does with her."
    "………"
    "……"
    "…"

    scene harukathirdinvite1
    with dissolve2
    play music "acoustic.mp3"

    h "Hey! Sorry if I took a little while. I was in the middle of dinner when you called, so...didn’t want to leave in the middle of that."
    s "It’s fine. I just got back myself."
    h "Wow, you wanted to see me so much that you invited me over before you were even home?"
    s "I just call that being good at time management."
    s "And, speaking of which..."
    h "Speaking of which, {i}what?{/i}"
    h "Do you have a good idea of how you’d like to spend our time together tonight?"
    s "A very good idea, actually. I think we should-"
    h "Hang out on the couch and talk to each other?"

    if bonus == True:
        s "Uhh, my idea actually involved a little less clothing."
        h "Will it appease you if I take my hoodie off?"
        s "Sure. As long as you take the rest of your clothes off with it."
        h "We can’t do it today, if that’s what you’re getting at."
        s "Why not?"
        h "Because {i}we can’t do it today.{/i}"
        s "Why does this always happen to me?"
    else:
        s "Without touching, ideally. The touch of a girl always makes me nervous and I don't want to feel that way in my own home."

    scene harukathirdinvite2
    with dissolve

    h "Uhh...always?"

    if bonus == True:
        s "Well, not always. But this is definitely not the first time that-"
        s "Oh. You’re upset because that insinuates there are other people."
        h "Well, I...I mean, of course there are other people. That’s...That’s pretty obvious with the way you conduct yourself."
        h "And it’s not like I’m really...the best person to comment on that sort of thing, since..."
    else:
        s "Yes. Always."

    scene harukathirdinvite3
    with dissolve

    h "You know what? Let’s not talk about that right now."
    h "I’ve been in a pretty good mood all day and I kind of want to shut my brain off."
    s "And I’m assuming that’s why you didn’t want to stick around here?"

    scene harukathirdinvite4
    with dissolve

    h "That and I had so much fun the last time we actually went out that I was kind of hoping it was going to happen again."
    s "And it will. I just don’t feel like going out again today now that I’m home."
    h "That’s fine. I mean, this is what we do best anyway."
    h "We’ll just chill on the couch and watch TV or something."

    if bonus == True:
        s "Can you at least inform me of whether or not there is a blowjob on the way to me in the near future?"

        scene harukathirdinvite5
        with dissolve

        h "Jesus, are you really that turned on right now?"
        s "This is just what life for me is like, Haruka. It’s incredibly sad."
        h "I mean, I definitely get it. It just sounds like you’re going to die without any action."
        s "I very well may."

        scene harukathirdinvite6
        with dissolve

        h "Did you get blueballed by one of the girls in your class or something?"
        s "I have no idea what you’re talking about. The only person I am sexually involved with is a local cafe owner with pink hair."
        h "One of my competitors has pink hair. You’re not fucking the enemy, are you?"
        s "I am not fucking the enemy."
        h "Because if you’re fucking the enemy, I’m going to be really pissed."
        s "I don’t even know who the enemy is."
        h "You should have just told me that it {i}was{/i} one of your students who did this to you. That would have been a lot more exciting."
        s "Sometimes, I think you might like [teenage]girls more than I do."

        scene harukathirdinvite1
        with dissolve

        h "That’s fine, because I’m pretty sure Rin likes them more than both of us combined."
        s "I...really can’t disagree with that. "
        s "It’s kind of unhealthy, actually."
        h "Definitely."
        h "So, are we done standing around yet? Because your couch looks really comfortable and I would like to one day sit on it."
        h "I have somehow not managed to do that despite being inside on multiple occasions now. You are a horrible host."
        s "Fine. But I still want to know about the blowjob thing."
    else:
        s "As long as we do not touch."

    scene harukathirdinvite7
    with dissolve

    h "Okay, you really might have some sort of problem if this is all you can think of. "

    if bonus == True:
        h "Even I’m not this bad and I have spent well over 100,000 yen at Maki’s store."
        s "That is...incredibly depressing."
        h "I am...so very lonely."
    else:
        s "At least my significant other isn't in space."
        h "That was uncalled for, good sir."
        s "You are right. I am sorry."

    scene black
    with dissolve

    if bonus == True:
        "Haruka and I swallow our self-pity (The same way I hope that she swallows my semen before the night’s end) and take a seat on the couch..."
    else:
        "Haruka and I swallow our self-pity and take a seat on the couch..."

    scene harukathirdinvite8
    with dissolve

    "She pulls her knees up against her chest and moves closer to me than she normally does when the two of us are alone together like this."

    if bonus == True:
        "Well...when we're not naked, I mean."
        "Her clothes smell similar to Nodoka’s in that they’re essentially permanently stained with the essence of coffee, but Haruka’s also contain a tinge of..."
    else:
        "She is getting so close to breaking the no touching rule that I can smell her shampoo."

    s "Lemon?"
    h "Uhh...I’m sorry?"
    s "Oh. Nothing. Thinking out loud."
    h "Of...lemons?"
    s "I...guess so."
    s "Anyway, now what?"

    if bonus == True:
        s "We’re not having sex and it’s becoming depressingly apparent that nothing else is going to happen either, so our choices are either watching television or...talking."
        h "Do you not like talking?"
        s "It’s not that. I just think you like talking a little too much sometimes."

        scene harukathirdinvite9
        with dissolve

        h "Well excuse me for wanting to converse with you!"
        h "It’s just not often that someone is able to hear all of my rambling and not think I’m annoying, so yeah. I’m going to talk a lot."
        s "You know, once you’re surrounded by a class of twenty [teenage]girls, it’s kind of hard to be annoyed by anything else ever again."
        s "It’s one of the three big reasons I keep inviting you over instead of any of them."

        scene harukathirdinvite10
        with dissolve

        h "If you tell me that the other two are my boobs, I-"
        s "The other two are your boobs."
        h "Why am I even here right now?"
        s "Because, for some strange reason, you enjoy being around me."

        scene harukathirdinvite11
        with dissolve

        h "Yeah...it {i}is{/i} kind of strange, isn’t it?"
        h "You’re a jerk...you have an annoyingly busy schedule...and you’re probably fucking both of my friends."

        if sarasex == True and makibj == True and makisex == False:
            s "Well...that depends on what you mean by {i}fucking{/i}."

            scene harukathirdinvite12
            with dissolve

            h "Like...putting your thing in...their things..."
            s "You can use adult words in this house, Haruka. You’re not going to get in trouble."
            s "Besides, I can say with confidence that I am not fucking {i}both{/i} of your friends."
            h "…"
            s "Just one of them."
            h "Yes. Yes, you made that pretty obvious."

        if sarasex == True and makibj == True and makisex == True:
            s "..."

            scene harukathirdinvite12
            with dissolve

            h "I'm...going to assume your silence means that it's no longer just {i}probably.{/i}"
            s "Hey, you said it. Not me."

        if sarasex == True and makibj == False:
            s "Well...not {i}both{/i} of them..."

            scene harukathirdinvite12
            with dissolve

            h "…"
            s "Just one of them."
            h "Yes. Yes, you made that pretty obvious."

        if sarasex == False and makibj == False:
            s "Actually...I’m not."
            s "I haven’t done anything with either of them."

            scene harukathirdinvite13
            with dissolve

            h "Wait, really? "
            h "But...you’ve had so many chances..."
            s "There’s this one girl my age who I just like a little more, I guess."
            s "Also, may I remind you of the three reasons that I continue to invite you-"

            scene harukathirdinvite14
            with dissolve

            h "No. You may not."
            s "Damn it."

            scene harukathirdinvite15
            with dissolve

            h "But...umm..."
            h "It does make me...a little happy hearing that for some reason."
            h "It’s kind of like...I’ve beaten those two in something for once."
            h "That doesn’t really happen often."

        elif sarasex == False and makibj == True:
            s "Well...no. I’m not fucking them."
            s "But I did get a blowjob from Maki."

            scene harukathirdinvite16
            with dissolve

            if harukalust10 == True:
                s "Other than the Halloween one, I mean."

            h "Well...uhh...thanks for telling me?..."
            s "Any time, Haruka. This is what friends are for."
            h "Is it really, though?"

        s "Anyway, the fact of the matter is...and forgive me for saying something remotely kind right now, I enjoy being around you as well."

        scene harukathirdinvite17
        with dissolve

        h "Really?"
        s "Of course."
        s "Do you think I would just allow you to sit on my couch immediately after informing me that we won’t be having sex if I didn’t actually like you?"
        h "I...feel like there are a million nicer ways to explain that."
        s "I’m not good with nice explanations. I prefer to get right to the point whenever possible."

        scene harukathirdinvite18
        with dissolve

        h "Then I’ll get right to the point as well."
        h "Well, {i}a{/i} point."
        h "There are actually a lot of...points that I’d like to make to you, but...actually figuring out how to explain them without sounding like a lunatic has been a lot harder than you’d expect."
        s "This doesn’t sound like getting right to the point."
        h "The point is..."
        h "Even if...this relationship started out of pity or...sexual attraction or...whatever it was that caused the two of us to go through with...what we went through..."
        h "It’s..."
        h "It’s starting to feel like...it’s a little more than that. At least for me."
        h "Like...I still see you as a friend. I’m not saying I’m in love with you or anything."
        h "But...I think about you a lot more than someone should be thinking about a friend. And not just when I’m horny or...when I’m lonely."
        h "But when I’m doing all kinds of things."
        h "Like...the other day, I passed by some restaurant and the first thing I thought was, “It would be nice to go there with Sensei.”"

        scene harukathirdinvite19
        with dissolve

        h "That’s...that’s kind of weird, isn’t it?"
        h "Like...that’s not the kind of relationship we have...and I still can’t help but think of things that way."
        h "I’m sure that...being alone for so long must have something to do with it, but..."
        h "Yeah. That’s one of the several points that I wanted to make about...this. "
        h "It’s...It’s just nice, you know?"

        "From either up above or down below, I hope the most important person to her is listening in."
        "I hope he’s listening in and realizing that this rose belongs to me now."
        "That the flower he planted and subsequently spent years cultivating has been plucked from his garden and dropped haphazardly into a shallow vase full of dirty, unfiltered tap water."
        "This is the power of all that I am."
        "The power of the center of the solar system."
        "Everything flows into me- and I flow back into them."
        "A cycle of endless orgasms and secrets spanning across an infinite plane of time that exists for no discernible reason, but exists nonetheless."
        "True love is a lie."
        "All flowers need water."
        "You can not plant one and leave it alone."
        "And if you do, be prepared for the worst."
        "Luckily for Haruka’s husband, wherever he may be, if he even {i}is{/i} at all-"
        "I will gladly tend to his roses."
        "I will tend to every single rose in every single garden."
        "And I will smile as I do it."

        s "Yeah..."
        s "It is nice."
    else:
        h "I guess we can just wait until Ami gets home and yells at me?"
        s "Sure. We have to cut the rest of the conversation out anyway, so..."
        h "..."
        s "..."
        h "..."
        s "..."
        h "..."
        s "..."

    stop music
    play sound "dooropen.mp3"
    scene harukathirdinvite20
    with dissolve

    a "I’m home! "

    play sound "static.mp3"
    scene harukathirdinvite21
    with flash
    stop sound

    "Bury me in {s}you{/s} worms."

    play sound "static.mp3"
    scene harukathirdinvite22
    with flash
    stop sound
    play music "lastdailysong.mp3"

    a "…"
    h "Hey. Welcome back."
    a "…"
    s "Hey, Ami. We were just going to watch TV."
    a "…"

    if bonus == True:
        "So, I obviously know this doesn’t look good."
        "But, based on prior experience, this really isn’t even half as bad as it could have been."
        "I’m actually somehow thankful that we didn’t wind up having sex today because...well, you can probably imagine why."
        "Still, though. "
        "Ami is sensitive as-is, so we’ll need to navigate this carefully if-"

        a "Aren’t you married?"
    else:
        a "That's the part of the couch that I always sit on."

    scene harukathirdinvite23
    with dissolve

    h "I..."

    "Or...I guess we’re just going to jump straight to that."

    h "I..."

    if bonus == True:
        a "You what?"
        a "You are, right?"
    else:
        a "You what?"
        a "You didn't know?"
        a "It's just a couch??????"

    play sound "static.mp3"
    scene harukathirdinvite24
    with flash
    stop sound

    if bonus == True:
        a "Because I asked Molly more about you the other day after you stole Sensei away and she told me you were."
        a "Was Molly lying to me? "
        a "Or are you just a whore?"
        h "We’re...we’re just sitting here! Nothing happened!"
        s "Ami, really. Nothing happened."
        a "She looks awfully close to you for “nothing,” Sensei."
        a "I don’t think her {i}husband{/i} would like it very much if he saw the two of you like this."
        h "We’re not-"
        a "Sorry, would you mind getting off the couch if you’re going to talk to me?"
        a "I’m having a hard time focusing when you’re that close to {i}my{/i} Sensei."
        s "Ami...come on."
        h "No...No, I should probably get going."
        h "She’s...she’s right. I {i}am{/i} married...and...and..."
        h "Huh?"
    else:
        a "Because I'm pretty sure that you got all of those emails I sent about not sitting on side of the couch."
        s "Haruka did you ignore the emails"
        h "I think they were caught by my spam folder."
        a "Likely story!"

    play sound "static.mp3"
    scene harukathirdinvite25
    with flash
    stop sound

    h "Where did all these tears come from?"
    a "Are you crying now?"
    h "I’m...I..."
    a "Why are you crying if you didn’t do anything wrong?"

    if bonus == True:
        a "Could it be that maybe you already {i}did{/i} something wrong and you’re so overcome with guilt that you’re having trouble stomaching it?"
        a "Do you want a bucket? Sensei used to bring me a bucket when I was feeling nauseous."
        a "That’s a thing I know he does because he’s been with me for years and you’ve only known him for a few months."
        s "Ami, stop."
        a "Why? I live here. That’s my couch."
        a "She’s in my spot. I want her gone."
    else:
        s "She is very sensitive, Ami. Her husband was a couch."
        h "He was so comfortable."

    scene harukathirdinvite26
    with dissolve

    h "So much for her not being around today..."
    s "I really had no idea."
    h "I knew she liked you, but...doesn’t this seem a little excessive?"

    if bonus == True:
        a "Who are you to judge what is and isn’t excessive, you fucking slut?"
        a "Get away from my [uncle]. I don’t want him catching any STDs or other icky stuff that might impact how much time he gets to spend with me."
    else:
        a "Who are you to judge what is and isn’t excessive when you don't even read your emails?"
        s "She has a point, Haruka."
        h "I know. I am bad."

    scene harukathirdinvite27
    with dissolve

    s "Isn’t that enough? She’s already crying."
    s "I get that you want to keep me to yourself, but Haruka is a friend of mine. You can’t talk to her like that."
    a "Sure I can. You heard her, right? She’s married."
    a "I’m saving everybody a load of heartbreak right now."
    h "She’s...got a point..."
    h "It would...be best for everyone if...I just went home for the night."
    a "Sensei, when she leaves, what do you want me to make you for dinner?"
    s "Can you at least go into your room and let me say goodbye to her alone?"
    a "I’d really rather not."

    scene harukathirdinvite28
    with dissolve

    h "{i}Let’s...go out next time, okay?{/i}"
    h "{i}I don’t really think I’m welcome here...{/i}"
    s "…"
    s "Sure..."

    scene black
    with dissolve2

    "Haruka quickly scurries out of the living room without making eye contact with Ami."
    "But what’s so confusing to me is that, even though she was confronted and berated from the moment Ami came home, she still suggested a “next time.”"
    "Is she really so lonely that she’s fine with risking another run-in like this for a chance to be with me?"
    "Why?"
    "…"
    "Oh, right."
    "She can’t help it."
    "She’s already in my vase."

    a "Sensei! Watch a movie and cuddle with me! "
    s "…"
    a "Sensei?"
    s "…"

    "I watch a movie and cuddle with Ami."

    $ renpy.end_replay()
    $ harukainvite3 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sadgirls2:
...
```

## Code that triggers this event

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label harukainvite:
    if harukainvite1 == False:
        jump harukainvite1
    if harukainvite1 == True and harukaskipped == False and harukainvite2 == False:
        jump harukainvite2
    if harukainvite3 == False and harukadate20 == True and harukasex == True:
        jump harukainvite3
...
```