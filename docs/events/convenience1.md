# Nakayarakawayama
Noriko event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=convenience1&go=Go)



## Event preconditions
✅Noriko love greater than or equal to 0

✅Event "[Noriko: Sculpture](./norikofirsthall.md)" is completed (event=norikofirsthall)



## Next events
* [Noriko: Semi-Constructive Criticism](./norikodorm5.md)
* [Noriko: Mouthjob](./convenience5.md)

## Event properties
* ID: convenience1
* Group: Noriko
* Triggered by label: convenience
* Triggered by branch label: afterschoolmenu

## Event code
File: \game\NorikoEvents.rpy
Code:
```python
...
label convenience1:
    scene black
    with dissolve
    stop music fadeout 5.0
    "........."
    "......"
    "..."
    scene nightsky
    with dissolve2
    play music "blueair.mp3"

    "A sudden desire to go somewhere far away washes over me."
    "I’m not sure what brings it on, but I guess that really ties into the word “sudden,” now doesn’t it?"
    "sud-den (sədn) {i}adjective{/i} - occurring or done quickly and unexpectedly or without warning."

    play sound "static.mp3"
    scene happy5 with flash
    scene tree3 with flash
    scene happy4 with flash
    scene happy3 with flash
    scene nightsky with flash
    stop sound

    "Sudden."
    "Definitions can be fun if you’re willing to swim through all of the words you don’t like."
    "What are some words you don’t like?"
    "Tell me."
    "I’m excited to hear them."

    play sound "static.mp3"
    scene tree3 with flash
    scene firstconvenience1 with flash
    play music "noriko.mp3"
    stop sound

    "Sudden."

    s "…"

    "I wind up at an unfamiliar convenience store in the blink of an eye."
    "I have...absolutely no idea how I got here or where in town this even is, but...I guess I’m going to buy a drink or something."
    "A [young_girl] sits at the counter and-"
    "Wait. Isn’t that Noriko?"
    "I’ve definitely heard her mention having a job before, and I guess something like a convenience store is suited to girls her age."
    "But it’s just all so sudden."
    "…"
    "I wonder if maybe I can take advantage of how much she likes me to get a discount on stuff?"

    scene firstconvenience2
    with dissolve

    s "Hey. How’s it going?"
    n "Can I help you?"
    s "What, you don’t recognize my voice?"

    scene firstconvenience3
    with dissolve

    n "If you’re here to start trouble, I-"

    scene firstconvenience4
    with dissolve

    n "Ah! Sensei! What are you doing here?!"
    n "Did Nee-chan tell you where I worked?"
    s "Nope. Just coincidentally happened to stumble in here."
    n "Ahh! That’s so great!"
    n "I’m glad we got our reunion out of the way in the classroom first, because breaking down behind the counter and confessing in front of the onigiri wouldn’t have been a good look for me."
    s "Sure, I’ll take the hit to all of my current relationships so the rice balls don’t think you’re weird."

    scene firstconvenience5
    with dissolve

    n "Heheh~ Thanks!"
    n "You sure you weren’t over here looking for me, though?"
    n "The old district seems like it’s kind of far from[school] to just show up in all coincidentally and whatnot."
    s "We’re all the way in the old district?"

    scene firstconvenience6
    with dissolve

    n "Wait, is this another memory thingy? "
    n "Are you sure it’s not Alzheimer’s? "
    s "Pretty positive."
    s "Are you really commuting from the dorms to the old district every day for work?"

    scene firstconvenience7
    with dissolve

    n "Yup! But I normally just take an Uber so it’s not like it’s crazy far."
    s "I’m surprised you can afford that."
    n "I still make money running errands for my sister every weekend, so I’m not totally broke. "
    n "Our parents are pretty well off now, too. Their business really took off a couple years ago."
    s "Is their business a thing I knew about?"
    n "They were just starting it up around the time you disappeared, so you probably knew a little bit about it at least."
    n "It’s just some Chinese restaurant thingy near my old[school]. If you’d like, I can take you there sometime?"
    n "I’m sure they’d be happy to see you."
    s "Maybe after I remember a little more about them."

    "Assuming that ever happens."
    "Which it likely won’t."
    "But, then again, I just happened to find this place out of nowhere tonight, so I wouldn’t say it’s entirely out of the question to find somewhere else just like it."

    scene firstconvenience8
    with dissolve

    n "Hmm..."
    s "What? What is that look?"
    n "I was just thinking that maybe your conscience led you here in search of me."
    n "What if your memories are trying to speak to you, Sensei?"
    n "Can you hear them shouting “Noriko! Noriko!” or something like that?"
    s "All I hear is a really loud song on the radio."

    scene firstconvenience9
    with dissolve

    n "The radio’s not even on, though. Are you sure you’re feeling okay?"
    n "Do you want a rice ball?"
    s "One of the sentient ones that judge you based on how you react to reuniting with a long lost love interest? No thanks."
    s "I prefer my food to not have a mind of its own."
    n "So, what? You don’t eat yogurt either then?"
    s "What?"

    if bonus == True:
        n "Yogurt. The thick sour white stuff full of living organisms that {i}doesn’t{/i} come out of a penis."
    else:
        n "Yogurt. The thick sour white stuff full of living organisms that people eat when they want to feel healthier."

    s "Yogurt is alive?"
    n "Yeah. And not only is it alive, it can {i}feel{/i}."
    s "You’re shitting me."

    scene firstconvenience10
    with dissolve

    n "I am not!"
    n "We watched a video in one of my old science classes where a bunch of researchers hooked a thing of yogurt up to a machine and then yelled at it and it got {i}scared{/i}."
    n "Or at least reacted in a way that emulated some level of fear. I guess it’s not technically possible to prove whether or not it actually {i}did{/i} display the more human type of fear."
    s "I’d like to meet whoever decided to hook yogurt up to a machine and yell at it. They sound very interesting."
    n "Hey, are we gonna do any cool experiments like that in your class, Sensei?"
    s "We’re not going to do anything in my class ever."

    scene firstconvenience11
    with dissolve

    n "Wait, ever? Why?"
    s "That’s just not how I teach."
    n "Did something happen? You used to love teaching."
    n "Like, sure there were days where you’d get all upset and mopey and just have us do worksheets, but everyone gets days like that. "
    n "Well, without the worksheets. I think that’s a thing specific to tutors and teachers and stuff."
    s "You can mess around with the science equipment if you want, just don’t burn the classroom down."
    s "Ami did something like that once and I’m pretty sure several of the girls had a near-brush with death as a result."

    scene firstconvenience12
    with dissolve

    n "Hell yeah. That’s what I like to hear."
    n "I’m a little upset that you won’t be doing any {i}actual{/i} teaching anymore, but I guess I’m already way ahead of most other girls my age anyway."
    s "Wait, really?"

    scene firstconvenience5
    with dissolve

    n "What? Are you surprised?"
    s "I’m not sure yet. How ahead are you, exactly?"
    n "I had the second highest standardized test score in my entire grade at my last[school]."
    n "Pretty cruel twist of fate, too, since I wound up transferring into Wakana’s class right beside the girl who beat me."
    s "Yup. Now I’m definitely a little surprised."

    scene firstconvenience7
    with dissolve

    n "Don’t judge books by their covers, Sensei. Especially when the books are in love with you and filled with lots of embarrassing secrets."
    s "And I’m assuming you’re going to weaponize those secrets as soon as it becomes convenient for you to do so?"

    scene firstconvenience13
    with dissolve

    n "What? No. Of course not."
    n "I have nothing to gain by embarrassing you in public. Which is why I also agree to start changing my wardrobe if I attract too much attention and you hate it."
    n "I realize some of my clothes can be a little...uhh...flashy?"
    s "Is that what the kids are calling it nowadays?"

    scene firstconvenience14
    with dissolve

    n "Or, as my sister would say, {i}trashy, tactless, and immeasurably undesirable.{/i}"
    n "{i}The complete opposite of what a girl should look like.{/i}"

    scene firstconvenience5
    with dissolve

    n "Or something."
    n "But, little does she know, this is all part of my patented strategy to show her that you can obtain everything you want in life without signing away your soul to do it."
    n "I will live free and dangerously in complete contrast to the name “Noriko!”"
    s "You do that. Just don’t get yourself into any trouble."

    scene firstconvenience15
    with dissolve

    n "Yes, Sir. I’ll be a good girl. "
    n "I mean, look at me now. I’ve already got a job. Two jobs if you count all of the PA stuff, and my grades are awesome."

    scene firstconvenience16
    with dissolve

    n "And, to top it all off, I get to spend at least seven hours of every day with the man of my dreams."
    n "This is the happiest I’ve been in a long time, Sensei."
    n "I don’t even care that Maya looks like she’s going to slit my throat every time our eyes accidentally meet."
    s "Thankfully, I don’t think Maya carries around a pocket knife like some other girl I know."
    n "Sensei?"
    s "...Yes?"
    n "I’m so happy you’re back."
    n "I know I keep saying it, but I really am. "
    s "The more times you say it, the worse I will feel for remembering literally none of it."
    n "You’ll remember. I know you will."
    n "There’s probably just some sort of...inhibitor that was implanted in your brain by aliens or something like that."
    s "Is that what the space war is all about?"

    scene firstconvenience17
    with dissolve

    n "Mmm...no. I’m pretty sure that was an economic thing."

    "What the hell is happening with the Japanese economy that provoked a war in space?"

    n "At least it would make sense for it to be. It’s not like wars have never been started for money before."
    n "In fact, war itself is a major money maker for a lot of different industries and helps bolster political favor for the powerful people neck deep inside of them."
    s "I agree and understand exactly what we are talking about."
    s "Is the ailing economy the same reason you got a job as well, Noriko?"

    scene firstconvenience5
    with dissolve

    n "Nah, I was just bored since Nee-chan only needs help on the weekends."
    n "I mean, I could have probably gone and worked at my parents’ restaurant, but being independent feels a lot better."
    n "And also, they started looking at me weirdly ever since I told them I was in love with you. Whoops."
    s "Why on earth did you do that? And how did this whole love thing even happen?"
    n "Which one of those do you want me to answer first?"
    s "The latter one. I’m just going to assume you told your parents because of an alien implant. I like that excuse and will be using it frequently."
    n "Ooooh, nice callback."
    n "But...love just happens, you know?"
    n "We were alone together a lot back in the day. And I thought you were super cool."
    n "Saying I’ve “loved” you since I was six is probably a bit of a stretch. I imagine it was something more akin to just pure admiration at first."

    if bonus == True:
        n "But it’s not uncommon for admiration to turn into something more once your thoughts on romance and sex develop."
        n "Now, here I am in [high_school] thinking about what it would be like to grow old and take over my family’s business with you."
        s "…"
    else:
        n "But now, literally all I think about is hugging you."
        s "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH"

    n "What now? You want to call me crazy again?"

    if bonus == True:
        n "I can take it. I’ve heard it plenty of times."
        s "Nah. You’re just really cute."
    else:
        s "No. I just saw a spider."

    scene firstconvenience18
    with dissolve

    n "Stop...you’re going to make me blush."

    if bonus == False:
        "Wow. Noriko must really like spiders."

        s "Oh, by the way, are you hiring? Being a teacher is stressful and I may quit soon."
    else:
        s "You are very much already blushing."
        n "The boy I like called me cute. Obviously, I’m going to blush."
        s "Very cute, actually. Even if your dream of us running a restaurant together involves me having to actually work- a thing I have sworn to never do again."

    scene firstconvenience19
    with dissolve

    n "Hey, man! If you’re gonna be my second in command, you’re gonna at least have to clean the bathrooms or something."

    if bonus == True:
        s "Just hire Ami instead of me. I’m sure she’ll gladly do it if I’m involved in any way."
    else:
        s "Ewwwwww gross. Aren't you supposed to be like a sister to me or something? Cut me some slack."

    scene firstconvenience20

    n "Oh! Then it will be like, a {i}double{/i} family business! The Nakayamas and the Arakawas coming together as one! Serving fried rice to all of Kumon-mi!"
    n "The Arakawayamas! The Nakakawas!"
    n "The Nakayarakawayamas!"
    s "Please calm down, Noriko..."

    scene firstconvenience15
    with dissolve

    n "Yes, Sir. I’ll be a good girl. "
    n "Besides, we don’t have to do something like that if it’s not a future you want for yourself."
    n "Anything is possible in Kumon-mi."

    if bonus == True:
        n "Like, if {i}Nee-chan{/i} can become a top idol when all she did up until she was 18 was doodle anime characters, I'm sure the two of us can explore some options."
    else:
        n "Like, if {i}Nee-chan{/i} can become a top idol when all she for the first 4000 years of her life was doodle anime characters, I'm sure the two of us can explore some options."

    n "If...you ever want to do that, I mean."
    n "Obviously, there’s more than one person fighting for your affection right now."
    n "But remember that...even if you forget me now, everything will come flooding back eventually."
    n "And when that happens, know you can count on me to be everything you’ll ever need."

    scene black
    with dissolve2

    "The way I leave the convenience store is a lot less sudden (sədn) than how I arrived."
    "Noriko and I wind up chatting for another hour or two about random things that pop into her head and, just as always, I have a hard time understanding why Maya hates her as much as she does."
    "She’s smart, extremely kind, good at holding a conversation, and even {i}did{/i} give me a discount on a [[non-sentient] rice ball as I left."
    "But I feel like there’s something else to her that I can’t quite put my finger on yet."
    "I feel the same way when looking at sculptures."
    "There’s too much perfection on the outside for everything to possibly be the same once you work your way in."
    "Just the insides of sculptures are pure stone or marble-"
    "And the insides of Noriko are a lot less beautiful."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ convenience1 = True
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label convenience5:
...
```

## Code that triggers this event
File: \game\NorikoEvents.rpy
Code:
```python
...
label convenience:
    if noriko_love >= 0 and norikofirsthall == True and convenience1 == False:
        jump convenience1
...
```