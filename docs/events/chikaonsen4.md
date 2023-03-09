# Zanzibar
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikaonsen4&go=Go)


Part of event chain [Three Words](./chikaonsen3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Main: Annabel Lee](./day280.md)
* [Main: The WAP Man](./day295.md)

## Event properties
* ID: chikaonsen4
* Group: Chika
* Triggered by label: chikavirginx

## Event code
File: \game\ChikaEvents.rpy
Code:
```python
...
label chikaonsen4:
    if bonus == True:
        scene chikawakesup1
        with dissolve2
    else:
        scene wintersky
        with dissolve

    play music "justlights.mp3"

    "I wake up again. A wonderful start to the day."
    "I stare at the girl in front of me who, in what I imagine is a vast departure from normal, fell asleep with her makeup on."
    "Sunlight leaks in through a small paper window and informs me that it’s morning."
    "Or, in more depressing terms- time to leave."
    "It’s unfortunate that this getaway was only for one night, but I’m sure that there will be plenty more just like it in the future."
    "I just have to hope Chika decides to call into more radio shows."
    "Of course, there’s always the chance for me to just...{i}buy{/i} tickets to places like this..."
    "But where’s the fun in that?"
    "It’s much better to have things dropped into your lap than it is to work for them."
    "You’re probably used to hearing that sort of opinion from me by now, aren’t you?"
    "Which means that you probably understand that it’s time for me to, once again, butcher the words of someone much smarter than I am."
    "I believe it was Thoreau who said, “It is not worth the while to go round the world to count the cats in Zanzibar.”"
    "Now, when he said this, he probably meant something along the lines of “It’s better to search within yourself for what you want than to go greatly out of your way for it.”"
    "Why someone would be so dedicated to counting cats, I don’t understand."
    "So I’m going to chalk his words up to insanity and repurpose them to fit my own narrative."
    "Don’t work hard because working hard sucks. "
    "Buy your own cats and count them."
    "There. Problem solved."

    if bonus == True:
        "I spit on Thoreau’s grave from my place beside a naked [teenager] and wish away my morning erection."
        "It probably sounds hard to believe, but after last night, the last thing I want is to have sex right now."
        "And I worry that if Chika wakes up and sees that her new best friend is already fully erect, I may never fuck again."
    else:
        "I spit on Thoreau's grave and think a few other things I'm not allowed to say in the censored version of the game."

    s "…"

    "Just how long is she going to sleep for, though?"
    "What time even is it right now?"
    "I reach over to grab my phone out of my pants (Which are conveniently only several feet away) and find that it’s just after 6:00 AM."
    "Also, my phone is about to die because I passed out without plugging it in last night."
    "I sigh to myself and bring my face closer to hers, hoping that she wakes up and quells this boredom soon."
    "I’d hate to be the one to disturb her slumber, but I honestly might have to at this rate."
    "Sometimes, I feel like I’ll waste away if I just stay in bed."
    "Like I’ll disintegrate and turn into sand."
    "And then, before I know it, girls will be having their hearts broken as they confess their feelings on top of me."
    "Thankfully, I managed to avoid that same tragedy last night."
    "Though, it was in a way that would not quite turn to glass if heated thoroughly."

    s "…"

    "My mind connects the word “thorough” to “Thoreau” and I loop back to the idea of cats and Zanzibar."
    "God, I hope Chika wakes up soon."

    c "Mn..."

    "All of the cats die and I don’t have to count anything anymore."

    c "Sen...sei..."
    s "…"
    s "Chi...ka..."

    if bonus == True:
        scene chikawakesup2
        with dissolve

    c "Mm...what time is it?"
    s "It’s a little after 6:00 AM."
    c "So...early..."

    if bonus == True:
        scene chikawakesup1
        with dissolve

    c "Goodnight..."
    s "You can’t say goodnight when the sun is rising."
    c "Good...sun..."
    s "That’s not even a thing."
    c "Mn..."
    s "…"

    "Huh."
    "All this time, I thought Chika was a morning person."
    "She’s always waking up early to make breakfast and...listening to radio shows with Chinami and-"
    "I wonder if maybe she’s only sleeping in now because she rarely ever has the chance to?"
    "But...then again, it is 6:00 AM."
    "I guess it doesn’t really constitute sleeping {i}in{/i} until it’s around...10:00 AM, I guess?"
    "Wait."
    "How come you can sleep {i}in{/i} but not {i}out?{/i}"

    s "Chika, please wake up. I can’t do this anymore."

    if bonus == True:
        scene chikawakesup3
        with dissolve

    c "Wha?...Do what?..."

    if bonus == True:
        scene chikawakesup4
        with dissolve

    if bonus == True:
        c "Do you wanna...have sex again?..."
        s "No. I’m pretty sure both of us would die."
        c "Sex~"
        s "Yes, Chika. That is a thing we did...many, many times last night."
        c "You’re a...good...sex guy..."
        s "Thank you very much for that completely normal compliment."
        c "{i}Sex man...{/i}"
    else:
        c "Do you wanna...hug again?..."
        s "No. I’m pretty sure both of us would die."
        c "Huuuuug~"
        s "Yes, Chika. That is a thing we did...many, many times last night."
        c "You’re a...good...hug guy..."
        s "Thank you very much for that completely normal compliment."
        c "{i}Hug man...{/i}"
    s "Wow, you’re really out of it, aren’t you?"

    if bonus == True:
        scene chikawakesup5
        with dissolve

    c "Pancakes..."
    s "You want breakfast?"
    c "Chinami likes...pancakes..."
    c "Gotta...make her some..."
    s "Chinami isn’t here right now, Chika. We’re at the onsen."
    c "Call...Yumi..."
    c "About the...pancakes..."
    s "My phone is basically dead."

    if yuminumber == False:
        s "Also, I don’t even have her number."

    if bonus == True:
        scene chikawakesup6
        with dissolve

    c "Mmm...I’ll do it..."
    c "I’m...up now."
    c "Good morning, Sensei~"
    s "Good morning, Chika."
    c "Did you enjoy our first night together?"
    s "I’m sure I’ll be remembering this for the rest of my life."
    c "Heheh~ I’m glad..."
    c "Hey, do you think they have a gift shop downstairs?"
    s "A gift shop? I don’t remember seeing one. Do you want a snack or something?"

    if bonus == True:
        c "I need a morning after pill."
        s "Oh."
        s "Uhh."
        c "Unless you want me to drop out, marry you, have a baby, and then move into Ami’s room."
        s "I can’t say I want any of those things right now."
        c "I didn’t think so."

        scene chikawakesup7
        with dissolve

        c "It’ll just be for this one time."
        c "I’ll start taking birth control now that I know we’re going to be “sexually active” together."
        s "I’m glad you didn’t suggest something as outrageous as a condom."
        c "Why would I do that when having you cum in me feels so good?"
        s "Okay, time to change the topic before I-"
        s "Wait. Too late. It’s hard again."

        scene chikawakesup6
        with dissolve

        c "Oh nooo~ Whatever will we do?"
        s "Nothing right now. "
        c "What if I’m really, really gentle?"
        s "Hands to yourself, woman. I can’t have you turning into a nymphomaniac on me."

        scene chikawakesup8
        with dissolve

        c "Hey! Just because you came in me like ten times last night and we passed out totally naked and covered in sweat doesn’t mean I’m any less wholesome than I was last week!"
        s "It...kind of {i}does{/i}, though."

        scene chikawakesup9
        with dissolve

        c "Nuh-uh."
        s "I am not going to argue with you about this."
        c "Put it in me or face the consequences, [chikamaster]."
        s "What kind of consequences would even come from this?"

        scene chikawakesup10
        with dissolve

        c "I only {i}pretend{/i} to take the morning after pill and just let myself get pregnant."
        s "That is...way too huge of a thing to do out of spite."

        scene chikawakesup11
        with dissolve

        c "I’m obviously kidding, Sensei. I can barely take care of Chinami."
        c "I’m {i}not{/i} a nympho, though. So don’t go saying anything like that to anybody."
        s "Who would I even say that to?"

        scene chikawakesup12
        with dissolve

        c "I mean, you can talk about what we did to whoever you want. I don’t care."
        c "Like, I’ve obviously gotta tell Yumi."
        s "I’m sorry, what?"
        c "She’s my best friend and this was like, a super big deal. I totally have to tell her."
        s "I...don’t think that’s a good idea."
        c "Why not? Cause she always acts all tough and talks about not liking you?"
        c "That’s only like, half-serious. You know that, right?"
        s "That is still enough seriousness for me to think it’s better if she doesn’t know that we’re having sex."
        c "I mean...I can probably leave out the sex part, but..."
        c "I can still tell her you’re my boyfriend now, right?"
        s "…"
        c "…"
    else:
        c "I want...coffee..."
        c "Also, I still have to tell Yumi that...you and me are dating now..."
        s "I'm sorry, what?"
        c "Yeah...because of the hugs...right?"
        s "..."

    "Uh-oh."
    "It appears we have a...dramatic misunderstanding about our future together."

    if bonus == True:
        "But how am I supposed to come out and say something like “Oh, I’m not your boyfriend, but thanks for telling me you loved me and letting me cum in you a bunch of times?”"
    else:
        "But how am I supposed to come out and say something like “Oh, I’m not your boyfriend. All of those hugs meant absolutely nothing?”"

    "How the fuck do I get out of this?"

    s "Why do you want to tell her anyway?"
    c "Because I love her. And I love you."
    c "And I want all of us to be happy together."
    s "And you think Yumi knowing about {i}us{/i} is going to make her happy?"
    c "I don’t think it would make her...{i}not{/i} happy?"
    s "I kind of think she’d oust the both of us."
    c "Yumi? No way, she-"

    if bonus == True:
        scene chikawakesup13
        with dissolve

    c "Wait...you’re not like...embarrassed of me, are you?"
    s "What? Not at all. I think you’re amazing."
    s "But I don’t think it would be safe for anyone else to really know just yet. And that’s including Yumi."

    if bonus == True:
        scene chikawakesup14
        with dissolve

    c "I...don’t want to keep this a secret from Yumi, Sensei. "
    c "You probably don’t get it since you’re a guy, but I need to like...I don’t know, mark my territory, I guess?"
    s "Do you...think Yumi is going to make a move on me or something?"
    c "Not at all. But I don’t think it’s impossible for her to like, wind up liking you or whatever."
    c "I don’t think she’d do something like that to me since the two of us are so close, but like-"
    c "If she knows we’re already together, it might prevent things from ever progressing that far."
    s "I really don’t think you need to worry about that happening, Chika."

    if bonus == True:
        scene chikawakesup12
        with dissolve

    c "Hmm..."
    c "Okay. It looks like we need to compromise."
    c "How about this?"
    c "I won’t go out of my way to tell her...but if it ever comes up in conversation, I’m not going to lie to her about it."
    c "It’s not like Yumi ever really wants to talk about stuff like that anyway. "
    c "And even if I do wind up telling her, I’ll make sure she never even {i}thinks{/i} about mentioning it to the other girls."
    c "She’s surprisingly loyal. And I don’t think she’d ever want to hurt either one of us."
    s "…"

    "Well-"
    "It’s better than nothing, I guess."

    if bonus == True:
        "I mean, Yumi already assumes I’m having sex with the entire class anyway."
    else:
        "I mean, Yumi already assumes I’m hugging the entire class anyway."

    "So having one of the girls confirmed (If things do come to that), likely won’t change much."
    "And, as far as the boyfriend things goes-"
    "I don’t think it’s necessarily {i}bad{/i} to let Chika go on thinking that."
    "I mean, I’m sure the other girls I’m involved with look at me the same way as well. "
    "They just haven’t come out and said it."
    "But that’s what sets Chika apart from the others."
    "She’s mature enough to set her sights on something and then just...take it without thinking of how it will affect anyone else."
    "It’s actually kind of relentless."
    "I admire her."

    s "Yeah. Okay."
    s "Let’s just try and keep it as secretive as possible until [high_school] is over."
    c "Heheh~ I never would have imagined my [high_school] sweetheart would be my teacher."
    s "And I never would have imagined we’d end up in a position like this after our first meeting at the mall."

    "That’s a lie. I imagined this a lot."

    if bonus == True:
        c "Really?"
        c "So you didn’t go home and rub one out to me?"
        s "Nope. Definitely not a thing that’s ever happened."
        c "Weird. Cause I totally did."
        s "Oh, come on. I literally just stopped being hard."

        scene chikawakesup7
        with dissolve

        c "Sensei, as long as the two of us are together, you can kinda count on getting hard pretty much all the time. "
        c "I’m gonna make your life Hell from now on."
        s "Yeah, that sounds like a real nightmare."
        c "Heheh~ Just wait until I start sending you naughty pictures of myself in the middle of class."
        s "Wow, the nightmare never ends."

        scene black
        with dissolve2

        "Chika laughs and hops out of the futon, making her way into the living room and rearranging some of the furniture we may have...knocked around last night."
        "I think about helping, but decide to bask in the stray sunlight for a moment longer."
        "And, once I’m able to do so without much of an...obstacle, I put my pants back on and head over to meet her."

        scene chikawakesup15
        with dissolve

        c "Why am I suddenly the only one that’s naked?"
        s "Why are you still naked and reaching for your bag as if you’re ready to leave?"
        c "Am I not supposed to walk back to the front office like this?"
        c "It’s not like I can wear the yukata anymore."
        s "Definitely don’t do that."
        c "Jealous somebody else might see me?"
        s "That and I don’t want us to be arrested for indecent exposure."
        c "People get naked in the hot spring, though. I’m sure they wouldn’t mind if we do it in the lobby."
        s "Uh-huh. And what about the bus stop that’s right outside of the building?"
        c "What about it?"
        s "Are you going to wait outside like that as well?"
        s "…"
        c "…"
        s "Chika."

        scene chikawakesup16
        with dissolve

        c "Oh my God, Sensei. Do you really not understand a joke when you hear it?"

        scene chikawakesup17
        with dissolve

        c "It’s kind of sad, though..."
        c "Like...I really don’t want to leave. "
        c "I had so much fun yesterday."
        c "Even if all we did was...you know...each other."
        s "Hey, that’s not {i}all{/i} we did. You took that extremely long bath as well."
        c "Yeah..."
        c "And that was...somehow just as good..."

        scene black
        with dissolve2

        "I stand there for a moment as Chika gets dressed, trying to come to terms with how a bath can be just as good as having sex with me."
        "I know Chika can get a little...crazy...but-"
        "Am I...not enough for her?"
        "Just what the hell is that girl into?"
        "………"
        "……"
        "…"
    else:
        scene black
        with dissolve

        "Some other stuff happens or whatever and then we wind up leaving the onsen."
        "........."
        "......"
        "..."

    scene chikawakesup18
    with dissolve

    "We make our way back to the lobby and hand in our room key. "
    "I wound up carrying the TV down as well since the person who brought it up while Chika was away seemed far too old to be doing manual labor like that."
    "And..."
    "Well, I guess that’s it."
    "It was short. It was sweet."
    "It was definitely a vacation."

    c "Have everything? Not forgetting anything in the room?"
    s "Not that I’m aware of."
    s "I mean, it’s not like I really brought anything to begin with."
    s "How about you?"
    c "Nope! Totally good."
    c "Guess...that’s that then."
    s "…"
    c "…"
    s "…"
    c "…"
    s "Cool, so what are we waiting for?"

    scene chikawakesup19
    with dissolve

    c "I was..."
    c "Kinda just hoping to..."
    tb "Oh! Good morning, you two."

    scene chikawakesup20
    with dissolve

    c "Oh, hey! "
    c "I was just hoping I’d run into you one last time."
    tb "Another example of fate, perhaps?"

    scene chikawakesup21
    with dissolve

    tk "Good morning, Mister."
    tk "Would you be willing to discuss with me what game you two were playing last night? "
    tk "It sounded very exciting."
    tb "Tsukasa...how many times do I have to tell you? They were playing a game for adults."
    s "You...uhh..."
    s "You heard all that?"

    scene chikawakesup22
    with dissolve

    if bonus == True:
        tb "You two...sure are lively."
    else:
        tb "Why, it sounded just like the two of you were hugging."
        tb "I could have sworn I heard a bit of clarinet as well."
        s "That was me. I'm not very good."

    c "Hahah...hah...hah..."
    c "This totally isn’t embarrassing at all..."
    s "I am...sorry you had to hear all that."
    tb "Oh, there’s no need to apologize."
    tb "Lovers will be lovers."

    scene chikawakesup23
    with dissolve

    tb "And Chika, dear...I forgot to bring it up yesterday, but I’d be happy to exchange contact information with you in the event that you’d want to meet up for lunch or something of the sort."

    scene chikawakesup24
    with dissolve

    tb "Please forgive me if I’m overstepping my bounds by saying that."
    c "No! Not at all! I’d like, totally love that!"

    "..."

    s "How about I leave you two alone for a little while?"
    s "To say goodbye, I mean."

    scene chikawakesup25
    with dissolve

    c "I’ll only be a few minutes. I promise."
    s "No worries. I’ll just wait outside."
    s "It was nice meeting you."
    tb "It’s been a pleasure meeting you as well. Truly."
    tk "Bye-bye! Please try to be a little more quiet when you play games in the future!"
    s "Right..."

    scene black
    with dissolve2

    "I head outside and come to terms with the trip being over."
    "Chika spends the next five or so minutes talking to the girls inside."
    "And while I can’t say for certain that I understand why, I’ve got a pretty good idea."

    if bonus == True:
        "Teenage girls are fragile."
    else:
        "College girls are fragile."

    "Sometimes, they require fully grown specimens to latch onto so they don’t float off into the air and get sucked into a jet engine. "
    "I don’t think Chika is close to floating away any time soon."
    "Especially now that the two of us are...whatever we are."
    "I’m sure our respective answers to that would be slightly different."
    "But I’m glad she seems to have found someone else to latch onto."
    "Frankly, I’d like to latch onto Tsubasa as well."
    "Albeit in an immensely less wholesome way."
    "But thoughts like that will have to wait until there aren’t feelings at stake."
    "For now...I’ll just-"

    s "…"

    "I see a group of cats off in the distance."

    $ renpy.end_replay()
    $ chika_love += 1
    $ chikaonsen4 = True
    $ onsenticket = False
    stop music fadeout 15.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}The trip to the onsen has come to an end.{/i}"

    if bonus == True:
        play sound "texttone.wav"

        "{i}You have received a photo from Chika to commemorate the occasion!{/i}"
        "………"
        "……"
        "…"
        "My stop comes first."
        "I get off the bus and watch Chika fade from my sight."
        "But not before giving her a few thousand yen for a morning after pill."

    jump saturdayafternoon

label chikalust15skip:
    play sound "dooropen.mp3"
    scene goodmorningio1
    with dissolve

    "I collapse into my hotel bed once more in a rather anticlimactic end to an action packed day."
    "I’m not sure what it was that compelled me to hang around the bar instead of coming back here earlier, but it is what it is."
    "Housekeeping made my bed, and now I must lay in it."
    "I notice that Io never turned the air off after leaving this morning."
    "This is good because it saves me a trip across the room and will prevent a second injury for her should she manage to sneak in again."
    "Which I’m sure she won’t."
    "Not after discovering that I’m not the only person actively seeking something out with repeated knocks on the doors of people who may or may not want to see me at that given moment."

    scene black
    with dissolve

    "I close my eyes and accept, however, that there will always be someone who wants to see me at {i}every{/i} given moment."
    "There’s no real reason for it, really."
    "I just conveniently exist in a convenient place during a convenient crack in time."
    "And, conveniently enough, I’ll be reminded of that all once more tomorrow morning-"
    "When every girl gathers around to hear the announcement of who it will be that can have me for one more night."
    "One more night."
    "That’s literally it."
    "That’s what all of this was about."
    "I am undeservedly blessed."
    "…"
    "I fall asleep to the violent whir of an air conditioner working its non-existent heart out."

    $ totaldays += 1
    $ day -= 6
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
    else:
        "ERROR ADVANCING DAYS"

    "........."
    "......"
    "..."
    "[totaldays] Days have passed..."

    jump dormwar17

label chikalust15:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
s "I’m not sure how accurate that is, Chika."

    scene chikavirgin21
    with dissolve

    c "Hah...hah...oh?..."
    c "Are you...getting close...[chikamaster]?..."
    c "Is that why you’re...slowing down again?..."
    s "The longer this lasts, the better..."
    c "Why’s...that?..."
    c "We can do it...as many times as you want..."
    c "If you’re gonna cum...just...fucking cum..."
    c "I told you it’s...okay to do it inside..."
    s "Oh, right...My reward for...being abandoned."
    c "I have to...give the yukata back..."
    c "I can’t have you...getting it all messy..."
    c "Besides...I kinda...love it when you cum for me..."
    c "And if it’s all inside...you wouldn’t be wasting any..."

    scene chikavirgin22
    with dissolve

    c "Ahhhhh!!!! Yes! Yes! Right there, [chikamaster]!"
    c "Just like that! It’s...so fucking hard...[chikamaster]!"
    c "Oh my...fuck...fuck...I’m gonna cum..."
    c "You’re gonna make me cum, [chikamaster]..."
    c "Let’s...do it together..."
    c "To commemorate...our..."

    scene chikavirgin23
    with dissolve

    c "Ahhhh! Fuck fuck fuck! Do it now! I...can’t..."
    c "[chikamaster]...[chikamaster]...I..."

    with sexfade
    with sexfade
    scene chikavirgin24
    with cumflash
    with hpunch

    c "NNGHHHHH!!!!!!!~~~~~"

    "The two of us erupt at the same time and Chika somehow manages to squeeze my hand with even more force."
    "Lost in the ecstasy, I can’t help but be impressed."
    "Because not only did she manage to have a decently violent orgasm during her first time, she also managed to not let go of my hand even once."
    "There's a chance she just wanted to hang on for...moral support or something like that..."
    "But I guess it's also possible that she just...really likes holding hands?"
    "These are all the things I think about in the several seconds after climaxing."

    scene chikavirgin25
    with dissolve

    c "Hah...ngh...[chikamaster]..."
    c "Holy shit..."
    c "Sex is...amazing..."
    c "Let’s do it again..."
    s "You are literally dripping with cum and blood right now. Relax."
    c "But I don’t wanna relax~ I want more."
    s "I need...time to recharge first."
    c "Pfft...no you don’t."
    c "Let me just...work my magic a little more..."

    scene black
    with dissolve2

    "Chika proceeds to “work her magic” and, to my surprise, that magic must include regenerative powers as I’m back to being fully erect in less than a minute."
    "She finishes three more times before I’m able to finish again, though."
    "And, fearing for her safety and sensing that she’s on the brink of passing out, I decide to pull the plug and give her a rest."
    "She falls asleep beside me."
    "Then wakes up two hours later."
    "And we do it all over again."
    "I think the original plan accounted for some trips to the actual hot spring in between sessions, but..."
    "The two of us were a little too distracted to bother wasting some of our time together in that way."
    "I lose track of the hours and the orgasms."
    "And fall asleep with her in my arms."
    "The last thing I notice before passing out is how wet and sticky her skin feels."

    $ renpy.end_replay()
    $ chika_virgin = False
    $ chikaonsen3 = True
    $ chika_love += 5
    stop music fadeout 10.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "………"
    "……"
    "…"

    $ totaldays += 1
    $ day += 1
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
    else:
        "ERROR"

    "{i}[totaldays] days have passed...{/i}"

    jump chikaonsen4
...
```