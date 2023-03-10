# The Art of Never Knowing (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Debatably Bisexual Musicians](./cafe45.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Main: Annabel Lee](./day280.md)

## Event properties

* Id: rindorm45
* Group: Rin
* Triggered by label: cafe45
* Chain sources: cafe45
* Chain sources path: cafe45

## Official wiki page

[The Art of Never Knowing](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm45&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm45:
    play sound "dooropen.mp3"

    r "I’m home!"

    "Rin throws the door open and calls out to absolutely no one."
    "She doesn’t step aside to let me in or make any other sort of polite gesture, just treats it like it’s any other day because-"
    "Well, it {i}is{/i} any other day. "
    "Every day is just another day and there is no single day any better or worse than the next."
    "They will all blend together- and we will all {i}fall{/i} together."
    "Or will we?"

    scene rindormfortyfive1
    with dissolve2
    play music "kimitoakinobouken.mp3"

    r "Baaaaah...I’m beat."
    r "Who would have thought walking six million miles would take that much out of you?"
    s "Everyone. Everyone would think that."

    scene rindormfortyfive2
    with dissolve

    r "Rhetorical question, good sir. I obviously know how legs work. I’m on them all day every day."
    r "Except for when I’m kicking your ass at video games and {i}railing the shit out of you.{/i}"
    s "You really like that euphemism, don’t you?"
    r "Oh, hell yeah. One of the several cool things about you coming instead of Otoha today was that I didn’t have to prevent myself from saying weird stuff like that."
    r "Otoha’s cool but even she’d probably be like, “Woah, chill” if I came out and talked about railing her all of a sudden."
    s "Speaking of which, how are things going with her? I noticed you pulling out your phone pretty frequently on the ride back."

    scene rindormfortyfive3
    with dissolve

    r "Uhh...hard to tell. I don’t think she has her phone back."
    r "Only reason I kept pulling it out was to check if she’s alive again yet."
    s "Not having a phone does not equate to being dead, you know."

    scene rindormfortyfive4
    with dissolve

    r "Try saying that to literally any [teenage]girl with a crush and see what they say, Sensei."
    r "Guarantee you that they’ll all say it’s basically the same thing."
    s "I can’t imagine there being anything that could be taken away from me that would make me-"
    r "Imagine all of the girls in your life were suddenly replaced with boys."
    s "Oh. Yeah, you clearly know me better than I know myself. That sounds horrible."

    scene rindormfortyfive5
    with dissolve

    r "Course I do. I see you almost as much as I see Futaba now."
    r "Like, I’m sure you could see plenty of things about me that I can’t see even if I try."
    r "Like how awkward I apparently am when it comes to talking to cute girls."
    r "You should give me some pointers one day. Maybe even become my wingman."
    s "I don’t think I’d be a very good wingman."
    r "Why? Cause everyone magically falls for you without you even doing anything?"
    s "Not {i}everyone{/i}. "
    s "There’s one girl I know who had the audacity to call me a backup date today. What’s up with that?"

    if rinbetrayed == True:
        r "Are you forgetting that you fingered my first major crush?"
        r "Sorry for not prioritizing you, all things considered."
        s "Apology accepted."
        r "Unreal."
    else:
        r "Hey, I’ve been with you all day. I know exactly who you’re talking about."
        r "If it’s any consolation, you were the best backup I’ve ever had."
        r "To be fair, though, I can count every date I’ve ever had on one hand."

    r "But yeah-"
    r "I think it’s safe to say that, if nothing else, you’ve earned yourself a special place in the memories I will one day share with my adopted children."
    s "Adopted?"
    s "So you don’t see yourself ever starting a family with a male?"
    r "I never said that."
    r "Who knows? Maybe a few years from now I’ll start prioritizing men over women and everything will change."
    r "You can still adopt when you’re in a heterosexual relationship, Sensei. There's no rule against that."
    r "I'm probably not one to talk since both of {i}my{/i} parents are girls, but hey. There are exceptions."
    s "Wait, what?"
    r "Oh, right. I forgot to tell you that I’m adopted."
    r "Surprise!"
    s "How are you going to just casually drop that sort of bombshell on me?"

    scene rindormfortyfive6
    with dissolve

    r "Bombshell?"
    r "I don’t really think it changes much about me."
    r "I would have turned out the same way I am with or {i}without{/i} being adopted."
    r "It’s just part of who I am. "
    r "{i}And{/i} I get the added benefit of being able to blame all of my mental issues on my biological parents since my adoptive ones are totally free of all that."
    s "It's just really surprising hearing this out of nowhere."

    scene rindormfortyfive7
    with dissolve

    r "Listen, man, I’ll gladly go into more detail if you want, but can we sit down first?"
    r "My feet are kinda killing me and my new bed is friggin’ soft as hell. I’ve been thinking about it all day long."
    s "Oh, sure. Yeah. "
    r "Feel free to join me if you’d like!"
    r "Or just stand around and look weird. That’s fine, too."

    scene black
    with dissolve

    "Rin unstraps her shoes and tosses them against the wall, causing Futaba’s bookshelf to shake."
    "Thankfully, no books were harmed in the process and they will all live to see another day."
    "Another day that is no better nor worse than every other."

    scene rindormfortyfive8
    with dissolve2

    r "Okay! The floor is now open to any cliche adoption questions you may have."
    r "Hit me with your best shot."

    "Right. "
    "I’m sure she’s already gone over everything I could possibly ask her a thousand times before."
    "But in order to sate my curiosity, I kind of {i}have{/i} to be a little cliche."
    "I’ve spent so much time with this girl now and, if I don’t even know anything about her past, do I really know anything about her at all?"
    "Who we are in the present is a direct result of our upbringing and experience."
    "And all I know is the present version of Rin."
    "So I let the cliche questions roll."

    s "How much do you know about your biological parents?"
    r "All I {i}really{/i} know is that they didn’t love me enough to keep me."
    r "I remember hearing something about how my mom was kind of insane and that my dad was a huge cheat who didn’t want to be burdened by a kid or something."
    r "But, then again, that’s just what other kids in the orphanage said. And you know how that sort of thing goes."
    s "I don’t, but if it’s anything like kids {i}outside{/i} of orphanages, I’m sure they were just trying to pick fights with you or something."
    r "Yeah, pretty much."
    r "Anything else you wanna know?"
    r "I’ll tell you in advance that I don’t have any brothers or sisters."
    s "You’re an only child?"
    r "You betcha. No one’s takin’ any of {i}my{/i} old clothes or going through my closet or other stuff big sisters have to deal with."
    s "Did it ever feel strange?"
    r "The only child part or the adopted part?"
    s "...Both?"

    scene rindormfortyfive9
    with dissolve

    r "That’s another thing I don’t understand why people ask."
    r "Like, obviously it felt strange. But it also kind of...didn’t."
    r "My parents have always been really supportive of me and never made me do anything I didn’t want to do."
    r "Except that one time with the swimming pool."
    s "The...what?"
    r "Doesn’t matter."
    r "Either way, they’re good parents."
    r "And I’m pretty sure they noticed my depression before even I did since they threw me into therapy before I even thought I needed it."
    r "Granted, it wasn’t really helpful. But at least they {i}tried{/i}, you know?"

    scene rindormfortyfive10
    with dissolve

    r "Anything else? Or can I start learning things about you now?"
    s "I’ll stop bothering you with cliche adoption questions, but I’m not sure how much I’ll be able to tell you about myself."
    r "Why’s that? "
    r "Are you actually an isekai protag who got tossed into Kumon-mi after getting hit by a truck or something?"
    s "Suicide, actually."
    r "Ahh, yes. Another popular excuse to show up in another world."
    r "Does your place of origin have elves? I’ve always thought elves were hot."
    s "There were no elves, no."
    r "Damn."

    scene rindormfortyfive11
    with dissolve

    r "I’m obviously not gonna make you tell me anything if you don’t want to."
    r "I just thought it would be kind of cool to learn more about you one of these days."
    s "And I’d gladly tell you if I could."
    s "I just...have memory issues or something?"
    r "Damn. Another good example of isekai syndrome. I thought you didn’t read manga, Sensei?"

    "It’s obviously understandable why she wouldn’t believe any of this."
    "But what’s the proper way to tell someone that you can’t remember your childhood?"
    "Should I blame it on trauma despite the complete and utter lack of what that trauma would even have been?"
    "Of course not. That’s not fair to people who actually went through horrible things."
    "Things that changed their lives."
    "It’s like mine was just erased one day."
    "And my consciousness was injected into someone else."
    "What an annoyingly unlucky situation for everyone involved."

    scene rindormfortyfive12
    with dissolve

    r "So, background info aside, did you have fun today?"
    r "Did it seem like something Otoha might enjoy?"
    r "Maybe I should just test all of my date ideas on you beforehand?"
    r "You can be my guinea pig in both love {i}and{/i} coffee."
    s "I don’t know much about Otoha, but if someone like me was able to have fun, I’m sure she would have enjoyed it as well."

    scene rindormfortyfive13
    with dissolve

    r "If only she didn’t stand me up."
    s "I don’t think she was actually standing you up. She just has strict parents. You said it yourself."
    s "Besides, I don’t think she would have stopped by the cafe just to hang out with you if she wasn’t at least interested in being friends."
    r "Right! And friends is...all I want to be right now anyway."
    r "Even if I kept calling it a date and openly admitted to thinking she’s super pretty and how I want to tie the lesbian tongue knot with her."
    r "Like, I could drop her right away if I-"

    play sound "phonebeep.wav"
    scene rindormfortyfive14
    with hpunch

    "Rin’s phone suddenly beeps and she’s able to pull it out of her pocket so quickly that I don’t even remember watching her reach for it."

    r "Ah! Otoha got her phone back!"
    s "What were you saying about being able to drop her?"
    r "What? I have no idea what you’re talking about."

    if rinbetrayed == True:
        "Rin spends the next several minutes sending a barrage of text messages to her friend as I sit there and ponder over what it would be like the be on the receiving end of them."
        "In a world like this, where everyone except for a few girls shower me with affection every moment of every day-"
        "Having someone I can be this close with {i}and{/i} this far away from at the exact same time is..."
        "Weird."
        "I don’t think I like it."
        "I want to move forward with Rin, but of course she doesn’t want to move forward with me."
        "Not after I went behind her back and “stole” the last girl she was interested in."
        "Hell, she still admires Chika so much that I’m positive she’d stop this whole pursuit of Otoha if Chika even {i}hinted{/i} at wanting something more with her."
        "But obviously nothing like that is going to happen-"
        "Because Chika is mine. And Chika is only interested in {i}being{/i} mine."
        "There was never any room for Rin to be involved in that."
        "Just like there was never any room for me to be involved with her."

        s "…"
        r "…"
        s "Okay, I think it’s about time for me to head out."

        scene rindormfortyfive15
        with dissolve

        r "Ah, shoot! I’m sorry!"
        r "I was just so excited to hear back from her that I zoned out for a bit."
        r "It’s okay, I’ll tell her I-"
        s "It’s fine. It’s getting kind of late anyway."
        r "But, I mean..."

        scene rindormfortyfive16
        with dissolve

        r "Are you sure?..."
        r "We spent the whole day together."
        r "Having you leave just because Otoha got her phone back is-"
        s "I was just the backup plan, remember?"
        s "There’s no need for me anymore now that you’ve got her on the line."
        r "I really mean it, dude. I can put the phone down for-"
        s "It’s fine. Don’t worry about it."
        s "I’m sure I’ve got a million texts from Ami about when I’m going to be home anyway."
        s "We can just call it a night here."

        scene rindormfortyfive17
        with dissolve

        r "Okay, but..."
        r "I really did have fun today."
        r "Even if you were just a backup."
        s "So did I."
        s "Here’s hoping your first choice won’t bail on you again next time."
        r "Yeah..."
        r "Here’s hoping."
        r "Night, Sensei."
        r "Thanks for spending the day with me..."

        scene black
        with dissolve
        play sound "dooropen.mp3"

        "I put my shoes back on and exit the room, taking a glance back at Rin to see if she was watching me leave or not."
        "She wasn’t."

        $ renpy.end_replay()
        $ rindorm45 = True
        $ rin_love += 1
        stop music fadeout 5.0

        "{i}Rin’s affection has increased to [rin_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    else:
        s "If you want to talk to Otoha, it’s fine. I can-"

        scene rindormfortyfive18
        with dissolve

        r "There. Dropped."
        s "…"
        s "You literally dropped your phone."
        r "Otoha can wait. "
        r "You’re the one who spent the entire day with me, so the least I can do is give you my undivided attention until the night is over, right?"

        scene rindormfortyfive19
        with dissolve

        s "You’re really smooth when you’re not tripping over your words."
        r "That only happens with cute girls. I’d say you should know this, but you’re always weirdly composed whenever you’re talking to them."
        r "Like, right now for example."
        r "You don’t seem nervous at all."
        s "What would I even have to be nervous about? I’m a backup date."

        scene rindormfortyfive20
        with dissolve

        r "A date’s a date, man. "
        r "You really think I would have spent all that time kicking your butt in all of those games if I didn’t like you?"
        s "I just thought you were really into schadenfreude."
        r "And how I opened up about the adoption thing- why do you think I said all that?"
        s "Because I kept asking you questions about it."

        scene rindormfortyfive21
        with dissolve

        r "It's because I want you to know more stuff about me."
        r "And I want you to tell me more stuff about yourself."
        r "I think you might be underestimating how important you are to me, Sensei."
        s "This sounds a lot like a confession, Rin."
        r "Oh trust me, you’d know if I was confessing. "
        r "I’m so bad at it that it’s almost laughable."
        r "What I’m doing right now is looking into your eyes and...telling you that..."
        s "…"
        r "…"
        s "Telling me what?"

        scene rindormfortyfive22
        with dissolve

        r "Huh..."
        r "That’s weird."
        r "Did you change your hair or something?"
        s "No. But I {i}am{/i} wearing a slightly thicker T-shirt today."
        r "You just seem a lot more attractive all of a sudden."
        s "Even after making a fool of myself in the arcade?"
        r "And after you couldn’t finish that last slice of pizza."
        s "That slice belonged to you. I had four and you only had three."
        r "I had four slices of pizza for breakfast. There was no way I was going to have four slices for dinner as well."
        s "Who has pizza for breakfast?"
        r "The same girl who feels suddenly compelled to kiss you."
        s "…"
        s "Excuse me?"

        scene rindormfortyfive23
        with dissolve

        r "I don’t know."
        r "It just..."
        r "It came out of nowhere."

        if bonus == False:
            s "Rin, no. We are friends. You can not do this."
            s "I do not even know how to kiss."
            r "We can find out together."
            s "I don't know if this will be allowed in the censored version of the game."
            r "It should be fine as long as nothing else happens, right?"
            s "I have no idea."
            r "I, Rin Rokuhara, a legal adult, hereby consent to kissing you without any additional contact."
            r "Does that work?"
            s "If it doesn't, Patreon is far too gone to ever be saved."
            r "Sensei. I'm going to kiss you now."

        s "…"
        r "…"
        r "You’re still not nervous."
        s "Are you?"
        r "I don’t know."

        scene rindormfortyfive24
        with dissolve

        r "…"
        s "…"

        play sound "phonebeep.wav"

        "Rin’s phone goes off again."
        "And, in other news, I feel like something big is about to happen."

        s "Are you going to answer that?"
        r "No."
        s "Why not?"
        r "I don’t know."
        s "There seems to be a lot you don’t know tonight."
        r "There is."

        scene rindormfortyfive25
        with dissolve

        r "If I had gone on that date with Otoha instead of you today, would you have been jealous?"
        s "Probably."
        r "And if she was sitting where you are right now, and the two of us were face to face like this, how would you feel then?"

        if bonus == True:
            s "Also jealous but probably a bit aroused, too."
        else:
            s "A lot more comfortable but also a little sad I guess."
            s "Not because I like you but because it would be so beautiful to see something like that."

        r "Right?"
        s "Right."
        r "Hey, Sensei?"
        s "Yes, Rin?"
        r "I know Molly got to steal the honor of being the very first {i}person{/i} I kissed-"
        r "But how do you feel about being the first boy?"
        s "I mean, I feel {i}great{/i} about that, but..."
        s "Is that what you really want?"
        r "Why do you care about what {i}I{/i} want?"
        s "Because you’re just as important to me as I apparently am to you."
        r "I want to say you’re just saying that, but watching you fail so badly all day makes me think it might actually be true."
        s "It {i}is{/i} actually true."
        r "Then we should probably kiss before I get weird and change my mind."
        r "It might be a...good way for me to..."
        r "To figure out..."
        r "How I..."
        r "I..."
        s "…"
        r "…"

        scene rindormfortyfive26
        with dissolve2

        r "Mnh~"

        "And then it somehow happens."
        "I don’t fully understand how things got to this point so suddenly, but..."
        "They did."

        r "…"
        s "…"

        "Rin doesn’t make much noise after the initial sensation of our lips pressing against each other."
        "In fact, it’s the quietest kiss I’ve ever had."
        "But, at the same time, it feels like everything freezes-"
        "Which could also explain the silence if you were that dead set on documenting how things wound up like this."
        "The answer is probably simple, though."
        "And I’m probably just overthinking it."
        "In front of me-"
        "No, {i}attached{/i} to me, is a girl caught in a vortex."
        "One who’s been giving out pieces of her heart left and right, but never forward."
        "And I guess it wasn’t until the day was about to come to a close that this truly dawned on her."
        "So she dropped everything and drew out her bravery, the same way she did on the beach-"
        "Just this time, things worked out."
        "They worked out all too well."

        scene rindormfortyfive27
        with dissolve

        "We break apart-"

        r "…"
        s "…"
        s "How do you feel now?"
        r "I don’t know."
        r "You still taste like pizza."
        s "Says the girl who ate seven slices today."
        r "Yeah, so I clearly know what I’m talking about."
        r "Also, I might like you."
        r "Surprise."
        s "What about Otoha?"
        r "I can...like more than one person."
        r "I’ve told you that before."
        r "I mean, I still like Chika, too. "
        r "My brain’s all over the place."
        s "Then just stop thinking."
        r "Okay...yeah."
        r "I need your help, though."
        s "Sure, just-"

        scene rindormfortyfive26
        with dissolve

        r "Mnh..."
        r "Sensei..."

        "And then it happens again."

        scene black
        with dissolve2

        "And again."
        "And again and again and again."
        "We kiss for what feels like a full ten minutes before finally stopping."

        if bonus == True:
            "The bad side to this is that there is never even an ounce of tongue involved."
            "The good side, though,  is that now I’ve finally confirmed Rin feels at least {i}something{/i} for me. "
            "What that something is, I can’t tell you."
            "Am I still the backup?"
            "Does tonight mean I’m a priority?"
            "There’s no way of knowing without time working its magic."
            "Fortunately, right now it seems I have an endless supply of that."
            "So I can wait as long as it takes."
            "I just hope it doesn’t take long..."
        else:
            "In fact, the only reason we {i}did{/i} stop is because I got overwhelmed and started crying."
            "I can not believe I just kissed a student."
            "What have I done?"

        $ renpy.end_replay()
        $ rin_love += 1
        $ rinkiss = True
        $ rindorm45 = True
        stop music fadeout 5.0

        "{i}Rin’s affection has increased to [rin_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label futabadorm40:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
"Rin leads me to the back of the arcade rather confidently despite never having been here before."
    "I guess she really did her research online first."
    "The only issue is that now I have to try to not look like a complete imbecile playing whichever game Rin decides she wants to play first."
    "As long as it’s not one of those...dancing machines I’ve seen other [teenager]s play, though, I should be fine."
    "………"
    "……"
    "…"

    scene rindate25
    with dissolve

    "Nevermind. There is apparently more than one type of machine that can make me feel like a child."
    "I do not like this."

    r "You look like a moron right now."
    s "I want to insult you as well but you look pretty fucking cool."
    r "It’s the hoodie, not me."
    s "It definitely helps."

    scene rindate26
    with dissolve

    r "So, it’s probably safe to assume you’ve never played anything like this before, right?"
    s "Very safe. I have absolutely no idea what I’m doing."
    r "Just make sure you have your feet on the little foot-holder thingies and put both hands on the grips up here."
    r "You’ll notice a button on one of them. Press that to accelerate and move the bars around to steer."
    r "Each race has three laps and it’ll be you, me, and a bunch of AI opponents."
    r "Don’t underestimate them, though. This game might be a little retro, but the AI will fuck your day up."
    s "I am fully prepared for my day to be fucked up. Congratulations on defeating me in advance."
    r "Hey, man. There’s no fun if you give up beforehand. You’ve gotta at least try."
    r "Just think of how easy it would be to tease me if you defeated me at a game I literally taught you how to play."
    s "One can only hope."

    scene rindate27
    with dissolve

    r "Ready to do this, then?"
    s "As ready as I’ll ever be..."
    r "Good! Then-"

    scene rindate28
    with dissolve

    r "Prepare to get railed~"
    s "…"
    s "I understand that the game’s tagline is “Rail on” but don’t you think what you just said is a little...racy?"
    r "I’m gonna rail you so hard."
    s "Uh-huh."
    r "So hard you won’t even be able to walk afterward."
    r "And then when I’m done, I’m gonna call Ami over and rail your [niece]. "
    s "Rin, please."
    r "I’m gonna rail {i}everybody{/i}. All day. All night."
    r "You’ll be begging me to rail you again once we leave today. Calling it now."
    s "If your plan is to distract me through phrases that can be easily misinterpreted, it’s really not necessary. "
    s "You’re going to win no matter what."

    if bonus == True:
        r "What can I say? I’ve been railing ever since I was a little girl."
        r "I know my way around the block, man."

    scene rindate29
    with dissolve

    r "NOW, PREPARE TO DIE, LOSER!"

    scene rindate30
    with fade

    "Rin’s shout was a bit pre-emptive as we still needed to select a track and I guess...different types of motorcycles or something?"
    "I don’t know. I chose the first one I saw and, as expected, was demolished so quickly that I couldn’t even blame the bike."
    "The same pattern repeated for the next few hours."
    "Rin would take me to a machine, explain how the machine works, and then make me look like an absolute idiot in front of the...three other people that were there."
    "I’m pretty sure they may have even started laughing at me after a while."
    "And while something like this would normally bother me, today it was fine."
    "Because not only was the purpose of this trip to help cheer Rin up after the new object of her affection bailed on her-"
    "But it was the first few hours in quite some time that I’ve felt like she was actually focused on me."
    "Backup date or not, it was fun getting to see this side of her. "
    "Otoha really did miss out on something great this afternoon."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Eventually, we run out of machines to try out and head over to a pizzeria on the corner of the street."
    "We take our time sharing a pizza and wind up begrudgingly leaving one slice that we were unable to finish behind."
    "Instead of the night ending there, though, Rin urges me to come back to the dorm since she still has more time to kill and Futaba is with Nodoka tonight."
    "Having nothing else to do, I obviously agree and allow the backup date to move into its second phase."

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe45 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    jump rindorm45
...
```