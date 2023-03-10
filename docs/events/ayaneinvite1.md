# Hail Mary (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

* [Ayane: One of Many Rooms](./ayaneinvite2.md)

## Event properties

* Id: ayaneinvite1
* Group: Ayane
* Triggered by label: ayaneinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->ayaneinvite->ayaneinvite1

## Official wiki page

[Hail Mary](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayaneinvite1&go=Go) for more details.

## Event code

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label ayaneinvite1:
    play sound "phonebeep.wav"

    "I tap on Ayane’s name in my phone and wait for her to answer. "
    "I figure that if there’s anyone who would be happy to receive an invite to the house from me directly, it would be her."
    "But, then again, there’s a good chance she’s already there right now if she went home with Ami."
    "If that were the case, I’d feel a little strange about calling her right now...but I guess it’s going to wind up being strange no matter what at this point."
    "As long as she agrees, that is."
    "Which she will because she is Ayane."

    play sound "phonebeep.wav"

    ay "Yes! I will!"
    s "What? I haven’t even asked you anything yet."
    ay "Whatever you want, the answer is yes!"

    if bonus == True:
        ay "Unless you’re breaking up with me. Then the answer is no."
        s "We’re not even dating, Ayane."
        ay "That’s okay! We don’t need to put a label on our love!"
        ay "I’ll be excited to spend the rest of my life with you no matter what we call it~"
        s "…"
    else:
        ay "Unless you are planning on ordering dinner from Wendy's! If that is the case, I don't want any!"
        s "That is not what is happening here."

    ay "So, anyway, what was it you wanted?"
    s "I was going to see if you wanted to come over but now I might be having second-"
    ay "I’m on my way!"

    play sound "phonebeep.wav"

    s "…"

    "Welp, any second thoughts I might have had don’t matter now."

    scene black
    with dissolve
    stop music fadeout 5.0

    "Ayane is already on the way to the house...and since I'm the one who invited her over, a certain [niece] of mine might be a little taken aback by a sudden appearance from the bubble wrap princess."
    "Especially an appearance that would likely begin with something along the lines of “I am here for your [uncle],” or whatever it is Ayane would say."
    "So I guess I should hurry up and get home before something like that happens."
    "………"
    "……"
    "…"

    scene ayanefirstinvite1
    with dissolve
    play music "happyandplotting.mp3"

    "I manage to show up at the house before Ayane makes it here and find Ami microwaving something in the kitchen."
    "She tries to start a conversation with me but, knowing how things like this tend to go, I dismiss her entirely and make it seem like I’m in no mood to talk."
    "An excellent strategy, if you ask me."
    "This way, once Ayane makes it over, the two of us can quickly duck into my room before Ami has a chance to-"

    play sound "knock.mp3"

    ay "Open up! I’m ready for love!"
    s "…"

    "Before Ami has a chance to find out that she’s here."

    play sound "lock.mp3"

    "The lock suddenly...unlocks?"

    play sound "dooropen.mp3"
    scene ayanefirstinvite2
    with dissolve

    ay "Oh, good. You’re right here."
    ay "I had to use my emergency key since you took too long to answer the door."
    s "You walked in two seconds after knocking."
    ay "And they were the longest, most painful two seconds of my life."

    scene ayanefirstinvite3
    with dissolve

    ay "Thanks for inviting me over today, Sensei."
    ay "Normally, it’s Ami who asks me to come over and I need to think up creative ways to get to you instead."
    ay "I’m glad that she isn’t around and that I won’t have to do that today."
    s "Here’s the thing, Ayane. Ami {i}is{/i} around today."

    scene ayanefirstinvite4
    with dissolve

    ay "And you still invited me over?"
    ay "Do you have a deathwish?"
    s "No. I do not have a deathwish."
    ay "Then are you trying to get {i}me{/i} killed? Because there is no way that one of those two things won’t be happening."

    if bonus == True:
        ay "Especially since you called me over to have sex with me on her bed."
        s "It’s going to be fi- "
        s "Wait a second. That is {i}not{/i} why I called you over here."
        ay "It’s not?"

    s "I feel like you gravely misinterpreted the purpose of this meeting."

    if bonus == True:
        ay "But we’ve already done it on my bed and your bed so the next logical step has to be hers, doesn’t it?"
        s "I just wanted to spend time with you..."
        ay "With me or in me?"
        ay "I’m very horny today."
        s "I can see that."

        scene ayanefirstinvite5
        with dissolve

        ay "I can’t imagine it will be easy doing something like that with Ami around, though."
        ay "I mean, I guess we could wait until she’s in the bath or something, but-"
        s "Why don’t we just hang out in my room and {i}not{/i} risk dismantling our relationship today?"

        scene ayanefirstinvite6
        with dissolve

        ay "Ah! You said relationship! I {i}knew{/i} we were dating! "
        ay "No take backs, [ayanemaster]! I hereby pronounce us husband and wife!"
        ay "You may kiss the Ayane!"

    play sound "dooropen.mp3"
    scene ayanefirstinvite7
    with dissolve

    a "Sensei? Is somebody else out here? I thought I heard-"

    scene ayanefirstinvite8
    with dissolve

    a "Ayane? What are you doing here?"
    a "Did we have plans to hang out today?"
    a "I’m really sorry. I completely forgot."
    a "If you want to come hang out in my room, I’m watching this show about-"
    ay "A-Actually, Ami..."
    ay "I’m...here to..."
    s "…"

    scene ayanefirstinvite9
    with dissolve

    ay "I’m sorry. I don’t want to be the one to break her heart."
    ay "Ami is my best friend and I could never hurt her like this."
    a "Hurt me like what? What are you talking about?"
    a "Also, what are you still doing out here, Sensei? "
    a "I thought you wanted to be left alone today?"
    a "This whole situation is starting to feel really-"

    scene ayanefirstinvite10
    with dissolve

    a "Hey, wait a second! I see what’s going on here!"
    ay "You...do?"
    a "You two were going to cook me a surprise dinner, weren’t you?!"
    s "…"
    ay "…"
    ay "Yes."

    if bonus == True:
        ay "I did not come here to defile your bed."

    ay "I came here to cook food."

    scene ayanefirstinvite11
    with dissolve

    a "Sensei...you weren't in a bad mood after all. You were just upset because you saw me microwaving food instead of cooking dinner..."
    a "So you probably called the first name in your phone and had them rush over here to help since you can’t cook at all."
    a "And since Ayane is the first name to come after Ami in your contacts, you just threw a Hail Mary and prayed she’d be free."
    a "I’m so sorry that I worried you so much. "
    a "I’m okay, Ayane. You can go home now and I will spend the rest of the night comforting my [uncle]."
    s "…"
    ay "…"
    s "Actually-"
    s "I asked Ayane to hang out today."

    scene ayanefirstinvite12
    with dissolve

    ay "Ah..."
    a "You...what?"
    a "You mean you tried to call me in your phone and then...pressed her name on accident and felt bad about turning her away...or?"
    ay "I really hope not. That would break my heart."
    s "No, I called her intentionally because I wanted to see her."
    ay "…"
    a "So...you probably just assumed I was working or something then, right?"
    a "Cause there’s no reason you’d ever...call her instead of me..."
    ay "{i}Just roll with it, Sensei. This is the best escape route you’re going to get.{/i}"
    s "…"
    a "…"
    s "Yeah, sure. Why not."

    scene ayanefirstinvite13
    with dissolve

    a "Jeez...Just check with me next time, Sensei...Do you really get lonely that easily?"
    a "You don’t have to invite people here just because you think I’m going to be away."
    a "In fact, if you close your eyes and think of me, it’s almost like I’m always there! Or something!"
    a "Hahaha...hahahahah..."

    "This level of denial is something I’d expect from a relapsing drug addict, not a girl catching her [uncle] spending time with one of her friends."
    "Though, to be fair, both of those things sound kind of bad when put into words."
    "If anything, mine might actually sound worse."
    "But that doesn’t change the fact that I {i}did{/i} invite Ayane to the house today, and abandoning her now of all times would be too rude even for me."
    "I just have to think of a way to get Ami out of the picture- which might actually be a little harder than normal given that she’s on high alert right now."

    s "Well...I {i}did{/i} promise Ayane that the two of us could do something tonight, so if you could-"

    scene ayanefirstinvite14
    with dissolve

    ay "Actually..."
    ay "How about we all just hang out together? Like old times."
    a "You mean like...when you first started coming over a billion years ago?"
    ay "Yeah, before Maya came into the picture."
    a "That makes it sound like you don’t like Maya."
    ay "I love Maya. But you and Sensei are basically family to me."
    ay "So spending time with the two of you like how we used to is really all I could ask for."

    scene ayanefirstinvite15
    with dissolve

    "Ayane and I lock eyes for a moment and I honestly can’t tell whether or not she’s actually okay with this."
    "Her words sound sincere but, just a few moments ago, she was over the moon at the prospect of hanging out alone with me."
    "Taking that away from her now seems like it would just be adding more weight to the burden she already carries in hiding (Or at least {i}trying{/i} to hide) her feelings for me."

    s "{i}Are you really okay with that?{/i}"
    ay "{i}Of course.{/i}"

    if bonus == True:
        ay "{i}Hearing you stand up for me made me happier than getting pounded on Ami’s bed ever would.{/i}"
        s "{i}That’s not a thing you should be whispering with her right there.{/i}"
        ay "{i}I’m going to go home and [masturbate] to you tonight.{/i}"
        s "{i}Cool.{/i}"

    a "Uhh...guys?"
    a "If the {i}three{/i} of us are going to hang out, you should probably stop whispering to each other."
    a "I’d like to be included too, you know."

    scene ayanefirstinvite16
    with dissolve

    ay "Oh, of course! "
    ay "Sorry, Ami. I was just striking up a compromise with Sensei since we’ve now included you in our plans."
    a "What kind of compromise?!"
    a "What happened to all that stuff about the “old times” or whatever?! Why is there suddenly a condition?!"
    ay "It’s a simple condition."
    ay "All I ask is that I get to hold Sensei’s hand for the rest of the day while you stay ten feet away from us."
    a "I might as well be in a different room at that point!"
    ay "Well, if that’s what you’d prefer, then feel free to-"
    a "Unhand my [uncle], Ayane! Your compromise is denied!"
    a "If anyone is holding Sensei’s hand, it is his [niece] and your {i}alleged{/i} best friend!"
    s "Let the record show that I have two hands and can easily solve this problem for everyone."
    ay "See, Ami? I was even kind enough to leave his other hand available for you."
    ay "As long as you’re able to remain ten feet away, that is."

    scene ayanefirstinvite17
    with dissolve

    a "Sensei’s super tall but even {i}his{/i} stupid hand won’t reach that far! This is an unrealistic condition!"
    ay "Five feet?"
    a "No!"
    ay "Four?"
    a "Still no!"
    ay "Okay, okay. Fine. You’re free to hold his other hand. But I also get to rest my head on his shoulder when we sit on the couch."

    scene ayanefirstinvite18
    with dissolve

    a "Then so...do...I..."

    if bonus == True:
        a "I’m gonna cuddle with him in ways that someone like you could never even imagine..."

    ay "Oh? Is that a challenge, Ami?"
    ay "I’m sure you remember how our last challenge ended up, don’t you?"
    a "You mean the cooking one?"
    a "I defeated you. I asserted dominance."
    ay "You may have won, yes..."
    ay "But who got to hold the giant banana?"

    scene ayanefirstinvite19
    with dissolve

    a "A...ya...neeeeeeeeeeeeeeeeeeee!!!!!!!!!!!"
    ay "{i}This banana belongs to me...{/i}"

    scene black
    with dissolve2

    "And that basically explains how the rest of the night went."
    "Ayane and Ami proceeded to fight over me for the next several hours, using my arms like some sort of tug-of-war rope and leaving me broken and bruised by the time the day ended."
    "But even though it’s become hard to feel my fingers, it was nice seeing two girls who care so much about me fight each other like that."
    "I kind of wish they would have pulled each other's hair or something, though."
    "That’s what this night {i}really{/i} needed."

    $ renpy.end_replay()
    $ ayane_love += 3
    $ ayaneinvite1 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayaneinvite2:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label ayaneinvite:
    if ayaneinvite1 == False:
        jump ayaneinvite1
...
```