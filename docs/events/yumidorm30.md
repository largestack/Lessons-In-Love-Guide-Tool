# Walls Too Thick to Hear Through
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumidorm30&go=Go)



## Event preconditions
✅Yumi love greater than or equal to 30

✅Event "[Yumi: Where the Sidewalk Ends](./streets30.md)" is completed (event=streets30)

✅Event "[Yuki: Rule #1](./yukidate1.md)" is completed (event=yukidate1)



## Next events
* [Yumi: Tech Support](./yumidorm35.md)
* [Main: Annabel Lee](./day280.md)
* [Yuki: Better Off Alone](./yukidate5.md)

## Event properties
* ID: yumidorm30
* Group: Yumi
* Triggered by label: yumidorm
* Triggered by branch label: yumidorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label yumidorm30:
    play sound "knock.mp3"

    "I knock on Yumi’s door and wait for-"

    y "Go the fuck away! I’m busy."
    s "…"

    "I knock on Yumi’s door and she immediately answers."

    s "Busy doing what?"
    s "Are all of your clothes on?"
    y "Of fucking course they are! But that shouldn't make a-"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Cool. Then that means I can come in."
    y "What the fuck do you think you’re doing?! I just said no!"

    "I open Yumi’s door and make my way into the room, which she definitely wanted me to do."

    scene yumidormnotebook1
    with dissolve

    y "Get out!"
    s "Are you...studying?"
    s "If I knew it was something this boring, I really would have left you alone."
    y "Cool! Bye!"
    s "…"
    s "So what are you studying?"

    scene yumidormnotebook2
    with dissolve

    y "A bunch of different shit Chika told me about since she knows I’m trying to get a job."
    y "Also, what happened to this being too boring to stick around for?"
    y "You know where the door is, right? Sure had no trouble finding it on the way in."
    s "If it’s something unrelated to actual education, I’m totally fine with helping you study."
    s "What did Chika tell you?"

    scene yumidormnotebook3
    with dissolve

    y "You should probably at least {i}try{/i} to sound like a good teacher every once in a while."
    y "Saying you’ll help me study with everything except[school] is like..."
    y "I don’t even know what it’s like. But it’s stupid."
    y "Now fuck off."
    s "Can I see the notebook?"

    scene yumidormnotebook1
    with dissolve

    y "No! You can’t see the fucking notebook!"
    s "Why not? You’re not secretly writing me another love note, are you?"

    scene yumidormnotebook4
    with dissolve

    y "Love note?! I never wrote you a fucking love note!"
    y "All I said was that you aren’t the worst thing ever!"
    y "Which was a total lie by the way, as I’m pretty sure you can tell right now!"
    s "You know if you keep yelling, someone is going to find out I’m in here, right?"

    scene yumidormnotebook5
    with dissolve

    y "Shouldn’t {i}you{/i} be more worried about that than me? The fuck do I have to lose if someone finds out about this?"
    y "Chances are they probably heard me screaming at you to not come in anyway."
    s "Can I sit down?"

    scene yumidormnotebook6
    with dissolve

    y "Sure, Sensei. I’d love that. In fact, why don’t you walk outside and take a seat on the curb? I’ll be down to meet you in just a few moments."
    s "I meant on the bed."

    scene yumidormnotebook7
    with dissolve

    y "The second you sit on my bed is the second I decide to throw myself into a volcano."
    s "Bad idea. I can’t imagine there are many job openings inside of volcanoes."

    scene yumidormnotebook8
    with dissolve

    y "Can you get out of my room now? Your jokes fucking blow and you’re distracting me from doing something that {i}you{/i} suggested I do in the first place."
    s "Let me help, for real this time."
    s "What sort of stuff did Chika tell you?"
    y "A bunch of shit that you never did. Like how important it is to smile and what an iDeCo is."
    s "I...don’t think you need to be worrying about iDeCo’s for a part time job. "

    if bonus == True:
        y "Maybe I don’t. But who do you think I should believe: some deadbeat who spends his entire work day staring at boobs or some girl who’s working her ass off to support her sister?"
    else:
        y "Maybe I don’t. But Chika seems a lot more trustworthy than some asshole like you."

    "Damnit, Chika. Why do you have to be so good?"
    "You’re making me look bad."
    "I mean, technically {i}I’m{/i} making me look bad."
    "But you’re not helping at all."

    s "Okay, fine. Whatever. I’m sure that even bringing up some term like “iDeCo” will make you look good in an interview, so we won’t cross it off for now."
    y "I’m more worried about the fuckin’ smiling part. I have no idea how to do that."
    s "You just smiled at me like a minute ago when you told me to go sit on the curb."

    scene yumidormnotebook9
    with dissolve

    y "I did?!"
    s "Yes. I remember distinctly because it hurt me."
    y "Maybe that’s the trick then? Maybe I just need to think of you every time I want to smile?"
    s "I know that you meant that in an insulting way, but it sounded very cute and I am no longer hurt."

    scene yumidormnotebook10
    with dissolve

    y "Ew! Gross! Please don’t even joke about that meaning what...you thought it sounded like. Or something."
    y "Fuck you."
    s "That aside, what else do you have in there?"
    s "Did Chika give you any ideas on more places to apply?"

    scene yumidormnotebook11
    with dissolve

    y "Well...she suggested a few places from the mall. But I’ve been caught stealing there before and I don’t know if I’m allowed back."
    s "I can’t imagine they keep track of everyone who’s stolen from them before. That sounds like way too much work."
    y "Probably not, but like three of the places she said I should apply to have caught me. And I don’t want word gettin’ around and shit."
    s "Just how many times have you stolen things from the mall?"

    scene yumidormnotebook12
    with dissolve

    y "Uhh...I don’t know. A lot?"
    y "I’m a fucking [teenage]girl. Even if I wasn’t a delinquent, I’d be stealing shit from the mall. Literally everyone does it."
    s "Well then there you go. It’s not a big deal after all."

    scene yumidormnotebook13
    with dissolve

    y "Oh shit. Maybe you’re right?"
    y "And like, there are a lot of fucking stores at the mall. There has to be at least one there that would take me. Right?"
    y "I’ve just gotta walk in, smile, namedrop the iDeCo and I’m in. "
    s "I’m still not sold on the iDeCo thing, but yeah. We can try that."
    y "We? You’re coming with me again?"
    s "Of course. I basically consider myself your manager at this point."
    y "Shitty fucking manager. All you do is stalk me and look at me like I’m some sort of meal or something."
    s "I can’t imagine you would taste good. You are pretty fucking malnourished, Yumi."

    scene yumidormnotebook1
    with dissolve

    y "Yeah, well you’re mal-whatever too, asshole! You would probably taste like fucking...stale bread and foot fungus!"
    s "You have such a way with words. I suggest repeating that same phrase during your next interview."

    scene yumidormnotebook14
    with dissolve

    y "Hah...are we done here?"
    y "Just asking me the shit I wrote down already isn’t exactly helpful."
    y "And now that we figured out that thing about the mall, I think it’s safe to say you’re going to be useless for the rest of the night."
    s "New idea- how about we stop doing job stuff all together and talk about something else?"
    y "The last time we did that, you sat there and watched me eat ice cream for ten minutes."
    y "Can’t say I’m excited to live through that level of trauma again."
    s "Thankfully, there’s no ice cream around. "
    s "But if you wanted to maybe close your eyes and drink from one of those water bottles-"

    scene yumidormnotebook1
    with dissolve

    if bonus == True:
        y "Stop with this weird fucking fetish of watching me eat and drink stuff! It doesn’t make any sense!"
    else:
        y "Stop wanting to watch me eat and drink stuff! It's weird!"

    stop music fadeout 25.0

    s "Then stop trying to push me away and actually talk to me for a little while."
    s "If you’re not going to be serious, neither am I. "
    s "But if you can hold a conversation without jumping down my throat, maybe we can actually get somewhere?"

    scene yumidormnotebook15
    with dissolve

    y "…"
    s "…"
    y "I want to believe you, but you kind of just fucking waltzed in here even though I told you not to."
    y "Why the fuck should I humor you if you won’t even be chill enough to respect a wish as simple as “don’t open the door.”"
    s "Because, at this rate, you will literally never open the door for me. Or anyone, really."
    y "And? "
    s "And that’s unhealthy."
    s "Let me sit down."

    scene yumidormnotebook16
    with dissolve

    y "No."
    s "Why? "
    y "Because you’re fucking creepy."

    if bonus == True:
        y "I’ll talk to you “seriously” for a few minutes, but I’m not letting you sit on my fucking bed when I know you can {i}snap{/i} at any moment."
        s "…"

    s "That’s fair. Fine."

    scene yumidormnotebook17
    with dissolve

    y "Cool."
    y "So...what’s this “serious” stuff you needed to come to my fucking room to talk about?"
    s "Well, to start-"
    s "I had dinner with your mom the other day."

    scene yumidormnotebook18
    with dissolve2
    play music "thingsthathurt.mp3" fadein 5.0

    y "…"
    y "You...fucking...{i}what?{/i}"
    s "I ran into her at the bathhouse recently, got her phone number, and had dinner with her."
    y "…"

    scene yumidormnotebook19
    with dissolve

    y "You barged in...to {i}my{/i} fucking room...to talk about going on a date with my fucking {i}mother?{/i}"
    y "Is this a joke? Or are you just really fucking bad at explaining things?"
    s "Probably the latter."
    s "It wasn’t a date. She was very adamant about that."
    y "Oh boy. What great news. Thank you so much for fucking telling me."
    s "…"
    y "Go on. I want to hear the rest."
    y "Did you have fun?"
    y "I bet I can guess at least one of the conversation topics."

    "Yeah, I don’t know what I was thinking bringing this up."
    "I should have known from the moment I saw Yuki’s reaction that this wouldn’t go well."
    "But hey, sometimes you have to-"

    if bonus == True:
        play sound "static.mp3"
        scene yumis1 with flash
        scene yumis2 with flash
        scene yumis3 with flash
        scene yumis4 with flash
        scene yumis5 with flash
        scene yumi6 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene yumi6 with flash
        stop sound

    "I teleport back in time to a moment of great importance."
    "It’s hotter than I’ve grown used to over the last few months."
    "The sun reflects off of the girl in front of me and I can see beads of sweat dripping down her arms."
    "She’s probably walked for a long time today."

    play sound "static.mp3"
    scene yumi6fun
    with flash
    stop sound

    "The sun is stronger than I imagined it was. "
    "It melts her eyes and turns them into a variety of colors that drip down her shirt before being absorbed into the fabric."
    "Off in the distance, I can hear the sound of a chainsaw or thunderstorm or tornado or something equally as loud."
    "It’s a rumbling noise. One that makes {i}my{/i} skin crawl and {i}her{/i} skin slide off of her bones."
    "I pick it up and wear it. "
    "I create a Yumi costume and walk around the second half of town, telling passersby I’m going to castrate them before returning home and crying myself to sleep."
    "I miss my mom."
    "I just want someone to love me. "
    "I-"
    "I-"
    "I-"

    menu:
        "Pry":
            if bonus == True:
                play sound "static.mp3"
                scene yumis1 with flash
                scene yumis2 with flash
                scene yumis3 with flash
                scene yumis4 with flash
                scene yumis5 with flash
                scene yumidormnotebook20 with flash
                stop sound
            else:
                play sound "static.mp3"
                scene yumidormnotebook20 with flash
                stop sound
        "Leave her alone":
            if bonus == True:
                play sound "static.mp3"
                scene yumis1 with flash
                scene yumis2 with flash
                scene yumis3 with flash
                scene yumis4 with flash
                scene yumis5 with flash
                scene yumidormnotebook20 with flash
                stop sound
            else:
                play sound "static.mp3"
                scene yumidormnotebook20 with flash
                stop sound

    y "TELL ME YOU FUCKING SEE ME!"
    s "...What?"
    y "Stop conveniently going into a fucking mind-coma or whatever it is you’re doing while you’re around me!"
    y "It creeps me the fuck out and I wasn’t finished yelling at you yet!"
    y "Why were you with my mom?!"
    s "She wanted to talk to me about something."
    y "What?!"
    y "What did she want to talk about?!"
    s "You."
    s "She wanted to see how you were doing."

    scene yumidormnotebook21
    with dissolve

    y "...Why?"
    s "Because you’re her daughter."
    y "Since fucking when?"
    s "Since she’s been sober."
    y "You think I haven’t heard that before?"
    s "I don’t know what you’ve heard before."
    s "I just talked to someone that wanted to talk to me."
    s "And I thought it might be good if you talked to her as well."

    scene yumidormnotebook22
    with dissolve

    y "Awe, you did all that just for me? How sweet of you!"
    y "What’s next, Sensei? Gonna buy me a car? Start paying for my phone bill?"
    s "…"

    if bonus == True:
        y "Are you still trying to make up for mouth-[raping] me?"
    else:
        y "Are you still trying to make up for hugging me?"

    y "You know you could do it again right now and nothing would even happen, right?"
    y "Everyone already heard me screaming at you earlier and no one showed up at all."
    y "Why do you think that is?"
    y "Are these walls too thick to hear through?"
    y "Or do you think that maybe, just {i}maybe{/i}, some of them want me to get hurt?"
    y "Maybe they want to hear me scream? "
    y "Want to find out, Sensei? "
    s "You probably shouldn’t be holding onto my shirt right now."

    scene yumidormnotebook23
    with dissolve

    y "You probably shouldn’t have turned into a fucking vegetable after dropping a bomb on me!"
    y "Stay the fuck away from my mom! She has nothing to do with you! She has nothing to do with me either!"
    s "I get it. I won’t bring her up again. "
    s "I didn’t mean for you to explode."
    y "You don’t drop fucking bombs without expecting them to explode, douchebag."

    scene yumidormnotebook24
    with dissolve

    y "I am the child of a fucking criminal and a drug addict. "
    y "And I am trying...my fucking hardest...to not be like either one of them."

    scene yumidormnotebook25
    with dissolve

    y "So stop trying to get me to open up to you and let me deal with it the same way I deal with everything else!"
    y "You want to “fix” the class delinquent?!"
    y "You want me to stop calling you so many names?!"
    y "Then use your fucking brain for the first time in your life and figure out what it is I need!"
    y "And, here’s a tip for you."
    y "It’s sure as hell not my fucking mother."
    s "I didn’t mean to offend you."

    if bonus == True:
        y "Yeah. You didn’t mean to fucking kiss me either."
    else:
        y "Yeah. You didn’t mean to hug me either."

    y "Wonder why you keep just “accidentally” doing shit to hurt {i}me{/i} but not anyone else."
    y "Are you having fun, Sensei?"
    y "I’m guessing you got bored of our detentions and now you’re just trying to fuck me up in even worse ways?"
    s "I’m sorry, okay? I don’t know what else you want me to say."

    scene yumidormnotebook26
    with dissolve

    y "God fucking damnit. Why did you even come in here?"
    y "Nothing good ever happens when you’re around."
    y "But...my fucking {i}mom{/i}?"
    y "I know you don’t like me, but that’s just...too fucking much."
    s "Yumi, I-"
    y "Just get out. I don’t want to hear it."
    s "…"
    y "…"
    s "…"

    scene yumidormnotebook25
    with hpunch

    y "I TOLD YOU TO GET OUT!"
    s "You’re...still holding onto my collar."

    scene yumidormnotebook27
    with dissolve

    y "Oh. Right. Yeah."
    y "Sorry."
    s "Why are {i}you{/i} apologizing when-"
    y "Just get out please."
    y "The only thing I hate more than crying in front of people is how often I have to fucking put up with you now."

    scene black
    with dissolve2

    "I do as she says and exit the room, once again confused about how things managed to go haywire at the worst possible moment."
    "Bringing up Yumi’s mom was a mistake."
    "I honestly don’t understand why I ever considered it in the first place."
    "And so I find myself in one more situation where she has been hurt by something I have done behind the wheel-"
    "And I can’t help but wonder who it is that I will hurt next."

    $ renpy.end_replay()
    $ yumidorm30 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection stays exactly the same!{/i}"
    "{i}Everything you touch turns to shit!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumidorm35:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label yumidorm:
    if yumi_love >= 5 and streets10 == True and yumidorm5 == False:
        jump yumidorm5
    if yumi_love >= 10 and yumidorm5 == True and yumidorm10 == False:
        jump yumidorm10
    elif yumi_love >= 5 and streets10 == False:
        play sound "knock.mp3"

        s "Hey Yumi, are you in there?"
        "..."
        "There's no answer."
        jump doorknock
    if yumi_love >= 15 and yumidorm10 == True and cafe20 == True and yumidorm15 == False:
        jump yumidorm15
    if yumi_love >= 20 and streets20 == True and yumidorm20 == False:
        jump yumidorm20
    if yumi_love >= 25 and streets25 == True and yumidorm25 == False:
        jump yumidorm25
    if yumi_love >= 30 and streets30 == True and yukidate1 == True and yumidorm30 == False:
        jump yumidorm30
...
```