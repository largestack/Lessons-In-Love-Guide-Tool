# Sayonara
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=thirdreset3&go=Go)


Part of event chain [Backwards Dancing](./thirdreset2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Sana: Sweet Vermouth](./bar45.md)
* [Sana: The Complete Absence of Everything](./sanadorm45.md)
* [Main: Food Groups](./day351.md)

## Event properties
* ID: thirdreset3
* Group: Main
* Triggered by label: thirdreset2

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label thirdreset3:
    scene picnicinspace1 with flash
    play music "iloveyou.mp3"

    "I find Maya leaned up against a flowerbed, clasping a canned beverage and staring off at the sky- likely wondering when I’m going to get here."
    "Little does she know, I’m right beside her."

    m "Quicker than usual this time."

    "Or she already knows and was just trying to look cool."

    s "Was I?"
    s "I don’t even really remember the trip here, to be honest."

    scene picnicinspace2
    with dissolve

    m "That’s to be expected."
    m "I was the same way the first...however many times it took for me to become comfortable with it."
    m "It’s not really possible to give you an exact number on account of me...not remembering those times."
    s "And the picnic?"

    scene picnicinspace3
    with dissolve

    m "A little present, I suppose."
    m "To congratulate you on making it where no other Sensei has ever made it before."
    m "It’s quite cold up here in the winter, isn’t it?"
    s "Why prepare a picnic if you didn’t know how long I was going to be, though?"
    m "I figured I could just eat everything myself if you didn’t show up within a reasonable amount of time."
    m "I’m slightly disappointed that you did, now that I’m actually thinking about it."
    m "But, on the bright side, we can get food wherever we want on account of everyone else being gone."
    s "I’d suggest taking a trip to the maid cafe before things start to go down, but I just don’t think it would be the same without the flavor beam."

    scene picnicinspace4
    with dissolve

    m "I can guarantee you that the flavor beam does not make even a tenth of the impact you think it does."
    s "But that implies it does make {i}some{/i} difference."
    m "It’s a beam of flavor. Of course there will be some difference."
    s "Do you want me to try beaming the food?"
    m "Is this how things are going to be tonight? Because if it’s just going to be a party, we might as well get the reset out of the way now."
    s "Hey, you’re the one who laid out food and made it a special occasion. I’m just trying to have a good time."
    m "Well then at least sit down. There’s more than enough room on the blanket for the two of us."

    if bonus == True:
        s "I think I’d prefer being {i}under{/i} the blanket with-"
        m "Five more seconds and I’m eating everything myself."
        s "Fine, fine. I get it."

    scene black
    with dissolve2

    "I walk past Maya, avoiding a trash can and bringing myself closer to the ground to take a spot on the blanket."
    "It’s-"

    scene picnicinspace5
    with dissolve

    s "Wait, did you get this blanket from my house?"
    m "…"
    m "Possibly."
    s "Are we going to get it back? I think Ami really likes this blanket."
    m "Possibly."
    m "I’ve never brought a blanket to the apocalypse before."
    m "I suppose we’ll just have to see how things pan out."
    s "You could have just brought your own blanket."
    m "Why would I do that if there was a chance I wouldn’t get it back?"
    s "Maya...are you actually a bad person?"
    m "Please. You are the last person I want to hear something like that from."
    m "Now, are you going to eat? Or are you just going to sit here and ask me questions about blankets for the next several hours?"
    s "I’m not really hungry."
    m "…"
    s "Also, why are you hugging a watermelon?"
    m "It’s a good melon."
    m "Can we talk about the world now?"
    s "That’s such a Maya thing to say."

    scene picnicinspace6
    with dissolve

    m "I’m glad that you’re still here, but I have to say that I really wouldn’t mind if you’d lose the snarky pokes at how predictable I am under certain pretenses."
    s "That’s the closest you’ve ever come to saying you love me."
    m "I’m trying to be serious here."

    scene picnicinspace7
    with dissolve

    m "I have absolutely no idea what’s going to happen after tonight."
    m "Maybe we’ll get ten more students. Maybe {i}our{/i}[school] will fall into an inexplicable sinkhole."
    m "There’s no way of knowing."
    s "I wouldn’t mind ten more students, but I highly doubt we’d be able to fit them into the classroom."
    m "I’d like to formally urge you to {i}not{/i} think about things like that for now and, instead, think about what you’re going to do if something goes wrong with someone you already know."
    s "What do you mean?"

    "Maya stops talking for a moment and takes a bite out of a slice of pre-cut watermelon."
    "She washes it down with a quarter-bottle of green tea before finally speaking again."

    m "We’ve talked before about what you’d do if {i}I{/i} were to suddenly undergo a dramatic change, correct?"
    s "I think so. About whether or not you’d still be the same person afterward and all of that."
    m "Right."
    s "Do you think that’s going to happen?"
    m "I don’t know what’s going to happen. I already told you that."
    m "But I do know that there have been several times as of late where I’ve been forced to recall certain things that I’d much prefer to stay buried."
    s "Like what?"
    m "Well, Noriko’s presence drudges up a number of bad memories, as I’m sure you've ascertained."
    m "But there was another occurrence recently, during the test of courage to be specific, that made me come to terms with my existence not being as permanent as it may have seemed."
    s "During the dorm war?"
    s "I wasn’t around for your contest, so I don’t really know how it went."
    m "And I’m not going to {i}tell{/i} you how it went as it would only further complicate things."
    s "That sounds rough considering how complicated things already are."

    scene picnicinspace8
    with dissolve

    m "It does, doesn’t it?"
    m "Don’t get me wrong, I’d much prefer to remain exactly where I am."
    m "I’m not very fond of the concept of just...not existing."
    m "So, when we do this tonight, I’m going back to the original method of hugging you and not attempting something childish like holding your hands instead."
    s "Bring it on."

    scene picnicinspace5
    with dissolve

    m "Please don’t sound that excited or it’s going to be extremely weird for me."
    s "It’s already extremely weird given our relationship."
    m "Yes, yes. We dislike each other immensely."

    scene black
    with dissolve2

    "We spend the next hour or so watching stars pass overhead."
    "It could have been more than an hour, though."
    "There’s really no good way of telling considering all of the clocks have stopped and our phones don’t have service."
    "I wonder if the sun would come out if we waited long enough?"
    "Probably not."
    "If time isn’t moving, I highly doubt the sun is."
    "I wouldn’t mind things getting a little warmer for a bit, though."

    scene picnicinspace9
    with dissolve2

    m "So, now that this has become somewhat of another tradition for us, albeit one that has only made it to the highly unimpressive total of three-"
    m "Is there anything else you’d like to ask me?"
    s "I’m surprised you’re still giving me the opportunity after revealing that you can’t really...reveal too much without breaking me."
    m "Just giving you the opportunity to ask certain things doesn’t mean I have to answer them truthfully, if even at all."
    s "That doesn’t really convince me that I want to ask you anything."

    scene picnicinspace10
    with dissolve

    m "Then I suppose you should close your eyes and-"
    s "Wait, wait, wait. Hold on."
    s "I’m sure I can think of something."
    s "Uhh..."

    menu thirdresetroof:
        "What happened with you and Noriko?":
            s "Can you tell me more about what led to you hating Noriko as much as you do?"

            scene picnicinspace11
            with dissolve

            m "Really? {i}That{/i} is what you’re going to ask me about?"
            s "I think it’s a pretty good question."
            m "It’s a fine question I guess, but it’s not something I particularly enjoy talking about."
            m "She’s just an overall bad person."
            s "Why, though?"
            s "She’s been nothing but nice to me and everyone else since she got here."
            s "Sure, she did say one questionable thing about {i}you{/i}...but it’s not like you haven’t done the same on...even more occasions."

            scene picnicinspace12
            with dissolve

            m "Hah..."
            m "You wouldn’t understand if I explained it to you."
            s "You have literally explained resetting time to me and that seemed to turn out okay."
            m "I can assure you that my distaste for that girl is even harder to explain."
            m "Just ask me about something else."

            $ reset3q1 = True

            jump thirdresetroof

        "How do you feel about birds?":
            s "How do you feel about birds?"

            scene picnicinspace11
            with dissolve

            m "…"
            s "…"
            m "Excuse me?"
            s "Just...birds in general."
            m "Is this like, some sort of compatibility test or something?"
            m "You don’t think this is a date, do you?"
            s "I’m just curious."
            m "…"
            m "They’re...fine?"
            m "I don’t know what you want me to say here."

            $ reset3q2 = True

            jump thirdresetroof

        "When can I try to do this?":
            s "When can I try to do this?"

            scene picnicinspace13
            with dissolve

            m "Try what?"
            m "Resetting?"
            s "Yeah."
            s "You’ve said that anyone can do it before."
            s "When do I get to take a stab at it?"

            scene picnicinspace11
            with dissolve

            m "It’s something that needs to be approached with a little more seriousness than just “taking a stab at it.”"
            m "I’m sure you’ll have your chance whenever I’ve overstayed my welcome and you’re forced to wait for somebody else on the rooftop."
            s "That...actually sounds really lonely."
            m "Yes. It sucks and I wouldn’t wish it upon anyone."
            m "Good luck."
            s "Well thank you very much for all of the encouragement."
            s "I’m proud of you, Maya."
            s "Good job hanging in there."

            scene picnicinspace12
            with dissolve

            if bonus == True:
                m "Please don’t act like some sort of guardian. It’s actually rather disgusting."
                m "Just continue to do as I tell you until one of us ceases to exist."
            else:
                m "If you're so proud of me, why don't you kiss me?"
                s "Because you're my friend and it would make things weird."
                m "Please? Just once. That's all."
                s "No means no, Maya."
                m "I hate the huggy boy world. This is the worst one yet."

            $ reset3q3 = True

            jump thirdresetroof

        "Have you ever watched someone disappear?":
            s "I’ve been wondering, but...."
            s "Have you ever actually witnessed someone disappearing?"

            scene picnicinspace10
            with dissolve

            m "Unfortunately, I have."
            m "Though, it’s been quite some time since it last happened."
            s "Do you mind if I ask who it was?"

            scene picnicinspace14
            with dissolve

            m "It’s happened with multiple people...but the most notable example was probably with Ami."
            m "Since the two of us are roommates, I’ve seen it through mere happenstance on a number of occasions."
            m "Each and every one of them has been horrifying and unforgettable."
            m "I hope you never have to see anything like it."
            m "Especially with someone you care about."
            s "You really love Ami, don’t you?"

            scene picnicinspace15
            with dissolve

            m "…"
            m "I really do."
            m "Though, it’s hard to explain exactly why."
            m "I’m sure it’s the same for you."
            s "It’s probably a lot easier for me to love her since she cooks and cleans for me every day."

            scene picnicinspace16
            with dissolve

            m "Oh, okay. I guess we’re done actually opening up about our mutual feelings for a girl who would likely die for both of us and are just going to make jokes about it."
            s "Of course I {i}actually{/i} love her. There’s just a {i}reason{/i} for me to love her."
            s "For you, it’s just-"

            scene picnicinspace10
            with dissolve

            m "Since when does anyone need a reason to love anyone?"
            m "Love simply {i}is{/i}."
            m "But I’m afraid that topic is far too sappy and devoid of logic for me to go into detail about it."
            m "Ask me something else now."

            $ reset3q4 = True

            jump thirdresetroof

        "I don’t have any more questions" if reset3q1 == True and reset3q2 == True and reset3q3 == True and reset3q4 == True:
            s "I think that’s it for tonight."

    s "Let’s get this show on the road."

    scene picnicinspace17
    with dissolve

    m "Someone has gotten awfully comfortable with the end of the world."
    s "Nah. I’m just really looking forward to the hug I’m about to get."
    m "The hug that you’re only going to get out of absolute necessity."
    s "Is it really a necessity if you’re choosing to do it?"
    m "Yes. Because it will also provide me the peace of mind in knowing that another[school] will likely {i}not{/i} wind up in the ground and-"

    scene picnicinspace18
    stop music

    q "What...is this?..."

    scene picnicinspace19
    with dissolve2

    m "...what?"

    play sound "static.mp3"
    scene picnicinspace20
    with flash
    stop sound
    play music "contemplation.mp3"

    ay "What’s...going on?"
    ay "I thought it was weird that no one was at the dorm when I got back, but..."
    ay "I...I just assumed they were either all at Sensei’s house or...just...I..."
    ay "And...and then my phone wasn’t working, so I just went to sleep and..."
    m "This..."
    m "What?"

    "Ayane somehow manages to find her way onto the roof during the one time I’d never expect her to be here."
    "And, judging by Maya’s reaction, I think it’s safe to say she didn’t expect her here either."

    ay "Is...something happening?"

    scene black
    with dissolve

    "Maya quickly straightens herself out and slaps her cheeks before making her way over to Ayane to..."
    "Actually, I have no idea how she’s going to explain this."

    scene picnicinspace21
    with dissolve

    m "You..."
    m "How did you get here?"
    ay "What do you mean?...I just...walked..."
    ay "I was here earlier with Sensei and..."
    ay "Maya...what’s going on right now?"
    m "This..."
    s "It’s the end of the world."

    scene picnicinspace22
    with dissolve

    ay "Sensei...I know we were making that joke earlier, but...I’m really scared right now and this isn’t the time for-"
    s "It’s not a joke."
    s "It really is the end of the world."
    s "But the world is going to start over."
    s "Hopefully."

    scene picnicinspace23
    with dissolve

    ay "What do you mean hopefully?! Where did everyone go?!"
    m "Ayane...everyone is gone. But they’ll be coming back any minute now."
    m "What I’m more concerned about is how you managed to make it here."

    scene picnicinspace24
    with dissolve

    ay "I told you! All I did was walk..."
    m "But why {i}here{/i}?"
    m "What led you to the roof of the[school] specifically?"
    ay "I..."

    scene picnicinspace25
    with dissolve

    ay "What..."
    ay "What was it again?"
    m "…"
    s "Maya, do you have any idea-"
    m "Yes."
    m "But we don’t have the time to talk about it now."

    scene picnicinspace26
    with dissolve

    ay "I’m so...confused..."
    ay "Why did I come here and..."
    ay "And where is everyone else?"
    m "You’ll see them again in no time at all."
    m "Just think of this all as one elaborate dream."
    m "And, if it ever happens again, we can talk about it a little more."
    ay "A...dream?..."
    s "Just do what Maya says and everything should turn out fine."
    m "Hopefully."
    s "Hopefully."

    scene picnicinspace27
    with dissolve

    ay "I’m really scared, Sensei..."
    s "Would coming a little closer help you feel better?"
    ay "Yeah, but...what about Maya?..."
    m "It’s extremely out of character for me to suggest something like this, but I think a group hug is in order."
    m "We’ll take a moment to catch our breath and then figure out how we’re going to handle this together..."

    scene black
    with dissolve2

    "So that’s what the gameplan is."
    "I can already tell that Maya is just going to go through with the reset once the three of us are in physical contact with one another."
    "I still don’t fully understand how this process works but, if the “proper method” includes a simple embrace, adding one more person to the mix wouldn’t do anything bad, would it?"
    "And...even if it does, there’s always the chance that none of us will ever find out about it."
    "Everything is going to be okay."
    "…"

    scene picnicinspace28
    with dissolve2

    m "Keep your eyes closed, Ayane."
    ay "Okay..."
    ay "I’m using Sensei’s shirt to dry my face, so I wouldn’t really be able to see anything anyway."

    "Ayane claws at my shirt and clips some of my skin in the process."
    "She’s trembling as if she were a dying animal on the side of the road, soaking wet after smacking off the windshield of a car and being tossed into a nearby rain-filled pothole."
    "And I’d like to say that Maya is the complete opposite-"
    "But the truth is that she’s trembling as well."
    "Less like roadkill and more like a very subtle earthquake, though."
    "Like there’s something happening beneath her that’s-"

    ay "Is..."
    ay "Is the ground...shaking right now?"
    m "It’s all in your head."
    m "Sensei, are your eyes closed as well?"
    s "…"
    m "…"

    scene picnicinspace29
    with dissolve

    s "Yeah."

    stop music
    play sound "static.mp3"
    scene 5 with flash
    scene 4 with flash
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene tree3 with flash
    scene happy9 with flash
    scene happy8 with flash
    scene happy7 with flash
    scene happy6 with flash
    scene happy5 with flash
    scene happy4 with flash
    scene happy3 with flash
    scene happy2 with flash
    scene happy1 with flash
    scene picnicinspace30 with flash
    stop sound
    $ renpy.pause(5, hard=True)

    $ renpy.end_replay()
    $ thirdreset3 = True

    jump ayanespecial2

label day351:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
ngk "I’m a new hire."
        s "Can I talk to your manager?"
        ngk "I’d really prefer you didn’t."
        s "I want to talk to your manager."
        ngk "I’m not looking for any trouble, man."
        ngk "Just tell me what it is you’re here to see and maybe we can work something out."
        s "I...don’t know."
        ngk "Gotta give me a little more than that, bud."
        s "No, I just..."
        s "I’m here for...something."
        ngk "Something...round? Shiny?"
        ngk "Maybe something like a Christmas ornament?"
        ngk "It is winter, after all."
        s "No...that’s not it..."
        s "I..."

        play sound "static.mp3"
        scene imissyou18 with flash
        scene journeytothatoneplace7 with flash
        stop sound

        s "A bird!"
        ngk "A bird?"

        play sound "static.mp3"
        scene imissyou19 with flash
        scene journeytothatoneplace7 with flash
        stop sound

        s "No! Not a bird!"
        s "Maya!"
        ngk "Hm..."
        ngk "I did see some girl go up there a little while ago."
        ngk "Walked right past me. Didn’t even say hello."
        ngk "The nerve of some people."
        s "Yes. She is who I’m here to meet. And she can be very rude."
        s "I’ll make sure she comes down and apologizes after we finish resetting the world together."
        ngk "Why reset the world?"
        ngk "Isn’t it kinda nice having everybody gone?"
        ngk "There’s no noise. Everything is free."
        ngk "It’s kinda like paradise."
        ngk "But...then again...I’m a net with a knife nose and a melon mouth, so I don’t really know much about paradise."
        s "Then...can I pass?"
        ngk "I don’t know. {i}Can{/i} you?"
        s "Are we really playing that game right now?"
        ngk "Nope. We’re playing Lessons in Love. A game created by Selebus for the express purpose of saving the world."
        ngk "None of this is actually happening and it’s just all one big simulation."
        s "What?"
        ngk "Oh, nothing."
        ngk "I’ve just been getting really into theorycrafting lately and I’m pretty sure I have everything figured out."
        ngk "Sure, the game’s come out and told me that’s not the case like six hundred times, but there are also all of these recurring themes about perception and-"
        ngk "You know what? Just join the Discord. I’ve got some notes I can share with you on there and you look pretty busy right now."
        s "I just want to go upstairs."
        ngk "What’s stopping you?"
        s "You are, aren’t you?"
        ngk "Dude, just walk past me. I have no legs. What would I even do?"
        s "I didn’t think of that."
        ngk "Well, you’re not really all there right now."
        ngk "Probably a side effect of slowly fading away or something."
        s "Fading away?"
        ngk "Yeah."
        ngk "Seems to me like you might be hanging on by a thread and fighting against whatever forces are trying to make {i}you{/i} disappear as well as everyone else you know."
        ngk "But hey, that’s just a theory."
        ngk "A {i}game{/i} theory."
        ngk "You may pass."
        s "Thank {s}God{/s} you."

        scene black
        with dissolve2

        "Left leg and right leg join forces one final time as they carry my body up the stairs and past the guardian of the top floor."
        "My peripheral vision catches sight of a familiar television program as I ascend and I can’t help but become distracted for a moment."
        "I stop watching when I realize that I don’t know anyone on the screen."
        "One of them did have familiar eyes, though."

        stop music

        "/////////////////////////////////BUFFERING MUSIC..."
        "/////////////////////////////////…"
        "/////////////////////////////////…"
        "/////////////////////////////////UNABLE TO LOAD MUSIC"
        "/////////////////////////////////YOU ARE NOW OUT OF RANGE OF “USER2”"
        "/////////////////////////////////YOU ARE NO LONGER SHARING YOUR SCREEN WITH “USER2”"
        "/////////////////////////////////WOULD YOU STILL LIKE TO CONTINUE?"

        menu:
            "Go to the roof":
                play sound "static.mp3"
                scene smile with flash
                scene frown with flash
                scene smile with flash
                scene frown with flash
                scene smile with flash
                scene frown with flash
                stop sound

                $ renpy.end_replay()
                $ thirdreset2 = True

                jump thirdreset3
...
```