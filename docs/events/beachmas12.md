# Robin Hood (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Toys](./makotofutabafuntimelustevent.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachmas12
* Group: Main
* Triggered by label: makotofutabafuntimelustevent
* Chain sources: makotofutabafuntimelustevent
* Chain sources path: makotofutabafuntimelustevent

## Official wiki page

[Robin Hood](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas12&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label beachmas12:
    play sound "phonebeep.wav"

    "My phone goes off on the way to the normal breakfast hangout spot the girls have flocked to over our last several trips. But when I look down to inspect the sender, I am quickly filled with both fear and remorse."

    "{i}You have received a text message from Maya Makinami!{/i}"

    s "...shit."

    play music "notabluearchivesong.mp3"

    "Getting sidetracked on my quest to find the missing class members last night completely overwrote the plans I made with Maya earlier that day."
    "But if Maya knows me as well as she is supposed to, she should have expected such a thing and followed up with me rather than just {i}allowing{/i} me to forget her."
    "Unless her plan was just keeping me from going on a date with Ayane instead. To which I say...smart."

    play sound "phonebeep.wav"
    scene sky with dissolve

    m "{i}Good morning. Are you still alive?{/i}"

    "I swallow my pride and text her back to prove that my heart still beats, just not entirely for her."

    s "{i}Good morning and yes.{/i}"
    m "{i}How unfortunate. I was beginning to hope that you had been mauled by bears as that would be the only reasonable explanation for bailing on the incredibly rare opportunity to go out on a date with me.{/i}"
    s "{i}There’s always your birthday next week.{/i}"
    m "{i}I’m shocked you’re able to remember that but not something twelve hours into the future.{/i}"
    s "{i}I forgot, Maya. I got caught up in something else.{/i}"
    m "{i}Yes, I realized that after watching you walk away from me without so much as a glance last night. But I suppose this is what I get for extending any amount of kindness to you.{/i}"
    s "{i}Texting with you sure is fun. We should do this more often.{/i}"
    m "{i}Delete my number and never talk to me again.{/i}"

    "Welp, it’s safe to say that Maya is mad. And understandably so."
    "But the silver lining to this is that I made similar arrangements with her arch-nemesis tonight and, if the past repeats itself (Which it so typically does around here), I’ll be disappointing Noriko next."
    "And if there is anything I know about Maya, it’s that hurting Noriko will make her happy. I just...still don’t exactly understand {i}why.{/i}"

    u "Yes! I win! Take that, Miku!"

    scene  anothermorningbeach1
    with dissolve2

    u "I {i}told{/i} you Sensei wasn’t dead! He was probably just having a romantic rendezvous with a secret lover of his for hours and hours and hours last night!"
    mi "Man! I was really bankin’ on him bein’ eaten by bears."
    s "What is it with everyone and wanting me mauled by bears this morning?"
    i "What is it with you disappearing so early on in the night without so much as saying anything? Do you have any idea how many times I knocked on your door hoping that you were around? I was so bored."

    scene anothermorningbeach2
    with dissolve

    mi "You should’a just hung out with me and Sana. All we did was play games and that ain’t much of a social thingy."
    i "I’ve seen the kinds of “games” she plays in her spare time and I have never been less interested in anything."
    mi "You got somethin’ against Minecraft, Io?"
    s "Uta, thank you for believing in me when Miku and many others so clearly didn’t."
    u "Any time! You’re not off the hook {i}yet,{/i} though! Just cause I believed you were alive doesn’t mean I’m not also suspicious of your disappearance. Specially since Makoto and Futaba were gone all night as well."

    scene anothermorningbeach3
    with dissolve

    mi "Yeah! What was up with that?! I know Makoto’s been havin’ some sleepin’ problems, but she ain’t the type to just sneak out in the middle of the night without a good reason!"
    s "Well...maybe she had a good reason?"
    mi "Like what? Gettin’ nasty with the teacher and everybody’s favorite librarian? This some kinda porno now?"
    s "Yeah, as if that would ever happen."

    if makotofutabafuntimelustevent == True:
        i "You look mighty pale all of a sudden, Sensei. "
        s "I have no idea what you’re talking about. "
        u "You {i}do{/i} look kinda like you saw a ghost right now. Not gonna lie."

        play sound "static.mp3"
        scene wearethechildren12 with flash
        scene anothermorningbeach3 with flash
        stop sound
    else:
        s "Besides, if any of you were smart enough to check this morning, you would have realized that I {i}did{/i} come home last night. I slept in my room and everything."
        i "Hey, I’m smarter than the two of them combined."
        s "So is Ami and that’s not saying much."
        u "Fair."
        mi "Yeah, that tracks."
        i "Also, if you understood anything about how my stupid brain works, you would realize that coming to your room in the {i}morning{/i} is both nerve wracking and terrifying."
        i "I have walked in on one utterly disgusting thing this weekend and was not about to risk the chance of walking in on a {i}second{/i} one that would just hurt my feelings as well."
        mi "Think Io means she didn’t wanna walk in on you railin’ Imani or something."
        i "Or anyone. Yeah."

    s "Listen, what I do in my free time is for me to know and all of {i}you{/i} to ignore if you don’t want your feelings getting hurt."
    s "But I can guarantee you that whatever it was didn’t involve Makoto or Futaba."

    scene anothermorningbeach4
    with dissolve

    i "I don’t believe that at all. But if I try hard enough, I can {i}make{/i} myself believe it and continue to live happily inside of my own world where the only person who matters to you is me! And sometimes Uta."
    u "Yay...sometimes Uta..."

    "Well, you can’t say I didn’t try."

    if makotofutabafuntimelustevent == True:
        "It’s just...lying through my teeth is way safer than telling the truth right now when the truth involves the most ejaculations I’ve had in one night since Chika lost her virginity."
    else:
        "Especially since telling them I {i}was{/i} with those two girls but that nothing happened would be met with more doubt than just flat out lying."

    s "My night aside, what are you three doing out here so early? It seems like everyone else is still back at the inn."

    scene anothermorningbeach5
    with dissolve

    u "You know what they say about the early bird getting the worm, don’t you? Well, today, that worm was sausage. And Uta loves herself some sausage."
    s "Yeah. I could tell by the way you stared at me yesterday. And then asked me to come on you."

    scene anothermorningbeach6
    with hpunch

    u "Hahah! Fun memory! Are you hungry?! Let’s eat!"
    mi "Uta too, Sensei?! Am I gonna start havin’ to make a list?!"
    s "Just win a contest and make me write one. That’s been proven to work and only {i}temporarily{/i} harms the recipient. "
    i "Boy, it sure is great being able to ignore everything I don’t like hearing! Looks like my brain’s getting a workout first thing this morning!"
    u "{i}Fix this.{/i}"
    s "Fix what?"
    u "{i}You’re making things awkward.{/i}"
    mi "I think it’s you who’s makin’ things awkward by whisperin’ so loudly the whole table can hear ya. And sayin’ all that stuff about lovin’ sausage. Course Sensei’s gonna capitalize on that."

    scene anothermorningbeach7
    with dissolve

    u "Just, uhh...just so we’re all on the same page and nobody harbors any ill-will against poor and defenseless Uta-chan for things you don’t have the context for..."
    u "The...{i}coming{/i} thing was..."
    u "That was a slip of the tongue..."
    mi "Hey, we don’t need to know what you’re doin’ with your tongue in your free time. I just didn’t think you guys were up to that kinda stuff together."

    scene anothermorningbeach8
    with dissolve

    u "We’re not...and we never will be."
    i "So, onto topics that aren’t disgusting or inappropriate for the breakfast table, do you notice anything new about me?"
    s "New? I’ve seen you with your hair down before. That’s not new."
    i "That’s not what I’m talking about."
    s "Uhh..."
    s "Are you...on a new medication?"
    i "Nope. But that’s a fair guess."
    s "Io, I’m going to be honest. I have no idea what you’re talking about."

    scene anothermorningbeach9
    with dissolve

    i "I did the thing you wanted me to do and made a new friend! I’ve been sitting next to Miku this whole time and haven’t been dying inside! Well, no more than usual at least."
    i "And what’s even better is that it’s not Kirin!"
    mi "She ain’t for everybody. I get it."
    s "You and Miku are actually {i}friends{/i} now? That’s the least believable part of this timeskip yet."
    i "Timeskip? "
    s "Doesn’t matter. How did {i}this{/i} happen, though? Miku’s one of the loudest- wait. "
    s "You confused her for a boy, didn’t you?"

    scene anothermorningbeach10
    with dissolve

    mi "Don’t worry, Io. I forget I’m a girl sometimes too."
    i "Well, it {i}does{/i} help that she’s not annoyingly feminine..."

    scene anothermorningbeach11
    with dissolve

    i "But we found something we can bond over!"
    s "Oh, right. You’re into baseball, aren’t you? Miku’s always been into sports-"
    mi "I ain’t that into baseball, actually. Think Io’s talkin’ about her anti-mind-explosion pills."
    s "What?"
    i "I’ve designated myself as Miku’s personal pharmacist and have been sharing some of my meds with her lately to help with her PTSD!"
    mi "It’s actually been a huge help. I’ve only had a couple bad reactions so far and Io says it’s just cause she didn’t get the measurements right or somethin’."
    s "I..."
    i "What?"
    s "I have...a strong and uncharacteristic urge to try and be responsible right now."
    i "Suppress it. That’s what I do with all of the stuff I’m not supposed to feel."
    u "I think Sensei’s right, Io. I’ve been wantin’ to say something, but I don’t really think it’s a good idea to be sharing that kind of stuff with Miku if she hasn’t been prescribed it."
    s "Not to mention I’m pretty sure that counts as drug dealing and is extremely illegal."

    scene anothermorningbeach12
    with dissolve

    i "Technically, yes. But the chances of a girl my age actually getting in trouble for that sort of thing are basically non-existant. Plus, the meds have been helping a lot, haven’t they?"
    mi "Yeah! I feel great. Haven’t had a thing happen in almost a whole month. Might even be a new record."
    mi "Plus, I ain’t got the money for that kinda stuff and Io gets it all for free. So it’s like everybody’s winning, ain’t it?"
    u "I mean...yeah, but...you’re not exactly a doctor and-"

    a "AH! THERE YOU ARE!"

    scene anothermorningbeach13
    with fade

    i "Uh-oh. Looks like Sensei’s in trouble now and we should all focus on the things {i}he’s{/i} doing wrong instead of me being the Robin Hood of Valium."
    a "What do you think you’re doing disappearing for a whole night without checking in with me?! I was worried sick!"
    s "I mean, if you really want to get technical, you took your eyes off of me during Ami time, so this is {i}kind of{/i} your-"
    a "Don’t go blaming this on me, Mister! Not after I dragged Ayane and Maya around for hours looking for you in the middle of the night!"
    a "Just look at how mad Maya is! You interrupted her very strict sleeping schedule!"
    s "Yes, I’m sure that’s exactly why Maya is mad."
    m "Did he say something, Ami? I promised myself last night I’d never listen to another word he said."
    a "Yes. He said he hates you and that he isn’t sorry for what he did because he is a giant, insensitive jerk who I still love more than anything in the world, but come on! You’re better than this!"
    a "At least invite me out next time you vanish so I can make sure you’re not doing anything I disapprove of!"
    s "Ami, I don’t have an excuse. I wandered off looking for people and then passed out. It’s that simple."

    scene anothermorningbeach14
    with dissolve

    a "That {i}is{/i} an excuse. And it's the {i}same{/i} excuse you've given me {i}every time{/i} you've come home super late."
    s "Yeah, so you should know that there is a precedent for this and that I’m not lying. Case closed."
    a "I’m not buying it. I sentence you to three consecutive years of Ami time, ending with high school graduation..."
    a "Which will then be followed by the two of us moving to a completely fenced-in facility where you are unable to leave without a passcode that only {i}I{/i} have. "
    a "It’s only fair, Sensei."
    s "That doesn’t sound fair at all."
    m "Sounds pretty fair to me. May I leave?"
    a "Thank you, Maya. You are excused."

    scene anothermorningbeach15
    with dissolve

    "Maya storms off and-"

    play sound "phonebeep.wav"

    m "{i}Die.{/i}"
    s "{i}Do you really have to be this dramatic?{/i}"
    m "{i}Yes.{/i}"
    s "{i}Let me make it up to you tonight.{/i}"
    m "{i}No.{/i}"
    s "{i}But I need you. Without you, I will simply perish.{/i}"
    m "{i}-_-{/i}"
    a "Who do you think you’re texting while you’re supposed to be talking to me?"
    s "Sorry. Just canceling all of my plans for the rest of eternity so we can spend that time together instead."

    scene anothermorningbeach16
    with dissolve

    a "Great! In that case, I forgive you. And I have a whole list of activities planned out for the rest of the day where we can show our love for one another without the worry of anyone else getting in the way."
    s "Should I wear a leash? It might help with how controlling you want to be."
    a "Sure! I packed one just in case you wound up seeing things my way and would be happy to break it in."
    s "Please tell me you don’t actually want to drag me around on a leash."
    a "Okay. I don’t actually want to drag you around on a leash."
    s "Ami."

    scene anothermorningbeach17
    with dissolve

    a "I totally want to drag you around on a leash."

    if amifingered == False:
        s "For the millionth time, we can’t-"

        stop music
        play sound "static.mp3"
        scene anothermorningbeach18
        with flash
        stop sound

        a "Yes! I know! You’ve made it loud and clear that you don’t care about how I feel! And that you’ll never look at me the same way I look at you!"
        a "But if that’s the case, stop saying things that you {i}know{/i} are going to make my heart go crazy! Because there is only so much of it I can take before I break!"
        u "Woah."
        i "Holy shit. Ami’s really-"

        play sound "static.mp3"
        scene anothermorningbeach19 with flash
        stop sound
        play music "notabluearchivesong.mp3"

        a "Just kidding! Tee-hee!"
        u "Never mind. Ami is normal."
        i "Yes. Ami is normal."
        s "Ami is so cute."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Ami drops the leash idea after a small bit of prodding and leads me to an annex of the beach inn that I have never noticed before. "
    "It’s just beyond the manmade baths and half-concealed by fallen trees to the point where it would be very easy to overlook if you didn’t already know about it."
    "How she found out, I’m not sure. But I follow her regardless, staying closely behind until she opens the doors and signals for me to go in first."

    $ renpy.end_replay()
    $ beachmas12 = True

    "........."
    "......"
    "..."

    if amifingered == False:
        jump amilust35skip
    else:
        jump amilust35intro

label beachmas13:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
"I lose track of how many times I fuck the two of them."
    "And while Makoto may have held the lead in the very beginning for the amount of cum extracted from me, it becomes a bit of a game for us to toy with Futaba following her vomit incident."
    "We tease her..."
    "Force orgasm after orgasm out of her..."
    "And we laugh while doing it."

    scene black
    stop music

    "It’s the best dream I’ve ever had."

    $ futaba_lust += 5
    $ makoto_lust += 5

    "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
    "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
    "........."
    "......"
    "..."

    scene actualthreesome15
    with dissolve4
    $ totaldays += 1
    $ day = 2
    hide monday onlayer date
    show tuesday onlayer date
    $ renpy.pause(4, hard=True)
    scene actualthreesome16
    with dissolve3
    $ renpy.pause(3, hard=True)
    scene actualthreesome17
    with dissolve2
    $ renpy.pause(3, hard=True)
    scene actualthreesome18
    with hpunch
    play music "10c.mp3"

    mak "WHAT THE FUCK?!?!?!"

    scene actualthreesome19
    with dissolve

    s "Hm?..."
    mak "W...Where are my clothes? Where are {i}all{/i} of our clothes?!"
    s "What’s going on?"

    scene actualthreesome20
    with dissolve

    mak "Did...did you drug me?! What the fuck, Sensei?"
    f "Haaaaah......good morning....."
    mak "What do you mean “good morning?!” Were you in on this too?!"
    f "In on what?...Why are you yelling?..."
    mak "Uhh...Because we’re naked in the woods and covered in semen?!"
    f "We’re what?..."

    scene actualthreesome21
    with hpunch

    f "{i}WE’RE WHAT?!{/i}"
    mak "I’m just as confused as you are! Why would you date rape girls you’re already sleeping with?!"
    s "Futaba, why are you shielding my eyes from something I’ve seen a million times before?"
    f "Because this is embarrassing and confusing and I feel gross right now!"
    mak "What did you do?! {i}Why{/i} did you do?! WHY DO?!"
    s "Hey, I’m just as confused as you are. "
    s "But I guess since we’re already naked-"
    mak "GO TO HELL!"

    scene black
    with dissolve2

    f "Oh God! Oh no! I have like twenty missed text messages!"
    mak "And I have-"
    mak "I have...one."
    mak "Seriously? That’s it? What the fuck, Miku?"
    f "We...We can’t ever tell anyone about this. We have to forget it ever- ack. What’s in my mouth? Is this a hai- OH MY GOD. EW! NO! NO, NO, NO!"
    mak "Where did you put our clothes, you date raping bastard?!"
    s "I told you, I have no idea how this happened. I don’t even know where {i}my{/i} clothes are."
    mak "LIKE I’M GOING TO BELIEVE THAT!"

    stop music fadeout 15.0

    "The truth is that I did have an idea."
    "I remember everything from the moment I woke up here the first time to the moment I woke up the second."
    "It’s what comes {i}before{/i} it that I can’t remember."
    "But..."
    "That’s a trade I’m willing to make."
    "Because I’m sure whatever that was wasn’t significant at all."
    "And I’m sure it’s a memory I’m okay with parting with."
    "{i}Futaba and Makoto send Sensei back to the beach first so they can clean themselves off and repair their broken bathing suits.{/i}"
    "{i}He swears to himself along the way to never tell a soul about this.{/i}"
    "{i}And prays to a god he does not believe in that the two of them never remember the details.{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ makotofutabafuntimelustevent = True

    jump beachmas12
...
```