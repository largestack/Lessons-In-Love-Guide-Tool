# Baby Steps
Maki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makiinv3&go=Go)



## Event preconditions
❌Event "[Makoto: A Beautiful Mind](./sadgirls8.md)" is completed (event=sadgirls8)

❌Day of week is Sunday

✅Event "[Main: Metal in Microwaves](./halloweentwo13.md)" is completed (event=halloweentwo13)



## Next events
* [Futaba: This Infected Wound](./futabadorm50.md)
* [Karin: Emerald Eyes](./karindate25.md)
* [Io: Cupid's Arrow](./ioarchery1.md)

## Event properties
* ID: makiinv3
* Group: Maki
* Triggered by label: makiinvite
* Triggered by branch label: inviteover

## Event code
File: \game\MakiEvents.rpy
Code:
```python
...
label makiinv3:
    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and wait for her to answer."
    "She hasn’t been back at my house ever since the impromptu semi-kidnapping that resulted in me failing (At least by my definition) to cheer up Makoto, so I figure I should invite her back now that things are..."
    "Well, less horrible."
    "Of course there will be some lingering pain for lifetimes to come, but who says you can’t counteract some of that with a little quality time?"

    play sound "phonebeep.wav"

    maki "Hello?"
    s "Hey. On a scale of one to ten, how miserable are you today?"
    maki "On the inside or on the outside?"
    s "Uhh...both?"
    maki "Eight and four. Why? Do you need a dildo? We offer delivery now."
    s "I can’t imagine there is very much demand for that."
    maki "The market for dildo delivery is actually surprisingly large."
    s "That aside, would you want to come hang out at my place? I can’t guarantee that I can do anything for you on the inside, but I might be able to bring that external misery down to a three."
    maki "Is that so? I think I might have to take you up on your offer then."
    maki "This actually works out really well. I had something to do in that area already. "
    s "It’s not dildo delivery, is it?"
    maki "Nah, it’s nothing that fun. I’m dropping Makoto off for a therapy session."
    s "Oh. "
    s "Yeah, that’s not fun at all."
    s "But good for her."
    maki "Yup! I’ll be over in about...half an hour?"
    s "Sounds good. See you soon."
    maki "Yup! See you!"

    scene black
    with dissolve

    play sound "phonebeep.wav"

    "I hang up the phone and decide to crash on the couch until Maki gets here."
    "........."
    "......"
    "..."

    scene makivisits1
    with dissolve2
    play sound "knock.mp3"
    play music "acoustic.mp3"

    "I spring up from the couch as soon as I hear a knock on the door, hoping I’m able to let Maki in and hide from Ami before that’s a thing I have to deal with today."
    "Should I have waited until Ami was {i}gone{/i} to invite Maki over? Yes. "
    "But part of me doubts she’ll put up much of a fight considering that she now understands everything that happened. "
    "Only part of me, though."
    "This could very well still end extremely poorly."

    play sound "dooropen.mp3"
    scene makivisits2
    with dissolve

    maki "Hey. Thanks for the invite. "
    maki "I was starting to worry that I’d never be invited back after the whole kidnapping thing."
    s "To be fair, that was a situation in which you weren’t invited at all. So I would think that it wouldn’t even matter if I were to invite you or not."
    maki "I guess it doesn’t. I like to keep my home intrusion to a minimum, though."
    s "Probably a good call. Do you have a time limit today?"

    scene makivisits3
    with dissolve

    maki "Time limit?"
    s "You know...since you dropped Makoto off?"
    s "I kind of figured you’d have to go pick her up as well."
    mak "Oh, don’t worry about that. She’s a lot closer than you think."
    s "What?"

    play sound "dooropen.mp3"
    scene makivisits4
    with dissolve

    s "..."
    mak "..."
    s "Please don’t tell me I’m the therapist."
    maki "Hey, I just said it was a therapy {i}session.{/i} I never said there was a therapist involved."

    scene makivisits5
    with dissolve

    maki "But, no. Makoto is here to see someone else. So you and me can hang out until she’s ready to leave. Such a convenient coincidence, right?"
    s "Maybe a little too convenient..."

    play sound "dooropen.mp3"
    scene makivisits6
    with dissolve

    a "Why, hello there. Are you ready for today’s session, Makoto?"
    mak "Can you not call it that? I just want to talk without feeling like I’m totally and irreversibly broken."

    scene makivisits7
    with dissolve

    a "Sure! Come on, I’ll show you my room."
    maki "Maybe keep the door cracked open a little. That look you just gave my daughter a second ago has me questioning just what type of therapist you are."

    scene makivisits8
    with dissolve

    mak "Can you maybe, like...{i}not{/i} ruin this before it even starts? I’m uncomfortable enough as is."
    s "You two can close the door, it’s fine. Just don’t lock it because we’ll be listening closely."

    scene makivisits9
    with dissolve

    mak "Uhh...please don’t."

    play sound "dooropen.mp3"
    scene makivisits10
    with dissolve

    "Makoto and Ami disappear into Ami’s bedroom- which is a thing I never thought I would say, but here we are."
    "I guess the fruits of tragedy can be a little surprising after repeatedly kicking its tree and hoping for something else to fall."

    maki "Makoto told me all about how Ami was able to help her when she ran away to school the other day."
    maki "Of all the people, who would’ve thought she’d be the one to throw her one of those...life saving, floaty tube things."
    s "They’ve found one more thing they have in common, I guess...albeit not a very good thing."

    if kirinkill == False:
        s "Though, I find it a little strange how Ami was able to do something for her Miku {i}wasn’t{/i} when both of them have dealt with the deaths of their parents."
        maki "True. Miku’s case is a little different from most, though."
        maki "In a lot of ways, she hasn’t really processed things either."
        maki "And while I have no idea what your niece’s situation is like, it seems that she was able to tell it to Makoto straight without having to hide everything behind a bunch of walls she put up."
        s "I wouldn’t say Ami has really processed things either. She still breaks down every now and then."
        maki "I think it’s kind of impossible for anyone that young to truly process something like this. It’ll be years before any of those girls can talk about it without bursting into tears."
        maki "For now, though...I say we let them be. They’ll help each other...they’ll connect with each other...and we’ll be here to plug them back in if they ever get disconnected."
    else:
        maki "Yeah...I guess so."

    maki "It pains me to say this as even {i}I’m{/i} starting to see her as a bit of rival, but Ami’s a good girl."
    s "Why would you ever see Ami as a rival?"
    maki "I have no idea. But every time I’m around her, I keep wanting to put her in her place."
    s "It’s starting to make a little sense why you wanted to keep the door cracked..."

    scene black
    with dissolve2

    "Maki takes a seat at the kitchen table."
    "I offer her something to drink but she respectfully declines as scattered but pained laughs play quietly in the background."
    "I turn on the TV to mask them as invading their respective privacies now would do me no good. And curiosity is only beneficial when there is something to be gained from its existence."
    "I will gain nothing from the acute awareness of the suffering of girls that I care for."
    "But they have everything to gain from one another."
    "Which is why I wouldn’t mind if they locked the door."
    "........."
    "......"
    "..."

    scene makivisits11
    with dissolve2

    maki "I’ve gotta say...your family’s been really good at bailing me out lately. This single mother thing isn’t easy. Especially when your relationship with your daughter is already all over the place."
    maki "I’ve got no idea how Sara does it. Especially after losing one of her kids."
    s "I think you’ll be fine. Things already seem to be getting a little better with you two."
    maki "Things {i}are{/i} a little better. We had dinner together for the first time in what feels like years last night."
    maki "Granted, it was a just a pizza we had delivered. But hey, baby steps are fine for now. We’ll be able to walk on our own two feet again in no time at all."
    maki "And all that lashing out in the beginning...while it hurt at the time...I get it now."
    maki "I probably would have done the same if either of my parents died when I was Makoto’s age. But, then again, I was never really as close to either of them as she was with her dad."
    maki "And, you know...while this is still one of the worst things that’s ever happened to me...part of me feels a little relieved."
    maki "I’ve got nothing left to dread anymore."
    maki "I don’t have to worry about the slow creep of tragedy in watching everyone I care about get older since everyone but Makoto is already gone- and I’m going to die {i}way{/i} before her."
    s "I'm pretty sure there should have been some knocking on wood there."

    scene makivisits12
    with dissolve

    maki "Heh. Wood."
    maki "But what about you? Anyone you’re dreading the eventual loss of?"
    s "Wow, what a fun conversation topic you’ve chosen."
    maki "Hey, we’ve got a few hours to kill. We might as well get all of the dark stuff out of the way now so we can get back to talking about the {i}real{/i} main topic today — dildo delivery."
    s "Main topic aside..."
    s "I guess there {i}is{/i} someone."
    maki "Mother? Father? Sister? Brother?"
    s "None of the above."
    s "It’s kind of complicated, really."
    maki "Are you going to tell me? Or am I going to have to keep naming potential relationships you may have in hopes of getting it right?"
    s "You can name as many “potential relationships” as you want, but the unfortunate truth is that I have no idea what I'd even {i}call{/i} a relationship like this."

    scene makivisits13
    with dissolve

    maki "Wow. That {i}does{/i} sound complicated."
    s "Even that doesn’t really begin to describe it. I guess I see your point, though. Not having to worry about that anymore does sound like it would be a load off of my back."
    s "I’m just...okay with carrying that load for now, I guess."

    scene makivisits14
    with dissolve

    maki "Yeah...if that were an option for me, I would have done the same without even giving it a second thought."
    maki "It’s kind of crazy how much my life has changed recently despite it having been me and- uhh, {i}Makoto and me{/i} on our own for over three years now."
    maki "Knowing that Masahiro is dead completely changes everything even when we’ve been “alone” all this time."
    maki "So now I’ve...just got a {i}new{/i} load to carry, I guess."
    s "..."
    maki "Heh. Load."
    s "Comparing single parenthood to semen seems low for even you, Maki."
    maki "Come on, man. Laughs are going to be few and far between for me from now on. You’ve gotta let me have moments like that."
    s "I’m sure you’ll laugh just as much as you always do. There just might be some...melancholy mixed in with everything now."
    maki "Maybe you’re right..."
    maki "Maybe I’m just worried right now that things are going to permanently change because of how different and horrible everything feels all of a sudden."
    maki "But before that, there were {i}other{/i} worries. And if this one fades as well, I’m sure even more will take its place."
    maki "Isn’t it weird, Sensei?"
    maki "How your worries become amplified the moment you’re all someone has left?"
    s "Yeah...the girl giving your daughter “therapy” right now intentionally reinforces that idea nearly every single day for me."
    maki "You should be glad she does. For it’s that exact sort of thing that will keep us alive longer since we’re no longer living for just ourselves."

    "A moment of silence passes."
    "Then, a set of unexpected words bent into the shape of an anecdote — pouring from the mouth of a woman who laughs at dick jokes — makes me realize just who she is beneath her skin."
    "It’s someone far more beautiful than I could have ever imagined."

    maki "You want to know the weirdest change that’s come from all of this?..."
    maki "There’s a one way road not far from the shop that I have to cross to get to the local corner store."
    maki "Before my husband died, I’d only look to the left when crossing since that’s where all of the cars come from."

    scene makivisits15
    with dissolve

    maki "But now...I look to the right as well."
    maki "Just to be sure."

    scene black
    with dissolve2

    "Maki and I remain at the table for another couple hours until Makoto and Ami emerge from the bedroom."
    "Both of their eyes are red from crying."
    "But for a brief moment, a slight smile spreads across Makoto’s face."
    "When I look toward Maki to see if she notices, I catch a glimpse of a thin layer of fluid beginning to form over her eyes."
    "I get lost somewhere between aquamarine and turquoise."
    "But I find myself just in time to watch her ruffle her daughter’s hair as the two of them leave my home."

    s "..."
    a "They’ll be okay, Sensei..."
    a "Just like us..."

    stop music fadeout 10.0

    "I follow suit and ruffle Ami’s hair as well."
    "And then I manage to get to sleep without my mind wandering off the deep end once more."

    $ renpy.end_replay()
    $ makiinv3 = True
    $ maki_love += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"

    jump advancetomon
...
```

## Code that triggers this event
File: \game\MakiEvents.rpy
Code:
```python
...
label makiinvite:
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump inviteover
    if makiinvite1 == False:
        jump makiinvite1
    if makiinvite1 == True and makiinvite2 == False:
        jump makiinvite2
    if sadgirls8 == True and day == 7 and makiinv3 == False:
        jump makiinv3
...
```