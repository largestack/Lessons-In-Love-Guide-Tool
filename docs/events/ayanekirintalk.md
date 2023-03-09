# Furlough
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanekirintalk&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 550

✅Event "[Ayane: What a Wonderful World](./ayanelust15.md)" is completed (event=ayanelust15)

❌Event "[Ayane: Chiburi](./ayanespecial50.md)" is completed (event=ayanespecial50)

❌Day of week is Thursday



## Next events
None

## Event properties
* ID: ayanekirintalk
* Group: Ayane
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label ayanekirintalk:
    scene furlough1
    with fade
    play music "normalday.mp3"

    m "...and that’s just one of the many reasons I don’t think children under the age of ten should be allowed in public spaces."
    s "Well said, Maya. Though, I’m a little confused as to why you’re the one kicking off this event when Ayane is the typical open-ended intro provider."
    ay "Hey, I’m fine with Maya stealing the spotlight every now and then. It’s not like I have an infinite amount of stories to tell all of you like she does."

    scene furlough2
    with dissolve

    a "What does that mean? I’m pretty sure Maya is younger than you and it’s not exactly like she leads a very exciting life."
    m "Hey."
    ay "What’s more exciting than immortality?"

    scene furlough3
    with dissolve

    a "Are you immortal now? Or is this just one more inside joke between you, Ayane, and Sensei that I am not a part of because you are slowly removing me from both the Love Squad and your lives?"
    m "I have no interest in the “Love Squad.” I simply wanted to share an opinion of mine. But if me having thoughts is going to be the cause of so many problems, I’ll just go back to being quiet."

    scene furlough4
    with dissolve

    a "So, what’s the plan now?"
    a "I was thinking we could stop at that cafe with all of the cool parfaits again. But if nobody else is hungry, we can always just go back to my house and play games or something."
    ay "Oh, yeah. About that. I forgot to tell you- I actually wound up making plans with somebody else today, so you guys can head over to...wherever without me."

    scene furlough5
    with dissolve

    a "Other plans? But we always go home together if we’re still around when our clubs finish meeting."
    ay "And I’m sure we’ll continue to do that in the future! I just can’t today. Sorry, Ami."

    scene furlough6
    with dissolve

    a "Man. I was really hoping we’d get to use your black card. I always feel so important whenever we get to pay with that. "
    a "Oh. What I actually meant to say there is that I will miss you and hope that whatever plans you made with someone I can only assume is Sana go well."
    s "Everything alright? It’s one thing to not provide the intro, but bailing on everyone isn’t exactly in-character for you."
    ay "Mhm! Everything is totally cool. Just have a couple loose-ends I need to tie up before leaving school today. But I’ll meet up with you guys again once it’s all over."
    a "Well...have fun, I guess. The three of us will probably just go home if you’re not coming since I don’t want to have to share a parfait with Maya. She’ll eat it all. And Sensei doesn’t eat anything “cute.”"
    s "It’s true. I have to remain masculine at all times or people won’t take me seriously anymore."

    scene black
    with dissolve2
    stop music fadeout 15.0

    ay "I guess I’ll just wind up seeing you all back at Ami’s house, then! Bye bye!"

    "{i}Four becomes three as Ayane wanders away from those she loves the most.{/i}"
    "{i}It is not the only example of numbers becoming numbers in recent memory, but it is the one I am contractually obligated to inform you of right now.{/i}"
    "{i}But where is she going, I wonder? And what or who will she find when she gets there?{/i}"
    "{i}A snake? A rabbit? A bat? A cat?{/i}"

    play sound "static.mp3"
    scene furlough7
    with flash
    stop sound
    play music "pianomelancholy3.mp3"

    "{i}Or the human embodiment of a trash can pretending to be sentient as it leans against the hood of a stranger’s car and thinks to itself about why sexual assault is okay so long as the majority of parties orgasm.{/i}"
    "{i}Anyway, I’m done here.{/i}"
    "{i}I don’t want to stick around for this.{/i}"

    ki "Hey. I was beginning to think you weren’t going to show up."
    ay "I wouldn’t have asked to meet you here if I was planning on ditching. Not all of us thrive on the amount of inconveniences we cause for those around us."
    ki "Well, you know me. The “amount of inconveniences I cause for those around me” is what gets my motor running in the morning."
    ki "And yet, despite that, I still took the time out of my extremely busy practice schedule to see you today. I’m such a good friend, aren’t I?"
    ay "Don’t give me that shit. We haven’t been friends in a long time."

    scene furlough8
    with dissolve

    ki "Hmm...when did our friendship end again?"
    ki "Was it the time you came all over my hand at the beach house? Or was it the time we treated Sensei’s cock like a giant lollipop together?"
    ki "Come to think of it, it was probably the first time since you weren’t even wet when I tried to put my fingers in during the Dorm Wars. And that’s just plain unfriendly."
    ay "Are you done?"

    scene furlough9
    with dissolve

    ki "I can be. Though, I’d be lying if I said I wasn’t a {i}little{/i} hopeful that the reason you called me out here today was to organize our next threesome."
    ki "Or twosome. I’d let you fuck me alone if you want. Or vice versa. See, I’ve been practicing this thing with my tongue where-"
    ay "We’re done."

    scene furlough10
    with dissolve

    ki "{i}Done?{/i}"
    ay "It’s over. I’m not letting you hold my life hostage anymore."
    ay "You want to keep seeing Sensei behind my back? Fine. But I’m done letting you come between us. "
    ki "Yeah, here’s the thing. That’s not really up to you, sweetheart."

    scene furlough11
    with dissolve

    ay "Don’t call me “sweetheart,” you fragile little bitch. We both know you’re overcompensating for how insignificant and unneeded you feel right now."
    ki "Ooooh. Where’d this side of you come from? It’s kind of turning me on."
    ay "Do me a favor and kindly fuck off for the rest of forever, please. I don’t have time for this anymore."
    ki "You don’t? What changed?"
    ay "Kirin."
    ki "If you’re worried about Sensei falling for {i}me{/i} instead, don’t. Like you said, I’m “insignificant” and “unneeded.”"
    ki "But I’m a great receptacle for his semen since he always seems to like it when I wrap my legs around him and make it so he can’t pull out."

    scene furlough12
    with dissolve

    ki "Oh, but don’t worry about me getting pregnant. I’m on birth control, so he can cum inside of me as much as he wants and everything will be totally fine!"
    ki "In terms of actual raw, {i}love{/i} though...don’t worry. I’m just not that type of girl."
    ay "Fantastic. Can I take that as you agreeing to simply fuck him while I’m not around then? Or are you still going to try and drag all three of us under the sheets together?"

    scene furlough13
    with dissolve

    ki "Hmm...depends on how horny I am, I guess. Just Sensei won’t always do it for me, you know. I like having you around as well. "
    ki "You do this cute, little...high pitched yelp thing whenever you’re feeling good that makes me a lot hotter than any cock ever has, that’s for sure."
    ki "I’m just not sure if I’m ready to give that up. Nor do I understand why I’d {i}have{/i} to just because you decided to finally stand up to me."

    scene furlough12
    with dissolve

    ki "{i}Why{/i} you decided to stand up to me, I’m not sure. It’s not like having you point out my flaws and cry about how you don’t like me touching you is going to make me magically not want to do it anymore."
    ki "Remember, Ayane- you’re the one who agreed to this little...{i}arrangement{/i} in order to protect Sensei."
    ki "If you’re going to try and back out of it, nothing’s stopping me from just telling everyone about the two of you and ruining {i}both{/i} of your lives once and-"

    play sound "static.mp3"
    scene furlough14 with flash
    stop sound

    ay "Do it."
    ki "Huh?"
    ay "Fucking do it. I dare you."
    ay "Ruin our lives."
    ay "Tell the world about us and see what happens. Sensei will love me just the same."
    ay "But you? "
    ay "You’ll never know what it’s like to feel what I feel. To feel any amount of love at all."
    ay "So stop fucking chasing it, you hear me?"
    ay "Don’t you fucking dare ruin {i}my{/i} time with him because you’re so desperate for a taste of affection that you’d sooner drink it from my pussy than take a second to {i}grow the fuck up.{/i}"
    ki "The fuck is this? Since when are you this aggro about literally anything?"
    ay "I told you. I don’t have time for this anymore."
    ay "And I’m not going to let you fuck up what little time I may have {i}left{/i} with your petty insistence on being there during our most private moments."
    ay "You want to tell everybody about it? Go ahead. Because I’d sure as fuck prefer being called a whore over having to spend one more second around your filthy fucking cunt."

    scene furlough15
    with dissolve

    ki "And Sensei’s career? You’re suddenly fine with throwing {i}that{/i} in the trash if it means the two of you get to fuck each other more privately from now on?"
    ay "Mhm. "
    ki "See! So you {i}don’t{/i} want-"

    scene furlough16
    with dissolve

    ki "Wait, what?"
    ay "I don’t think {i}shit{/i} will happen to Sensei’s career. Nor do I think you have the balls to actually {i}tell{/i} anyone about this. {i}Nor{/i} do I think anyone would believe a thirsty, jealous bitch like you."

    scene furlough17
    with dissolve

    ki "You’ll regret saying that to me, you know. I might not be as popular as you, but people will still believe what I-"
    ay "The only thing I regret is letting things get to this point in the first place. "
    ay "If I had known back then what I know {i}now,{/i} I would have hopped off his dick and slammed that door right in your fucking face."
    ay "You should have been stuck outside of it like the fucking parasite you are...thriving off of what the two of us were doing together because you know damn well you’d die on your own."
    ki "Parasite?..."
    ki "Well..."
    ki "Well at least I don’t have a fucking daddy complex that drove me to fucking my teacher in the first-"

    play sound "static.mp3"
    scene furlough18 with flash
    stop sound

    ki "NGH-?!"
    ay "Why {i}would{/i} you? Your parents don’t even {i}like{/i} you. That’s why they spend all of their time and energy on Karin instead."
    ay "So what if Sensei stepped in when my dad started neglecting me? So what if he filled a role I desperately needed someone to fill? We’re in love now and that’s all that matters."
    ay "Meanwhile, you’re so fucking desperate for attention that I bet you’d let your {i}actual{/i} father fill that loose cunt of yours if it meant making you feel alive for a fraction of a second."

    scene furlough19
    with dissolve

    ki "Let...go..."
    ay "Shut the fuck up. I’m barely even squeezing."
    ki "You think you’re...so much better...than me!"
    ay "Of course I do. I {i}am{/i} better than you. "
    ay "I don’t get off on hurting people. I {i}accept{/i} the parts of myself I’m not comfortable with. "
    ay "All {i}you{/i} do is involve yourself in everyone else’s issues because the ones {i}you{/i} have are so uninteresting and petty that they’re barely even {i}issues{/i} at all."
    ay "Get over yourself, Kirin. It’s very sad. "
    ay "But what’s even sadder is that, when I let go, you’re probably going to tell me that you {i}still{/i} refuse to leave Sensei and me alone."
    ay "But that wouldn’t be very good for you because, if you haven’t been able to figure it out so far, {i}I don’t give a shit anymore.{/i}"
    ay "And I can ruin your life a hell of a lot easier than you can ruin mine."

    scene furlough20
    with dissolve

    ki "S..."
    ay "..."
    ki "S...S-"
    ay "Stop?...Sensei?...Sorry?..."
    ay "What are you trying to say? Speak up."

    scene furlough21
    with dissolve

    ki "S..."
    ki "Science...fair!"
    ay "..."

    scene furlough22
    with dissolve

    ay "Heh?"
    ki "The...science fair!"
    ki "This...never would have happened if...you just...didn’t beat me!"
    ay "..."
    ki "You ruined...everything! I finally...could have...made my parents...proud of me!"

    scene furlough23
    with dissolve

    ki "If that never happened...I never would have wanted revenge...I never would have started watching you...being jealous of you..."
    ki "It’s all because you ruined the {i}one{/i} thing in my life that I felt like I did well! You ruined it!"
    ay "..."
    ki "..."
    ay "Are you fucking kidding me?"

    scene furlough24
    with dissolve

    ki "It’s not funny!"
    ay "You...tried to ruin my life...over the fucking {i}science fair?{/i}"
    ki "You...You ruined mine first! You-"

    scene furlough25
    with dissolve

    ay "Hah...hahah...hahaha..."
    ay "Hahahahahah!"
    ki "Why are you laughing? It’s not-"

    scene furlough26
    with dissolve

    ay "I'm laughing because you’re a fucking joke."
    ki "I’m not a joke. Just because I’m not as lucky or gifted as you doesn’t mean I-"
    ay "No. You’re seriously a fucking joke. "
    ay "And if you ever try to come between Sensei and me again, I will snap your trachea like a twig."

    scene furlough27
    with dissolve

    ki "D...Don’t laugh at me! Ayane!"
    ay "I wonder if Sensei and the others are back at home yet? I might still be able to catch up if I start running."
    ki "Pay attention to me! This is serious!"

    scene furlough28
    with dissolve

    ay "What’s so serious about you wanting attention? That’s literally all you ever do. It’s pathetic. {i}You’re{/i} pathetic. Trash. Worthless. Scum. Go fuck yourself."
    ki "I just...I just wanted to feel like I-"
    ay "I don’t care."
    ay "In fact, I kind of wish you were dead."
    ay "Now, if you’ll please excuse me, I am going to go hang out with a group of people who enjoy my presence. Which is, coincidentally and quite hilariously, something you will never be able to do."
    ki "There are...people who-"
    ay "No. "
    ay "There really aren’t, Kirin."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "{i}I heard from someone else that things went better than I thought they would.{/i}"
    "{i}How ironic.{/i}"
    "{i}I’ve grown so used to the slow burn of divine comedy that any punchline dissimilar to the feeling brought on by fiery coals beneath my feet is like an ice pack for an aneurysm.{/i}"
    "{i}It helps, but just slightly enough to distract me from the fact that everything is horrible and that it will all be over soon.{/i}"
    "{i}Or at least it would be in most cases.{/i}"
    "{i}The cycle would see otherwise.{/i}"
    "{i}But it seems the cycle can’t see at all.{/i}"
    "{i}For if it could, none of this would happen.{/i}"
    "{i}For if it could, things would never change.{/i}"
    "{i}It’s so interesting that they finally are.{/i}"

    $ renpy.end_replay()
    $ ayanekirintalk = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
    if totaldays >= 410 and kirin_love >= 30 and kirinsoccer25 == True and ayanelust15 == True and kirinspecial30 == False:
        jump kirinspecial30
    if totaldays >= 417 and streets40 == True and day == 5 and yumispecial45 == False:
        jump yumispecial45
    if totaldays >= 424 and kirindorm25 == True and day == 1 and chikaspecial40 == False:
        jump chikaspecial40
    if totaldays >= 455 and chikadate45 == True and yumispecial45 == True and norikodorm25 == True and nikiinvite2 == True and sarabar25p2 == True and day == 4 and christmastwo1 == False:
        jump christmastwo1
    if totaldays >= 500 and chapthree8 == True and church15 == True and yasuspecial15 == False:
        jump yasuspecial15
    if totaldays >= 514 and yasudorm20 == True and nodokadorm15 == True and day == 4 and nodokaspecial15p1 == False:
        jump nodokaspecial15p1
    if totaldays >= 522 and sadgirls7 == True and day == 5 and sadgirls8 == False:
        jump sadgirls8
    if totaldays >= 530 and iospecial30 == True and karindate25 == True and day == 1 and tsukasaspecial1 == False:
        jump tsukasaspecial1
    if totaldays >= 535 and wakanadate15 == True and day == 5 and imanispecial1 == False:
        jump imanispecial1
    if totaldays >= 540 and imanispecial1 == True and day == 2 and ayanespecial40 == False:
        jump ayanespecial40
    if totaldays >= 541 and rindorm55p2 == True and bar55 == True and day == 3 and rikaspecial1 == False:
        jump rikaspecial1
    if totaldays >= 543 and rikaspecial1 == True and osakodate20 == True and day == 5 and day543 == False:
        jump day543
    if totaldays >= 547 and day543 == True and ayanesanabeach1 == True and day == 1 and ayanespecial50 == False:
        jump ayanespecial50
    if totaldays >= 550 and ayanelust15 == True and ayanespecial50 == True and day == 4 and ayanekirintalk == False:
        jump ayanekirintalk
...
```