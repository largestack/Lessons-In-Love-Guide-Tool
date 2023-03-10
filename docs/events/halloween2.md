# Guest of Honor (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Value of Sharing](./halloween1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween2
* Group: Main
* Triggered by label: halloween1
* Chain sources: halloween1
* Chain sources path: halloween1

## Official wiki page

[Guest of Honor](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween2&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween2:
    if _in_replay:
        play music "justbehappy.mp3"

    scene nightsky
    with dissolve

    s "Costumes, huh?"
    s "I wonder what everyone is going to dress up as?"

    "My head hits the pillow and my eyes navigate to the small crack in my window, focusing in on the only sliver of the night sky that I’m able to see from inside of my room."
    "I never particularly cared for Halloween until roughly half an hour ago when I realized it won’t just be another excuse for people to get drunk and wander the streets anymore."

    if bonus == True:
        "This year, I’m going to be spending my time with a bunch of [teenager]s who will, hopefully, be attempting to seduce me or something along those lines."
    else:
        "Now, it's one more opportunity to teach!"
        "Unfortunately, most of the girls don't seem to like mixing vacations with education."

    "Kind of like how the beach trip went, I guess."
    "Sure, the beach didn’t exactly end in the most ideal way for everyone involved (Sorry, Rin), but what could possibly go wrong at a Halloween party?"
    "Especially one at the coveted Amamiya mansion, which I’ll finally be seeing for the first time."
    "That does come with its own list of setbacks, however."

    if bonus == True:
        "Knowing that Ayane’s father and butler live there, I don’t know if I’ll be able to have as much...alone time with anyone as I’d like."
        "But it’s a mansion, right? I’m sure there’s some...hidden bookcase-door or something that I can disappear into with someone if I really want."
    else:
        "Like, what if I get lost and can't find my way back to the party and get really scared and then cry a lot?"

    scene black
    with dissolve

    if bonus == True:
        "I close my eyes and think of the many horrible things that are bound to happen over the next two days, trying to drown them out with thoughts of scantily dressed girls."
        "It’s only a matter of time until I start getting roped into more uncomfortable conversations where I need to conceal my relationships with pretty much everyone in the class inside of one confined space."
        "It’s actually kind of nerve-wracking when I put it that way. "
        "But if there’s anything I can be associated with, it’s danger."
        "Just kidding."
        "I’m not really an exciting person."
        "But you already know that."
        "Either way, I’m suddenly looking forward to the next couple days. "
        "Unfortunately, it looks like it’s going to start with a large hit to my wallet."
    else:
        "I close my eyes and think of the many horrible things that are bound to happen over the next two days."
        "Hopefully, Ayane will have a tour guide who can hold my hand or something."

    "………"
    "……"
    "…"

    $ totaldays += 1
    $ day = 6
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date

    "{i}[totaldays] Days have passed...{/i}"
    "{i}Roughly twelve hours and forty-three minutes later...{/i}"

    scene halloweenmall1
    with dissolve

    "Just as planned last night, Ayane and Sana show up at the house first thing in the morning and I am forcefully dragged out of bed and into the chaperone position."
    "As soon as we get to the mall, the girls make a beeline to a familiar clothing store that...apparently also sells Halloween stuff?"
    "Or at least, that’s what I expected when they came here first."
    "Actually looking around, I don’t see anything out of the ordinary whatsoever."

    s "Ami, why are we here? Isn’t there an actual costume shop at the mall?"
    a "Well...yeah. "
    a "But you seemed worried about spending too much money yesterday, so I’m probably just going to buy a few small accessories here and kind of..."
    a "I don’t know, throw something together maybe?"
    s "You’re going to make your own costume?"
    s "Isn’t Halloween tomorrow? That seems kind of rushed."

    scene halloweenmall2
    with dissolve

    a "Yeah, but I don’t want to bother you when you already let me live there for free and stuff..."

    if bonus == True:
        s "I’m your legal guardian. I think at least that much is expected of me."
    else:
        s "You are my accountant and I do not pay your salary. The least I can do is this."

    a "It’s fine, really. I make costumes with Molly and stuff all the time. "
    a "If I really can’t throw anything together on time, I can just have her help me. She's pretty amazing when it comes to that stuff."
    a "I’ll probably just wind up being an anime character or something anyway."
    a "And I’m pretty sure the Halloween shop doesn’t carry those because of copyright stuff."

    scene halloweenmall3
    with dissolve

    c "Heya! You guys are up early today!"

    "Chika suddenly shows up, which I guess was bound to happen on account of her working here, and wastes no time in pointing out that...yes, it is very early."

    s "Halloween shopping."

    scene halloweenmall4
    with dissolve

    c "Here? Strange choice."
    c "You know there’s a-"

    scene halloweenmall5
    with dissolve

    a "We know. I just need a few accessories and stuff. I'm making my own costume this year."

    scene halloweenmall6
    with dissolve

    c "Oh, awesome! Is this for the thing at Ayane’s place?"
    a "Mhm~ Were you coming too, Chika?"
    c "You know it. I already bought my costume and stuff, but I’m still trying to figure out a way to get Yumi to come as well."
    s "You could always just...{i}not{/i} do that instead."

    scene halloweenmall7
    with dissolve

    c "Don’t be mean. She’s not even here to defend herself."
    a "Heh...Well...at least I don’t have to worry about {i}Yumi{/i} stealing you, apparently..."
    c "You know Yumi’s birthday is on Halloween, right? I can’t just not include her."
    c "Do you have any idea how depressing it is to be alone on your birthday AND Halloween at once? That's like, mega-depressing."
    s "It’s not depressing if she has Chinami. Just put those two together again."

    scene halloweenmall8
    with dissolve

    c "See, the thing is that Chinami’s never really experienced Halloween before, so it would be just another day for her."
    s "To be fair, she gets her own personal Halloween every time she comes to the mall."
    c "Is that a dog-mask joke?"
    s "Yeah, that’s a dog-mask joke."
    a "Can we, umm...not talk about the dog mask? I’m still a little shocked after seeing my [uncle] walking around holding hands with a small girl dressed as a dog."
    a "Not really a thing I ever wanted to see."

    scene halloweenmall9
    with dissolve

    c "You guys...held hands?"
    s "…"
    a "…"

    "You know, now that I think about it, that part probably wasn’t necessary and I’m sure it sounds weird to hear out of nowhere."

    s "I probably shouldn’t have done that, should I?"

    scene halloweenmall10
    with dissolve

    a "Yeah, you really shouldn’t have. It was weird."
    c "Nononono! It’s totally fine! I’m just surprised she let you hold her hand in the first place!"
    c "She’s normally super careful about touching people she’s not familiar with."
    a "Sensei, why is a girl that small so familiar with you?"
    s "Ami, don’t you need to be shopping right now?"
    s "Sana and Ayane have just been browsing since we walked in and I’m pretty sure they’re waiting for you to finish."

    scene halloweenmall11
    with dissolve

    c "R-Right! You still need to buy stuff!"
    c "Sorry. I don’t normally get visitors this early so I got a little wrapped up in chatting."
    a "It’s fine. Sensei was just leaving anyway."
    s "I was?"
    a "Mhm. Right after you give me your credit card."
    s "Who do you think you’re talking to, Ami?"
    a "A loser. "
    a "Card, please."

    "I sigh to myself and pull my credit card out of my wallet, handing it over to Ami as I am incredibly weak to her for reasons beyond my comprehension."
    "The power of [niece]s, I guess."

    scene black
    with dissolve2

    s "I guess I’m leaving now?..."
    a "Yup! Can you meet us at the food court in like thirty minutes?"
    s "But what am I supposed to do until then? I came here with you guys."
    a "You’ll find something~"
    c "Sensei! Could you bring me back something from the Chinese place, pleeeeease? I forgot to pack something for lunch sooo...thank you~"
    s "Why does everyone always expect me to buy them things?"
    ay "Sensei! If you’re buying us things, can you stop at Asteriskbucks and get me an iced coffee?"
    ay "Thank you and I love you!"
    s "No, Ayane. You’re rich. Buy your own coffee."
    s "I’ll get one for Sana, though."
    sa "W-What? But I...don’t even like...coffee..."

    scene halloweenmall12
    with dissolve2

    "I don’t make it more than two minutes away from Chika’s boutique before bumping into two more familiar faces."
    "They don’t appear to have any bags with them, so I come to the conclusion that there can only be one thing that brought them here today."

    s "Why are you two spying on me?"
    sar "…"
    h "...What?"
    s "Oh. Never mind."
    s "I just didn’t see any bags."
    h "So...you decided we were spying on you?"
    sar "It was Haru-chan’s idea. I told her it was a bad one, but she wouldn’t listen."
    sar "In fact, she’s been bullying me all morning. Please come save me, Sensei~"

    scene halloweenmall13
    with dissolve

    h "You’re a really bad actor. You know that?"
    sar "Yes, but I’m cute so I can get away with it."
    s "So, if you two aren’t here spying on me, what are you up to exactly?"

    scene halloweenmall14
    with dissolve

    sar "Halloween shopping!"
    sar "We’re going to buy sexy outfits and get drunk at my place tonight."
    s "That just sounds like a normal night but with sexy outfits added into the mixture."
    sar "I know. Great, right?"

    scene halloweenmall14
    with dissolve

    sar "I’m going to make myself feel good by dressing as one of those sexy nurses you always see around Halloween and Haru-chan is..."
    sar "Doing something with Maki? What was it again? A cat?"

    scene halloweenmall15
    with dissolve

    h "Nyaa~"

    scene halloweenmall16
    with dissolve

    h "I can’t believe I just did that in public. Please kill me."
    sar "Do it again, do it again! "
    s "Yes, please do it again."

    scene halloweenmall17
    with dissolve

    h "I’ll do it plenty more times if you come hang out with us tonight!"
    s "I was beginning to worry that you two weren’t going to ask me."
    sar "Of course we were going to ask you. We were actually just talking about you before you showed up."
    s "Good things, I hope?"
    sar "Are there any bad ones?"
    s "Oh yeah. Tons."
    s "For starters, I’m here with your daughter right now."

    scene halloweenmall18
    with dissolve

    sar "Uhh...what?"
    s "That sounded worse than I wanted it to. "
    sar "What...are you two doing? Where is she?"
    s "Costume shopping with my [niece] and Ayane."

    scene halloweenmall19
    with dissolve

    sar "Oh."
    sar "Well...I guess it makes sense why you’re walking around by yourself then, at least."
    sar "But that’s just one more reason you should come to my place tonight. "
    h "She’s got a point. Don’t you spend like, every waking moment surrounded by [teenage]girls?"
    s "I see no problem with this."
    h "Well it’s just like...don’t you want to hang out with people your own age every once in a while?"

    "Well...it’s true that people my age are less loud but-"
    "Wait a minute. That isn’t true at all. "
    "Sara and Haruka are two of the loudest people I know when they get drunk."
    "But...two drunk women in the same room...with a third in Maki..."

    s "Yeah. Count me in."
    s "I don’t think the girls’ Halloween party is until tomorrow night, so I should be free."

    scene halloweenmall20
    with dissolve

    h "You’re even going to their Halloween party?"
    s "I’m the guest of honor. Probably."
    sar "You can be the guest of honor at the bar, too!"
    sar "You’ll be the only boy, so it makes sense. "

    if bonus == True:
        sar "Now there’s just the issue of finding a temporary bartender since I don’t want Sana hanging around three horny drunk women all night."
    else:
        sar "Of course, if my son was never murdered you wouldn't be the {i}only{/i} boy. But that's a story for another day."

    s "I’m glad to see you’re wearing your mom-hat today."

    scene halloweenmall21
    with dissolve

    if bonus == True:
        h "Okay then. I guess we’re going to ignore the fact that she just called all of us horny."
        h "This is fine."
    else:
        h "Wait. I feel like we probably shouldn't just ignore-"

    s "Why can’t you just tend the bar, Sara? "

    scene halloweenmall22
    with dissolve

    if bonus == True:
        sar "I want to get drunk and eat candy and feel pretty and sit on your lap!"
        s "If you sit on my lap, won’t the other two girls get jealous?"
    else:
        sar "I want to get drunk and eat candy and feel pretty and talk about my son!"
        s "You can't talk about that until later in the game."

    h "Do they not realize I’m still here? Should I clap or something?"

    scene halloweenmall23
    with dissolve

    if bonus == True:
        sar "So what if they get jealous? I’ll be Nurse Sara tonight. Sitting on your lap is the only way to cure your chronic illness."
        s "You would not have lasted very long in medical[school]."

        scene halloweenmall24
        with dissolve

        h "Okay, I’m gonna just step in and say it’s not really the best idea to start talking about sitting on his lap when your daughter could show up at any moment."
        sar "Oooh? Sounds to me like someone is jealous."
        sar "Do you want to sit on his lap too, Haru-chan?"

        if harukafirstlust == True:
            scene halloweenmall25
            with dissolve

            h "Uhhh..."

            "Oh, she’s done a lot more than just sit on my lap, Sara."

        scene halloweenmall25
        with dissolve

        h "Even if I did, it’s not like I’d say anything about it in public. "
        sar "Aww, come on~ You can be his little lap-cat and cuddle up really close."
        sar "I bet you purr {i}really{/i} loudly...don’t you, kitty?"
    else:
        sar "I miss him every day."

    scene halloweenmall26
    with dissolve

    h "Okay, time to go. "
    h "I have to go take over a shift at the cafe soon anyway."

    scene halloweenmall27
    with dissolve

    sar "Boo~ Haru-chan is making me say goodbye early. "
    sar "You’ll come tonight, though. Right?"
    sar "Nurse Sara will be really sad if you don’t."

    if bonus == True:
        h "Oh, he’ll come alright."
        h "…"
        sar "…"
        h "I really didn’t want that to sound sexual and I’m sorry."
        sar "Can you keep an eye out for a spare bartender for us, Sensei?"
        sar "I’ll do it if I reaaaaaaally need to, but I wanna relaaaaaax."

        "Sara begins to sound like a kid on the verge of a temper-tantrum."
        "She {i}does{/i} work almost every night. And even if she’s doing virtually nothing for most of those shifts, it would probably still be good for her to get some rest."

        s "I’ll keep an eye out, but I only know like...two and a half bartenders."
        h "How do you know half of a bartender?"
        s "The third one isn’t really...all-there."
        h "...Okay, well we’re gonna go."
        s "Right. See you later. "
        sar "Bye, Sensei. I’ll miss you~"
    else:
        s "I don't know. You're acting rather weird right now and I'd be lying if I said it didn't make me a little uncomfortable."
        sar "Was it all of the stuff about my dead son?"
        s "Yes."
        s "Anyway, bye."
        sar "Aren't you going to at least hug me first?"
        s "Uhhhhhhhhhhhhhhh..."
        sar ".......?"

    scene black
    with dissolve2

    if bonus == False:
        "I slowly back away from Sara and hope that she doesn't notice me."
        "She does."
        "She also forgets to mention anything about needing to find a temporary bartender for the night, but I know she needs one since {i}I am from the future.{/i}"

    "I continue to walk aimlessly around the mall for another few minutes before heading to the food court to meet up with the girls."
    "They all eat lunch while I sit there and ponder over exactly what’s going to happen tonight."
    "And, of course, I forget to buy Chika’s..."
    "…"
    "Wait, what was it she wanted again?"

    $ renpy.end_replay()
    $ haruka_love += 1
    $ sara_love += 1
    $ halloween2 = True
    stop music fadeout 5.0

    "{i}Sara's affection has increased to [sara_love]!{/i}"
    "{i}Haruka's affection has increased to [haruka_love]!{/i}"
    "………"
    "……"
    "…"
    "{i}An hour or so later...{/i}"

label halloween3:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```