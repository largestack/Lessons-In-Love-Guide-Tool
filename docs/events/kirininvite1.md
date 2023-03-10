# Too Much, All at Once (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

* [Kirin: No Extortion Necessary](./kirininvite2.md)

## Event properties

* Id: kirininvite1
* Group: Kirin
* Triggered by label: kirininvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->kirininvite->kirininvite1

## Official wiki page

[Too Much, All at Once](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirininvite1&go=Go) for more details.

## Event code

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirininvite1:
    play sound "phonebeep.wav"

    "I tap on Kirin’s name in my phone and wait for her to answer."
    "Whenever the two of us hang out, it’s usually something along the lines of me going over to {i}her{/i} part of town and just...killing time however {i}she{/i} wants to that day."
    "But I feel like we’ve gotten close enough at this point that she’d be willing to hang out at my place instead."
    "Now, knowing Kirin, it’s highly possible that she’s been waiting for me to invite her over this entire time-"
    "But it’s not exactly easy finding an opportunity to bring over a girl from another class, and there’s no way Ami wouldn’t be suspicious of that if she caught it happening."
    "As such, today might be the only chance I have for a while to actually follow through with the idea, as her and some of the others are going shopping in the urban district of Kumon-mi."

    play sound "phonebeep.wav"

    ki "Hey~ Whatcha up to?"
    s "Heading back to my place. You?"
    ki "What a coincidence. I’m {i}also{/i} heading back to my place."
    s "Wow. Maybe this is some sort of sign?"
    ki "Maybe it is! Are you suggesting we hang out?"
    s "I suppose I might be. Do you have any objections to coming over my place this time?"
    ki "Uhh...where do you even live?"
    s "Do you know where Ayane lives?"
    ki "Yeah. You’re over there?"
    s "No. Nowhere near it, actually."
    ki "...Then why would you even bring that up?"
    s "I’ll just text you the address. You can make it in less than an hour coming from your apartment."
    ki "You’ve been traveling that far just to meet up with me this whole time?"
    s "Yeah. I’m so kind, aren’t I?"
    ki "That or you just really like walking."
    ki "Is Ami home right now? Or is this the same kind of secret meeting we have when you come over my place?"
    s "I would absolutely not invite you over if Ami was there."
    ki "Ouch."
    ki "But yeah, text me the address. I’ll head over now."
    ki "We’re ordering food, though. I’m starving."
    s "Deal."
    ki "Sweet. See you soon, [kirinmaster]~"

    play sound "phonebeep.wav"

    "The call comes to an end and I immediately send Kirin my address."
    "She doesn’t respond, but I guess there’s not really any reason to, considering a street name and some numbers aren’t a great start to a conversation."

    scene black
    with dissolve
    stop music fadeout 5.0

    "The walk back is a cold one. The wind is out in full force today."
    "I feel kind of bad for making Kirin bear this all the way over, but one of us was going to wind up suffering through it no matter what."
    "I’ll just make it up to her by buying her dinner whenever we decide on something to order."
    "………"
    "……"
    "…"

    scene kirinfirstinvite1
    with dissolve
    play music "normalday.mp3"

    ki "Thanks for having me~"

    "Kirin lets herself in once I give her the okay and slides her boots off at the door before gleefully trotting up to me."

    s "Your cheeks are bright red. You’re not nervous about being alone in my house, are you?"

    if bonus == True:
        ki "No. I’m just freezing cold since I walked all the way over here on the windiest day ever."
        ki "I basically had to hold my skirt down the entire way so it wouldn’t blow up and give everybody a peek at my underwear."
        ki "They're black, in case you were wondering."
    else:
        ki "No, I'm just cold."
        ki "Also, what the fuck is a canola and how do they get the oil out of it? Do you ever wonder that, Sensei?"

    "Jokes on you, Kirin. I'm {i}always{/i} wondering."

    if bonus == True:
        s "That’s basically the exact opposite of what you did when you came into my office for the first time."
        ki "Ooooh, I remember that. When I showed you my panties and you didn’t even get hard."
        s "I think I did. But it was a pretty confusing meeting and I don’t remember much of it other than that you owe me your virginity now."

        scene kirinfirstinvite2
        with dissolve

        ki "Oh, about that. "
        ki "Do you think there will be a lot of blood? I’m not really sure what to expect."
        s "Just look it up online. I don’t want to talk about the amount of blood that will come out of you."
        ki "I tried, but I keep getting different answers and I figured it would be better to ask you since you’ve definitely taken a few v-cards by now."
        s "You’re wasting no time in getting into the accusations today."

        scene kirinfirstinvite3
        with dissolve

        ki "Heheh~ I know you’ve stolen at least {i}one{/i}. But, for all I know, you could be screwing half of the soccer team by now."
        s "There’s no way I’d be able to do that without you finding out about it."
        ki "Yeah, I think it’s fair to assume that I’ll figure out pretty much everything you do sooner or later, so you should just be open and honest with me."
        ki "That’s more fun anyway, right?"
        s "In that case, let me start this “open and honest” meeting by saying you look very cute today."

        scene kirinfirstinvite4
        with dissolve

        ki "Thanks! But, just so you remember, I’m not blushing and my cheeks are only red from the cold."
        ki "I {i}know{/i} I look extra cute today, though, so I’m glad you’re being honest with me."
        ki "As repayment, I’ll say one honest thing to you as well."

        scene kirinfirstinvite5
        with dissolve

        ki "I’m lowkey really fucking nervous about losing my virginity today."
        ki "Like, I was fine with it when you called me. "
        ki "But the walk over here was so long that it gave me way too much time to think and now I can’t tell if my hands are shaking from the cold or from my nerves."
        s "…"
        s "Well, that’s significantly more open and honest than I was."

        scene kirinfirstinvite6
        with dissolve

        ki "Hahahaha...yeaaaaaah..."
        ki "Also, I didn’t have time to shave since I came directly from the convenience store and that’s making me self-conscious too."
        ki "So like, you can still totally do me some other time buuuuuut I’m kind of scared as fuck right now."
        ki "Just too much all at once, I guess."
    else:
        s "Well, if you need a warm blanket or a mug of hot cacao to warm yourself up, just let me know. My primary concern is making you feel safe and welcome."
        ki "Wait, no. Answer the canola question. It's important."
        s "I can't, Kirin. Knowing the truth would only make you too powerful."
        ki "Sensei-"
        s "Do you want the cacao or not?"
        ki "...Yes please."
        s "I will put the kettle on right away."

    scene kirinfirstinvite7
    with dissolve

    ki "But, uhh...now that {i}that’s{/i} out of the way, what did you want to eat for dinner?"
    ki "I was thinking we could just order from a bunch of different places and then split whatever the cost is."

    if bonus == True:
        s "That jump between subjects was incredibly jarring based on everything I just learned."
        ki "I was just repaying your honesty with my own honesty. Don’t think it was some huge breakthrough or anything."
        ki "The {i}real{/i} breakthrough will be when you tear through my hymen and cause an undisclosed amount of blood to come pouring out of me."
        s "…"
        ki "…"
        s "So, about dinner-"
    else:
        s "Absolutely not. Allow me to front the bill as both your teacher and closest friend."

    scene kirinfirstinvite8
    with dissolve

    ki "This is really awkward."
    s "It is, but I’m definitely not taking the blame for it this time."
    ki "I know. I’m clearly less prepared than I thought I’d be for something like this."
    s "…"
    ki "…"
    ki "So, dinner."
    s "Right, dinner."

    scene black
    with dissolve

    "Well, that was not exactly the start to this visit that I was expecting."
    "It was...nice seeing Kirin be honest about something that wasn’t entirely malicious or confusing for once, though."
    "It’s probably the first thing I’ve seen her do that I can actually say I understand."

    if bonus == True:
        "Opening up about your fears isn’t an easy thing to do, which is likely why she used my compliment as a crutch to piggyback off of."
        "Within minutes of arriving here, she felt threatened and took a defensive stance."
        "And, when you’re around someone like me, or whatever her vision of me is, there’s no harm in taking a few extra precautions."

    "…"
    "The two of us proceed to flip through a number of takeout menus that Ami and I keep on top of the microwave, ordering from a grand total of four of them."
    "I don’t take Kirin up on her offer to split the bill and decide to pay for everything myself, figuring I can keep any leftovers and just...eat them throughout the week."
    "And, within forty-five minutes or so, our feast is finally ready to begin."

    scene kirinfirstinvite9
    with dissolve

    ki "So, uhh...That was kind of weird before, right?"

    if bonus == True:
        ki "I mean, {i}me{/i} being the one to say all that stuff about getting nervous when I’ve done nothing but try and get into your pants since I met you."
        ki "What was that all about, right? Hahaha..."
    else:
        ki "I mean, like...what if {i}Canola{/i} is just the name of the brand?"

    s "You really don’t have to keep bringing this up, Kirin. We can just eat now."

    scene kirinfirstinvite10
    with dissolve

    ki "Ahhhhh I know that!"
    ki "I just feel so immature all of a sudden and I don’t like it."
    ki "Can’t you just come out and admit something equally embarrassing so I can get over this?"
    s "I...can’t really think of anything that embarrassing, to be honest."

    if bonus == True:
        ki "What, you never like, walked in on your parents having sex when you were little or something?"
        s "Not that I can remember."

        "I can’t even remember what my parents looked like..."

        ki "Nothing with your [niece], either?"
        ki "You guys live together so like...she’s probably caught you jerking it or something before, right?"
    else:
        ki "What, you never like, accidentally called your teacher Mom or anything?"

    s "Surprisingly, no."

    scene kirinfirstinvite11
    with dissolve

    ki "Jesus, how boring is your life?"

    if bonus == True:
        ki "How have you not done {i}anything{/i} embarrassing when there are over ten hormonal [teenager]s watching you at all times?"
        ki "Myself included."
        ki "Don’t think I’m quitting the game just because I got nervous and said some stuff I was thinking earlier."
        ki "I still want you to go to fucking town on me eventually."
        s "..."
        s "I’m glad to see you’re back to normal, Kirin."
    else:
        s "It's not boring. It's fulfilling, calm, and full of hugs. Just the way I want it."
        ki "Yeah, yeah...I get it. I'm just feeling a little off today."
        s "Well I hope that the cacao you drank offscreen helped."
        ki "It did."

    scene kirinfirstinvite12
    with dissolve

    ki "Yeah, I’m pretty sure I just needed sugar or something."
    ki "I’m feeling a lot better now and I’m literally like two inches away from you."

    scene kirinfirstinvite13
    with dissolve

    if bonus == True:
        ki "Do you want a blowjob after we’re done eating?"
    else:
        ki "Do you want a hug after we’re done eating?"
        s "Ah! Hug! I love hugs!"

    ki "That’s gotta be worth dinner and those five minutes of counseling I needed earlier, right?"
    s "Not if you’re going to make it sound like I’m extorting you."

    if kirinbeachhj == False and bonus == True:
        scene kirinfirstinvite14
        with dissolve

        ki "So...first you turn down my free handjob on the beach...and now you’re turning down my mouth?"
        ki "You really {i}are{/i} gay, aren’t you?"
        s "I’m not gay..."
        ki "Well then what’s the deal?"
        ki "Why are you pushing me away? What am I doing that’s so wrong?"
        ki "I just..."

    scene kirinfirstinvite15
    with dissolve

    ki "Hah..."
    ki "I don’t offer these things just to get you to like me, Sensei. "
    ki "I want to have fun with you and I want {i}you{/i} to {i}want{/i} to have fun with me."

    if bonus == False:
        s "How are we to have fun without any board games?"

    scene kirinfirstinvite16
    with dissolve

    ki "But I guess having you buy me dinner is enough fun for today."

    if bonus == True:
        ki "I’ll probably be too full afterward to suck you off anyway."
        ki "And you know what they say about giving blowjobs on a full stomach."
        s "I have no idea what they say about that."
        ki "Oh. Well, they probably say it’s bad or whatever."
        ki "I don’t know. I kind of just made that up hoping you wouldn't actually respond to it."
    else:
        ki "Besides, any second now, lock.mp3 is going to play and Ami is going to show up."

    play sound "lock.mp3"
    scene kirinfirstinvite17
    "Our conversation is suddenly interrupted by what may just be the last sound effect I ever hear."

    ki "What was that noise just now?"

    if bonus == False:
        s "lock.mp3"

    ki "You heard that, right?"
    s "Either Ami is home way ahead of schedule or I am about to be robbed."
    ki "Neither of those things are good for me."
    s "Which one of them do you think sounds good for {i}me{/i}?"
    ki "The Ami one, obviously."
    s "It would probably be safer getting robbed than having to deal with the fallout of her finding us together."
    ki "Jesus. What kind of relationship do you two have?"

    play sound "dooropen.mp3"

    a "I’m home!"
    s "I’m going to die."

    scene kirinfirstinvite18
    with dissolve

    ki "No...you’re not."
    ki "Do you have any idea how many times I’ve stealthily [masturbate]d in the same room as my sister, Sensei?"
    ki "I’ll show you how good I am at being undetected."
    ki "Watch."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene kirinfirstinvite19
    with dissolve

    a "…"
    s "…"
    ki "…"
    a "Umm..."
    a "What’s...going on here?"
    s "…"
    s "I was very hungry."

    scene kirinfirstinvite20
    with dissolve

    a "Don’t you think...this is a little much?"
    s "…"
    s "I thought Maya might be coming over when you got home."

    scene kirinfirstinvite21

    a "Oh, okay. Then yeah, that makes sense."
    s "Why are you back so early? I thought you were going shopping."

    scene kirinfirstinvite22
    with dissolve

    a "We were going to but...it was just way too cold and none of us wanted to wait at the bus stop."
    a "So we all just decided to head back."
    s "Cool, cool."
    a "Oh, Sensei. I saw a nice pair of boots at the door. Did you buy those for me?"

    scene kirinfirstinvite23
    with dissolve

    s "...Yes."
    ki "{i}For real? Those are my favorite boots.{/i}"
    a "Hm?"
    a "Did you hear something just now?"
    s "All I heard was the sound of my regret for not being able to wrap the boots I definitely bought you in time."
    a "Do you...want me to go into my room so you can wrap them now?"
    s "...Yes."

    scene black
    with dissolve2

    "Ami, bless her heart, is gullible enough to take the bait and disappears into her room for the next few minutes, giving Kirin enough time to flee the house."
    "Obviously, I didn’t make her walk home without her boots on, so now I just...need to figure out an excuse to give to Ami for why her “present” so suddenly vanished."
    "I don’t hear from Kirin again until she gets home- and even then, all I get are exhausted face emojis."
    "But, despite a rocky start, a rocky ending, and a...normal middle part (?) the evening isn’t a complete disaster."
    "It wasn’t ideal by any means, but I don’t think something like this will be enough to keep her away in the future..."

    $ renpy.end_replay()
    $ kirininvite1 = True
    $ kirin_love += 3
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirininvite2:
...
```

## Code that triggers this event

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirininvite:
    if kirininvite1 == False:
        jump kirininvite1
...
```