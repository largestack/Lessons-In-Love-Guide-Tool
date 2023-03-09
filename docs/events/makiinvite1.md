# Traveling Lube Dealer
Maki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makiinvite1&go=Go)



## Event preconditions
✅Event "[Main: Metal in Microwaves](./halloweentwo13.md)" is completed (event=halloweentwo13)



## Next events
* [Maki: Special Occasions](./makiinvite2.md)

## Event properties
* ID: makiinvite1
* Group: Maki
* Triggered by label: makiinvite
* Triggered by branch label: inviteover

## Event code
File: \game\MakiEvents.rpy
Code:
```python
...
label makiinvite1:
    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and wait for her to answer."
    "I’m not exactly sure how Ami will handle me inviting over the mother of her arch nemesis, but I’ll be damned if I let an obnoxious girl with A-cups rule my life."
    "I am an adult looking for another adult to do adult things with- and Maki is the only adult I know who is very rarely busy with anything since her daughter can just take over."
    "I mean, I guess Sara would also work, but I feel like it’s a lot easier to sell porn than it is to revitalize a failing bar. No offense, Sana."

    play sound "phonebeep.wav"

    if bonus == True:
        maki "Gangbang hotline, this is Maki speaking."
        s "Before I place an order, are you able to clarify if {i}I{/i} would be the one getting gangbanged? Or am I calling to participate in a gangbang? "
        maki "I would not be willing to clarify that, no. Would you still like to place an order?"
        s "Sure. One Maki, please."
        maki "Can it be any Maki or are you looking for a particular model?"
        s "Do you want to hang out or are you just going to keep being weird?"
        maki "Mmm...I choose both!"
    else:
        maki "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHH!"
        s "Why are you screaming?"
        maki "I don't know. Can I come over?"
        s "I guess."

    s "Just don’t be {i}too{/i} weird in front of my [niece]. She already kind of hates your daughter, so you’re kind of starting off on thin ice."
    maki "What? Why would anyone ever hate Makoto? Makoto is great. "
    maki "I hope your [niece] is ready to throw hands."
    s "Okay. Sending you the address now. "

    if bonus == True:
        maki "How much lube should I-"
    else:
        maki "Sure! But I recently started selling lotion and-"

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone and quickly text Maki my address."

    if bonus == True:
        "I feel mostly safe in assuming that she won’t actually be bringing any lube, but I ask her to leave everything behind in the event that she just...doesn't care about anything I say."
        "It’s one thing bringing an older, lazier looking Makoto over to the house, but having her come equipped with what I imagine is an entire collection of lubricant would be too hard for even {i}me{/i} to get out of."
        "Either way, I wait for Maki to confirm that she’s on her way over and slide my phone back into my pocket before setting course home."

    "………"
    "……"
    "…"

    scene makifirstinv1
    with dissolve
    play sound "dooropen.mp3"
    play music "normalday.mp3"

    "I make my way inside and prepare myself for what I hope will be a rather easy and dramaless night in."

    a "Get out of here!"

    "It appears that will not be the case."

    s "I don’t know what I did, but-"
    a "You mean to tell me that for only 1,000 yen a month, I can get all of the lotion I want?! "
    s "…"
    maki "That’s right, Ami! And this isn’t just {i}any{/i} lotion...it’s lotion {i}guaranteed{/i} to keep you looking [young]and energetic for the rest of eternity."
    a "Ahh, that’s even better! My [uncle]’s not home right now so he won’t get mad at me for saying this, but he {i}really{/i} seems to like [younger_girls]."
    s "…"
    maki "Does he now? Well, then I...totally understand why you’d want him to look at you that way! "

    play sound "dooropen.mp3"
    scene black
    with dissolve

    "Maybe I should just come back later."

    a "Wait, Sensei?! Is that you or did somebody break in?!"
    s "…"

    play sound "dooropen.mp3"
    scene makifirstinv2
    with dissolve

    s "Hah...Hi, Ami. And hi-"

    if bonus == True:
        maki "Felicity Fellatio, at your service!"
        s "…"
        a "Sensei! Miss Fellatio says that for only 1,000 yen a month, I can have all the lotion I want!"
        a "Can I borrow 1,000 yen a month so I can be pretty {i}forever?{/i}"
        s "You have a job now. Use your own money."
        s "Also, don’t you think her last name is kind of suspicious?"
        a "Hm? Isn’t fellatio some type of...Italian dessert or something? Stop being so culturally insensitive, Sensei."
    else:
        maki "Just call me Ami 2!"
        s "No."

    scene makifirstinv3
    with dissolve

    maki "Now, I know what you’re thinking."
    s "Do you really, though?"
    maki "Of course! {i}You’re{/i} thinking...“Wow! Only 1,000 yen a month?! What a steal!” "
    maki "Well, let me tell you this, buddy. It really all starts to make sense when you take a look at our business model."
    s "You don’t even have any products with you."
    a "She showed up with a whole suitcase of all different kinds of exotic lotions. "
    a "I thought it was a little strange when she knocked since we don’t really get a lot of door to door salespeople around here, but as soon as I smelled what was inside, I immediately knew what was going on."
    s "I’m sure you did, Ami. "

    scene makifirstinv4
    with dissolve

    maki "Oh my. It appears we may have a bit of a skeptic on our hands!"
    maki "Tell me, fine sir who I have never met before, how would {i}you{/i} like to sample some of my one of a kind, {i}exotic{/i} hand lotions?"
    s "You mean the “hand lotions” I specifically asked you not to bring?"

    scene makifirstinv5
    with dissolve

    a "Wait, you were expecting her, Sensei? Did you set up an appointment thingy with this lady?"
    a "My birthday isn’t for a long time, so-"

    scene makifirstinv6
    with dissolve

    a "Wait, is this an early Christmas present?! You’re getting me a lifetime supply of youthful lotion so I can stay adorable forever?!"

    if bonus == True:
        s "No. This is actually Makoto’s mom and her suitcase is full of a bunch of stuff that is most definitely not lotion."
        a "...What?"
    else:
        s "No. This is actually Makoto’s mom and all of that lotion is for me. I have very dry skin."
        a "...What?"

    maki "Why didn’t you just go along with it? "
    s "Better question, how did you manage to get here before me?"

    scene makifirstinv7
    with dissolve

    maki "I just happened to be making my rounds in the area as a totally legitimate lotion sales rep! And since you {i}scheduled an appointment with me{/i}, I was {i}always{/i} going to show up."
    a "Sensei, would you mind explaining to me what is going on here?"
    s "I kind of did already."
    a "So this actually {i}is{/i} Makoto’s mom?"

    scene makifirstinv8
    with dissolve

    maki "Uhh...yes! But just because I lied about my name doesn’t mean I lied about the product!"
    a "I {i}thought{/i} you looked familiar..."

    if bonus == True:
        s "Maki, why are you still so focused on selling a product that doesn’t even exist?"
    else:
        s "Anything for a sale, right? You're a true business woman, Ami 2."

    scene makifirstinv9
    with dissolve

    maki "It’s in my blood, obviously! My job is to sell things! And sometimes, in order to sell things, you need to lie about them!"

    if bonus == True:
        maki "“{i}Excuse me, miss, but does this vibrator have multiple speeds?{/i}” “Why, of course it does! Just don’t read the part of the box that says it only has one!”"
        maki "“{i}Excuse me, miss, but my wrists are very sensitive. Do you have any velcro handcuffs?{/i}” “Why, of course I do! Because that product totally exists!”"

    s "How are you still in business?"

    if bonus == True:
        maki "Because I sell fucking porn, not security devices. No one’s going to ask for their money back so long as they still have an orgasm at the end of the day."
    else:
        maki "Because I sell fucking porn, not security devices."

    a "You sell {i}what{/i}?"

    scene makifirstinv10
    with dissolve

    maki "Corn! Canned! Cobbed! Creamed! Any type of-"

    scene makifirstinv11
    with dissolve

    maki "Pfft~"

    if bonus == True:
        maki "Creamed..."
    else:
        maki "Corn..."

    a "..."
    s "..."

    scene black
    with dissolve

    "Perhaps I should have played along."
    "And you know, maybe in another life, I would have."

    if bonus == True:
        "But as Ami’s legal guardian and a man who, on several occasions, has let her borrow my credit card, I refuse to allow her to get sucked into a fictional pyramid scheme."
    else:
        "But as Ami's little pogchamp, I owe it to her to be honest."

    "Even if it means sentencing her to a life of hating Makoto’s mother- something I’m already sure was going to happen anyway."
    "………"
    "……"
    "…"

    scene makifirstinv12
    with dissolve

    a "You betrayed me! I invite you into my house because your suitcase smells good and {i}this{/i} is how you repay me?!"
    a "Get out and never come back!"

    if bonus == True:
        maki "Fine! I admit it! I took advantage of your trust and made you believe my suitcase full of lubricant was a suitcase full of lotion! "
        a "Why are you selling something that weird door to door?! Are you some kind of...nymphomaniac or something?!"
        s "Ami, come on. You can’t just elect to believe the door to door part of her story. It’s clearly all part of a coordinated effort to-"
    else:
        maki "You're not my mom! I don't have to listen to you!"

    scene makifirstinv13
    with dissolve

    a "How many more Miyamuras are you going to invite into this household, Sensei?"
    maki "If you wind up inviting a third, can you ask him to {i}at least{/i} come say hello to his daughter? She misses him."

    if bonus == True:
        s "I’m not inviting any other Miyamuras over to the house. One was more than enough and that still didn’t deter me from bringing in Maki and her lube collection."
        maki "Heh. You said lube."
    else:
        s "I’m not inviting any other Miyamuras over to the house. One was more than enough and that still didn’t deter me from bringing in Maki and all of her fancy lotions."
        maki "I'm not Maki. I am Ami 2."

    scene makifirstinv14
    with dissolve

    a "Get out of my house, you harlot!"
    maki "Harlot? Is this the renaissance? Have some dignity and call me a whore like a normal girl."
    a "I can’t tell which of you is worse! You or Makoto!"

    if bonus == True:
        maki "Me, obviously. Makoto is just the prettier, smarter, less sexually confident version. And if there is anything worth admiring in today’s political climate, it is a lack of sexual confidence."
        maki "And also a surplus of sexual confidence. As long as it’s one or the other, things’ll be good. "
        maki "Anyway, were you going to buy any {i}lotion{/i} or should I start packing my things?"
    else:
        maki "Obviously me! Makoto is great!"
        maki "But seeing as I am no longer welcome here, I will start packing my things."

    s "You’re not planning on leaving already, are you?"

    scene makifirstinv15
    with dissolve

    a "Why do you want her here when you have me?!"
    maki "You’re actually okay with me staying? "

    if bonus == True:
        maki "I could have sworn the whole pretending to be a saleswoman and roping your [niece] into a make believe pyramid scheme by calling lube lotion would have been your sign to be like, “Bye, Maki.”"
        s "Well, you have sworn incorrectly."
        s "Besides, this gives me the opportunity to try something I’ve been wanting to try for a long time now."
        maki "I hope it involves lube, because I brought plenty."
    else:
        s "Yeah. I still need to go through all of the lotions and figure out which one is best for my skin."

    a "You can’t be serious!"
    s "I am serious. In fact...I am so serious, that I am, going to do {i}this.{/i}"
    a "Lay one finger on her and she’ll be leaving this house in a variety of different bags!"
    s "Ami-"

    stop music

    s "Go to your room."

    scene makifirstinv16
    with dissolve

    a "Ah..."
    a "You {i}didn’t...{/i}"
    maki "Hah. Get parented, loser."
    s "Right now, [young]lady."

    "I do my best to put on an adult voice, but I’m pretty sure it’s just my normal voice."
    "Probably because I’m an adult."

    play music "normalday.mp3"

    a "You..."
    a "Why do I...actually feel compelled to go to my room?..."
    s "Because starting right now, you are grounded."

    scene makifirstinv17
    with dissolve

    a "For...for how long?!"
    s "Until Maki leaves. After that, you can do whatever. "
    a "Why am I in trouble when all I wanted to do was protect your honor?!"
    maki "Be careful or he might {i}actually{/i} ground you."
    s "Ami. Room."

    scene makifirstinv18
    with dissolve

    a "GRAAAAAAH! I STILL HATE YOU AND YOUR STUPID DAUGHTER!"

    scene makifirstinv19
    with dissolve
    play sound "doorslam.mp3"

    "Ami [[miraculously] goes into her room and slams the door behind her."
    "And, in other news, I gained a new power today."

    if bonus == True:
        maki "You know, if I knew this was going to turn into a whole thing, I would have just left the lube behind."
    else:
        maki "You know, if I knew this was going to turn into a whole thing, I would have just left the lotion behind."

    scene makifirstinv20
    with fade

    s "You mean like I {i}asked{/i} you to?"

    if bonus == True:
        maki "I thought that was a joke. I wasn’t about to miss out on an opportunity to break out the travel lube. Do you have any idea how long it’s been since I got to show that to anyone?"
        maki "Cause it’s been a long time, Sensei. A {i}long{/i} time."
    else:
        maki "Did you ask me something like that?"
        s "Maybe not in this game, but I swore I could have asked in the last one."
        maki "Huh. Either way-"
        maki "You hung up on me and I wanted to spite you."

    s "That aside, I think it’s safe to assume Ami hates you now."

    scene makifirstinv21
    with dissolve

    maki "Excellent."
    s "Why is that excellent? Normally, when you get invited over to a person’s house, you’re supposed to try to {i}not{/i} make them hate you."
    maki "Normally, yes. But I came here with the knowledge that, for some reason, your fake daughter has a problem with my real daughter."
    s "She is my [niece], not my daughter."

    if bonus == True:
        maki "I bet she calls you Daddy in her fantasies."
    else:
        maki "I bet she still thinks of you as her daddy."

    if amimaster.lower() in ["daddy"]:
        "I mean...she calls me that in a lot more than just her fantasies."
        "But even if that’s the case, I can’t let Maki actually believe it."

    s "Her real dad is actually dead, so...probably not."

    scene makifirstinv22
    with dissolve

    maki "Oh...crap."
    maki "I’m sorry. I didn’t mean to bring up bad memories."
    s "It’s fine. I don’t have many memories of it in the first place."

    play sound "static.mp3"
    scene amiani4 with flash
    scene makifirstinv22 with flash
    stop sound

    maki "Either way, I crossed a line and I’m sorry."
    s "..."

    scene makifirstinv23
    with dissolve

    maki "But, uhh...what I meant by the whole “excellent” comment is that now, by comparison, Ami will probably hate {i}me{/i} a little more than Makoto."
    s "That wasn’t your plan from the start, was it?"

    scene makifirstinv24
    with dissolve

    if bonus == True:
        maki "No. I just wanted to hang out and talk and maybe show off all of my cool lubes."
        maki "But halfway through my sales pitch, I started thinking, “You know what? This is probably going to go south eventually.”"
        maki "In my defense, though, if you hadn’t taken your sweet ass time getting over here, this never would have happened."
        s "What are you talking about? I came right over after I called you."
        maki "Well then I guess I’m just super fast and you’re the human equivalent of a turtle."
        maki "Anyway, want to go get dinner or something? It’s nice being invited over, but it feels a little strange when your [niece] likely has her ear to the door to make sure we’re not having sex."
    else:
        maki "No. I just really need the money and have to sell as many lotions as possible or I'm going to have to take out a second mortgage on my home."
        maki "Anyway, want to go out to a fancy restaurant or something? I will pay."
        s "Sure. That sounds great."

    play sound "knock.mp3"

    a "{i}THAT’S RIGHT! RUN AWAY, MAKOTO’S MOM! THIS HOUSE BELONGS TO THE ARAKAWAS!"

    if bonus == True:
        maki "See what I mean?"
        s "You’ll grow to accept her in due time. Ami just has a very strong sense of family values."

        if amilust15 == True:
            "In fact, it’s so strong that sometimes she even starts masturbating in my bed while I’m asleep."
            "Just normal family stuff, I suppose."

        scene makifirstinv25
        with dissolve

        maki "I wish Makoto was like that."
        maki "Sometimes, I feel like she doesn’t really care {i}what{/i} I do."

        scene makifirstinv26
        with dissolve

        maki "Buuuut I’m not about to start complaining right before we leave."
        maki "I have wreaked enough havoc on your relationship with {i}one{/i} [teenager] today, and I’ll be damned if I make you think less of Makoto by complaining or venting to you."
        s "I mean...if you really want to talk-"
        maki "You’ll hear me out and help me with my problems?"
        s "The first part, sure. But if you ever have to come to me for help, you’re likely so far off the deep end that literally {i}no one{/i} can help you anymore."
        maki "Blah blah blah self-deprecation and sad stuff. I want meat. Let’s go get...barbecue or something."
        s "Deal."

    scene black
    with dissolve
    play sound "knock.mp3"

    if bonus == False:
        s "Come, Maki. Fine dining awaits."

    a "WAIT! NO! SENSEI! YOU HAVEN’T TOLD ME I CAN LEAVE MY ROOM YET!"
    maki "Should you maybe let your [niece] out first? She might have to go to the bathroom at some point."
    s "She’ll be fine. She’s well behaved when she wants to be."

    play sound "dooropen.mp3"

    a "NO! DON’T LEAVE ME!"
    a "ESPECIALLY NOT WITH A MIYAMURA!!!!!!!!!!!"

    "Maki and I make our way over to some restaurant close to her shop so that, once we’re done, she can head back home to sub in for Makoto."
    "As it turns out, Maki was supposed to work tonight and Makoto was supposed to be helping Miku with something."
    "But, of course, whenever I ask anyone to do anything, they almost always drop their previous plans for me."
    "Just one of the perks of living in Kumon-mi, I guess."
    "Anyway, dinner is great and Maki winds up fronting the bill to pay for causing a disturbance at my house."
    "Was it a disturbance I both expected and created by inviting her there? Yes. But it’s not like I’m going to give away a free dinner in exchange for admitting that."
    "Instead, I’ll just shelve that idea alongside the thousands of others that I have pushed away from me in a never ending journey toward complacency."
    "The two of us split apart-"
    "And I go home to let my [niece] out of her cage."

    $ renpy.end_replay()
    $ maki_love += 1
    $ makiinvite1 = True
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makiinvite2:
...
```

## Code that triggers this event
File: \game\MakiEvents.rpy
Code:
```python
...
label makiinvite:
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump inviteover
    if makiinvite1 == False:
        jump makiinvite1
...
```