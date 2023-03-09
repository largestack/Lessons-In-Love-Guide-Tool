# Fair & Square
Noriko event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikospecial20&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 400

❌Day of week is Monday

✅Event "[Main: Metal in Microwaves](./halloweentwo13.md)" is completed (event=halloweentwo13)



## Next events
* [Noriko: Homes for the Homeless](./norikodorm20.md)

## Event properties
* ID: norikospecial20
* Group: Noriko
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\NorikoEvents.rpy
Code:
```python
...
label norikospecial20:
    scene norikobow1
    with fade
    play music "wewereangels.mp3"

    a "And so the ice cream man said to Ayane, “That’s no golden retriever! That’s my landlord!”"
    s "…"
    a "What’s wrong? You normally love stories about the spontaneous yet lovable antics of Ayane Amamiya that always seem to have the beginnings cut out."
    s "Cut out of what, exactly?"
    a "What?"
    s "…"
    s "Nevermind."

    "I walk down the hall with Ami, preparing to leave[school] after a...day."
    "I don’t want to say it was a {i}normal{/i} day, though...because it was really anything but."
    "Molly is still determined to try and clear things up with me after what happened on Halloween, and I’m running out of excuses when it comes to avoiding her."
    "Sooner or later, I’m going to have to look her in the eyes and admit to what happened...but that’s kind of impossible to do when I can’t even {i}remember{/i} it."
    "The aftermath is still ingrained into my memory, though."

    if bonus == True:
        "And each time I feel myself getting harder from thinking about it, I have to slow down and remind myself that none of it was real."
    else:
        "I know it seemed like I hugged her while she was asleep, but if hug happens and no one is around to see the hug, does the hug {i}actually{/i} happen?"
        "None of it was real."

    "Or some of it was real."
    "Or none."
    "Or some."
    "Something did or didn’t happen."
    "I either liked or didn’t like it."
    "Part of me wishes that Tsuneyo would have just ended it right there, but I feel as if that part is not an actual desire of mine and just some selfish avoidance tactic buried underneath mountains of greed."
    "I’m tired of digging, though."
    "It’s impossible to know what lies beneath the surface without someone informing you, and I’ve always hated the feeling of dirt underneath my fingertips."
    "I don’t want to dig anymore. "
    "I just want someone to unearth whatever’s down there and tell me what I’m supposed to do."
    "How do I turn things back to normal? "
    "And what {i}was{/i} normal in the first place?"

    if bonus == True:
        "Emotionless sex with a handful of girls who were already attached to me before I even had to do anything?"
        "Is that what I want?"
        "Or, scratch that-"
        "Is that {i}everything{/i} I want?"

        play sound "static.mp3"
        scene lavendersgreen1 with flash
        scene lavendersgreen13 with flash
        scene lavendersgreen18 with flash
        scene lavendersgreen23 with flash
        scene lavendersgreen29 with flash
        scene lavendersgreen30 with flash
        scene norikobow2 with flash
        stop sound

        "Yes."
        "That’s everything."
        "This is my life."
        "This is who I am. "
        "Why would I ever want anything other than the easiest possible option?"
        "Working for things is exhausting."
        "I can just not work."
        "I can have Ami do everything for me."
        "She’ll do it. She loves me."
        "I didn’t do anything to Molly. I wouldn’t have done anything. "
        "Unless she wanted me to."
        "Did she want me to?"
        "Is that why she wants to talk to me?"
        "Does she want to do it again?"
        "What-"
    else:
        play sound "static.mp3"
        scene norikobow2 with flash
        stop sound

    a "Sensei?"
    s "…"
    a "What’s wrong?"
    s "…"
    s "Nothing, Ami."
    a "It doesn’t look like nothing."
    s "It’s-"
    a "Is it about Molly?"

    scene norikobow3
    with dissolve

    s "What do you know about Molly?"
    a "Uhh...nothing. I just noticed you were kinda avoiding her all day. And it seemed like it was a little more than just because she’s really annoying in...large doses."
    s "…"
    a "…"

    scene norikobow4
    with dissolve

    s "It’s not about her. "
    s "I’m just tired."
    a "I see..."
    a "Well, you can take a nap when we get home and I’ll make you dinner."
    a "It’s probably best to just stay home all day if you’re not feeling great. You can go be a weirdo dorm-invader some other time."
    s "...Yeah."
    s "Actually, can I ask you something?"
    a "Of course, Sensei. You can ask me anything you want."
    s "Is there {i}anything{/i} I could do that would make you...feel differently for me than you do right now?"

    scene norikobow5
    with dissolve

    a "Is there something specific you have in mind?"
    s "No."
    a "Quick answer."
    s "Yes. But yours isn’t. Just tell me and-"

    scene norikobow6
    with dissolve

    a "Of course not."
    a "I’ll love you forever and ever."

    if amifingered == False:
        a "The only question is whether or not that love will become too much for you one day."
        s "I don’t know what that’s supposed to mean."
        a "That’s just what you’re saying to yourself. "
        a "You know, Sensei."
        a "I think you’ve always known."
        a "But that’s a story for another-"

    else:
        a "There’s not a single thing you could do that would change that."
        a "Even if you became the most horrible person in the whole wide world, I’d still welcome you home with open arms and a warm bath."

        scene norikobow7
        with dissolve

        if bonus == True:
            a "Then maybe even a little {i}more{/i} if you know what I mean..."
            s "You only have two modes. I definitely know what you mean."
            a "I’ve got a third one, too. It just hasn’t been turned on yet."
        else:
            a "Except the bath would not be filled with water. It would be filled with {i}hermit crabs.{/i}"

        s "That's...worrying?"

    scene norikobow8
    with dissolve

    n "Sensei!"
    a "Noriko? What are you-"

    scene norikobow9
    with dissolve

    n "I’m sorry for my outburst during the Halloween party! "
    n "It was impulsive and childish and I want to put it behind us!"
    n "Please accept my apology!"
    s "…"
    a "Outburst? Is this about the bathroom thing?"

    "Why is she apologizing?"

    if bonus == True:
        "Because I fingered her sister?"
        "She’s apologizing to {i}me{/i} because {i}I{/i} fingered her sister and {i}she{/i} got upset about it?"
        "I don’t understand."
        "Why do things keep happening that I don’t understand lately?"
        "I should be saying sorry to her."

        play sound "static.mp3"
        scene nikihotel26 with flash
        scene norikosadhalloween5 with flash
        scene norikobow10 with flash
        stop sound
    else:
        "Because I keep putting vegetables in her desk when she isn't looking?"
        "I had no idea she even knew that was me."

        play sound "static.mp3"
        scene norikobow10 with flash
        stop sound

    "No. I didn’t do anything wrong."

    if bonus == True:
        "All I did was slip my fingers inside of someone she’s related to."
        "Someone I’ve done that same thing to probably hundreds of times before."
        "If she gets upset about that, that’s on her. "
        "I am not obligated to make her or anyone else happy. It would just make things better and easier if I did."
    else:
        "They were only vegetables."

    n "I understand that this is probably not the best time to do this, but if I have to go one more night without telling you how I feel, I’m going to rip my hair out."
    n "It doesn’t matter to me what you do with anyone! Whether it be Niki or...Maya...or even Ami! "
    a "It’s not {i}even{/i} Ami when I am indisputably Sensei’s number one girl, thank you very much."
    n "The point is that I need to be stronger! And less sensitive!"

    scene norikobow11
    with dissolve

    n "You don’t deserve to be burdened by the feelings of one more girl who doesn’t have her head on straight."
    n "So I want you to know that I, Noriko Nakayama, am not that!"
    n "I am impulsive! And I am selfish! And I am far too sensitive at times! "
    n "But I am strong! And independent! And so many more things that I want you to find out about!"

    scene norikobow12
    with dissolve

    n "So please...accept my apology!"
    a "…"
    s "…"

    scene norikobow13
    with fade

    a "Umm..."
    a "I’m...going to go home now and start warming up the bath for you..."
    a "I still don’t know what’s wrong, but...if it’s something involving Noriko and {i}not{/i} Molly, maybe talking to her about it will make you feel better?..."

    scene norikobow14
    with dissolve

    a "You’ve still gotta come home right away, though! Got it?"
    a "Don’t go running off with other people from your past when you’ve got the perfect [niece] waiting at home for you!"
    s "…"
    a "…"

    scene norikobow15
    with dissolve

    a "Really. Please don’t. "
    a "I know I said there’s nothing you could ever do that would make me change how I feel, but that would still hurt a lot and I’d cry forever. Also, the house would flood because we are out of tissues."

    if bonus == True:
        a "Why can’t you just use a sock or a t-shirt to do your business like a normal boy?"
        a "Not that I know what a {i}normal{/i} boy is when I’m just an innocent [niece] who-"

    s "I’ll still come home, Ami. Just let me talk to Noriko first."

    scene norikobow13
    with dissolve

    a "Okay."
    a "I love you, Sensei."
    s "…"
    a "…"
    a "............?"
    s "I love you too, Ami."

    scene norikobow16
    with dissolve

    a "Aww! I didn’t even have to tell you to say it that time!"

    scene norikobow17
    with dissolve

    a "Bye-bye, Sensei! Bye, Noriko!"
    a "Touch my [uncle] and I’ll cut your limbs off!"
    n "Thank you very much, Ami! I am humbled by the privilege to spend time with your [uncle]!"

    scene norikobow18
    with fade

    s "You know you don’t have to be that formal, right?"
    s "You don’t even have to apologize for your outburst. Let’s just ignore it and move on with our lives."
    n "I can’t do that, Sensei. "
    n "I’ve done something I promised not to do- and that’s getting in the way of you and someone else...Even if that someone else is my sister."
    n "But I made a {i}new{/i} promise to myself that I would win your heart fair and square! And that means no telling you who to see or what to do!"
    n "I want you to choose me for me! Not me as an alternative! And if your interest is going to wane, that just means I have to work harder!"
    s "…"
    n "I realize that I {i}am{/i} making a scene right now and that we have been likely receiving strange looks from some of the people in other classes...I can’t really tell because of the whole bowing thing-"
    n "But I need you to know that I am serious! And that I will accept any punishment you deem necessary!"
    s "…"
    n "{i}Any{/i} punishment! No matter how sick or twisted it may be!"
    s "…"
    n "And I know that now we’re probably getting even more stares, so it would be really nice if you would respond to me because I’m beginning to get embarrassed!"
    q "He accepts!"

    scene norikobow19
    with fade

    q "Such passion! Such determination! "
    q "Of course he accepts your apology! He’d be foolish not to!"
    s "…"

    scene norikobow20
    with dissolve

    if bonus == True:
        q "I have to admit, when I heard you screaming from around the corner of the hall, I thought “Oh great. Teenage drama. Don’t wanna touch this with a ten foot pole.”"
    else:
        q "I have to admit, when I heard you screaming from around the corner of the hall, I thought “Oh great. Drama. Don’t wanna touch this with a ten foot pole.”"

    q "But as my legs carried me closer and closer to the source of the noise, I was reminded that I {i}live{/i} for this sort of thing! And now I wish nothing but the best for the two of you!"
    s "..."

    scene norikobow21
    with dissolve

    if bonus == True:
        q "I don’t even care that this guy’s probably twice your age! Give ‘em hell, girl! "
    else:
        q "I don’t even care that this guy’s your teacher! Give ‘em hell, girl! "
        s "(Gasp)"

    q "Just remember to invite me to the wedding since I’ve been there for you from the start!"
    s "…"
    s "Who are you, exactly?"

    scene norikobow22
    with dissolve

    ima "Imani. "
    s "…"
    ima "Sorry, Imai. Keep forgetting we’re supposed to use last names first over here."
    ima "But if you want to just call me Imani, that’s cool too. What’s your name? You look like a..."
    ima "Uhhhhhhhh..."

    scene norikobow23
    with dissolve

    ima "Jose."
    s "…"
    s "No."
    s "What are you even doing here? We’re kind of in the middle of something."

    scene norikobow24
    with dissolve

    ima "Hey! Is that any way to treat the newest staff member at [kumon_mi_high]?! "
    ima "I’ve been nothing but accepting and supportive of you since the get-go and you’re already getting rid of me?! Where is my lawyer?!"
    s "You work here?"

    scene norikobow25
    with dissolve

    ima "I’m filling in for uhh...Miss Watabe, I think? Whoever the one on medical leave is."

    "Oh...right."
    "Wakana not being around means that someone obviously has to look after her students."
    "So I guess this Imani girl is just going to be around until she comes back."

    s "Well...nice to meet you, I guess. But-"

    scene norikobow26
    with dissolve

    if bonus == True:
        ima "Yeah, yeah. Hearts to break. Cradles to rock. I know how it is. "

    ima "Just take it easy on her, would ya? She seems really nice based on the five or six lines of dialogue I’ve heard from her."

    scene norikobow27
    with dissolve

    ima "Anyway byeeeeeeeeeeeeeeeeee! See you around probably maybe unless I get fired! WE’LL SEE!"
    s "…"

    scene norikobow28
    with fade

    s "Well, that was weird."

    if bonus == True:
        n "Yes. But it did not prevent me from imagining her with her clothes off."
    else:
        n "Yes. But she was nice and I am excited for her to be a recurring character in Lessons in Love from this point on."

    s "I’m glad to see that she at least managed to lighten the mood a little. It’s weird seeing you get serious like that."

    scene norikobow29
    with dissolve

    n "I {i}had{/i} to be."
    n "I hate coming off as weak or childish, and crying to you about a thing you did with my sister just made me look like some desperate loser who doesn’t want to actually {i}fight{/i} for you."
    n "But I really do wanna fight, Sensei. I’m not a kid anymore. "
    n "These feelings aren’t just...lingering traces of a first crush or...something I’ve become dependent on in order to get by. They’re {i}real{/i} feelings. For {i}you{/i}."
    n "So if bowing to you and asking for your forgiveness in the halls is the best way for me to get that across, I’ll be damned if I’m not gonna take the leap."

    "I sigh and attempt to force myself into the realization that I can’t control how Noriko or...how anyone else, for that matter, acts. "
    "She’s still just a [teenage]girl at the end of the day, no matter how “adult” she tries to be."
    "The real adult thing to do in this scenario would just be bottling up those feelings and turning a simple misunderstanding into an event that would prevent us from ever seeing one another again."
    "It’s that immature striving for forgiveness...or the hope that things can eventually change that you only get to see from girls like her."
    "And, if even for only a moment, I’m reminded of why I’ve been having so much “fun” in Kumon-mi."
    "In moments like this, where my back isn’t against the wall."
    "Where I don’t have to take the passenger seat and let my disfigured sense of morals guide my actions."
    "Where I can live without the worry of how {i}me{/i} living will impact others."
    "I wish it was possible to just ignore all of those more horrible parts of life."
    "But, then again, I’m sure that’s something everyone wishes."

    s "…"
    s "Okay. You’re forgiven."

    scene norikobow30
    with dissolve

    n "Really?!"
    s "Is it that much of a surprise? This whole time, I’ve been saying you have nothing to apologize for."
    n "Yeah, I know. But you could have been lying. People lie about stuff like that all the time."
    s "I try to only lie when I have something to gain from it. This isn’t really one of those times."
    s "Besides, just crying and begging for me to not do something isn’t really childish in my book. You’re fine, Noriko."

    scene norikobow31
    with dissolve

    n "Then, umm..."
    n "Can we maybe walk home together?"
    n "I know that Ami asked you to come home right away, but...it’s not like the dorms are that big of a detour. And it would make me really happy if-"
    s "Sure. I’m tired of just standing around here anyway."
    s "The sooner we get out of here, the better."
    n "Right!"
    n "Just, uhh..."
    n "I left my winter clothes in one of the gym lockers, so...I’m gonna run and grab them really quick."

    scene black
    with dissolve2

    "Noriko sprints off in the direction of the gym and I don’t know what else to do but just...continue standing around."
    "I don’t like standing around."
    "I want to walk."
    "I need to walk."
    "I need to leave[school]."
    "I need to-"

    n "Okay! Ready to go."
    s "Already? It’s only been thirty seconds."
    n "What are you talking about?"

    play sound "static.mp3"
    scene norikobow32 with flash
    stop sound

    n "What’s only been thirty seconds?"
    s "…"
    s "Weren’t we just in[school]?"
    n "Define “just,” because we left like ten minutes ago."
    n "Also, are you sure it’s okay for me to be holding your arm like this? I was kinda joking when I suggested it, but I’m all for it if you’re actually enjoying it."

    scene norikobow33
    with dissolve

    s "Oh. Yeah, you’re fine. I don’t really care. "
    n "Works for me! Your arms are a lot bigger now than when we were younger."
    s "That is how growing works, Noriko."
    n "I know, I know. Just...trying to make small talk since you seem a little out of it."
    s "I’m fine."
    s "I didn’t do anything."

    scene norikobow34
    with dissolve

    n "O...kay?..."
    s "…"
    n "…"
    s "…"
    n "…"

    scene black
    stop music

    if amifingered == False:
        "I walk Noriko home and everything is good."

        $ noriko_love += 1

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"

    else:
        if bonus == True:
            "I go home and fuck my [niece]."
        else:
            "I go home and hug my [niece]."

        $ noriko_love += 1
        $ ami_lust += 1

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
        "{i}Ami’s lust has increased to [ami_lust]!{/i}"

    $ renpy.end_replay()
    $ norikospecial20 = True

    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve

    "Bed."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    jump advancetotues

label norikodorm20:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
jump day120
    if totaldays >= 121 and day85 == True and day103 == True and day121 == False:
        jump day121
    if totaldays >= 126 and day103 == True and streets15 == True and chikadorm15 == True and day126 == False:
        jump day126
    if totaldays >= 128 and day103 == True and day126 == True and day == 5 and day128 == False:
        jump day128
    if totaldays >= 138 and day103 == True and day130 == True and day85 == True and day138 == False:
        jump day138
    if totaldays >= 139 and chika_lust >= 5 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False or chikadorm20 == True and mall20 == True and chika_lust >= 10 and day139 == False:
        jump day139
    if totaldays >= 140 and day138 == True and day140 == False:
        jump day140
    if totaldays >= 142 and amidorm15 == True and day140 == True and day142 == False:
        jump day142
    if totaldays >= 144 and day128 == True and day142 == True and day144 == False:
        jump day144
    if totaldays >= 150 and day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False:
        jump day150
    if totaldays >= 153 and day150 == True and day153 == False:
        jump day153
    if totaldays >= 154 and day153 == True and day154 == False:
        jump day154
    if (totaldays >= 200 and day == 5 and beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True
    and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and halloween1 == False):
        jump halloween1
    if totaldays >= 214 and makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day == 1 and day214 == False:
        jump day214
    if totaldays >= 215 and day214 == True and day == 2 and day215 == False:
        jump day215
    if totaldays >= 216 and day215 == True and day == 3 and day216 == False:
        jump day216
    if totaldays >= 217 and day216 == True and day == 4 and day217 == False:
        jump day217
    if totaldays >= 218 and day217 == True and day == 5 and day218 == False:
        jump day218
    if totaldays >= 230 and makoto_lust >= 10 and christmas7 == True and makotolust10 == False:
        jump makotolust10
    if totaldays >= 237 and day == 1 and christmas7 == True and day237 == False:
        jump day237
    if totaldays >= 239 and day == 3 and day237 == True and day239 == False:
        jump day239
    if totaldays >= 240 and day == 4 and day239 == True and day240 == False:
        jump day240
    if totaldays >= 244 and day == 1 and day240 == True and day244 == False:
        jump day244
    if totaldays >= 246 and day == 3 and day244 == True and day246 == False:
        jump day246
    if totaldays >= 247 and day == 4 and day246 == True and day247 == False:
        jump day247
    if totaldays >= 261 and day == 3 and day247 == True and kirininvite2 == True and bar35 == True and day261 == False:
        jump day261
    if totaldays >= 263 and day == 5 and day261 == True and day263 == False:
        jump day263
    if totaldays >= 264 and day == 1 and day263 == True and day264 == False:
        jump day264
    if totaldays >= 269 and day == 3 and day264 == True and day269 == False:
        jump day269
    if totaldays >= 270 and day == 4 and day269 == True and day270 == False:
        jump day270
    if totaldays >= 271 and day == 5 and day270 == True and day271 == False:
        jump day271
    if totaldays >= 272 and day271 == True and onseninvite == False:
        jump day272
    if totaldays >= 280 and day == 1 and day271 == True and rindorm45 == True and iodorm10 == True and nikidate5 == True and chikaonsen4 == True and yumidorm30 == True and norikofirsthall == True and convenience5 == True and day280 == False:
        jump day280
    if totaldays >= 281 and day == 2 and day280 == True and day281 == False:
        jump day281
    if totaldays >= 282 and day == 3 and day281 == True and day282 == False:
        jump day282
    if totaldays >= 283 and day == 4 and day282 == True and day283 == False:
        jump day283
    if totaldays >= 287 and day == 1 and day283 == True and day287 == False:
        jump day287
    if totaldays >= 288 and day == 2 and day287 == True and day288 == False:
        jump day288
    if totaldays >= 295 and day == 3 and day288 == True and chikaonsen4 == True and amidate35 == True and makotowinterbeach4 == True and day295 == False:
        jump day295
    if totaldays >= 297 and day == 5 and day295parttwo == True and day297 == False:
        jump day297
    if totaldays >= 302 and day == 3 and day297 == True and day302 == False:
        jump day302
    if totaldays >= 303 and day == 4 and day302 == True and day303 == False:
        jump day303
    if totaldays >= 304 and day == 5 and day303 == True and day304 == False:
        jump day304
    if totaldays >= 318 and day == 5 and toukadorm5 == True and utadorm10 == True and mikudorm40 == True and mollydorm20 == True and otohadorm5 == True and kirindorm20 == True and iodorm10 == True and yukidate5 == True and sanadorm40 == True and yasudorm10 == True and day318 == False:
        jump day318
    if totaldays >= 333 and dormwar17 == True and day333 == False:
        jump day333
    if totaldays >= 340 and ayanedorm35 == True and day == 2 and day340 == False:
        jump day340
    if totaldays >= 351 and thirdreset3 == True and utadorm20 == True and day351 == False:
        jump day351
    if totaldays >= 355 and day351 == True and day355 == False:
        jump day355
    if totaldays >= 400 and secondbeach18 == True and (rindate50 == True or (rindorm50special == True and rinbetrayed == True)) and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False:
        jump halloweentwo1
    if totaldays >= 400 and day == 1 and halloweentwo13 == True and norikospecial20 == False:
        jump norikospecial20
...
```