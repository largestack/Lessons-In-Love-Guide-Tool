# Ruthless Rhyme Rhomp! Rap Rampage!
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar7&go=Go)


Part of event chain [Sphenopalatine Ganglioneuralgia](./dormwar6.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwar7
* Group: Main
* Triggered by label: dormwar6

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label dormwar7:
    scene nightsky
    with dissolve
    play music "maidcafe.mp3" fadein 4.0

    "It finally starts getting a little bit colder now that night has begun to set in, but not cold enough to cool my body off as we are currently heading to my favorite place in the world."
    "Apparently, Ayane arrived at the cafe in the middle of the test of knowledge, so Uta had to sprint over there to meet up with her the second that contest came to an end."
    "Now, I’m not going to pretend I know anything about rap..."
    "In fact, if you were to quiz me on every single genre of music, that’s the one I’d probably score the lowest in."
    "But, then again, there are all sorts of music genres now, so who even knows?"
    "Maybe I know more about rap now than I do, like...post-alternative countrycore or something. "
    "Is that a genre?"
    "I guess that doesn’t matter. "
    "What does matter, though, is that I am about to see girls in maid dresses. "
    "So fuck yeah."

    scene rapbattle1
    with dissolve

    ay "Sensei! Ready to watch me kill a girl?"
    u "Good evening, Master! Table for one? "
    s "Uta, why aren’t you in costume?"
    u "Because we closed early tonight to hold the rap battle thingy. Duh."
    s "So there...won't be maid outfits?"
    u "Nope!"
    s "At all?"
    u "There are some in the back room if ya wanna try one on. None of us girls are wearin’ ‘em, though."
    ay "Do you need help putting one on, Sensei?"

    if bonus == True:
        s "It’s not the same if I wear it..."
        u "C’mon! You might look really cute! "
        ay "You also have the same chest size as Ami, so we could probably find one that fits pretty easily!"
        a "Hey! I didn’t hear whatever you just said, but I feel like it was something mean!"
        u "Ahh, youth. Poor girl will get ‘em some day. Just has to believe in herself."
        s "Sure. I was just reading a paper about the effects of believing in yourself on the female anatomy the other day."
    else:
        s "No thanks. I've tried on Ami's before, so I know where all the drawstrings are and stuff."

    scene rapbattle2
    with dissolve

    u "Holy heck, really? I was just kidding."

    if bonus == True:
        u "I'm pretty sure mine just came from all the meat I ate and stuff."

    ay "See what I’m up against, Sensei? {i}This{/i} is what I have to battle for your love. "
    ay "You are as good as mine."

    scene rapbattle3
    with dissolve

    u "Ooooh, look at this wave of confidence. "
    u "That’s gonna make it all the more sweet once I take you down to Chinatown and claim Sensei for the girls of the second floor! Hoo-rah! "
    s "How is this even going to work? Are you two just going to...see who can rap the most...effectively or something?"

    scene rapbattle4
    with dissolve

    u "Wow. Really showin’ your age now, aren’t you?"
    s "I’m showing a disinterest in rap. I just want to know how I’m supposed to judge who is better."
    ay "Rap isn’t something you can just {i}judge{/i}, Sensei."
    s "Well if it’s not something I can easily judge and no one is wearing a costume, why am I even here?"
    u "Obvs cause there’s a giant magnet inside of me that keeps pulling you over. There’s no other explanation."
    u "Now go sit down and watch me demolish your adopted daughter. "

    scene rapbattle5
    with dissolve

    ay "Don’t worry about me getting “demolished,” Sensei. I’ll be fine."
    s "Sure. {i}But what do I do?{/i}"
    ay "Just follow your heart!"
    ay "Rap’s about feeling the beat and listening to the words. The second we start grading it based on predetermined qualities laid out on a spreadsheet is the second hip hop dies."
    u "You’re right on that, Ayane! "
    u "And Sensei, shouldn’t a poem nerd like you be all about rap considering it wouldn’t even exist if not for poetry and the effect of spoken word on the human subconscious?"
    s "Why are two [teenage]Japanese girls lecturing me on the origins and importance of rap music?"
    u "Cause you’re closed-minded and trapped in your ways!"
    ay "And it’s our job as your loving students to pull you out and teach you just as many things as you teach us!"
    s "I haven’t taught you anything, though."
    u "Well then...make it up to us or something! "
    u "Ayane and I have to get the ball rolling!"
    ay "That we do!"
    ay "And remember, Sensei. Do not judge. Just {i}feel{/i}."

    scene black
    with dissolve

    "I can already tell that I am going to hate this."
    "………"
    "……"
    "…"

    scene rapbattle6
    with dissolve

    ki "Hey! Come to cheer on Ayane, Sensei?"
    s "I came here to see girls in maid outfits. "
    a "Want me to go get changed?"
    s "Kind of, but that would make it weird for literally everyone else."
    ki "Little bit. "
    ki "I like maids as much as the next person, but there’s a time and place for everything. "
    a "And that time and place is whenever Sensei wants, wherever he wants."
    a "I’ll go get changed."
    s "It’s fine. Don’t worry about it."
    s "Also, do either of you two know anything about “feeling” rap?"
    a "There’s three of us, Sensei. Maya is right there."
    m "No I’m not. Please ignore me."
    s "I feel like Maya knows even less about rap than I do."
    m "For once, you are definitely not wrong."
    ki "It’s kinda just like...if you wanna move your body. Or if you hear a phrase or lyric that stands out in your mind."
    a "Think of all those poems you used to read me when I was little and stuff. There were always lines that you were teaching me the importance of."
    a "I think anything that makes you feel like that in song form is what you’re supposed to feel tonight...or something."
    ki "Granted, it’s two [teenage]girls who have never rap battled before freestyling at each other, so I think we can fully expect to feel absolutely nothing throughout this entire contest."
    s "Yeah, I can’t imagine this going well...but I guess we’ll have to-"
    w "Hey. You there. Imbecile."

    scene rapbattle7
    with fade

    s "Oh, you two are here."
    w "We are here."
    w "Now, tell me, who is the girl in the cute dress?"
    s "Wakana Watabe."

    scene rapbattle8
    with dissolve

    w "Not me, you fucking idiot. The tiny one. "
    w "Also, be careful about what you say to me in front of Osako. She can snap your neck with just two fingers."
    os "It would probably take a whole hand, but yeah. "
    s "Terrifying."
    s "Anyway, that girl in the dress is Sana Sakakibara. I figured you’d remember her considering you ordered like fifty beers from her that one time."
    os "That’s exactly {i}why{/i} she can’t remember..."
    os "I had to carry her up the stairs when we got home."

    scene rapbattle9
    with dissolve

    w "Ooooohhh..."
    w "Yeah, I don’t remember you at all."
    sa "I’m...also in the class next door to yours but...I don’t really talk much, so..."
    w "Good. You’ll absorb lessons better if you sit there and shut up. I’m surprised someone like you even exists in this man’s class."
    sa "Sensei...has actually helped me a lot and..."
    w "I can help you more. Come to my class instead."
    s "Sana, come here. Get away from her as quickly as you can or you’ll start talking about how much you want to die every thirty seconds."

    scene rapbattle10
    with dissolve

    sa "But...I’d never say something like that!"
    s "Exactly. Because you are the embodiment of purity and Wakana Watabe is everything impure about the world itself."
    os "That’s not true. You should see her when she tries cooking dinner. It’s like a whole different Wakana."
    s "Wakana, please cook dinner for me sometime."
    w "Osako. His kneecaps, please."
    os "Heheh~ You really like him, don’t you?"

    "Is this seriously how Wakana shows affection?"

    scene rapbattle11
    with dissolve

    w "Hah...listen-"
    w "In the event that you want to actually do something with your life and agree to not undergo any sudden personality shifts that cause you to act out in a rowdy, irresponsible, or uncouth way..."
    w "You may transfer into my class."
    w "You are cute and you are quiet. The ideal combination for a girl of your age and...size."
    sa "I...umm..."
    sa "Thank you?..."
    w "You’re welcome."
    s "…"
    s "I think that’s the nicest I’ve ever seen her treat anyone that isn’t named Makoto Miyamura."

    scene rapbattle12
    with dissolve

    os "She’s probably just feeling a little reminded of how she was when she was younger."
    os "Wakana’s never had a hard time {i}approaching{/i} people per se, but her social skills have always been a little...lacking."
    s "When did she start saying her catchphrase?"
    os "She’s been saying that for as long as I’ve known her."
    s "Then kudos to her for having the willpower to stick it out and not follow through on her desires."
    s "I think I have to watch girls yell at each other or something, though, so I’ll catch up with you some other time."
    os "Well, we get to keep the dojo now, so there’s always there. "
    os "But yeah, see you around. "

    scene black
    with dissolve
    stop music fadeout 30.0

    "………"
    "……"
    "…"

    scene rapbattle13
    with dissolve

    u "Ladies and gentlemen! Boys and girls! Molly!"
    a "Uta, it’s just mean to say that when she’s not even around to react to it."
    t "I will speak with the green onion on behalf of the Emerald Guardian. Speak."
    u "That won’t be necessary, Tsunecchi! But please relay my words to Molly so she can know she is loved."
    ay "Uta and I would like to thank everyone for coming out to the main event of night one!"
    ay "We realize that some people have decided to go to the hotel instead, so everyone here will receive a bonus present of one hug from either me or Uta! Your choice!"
    u "Unless your name is Sensei! Then you have to hug Ayane because my body is still off limits."
    s "God damnit."
    ay "I’m going to pretend I didn’t hear that!"
    u "Anyway, tonight’s battle will be a standard, single round freestyle exhibition match!"
    u "Ayane will go first and say some words, then I will go second and say some better words! The end!"
    s "Weren’t you just talking yesterday about how you weren’t good at “the words?”"
    u "Nope! Start the beat, Osako!"
    os "Wait, what? Me? Why?"
    u "Because you work here and you can reach the PA system in the back!"
    u "Just go turn on the speakers and press play on my phone! It’s already hooked up."
    os "Uhh...I mean...I guess if no one else can do it..."
    u "…"
    ay "…"
    u "Stay with us, folks! We should have music any minute now!"
    ay "…"
    u "…"
    ay "…"
    u "…"
    u "Any minute now!"
    ay "…"
    u "…"
    os "Uta! You have a text from your dad! Do you want me to read it?"
    u "No thank you, Osako! Just press play, please!"
    ay "…"
    u "…"

    play music "recognize.mp3"
    scene rapbattle14
    with dissolve

    u "There we go, there we go!"
    u "Show us what you got, Master-A!"

    scene black
    with dissolve

    "Uta steps aside and lets Ayane take a more centered position with her microphone."
    "And, in other news, I feel a lot more uncomfortable than I expected to feel."
    "Which was already very uncomfortable."

    scene rapbattle15
    with dissolve

    ay "I’m sorry in advance for the beats that I drop-\nbut the truth is, {i}bitch{/i}, that my flow can’t be stopped."
    ay "I’m a legend with the mic and a beast on the stage-\nand you {i}can’t{/i} take my man, we’re already engaged."
    s "We are not. That is not true."
    ki "Shh!"

    scene rapbattle16
    with dissolve

    ay "A battle for Sensei’s a battle I’ll win-\nAny words you spit my way slide right off my skin."
    ay "Karate to rapping, my skills are the best\nAnd what do you have, Uta? The size of your chest?"
    ay "It’s surprising you’re small when you talk so damn big-\nMy rhymes crumble mountains, you can’t even snap twigs."
    ay "A butler named Geoffrey, a chicken named Todd.\nA boyfriend named Sensei, who’s more like my god."
    ay "The list is enormous. It goes on forever.\nTo battle with me is a heavy endeavor."
    ay "You up to the task? Gonna run away scared?\nYou nervous? You frightened? Do your thoughts feel impaired?"
    ay "You sit there and smile, but I feel it inside-\nYou’re a scared little girl. So go run away. {i}Hide.{/i}"
    ay "Didn’t think for a second we’d be doing it my way\nStill I’m here in control because, bitch, I’m Ayane."
    ay "A princess. A queen. Ride to[school] in a Lexus.\nWith so many guns that you’d think I’m from Texas."
    ay "The dorm war is over. I’ve already won it."
    ay "Uta’s the ground. Ayane’s the summit."

    scene rapbattle17
    with fade

    u "Okay okay okay! Short, but sweet! Color me impressed! "
    u "Gotta say, Ayane, you did pretty darn good just now."
    ay "Think you still have a chance?"
    u "A chance? Ha."
    u "Listen up, {i}princess...{/i}"

    scene rapbattle18
    with dissolve

    u "My feelings are hurt, guys! What on earth should I do?"
    u "Should I listen to her and give up on round two?"
    u "Or should I take her to[school]?\nSit her down at her chair?\nTeach her not to step up 'less she's truly prepared?"

    scene rapbattle20
    with dissolve

    u "Your rapping was good. Hell, it was even expressive.\nBut to mention my breasts is a tad unimpressive."

    if bonus == True:
        u "You’re better than that. It was really unsightly.\nBut of course you play dirty when you [masturbate] nightly."
    else:
        u "You’re better than that. It was really unsightly.\nBut of course you play dirty when you drown kittens nightly."
        s "What"

    u "The world's greatest maid don’t need slander for victory.\n She thinks winning like that'd be too contradictory."
    u "Cause I know you and me don’t have all that much history-\nAnd this freestyle’s your intro, while it’s my valedictory."

    scene rapbattle19
    with dissolve

    if bonus == True:
        u "Ha! I said “dictory.” And dick’s slang for penis.\nBut Ayane probs knows this since she’s so libidinous."
    else:
        u "Ha! I said “dictory.” That's not even a genus.\nAnd that doesn't make sense cause of censorship. Venus."

    u "Is Uta a genius? Does anyone see this?\nDoes she have an IV?\nAre these rhymes intravenous?"

    scene rapbattle20
    with dissolve

    u "You say I’m the ground...and you are the summit.\nThing is, after this battle, your stock’s gonna plummet."
    u "Why should you win when you fight with no dignity?\nAnd why should I fail from your selfish malignity?"
    u "Why even rap? Why not fight differently?\nCause you might have weapons, but I’ve got creativity."

    if bonus == True:
        u "It's a battle of boring versus sheer versatility.\nAnd yeah, you might have Sensei, but I’ve got my virginity."
    else:
        u "It's a battle of boring versus sheer versatility.\nAnd yeah, you might have Sensei, but I’ve got masculinity."

    scene rapbattle21
    with dissolve

    a "Wait, what? That’s just part of the rap, right?"

    if bonus == False:
        s "I have always thought Uta felt rather masculine, though I wish she'd stop beating me up and trying to watch football with me."

    ki "Hahahahahahah! Oh my god!"
    c "Holy shit. Uta’s actually really good."
    m "She’s...probably just trying to get a rise out of Ayane. That’s how these contests go, Ami."
    s "I thought you didn’t know anything about rap?"
    m "You’re disgusting."
    ay "Uhhh...Uta? That’s enough. And you probably shouldn’t say things like that when the entire class is-"
    u "I’m so heckin’ sorry. I’m just in the zone.\nSee when I have the mic, it gets a mind of its own."
    u "I don’t claim to be perfect. I don’t own the world.\nAnd yeah, I am short. But I’m no little girl."
    u "I’m Uta, you see. There’s no one like me.\nA reincarnated rap god that’s finally set free."

    scene rapbattle22
    with dissolve

    u "So I hope that this all leaves a lasting impression."
    u "Now take a seat, bitch...cause class is in session. "
    ay "…"
    u "What up?"
    ki "Encore! Encore!"

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene rapbattle23
    with dissolve

    c "And you said you didn’t want to come here tonight."

    if bonus == True:
        y "Shouldn’t you be a little more pissed off after that virginity comment?"
        c "That was just Uta calling Ayane slutty. It doesn’t mean she knows something about her."
        c "The two of them only like, just started hanging out I think. "
    else:
        y "Shouldn’t you be a little more pissed off after that masculinity comment?"
        c "What? Why would I? Girls can be masculine if they want. Just like guys can be feminine."

    t "That green onion can really spit."

    scene rapbattle24
    with dissolve

    c "Did someone tell you to say that, Tsuneyo?"
    t "I felt it in my heart. "
    t "Though that could just be heartburn. "
    y "So...contest is basically over then, right?"
    c "We’ve still gotta wait for Sensei to choose the winner. "
    y "Well at least we know if he chooses Ayane that there’s a clear bias thing going on. "
    y "I don’t care about music at all, but even I can tell she was the loser there."
    y "Fuckin’ midget girl was sayin’ words I’ve never even fuckin’ heard before."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene rapbattle25
    with dissolve

    u "Well, Sensei! Which one of us do you think did better?"
    u "Keep in mind that whoever you choose will have a point added onto their team’s total!"
    s "…"

    "While it’s true that Uta’s rap was definitely...more detailed, I don’t know if I really {i}felt{/i} anything."
    "I mean, I didn’t really feel anything from Ayane’s either, but that’s probably because I just don’t like rap. "
    "Tonight absolutely did not change that."
    "Ayane {i}did{/i} call me her god, though...so..."

    s "The person I choose is..."

    scene rapbattle26
    with dissolve

    ay "Wait."
    u "What do you mean wait? This is the most important part."
    ay "Sensei, you should choose Uta. "
    ay "She’s clearly much better at this than I am and deserves the victory, as much as it pains me to say that."
    u "Hey...you did great, too. Maybe Sensei liked yours more? It’s really up to him."

    scene rapbattle27
    with dissolve

    ay "Sensei will just wind up looking biased if he picks me. "

    if bonus == True:
        ay "And after your...virginity comment, we should probably make sure that my relationship with him doesn’t snowball into something that will get him in trouble."
        u "I was just makin’ a joke. I don’t know the first thing about your sex life."
    else:
        ay "And after your...masculinity comment, we should probably make sure that my relationship with him doesn’t snowball into something that will get him in trouble."
        u "Uhh...not sure what kinda difference that would make, but I'll try and...clear things up?"

    u "Want me to go around and clear that up with everybody, or-"
    ay "It’s fine. Really, don’t worry about it."

    scene rapbattle28
    with dissolve

    ay "Everyone! I am conceding the competition to Uta as she was the clear victor!"
    ay "If Makoto asks, just tell her Sensei picked her instead! I don’t want to get yelled at for “quitting.”"
    a "Yeah...I love you, Ayane, but you definitely lost."
    m "More people should be talking about Uta’s sudden extreme increase in vocabulary. That was weird."
    s "Yeah, what happened to being bad with words?"
    u "Didn’t you hear my rap, Sensei? The mic had a mind of its own. I’m just little ole’ Uta."

    if ayanelust10 == True and ayane_lust >= 15 and kirin_lust >= 15:
        scene rapbattle29
        with dissolve

        ay "So, now that the final competition is over, should we start heading over to the hotel to meet up with the rest of the girls?"

        if bonus == True:
            u "Wanna come sleep in our room to celebrate my victory, Sensei?"
            ay "Ooooooor, you could come sleep in {i}our{/i} room to reward me for my generous concession. "
            u "But Ayane, what would people think after my totally serious virginity comment? "
            ay "Perhaps being under the supervision of nine other girls will be enough to dispel any rumors?"
            ay "Or, if Sensei wants to just give up on his career and be with me and only me for forever starting right now, it would also be a good time."
            s "Or, alternatively, the three of us could get our own room and celebrate by-"
            ki "Ayaneeeeeeee~"

            scene rapbattle30
            with dissolve

            "Kirin comes trotting over to the three of us and quickly steals away Ayane’s attention."

            ay "What do you want?"
            ki "I just want to talk for a little while. Is that okay?"
            ay "About?"
            ki "Stuuuuuuuff~"
            ki "It would be nice if we could talk in private, though."
            u "Why’s Kirin actin’ all weird?"
            s "It’s probably best not to ask."
            s "Ayane, do you need me to stay here? Or do you want to talk to her?"
            ay "…"
            ay "You can go, Sensei. I’ll be fine."
        else:
            s "Yes. I see no need for additional dialogue here."

        scene black
        with dissolve

        "Uta and I walk away from Ayane as Kirin approaches and begin to clean up the maid cafe with the rest of the girls."
        "Even Wakana and Osako chip in, so-"
        "Well, I guess Osako works here. So that isn’t really much of a surprise."
        "Either way, all of us start tidying things up while Kirin pulls Ayane to the side."
        "I try to listen in, but I’m not able to catch any of what is discussed."
        "………"
        "……"
        "…"

        scene rapbattle31
        with dissolve

        ki "Hey! Great job up there. You really impressed me."
        ki "Kind of cool that you gave the win to Uta, though. She deserved it with all those crazy rhymes. "
        ki "Like, where did all of that even come from? Hahahaha!"
        ay "Just get to the point, Kirin. You wouldn’t have needed to pull me away from Uta and Sensei if you were just going to talk about this."
        ki "What the fuck do you know about what I would or wouldn’t do? I’m just trying to be nice."
        ay "And that’s it? There’s nothing else you want?"
        ki "Actually...there {i}is{/i} something. "
        ki "See, I lost my contest today too. So we both let our teams down pretty badly."
        ay "No one expected you to beat Miku, so you didn’t let anyone down."
        ki "That might be true, but I still can’t help but beat myself up over it. You know?"
        ay "And? What are you getting at?"
        ki "Hmm..."
        ki "Come here."
        ay "I don’t-"
        ki "Fine, I’ll just whisper it into your ear then."

        scene rapbattle32
        with dissolve

        ki "…"
        ay "…"

        "…"
        "…"
        "…"

        scene rapbattle33
        with dissolve2

        ay "…"
        ay "Are you kidding?"
        ay "Is this a joke?"

        scene rapbattle34
        with dissolve

        ki "Come on~ I think it sounds fun."
        ki "Just the once and I won’t bother you about it anymore."
        ay "That’s what you said last time."
        ki "I know, I know, but...well, you know how hormones work and all that."
        ki "Anyway, I’ll come pick you up when I’m ready. Sound good?"
        ay "Why are you doing this to me?"

        if bonus == True:
            ki "Cause I’m horny. Duh. "
        else:
            ki "Cause it's boring with only two players. Duh. "

        ki "Anyway, nice talking to you. And good job with your rapping and stuff."
        ki "See you tonight, Ayane."

        scene black
        with dissolve2

        "Welp, I guess that about wraps it up for the first day of competitions."
        "I have no idea what tomorrow is going to bring, but if it’s even a fraction as...exciting as it was today, I am going to have to call out of work on Monday to recuperate."
        "We all finish cleaning up the maid cafe within thirty minutes or so and then make our way through the cold of the night to the hotel..."

        $ renpy.end_replay()
        $ dorm2warpoints += 1
        $ dormwar7 = True
        stop music fadeout 5.0

        "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
        "………"
        "……"
        "…"

        jump dormwar8

    else:
        scene rapbattle29
        with dissolve

        ay "So, now that the final competition is over, should we start heading over to the hotel to meet up with the rest of the girls?"

        if bonus == True:
            u "Wanna come sleep in our room to celebrate my victory, Sensei?"
            ay "Ooooooor, you could come sleep in {i}our{/i} room to reward me for my generous concession. "
            u "But Ayane, what would people think after my totally serious virginity comment? "
            ay "Perhaps being under the supervision of nine other girls will be enough to dispel any rumors?"
            ay "Or, if Sensei wants to just give up on his career and be with me and me only for forever starting right now, it would also be a good time."
            s "Or, alternatively, the three of us could get our own room and celebrate by-"
            u "Nope!"
            ay "…"
            s "…"
            ay "I mean...{i}I{/i} didn’t say no..."
        else:
            s "Yes. I see no need for additional dialogue here."

        scene black
        with dissolve2

        "Everyone (Except me) works together to clean up the maid cafe and, within the next twenty minutes or so, we begin our journey to the hotel."
        "Thankfully, it isn’t {i}that{/i} far from where we are now, so the walk doesn’t take that long."
        "But anyway, I guess that wraps it up for the first day of competitions."
        "I have no idea what tomorrow is going to bring, but if it’s even a fraction as...exciting as it was today, I am going to have to call out of work on Monday to recuperate."

        $ renpy.end_replay()
        $ dorm2warpoints += 1
        $ ayanelust15skip = True
        $ dormwar7 = True
        stop music fadeout 5.0

        "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
        "………"
        "……"
        "…"

        jump dormwar8

label dormwar8:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```