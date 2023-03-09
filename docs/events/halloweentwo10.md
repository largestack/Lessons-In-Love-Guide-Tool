# Escape Rope
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo10&go=Go)


Part of event chain [In Circles](./halloweentwo9.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloweentwo10
* Group: Main
* Triggered by label: halloweentwo9

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label halloweentwo10:
    stop music
    play sound "static.mp3"
    scene beforewefall1 with flash
    scene beforewefall2 with flash
    scene beforewefall3 with flash
    scene beforewefall4 with flash
    scene beforewefall5 with flash
    scene mollydrunkagain1 with flash
    stop sound
    play music "justbehappy.mp3"

    mo "{i}*Hic*{/i}"
    mo "Whadr’ye lookin’ at, Sensei?"
    s "Hey, Molly. I just figured I’d come keep you company since you’re drunk and alone and no one seems to be paying any attention to you."
    mo "Story of my life."
    s "Where’s Tsuneyo?"
    mo "‘Ell if I know. Probably...bein’ a cat?"
    mo "I ever tell you how I feel about cats?"
    s "I don’t think that topic has ever come up before, no."
    s "How much have you had to drink?"

    scene mollydrunkagain2
    with dissolve

    mo "Yes."
    s "Well, that more or less answers that."
    mo "Ye want’some, Sensei? Can *hic* finish mine if ye pay me for it."
    s "Why would I pay you for a half empty beer in a place where I can very likely get as many of them as I want for free?"
    mo "‘Alf empty?...Or 'alf {i}full?{/i}"
    s "Do I look like an optimist to you? Of course it’s half empty."

    scene mollydrunkagain3
    with dissolve

    mo "Ha! Dass...where’yer wrong! I jusssssss..."
    mo "Jusss opened this one, idiot."

    "So, it appears that I may have shown up a bit too late to prevent Molly from slipping into an alcohol induced coma."
    "Is she still standing right now? Sure. But...there’s no way that’s going to last much longer."
    "I’m glad she at least decided to drink alone instead of taking Kirin up on her offer, though."
    "It’s one thing to get blackout drunk, but a completely different thing to get blackout drunk around someone who would likely attempt to [molest] you."

    s "Where did you even get that? I thought everyone was actively trying to prevent a repeat of last year."

    scene mollydrunkagain4
    with dissolve

    mo "Obvenously from the *hic* alcohol room."
    s "{i}Obviously.{/i} But that doesn’t explain-"
    mo "Sensei. Nooooobody’s tryin’ to stop me from doin’ anything."
    s "Futaba was."

    scene mollydrunkagain5
    with dissolve

    mo "She here now? Or is she a...*hic* {i}traitor{/i} who left me all alone to go talk to my arch nemesis?"
    s "Rin is your nemesis now?"

    scene mollydrunkagain6
    with dissolve

    mo "Juss {i}look{/i} at her! Holdin’ hands with a {i}girl{/i}. "

    scene mollydrunkagain7
    with dissolve

    mo "LESBIAN!!!"
    mo "GIRL...LIKER!!!"

    scene mollydrunkagain8
    with dissolve

    mo "She’s so *hic* hot..."

    "Well, on the bright side, this time she’s yelling about lesbians and not her father."
    "That is a step in the right direction."
    "Or at least...{i}a{/i} direction."
    "I don’t think either one of those things is a particularly {i}good{/i} thing to yell about while inebriated beyond belief in a room full of your peers."
    "But, again, at least she’s standing."

    s "Molly, I-"

    play sound "static.mp3"
    scene mollydrunkagain9
    with flash
    stop sound

    s "I..."
    mo "*Hic* Whaaatsyer...problem?"
    mo "Why ya just lookin’ at me with those...eyes?"
    s "I..."
    s "{s}Can you hear me?{/s} I don’t really...know."
    mo "Ay! If you’ve got sometin’ ta say, ye best say it before I start yellin’!"
    s "{s}Everything is better where it’s dark.{/s} You’re already yelling, though."
    s "{s}GO! RUN!{/s} I just wanted to know what-"

    scene frog

    "{b}/////////////////////////SUCCESSFULLY CONNECTED TO “HALLOWEEN SPECIAL”{/b}"
    "{b}/////////////////////////CHECKING FOR FLAG “mollyhalloween2win”{/b}"
    "{b}/////////////////////////…{/b}"
    "{b}/////////////////////////…{/b}"
    "{b}/////////////////////////…{/b}"

    if mollyhalloween2win == True:
        "{b}/////////////////////////FLAG LOCATED{/b}"
        "{b}/////////////////////////ACCESSING ADDITIONAL PROFILE INFORMATION{/b}"
        "{b}/////////////////////////…{/b}"
        "{b}/////////////////////////…{/b}"
        "{b}/////////////////////////…{/b}"

        if bonus == True:
            scene mollyspecialstats
        else:
            scene white

        "{b}/////////////////////////ACCESSED{/b}"
        "{b}/////////////////////////PLEASE TAKE YOUR TIME IN FAMILIARIZING YOURSELF WITH THIS INFORMATION{/b}"
        "{b}/////////////////////////MOLLY MACCORMACK IS A [[MANDATORY] ROMANCEABLE CHARACTER{/b}"
        "{b}/////////////////////////PLEASE CONTINUE TO RAISE YOUR AFFECTION WITH MOLLY MACCORMACK{/b}"
        "{b}/////////////////////////PLEASE CONTINUE TO SPEND TIME WITH MOLLY MACCORMACK{/b}"

    else:
        "{b}/////////////////////////FLAG NOT LOCATED{/b}"


    scene black

    "{b}/////////////////////////CONNECTION TERMINATED{/b}"

    scene mollydrunkagain10

    mo "Really, though! Who the *hic* heck do they think they are?!"
    mo "What is this? A {i}love{/i} hotel? Have some tact! "
    s "They’re just...holding hands."

    scene mollydrunkagain11
    with dissolve

    mo "I know! Disgusting, right?! In a place like *hic* this. The nerve!"
    s "To be fair, the two of them are dating now and, if they want to hold hands in public, it’s well within their right to do so."

    scene mollydrunkagain12
    with dissolve

    mo "Sounds to me like we got...*hic*...an imposter in our midst."
    s "...What?"
    mo "You got ta nerve...ta come over ta me...and {i}not{/i} be on my side? Whaddya tink tis is? AMOGUS?!"
    s "I...have no idea what you’re talking about."

    scene mollydrunkagain13
    with dissolve

    mo "Cause ya never try ta learn! All ya do is sit in your fancy office chair, eat hot chip, and lie!"
    s "How have you gotten drunker by just...standing there and not drinking?"
    mo "I had a whole other *hic* beer while you were starin’ off inta space!"
    mo "Ya see anytin’ out there, Sensei?! ‘Dya find Haruka’s husband?!"
    s "When was I staring off into space?"

    scene mollydrunkagain14
    with dissolve

    mo "Unbelievable! Kids these days! Always on their phones and not even payin’ attention to ta world around ‘em."
    s "You are...not one to speak."

    scene mollydrunkagain15
    with dissolve

    mo "And now yer takin’ me freedom of speech?! "
    mo "Somebody ping the mods!"
    s "Okay, you know what? I’m going to be a responsible adult and confiscate that beer from-"

    play sound "static.mp3"
    scene mollydrunkagain16 with flash
    stop sound

    s "Okay, you know what? Let’s distract you from drinking anymore by talking more about Rin and Otoha."
    mo "*Hic*"
    mo "I shoulda never came to this party."
    mo "Nobody wants ta talk to me when they’ve gotta burn their feet on coals ta do it."
    mo "S’one ting ta have Futaba ditch me for ‘er best friend, but th’rest o’ta manga club’s too’fraid ta’proach me while we’ve got Little Miss PDA and her super hot girlfriend makin’ hand sex at the table."
    s "Please don’t call holding hands “hand sex.” It makes me feel strange."

    scene mollydrunkagain15
    with dissolve

    mo "If it makes {i}you{/i} feel strange, imagine how I feel!"
    mo "S’like when ya die to th’frickin’ dance on Council of Blood and have to sit there watchin’ everyone else boogie down while ya ask yer death knight for a b-res!"
    s "…"
    mo "S’like pingin’ for your jungler to gank mid because ‘yer getting ‘yer arse handed to ya, but he’s too busy campin’ top because that’s where ‘is friend is laning!"
    s "…"
    mo "S’like when Genji asks you to nano boost ‘im but then dives in and get’s ‘is arse flash-fanned by McCree!"

    scene mollydrunkagain17
    with dissolve

    mo "Oh, sorry- Cole frickin’ Cassidy’s ‘is name now because Blizzard’s conflict resolution team’s run by a’bunch’a monkeys."

    "Molly is so drunk at this point that she has begun making up words and people and...I really have no idea how to handle it."

    s "I’m sure it doesn’t feel great being you right now, but..."

    scene mollydrunkagain18
    with dissolve

    mo "But what, Sir? What can ya possibly say right now tat’ll make me feel any better?"
    s "You know, I probably should have thought of that before speaking because I’ve honestly got nothing."
    s "But hey. {i}I’m{/i} here. And I’ve been diffusing problems left and right since I showed up."

    "This obviously isn’t true since I’ve been tossed into four or five of them at this point and really haven’t resolved any. "
    "But Molly doesn’t need to know that."
    "She just needs someone to lean on."
    "Literally, because she is going to fall over any minute now."

    scene mollydrunkagain19
    with dissolve

    mo "Hah...yeah...you’re here."
    mo "But so am I. And that’s exactly the problem, Sensei."
    s "Go back to calling me Sir, please. Hearing you say “Sensei” repeatedly is somehow the weirdest part of all of this to me."

    scene mollydrunkagain20
    with dissolve

    mo "I’ll try, Sir. But I can barely feel me face right now."

    scene mollydrunkagain21
    with dissolve

    mo "Like...{i}look!{/i} "
    mo "Is she {i}tryin’{/i} to make me jealous or d’she literally forget I exist? Which one is it, Sir?!"
    s "...Neither?"
    s "She’s just enjoying herself with her new girlfriend."

    scene mollydrunkagain22
    with dissolve

    mo "{i}I{/i} wanna be the new girlfriend..."
    s "You’re not even succeeding at being Molly right now."
    s "You drank yourself into a stupor to avoid having to deal with your problems because you can’t play video games right now and are handling the consequences of that decision by just...complaining."

    scene mollydrunkagain23
    with dissolve

    mo "Sounds pretty familiar to me, Sir."
    mo "Nothin’ says the Emerald Guardian like hidin’ your problems behind other stuff while *hic* shummle...taneously complainin’ about ‘em."
    s "Simultaneously."

    scene mollydrunkagain24
    with dissolve

    mo "You’re not smarter than me!"
    s "Maybe not, but I {i}am{/i} sober- which allows me to do this thing where I say words correctly."
    mo "You’ve been on my case ta whole night! Why aren’t ya makin’ me feel better?!"
    s "What do you want me to do? Go force Rin to talk to you?"
    s "The last time we tried that, she not only made you cry, but made {i}me{/i} sit there holding her arm closed so she didn’t bleed out."

    scene mollydrunkagain20
    with dissolve

    mo "Bet her new {i}girlfriend{/i} doesn’t even know about that yet."
    mo "F’I know Rin, she’s just gonna hide it and hide it and hide it and pretend everyting’s okay ‘til she gets caught."
    mo "S’what she always does. I know ‘er better t’en I know meself."
    s "That checks out. Because pretending everything is okay until you get caught is exactly what you did concerning your feelings for her, isn’t it?"

    scene mollydrunkagain25
    with dissolve
    stop music fadeout 45.0

    mo "Ah-"
    s "Oh."
    s "Please don’t cry."

    scene mollydrunkagain26
    with dissolve

    mo "That was so mean!"
    s "It wasn’t meant to be mean. I’m just pointing out how you and Rin aren’t that different-"
    mo "I know that, Sir! Why do you think I like her so much?!"
    s "Molly, I know you’re drunk, but someone is going to hear you if you keep yelling like that."
    mo "Let ‘em! S’not like t’ey care anyway!"
    s "Of course they do. They...probably just don’t want to spend a night that is supposed to be fun consoling a drunken girl who’s still pining after a friend in a relationship."

    scene mollydrunkagain25
    with dissolve

    mo "You {i}are{/i} on her side..."
    s "Molly, there are no sides. You’re both [teenager]s with little to no impulse control who are going to get hurt and make stupid decisions because that is the part of life you’re in right now."
    s "I’m just trying to avoid you making things worse than they already are, which, judging by the condition you’re in and the literal tears in your eyes, is pretty bad."

    scene mollydrunkagain26
    with dissolve

    mo "L-Leave me alone!"
    s "Molly, come on."
    mo "I’m...going home!"
    s "You can barely stand up."
    mo "I’m fine!"

    scene mollydrunkagain27
    with dissolve

    mo "You! Butler! Hold my potion!"
    s "Molly, that’s-"

    scene mollydrunkagain28
    with dissolve

    s "Not a butler..."
    mo "Don’t follow me!"
    s "Do you have any idea how many hallways this place has? No one will ever see you again."
    mo "Well maybe things are *hic* better that way!"
    s "Molly, come-"
    mo "Goodbye forever!"
    s "…"
    s "Hah..."

    "Molly opens up some door near the back of the room and disappears inside. "
    "Not only am I thankful that she didn’t elect to turn into the hall of many halls (The cool name I’ve decided to give to Ayane’s maze thing), but I’m glad she’s going to be alone for a while."
    "Granted, she’s been alone ever since Futaba left her side- but still."
    "She’s safer locked away in some room than out in the open, screaming about how mean I am and how her friend should be dating her instead."

    s "…"

    "But, at the same time, thousands of people die every year by choking on their vomit after passing out drunk."
    "Probably."
    "That’s not a real statistic, but it sounds believable enough and I know for a fact that it does happen {i}sometimes{/i}."

    s "…"

    "Damn it. Where’s Tsuneyo?"

    u "Go to her."

    scene mollydrunkagain29
    with dissolve

    s "Uta? "

    scene mollydrunkagain30
    with dissolve
    play music "lastdailysong.mp3"

    u "N...Nyaa~"
    s "How much of that did you hear?"

    scene mollydrunkagain29
    with dissolve

    u "Enough to know that you hurt Molly’s feelings."
    s "Thankfully, she won’t remember that I hurt her feelings because of how drunk she is."

    scene mollydrunkagain31
    with dissolve

    u "You should still go to her, Sensei."
    u "Even if it wasn’t on purpose, you made her cry. So now it’s your job to make her feel better."
    s "What are you even doing over here? I thought you were playing a game with Nodoka and company."
    u "We were."
    u "Well...we {i}are{/i}."
    u "Which is..."

    scene mollydrunkagain32
    with dissolve

    u "Nyaa..."
    s "…"
    s "I don’t speak cat."
    u "Just...go check on her. "
    u "I’ll make sure no one gets in the way."
    u "You...definitely attracted some attention with Molly’s yelling...and...my group was kind of already looking over here, so..."
    s "…"
    s "Do you want to come with me?"

    scene mollydrunkagain33
    with dissolve

    u "Nyaa?"
    s "...Is that a yes or?"
    u "Why would I come?"
    s "Just had a feeling you might want to."

    scene mollydrunkagain34
    with dissolve

    u "You should go alone."
    u "Wipe that frown off of Molly’s face! And make sure she drinks some water while you’re at it!"
    s "…"
    s "Hah...fine."
    s "But the second she starts accusing me of taking sides again, I’m coming back out here and hanging out with you instead."

    scene mollydrunkagain35
    with dissolve

    u "Nyahaha! You may think that, but the truth is that I’m far too cool for you, Sensei!"
    u "You’ll be forced to sit with your [niece] and her friends instead!"
    s "But things got weird there last time..."
    u "Don’t wanna hear it, mister! Your time with Uta-nyan has expired!"
    u "If you’d like to proceed with the conversation, please give her six billion yen."
    s "Why the hell have your rates gone up so much?"
    u "Hmmm...the whiskers, probably?"

    scene mollydrunkagain36
    with dissolve

    u "Now go! Go go go go go! Make the Irish girl smile and you'll get free flavor beams for the next month!"

    scene black
    with dissolve

    s "Say no more. I’m going."
    u "Heheh..."
    u "See you later, Sensei..."

    "I make my way across the hall and look back to find Uta explaining to a few of the other girls what’s going on."
    "Well, it’s probably something closer to {i}attempting{/i} to explain what is going on since I, a person who was there for the entire exchange, do not fully understand."
    "So, let’s recap what I {i}do{/i} know."

    play sound "static.mp3"
    stop music
    scene recap with flash
    stop sound

    "Molly is drunk."
    "Molly is mad at me."
    "Molly is mad at virtually everything."
    "Molly is also sad."

    if bonus == True:
        "Her costume is very tight."
        "I want to take her costume off."
        "Molly is crying. "
        "I want to take her costume off."
        "No one is coming to the room."
        "Molly is drunk."
        "I want to take her costume off."
        "I am walking."
        "I am using my feet to walk toward Molly."
        "Molly is drunk."
        "I want to take her costume off."
        "Molly won’t remember anything."
        "Molly is sad."
        "Molly wants to be loved."
        "Molly wants to be touched."
        "I want to touch Molly."
        "I want to take her costume off."
        "I want to take her costume off."
        "I want to fuck her."
        "I shouldn’t fuck her."
        "Molly is drunk."
        "I want to fuck Molly."
        "Molly is mad."
        "Molly is mad at me."
        "I want to take her costume off."
        "No one is coming to the room."
        "I am here."
        "I have found Molly."
        "I want to make her feel better."
        "I came here to make Molly feel better."
        "Molly is crying."
        "Molly is drunk."
        "I am a good person."
        "I am a good person."
        "I am."
    else:
        "That's it."

    $ renpy.end_replay()
    $ halloweentwo10 = True
    $ molly_love += 1

    scene black

    if bonus == True:
        "{s}{i}Molly’s affection has increased to [molly_love]!{/s} I want to take her costume off.{/i}"
    else:
        "{s}{i}Molly’s affection has increased to [molly_love]!{/s} This event has been ruined!{/i}"

    "………"
    "……"
    "…"

    jump halloweentwo11

label halloweentwo11:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
c "You can’t just kiss someone who doesn’t want you to kiss them. That’s assault."
    no "Oh? Are you implying that Sensei wouldn’t want to kiss our adorable little Uta-nyan?"
    c "Yeah. I am. "
    c "No offense to Uta, of course. But Sensei is off limits for this and you need to think of something else."
    mak "Agreed. This is entirely unacceptable."

    scene truthordarehalloween38
    with fade

    mi "Well, like...what if it’s just on the cheek or somethin’?"
    mi "Everybody in the room knows we’re playin’ a game, so they’ll all just think it’s part of that."
    mak "Miku! You can’t seriously be siding with Nodoka on this, can you?"
    mi "I’m not sidin’ with anybody...I just don’t think it’s a big deal if it’s a little peck on the cheek."
    mi "Would get everybody to stop yellin’ too."

    scene truthordarehalloween39
    with dissolve

    mak "Oh...I’m sorry..."
    mak "I wasn’t even thinking about the noise."
    mi "Nah. I’m okay. "
    mi "I just...don’t want any fights breakin’ out over somethin’ that...doesn’t really change anything..."

    scene truthordarehalloween40
    with fade

    u "Is it...too late to pick a truth instead?"
    no "Hmm...How about this one?"
    no "Do you {i}want{/i} to kiss Sensei?"
    mi "I feel like answerin’ that is even more dangerous than the cheek thing..."
    to "The poor kitty."
    u "I...uhh..."
    no "You can always back out of the game if you’d like, Uta-nyan. "
    no "It {i}is{/i} just a game after all."
    no "Everything that comes out of the circle is all in good fun."
    no "Besides, if you {i}do{/i} want to kiss our teacher, now would be a perfect opportunity."
    u "But...we’re not supposed to be adding him to the game! We said we wouldn’t..."
    c "Nodoka, seriously. Just think up another dare."
    mak "I agree with Chika."
    no "It appears it may be democracy’s time to shine, then."

    scene truthordarehalloween41
    with fade

    no "Makoto and Chika have vocalized their agreeance with the core rule this game was built upon."
    no "However, new circumstances have arisen and now Miku and I think a minor change would be both acceptable and beneficial to the game’s enjoyment for all."
    no "My initial dare is now formally amended to a simple kiss on the cheek, just to clarify."
    no "The only members who have yet to vote are Uta, who is exempt due to a conflict of interest-"

    scene truthordarehalloween42
    with dissolve

    no "And Touka..."
    to "I am...the deciding factor in this vote?"
    to "But that’s so much pressure..."
    no "Is it?"
    no "All you need to really do is tell the circle whether or not you think a kiss on the cheek is romantic or not."
    no "Do you see a problem with one or more members, if dared, kissing each other on the cheek?"
    to "I..."

    scene truthordarehalloween43
    with dissolve

    to "Well...in my family...things like that aren’t called romantic..."
    to "My father kisses both my sister and me on the cheek quite frequently. And I do the same with my mother and...even other extended members of the family."
    to "I don’t believe there to be any romantic significance to such a thing and..."
    to "I think I’d have to side with...Miku and Nodoka..."
    c "Seriously?"
    c "I mean...yeah, it {i}is{/i} just the cheek. But you don’t think it’s weird to just do that in the middle of a party?"

    scene truthordarehalloween44
    with dissolve

    to "I’m afraid that wasn’t the question I was asked..."
    mak "Then it’s not too late to revise the poll to-"
    no "No objections were made to the poll when presented and time has already been yielded for both parties on the opposing side."
    no "As such, Uta-nyan must now either abide by the amended rules of the game and kiss Sensei or...stop playing."
    mak "Hah..."
    mak "Uta, what will it be?"
    u "I...umm..."

    scene truthordarehalloween45
    with fade

    u "I..."
    mi "Truth or dare sure can get serious, huh?"
    mi "You feelin’ okay, Uta? It’s just a little kiss on the cheek. It's not like-"

    scene truthordarehalloween46
    with dissolve

    mi "You're..."
    mi "Doin'...anything else..."
    u "…"
    u "I..."

    $ renpy.end_replay()
    $ halloweentwo9 = True

    jump halloweentwo10
...
```