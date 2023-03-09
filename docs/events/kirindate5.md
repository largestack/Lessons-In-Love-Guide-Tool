# Long and Hard
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindate5&go=Go)



## Event preconditions
✅Kirin love greater than or equal to 5

✅Event "[Kirin: Partners in Crime](./kirindate1.md)" is completed (event=kirindate1)

✅Event "[Main: See You in the Morning](./beachvacation16.md)" is completed (event=beachvacation16)

✅kirinnumber equal to True (unknown variable)



## Next events
* [Kirin: Politics! Pleasure! Ponies!](./kirindate10.md)

## Event properties
* ID: kirindate5
* Group: Kirin
* Triggered by label: callkirinnight
* Triggered by branch label: callnight

## Event code
File: \game\KirinEvents.rpy
Code:
```python
...
label kirindate5:
    play sound "phonebeep.wav"

    if ayanelust10 == True and bonus == True:
        "I tap on Kirin’s name in my phone with a slight bit of hesitation."
        "The two of us haven’t really had any...in-depth conversations since what transpired on the beach and, frankly, I’m not really sure what to make of it."
        "Don’t get me wrong, from a sheer sexual standpoint, I’m all about it."
        "That was one of the best things to happen to me since spawning in Kumon-mi."
        "But the effect it had on Ayane was not only surprising but a bit horrifying in a sense."
        "I’ve never seen her look that way before."
        "Kirin’s not just...planning on ignoring that, is she?"

    else:
        "I tap on Kirin’s name in my phone and wait for her to answer..."

    "………"
    "……"

    play sound "phonebeep.wav"

    ki "Hellooooo Sensei~"
    ki "You're calling 'cause you want to see me, right?"
    ki "Do you really miss me that much?"
    s "Yes. I miss you horribly."
    ki "Aww, you’re so cute."
    ki "Wanna come meet up somewhere?"
    ki "My parents are home right now but I can just lie and tell them I’m going out with friends or something."
    s "Am I not actually your friend?"
    ki "Hehehe~ I don’t know. What are you to me, Sensei?"
    s "…"
    ki "…"
    s "I’ll meet you around the corner from your apartment."
    ki "Kay kay! See you soon~"

    play sound "phonebeep.wav"

    "I hang up the phone and slide it back into my pocket."

    scene black
    with dissolve

    "What {i}am{/i} I to Kirin? Because obviously, 'friend' isn’t the right word."
    "At times, it almost feels like I’m being manipulated."
    "But hey, being manipulated isn’t always bad as long as the relationship is mutually beneficial."
    "Sometimes, it’s best to let yourself be manipulated in order to progress."
    "So, if that {i}is{/i} what she’s doing, she can carry on."
    "And I’ll carry on as well."
    "………"
    "……"

    play music "pianomelancholy3.mp3" fadein 10.0
    scene kirinnightdate1
    with dissolve

    "Kirin and I meet up under the cover of a nearby office building that we’ve visited once or twice before."
    "She’s a strange girl, but she’s smart when it comes to keeping things discreet."
    "It’s late enough that whatever office this is has already closed down. And since it’s not even facing the street, there isn’t really anyone who would ever see us here."
    "Well, unless there’s late-night cleaning staff or something along those lines."
    "But who really cares, right?"
    "We’re not doing anything wrong."
    "Yet."

    ki "No [niece] tonight?"
    s "No sister tonight?"
    ki "I asked you first~"
    s "You did. But I think the fact that I’m here is enough to prove that there is, in fact, no [niece] tonight."
    ki "Hmm, yes. Yes, I suppose it does."
    ki "Karin {i}is{/i} home tonight, so I guess I'm not completely devoid of a sister."
    ki "She’s having dinner with our parents, though."
    s "Shouldn’t you be joining them as well, then?"

    scene kirinnightdate2
    with dissolve

    ki "Shouldn’t you be joining your [niece]?"
    s "She’s a big girl. She’ll be fine eating on her own."

    "If she’s even cooking right now."
    "I didn’t bother to ask but it wouldn’t surprise me if she was."
    "Oh well. I guess there will be leftovers either way."

    ki "Ooooh, that means I’m a big girl, too. Doesn’t it?"
    ki "You know, since I’ll wind up eating by myself tonight after we finish doing...whatever it is we’re doing here."
    ki "Which is...what exactly? What {i}are{/i} we doing here?"
    s "Just hanging out like two normal people who definitely aren’t hiding from anyone else."
    ki "You really know how to woo a girl, don’t you?"

    if bonus == True:
        ki "Let's fuck, Sensei. Right up against the vending machine."
    else:
        ki "Hug me up against the vending machine, but don't press your body too closely against mine or I'll get angry."

    s "No way. You have no idea where that thing’s been."

    scene kirinnightdate3
    with dissolve

    ki "It literally hasn’t moved in like seven years."
    s "Why have you been keeping tabs on an office vending machine for seven years?"

    scene kirinnightdate4
    with dissolve

    ki "Maybe I’m involved in a secret relationship with someone who works here?"
    s "Right. So you’ve been sneaking around and engaging in secret relationships with salarymen for seven years."

    scene kirinnightdate5
    with dissolve

    if bonus == True:
        ki "Obviously not. I’m a faithful, innocent virgin who’s promised you her chastity in exchange for whatever that one thing I asked for was."
        s "Delinquency, I believe."

        scene kirinnightdate2
        with dissolve

        ki "Right. Delinquency."
        ki "Maybe you should skip[school] with me one day and deflower me on my sister’s bed? "
        ki "That would be fun, right?"
        s "Wow, you really know how to woo a guy, don’t you?"
        ki "Ohhhh, using my lines against me now?"
        s "It appears that way."
    else:
        ki "Hey. His name is Tony and he is a nice guy."
        s "Tony can go suck an egg for all I care."
        ki "Are you saying you care about me, Sensei."
        s "Yes. But more than that, I {i}don't{/i} care about Tony."

    scene kirinnightdate6
    with dissolve

    ki "Fine by me."
    ki "I mean, the two of us aren’t really that different, are we?"
    ki "We’re both just in this to have a good time."

    if ayanelust10 == True and bonus == True:
        s "I know that’s the case for {i}me{/i}, but is that really how it is for you?"

        scene kirinnightdate2
        with dissolve

        ki "What, was holding your cock while you fucked Ayane’s slutty, rich-girl pussy not enough for you to realize that I maybe-sort-of like that kind of stuff?"
        ki "Are you trying to tell me that you would have just stood there and watched if you walked in on me with another guy?"
        s "Probably. Not really into that multiple males, one female sort of thing."

        scene kirinnightdate7
        with dissolve

        ki "You..."
        ki "You really wouldn’t care if some other guy fucked me?"
        s "It’s not really my place to care about that."

        scene kirinnightdate8
        with dissolve

        ki "Well it fucking should be!"
        ki "I promised you my virginity, remember?!"
        ki "I obviously want you to fucking care about things like that!"
        ki "Is it so much to ask to just be looked at the same way as everyone else?"
        s "It’s just, that mentality contradicts your whole “Life is all about having fun” outlook."
        ki "So what, I need to back up every single outlook I have with logic and reason now? I can’t just think stuff because that’s what I want to think?"

        scene kirinnightdate9
        with dissolve

        ki "Fucking annoying. "
        ki "Just leave. I’m not in the mood to hang out anymore."
        s "…"
        ki "…"
        s "Well, if that’s what you want-"

        scene kirinnightdate8
        with dissolve

        ki "See?! This! This is what I hate!"
        ki "Of course I don’t want you to leave! I just..."
        s "...You just what?"

        scene kirinnightdate10
        with dissolve

        ki "I don’t know. "
        ki "People normally freak out when I start yelling at them."
        ki "No one really sits there and just...lets it happen. This is new for me."
        ki "Lots of new things are happening to me all of a sudden."
        ki "It’s...weird."
        s "If it’s any consolation, a lot of new things are happening to me too."
        s "Like that whole walking in on Ayane and me thing. That was new."

        scene kirinnightdate11
        with dissolve

        ki "But it was fun, right?"
        ki "Looked like you felt really, {i}really{/i} good."
        s "It was pretty amazing, I won’t lie."
        s "But I don’t think Ayane felt the same way."
        ki "You sure about that? "
        ki "Maybe it was just biological or whatever but she was literally dripping all over my hand."

        scene kirinnightdate12
        with dissolve

        ki "I mean...it’s only natural for her to be so turned on when she has a cock as big as yours inside of her."
        ki "I was the same way just from watching."
        ki "But, of course, you wouldn’t know that because you didn’t actually do anything to me."
        s "Sorry. I was too busy dealing with the psychological trauma you inflicted on my [niece]’s best friend."
        ki "Nuh-uh. You were busy filling her with your cum. Liar."
        ki "Besides, do you really think she’s traumatized from a little thing like that?"
        ki "Girls have threesomes all the time. It’s totally normal."
        s "Yeah but normally the third person is invited."
        ki "I took the fact that you both ignored my existence as you stormed through the door as an invitation."
        ki "Next time, tell me you don’t want me there if you don’t want me there."
        s "Why don’t {i}you{/i} tell me what you were doing in my room all by yourself?"
        s "That’s what I want to know."

        scene kirinnightdate13
        with dissolve

        ki "Do you?"
        ki "Well that just sucks, doesn't it?"
        s "Why? What do you mean?"
        ki "Because I don’t have to tell you shit."
        ki "You’re not my boyfriend. You’re just the guy I’ve chosen to take my virginity."
        ki "So sorry if you weren’t entirely satisfied with having two adorable girls service your monster-cock while everyone else played fucking beach-volleyball or whatever."
        ki "I’ll make sure to submit my next threesome application with your secretary."
        s "I just want to know why you do the things you do. That’s all."
        ki "Of course you do. Because I’m weird, right?"
        ki "Because I’m one of those diaries that come with the built-in lock thingy. "
        ki "And all you’re able to do is fit the tips of your fingers in through the tiny, {i}tight{/i}, little cracks and rip out one page at a time instead of reading the whole thing."
        ki "But without the key, you’ll never know what any of it really means. Right?"
        ki "Do you want my key, Sensei?"
        ki "Do you want to look into my diary?"

        scene kirinnightdate14
        with dissolve

        ki "Or do you just want to fuck my tiny, {i}tight{/i}, little pussy?"

        "I can’t tell if I’m intimidated or aroused right now."
        "So yeah, it’s basically a normal night with Kirin. Albeit a significantly less reserved one. "
        "Which is not to say that she’s ever reserved in the first place (She’s not). But even this is more aggressive than normal."
        "She must really despise confrontation..."

        scene kirinnightdate15
        with dissolve

        ki "Hah...Of course you won’t answer that question. It’s too hard."
        ki "I’ll just answer it for you, kay?"
        ki "You want both."
        ki "You want to fuck me and “fix” me at the same time."
        ki "It’s what you want to do with everyone. "
        ki "But things don’t work that way."
        ki "You can only have one or the other."

        scene kirinnightdate14
        with dissolve

        ki "Do you plan on fixing {i}everyone{/i}, Sensei? Even the ones who don’t need it?"
        ki "Or do you just want to push your way inside all of us and see how our faces light up as you fill us with your cum?"
        s "Kirin..."

        scene kirinnightdate16
        with dissolve

        ki "I like fixing things too, you know."
        ki "I’m just not very good at it, I guess."
        ki "Friends will come to me with problems and I’ll give them the advice I think is best. I’ll tell them what I would do in their shoes."
        ki "But then they forget all about it if it’s not what they want to hear and just go ask other people until they finally get an answer they’re satisfied with."
        ki "Why bother asking anyone for help if you’re only looking for validation? Right?"

        scene kirinnightdate15
        with dissolve

        ki "Sorry. I’m rambling."
        ki "You’re all frozen and stuff so I figured I’d just take the lead while you daydream about my virginity."
        s "I’m not frozen, just confused."
        s "I still don’t understand what any of that has to do with Ayane."
        s "I really just want to know what compelled you to break someone else in exchange for your own satisfaction."

        scene kirinnightdate16
        with dissolve

        ki "I want you to think {i}long{/i} and {i}hard{/i} about that last sentence, Sensei."
        ki "Isn’t that one more thing that the two of us have in common?"
        ki "Breaking others for our own satisfaction?"
        ki "If you think you’re going to be able to do all of these things without any sort of consequences, you’re wrong."
        ki "You can't {i}fix{/i} anything. You can only break things."
        ki "So what’s the problem if I do the same every once in a while? It gets both of us off, doesn't it?"

        scene kirinnightdate6
        with dissolve

        ki "And hey! Maybe I’ll even be lucky enough to be the one you finish inside of next time."
        ki "That would be swell. It’s not like I’ve already offered myself to you or anything. "
        ki "And it’s not like I literally followed you behind a bathroom just to ask if I could jerk you off on the beach."
        ki "So just keep fucking other girls. It’s cool. I’ll be good."
        ki "I’ll wait my turn."

        scene kirinnightdate16
        with dissolve

        ki "Anyway, rant over I guess."
        ki "Sorry for the thing with Ayane. Hope she’s not as bummed out as you are about it."
        ki "My bad."
        s "I’m not {i}bummed out{/i}. I just wish you’d think about other people a little more."
        ki "I’ll start doing that the second you do."
        ki "Until then, let’s just keep having fun. Okay?"
        s "…"
        ki "…"

        "Kirin and I stand there staring at each other for what feels like hours."
        "But despite how hard I try to siphon some emotion out of those green eyes, I get nothing."
        "She’s just blank."
        "Wait."
        "No."
        "She’s not blank."
        "She’s pitch black."

    else:
        "Are we really, though?"
        "Something about the way Kirin acts still makes me unsure about that."

        if bonus == True:
            "Sometimes, it feels like a complete facade. And others, I feel like she wants me to just take everything she has by force. "

        "I don’t understand her at all."
        "Are the two of us really the same in her eyes?"

    scene kirinnightdate17
    with dissolve

    ki "Oh! Thanks for never asking for money for letting Karin and me crash in that inn, by the way."
    ki "She wouldn’t shut up about how kind it was for the entire ride home. I almost jumped out of the bus."
    s "To be fair, I didn’t really pay either. That was all Ayane."

    scene kirinnightdate18
    with dissolve

    ki "Of course it was. "
    ki "Fucking bubble-wrap queen of Kumon-mi."
    s "That’s an absolutely horrible nickname."
    ki "Blame her father’s absolutely horrible invention."
    ki "Still cool, though. Being that rich, I mean."
    ki "I don’t even know what my dad does."
    ki "Hell, this could be his office building and I wouldn’t even know it."
    s "Are you not on good terms with your parents or something?"

    scene kirinnightdate6
    with dissolve

    ki "Nothing like that. Our terms are fine. I just try not to get too involved, I guess."
    ki "Which might be why it always seems like I’m trying to get involved elsewhere."

    scene kirinnightdate4
    with dissolve

    if bonus == True:
        ki "Like inside of your pants~"
        s "Thank you, Kirin. For reminding me of your strangely high sex drive despite being a literal virgin."
        ki "Literal, yes. But I can assure you my mind is quite corrupt already."
        s "Oh I’m well aware of that. You talked about porn the first time I came over."
        ki "I’ll talk about it again right now if you want. "
        ki "Wanna compare browser histories? I think you’ll be surprised by some of my tastes."
        s "Honestly, I don’t think anything about you would surprise me at this point."
    else:
        s "Like at a zoo?"
        ki "{i}Exactly{/i} like that, Sensei."
        s "That is so interesting."

    scene kirinnightdate12
    with dissolve

    ki "Can I take that as you thinking I’m interesting?"

    if bonus == True:
        s "Interesting is an understatement."
        s "I’d be down to write a thesis paper with you as the subject if I actually cared anything about actual work."
        ki "That sounds boring. Let’s just make out instead."

        "As much as I'm enticed by the offer to stay here and make out with Kirin, I feel like I should probably be leaving right about now..."
        "It’s already late and I really don’t want to have to walk home in the pitch black."
        "Is that a selfish reason? Sure. But it’s not like Kirin should be out right now either."
        "Her sister and her parents are probably still eating and talking about their day and...other family stuff, I guess."
        "She has no place out here next to me."

        s "We can make out next time. I need to start heading back."

        scene kirinnightdate3
        with dissolve

        ki "Really?"
        ki "Even though I studied in preparation for you to stick your tongue down my throat?"
        s "You...studied how to make out?"
    else:
        s "Yes. Just make sure to study up on the needs and requirements for every single animal there. We don't want any of them getting hurt."
        s "Being a zookeeper is a tough job."

    scene kirinnightdate19
    with dissolve

    ki "Well, I obviously don’t want to suck at it..."
    s "That’s...kind of adorable."
    ki "I know it is. I’m an adorable girl. "
    ki "You should say that more."
    s "I will do my best to remember..."

    scene black
    with dissolve2

    "Kirin and I part ways with an extremely brief goodbye."
    "I watch her take her phone out of her pocket and start typing out a message or social media post the second we part ways."
    "I hope she isn’t writing anything about me."
    "I feel like tonight’s conversation could have gone a little better..."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirindate5 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "{i}Sensei eats a hot dinner when he returns home!{/i}"
    "{i}Kirin does not!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirindate10:
...
```

## Code that triggers this event
File: \game\KirinEvents.rpy
Code:
```python
...
label callkirinnight:
    if kirindate1 == False:
        play sound "phonebeep.wav"

        "I tap on Kirin's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        ki "Hihi~ How can I help you, Sensei?"
        s "Hey, Kirin. I was wondering if you'd want to meet up tonight?"
        ki "Tonight? You should have told me sooner. I already made plans with some friends."
        s "Damn. And you can't get out of them?"
        ki "Sensei, are you really asking me to bail on everyone {i}just{/i} so I can hang out with you?"
        s "Yes. Yes, I am."
        ki "Hmm...Well, I {i}do{/i} like you...But I don't know if I like you {i}that{/i} much."
        ki "How about you just call me a little earlier next time and I'll drop everything so we can hang? Cool?"
        s "Yeah, that's fine. Have fun with your friends tonight."
        ki "I will certainly try~"

        play sound "phonebeep.wav"

        "Looks like Kirin is busy tonight. I guess I'll have to call someone else."
        jump callnight
    if kirin_love >= 5 and kirindate1 == True and beachvacation16 == True and kirindate5 == False:
        jump kirindate5
...
```