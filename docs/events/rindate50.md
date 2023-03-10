# The Happiest Girl in the World (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* rinbetrayed equal to False (unknown variable)

* Event [Lifejacket](./rindorm50special.md) (Rin) is completed)

* rinnumber equal to True (unknown variable)



## Next events

* [Main: Girls in Spandex](./halloweentwo1.md)

## Event properties

* Id: rindate50
* Group: Rin
* Triggered by label: callrinnight
* Triggered by branch label: callnight
* Triggered by path: callnight->callrinnight->rindate50

## Official wiki page

[The Happiest Girl in the World](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindate50&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label rindate50:
    play sound "phonebeep.wav"

    "I tap on Rin’s name in my phone and wait for her to answer. "
    "I’m not sure if she’ll pick up or not following the recent episode in her dorm room, but even {i}I’m{/i} not horrible enough to just leave her hanging if she feels like shit."
    "I was there for Molly, wasn't I? "
    "Granted, I don’t really think I did anything to {i}help{/i} her...but {i}she’s{/i} still alive and, at least to my knowledge, not cutting herself."

    s "…"

    "The phone rings for longer than normal."
    "I’m not sure if Rin is just one of those people who never bothered setting up a voicemail box, but at this point, I feel like I’d probably be better off-"

    play sound "phonebeep.wav"

    s "…"

    "Well, nevermind then."

    s "Rin?"

    "…"

    "I can hear breathing, so I know she’s there...but she’s sure taking her sweet ass time to say hello."

    s "I know you’re there, you know. I can hear you."
    s "…"

    play music "lastdailysong.mp3"

    r "Hey. "

    "I stop pacing around and lean up against the first wall I see to better focus on the conversation."
    "I have a feeling it might be a rough one."

    s "What’s up?"
    r "…"
    s "…"
    s "Rin-"
    r "Are you...free right now, by any chance?"
    s "I wouldn’t have called you if I wasn’t."
    r "Do you think we could maybe...meet up or something?"
    r "Like, somewhere private."
    s "You don’t want to bring Futaba along?"
    r "No...Not this time."
    r "I kind of just want it to be you."
    s "That’s...odd."
    r "Why? Do you not want to?"
    s "No, it’s just that you don’t normally ask to be alone with me when it doesn’t involve your feelings for a girl in some way or another."
    s "Did something happen with Otoha?"
    r "No, Otoha’s great. It’s just..."
    r "It’s just not something I can talk to her about. And Futaba’s already worried sick, so..."
    s "There’s always Molly."
    r "Please, I’m asking for you. "
    r "I want to see you."
    s "Well then hurry up and tell me where to go. It’s not doing you any good just waiting wherever you are."
    s "Oh, where {i}are{/i} you by the way?"
    r "Just in the dorm right now. "
    r "I don’t really want anyone else to see us, so...is it okay if we hang out in some sketchy alley or something like that?"
    s "What a strange request."
    s "You’re not planning on taking advantage of me, are you?"
    r "The only thing I’ll be taking advantage of is your................time."
    s "…"
    r "Get it? Because I paused for a-"
    s "You’re not upset at all, are you?"
    r "I have no idea what I am, Sensei."
    r "I’ll see you soon."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Rin hangs up the phone and sends me an address not far away from the creepy cathedral Yasu hangs out at."
    "Great."
    "I slide my phone into my pocket and figure that it’s just a coincidence and that Rin isn’t also just a religious cult member now..."
    "But, in the event that she starts trying to indoctrinate me next, I should be prepared."
    "I slide a bullet into the chamber of my revolver and get ready to fight for what I love, which is...not loving anything."
    "Then, I wave my hand to remind myself that the revolver is imaginary and set out toward an area of Kumon-mi that’s almost as sketchy as the second half of town."
    "………"
    "……"
    "…"

    scene rinhappynight1
    with dissolve

    r "Umm...hey."
    s "Hey. You look like shit."
    r "I feel like shit. But I think I’m getting close to the tail end of it."
    s "Did you...come all the way here without a jacket? Aren’t you cold?"
    r "Yeah. I don’t know."
    r "I left it at the dorm and didn’t feel like going back for it."
    s "So you just walked a few miles without it instead."
    r "Pretty much, yeah."
    s "So, what’s the reason for this incredibly suspicious private meeting in the middle of nowhere?"
    r "Venting, I guess? Taking my mind off of stuff."
    r "Probably just going to rattle off a bunch of stuff that’s been popping into my head and hope you can help with some of it because, weirdly enough, I really trust your judgement."
    s "Well, that seems like a horrible idea on your end. My judgement is terrible."

    scene rinhappynight2
    with dissolve

    r "It’s really not, though..."
    r "Like...you’ve never done anything messed up to me and we’ve been friends for a really long time now."

    if bonus == True:
        r "You even gave me a chance to confess to Chika before going after her...when you knew all along that you could have had her whenever you wanted."
    else:
        r "You even gave me a chance to confess to Chika before you started hugging her when you knew all along that you could have had her whenever you wanted."

    r "I...really care about your advice. And I kind of need a lot of it right now."
    s "I’m starting to think I might be a bad influence on you if you’re coming to {i}me{/i} for advice."

    scene rinhappynight3
    with dissolve

    r "Then just pretend I’m coming to you like you’re my counselor and not {i}Sensei{/i}."
    s "You wouldn’t know this since you never show up for counseling, but I’m just as bad at that as I am at normal advice."
    s "In fact, I’m probably even worse when the counselor mask is on."

    scene rinhappynight4
    with dissolve

    r "Well then I guess you {i}are{/i} a bad influence and...that you’re just rubbing off on me or something, because I have no idea who else to talk to about this, or..."
    r "Or how I’m even {i}going{/i} to talk about this because it’s all just circling around inside of my head like some...fucked up, broken washing machine."
    s "Weird comparison, but I get it."
    s "Before that, though, how is your arm?"

    scene rinhappynight5
    with dissolve

    r "Sore."
    r "I obviously have to wear sweaters and stuff to cover everything up, but my sleeves keep sticking to the cuts as the scabs are forming."
    r "And every time I move my arm too quickly, it rips them off and reopens a few and it’s just rinse-repeat, rinse-repeat."
    r "It’s weird, cause like...when I’m doing it, I can barely even feel it. It’s always the days after that hurt the most."
    s "Well, if you don’t mind me going on one of my famous depressing tangents-"

    scene rinhappynight6
    with dissolve

    r "Ooh, I love those! They’re fun!"
    s "Thank you."
    s "But anyway, that feeling you described is essentially just how pain works as a whole."
    s "Nothing is ever its worst as soon as it happens."
    s "The natural reaction to bad news or a traumatic injury is panic."
    s "You don’t have time to really {i}think{/i} about what went down or...feel anything, because it’s all happening so fast."
    s "I’m sure whatever was going through your head at the time of...what you were doing to yourself is no exception to that."

    scene rinhappynight7
    with dissolve

    r "I told you, though...there wasn’t {i}anything{/i} going through my head. That’s why it was all so weird."
    r "It’s like when the battery of your phone dies or something. An immediate switch from full of life to...complete blackness."
    r "And the only thing that can bring it back to life is a surge of power."
    s "You don’t need to explain it or anything. I just don’t want you doing something that will not only put you in danger but ruin everything you finally have going for you."

    scene rinhappynight2
    with dissolve

    r "See, this is why I wanted to see you."
    r "Futaba’s great, but she’s too sentimental when it comes to stuff like this. You’ll just give it to me straight."
    r "Call me a fucking idiot, Sensei. Do it."
    s "Okay. You’re a fucking idiot."
    r "Now...tell me to beat this stupid depression’s...stupid face!"
    s "Beat your stupid depression’s face or whatever."
    r "Now tell me you love me!"
    s "No."

    scene rinhappynight8
    with dissolve

    r "Aww. Mean."
    r "I love {i}you{/i}."
    s "Sorry, did I turn into Otoha overnight or something?"

    scene rinhappynight6
    with dissolve

    if bonus == True:
        r "No, but if you ever do, please send nudes."
        r "I need them to hold me over as I endlessly fight off the undying need to tackle her and just...{i}ugh.{/i}"
        s "Hang in there, Rin. I’m sure it’ll happen soon enough."
    else:
        r "No way. You don't have nearly enough rings."
        s "I would if they could only fit on my stubby little fingers."

    scene rinhappynight7
    with dissolve

    r "I know, I know...It’s just..."
    r "You know what, come with me."
    r "I know nobody’s around because this part of town is dead, but I’d feel a little more...secretive if we weren’t in the middle of the sidewalk."

    scene black
    with dissolve2

    "Rin scurries off and, for a brief moment, her childish energy distracts me from the bags beneath her eyes."
    "It takes a special type of person to wear a smile like that on a body covered in scars, and I’m reminded once more of why I took to Rin in the first place."
    "She’s like a canvas that an artist accidentally spilled every one of his paints on."
    "But instead of trashing it like anyone else would do, he started punching it and punching it, filling it with holes in the shape of a face that, if you look closely enough, resembles something we’ve all felt before."
    "The inherent desire to love and be loved, mixed with a tinge of self-doubt and so many hormones that one good stroke would do it in for the night."
    "This is the person Rin is."
    "A mixture of bad things and good things, held together with glue made from only the best of bodily fluids."
    "It’s a shame she still seems so far away from that last part, though."

    scene rinhappynight9
    with dissolve

    r "Okay. This is {i}slightly{/i} better than out there in the open."
    s "What was it that you couldn’t tell me twenty feet away from where we’re standing right now?"
    r "Just more stuff about Otoha, probably."
    r "And how I’m worried I’m gonna snap and do something bad before she’s ready for it."
    s "Probably not the best idea, Rin."

    scene rinhappynight10
    with dissolve

    r "Then...teach me how to control myself better!"
    r "I don’t wanna mess things up, and I’m already one step closer to doing that by hiding my cutting from her."

    if bonus == True:
        s "You’re asking {i}me{/i} how to...not have sex with girls?"
    else:
        s "Are you asking me to purchase you a straight jacket?"

    r "No, dude. I’m asking you how you always manage to hold yourself back."

    scene rinhappynight11
    with dissolve

    r "The Chika thing {i}still{/i} surprises me."
    r "Like...I’m not allowed to say this anymore because girlfriend-"
    s "I won’t say anything. Don’t worry."
    r "I know. I was gonna say it anyway because I trust you. But yeah, Chika is {i}so{/i} fucking hot."
    r "I don’t know how you kept your hands to yourself. I really don’t."

    if bonus == True:
        s "There was just someone else I liked more, I guess."
    else:
        s "Easy. I have a complete disinterest in both romance and intercourse and am only here to make all of you happy and help you pass college."

    scene rinhappynight12
    with dissolve

    r "And, like..."
    r "With me too."

    if bonus == True:
        r "Not just with the delirious flashing stuff and the...random kiss we had after our date. But like, as a whole."
        r "Why didn’t you ever push for more?"
        r "You wanted to, didn’t you?"
        r "I might seem dense sometimes...but there have been a lot of moments where I’ve thought, “You know, I wouldn’t stop him if he did something right now.”"
        r "But you never did."
        r "I don’t want you to tell me {i}why{/i}, though. I want you to tell me {i}how{/i}."
        r "How can I do that with Otoha to avoid ruining the best thing that’s happened to me since meeting you?"
        s "Wow. Was I really the best thing up until that?"
    else:
        r "I know you know about the trombone, Sensei..."
        r "And I know...you've always wanted to try playing it as well..."
        s "Not now, Rin. I'm not ready to talk about that yet."

    scene rinhappynight13
    with dissolve

    r "I wasn’t kidding when I said I loved you, you know."
    r "Not everyone would hold my wrist and call my roommate in the middle of the night to come take care of me."
    r "Not everyone would volunteer to let me cry into them if things get terrible."
    r "And not everyone would come meet me in some sketchy part of Kumon-mi this late to just...talk about stuff."
    r "You are...{i}so{/i} important to me, Sensei. So important."
    r "Like..."
    r "Yeah."
    r "{i}So{/i} important..."
    s "Well, thanks. But I’m pretty sure this conversation was supposed to be about Otoha and not me."

    if bonus == True:
        r "I’m still waiting on you to tell me how to not start groping her in the middle of casual conversation."
        s "I mean, that’s just kind of a common sense thing. Don’t grope {i}anyone{/i} in the middle of casual conversation."
    else:
        r "I'm still waiting on you to tell me how to not start hugging her in the middle of casual conversation."
        s "The best hugs are those not witnessed by entire groups of people. Keep that in mind."

    scene rinhappynight14
    with dissolve

    r "Got it! Next tip, please."

    if bonus == True:
        s "Masturbate frequently."
    else:
        s "Dance frequently."

    s "Like, before every time you two hang out."

    scene rinhappynight15
    with dissolve

    if bonus == True:
        r "Oh my god. Is {i}that{/i} why you never made a move on me? Because you were too busy making moves on yourself?"
        s "Some secrets are meant to stay hidden, Rin."
        r "I don’t know if I should be flattered, embarrassed, or grossed out."
        s "You should be listening to my advice, because I’m about to give you the most important piece of the puzzle you’re trying to solve."
        r "Okay, okay. I’m all ears. Hit me."
        r "Just not in the arm because it still hurts."
        s "The best way to hold yourself back is to just...do it."
        r "…"
        s "…"
        r "That’s it? That’s your super awesome, foolproof advice? Just don’t do it?"
        s "Simple, right?"
        r "So simple that it must be a joke."
        s "Rin, have you stopped to think that maybe the reason you’re having such a hard time holding back is because that’s {i}all{/i} you’re thinking about when you’re with Otoha?"
        s "Just enjoy your time finally being happy or whatever."
        s "And, it sounds very weird saying this, but stop thinking of sex so much."
    else:
        r "That helps?"
        s "Surprisingly, yes. Dancing gets the blood pumping and prevents you from making bad decisions."
        r "But every time I try to dance, I fall down and scrape my knee."
        r "And every time I'm around Otoha, I get this crazy urge to just dance anyway. Even when I know my knees will hate me for it."
        s "You must learn to control the dance."

    scene rinhappynight16
    with dissolve

    r "But she’s so hot! It’s hard!"

    if bonus == True:
        s "Well, the only alternative is just making {i}her{/i} want {i}you.{/i}"
        r "But I’m dorky and weird and awkward. And if I take my clothes off, she’ll see my arm."
        s "Then just...put yourself into risky situations. Sleep in the same bed. Lock yourselves in a room together. Shower in the same stall."
        s "There are a bunch of opportunities open to you as two girls in an all-girls[school]. We make literally no effort to separate you all."
    else:
        s "Do not give into the dark, Rin. You are better than that."

    scene rinhappynight17
    with dissolve

    if bonus == True:
        r "That was quite a few scenarios you managed to drum up off the top of your head, Sensei."
        s "I spend a lot of time thinking about lesbians."
        r "You sure you’re not just trying to spy on Otoha and me?"
        s "No. But if you happen to accidentally call me before the first time you two start experimenting on one another, I won’t mind."
        r "I don’t know if I like the idea of you listening to Otoha’s sexual moaning and stuff."
        r "Assuming of course that I’m actually able to make her feel anything and that I’m not the world’s worst bisexual."
        s "Just keep the phone closer to you then. Just one voice will do."
        r "Okay but what if I sound really weird? Like, not sexy at all. Just weird noises."
        s "…"
        s "I can always hang up?"
    else:
        r "I am?"
        s "Maybe? I don't really know. I'm just trying to give good advice."

    scene rinhappynight18
    with dissolve

    r "Solid plan. Thanks, homie."
    r "Will keep it in mind when I try and inevitably fail at making Otoha want to do stuff."

    play sound "texttone.wav"
    scene rinhappynight19
    with dissolve

    r "Oh! Speaking of which, that’s probably her."
    r "We send each other goodnight texts because we’re dating."
    r "Have I mentioned yet that Otoha and I are dating?"

    if bonus == True:
        s "I’ll consider it a real relationship the moment one of you two gets the other to orgasm."

        scene rinhappynight20
        with dissolve

        r "Like, physically? Because...you know..."
        r "If fantasies are involved and stuff, it’s prooooooobably safe to assume it’s already a real relationship based on that criteria."
        s "Obviously not counting that."
        r "You sure? Cause I’m not confirming anything, but it’s prooooooooobably happened more than once. By like...somewhere in the double digits."
        r "Or triple."
        r "She’s so hot."
        s "…"
        s "Just text her back, Rin."

    scene black
    with dissolve2

    if bonus == True:
        "Instead of just texting her, Rin decides to call Otoha and say goodnight."
        "They continue to chat for a few moments, and it ultimately leads to Rin admitting that she went out for a late night walk to “get her mind off of stuff.”"
        "Of course, she never admits that she met up with me. And I don’t blame her for that."
        "Otoha knows that Rin and I have kissed. And she doesn’t seem to have fully warmed up to me just yet in general...so keeping it secret is probably for the best."
        "The call ends shortly after and, without really exchanging any words about it, Rin and I appear to silently and mutually agree that it’s time to head back."
        "Along the way, we talk about a number of other things."
        "I don’t remember any of them."
        "I wound up, once again, getting too distracted by the dramatic contrast between her appearance and her actions."
        "When we make it back to the dorm, she tells me she loves me again."
        "I nod and head home."
    else:
        "Rin quickly goes back to doing that thing where she just repeatedly talks about dating Otoha and I have to escape into an alleyway because I drank too much water and had to pee."
        "I do it while she's looking away, so she doesn't realize I'm gone at first and I feel really bad about it afterwards."
        "But this is for the best and now my bladder is happy."

        r "Sensei? Where did you go? I have to tell you about my girlfriend."
        s "Oh no."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindate50 = True
    $ rinsad = False
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm55:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label callrinnight:
    if dormwar17 == False:
        "Rin doesn't know I have her number yet, so I probably shouldn't call her..."
        jump callnight
    if rinbetrayed == False and rindorm50special == True and rindate50 == False:
        jump rindate50
...
```