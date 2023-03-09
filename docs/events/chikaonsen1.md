# Little Miracles
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikaonsen1&go=Go)



## Event preconditions
❌onsenticket equal to True (unknown variable)

✅Event "[Yumi: Where the Sidewalk Ends](./streets30.md)" is completed (event=streets30)

✅Day of week is Saturday

✅chikanumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: chikaonsen1
* Group: Chika
* Triggered by label: callchikamorning
* Triggered by branch label: callmorning

## Event code
File: \game\ChikaEvents.rpy
Code:
```python
...
label chikaonsen1:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "Now that I know Yumi’s going to be watching Chinami, I feel a little less bad about stealing Chika away for a night."
    "And given how excited she was for the prospect of spending some time alone with me, I’m sure she’ll be ready to go as soon as I give the word."
    "In fact, she’d probably ditch work even if she was on the clock right now."
    "Not that I want her to do that or anything."
    "But...it would be kind of nice, I guess."
    "It’s a good feeling having so many lives that revolve around yours."

    play sound "phonebeep.wav"

    c "Hihi~ Good morning, Sensei."
    s "Morning. Are you busy today?"
    c "I’m actually off today! "
    s "Really? Don’t you work every weekend, though?"
    c "Yup! But I had a feeling that today was gonna be {i}that{/i} day, you know?"
    s "...Your period?"
    c "What? No. I meant the day you invite me out."

    "Thank God."

    c "So, are you ready to go?"

    "{i}Saying “Yes” will trigger a four part event that will last until Sunday morning.{/i}"
    "{i}Are you absolutely sure you’re ready to go?{/i}"

    menu:
        "Yes":
            play music "acoustic.mp3"

            s "Let’s do it. Start packing now."
            c "Heheh~ It’s only one night. It’s not like I need to bring all of my stuff."
            c "I’ll just grab my charger and some underwear and start heading over to your place. Is that okay?"
            s "You’re coming here?"
            c "Duh. Unless you want to stop by here. But that’s like, totally out of the way since there’s a bus stop right around the corner from your place."
            s "True. Alright, sure."
            s "Let me know when you’re here."
            c "Yup! See you soon, Sensei!"

            play sound "phonebeep.wav"

            "Chika hangs up and I take a seat on the bed, wondering what a one-night vacation with her will wind up being like."

            scene black
            with dissolve

            "………"
            "……"
            "…"

            jump onsenbegin

        "No":
            s "Actually...on second thought, maybe we should wait a little bit?"
            c "What? How come?"
            s "I’m pretty sure Ami and I already have plans tonight. "
            c "Ugh...stupid Ami."

            "Living with a [niece] shows off its convenience once again."

            c "Fine...but only because I like you so much."
            c "You’re lucky you have a girl like me, you know? Not many people would offer up a chance like this just to let you do whatever you want with it."
            s "Yeah, yeah. I’m glad that you exist."
            s "I’ve gotta go, though. Enjoy your day off, Chika."
            c "Guhhhh...Maybe someone will let me take one of their shifts or something now that I know I’m not busy?"

            play sound "phonebeep.wav"

            "The two of us hang up and I suddenly have to figure out something else to do today."

            $ renpy.end_replay()
            jump callmorning

label onsenbegin:
    scene wintersky
    with dissolve

    "Chika shows up around an hour later with only one bag."
    "I know she mentioned not needing much but, for some reason, I expected her to be the type to pack her entire closet away for even a short trip."
    "The two of us make our way to the bus station and decide to remain standing so as to not freeze ourselves against the cold steel of the bench."
    "She tells me a little more about the hot spring. How it’s not really a place someone like her could ever afford without little miracles like this."
    "The fact that she refers to it as a “miracle” is actually quite humbling."
    "I never thought of myself as the type to be involved in anything miraculous, let alone a miracle with a girl that is far too good for me by every stretch of the word."
    "I guess that applies to most of the girls I hang around, though."
    "But I probably shouldn’t be thinking of any of them right now."
    "If Chika’s going to be kind enough to use something like this on me instead of someone else she's close with, the least I can do is give her my undivided attention."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene firstonsen1
    with dissolve

    c "Soooo...you like?"

    "We arrive at the onsen half an hour later and receive yukata to change into."
    "I shrug mine off because I’m too stoic and manly to ever be seen in something like that, but Chika happily accepts hers and scurries off to a changing room to put it on right away."
    "And now...here we are."
    "In a completely unfamiliar environment, face to face with one another and-"

    s "You are adorable."

    scene firstonsen2
    with dissolve

    c "Heheh~ Thanks!"
    c "I haven’t worn one of these in ages. I’m surprised I even remembered how to put it on."

    if bonus == True:
        s "I hope it is equally as easy to take off."
    else:
        s "I am surprised as well. Your hippocampus must be very impressive."

    scene firstonsen3
    with dissolve

    c "[chikamaster]...we’ve only been here for five minutes and you’re already trying to rile me up?"

    if bonus == True:
        c "What if I wanted this to be a completely wholesome weekend without any of those {i}extra-curricular{/i} activities you’ve started having me do?"
        s "I’d say that you should probably put on normal clothes because it is hard to not get excited right now."
        c "Just don’t get {i}too{/i} excited or someone’s bound to notice."
    else:
        s "Of course not. I just want to hold your brain for a little while and see what it feels like."

    scene firstonsen4
    with dissolve

    c "Why aren’t you wearing yours, by the way? Isn’t that like, disrespectful or something?"
    s "I’ll be fine. I don’t think I’d look normal in one of those."
    c "Really? I think you’d look hot."
    s "Thanks. But I’ll stick to my normal clothes for-"

    scene firstonsen5
    with dissolve

    q "Get out of here, peasant!"
    q "This hot spring belongs to me!"
    q "Do yourselves a favor and run off before I call security!"
    c "But...we have tickets."
    s "You look a little [young]to be the owner of an onsen."

    scene firstonsen6
    with dissolve

    tk "Silence! I am Tsukasa Tsukioka of the Tsukioka family! A very powerful, 5000 year old wizard!"

    "Tsukioka? Why does that name sound familiar?"

    tk "I own many hot springs! Now, be gone!"
    s "Another wizard."
    c "Just like Chinami..."

    scene firstonsen7
    with dissolve

    q "Tsukasa, dear..."
    tk "Yes, mother?"
    tk "I was just informing this lovely [young]couple of the amenities this facility has to offer."
    q "Oh?"
    q "So I {i}didn’t{/i} just hear you talking about being a wizard again?"
    tk "Whatever do you mean, Mother? Why would I ever say something as silly as that?"

    scene firstonsen8
    with dissolve

    q "Hah...please forgive my daughter."
    q "It’s not often that she gets to converse with those outside of the manor, so she gets a little excited at times."
    c "Oh, yeah. It’s fine. I have a sister her age, so I kinda get what you mean."
    c "I’m Chika. Are you two actually the owners of this place? It’s absolutely beautiful so far."
    c "I mean...we still haven’t made it out of the entrance. But it was suuuuper nice on the outside."

    scene firstonsen9
    with dissolve

    q "Oh dear, pardon my manners."
    tb "I'm Tsubasa. And I assume you’ve already heard my family name from my daughter here."
    tb "We {i}do{/i} own this building, but we’re not here very often."
    tb "We just happen to be on a little retreat right now as my husband renovates our own hot spring."
    tb "I have another daughter who was supposed to be joining us, but it seems she had other matters to attend to this evening."
    tk "How disappointing Big Sister can be at times."
    tk "Does she not understand that a place like this is a truly splendid environment for mothers and daughters to bond?"

    scene firstonsen10
    with dissolve

    c "You love your mom a lot, huh?"
    tk "She is perfectly adequate. Though, I do wish she’d allow me a bit more freedom like Papa does."
    tb "And you are?"
    s "You can just call me Sensei."
    tb "Oh? You’re a teacher? Kumon-mi Academy or [kumon_mi_high]?"
    s "Uhh..."
    s "Chika, which one is ours again?"

    scene firstonsen11
    with dissolve

    c "[kumon_mi_high], Sensei."
    s "Sorry. The names are so similar that I wind up confusing them pretty frequently."
    tb "That’s hilarious. Do you enjoy teaching there?"
    tb "My oldest daughter attends Kumon-mi Academy, but I can’t say I’m exactly pleased with their...performance so far."
    s "Yeah. Crazy how they’d do something as outside of the curriculum as falling into a sinkhole."

    scene firstonsen12
    with dissolve

    tb "Hahahahah! Hilarious!"
    tb "I forgot how funny people could be outside of the manor!"
    tk "Mother? Papa told us not to laugh at commoners because it’s rude."

    scene firstonsen13
    with dissolve

    tb "I’m not laughing {i}at{/i} them, Tsukasa dear. I’m laughing because Sensei said something funny."
    tb "Now, come with me and leave these two alone. I’m sure they didn’t come all the way here to converse with a little girl and an old woman."
    s "You’re not old. You look the same age as me."

    scene firstonsen14
    with dissolve

    if bonus == True:
        tb "Apologies, again. I meant {i}older{/i} than your...tastes, given the lovely [young_girl] you’ve shown up with."
    else:
        tb "Why, how kind of you. I will be sure to remember that when my events are obtainable."

    tb "Now, please do excuse us."

    scene firstonsen15
    with dissolve

    tk "Bye bye, peasant man!"
    tk "Do enjoy your stay at Casa del Tsukasa!"
    tb "Good day to both of you."

    scene firstonsen16
    with dissolve

    "The two rich girls wander into what looks like a sauna and leave Chika and I to ourselves in the entryway again."

    c "That was...umm...interesting."
    c "Do you think she knows we’re like...here {i}together?{/i}"
    s "I’m fairly sure that much was obvious."
    s "I’m more surprised by how casual she was about everything."
    c "Heheh...maybe we just look {i}that{/i} good as a couple?"
    s "Yeah."
    s "I guess that must be it."

    scene black
    with dissolve

    "We turn around and begin to head toward the room we were assigned to."
    "The halls are lined with ornate lights that don’t quite match the overall Japanese theme of the place, but they definitely don’t look bad either."
    "And it seems that despite this being on the more “high class” side, there really aren’t many rooms."
    "Or people, for that matter."
    "It’s remarkably empty."
    "But I guess that just means it’ll be easier having some...”private time” in the hot spring."
    "………"
    "……"
    "…"

    scene firstonsen17
    with dissolve

    c "Woah! This place is like, totally retro!"
    c "I don’t even think there’s a TV in here!"
    s "I think the whole point of places like this is to relax and detach yourself from normal society or something."

    scene firstonsen18
    with dissolve

    c "And there’s only one futon~"
    c "It looks tiny, too. We’re probably gonna have to cuddle if we both want to fit."
    s "Oh no. What a horrible turn of events. However will we survive?"

    scene firstonsen19
    with dissolve

    c "Heheh~ I’m glad you’re just as excited as I am."
    c "This whole thing like, still hasn’t even set in for me I don’t think."
    c "Like, if I heard at the beginning of the[school] year that I’d be talking about cuddling my teacher at some high class onsen, I never would have believed it."
    s "I feel like that applies to pretty much everyone once they start [high_school]."
    s "We live in a sad world if people expect those things right away."
    c "You know what I mean."
    c "It’s just crazy how far we’ve come in such a short amount of time."
    c "Like, it doesn’t even feel like just one[school] year. You know?"
    s "Oh, I know very well."

    "Or at least better than you ever will, Chika."

    scene firstonsen20
    with dissolve

    c "Soooo...now what do we do?"
    s "Hell if I know. This is your trip."
    s "Not like there’s much {i}to{/i} do here other than like...relax or bathe."

    scene firstonsen21
    with dissolve

    c "Want to make out?"
    s "And that. That’s also a thing we can do."
    c "Is that a yes?"
    s "That’s obviously a yes."
    c "Then what are we waiting for? We’ve only got one night."
    c "We need to get as many kisses in as we possibly can, [chikamaster]~"

    scene black
    with dissolve

    "Chika grabs me by the wrist and pulls me into the bedroom."
    "She slides my blazer off and brings her hands to my chest, poking and pulling at the fabric of my shirt."

    scene firstonsen22
    with dissolve

    c "Actually, before we start, I wanna ask you something."
    c "And it’s important, so you’re not allowed to laugh at me."
    s "Can this really not wait until after we make out?"
    c "I don’t think you’ll want it to wait that long."
    s "Okay then. Color me intrigued."

    scene firstonsen23
    with dissolve

    c "Then..."

    if bonus == True:
        c "How do you feel about being my “first” tonight?"
        s "You were right. I’m glad you didn’t make me wait to hear that."
        c "You know what I’m talking about, right?"
        s "I sure hope so. If I don’t, this would be one hell of a tease."

        scene firstonsen24
        with dissolve

        c "It’s not a tease, [chikamaster]."
        c "I want to lose it tonight."
        c "This is the perfect place for a first time, isn’t it?"

        scene firstonsen25
        with dissolve

        c "I would have preferred you being in a yukata for it since I {i}do{/i} think that would be really hot..."
        c "But I wanna do it either way."
        s "Then why are we just standing here?"

        scene firstonsen26
        with dissolve

        c "Probs cause you haven’t kissed me yet."

        scene firstonsen27
        with dissolve

        "Chika presses her body against mine and immediately slides her tongue into my mouth."
        "Our hands find each other’s heads as we forcefully kiss, moving our waists closer together with every inhale and exhale."

        c "Mmn~"
        c "Mnch...mmm...hmm...[chikamaster]..."
        c "I’m so...mmnch...glad we can be...mmm...alone~"

        "I reach for her ass with my free hand and grab onto her, forcing her even closer to me."
        "She seems to like it as she bites my lip in response, moaning gently and running her fingers through my hair."

        c "[chikamaster]...[chikamaster]..."
        c "You want me...mmn...really bad...don’t you?..."

        "I bite her lip next to say yes since not everyone is as good at talking while kissing as Chika is."
        "And she must take that as a signal because-"

        scene firstonsen28
        with fade

        "She winds up pushing me to the ground and climbing on top of me just seconds later."

        c "Hah...hah...hah..."
        c "[chikamaster]..."
        c "Are you gonna make me feel good?"
        s "Hate to break it to you now of all times, but the first time probably won’t feel that great."
        c "You think you’re gonna hurt me?"
        s "I mean...yeah. Kind of."
        c "I don’t think so."
        c "I’ve got pretty high pain tolerance."
        c "And also-"
        c "I {i}really{/i}...fucking want it..."

        "I reach toward Chika’s chest to open her yukata-"

        scene firstonsen29
        with dissolve

        c "Nuh-uh-uh. Not yet, [chikamaster]."
        s "What? Why?"
        s "I am way too into this for any more foreplay right now."
        c "Who says I’m looking for any foreplay?"
        c "Maybe I just wanna watch you squirm a little bit?"
        c "Really make you work for it, you know?"
        s "Since when are you evil? You’re supposed to be the wholesome one."
        c "Hmm...maybe I just feel strong cause I’m on top right now?"
        c "Besides, I’m still totally wholesome. But there’s a time for that and that time is definitely not now."
        s "Okay, time to switch positions then."
        c "Positions or locations?"
        s "What does that even mean?"

        scene firstonsen30
        with dissolve

        c "Hmm...I think I wanna go check out the hot spring first."
        c "That is the purpose of an onsen, after all."
        c "And the bus was kinda hot on the way here, so a bath {i}does{/i} sound refreshing."
        s "Cool. Let’s go have sex in the bath."

        scene firstonsen31
        with dissolve

        c "No, no! That won’t do, [chikamaster]! The baths here aren’t co-ed."
        s "Excuse me?"
        c "But I’ll go by myself and I’ll try to be really quick, okay?"
        s "Why are you doing this to me?"

        scene firstonsen32
        with dissolve

        c "I'm sorry."
        c "I just need a few minutes to mentally prepare myself."
        c "Like yeah, I’m really fucking horny right now, but I didn’t think this was gonna happen like, {i}right away{/i}."
        s "You literally started this."

        scene firstonsen33
        with dissolve

        c "Sorry. But you were just so cute that I couldn’t help myself."
        c "I’ll be quick, okay?"
        s "Can you at least jerk me off or something first?"
        c "No way, Jose. You’ve gotta save everything up for me."
        c "And as a reward for your hard work and dedication, I’ll let you do it inside."
        s "Gee, thanks. Being blue-balled feels so much better now."

        scene firstonsen32
        with dissolve

        c "I’m really sorry...I am."
        c "But I’m not backing out."
        c "All I’m asking for is like...twenty minutes. Thirty tops."
        c "Why don’t you take a bath, too? Then we can have sex for a few hours and then take another bath and then go to sleep."
        c "Doesn’t that sound fun?"
        s "If you manage to go for a few hours without wanting to stop, I will be extremely impressed."
        c "Well, you know how much I like to impress you, so I’ll try my hardest to make that happen."

        scene firstonsen33
        with dissolve

        c "Sorry for killing your hard-on~"
        c "But think about me while I’m gone, kay?"

        scene black
        with dissolve2
        stop music fadeout 15.0

        "Chika hops off of me and happily skips out of the room, humming some upbeat pop song to herself as she goes."
        "I feel kind of betrayed for being left in this...condition."
        "But I get it."
        "This {i}is{/i} still a big moment for her after all."
        "She probably just wants to savor it."

        s "…"
        s "I guess a quick bath wouldn’t hurt..."

        "I lift myself off of the futon and make my way over to the apparent single-sex baths, wondering exactly how Chika is “preparing herself” right about now."

        $ renpy.end_replay()
        $ chikaonsen1 = True
        $ chika_love += 1

        "{i}Chika’s affection has increased to [chika_love]!{/i}"
        "………"
        "……"
        "…"

        "{i}Ten minutes later...{/i}"
    else:
        c "How do you feel about hugging me tonight?"

        scene black
        with dissolve2
        stop music fadeout 15.0

        s "Sure. That sounds like an enjoyable experience."

        "Chika hops off of me and happily skips out of the room, humming some upbeat pop song to herself as she goes."
        "I feel kind of betrayed for being left in this...condition."
        "But I get it. I also thing hugs are awesome."

        "I lift myself off of the futon and make my way over to the apparent single-sex baths, wondering exactly how Chika is “preparing herself” right about now."

        $ renpy.end_replay()
        $ chikaonsen1 = True
        $ chika_love += 1

        "{i}Chika’s affection has increased to [chika_love]!{/i}"
        "………"
        "……"
        "…"

        "{i}Ten minutes later...{/i}"

label chikaonsen2:
...
```

## Code that triggers this event
File: \game\ChikaEvents.rpy
Code:
```python
...
label callchikamorning:
    if onsenticket == True and streets30 == True and day == 6:
        jump chikaonsen1
...
```