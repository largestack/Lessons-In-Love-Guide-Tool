# Lifejacket
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm50special&go=Go)


Part of event chain [Transmogrification](./mollydorm25.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Rin: The Happiest Girl in the World](./rindate50.md)
* [Molly: Walkthrough](./mollydorm30.md)
* [Main: Girls in Spandex](./halloweentwo1.md)

## Event properties
* ID: rindorm50special
* Group: Rin
* Triggered by label: mollydorm25

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label rindorm50special:
    scene rinisstillfine1
    with dissolve2

    mo "Actually, Sir...On second thought, I don’t think this is a good idea anymore."
    mo "It sounded reasonable when we were in my room, but now that I’m in front of her door, I’m beginning to think that this isn’t exactly “staying away.”"
    s "Isn’t that the entire reason we came down here? Because staying away isn’t helping either of you?"
    mo "I don’t know...If what Haruka says is true, Rin has been doing pretty okay without me."
    mo "And it’s not like I’m doing anything self-destructive either. I’m just more...tired. Both physically and mentally."
    s "Molly, what happens in a game if you give up or fail a quest?"
    mo "You normally just get to try again later."
    s "See? You’ll never-"
    s "Wait, really? That’s not a harsh consequence at all."

    scene rinisstillfine2
    with dissolve

    mo "I know! Which is one of the many reasons I keep telling you that games are better than real life!"
    mo "If I fail this mission now, I might not be {i}able{/i} to try again! "
    s "But, on the other hand, if you succeed...you get your best friend and unrequited love back."

    scene rinisstillfine3
    with dissolve

    mo "Rejoice! Another chance to be unloved!"
    mo "Just kidding. The first part sounds rather nice."

    scene rinisstillfine1
    with dissolve

    mo "I just don’t think it’s going to go the way you imagine, Sir."

    if bonus == True:
        mo "For all we know, Rin could be in there unlocking event CGs with her new girlfriend right now. "
    else:
        mo "For all we know, Rin could be in there playing the trombone right now. She's been all about that life lately."

    s "Or, alternatively, she could be in there sleeping."
    mo "How is that any better?"

    if bonus == True:
        s "Would you rather her be fingering Otoha?"
    else:
        s "Would you rather her be playing the trombone?"

    scene rinisstillfine4
    with dissolve

    if bonus == True:
        mo "I’d rather her be fingering {i}me.{/i}"
    else:
        mo "I'd rather her be playing {i}my{/i} trombone."
        mo "I got it for Christmas last year and it's just been collecting dust this whole time."
        mo "If I had known she wanted one, I would have given her mine."

    s "There’s the Molly I know and...don’t love."
    mo "Thank you, Sir. Thank you for not loving me."
    s "Don’t take it personally. I don’t really love anyone."
    mo "This disclaimer should have been printed on the back of the cartridge before I plugged it into my system."
    s "There’s no way they’re still using cartridges for games in this day and age."
    mo "They’re not, Sir. I intentionally dated my analogy so you wouldn’t get confused by it."
    s "Appreciated. Now, are we doing this or not?"
    mo "…"
    s "…"
    s "Molly?"

    scene rinisstillfine5
    with dissolve
    play sound "knock.mp3"

    mo "Um...Rin? "
    mo "I’m sorry to bother you even though you told me to stay away...but I was wondering if...I could come in for a minute or two."
    s "…"
    mo "…"

    "A moment of silence goes by as Molly and I wait out in the hall. "
    "The rest of the girls are holed up inside of their rooms right now and are likely trying to go to sleep given the fact it’s-"

    s "Holy shit. Is it really midnight already?"
    s "Today went by way too quickly."

    scene rinisstillfine1
    with dissolve

    mo "I don’t think she’s in there, Sir. And...if she {i}is{/i}, she’s probably sleeping."
    s "Why not go in and check? That’s what I always do when I’m in doubt."
    mo "Why aren’t you understanding that me being intrusive is exactly what got me into this mess? I’m not going to fix that by...being intrusive in a slightly different way."
    s "You don’t know that, though."
    mo "I {i}do{/i} know that, though."
    s "Well, if you want to give up now, we can always-"

    scene rinisstillfine6
    with dissolve

    mo "Excellent idea, Sir. Let’s give up now and try again later."
    s "{i}Hah...{/i}"
    s "Well, it’s an anticlimactic end to the night. But if that’s really what you think is-"

    scene rinisstillfine7
    with dissolve
    stop music fadeout 3.0

    mo "Wait."
    mo "Listen."
    mo "I think I heard something."
    s "Heard what? It’s the middle of the night."

    scene rinisstillfine8
    with dissolve

    mo "...Which is also the perfect time to unlock event CGs."
    s "…"
    s "No way. She’s probably just talking in her sleep."
    mo "I’m scared, Sir."
    s "If you’re that scared, just leave. That’s what we were about to do anyway."
    mo "Yes, but...that was before we confirmed movement."
    mo "The event is already in progress. We can’t back out anymore."
    s "Is that really how it works?"
    mo "…"
    mo "I’m going in."
    s "How did we switch sides on this matter so quickly?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    mo "Rin?"
    mo "I’m coming-"
    mo "AHH!"

    play sound "static.mp3"
    scene contentwarning with flash
    scene everythingg7 with flash
    scene treefall1 with flash
    scene amibreak1 with flash
    scene rinisstillfine9 with flash
    stop sound
    play music "thingsthathurt.mp3"

    mo "What are you doing?!"
    r "Heeeeeeeeeeey."
    r "What’s up, you guys?"
    mo "Rin, what have you done?! I thought you stopped!"
    mo "You told me you stopped!"

    scene rinisstillfine10
    with dissolve

    r "Heheh..."
    r "Whoooooops..."
    r "Looks like I’m a liar..."
    mo "Rin..."
    r "Careful, Molly. Your hands are gonna get all messy."
    mo "I...I don’t..."
    s "When did you do this?"

    scene rinisstillfine11
    with dissolve

    r "Aaaaaay, Sensei’s here too. "
    s "Rin-"
    r "Just look. When do you think I did it, dude? Why’s that even matter?"
    mo "That’s...so much blood..."
    s "Why?"
    r "Felt like it."

    scene rinisstillfine12
    with dissolve

    mo "Are you okay? Well, I mean...obviously you’re not okay. But...are you feeling lightheaded? Are you dizzy?"
    r "Molly."
    r "Molly, Molly, Molly."
    r "Molly, Molly, Molly, Molly, Molly."
    mo "What? What is it?"
    r "You fucked up, girl."

    scene rinisstillfine13
    with dissolve

    mo "What?..."
    mo "This...isn’t because-"
    r "Oh, no. No no no. This isn’t your fault. It’s nobody’s."
    r "Just happens sometimes."
    r "Sorry. Hard to think when my body feels like it’s being packed into a ziplock bag."
    mo "Then...how did I mess up?"
    r "Cause you chose {i}me{/i}, idiot."
    r "Is this really what you want? "

    scene rinisstillfine14
    with dissolve

    s "Okay, you didn't have to say it like-"
    mo "What is that supposed to mean?"
    r "Just that you can do better. That’s all."
    mo "..."
    s "..."
    s "Did something happen to cause this?"

    scene rinisstillfine15
    with dissolve

    r "You know, that’s the craziest part."
    r "Everything’s fine. I’ve got no reason to be like this anymore."

    play sound "static.mp3"
    scene rinisstillfine16 with flash
    stop sound

    r "But I am!"
    r "I am like this!"
    r "It never ends, Sensei."
    r "The pain isn’t even pain anymore."
    r "It’s just...numb."
    r "I had everything. "
    r "I {i}have{/i} everything."
    r "Why can’t I just enjoy it? "
    s "…"
    mo "You realize doing this is just going to hurt everyone else, don’t you?"

    scene rinisstillfine17
    with dissolve

    r "Mhm."
    mo "And, for the record, I didn’t just {i}decide{/i} to like you one day. There was no {i}choice{/i} involved."

    scene rinisstillfine18
    with dissolve

    mo "So...So don’t tell me I messed up when I didn’t ask for any of this!"
    mo "I’ve liked you for so long! Those feelings aren’t a mistake!"
    r "I know."
    r "But you can do better."

    scene rinisstillfine19
    with dissolve

    mo "Why?..."
    mo "Why can’t you just let me make you feel better? "
    mo "Even now, when you need someone more than anything?"
    s "It’s not that simple, Molly."

    scene rinisstillfine20
    with dissolve

    mo "I know that!"
    mo "But even if she’s like this right now, it hurts to hear all of the pain {i}I’ve{/i} felt called some sort of...mistake!"
    mo "I just wanted to know if she was okay! I’m worried!"

    scene rinisstillfine21
    with dissolve

    mo "I’m...really worried..."
    r "Sorry, yo..."
    r "I..."
    r "I don’t know what I’m doing anymore..."
    s "Molly...can you run to the bathroom or...downstairs to see if you can find something to wrap her arm up with?"
    s "I’ll look after Rin while you’re gone."
    mo "I’m...so glad we didn’t just go back to my room..."
    mo "I don't know what I would have done if..."

    scene black
    with dissolve2

    mo "I’m just...so glad..."

    "………"
    "……"
    "…"

    scene rinisstillfine22
    with dissolve2

    s "Futaba?"
    f "{i}Sensei? You’re calling really late. Is something wrong?{/i}"
    s "Where are you right now?"
    f "{i}I’m at a diner with Nodoka. I know it’s late, but if you want to join us-{/i}"
    s "There’s a problem with Rin."
    s "Can you come back to the dorm?"
    f "{i}A problem with-{/i}"
    f "{i}Yes. I’ll leave right now.{/i}"
    f "{i}Please stay with her until I’m back.{/i}"
    s "Planned on it. Thanks."

    play sound "phonebeep.wav"
    scene rinisstillfine23
    with dissolve

    s "Futaba’s on the way."
    r "I heard. You keep your volume up so loud, man."
    s "Yes. Let’s talk more about the volume of my phone instead of the blood dripping down your arm."

    scene rinisstillfine24
    with dissolve

    r "You know...it’s so weird."
    r "I actually had a really good day today."
    r "Otoha came and visited me at work...and then we made plans to go to the movies this weekend. "
    r "She was even all cute and kissed me on the cheek before she left. "
    r "I mean, yeah...she looked both ways like five times to make sure nobody was watching first, but that didn’t really bother me."
    r "But then...this wound up happening."
    r "Why?"
    s "You don’t actually think I have an answer for that, do you?"

    scene rinisstillfine25
    with dissolve

    r "Guh. I got myself pretty good this time, didn’t I?"
    s "Should we call an ambulance or something? I don't really know what's {i}bad{/i} or...less bad when it comes to this."
    r "Mmmmmm...probably not. "
    r "I didn’t mean to go that deep. It was just a new boxcutter and-"
    s "I don’t care what it was. You shouldn’t have done this."
    r "Easier said than...not done, I guess."
    r "You think I like this, Sensei? "
    s "I didn’t say that..."

    scene rinisstillfine26
    with dissolve

    r "It was only a matter of time, you know. "
    r "These sorts of things come in waves."
    r "They pull you under and start drowning you before you even have the chance to buckle up your lifejacket."
    s "Except you’ve openly admitted to not wanting to wear a “lifejacket” in the past because of how it makes you feel."
    r "Heheh. Lifejacket means pills. I get it."
    s "It's not funny."
    r "Relax, Sensei...I haven’t drowned yet."
    s "“Yet” being the key word."

    scene rinisstillfine27
    with dissolve

    r "I’ve told you, haven’t I? "
    r "I don’t want to die...I don’t want to feel like this at all..."
    r "And yet, once or twice a week, I’ll feel this...blanket of everything I’m afraid of draped over me."
    r "It’s so heavy, Sensei. I can’t breathe when it’s on top of me."
    r "I can’t think or feel or...{i}anything.{/i}"
    r "I just can’t."
    r "In every sense of the word...I {i}can’t{/i}."
    r "There’s no other way I know how to describe it."
    s "I really don’t know what you want me to say here."

    scene rinisstillfine28
    with dissolve

    r "That’s fine. "
    r "It’s not like there’s anything I could hear that would just magically make me feel better anyway."
    r "Some people just aren’t allowed to be happy I guess."

    play sound "static.mp3"
    scene everythingg with flash
    scene rinisstillfine29 with flash
    stop sound

    r "Ngh! That stings."
    r "Try not to grip so hard, please."

    scene rinisstillfine30
    with dissolve

    s "I have to keep putting pressure on your wrist until Molly gets back with something to wrap you up with."
    r "You're gonna have to grab more than just that one spot, then. They're all over the place."
    s "This is where the important veins are. I think."
    r "Why did you bring Molly here anyway?..."
    s "Does that really matter right now?"
    r "We could probably talk about it some other time, but you squeezing me just now just made me aware of how much I’m bleeding and...I’m starting to get nauseous. "
    s "Well, you should have thought of that before you went and did something this stupid."

    scene rinisstillfine31
    with dissolve

    r "It’s not stupid..."
    r "It’s just a little...self-destructive."
    s "Sounds pretty stupid to me."
    r "It’s easy to look at what someone else does to try and feel better and write it off as dumb...but to me, this makes sense."
    r "It’s something I can control. Something I have power over when the rest of me is stripped away."
    s "I can’t say I’m a big fan of you justifying why it’s acceptable for you to bleed all over my hands as it’s happening."

    scene rinisstillfine32
    with dissolve

    if bonus == True:
        r "True. And it must {i}really{/i} suck since I didn’t even flash you to take your mind off of it all tonight."
        s "That wasn’t something I enjoyed, for the record. It was incredibly depressing."

    r "Yeah, well...if you’re gonna keep hanging around me while I’m like this, chances are you might get a little depressed every now and then."
    r "You’ve always got the option to walk away, you know. "
    r "Molly, too. "
    r "If I were her, I probably would have ran off the moment I said she fucked up."
    s "Molly’s actually been surprisingly mature about this whole situation. I’ve been with her all night."
    r "Bet that makes me look like a real immature son of a bitch then, huh?"
    s "I’m going to do my best to abstain from judging you right now, thanks. "
    r "You’re cute when you pretend to care."
    s "Don’t let Otoha hear that or there might be another breakdown like this in store for the near future."

    scene rinisstillfine33
    with dissolve

    r "Fuck! "
    r "Fuck fuck fuck! "
    r "What am I gonna tell Otoha?"
    s "Doesn’t she already know you have a history of...this?"
    r "Yes, but if she finds out that I started doing it again {i}right{/i} after we started dating, how do you think that’s going to make her feel?!"
    s "I imagine pretty shitty."

    scene rinisstillfine34
    with dissolve

    r "No. No no no no no no no no no. I have to hide it. She can’t know."
    r "If she knows then she’ll start worrying. If she worries too much, she’ll get exhausted. If she’s exhausted, she won’t want me anymore."
    r "I have to be wanted. I need her to want me. I can’t lose her now, Sensei. I can’t. I can’t. I can’t. I can’t."
    s "Calm down."
    s "You’re good at hiding this sort of thing, aren’t you?"
    r "That’s right. Yeah. I’m good at hiding this. She’s not going to find out."
    s "I mean, it would probably be best if you just dropped this habit altogether as well but, based on what you said earlier, I can’t foresee that happening any time soon."
    r "I’ll stop. I’ll stop for Otoha. Otoha doesn’t want me to do this. I’ll get better. I’ll be better."
    r "I won’t cut myself anymore. I’ll be happier. I’ll be the happiest girl in the world."
    r "I have everything I want. Why on earth would I be sad?"

    scene rinisstillfine35
    with dissolve

    r "Fuck! "
    r "Why can’t I fucking feel anything?!"
    r "I’m supposed to be better now!"

    scene rinisstillfine36
    with dissolve

    r "I’m...supposed to.."
    r "Be better now..."
    s "…"
    r "…"

    scene rinisstillfine37
    with dissolve

    r "Sensei..."
    r "Why can’t I feel anything?..."

    scene black
    with dissolve2

    "Molly shows up a few minutes later with some gauze she bought from a nearby convenience store."
    "Apparently, she couldn’t find any in the bathroom or her room, so she frantically took off down the road without checking the lobby for any medical supplies."
    "Either way, by the time she gets back, the bleeding has mostly stopped."
    "I wrap up Rin’s arm the best I can but it is admittedly not great."
    "Once Futaba gets back, though, she redoes it herself."
    "It looks like she’s had practice."
    "…"
    "What a terrible thing to become experienced at."

    $ renpy.end_replay()
    $ rindorm50special = True
    $ rin_love += 1
    $ rinsad = True
    stop music fadeout 7.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "{i}At least she can feel that.{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

                    ###############################################
                    ################## ROOM 5 #####################
                    ###############################################

label amidorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ami_love >= 5 and amidorm5 == False and day == 1 or day == 5:
                play sound "knock.mp3"

                s "Hey, Ami. Are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            if ami_love >= 5 and day != 1 and day != 5 and amidorm5 == False:
                jump amidorm5
            if ami_love >= 10 and day > 5 and day60 == True and amidorm5 == True and amidorm10 == False and day24 == True and amisroom10 == True:
                jump amidorm10
            if ami_love >= 15 and amidorm10 == True and mayadorm5 == True and amidorm15 == False:
                jump amidorm15
            if ami_love >= 20 and day != 1 and day != 5 and amisroom20 == True and amidorm20 == False:
                jump amidorm20
            if ami_love >= 25 and amidorm20 == True and day != 5 and amidorm25 == False:
                jump amidorm25
            if ami_love >= 40 and amidate35 == True and amidorm40miss == False and shrine35 == True and day != 1 and amidorm40 == False:
                jump amidorm40
            else:
                jump amidormgen
        "Finger Your [niece]" if amifingered == True and bonus == True:
            jump amifingerreplay
        "Have Sex (Missionary)" if ami_virgin == False and bonus == True:
            jump amimissionaryanim

label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
        if maya_love >= 10 and day != 1 and day != 5 and mayadorm5 == True and mayadorm10 == False:
            jump mayadorm10
        if maya_love >= 15 and shrine15 == True and mayadorm15 == False:
            jump mayadorm15
        if maya_love >= 20 and shrine20 == True and yumidorm10 == True and mayadorm20 == False:
            jump mayadorm20
        if maya_love >= 25 and shrine25 == True and mayadorm25 == False:
            jump mayadorm25
        if maya_love >= 30 and mayadorm25 == True and norikoinvite2 == True and mayadorm30 == False:
            jump mayadorm30
        if maya_love >= 35 and mayadorm30 == True and day > 5 and nikidate5 == True and mayadorm35 == False:
            jump mayadorm35
        if mayadorm5 == True and mayadorm10 == True:
            jump mayadormgen
        else:
            play sound "knock.mp3"

            s "Hey, Maya. Are you in there?"
            "..."
            "There's no answer."
            jump doorknock

label amidormgen:
    play sound "knock.mp3"

    s "Hey, Ami. Are you in there?"
    a "Mhm! Come in, Sensei!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

    scene amidormgen
    with dissolve

    "Ami lets me in and the two of us hang out in her room for a few hours."
    "She coerces me into watching some girly anime with her and gets mad whenever I ask a question."

    if day < 4:
        "After a while, she tells me that she has plans with Maya tonight and that we can't hang out for much longer."
        "Despite that, we wind up watching a few more episodes until Ami's phone blows up with 'Where are you?' texts."

        scene black
        with dissolve

        "Being the exceptional legal guardian I am, I walk her to the park to meet up with Maya and company and begin a very boring trek home..."

        $ ami_love += 1
        stop music fadeout 3.0

        "{i}Ami's affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    else:
        "After a while, the two of us begin to get hungry and decide that we should probably continue this at home."
        "Since Ami isn't staying at the dorm tonight, we walk back together and stop at a convenience store along the way."
        "I get talked into buying her a disgusting amount of candy and, before I know it, we are skipping dinner and eating junk food."

        scene black
        with dissolve

        "But hey...At least I got to spend some quality time with my [niece]."
        "I can't ask for much more than that..."

        $ ami_love += 1
        stop music fadeout 3.0

        "{i}Ami's affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mayadormgen:
    play sound "knock.mp3"
    s "Hey, Maya. Are you around right now?"
    m "Why are you here? Please leave."
    s "What's that? You want me to come in?"

    scene black
    with dissolve
    play sound "dooropen.mp3"
    "..."

    scene mayadormgen
    with dissolve

    m "Why do you do things like this?"

    "Maya begrudgingly hangs out in her room with me as she 'doesn't have enough energy to leave.'"
    "Of course, she spends most of this time either ignoring me or trying to educate me about the universe."
    "I'm unable to follow any of it, but I'm at least glad that she isn't calling the police."
    "It has become a personal goal to have Maya accept me, and I feel like moments like this will get us there one step at a time..."

    scene black
    with dissolve

    "...But as soon as I finish thinking that, she kicks me out of the room and I am forced to walk back home alone..."

    $ maya_love += 1
    stop music fadeout 3.0

    "{i}Maya's affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amidorm5:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
mo "That “maybe” causes me a great deal of worry, Sir."
    s "Well, if you’re {i}that{/i} worried...just go talk to her."
    mo "I don’t know...the last time I took someone’s advice about this, I was either duped or...I greatly misunderstood that person."
    mo "The great downfall occurred just shortly after that, when I had already chosen the path I was going to walk."

    scene mollydormchanging23
    with dissolve

    mo "But...as the gears screeched to a halt and all of the cogs in this machine called “life”  stopped spinning, I knew something needed to be done."
    mo "If only I had known that “something” was the opposite of what the voice inside of my head commanded of me."
    s "…"
    mo "…"
    s "So, are you going to talk to her or not?"

    scene mollydormchanging24
    with dissolve

    mo "What, like...right now?"
    s "Sure. Rin stays up late, doesn’t she?"
    s "And if there’s anything I’ve learned about serious situations in the dorms, it’s that a person’s roommate is almost always conveniently missing exactly when they need to be."
    mo "You know, Sir...Now that you mention it, I do remember Futaba mentioning something about going to the bookstore with Nodoka tonight."
    s "See what I mean? Now is as good a time as any."

    scene mollydormchanging25
    with dissolve

    mo "I don’t know..."
    mo "Rin said she wanted to take a break from speaking for a while."
    mo "And...and what if Otoha is there?"
    s "At this hour? Her mother would never allow that."
    mo "…"
    s "…"

    "Molly takes a moment to think about what her next move is going to be."
    "I’m sure it's hard deliberation considering her only options are “keep indefinitely being sad” or “risk becoming more sad in order to be less sad right now,” but...those are kind of the only options we ever have."
    "And even if time does have a way of mysteriously healing things, it doesn’t mean it’s exciting to just sit back and let that happen."
    "The most ideal scenario right now would be for Molly and Rin to {i}both{/i} be happy."
    "And if I have to put someone else’s well-being at stake in order to risk that, so be it."

    mo "Will you...come with me?"
    s "Me? Why?"
    mo "Moral support, I suppose."
    mo "Our party hasn’t disbanded yet, so...just think of it as another side quest."
    s "…"

    if bonus == True:
        s "Fine. But the reward for this better be more than just a picture of my students wearing clothes, skin tight or not."
    else:
        s "Fine. But you owe me a soda."

    scene mollydormchanging26
    with dissolve

    mo "Understood, Sir. And thank you."
    mo "But...I still don’t know what I should say."
    s "When in doubt, just be honest. "
    s "That’s what I always do and it only backfires like...less than half of the time."
    mo "...Slightly less than half? Or significantly less than half? Because I do not feel good about those odds if it is the former."
    s "Doesn’t matter. You’ve already decided and I’m going to be there with you every step of the way."
    s "Unless you or Rin asks me to leave. "
    s "If that happens, I imagine I’ll put up a fight for a little while but ultimately just go anyway."
    mo "…"
    s "…"

    scene mollydormchanging23
    with dissolve

    mo "{i}Hah...{/i}"
    mo "Good thing we stopped at that leyline earlier. Otherwise, there is no way I’d allow you to talk me into this."
    s "Sure you would. You just needed an excuse to do something you already wanted to do, and telling you this is just one more example of my brutal honesty making things better."
    mo "That didn’t make anything better at all..."

    scene black
    with dissolve2

    "Molly decides to keep her pajamas on for the trip back downstairs- probably because it would look weird to get dressed up for a second round of rejection."
    "Or, in the best case scenario- the {i}first{/i} case of her and Rin trying to make things work."
    "We just have to hope at this point that Rin is still awake."
    "But given how excited she still seems to have a girlfriend, I imagine it’s possible she hasn’t slept at all since the beach."
    "But hey, that puts her back into the same category as Molly, even if the two of them have already begun to drift apart."
    "Maybe this small similarity, albeit the result of opposite extremes, is all they’ll need in order to get closer again."

    play sound "dooropen.mp3"

    s "…"

    "Or maybe it will end things once and for all."
    "You can’t ever really know until it’s too late, can you?"

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollydorm25 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    jump rindorm50special
...
```