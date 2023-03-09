# Mouthjob
Noriko event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=convenience5&go=Go)



## Event preconditions
✅Noriko love greater than or equal to 5

✅Event "[Noriko: Semi-Constructive Criticism](./norikodorm5.md)" is completed (event=norikodorm5)

✅Event "[Molly: Unpaid Promotion](./mollydorm15.md)" is completed (event=mollydorm15)

✅Event "[Noriko: Nakayarakawayama](./convenience1.md)" is completed (event=convenience1)



## Next events
* [Main: Annabel Lee](./day280.md)
* [Noriko: Kind Of, Yes. Kind Of, No.](./norikodorm10.md)
* [Touka: A Brief Moment in Time](./toukastreets5.md)

## Event properties
* ID: convenience5
* Group: Noriko
* Triggered by label: convenience
* Triggered by branch label: afterschoolmenu

## Event code
File: \game\NorikoEvents.rpy
Code:
```python
...
label convenience5:
    scene norikobreak1
    with fade
    play music "noriko.mp3"

    "I show up at the convenience store to find it completely empty."
    "I steal everything and go home."
    "Just kidding."

    s "…"

    "I do stand there for a mildly concerning amount of time, though."
    "Leaving the counter in a place like this unattended isn’t exactly a good move, especially considering I could reach over and open the register whenever I want."
    "Granted, there are probably cameras installed and I can’t imagine it would be particularly hard to identify someone who looks like me."
    "So I guess I’ll just keep waiting until Noriko shows up."

    s "…"
    s "…"
    s "…"
    s "Okay, I’m done with this. "

    "I turn around to leave and-"

    n "Psst!"

    scene norikobreak2
    with dissolve

    n "Hi."
    s "Did you really just let me stand at the counter that entire time without saying anything?"
    n "I was just admiring that you’re equally as cute from behind as you are from the front."
    n "Also, I thought you’d be smart enough to maybe look behind you once or twice before giving up and going home."
    s "Always look forward, Noriko. Let this be your lesson for the day."
    n "What if somebody taps on my shoulder or something?"
    s "Just keep on walking."
    n "This sounds like bad advice."
    s "It's a lot more motivational without any follow-ups."

    scene norikobreak3
    with dissolve

    n "So...did you actually come here of your own volition today? Or did you just happen to wander in coincidentally again?"
    s "My appearance is very much intentional. I’m here to hang out with you."
    s "Are you on break or something?"

    scene norikobreak4
    with dissolve

    n "I’m pretty much always on break. "
    n "People don’t like to walk around this neighborhood at night, so we’re dead for most of the hours that I'm here."
    n "You should see the place at like 3:00 AM. Total ghost town. Or...ghost store, I guess."
    s "You don’t actually work that late do you?"
    n "Not all the time, but I have in the past. Normally during summer or winter break, though. Just for extra money and stuff."
    s "I applaud your work ethic. I can barely handle the hours I put in at[school]. "

    scene norikobreak5
    with dissolve

    n "I’m sure it’s really taxing for you to just show up and do nothing every day, huh?"
    s "You have no idea."

    scene norikobreak2
    with dissolve

    n "Well, hey. If you ever need any help around the class or anything, I’d be more than willing to lend a hand."
    n "I’m sure you’ve got loads of clerical stuff piling up by now, right?"
    s "Oh, not really. The class rep normally handles all of that for me."
    n "Is she in love with you too?"
    s "Maybe?"
    n "Well that’s just fucking great."
    s "Or maybe not. I don’t know. Please don’t kill her."

    scene norikobreak6
    with dissolve

    n "I’m not going to kill her. It’s just..."
    n "More and more people keep getting in between us and I kind of want them to at least let me catch up first."
    n "Like, I’m way behind in everything except for stuff that you can’t even remember yet."
    s "On the bright side, I’m giving you plenty of time to catch up with how much I’m starting to visit your workplace."

    scene norikobreak7
    with dissolve

    n "Yeah...But do you think that maybe you’d visit me more if I worked a little closer to the dorms?"

    scene norikobreak8
    with dissolve

    n "Oh! How do you think I would look as a maid?!"

    if bonus == True:
        n "Ami and that really short girl with the surprisingly large chest work there, right?!"
    else:
        n "Ami and Uta work there, right?!"

    n "That seems easy enough. And a lot more exciting than sitting around eating prepackaged vegan sushi all night."
    s "I’m actually not sure how you’d look in a maid uniform."

    scene norikobreak9
    with dissolve

    n "Because I’m not girly enough?"
    s "Yes. And no. "
    s "I’ve just never seen you in anything girlier than your pajamas, so it’s hard for me to envision it."

    scene norikobreak10
    with dissolve

    n "I can be girly! "
    n "Let me come over and try on Ami’s uniform. She’ll let me. "
    s "Are you sure about that?"
    n "If she doesn’t, you can hold her down and I can run into her room and raid her closet."
    s "I thought you didn’t like dressing like that? Because of...your expression or whatever it was."

    scene norikobreak11
    with dissolve

    n "Well it would obviously be different if it was for a job. "
    n "Maids are just personas those girls put on to trick gullible men like you into giving them all of your money."
    s "I can assure you that I am fully aware of how greatly I am taken advantage of inside that place. Gullibility has nothing to do with it."
    s "The last thing I need is one more girl who’s able to peer into my soul that effectively."

    scene norikobreak12
    with dissolve

    n "Are you sure about that, Sensei? "

    if bonus == True:
        n "I’ve told you before that I bring both the childhood friend trope {i}and{/i} the little sister trope to the table."
    else:
        n "Wouldn't it be nifty being so close with a girl who can {i}see inside of your heart?{/i}"
        s "Uhhhhhhhhh..."

    scene norikobreak13
    with dissolve

    if bonus == True:
        n "Unless...Onii-chan just doesn’t want to see his sister in a dress because he’ll realize how quickly she’s growing up..."
        n "I’m not the same girl I used to be, Onii-chan. I have...feelings."
        n "I have...{i}needs{/i}."

        "I look down to find that I am already reaching into my wallet for spare change."
        "Damn all of these girls."

        s "As good as I think you’d be at the maid cafe, I don’t see a need for you to relocate just for me."
        n "…"
        s "…"
        n "… "
        s "Noriko?"
    else:
        n "I swear I'd only take a little bite out of it..."
        s "Uhhhhhhhhhhh???????"

    scene norikobreak14
    stop music

    if bonus == True:
        n "Don’t you want to fulfill my needs, Onii-chan?..."
        s "…"
        n "…"
    else:
        n "Am I not allowed to take a bite out of your heart?"
        s "…"
        n "…"
        s "I mean...as long as it's a small one?..."

    scene norikobreak15
    play music "noriko.mp3"

    n "Pfft!"
    n "I can’t keep a straight face anymore, I’m sorry."
    s "You are...actually a pretty good actor."
    n "Oh, stop. A good actor wouldn’t break out in laughter after delivering a line like that."

    scene norikobreak16
    with dissolve

    n "Also...it’s not really acting."

    if bonus == True:
        n "I obviously think of you when...yeah."
        n "But it is kind of embarrassing saying it out loud."
        s "I feel like you’ve said much worse and gotten much less embarrassed."

        scene norikobreak17
        with dissolve

        n "The mood someone is in when they say something greatly impacts the way in which it’s delivered, Onii-chan."
        n "If I’m turned on while I talk to you about being turned-on, I’ll probably be a lot more reserved than I would be if I was feeling totally normal."
        s "Are you...actually turned on right now?"

        scene norikobreak18
        with dissolve

        n "I think this “Onii-chan” thing might be a kink for me."
        n "The more I think about it...the more I..."
        n "…"
        s "…"
        s "Earth to Noriko."
    else:
        s "???????????????"
        s "Noriko wtf stop"

    scene norikobreak19
    with dissolve

    n "Yes! Noriko! Me! Hi!"
    n "What’s up?"

    if bonus == True:
        s "Just trying to figure out how I should handle the horny version of you."
        n "Why would you word it like that?! That’s just going to make it worse!"
        n "Also, I..."
        s "You what?"
        n "I..."
    else:
        s "Do not eat my heart."

    scene norikobreak20
    with dissolve

    n "Job!"

    if bonus == True:
        s "What kind of job?"
        n "Mouth!"
        s "Please don’t call it a “mouthjob.”"
        n "I mean work job! Future! Plans! Help!"

        scene norikobreak21
        with dissolve

        n "I want you to help me think about stuff that doesn’t cause my innocent heart to crave less than innocent things."
        n "Especially while the rice balls are watching."
        s "Are we really back to that?"
        n "They are like children to me."
        n "Tiny, delicious Nakayarakawayamas."
        n "I will destroy anyone who comes close to them."
        s "That will likely be bad for business."
    else:
        s "Yes. You are at work right now. You should attempt to contain your cannibalistic desires as much as possible."

    scene norikobreak22
    with dissolve

    n "Let’s just...talk more about other stuff I can do. Okay?"
    n "Like, I obviously can’t work at a convenience store forever. And if you choose someone else over me, I’ll need something solid to fall back on."
    n "Preferably something where I’ll still have enough free time to dedicate to making you realize you made the wrong choice."
    s "You’re not going to give up on me even if I wind up with someone else?"
    n "I am in...{i}way{/i} too deep to ever do something like that."
    n "Nee-chan, too, probably. "
    n "I guess our whole family is just naturally weak to you for some reason, Onii-chan."

    if bonus == False:
        s "Everyone is weak to me. I am strong and brave and awesome."

    if bonus == True:
        scene norikobreak23
        with dissolve

        n "Oh no! The horny! It’s back!"
        s "There’s no way your whole family is weak to me. Like, what about your parents?"

        scene norikobreak24
        with dissolve

        n "Thanks. The horny is gone again."
        n "I thought about you and my dad and that just..."
        n "Yeah, that’s just not doing it for me."
        s "I would have much preferred if you had used your mother in that fantasy."
        n "But that could like...actually happen."
        n "She loved you just as much as Nee-chan and I did. I don’t think it’s crazy to believe someone her age looked at [teenage]Sensei and thought “You know what? I’m down.”"
        n "My dad, though..."
        s "Please stop bringing up your dad."

        scene norikobreak25
        with dissolve

        n "Oh my God! What if we actually started dating and you wanted to marry me, so like..."
        n "You went to my father to ask him for permission and he was just like..."

        scene norikobreak26
        with dissolve

        n "You can have my daughter...but only {i}after{/i} I test your abilities as a man..."
        n "And then he’d ask you to take your pants off and-"
        s "Wow, would you look at the time? I think I have to get going."

        scene norikobreak25
        with dissolve

        play sound "entrybell.mp3"

        n "Wait, no! I promise I’ll stop fantasizing about you and my dad!"

        cust "…"

        scene norikobreak27
        with dissolve

        n "Oh, hi! I’ll be with you in just a sec!"

        cust "…"

        play sound "entrybell.mp3"

        n "Okay! See you later!"
        s "She left."
        n "She did."
        s "You should probably be careful about what you yell inside of a convenience store."

        scene norikobreak2
        with dissolve

        n "Eh. It’s late. She knew what she was getting herself into when she walked in."
        n "And now {i}she’s{/i} probably adding her dad to some sort of weird sexual fantasy and is going to blame us for it."
        n "Look what we’ve done, Onii-"
        n "Sensei."
        s "…"
        n "…"

        scene norikobreak16
        with dissolve

        n "I didn’t stop myself in time."
        n "The horny returns."
        s "I’m going to have to remember this for when it comes time to choose your lust name."

        scene norikobreak2
        with dissolve

        n "What’s a lust name? It sounds fun."
        s "It’s just a thing. I wouldn’t worry about it until later."
        n "Do I get to choose one too?"
        s "No. You stay out of this."

        scene norikobreak10
        with dissolve

        n "Mmm!"
        s "You do that pouting thing a lot, don’t you?"
        n "It helps me get what I want! "
        n "Or at least it probably would if I didn’t have these “crazy eyes” people keep talking about!"
        n "The failure rate of my pouting suddenly makes a lot more sense!"
        s "Then...stop?"
        n "It’s muscle memory at this point! I can’t!"

    scene norikobreak19
    with dissolve

    n "Oh! I totally forgot to ask you something!"
    s "What’s up?"

    if brony == True:
        if bonus == True:
            n "Is it true that you’re sexually attracted to those cartoon ponies from that one TV show?"
        else:
            n "Is it true that you're a hardcore brony?!"

        s "Did Kirin tell you this?"
        n "It just slipped out, I think."
        s "How does something like that just slip out?"
        n "I don’t know, but I {i}need{/i} to know."
        s "If you {i}need{/i} to know...then, yes. "
        s "I am a proud brony. Tried and true."
        n "Do you have a favorite? I like the one with the hair that’s all like “whoooosh,” you know?"
        s "Ahh, yes. Rainbow Dash."
        n "Yeah, her! Is she your favorite too?"
        s "My favorite pony is whichever one is on screen at the time."
        s "I didn’t realize you were into them, too, Noriko."

        if bonus == True:
            n "Well...I definitely don’t get the urge to fuck them. But they’re totally cute. "
        else:
            n "Yeah! They're great!"

        n "Oh, and have you seen the human versions? They’re like, just as good."
        s "Oh. You’re one of {i}those{/i}..."
        n "...One of what?"
        s "Don’t worry about it."

    else:
        n "Have you ever played Raid: Shadow Legends before?"
        s "…"
        n "…"

        "{i}Hi guys, it’s me! Selebus!{/i}"
        "{i}I just wanted to take a second to tell you about-{/i}"
        "{i}Sike.{/i}"
        "{i}I had you going for a second though, didn’t I?{/i}"

        play sound "static.mp3"
        scene norikobreak19
        with flash
        stop sound

        n "Remember how I was talking about that one super smart girl who beat me in the standardized tests?"
        n "Is there any chance she could move to our class, too?"
        n "She was talking to me about it and apparently she’s already friends with that girl Futaba who sits by the window."

        "Smart girl...friends with Futaba..."

        s "Is her name Nodoka?"

        scene norikobreak2
        with dissolve

        n "Yeah!"
        n "She said that you two met before, but she wasn’t sure if you’d remember her or not."

        if bonus == True:
            s "I have a hard time forgetting girls who talk about seeing other girls naked. I remember her."
            n "I see Kirin naked all the time now. She’s hot."
            s "See? Like, I’m going to remember that for the rest of forever. "
        else:
            s "I remember everyone. I am 75%% magic."

        n "Boy brains are funny."
        s "They’re not funny. They’re just simple. "
        s "Leave us alone."
        n "Never~"

    s "Anyway, I should probably start heading back. "
    s "I really only came over here to see how you were doing."

    scene norikobreak22
    with dissolve

    n "You didn’t need to do that...I know it’s a crazy far walk."
    n "I’m sure Kirin wouldn’t mind if you came over to the dorm to hang out really late, so just do that instead from now on and save yourself some steps."
    s "I don’t know if I like the idea of staying up that late just to come hang out in the dorm."

    scene norikobreak5
    with dissolve

    n "Okaaaaay~ But you’ll be missing a chance to cuddle with pajama Noriko. "
    n "Or pajama Kirin, I guess. But I’m less enthusiastic about you coming over at night to choose her over me."
    s "How about I just...keep doing what I normally do and hope it doesn’t become too annoying?"
    n "That’s fine, too, I guess."

    if bonus == True:
        n "I’ll just go to sleep all alone, without my Onii-chan there to-"

        scene norikobreak15
        with dissolve

        n "{i}Ahh~{/i}"
        n "Why aren’t you stopping me from calling you that?"
        s "Why would I ever stop something as awesome as this? Do it again."
        n "Onii..."
        n "Mm~"

    scene black
    with dissolve2

    if bonus == True:
        "I stay just long enough to watch Noriko squirm in her seat a few more times before deciding to buy a drink and heading back home."
        "She texts me for the next ten minutes or so as I make my way through the dark streets of the second half of town."
        "I’m pretty sure she just wants to keep tabs on me so I don’t get mugged or something like that."
        "She’s a good girl."
        "Probably."
        "She still worries me from time to time."
        "But at least her heart is in the right place-"
        "Tightly wrapped around my fingers."
    else:
        "I sure wish girls would stop flirting with me. I am only going to disappoint them in the end."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ convenience5 = True
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikoinvite1:
...
```

## Code that triggers this event
File: \game\NorikoEvents.rpy
Code:
```python
...
label convenience:
    if noriko_love >= 0 and norikofirsthall == True and convenience1 == False:
        jump convenience1
    if noriko_love >= 5 and norikodorm5 == True and mollydorm15 == True and convenience1 == True and convenience5 == False:
        jump convenience5
...
```