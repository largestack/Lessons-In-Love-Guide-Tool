# Goodnight
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach17&go=Go)


Part of event chain [Try. Try. Try.](./secondbeach16.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: secondbeach17
* Group: Main
* Triggered by label: secondbeach16

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach17:
    if _in_replay:
        play music "goodnight.mp3"

    scene clearnightsky
    with dissolve

    "There we go."
    "That’s better."
    "I picked out a beautiful song for you so we could have some nice background music as we watch the stars together."
    "If you look close enough, you might see one falling."
    "But if you blink, you’ll miss it."
    "Probably."
    "I don’t really know how fast shooting stars move as I’ve never been fortunate enough to see one."
    "But that’s beside the point."
    "So what {i}is{/i} the point, you ask? "
    "And why have you been pulled aside to stare up at a clear night sky instead of into the eyes of one of many love interests?"
    "The answer is simple."
    "I wanted to be alone with you."
    "Because even if it’s only for a little while, it is a moment I will cherish for the rest of eternity."
    "Please take the next ten seconds to think about what you love."

    $ renpy.pause(10, hard=True)

    scene goodnight1
    with dissolve2

    "Did you think of anything nice?"
    "Or are you one of those people who’s so bad at sinking your nails into your feelings that you let those ten seconds slip by without thinking of anything at all?"
    "You’re valid either way, I guess."
    "So long as you’re not out there literally stealing candy from children or, like...murdering anybody."
    "Actually, even if you are one of those people, you’re still probably kind of valid."
    "Children suck and many of them deserve to have their candy stolen."
    "The killing thing is a little bit more serious but, at the same time, there are probably people out there who have it coming. I guess {i}they’re{/i} the ones who aren’t valid."
    "By the way, that’s not me giving you the go-ahead to kill anybody. I’d prefer you didn’t do anything that dramatic."
    "But, if it helps, you can stay here."
    "Look, there’s even a girl sitting all by herself and looking sad."
    "Do you want to go cheer her up?"

    menu:
        "Yes":
            jump goodnightp2
        "No":
            "Why not?"
            "Is it because you think she’s mean?"
            "That she doesn’t like you?"
            "…"
            "Huh."
            "You’re not very good at reading people, are you?"
            "Either that or you’re too self-absorbed to think, even if only for a moment, about why certain people act the way they do."
            "What else is it you have trouble understanding?"
            "I want to help you."
            "This is all because I want to help you."
            "The song...the sky..."
            "All of it."
            "It’s all for you."
            "So the least you can do is try helping someone who shares the same point of view."
            "I ask you again."
            "Will you help her?"
            menu:
                "Yes":
                    jump goodnightp2
                "No":
                    "I see."
                    "Then-"
                    "Goodnight."
                    $ renpy.quit()

label goodnightp2:
    "Excellent."
    "Then-"

    scene goodnight2
    with dissolve

    "Oof. Looks like you’re a little too late."
    "If only I’d given you five seconds to think about what you love rather than ten."
    "Maybe then, you’d have gotten a chance to sit next to Maya before whoever it is that’s standing behind her."
    "Don’t worry, though."
    "I’m sure you’ll get the chance to feel her arms wrapped around you soon enough."
    "But “soon” is, of course, subjective."
    "For some people, those without a limited amount of time here like you and me-"
    "For some people, “soon” could mean hundreds...or thousands...or millions of years."
    "It would be a real shame if this all ended before you ever got to patch things up with her, wouldn’t it?"
    "Don’t worry, though."
    "There’s no way I’d ever hurt you like that."
    "But I guess this isn’t really the time to talk about when it is or isn’t acceptable to hurt others."
    "We’re on the last leg of the second beach update."
    "I wonder what wonders await us?"

    scene goodnight3
    with fade

    n "You realize {i}I’m{/i} the one who should hate {i}you{/i}, right?"
    n "I have no idea why you’re out here sulking like this, but you should at least head over to the bonfire before all of your friends think you don’t like them anymore."

    scene goodnight4
    with fade

    if bonus == True:
        m "Don’t pretend that you care about what my friends think of me."
        m "Why are you out here in the first place?"
        m "You have just as many friends as I do."
        m "You should be worrying about what {i}they{/i} think of {i}you{/i} more than what {i}mine{/i} think of {i}me.{/i}"
    else:
        m "...I don't like sand."
        m "It's coarse and...rough and...irritating."
        m "And it get's everywhere."
        m "Not like here."
        m "Here, everything is soft and..."
        m "And smooth..."

    play sound "static.mp3"
    scene goodnight5
    with flash
    stop sound

    if bonus == True:
        n "I’m looking for Sensei."
        m "Surprise, surprise."
        m "Didn’t I tell you to stay away from him?"
        n "Didn’t I tell you that I have no intention of doing that?"
        m "How unfortunate that your[school] didn’t implode during the day."
        m "Things would be so much better for me if you were trapped inside for that."
        m "Now, leave Sensei out of whatever it is you’re trying to do or-"
    else:
        n "This again? You know damn well how I feel about that scene, Maya."
        n "I don't want to hear it."
        m "But I have to say it. I need to get it out or-"

    scene goodnight6
    with dissolve

    n "Or what?"
    n "Are you going to run away again?"

    scene goodnight7
    with dissolve

    m "Where else would I go if I did?!"
    n "Fuck if I know! But I’m not {i}trying{/i} to do anything other than make up for time {i}I{/i} lost because {i}you{/i} decided to be an entitled little bitch!"

    scene goodnight8
    with dissolve

    if bonus == True:
        m "Entitled? For protecting someone that {i}chose{/i} me over an overbearing, thirsty cunt?"
    else:
        m "I don't like sand, Noriko."

    scene goodnight9
    with dissolve

    if bonus == True:
        n "Oh, {i}I’m{/i} the thirsty one?!"
        n "Me? The one who never made {i}any{/i} sort of move on him? Not you, who was already-"
    else:
        n "I don't care how you fucking feel about sand! Fight with me like a real girl!"

    scene goodnight10
    with dissolve

    m "He fucking chose me! Get over it!"
    n "Yeah. Sure. Just like he “chose” to abandon my sister and me."

    scene goodnight11
    with dissolve

    m "He {i}did.{/i}"
    n "Not the second time..."
    m "The second time, too."
    n "But who was it who {i}made{/i} him choose, Maya?"
    n "I was perfectly fine with how things were. I was happy. And you took that away-"
    m "You weren’t happy. None of us were. And none of us were ever {i}going{/i} to be."
    m "That’s why we’re still arguing about this fucking bullshit...however many years it’s been later."
    n "Almost five...but it feels a hell of a lot longer."
    m "Oh, fuck off. You have no idea what you’re even talking about."
    n "Maybe I don’t. But at least I’m not out here fucking crying despite having everything I could ever want."

    scene goodnight12
    with dissolve

    m "I don’t have anything..."
    m "Not anymore."
    n "Well don’t go blaming {i}me{/i} for Sensei not wanting to dance on your little puppet strings anymore."
    n "Oh...and that shit you said about me being some sort of “stalker?” Are you kidding?"
    n "How the fuck am I supposed to stalk someone when {i}I don’t know where they are?{/i}"
    n "You’re the one who refused to leave his side."
    n "And yeah, I get that you didn’t have anywhere else to go, but that doesn’t change the fact that from the moment you showed up, you were his favorite."
    n "You were closer to him than I ever was."
    m "And? What’s your point?"
    n "My {i}point{/i} is that the only reason you hate me is because I love him. Right?"
    m "…"
    n "Don’t you fucking go silent on me. That’s not fair."
    n "Like half of our class loves him and yet {i}I’m{/i} the one you treat like some sort of demon when I have never done {i}anything{/i} to you."
    m "But you would have."

    scene goodnight13
    with dissolve

    n "Yeah."
    n "I would have."

    if bonus == True:
        n "I would have fucked the daylights out of him if he wanted me."
        n "But guess what? He didn’t."
    else:
        n "Just like Anakin killed all of those younglings."
        n "You would have been toast, Maya. Fucking {i}toast.{/i}"

    n "So, would you mind telling me why you felt so pressured to get him away from me even though you two were apparently...in love, or however it is you made sense of that fucked up relationship?"

    scene goodnight14
    with dissolve

    m "I was {i}protecting{/i} him."

    if bonus == True:
        n "From what? Hugs? Kisses?"
        n "What were you afraid of?"
        n "I was a fucking normal little girl who had a crush on an older guy...A guy that I had known {i}way{/i} before you were even a part of his life."
        n "What did you have to protect him from, Maya? What were you so afraid of?"
    else:
        n "From what? Hugs?"
        n "He's the huggy boy, Maya. He loves hugs. They are in his name."

    scene goodnight12
    with dissolve

    m "Back then?"
    m "..."
    m "That you’d wind up pulling him back into a life he was trying to forget."
    m "That it would dredge up horrible memories and send him spiralling downward..."
    m "And that-"
    n "And that you wouldn’t be able to fix him?"
    m "That it wouldn’t be {i}possible{/i} to fix him."
    m "And all these years later, I’m protecting him from the same thing- just in a different way."
    m "There’s only so much sadness a person can take before they break into a million pieces."
    m "Your entire existence is a memento of those horrible times."
    n "And what does that make yours? A trophy of the times he’s yet to have?"
    m "No."
    m "It makes me nothing."
    n "…"
    n "Hah..."

    scene goodnight15
    with fade

    n "You’re not “nothing.”"
    n "You’re a selfish little bitch who always needs to have things her way or the whole world will fall apart."

    if bonus == True:
        m "And you’re a desperate slut who keeps sticking her nose where it doesn’t belong."
    else:
        m "And you're a big loser pants with stupid hair. Fight me."

    n "Says the girl who’s devoted herself to keeping the man she supposedly loves locked inside of a box."
    n "How do you expect him to grow if you won’t {i}let{/i} him?"
    m "I’ve tried."
    m "It didn’t work."
    m "And I implore you to stop trying as well or my hatred for you will get a bit heavier than just strings of harsh insults."
    n "Why did you have to take him away from me?"
    m "Why did you have to keep looking?"
    m "You should have just moved on with your happy little life instead of turning it into one that could very well erase his."
    n "Oh, yay. Another dramatic overreaction. Token Maya."

    scene goodnight16
    with dissolve

    m "I’m not kidding. Go back to the fucking old district and stay out of this. Your role ended a long time ago."
    n "Is the reason you’re so desperate about this {i}now{/i} because you know he won’t follow you again?"
    n "Or are you just afraid that Sensei accepting his past will make it so he doesn’t {i}need{/i} you anymore?"
    m "What a strange way of saying, “I’m sorry. I’ll stay out of it.”"
    n "I’m sorry you’re such a selfish bitch."
    m "Get the fuck away from me."

    scene clearnightsky
    with dissolve2

    "How interesting!"
    "That was a much more exciting conversation than you would have had with her, wouldn’t you agree?"
    "If that was you sitting there, you probably would have just leaned back and listened as she talked about the stars."
    "You’d find yourself dozing off...then awaken with your head in her lap as she lovingly strokes your hair."
    "You’d gaze up at her eyes in between yawns and think to yourself, “This is how Heaven would look if it truly existed.”"
    "And reflecting off of them would be a shooting star."
    "We’d finally know how quickly they move."

    if bonus == True:
        "Then, the night would end and you’d have passionate, rough missionary sex two or three times before finally falling to sleep."
    else:
        "Then, the night would end and you’d hug or something!"

    "Oh, what a life that would be."

    scene black
    with dissolve2

    "What a life it is in general."
    "Everywhere we go, we’re surrounded by little miracles."
    "Oh, look."
    "Here’s one now."

    scene goodnight17
    with dissolve

    r "Everyone! Attention, please!"
    r "Otoha and I would like to make an announcement!"
    o "Oh my God...please don’t scream it. This is still kind of...really embarrassing."

    scene goodnight18
    with dissolve

    r "Oh, come on! It’ll be easier doing it like this than going up to everyone one by one!"
    o "Can’t we just like...send out a group text or something?"
    r "Maybe for the girls who aren't here right now, but I’m afraid there’s no stopping me once I start an important announcement."
    o "There's no stopping you doing...literally anything ever."
    r "Just hang back and leave this part to me, new girlfriend!"
    f "Wait...what?"

    scene goodnight19
    with dissolve

    r "Everyone!"
    r "Otoha and I are officially a couple!"
    r "We will now be answering questions for the next ten minutes! But after that, we’re gonna go be cute somewhere or something!"

    scene goodnight20
    with fade

    no "I’ll be damned. That crazy lesbian actually did it."
    f "{i}*Sniff*{/i}"

    scene goodnight21
    with dissolve

    no "Futaba?"
    r "Now, if anyone has any-"
    r "Wait, Futaba! What’s wrong?"
    f "I’m just..."
    f "So happy for you..."
    o "Rin, you should-"
    r "I know."

    scene goodnight22
    with dissolve2

    r "Thank you so much."
    r "For always being there for me..."
    r "For helping me find the confidence I needed to actually follow through with this..."
    r "And for assuring me that Otoha didn’t think I had a penis, even though I wound up bringing that up anyway."
    no "Excuse me, Rin. But I would also like to join in on this if you do not mind."

    scene goodnight23 with fade

    a "Awwwww...I’m so happy for them..."
    ay "They’ll make a cute couple."
    ay "I would have said yes if I was Otoha, too. Especially after Rin’s valiant defense last night."
    sa "Did...you two know that Rin was interested in girls?"

    scene goodnight24
    with dissolve

    ay "Did...did you not?"
    sa "I had no idea! This is a huge surprise for me!"
    a "That’s...actually kind of impressive..."

    scene goodnight25
    with fade

    o "Uh...you guys doing okay over here?"
    no "We’re bonding."
    f "I’m so...proud of you, Rin..."
    f "I knew...that one day...you’d finally get-"

    scene goodnight26
    with dissolve

    f "That you’d get..."
    no "..."
    o "Uh..."

    scene goodnight27
    with dissolve

    f "Really?...Now?..."
    no "Now what?"
    r "…"

    scene goodnight28
    with dissolve

    o "Dude!"
    f "Hah..."

    scene black
    with dissolve2

    "There are miracles everywhere."
    "But for every single thing that someone out there wants, there is another who wants the opposite."
    "Every up comes from a down. Every smile comes from a frown."
    "It’s all born from nothing."
    "And so we’ll float now in the opposite direction, where things are less joy{i}ous{/i} or more joy{i}less.{/i}"
    "Where it doesn’t matter how hard anyone smiles because there is an underlying misery in everything that makes even the best moments in life a precursor to disaster."

    scene goodnight29
    with dissolve2

    "There is just so much of it."

    mo "Do you ever wish you could just reroll life, Kendo Princess?"
    t "I’m not sure if I understand."
    mo "You know how sometimes you’ll get a bad draw in something, but have some sort of ability or...chance to just undo it and start over?"
    mo "Sometimes, I wish I could do that. And...be born as someone else."
    mo "Someone with less...feelings. Or someone...cooler."
    mo "Someone who likes different things or is...prettier."
    mo "There’s so much about me I wish I could just...undo."

    scene goodnight30
    with dissolve

    t "I see."
    t "Personally, I would prefer that you remain the person you are."
    t "It is not someone else who stays up late into the night, teaching me the differences between sorcerers and wizards."
    t "It is not someone else who tries my new recipes and remains honest and impartial, even when they are entirely inedible due to snake venom."
    t "The person who does all of that is you."
    t "I would not change anything at all."
    mo "Thanks, Tsuneyo."
    mo "If we’re ever able to leave Kumon-mi again, you should come with me to Ireland."
    t "The Isle of Emeralds. It sounds sharp."
    mo "We wouldn’t have to stay or anything."
    mo "I just..."
    mo "I kind of wish I had my dad right now."

    scene black
    with dissolve2

    "I suppose calling conversations like that a disaster is a bit of an exaggeration when ones just like it are happening all around us every day."
    "And so why don’t we take a look at some that are a little more disheartening?"

    play sound "static.mp3"
    scene goodnight31 with flash
    stop sound

    "Self deprecation comes in all sorts of interesting flavors and colors."
    "The first example we’ll look at is that of a girl who has given up on the idea of ever being more than an empty container."
    "And while she wishes it was as simple as waiting to be filled, her container comes equipped with a carved out bottom, incapable of ever returning to its “correct” form."
    "Whatever that correct form is."
    "So she waits in the room of a man who is elsewhere, hoping that he’ll show up and tell her it’s okay to be empty."
    "And that he is empty himself."
    "And she will find solace in the fact that she is not alone in her grief."
    "In that whoever or whatever it was that robbed her of the bottom of her container is nothing but a blip on the radar now."
    "But that man never comes."
    "And she grows tired of waiting."

    if bonus == True:
        play sound "static.mp3"
        scene goodnight32 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown with flash
        stop sound

    "Meanwhile, another girl in another room drowns her sorrow in the only thing she’s able to feel at this point."
    "She keeps the volume loud enough so that anyone who enters will be able to hear what’s happening behind a closed door."
    "She wants to be found because she wants to be seen."
    "Any amount of attention or sympathy or empathy or {i}anything at all{/i} would make her remember that {i}she is alive.{/i}"
    "She doesn’t mind being seen in a dim red light while the rest of her acquaintances dance under the moon- as any light is better than no light at all."
    "No one ever finds her."

    if bonus == True:
        "And as she climaxes to a film of two people she’ll never meet connecting with one another, all she wishes is to connect herself."
        "But then she cuts her wire in two because connections are scary."
    else:
        "All she wishes is to connect with anyone."
        "And it's a shame she never will."
        "Especially not in this version of the game."

    play sound "static.mp3"
    scene goodnight33 with flash
    stop sound

    "All types of people in all types of places hate who they are or what they were or what they think or how they live."
    "This entire world is shrouded in misery and regret, and we have one more example of that here, miles and miles away from where we were just moments ago."
    "And while it’s easy to look at the picture in front of you and assume why this woman is crying-"
    "The real answer may very well be a bit more complicated than that."

    play sound "static.mp3"
    scene goodnight34 with flash
    stop sound

    "It might be {i}much{/i} more complicated than that."

    tdtl "tev albp bsbovqefkd exsb ql eroq pl jrze"
    sar "[[DIALOGUE CENSORED DUE TO UNIMPORTANCE. SARA SAKAKIBARA IS A SIDE CHARACTER.]"
    ## WHY NOW?! THIS IS SUPPOSED TO BE OVER!

    play sound "static.mp3"
    scene happy4 with flash
    scene happy5 with flash
    scene happy6 with flash
    scene happy7 with flash
    scene goodnight35 with flash
    stop sound

    os "Babe? Sorry I’m back late, but the girls decided to just leave their bonfire thing burning."
    os "I’ll finish packing up all of your stuff out here, but if you could bring whatever we have in the bedroom out, it would be a big help."
    os "No idea why you always pack so much even when we know we’ll only be gone for a couple days...but this {i}is{/i} what I signed up for, I guess."
    os "…"
    os "…"
    os "…"

    scene goodnight36 with dissolve

    os "Wakana?"

    scene goodnight37
    with fade

    os "Is everything okay?"

    play sound "static.mp3"
    scene frown with flash
    scene smile with flash
    scene frown with flash
    stop sound

    "No."
    "It never is."
    "But we learn to accept this as life moves on because-"
    "Actually."
    "I don’t know."
    "Why {i}do{/i} we accept this?"

    play sound "static.mp3"
    scene goodnight38
    with flash
    stop sound

    "We all find ourselves back in bed each night, thanking God or a friend or a piece of media for being the drug we need to make it through the day."
    "But when there is so much happening behind the scenes, it’s easy to forget that there are people out there having a much harder time."
    "So we wait."
    "And we wait and we wait and we wait and we wait-"
    "For something to make us feel whole again."
    "Sometimes, you have to work for it."
    "But sometimes-"

    play sound "slidedoor.mp3"
    scene goodnight39 with dissolve

    "It comes to you instead."

    scene goodnight40
    with fade

    s "Niki?"
    ni "Can I stay here tonight?"
    s "I mean...sure."
    s "But don’t you-"
    ni "I just had a little more free time than I thought."
    ni "That’s all."
    s "…"

    scene black
    with dissolve2

    "Life is miserable."
    "But sometimes, it’s not."

    scene goodnight41
    with dissolve2

    ni "Are you okay?"
    s "Yeah."
    s "Just thinking."
    ni "About what?"
    s "I’m not really sure."
    ni "Fun."
    ni "Do you have a t-shirt I can borrow? I didn’t bring my bag."
    s "I mean, yeah...but..."
    s "This is a pretty dramatic departure from how we were this morning."
    s "And...every day before that."
    ni "Yeah."
    ni "..."
    ni "Yeah, I guess it is."

    scene black
    with dissolve2

    "Goodnight."

    $ renpy.end_replay()
    $ secondbeach17 = True

    "………"
    "……"
    "…"

    jump secondbeach18

label secondbeach18:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
o "Woah! Where did you come from?"
    r "Right next to you."
    o "We’re...really close all of a sudden."
    r "Cause I wanted to be really close to you."

    scene tryagain32
    with dissolve

    o "Well, I mean...since I guess we’re like...you know...dating now or whatever..."
    o "It’s okay."
    o "Just...take it slow, please. I don’t want to jump right into-"

    scene tryagain33
    with dissolve2

    r "Chu~"
    o "Mmf!"

    scene tryagain34
    with dissolve

    r "Sorry, were you saying something?"
    o "You..."
    o "Um."
    o "You are very...very bad at listening..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene tryagain35
    with dissolve2

    o "So..."
    o "This is...gonna be a thing we have to tell people about, isn’t it?"
    r "Yeah..."
    r "If I wake up in ten minutes and this was all some sort of crazy dream, I’m going to kill myself."
    o "Please don’t say things like that. As your girlfriend, I’m now obligated to care even more."
    o "I think that’s how these things work, at least. I could be wrong."

    scene tryagain36
    with dissolve

    o "But I’m...excited! This was-"

    scene tryagain37
    with dissolve

    o "Wait, why are you crying? Did I fuck up already?"
    r "No...Of course not..."

    scene tryagain38
    with dissolve

    r "I’m just...really happy..."
    o "…"
    r "…"

    scene tryagain39
    with dissolve

    o "Good."
    o "I hope you can stay that way."
    r "…"
    o "…"
    o "The moon is beautiful tonight."

    scene black
    with dissolve2

    "Sometimes, good things happen."
    "Not all the time...but if you try enough, something is bound to work eventually."
    "This was just one of those nights."
    "So revel in it while you can because, soon enough, the world will swell with misery once more."
    "Then twice more."
    "Then thrice."
    "Over and over and over again, the clock goes around in circles."
    "It ticks, it tocks. Repeats. Resets."
    "Because time itself’s eternal."
    "Wherever you are, I hope you’re happy."
    "Because God knows that I am not."

    stop music

    "///////////////////////STOP MUSIC"
    "///////////////////////…"
    "///////////////////////…"
    "///////////////////////…"

    play music "goodnight.mp3"

    "///////////////////////PLAY “GOODNIGHT.MP3”"

    $ renpy.end_replay()
    $ secondbeach16 = True

    jump secondbeach17
...
```