# Something Less Lonely
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukaspecial15p3&go=Go)


Part of event chain [Red-ish Light District](./toukaspecial15p2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Tsubasa: Everbloom](./tsubasadate1.md)

## Event properties
* ID: toukaspecial15p3
* Group: Touka
* Triggered by label: endoftoukaarcade

## Event code
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukaspecial15p3:
    if _in_replay:
        scene black
        play music "justbehappy.mp3"

    "The next half hour or so goes by without much of a change to anything. "
    "Touka continues training her virtual combat skills against AI opponents, Tsukasa sits by herself at some table likely thinking about poor people, and Tsubasa downs probably an entire bottle of wine."
    "As for me, I repeatedly cycle around the arcade, spending short bursts of time with each one of them until things devolve into what I would call a mild amount of chaos."

    if bonus == True:
        tk "Mother! Mother! Can I have permission to rail Touka’s teacher?"
        tb "Of course dear. Just don’t get hurt. That thing looks like it’s meant for big girls and you’re still so young."
        to "Tsukasa, no! He’s {i}my{/i} teacher and I get to rail him first!"
        to "Mother! Tell Tsukasa to not rail Sensei before me!"
        tb "Perhaps I should be the one to rail him if you two are just going to fight over it?"
        s "Am I really the only person finding something odd about this conversation?"
    else:
        tk "Mwahahah! The time has come for me to activate the many bombs I have placed in this building!"

    "As you can see- a mild amount of chaos."

    if bonus == True:
        "Anyway, the Tsukiokas take turns railing me and, after they tire themselves out, the time comes for us to leave the arcade."

    scene noonsky
    with dissolve2

    "We spent enough time inside that the sun has already begun to set, taking a bit of the pre-summer warmth back behind the clouds as it disappears."
    "And, in other news, I wish it also took Tsukasa along with it since she has been doing nothing but annoying me ever since leaving the arcade."

    tk "Mr. Teacher Man, have you played the same game with my sister that you played with the hot spring peasant girl?"
    tb "I certainly hope not~"
    to "Hot spring peasant girl? Are you speaking of Io, Tsukasa?"
    tk "Does Io look like she fell asleep in a tanning bed?"
    tb "Tsukasa! Chika is part Filipino, her skin color has nothing to do with tanning."
    to "What sort of game were you playing with Chika at a hot spring? Is it one that I can play as well?"
    s "Sure."
    tb "{i}Ahem.{/i}"
    s "I mean no."
    to "Well, that doesn’t seem very fair at all..."

    scene black
    with dissolve2

    "The four of us continue to walk around what I am now going to refer to as the “Entertainment District” for lack of a better term."
    "I think it’s technically part of the urban one given the size and scope of everything but, at the same time, I don’t really think it makes much of a difference."
    "All I know is that I haven’t blacked out and forced myself on anyone here, so it’s likely not part of the old district."
    "Regardless, we decide to make our way back to the station for some budget commoner food before venturing back to the area of Kumon-mi we’re all more familiar with."
    "Here’s hoping that the Tsukiokas have any amount of exposure to Mexican street food- which is, very strangely, the only thing this subway station seems to have."

    scene toukataco1
    with dissolve2

    to "If I ask you how I am supposed to order, will you assist me? Or will you just make me look like a nuisance again?"
    s "Of course I’ll help you, Touka. I’d do anything for you."
    to "You intend to make me look like a nuisance after all, don’t you?"
    s "Why would I ever {i}not{/i} do that?"

    scene toukataco2
    with dissolve

    taco "Hi. How can I help you?"

    scene toukataco3
    with dissolve

    to "Oh, good afternoon. My name is Touka Tsukioka of the Tsukioka family, and this man behind me is my [high_school] teacher."
    taco "I am the taco man. Behind me is a sink."
    to "Say hello, Sensei. You don’t want to be rude to the taco man, do you?"

    "Well, this is already going better than I expected."

    to "May I trouble you for a recommendation, taco man? I am not well-versed in the art of Mexican cuisine, so I’m not quite sure what to order."
    taco "All we have are tacos. I recommend those."
    s "Really living up to your name, aren’t you?"
    taco "I don’t get it."

    "Sometimes, I feel like I’m the only normal person in this city."

    to "I suppose I will take the tacos, then! How many would you say a three person family would consume on average?"
    taco "I have no idea, Touka Tsukioka of the Tsukioka family."
    to "There’s no need to worry, taco man. I’m sure Sensei knows the answer to a question as simple as this."
    s "One thousand tacos."
    to "Or not. "
    taco "How about I just give you a random amount of tacos and you come back if you need more?"
    to "Splendid! Thank you very much for your assistance, taco man. Have you ever considered teaching [high_school]? We could use more people like you."
    taco "My brother used to work at Kumon-mi High. I heard nice things."
    to "Used to? Did he retire?"
    taco "He died after some girl hit him with a dodgeball."
    taco "No one came to the funeral but me."
    s "Well that’s certainly a part of the plot I didn’t expect to ever show up again."
    to "Oh my! I’m so very sorry to hear that. I hope the purchasing of your tacos will, in some way, help to numb the pain."
    taco "It really will. "
    taco "Thank you, Taco Tsukioka of the Tsukioka family. "
    to "And thank {i}you{/i}, Touka man!"
    to "Wait-"

    scene black
    with dissolve2

    s "Nope. We’re done here. No one said anything weird and it’s time to eat."
    to "But...I could have sworn I just-"
    s "Nope."

    "Touka and I wait patiently as the taco man does what he does best and, before long, we’re carrying several trays worth of tacos over to a nearby picnic table."
    "........."
    "......"
    "..."

    scene toukataco4
    with dissolve2

    to "So...{i}these{/i} are tacos."
    tk "..."
    s "..."
    tb "How exactly are we supposed to eat them?"

    scene toukataco5
    with dissolve

    s "You start by grabbing them. Then you finish by biting them. "
    s "It’s really just a two step process."
    tb "We grab them...with our hands?"
    s "I mean...I guess you could use your feet if you’re agile enough?"
    tb "Is there no option for chopsticks? Or perhaps a fork or knife? All of us were taught to never eat with our hands."
    s "That is very unfortunate because I can’t imagine these being consumable any other way."
    tk "What’s the yellow thing holding all of the stuff inside called?"
    to "I believe that is the...taco bone?"

    scene toukataco6
    with dissolve

    s "The taco bone?..."
    to "I-I don’t know! It just appears to be the bone of the taco!"
    to "Are we supposed to remove the innards? Or is the bone edible?"
    s "Touka, it’s a shell."
    to "Then say that before I call it a bone, Sensei! Stop allowing me to appear uncivilized in front of my family."
    tk "How come I got more than everybody else? I’m the smallest one here."
    tb "Probably because you’re the most special, dear. Now, eat your tacos before they get cold."
    tb "Unless they...already are cold? I’m not quite sure."

    scene toukataco7
    with dissolve

    s "I understand that you’re all very sheltered and don’t understand how most things in the outside world work, but I really feel like you’re making this harder than it has to be."
    tk "Mother. You go first. I need to know they are safe."
    tb "No, dear. I’m not expendable the way you are. I have a business to run."
    tk "I’m telling Father you called me expendable. "
    to "I...I will do it."
    to "I will be..."

    scene toukataco8
    with dissolve

    to "The sacrifice!"
    tb "Be careful, dear. Have you washed your hands? "
    to "Of course, Mother. I’m no heathen. "
    tk "Mother, if Touka dies from taco poisoning, can I get {i}all{/i} of her bedrooms?"
    tb "We’ll see, Tsukasa. Now, pay close attention to your sister. These could very well be her final moments."
    s "..."
    to "Here I go..."

    scene black
    with dissolve2

    "Being around rich people is exhausting."

    stop music fadeout 20.0

    "Eventually, the Tsukiokas {i}do{/i} eat their tacos. But, unfortunately for the taco man and his deceased brother, I don’t think they particularly enjoy them."
    "I guess that’s to be expected, though."
    "If you spend your life consuming the best of the best, you’ll be nothing but underwhelmed or let down the moment you try something less...refined."
    "Which I guess allows me to segue into this thought that I’ve been having ever since Tsukasa mentioned Touka openly admitting she likes me as a teacher."
    "Why?"
    "I don’t work with her schedule. I don’t do what she asks or wants me to do. Hell, I’m not even {i}nice{/i} to her the vast majority of the time. "
    "So why am I preferred over all of the people who were handpicked for the sole purpose of educating her?"
    "A small part of me thinks that it might be because Touka isn’t really what her family and upbringing have turned her into."
    "That part of me is wrong, though."
    "Touka is who she is and doesn’t seem to inherently {i}dislike{/i} that."
    "But, somehow, having everything she could ever want served to her on a silver platter just...isn’t enough for some strange reason."
    "I’m not sure why."

    scene nightsky
    with dissolve2
    play music "thesleepingcity.mp3"

    "But I’m also not sure why she asks me to walk her back to the dorm instead of just taking a cab or limo, and here I am- "

    if bonus == True:
        "Fighting off the return of the cold alongside the desire to defile one of the closest things to perfection this horrible world has ever spit out."
        "I won’t, of course."
        "Not unless she wants me to."
        "But, you know what? Maybe she {i}does{/i} want me to."
        "Maybe {i}that’s{/i} why she apparently “likes” me so much. "
        "It has nothing to do with my skills as a teacher or the way I can make her flustered by simply calling her the wrong name a few times in a row."
        "It’s the power I possess- and how she knows that her livelihood outside of the bubble she’s grown up in is entirely within my hands."
        "I’m likely the first person she’s ever felt powerless against."
        "Maybe that powerlessness excites her."
    else:
        "Super chilly and mildly sad =/"

    scene toukataco9
    with dissolve2

    "Or maybe that’s just what I’m telling myself to fill the several inches of space between us with something less lonely."

    to "Thank you again for putting up with my family and me today. I’m sure it was awfully stressful having to deal with a group of women so much-"
    s "Better than me?"
    to "{i}Different{/i} from you."
    to "If we were to grade our respective performances at the arcade, I’m sure you would have emerged as the “best.” Would you not?"
    s "If only who we are as people could be quantified by something as simple as that."
    to "Yes, if only. Imagine how many hours I could have saved if all of my lessons were replaced by leisurely activities growing up."
    s "Do you ever feel like you sort of wasted your childhood, Touka?"

    scene toukataco10
    with dissolve

    to "That’s certainly a strange question to ask out of the blue."
    s "Your mom said something like that earlier. I was wondering if you felt that way as well."

    scene toukataco11
    with dissolve

    to "Hm."
    s "..."
    to "..."
    to "No."
    to "I wouldn’t say any of my childhood was wasted."
    to "Sure, I do wish there was a little more of {i}me{/i} choosing things rather than just allowing myself to be pushed in the directions my family {i}thought{/i} I wanted to be pushed in."
    to "But to say that any of that was a waste would be akin to saying that I’m not comfortable with the result of all of those years and all of that hard work."

    scene toukataco12
    with dissolve

    to "Do you think I’m a good person, Sensei?"
    s "I do."
    s "Annoyingly good, sometimes."
    to "I think I’m a good person as well."
    to "That’s why I don’t consider any of my early years wasted."
    to "Seeing as those years are over, though, there’s not much purpose in dwelling on them."
    to "And there’s not much purpose dwelling on the current years either."
    to "Only a small portion of my life will be spent in this state, you know. "
    to "I’ll be an adult for the vast majority of my time on this planet. So why would I not look toward the future instead of getting so hung up on the me of the past or the present?"
    to "As long as I can remain a good person, anything I endure will be worth it."

    scene toukataco13
    with dissolve

    to "And I assume there will be a fair bit I have to endure, what with you suddenly turning my existence into some form of entertainment for yourself and all."
    s "You’ve been spending far too much time with Yasu if you think you can just poke me into changing."
    to "I’m spending far too much time with Yasu regardless of whether I want you to change or not."
    s "You absolutely want me to change."
    to "A little change would be nice, yes."

    scene toukataco14
    with dissolve

    to "But I will accept you for who you are now as well. Because I know, deep down in this...{i}suspiciously hard{/i} chest of yours, there is a heart. "
    to "It is not as big as mine, nor is there as much room inside for love, but it exists. "
    to "And {i}I{/i} think you should stop pretending it doesn’t."
    s "..."
    to "Goodnight, Sensei."
    to "I had a nice time today."
    to "In fact, it was {i}so{/i} nice that I may even consider leaving my family behind for our next outing."
    s "At the very least, let me know in advance if they’re going to be there so I can mentally prepare to deal with more than one rich person."
    to "I’ll see what I can do."

    scene toukataco15
    with dissolve

    to "Goodnight! "
    s "What, you’re not going to invite me up?"
    to "Hahah..."
    to "Now {i}why{/i} would I do that?"
    s "..."
    to "{i}Goodnight,{/i} Sensei."
    to "Thank you again for a wonderful day."

    s "..."
    s "..."
    s "..."

    scene black
    with dissolve2

    "I go home."

    $ renpy.end_replay()
    $ touka_love += 3
    $ toukaspecial15p3 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday
...
```

## Code that triggers this event
File: \game\ToukaEvents.rpy
Code:
```python
...
label endoftoukaarcade:
    $ renpy.end_replay()
    $ toukaspecial15p2 = True
    $ touka_love += 1
    $ tsubasa_love += 1
    $ tsukasa_love += 1

    "{i}Your affection with the entire Tsukioka family has increased by 1!{/i}"

    jump toukaspecial15p3
...
```