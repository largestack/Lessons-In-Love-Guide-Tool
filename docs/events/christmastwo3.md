# Room to Grow (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Reliable and Totally Legitimate Princess Imani](./christmastwo2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmastwo3
* Group: Main
* Triggered by label: christmastwo2
* Chain sources: christmastwo2
* Chain sources path: christmastwo2

## Official wiki page

[Room to Grow](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo3&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo3:
    $ totaldays += 1
    $ day = 5
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
    else:
        "ERROR ADVANCING TO FRIDAY"

    scene imaniclassintro1
    with dissolve2
    play music "10c.mp3"

    "Another day begins and, lo and behold, Imani storms into class and immediately usurps my role as “most important person in the room.”"
    "But hey, she brought me coffee from the teacher’s lounge so, as far as I’m concerned, she can do whatever she wants for pretty much the rest of the day."
    "Sure, I imagined that we’d kind of ease into her intro instead of just letting her walk to the front of the room and start teaching a bunch of girls who have likely forgotten by now how school is supposed to work-"

    if bonus == True:
        "But it’s not like this changes my itinerary at all. In fact, it even takes some of the pressure off of me in that I can now hang out with the girls like I’m some sort of oversized, middle-aged high school student."
    else:
        "But it’s not like this changes my itinerary at all. In fact, it even takes some of the pressure off of me in that I can now hang out with the girls like I’m some sort of oversized, middle-aged college student."

    "I hope the new teacher asks me to stay after class."

    ima "Knowledge! Or, as I like to call it, {i}the key to knowing stuff...{/i}is the third most important thing to fill your body with."
    ima "The first of which is water, since us humans are comprised of roughly 75ish%% of it-"

    scene imaniclassintro2
    with dissolve

    ima "And the second?"

    "Imani pauses for dramatic effect, but everyone seems to be more confused than anything else."

    ima "The second..."
    ima "Is friendship."

    scene imaniclassintro3
    with fade

    mak "Excuse me. I have a question."
    ima "Yes! Ask me anything you’re curious about! I’m a repository of useful information!"
    mak "Pardon my language but, who the hell do you think you are?"

    scene imaniclassintro4
    with dissolve

    mi "Woah there, Makoto! Ya can’t just go around askin’ teachers stuff like that! Not everybody’s as forgiving as Sensei is!"
    mak "We haven’t even confirmed if she’s an actual teacher yet. For all we know, she could be some random woman who just waltzed into class with a desire to {i}try it out.{/i}"
    mi "But...I coulda sworn I heard ya talkin' about how she was the stand-in for Miss Watabe the other-"
    mak "Teaching’s no small task, Miku. It’s not something a person can just decide they want to do one day."
    mi "..."

    scene imaniclassintro5
    with dissolve

    mi "Okay but like...do they {i}have{/i} to decide that? Cause I feel like our normal teacher hasn’t even gotten to that point yet."
    mak "Nonsense. Sensei just has unshakeable faith in me as a student and has decided to take the backseat in actual instructing so that I have more room to grow."

    "Oh, Makoto. I thought you were smarter than that."

    scene imaniclassintro6
    with fade

    ima "Hey, I get the frustration. It doesn’t take a rocket scientist to figure out you might just think I’m some random woman who got lost and started scribbling things on a chalkboard."
    mak "You didn’t even figure that out. You’re just paraphrasing what I said to my friend just now."
    ima "What is your name, child?"
    mak "I’m not a child!"
    ima "What is your name, not-child?"
    mak "I’m...hah. Makoto Miyamura."

    scene imaniclassintro7
    with dissolve

    ima "Ahh, so {i}you’re{/i} the one who was brought up at the maid cafe."
    mak "Maid cafe? What are you talking about?"

    scene imaniclassintro8
    with dissolve

    ima "What’s the issue here, Makoto? Is this more of a “Don’t interfere with how my favorite teacher does things” problem? Or a “You’re stealing my job” problem?"

    scene imaniclassintro9
    with fade

    mak "It’s an “I don’t even know who you are” problem. I didn’t hear anything from Sensei or the principal about a new teacher, and I {i}always{/i} hear about things like this before they happen."
    ima "Apparently not! Because I’ve known about this all week and Sensei’s known about it for like, twelve hours or something."
    mak "Are you a student teacher, then? Is that what’s going on?"
    mak "And, if that’s the case, shouldn’t you maybe...introduce yourself before telling us to put {i}friendship{/i} into our bodies? Like, how would that even work?"
    mi "Yeah. I love Makoto, but I don’t really know how I feel about her gettin’ all up in my body, new teacher lady."

    scene imaniclassintro10
    with fade

    ima "To whom it may concern! Which...I guess is all of you."
    ima "My name is Imani Imai and I’m going to be your new student teacher."
    ima "You don’t have to call me Sensei or anything since that would probably get confusing really fast."
    ima "In fact, you don’t even have to treat me like a teacher if you don’t want to! I’m of the belief that minds are better molded when done so on a casual, informal level."
    ima "I’ve been sent here to keep you guys up to snuff on education stuff, while also keeping the school off of Sensei’s back for extremely understandable reasons!"

    scene imaniclassintro11
    with fade

    r "Are you getting fired, Sensei? Because this teacher just seems like a better, cuter version of you so far."
    s "I don’t know if I’d compare her to {i}me{/i} just yet. But, at least from what I figured out yesterday, she’s not exactly an average teacher either."
    r "What do you mean?"

    if bonus == True:
        s "Well, the first time she came into my office, she accused Miss Watabe and me of “fucking” each other."
    else:
        s "Well, the first time she came into my office, she asked Miss Watabe about her girlfriend's favorite breed of dog."

    scene imaniclassintro12
    with dissolve

    if bonus == True:
        r "Oh my god. {i}Are{/i} you? Does Nodoka know?"
        r "Wait, was Nodoka {i}there?{/i} Did all three of you-"
    else:
        r "Oh my god. Does Nodoka know about this?"
        r "Nodoka loves discussions relating to other peoples' dogs."

    s "No, Rin."

    "Not yet, at least."

    if bonus == True:
        sa "Why would...she assume something like that?"
    else:
        sa "Why would...she ask you something like that?"

    scene imaniclassintro13
    with dissolve

    s "Because she’s weird? I don’t know what you want me to say here."
    s "She’s already taken over the room and she’s only been here for five minutes. She’s clearly a force to be reckoned with."
    sa "You just...seem to know her pretty well for...someone you just met..."

    scene imaniclassintro14
    with dissolve

    s "Hm."
    s "I guess that’s not entirely incorrect."
    s "I’m sure you’ll all be saying the same thing about her soon enough, though."
    s "Just look at Makoto, she’s already coming to terms with it."

    scene imaniclassintro15
    with fade

    mak "Listen! All I’m saying is that it’s not wrong for me to doubt the legitimacy of this without seeing your papers!"
    ima "Woah there! You already taking shots at my heritage, Makoto?! I’ll have you know I’m a legal citizen of Japan, thank you very much!"
    mak "Your {i}assignment{/i} papers! I couldn’t care less about your citizenship paperwork!"

    scene imaniclassintro16
    with fade

    ima "Which brings us right to today’s discussion- dual citizenship! Thank you, Makoto, for the excellent segue!"
    mak "It wasn’t a segue! And why is this your choice for a first lesson in our class?!"
    ima "So, now that we have an actual topic to go off of, how about we dive in a little deeper?"
    ima "I figure that just having one good discussion every morning is a much better way of getting you guys to learn stuff than forcing you to read textbooks and all that junk."
    mi "Oooh! I’m sorry, Makoto, but I’m startin’ to like her! She’s speakin’ my language all of a sudden."
    ima "So, dual citizenship...what is it?"
    ima "Well, just as the name implies, it’s when one person is registered as a legal citizen in two separate countries or states or- you know, basically, just two different places."
    ima "But Japan is actually one of the few nations that {i}doesn’t{/i} recognize dual citizenship."
    ima "This means that mixed people like me are forced to choose one before we turn 22."
    f "So...does that mean you legally count as 100%% Japanese now? I don’t think I’m understanding the...legality of this rule."

    scene imaniclassintro17
    with dissolve

    ima "Great question and nice to meet you! What’s your name?"
    f "Futaba...Fukuyama."
    ima "Well, Futaba, I don’t blame you for not understanding the rules since they’re pretty inconsistent and nonsensical, but I’ll try to break down a few more aspects of it for you."
    ima "I’m 100%% Japanese on a strictly legal basis because I was forced to surrender my Ghanaian nationality in order to count as a full citizen here."
    ima "Well, {i}forced{/i} probably isn’t the right word since it was something I chose to do, but still! Surrendering a nationality you’re born with is just one of several ways to legally {i}become{/i} Japanese."

    scene imaniclassintro18
    with dissolve

    ima "Foreign adults can acquire that nationality by living in the country for over five years, whereas adopted children from foreign countries only have to live here for one."
    ima "It works in reverse, too. For example, if I registered for dual citizenship in Ghana, a country that allows it, I would automatically {i}lose{/i} my Japanese nationality despite being a current citizen."
    ima "What a world we live in! Where the country we live in can just decide we’re not a real citizen anymore because we want to exist in two places at once."
    ima "So! Do we have anyone else from mixed backgrounds here? Or am I just going to stick out even more than I already do?"

    scene imaniclassintro19
    with fade

    if bonus == True:
        ki "I’m kind of zoning out because this discussion is boring, but I just wanna say right now that I really want to fuck the new teacher."
        n "You want to fuck every teacher, Kirin."
    else:
        ki "I want to watch the third season of Seinfeld with the new teacher."
        n "You want to watch that show with every teacher, Kirin."

    scene imaniclassintro20
    with dissolve

    if bonus == True:
        ki "Well, I mean...not {i}every{/i} teacher..."
        ki "Just...the two that are in this room."
        ki "I’d probably be down to let Miss Watabe dom me too since I’ve heard she’s into that sort of thing."
        n "Wakana? Yeah, I can see that."
    else:
        ki "It's a good show."

    scene imaniclassintro21
    with dissolve

    if bonus == True:
        n "Hey! How about we make a deal? You can get the new teacher and I can get Sensei!"
        n "Then, when I’m no longer able to suppress the aggressive hormones raging inside of my body, we can have hot group sex every Friday night."
        ki "Does it even count as “group sex” if it’s just two couples fucking each other in the same room?"
        n "Is it a group of people?"
        ki "Yeah."
        n "Is there sex?"
        ki "Uhh, yeah."
        n "Well, then that should answer all of your questions."
    else:
        n "Hey! How about we make a deal? {i}I'll{/i} watch the third season of Seinfeld with you and you can give me your stuffed Pikachu plushie thing!"
        ki "Noooooooo my mommy bought me that when I was little."

    scene imaniclassintro10
    with fade
    play sound "bell.mp3"

    ima "Okay! There’s the bell!"
    ima "Everybody get ready for gym class! Unless you’re too embarrassed to change in front of others or just...don’t want to or something!"
    ima "I don’t know! Do whatever it is you normally do when the real teacher is leading the class!"
    ima "I’m going to go find a burrito somewhere!"
    ima "Class dismissed!"

    scene black
    with dissolve2

    "Imani rushes out of the classroom and is quickly followed by a bunch of girls who still don’t understand if she’s really going to stick around or if this was just a long, elaborate joke."
    "One notable student {i}does{/i} wind up sticking around after everyone else leaves, though."
    "........."
    "......"
    "..."

    scene imaniclassintro22
    with dissolve2

    s "Maya? What’s up?"
    s "Are you here to tell me some secret about another cycle coming to a close or something like that?"
    m "No. I’m here to remind you of another Secret Santa exchange so you don’t wind up disappointing some other girl the way you disappointed me last Christmas."
    s "Wait, did I actually disappoint you?"
    m "Of course. But you disappoint me every single day, so I didn’t think it was a particularly big deal."
    s "Well first off, I apologize for existing."
    m "It’s okay. I forgive you."
    s "Second, how do you know about this year’s Secret Santa? I thought everything happening was {i}new{/i} to you now."

    scene imaniclassintro23
    with dissolve

    m "Because it’s been written on the board for two weeks and you were asleep when we drew names."
    m "You’re not very observant, are you?"
    s "Not about things I’m not particularly interested in, no."
    s "So, who do I have this year?"

    scene imaniclassintro24
    with dissolve

    m "Not a clue. But we shoved the only unclaimed slip of paper into your podium earlier this morning before our new...student teacher showed up?"
    s "How do you feel about that, by the way?"

    scene imaniclassintro25
    with dissolve

    m "I feel as though I may be forced to actually learn something for the first time in a very, very long time. And I worry that my hands may no longer remember how to hold a pencil for any tests assigned to us."
    s "Well, you sure knew how to hold one when you filled a fake journal with information on yourself and all of your-"

    scene imaniclassintro24
    with dissolve

    m "I’m leaving now. I’ll see you later tonight."
    s "Wait, tonight?"
    m "I’m sleeping over for the mini Christmas party we’re having at your house."
    s "How do you know about all of these things without secret knowledge from the future?"

    if bonus == True:
        m "Because I talk to people about things other than just sex and boobies."
    else:
        m "Because I talk to people about things other than hugs."

    m "Anyway, bye."
    m "Make sure that whatever present you decide to buy for the person unfortunate enough to be assigned to you isn’t one that will get immediately tossed into the trash."
    s "Thanks, Maya. I’ll make sure to pick up a separate present for you too and-"

    scene imaniclassintro26
    with dissolve
    play sound "slidedoor.mp3"

    s "Okay. Good talk."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene imaniclassintro27
    with dissolve2

    "Huh."
    "Well, at least it’s not Maya this time."
    "But what the hell am I supposed to buy for Miku?"
    "I don’t think it’ll be {i}too{/i} hard since I know she likes...soccer and...running and stuff- but neither of those things sound like they’d make particularly exciting gifts."
    "Oh well."
    "I’ll probably just wait until the last minute and choose whatever I can find."
    "Or, if I’m really struggling, just get her a gift card or something."
    "I don’t care what anyone says about how gift cards are {i}impersonal{/i} or bad gifts or anything."
    "Nothing says “I care about you” more than trusting someone with the free will to make their own decisions rather than making one for them, in my opinion."
    "But, this is clearly no time for an inner debate like that since I’m now acutely aware that someone {i}else{/i} is standing in front of my desk."

    if ayane_lust >= 20:
        scene imaniclassintro28
        with fade

        ay "Surprise Ayane visit! Time to love me!"
        s "You need to stop skipping gym class to come and see me. People are going to realize what your game is."

        scene imaniclassintro29
        with dissolve

        if bonus == True:
            ay "Everyone’s known my game since the start, Sensei! I’m like the Ami that people won’t think is weird for liking you so much since you and me aren’t {i}actually{/i} related."
        else:
            ay "Everyone’s known my game since the start, Sensei! Some people have already started lending me bones!"

        s "So, what’s up then? If this is about the Secret Santa thing, Maya just reminded me."

        scene imaniclassintro30
        with dissolve
        stop music fadeout 25.0

        ay "Well...it’s not about that. But it is {i}kind of{/i} a present, I guess?"
        ay "I just wanted to give you a sneak peek of something so I could get your thoughts on it before everyone else sees it."

        scene imaniclassintro31
        with dissolve

        ay "Plus, we haven’t really been spending any time in school {i}alone{/i} lately and...yeah."
        s "It’s kind of hard to find alone time when I’m surrounded by an ever-increasing number of girls."
        s "So, what is it you wanted to show me?"

        scene imaniclassintro32
        with dissolve

        ay "Well, I’m not going to just {i}tell{/i} you! That would ruin the surprise!"
        ay "You’ll have to follow me if you want to see it!"
        s "Then...lead the way, I guess?"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ christmastwo3 = True

        jump ayanelust20

    else:
        scene imaniclassintro33
        with fade

        s "Oh, Io. What’s up? Hiding from the rest of the girls again?"
        i "Something like that..."
        s "Did you need something?"
        i "Yeah, but I’m trying to figure out how to say it in a way that doesn’t sound annoying or cringeworthy or like...lame? Weird? I don’t know."
        s "Well you’re already off to a rocky start, but that’s basically what I’ve come to expect from you by now."

        scene imaniclassintro34
        with dissolve

        i "I...uhh..."
        i "Okay, so...hypothetically, if a girl that liked you made you a Christmas present and wanted to give it to you, would you rather she be honest about it? Or would that come off as like...overbearing?"
        s "If this is about me coming over to see what you made for me after school, I already planned on it."

        scene imaniclassintro35
        with dissolve

        i "What? How did you know about that?"
        s "Uta told me yesterday when I went to the maid cafe with Imani and Wakana."
        s "Was she...not supposed to do that?"

        scene imaniclassintro36
        with dissolve

        i "Uta did?...Huh. That’s weird."

        "If I’m remembering correctly, I’m pretty sure Uta said that Io {i}asked{/i} her to tell me about it, too- which I’m suddenly realizing was probably not the case."

        scene imaniclassintro37
        with dissolve

        i "So...Uta aside, you’ll come then?"
        s "I will."
        i "And you won’t think I went way overboard when you see what I made?"
        s "Well...I mean, that kind of depends."
        s "I’m sure that as long as I can carry it home, whatever you made will be fine."
        i "..."
        s "..."
        i "And if you can’t carry it home?"
        s "..."
        s "Io, what did you make me?"

        scene imaniclassintro38
        with dissolve

        i "A-Anyway! See you later! And remember that you can always regift stuff if you don’t like it and I won’t blame you at all since I definitely went way overboard!"
        s "Io, what did you-"

        scene imaniclassintro39
        with dissolve
        play sound "slidedoor.mp3"

        i "Nothing! Bye!"
        s "..."

        scene black
        with dissolve2
        stop music fadeout 10.0

        "Well, looks like my first Christmas present of the year might wind up being a little more than I bargained for."
        "Which, need I remind you, was absolutely nothing."
        "But hey, if Io wants to bust her ass making some sort of crazy gift for me, she can feel free."
        "Here’s hoping that it provided at least some sort of distraction for her."
        "And here’s hoping that I didn’t accidentally get Uta in trouble by revealing I knew about this gift from the get go."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ ayanelust20skip = True
        $ christmastwo3 = True

        jump christmastwo4

label christmastwo4:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
scene christmastwomaid32
    with dissolve

    u "Not...for Uta-chan. "
    u "For normal Uta."
    s "Normal Uta?"
    u "Yeah..."
    s "You...do realize how this sounds, right?"
    u "What if I told you...I already called my parents?"
    s "Well, I’d first confirm that you didn’t tell them who I am or where I live. But after that, I’d-"

    scene christmastwomaid33
    with dissolve

    u "Uhh- actually! I forgot to mention that Io is going to be there too. And that...well, she’s the one who wanted me to ask you to come over in the first place."
    u "I just...went about asking in a really weird way, I guess. Hahaha..."

    if bonus == True:
        s "Yet again, lured into a false state of arousal by a tiny girl in a maid costume."
    else:
        s "Yeah, you should really focus on improving that part of yourself."

    scene christmastwomaid34
    with dissolve

    u "So...even if it wasn’t Io and it really was just me...you’d come?"
    s "Is that even a question? Of course."

    scene christmastwomaid35
    with dissolve

    u "I see..."
    s "..."
    s "Why are you being so weird all of a sudden?"
    u "Weird in what way?"
    s "Weird in the fact that you’re not mindlessly flirting with me and that you’re blushing like you’ve been in a sauna for three hours."
    u "I guess my face does feel a little hot..."

    scene christmastwomaid36
    with dissolve

    u "B-But that’s just because I {i}wanted{/i} you to think I was embarrassed about asking! I mean, why would I feel nervous about asking you to come over when you’ve been over so many times before?!"
    u "That would be totally weird! And it’s not like I have any intention of letting you put your hands on me or anything!"
    s "Okay, that’s getting back on track. But you still seem a little off and-"

    scene christmastwomaid37
    with dissolve

    u "A-Are you coming or not?! Io made you a Christmas present and it’s taking up too much space in our dorm!"
    s "Space? What space?"
    u "That’s exactly the problem! I had to crawl under a table just to get to my skirt this morning!"
    s "Have you considered, you know, storing your clothes somewhere that isn’t directly on the floor?"

    scene christmastwomaid38
    with dissolve

    u "Nonsense. The floor is where clothes are {i}supposed{/i} to go. If that wasn’t the case, it wouldn’t be so big."
    s "I’ll make sure to drop by, Uta. Whether or not Io is there."

    scene christmastwomaid35
    with dissolve

    u "Cool...yeah."
    u "Io will be really happy."
    s "And you?"

    scene christmastwomaid34
    with dissolve

    u "Me?"
    s "Yeah. You’re the one asking. I’m not just dropping by to make Io happy."
    u "..."
    s "..."

    scene christmastwomaid36
    with dissolve

    u "That’s for me to know and you to find out!"
    s "What?"
    u "I...I don’t know!"
    u "I’ll see you tomorrow!"
    s "..."

    scene black
    with dissolve2

    s "But..."
    s "We still haven’t ordered..."

    $ renpy.end_replay()
    $ uta_love += 1
    $ christmastwo2 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo3
...
```