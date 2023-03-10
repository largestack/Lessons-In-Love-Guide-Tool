# Cold Air of an Encroaching Winter (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 25

* Day of week is not Thursday

* Event [Regularly Scheduled Programming](./dojo25.md) (Ayane) is completed)



## Next events

* [Ayane: First and Second](./dojo30.md)

## Event properties

* Id: ayanedorm25
* Group: Ayane
* Triggered by label: ayanedorm
* Triggered by branch label: ayanedorm
* Triggered by path: ayanedorm->ayanedorm25

## Official wiki page

[Cold Air of an Encroaching Winter](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanedorm25&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm25:
    play sound "knock.mp3"

    "I knock on Ayane’s door and wait for her to answer."

    ay "Coming, Sensei! Give me one second!"

    if bonus == True:
        s "Can’t I just walk in? I’m pretty sure I’m desensitized to seeing you naked at this point."
        ay "A - Rude! You should always be excited to see me naked."
        ay "B - We’re going somewhere tonight and I’m just grabbing some stuff."
        ay "Do you need a towel?"
        s "What? Why would I need a towel?"

        "I hear Ayane close her wardrobe through the thin walls of the dorm before she opens the door and joins me in the hall."
    else:
        s "Sure thing. I would never do something as impure as walking in on a girl before she allows me to."

    play sound "dooropen.mp3"
    scene ayanebathredux1
    with fade

    if bonus == True:
        ay "You need a towel because we’re going to go take a bath together and the towels they give you in public bathhouses are kind of bleh."
        s "Correct me if I’m wrong here, but I’m pretty sure there isn’t really a public bathhouse {i}anywhere{/i} that would be okay with the two of us bathing together."
    else:
        ay "Thanks!"
        ay "You need a towel because we’re going to go the bathhouse!"
        s "But bathing together would be icky and not allowed."

    scene ayanebathredux2
    with dissolve

    ay "And {i}that's{/i} where you're wrong, Sensei!"
    ay "Under normal circumstances, that would be correct-"

    if bonus == True:
        ay "But lucky for us, I have discovered through the power of money that I can rent out the mens’ side of the local bathhouse for a very negligible amount of money."
        s "What exactly is a negligible amount of money to you, Ayane?"
        ay "I think it’s only like 40,000 Yen to rent out the men's side per hour. The girls’ one is a lot more expensive because, well, girls actually exist in Kumon-mi."
        s "Men exist as well. Just...less of them."
    else:
        ay "And you are right about it today as well!"

    scene ayanebathredux3
    with dissolve

    ay "You’re the only man that exists for me, Sensei."
    s "Thank you?..."

    scene ayanebathredux4
    with dissolve

    ay "Well, you and Geoffrey. "
    ay "And I guess my dad by default."
    ay "But mostly you."
    ay "But anyway, I packed an extra towel for you, so you don’t need to worry about the weird public ones they probably only clean like, once every three days."
    ay "So, are you excited to see me naked again or are you still “desensitized” to it?"

    "I wasn’t exactly planning on spending the night in a public bathhouse but, I guess something like that could be nice every once in a while."
    "Ayane and I haven’t really had any time to relax together since the beach, and..."

    if ayanelust10 == True:
        "Well, frankly, I’m still a little confused about how to even bring what happened with Kirin up."
        "It seems like Ayane’s been content with just ignoring it so far and that’s...weird to me."
        "Here’s hoping I’ll be able to actually gauge how she feels about that tonight instead of putting up with her immense talent to deflect anything and everything."
        "I don’t want her to just keep pretending to be happy if she’s not."
        "She does that often. "
        "It’s the worst thing about her, if I’m being honest."
        "Granted, that isn’t exactly saying much since she doesn’t have many bad qualities, but-"
    else:
        "Well, something like that might actually be a good change for us."
        "She’s clearly hyperactive and I’m admittedly tense all of the time, so finding out a way for the two of us to wind down sounds pretty solid to-"

    scene ayanebathredux5
    with dissolve

    ay "Sensei? You’re zoning out. Is everything okay?"

    scene ayanebathredux3
    with dissolve
    stop music fadeout 15.0

    if bonus == True:
        ay "Oh, wait! You started zoning out the second I mentioned my naked body. You aren’t desensitized at all, are you?"
        ay "Wanna go back into my room for a quickie before we head over to the baths? It might help to get some of that {i}energy{/i} out of you."

        if day < 6:
            s "Please don't say things like that when there are other girls in the hallway."
        else:
            s "Well, it’s true that no one else seems to be around right now but..."
            s "Maybe it would be better if we just took advantage of the bathhouse instead?"

        ay "Whatever you say, Sensei~"
        ay "It just might be hard for us to do anything {i}at{/i} the bathhouse since the staff could show up at any moment."
        ay "But we’ll see..."
    else:
        s "Yes. I am just very excited to bathe all by myself."
        ay "Me too! Let's get a move on!"

    scene black
    with dissolve2

    if ayanelust10 == True and bonus == True:
        "We’ll see, huh?"
        "Normally, I feel like Ayane would have jumped at the thought of messing around in public."

        s "..."

        "Maybe the Kirin thing {i}has{/i} gotten to her after all?..."

    "………"
    "……"
    "…"

    scene ayanebathredux6
    with dissolve2
    play music "acoustic.mp3" fadein 5.0

    "We show up at the bathhouse roughly twenty minutes later and Ayane semi-awkwardly approaches a girl that looks to be around her age at the desk."

    if bonus == True:
        ay "Heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey..."

        "Nevermind. It isn't semi-awkward at all. It is 100%% awkward."

        ay "We'd, uhh...like to rent out the entire men's side of the bath for a couple hours."
        q "..."
        ay "..."
        q  "Just the two of you?"
        ay "...Yup!"
        q "..."
        s "..."
        q "You do know how that looks, right?"
        ay "Completely and totally normal?"

        scene ayanebathredux7
        with dissolve

        s "If it's not allowed, feel free to kick us out. I had a feeling this wasn't going to work anyway."
        q "It's not that it's not {i}allowed.{/i} We can rent out that side of the bathhouse to pretty much anybody since there's no one around to use it anymore."
        q "I just know that I'm going to have to be the one to clean up after you two are done doing whatever disgusting things you came here to do and I really don't want to have to deal with that tonight."
        s "You're...very forward about this."
        q "Yeah, that's kind of my thing."

        scene ayanebathredux8
        with dissolve

        ay "You're...not going to, like...report us or anything, are you?"
        q "You are greatly overestimating how involved in this affair I want to be."
        s "We're really just here to take a bath."

        scene ayanebathredux9
        with dissolve

        q "And I'm really just here to take your money and ask you very kindly to not clog the filters in the bath with bodily fluids."

        "I don't think I'm going to return to this bathhouse any time soon."

        s "Listen, we-"

        q "Nope! Looking away. Not involved. Your total is 50,000 yen. Just leave the money on the table and we can all forget this ever happened."
        ay "I..."
        ay "Uhh..."
        ay "Is there an ATM here? Because that's more cash than I have on me at the moment."

        scene ayanebathredux10
        with dissolve

        q "..."
        ay "..."
        q "There's a convenience store down the road."

        scene black
        with dissolve2

        "Ayane and I make an awkward trip to the convenience store for more money and I attempt on the way to coerce her into backing out of this."
        "Of course, she doesn't agree since we have already {i}made it through the hard part{/i}, and we wind up, once again, entering the bathhouse and doing our best impressions of people who are not sexually attracted to one another."
        "Thankfully, the girl at the counter doesn't ask any questions this time and takes Ayane's money before pointing us in the direction of the bath."

        if ayanelust10 == False:
            "So...everything kind of works out in the end if you're able to ignore the fact that a random teenager now knows more about our relationship than literally anyone else."
            "I'm sure nothing bad will come out of that at all."
        else:
            "So...everything kind of works out in the end if you're able to ignore the fact that yet {i}another{/i} teenager knows about Ayane and me now..."

        "........."
        "......"
        "..."

        scene ayanesenseibath1
        with dissolve2

        ay "So, uhh...that was weird. Right?"
        ay "I had this whole cover story about you being my step-dad planned out, but I didn't even get to use it since I started blanking as soon as we reached the counter."
        s "To be fair, I doubt she would have bought it anyway. That girl has clearly seen some things."

        scene ayanesenseibath2
        with dissolve

        ay "You don't think she's going to tell anyone, do you? Because if we get in that bath and the police show up to take you away, we're going to have to run away naked and that sounds kind of embarrassing."
        s "Embarrassment would be the least of our problems if that were to happen but, honestly...I don't think she will."
        ay "I really hope not. I don't want to imagine a life where the two of us couldn't do things like this."
        s "You mean the life we almost had up until like, five minutes ago? Because I probably don't have to remind you, but this just {i}barely{/i} worked."

        scene ayanesenseibath3
        with dissolve

        ay "That may be true, but we're here now! So we should start thinking more about each other and less about the girl who now probably knows but hopefully {i}doesn't{/i} know about our secret."
        s "She definitely knows, Ayane."

        if ayanelust10 == True:
            scene ayanesenseibath2
            with dissolve
            ay "We don't know that! It could still be a huge misunderstanding or something!"
            ay "It's nothing like-"

            scene ayanesenseibath4
            with dissolve

            ay "It's nothing like..."
            ay "What happened with Kirin..."
            s "..."
            ay "..."

            "Ahh, there it is."
            "It was only a matter of time."

            scene black
            with dissolve2

            s "Come on. Let's get in the bath that we just paid a disgusting amount of money for instead of having an entire conversation directly outside of it."
            ay "Y...Yeah."
            ay "Hey, wait a second! You didn't pay anything at all! My money isn't {i}your{/i} money until you sign the marriage papers!"
            s "Just forge my signature. You memorized it, right?"
            ay "I tried! But {i}apparently{/i} we both have to be present for it."
            s "Ayane, don't tell me you actually-"
            ay "Sorry, Sensei. Are you saying something? I can't hear you over the sound of my love!"
        else:
            scene ayanesenseibath5
            with dissolve

            ay "Well, uhh..."
            ay "Maybe she'll feel more inclined to {i}keep{/i} it a secret if we invite her in as well?"
            s "Genius plan. You go ask her and I'll wait here for the impending threesome."
            ay "..."
            s "What?"
            ay "Is that really what you want?"
            s "Ayane, no."
            s "Well, yes. But no."
            s "That was obviously sarcasm."
            scene ayanesenseibath5r
            with dissolve
            ay "Well, I'm sorry for not picking up on it! It's hard enough ignoring the outline of your penis through your towel!"
            s "Then {i}stop staring at it.{/i}"
            ay "I can't! It's like it's calling my name!"
            s "I think this might be sexual harassment."
            ay "Just...ignore anything I say until we're in the penis!"
            ay "I mean bath! Ignore anything I say until we're in the bath!"
            s "…"
            ay "No! {i}You're{/i} a pervert!"

            scene black
            with dissolve2

        "I sigh to myself and remove my towel, watching from behind as Ayane lowers herself into the bath."

        scene nightsky
        with dissolve2

        "The cold air of an encroaching winter confuses my skin as I come into contact with the water."

        play sound "water1.mp3"

        "I move over to Ayane, who has since slumped down to the point where I can no longer see any of her “features.”"
        "She notices me staring and pops above the water for a moment, teasing me with a brief flash of her chest before sitting back down."
        "Sensing I won’t be getting any more than that, I take my place beside her..."

        scene ayanesenseibath6
        with dissolve2

        ay "…"
        s "…"

        "The two of us sit in silence for a few minutes, listening to the soft sounds of running water and occasional gusts of wind. "
        "Despite half of my body being submerged in nearly-scalding water, the top part of me can’t help but freeze."
        "The feeling of Ayane’s back pressing up against mine provides some temporary relief, but does nothing for my chest."
        "I’m sure she’s in the same boat."

        s "Are you also freezing?"
        ay "I’m actually kind of burning up."
        ay "And no, not because I’m horny."
        s "Are you horny, though?"
        ay "Am I ever not horny?"
        s "Maybe like once or twice since I’ve met you, you haven’t been."

        scene ayanesenseibath7
        with dissolve

        ay "You’re the same, though. Aren’t you?"
        s "For the most part. Which is why I’m surprised we’re not having sex right now."
        ay "We can have sex when we get home if you want. "
        ay "Or we can go to your house and have sex after this."
        ay "I don’t think I want to do it in the bath, though."
        ay "Baths are meant for getting clean, not dirty."
        s "Couldn’t you have just taken a bath at the dorm then?"
        ay "We only have showers in the dorm. And it wouldn’t have been easy for me to sneak you into them."
        ay "Are you not pleased with our alone time here? Even after all of the money I spent on it?"
        s "Yeah, I’m sure that 50,000 Yen is putting a huge dent in your savings."

        scene ayanesenseibath8
        with dissolve

        ay "Hahah~ It sure is..."
        ay "I am never going to financially recover from this."

        scene ayanesenseibath9
        with dissolve

        ay "Oh, speaking of finances, you’re not opposed to me bribing the principal to end up in your class again next year, are you?"
        ay "I think I can get Ami and me in. I’m not sure about Maya, though."
        s "I’m pretty sure Maya would prefer to be in a different class anyway."
        ay "Not if Ami and I are with you. She needs at least one of us or everybody will think she’s a weirdo."
        s "Good. She is a weirdo."

        scene ayanesenseibath10
        with dissolve

        ay "You’re not supposed to talk down to people who aren’t here, you know?"
        ay "It would be completely different if Maya were bathing with us. But alas, ‘tis just you and I."
        ay "Two lovers half-submerged in public bathwater, forced to keep our chests underneath the water to stop our nipples from getting hard."
        s "I’m too tall to be able to do that."
        ay "Yeah, you’re kind of big for a Japanese man."
        ay "Meanwhile I’m the ideal [teenage]girl. A perfectly-sized specimen for you to experiment with. "
        ay "Want to conduct an experiment together, Sensei?"
        s "A sexual experiment?"

        scene ayanesenseibath11
        with dissolve

        ay "How about an emotional one instead?"
        s "How does your size have anything to do with your emotions?"
        ay "Shhh, don’t think too much about it."
        ay "What we’re going to do is ask each other one question that we’re forced to answer and can’t talk our way out of."
        s "This sounds like a very dangerous experiment. "
        ay "Don’t worry. My question for you will be easy. I’ll even go first."

        scene ayanesenseibath12
        with dissolve

        ay "Does that work for you, Sensei?"
        ay "It’s just an experiment, so there’s a chance nothing comes of it."
        ay "But there’s also a big chance that we could discover something amazing about one another."
        ay "And I, for one, want to know everything I possibly can about you since we’ll be spending our entire lives together."
        ay "I hope."

        "I might be in a bit of trouble if Ayane’s question is actually whether or not I want to spend my entire life with her."
        "I mean, I’m not exactly {i}opposed{/i}. At least not right now."
        "But that’s a huge commitment for someone her age and answering incorrectly might wind up hurting her."
        "So...let’s just hope the question is something a little easier than that."

        s "Fine."
        s "Ask away."
        ay "Okay~ But remember, you need to be completely honest. "
        s "Yeah, yeah. I’ll be honest."

        "Probably."

        s "Go ahead, then."
        s "Ask me anything."
        ay "…"
        ay "Okay."

        scene ayanesenseibath13
        with dissolve

        ay "…"

        "Ayane goes quiet for a minute."
        "I feel her back press up against mine a little harder, like she’s trying to absorb my warmth in order to feel comfortable or something corny like that."
        "That sounds like a thing Ayane would do."
        "I wonder if this question is really going to be easy, though?"
        "It seems like she’s having a hard time getting it out."

        ay "Sensei..."
        ay "Do you..."
        ay "Um..."

        scene ayanesenseibath14
        with dissolve

        ay "…"
        ay "Do you think I’d be a good mom?"
        s "…"
        ay "…"
        s "That’s your question?"
        ay "Yeah. And you have to answer it. Those are the rules."
        s "Can I ask why you’d ask something like that?"

        scene ayanesenseibath15
        with dissolve

        ay "If that’s what you want to waste your question on."
        s "Hm..."

        if ayanelust10 == True:
            s "No. I think I’ve got another question for you instead."
            s "So let me answer yours first."
            ay "Mhm...I’m waiting."

        else:
            s "Get back to me on that. I’m not sure if I’ll be able to think of something yet."
            ay "Roger. Answer mine then, please."

        "Ayane as a mom, huh?"
        "I’m hoping she doesn’t mean {i}now{/i}."
        "Because if she even jokes about being pregnant again, I will drown her and my unborn child in this very bath."
        "Just kidding."
        "I’d never drown Ayane {i}or{/i} an unborn child of mine."
        "In fact, I don’t even want to think of having a child right now, so I’ll isolate Ayane’s personality and completely take myself out of the equation for this question."

        s "I think..."
        s "Yeah. "
        s "I think you’d be a good mom."

        scene ayanesenseibath16
        with dissolve

        ay "Really?! You mean that?"
        s "Obviously not right now, but when you’re ready."
        s "You’re one of the most caring people I’ve ever met. You’re confident. Optimistic."
        s "You’re a lot of great qualities wrapped into one tiny person."
        s "And sure, you’re incredibly obnoxious a lot of the time and almost unbearably clingy-"
        ay "Yeah. Those are both true. I know."
        s "Even though they’re true, though, I think you’d be a good mother."
        s "The kind that would devote her entire life to her kids."

        scene ayanesenseibath17
        with dissolve

        ay "Well I’d obviously have to devote {i}some{/i} of myself to you since you’d be their daddy, but I think you’re mostly right."
        ay "There’s nothing worse for a kid than a parent who doesn’t seem to care about them...So if I ever have a baby, I’ll make her the center of my world."
        ay "I’ll use all of my money to buy her anything she wants and teach her karate and let her dye her hair any color she can think of."
        s "You’ve already decided that your imaginary child is going to be a girl?"
        ay "Of course. Boys are harder to take care of. Probably."
        ay "I don’t know. I’ve never been a mom before."
        ay "But I want to someday. "
        ay "I want to start a big family and live happily ever after in some cottage outside of everything."
        ay "I’d wait for you to come home every day and have dinner on the table when you get there."
        ay "And after you'd finish eating, I’d bring you upstairs and give you a blowjob on the bed while our kids watch TV."
        s "I like that last part a lot."

        "Not so much the part about the kids, though."

        scene ayanesenseibath18
        with dissolve

        ay "Heheh~ I figured you would."
        ay "We’re gonna have to be careful about how much we have sex or we’ll wind up having more kids than we can take care of."
        ay "I think even I might pull the plug after like, nine."
        s "You should worry about taking care of {i}one{/i} first before setting your cut-off at nine."
        ay "Hurry up and give me one so I can try it out, then."
        s "Absolutely not."
        ay "Pleeeeeeease?"
        s "Ayane."

        scene ayanesenseibath19
        with dissolve

        ay "I’m kidding, I’m kidding~"
        ay "If you think we should wait, then we’ll wait."

        scene ayanesenseibath20
        with dissolve

        ay "I’m kind of curious about what your question for me will be now, though."
        ay "Do you actually have something fun? Or are you going to take the easy way out and ask me about the reason for my question?"
        s "Hmm..."

        if ayanelust10 == True:
            s "Actually, there is something I’ve been meaning to ask you."
            ay "Oh?"
            s "I wouldn’t exactly call it “fun” though."
            ay "…"
            s "…"

            scene ayanesenseibath21
            with dissolve

            ay "Oh..."
            ay "I...think I know what it is."
            s "You didn’t expect to just avoid this conversation forever, did you?"
            ay "No but...I didn’t really expect you to bring it up after I told you I’d answer {i}anything{/i} you want."
            ay "Like, literally anything."
            s "Getting you to talk about things that are troubling you is hard enough as-is."
            s "I might as well use this opportunity to see why you’ve been acting fine despite literally breaking at the beach."
            ay "Were you really worrying that much?"
            s "Call it worry. Call it curiosity. Call it whatever you want."
            s "But you have to answer it."
            ay "…"
            ay "Okay, but..."

            scene ayanesenseibath22
            with dissolve

            ay "I’m going to hug you while I talk about it so you can’t run away."
            s "Why would I run away from a question that I asked you?"
            ay "Because I’m an idiot who almost ruined your life and I don’t want you to remember that and start hating me."
            s "I don’t hate you, Ayane. I’m just a little confused about what happened back there."
            s "I’ve never seen you look so scared before."

            scene ayanesenseibath23
            with dissolve

            ay "I’ve never been that scared before."
            ay "I finally get to be together with you after all of these years as long as we keep it a secret."
            ay "Of course I’d be afraid that someone finding out about it would ruin that."
            ay "Not to mention that a girl I’ve known since I was little is the one who found us."
            ay "And that she just forced her way in like I didn’t even care about it."
            s "Did you care about it?"

            scene ayanesenseibath24
            with dissolve

            ay "Of course!"
            ay "My biggest fears in the entire world are you leaving me for someone else and caterpillars."
            s "You’re afraid of caterpillars?"
            ay "Yes! But that doesn’t matter right now."
            ay "Kirin’s really pretty and petite and flirty and funny and a bunch of other stuff."
            ay "And yeah I’m all of those things too, but what if you like her more for some reason?"
            ay "You didn’t even try to stop her from touching you, so that made me even more nervous."
            s "I didn’t really think I was in the position to be calling any shots there."

            scene ayanesenseibath25
            with dissolve

            ay "I know that...and I’m not blaming you."
            ay "It’s my fault for being so careless and not even checking to see if anyone was in the room."
            s "I still don’t understand why she was there in the first place."
            ay "Neither do I, but she {i}was{/i} and she caught us and I was worried that this was all going to end right there."
            ay "Also, she said some really mean things to me while it was happening and I didn’t know how to handle it."
            s "What did she say to you afterwards? You guys went outside to talk, didn’t you?"
            ay "Just some stuff about how she wouldn’t tell anyone and that it wasn’t a big deal."
            ay "It definitely felt like a big deal to me, though."
            s "Have you talked since then?"

            scene ayanesenseibath26
            with dissolve

            ay "Not at all. She hasn’t even tried reaching out."
            ay "And I’ve been really on edge because I know she could tell anyone whenever she wants."
            ay "And Kirin is pretty popular so people would definitely listen to her as well."
            ay "Your career would be ruined and my dad would find out and probably force me to get homeschooled or something."

            scene ayanesenseibath27
            with dissolve

            ay "All because I was too stupid and too horny to think about making sure we were safe."
            ay "It was a stupid idea and I hate that we had to go through that during a time that was so special and sweet."
            ay "All I want is for you to like me. Any time something threatens that I’m probably going to freak out, so sorry in advance."

            scene ayanesenseibath28
            with dissolve

            ay "Also, I’m pretty sure Kirin being there made you harder than normal and that made me angry."
            s "To be fair, you were also extremely turned-on during that exchange."
            ay "I know."
            ay "I’m pretty sure I came on her hand. I can’t even look at her anymore."
            s "Then don’t."
            s "Kirin’s obviously got it out for you for whatever reason, so staying away from her is probably best for both of you."

            scene ayanesenseibath29
            with dissolve

            ay "It’s so weird, though..."
            ay "I thought the two of us were friends."
            ay "I have no idea why she’d do something like that when she’s well aware of how I feel about you..."
            s "Some people are just...toxic, I guess."
            ay "I guess..."
            ay "I don’t know. It’s a giant mess. I wish it never happened."
            ay "I’ll be more careful from now on, I promise."
            s "Your idea of being careful is being naked together in a public bathhouse?"
            ay "…"

            scene ayanesenseibath30
            with dissolve

            ay "Baby-steps."
            ay "I’ll get there."
            s "…"
            s "I’m sure you will."

            scene black
            with dissolve2

            "Ayane and I sit in the bath for a little while longer and return to our original positions."
            "She gets embarrassed about crying in front of me and needs to constantly splash water onto her face in order to get rid of her tears."
            "Of course, the water in the bath is extremely hot, so by the time we’re out, her face is as red as a tomato."
            "But thankfully-"
            "The cold air of an encroaching winter is able to return her to normal on the way home."

            $ renpy.end_replay()
            $ ayane_love += 1
            $ ayanedorm25 = True
            stop music fadeout 5.0

            "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
            "………"
            "……"
            "…"

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

        else:
            s "I think I’m going to take the easy way out."

            scene ayanesenseibath18
            with dissolve

            ay "Booooooring."
            ay "I don’t mind answering it, though."
            ay "Buckle up your seatbelt for some of Ayane Amamiya’s story-time."

            scene black
            with dissolve2

            "Ayane goes on to talk about the relationship she had with her mom when she was little."
            "I keep expecting her to tear up or...get emotional or anything while discussing her past, but it’s an overwhelmingly positive story."
            "She goes over how her mother always placed her at the center of the world. How she’d do anything to make her feel safe."
            "Or loved."
            "She talks about how gently she’d tuck her in before bed...how she’d help her pick out clothes when they went shopping-"
            "And even smaller things like how much milk she’d put in her cereal or the shape of her crooked smile."
            "Luckily for Ayane, her smile is perfectly straight."
            "And even though I could not see it with our backs pressed together, I could tell she was wearing one throughout her entire rant."

            $ renpy.end_replay()
            $ ayane_love += 1
            $ ayanedorm25 = True
            stop music fadeout 5.0

            "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
            "{i}You are unable to have sex when returning to the dorm because Sana is there!{/i}"
            "………"
            "……"
            "…"

            if day < 6:
                jump endofweekday
            else:
                jump endofsat
    else:
        ay "Hello! One ticket for the female side and one for the male side, please!"
        i "Okay. Thank you for not doing anything inappropriate."
        s "Woah. Why can I see her name? Is she going to be a major character?"
        i "No. I am a trash person and you should not care about me."
        ay "Here is your ticket, Sensei. Please enjoy your bath all by yourself."
        s "Thank you, Ayane. You do the same."

        $ renpy.end_replay()
        $ ayane_love += 1
        $ ayanedorm25 = True
        stop music fadeout 5.0

        "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
        "{i}You both enjoy private baths because co-ed bathing is gross!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label ayanedorm30:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ayane_love >= 5 and ayanedorm5 == False:
                jump ayanedorm5
            if ayane_love >= 15 and ayanedorm10 == True and ayanedorm15 == False:
                jump ayanedorm15
            if ayane_love >= 20 and dojo20 == True and ayanedorm10 == True and sanadorm15 == True and day == 6 and ayanedorm20 == False:
                jump ayanedorm20
            if ayane_love >= 25 and day != 4 and dojo25 == True and ayanedorm25 == False:
                jump ayanedorm25
...
```