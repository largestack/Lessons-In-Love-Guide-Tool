# Facetime With My Mom (Uta)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Uta love greater than or equal to 15

* Day of week is not Tuesday

* Event [Happier Things](./utamaid10.md) (Uta) is completed)



## Next events

* [Uta: Veins and the Circulatory System](./utamaid20.md)

## Event properties

* Id: utadorm15
* Group: Uta
* Triggered by label: utadorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->utadorm->utadorm15

## Official wiki page

[Facetime With My Mom](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utadorm15&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label utadorm15:
    play sound "knock.mp3"

    "I knock on Uta’s door and wait for her to answer."
    "I have also decided against bringing my wallet with me tonight because, even though this is her room and not the maid cafe, I will be damned if I trust that girl."

    u "Whooooo is it?"
    s "Someone without any money. Let me in."
    u "Sorry, Sensei! Gotta pay the admission price if you wanna hang out with Uta after hours."
    s "I’ve never had to pay before."
    u "Yeah, but now you’re attached. You payin’ or not?"
    s "Joke’s on you. I’ve been attached since the beginning."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Is this open?"
    u "Hey! That’s shoplifting, mister!"

    "I turn the handle and, as expected, the door isn’t locked."
    "Here’s hoping that a police report isn’t filed and that Uta takes it upon herself to frisk me and prevent me from “shoplifting” again in the future."

    scene utafacetime1
    with dissolve

    if bonus == True:
        u "Fine. I’ll let you off the hook this one time. No hidden fees tonight. But don’t expect me to be doin’ anything {i}extra{/i} for ya."
        s "You’re all talk. You wouldn’t have done anything extra even if I brought my wallet with me."
    else:
        u "Okay, okay. Fine. I'm not gonna get the cops involved or anythin' like that because of any outstanding warrants you might have."
        s "Could you take an IOU? I didn't even bring my wallet."

    scene utafacetime2
    with dissolve

    u "Am I really so tempting that you had to start leaving your money at home before coming to say hi?"
    s "Yes. "
    u "That’s really sad, Sensei."
    s "I have a problem, okay?"
    s "Anyway, what are you up to? No Io tonight?"

    scene utafacetime3
    with dissolve

    u "She’s over at the bathhouse doin’ some extra scrubbin’ or something."
    u "I was gonna go with her, but decided to stay home and check in with my parents instead."
    s "Are you telling me I missed an opportunity to formally introduce myself to your parents as your future husband?"

    scene utafacetime4
    with dissolve

    u "I’m sorry, darling. But you know how my parents get when we show off our love for one another while I'm on Facetime."

    if bonus == True:
        s "It’s okay. We can show off our love for one another right now instead. They don’t have to watch."
        u "I’m sorry again, but I’m far too tired to allow that tonight. Even if all I’d have to do is lay there like a dead fish and let you go to town on me."
        s "Man, I can’t wait for the day when you run out of excuses."
    else:
        s "But my love is so pure. I just want to hug."

    scene utafacetime5
    with dissolve

    u "Hope you’re okay with waitin’ a while!"
    u "I’m glad you showed up when ya did, though. If you’d have walked into the room while I was talkin’ to my mom, she would have flipped."
    s "Because I’m a male or because I’m your teacher?"
    u "Both of those things. And also that I’m not wearin’ pants."
    u "Basically, we’d both have a lot of explainin’ to do. And even after, they’d never give you their blessing and we wouldn’t be able to get married."
    u "To think our entire futures could have been destroyed if you came a few seconds earlier."
    s "That’s what she said."
    u "Ooooh, nice one. Ten points to Uta for the glorious set up."
    s "So, now that your parents are out of the way, do I get you all to myself?"
    u "For a little while! I’m still waitin’ on a call from my brother, too. But his hours are all wacky because of prison and stuff."
    s "Wait, yeah. You said something about that before, but I couldn’t tell if it was a joke or not."
    u "Did you think I was joking about my grandpa’s cancer, too? "
    u "What kinda sick sense of humor do you think I have, Sensei?"
    s "I...have no idea."
    s "Why is your brother in jail, though?"

    scene utafacetime6
    with dissolve

    u "Cause he’s an idiot."
    u "And maybe sorta kinda tried to kill somebody."
    s "I’m sorry, what?"
    u "Long story. "
    u "He’ll probably get out in a couple years since the person didn’t actually die, but he’s in pretty hot water right now."
    s "Is there...something I’m not understanding about your family? Because we already have one girl with Yakuza ties and-"

    scene utafacetime7
    with dissolve

    u "Oh, come on. Just because {i}one{/i} Ushibori has attempted murder doesn’t mean we’re {i}all{/i} gonna do it."
    u "My family’s pretty normal apart from him and the long line of debilitating diseases on my mom’s side."
    u "RIP grandpa."
    s "I think you really underestimate how uncomfortable it can be talking to you at times like this."

    scene utafacetime8
    with dissolve

    u "Nothin’ wrong with sayin’ things how they are, Sensei. And it’s not really {i}my{/i} fault if ya get uncomfortable because of it."
    s "I think it’s more of a matter of just not knowing how to respond to certain things you say."
    u "Is somebody forcin’ you to respond? Cause you can always walk away."
    s "But then I’d miss out on precious Uta time."
    u "Not to mention you’ve encountered the rare glasses-pajama Uta. This only happens once a week for a two to three hour period based on the availability of the rest of the Ushiboris."
    s "Well, I hope that the rest of the Ushiboris are not as lively or weird as you."
    u "I think I prefer “bubbly and spunky.”"
    s "And I think I’d prefer not standing across from a beetle while talking to you. Move over."

    if bonus == True:
        u "Okay! But you’ve gotta promise not to touch me or look down my shirt to sneak a peek at my girls."
        u "Or {i}up{/i} my shirt to see my underwear."
        u "Basically, just don’t look at me and everything will be okay."
        s "Impossible. Do you have any idea how cute you are?"
        u "Of course. Why else do you think I started charging people to see me?"
        s "Because you’re actually a demon trapped inside the body of a suspiciously well-endowed freshman."
        u "Blah blah boobies blah blah."
        u "You’re lucky I’m goin’ through my rebellious phase or I wouldn’t let ya on the bed at all."

    scene black
    with dissolve

    "Uta rolls over and drags her laptop to the end of the bed."

    if bonus == True:
        "I immediately attempt to bypass one of her conditions by glancing up her shirt to catch a glimpse of her underwear-"
        "But alas."
        "I fail."
        "I’ll just use my imagination instead and position myself in a way that will allow me to achieve an erection without drawing too much attention to it and making her run away- a thing I’m pretty sure she’d do."

    scene utafacetime9
    with dissolve

    u "Did you see?"

    if bonus == True:
        s "Unfortunately, no."
        u "Really? But I gave you such a good opportunity to."
        s "I will gladly accept a second opportunity if you’re offering."
        u "No can do, Sensei. I only expose my panties once per year and now you have to wait for a whole other trip around the sun to get another shot."
        s "Do you get pleasure out of disappointing me or something?"
        u "Maybe~"
        u "Do you get pleasure out of {i}being{/i} disappointed?"
        s "No. It sucks."
        u "Then why do you keep comin’ to see me if you know I’m all bark and no bite?"
        s "Because all dogs will bite if they’re antagonized enough and your bite sounds incredibly appealing."
    else:
        s "The beetle? Yes."
        u "Cool."

    scene utafacetime10
    with dissolve

    u "You want me to {i}bite{/i} you now?"

    if bonus == True:
        u "I was just using a popular expression, Sensei. But to think you want an innocent little girl like me to push you down and sink her teeth into your private parts is just flat out gross."
        s "First off, I was also using an expression."
        s "Second, why did you immediately assume {i}that{/i} is where I wanted to be bitten? That sounds horrible."
        u "You’re the one who asked for it. All I’m doing is trying to uphold my chastity."
        s "It doesn’t seem like you’re trying very hard based on your no pants policy and seductively unbuttoned, oversized pajama top."
        u "Bein’ comfy ain’t a crime, Sensei. You’re the one who showed up here unannounced."
        u "So unless you think I’m tryin’ to seduce Io or something..."
        s "I like that image. Please continue describing it."
    else:
        s "What? No. Please don't."

    scene utafacetime11
    with dissolve

    u "Why’s your posture gettin’ all weird all of a sudden?"

    if bonus == True:
        s "No reason. Please continue."
    else:
        s "Because I am scared."

    scene utafacetime12
    with dissolve

    if bonus == True:
        u "No thank you, Sensei. If I {i}was{/i} going to seduce Io, I wouldn’t risk ruining the surprise by telling you about it first."
    else:
        u "So, now that we're on the topic of Io."
        s "But we're not on the topic of Io."

    u "You two are close enough to stay in hotel rooms together so, for all I know, you could be wearin’ a wire and feedin’ this all over to her right now."

    if bonus == True:
        s "I give you full permission to search every inch of my body for said wire."
        u "But if I did that, Io would know that I rubbed my hands all over you and suddenly we’d have a big ole love triangle on our hands."

    s "Do you actually hate me or are you just the national grand master of deflection?"

    scene utafacetime13
    with dissolve

    u "It’s nothing personal, Sensei. If I actually thought you were creepy, I wouldn’t hang out with you like this."
    u "I just think the back and forth stuff is really fun and that it wouldn’t be good to jump straight into anything lewd."
    s "And you’re probably right about that. It’s just-"

    if bonus == True:
        u "That I’m such a tease that you can’t help but wanna pick me up and throw me around?"
    else:
        u "You really like need a partner for your professional shuffleboard team?"

    s "Bingo."

    scene utafacetime14
    with dissolve

    if bonus == True:
        u "How about I make you a punch card? "
        u "Six thousand visits to the maid cafe will earn you one kiss. Then six thousand more will let you cop a feel."
        s "These rates are somehow even worse than Nodoka points."

        scene utafacetime15
        with dissolve

        u "Oh! What can we use those for? Because I earned like a thousand during the dorm war sleepover thingy and I don’t know what to do with ‘em."
        s "Collect enough and Nodoka will have sex with you."
        u "Wow."
        s "Thinking of saving up?"
        u "No, I’m just surprised because I watched her give Sana a million of them at the bar and that can really only mean one thing."
        s "I am not even remotely surprised by this."

        scene utafacetime16
        with dissolve

        u "I wonder if she’ll use them."
        s "Sana?"
        u "Mhm. A million should be enough for the grand prize, right?"
        s "I think so...But this is Sana we’re talking about."
        u "So?"
        s "So..."
        s "It’s {i}Sana.{/i}"
        u "Do you think it would be weird if Sana liked girls?"
        s "I think it would be weird if Sana liked {i}anyone.{/i}"

        scene utafacetime17
        with dissolve

        u "You don’t think it would be hot?"
        s "Of course I do. But that doesn’t change how weird it would be."
        u "Hmmmmmmmmmm..."
        s "Why “Hmmmmmmmm?” Why are you being so sketchy about this?"
        u "I’m wearing a wire for Maya and trying to catch you admit that you want to have a threesome with Nodoka and Sana."
        s "Maya, if you are listening right now, this is correct. "
        s "In fact, I welcome any and all threesomes. Bring it on."

        scene utafacetime18
        with dissolve

        u "You’re a really bad boyfriend, Sensei."
        s "Yeah, whatever. Can I have your Nodoka points?"
        u "Can we trade them? Is that allowed?"
        s "I have no idea. "

        scene utafacetime19
        with dissolve

        u "Want me to just kiss her for you?"
        s "I’d much rather redeem this reward on my own."
        s "But, in the event that you do redeem it yourself, I’d greatly appreciate it if I could be there for it."

        scene utafacetime12
        with dissolve

        u "I’m afraid that will be up to Nodoka, Sensei. This is entirely out of my hands."

    "I sigh to myself and attempt to break free of Uta’s incessant teasing loop."

    if bonus == True:
        "I don’t know if it’s her intention to just keep me permanently half-mast but, if it is, she is very much succeeding."

    "A few minutes go by as she scrolls through her phone and I begin to wonder if I’ll have to leave once her brother calls."
    "It’s one thing to stay around and joke with girls while they’re talking to their parents, but..."
    "I’m not sure if I’m brave or...stupid enough to do something like that with a person who has literally attempted murder on the other line."

    s "Uta?"
    u "Yeah?"
    s "What exactly happened with your brother?"
    u "I told you it’s a long story."
    s "Do you not have time?"

    scene utafacetime13
    with dissolve

    u "I have plenty of time. "
    u "It’s just not something I really like talking about."
    s "He didn’t...try to murder {i}you{/i}, did he?"

    scene utafacetime20
    with dissolve

    u "Do you really think I’d be talking to him on the phone if he tried to murder me?"
    s "Good point. "
    s "It’s just my first time talking to someone with a relative in prison, so I can’t help but be a little curious."

    scene utafacetime13
    with dissolve

    u "You’re free to be curious about me or the rest of my family! Mom. Dad. Dead grandpa. You name it."
    u "Let’s save the brother stuff for another time, though. "
    s "I really don’t want to talk about your dead grandpa."
    u "Really? Cause he was a super interesting guy. And a super awesome koto player before his hands stopped working."
    s "Yeah, see, this is why I didn’t want to go down that route."
    s "Just tell me about your parents instead. That sounds easier."

    scene utafacetime21
    with dissolve

    u "You sure you don’t wanna keep flirting with me instead?"

    if bonus == True:
        s "I’m trying a new strategy of getting to know you before getting to the lewd stuff."
        u "Who are you and what have you done with Sensei?"
        s "Oh, okay then. I’ll just go back to trying to make out with you."
    else:
        s "I am offended that you would suggest such a thing when I have been nothing but kind and caring to you."

    scene utafacetime22
    with dissolve

    u "No no no no! It’s fine. I’m just messin’ with ya. I’d be happy to tell you more about my folks."
    u "Just gotta keep in mind that we’re country people and that it’s probably not as interesting of a story as anyone you’d talk to over here."

    scene utafacetime23
    with dissolve

    u "My parents have a pretty huge age gap between ‘em."

    if bonus == True:
        u "Kinda like if you actually started seein’ somebody in our class for real."

    u "They never told me much about how they met or what things were like when they were little, but it seemed to me like they were always pretty happy when I was growin’ up."
    u "And even though we were out in the woods, we weren’t livin’ off the land or anything like that."
    u "Our house was actually kinda big by comparison to a lot of the other ones in the area."
    u "But since they both had full time jobs, my brother and I had to stay at home a lot. And he was the one who watched me most of the time."

    scene utafacetime24
    with dissolve

    u "Then a whole bunch of other stuff happened and I moved here."
    s "Didn't you move here to take care of your grandfather?"
    u "Yup yup! Good ole grandpa Ushibori. "
    s "That isn’t “other stuff.” It's a pretty major detail."
    u "It is!"
    u "But that’s not the only reason I came to Kumon-mi."

    scene utafacetime25
    with dissolve

    u "The “other stuff” meant other stuff."
    u "It was never the intention for me to stay here and finish [high_school]- just like it was never the intention to have me be the only one around when gramps died."
    u "I came because my parents thought it would be good for me to get away for a little while."
    u "And they were already familiar with Io’s aunt from when me and Io would chat online."
    s "What did you have to “get away” from, though?"
    u "That’s the same thing I asked them when they talked about me coming here."
    u "I didn’t like the idea at first. I thought it was hopeless and a waste of time."
    u "But then I thought about how lonely grandpa and Io were...and I decided it would be good to come here and be there for them."
    s "I’m not really sure if I agree with uprooting your entire life for the sake of-"

    "I stop talking mid-sentence, though I’m not sure why."
    "I had a thought-"
    "But the thought disappeared."
    "And it doesn’t return until Uta drags it back by its neck."

    scene utafacetime26
    with dissolve

    u "It didn’t really matter what I wanted. I was going to wind up here one way or another."
    u "Grandpa and Io were just the bright sides I grabbed hold of to help start over. "
    u "Course, I wound up losin’ one of those bright sides to the grim reaper, but now I’ve got a bunch of {i}new{/i} bright sides instead."
    u "I haven’t been here long, but I love Kumon-mi. "
    u "And I love my class. "
    u "And I love yo-"
    s "..."
    u "...gurt."
    s "..."
    s "You love yogurt?"

    scene utafacetime27
    with dissolve

    u "Did you think I was gonna say “you?”"
    s "Did you {i}want{/i} me to think that? Because that’s definitely how it sounded."

    scene utafacetime28
    with dissolve

    u "Sensei! Why are you trying to get me to say I love you when you already have Maya? And Ami? And Ayane? And...everyone else?"

    if bonus == True:
        s "Because {i}you’re{/i} the one I want, Uta."
    else:
        s "Because I feel like you would be the best at hugging."

    scene utafacetime29
    with dissolve

    u "...Huh?"
    s "...?"
    s "I was..."
    s "Were we not doing our back and forth anymore?"

    scene utafacetime30
    with dissolve

    u "Oh!"
    u "Uhh...yeah! "
    u "I just...kinda forgot for a second and...my mind kinda wandered."
    u "Sorry...about that..."
    s "…"
    u "…"

    scene utafacetime31
    with dissolve

    u "…"

    "This is...new."

    u "Soooooo, uhh..."
    u "Yeah. Some more stuff about my parents..."
    u "Let’s see...let’s see..."

    stop music
    scene utafacetime32
    with hpunch
    play sound "phonering.mp3"

    u "Ah! Onii-chan’s jail!"
    u "Perfect timing!"
    s "This timing is horrible. It seemed like you were actually about to fall in love with me or something."

    scene utafacetime33
    with dissolve

    u "I’m sorry, Sensei. But you and I are not meant to be. And even if the red string of fate is wrapped neatly around our fingers, the time will come where we must snap it and-"
    s "Yeah, yeah. Save your rejection for my next hundred confessions."
    s "I’ll leave you and your brother alone."

    scene utafacetime34
    with dissolve
    stop sound fadeout 8.0

    u "Uhh...wait!"
    s "What’s up?"
    u "Do you..."
    u "Um..."

    scene utafacetime35
    with dissolve

    u "Do you think that maybe you could spare some money for his commissary?..."

    scene black
    with dissolve

    s "Goodbye, Uta."
    u "Noooo, wait! How will he be able to afford his ramen without your hard-earned money?"
    s "Use some of the millions of yen I’ve given you."
    u "But that’s mine! I need it for Uta stuff!"
    s "Goodnight, Uta."
    u "Sensei! Come baaaaaaaack!"

    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm15 = True

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadorm20:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label utadorm:
    if uta_love >= 5 and utamaid5 == True and utadorm5 == False:
        jump utadorm5
    if uta_love >= 10 and utadorm5 == True and day != 2 and utadorm10 == False:
        jump utadorm10
    if uta_love >= 15 and day != 2 and utamaid10 == True and utadorm15 == False:
        jump utadorm15
...
```