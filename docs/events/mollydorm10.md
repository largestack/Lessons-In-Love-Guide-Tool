# The Dark Entity (Molly)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Molly love greater than or equal to 10

* Event [Torrent of Power](./mollydorm5.md) (Molly) is completed)

* Event [Something Out of a Nukige](./mollycafe10.md) (Molly) is completed)



## Next events

* [Main: What's Done is Done](./beachvacation1.md)

## Event properties

* Id: mollydorm10
* Group: Molly
* Triggered by label: mollydorm
* Triggered by branch label: mollydorm
* Triggered by path: mollydorm->mollydorm10

## Official wiki page

[The Dark Entity](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollydorm10&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm10:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait to see if she’s around."
    "I can hear the sound effects from some game or anime going off in the background, so I imagine she is."
    "Tsuneyo doesn’t seem like she would be the type to spend her free time on that, so process of elimination really only leaves the one I came here to see in the first place."

    mo "Who goes there?!"
    s "Your teacher."
    mo "Oh, Master!"
    mo "You may enter! "

    "I grab the handle and attempt to open the door, but it appears to be locked."

    s "I can’t enter if the door is locked, Molly."
    mo "Oh. Uhhh, crap. Give me a second. "
    mo "I’m in the middle of a thing in a game."
    s "Can’t you just pause it?"
    mo "Pause it? What year is this, 2005?"
    mo "Have I activated my time-jump ability on accident?!"
    s "Just...hurry up and finish your game. It always feels strange standing in the middle of the hallway here."
    mo "Roger! Just gotta pop my CD’s and..."
    s "…"
    mo "…"
    s "…"
    mo "Done!"

    "I hear a set of frantic footsteps clopping against the floor as Molly rushes to the door and pulls it open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "What ever happened to the good old days where you were able to pause video games?"

    scene mollydormten1
    with dissolve

    mo "Those days have long since vanished, Sir. Lost like teardrops in the rain."
    s "Insightful. Is that a line out of a dating game?"
    mo "Probably, Sir. Though I don’t know which one off the top of my head."

    "Molly begins to play with one of the sleeves of her hoodie, incessantly plucking at the same spot over and over again."
    "She looks surprisingly cute in her...rather Irish-themed pajamas."
    "I can’t help but notice a rather fresh aroma permeating throughout the room as well."

    s "What is that smell? "
    mo "Me, Sir. Lemon scented shampoo. "
    mo "I just took a bath with Ami and Maya."
    mo "We were discussing the logistics of our upcoming campaign at the edge of the world."
    s "You mean the beach?"
    mo "I do, Sir. The beach is what it appears as to those not blessed with clairvoyance."
    mo "But people like you and I see it for what it truly is."
    s "I see it as a beach."

    if bonus == True:
        mo "You will know the meaning in time, Sir. A beach is not simply a beach when it is filled with blossoming [young]ladies like myself, Sir."
        mo "A true haven for degeneracy. A real set-up for top-notch H-scenes and lost bikini tops."
        s "I think you watch too much anime."
        s "{i}Though, I guess none of that sounds bad to me.{/i}"
    else:
        mo "But the fanservice, Sir!"
        s "You watch too much anime. There is no fanservice in Lessons in Love."

        "Or at least...not anymore there's not..."

    scene mollydormten2
    with dissolve

    mo "There is no such thing as too much anime. Especially when there are so many cute figures to collect."
    s "You’re still planning on getting more? You have plenty."

    if bonus == True:
        mo "Always, Sir. I will spend every penny I earn from the cafe and the pictures you purchase from me on objects to fuel my passion."
        s "Speaking of which, do you happen to have any of those pictures yet?"
        s "Plenty of time has passed by, so if you don't have any, you owe me a good excuse."

        scene mollydormten3
        with dissolve

        mo "I regret to inform you that I do not have any. Please accept the following excuse."
        mo "The stuff I ordered online just came in the other day and none of it really fits. I’m growing at an alarming rate."
        s "I’m having a hard time believing that. You’re one of the smallest girls in the class."

        scene mollydormten4
        with dissolve

        mo "Day by day, I stray further and further from the loli tag."
        mo "Who will ever love me if I become an average-sized girl?"
        s "I mean, I think you’d be cute either way."
    else:
        mo "Is that a problem, Sir?"
        s "Absolutely not. You are a grown woman with the money to fund her hobbies and I will enthusiastically support you if it means bringing you even slightly closer to happines."

    scene mollydormten5
    with dissolve

    mo "Thank you, Sir. I would return the compliment if you had one less dimension."
    s "You’re sure blushing a lot for someone who isn’t interested in 3D characters."

    if bonus == True:
        mo "Hormones, Sir."
        mo "They control the brains of [young]women like myself and make us act in ways we normally regret."
        s "Is that Mollyspeak for saying you’re getting turned on?"

        scene mollydormten6
        with dissolve

        mo "O-Of course not! What would the players think if an innocent virgin like me received her first H-scene in her initial update?!"
        s "I’m sure there would be plenty of players who’d be absolutely thrilled by that."

        scene mollydormten7
        with dissolve

        mo "Guh...I’m not ready to grow up yet..."
        mo "I haven’t even unlocked the fabled “first kiss” CG. "
        s "Kissing is overrated anyway. Once you get older, you’ll realize that relationships become more about sex than actual affection."
        s "Well, in my experience at least."

        scene mollydormten8
        with dissolve

        mo "Sir, this may be hard for you to hear, but I’m beginning to feel a bit uncomfortable with the direction this conversation is headed."
        mo "It’s one thing to talk about sex in games, but the real life kind sounds...scary."

        scene mollydormten9
        with dissolve

        mo "Though...I suppose if you were to use a command seal..."
        mo "I would be forced to oblige..."
        s "..."
        mo "..."

        "Molly is clearly starting to get a little flustered, so I might as well take things down a notch before I actually do something to hurt her."
        "Despite being a full on, admissible pervert when it comes to video games, she still clearly isn’t ready for the actual thing yet."
        "But I guess that’s not too hard to understand given the type of person she is."
        "It seems that Molly is willing to do virtually anything in order to separate herself from the real world. "
        "And if deflowering every character in every game she plays is how she wants to do that, more power to her."
    else:
        mo "I just remembered a really embarrassing thing that happened to me once!"
        mo "It was in the original version of the game, though!"
        s "Can you tell me about it?"
        mo "I can not, Sir! It is against the rules!"

    scene mollydormten10
    with dissolve

    mo "Oh! Sir!"

    if bonus == True:
        s "Wow. You got over that whole 'hormonal embarrassment' thing pretty quickly. "
    else:
        mo "I forgot to pick up my laundry from downstairs! Please help me carry all of it up here so my arms do not snap!"
        s "Just do it later. My legs feel all blah and I like how your room smells."
        mo "It {i}is{/i} later, Sir! I meant to do it at five different points today."
        s "Just get better at remembering stuff. I don't know what you want from me."
        mo "Unfortunately, I can not."

    mo "ADHD, Sir. There's not a lot of space on my hard drive so I need to constantly delete things to make place for new ones."

    if bonus == True:
        s "Gotcha. So what is it that captured your mind this time around?"
    else:
        mo "Oh, look. A chair. Chairs are for sitting."

    scene mollydormten11
    with fade

    "Molly moves several steps closer to her computer and starts to look at something in the corner of the room."
    "I stare at the same corner as well and see nothing, so I’m not quite sure what it is she’s looking at."

    mo "I actually have something I’d like to confide in you about."
    s "Oh? What’s with the sudden shift in tone?"
    mo "I will explain the step-by-step process as to how I wound up here."

    if bonus == True:
        mo "It all began with the mention of sex."
        mo "Which then made me think about nudity."
        mo "Which then made me think about my own personal experiences with nudity."
        mo "Which then reminded me of something I saw recently."
        mo "Which then somehow distracted me from thinking about the thing that made me think about all of those things in the first place."
        s "I’m...not sure if I follow."
        mo "Then I will get right to the point."
    else:
        mo "First, I was over there. Then I was somewhere in the middle. Now I'm here."
        s "I feel like the music is about to turn off."

    stop music
    scene mollydormten12

    mo "What is the right thing to do when you find out that someone you care about is hurting themself? "
    s "..."
    mo "I think I saw something I wasn’t supposed to see."
    mo "I don’t know what to do."
    s "..."
    s "Is it okay if I ask for a few more details?"

    "I’m almost positive I know what this is about, but I don’t want to reveal anything until I’m sure."

    scene mollydormten13
    with dissolve

    mo "Well...Let’s just say that girls sometimes use the same dressing room as one another when they go shopping."
    mo "And a girl I happened to be changing with had some marks on her that I’m smart enough to recognize."
    mo "I might be a huge geek, but I know when to snap out of it."

    scene mollydormten14
    with dissolve

    mo "I obviously didn’t say anything because like, what do you even say when you see something like that?"
    mo "“Are you okay? What happened? Do you need help?”"
    mo "Those are all things that would make her catch on."

    scene mollydormten15
    with dissolve

    mo "And now I’m in this weird place where there are a million things I wanna say but none of them will come out because I’m afraid of people getting mad at me."
    s "…"
    s "This person sounds really important to you."

    scene mollydormten16
    with dissolve
    play music "closeto.mp3"

    mo "..."
    mo "Yeah."
    mo "They are."
    mo "..."
    mo "Very important."
    mo "Like, so important that I just wanna squeeze her and be like “Wake up!” and not let go until she promises to not do anything like that again."

    scene mollydormten17
    with dissolve

    mo "My mom killed herself when I was little. So ever since then I’ve tried to be really conscious about how other people feel."
    mo "But even when you know they’re not feeling well, it’s not like you can actually do anything about it."
    mo "You can’t even make jokes because then it will seem like you’re just brushing everything off."
    mo "So I wanna know what you would do in my position."
    s "…"

    scene mollydormten18
    with dissolve

    mo "Hahah...Hahahah! Pretty crazy how we wound up here all of a sudden, right?"
    mo "The dorms must be possessed by some kind of dark entity or something! Right?"
    mo "That’s gotta be it!"

    scene mollydormten19
    with dissolve2

    mo "That’s gotta be it..."
    mo "And it’s gotten to her too. And it’s making her do weird things to her arms. "
    mo "So all we need to do is take down whatever entity is spreading all of these negative emotions around and everything will go back to normal."

    scene mollydormten20
    with dissolve

    mo "Everything will go back to normal. "
    mo "It’s all just part of an evil conspiracy. "

    "Molly picks at the fabric of her clothes even harder than before."
    "Her hands are shaking as tears begin to slowly but surely stream down her pale, white cheeks and drip onto the sleeves of her hoodie."
    "Meanwhile, I sit across from her...At a table the same girl she’s so concerned about often shows up to in order to play games and get away from everything."
    "We’re all looking to get away from everything. And we all have different ways to do that."
    "But what happens when someone you know forgets how? "
    "What do you do?"
    "I doubt Molly {i}wanted{/i} to talk about this at all."
    "It just managed to grab hold of her and force her head underwater before she could do anything about it."
    "And so everything just started to leak out."
    "Everything always leaks out."

    s "This sounds like a job for your master."

    scene mollydormten21
    with dissolve2

    mo "Huh?..."
    s "Come on...Don’t drop the act now."
    s "I finally start playing along and you’re going to give me that face?"
    s "If you care so much about this person and you want to get rid of the “demon” or whatever it was you said was possessing them, we just have to defeat it. Right?"
    s "Maybe it’s time I show off {i}my{/i} true power?"
    s "I’m the Supreme whatever it is-"

    scene mollydormten22
    with dissolve

    mo "Supreme Overlord. Herald of the Adolescents."
    s "Yeah. That thing. "
    s "And besides, I’m pretty sure I know who you’re talking about anyway."

    scene mollydormten21
    with dissolve

    mo "You do?"
    s "Yeah. It’s something I’ve known about for a while. And I care about her just as much as you do."

    scene mollydormten23
    with dissolve

    mo "Oh yeah?"
    mo "You dare challenge the love of the Emerald Guardian of the Crystal Forest?"
    mo "You may be my master, but you must know by now that there are aspects of power where even {i}I{/i} surpass you."

    "Her eyes return to the same corner she’s continuously focused on throughout this impromptu confession. "
    "I guess it’s a habit of hers. Just like plucking at the strings of fabric on her clothing."
    "It’s great being able to find things that will calm you down while your mind runs wild. "
    "You need to stay grounded or you’ll eventually just float off into the ether."
    "There’s your half-assed philosophy for the day, coming from a man who seems to always just-so-happen to be around girls when they start to cry."
    "Sometimes, I wonder if they’d cry at all if I were to just leave."

    s "There’s no need to challenge anyone here. It’s clear how worried you are by how you’re acting right now."
    mo "That’s because of the dark entity."
    s "Right. The dark entity."
    s "So if the dark entity happens to wipe our memories of this conversation, everything will be just like it was before, right?"

    scene mollydormten24
    with dissolve

    mo "It can do that?!"
    mo "It’s even more powerful than I thought!"
    mo "Are you sure you’ll be able to handle it, Master?"
    mo "I may be small, but I’m willing to assist you in any possible way. Just name it!"

    "It’s hard for me to tell if Molly is just acting right now or if all of these words are her true feelings wrapped in intentionally faked delusions of grandeur. "
    "Maybe she {i}does{/i} think that there is something she can do to help bring Rin back to normal."
    "But before any of that, I need to find out if something’s actually going on again or if the marks she saw were the same ones I did."

    s "You can assist me by guarding yourself, Molly. You’re of no use to me if you fall victim to the darkness as well."

    scene mollydormten25
    with dissolve

    mo "Ahh, an excellent plan, Sir. I will support you from the backlines, just as any good priest would."
    mo "I’ll be sure to cast Power Word: Shield on you before you pull."
    s "I...wouldn’t have it any other way."

    scene black
    with dissolve2

    "We find a way to carry on our conversation without ever directly addressing anything again."
    "Life is easier that way."
    "Sometimes, you need to disguise your problems as happier things to avoid {i}the dark entity{/i} consuming you."
    "And even if Molly is too much to handle at most hours of the day, I {i}do{/i} want to protect her."
    "Just as I want to protect the rest of the girls."
    "She doesn’t deserve to be beaten down the way so many others have been."
    "So if there’s anything I can do about that-"
    "I will gladly do it."

    $ renpy.end_replay()
    $ molly_love += 3
    $ mollydorm10 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat


label tsuneyodorm:
    if tsuneyo_love >= 5 and ramen1 == True and tsuneyofirsthall == True and tsuneyodorm5 == False:
        jump tsuneyodorm5
    if tsuneyo_love >= 10 and ramen10 == True and tsuneyodorm5 == True and tsuneyodorm10 == False:
        jump tsuneyodorm10
    if tsuneyo_love >= 15 and ramen15 == True and day != 1 and tsuneyodorm15 == False:
        jump tsuneyodorm15
    if tsuneyo_love >= 20 and tsuneyodorm15 == True and day != 5 and day247 == True and tsuneyodorm20 == False:
        jump tsuneyodorm20
    if tsuneyo_love >= 25 and secondbeach18 == True and tsuneyodorm25 == False:
        jump tsuneyodorm25
    else:
        jump tsuneyodormgen

label tsuneyodormgen:
    play sound "knock.mp3"

    t "Noodles."
    t "Oh. I mean, come in."

    scene tsuneyodormgen
    with dissolve

    "I decide to spend the night hanging out with Tsuneyo in her dorm."
    "And by 'hanging out' I mean that we essentially stare at each other without saying anything for an hour or two."
    "And not in the romantic or sexual way either. It's sort of like an awkward exchange between two people who have no idea what to say, so they elect to say nothing instead."
    "Such is dating in this day and age."
    "Eventually, she starts talking about soup because she is Tsuneyo and it is the only thing she has a defined opinion on."
    "It's a little strange to me how she's managed to get so far in life with what seems to be no feelings whatsoever."
    "But I'm sure that line of thinking is just me being presumptuous and not taking into account her situation at home."

    scene black
    with dissolve

    "Eventually, it gets dark and Tsuneyo asks me if I'd like to walk with her to the store so she can buy some things for her room."
    "I agree and the two of us set out into the night, parting ways once we get to a nearby 7/11."
    "And even though there weren't many words exchanged between the two of us, I still can't help but feel like we've grown closer..."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo's affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyodorm5:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm:
    if molly_love >= 5 and mollycafe1 == True and mollydorm5 == False:
        jump mollydorm5
    if molly_love >= 10 and mollydorm5 == True and mollycafe10 == True and mollydorm10 == False:
        jump mollydorm10
...
```