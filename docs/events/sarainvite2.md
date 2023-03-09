# A Mostly Empty Home
Sara event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sarainvite2&go=Go)



## Event preconditions
✅Event "[Sara: Third Wheel](./sarainvite1.md)" is completed (event=sarainvite1)

✅Event "[Sara: A Woman's Heart](./saradate1.md)" is completed (event=saradate1)



## Next events
None

## Event properties
* ID: sarainvite2
* Group: Sara
* Triggered by label: sarainvite
* Triggered by branch label: inviteover

## Event code
File: \game\SaraEvents.rpy
Code:
```python
...
label sarainvite2:
    play sound "phonebeep.wav"

    "I tap on Sara’s name in my phone and wait for her to answer."
    "The last time she came over ended in an unprecedented success, so I’m hoping for more of the same this time."
    "Well, in the broad sense at least. I’d much prefer if I actually got to spend time with {i}her{/i} instead of her and my [niece]."

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    sar "Hey, [saramaster]~ What’s up?"
    s "Not much. What are you doing?"
    sar "Oh you know. A little of this. A little of that. "
    sar "I’m off tonight~"
    s "Are you actually off or are you just going to make Sana cover for you when I invite you over?"
    sar "Does the answer to that really matter?"
    s "I guess it doesn’t."
    sar "Hehehe~ Good. Then I’ll be right over."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 3.0

    "………"
    "……"
    "…"

    scene sarafirstinvitesex1
    with dissolve
    play music "asobeatsex7.mp3" fadein 5.0

    "A mostly empty home is what I find after opening the door."
    "Empty in the sense that Ami is nowhere to be found and won’t be returning any time soon."
    "She sent me a text on the way home that her and some of the others were going to the movies tonight."
    "But it’s not like it’s {i}entirely{/i} empty in the fact that-"
    "Well, I’m here."
    "And soon someone else will be here as well."
    "And there’s also the furniture and...the walls and..."
    "Everything that makes a house a house."
    "I don’t know what I’m talking about."
    "I’m not great at thinking when I’m alone."

    if bonus == True:
        "It’s one of the many reasons I prefer the company of others."
        "The bulk of those reasons being unsavory but-"
        "Well, I’m sure you’ll have a chance to see exactly what I mean by that by the end of the night."
    else:
        "I always wind up just endlessly scrolling through Facebook and liking the pictures of pretty girls who will never talk to me."

    play sound "doorbell.mp3"

    sar "Hellooooo~ Special delivery! One beautiful mom!"

    "What an excellent delivery. There should be a service that specializes in just that."

    s "You can let yourself in."

    "I shout to Sara from the living room."
    "The front door is thin so I don’t doubt that she’ll be able to hear me."

    play sound "dooropen.mp3"
    scene sarafirstinvitesex2
    with dissolve

    sar "Why hello there. Did I keep you waiting long?"
    s "Not long at all. I only got here a few minutes ago myself."
    sar "Is that so?"
    sar "Where’s Ami?"
    s "Not here."

    scene sarafirstinvitesex3
    with dissolve

    sar "You mean we have the place to ourselves tonight?"
    s "It certainly appears that way. The girls are out watching some action movie or something."

    scene sarafirstinvitesex4
    with dissolve

    sar "Excellent...excellent."
    sar "You must have been upset that you didn’t get me all to yourself last time, huh?"
    s "I guess so. Which is weird because, if anything, I figured you would be the one to be upset."

    scene sarafirstinvitesex5
    with dissolve

    sar "You say that as if I like you or something. I wonder what gave you that idea?"

    if sarasex == False:
        s "It’s kind of hard to not get that idea when you’ve cornered me in your room and asked me to lock the door before."

        scene sarafirstinvitesex6
        with dissolve

        if bonus == True:
            sar "Yeah, silly me for getting horny and thinking you might wanna fool around. "
            sar "That really wasn’t my finest moment, you know. I was so embarrassed when you left that I think I even cried."
            sar "I couldn’t even [masturbate] that night. That’s how much you hurt my feelings."
            s "I didn’t mean to hurt your feelings. It’s just..."

            scene sarafirstinvitesex7
            with dissolve

            sar "Yeah, yeah. It’s just that my daughter was passed out several rooms away and you didn’t want her to catch you screwing her mom."
            s "Bingo."
            sar "I’m sorry for coming on so strong in the first place."
            sar "I’m not really the best when it comes to hiding my feelings...so if I ever want something I just kinda reach out and take it."
        else:
            sar "Yeah, silly me for thinking it was appropriate to hug my daughter's teacher. "
            s "Let that be a lesson to you, Sara. A lesson in............................"
            s "Not hugging whoever you think about hugging."
            sar "Ugh."

        scene sarafirstinvitesex6
        with dissolve

        sar "Of course that method doesn’t normally work if someone on the other side isn’t willing, though."
        s "You say that as if it’s something that happens pretty frequently."

        scene sarafirstinvitesex8
        with dissolve

        sar "Not at all."

        if bonus == True:
            sar "It’s been a really long time since I’ve been with a guy. "
        else:
            sar "It’s been a really long time since I’ve hugged a guy. "

        sar "Some things happened and I just kind of...lost interest."
        sar "But something about you makes me want to change that."
        sar "I wonder what it is?..."

        "So do I. "
        "There’s really no reason to like someone like me."
        "I’ve got no special qualities. And I’m mediocre at best when it comes to talking to people."
        "But yet here we are, alone in my house and with another opportunity to take things further."

        sar "Listen..."
        sar "I understand if you still don’t feel comfortable moving this relationship along."
        sar "But, on the off chance that you maybe...you know...want to spend some quality time together, I am {i}more than willing{/i}."
        sar "It’s up to you..."

        "What should I do?"
        "If I turn Sara down now, I don’t think I’ll ever get another chance with her."
        "This decides everything."

        menu:
            "Stay friends":
                s "Sara..."
                sar "I don’t like that face."
                sar "It makes it look like I’m going to be rejected again."
                s "…"
                sar "…"

                scene sarafirstinvitesex9
                with dissolve

                sar "Hah..."
                sar "And boys are always saying how {i}girls{/i} are the confusing ones..."

                scene sarafirstinvitesex10
                with dissolve

                if bonus == True:
                    sar "So what? We stay friends? Not even any foreplay?"
                else:
                    sar "So what? No hug?"

                s "It’s probably for the best. "
                s "Ami seems to like you and there's still the issue of your daughter being in my class."
                sar "Those are both good reasons."
                sar "You obviously wouldn’t want to risk relationships you already have for a chance at one you don’t yet."
                sar "It’s kind of sad, though."
                sar "I think you and I could have been really happy together."
                s "…"
                sar "…"

                scene sarafirstinvitesex5
                with dissolve

                sar "But...I guess that’s nothing more than just a thought in the end."
                sar "Wanna go for a walk or something?"
                s "…"
                s "Sure."

                scene black
                with dissolve2

                "Sara and I leave the house as friends."
                "Nothing more."
                "And chances are there will never be any more."
                "I’ve destroyed the precious thoughts of us that had been swimming in her head since the first time I rejected her."
                "I’ve destroyed any chance for those thoughts to ever be more."
                "And yet-"
                "She continues to smile."
                "She’s stronger than she makes herself out to be."
                "But I guess that’s just how moms are."

                sar "Welp! I think that’s gonna be it for me~"
                s "Leaving already?"
                sar "Yeaaaaah. I’m gonna head back to the bar and give Sana a night off."
                sar "It was nice chatting with you, though...Sensei."
                s "Of course. It was nice chatting with you as well."
                s "I’ll see you soon."
                sar "Yup!"
                sar "See you soon~"

                "Sara heads back to her home-"
                "And I head back to mine..."

                "{i}Somewhere far away, a red string snaps.{/i}"
                "{i}Sara is no longer romanceable.{/i}"
                "{i}You will still be able to view some of her future scenes, but will be locked out of others.{/i}"

                $ renpy.end_replay()
                $ sara_love += 1
                $ sarainvite2 = True
                stop music fadeout 5.0

                "{i}Regardless, her affection has increased to [sara_love]!{/i}"
                "………"
                "……"
                "…"

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

            "Take things further":
                s "I was just waiting for a better opportunity."
                s "I’m more than willing to start moving things forward with you now that we’re alone."

                scene sarafirstinvitesex11
                with dissolve

                sar "But what if Ami comes home? How will you explain the strange noises coming from your bedroom?"

                if bonus == False:
                    s "Ami knows about the noises I make when I hug."
                    sar "Okay. Good."
                    s "But...just in case-"

                s "I’ll just pretend nothing ever happened."
                sar "She seems pretty dedicated to you. I’m not really sure she’ll let you get away with that."
                s "Well we’ll cross that bridge when we come to it, won’t we?"

                scene sarafirstinvitesex12
                with dissolve

                sar "And you’re sure you want to cross it with someone like me?"
                s "I would have turned you down again if I wasn’t."
                sar "I don’t think I would have handled a second rejection very well. Things like that can kill a girl, you know?"
                s "That seems a little drastic..."

                scene sarafirstinvitesex5
                with dissolve

                if bonus == True:
                    sar "Who cares? You said yes so stop making me wait and fuck me already. Jeez."
                else:
                    sar "Who cares? You said yes so stop making me wait and hug me already. Jeez."

                s "You don’t have to tell me twice..."

    else:
        s "It sure as hell can’t be the fact that you’re borderline-obsessed with me, now could it?"

        scene sarafirstinvitesex13
        with dissolve

        sar "O-Obsessed?! I’m not obsessed!"
        sar "That’s really mean!"
        sar "We’re supposed to mutually like each other! You’re supposed to want to hold my hand and stuff!"

        scene sarafirstinvitesex14
        with dissolve

        sar "Love me more or I’ll hit you."
        s "I can’t imagine you hitting me would do much."
        sar "I wouldn’t be so sure, Sensei. I got into tons of fights in [high_school]. I’m vicious when I want to be."
        sar "I’ll scratch you and...pull your hair and..."

        scene sarafirstinvitesex15
        with dissolve

        if bonus == True:
            sar "Shoot...now I’m turned on..."
            s "Already? I didn’t even do anything."
            sar "It’s the scratching and stuff. It made me think of sex."
            s "Don’t most things in general make you think of sex?"

            scene sarafirstinvitesex16
            with dissolve

            sar "I blame you and your perfectly-sized penis. "
            sar "I’m addicted now and it’s all your fault."
            s "Is that supposed to be an insult?"

            scene sarafirstinvitesex17
            with dissolve

            sar "It was, but I didn’t really think it through beforehand. It definitely sounds more like a compliment when I say it out loud."
            s "Well, thank you for the insult. It was quite generous."

            scene sarafirstinvitesex18
            with dissolve

            sar "Anything for you, [saramaster]~"
            sar "As long as you’ll continue to have me, I’ll be happy to make you feel good about yourself...or just {i}good{/i} in general whenever you like."
            s "Whenever I like? I'm not sure if you’ve realized this but I have a pretty high sex drive."
            sar "I'm not sure if you’ve realized this but so do I."
            s "So if I call you at 3:00 in the morning and ask you to come over, will you come?"
            sar "I probably won’t wake up, but I can give you a spare key to my apartment in the event that you wanna come fuck me in my sleep."
            s "And if I call you while I’m at[school]?"
            sar "I’ll come bring Sana lunch and then suck you off in the bathroom."
            s "Are you an angel?"
            sar "I’m whatever you want me to be~"
            sar "All I ask is that you buy me candy and cuddle with me and lick my pussy every once in a while."
            sar "That’s all~"
            s "Can I just...lick more instead of buying you candy?"
            sar "Depends on how much effort you put into it."

            scene sarafirstinvitesex19
            with dissolve

            sar "Really, though...Thanks for not being weirded out by how quickly I came onto you and stuff."
            sar "The first time we had sex I couldn’t help but feel like I was rushing into things."
            sar "I half-expected you to just turn around and leave, but nope."
            sar "You took me right then and there. You didn’t even care that I was so drunk that I was about to pass out."
            s "Okay, saying it like that makes me sound like some sort of creep."
            sar "Nononono. You’re not a creep at all. Just horny. That’s how boys are."
            sar "I’m not going to hold that against you. I put myself out there and you took me. "

            scene sarafirstinvitesex20
            with dissolve

            sar "And also gave me what was probably my hardest orgasm ever in the process. "
            sar "Everyone wins! Yay!"

            "Sara is too cute."
            "So cute that she shouldn’t be allowed to exist."
            "She truly is a [teenager] trapped in a...slightly older woman’s body."
            "The way she winks at me...speaks with sincerity...suggests giving me blowjobs in the[school] bathroom..."
            "All of these things and more make me realize just how special she is."
            "So if buying candy, cuddling, and licking her pussy is all it takes to keep her by my side, I have absolutely no reason not to."

            s "Sara."
            sar "[saramaster]."
            s "Why are we still in the living room?"
            sar "Because you haven’t picked me up and carried me to the bedroom yet~"
        else:
            sar "Probably hug you or something."
            s "Fuck yeah."

    if bonus == True:
        jump sarainvsexx
    else:
        scene black
        with dissolve

        "Sara and I hug for almost seven minutes before I remember that I have something to do."

        s "I have something to do."
        sar "Okay."

        "Sara leaves."

        $ renpy.end_replay()
        $ sara_lust += 3
        $ sarainvite2 = True
        $ sarasex = True
        stop music fadeout 10.0

        "{i}Sara’s lust has increased to [sara_lust]!{/i}"
        "{i}You can now choose between affection and lust when inviting her over!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label sarainviteaff:
    scene sarainvitegen
    with fade

    "The two of us decide to spend the night together...not really doing anything."
    "But it's a pleasant form of nothingness."
    "Sara lays down next to me on the bed and moves closer."
    "Her eyes lock onto mine and only stray from them in short bursts."
    "But, for the most part, I'm all that she focuses on."
    "It feels a little uncomfortable at first given that neither of us are saying much."
    "But once that initial unease subsides, it becomes overwhelmingly apparent to me that this might just be the most comfortable I've felt in a very long time..."

    scene black
    with dissolve

    "Sara falls asleep next to me and I can't find it in myself to wake her up until Ami gets home."
    "It's a little awkward having to explain to her that Sara was literally {i}just{/i} sleeping and that nothing else happened at all, but she manages to buy it somehow."
    "Maybe it's due to how much she likes her or just...the fact that Sara could barely even keep her eyes open on the way out of the house but-"
    "Well, somehow or another, everything seemed to work out in the end."
    "It was a good night."

    $ sara_love += 3
    stop music fadeout 5.0

    "{i}Sara's affection has increased to [sara_love]!{/i}"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sarainvitedoggy:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump sarainvitedoggyx
    else:
        $ sara_lust += 3
        stop music fadeout 5.0

        "{i}Sara's lust has increased to [sara_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label sarabjreplay:
        scene black
        with dissolve
        play music "calmbar.mp3"
        play sound "dooropen.mp3"

        "I head over to Sara's place and the two of us get to talking about a number of things."

        if bonus == True:
            "Most of those things are of sexual nature so, before we know it, we wind up inside of her apartment and my penis winds up inside of her mouth."
            jump sarabjreplayx
        else:
            "Most of those things involve hugging, so we decide to do that for a couple hours."

            $ sara_lust += 1
            stop music fadeout 4.0

            "{i}Sara's lust has increased to [sara_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label sarainvitemissionary:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump sarainvitemissionaryx
    else:
        $ sara_lust += 3
        stop music fadeout 5.0

        "{i}Sara's lust has increased to [sara_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label saradate10:
...
```

## Code that triggers this event
File: \game\SaraEvents.rpy
Code:
```python
...
label sarainvite:
    if sarainvite1 == False:
        jump sarainvite1
    if sarainvite1 == True and sarainvite2 == False:
        jump sarainvite2
...
```