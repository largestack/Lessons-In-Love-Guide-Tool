# A Way's Away
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo15&go=Go)


Part of event chain [Chashu](./christmastwo14.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo15
* Group: Main
* Triggered by label: christmastwo14

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo15:
    scene secretsantatime1
    with dissolve2
    play music "christmasyay.mp3"

    t "Life can be all sorts of things. Happy. Sad. All of the emotions that occur in the middle-"
    t "But noodles will always be noodles."
    t "And once you lose sight of that, you have lost at both life and at Christmas."
    t "The moral of the story is to cherish your friends, because you never know when one of them might become a slice of pork or a cracked bowl."
    t "The end."
    mo "..."
    to "..."
    u "I forget. What was it we were talkin’ about again?"
    to "I believe it was the topic of tradition. Though, I’m struggling to see how any of what was just said pertains to that."
    mo "You should really consider putting more points into charisma next time, Kendo Princess. None of us understood any of that speech."

    scene secretsantatime2
    with dissolve

    t "I apologize for derailing this conversation. I simply wanted to say that I would enjoy doing this again with all of you in the future."
    t "But, on the bright side, the mood seems to be a bit lighter now. "

    scene secretsantatime3
    with dissolve

    u "Hey, yeah! It kinda does! Look at us, movin’ past all the bad stuff and gettin’ back to what {i}really{/i} brings all of us here today! Christmas!"
    u "It’s gettin’ to be around time for Secret Santa, which I’m really friggin’ pumped about since I wasn’t able to do it with you guys last year."
    to "Aren’t we still missing a few people, though? "

    scene secretsantatime4
    with dissolve

    u "Are we? I saw Yumi walk back in a couple of minutes ago, so I kinda figured that was everybody."
    mo "It looks like...several people are missing, actually. But we have more than half, so..."
    t "Are you still worried about whether or not the Herald of the Adolescents will enjoy your gift?"

    scene secretsantatime5
    with dissolve

    mo "I’m more worried about whether or not he’ll ever like {i}me{/i} again. I rolled a nat-one when I tried talking to him the other night and I might have somehow made things even worse."

    scene secretsantatime6
    with dissolve

    to "Well, {i}I{/i} am certainly excited for this gift exchange. "
    to "It will be my first time receiving something from a classmate, so I’m sure that whatever gift I am given will find its place in a loving home."
    u "You haven’t gotten yours yet, Touka? I saw you carryin’ around a stuffed bear thingy before and kinda assumed that was just your present."
    to "Oh, no. Not at all. That was-"

    scene secretsantatime7
    with hpunch

    to "Wait! Where did the bear go?! It was on the counter behind Tsuneyo just a moment ago!"
    t "It is likely gone forever."
    mo "Fission mailed."
    to "No, no, no! That’s not good! It was my duty to look after it! We need to find it!"
    u "Ugh. Fine. But I’m only givin’ it five minutes before I pull the plug and start Secret Santa without it."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene secretsantatime8
    with dissolve2

    y "..."
    sa "..."
    y "Uhh...Sana?..."

    scene secretsantatime9
    with dissolve

    sa "Hm? "

    scene secretsantatime10
    with hpunch

    sa "Ah! Wha...what did I do? Why are you-"
    y "I ain’t here to pick on you. Just heard some shit about my mom workin’ at your bar or whatever and I...wanted to see if it was true, I guess."

    scene secretsantatime11
    with dissolve

    sa "So, you’re...not here to...pick on me?..."
    y "Have I ever picked on you before? Why the fuck would I start now?"
    sa "You haven’t, but...I’m easy to miss, so..."
    y "Listen, I’m not plannin’ on bothering you or whatever. I just wanna know if the shit I’ve been hearin’ is true."
    y "You probably know her as Yuki. But I’ve known her since I was a kid and- "

    scene secretsantatime12
    with dissolve

    y "Well...{i}obviously{/i} I’ve known her since I was a kid since she’s my fucking mom."
    y "But, like...she ain’t ever worked a real job in her whole fuckin’ life. And I can’t figure out why the fuck she’d...start now instead of just doin’ what she’s always done."
    sa "I’ve...heard from her that...you two aren’t on very good terms..."

    scene secretsantatime13
    with dissolve

    y "It’s true, then? She’s really working there? She like a...bodyguard or something?"
    sa "We aren’t...busy enough to hire any bodyguards..."
    sa "She’s just a...normal bartender..."
    sa "She hasn’t...been there long, but...she’s doing her best..."
    y "That’s..."
    y "I just don’t really get {i}why.{/i}"
    y "But I don’t really expect you to know either. "
    sa "I..."

    scene secretsantatime14
    with dissolve

    y "Uhh...anyway! That was pretty much it. "
    y "I’m gonna...probably go back to the other room to chill with Chika for a bit, so as long as you ain’t got anything you need to ask me, I’ll-"

    scene secretsantatime15
    with dissolve

    u "Attention, attention! All ladies and Sensei! "

    scene secretsantatime16
    with fade

    u "I know we’re still missing a few people, but the time has come for us to give each other stuff so we don’t miss out on the fireworks later!"
    u "If the person you’re supposed to give a present to isn’t here, by no means give it to Touka! She has proven she can not be trusted with looking after presents!"
    to "Uta, please! I’m sure it will turn up somewhere! I just have to-"
    u "No excuses, bear killer! "
    u "Everyone, go! Go, go, go! "

    scene black
    with dissolve2

    "One by one, all of the girls begin making their way over to the table that they’d left all of their gifts on shortly after entering the party. "
    "Thankfully, I manage to avoid getting caught up in the congestion as I reclaimed Miku’s present from Touka (Unbeknownst to her) just a few minutes ago."
    "Feeling ever so slightly bad about watching her frantically search the room for it, I let her know that it’s not lost after all and that she’s free to live at least a temporarily guilt free life."
    "Touka breathes a sigh of relief and, without saying anything else, walks directly past me and over to an...extremely large gift wrapped object that I somehow did not notice at all tonight."
    "Knowing that it’s time for me to actually be a decent person and give someone something, I glance over at Rin one final time to make sure she’s doing okay now."
    "Futaba was able to calm her down for the most part. And I-"
    "Well, I was there."
    "But that’s more than I can say most of the time."
    "Now, I should probably get this bear over to Miku before I get sidetracked and-"

    mo "Umm...Sir!"

    "Nevermind, I guess."

    scene secretsantatime17
    with dissolve2

    mo "I...umm..."
    mo "I know things are...not the best between us right now and...that you still haven’t...sorted out your feelings, but..."
    mo "But I got this for you..."
    s "You mean to tell me that the hypothetical scenario you threw out the other night about buying me a present was actually {i}true?{/i}"
    mo "S...Surprise~"

    scene secretsantatime18
    with dissolve

    s "Thank you, Molly. I appreciate it."
    s "This seems a little large to be a gift card, though."
    mo "It’s actually...something I made. The mats for it did technically run a bit under the spending limit, but it took a little while to put together, so...I hope that makes up for the discrepancy in spending..."
    s "Can I open it now?"

    scene secretsantatime19
    with dissolve

    mo "Now?! Why?!"
    s "Because it’s...a present for me?..."
    mo "Yes! I mean no! Don’t open it!"

    scene secretsantatime20
    with dissolve

    mo "At the very least, Sir...please wait until you make it back home..."
    mo "It would be...a bit embarrassing seeing you try it on now..."
    s "Please tell me you did not make me some sort of cosplay outfit."

    scene secretsantatime21
    with dissolve

    mo "Of course not. Though, it is certainly something in the...apparel family."
    mo "I just figured that since summer is right around the corner, this might come in handy."
    s "So you don’t find it strange that summer is right around the corner from Christmas?"

    scene secretsantatime22
    with dissolve

    mo "That’s..."
    mo "Wait..."
    mo "No..."
    mo "Summer is still quite a way’s away if today is Christmas..."
    mo "So...{i}what?{/i} Why did I feel the need to make you-"
    no "*Hic*"

    scene secretsantatime23
    with dissolve

    no "..."
    mo "..."
    s "You doing okay, Nodoka?"
    no "I...{i}hic{/i}...held the glass for too long..."
    mo "Is this what {i}normal{/i} people look like when they’re drunk? "
    mo "She’s incredibly less annoying than I heard I was."
    s "I say we don’t talk about how you are when you’re drunk."

    scene secretsantatime24
    with dissolve

    mo "Yes...right."
    mo "I’m sorry, Sir..."
    no "You ever {i}hic{/i} take a second to think about how fucking {i}wild{/i} tardigrades are? "
    no "They can live in fucking {i}lava.{/i} Can {i}you{/i} live in lava, Sensei?"
    s "Nodoka, when did this even happen to you? You were fine just a few minutes ago."

    if bonus == True:
        no "I don’t remember. Some time after Otoha decided she didn’t want her parents knowing she fucks girls."
    else:
        no "I don’t remember. Some time after Otoha decided she didn’t want her parents knowing she hugs girls."

    scene secretsantatime25
    with dissolve

    mo "Uhh...okay. I’m going to walk away now. But...thank you for accepting my present, Sir. I...hope you enjoy it."
    mo "You can...let me know if...you ever decide to text me back."
    no "Nooo, don’t go~ "

    if bonus == True:
        no "I didn’t mean that Otoha is {i}actually{/i} fucking Rin. She just probably {i}thinks{/i} about fucking Rin. "
        no "But we {i}all{/i} think about fucking Rin. She’s Rin. She’s fuckable."
    else:
        no "I didn’t mean that Otoha is {i}actually{/i} hugging Rin. She just probably {i}thinks{/i} about hugging Rin. "
        no "But we {i}all{/i} think about hugging Rin. She’s Rin. She’s huggable."

    f "Nodoka...we are literally right here..."

    scene secretsantatime26
    with dissolve

    no "Heeeeeey~ "
    f "Don’t “heeeeeey” me, please. Go get a bottle of water and lay down."
    no "Can I lay on your lap? "
    f "No. I’m helping Rin right now. "

    if bonus == True:
        no "Rin? You mean the fuckable one?"
    else:
        no "Rin? You mean the huggable one?"

    r "Is it weird that this is actually making me feel a little bit better right now?"
    mo "Merry Christmas, Sir. I’m walking away now."
    s "Yeah, so am I. As much as I like this conversation, this is probably the last place I should be getting involved in it."

    scene black
    with dissolve2

    "Besides, I have other things to do right now and-"

    ima "Senpai! "

    "{i}Hah...{/i}"

    scene secretsantatime27
    with dissolve2

    ima "Nobody got me a Christmas present! This is the single worst party I’ve ever crashed! And I’ve crashed at least {i}three{/i} parties! Three!"
    s "I’m going to go out on a limb here and assume that’s because you’ve been a part of the class for one day. "

    scene secretsantatime28
    with dissolve

    ima "Sure, yeah...but that doesn’t mean it doesn’t still hurt."
    ima "Will {i}you{/i} buy me a present, Senpai? Pleeeeeease?"
    s "No. Go away. "

    scene secretsantatime29
    with dissolve

    ima "Nothing?! Not even an innuendo for me to feed off of?!"
    s "I’m busy right now. Just let me drop this thing off and {i}then{/i} we can practice our...innuendo trading."

    scene secretsantatime30
    with dissolve

    ima "Fine. Give it here. "
    ima "I’m a little too old for stuffed animals, but I guess this’ll have to do. "
    s "Imani."
    ima "What, dude? You said you needed to drop that thing off. I’ve got arms. I can handle the drop."

    scene black
    with dissolve2

    s "Maybe next year."

    "If she’s even still around next year."
    "Based on my current track record, though, I think it’s probably safe to assume she will be."
    "Unless tonight ends with another dramatic turn of events, of course."
    "But I should probably find a tomboy to give this bear to before that winds up being the case."

    scene secretsantatime31
    with dissolve2

    s "Makoto, where-"
    s "Woah. What’s wrong?"
    mak "What am I supposed to do with this, Sensei?!"
    s "It’s a picture, so...I think you’re supposed to hang it up?"

    scene secretsantatime32
    with dissolve

    mak "It’s worth a million yen! I’ve never even touched anything this expensive before!"
    s "That is well over the $20 spending limit."
    mak "I knew something like this might happen when we set the limit in US dollars! Touka barely understands the value of {i}our{/i} currency, let alone a foreign one!"
    s "You know, I was wondering what the reasoning behind that was when I saw it written on the board the other day, but I decided against asking."
    mak "I need your help! I don’t know what to do with this thing!"
    s "I will gladly take it off your hands."

    scene secretsantatime33
    with dissolve

    mak "Not that kind of help! I need your help returning it! I can barely even hold this thing up! It’s too heavy!"
    s "Yeah, it must be really tough having all of that wealth in the palms of your hands. Poor you."

    scene secretsantatime34
    with dissolve

    mak "Ugh...why did she think something like this was okay?"
    s "That aside, have you seen Miku? I have to give her this present."

    scene secretsantatime35
    with dissolve

    mak "Miku? Yeah. She went outside to get some air a little while ago when things started getting loud."
    mak "Is that...stuffed animal you’re carrying for her?"
    s "Yeah. I didn’t really know what else to get and it kind of just jumped out at me."
    mak "And you...didn’t think she was too {i}boyish{/i} to enjoy something like that?"

    scene secretsantatime36
    with dissolve

    s "I have no idea if she’ll enjoy it or not. It’s just what I bought. If she likes it, she likes it. If she doesn’t-"
    mak "..."
    s "..."
    s "Makoto?"

    scene secretsantatime37
    with dissolve

    mak "She’s probably somewhere on the side of the hotel, where you can’t see any of the other buildings or cars or anything."
    mak "So...as far away from everything that she can possibly be right now without completely abandoning the party."
    s "Oh. Uhh, okay. "
    s "I guess I’ll just head out there now then."
    mak "And I’ll...be here. Stuck standing in place with this extremely valuable painting."
    s "I believe in you, Makoto. If there’s anyone good at not being crushed by the weight of responsibility and obligation, it’s you."

    scene secretsantatime38
    with dissolve

    mak "Okay. You can leave now."
    s "And I will do just that. See you later."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ christmastwo15 = True
    $ makoto_love += 1
    $ molly_love += 1
    stop music fadeout 7.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo16

label christmastwo16:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
with dissolve

        h "Definitely an interesting way to start Christmas, though."
        h "Can’t say I expected to watch my best friend get railed like an hour after helping her choose which color of tinsel to use."
        sar "And I can’t say I expected mine to enjoy it so much."
        sar "Also, did I sound weird? And don’t say you didn’t hear it this time since you were literally right there."
        h "I don’t remember. I was too busy being hurtful and perverted."
        sar "Ugh. Please pay more attention next time because I really need to know and I don’t want to record myself."
        h "You know, I really didn’t expect there to be a next time."
        sar "Me neither, but...we’re mature adults. I think we can do it again without all of the...meanness next time."
        h "..."
        sar "..."
        h "So, uhh...the bar."

        scene sidechristmas19
        with dissolve

        sar "Right! The bar!"

    sar "It looks so good. And we’ve got three whole employees working tonight."
    sar "I wish Sana could have been here as well, but her Christmas party just had to be on like, the single least convenient day of all time."
    h "You mean...Christmas?"
    sar "..."
    sar "Shut up."

    scene sidechristmas20
    with fade

    yu "Wait, Kaori..."
    k "Yes, Aunt Yukiburger? Do you need help finding another shiny item in this labyrinth of intoxicated women?"
    yu "No, it’s just..."
    yu "I could be completely misremembering but like, ain’t it your birthday today?"

    scene sidechristmas21
    with dissolve

    k "But I have so many memories of other days! How could I have been born today?!"
    yu "No, it means like...you were born on a different “today” in the past."
    k "I am from the past?!"
    yu "I mean...we kinda all are."

    scene sidechristmas22
    with fade

    sar "Kaori, is that true? Is it really your birthday today?"
    k "I still do not understand the concept of this “day of birthing,” but if Aunt Yukiburger, who is also from the past, knows the past-version of me...it might be true!"
    k "Will something bad happen as a result of this? Has my time here finally come to an end?"
    k "I must say goodbye to John!"
    maki "Is John your chicken boyfriend?"
    yu "Just her chicken. And he’s fucking huge, too. You should see that thing."

    scene sidechristmas23
    with dissolve

    maki "Heh. Huge cock."
    sar "Haru-chan, you didn’t see any birthday decorations in the storage room, did you?"
    h "Hm? I might have seen like, a banner or something. But are you really sure you want to put something like that up while we already have all of the Christmas decorations out?"

    scene sidechristmas24
    with dissolve

    sar "Kaori, are you going straight home after we close tonight?"
    k "Sleeping at work is forbidden, so I normally go home at the end of the day."
    sar "Stay later tonight. After all of the customers leave, we’ll throw a little birthday party for you."
    maki "Ooooh, fun! I haven’t pulled an all-nighter in years. What better reason to break that streak than for a temporary bartender’s birthday party?"

    scene sidechristmas25
    with fade

    k "A party? For me? Just because I was born?"
    k "Is that really a cause for celebration?"
    sar "Of course it is! Be happy you’re alive!"
    yu "I feel shitty for not gettin’ you somethin’ now. Can’t believe I forgot."
    yu "Not a big fan of stayin’ awake through the night, but I’ll make an exception for you since we’re related and shit."
    k "I do not understand the customs that typically accompany human birth-parties, but since I am the subject of the tradition this time, I will remain inside and do as you instruct."
    sar "Woo-hoo! It’s settled, then! Haruka, go get the banner!"
    h "Sara, I think you’re forgetting that I don’t actually work here. I’m a customer right now."
    sar "Maki, banner!"
    maki "Are you just going to ask {i}everyone{/i} who doesn’t work here?"

    scene black
    with dissolve2
    stop music fadeout 10.0

    sar "You there! What’s your name?"
    q "Me?"
    sar "Yes! Who are you?"
    matt "Matthew."
    sar "Take this key, open that door over there, pull out the birthday banner, and your next drink is on me."
    matt "Oh. Uhh...okay. I’m on it."
    sar "Wonderful! Thanks, Matthew."

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ christmastwo14 = True

    jump christmastwo15
...
```