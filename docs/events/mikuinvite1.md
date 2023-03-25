# Breakaway (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Miku: Fair is Fair](./mikuinvite2.md)

## Event properties

* Id: mikuinvite1
* Group: Miku
* Triggered by label: mikuinvite

## Official wiki page

[Breakaway](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikuinvite1&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label mikuinvite1:
    play sound "phonebeep.wav"

    "I tap on Miku’s name in my phone and wait for her to answer."
    "Now that things have calmed down for the time being, I feel that it’s finally safe for me to invite her over so we continue progressing our...{i}relationship{/i} in a much more private manner."

    if kirinlust30 == False:
        "Hopefully in a way that leads to me receiving some form of satisfaction this time as all I’ve really done thus far is finger her until she cries."
    else:
        "Hopefully in a way that leads to me receiving some form of {i}fully-conscious{/i} satisfaction this time. Or, at the bare minimum, something more exciting than fingering her until she cries again."

    "And while that’s cool and all, it would be nice to shake things up in a manner more intimate than letting her dry hump me in bed next to her friend."
    "If she {i}wants{/i} to do that again, I’m not opposed. I should just probably get permission from Makoto first so I don’t have to go through another intervention."

    play sound "phonebeep.wav"
    play music "acoustic.mp3"

    mi "Hiyo, Sensei! What’cha up to?"
    s "Oh, you know. Just letting my imagination run wild. You?"
    mi "Just hangin’ with Makoto. Wanna say hi?"
    s "Yeah. Put her on for a second."
    mi "Roger that! Please hold. {i}Makoto! Your boyfriend wants to talk!{/i}"
    mak "{i}To me? Really? Why?{/i}"
    mi "{i}Maybe to confess his undying love? Come find out!{/i}"
    mak "Uhh...hello?"
    s "Hey. I was just wondering if I could have permission to bone your roommate."
    mak "{i}Here, Miku. You can have the phone back.{/i}"
    mi "{i}Huh? Already? That was quick.{/i}"
    mi "Sensei? Makoto looks friggin’ pissed. What did you say to her?"
    s "Just something that needed to be said. Don’t worry about it. Anyway, do you want to come over?"
    mi "Sure! When?"
    s "Now."
    mi "Like...{i}now{/i} now? "
    s "Does that work for you?"
    mi "I mean...I’ve gotta bring Makoto. We had plans and stuff."
    s "Gotcha. Can you put her on again?"
    mi "{i}Makoto! Round two!{/i}"
    mak "{i}Ugh! What now?{/i}"
    mak "Hello?"
    s "How do you feel about threesomes?"

    if makotofutabafuntimelustevent == False:
        mak "Aren’t you supposed to be nicer to me? Isn’t that a thing we talked about?"
        s "How do you feel about threesomes...{i}please?{/i}"
    else:
        mak "..."
        s "..."
        mak "Are you seriously asking me that right now? Have you not already done enough?"
        s "I just want to know more about you."
        mak "I think you know more than enough by now, thank you."
        s "It would sure be swell if you were into them as much as I am."

    mak "{i}Take it back. I can’t handle this today.{/i}"
    mi "Jeez, Sensei. You’re really strikin’ out this morning, aren’t ya?"
    s "It unfortunately appears that way. I’ll get her to come around, though."
    mi "Oh she’s come plenty of rounds if you know what I’m sayin’. "
    s "..."
    mi "Get it? Cause you give her orgasms and stuff. "
    s "Have I unlocked a new side of you?"
    mi "Probably! I’ll start gettin’ ready and the two of us’ll drop by your house in like...an hour? That work?"
    s "Sure. I hope Makoto is prepared. She seems a little confrontational today."
    mak "{i}Go to Hell! I can hear you!{/i}"
    s "See?"
    mi "Hahah! I’m sure she’ll be fine once we get there. But I’m gonna go shower and stuff, so...bye! See you soon!"

    scene black
    with dissolve2
    play sound "phonebeep.wav"

    "Miku hangs up the phone and..."
    "And I am left on my own to prepare for a threesome that will almost definitely not happen."
    "........."
    "......"
    "..."

    scene mikumakotoinv1
    with dissolve2

    mi "Heeeey. Haven’t been here in a hot minute. "
    mi "You still lettin’ girls sneak into your room to ride your junk while you’re asleep?"
    s "On occasion. Interesting choice of ice breaker, Miku."
    mi "Yeah...I ain’t really used to this whole “boy house” thing after my sexual awakening. Not gonna lie. Feels kinda lewd."
    mak "I hate you."
    s "So that’s a no to the threesome, huh?"
    mak "I hate you a lot."

    scene mikumakotoinv2
    with dissolve

    mi "What’s this about a threesome?"
    mak "Miku. Don’t."
    mi "I mean, I guess if I’m gonna have one, doin’ it with you would probably be best. I still don’t really know what I’m doin’, though. Ya might have to show me the ropes."

    scene mikumakotoinv3
    with dissolve

    mak "Look at what you’ve done to my sweet, innocent friend! She’s turning into my mom and I would literally die if I suddenly had two of them!"
    s "There goes my secret dream of her ending up with Haruka."
    s "Besides, I doubt it was {i}me{/i} who did this to her. This side of Miku has probably been buried deep down her entire life. Right, Miku?"
    mi "Hm? Oh, no. This is your fault. I have seen the light."
    mak "Sensei!"
    s "I did not mean for this to happen...but I am glad it did."
    mak "Yeah, until she starts running her mouth about it to everyone else! "
    mak "You know Miku’s attention span is...inadequate! It’s only a matter of time until she forgets this is something that’s meant to be kept {i}secret!{/i}"
    s "That’s fair. Ami could have been home and listening in on this entire conversation. You’re lucky she’s not."
    mi "If Ami was home, she woulda popped out of her room the second I talked about ridin’ your junk."

    scene mikumakotoinv4
    with dissolve

    mi "Also, you guys ain’t givin’ me enough credit! I ain’t gonna go around blabbin’ about this to everybody! I‘m too young to die! "
    mak "Just..."
    mak "Listen, I get that you’re excited to be, umm...{i}learning about your body-{/i}"

    scene mikumakotoinv5
    with dissolve

    mi "Oh, come on! Please don’t go into teacher mode in front of my friend-with-benefits. You’re gonna take all the benefits away."
    mak "...but, you need to be careful. This man is relentless. He will use you and cast you aside for someone else before you even know it."
    s "Hi. Still here."
    mi "Ain’t that a little hyper-critical? "
    mak "A little...{i}what?{/i}"

    scene mikumakotoinv6
    with dissolve

    mi "Uhh..."
    mi "Hippo...criminal?"
    mi "No...I’m pretty sure “critical” is in there somewhere and..."

    scene mikumakotoinv7
    with dissolve

    mi "A-hah! It’s hippie-critical, ain’t it?! Cause they were always sayin’ stuff that didn’t make much sense! See! I ain’t dumb!"
    mak "Is this really a creature you think you should be making sexual contact with?"
    s "I may be currently rethinking my decision. That much I will admit."

    scene mikumakotoinv8
    with dissolve

    mak "{i}Regardless,{/i} the reason I accompanied Miku here instead of letting her run off alone was precisely so something like that would {i}not{/i} happen."
    s "So, in other words, you were jealous."
    mak "That...may have played some role as well, I will admit. "
    mak "But the gist is that nothing like that will be happening today because we are {i}both{/i} here and singling out {i}one{/i} of us for...things...would be unfair."
    s "So if I wanted to single out {i}you{/i} instead..."

    scene mikumakotoinv9
    with dissolve

    mak "Obviously, Miku would never agree to such-"
    mi "I can wait out here. Feels like you need it more than me. Knock ‘im dead, Makoto. "
    mak "..."

    scene mikumakotoinv10
    with dissolve

    mak "I...suppose letting you get it out of your system may be of {i}some{/i} benefit to us."
    mi "I’m telling ya, Sensei. You’ve got a magic wiener. It’s the only explanation."
    s "Listen, we don’t {i}need{/i} to do anything like that today if it will exclude one of you. I called Miku because I wanted to invite her over. Making her wait out here would be flat out rude."
    mak "As if being rude was ever an actual concern of yours..."
    mi "If we ain’t gonna bump uglies, whaddya wanna do instead? Jump on Ami’s bed? Microwave stuff we ain’t supposed to microwave? Oooh, you got any games we could play?"
    s "I have the 1999 PC classic, Rollercoaster Tycoon."

    scene mikumakotoinv11
    with dissolve

    mi "I {i}love{/i} the 1999 PC classic, Rollercoaster Tycoon!"
    mak "Why are you guys saying it like that?"
    mi "Where’d you get a copy? That’s a piece of vintage memorabilia, ya know."
    s "Io found the time to drop it off between pretending to be a pharmacist and slinging you pills. "

    scene mikumakotoinv12
    with dissolve

    mak "Between {i}what?{/i}"
    mi "{i}Shh!{/i}"

    scene mikumakotoinv13
    with dissolve

    mak "Miku, what-"
    mi "Oh, Sensei! That’s a funny joke you just made! Anyway, time to go into your room and see what kind of stuff you’re hiding from us!"

    scene mikumakotoinv14
    with dissolve
    play sound "dooropen.mp3"

    mi "It’s this one, right? Hope you don’t mind me looking through your stuff!"
    mak "..."

    scene mikumakotoinv15
    with dissolve

    mak "I’m sorry, I think I misheard you. Something about...pills? And...Io pretending to be a pharmacist?"
    s "..."
    mak "Sensei, if you know something-"
    s "It was just a tasteless joke. It didn’t actually mean anything."
    mak "That just seems like such a random and uncalled for-"

    scene black
    with dissolve

    s "Come on. Let’s go make sure Miku doesn’t find my secret porn stash and unlock an even dirtier section of her brain."
    mak "...Yeah."
    mak "Okay..."

    "I wanted to tell Makoto."
    "And in hindsight, I probably should have."
    "But sometimes the “right” thing to do isn’t as easy as the other options. "
    "And sometimes, in order to save someone, you must sacrifice something else."
    "Not only would giving away Miku’s newest secret put our new {i}relationship{/i} in jeopardy, but it could potentially expose {i}me{/i} as well."
    "She’s not the only one who’s hiding something. And by all means, what I’m hiding is a lot more sinister."
    "Besides, it’s quite possible she doesn’t need saving in the first place."
    "It’s quite possible that whatever Io is doing will work for Miku...and that there’s no real risk involved at all."
    "But..."
    "If that were the case, Makoto would know."
    "And the fact that she doesn’t tells me Miku’s hiding it from her on purpose."

    scene mikumakotoinv16
    with dissolve2

    "At what point is it okay to begin distributing information that doesn’t belong to you? And how can you package it up to make it seem like you’re doing it with good intentions?"
    "In all actuality, it’s not about wanting to save anyone at all. It’s about wanting to maintain the status quo — where everything is peaceful and you can stick your dick inside of as many teenagers as you want."
    "The disruption of that pattern would shake my world to the core when my world was built upon that principle. "
    "It is not my place to put Miku in hers, and it is not Makoto’s place to raze both of them in an endless pursuit of what is right."
    "The three of us will stay like this so we may one day stay as something else."
    "Something close to what the real me wants."
    "Not whoever I’m becoming."

    mi "Sensei, why the heck do you even own Mario Kart if you’re so friggin’ bad at it?"
    s "I didn’t even realize I had this."
    mak "I fucking hate Waluigi. Get out of my way, you piece of shit. I hope the fishing line snaps the next time they reel you up. Asshole."

    scene mikumakotoinv17
    with dissolve

    mi "Need some help figurin’ out the controls? I’ve heard it can be pretty tough for people your age to just start playin’ games this late in life."
    s "I’m only 31, Miku. I’m still well below the median age in the country."
    mi "Yeah, but Japan’s got a bazillion old people. You’re still kinda prehistoric by our standards, ya know."
    mi "Even if half the class is apparently into that sort of thing."
    mak "It isn’t half the class. It’s the entire class. Everyone is fighting for Sensei’s affection- even the ones who deny it."

    scene mikumakotoinv18
    with dissolve

    mak "WALUIGI, YOU LANKY CUCK! I WILL FUCKING MURDER YOU!"
    s "I’ll be fine figuring out the controls. Just promise not to laugh at me when I come in last place."
    mi "I ain’t gonna laugh at ya, Sensei. It’s still just a game at the end of the day and havin’ fun will always be the most important thing."
    mak "FUCK! YOU!"
    mi "Even if we’ve got people like Makoto who have trouble turning the competitive part of their brain off."
    s "You’d think Kumon-mi High’s greatest athlete would be the {i}more{/i} competitive one, wouldn’t you?"

    scene mikumakotoinv19
    with dissolve

    mi "I ain’t that special. 'Specially now that soccer’s gone."
    mi "Swimming’s fun, I guess. Just doesn’t feel the same, though. Ain’t no crazy adrenaline rush that comes from a breakaway or anythin’ like that."
    s "It...could come back one day. Right?"
    mi "Soccer? Doubt it. We ain’t got the numbers for it and there ain’t any reason to form the team back up without anybody to play."
    mi "It’s fine, though. Just gives me more time to focus on other things. "
    s "Other things...like what?"
    mi "I wonder."

    scene mikumakotoinv20
    with dissolve

    mak "Hey. What do you think you’re doing? Public displays of affection are rude even {i}if{/i} you’re only displaying said affection in front of your best friend."
    mi "Guess I’m rude, then. Cause I ain’t got any intention of movin’ any time soon."
    mi "You know he’s got a second shoulder open, don’t ya? Why don’t you rest your head a little too? "
    mi "Ain’t a threesome like Sensei wanted but it still lets all of us be close together. "

    scene mikumakotoinv21
    with dissolve

    mak "You’re going to lose the race with that sort of mindset, Miku."
    mi "You sure it ain’t you who’s gonna run out of gas first? Always keepin’ the pedal to the metal and whatnot. Just stay steady and keep your eyes on the prize, Makoto."
    mak "Nice try, but there is no gas in Mario Kart."
    mi "Who says I’m still talkin’ about Mario Kart?"
    s "What are those boxes? Do they slow you down if you hit them?"

    scene mikumakotoinv22
    with dissolve

    mi "They’ve got power-ups and stuff inside. You smash ‘em and use whatever you get to mess with the other people on the track. "
    s "I see..."
    mi "Do ya? Cause it seems to me like you’re just starin’ at Makoto now."
    s "That’s a new dress, isn’t it?"
    mak "Took you long enough."
    s "It looks great. You’re beautiful."

    scene mikumakotoinv23
    with dissolve

    mak "Wha- huh?! Me?! You...really think so?! "
    mak "I got a little jealous that Miku had one and I didn’t so-"
    s "That was Makoto I just hit, wasn’t it?"
    mi "Yuuuup. Great strategy, Sensei."
    mi "Takin’ somebody out IRL so you can hit ‘em in-game is a real power move."

    scene mikumakotoinv24
    with dissolve

    mak "You...fucking asshole! You distracted me! I’ll get you back for this!"
    mi "Not if I have anything to do with it."

    scene mikumakotoinv25
    with dissolve

    mak "Wha- you too?! {i}Both{/i} of you are ganging up on me now?! What did I do to deserve this?!"
    mi "Drive, Sensei! Drive! Show us how much all those years of wisdom are really worth!"
    s "I think I just fell off."
    mi "Baby steps, Sensei. Baby steps."

    scene black
    with dissolve2

    "The three of us sit in my room playing the same game for the next two hours."
    "Makoto eventually falls asleep on my arm, prompting Miku to take it upon herself to talk more about how “cute” the two of us look together."
    "It’s strange to me how she can still say something like that with a smile on her face."
    "I find it cute how genuine the love she has for her best friend is. And while something like that {i}should{/i} feel ideal for me as Miku doesn’t intend to pose any sort of threat..."
    "All I can think of is that I really wish she would."
    "And that she’d look better in my eyes if she would just pull me a little closer to her."

    $ renpy.end_replay()
    $ mikuinvite1 = True
    $ miku_love += 1
    $ makoto_love += 1
    stop music fadeout 6.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label mikuinvite2:
...
```

## Code that triggers this event

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label mikuinvite:
    if mikuinvite1 == False:
        jump mikuinvite1
...
```