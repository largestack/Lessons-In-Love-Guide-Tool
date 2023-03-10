# Adulting (Maki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The World Outside The Walls](./sadgirls2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: sadgirls3
* Group: Maki
* Triggered by label: sadgirls2
* Chain sources: sadgirls2
* Chain sources path: sadgirls2

## Official wiki page

[Adulting](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls3&go=Go) for more details.

## Event code

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label sadgirls3:
    $ totaldays += 1
    $ day = 6
    hide friday onlayer date
    show saturday onlayer date

    scene makidayafter1
    with dissolve2
    play music "comfort.mp3"

    maki "Hey, sorry I’m late. I didn’t wind up falling asleep until a few hours ago and may or may not have slept through my alarm."
    s "There’s no need to apologize. I’ve only been here for a little while myself."
    maki "Oh yeah? Did {i}your{/i} husband die too?"
    s "..."

    scene makidayafter2
    with dissolve

    maki "Uhh...sorry. "
    maki "Fair warning, though- I’m one of those “mask the pain with jokes” types. So chances are that it’s going to happen again."
    s "If it happens, it happens. I don’t really have any right to talk about how uncomfortable {i}I{/i} am when you’re the one who has to deal with this."

    scene makidayafter3
    with dissolve

    maki "Well, I appreciate that as you’re the first person I’ve been able to actually talk {i}to{/i} about this. The fact that you respect my newfound status as a widow really means a lot."
    s "Was that another joke?"
    maki "It was supposed to be. It sounded funnier in my head."
    s "What about Sara and Haruka? You haven’t talked to them?"
    maki "I texted Sara yesterday. I’m going over to her place after this so I can tell her the full story."
    maki "Haruka, I didn’t talk to until this morning...but she called me yesterday while I was handling Makoto."
    maki "When I looked at my recent calls, my heart dropped as I figured she’d just gone through the same thing I did...and that she was reaching out for someone to lean on."

    scene makidayafter4
    with dissolve

    maki "Of course, that was before the text about how {i}her{/i} husband is still alive and how hearing the news was the best thing that ever happened to her."

    if harukasex == True:
        "Well, it’s good to see that Haruka has an easier time lying through text than in person."

    maki "Sooo...yeah. I kinda gave up on the idea of calling her yesterday out of a mix of envy and misdirected frustration. "
    maki "Especially considering the fact that she didn’t even {i}ask{/i} if I heard anything about my husband. But hey, she rarely ever finds the time to think about anyone other than herself anyway, so it is what it is."
    maki "Actually, come to think of it, maybe my frustration {i}wasn’t{/i} misdirected...and that it was totally okay for me to be angry about that?"

    scene makidayafter1
    with dissolve

    maki "Either way, it’s fine now. I told her on my way over this morning since I figured it would be easier than letting her see me as a zombie and figuring things out through context."
    s "If it’s any consolation, I think you look pretty good as a zombie."
    maki "It’s the hair. It keeps growing even after death."

    scene makidayafter5
    with dissolve

    maki "But, that aside, I guess you’re probably curious about what exactly {i}happened,{/i} right?"
    s "I’d be lying if I said I wasn’t. But it’s not like I expect you to give me all of the specifics since going over them likely won’t do your mental health any good."
    maki "You know, that’s the weirdest part."
    maki "Like, yeah. Yesterday was one of the most miserable days of my life."
    maki "But when I woke up this morning, I brushed my teeth...I got dressed...fixed my hair in the mirror...and for a moment, I forgot my husband was even dead."
    maki "When you rip away the constant realization of something you love being gone, it’s easy to just trick yourself back into feeling normal."
    maki "I don’t know. Maybe it just hasn’t fully set in yet."
    maki "But being able to sit at this table without needing to use your sleeve to dry my tears is pretty nice."
    s "..."
    r "Uhh...good morning."

    scene makidayafter6
    with dissolve

    maki "Good morning, Rin. I like your hair like that. "
    r "Oh. Uhh...thanks. But that’s...not really why I..."
    s "..."

    scene makidayafter7
    with dissolve

    r "Um..."
    r "Is everything okay? Like...with Makoto?"
    r "I heard that she got called to the office yesterday and never came back. And then Miku left too and..."
    r "And now you guys are here and the vibe is all weird and neither of you have even ordered anything and-"
    maki "You don’t have to worry. Everything’s fine."
    maki "Makoto’s just probably not going to be back in school for a while. "
    r "Is she, like...in trouble? Because we don’t really talk much, but she’s seriously one of the most well-behaved people I’ve ever met. And like, there’s no way she actually did something bad."
    maki "She’s not in trouble, don’t worry. It’s just not something you need to be concerned about right now."
    maki "If Makoto wants you to know, she’ll tell you. But knowing that girl, she probably just wants to keep things to herself for now."

    scene makidayafter8
    with dissolve

    r "Okay..."
    r "Can I at least get you something to drink? Coffee? Tea?"
    maki "Coffee sounds nice, actually. Thank you."
    s "And I’ll just have whatever you decide to make me today."

    scene makidayafter9
    with dissolve

    r "Got it..."
    r "I’ll...uhhh..."
    r "..."
    r "Yeah."

    scene makidayafter10
    with dissolve

    "Rin wanders back behind the bar and begins to get our drinks ready, prompting Maki to focus on her as a means of temporarily escaping the reality of the conversation we’re here to have."
    "I don’t attempt to pull her away as even I don’t like having to do this."
    "The whole way here this morning, I was dreading it."
    "Not because I don’t want to see Maki sad...or not because I don’t want to be {i}aware{/i} that Makoto is sad either..."
    "Those things are horrible, don’t get me wrong-"
    "But the reason I was dreading this is because I have no idea what {i}I{/i} am meant to do here."
    "I can’t {i}console{/i} anyone. And Maki is far too old and not nearly naive enough to treat my words as gospel."
    "She’s an adult dealing with an adult issue in an adult way and I’m..."
    "I’m admittedly not good with things like that."
    "If only her daughter were here."
    "If only there was someone still too inexperienced with the world to see through the lack of meaning in all that I say."
    "And how despite acknowledging that, I still wholeheartedly believe it all."

    maki "I like her."
    s "As...a barista? Or as a human being?"
    maki "Mostly as a barista. She seems pretty high maintenance. But she seems like a good person too."
    s "You deal with Miku on a regular basis and you’re worried about how high maintenance {i}Rin{/i} is?"

    scene makidayafter11
    with dissolve

    maki "Okay, listen. Miku may be hyper, but she’s pretty one dimensional when you strip away the baggage she carries."
    maki "I always know what I’m going to get with her. Just...unreserved, innocent sweetness and childlike fascination with pretty much everything and everyone she sees on a regular basis."
    maki "There’s a reason I call her my second daughter, you know."
    s "Is it because your first one doesn’t like you enough?"

    scene makidayafter12
    with dissolve

    maki "Woah, there! Only I’m allowed to make jokes like that today! When you do it, it just makes everything feel more real."
    s "Sorry. I’m a lot better at dragging down the mood than lightening it."

    scene makidayafter13
    with dissolve

    maki "Then I guess I’ll have to switch roles and be the one to make things sad again."
    s "Or we can just...you know, avoid that."
    maki "If it were a small problem, sure. I’d be all for just ignoring it and waiting for it to get bigger."
    maki "But what we’re dealing with is something that has dramatically altered both my life and my daughter’s life. And seeing as you play a part in both of those lives, you should be in the know."
    s "Maki-"
    maki "Yesterday morning, I got a call from my husband’s branch in the JSDF or...KMDF? Whatever the name of the defense force is called. I really wasn’t paying much attention to that part."
    maki "In fact, I was barely paying attention {i}at all{/i} when the call started since it sounded like it was going to be one of those robots who try to sell you stuff. You know?"
    maki "But just as I was about to hang up, I heard my husband’s name and started to put the pieces together."
    maki "Which is probably why I remember the rest of the call word-for-word when I’ve already forgotten the beginning."

    scene makidayafter14
    with dissolve

    maki "Masahiro Miyamura."
    maki "Status: deceased."
    maki "Cause of death: asphyxiation."
    maki "Date and time of death: June 19th, 21:13."
    maki "Remember to smile."
    maki "Transmission over."
    s "June 19th? But that’s-"
    maki "They waited two months to tell me."
    maki "For two fucking months, my husband has been dead."
    maki "And we’ve been talking about him and telling stories about what we’ll do when he gets back without a single fucking clue."
    maki "Isn’t that ridiculous?"

    scene makidayafter15
    with dissolve

    maki "They didn’t even have the dignity to make a {i}person{/i} call me. "
    maki "To have a {i}real, live fucking person{/i} call and tell me my daughter will never see her father again."
    maki "This is a man who lived for over 30 years...who had a daughter...who went into fucking {i}space{/i} to fight in a war despite being a wimpy ass pacifist...and all he gets in memoriam is an {i}automated phone call?{/i}"
    maki "Are you fucking kidding me?"
    maki "That’s seriously it?"
    s "..."

    scene makidayafter16
    with dissolve

    maki "No...No, it’s fine. That’s not even the big issue right now. After all, he’s been dead for {i}two fucking months.{/i} The big issue {i}now{/i} is getting Makoto over this hurdle. "
    maki "It’s spending the next fucking...I don’t know, two years. Three years. Any amount of fucking years watching her excitedly spout out plans for his return and then {i}remembering{/i} that he’s fucking gone."
    maki "Do you think {i}she{/i} got up this morning, brushed her teeth, and fixed her hair in the mirror? Fuck no."

    scene makidayafter17
    with dissolve

    maki "That’s my little girl, Sensei. That’s my little girl and she’s suffering. She’s suffering and I can’t even do anything about it because, let’s face it, {i}who the fuck could in my shoes?{/i}"
    s "How about you, though?"
    maki "What do you mean? What about me? "
    s "I mean how are {i}you{/i} going to get over this hurdle?"

    scene makidayafter18
    with dissolve

    s "Makoto’s not the only person who lost something. You did too. And you need to grieve just as badly as she does."
    maki "..."
    s "What? Am I wrong?"

    scene makidayafter19
    with dissolve

    maki "Hah..."
    maki "It’s going to be hard explaining this to someone without a kid."
    s "I have Ami. She’s close enough."
    maki "If she was “close enough” you’d understand that what you just said might {i}sound{/i} good...but that’s really it. Just sound. "
    maki "I want to grieve. I want to struggle. It feels wrong {i}not{/i} doing that right now."

    scene makidayafter20
    with dissolve

    maki "But, as of yesterday, I'm the only parent Makoto has left. "
    maki "And if {i}I{/i} start breaking down and forgetting to eat and shower and brush my teeth, there’s no way that she’ll get over this in a healthy way."
    maki "So {i}that{/i} is what I’m worried about right now. Getting {i}her{/i} over this."
    maki "I can cry when that’s done."
    s "..."
    maki "..."

    scene makidayafter21
    with dissolve

    "As if on cue, Haruka walks into the cafe and immediately takes note of the friend she absentmindedly forgot to check on yesterday."

    if harukasex == True:
        "And while Haruka and I certainly have our own share of “issues” that we’ll need to address, that doesn’t matter right now."

    scene makidayafter22
    with dissolve

    "She stops at the counter and grabs a small tray of drinks and assorted pastries that Rin prepared for us but likely refrained from delivering on account of the conversation heating up."
    "With Maki’s eyes still closed in either reflection or avoidance at the sound of the door opening, I find no other space to rest {i}my{/i} eyes than in Haruka’s."
    "In that moment, hers rest in mine as well."
    "And they become congruent not in the fact that they share the same level of concern for someone that we enjoy the company of-"
    "But in the fact that they share in mutual pity."
    "For we may {i}think{/i} that we can connect with Maki in this moment."
    "But truly no one can without having experienced what she has."

    scene makidayafter23
    with dissolve

    "Haruka puts the tray down and fills her arms with something else before saying what any reasonable person in this situation would."

    h "I’m so sorry for your loss..."

    "But what does saying something like that even do?"
    "What good is the apology of an uninvolved party in the face of having your life ripped away from you?"
    "Are we not meant to mask our pity in situations like these?"
    "Are we not meant to scrounge up more genuine responses than we’d be able to find at the bottom of a barrel?"
    "Are we truly supposed to say we’re {i}sorry?{/i}"
    "Why?"
    "It doesn’t make sense."
    "But I suppose most things in this life don’t."
    "And I suppose that sometimes a genuinely sorrowful canned response can work as serviceable acknowledgment of that."

    maki "Thanks, Haruka. "
    maki "I’m really happy for you."
    h "Maki...if I knew that your husband-"
    maki "Don’t worry about it. You were excited and...wanted to share the news with someone."
    maki "You had no way of knowing."
    h "But if I did, I-"
    maki "It doesn’t matter."
    maki "So...thanks for your apology. I really appreciate it. But if you don’t mind, I’d like to finish up my conversation with Sensei. "
    maki "You and I can talk later."

    scene black
    with dissolve2

    "Maki tells me more about what she expects from Makoto going forward."
    "She has no idea when she’ll be able to return to school, but assured me that it wouldn’t be a problem as Miku would be taking all of her work directly to her."
    "As if that would even matter right now."
    "I’m not just saying this because I am a horrible teacher, but the last thing I expect out of a girl whose father just died is {i}schoolwork.{/i}"
    "Regardless, I nod and tell Maki not to worry about it- going so far as even offering to deliver Makoto’s “schoolwork” myself."
    "But of course, she in her unwavering devotion to not burdening anyone, refuses such a gesture before getting up from the table and straightening out her clothes."

    scene makidayafter24
    with dissolve2

    maki "Thanks again for meeting with me. I didn’t want the Maki from yesterday ruining your thoughts about the Maki from the future."
    s "I like all Makis equally. Though, I could do with this one being a little more selfish when it comes to her personal feelings."
    maki "Psht. Who needs feelings anyway? All they ever do is get in the way."
    maki "I’ve got a genius to take care of, Sensei. If she stays upset, she’ll never develop the cure for whatever the next big pandemic is."
    maki "I am doing this to save the world. My tears mean nothing in the face of the greater good."
    s "Well, whatever the case, good luck. And if you need any help with Makoto, don’t hesitate to ask."

    scene makidayafter25
    with dissolve

    maki "Leave it to me, Sensei!"
    maki "There’s no problem that Maki Miyamura can’t handle!"

    scene black
    with dissolve2

    "Maki says goodbye and wanders off to meet up with Sara and give her what I imagine will be a very similar speech."
    "I watch from the opposite side of the window, expecting to see her break down now that she’s no longer faced with a situation where she feels obligated to keep her tears in."
    "But she’s an adult."
    "So she probably holds it in until she’s at least a few blocks away."

    $ renpy.end_replay()
    $ sadgirls3 = True
    $ maki_love += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    jump sadgirls4

label sadgirls6:
...
```

## Code that triggers this event

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
h "AAAAAAAAAAAAAHHHHHHHHHHHHHHHHHH!!!!!!!!!"
        h "I DON’T...KNOW WHAT...TO DO!!!"
        h "I LOVE MY HUSBAND! I LOVE HIM SO MUCH! BUT..."
        h "BUT I DON’T WANT YOU TO LEAVE!!!"
        h "AND I KNOW THAT MAKES ME A BAD PERSON! I’M HORRIBLE! UNFAITHFUL! "
        h "BUT I DON’T KNOW WHAT ELSE TO DO!!!"
        h "WHAT IF HE NEVER COMES BACK?! I DON’T WANT TO KEEP BEING ALONE!"
        s "I know. You just want someone to kill the loneliness-"

        scene harukasgoodday20
        with dissolve

        h "That’s not it either!"
        h "Just {i}someone{/i} isn’t good enough! It has to be {i}you!{/i}"
        s "I don’t-"
        h "I wasn’t lying when I told you I needed you! I do! I just...don’t know how!"
        s "..."

        scene harukasgoodday19
        with dissolve

        h "You can hate me if you want! I already hate myself! Just...don’t leave me yet! Not yet! Please!"
        s "..."
        h "PLEASE!!!!!!!!!!"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene bedroom_night
        with dissolve2

        "Despite her pleas for me to stay, I wound up leaving Haruka."
        "Though, not for good- as I may have contemplated for a moment."
        "My desire to stay can be traced to more than just how sexually compatible we are, though."
        "The truth is that I enjoy being needed. And, for some reason, she’s decided to latch onto me like some sort of sea lamprey, using her teeth to scrape away at what’s left of me so that {i}she{/i} can flourish."
        "Or maybe a leech would be a better-suited metaphor."
        "She’s something grotesque, yet anatomically interesting in the fact that there’s much I’ve left to learn about her body."
        "But, for the moment, I think it’s best if she suffers in silence. "
        "Especially considering those who have it worse."

        $ sadgirls2 = True

    play sound "phonering.mp3"

    s "..."

    play sound "phonebeep.wav"

    s "Hello?"

    "I hear a sigh on the other end of the phone- likely as a result of me answering too quickly and not giving the caller a chance to prepare her opening statement."
    "I wait, as I have a feeling that what comes next will be the handful of sleeping pills I take before bed tonight."

    maki "I..."
    maki "I wanted to say I’m sorry for yelling at you earlier."
    maki "A lot happened."
    maki "A lot that...I’m sure you figured out when you walked into the bathroom."
    s "You don’t have to apologize. I shouldn’t have followed you."
    maki "You were just worried. I understand."
    maki "Telling Miku where we were was a good move, though. She was able to cheer Makoto up a lot better than I was. "
    s "I’m sure that’s not-"
    maki "Listen, uhh..."
    maki "Can we meet up in the morning? Maybe at the cafe? "
    maki "This isn’t really something I should keep you in the dark about."
    s "I don’t really think it’s necessary to get me involved with your family matters."
    maki "It is when my daughter is one of your students."
    maki "Because there’s no way in hell that this isn’t going to have a huge impact how she is in school. And it’s something I need to know you’ll be able to handle."
    s "Then, sure..."
    s "We can meet up."
    maki "Thanks. "
    maki "Anyway, uhh...goodnight, I guess. Not that I’ll be able to sleep much. "
    maki "I just..."
    maki "Yeah."
    maki "I’ll see you tomorrow."

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "Maki hangs up the phone without giving me a chance to say goodnight."
    "But as I climb into bed, it is not her that I think about."
    "It is her daughter."
    "And the fact that she now has no choice but to fall further into me than she already has."
    "So far that even I might lose track of her."

    $ renpy.end_replay()
    stop music fadeout 10.0

    "{i}When you fall asleep, you dream of a bluejay.{/i}"
    "{i}Its beak breaks and you must help it preen its feathers.{/i}"
    "{i}The keratin tastes like the outermost layer of a coconut.{/i}"
    "........."
    "......"
    "..."

    jump sadgirls3
...
```