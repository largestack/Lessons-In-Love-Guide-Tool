# Transference (Yasu)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yasu love greater than or equal to 0

* Event [Blackout](./ramen20.md) (Tsuneyo) is completed)



## Next events

* [Yasu: Armor of Older Gods](./church5.md)

## Event properties

* Id: church1
* Group: Yasu
* Triggered by label: church
* Triggered by branch label: church
* Triggered by path: church->church1

## Official wiki page

[Transference](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=church1&go=Go) for more details.

## Event code

File: (install folder)\game\YasuEvents.rpy

Code:
```python
...
label church1:
    play sound "static.mp3"
    scene urbanparadise
    with flash
    stop sound
    stop music
    play music "sanctuary.mp3"

    "City lights, city lights. "
    "How do you fall asleep at night?"
    "Through stained glass panes, they shine so bright."
    "And kill the dark to grant us sight."

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "I close my eyes and shut my mouth. "
    "I can not scream. I can not shout."
    "My limbs fall off where branches sprout."
    "Yet with no arms, I still reach out."

    play sound "static.mp3"
    scene urbanparadiseupsidedown
    with flash
    stop sound

    "The sky, it burns! It burns my eyes!"
    "My words ring out to no reply."
    "While one god lives, another dies."
    "When one descends, one more must rise."

    play sound "static.mp3"
    scene urbanparadise
    with flash
    stop sound

    "Hello."
    "I’m going to church tonight."
    "Or rather, a {i}cathedral,{/i} if we’re going by what the newspaper clipping Yasu gave me calls it."
    "{i}Godnote: A cathedral is kind of like a mega church that is run by a bishop, meaning that it’s more than just a standard place of worship.{/i}"
    "{i}Sure, you can still go there to say hi to God or whatever, but it’s also kind of like a headquarters.{/i}"
    "{i}Which also means that it’s easier to get away with horrible things there as it’s metaphorically towering over all of the smaller churches in the respective jurisdiction.{/i}"
    "{i}Cathedral...church...the name of the building doesn’t make much of a difference in the long run because it’s not like any of us will be kept there when we die.{/i}"
    "{i}I’ve heard stories of priests being stashed away in the basements of some places like that, though.{/i}"
    "{i}Which means that there’s likely a few cathedrals out there with basements overrun by flies, squeezing their way into caskets and laying eggs in the sockets of the holiest of holy.{/i}"
    "(End of godnote.)"
    "{i}Flynote: Standard house flies can lay over 500 eggs in a three to four day period of time.{/i}"
    "{i}They come in batches of anywhere from 70ish to 150ish and each measure up to around 1.2mm in size.{/i}"
    "{i}Their color is a yellowish white and if you put one in your mouth, you likely won’t taste anything.{/i}"
    "{i}Don’t take that as me granting you permission to go around eating fly eggs, though, you fucking weirdo. {/i}"
    "{i}Oh, sorry.{/i}"
    "(End of flynote.)"

    if bonus == True:
        "Anyway, I guess you’re probably wondering why I’ve decided to take it upon myself to come here instead of getting my dick sucked in one of several different girls’ rooms."
        "Me too."

    scene black
    with dissolve

    "Black."
    "Nine periods."
    "Six periods."
    "Three periods."
    "Dissolve."

    scene yasufirstchurch1
    with dissolve

    "I find the girl I expected to find sitting in front of the place I expected her to be sitting in front of."
    "My success rate in terms of identifying the respective locations of girls goes slightly up, but does not offset the countless other times I have searched to no avail."
    "But we are all searching for things to no avail."
    "Some people search for salvation."
    "While others search for strange things, like fly eggs to put in their mouths."
    "Both of those types of people will die horrible or slow deaths in hospital beds."
    "And any family members fortunate (Or unfortunate) enough to watch said passing will likely not even remember the number on the door they were kept in."
    "But life will move on and so will we."
    "So will I."
    "I move one step closer to the truth."

    scene yasufirstchurch2
    with dissolve

    "Yasu is too tangled up in some indiscernible paper web of words to notice my presence."
    "I doubt she receives visitors here very often."
    "Actually, I’m not even sure if I should be citing her as the entity who receives them."
    "If we have learned anything from the most recent Godnote, it is that cathedrals are run by bishops. "
    "And I do not think Yasu is old enough to be a bishop."
    "{i}Godnote #2: You must be at least 35 years old to be a bishop according to the Code of Canon Law (Canon 378 § 1, 3). {/i}"
    "Wow, thanks Godnote #2. I am learning quite a bit tonight."

    s "Hello, Yasu. "

    scene yasufirstchurch3
    with dissolve3

    ya "Huh?..."

    play sound "static.mp3"
    scene yasufirstchurch4
    with flash
    stop sound

    ya "Sensei! You came!"
    ya "The amount of joy I am feeling is indescribable! "
    ya "It courses through my veins! I can feel it curdling the blood inside of them with the happiest of clots! "
    ya "Like burning marshmallows bursting and oozing the righteous fluid of God himself!"
    s "That’s nice."
    s "What are you reading?"

    scene yasufirstchurch5
    with dissolve

    ya "Nothing particularly noteworthy. Just a book I obtained from the library."
    ya "Did you know that the standard house fly can lay up to 500 eggs over a three to four day period of time?"
    ya "Imagine if we, as humans, could lay that many eggs."
    s "We can’t lay any eggs at all, Yasu. We are mammals."
    ya "Live babies are like eggs, are they not?"
    ya "They must be closely monitored and cultivated until they can eat or move without the assistance of others."
    ya "Whereas many birds or insects are able to walk shortly after hatching."
    ya "In that regard, don’t you think those two things are a little better than human beings? "
    ya "Or at least far less worthless without the effort required to turn them into what we want them to be."
    s "They also cost a lot less to raise, I’m sure."

    scene yasufirstchurch6
    with dissolve

    ya "Do you have experience in raising children, Sensei?"
    s "I’m raising twenty of them right-"

    play sound "static.mp3"
    scene amiani16 with flash
    scene yasufirstchurch5
    stop sound

    s "Just one. My [niece]."
    s "Though I didn’t really start “raising” her until some...things happened."

    scene yasufirstchurch7
    with dissolve2

    ya "Did someone die?"

    play sound "static.mp3"
    scene yasufirstchurch4
    with flash
    stop sound

    ya "This is a church, Sensei. It’s okay to talk about the things that scare you here."
    ya "Both myself and {i}He{/i} are listening."
    s "I thought this was a cathedral and not a church?"
    ya "It used to be."
    ya "This building has not been used for its original purpose in quite some time."
    ya "It’s been abandoned for years now. Though, in its abandonment, it has saved the life of at least one girl."
    ya "You might know her. Her name iiiiiiiiiiiiiiiiis..."

    play sound "static.mp3"
    scene yasufirstchurch8
    with flash
    stop sound

    ya "Yasu! Woooooo! Yayyyy!"
    ya "The crowd goes wild!!!"

    "Yasu proceeds to make silly cheering noises for the next several seconds, likely expecting me to clap along or something like that."
    "But the truth is that my body feels rather heavy tonight. So heavy that just clapping alone might be enough to cause me to pass out."
    "But hey, at least if I {i}do{/i} pass out, she’d be here to take care of me."
    "I can’t guarantee that she won’t perform experiments on me while I’m out, but I can’t guarantee that Ami won’t do that either and I sleep in the same house as her nearly every night."

    s "So, are you going to give me a tour of the place? Or are we just going to sit out here and look suspicious?"

    scene yasufirstchurch9
    with dissolve

    ya "Hand of many clocks...father of all children...feed me your precious whispers of-"

    play sound "static.mp3"
    scene yasufirstchurch10
    with flash
    stop sound

    ya "God says no."
    s "What? What do you mean he says no?"
    ya "He seems...mad at you for some reason. "
    ya "He can be very temperamental at times. You’ve likely done something to offend him."
    ya "But you can gain his favor by coming back. I’m sure that the next time you arrive will be much more invigorating than this."
    s "So...I walked all the way to this weird, slummy part of the urban district to watch you read a library book?"
    ya "Hehehehehehehehe...yes."
    s "Welp, time to head back then."

    play sound "static.mp3"
    scene yasufirstchurch11 with flash
    stop sound

    ya "No! Don’t leave!"
    ya "Not before learning who we are and why we are here!"
    ya "There is still so much you can absorb by simply listening! "
    ya "The fact that His Holiness will not seep into your pores just yet does not mean you must give up!"
    ya "I implore you! Stay here and-"
    s "Holy shit, okay. Just stop yelling before someone comes over here."

    scene yasufirstchurch12
    with dissolve

    ya "Okay!"
    ya "But you don’t need to worry about that, Sensei."
    ya "In all of my time coming here, I’ve yet to see a single person enter the building other than me. "
    ya "Which is why I’m so very excited to finally have you here. "
    s "Even though I also can’t enter the building."

    scene yasufirstchurch13
    with dissolve

    ya "But you {i}will{/i} soon enough. "
    ya "The difference with you is that you can see it. The others can not."
    ya "To them, the torches are not lit. The glass is not stained. And the door is barred shut."
    ya "It’s nothing more than an old, abandoned building to the average person."
    ya "You and I have already transcended what it means to be average. Which means that we have what it takes to be saved."
    s "Correct me if I’m wrong, but wasn’t your pitch that night under the streetlight that your god accepts anyone willing to reach out or whatever?"
    ya "He does."
    ya "But the unfortunate truth is that even though there are so so so so so so so many people in Kumon-mi, only several of them have arms."
    ya "And of course not {i}all{/i} of those people with arms are going to reach out. So God becomes very sad watching them pass by."
    ya "He needs all the help he can get. Which is why I have devoted myself entirely to him."
    s "Well, you’re free to enjoy the missionary life, but I'd much rather not get involved."
    ya "Missionary is such a bad word. It has so much negativity glued to it."
    ya "And it also doesn’t apply to me as I haven’t been given a “mission.”"
    ya "I am simply a messenger relaying what she knows and what she has been told."
    ya "I can stop whenever I want to. "
    ya "But I don’t want to stop, Sensei. Not until His appetite has been filled."
    ya "Not until my body is flooded with the warmth of His love. "
    ya "Not until I can reach out and touch the light myself."
    s "Why can’t you, exactly?"

    scene yasufirstchurch12
    with dissolve

    ya "An excellent question! And one I am excited to answer."

    scene yasufirstchurch14
    with dissolve

    ya "You know the difference between boys and girls, correct?"
    s "…"
    s "Yes."
    ya "It’s customary in many religions for boys and girls to have different roles."
    ya "My role, as the purest of the pure and a devout follower of he who fills the well-"
    ya "Is to work hard and trust in His word."
    ya "To plant seeds all over the world and deliver the message of-"
    s "Wait, hold on. Isn’t that a mission?"

    scene yasufirstchurch15
    with dissolve

    ya "…"
    ya "Huh. I guess it is."

    scene yasufirstchurch16
    with dissolve

    ya "But I am still no missionary as I decided to do this all by myself!"
    ya "Essentially, what I must do is rid myself of all feelings and all desires."
    ya "I must act as a vessel for His warmth, which he will drip feed into me as if I’m connected to an invisible IV powered by my actions and my words."

    scene yasufirstchurch17
    with dissolve

    ya "You coming here tonight earned me a lot of IV fluid, Sensei. "
    ya "I feel warmer now than I have in a very long time."
    s "You’re...welcome, I guess."
    s "What about men? What's their role?"

    play sound "static.mp3"
    scene yasufirstchurch18
    with flash
    stop sound

    ya "You want to know?!"
    s "I mean, I wouldn’t have asked if I didn’t want to know."
    ya "It’s a very exciting role! One that only people like yourself can fill!"
    s "Trying to sell me on changing my beliefs just because I’d have an important role isn’t really going to do much, Yasu."
    s "I’m pretty set in my ways."

    scene yasufirstchurch19
    with dissolve

    ya "How unfortunate. I think you’d be quite good at it."
    s "And what is “it” exactly?"
    ya "{i}Transference.{/i}"
    s "...What?"
    ya "Filling your body with His warmth and moving it from one place to the next."
    ya "You see, girls are weak. "
    ya "Our bodies would simply explode if He gave us any more than a gradual drip feed."
    ya "But if you were to earn his blessing...you, too, could become a vessel."
    ya "One that transfers the greatest amounts of warmth from Him unto us."
    ya "And we would, in turn, cleanse ourselves of our desires and ask that you carry them back to him to be purified."
    s "Can I have a translation of that, please?"

    scene yasufirstchurch20
    with dissolve

    ya "Hehehehehehehehehe..."
    ya "Hahahehehehhaahhehahehehe..."
    s "That isn’t-"

    play sound "static.mp3"
    scene yasufirstchurch21
    with flash
    stop sound

    if bonus == True:
        ya "Sex! "
        ya "Lots and lots of sex!"
        ya "Girls plant the seeds and boys provide them! That is His wish!"
    else:
        ya "(Airplane noises)"
        s "Oh, okay. I understand now."

    scene yasufirstchurch22
    with dissolve

    if bonus == True:
        ya "Without you, what am I to deliver?"
        ya "How can I remain enthusiastic about His love if I feel that love dwindling with every passing moment?"

    ya "God is dying, Sensei."

    if bonus == True:
        ya "Do you understand why you are needed now? How important your role could be?"
    else:
        s "So I've heard."

    play sound "static.mp3"
    scene yasufirstchurch23
    with flash
    stop sound

    ya "And all you have to do is believe in order to be blessed."
    ya "That doesn’t sound very hard, does it?"
    s "I mean...no."

    if bonus == True:
        s "This might actually be the first time a religion has ever had some sort of appeal to me."
        s "It just comes as a bit of a shock since you already said all that stuff about no romance and blah, blah, blah."
        ya "Transference has nothing to do with romance, Sensei. It’s taking one important resource and putting it where it belongs."
        ya "It’s entirely practical."
    else:
        s "I just don't really have any idea what to believe in since you keep making airplane noises."

    scene yasufirstchurch24
    with dissolve

    if bonus == True:
        ya "But I bet it feels really...{i}really{/i} good."
        ya "To think of how hot the insides of my body would be as they fill with His love..."
        ya "It almost makes me think things. Things that someone as pure as me should never think."
        s "Sorry for just throwing this out there, but..."
        s "Did you make this religion up or something?"
        s "Kind of weird that I've never heard about it before if the main perk is getting to have lots of sex."
    else:
        ya "You mean like this? (Airplane noises)"
        s "Yes, exactly like that."
        ya "I'm speaking a special language."

    scene yasufirstchurch25
    with dissolve

    ya "I’m certain you’ve heard of it. Even experienced some of it if the whispers I hear are correct."
    ya "You just didn’t know how it worked."
    ya "But now you do. Because I was told to tell you."
    ya "And I do hope that you’ll consider learning more about it in the future."
    ya "The end of the world is coming. And it is my job...no."
    ya "It is {i}our{/i} job to save as many souls as we possibly can."
    ya "Please help me. "
    ya "All you need to do is open your eyes."
    s "Open my-"

    scene black
    stop music

    "I wound up leaving some time after that conversation ended, but I don’t remember when."

    $ renpy.end_replay()
    $ yasu_love += 1
    $ church1 = True

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "………"
    "……"
    "…"

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon

label church5:
...
```

## Code that triggers this event

File: (install folder)\game\YasuEvents.rpy

Code:
```python
...
label church:
    if yasu_love >= 0 and ramen20 == True and church1 == False:
        jump church1
...
```