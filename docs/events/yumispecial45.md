# See You Around (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 417

* Event [Unsung Heroes](./streets40.md) (Yumi) is completed)

* Day of week is Friday



## Next events

* [Main: Three Amigos](./christmastwo1.md)

## Event properties

* Id: yumispecial45
* Group: Yumi
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->yumispecial45

## Official wiki page

[See You Around](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumispecial45&go=Go) for more details.

## Event code

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label yumispecial45:
    scene yuminodoka1
    with fade
    play music "normalday.mp3"

    "Today’s story starts in the back of a familiar classroom- close to where the main character would sit if this were a run of the mill anime or manga series."
    "Fortunately for some and {i}un{/i}fortunately for others, {i}our{/i} protagonist is off doing something else right now."
    "But don’t worry! I’ll be here to keep you entertained until he makes it back."
    "I mean, what’s the sense in constantly following Sensei around if all of the interesting stuff is going to be happening here, right?"
    "This is no different from all of the other times we’ve spent together. "
    "I was just feeling a little friendly today."
    "..."
    "Who am I, you ask?"
    "Ha! "
    "Wouldn’t you like to know?"
    "Now, before we begin, I’d like to remind you that these are [teenage]girls we’re dealing with."
    "And sometimes, [teenage]girls tend to be impulsive or irrational or whatever else you want to call it. "
    "Do you see where I’m going with this?"
    "Sometimes, mountains are made out of molehills. And other times, things that are supposed to be perceived one way wind up being twisted into something entirely different."
    "But I’m sure you’re familiar with the concept of perception by now, aren’t you?"
    "You’re so smart."
    "Unless you’re one of those people who didn’t work for where you are right now, I mean."
    "Frankly, I wish those people would explode."
    "That’s something I’m allowed to say because you still have no idea who I am, or even the voice you’re supposed to be reading these words in."
    "But I won’t waste any more of your time dwelling on that- not when there are so many cute girls right in front of you!"
    "Now, which of these girls do you think will be the main character of this event?"
    "I guess there’s only one way to find out!"

    r "Do you guys think I’d look good with short hair?"

    scene yuminodoka2
    with dissolve

    f "Are you actually thinking of cutting it?"
    r "Mmm...I don’t know. Maybe? "
    r "Like half of the girls in this manga have short hair and they all look really cool and hot and stuff. {i}I{/i} want to be cool and hot and stuff."
    o "I already think you’re hot and stuff. But hey, follow your dreams and all that."
    r "Why did you leave out the part about me being cool?"

    scene yuminodoka3
    with dissolve

    o "So anyway, Futaba, you have any plans for Christmas? Rin and I were thinking about going to the urban district if you wanted to tag along."
    o "And if you’re worried about being the third wheel or something, just invite Nodoka along. I’m sure she’d be happy to be your date."
    no "Few things in life would make me happier."

    play sound "slidedoor.mp3"

    f "I’ll...be sure to check my schedule..."

    scene yuminodoka4
    with fade

    c "Oh, Yumi. I didn’t think you were going to show up today."
    y "Neither did I, but here I am..."
    y "The fuck are {i}you{/i} doing, though? Why’s it look like you’re about to leave?"

    scene yuminodoka5
    with dissolve

    c "Oh...you know...I was just gonna go...walk around and stuff..."
    y "If you’re looking for our douchebag teacher, I think I saw him near the library."

    scene yuminodoka6
    with dissolve

    c "See, this is why I keep you around. You always know exactly what it is I’m looking for."
    y "You do realize how fucking easy you are to read, right? No need to be impressed."
    c "Wanna come with me? Or are you going to hang out here?"

    scene yuminodoka7
    with dissolve

    c "Wait...don’t tell me {i}today’s{/i} the day..."
    c "Is it?"
    c "Is it finally happening?"
    c "Is my best friend taking her first step toward adulthood?"
    y "Okay, first off, can you word it in a way that makes it sound, you know, less fucking disgusting?"
    y "And second, I’ve taken plenty of steps toward adulthood. I watch your sister just as much as you do. Fuck, probably even more, actually."

    scene yuminodoka8
    with dissolve

    c "Yeah. You’ve been a huge help. "
    c "But I’m really proud of you for this, Yumi. I mean it."
    c "I feel like it was just the other day that-"

    scene yuminodoka9
    with dissolve

    if yumiknows == True:
        y "Yeah, yeah. Whatever. Just go back to stalking your totally legitimate boyfriend and stop being all mushy and shit. It’s gonna make me sick."
    else:
        y "Yeah, yeah. Whatever. Just go back to stalking our creepy fucking teacher and stop being all mushy and shit. It’s gonna make me sick."

    c "You know, it’s really impressive how you can still manage to be such a bitch even when you’re taking steps to improve yourself."

    if bonus == True:
        y "Don’t get too impressed. Wouldn’t want you falling for me instead of a dude twice your age."
    else:
        y "Don’t get too impressed. Wouldn’t want you falling for {i}me{/i} instead."

    c "Ew, I’m not going to fall for my roommate."

    scene yuminodoka10
    with dissolve

    if bonus == True:
        c "I’d let you join in if Sensei wanted, though."
    else:
        c "I’d let you join in on a group hug if Sensei wanted, though."

    y "Yo! Don’t even fuckin’ joke about shit like-"

    play sound "slidedoor.mp3"
    scene yuminodoka11
    with dissolve

    c "Bye, Yumi! I’ll let you know if you’re {i}needed{/i}~"
    y "...that."

    "As Chika wanders off to locate the object of her ever-apparent affection, the real main character of today’s event wanders into the classroom."
    "And, if you haven’t guessed by the obvious mentions of self-betterment and taking steps toward adulthood, that main character plans on doing something she should have done a long time ago."
    "Of course, a plan is just a plan- and until that plan is actually in motion, it’s no better than any of the many goals people set for themselves only to either fail or give up entirely."
    "So, who knows? Maybe she’ll do it, maybe she-"

    scene yuminodoka12
    with dissolve

    "Oh, look!"
    "There she goes!"
    "Come on! Let’s see what happens!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yuminodoka13
    with dissolve

    y "Yo."
    f "..."
    o "..."
    o "I think she’s talking to you, Futaba."
    f "Oh. Uhh..."

    scene yuminodoka14
    with dissolve

    f "{i}Are{/i} you...talking to me, Yumi?..."
    y "There a problem with that?"
    f "N-Not at all! It’s just...not how this normally goes..."
    o "Do you need something?"

    scene yuminodoka15
    with dissolve

    y "Why? You her gatekeeper now?"
    o "No, but if you’re just here to be mean to her, I see no reason for her to have to respond to you."

    scene yuminodoka16
    with dissolve

    y "Listen...can you like...come out into the hall for a second? There’s some shit I’ve gotta say to-"
    no "Anything you have to say to her can be said in front of all of us."

    scene yuminodoka17
    with dissolve

    y "Oh, great. Are {i}you{/i} her gatekeeper?"

    scene yuminodoka18
    with fade
    stop music fadeout 20.0

    no "I don’t think that’s what I’d necessarily call myself, but for the sake of the conversation, we can just assume that I am."
    f "Nodoka, I can-"
    r "Shh, no. Let Nodoka handle this. I feel like she can be really scary when she wants to be."
    y "Excuse me, fair lady, but could I trouble you for the permission to spend a few minutes alone with your princess?"
    no "Maybe if you try asking again without the unappreciated and irrefutably immature dose of sarcasm you decided to add in."
    y "..."
    y "I’m sorry, what’s your name again?"
    no "Nodoka Nagasawa."

    scene yuminodoka19
    with dissolve

    y "Hi, Nodoka. Nice to meet you. "
    y "Now, please step aside if you have any interest in keeping all of your teeth."

    scene yuminodoka20
    with dissolve
    play music "pianomelancholy3.mp3"

    no "Well, would you look at that? Only forty-five seconds in and you’re already resorting to violence."
    no "I knew from all I’ve heard that you were the type to jump to that right away, but I imagined we’d be able to talk for at least two minutes before any threats showed up."
    y "Listen, I don’t know who the fuck you think you are, but if I had business with you, I would have talked to {i}you.{/i}"
    y "I didn’t do shit, {i}Nodoka.{/i} So step the fuck aside and let me do what I came here to do without getting in the way."

    scene yuminodoka21
    with dissolve

    no "And what might that be? Because probability shows that it’s likely something along the lines of hurting my friend’s feelings in complete disregard for-"
    f "Nodoka...I’m glad that you’re standing up for me, but you really don’t have to do this..."
    no "No. No, I suppose I don’t."
    no "But that doesn’t change the fact that I am tired of this girl thinking she's allowed to just hurt you whenever her withered heart desires."
    no "So if she even {i}thinks{/i} about hurting you again, she’ll have to hurt me first."
    y "My fucking pleasure."
    r "Did Sensei say when he was coming back? Because I’m starting to think this might get bad."
    o "Uhh...let me see if I can find-"
    r "Wait, no! I need you here to protect me in case I somehow get roped into this. I’m a lover, not a fighter."

    scene yuminodoka22
    with dissolve

    y "I didn’t come over here to fucking fight! But if this four-eyed freak who thinks she’s being brave or something by confronting me wants to feel tough, I’ll give her what she wants!"
    no "I {i}want{/i} you to run back to whatever hole you crawled out of this morning and think long and hard about what you’ve done to this poor girl."

    scene yuminodoka23
    with dissolve

    y "That’s exactly what I’m fucking-"
    no "Who do you think you are, raising your voice when {i}you're{/i} the one constantly trampling all over everyone?"
    no "What gives you the right to hurt others? What gives you the right to hurt {i}Futaba?{/i}"
    no "Do you really feel so weak that the only way you can even {i}pretend{/i} to be strong is to tear good people who mind their own business down?"

    scene yuminodoka24
    with dissolve

    y "I...am not...fucking {i}weak.{/i}"
    y "Do you have any idea-"
    no "Oh, spare me the sob story."
    no "I’m well-read enough to know that this is the part where your character comes out and cries about her background in an effort to explain away her misdeeds."
    no "Thing is, I care a little too much about Futaba to be swayed by any of what you have to say. "
    no "So please do all of us a favor and just hit me instead of crying and risking getting your tears all over my uniform."
    y "That’s it. "
    y "You’re fucking dead."

    play sound "static.mp3"
    scene treefall1 with flash
    scene gymbully1 with flash
    scene futabagymtwo5 with flash
    scene showers12 with flash
    scene treefall1 with flash
    scene futabayumisnow21 with flash
    scene futabagymtwo5 with flash
    scene yuminodoka25 with flash
    stop sound

    y "What-"
    y "Let go of me!"
    t "Bullying is wrong. I will prevent this behavior in the absence of our teacher."
    r "Okay, that’s enough. Let’s sit back down, Nodoka. "
    r "I know you're just trying to help, but I think Futaba's enjoying this the least out of everyone right now..."
    f "Yumi...I-"
    y "I’m going to tell you one more time..."
    y "Let...me...go..."
    t "I’m sorry. I can not do that until I confirm that you will not be harming any of my classmates."

    scene yuminodoka26
    with dissolve

    y "Please..."
    t "..."
    y "Let me go..."
    t "..."
    no "..."

    scene yuminodoka27
    with dissolve
    play sound "slidedoor.mp3"

    t "..."
    no "..."
    t "I no longer sensed a threat..."
    r "Was...Yumi actually crying just now?"
    f "You were too hard on her, Nodoka..."
    no "Perhaps I was. "
    no "I just didn’t want to take any ch-"
    f "I...have to chase after her."

    scene yuminodoka28
    with dissolve

    no "What? Why? She’s done nothing but torment you the entire school year. I say you let {i}her{/i} wallow in misery for a change."
    f "That makes me just as bad as her..."
    no "It really doesn’t. "
    r "If you’re going to go, do it now. Wait any longer and I doubt you’ll be able to catch her."
    no "Futaba-"

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    f "I’m sorry, Nodoka...I have to..."

    "........."
    "......"
    "..."

    scene yuminodoka29
    with dissolve

    f "Yumi! Wait!"
    y "The fuck do you want, fatass?! You know I was just going to make fun of you again, right?!"
    f "I know that’s not true!"


    scene yuminodoka30
    with dissolve

    f "You’ve always just...done that in front of whoever was around."
    f "It’s not something you’d have to get me alone for..."
    y "Yeah, well...this time it was! Now, beat it!"

    scene yuminodoka31
    with dissolve

    f "Yumi, I’m sorry!"
    y "Wha- for what?! The fuck do {i}you{/i} have to apologize for?!"
    f "For Nodoka! She went too far! I didn’t want her to do that!"
    f "I was open to...talking."

    scene yuminodoka32
    with dissolve

    y "Yeah, well...tell that to your fucking girlfriend next time."
    f "Can you please just...stop for a second and talk to me?..."

    scene yuminodoka33
    with dissolve

    y "..."
    f "...Please?"
    y "..."
    y "Yeah, alright. Whatever."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yuminodoka34
    with dissolve

    f "..."
    y "..."
    f "What..."
    f "What did you want to tell me?..."
    y "..."
    y "So, uhh..."
    y "I don’t really know how to do this kinda shit, so if it sounds like I’m makin’ fun of you or whatever, that’s...not what I’m tryin’ to do."
    y "I, uhh..."
    y "I know I’ve been a huge dick to you and whatnot..."
    y "And apparently it’s bad enough that your friends are worried about me even being {i}near{/i} you now..."

    scene yuminodoka35
    with dissolve

    y "Hah...pretty pathetic, right? Not for you. For me, I mean. "
    y "I deserve it, though."
    y "I’ve been treatin’ people like shit for my entire life. It’s just...kind of what I’ve always done."
    y "And I know it should be like common sense or whatever to not pick on people...but it woulda been nice if there was like...someone who woulda told me that early on, you know?"

    scene yuminodoka36
    with dissolve

    y "I...I’m not tryin’ to make excuses! I just know that...I’ve been really fucked up to you and..."
    y "And I guess what I wanna say is that I’m gonna try and be like...less fucked up to you or whatever..."
    y "And..."

    scene yuminodoka37
    with dissolve

    y "And I’m like...sorry and shit..."
    f "..."
    y "..."
    y "I don’t expect you to just forgive me after all this time, but I’m like..."

    scene yuminodoka38
    with dissolve

    y "Uhh..."
    y "Let’s just say I’m starting to get a little worried about how I might end up if I don’t start changin’ shit."
    f "I forgive you."

    scene yuminodoka39
    with dissolve

    y "What?! No, hold up. That was way too fuckin’ easy. You’re supposed to hate me."
    y "Like, look at that Nodoka girl. I didn’t speak a word to her at all until today and she fuckin’ {i}despises{/i} me. If anyone should hate me even more than that, it’s you."
    f "You’re right. "
    f "I should hate you more."

    scene yuminodoka40
    with dissolve

    f "I lost track of how many times things you’ve said to me have made me cry or...run to Sensei’s office for help or..."
    f "Or just acknowledgment that I'm more than all of those horrible insults."
    f "And I’d be lying if I said I never wished you would transfer to a different school or something."
    y "I would've wished a lot worse than that if I was in your shoes."

    scene yuminodoka41
    with dissolve

    f "But even with that...I still forgive you."
    y "But...{i}why?{/i} I don’t get it."
    f "Does there need to be a reason?"
    f "I just do."
    y "..."
    f "..."

    scene yuminodoka42
    with dissolve

    f "I’m...gonna go back to class now. But...I’m glad we were able to talk."
    f "And I’m sorry again for Nodoka."
    y "..."
    y "Oh, okay. Uhh..."
    y "I guess...see you around then?"

    scene yuminodoka43
    with dissolve

    f "Yeah."
    f "See you around."

    scene yuminodoka44
    with dissolve

    y "Hah..."
    y "..."
    y "..."
    y "..."

    play sound "slidedoor.mp3"
    scene yuminodoka45
    with dissolve

    s "..."
    y "..."
    s "I heard all of that, you know."
    s "I’m really proud of you."
    y "Suck my dick, asshole."
    s "So proud."

    scene yuminodoka46
    with dissolve

    y "..."
    y "Apologizing to people is fuckin’ exhausting."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ yumispecial45 = True
    stop music fadeout 5.0

    "{i}Yumi will no longer bully Futaba!{/i}"
    "{i}Hopefully!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
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
    if totaldays >= 410 and kirin_love >= 30 and kirinsoccer25 == True and ayanelust15 == True and kirinspecial30 == False:
        jump kirinspecial30
    if totaldays >= 417 and streets40 == True and day == 5 and yumispecial45 == False:
        jump yumispecial45
...
```