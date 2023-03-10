# Repentance (Yasu)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yasu love greater than or equal to 10

* Event [The Hole That Swallowed Everything](./yasufirsthall.md) (Yasu) is completed)

* Event [Loser](./toukadorm5.md) (Touka) is completed)

* Event [Something, Somewhere](./makotowinterbeach4.md) (Makoto) is completed)



## Next events

* [Main: Operation: Firestarter](./day318.md)
* [Yasu: Sakura Season](./church10.md)

## Event properties

* Id: yasudorm10
* Group: Yasu
* Triggered by label: yasudorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->yasudorm->yasudorm10

## Official wiki page

[Repentance](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yasudorm10&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label yasudorm10:
    if _in_replay:
        scene dorm2

    play sound "knock.mp3"
    stop music

    "I knock on Yasu’s door and wait for her to answer."
    "Why? I have no idea."
    "But it’s a thing I do and now I have to live with the consequences."
    "And I don’t mean consequences in the sense that I think tragedy might befall me for simply doing this-"
    "But moreso in the fact that from this point on, I will be completely out of my element and, as such, out of control."
    "It’s rather interesting, really."
    "I normally feel like I have the upper hand when it comes to conversing with everyone who lives in this building. "
    "Let’s look at Touka, for example."

    if bonus == True:
        play sound "static.mp3"
        scene realtoukaimage with flash
        stop sound
        play music "shiningstarvocals.mp3"
    else:
        play sound "static.mp3"
        scene toukaolddis8 with flash
        stop sound
        play music "shiningstarvocals.mp3"

    "Touka is a girl who is not Yasu but sleeps in the same room as Yasu."
    "If you pay close attention to the image in front of you, you will see that she is frowning."
    "But why?"

    if bonus == True:
        "Is it because we have not done the sex to her yet? "
    else:
        "Is it because she missed the latest Game Grumps video?"

    "Probably not."

    if bonus == True:
        "Though I would not doubt that she has, on several occasions, had to contemplate whether or not the act of pleasuring herself in the same room as a semi-comatose half nun would be moral or not."
        "I would not think any less of her if she tried, but do not expect that she would have been able to do it to completion because of how strange it would likely be."
        "Masturbatory tangent aside, Touka is probably frowning because she is one of the girls that I typically have the upper hand with."
        "Not just because my hands can reach higher things than hers, but because she is a weak little girl and I am a big strong man."
        "I will do the sex to her and make her smile happen."

    scene dorm2
    play sound "knock.mp3"
    stop music

    "I knock on Yasu’s door and wait for her to answer."
    "Why? I have no idea."
    "But it’s a thing I do and now I have to live with the consequences."

    ya "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "………"
    "……"
    "…"

    scene yasufirstdorm1
    with dissolve
    play music "undersea.mp3"

    ya "Good morning, Sensei."
    s "It’s nighttime, Yasu."
    ya "Is it? I suppose I lost track of time in the midst of prayer."
    ya "It would not be the first time I’ve let an entire period of day slip by without noticing."
    s "Fair enough. Don’t you want to turn the lights on, though?"
    ya "Not particularly. "
    ya "There is only one light that matters to me. The rest of them are nothing but hindrances meant to-"
    s "Before you continue that, I just want to make sure you’re going to put it in terms that I understand and not some weird religious way."
    ya "Sunlight hurts my eyes and my skin."
    ya "It makes coming to[school] very difficult sometimes."

    scene yasufirstdorm2
    with dissolve

    ya "But I am a good girl and will do what God tells me to do."
    s "Well I’m happy to hear your god is concerned about your education."

    scene yasufirstdorm3
    with dissolve

    ya "He is more concerned with spreading the message of His love than of my menial general studies."

    if bonus == True:
        ya "There are no better candidates for angels than [adolescent] girls, untouched by the evils of man and untainted by the stink of life."
        s "Well, uhh...good luck."
        s "I wouldn’t count on everyone being {i}untainted{/i}, though."
        ya "Even {i}if{/i} they’ve already been contaminated, they are not so broken that they are beyond repair."
        ya "Life is long. And if they wish to atone for any misdeeds they may have done, now is the best possible time to begin their repentance."
        ya "They can all still be saved. And it is my duty as an angel in training to usher them to safety like the confused sheep they are."
        s "Just...don’t repeat any of that out loud to them or it will be even harder for you to make friends than it is for Touka."
    else:
        s "He should start a mailing list."
        ya "A mailing what?"
        s "It's a thing that lets you email a bunch of people at once."
        ya "What is an email?"
        s "..."
        ya "I am lost without you, Sensei."

    if bonus == True:
        play sound "static.mp3"
        scene realtoukaimage with flash
        scene yasufirstdorm4 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown with flash
        scene yasufirstdorm4 with flash
        stop sound

    ya "LET US WALK!"
    s "Woah, what?"
    ya "I TIRE OF THESE WALLS!"
    ya "LET US GO SOMEWHERE ELSE!"
    s "We don’t have to hang out here, but I’d certainly appreciate it if you’d stop yelling."

    play sound "static.mp3"
    scene yasufirstdorm5 with flash
    stop sound

    ya "I can do that."
    ya "I’m sorry, Sensei. A sudden urge came over me and I was not able to suppress it."
    ya "The first hours after I pray are the hours when the noises become loudest."
    ya "I can’t help it if they take over sometimes."
    ya "I hope it will not ruin our blossoming friendship or any chance you have of following me in the future."

    scene yasufirstdorm1
    with dissolve

    ya "But for now, I shall follow {i}you{/i}."
    ya "I leave you in charge of taking me somewhere exciting."
    s "That’s a big ask when I know your preferred hang out spots are a church and directly in front of your bedroom wall."
    s "I’m not really sure if we find the same things “exciting.”"
    ya "Hmm...I suppose we most likely don’t."
    ya "Oh, here is an idea."
    ya "How would you like to return to the spot where we first met?"
    s "Great idea. Nothing says exciting like the place where I watched you cause the most innocent girl in my class to break out in tears."

    scene yasufirstdorm6
    with dissolve

    ya "Not all tears are bad, Sensei."
    ya "Even if my words brought them to her eyes, I’m sure they were for happy reasons."
    ya "For she had likely heard something she’d been waiting to hear for a very long time."
    s "What does that-"

    scene yasufirstdorm5
    with dissolve

    ya "But for now, let us go! Adventure awaits! "
    s "…"

    scene black with dissolve

    s "Okay, I guess."

    "Yasu puts her shoes on and the two of us make our way out of the dorms and into the streets."
    "I’ve been to the park where I met Yasu on several other occasions since then, so I know where we’re heading and lead the way."
    "There isn’t much discussion on the way there, but it’s not really an uncomfortable silence or anything like that."
    "In fact, the silence is probably even more comfortable than the parts of the night where we're talking."
    "Maybe Yasu and I should just remain quiet all the time?"

    if bonus == True:
        "It might be a little boring at first, but at least I won’t be tempted into joining a cult based on the promise of transferring spiritual warmth through my penis."
    else:
        "Or, at the very least, maybe she could stop making airplane noises."

    "I’ve still yet to wrap my head around that."
    "………"
    "……"
    "…"

    scene yasufirstdorm7
    with dissolve

    s "…"
    ya "…"
    s "Did you really have to bring the umbrella?"
    ya "I must have instinctively grabbed it thinking it was morning again."
    s "You’re still on that?"
    ya "I suppose so."
    ya "It’s a bit of a reflex at this point, though. I’ve despised the sun ever since I was a little girl."
    s "I somehow have a hard time imagining a younger version of you."
    ya "Why is that?"
    s "You’re just so...eccentric now that I can’t imagine a time where you weren’t like that."
    s "And I have a hard time believing you’ve been a religious fanatic since you were born."

    scene yasufirstdorm8
    with dissolve

    ya "Fanatic sounds a little hurtful."
    ya "It makes it sound like I’m over the top or irrational."
    s "Oh, I know how it sounds."
    ya "I spoke about it at the church, but there are things etched into us at birth that play a great role in determining our purpose. The people we hope to become."
    ya "Do you think this version of me is the result of a single event and not simply the way I was designed?"
    s "So...you {i}have{/i} been insane ever since you were born?"

    scene yasufirstdorm9
    with dissolve

    ya "That seems to be the consensus. "
    ya "If you were to ask anyone that knew me back then, I’m sure they would tell you you’re correct."
    ya "I am far from insane, though. "
    ya "I actually find myself to be more rational and level headed than anyone when I’m not listening to the voices trapped in the aether."
    s "Yasu, the reason so many people think you’re insane is very likely because you say things like that."
    ya "Having better hearing than anyone else makes me insane?"
    s "No, but thinking there are voices floating around in “the aether” kind of does."
    s "What does that even mean?"

    scene yasufirstdorm10
    with dissolve

    ya "You know what a {i}soul{/i} is, correct?"
    s "In the vague moral sense, yes. But in the religious one...kind of?"
    s "Something about an imaginary entity inside of you that contains your consciousness and history or whatever mumbo jumbo they use to trick kids into thinking there is an afterlife."
    ya "That is such a sad way to look at things."
    ya "The soul is not imaginary. Though, it’s a bit more complicated than an invisible stream of consciousness. "
    ya "If your body is the container that stores your thoughts now, what would happen if you switched containers?"
    ya "What if you no longer had a use for your body as you were able to simply store your thoughts in the world itself?"
    s "…"
    s "Isn’t that an invisible stream of consciousness?"

    scene yasufirstdorm11
    with dissolve

    ya "Yes. But like I said, it’s more complicated than that."

    scene yasufirstdorm8
    with dissolve

    ya "Some fake religions certainly do deceive people with the promise of souls moving into the afterlife."
    ya "But as I know with absolute certainty, for I see the light and hear the light, the afterlife is all around us."
    ya "There is a second plane of existence that lies directly on top of our current plane."
    ya "It’s just impossible to see with your eyes only partially open."
    s "So basically, once someone dies, their consciousness exits their body, but continues to exist outside of it?"

    scene yasufirstdorm7
    with dissolve

    ya "That is the gist of it."
    s "Yeah, we should take you to a hospital. Let’s go."
    ya "Oh, stop. What makes this possibility any less believable than a fortress in the clouds or being reborn as a plant?"
    ya "To die is to disappear. And since it’s impossible to fully vanish, there is no death."
    s "What you’re saying isn’t exactly {i}less{/i} believable. It’s that none of those things are believable in the first place."
    ya "So you are one of those people who believes in eternal darkness succeeding the end of traditional life?"
    s "I guess you could say that. Yeah."
    ya "And are you happy with that way of thinking?"
    s "I’m not {i}unhappy{/i} with it."
    ya "You are very good at dodging questions you find inconvenient, aren’t you?"
    s "It’s definitely one of my strengths."
    ya "What can I do to have you reconsider?"
    ya "Would hearing the disembodied whispers of friends or lovers past grant you the solace you need to try a new system of beliefs?"
    ya "To step out into the night and spread your arms, letting tendrils of the winter winds wrap around you and embrace you the way you long to be embraced."
    ya "We are sensitive creatures, you and me. You and me and everyone else."
    s "I am far from sensitive. “Detached” is probably a better word."
    ya "You and your silly textbook definitions of words..."
    ya "I do not mean sensitive emotionally and physically."
    ya "I mean sensitive in the fact that our entire existences could be entirely rewritten by even the most minor of events."
    ya "If you heard the things I hear, you would believe. And I would not have to ask you to follow."
    ya "You would simply fall into line alongside me and spread His word for the rest of the world to hear."
    ya "We’d approach the end of days together, and I would carry you to the place where all is safe with the help of my new wings."
    ya "And yet you still feel inclined to disbelieve me."
    s "Yes. Because you are crazy."
    ya "If believing in what I know to be the truth is crazy, I fear for the rest of this city."
    ya "I fear the thoughts they must have. The lack of closure. The sensation of a loved one wrapping around them as they make their way down the street."
    ya "I fear those who will not accept messages from the one person in the world who can carry them."
    ya "I fear everything and nothing at all."

    scene yasufirstdorm12
    with dissolve2

    ya "I fear you."
    s "Me?"
    ya "You. Surrounded by a thick blanket that forces back the whispers of someone so lonely it shakes the earth to the core."
    ya "You. Who not only denies what he has seen, but attempts to carve out paths in all directions and separate his body into pieces so he may walk down all of them at once."
    ya "You. Who is blessed and cursed at the same time. Who is both the purest entity I have ever seen and a person so tainted that it’s a miracle you can still walk."
    ya "You, who lives. "
    ya "You exist as both my greatest fear and my greatest hope. For all that I am will surely rely on you before you are ready to be relied on."
    ya "That is why I fear everything and nothing at all."
    ya "Not because I can hear the whispers and wishes in rivers of lost souls."
    ya "Not because I can feel the pain in every person and every place."
    ya "But because I can not feel you."

    scene yasufirstdorm13
    with dissolve2

    ya "…"
    s "…"
    s "Are you sure you don’t want to go to the hospital?"
    ya "Hehehe~"
    ya "I’m sure."
    ya "I’m a rational girl. And I’ve already been a little pushier about earning your trust than He wants me to be."
    ya "But I can’t help but worry about the end of the world when I can feel it looming on the horizon."
    ya "Before long, the snow will melt. "
    ya "The seasons will change."
    ya "And His slumber will come to its end."
    ya "Perhaps it is only then that you will learn to accept the truth in everything."

    scene yasufirstdorm14
    with dissolve

    ya "I am not crazy, though."
    ya "I am chosen."
    ya "I am the sole bearer of the word of truth and the sole believer of the light. "
    ya "And through the gift of the divine and the aetheric whispers of all else who have learned the truth-"
    ya "I will teach you. "
    ya "I will give you myself and you will give me yours."

    if bonus == False:
        s "No thank you."

    ya "And then we will give it all to him."
    ya "Praise be."
    s "…"
    ya "…"
    s "Sorry, just still figuring out what the hell I’m supposed to add to this conversation."
    s "I expected things to get a little weird but I didn’t really expect you to go on a rant like that."
    s "Though, I probably should have, considering that’s really all you ever do around me."
    ya "I can’t help that I have many things to say, Sensei. I exist to deliver messages and can not be faulted for being good at my job."
    s "I hope you’re getting paid well, at least."
    ya "Not yet. But it will all be worth it in the end."
    ya "I hope you will be there to see how beautiful I become."

    scene black
    with dissolve2

    "Yasu says some more stuff about her god or whatever but I zone out and stop listening almost immediately."
    "Frankly, I’ve been doing that for basically all of our walk tonight."
    "It’s not like I’m intentionally ignoring her, though."
    "And it’s also not like what she’s saying is boring me to the point where I no longer care."
    "I just can’t manage to prevent my mind from trailing elsewhere."
    "And before long I get lost."
    "Lost in the artistic sense of the word."
    "And before I know it, I’m back at the dorm, wishing her sweet dreams."
    "Though, I doubt she’ll dream of anything."
    "And if she does, I doubt it will be sweet."
    "I go home."

    $ renpy.end_replay()
    $ yasudorm10 = True
    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

                    ############################################
                    ##########        ROOM 10         ##########
                    ############################################

label kirindorm:
    if kirin_love >= 10 and day271 == True and day != 3 and utadorm5 == True and iodorm5 == True and kirindorm10 == False:
        jump kirindorm10
    if kirin_love >= 15 and kirinsoccer20 == True and day != 3 and kirindorm15 == False:
        jump kirindorm15
    if kirin_love >= 20 and kirindorm15 == True and day != 3 and kirindorm20 == False:
        jump kirindorm20
    if kirin_love >= 25 and norikodorm25 == True and day != 3 and kirindorm25 == False:
        jump kirindorm25
    else:
        jump kirindormgen

label kirindormgen:
    play sound "knock.mp3"

    ki "Come in!"

    scene kirindormgen
    with fade

    "Kirin invites me in and the two of us proceed to spend the next hour or two laying on her bed, discussing the different bilateral and multilateral trade agreements of Japan."
    "Just kidding."
    "We lie there and talk about life."
    "The good parts of it, the bad parts of it, and the parts of it that ooze so much mundanity that they may as well not even exist at all."
    "For someone so routinely toxic or manipulative or whatever she's trying to trick herself and everyone else into thinking she is, she certainly has a lot of well-informed opinions on the world."
    "But I guess something like that is easy when the world is such a terrible, worthless place."
    "Sometimes, I feel like the two of us wish we could destroy the world and just float around in the ether until we suffocate and die from lack of oxygen."
    "But then again, it could just be me."
    "So I shall continue to dream of a world without anything-"
    "And Kirin will continue to suffocate in her own, special ways."

    scene black
    with dissolve

    "One [[non-sexual] thing that happens when two people lie in bed for X amount of time is that one of them normally grows tired."
    "Not tired of the same mundanity I mentioned previously, but tired in general."
    "Tonight, that person is Kirin."
    "The conversation carries on until she can no longer keep her eyes open."
    "She trails off in the middle of a discussion and passes out."
    "I think about waking her up to sate my boredom but ultimately decide against it, pulling her blanket over her and turning the lights off as I head back home."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label norikodorm:
    if noriko_love >= 5 and kirindorm10 == True and convenience1 == True and norikodorm5 == False:
        jump norikodorm5
    if noriko_love >= 10 and convenience5 == True and kirindorm20 == True and norikodorm10 == False:
        jump norikodorm10
    if noriko_love >= 20 and norikospecial20 == True and norikodorm20 == False:
        jump norikodorm20
    if noriko_love >= 25 and convenience25 == True and day != 3 and norikodorm25 == False:
        jump norikodorm25
    else:
        jump norikodormgen

label norikodormgen:
    play sound "knock.mp3"

    n "Come in, Sensei!"

    scene norikodormgen
    with fade

    "I head into Noriko's room to be immediately greeted by a big hug and a kiss on the cheek."

    if bonus == True:
        "As you probably know by now, I'm not the biggest fan of actual affection. But at least she's able to do all of these things without making me feel strange about it."
        "Despite the notable gap in our ages, there's a clear, unique connection between us that even I have a hard time comprehending."
        "It's possible that's just this body's old memories banging against the bars of the prison I forced them into, but it could also be that Noriko's just...different."
        "So I'll continue to spend time with her."
        "Not just to discover why I might be feeling this way, but because the act of discovering in itself is inherently enjoyable."
    else:
        "I could have done without the kiss part, but I'm not about to deny a nice, warm hug from one of my favorite people."

    scene black
    with dissolve

    "The two of us hang out under the kotatsu, conversing about random things and treating whatever television show she put on as white noise."
    "She playfully kicks at my legs from time to time, sort of like how I'd expect a little sister to if I was fortunate enough to have one."
    "I guess Noriko's the closest I'll ever come to that, though."
    "So I might as well enjoy this sensation now, while it still lasts."

    if bonus == True:
        "Because who knows if she'll want to do this when (and if) she ever grows old?"

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko's affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirinhall:
    if chapthreeactive == True:
        scene kirinsummer2hallgen
        with dissolve
    else:
        scene kirinhall1
        with dissolve

    ki "Thank fucking God. I was dying of boredom."
    ki "Please, {i}please{/i} do something with me before my brain starts to ooze out of my ears."
    s "I will certainly do my best to prevent that from happening."
    s "Did you want to go into your-"
    ki "No. Let's talk out here."

    "Kirin and I spend the night in the hallway instead of going into her room for whatever reason."
    "I get feeling cooped up sometimes, but what is it about standing around in the hallway that seemed so alluring to her tonight?"
    "Oh."
    "Oh, okay. I get it."
    "She probably just wants the others to see me hanging out with her."
    "Or at least that's what I imagine is going through her head."
    "Regardless, we talk for an hour or so before deciding to call it a night, and I find myself heading back home having accomplished virtually nothing today."

    scene black
    with dissolve
    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label norikohall:
    if chapthreeactive == True:
        scene norikosummer2hallgen
        with dissolve
    else:
        scene norikohall1
        with dissolve

    n "Hey! We made eye contact so that means you have to hang out with me now."
    s "I had no idea such a rule existed."
    n "It exists and if you break it, I get to cut your arms off and wrap them around myself so I can be eternally hugged."
    s "You're a fucking psychopath, Noriko."
    n "But I'm {i}your{/i} psychopath."

    "Noriko and I spend the evening hanging out in the hallway, doing nothing in particular."
    "Some of the other girls wind up walking by and seeing us chatting."
    "I can tell that they want to get involved as well, but either out of respect for Noriko (Or for fear of her existence), they abstain."
    "Before I know it, it's almost midnight and I can already hear Ami scolding me for taking too long to get home..."

    scene black
    with dissolve
    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label kirinfirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label yasudorm:
    if yasu_love >= 10 and yasufirsthall == True and toukadorm5 == True and makotowinterbeach4 == True and yasudorm10 == False:
        jump yasudorm10
...
```