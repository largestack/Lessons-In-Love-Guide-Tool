# Redeemer
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo19&go=Go)


Part of event chain [Falling Asleep Standing Up](./kirinlust30.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwartwo19
* Group: Main
* Triggered by label: kirinlust30intro

## Event code
File: \game\chap3.rpy
Code:
```python
...
label dormwartwo19:
    scene endofsecondwar1
    with dissolve2
    play music "notabluearchivesong.mp3"
    $ totaldays += 1
    $ day -= 6
    hide sunday onlayer date
    show monday onlayer date

    "And so it all comes to an end once more."
    "The girls, with one notable maritime exception, have shed their appropriated (And often times {i}inappropriate{/i}) skin in order to return to their normal forms."
    "And after two full days of seeing them in costumes, it comes as a relief in saying-"
    "Actually, no. I still wish they were in their costumes."
    "But I’m glad this is all wrapping and that I likely won’t have to deal with this much excitement again for a full year."
    "Or at least however long it takes for Kumon-mi’s malformed timeline to reach my fourth Halloween. Which could honestly be like, three weeks at this point. But who knows?"
    "Either way, play time is over. Which means it’s time to get serious and pass out results."
    "And also find out what everyone gets to do with me as the reward this time, which I don’t think has been confirmed as of yet."

    s "Let’s do this."
    ima "Somebody’s really raring to go this morning, huh?"
    s "There’s no time to be gentle when the lives of ten girls are at stake."
    ima "I want to say that no one is taking this contest that seriously but, unfortunately (And rather depressingly) I think you might be right."

    scene endofsecondwar2
    with dissolve

    ima "Alright! Listen up, everybody! In just a few minutes, we’ll be going over the final results for this year’s Super Mega Ultimate Dorm War (Halloween Version)!"
    ima "But before we do that, we have one {i}other{/i} batch of votes we need to go over. And, as I’m sure you already know, those votes are for this year’s popularity contest."
    ima "So if Chika and Otoha could-"
    ima "Wait, where’s Otoha? I don’t see her out there."

    scene endofsecondwar3
    with fade

    r "She didn’t want to come. "
    ima "Seriously? Is she still mad about last night? "
    r "Probably. All I asked was if she was coming or not. We haven’t really {i}talked{/i} yet. "
    ima "Well, I guess that makes things easier to announce then since voting was a total blowout in Chika’s favor."

    scene endofsecondwar4
    with fade

    c "Heh. Of course it was."
    ima "Yup! As it turns out, not showing up to events or campaigning to get votes doesn’t do much to bolster your chances of victory! So...congratulations, Chika! And great job at...being places!"

    $ dorm1war2points += 1

    c "Thank you, Imani. And thank you to everyone who voted for me. I happily accept both my second consecutive Dorm War victory {i}and{/i} my role as the most popular girl in school."
    u "Did you see the full results? Our class was obviously split, but you blew it out of the water with the rest of the school."
    i "Yeah. And I’m sure that has {i}nothing{/i} to do with the fact that Otoha transferred in late and doesn’t know as many people."
    c "It really comes down to just knowing how to talk to the voters. And if there is anything I’m good at, it’s-"
    i "Manipulation? Bribery? Blackmail?"

    scene endofsecondwar5
    with dissolve

    c "Being {i}social.{/i}"
    i "{i}Blech.{/i} Even worse."

    scene endofsecondwar6
    with fade

    ima "Okay! So now that our final contest is all wrapped up...who’s ready to hear the results?!"

    "A small round of applause rings out and attracts a few passersby to stop and observe what’s going on, only to find a crowd of teenagers, a girl in a dolphin suit, and a “foreigner” reading something off of a tablet."
    "Needless to say, the applause does not hold their attention for long. Which is good because I highly doubt they’d understand what’s happening here anyway."

    if harukalust25 == True or kirinlust30 == True:
        ima "Oh, but we {i}do{/i} have some bonus points we need to factor in first, just so we’re all on the same page."

        if harukalust25 == True:
            scene endofsecondwar7
            with fade

            ima "Concerning that matter of Sara Sakakibara representing her daughter and Haruka Hamasaki representing Molly..."
            mo "This is not a matter I had any prior knowledge of."
            sa "Did they...have some kind of rematch behind our back?..."
            mo "Either that or Sir has been hosting some rather unsavory “bonus contests” on GM Island in exchange for additional points. Which of course sounds utterly ridiculous to-"
            sa "Please...stop talking..."
            mo "Yeah, I was just about to."

            if harukabjwin == True:
                ima "One bonus point has been awarded to the second floor!"

                scene endofsecondwar8
                with dissolve

                mo "Mwahahaha...it appears my power is so great that even the Magistrate of Mammaries was able to win on my behalf. "
                sa "And...I guess my mom is just as useless as I am..."

            else:
                ima "One bonus point has been awarded to the first floor!"

                scene endofsecondwar9
                with dissolve

                mo "Tch!"
                sa "My mom...redeemed me..."
                mo "But at what cost, Zagull? {i}At what cost?{/i}"
                sa "I don’t...want to think about that..."

        if kirinlust30 == True:
            scene endofsecondwar10
            with fade

            ima "Concerning the matter of Miku Maruyama vs Kirin Kanda..."
            mi "The what now?"
            mak "It appears that you and Kirin may have taken it into your hands to act outside the jurisdiction of official Dorm War regulations. "
            mi "Uh-huh. But what’s that mean?"
            mak "It means you two had some sort of rogue contest without telling anyone about it. Likely after you left with Kirin last night."

            scene endofsecondwar11
            with dissolve

            mi "That true? What’d we even do?"
            ki "We played Monopoly. "
            mi "But I ain’t ever even played Monopoly before."

            if mikuwarhjwin == True:
                ima "One bonus point has been awarded to the first floor!"

                scene endofsecondwar12
                with dissolve

                mi "How the heck did I manage to win a game I ain’t ever played?! Am I actually kind of amazing?!"
                ki "I kept getting distracted. "
                ki "That’s all it was."

            else:
                ima "One point has been awarded to the second floor!"

                scene endofsecondwar12
                with dissolve

                mi "That ain’t fair! I got talked into playin’ a game I didn’t know how to play! And I don’t even remember any bonus contests!"

        scene endofsecondwar13
        with fade

        s "How did you even find out about the bonus points anyway? "
        ima "Through the app, of course. There’s a special submission page for “Anonymous bonus contests.”"
        s "They’re not anonymous anymore once you start providing names and announcing victors."
        ima "Shh. It’s my first time doing this. You have to be gentle with me."
        s "Just read the rest of the results, Imani."
        ima "Fine, fine."

    scene endofsecondwar14
    with dissolve

    ima "The winner..."
    ima "Of this year’s Super Mega Ultimate Dorm War..."

    if dorm1war2points > dorm2war2points:
        $ dormwar2floor1win = True

        scene endofsecondwar15
        with dissolve

        ima "Is the first floor with a final score of [dorm1war2points] to [dorm2war2points]! Congratulations, guys!"

        scene endofsecondwar20
        with fade

        a "I’d like to thank myself. Ayane. Maya. Dorm 1. Sana. Miku. Dorm 4. And myself again."
        m "I take it that means the truce between you and Makoto has ended?"
        a "That depends entirely on how much she clings to my uncle when we redeem our prize."
        m "And exactly what was that prize again? Because last year, it was keeping Sensei in our room for the beach trip. And this year it’s just {i}Sensei.{/i}"
        m "That’s it. That’s all anyone ever said."
        a "Guess that means he’s ours forever then!"
        m "Trust me when I say this, but that’s the single worst thing you could ever wish for."
        ay "I don’t think it’s that bad."

        scene endofsecondwar21
        with dissolve

        ay "There are always debates about whether eternal life would be good or bad and...I can kind of see both sides in those."
        ay "But spending an eternity with the person you love isn’t ever {i}bad.{/i} It can just...have bad parts? Or something?"
        a "The way you say that makes it sound like you actually {i}are{/i} immortal. "
        ay "Yeah...that would be great, wouldn’t it?"

        scene endofsecondwar22
        with fade

        f "Does winning make you feel any better, Rin? I know Otoha isn’t here to celebrate or anything, but-"
        r "She wouldn’t {i}celebrate{/i} in the first place. She’d just be like “Rin, why are you so excited to win some middle aged dude who probably just wants to fuck you?”"
        no "Sounds exciting to me."
        f "It’s probably just hard for her to understand there’s more to your relationship than that. From an outside perspective...I’m sure a lot of people would think that about you and Sensei."
        r "Well, a lot of people would be wrong. Things are more complicated than that."
        no "Are you implying Sensei {i}doesn’t{/i} want to fuck you?"
        r "I mean...no. He probably does. But that’s not {i}why{/i} we’re close. Or...{i}were{/i} close. I’ve thought about having sex with all of my friends before but that doesn’t mean that’s the only reason I keep them around."
        f "{i}All{/i} of your friends?"
        r "Futaba, do you have any idea how dramatically different my life would be if you liked girls?"
        f "I...try not to think about that."
        no "{i}I{/i} like girls. And boys. And women. And men. And pretty much anything else that can be used in a sexual manner. Which includes your mother- who is currently my new fascination."
        r "I don’t know if I should be more offended that you want to bang my mom or that you put her after “anything that can be used in a sexual manner.”"
        no "Oh, I’m sure I could find plenty of uses for her."
        r "Don’t bang my mom, Nodoka. "
        no "I do what I please."

        scene endofsecondwar23
        with fade

        n "Congratulations, guys. It was a hard fought battle and I think I speak for all of us on the second floor when I say..."
        n "I am extremely jealous and hope these results are overridden by some supernatural force that compels Sensei to come to us instead of you. Also, grr."
        mak "It’s only natural that we won. Your floor is far too spontaneous and disorganized to truly compete for Sensei’s heart as a group."
        mak "You’re like a bunch of solo entities just floating around and trying to take him for yourselves."
        ki "That makes it sound like the first floor is aiming for one giant, loving orgy."
        mi "Well, I can’t speak for Makoto, but-"
        mak "Miku, this is one of those times you probably shouldn’t speak at all."
        mi "Hey, I’m just sayin’ that I wouldn’t mind if Sensei wanted to date all of us so long as we put some kinda schedule together."
        mak "Yes, and that’s exactly what I wanted you to avoid saying."
        mak "The fact of the matter is, and I’m sure I can speak for {i}all{/i} of the first floor when I say this, but..."
        mak "Nana-nana-poo-poo. Sensei loves us more than you. "
        mak "Get wrecked, losers."

        scene endofsecondwar24
        with dissolve

        mi "That’s my Makoto. Only toxic when it counts."
        mi "Happy to have ya back."
        ki "Wish I could say the same..."

    if dorm2war2points > dorm1war2points:
        $ dormwar2floor2win = True

        scene endofsecondwar15
        with dissolve

        ima "Is the second floor with a final score of [dorm2war2points] to [dorm1war2points]! Congratulations, guys!"

        scene endofsecondwar25
        with fade

        ki "Sorry for your loss, Miku. "
        mi "Yeah and {i}I’m{/i} sorry you’re such a butt."
        n "We did it! The second floor prevails! "
        n "But...what exactly is our prize again? Because last year it was the whole rooming thing but this year all I ever heard anyone say was “Sensei.”"

        scene endofsecondwar26
        with dissolve

        n "It’s more than enough! I just want to know what I am and {i}am not{/i} allowed to do and whether or not the rest of you have to be involved or if I can just run away with him."
        ki "I’m fine with you running away so long as you film your first time and send it to me. That’s a thing friends do, right?"
        n "Okay, but you’re not allowed to make fun of me if I cry. "
        mak "You two are kind of disgusting."

        scene endofsecondwar27
        with dissolve

        n "What’s so disgusting about friendship? Are you telling me you wouldn’t let Miku watch your sex tape? Not even for moral support or constructive criticism?"
        mi "If anybody’s gonna be givin’ Makoto constructive criticism on the art of knockin’ boots, it’s gonna be her mom. She knows her way around those kinda tapes."

        scene endofsecondwar28
        with dissolve

        mak "I’m going to the convenience store. Does anyone want anything?"
        mi "Makoto, wait! My phone’s in your pocket!"

        scene endofsecondwar29
        with fade

        mo "Alas, it appears the raid boss known as floor one has been taken down after a mere two days worth of progression. And the loot drop? A large, handsome Japanese man."
        mo "But who will it be that gets to equip him? Will such armor fit in- err...{i}on{/i} any one of us?"
        t "If size is the important factor, I believe I am the one most suited for this job."

        scene endofsecondwar30
        with dissolve

        mo "I’m not even sure if you know what the job entails."
        t "If this is about Virginia, I have been studying so as to not make myself look like a fool."
        t "And with a population of 8.642 million and 44 inches of average annual rainfall, it is safe to say that I know everything there is to know."
        mo "..."
        mo "Yup. You’ve got it, Kendo Princess. You’re ready to become a woman now."

        scene endofsecondwar31
        with dissolve

        t "If only my father were here and healthy enough to hear that."
        sa "Um...congratulations on...winning the Dorm War..."
        mo "No grats needed, Zagull. Tis’ but the fruits of our hard labor ripening and being knocked from the trees like Sunsettias. "
        mo "But while the next chapter in the story of the second floor is still a work in progress, we should go back to that arcade and conquer the escape game once and for all."
        mo "Unless being in the light music club means that you’re also too much of a normie to spend time with me now."
        sa "It...doesn’t..."
        sa "I’d...I’d be happy to go..."

        scene endofsecondwar32
        with fade

        ya "Touka, Touka...All of the girls on our floor look very happy. Is it because Sensei is now our prisoner?"
        to "Something like that, Yasu. I believe the details are a bit hazy at the moment, though. But, that said, we couldn’t have done it without you."
        ya "Yes you could have. There is nothing special about my existence- only what goes {i}through{/i} me."
        to "But the fact that those things go through you at all makes you special, does it not?"
        to "Regardless of what you believe or what anyone may say about you, you’re an essential member of our floor and things would surely fall apart without you."
        ya "Things will fall apart regardless of whether or not I am there to take up space. It is the way the world must move."
        ya "Destroy. Rebuild. And when rebuilding is impossible, create something new. It is this cycle that permeates our daily lives. Drips out of our faucets and-"

        scene endofsecondwar33
        with dissolve

        to "Boop."
        ya "Eep!"

    if dorm1war2points == dorm2war2points:
        $ dormwar2tie = True

        scene endofsecondwar15
        with dissolve

        ima "Is no one!"
        s "Hah..."
        ima "No one wins! It was a tie!"

        scene endofsecondwar16
        with dissolve

        m "Oh well. I suppose Sensei will have to sleep alone for our next beach trip. What a shame."
        a "The winner in the event of a tie should be the first floor! We’ve known him longer and like him more, so obviously we deserve to win! "
        n "Big disagree! Providing a numerical value to express our love for Sensei is inherently flawed due to people having different opinions on what “love” is...but I can guarantee you I sit alone at the top!"
        n "Which means it shall be me, Noriko, who gets to sit on his face. Thank you for coming to my Ted talk."
        a "If anyone is sitting on Sensei’s face, its going to be-"
        ay "{i}Psst. Bad idea.{/i}"
        a "...not me because I am his niece! "
        a "But anyone who so much as tries to needs to take it up with me first so I can say no!"

        scene endofsecondwar17
        with dissolve

        ya "Touka, can I ask you something?"
        to "Always, Yasu. What is it?"
        ya "Why do people want to sit on our teacher’s face?"
        to "..."
        ya "Chairs are not just the instrument we use to sit, but they also rid us of our senses and bring us closer to God in the process."
        to "If that is what you believe...that’s...{i}nice.{/i}"
        ya "But why a human? There are so many other things we can do with humans. Why would you sit on one?"
        to "Um..."
        to "I don’t really-"

        scene endofsecondwar18
        with dissolve

        ya "Wait! I understand!"
        to "I highly doubt that, but please. Proceed."
        ya "An alternative to duct tape!"
        to "Mhm."
        ya "A blindfold of flesh for when the adhesive will not adhere! A means of blinding someone who refuses to blind themself! A means of forcing that person closer to God!"

        scene endofsecondwar19
        with dissolve

        ya "Which means..."
        to "Please don’t, Yasu."
        ya "{i}I must sit on his face as well...{/i}"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene endofsecondwar34
    with dissolve2

    u "Well...it’s all over. The best holiday of the year has finally come to an end."
    u "Memories were made...lives were destroyed..."
    u "But most importantly...we got to see Io in a butler outfit."
    i "Was that seriously the best part of the weekend for you? Because that was probably in my bottom ten."
    c "I’m surprised you stuck around long enough to make any sort of ranking. I feel like we barely saw you at the last Dorm War."
    i "Probably because I find everyone but Uta, Sensei, and sometimes Otoha entirely unbearable."
    c "I take it you didn’t vote for me, then?"
    i "I would have voted for a literal dog over you."

    scene endofsecondwar35
    with dissolve

    c "I’m glad I didn’t have to run against a dog. I might be popular, but I’m not “beat a dog in a popularity contest” popular."
    u "If we do this contest again next year...maybe you should run, Io?"
    i "Run {i}away?{/i} Sure. I can do that."
    u "Run in the contest, obviously. Might be good to show people you’re not just a big ole antisocial jerk. "
    i "But...But that’s exactly who I am."
    u "Yeah, but you’re also really good at faking stuff when you really want to."
    c "If it’s any consolation, I don’t hate you or anything. But I probably wouldn’t vote for you either because of the whole second floor thing."
    i "Wait, why are you even here? Since when do you hang out with us?"
    c "Rin is mad at me and Yumi is MIA. I gravitated toward Uta since she talks a lot. "
    i "Oh. Well, can you gravitate away now? "

    scene endofsecondwar36
    with dissolve

    c "Nah. Not unless Yumi randomly shows up."
    y "I’m Yumi."
    u "Wow. Talk about convenient timing."

    scene endofsecondwar37
    with dissolve

    c "Yumi?! What are you doing here?!"
    y "Have somethin’ to take care of. "
    u "Nodoka, run!"
    y "Not that. "
    c "What do you have to take care of? Because I’m being kicked out of this group and I don’t want to walk around in circles pretending I’m on the phone."
    y "Just gotta have a quick conversation. Five minutes tops. Then we can go get breakfast or some shit. I don’t know."
    y "Wait, don’t you have school today? The fuck you guys doing just hanging out like this?"
    i "Since when does skipping matter to you?"
    c "There’s no class today. Imani got the Dorm Wars labeled as a school-wide holiday so everybody can go home and watch the televised version."
    y "You mean to tell me this shit’s actually televised?"
    c "Yeah. Crazy, right?"
    u "We’ve sure come a long way in just a year."
    y "Aight, well...I guess just keep not fitting in or some shit until I get back. Like I said, won’t take long."

    scene black
    with dissolve2

    c "Okay! Good luck with whatever it is you’re doing! "
    i "Yeah! And please hurry!"

    "........."
    "......"
    "..."

    scene endofsecondwar38
    with dissolve2

    ima "Oh, Yumi. What a surprise."
    y "Yeah, hi. I ain’t here to beat the shit out of anybody."
    ima "That’s good."
    ima "Do you want to hear who won the-"
    y "Nah. Don’t care. Ain’t even really a part of the class anymore. "
    y "Just wanted to talk to the douchebag beside you for a few minutes."
    s "I’m assuming I am the douchebag?"
    y "Do you see anyone around here douchier than you?"
    s "Might I suggest the dolphin to my left?"
    mysdol "Fuck off."

    scene endofsecondwar39
    with dissolve

    ima "Jesus Christ, it speaks?!"
    y "I ain’t talkin’ to a fuckin’ dolphin. Just come with me for a minute. It won’t take long."
    s "Imani...there’s not anything left for me to do, right?"
    ima "Yeah there is. You’ve gotta protect me from the mystery dolphin. I didn’t realize it was {i}intelligent.{/i}"
    y "Ain’t got all day."
    s "Sorry. Protect yourself."

    scene black
    with dissolve2

    ima "Senpai! Be careful! She’s a known assailant!"
    s "I think I can take her."
    y "Yeah, you fucking wish."

    "........."
    "......"
    "..."

    scene endofsecondwar40
    with dissolve2

    s "So...what’s going-"
    y "Listen...I'm just gonna cut right to the chase."
    y "Why’d you just let it happen?"

    stop music fadeout 20.0

    s "..."
    y "You know what I’m talking about."

    if nodokaspecial15p3 == False:
        y "It’s one thing to just sit there with your dick in your hands while a girl gets harrassed — a {i}shitty{/i} thing, I’ll add — but letting that happen to someone you {i}know?{/i}"
        y "Someone you’ve been actually pretty fuckin’ decent to recently?"
        y "Was that all just for fun? "
        y "Did you ever actually want me to get better? Or was that all just some kind of sick game to you?"

    else:
        s "I don’t have an excuse, Yumi."

        scene endofsecondwar41
        with dissolve

        y "Yeah, how the fuck {i}could{/i} you?!"
        y "What kind of shit do you think you can just say to make it feel like none of that ever happened?! Because if there’s some sorta miracle cure you think you can pull outta thin air, I’d love to hear it!"
        s "Yumi-"
        y "I was finally starting to trust you! I thought you were on my side!"
        y "All that shit with...helping me get a job! Helping me study! Genuinely fucking apologizing for the shitty things you’ve done to me! Was that all fake?! Some kind of plot to get me undressed?! To corner me?!"
        y "Is this just a game to you?! Am I a plaything?!"

    s "Nothing about that was or {i}is{/i} a game. I told you back then that I was just as surprised as you."

    scene endofsecondwar42
    with dissolve

    y "Then why?..."
    y "Why did you just freeze?"
    y "You're a fucking {i}adult...{/i}"
    s "..."
    y "Why didn’t you stand up to her?"
    s "Because I didn’t know {i}how...{/i}"
    y "..."
    s "..."
    s "Or maybe some part of me didn’t want to. "
    s "I don’t know."
    y "..."
    s "I’m disgusting, Yumi. "
    s "You know it. I know it. Everyone knows it. It’s not like I try to keep it a secret."
    s "And I’m not just talking about forcing myself on you either. I’m talking about {i}everything.{/i}"
    s "Do you have {i}any{/i} idea how many times I’ve gotten off while thinking about you? Because the number would make you sick."
    y "Why...are you telling me this? That’s not why I-"

    play sound "static.mp3"
    scene endofsecondwar43
    with flash
    stop sound

    s "Because lying to you doesn’t work. And I’m sure you don’t {i}want{/i} me to lie to you either."
    s "I don’t {i}know{/i} why I froze. But I did. And I can’t go back in time and change that, just like I can’t go back in time and change when I kissed you."
    s "Or, I don’t know. Maybe I can. But I don’t {i}want{/i} to because it’s those things that brought us here."
    s "And even if this world is fucked beyond belief and I’m going to repeatedly destroy any hope you’ll ever have in me, I can’t change."
    s "I {i}won’t{/i} change."
    s "But {i}you{/i} will."

    play sound "static.mp3"
    scene endofsecondwar44 with flash
    stop sound

    s "If you want to keep staying away from me, that’s fine. I don’t blame you. "
    s "You’ve already given me multiple chances to redeem myself and I’ve squandered every single one of them."
    s "You can’t trust me. "
    s "You were an idiot for ever {i}thinking{/i} you could trust me after all I’ve done to you."
    s "And the most disheartening part of all of that is I can’t even remember some of it."

    play sound "static.mp3"
    scene endofsecondwar45 with flash
    stop sound

    s "Or maybe I can...but I {i}don't.{/i}"
    s "Maybe I just {i}choose{/i} not to remember because of the way it makes me feel."
    s "But I’d do it all again in a heartbeat because that’s just who I am."
    s "Never count on me."
    s "Never believe in me."
    s "{s}And run away while you still can.{/s}"
    y "But why?..."
    s "Why what?"

    play sound "static.mp3"
    scene endofsecondwar46
    with flash
    stop sound

    y "Why are you telling me this {i}now?...{/i}"
    s "..."
    y "..."
    ay "Uhh...Sensei?"

    scene endofsecondwar47
    with fade

    ay "I think we’ve got a bit of a problem..."

    $ renpy.end_replay()
    $ dormwartwo19 = True

    play sound "eggcrack.mp3"
    scene black

    jump beachmas1

label beachmas1:
...
```

## Code that triggers this event
File: \game\KirinEvents.rpy
Code:
```python
...
mi "No way! I demand a recount!"
            ki "Mm! Thank you...[kirinmaster]...thank you so much!"
            ki "Don’t hold back..I’ll drink every last drop..."
            mi "I woulda studied if I knew this was coming! And no! That metaphor was not intentional!"
            s "That...was a pun..."
            mi "Whatever! Same thing..."
            ki "Pay...attention...to me!"

            "Kirin diverts all of her focus to the end of my cock as she presses it against her tongue, hoping to get a mouth full of semen."
            "Choosing her wasn’t very hard, to be honest."
            "Not only is her technical skill light years ahead of Miku, but she was actually {i}into it.{/i}"
            "And the way she came humming back to life as soon as I called her on her shit was perhaps the best part of my day."
            "But it doesn’t change the fact that she was willing to do something despicable..."
            "That she {i}did{/i} do something despicable...and that I helped her do it."
            "But that’s fine."
            "Because there’s no guarantee Miku will remember this in the morning."
            "And while that doesn’t make taking advantage of her {i}okay-{/i}"
            "It makes it a hell of a lot safer."
            "And I’m already taking advantage of these girls to begin with."

            ki "[kirinmaster]...[kirinmaster]!"

            with sexfade
            with sexfade
            scene thevaliumscene53
            with cumflash
            with hpunch

            ki "Mmngh! Mmnn........mmph......"

            scene thevaliumscene54
            with dissolve

            ki "{i}*Gulp*{/i}"
            mi "Gross."
            ki "I know."
            ki "Perfect for someone like me."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "........."
    "......"
    "..."

    scene thevaliumscene55
    with dissolve2

    ki "Falling asleep standing up."
    ki "If only she’d have done that forty five minutes ago."
    s "Do you regret it?"

    scene thevaliumscene56
    with dissolve

    ki "Do you regret what you did to Molly?"
    s "..."
    ki "..."
    s "I didn’t do anything."
    ki "Yeah."
    ki "And neither did I."

    scene thevaliumscene57
    with dissolve

    ki "Come on, Miku. Let’s get you to bed."
    mi "Hm? Oh...yeah..."
    mi "Night, Sensei..."
    mi "Hope ya...had fun..."
    s "..."

    scene black
    with dissolve2

    s "Goodnight."

    play sound "dooropen.mp3"

    "The two of them exit the room and I remove my phone from my pocket to find a flurry of text messages from essentially everyone."
    "I ask myself if it was worth it as I climb into bed...or if I should try and head back to the bar to see if anything is still happening."
    "But instead-"
    "I find myself wondering if Kirin would be any different if she never met me."

    s "..."

    "I think that she would."

    $ renpy.end_replay()
    $ kirinlust30 = True
    $ kirin_lust += 1

    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
    "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo19
...
```