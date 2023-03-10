# This Town Has Two Halves (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 44

* Event [Walk in the Park](./day38.md) (Main) is completed)



## Next events

* [Yumi: I See You](./streets10.md)

## Event properties

* Id: day44
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day44

## Official wiki page

[This Town Has Two Halves](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day44&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day44:
    play music "blueair.mp3" fadein 5.0
    scene town2_noon
    with dissolve2

    "This town has two halves."
    "There’s the normal half with the[school], the cafe, and the countless other shops and locations where I'm normally content with wasting away my days."
    "And then there’s this half."
    "This half is made up of low-income housing and dilapidated buildings that were once full of life."
    "Now, there’s barely anything."
    "‘How do I know this,’ you ask?"
    "A good question."
    "I feel like just the other day, I was being lectured by my {i}niece{/i} about the variety of locations I'd need to memorize in order to survive here."
    "But this location was omitted from the list."

    if chikadorm10 == True:
        "Instead, I learned about this half of town from Chika."
        "It was the night we watched TV together."
        "I distinctly remember the shape of her thighs and the idea of pulling them apart before bringing her to orgasm with my tongue."
        "Of course, that was all just an idea."
        "None of it ever happened."
        "And that makes me very sad."
        "She should give me permission to perform oral sex on her whenever I want."
        "I think it would bring the two of us closer together."

    else:
        "Thankfully, I remembered it all on my own today."
        "Or...at least it feels like I remembered it."
        "It's hard to recollect memories you've never had in the first place, but much easier to collect the ones that someone else let slip out of their hands."
        "That's precisely what happened with my name- another seemingly important detail about myself that I'm unable to remember."
        "But that’s okay."
        "Being Sensei is easier."
        "And I will hold onto that thought for dear life, for I'd feel simply horrible if someone were to have to pick up after me."

    s "I wonder if there’s anything to do around here?"

    "I speak to myself while kicking a rock down the street."
    "I told Ami I had plans today, so we weren’t able to go home together."
    "Of course, my ‘plans’ consisted of getting mildly lost in unfamiliar territory, waiting for something to cross my path as if to say ‘You’re finally here.’"
    "But after an hour or so of wandering around this place-"
    "I’m not anywhere."

    scene theskyisgod
    with dissolve2

    "No one is anywhere."
    "At least not in this half of town."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    y "Ah-"

    scene yumi1
    with dissolve2

    y "What are you doing here?..."

    "A girl sits with her back pressed against a wooden barrier constructed to prevent people from falling to their deaths."
    "I suppress the urge to push her over and respond."

    s "Hey, Yumi. Nice to see you."
    y "No it ain't. And I asked you a question, numnuts. {i}What are you doing here?...{/i}"
    s "Just...walking around. Is that a problem?"
    y "Yeah...it is. You’re not supposed to be here."
    s "I’m not? Why?"

    scene yumi2
    with dissolve

    y "Because there’s no fucking reason for you to be here...and there will never {i}be{/i} a reason for that in the first place."
    y "The fuck even is this? Don't tell me you're stalking me again or some shit, because I swear to-"
    s "I wasn’t stalking you...Besides, how would I have even known you were here? You didn't show up to school today."

    scene yumi3
    with dissolve

    y "That ain't ever stopped you from finding me before."

    "A moment of silence climbs up the wall behind Yumi and slips in through the barrier, wrapping itself around her legs and forcing her to pause for a moment as her mind figures out how to dispose of it."
    "I should be afraid, yet I am too caught up in envying the intangible being as I, too, wish to be wrapped around Yumi's legs."
    "There are many things I wish to do to Yumi. There are many things I wish that she would do to me."
    "If only I could turn invisible."
    "If only I could twist myself into vines."

    y "You...don't even know {i}why{/i} I'm here, do you?"
    s "Why would I?"
    s "I don’t know anything about you...let alone why you’d be hanging out in the middle of nowhere right before nightfall."
    s "That can be easily changed, though. It just requires you actually...you know, talking to me."

    "Yumi, who appears to be on the verge of slipping into an uncharacteristic bout of despondency right now, takes a moment to ponder over something."
    "When she speaks again, her voice is an octave or two lower than normal."

    y "I..."
    y "I've got my reasons, okay?"
    y "I’m going back to the dorms soon, so just..."

    scene yumi2
    with dissolve

    y "This place turns to shit after dark, so you should probably get out of here too."
    s "You're not worried about me, are you?"

    scene yumi4
    with dissolve

    y "Fuck no I’m not worried about you! I'm just tryin’ to be nice so you don't wind up fuckin' mugged in some alley on the way back home!"
    y "But if you’re gonna be a fucking prick about it then whatever! Stay! See what I care!"
    s "I’m not trying to be a prick, I was just-"
    y "..."
    s "..."
    y "Just what, asshole?!"

    "Something Chika said in the classroom the other day rings out in my head like thunder and spooks me into allowing it to cross my teeth and find its way back to Yumi."

    s "Is...everything okay with you?"
    s "Like...is there actually something you need help with? Or..."

    scene yumi5
    with dissolve

    y "Huh?..."
    s "Is that a yes or a no? Because I really don't mind."
    s "I know that we're not on the best terms, but-"

    scene yumi6
    with dissolve

    y "You're right. We're {i}not{/i} on the best terms."
    y "And everything is definitely not {i}okay.{/i}"
    y "You piss me the fuck off...and it pisses me off even more that you don’t understand that."
    s "It's not {i}my{/i} fault that you act so...abrasive all the time, is it?"
    y "Maybe not entirely, but you sure as hell don't help at all."
    s "Then let me help you now...because it's not like I can help you in school when you haven't even shown up over the past two weeks."

    scene yumi7
    with dissolve

    y "See, this is the exact sort of bullshit that pisses me off!"
    y "You’re like...two different people, dude!"
    y "Some days, you pretend to be all caring and shit...and then other days you’re fucking...sneaking around and..."

    scene yumi6
    with dissolve

    y "...Ugh. Just fucking forget about it."
    y "I already said too much."
    s "…"

    menu:
        "Pry":
            s "Tell me."

            scene yumi7
            with dissolve

            y "And why the fuck should I? So you can make fun of me for blowing things out of proportion?"
            y "Is that what you want?"
            s "No. I just want you to actually tell me something for once."
            s "I don’t know why you think I’m always out to get you, but I can guarantee that isn’t the case."
            s "In fact, I couldn’t really care less about-"
            y "Jesus Christ, okay! I’ll fucking tell you if it will get you to stop being all sappy and shit!"

            "Well...if it works, it works."

            scene yumi7r
            with dissolve

            "Yumi pauses for another moment, swallowing her pride as she-"

            y "I saw you this weekend, you know."
            s "Saw me doing {i}what{/i} exactly?"
            y "Goin' on some cutesy fucking date in the park with that blindly loyal teacher's pet of yours."
            s "Makoto? You saw us?"

            "Was Yumi in the park that day?..."

            y "Might wanna bring a leash next time. Would be a problem for you if a bitch as thirsty as that ran off and started humping somebody else in public."
            s "It's not like that, Yumi. We just bumped into each other, that's all."
            s "I don't get why this would even matter to you anyway."

            if bonus == True:
                scene yumi4
                with dissolve

                y "It {i}matters{/i} because you’re way too fucking old to be hanging out with your goddamn students in your spare time! Let alone going for romantic walks in the park with them!"
                y "Are you two fucking?"
                y "Is that what's going on?"
                y "Cause God knows she’d be all for it. That girl's had her mind on your dick since the first time you walked into the classroom."
                y "And with the way you look at literally {i}all{/i} of us I can’t imagine you wouldn’t jump all over her the second the opportunity arose."
                y "It’s fucking creepy, dude! And what makes it even creepier is that everyone seems to be {i}okay{/i} with it except me!"
                s "Why aren't you okay with it, Yumi?"
                y "Because there is no fucking world where any of this would be okay! We're in fucking high school and you're a goddamn adult! You should start acting like one!"
                s "Big words from the most childish person in the class."

                scene yumi7r2
                with dissolve

                y "Excuse me?"
                s "Am I wrong? I know I might not be acting my age, but you're not acting yours either with your constant need to make other people feel smaller than you."
                y "Do you not understand why I'm telling you this shit right now? If you don't listen to me, you're going to wind up fucking-"
                s "You know what I think the problem is?"

                play sound "static.mp3"
                scene yumis4 with flash
                scene yumi7r2 with flash
                stop sound

                s "I think the problem is that you wish {i}you{/i} were in Makoto's place at the park."

                scene yumi7r3

                y "Is that really what you think?"
                s "What other reason would you have to get so jealous about seeing the two of us together?"
                y "It wasn't jealousy, asshole...you have any idea what kinda shit being caught with someone like you could do to that girl's future?"

                play sound "static.mp3"
                scene yumis4 with flash
                scene yumi7r4 with flash
                stop sound

                s "What would you have done if you saw something else happen, Yumi?"

                play sound "static.mp3"
                scene yumis4 with flash
                scene yumi7r2 with flash
                stop sound

                s "What if you saw us kiss?"
                y "What would I {i}do?{/i} I'd fucking puke. That's what."
                s "Really?"
                y "Yeah. Really. Now stop being such a fucking creep and-"

                play sound "static.mp3"
                scene smile with flash
                scene yumi9 with flash
                stop sound

                y "Wha-"
                y "What the fuck do you think you're doing?!"

                "I compulsively grab Yumi’s face and begin to pull it toward mine."
                "She resists. But I know that deep down, she doesn't want to."

                s "Isn't this what you want?"
                y "Fuck no this isn't what I want! Get the fuck off of me!"
                s "What's wrong? You don't have to be jealous anymore."
                s "I'm looking at you and you only right now."
                y "I fucking told you, already! I was never jealous!"
                y "You want to fuck the class rep in your free time?! Go for it! But leave me the fuck out of it and don't do shit where people can see you! It's disgusting!"
                s "Are you afraid of people seeing {i}us{/i} right now?"
                y "I'm afraid of {i}you,{/i} dipshit! Let go!"
                y "You're lucky I'm not screaming for help!"

                jump restofyumibridge

        "Leave her alone":
            if bonus == True:
                stop music
                play sound "static.mp3"
                scene yumis1
                with flash
                scene yumis2
                with flash
                scene yumis3
                with flash
                scene yumis4
                with flash
                scene yumis5
                with flash
                scene yumi9
                stop sound
                play music "blueair.mp3"

                y "Wha-"
                y "What the fuck do you think you're doing?!"

                "I compulsively grab Yumi’s face and begin to pull it toward mine."
                "She resists. But I know that deep down, she doesn't want to."

                s "..."
                y "Yo, what the fuck is this?! What do you think you're doing?!"
                s "..."
                y "S...Seriously! Get the fuck off of me! Don't just...fucking stare at me like that!"
                s "..."

                scene yumi9r
                with dissolve

                y "Is this, like...fucking blackmail or something? What are you doing? What do you want?"
                s "..."
                y "I..."
                y "I'll stop being mean to Futaba! I'll stop being mean to everyone! Just don't fucking touch me anymore, got it?!"
                s "..."
                y "..."

                "For the first time, I see fear in Yumi's eyes."
                "I then see my reflection in them as they begin to fill with tears."
                "Her skin is softer than I thought it would be."
                "She's more fragile than she portrays herself."

                y "Please...don't..."
                s "Isn't this what you want?"

                scene yumi9
                with dissolve

                y "Fuck no this is not {i}what I want!{/i} How delusional are you?!"
                s "It would hurt if you fell from here, wouldn't it?"

                scene yumi9r
                with dissolve

                y "What?..."
                s "I'm just making an observation."
                s "The drop looks quite far."

                play sound "static.mp3"
                scene smile with flash
                scene yumi9r2
                stop sound

                y "For the last time, let me go!"
                s "I'm sorry."
                y "Help! Someone!"

                jump restofyumibridge

label restofyumibridge:
    s "Go on. Scream for help. There's no one around."
    y "Let...go!"
    s "I can't."

    scene yumi9r3
    with dissolve

    y "The fuck do you mean you can't?!"
    s "I just...can't."
    s "There's..."
    s "Something..."
    y "Just...get off of me and I'll forget you ever did this! Okay?! We all win that way...right?!"
    y "I...I have to get back to the dorm anyway! Chika is waiting and I-!"
    s "I don't care."

    "Yumi's eyes widen as they connect with mine."
    "Her pupils rapidly bounce between the surrounding areas and me, desperately looking for a way out."
    "But I am much stronger than her."
    "She is mine until I let her go."

    scene yumi10
    with dissolve

    y "Why?..."
    y "Why are you doing this?..."
    s "..."
    s "I don’t know."

    "It’s a shitty answer, but it’s sincere."
    "I {i}don’t{/i} know why I’m doing this."
    "I just am."
    "And..."
    "I can't bring myself to stop."

    s "Have you ever kissed a boy before?"
    y "Don’t...please..."
    s "Answer the question, Yumi."

    scene yumi11
    with dissolve

    y "LET GO OF ME, YOU FUCKING RAPIST!"
    s "Aren’t you supposed to be strong?"
    s "Weren't you supposed to rip my dick off if I ever got close to you?"
    s "It's right there, Yumi. Can you feel it pressing up against you?"
    s "All you have to do is reach down."
    s "Reach down and rip it off."
    y "I...FUCKING CAN'T!"
    y "YOU'RE TOO...STRONG!"

    "Yumi’s resistance strengthens, but it's still not enough."
    "Her mouth opens wider every few seconds to breathe as the sudden onslaught of suppressed tears causes her nose to become congested."
    "I will help her breathe."
    "I will keep her alive."

    play sound "static.mp3"
    scene yumi11r with flash
    stop sound

    s "You are so beautiful."
    s "The list of things I want to do to you would carry on for years."
    y "Please...stop it..."

    "Yumi's right arm goes limp. Her left arm serves as the final barrier I must break through on the way to her tongue."

    play sound "static.mp3"
    scene yumi12 with flash
    stop sound

    "It shatters easily, like the windows of a car colliding with the asphalt over and over and over again as it rolls repeatedly down the road."
    "Over. And over. And over. And over. And over. And over."
    "Rolling forever."
    "Forever and ever and ever."
    "And ever and ever and ever."
    "Strange."
    "Yumi's tongue feels a lot like a slug."

    y "Mmf-"
    y "Nmmmm....mm...mmm...nnmm..."
    y "Mmm..."

    "She fights back against my kiss, but it's a weak fight as I must have already eliminated her resolve."
    "How unfortunate that her first had to be taken under such unfortunate circumstances."

    y "Mmnch...mmf...ammmn......"

    scene yumi13
    with dissolve

    "I can feel her eyes attempt to connect with mine, which is very strange considering mine have been closed for quite some time."
    "Things like that have always interested me- how you can feel a gaze despite there being no tangible aspect to it."
    "I wonder what she'd try to communicate with me if I looked back at her."
    "And I wonder why she hasn't attempted to communicate it with her tongue instead."
    "Her struggling has all but subsided as I spread my saliva throughout her mouth."
    "All she can do at this point is wait for me to finish."

    scene yumi14
    with dissolve

    y "Mmf!...mmm...ngh...mmm...nhhh!"

    "Or start kissing back."

    y "Mmf...mmmm!...Mnnch! Mmmm!"


    "It's hard to tell if it's out of pity or hormones, but her tongue eventually starts moving as well."
    "It's clumsy and slow, but I wouldn't expect much more out of a slug."
    "I don't know how long this goes on for."
    "But I know that by the time I let go, I need to fully dedicate myself to not bending her over the barrier and violating her even further."

    scene yumi15
    with dissolve

    y "Pah...hah...hah...ahh..."
    s "..."
    y "Why?..."
    y "Why?..."
    y "Why...why...why?..."
    s "..."
    y "I..."
    y "I fucking hate you..."
    y "I’ll never understand what anyone sees in you..."
    y "You’re no different from every other guy on this fucking planet, are you?..."
    y "You don’t actually care about anyone..."
    y "You’re just trying to fuck us..."
    y "That's...seriously all it is..."
    s "…"
    y "I won’t forget this, you know....You’ll be lucky if the police aren't knocking on your door by the end of the night."
    s "…"
    y "Why?..."
    y "Why aren’t you saying anything?..."
    s "This wasn’t supposed to happen."
    y "..."
    s "This..."
    s "This was an accident."
    y "An...accident?..."
    s "Yes."
    y "..."
    s "..."
    y "Then fucking let me go..."

    scene black
    with dissolve2

    "I look over the barrier once more."
    "The drop isn't as high up as it initally seemed."
    "........."
    "......"
    "..."

    scene yumi17
    with dissolve2

    y "..."
    y "..."
    y "..."
    s "Yumi-"
    y "Don't..."
    y "Don't say anything."
    s "..."
    y "I just don’t get it..."

    scene yumi18
    with dissolve

    y "I don't understand you at all..."
    s "..."
    y "..."

    play sound "static.mp3"
    scene yumi19 with flash
    stop sound
    stop music

    "Yumi takes off down the street and I’m left standing in the middle of the road with her tears on my jacket and precum soaking the front of my boxers."
    "I don’t think I should come to this half of town anymore."
    "I think that only bad things will happen here."

    scene black

    "I think that only bad things will happen here."
    "{i}Oh no! It looks like you’ve left an emotional scar on Yumi!{/i}"
    "{i}You are a horrible person!{/i}"
    "{i}But that's okay!{/i}"
    "{i}Nothing is real!{/i}"
    "{i}None of this ever happened!{/i}"
    "{i}Now, go back to being happy!{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ day44 = True

    jump endofweekday

label day48:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
...
```