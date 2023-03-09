# Into the Woods
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikalust20&go=Go)


Part of event chain [Torrential Downpour. Child of Man.](./secondbeach10.md)

## Event preconditions
✅Chika lust greater than or equal to 20



## Next events
None

## Event properties
* ID: chikalust20
* Group: Chika
* Triggered by label: chikalust20intro

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label chikalust20:
    if _in_replay:
        play music "asobeatsex2.mp3"

    scene chikawoods4
    with dissolve

    if bonus == True:
        jump chikalust20x
    else:
        c "We can hug, though."
        s "Fuck yeah."

        scene black with dissolve

        "Chika and I get approximately one-thousand hugs from somewhere in the realm of ten-thousand lightning bugs."
        "They try to teach us how to dance."

        $ renpy.end_replay()
        $ chikalust20 = True
        $ chika_lust += 1
        stop music fadeout 5.0

        "{i}Chika’s lust has increased to [chika_lust]!{/i}"

        if dormwarfloor1win == True:
            jump secondbeach11floor1
        else:
            jump secondbeach11floor2

label secondbeach11floor1:
    play sound "slidedoor.mp3"

    "I stop by my room before heading over to the one the first floor girls are staying in to get changed into something more comfortable."
    "The good thing about this is that it means I won’t be going to sleep in jeans tonight."

    if bonus == True:
        "The bad thing, however, is that it is much harder to conceal an erection in sweatpants."
        "And given the fact that there are soon to be ten cute girls (Or less, if any of them were either kidnapped or killed tonight) paying attention to me, an erection seems very likely in the future."
        "But hey, I’m sure that sort of thing would go over a lot better in the first floor room than it would in the second, give or take several notable exceptions."
    else:
        "The bad thing, however, is that I'll be surrounded by a bunch of icky girls."

    play sound "slidedoor.mp3"
    scene floor1sleepover1
    with dissolve
    play music "sweetvermouth.mp3"

    "I make my way into the room with a pep in my step and a dream in my heart."

    if amifingered == True and bonus == True:
        "Tonight is the night I have sex with ten girls at once."

    else:
        if bonus == True:
            "Tonight is the night I have sex with nine girls at once and make Ami wait out in the hallway and cry."
            "Sorry, Ami."
        else:
            "Tonight is going to be tough, but I will do my best to survive."

    "I take a look around the room to find everyone essentially doing their own thing and am quickly hit with my first dilemma out of what I imagine will be many."
    "Who am I going to talk to first?"
    "We have all night, so I’m sure I’ll be able to spend at least a {i}little{/i} time with everyone, but..."
    "Well...I guess there’d be even less use in standing around. So I should probably just make a decision now."

    "Who do I want to talk to?"

    menu floor1sleepovermenu:
        "Futaba & Makoto" if futamaksleep == False:
            scene floor1sleepover2
            with dissolve

            mak "Oh, excellent timing."
            mak "Futaba and I were actually just talking about you."
            f "We were wondering if you were...actually going to show up or not."
            s "Was that actually a real concern of yours? Because I thought it would be pretty obvious that I wouldn’t miss something like this for the world."
            f "That’s what I said. Makoto is the one who disagreed."
            s "What? Why?"

            scene floor1sleepover3
            with dissolve

            mak "Well...there was the whole thing with the rules earlier."
            mak "So I thought that maybe you’d think things would be too boring with me here and run off to sleep with the other floor instead."
            s "I wouldn’t have done that even if you made me stay ten feet away from everyone here at all times."

            scene floor1sleepover4
            with dissolve

            mak "Don’t be ridiculous. There’s not nearly enough space in this room for something like that."
            mak "I was only going to impose a five foot rule. At least that would be manageable."
            s "…"
            f "…"

            scene floor1sleepover5
            with dissolve

            mak "I’m kidding..."
            mak "I {i}am{/i} glad you showed up, though. Because this means you can join in on our discussion about literature."
            s "Oh boy. How exciting."

            scene floor1sleepover6
            with dissolve

            f "Oh, stop..."
            f "You can pretend it’s boring, but Makoto and I both know you actually love reading."
            f "And...back before you started treating all of us more like {i}friends{/i} than students, you always had so much to say about it."

            if bonus == True:
                "How in the world was past-me such a buzzkill when there were this many attractive girls around?"

            s "Is that all you two planned on doing tonight? Just...talking about books?"

            scene floor1sleepover7
            with dissolve

            f "I’m sure the conversation would move onto other topics eventually...but both of our roommates went off and started doing their own things, so..."
            mak "This gave us a great opportunity to talk about what we have in common."
            mak "I’ve been meaning to lend this to Futaba anyway, as I’m sure if there is anyone who would appreciate it, it’s her."
            s "And what are you lending her exactly?"
            mak "A deconstruction of important events that may have led to the space war we’re currently-"
            f "I don’t think Sensei...really cares about the space war..."
            s "What space war?"

            scene floor1sleepover8
            with dissolve

            mak "The..."
            mak "The one that’s happening above us..."
            mak "In space..."
            s "Was there something like that going on?"
            mak "You know...sometimes I wish teachers weren’t exempt from the draft."
            mak "There is a lot of important information in this book that I’m sure even someone like you could-"
            s "Anyway, how was {i}your{/i} day, Futaba?"

            scene floor1sleepover9
            with dissolve

            f "It was...really fun, actually."
            f "Well...until a thing happened during D&D...but I’m kind of sure you don’t really want to hear about that."
            s "I’m sure I wouldn’t understand either way."
            s "But, on that note, I’m probably going to go say hi to a few of the other girls before the night gets a little too late."
            mak "Here’s hoping they’re able to interest you a little more than {i}we{/i} did."
            s "Not both of you, Makoto. Just you."
            mak "Bite me."
            s "Sorry. Five foot rule. Your fault."

            $ futamaksleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor1sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor1sleepovermenu

        "Rin & Maya" if rinmayasleep == False:
            scene floor1sleepover10
            with dissolve

            r "Yo! What’s crackalackin’ homie? Come to chill with the t-shirt gang?"
            s "The what?"
            r "You know. Cause we’re both wearing t-shirts to sleep."
            s "Okay. So are Makoto and Sana."
            r "Those don’t count. They’ve got extended neck hole thingies that reveal more skin."
            r "Maya and I are much more modest, which means that we’re more sought after than those other losers."

            scene floor1sleepover11
            with dissolve

            m "I don’t really see much purpose in insulting them over their wardrobe choices."
            r "I didn’t mean to. I meant “losers” in the broad sense because they’re not here right now and...we are and...I kinda want you to like me more."
            m "You don’t think I dislike you, do you?"
            r "No...But like, you’re always so cool and mysterious and I think it would be rad if I could...be a little more like you."
            m "I can promise you that you don’t want to be anything like me. I’m nothing special."
            s "{i}Ahem...{/i}"

            scene floor1sleepover12
            with dissolve

            m "What?"
            m "You are aware that you don’t have to stand there and talk to us, correct? You can leave whenever you want to."
            r "Sorry for ignoring you, Sensei. It’s just been...kind of a weird night."
            s "Weird in what way?"
            r "Well..."

            scene floor1sleepover13
            with dissolve

            m "Otoha wanted to play a game but Molly said no. But then Rin said yes. And then Otoha agreed to it being a no. But Rin kept saying yes."
            m "Then there was a lot of crying. The end."
            s "Yup. That definitely sounds kind of weird to me."
            r "Hahah...hah..."

            scene floor1sleepover14
            with dissolve

            r "But that’s okay! Because tomorrow is gonna be the day that the thing happens and I’m trying to stay positive!"
            r "Also, have you found any sheds yet?!"
            s "Sheds?"
            r "You know...a place for me to cry and use your shoulder as a handkerchief when I am inevitably crushed tomorrow night?"
            s "Is it really okay to be talking about those plans in front of Maya?"

            scene floor1sleepover15
            with dissolve

            m "Why wouldn’t it be?"
            m "Just because I’m good at remaining emotionally distant doesn’t mean I lack empathy. "
            m "Do I think Rin’s time would be better served on crying into the shoulder of anyone else? Of course."
            m "And do I think it’s a bad idea to use you as a means of coping when you only exacerbate existing conditions to the point where they are no longer even able to be coped with? Definitely."

            if bonus == True:
                m "Do I also believe that you’ll only pretend to care about her feelings because it will bring you one step closer to adding her to your harem? Absolutely. "
            else:
                m "Do I also accept those flaws as just one more aspect of your personality and love you regardless of that and any of your {i}other{/i} many flaws? Sure."

            m "Am I fine with the fact that-"
            s "Okay, Maya. I think I get it."

            scene floor1sleepover16
            with dissolve

            m "I’m tired. Can you leave now, please?"
            r "...Me? Or Sensei?"
            m "You can stay. He’s the exhausting one."
            s "You think {i}Rin{/i} is less exhausting than {i}me?{/i}"
            m "That is what I said, yes."
            r "Even I’m gonna go ahead and disagree with that one, Maya. I’m kind of a lot."
            s "Luckily for you, Maya, I was just about to go talk to some of the others anyway."
            m "Hooray. "
            m "Just try to keep the volume to a minimum."

            $ rinmayasleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor1sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor1sleepovermenu

        "Chika" if chikasleep == False:
            scene floor1sleepover17
            with dissolve

            c "Oh, hey! "

            if chikalust20 == True:
                c "Crazy seeing you here after definitely not seeing you at any other point tonight!"
                s "Yes. This is the first time we are seeing each other in several hours."
                s "Where have you been all day, Chika? Because it’s definitely not somewhere I have any idea of."
                c "Just...around! Definitely not walking around the woods or anything! Way too many bugs over there."

            else:
                c "I didn’t even hear you come in! I’ve been a little distracted by-"

            ch "Is that Papa?! Is Papa there?!"

            scene floor1sleepover18
            with dissolve

            c "Yes, Chinami. But please don’t call him that while you’re on speaker phone."

            if bonus == True:
                ch "What did I tell you about having boys over this late at night, big sister?"
                ch "Chinami doesn’t have the time to take care of a baby! She has important business transactions to make!"
                ch "Just kidding. Please give Chinami a little sister. "
                ch "That goes for you too, Papa! "
                ch "Chinami’s smartphone has unlocked all sorts of new information for her to learn!"
                ch "She understands eeeeeeeverything now!"
            else:
                ch "SILENCE, BIG SISTER. I WILL CALL HIM WHAT I WANT TO CALL HIM AND YOU CAN NOT DO ANYTHING ABOUT IT."
                ch "IF YOU ATTEMPT TO STOP CHINAMI, YOU WILL FEEL HER RAGE HARDER THAN EVER BEFORE."

            scene floor1sleepover19
            with dissolve

            c "Hahah...hah...heh..."
            s "Why did you think it was a good idea to let her have a phone again?"
            c "Can you blame me for not thinking she would just use it to play games all day?"
            c "Even parental locks were no match for her. She’s too smart."
            ch "Chinami isn’t just smart! She is...very smart!"

            scene floor1sleepover20
            with dissolve

            c "Chinami is {i}also{/i} still awake after her bedtime. "
            c "Do I need to come home and force you to go to sleep?"
            ch "Chinami is a loose cannon cop on the edge with nothing to lose! She drank coffee tonight!"

            scene floor1sleepover21
            with dissolve

            c "Chinami! I told you that you can’t have coffee! You’ll get a tummy ache!"
            ch "Chinami thinks it will be worth it! Her heart is going crazy! This must be what love feels like!"
            ch "Is that right, big sister?! Is Chinami feeling love?!"
            s "I bet you’re starting to second guess leaving her alone now, huh?"

            scene floor1sleepover22
            with dissolve

            c "The results of that remain to be seen..."
            c "Sorry, but would you let me finish up with her really quick? I just need to make sure she’s taken all of her vitamins and stuff."
            c "I’ll catch up with you again in a few minutes."
            s "Yeah, no worries. I’ll be here all night."
            c "Thanks..."

            if bonus == True:
                ch "Bye bye, Papa! Good luck making babies with my sister!"
                ch "Make sure you give one to big sis Yumi too! Chinami wants {i}two{/i} little sisters!"
            else:
                ch "Bye bye, Papa! Remember to invest in Chinami-corp before it goes to the moon!"

            s "I’ll do my best, Chinami."

            scene floor1sleepover23
            with dissolve

            c "No. You most certainly will not."

            $ chikasleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor1sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor1sleepovermenu

        "Yumi" if yumisleep == False:
            scene floor1sleepover24
            with dissolve

            "I make my way over to Yumi to find her eyes already closed for the night."
            "I also recognize the pillow with her as one she must have brought from her room, and the idea of her doing that is extremely cute to me."
            "It’s a shame she already appears to be asleep, though..."
            "Not."

            s "Yumi. I know you’re just faking being asleep to avoid talking to me."

            scene floor1sleepover25
            with dissolve

            y "Well then why the fuck would you talk to me in the first place?!"
            y "If it’s obvious I don’t want to be near you, wouldn’t the rational choice be to just leave me alone?!"
            s "Yes. But I am a very irrational man."
            s "Also, it’s way too early in this event for you to actually be sleeping. You don't want to disappoint all of your adoring fans, do you?"

            scene floor1sleepover26
            with dissolve

            y "Event? Fans?"
            y "The fuck are you talking about?"
            s "Don’t worry about it. But hey, now that you’re awake, do you want to tell me about that thing you said you...wanted to tell me about or whatever?"

            scene floor1sleepover27
            with dissolve

            y "I already fucking told you I would do that tomorrow, didn’t I?"
            y "I still don’t really know what to say without sounding like a fuckin’ creep about it."
            y "Was probably just seein’ shit anyway, so..."
            y "I wouldn’t even worry about it if I was you."
            s "So it’s actually kind of serious, then?"
            y "Not really. More...fuckin’ weird than anything else."
            y "But...like I said...tomorrow’s better."
            s "I see."
            s "Do you have any plans during the day? Maybe we could hang out for a little while beforehand?"

            scene floor1sleepover28
            with dissolve

            if bonus == True:
                y "Why the fuck would you wanna hang out with me? You’ve got nineteen other choices who wouldn’t actually rip your dick off if given the opportunity."
                s "I have a hard time believing you would actually do something like that to me."
            else:
                y "Why the fuck would you wanna hang out with me? You’ve got nineteen other choices who wouldn’t actually rip your arms off if given the opportunity."
                s "I have a hard time believing you would actually do something like that to me."

            scene floor1sleepover29
            with dissolve

            y "Why? You think I’m all talk or some shit?"
            s "Of course not. "

            if bonus == True:
                s "It’s just that doing that would require you willingly touching my penis- and I can’t see that happening for at least a few more beach updates."
            else:
                s "It’s just that doing that would require you willingly touching my arms- which is pretty close to a hug."

            scene floor1sleepover30
            with dissolve

            y "Aaaaaahhh! Ew ew ew ew ew! I don’t even want to think about that!"
            s "{i}Then stop threatening me...{/i}"
            y "Fine! Whatever! Just...leave me the fuck alone!"
            s "Fine, fine. I was just leaving anyway."
            s "See you tomorrow, Yumi."
            y "Die, pig!"

            $ yumisleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor1sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor1sleepovermenu

        "Miku & Sana" if sanamikusleep == False:
            scene floor1sleepover31
            with dissolve

            s "Hey, you two. What are you-"
            mi "DIE! DIE! DIE!"
            sa "Just...playing games."
            s "It doesn’t look like {i}you’re{/i} playing anything at all, though."
            sa "Well...not right now, I’m not."
            sa "I brought my Switch since I thought...I wouldn’t have anything else to do tonight..."
            sa "But Miku and I were talking earlier and...she said she was interested in playing something, so..."

            scene floor1sleepover32
            with dissolve

            mi "That’s right, Sensei."
            mi "And with my roommate payin’ attention to books and stuff, I’m finally free to be a normal girl again!"
            mi "All of those days of hidin’ my love for Tetris are gone! I’m free to kill all of those stupid blocks to my heart’s content!"
            sa "Ooh. There’s a long one coming up."

            scene floor1sleepover33
            with dissolve

            mi "Looks like it’s gonna be a tight fit, but I can make it work!"
            s "…"
            s "So uhh, ignoring that last part, you seem...really into Tetris, Miku. "
            mi "We were gonna play somethin’ else, but the wifi is actin’ up and we’ve gotta wait for it to download."
            mi "So, ‘til then, I’m just brushin’ up on my skills."
            mi "Used to be crazy good with my fingers back in the day, but then I started workin’ on my legs and it aaaaall went to shit."

            scene floor1sleepover34
            with hpunch

            mi "EAT BLOCK YOU STUPID...BLOCK!"
            sa "Do you..."
            sa "Do you want to try playing as well, Sensei?..."
            sa "When Miku is done, I mean..."
            s "I’m okay, Sana. But thanks."
            sa "Really?"
            sa "I thought that...since it’s Tetris and...you’re old...you might’ve-"
            s "Please don’t finish that train of thought."
            s "Besides, not all old people like Tetris...and I’m not even that old."
            sa "You’re a lot older than me."
            s "Right. But please don’t compare me to some sort of father figure again because there is a time and a place for everything and neither of those are right now or right here."

            scene floor1sleepover35
            with dissolve

            sa "That...yeah..."
            sa "That was...definitely a mistake in hindsight..."
            mi "Hm. "
            mi "Ya know, I can see it."

            scene floor1sleepover36
            with dissolve

            sa "Hm? See what?"
            mi "You bein’ Sensei’s daughter."

            scene floor1sleepover37
            with dissolve

            sa "Uhh...what?"
            mi "Yeah, I totally see it. "
            mi "Sure, Sana’s a little on the tiny side, but if I saw you two walkin’ down the sidewalk holdin’ hands, I’d be closer to thinkin’ “Oh! Cute family!” than “Somebody call the cops!”"
            s "Thanks. "
            s "I think."
            mi "Hey, don’t thank me. Thank your daughter for helpin’ me rediscover a brand new side of myself."
            sa "I’m...not his..."
            s "Sana, be a good girl and thank Miku for pointing out how nice of a family we are."

            scene floor1sleepover38
            with dissolve

            sa "I...actually think I’m...just gonna go take a shower or something..."

            $ sanamikusleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor1sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor1sleepovermenu

        "Ami & Ayane" if futamaksleep and chikasleep and yumisleep and rinmayasleep and sanamikusleep:
            "After talking to everyone else, I realize I haven’t touched base with Ami & Ayane yet."
            "And while it would be fun to make their presence into some sort of mystery that would devolve into a search of the entire inn, I can already hear their giggling coming from the bedroom."

            scene black
            with dissolve

            "As such, I take one last glimpse at the rest of the girls in the main part of the room and slide the door open to greet my two surrogate daughters."
            "………"
            "……"

            play sound "slidedoor.mp3"

            "…"

            scene floor1sleepover39
            with dissolve

            ay "At last! The final wing of the slumber party has begun!"
            a "I hope you didn’t have any other plans for the rest of the night, Sensei! Because you’re never leaving this room again."
            s "Never?"
            a "Well, not until tomorrow."
            s "That’s not even close to never."
            ay "I’ve gotta say, when I first came up with the idea for the dorm war, I didn’t think anybody would agree to you actually being the prize."
            ay "But, now that it’s all said and done, I couldn’t be happier."
            s "I don’t see how this is much different from a normal sleepover at my house apart from the fact that there are just...more girls than normal."
            a "That’s exactly why it’s great! Because now all of them will know for sure that you love me the most."
            a "And Ayane can be second place, I guess. But it’s a really distant second place. Like I’ve already lapped her and stuff."
            ay "As you can see, I’ve just decided to let Ami believe whatever she wants as long as it helps her sleep at night."
            a "I can’t imagine I’ll have any trouble falling asleep tonight with Sensei right beside me."

            if bonus == True:
                s "I’m sleeping in here?"
                ay "The answer to that question is written on Ami’s pillow."
                a "The pillow says yes."
                s "I see that."
                s "But...you {i}do{/i} know what that pillow actually-"
                a "Oh, I know what the pillow means."
                ay "What happens at the beach stays at the beach."
            else:
                s "But I don't wanna sleep in here. There's no nightlight."

            if ayanelust10 == True and bonus == True:
                ay "Thankfully, nothing bad has ever happened at the beach and it is nothing but good memories for all of us. Yay."
                s "…"

            scene floor1sleepover40
            with dissolve

            a "Anyway, we’re still in agreement that Sensei will be sleeping between the two of us, correct?"

            if bonus == True:
                a "And that you won’t touch him at all?"
                ay "Was that part of the deal? Because I can’t imagine I would have agreed to it if it was."
                a "It was part of the deal."
                ay "Hoooooow aboooout...I only touch him as much as you touch him? But also, my clothes are off."
                a "…"
                a "How about I cut you into little pieces and cook you into macaroni?"
                ay "Oooh, I love macaroni."
            else:
                s "No! We are not!"

            play sound "slidedoor.mp3"
            scene floor1sleepover41
            with dissolve

            c "Or, how about you two let Sensei choose where he wants to sleep instead of keeping him locked in here?"

            scene floor1sleepover42
            with fade

            c "I’m off the phone now."

            if bonus == True:
                s "I...can see that."
            else:
                s "Thank you for coming to rescue me."

            scene floor1sleepover43
            with dissolve

            ay "You have a problem with Sensei sleeping in here, Chika?"
            c "I mean...I don’t have a {i}problem{/i} with it. "
            c "I just think it’s a little immature to not let a grown man choose for himself."
            ay "Hmm."

            scene floor1sleepover44
            with dissolve

            ay "I think you should mind your own business."
            c "…"

            scene floor1sleepover45
            with dissolve

            c "Excuse me?"
            a "Why are you assuming that we’re forcing Sensei to stay in here when it’s exactly where he would have chosen to sleep no matter {i}who{/i} was inside?"
            ay "You don’t know him as well as we do, so allow me to inform you that Sensei couldn’t care less about which girls are in here. He just hates sleeping on the floor."
            a "Which is exactly why Ayane and I were so adamant about getting the bed. "
            c "Just seems a little weird for his {i}[niece]{/i} to be so adamant about sleeping next to him."
            a "I don’t care how weird it seems. That’s just how things are."
            ay "It’s nothing against you, of course. But I kinda need this right now."
            c "You “kind of need him” all the time."
            ay "Yup! Now you’re starting to get it."

            scene floor1sleepover46
            with dissolve

            c "…"
            s "…"
            c "You’re really going to sleep in here?"
            s "…"
            s "Well...this {i}is{/i} where the bed is..."
            c "…"

            scene floor1sleepover47
            with dissolve

            c "Hmph. Fine."
            a "Woo! The SLS wins its first battle!"
            ay "With many, many more sure to come."
            s "I feel like you two could have been a {i}little{/i} bit nicer..."

            scene black
            with dissolve

            a "Probably! But you’re all ours now."
            ay "Ami! Attack!"
            a "On it!"

            if bonus == True:
                s "What do you mean “attack?” I’m a willing participant-"
            else:
                s "No! I bruise easily!"

            "I am ruthlessly tackled onto the bed and pinned down by my shoulders as Ami and Ayane climb on top of me."

            if bonus == True:
                "The inevitable erection I alluded to earlier finally begins to come into existence and I do everything in my power to fight it off for as long as I can..."
            else:
                "It is scary and I hate it."

            scene floor1sleepover48
            with dissolve

            a "Now...where were we?"
            s "The inn...surrounded by all of your friends...right outside of an open door."

            if bonus == True:
                ay "Sensei! Are you insinuating that Ami and I were about to do something NSFW?"
                ay "Because that wasn’t the idea, but I guess I could be convinced as long as you pay more attention to me than her."
            else:
                ay "Sensei! Are you insinuating that Ami and I were about to do something NSFW? This is the Patreon version! That can't happen!"
                s "Oh thank goodness."

            if amifingered == False:
                a "It’s not like he pays enough attention to me in the first place."
                a "If Ayane being here is what it takes to change that, fine. So be it."

            if bonus == True:
                "Slowly but surely, I can feel my mind beginning to consume my body."
                "I can not fight this off much longer."

            a "You know...I thought I’d have an easier time falling asleep tonight..."
            a "But maybe it will be the exact opposite?"

            if bonus == True:
                ay "I know what you mean, Ami. But I’m going to go ahead and ignore that you feel the same way because you two are still related and your babies wouldn’t be as cute as mine."
            else:
                ay "I know what you mean, Ami. It's pretty cramped with three people in here. Maybe one of us should {i}die?{/i}"

            scene floor1sleepover49
            with dissolve

            a "I’m sorry, what was that, Ayane? "
            a "I couldn’t hear you over the sound of your...stupid face."
            s "Ami, come on. I raised you better than that."
            s "I think."

            scene floor1sleepover50
            with dissolve

            a "Love me."
            ay "Love {i}me...{/i}"
            s "…"

            scene floor1sleepover51
            with dissolve

            c "…"
            s "…"
            s "It’s not what it looks like."
            a "Yes it is."
            ay "It totally is."
            c "I {i}know{/i} it’s not what it looks like...because {i}I’ve{/i} decided that I’m going to be sleeping in here as well."

            scene floor1sleepover52
            with dissolve

            a "What?! No! You’re too pretty! It won’t be fair to us!"
            ay "I’m not really opposed...but you’ll probably have to sleep on the-"

            scene floor1sleepover53
            with dissolve

            c "I know. I won’t be on the bed..."
            c "But...I’ll be closer to Sensei, and..."
            c "…"
            s "…"
            c "I’ll go get my futon."

            scene black
            with dissolve2

            "So..."
            "The rest of the night basically takes place inside of the bedroom."
            "Several other girls come in and out as the night goes by to see what’s going on, but neither Ami nor Ayane is willing to get off of me at any point."
            "As such, I spend all of my time participating in conversations as they are delivered to me, and ultimately fall asleep with two tiny love machines strapped to my body."

            if bonus == True:
                "It’s exhausting at first, sure..."
                "But I think I like it at the end of the day."
            else:
                "It is probably the worst night ever."

            $ renpy.end_replay()
            $ secondbeach11 = True
            $ chika_love += 1
            $ yumi_love += 1
            $ sana_love += 1
            $ ayane_love += 1
            $ makoto_love += 1
            $ miku_love += 1
            $ rin_love += 1
            $ futaba_love += 1
            $ ami_love += 1
            $ maya_love += 1
            stop music fadeout 7.0

            "{i}Your affection with everyone on the first floor has increased by 1!{/i}"
            "………"
            "……"
            "…"

            jump secondbeach12

label secondbeach11floor2:
    play sound "slidedoor.mp3"

    "I stop by my room before heading over to the one the second floor girls are staying in to get changed into something more comfortable."
    "The good thing about this is that it means I won’t be going to sleep in jeans tonight."

    if bonus == True:
        "The bad thing, however, is that it is much harder to conceal an erection in sweatpants."
        "And given the fact that there are soon to be ten cute girls (Or less, if any of them were either kidnapped or killed tonight) paying attention to me, an erection seems very likely in the future."
        "But hey, all of the residents of the second floor are pretty chill."
        "Some of them are a little intimidating, sure. But they’re still mostly normal."
        "Apart from...most of them."
        "You know what? I’m not going to think about how normal anyone is right now."
        "I’m just going to have fun."
    else:
        "The bad thing, however, is that the room is filled with icky girls that I'm going to have to try and talk to."

    play sound "slidedoor.mp3"
    scene floor2sleepover1
    with dissolve
    play music "sweetvermouth.mp3"

    "I make my way into the room with a pep in my step and a dream in my heart."

    if bonus == True:
        "Tonight is the night I have sex with ten girls at once."

    "I take a look around the room to find everyone essentially doing their own thing and am quickly hit with my first dilemma out of what I imagine will be many."
    "Who am I going to talk to first?"
    "We have all night, so I’m sure I’ll be able to spend at least a {i}little{/i} time with everyone, but..."
    "Well...I guess there’d be even less use in standing around. So I should probably just make a decision now."

    "Who do I want to talk to?"

    menu floor2sleepovermenu:
        "Karin & Kirin" if kandasleep == False:
            scene floor2sleepover2
            with dissolve

            "I make my way over to the Kanda sisters to see how Karin mysteriously wound up reconciling with Kirin over the last several hours."

            ka "Umm...hey!"
            ki "Sup?"
            s "Hey. Just figured I’d see what you two were up to on account of the whole “me sleeping in here” thing."
            ka "…"
            ka "I’m sorry, what was that?"

            scene floor2sleepover3
            with dissolve

            ki "Remember that dorm war thing we had you judge a while ago?"
            ka "I remember you licking Miku."
            ki "Yeah, that one."
            ki "Sensei was the prize for that. And since we won, he has to sleep in our room."
            ka "But..."
            ka "But then where will all of you sleep?"
            ki "Probs on top of him or something. I don’t know."

            scene floor2sleepover4
            with dissolve

            ka "But...there are so many of you!"
            ka "Surely he’ll suffocate!"

            if bonus == True:
                s "Hey, if that’s the way I’m meant to go, so be it."
                ki "Yeah, I was about to say. I don’t think he’d mind."
            else:
                s "That sounds not only unconventional but just plain weird. I'll sleep in the tub or something."

            s "That aside, what’s going on with you two?"

            scene floor2sleepover5
            with dissolve

            ki "Hm? What’re you talking about?"
            s "I mean...didn’t today start off with you being mad at Karin for coming to the beach when you told her not to?"
            ki "Ahh. Yeah, I guess the morning did start like that."
            ki "We’re fine now, though."
            ka "Kirin and I are...about to go night swimming."
            s "Having a sister sounds exhausting. That’s too dramatic a change for only several hours passing by."

            if kirinlust20 == True and bonus == True:
                scene floor2sleepover6
                with dissolve

                ki "Well, hey! A certain somebody and {i}another{/i} certain {i}female{/i} somebody really helped me get over it earlier."
                ka "A certain somebody and...a female somebody that...Wait, what?"
                ka "I don’t understand what you just said."
                ki "And you don’t have to worry about it, Karin! Thanks for agreeing to stay out of it!"
                ka "But then...why would you-"

            else:
                scene floor2sleepover7
                with dissolve

                ki "Eh. It is what it is."
                ki "I know I can be kinda hot and cold or whatever. And it’s not like I could stay mad at Karin when she was the one our parents gave the dinner money to."
                ka "I...really hope that’s not the only-"

            scene floor2sleepover8
            with dissolve

            ki "Anyway, did you wanna come swimming with us? "
            ki "We’re both pretty good, but we can pretend we’re not and you could give us lessons or something."
            ki "I think that sounds like a load of fun, don’t you, sis?"
            ka "I’ll just...close my eyes while he teaches you, so...I don’t get jealous."

            scene floor2sleepover9
            with dissolve

            ka "Ah! Did I say jealous?! I meant...jelly!"
            ka "Jellyfish! That’s what I was trying to say!"
            ka "I can’t get swimming lessons because of my...jellyfish allergy!"
            ki "Oh? I guess more Sensei for me then."

            if bonus == False:
                "{i}Ugh...{/i}"

            s "As fun as that sounds, I don’t really think I’m allowed to leave the room."

            scene floor2sleepover10
            with dissolve

            ki "You’re {i}allowed{/i} to do whatever you want. You’re a grown man."
            ka "You’re...really not coming?"
            s "Karin, literally two seconds ago you were telling us that you couldn’t even swim because of your alleged jellyfish allergy."
            ka "I wasn’t sad two seconds ago...now I am."
            s "Well, if I’m still awake when you guys get back, feel free to come...tell me about it or whatever."
            ki "Laaaaaame."
            ka "Okay..."
            ka "Goodnight, Sensei..."

            $ kandasleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor2sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor2sleepovermenu

        "Tsuneyo & Molly" if tsuneyosleep == False:
            scene floor2sleepover11
            with dissolve

            s "Hey, Tsuneyo."
            t "Sup, bro?"
            s "Why are you still saying that?"
            t "It is an important greeting I have learned. And once I learn something, I am incapable of forgetting it."
            t "Also, your son is here. You two need to stop fighting. It is tearing our family apart."
            s "My son?"

            scene floor2sleepover12
            with dissolve

            t "I can’t believe I ever married you."
            s "Probably because you didn’t."
            t "I am referring to Noodles."
            s "Yeah, what else is new?"
            t "Noodles the bird."
            s "The one who carries the knife and says all that existential stuff?"
            t "This is why you two always fight. You refuse to understand one another."
            s "Tsuneyo, I haven’t “talked” to that bird since we decided to name him."
            t "Dear God, it’s even worse than I thought."
            s "Can we stop talking about birds for a second? I am spending my extremely valuable time during this sleepover talking to you and I would appreciate it if the conversation would at least be...good."

            scene floor2sleepover11
            with dissolve

            t "I am afraid you have come to the wrong person if that is what you are after."
            t "One of the many things I have learned from the other girls in this room is that I am not very good at socializing. "
            t "The Green Onion wants me to get better at facial expressions, but they seem very difficult. "
            s "Yeah, I never really got the hang of those either."

            scene floor2sleepover13
            with dissolve

            t "Of course. That explains why I never enjoy talking to you."
            s "…"
            t "…"
            s "So, anyway, is Molly already asleep?"

            scene floor2sleepover14
            with dissolve

            t "The Emerald Guardian had a...difficult night."
            t "She is currently recovering her mana so she can start anew in the morning. "
            s "Did something happen?"
            t "A disagreement of sorts regarding the one the Guardian refers to as a “Succubus.”"
            s "I don’t really know what that means, but I can probably guess who she’s referring to based on...past experiences."
            t "I worry about her, Supreme Overlord Horrible Father."
            s "That’s definitely one of my worst nicknames, not going to lie."
            t "You have helped me prepare for loss, but I have not yet studied the means of becoming a better friend."
            t "What can I do to restore her mana quicker?"

            if bonus == True:
                s "I know one way that she’s told me about before, but I don’t really know if either of you would find it particularly-"
                s "Actually, you both probably would."
                s "But I still shouldn’t tell you."
            else:
                s "Do you have any mana potions?"
                t "No."
                s "Oh. Well, then there's not much you can do."

            scene floor2sleepover13
            with dissolve

            t "Darn it."
            t "It appears that I will simply remain by her side in the event that she needs anything."

            if bonus == True:
                s "Honestly, that’s kind of what a good friend would do anyway. My thing was a lot more, uhh...physical."
            else:
                s "I mean...there is {i}one{/i} other way..."

            scene floor2sleepover11
            with dissolve

            t "If you are referring to a “hug,” I have already tried."

            if bonus == True:
                s "I’m not."
            else:
                s "And it...didn't work?"
                t "It did not."
                s "That is...so, so sad."

            s "But anyway, it’s been real. I think I’m going to go talk to a few of the others now."
            t "I understand and apologize for making things awkward."
            s "You actually kind of didn’t this time, as weird as that sounds."
            t "You are just saying that to make me feel better. I make everything awkward."
            s "Okay, now it’s awkward."
            t "Peace out, bro."
            s "…"
            s "Bye, Tsuneyo."
            t "Ah-"

            $ tsuneyosleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor2sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor2sleepovermenu

        "Touka" if toukasleep == False:
            if bonus == True:
                scene floor2sleepover15
                with dissolve

                s "…"

                "I don’t say anything when I make it over to Touka’s futon. I just kind of stare for a little while."
                "And I guess my plan for the rest of the night is to just keep staring for as long as I can since she already appears to be asleep."

                s "…"

                "I probably shouldn’t have worn sweatpants."

                to "Are you getting a good look?"
                s "Yes. And thank you."

            scene floor2sleepover16
            with dissolve

            to "May I help you with something?"
            s "Why aren’t you excited to be sleeping in the same room as me?"
            to "Because it’s entirely inappropriate...but that is not the reason for my foul mood."
            to "This futon is paperthin. I can feel my back pressing right through it into the floor."
            to "I’m almost certain I’m going to have to visit the chiropractor as soon as we return home."

            if bonus == True:
                s "To be fair, I’m surprised you don’t already have to visit one on a regular basis."
                to "…"
                s "Get it? Because-"
                to "Yes."
                to "And, might I add, {i}that{/i} was entirely inappropriate as well."
                s "Sorry. I just figured it was okay since we’ve been on a date before."

                scene floor2sleepover17
                with dissolve

                to "Wha-"
                to "Must I inform you again that that {i}wasn’t{/i} a real date? I was only involved in that contest because of reasons completely out of my control."
                s "Yeah, yeah. You wanted the athletics or knowledge thing instead. I remember."
            else:
                s "That is a great idea. Staying healthy is the key to living a fulfilling and long life."

            scene floor2sleepover18
            with dissolve

            to "Hah...maybe next year, I suppose."

            if bonus == False:
                s "That is far too long, Touka. You need to go at the first sign of issues."

            if chikalust15 == True and bonus == True:
                s "Speaking of next year, I’m also hoping for a repeat of your little bonus contest. That was one of the highlights of the whole weekend."

                scene floor2sleepover19
                with dissolve

                to "Bonus contest? Whatever are you talking about?"
                s "Nothing at all, Touka."
                s "{i}Nothing at all...{/i}"
                to "And there you go with that horrid whispering again. I don’t understand how hard it is to just lower your voice to an inaudible level."
                to "But I suppose that doesn’t matter."

                "Note to self: encourage Touka to drink more."

            scene floor2sleepover20
            with dissolve

            to "So, is this how you’re going to spend your night?"
            to "Talking to me out of pity because I’m all alone?"
            s "It’s not out of pity. I came over here because I actually {i}wanted{/i} to talk to you."

            scene floor2sleepover21
            with dissolve

            to "Sensei..."
            to "Do you...do you really mean that?"
            s "Of course. You’re one of my favorite students, Tomoko."
            to "…"

            scene floor2sleepover15
            with dissolve

            to "Goodnight."
            s "Oh, come on. That was hilarious. "
            to "The first time? Maybe. The second time? Okay."
            to "But you have now referred to me by the incorrect name roughly one hundred separate times and I am becoming exhausted from tricking myself into thinking you’ll drop those petty games of yours."
            s "I’m beginning to feel my chances of marrying into the Tsukioka family slip away."
            to "I still have a mother and younger sister. Perhaps you’ll find yourself tormenting one of them instead of me one of these days?"
            s "I have a creeping suspicion that I will be doing just that eventually, yes."

            scene floor2sleepover22
            with dissolve

            to "I suppose we’ll be putting up with each other for quite some time then, won’t we?"
            s "You don’t know the half of it."
            to "…"
            s "…"
            to "I...wouldn’t mind listening if you wanted to-"
            s "Anyway, it’s been fun, but I’m going to go mingle with some of the other girls now."

            scene floor2sleepover17
            with dissolve

            to "Wait...already? But you just got here!"
            s "Yeah, but there are ten of you. I have to distribute my time evenly. "
            to "Oh..."
            to "Well...okay, then..."
            to "Good...goodnight?"

            $ toukasleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor2sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor2sleepovermenu

        "Otoha & Nodoka" if nodokaotohasleep == False:
            if bonus == True:
                scene floor2sleepover23
                with dissolve

                s "Hey, Otoha. What are you up to over- woah."
                o "…"
                s "…"
                s "Have I told you lately how much I like your pajamas?"
                o "…"
                s "Because I really like them."
                o "…"
                s "Like, a lot."
                o "…"
                s "You should stop wearing other clothes altogether and just only wear those from now on."
                o "…"
                s "Hey, Otoha. If you want me to touch you, stay silent."
                o "…"
                s "Welp, guess I’ll just-"
                no "Not so fast, Sensei."
                no "I’ve sworn to protect Otoha from predators while she is “in the zone,” so to speak."

            scene floor2sleepover24
            with fade

            if bonus == False:
                no "Hey."
                no "This part was just entirely cut out of the event."
                no "You have to leave."
                s "Darn it."

                scene black
                with dissolve

                "I decide to do that and go to talk to someone else."

                $ nodokaotohasleep = True

                "………"
                "……"
                "…"

                scene floor2sleepover1
                with dissolve

                "Now who do I want to talk to?"

                jump floor2sleepovermenu
            else:
                s "Is she like...alive?"
                no "Quite."
                no "She’s writing at the moment."
                no "My roommate here has a tendency to shut the world out when she has her heart set on something. And right now appears to be one of those times."
                no "However, I’d like to offer you up a slice of someone slightly less sane if you’d be so obliged to partake."
                s "Only {i}slightly{/i} less sane?"
                s "I’ve seen you hopped up on caffeine before, Nodoka. That was anything but {i}slightly less{/i} sane."
                no "Fortunately for all of us, there’s no means of making hot coffee in the inn and I’ve been subjected to drinking these blasted boxed coffee things with only a portion of the caffeine of {i}actual{/i} coffee."
                no "I’d call it my own personal hell but, as you’ve seen with your own eyes, I have quite the view beside me."
                s "It was definitely a view. "
                s "In fact, let me make sure it’s still there really quick."

                scene floor2sleepover23
                with dissolve

                o "…"
                s "Yup, still there."
                no "Eyes over here, good sir."

                scene floor2sleepover24
                with dissolve

                no "If Otoha is going to ban {i}me{/i} from staring at her ass, I’ll be damned if I’m going to let {i}you{/i} do it."
                s "You two have an interesting relationship if you’re still friends after she had to literally ban you from that."
                no "I agree. Especially when I was kind enough to offer her the same thing in return."
                no "Though, I’ll admit that mine isn’t quite as impressive."
                s "I would like to be the judge of that, thanks."
                no "Would you like to get underneath the covers and get a feel for yourself?"
                s "Yes."

                scene floor2sleepover25
                with dissolve

                no "Excellent."
                no "Could you remind me of how many Nodoka points you have again?"
                s "I-"
                no "Alas. That’s not quite enough."
                s "I didn't even tell you how many I had."
                no "It wouldn't have been enough either way."
                s "I’m beginning to think Nodoka points aren’t even real."
                no "Are any of us real? Or is this all one big fever dream slash dating sim, where you impregnate each of us one by one and then go off to save the world or something?"
                s "Doubtful. I can’t imagine myself ever willingly impregnating any of you."
                no "“Willingly” being the key word there."
                s "Well I’m not going to accidentally impregnate you."
                no "You don’t know that."

                scene floor2sleepover26
                with dissolve

                no "What if I’m the type to lock my legs around you and force you to empty it out inside?"
                s "I’d say that I probably would have wound up doing that anyway."
                no "Living on the edge, I see. How fun."

                scene floor2sleepover27
                with dissolve

                no "Now, if you’ll please excuse me, I’d like to get back to my book."
                s "But...the sex talk."
                no "There is “sex talk” in this book, Sensei."
                s "And you like that more than the real thing?"
                no "If you're that desperate, I’ll give you five minutes alone with Otoha. She probably won’t notice if it's only that much."
                s "I think {i}all of the other girls in the room{/i} would, though."
                no "Only one way to find out, isn’t there?"
                s "…"

                scene black
                with dissolve

                "I decide to...{i}not{/i} do that and go to talk to someone else."

                $ nodokaotohasleep = True

                "………"
                "……"
                "…"

                scene floor2sleepover1
                with dissolve

                "Now who do I want to talk to?"

                jump floor2sleepovermenu

        "Noriko" if norikosleep == False:
            scene floor2sleepover28
            with dissolve

            s "Hey, Noriko."
            n "Hi, Sensei."
            n "Can you pinch me please?"

            if bonus == True:
                s "Like, in a sexual way?"
                n "Like, in a “I think I’m actually dreaming” kind of way. But it can be sexual too if you want. I’m down with a little bit of pain."
                s "I am somehow not surprised by this."
                s "Why aren’t you hanging out with any of the other girls? I had the feeling that you were starting to get kind of popular with them."
                n "Because I was waiting for you, obviously."

            scene floor2sleepover29
            with dissolve

            n "We haven’t had a sleepover since I was still really little, so I’m kind of...really excited and stuff."

            if bonus == True:
                s "You know we can sleep together whenever you want, right?"
                n "No, we can’t. Not with Maya basically living at your house and Kirin always trying to put your dick in her mouth."
                s "Well..."
            else:
                s "I mean...it's certainly strange having one in a place like this."
                s "But if you ever wanted to have a platonic one in a different location, I could probably be talked into it."
                n "Really? But...where?"
                s "Uhhhhhhhhhhhhh..."

            s "Other places exist?"

            scene floor2sleepover30
            with dissolve

            n "Yeah...there are plenty of other places that exist. And any one of them would be fine so long as we’re together."

            "Noriko begins to pick at a loose string on one of the kneecaps of her pajama pants. "
            "I notice her hands trembling slightly, which is a little surprising given that all we’re doing right now is talking."

            n "Um...do you mind if I ask you a question?"
            s "Not really, no. Go ahead."
            n "Rhetorically, if I just so happened to convince the rest of the girls to let me have you tonight and that you had to sleep in the futon with me...how would that make you feel?"

            if bonus == True:
                s "…"
            else:
                s "Scared."

            s "This isn’t rhetorical, is it?"

            scene floor2sleepover31
            with dissolve

            n "Will you think I’m crazy if I say no?"
            s "I already kind of think you’re crazy. But not because of this."
            s "If anything, I’m more surprised you were {i}able{/i} to convince them."

            scene floor2sleepover32
            with dissolve

            n "It probably never would have worked if I wasn’t on the second floor. There’s no way Ami or Ayane or...anyone else down there would have accepted this."
            n "But...all of the girls on the second floor are kind of playing this big...strategy game with one another and waiting to see what everyone else does."
            n "I just got tired of waiting and wanted to feel like I did when I was younger for a little while tonight."
            s "Why are you crying, though? You got what you wanted."

            scene floor2sleepover33
            with dissolve

            n "They’re happy tears. I think. Probably."
            n "I don’t know. I don’t really cry that much."
            n "I’m just feeling a lot of things right now and...thinking of how far this has all come."
            n "It’s still kind of surreal that I can even look at you again. I guess it’s just not...done sinking in yet."
            s "Well...stop. I don’t like crying."

            scene floor2sleepover28
            with dissolve

            n "Okay! Done!"
            s "Really? That easily?"
            n "Yup!"
            s "…"
            s "Bark like a dog."

            scene floor2sleepover34
            with dissolve

            n "Arf!"
            s "Now meow like a cat."

            scene floor2sleepover35
            with dissolve

            n "Nyaa~"

            if bonus == True:
                s "Now say something sexy."
            else:
                s "Now give me stock advice."

            scene floor2sleepover36
            with dissolve

            if bonus == True:
                n "This one time, I hid in the closet while you were fingering my sister and had to hold my mouth closed so you wouldn’t hear me moan from playing with myself."
                s "…"
                n "Okay, maybe it wasn’t just one time. Maybe it was a few."
                s "…"
                n "Maybe it was a lot."
                s "…"
            else:
                n "With the US economy on the brink of a stock market crash due to nearly unprecendented inflation, it is important to remember that the real estate industry benefits from that and will likely flourish in the coming years."
                s "Does your sister know you're a financial advisor now?"

            scene floor2sleepover37
            with dissolve

            if bonus == True:
                n "I was a growing girl, okay?! I found a thing that felt good and I kept doing it! Sue me!"
                s "If anything, I’m just surprised Niki never found out."
                n "…"
                s "…"
            else:
                n "No! And she's never going to find out!"
                s "…"

            scene floor2sleepover38
            with dissolve

            n "…"
            s "She found out, didn’t she?"

            if bonus == True:
                n "I...think I managed to convince her I was just trying on her clothes? But I’m still kind of embarrassed about it and bringing up that part evokes some really cringey memories."
            else:
                n "No comment."

            s "…"
            s "Well, on that note, I think I’m going to talk to a few more of the girls before...apparently returning to you and sleeping in your futon."

            scene floor2sleepover28
            with dissolve

            n "Okay!"
            n "Don’t miss me as much as I’ll miss you, because the pain would probably cause your head to explode into a million pieces and I don’t want to turn into Jackie Kennedy tonight."
            s "...Got it."

            $ norikosleep = True

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor2sleepover1
            with dissolve

            "Now who do I want to talk to?"

            jump floor2sleepovermenu

        "Uta & Io" if toukasleep and nodokaotohasleep and norikosleep and kandasleep and tsuneyosleep:
            scene black
            with dissolve

            "I notice Uta and Io out of the corner of my eye and make my way into the bedroom to see what they’re up to."
            "However, immediately upon entering the room, I find that their mood doesn’t really match the rest of the inn..."

            scene floor2sleepover39
            with dissolve

            u "Uhhhhh hey, Sensei! Don’t mind us, just...tryin’ to figure out what the heck is goin’ on in here."
            s "What do you mean? "
            i "She means that Yasu’s been just...staring at the wall for like twenty minutes and not moving."
            s "Oh. Yeah, she does that."
            u "Do you...do you know why?"
            s "I think it’s how she prays? I don’t know. I try not to get too wrapped up in religion."

            scene floor2sleepover40
            with dissolve

            i "Should we like...do anything? "
            i "I brought some of my pills. Do you think maybe if we just throw a bunch of them at her, one might work?"
            s "I think she’d need to ingest them, but sure. It’s worth a shot."

            scene floor2sleepover41
            with dissolve

            u "Io! You can’t just throw a bunch of different medications at somebody and hope one works!"
            i "Why not? That’s basically what all of the the[rapist]s did for me and I turned out-"

            scene floor2sleepover42
            with dissolve

            i "Oh. "
            i "Shit."
            i "Yeah, okay. I get it now."
            u "Sensei, I don’t know how I’m gonna fall asleep if she’s in here with us. She’s kinda creepin’ me out."
            s "Again, yeah. She does that."
            s "But, on the topic of sleep...did you guys really agree to surrender me to Noriko?"

            scene floor2sleepover43
            with dissolve

            i "{i}I{/i} didn’t. I wanted you in here with Uta and me so I wouldn’t feel pressured to go out there to see you."
            i "But Uta decided for whatever reason to go along with it. And everyone else basically followed suit after that and just...let it happen."
            u "I just figured...that we’d be staying up really late and that...it wouldn’t matter if it was just the sleepin’ part..."

            scene floor2sleepover44
            with dissolve

            i "It’s whatever...I’ll just wait until tomorrow night and sneak into his room then or something."

            "Well, I’m glad the Noriko thing didn’t get Io down, at least."

            u "You’re not...upset about this, are you?"
            u "I know the whole thing with the sleepover was that we were gonna share you, but like...we still {i}are{/i} sharing you, ya know?"
            u "Just...when the lights go out..."
            u "You'll be with her..."
            s "I’m not upset at all. I was just curious about how that wound up happening because, like Noriko said, that never would have happened so easily with the first floor girls."

            scene floor2sleepover45
            with dissolve

            u "Yeah..."
            u "It probably wouldn’t have..."
            s "…"
            u "…"
            i "We should really do something about Yasu."
            s "I’ll...see what I can do..."

            scene black
            with dissolve

            "………"
            "……"
            "…"

            scene floor2sleepover46
            with dissolve

            s "Uhh...Yasu?"
            ya "{size=-15}It’s dark. It’s dark. It’s dark. It’s dark. It’s dark. It’s dark. It’s dark. {/size}"
            i "What’s she saying? I can’t hear her over that weird funk song blasting in the other room right now."
            t "The song is called “Sweet Vermouth,” Green Onion’s slightly greener friend."
            i "I don’t care what it’s called. I just want Yasu to go to sleep."
            u "We had a mostly normal conversation with her earlier...do you think that might have tired her out?"
            s "Yasu...will it help if I like...give you the light or whatever?"
            ya "{size=-15}There are some things not even the light can repair.{/size}"
            ya "{size=-15}He can’t see. It’s all...just nothing.{/size}"
            ya "{size=-15}Everything is already g-{/size}"

            scene floor2sleepover47
            with dissolve

            u "Uhh...Touka?! Your roommate’s being...your roommate again!"
            to "Yasu-"
            to "Ugh...that girl will be the death of me."

            scene floor2sleepover48
            with dissolve

            ya "{size=-15}When the dust settles, you will find me alone on the rooftop.{/size}"
            ya "{size=-15}In the same place as always.{/size}"
            ya "{size=-15}And if you don’t-{/size}"
            ya "{size=-15}If you make it there and don’t see me, I need you to-{/size}"
            to "Yasu. It’s time for bed."
            ya "{size=-15}I need you...I need you...I need you...{/size}"
            ya "{size=-15}Who do I need?{/size}"
            s "Do you have a trick for when you need to like...break her out of stuff like this?"
            to "I do. But it’s only 75%% effective based on my testing."
            u "That’s better than what we got! Just...give it a shot! I’m startin’ to worry."
            to "Okay...here goes-"

            scene floor2sleepover49
            with dissolve

            to "Boop~"
            s "…"
            i "…"
            u "…"
            s "That’s it?"

            scene floor2sleepover50
            with dissolve

            ya "...Touka?"
            to "Is everything okay? You’ve given a few of us quite the scare."
            ya "I..."
            ya "I’m...thirsty..."
            to "Well, then let’s go get you a drink."

            scene floor2sleepover51
            with dissolve
            play sound "slidedoor.mp3"

            ya "Can I have...a strawberry milk?"
            to "You can have whatever you like, Yasu. Have I told you lately about how insanely wealthy I am?"
            u "Well, heck. I coulda done that."
            i "I guess we...know for the future now?"
            s "…"

            scene black
            with dissolve2

            "I hang out with Uta and Io for a little while longer and several of the other girls begin to filter in as the night goes by."
            "Yasu and Touka return after around twenty minutes or so and Yasu seems to be completely fine."
            "Well, at least by Yasu standards."
            "The only person who doesn’t come into the room, however, is Noriko."
            "And I don’t know if it’s pity or compassion or just flat out obligation...but I feel myself being pushed toward her the moment the lights go out..."
            "………"
            "……"
            "…"

            scene floor2sleepover52
            with dissolve

            s "Are you really going to be the big spoon?"
            n "I like being the big spoon."
            s "But I’m like, twice your size."

            if bonus == True:
                n "That’s why it’s fun. I’ve got so much of you to hold and rub up against that it’s like I’ll never run out."
                n "Also, if I was the little spoon, you’d probably start humping me."
                s "That does sound likely, yes."
                n "Yeah. And it would turn into a whole thing where I’d wind up losing my virginity and being really loud and waking everybody up."
                n "Unless you wanna go back to your room and-"
            else:
                n "True. But it's comforting knowing the huggy boy is so much larger than me. It will make the hugs feel more important."
                s "Call me the huggy boy again. It warms my heart."
                n "You are the huggy boy."

            ki "Noriko, shut the fuck up. I’m trying to sleep."

            scene floor2sleepover53
            with dissolve

            n "No! You shut up! This is a big moment for me!"

            if bonus == True:
                ki "You like Sensei. We get it. Can’t you just sleep quietly or whatever?"
            else:
                ki "He is the huggy boy. We get it. Can’t you just sleep quietly or whatever?"

            n "Aren't you supposed to be swimming right now?!"

            scene floor2sleepover52
            with dissolve

            n "So anyway, where were we?"
            n "Oh right. Spoons."

            if bonus == True:
                n "If you hate being the little spoon that much, just make sure you do an awesome job as the big spoon next time."
                n "And hey, who knows? Maybe I won’t have my pants on then and we'll be in a place where it's actually safe to put it in?"
            else:
                s "Such a great utensil."
                n "They're okay, I guess."

            s "That’s a horrible thing to say to someone right before going to sleep."

            scene floor2sleepover54
            with dissolve

            n "That’s fine. "

            if bonus == True:
                n "I heard that if you go to sleep hard, you’ll have sex dreams. "
                n "Besides, maybe you’ll get lucky and I’ll subconsciously reach my hand down a little too far and give you a sleep-handie or something."
                s "This isn’t helping."

            n "I love you, Sensei."

            if bonus == True:
                s "Noriko, you-"
                s "Oh. Wait. That helped."
                n "Are you telling me you got soft from hearing me say I love you?"
                s "Not soft. Just soft{i}er{/i}."
                n "So mean."
            else:
                s "I will never love anyone who thinks spoons are just {i}okay.{/i}"
                n "Is that so, huggy boy?"

            ki "Noriko, oh my fucking God."

            scene floor2sleepover53
            with hpunch

            n "FUCK OFF, KIRIN! JESUS."

            scene black
            with dissolve2

            "Noriko makes small talk for a while longer, but I eventually find my consciousness fading."
            "It feels strange falling asleep with the arms of someone other than Ami or Ayane wrapped around me, but I guess if anyone was going to be next in line, it’s another girl I’ve known forever."
            "Sure, it would probably make a little more sense if it was her sister instead, but given the...pattern of girls I’ve been seeing, Noriko definitely fits the bill."
            "And even though I’ve been forced into the position of the little spoon, I don’t really feel out of place."
            "Then again, I don’t feel {i}in{/i} place either."
            "I just kind of...feel, I guess."
            "Which is more than I can say most of the time."
            "…"
            "Somehow, Noriko falls asleep before I do."
            "I follow her into the darkness shortly after."

            $ renpy.end_replay()
            $ secondbeach11 = True
            $ molly_love += 1
            $ tsuneyo_love += 1
            $ uta_love += 1
            $ io_love += 1
            $ otoha_love += 1
            $ nodoka_love += 1
            $ touka_love += 1
            $ yasu_love += 1
            $ kirin_love += 1
            $ noriko_love += 1
            stop music fadeout 7.0

            "{i}Your affection with everyone on the second floor has increased by 1!{/i}"
            "………"
            "……"
            "…"

            jump secondbeach12

label secondbeach12:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
label chikalust20intro:
    scene chikawoods1
    with dissolve2
    play music "asobeatsex2.mp3"

    "I follow Chika into the woods."
    "The sound of small sticks and branches cracking underneath her feet gets lost in a cacophony of various insect noises, and I wonder to myself why it is they’re so rowdy in the midst of winter."
    "Or at least what I imagine is the midst of winter."
    "All things considered, it could very well be the tail end as it’s certainly a little warmer now than it was when I woke up this morning."
    "That’s not saying much, though, given that it was still snowing when I left home with the girls."

    c "Hmm hmm hmm~"
    c "Hm hm hm hm hmmm~"
    s "Someone’s in a good mood."
    c "Of course I’m in a good mood. "
    c "It’s exhausting watching you run around with a bunch of other girls when I’m the only one with the privilege of seeing the...more {i}interesting{/i} side of you."

    if bonus == True:
        s "Are you...referring to my penis as “the more interesting side of me?”"
        c "Hey, what can I say? Penises are still brand new to me or whatever."
        c "I can’t help but be curious about the stuff I don’t fully understand yet."
        s "If there is anything you have proven to me so far, it is that you definitely understand my penis."
        c "Heheh~ He’s such a good boy."
        s "Please don’t personify it, though. I don’t know how to feel about that."
        c "Hmm hm hmmm~"
        c "Hmmm hmm hmm hmmmm~"

    "Chika goes right back to humming, leading me further and further into the forest as if she knows exactly where she’s heading."
    "We’re far enough in at this point, though, that I begin feeling a bit uneasy."
    "And even the moonlight crawling in through the trees isn’t enough to really push away the overwhelming darkness surrounding the two of us."

    c "Hmm hmm hm~"
    s "Chika?"
    c "Yeah?"
    s "Would you mind telling me where we’re going?"
    c "Why do you wanna know?"
    s "Because we’ve been walking for a while now and I’m not really in the mood to get lost."
    c "Heheh~"
    c "We need to go far enough that no one will be able to hear you scream."
    s "…"
    s "What?"

    play sound "static.mp3"
    scene chikawoods2 with flash
    stop sound
    stop music


    c "Because I’m going to kill you."
    s "…"
    c "…"
    s "Please don’t."
    c "Don’t kill you?"
    s "Correct. Don’t do that."
    c "Why not?"
    s "The fact that I need to give you a reason is somehow scarier than the prospect of you killing me itself."

    scene chikawoods3
    with dissolve
    play music "asobeatsex2.mp3"

    c "Don’t worry. I wouldn’t actually kill you."
    s "I appreciate that."

    if chika_lust >= 20:
        jump chikalust20
...
```