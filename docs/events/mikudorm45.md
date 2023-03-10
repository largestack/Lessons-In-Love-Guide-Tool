# Acute Love Triangle (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 45

* Event [Glued to the Sky](./christmastwo20.md) (Main) is completed)

* Day of week is not Thursday



## Next events

None

## Event properties

* Id: mikudorm45
* Group: Miku
* Triggered by label: mikudorm
* Triggered by branch label: mikudorm
* Triggered by path: mikudorm->mikudorm45

## Official wiki page

[Acute Love Triangle](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm45&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label mikudorm45:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Miku’s door and wait for her to answer."
    "It’s the first instance of me coming here to spend time with her since the Christmas party, and while I {i}should{/i} be of the mindset that maybe things might {i}go somewhere{/i} this time-"
    "I can’t help but worry that Makoto might somehow get involved again."

    if bonus == True:
        "I was able to miraculously survive one topless Miku run-in with her (Albeit with a surprisingly painful slap) but I really don’t know if I’d be able to emerge from a second alive."
        "Considering that I haven’t heard anything from Makoto yet, though, I doubt that Miku has told her anything."
        "Which is good, because I have no idea how I’d react if I were to be suddenly confronted by the two of them at once regarding our respective relationships."
    else:
        "Every time Makoto is involved in anything, my tummy starts hurting."

    s "..."

    "Oh no."

    if bonus == False:
        "It is happening again."

    mi "Ah! One more second, Sensei! I’m...not done gettin' ready yet!"
    s "What exactly are you getting ready {i}for{/i}, Miku?"
    mi "I...can’t tell you that!"
    s "Well, that’s not suspicious at all."
    mi "Just...give me another minute! I made a mistake!"
    s "What kind of mistake would-"
    mi "Just give me a friggin’ minute, okay?! Jeez!"
    s "..."

    "You know, maybe I should just quietly back out of the hall and go find something else to do?"
    "This is likely one of those times where my inner monologue mysteriously predicts what is going to happen next, and I’m not really in the mood for a confrontation right now."
    "Or...ever, for that matter."
    "Let alone one that potentially involves someone as good at slapping as Makoto."

    mi "Okay! You can come in now, Sensei!"
    s "Before I do, can you confirm whether or not Makoto is in there?"
    mi "Makoto? No, she’s at work right now."

    "Oh."
    "I guess...Miku wasn’t getting ready for an intervention then?"
    "What else would she be getting ready for, though?"

    play sound "dooropen.mp3"
    scene black
    with dissolve

    "I open the door to greet Miku and-"

    scene intervention1
    with dissolve2

    mi "Why don’t you take a seat, Sensei?"
    s "You know, I was really hoping I wouldn’t ever have to hear those words."
    mi "Also, Makoto is here after all. Surprise."
    s "You fucking liar."
    mak "We’re here precisely because Miku {i}isn’t{/i} a liar, Sensei."
    mak "Or rather- that she’d prefer to not keep things hidden from her best friend, despite how desperately you may want her to."
    s "Why is it okay to lie to me and not to you? That doesn’t seem fair at all."

    scene intervention2
    with dissolve

    mak "Oh, fantastic! Since we’re now on topic of what constitutes “fair,” how about you-"
    mi "{i}Ahem.{/i}"
    mi "I believe I told Sensei to take a seat, Makoto. ‘Yer gonna ruin the innervention."

    scene intervention3
    with dissolve

    mak "Ugh. Fine. Sensei, please sit down so we can proceed with this {i}intervention.{/i}"
    s "I really don’t want to."
    mi "You’ve gotta, Sensei. You’ve got two ladies wrapped around ‘yer finger and the time’s come to untangle ‘em."
    mak "There are a lot more than just two, Miku. Frankly, there are so many at this point that I doubt Sensei will ever be able to untangle all of them."
    s "Yeah, thanks for the reminder."

    scene black
    with dissolve

    "I take a seat in a third chair that Miku and Makoto set up on the side of the room and wonder why they went to the trouble of doing that instead of just letting me sit on the couch."
    "But I guess comfort is probably the least of their concerns right now, when-"

    mak "Oh, no. Don’t go getting lost in thought right now, Sensei..."

    scene intervention4
    with dissolve

    s "I should have just stayed at home."
    mi "This was gonna happen whether ya liked it or not, Sensei. It’s the only way we can settle matters once and for all."
    s "Fine. Then I pick Makoto since at least she doesn’t lie to me. Meeting adjourned."

    scene intervention5
    with dissolve

    if day > 5:
        mak "Excellent. See you in school on Monday, Sensei."
    else:
        mak "Excellent. See you in school tomorrow, Sensei."

    mi "Wait, no! The choice ain’t supposed to be as easy as that! In fact, there ain’t supposed to be a choice at all! Neither one of us expects ya to just-"
    mak "Sensei’s clearly made his decision already, Miku. I believe the only thing left for us to do is accept it."

    scene intervention6
    with dissolve

    mi "Well...yeah. I guess that would be the easiest thing to do. Definitely a heck of a lot easier for me. But I kinda figured we were gonna at least talk about it a little."
    mi "I ain’t ever liked somebody before, and I don’t want all these weird feelings cloggin’ up my brain when it’s already givin’ Usain Bolt a run for his money."
    mak "I know, I know. I was only being half serious. I’m just...not sure how to do this, though. Organizing an intervention for a love triangle is not exactly “normal.”"
    s "You know an organized meeting is bad when even Makoto isn’t into it."

    scene intervention7
    with dissolve

    mi "I’m doin’ my best, okay?! "
    mak "Let’s just...let Miku take charge of this. She’s proven to be quite effective at making the first move as of late."

    scene intervention8
    with dissolve

    s "You seem less mad at me than I expected you to be."
    mak "Oh, don’t get me wrong. I {i}want{/i} to be angrier with you. I just know that, in this case, Miku was the one who pounced on you."
    mak "All you did was buy her a present she really liked."
    mak "Granted, I’m sure there was much more that happened beforehand that ultimately {i}culminated{/i} in this all happening, but the fault isn’t yours alone."
    mak "Miku’s obviously had feelings for you for quite some time. {i}Obviously{/i} not as long as I have, but it’s not as if we can ignore those feelings when they’re just as real as anyone else’s."
    s "So much for letting Miku take charge of the meeting."

    scene intervention9
    with dissolve

    mak "I can’t believe you kissed her before me!"
    mi "Didn’t ya just admit {i}I{/i} was the one who kissed {i}him,{/i} Makoto? "
    mak "Yes, but still! "
    s "Do you want me to kiss you right now and even the playing field?"

    scene intervention10
    with dissolve

    mak "Yes, actually. I would very much appreciate that."
    mi "Wait, wait, wait! Hold on a sec! Nobody’s kissin’ anyone!"
    mak "Maybe not right now. But who knows what the fuck you two would do if I were to leave the room."
    mi "Just cause I kinda attacked Sensei doesn’t mean I think I’m at the front of the race or anythin’ like that! "
    mi "I just didn’t want us keepin’ secrets from each other anymore! ‘Specially if I’ve got the green light to go ahead and try and make sense of all these butterflies!"
    s "Green light? What are you talking about? "

    scene intervention11
    with dissolve

    mak "Did you really think I was going to stop Miku from following her heart just because it’s trailing my own?"
    mak "I’ll admit that I was hoping things would never come to this but, now that they have, what else are we supposed to do other than simply deal with them?"
    mak "Frankly, I’m {i}more{/i} comfortable with the idea of you romantically pursuing Miku than any of the other girls."
    mak "Not that I’d ever expect you to romantically pursue {i}anyone{/i} when romance is the furthest thing from your mind...but still."
    s "So what, then? I’m free to just mess around with both of you? Because if that’s the case, this meeting could have been solved with a single text message."

    scene intervention12
    with dissolve

    mi "Sensei...you know we’re not just tryin’ to “mess around,” right? Me and Makoto actually {i}like{/i} like you."
    mak "Makoto and I."
    s "What am I supposed to do about that, though?"
    mi "I don’t know...maybe just...{i}consider{/i} it when we’re all doin’ stuff together?"
    mi "The whole reason I wanted to do somethin’ like this is so we wouldn’t hurt each other’s feelings in the long run."
    mi "Both of you guys are crazy important to me, and I don’t wanna risk hidin’ anything if I think it could make stuff worse."

    "That’s a surprisingly mature outlook from one of the least mature girls I know."
    "But it’s...respectable in its own twisted sort of way."
    "How much exactly does Miku intend to share, though? Because there’s certainly one thing I can think of that I can’t really imagine Makoto just brushing off."

    s "I just feel like this is more of a thing for the two of you rather than me."
    s "If I’m not being forced to pick between you, I can’t imagine this meeting making any sort of impact on things to come."

    scene intervention13
    with dissolve

    mi "It {i}is{/i} mostly for just me and Makoto-"
    mak "Makoto and me, in this case."
    mi "But you {i}are{/i} Makoto. "
    mak "..."
    mi "Oh, I get it."
    mi "But yeah. It is mostly for us two, I guess. I just think that if everybody’s gonna be involved in this weird triangle thingy...that we should all know about it."
    mi "And that even if none of us are tryin’ to hold the other ones back...that we’re okay with whatever happens."
    s "Are you really {i}okay{/i} with whatever happens, though, Miku?"

    scene intervention14
    with dissolve

    mi "Whaddya mean?..."
    mi "Like if you decide to just go full-Makoto and ignore how I feel? Course I wouldn’t be {i}okay{/i} with it...so maybe that ain’t the best word."
    mi "I’d understand, though. "
    mi "I don’t really know how you make decisions and stuff, Sensei, but if I were in your shoes, I’d be tryin’ to hurt the least amount’a people possible."
    mi "One of us is obviously gonna get hurt. Maybe even all three. But I feel like just knowin’ that is enough to make it all hurt a little less."
    s "..."
    mak "..."
    mak "I want to give you a hug, but I hardly think this is the right time."

    scene intervention15
    with dissolve

    mi "Huggin’ your rival’s just as good as admitting defeat! We can hug when all of this is said and done."
    mak "{i}If{/i} things are ever said and done. Sensei here is so helpless when it comes to making decisions that, more often than not, I find myself making them for him."
    s "Can you do me a favor and decide that this meeting is over, then? Because if nobody has any questions-"

    scene intervention16
    with dissolve

    mi "Oh, I’ve got a question. How come ya ain’t kissed my roommate yet? "
    mak "I don’t like the bluntness with which that question was asked, but I definitely {i}would{/i} like to know the answer to that as well."
    s "Just hasn’t come up yet."
    mi "But, like..."

    scene intervention17
    with dissolve

    if bonus == True:
        mi "Ain’t you two already doin’ more...adult stuff?"
    else:
        mi "Ain’t you two already in the secret hug club?"

    mak "..."
    s "You know, I kind of assumed that when you said you two share everything that you didn’t literally mean {i}everything.{/i}"
    mi "Isn’t...goin’ straight to the major stuff like that kinda like cheating?"
    mak "Is this something we really have to discuss right now?"
    mi "Does it have somethin’ to do with how Makoto’s always surrounded by those videos? You like...doin’ her a favor to prevent her from goin’ crazy or somethin’?"

    scene intervention18
    with dissolve

    mak "Obviously n-"
    s "Yes."

    scene intervention19
    with dissolve

    mak "That is absolutely {i}not{/i} why we have been doing those things!"
    s "So if you ever find yourself going crazy as well, Miku-"

    scene intervention20
    with dissolve

    mak "Don’t listen to him. This is how he traps you into a relationship where he doesn’t {i}have{/i} to kiss you because you’ve already skipped that step. "
    mak "Run while you still can. Don’t turn into another me."
    mi "Two Makotos does sound like a little too much now that ya mention it..."
    mi "Why don’t ya just kiss him yourself, though? It ain’t that hard. Ya just kinda...go for it."
    s "Yeah, Makoto. This is all your fault and you should try and be more like Miku."

    scene intervention21
    with dissolve

    mak "Maybe {i}you{/i} should try and be more like Miku! I have done more than enough for you and deserve a reward every once in a while!"
    mi "She {i}does{/i} deserve it, Sensei. "
    s "Correct me if I’m wrong, but...aren’t you supposed to be rooting for yourself right now? "
    s "I figured the whole “Team Makoto” thing would be over with after today and that you’d try a little harder to keep me to yourself."

    scene intervention22
    with dissolve

    mi "Why would I try and keep ya to myself when Makoto likes you too? That ain’t fair at all."
    mi "I don’t see any reason why I can’t stay on Team Makoto {i}and{/i} like you. There some kinda rule against that?"
    mak "I mean...I don’t think there’s a {i}rulebook{/i} we can consult...but that’s not normally how love triangles go..."

    scene intervention23
    with dissolve

    mi "Well, maybe it ain’t really a triangle then?"
    mi "Aren’t you kinda rootin’ for me too, Makoto?"
    mak "Uhh..."
    mak "Not really?"
    mak "I obviously don’t want to hold you back from pursuing the person you admire, but if you’re asking if I’m hoping you and Sensei get closer...absolutely not."
    mi "Oh. "
    mi "Huh."

    scene intervention24
    with dissolve

    mi "Guess I’m the weird one, then."
    s "No surprise there."
    mak "Do {i}you{/i} have any questions, Sensei?"
    s "Just one. Was this really necessary?"
    mak "Probably not. But I’m sure it made Miku feel a little more comfortable and, strangely enough, I think I feel that way as well."
    s "Well, I don’t. This was weird and I’d prefer that we don’t ever do anything like this again in the future."
    mak "If you honestly think you’ll be able to avoid a similar conflict in the future, you’re out of your mind."
    mak "It’s only a matter of time until you’re having this exact conversation with every pair of friends who fall hopelessly in love or...{i}like{/i} with you."
    mak "All things considered, I think Miku and me handled this extremely well."
    s "Miku and I."
    mak "..."
    s "..."

    scene intervention25
    with dissolve

    mak "I changed my mind. You can have him."

    scene black
    with dissolve2

    "The intervention comes to a close as Makoto needs to start getting ready for work."
    "It definitely feels a little later than normal for her to start heading over there, so I initially dismiss it as an excuse to give Miku and me some time alone. "
    "But that notion is immediately quelled when Makoto says this."

    if bonus == True:
        mak "Oh, and you two are going to be walking there with me. I refuse to leave this room knowing that her shirt would immediately come off as soon as the door closes."
        mi "That happened one time! "
        mi "I do kinda wanna walk, though. So I’ll come."
        mak "And you, Sensei?"
        s "..."
        s "Ugh, fine."
    else:
        mak "Yahtzee!"
        s "Congratulations, Makoto."

    scene intervention26
    with dissolve

    mak "Oh, for fuck’s sake! Who keeps turning the number on our door upside down?! It’s getting very tiring!"
    mi "Do you really think it’s weird that I wanna be on Team Makoto {i}and{/i} Team Miku? Cause I just don’t really get why."
    s "That’s something you’ll have to talk to Makoto about. I’m perfectly fine with it."
    s "I do stand to benefit the most, though, so I’m probably biased."

    scene intervention27
    with dissolve

    mak "Why are we talking about that again?! The intervention is over and it’s time to return to reality!"
    mi "Oh, and sorry for lyin’ about Makoto not bein’ around. I figured ya would’ve ran if I told ya she was with me."
    s "It’s whatever. That honestly went a lot better than I was expecting. "
    mi "Yeah, nobody cried at all. And Makoto only got a tiny bit flustered when I brought up her {i}relationship{/i} with “little” Sensei."

    if bonus == True:
        s "Please don’t call it that, Miku."
        mak "Please don’t talk about that at all! And {i}definitely{/i} not in the halls!"
    else:
        s "Who told you about my miniature clone? That was supposed to be a secret."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ mikudorm45 = True
    $ makoto_love += 1
    $ miku_love += 1
    stop music fadeout 8.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump mikudorm45p2

label mikudorm45p2:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if miku_love >= 5 and firsttimesoccerfield == True and mikudorm5 == False:
                jump mikudorm5
            if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
                jump mikudorm10
            if miku_love >= 15 and mikudorm10 == True and mikudorm15 == False:
                jump mikudorm15
            if miku_love >= 25 and soccer25 == True and mikudorm25 == False:
                jump mikudorm25
            if miku_love >= 30 and soccer30 == True and day != 4 and trinity3track == True and mikudorm30 == False:
                jump mikudorm30
            if miku_love >= 35 and makotowinterbeach4 == True and day != 4 and mikudorm35 == False:
                jump mikudorm35
            if miku_love >= 35 and mikudorm35 == True and day != 4 and mikudorm40 == False:
                jump mikudorm40
            if miku_love >= 45 and christmastwo20 == True and day != 4 and mikudorm45 == False:
                jump mikudorm45
...
```