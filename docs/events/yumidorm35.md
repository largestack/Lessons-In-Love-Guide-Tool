# Tech Support (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 35

* Event [Walls Too Thick to Hear Through](./yumidorm30.md) (Yumi) is completed)



## Next events

* [Yumi: Abyss](./yumicallnight35.md)

## Event properties

* Id: yumidorm35
* Group: Yumi
* Triggered by label: yumidorm
* Triggered by branch label: yumidorm
* Triggered by path: yumidorm->yumidorm35

## Official wiki page

[Tech Support](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumidorm35&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm35:
    play sound "knock.mp3"

    "I knock on Yumi’s door, fully expecting to be turned away again as we haven’t really had much contact with one another following my decision to mention her mother."

    y "Thank fucking God! "
    y "Get in here!"

    "Or...I guess I’m going to be hastily invited inside for some reason?"
    "This is new."

    s "Did I knock on the wrong door? Ami, is that you?"
    y "I’m not your fucking weirdo [niece]!"
    y "I need your fucking help with something. I have no idea what I’m doing right now."
    s "Okay but, just to be sure, you’re not holding a gun or anything, right?"
    s "This level of excitement only makes sense from you if you’re getting ready to assassinate me."
    y "I don't have a fucking gun! I’m not that weirdo blonde chick either!"
    y "Are you coming in or do I have to go out there and {i}pull{/i} you in by your fucking collar?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        "I do my best to stifle the erection forming as a result of Yumi’s sudden switch in personalities and open the door."
    else:
        "........."
        "......"
        "..."

    scene yumicomp1
    with dissolve

    "Instead of being on her side of the room like she normally is, Yumi sits with her legs crossed underneath the table and nervously prods at some of the keys on Chika’s laptop."

    y "What the fuck are “sticky keys” and why does this thing keep asking me if I want to turn them on?"
    y "Why would I ever want my keys to be sticky? That sounds gross as fuck."
    s "Just hit no and it should go away."
    s "Why are you on Chika’s computer?"

    scene yumicomp2
    with dissolve

    y "Stupid fucking mall apparently does this thing where you have to apply online to work there, so Chika’s letting me use her thing."
    y "But I fucking hate computers and I have no idea what I’m doing."
    y "So...I need your help."
    s "Does this mean you aren’t mad at me anymore?"
    y "Yeah, sure. Whatever. Helping me with a computer is totally enough to make up for evoking the horrible memories of my absent, junkie mother."

    scene yumicomp3
    with hpunch

    y "NO! I DON’T WANT TO TURN FUCKING STICKY KEYS ON! STOP ASKING ME!"
    s "You’re keeping the buttons pressed down for too long. Just tap them and let them go."

    scene yumicomp4
    with dissolve

    y "…"
    y "You do it."
    s "Do what?"
    y "You type for me. This is stupid and is going to take me all fucking night at this rate."
    s "Sorry, I don’t have Chika’s permission to use her laptop. This is all on you."

    scene yumicomp5
    with dissolve

    y "Oh come the fuck on. I really don’t think she’ll care if it’s you."
    y "If anything, she’ll probably fucking come home and lick her stupid keyboard just knowing you touched it."
    s "That’s totally not creepy at all."
    y "Course it’s fucking creepy. You’re both creepy. The fuck does she even see in you?"

    scene yumicomp6
    with dissolve

    y "Oh! Maybe it’s because you can’t go off and hang out with her mom!"
    y "I’m sure something like that makes a huge difference."

    "Well...she's definitely still mad."

    s "I don’t think it does. I’m friends with several of the girls’ moms."
    y "Of fucking course you are. Real glad to be a part of the club."
    y "Now, are you going to help me or do I have to bash your fucking brains in with this computer?"
    s "Okay but, fair warning, I’m going to have to sit pretty close to you."

    scene yumicomp7
    with dissolve

    if bonus == True:
        y "Whatever. It’s not like your fucking tongue hasn’t been halfway down my esophagus by now."
        s "There is no way my tongue is that long."

    y "It’s fine as long as you don’t try to touch me or some shit."
    y "But, now that I think about it, that’s probably too hard of a task for you."
    y "Maybe I should just fucking wait for Chika or something."

    scene yumicomp8
    with fade

    "I sigh to myself and take a seat next to Yumi, realizing that even if she {i}does{/i} freak out about our sudden increased proximity to one another, that we’ll be able to move past it."
    "That’s basically just how things work at this point."
    "She gets dismissive, I do something shitty, she gets mad, she needs help, I give help, she doesn’t want help anymore, rinse repeat."

    y "Are you going to type or do I still have to do it?"
    s "You have to do it. "
    s "People who are looking to hire someone your age are probably expecting someone with technical experience."
    s "Knowing how to use a computer is an incredibly valuable skill."
    s "Now, click on that bar at the top of the screen."

    scene yumicomp9
    with dissolve

    y "This bar up here?"
    y "Okay...now what?"

    if bonus == True:
        s "Type in “Pornhub.com” and see what comes up."
    else:
        s "Type in “Reddit.com” and see what comes up."

    s "It’s a surprisingly useful resource for-"

    scene yumicomp10
    with dissolve

    if bonus == True:
        y "I’m not going to watch fucking porn with my teacher! Help me or get out!"
        s "If you let me finish, you would have found out that Pornhub is a surprisingly welcoming community full of people who can give great advice and-"
        y "Fuck off! No!"
        y "Why do you even remember the name of a porn site anyway?!"
        y "Don’t you just like...type “boobs” into Google or whatever and then just go to town?!"
        y "Actually, don’t answer that! I don’t want to know."
        s "Right."
    else:
        y "I'm not going on fucking Reddit! I'm horrible with technology and even I understand how much that place sucks!"

    s "Well, if you’re not going to listen to my first piece of advice, drag your cursor over that little box over there."

    scene yumicomp11
    with dissolve

    if bonus == True:
        y "If this is another porn site, I swear to fucking God."
        s "If the mall’s website lists a porn site in their drop down menu for open applications, I am going to quit being a teacher and go work there instead."
        y "Kinda hoping it does now. That sounds like a load off my fucking back."
    else:
        y "If this is some kind of Reddit shortcut, I swear to fucking god."
        s "It's not."

    y "There. I clicked the thing. Now what do I do?"
    s "Select the store you want to apply to from that list."
    y "I don’t know what any of these stores even sell."
    s "What about Chika’s store? They’re listed right there."
    y "I can’t work at the same place as Chika."
    s "Does she not want you there or something?"
    y "I think {i}she’d{/i} be fine with it. But I’ve seen what they sell and shit and there’s no way I’d be able to...contribute or anything."
    y "I’d be way out of place. "
    y "None of that shit would even look good on me anyway."
    s "I don’t think that’s true."
    s "You definitely pull off your winter look really well and that’s not...low class or anything."

    scene yumicomp12
    with dissolve

    y "Are you trying to fucking hit on me right now?"
    s "Not really. Just giving you a compliment."
    y "I don’t want compliments. "
    s "Too bad. "
    s "You’re really cute whether you want me to say that or not."

    scene yumicomp13
    with dissolve

    y "Fuck you."
    y "So...what do I do now? Just choose a random place and apply there?"
    s "I mean, you’d be fine with most things at this point, right?"
    s "Does it really matter which one you apply to?"
    y "I guess not when you put it that way."
    y "What about this one? T-Mobile?"
    s "Horrible letter. Pick something else."
    y "Sprint?"
    s "Why are you only naming cell phone stores?"
    y "I’ve like...been making Chika pay for my phone for a long time now and I feel really bad about it."
    y "So if I could get like, a free phone plan or a discount or whatever it would probably make things easier on her."
    y "I hear those places work off commission too and I’ve got like...experience selling stuff and shit."
    s "I don’t really think it’s necessary to do something like that for Chika."

    scene yumicomp14
    with dissolve

    y "Hey, you might not realize this, but everyone else isn’t made of money, dick."
    y "Chika works her ass off to pay for all three of our phones {i}and{/i} groceries. The fuck do you do?"
    s "The first half of what you just said."
    y "What? The hell does that even mean?"
    s "I pay for all three of your phones."

    scene yumicomp15
    with dissolve

    y "What?"
    s "Yeah. So getting a job at a phone store won’t really help out the way you want it to."
    s "But I guess it would save {i}me{/i} some money so...yeah, go ahead and click on the Sprint application."
    y "Wait wait wait wait wait..."
    y "Are you just screwing with me right now?"
    y "You are, right?"
    y "Why the fuck would you do something like that?"

    if bonus == True:
        y "You’re not making Chika like...{i}do{/i} shit in return for it, are you?"

    s "I blame Chinami. Saying no to a cute girl in a dog helmet is apparently not a thing I can do."
    y "Why include me, though? Why not just pay for those two?"
    s "Don’t ask questions that you’re going to yell at me for answering."
    y "I won’t fucking yell at you this time. I just don’t get it."
    s "It’s because I care about you just as much as I care about them."

    scene yumicomp16
    with dissolve

    y "Oh bullshit! It’s gotta be something else!"

    if bonus == True:
        y "You can like...probably spy on the pictures I take or something! Can’t you?"
        s "…"
    else:
        y "You can like...probably secretly invite me to different apps you play or something! Can't you?!"

    "{i}Can I?{/i}"
    "I’m going to have to look into this."

    s "See? You’re yelling at me."
    y "Because I asked you a serious question and you responded with an outright lie!"
    s "Uh-huh. So anyway, click on Sprint."

    scene yumicomp17
    with dissolve

    y "R-Right. Sure."

    "Yumi’s hands begin to shake as she drags her finger across the trackpad and selects the phone store."
    "Or, I guess it’s possible that they’ve been shaking for some time now."
    "I admittedly haven’t been watching."

    if bonus == True:
        "Not because I don’t want to. I mean, she’s adorable in her pajamas."
        "But because the closer I am to her, the more on-guard she is."
        "And despite this room being her natural habitat, she’s still the prey right now."
        "She understands that. And the moment she feels cornered, she’ll attack."
    else:
        "Probably because I am respectful and kind and she is my student."

    y "Okay. Now what do I do?"
    s "Move to the next column and start typing in your info."
    y "Okay...yeah."
    y "It will probably take me a little while, so...sorry if you get bored or whatever."
    s "That’s fine. I have all night."

    "One by one, Yumi presses down on the keys with her index fingers."
    "She hasn’t memorized where all of the characters are yet, so she definitely takes some time to make sure she gets everything correct."
    "I’m a little surprised she’s managed to make it this far into life without ever really using a computer-"
    "But, then again, when you live your entire life just wandering around the streets, picking the locks on pachinko machines and...buying ice cream or something-"
    "You miss out on certain things that other girls don’t have any issues with."

    scene yumicomp18
    with dissolve

    y "Uhh...can you look away for a second?"

    if bonus == True:
        s "Why? "
        y "This question here..."
        y "The...sex one."
        s "…"
        y "…"
        s "Do you..."
        s "Do you think the application is asking you if you’ve had sex before?"
    else:
        s "Is it because you have forgotten how to spell your name?"

    scene yumicomp19
    with dissolve

    y "Wha-"
    y "No! "
    y "Obviously not!"
    y "I’m not some kind of idiot!"

    "God I love this side of her."

    scene yumicomp20
    with dissolve

    y "I’ll just..."
    y "There."
    y "Done."
    s "..."
    y "..."
    s "You selected “male.”"

    if bonus == True:
        y "Well...yeah. I’m not a fucking lesbian, dude."
    else:
        y "Oh. My mistake."

    s "Wow. This is one of the greatest moments of my life."

    scene yumicomp19
    with dissolve

    if bonus == True:
        y "What did I do wrong this time?!"
        s "Yumi, it’s asking you what sex you {i}are{/i}. Not for your experience or who you'd prefer to fuck."
        s "Are you really that bad at this or are you just trying to get me to fall in love with you?"
    else:
        y "I just clicked the wrong box! Grow the fuck up!"
        s "You are entirely worthless in the face of technology."

    scene yumicomp21
    with dissolve

    if bonus == True:
        y "I’m {i}that{/i} bad, okay?! "

    y "Sorry for being such a fucking moron!"
    s "Don’t worry. I’m sure I sucked the first time I used a computer as well."

    "I obviously don’t think I was {i}this{/i} bad...but I can at least humor her for now."

    scene yumicomp22
    with dissolve

    y "Ugh...whatever."
    y "Can you look away for this part too?"
    s "Your phone number?"

    if bonus == True:
        y "Yeah. I don’t want you sending me fucking...gross pictures at ungodly hours of the day."
        s "Are...there hours that {i}are{/i} okay?"
    else:
        y "Yeah. I don't want you sending me pictures of farm animals."
        s "Can I send you pictures of animals that {i}don't{/i} live on farms?"

    y "Fuck no. Never send me anything ever."
    s "…"
    y "…"
    y "Are you going to look away...or?"
    s "Oh. No. I think I deserve to know your phone number on account of me paying for it and all that."

    scene yumicomp23
    with dissolve

    y "Uhh...isn’t that technically blackmail?"
    s "Blackmail? No. Manipulation? Probably."
    s "I won’t send you any pictures. Don’t worry."
    s "But if there’s an emergency with Chinami or something, I’d like to be able to let you know."
    y "Dick move, using the Chinami card against me. That’s not fair."
    s "Yeah, well, life isn’t fair sometimes. Get used to it."

    scene yumicomp24
    with dissolve

    y "Fine..."
    y "But only cause you pay and shit."
    y "I’m not answering if you just call me to “talk” or whatever."

    $ yuminumber = True

    "{i}Congratulations! You now have Yumi’s phone number!{/i}"

    "Yumi finishes typing in her phone number and slowly begins to move through the rest of the application."
    "She does this for a few more stores with slightly lower standards like fast food places and pet shops before finally deciding to close the laptop and call it a night."

    scene black
    with dissolve2

    "She gets a text message from Chika shortly after that saying that she’s on her way home and, just as I expected, I was subsequently kicked out of the room."
    "But at least today’s visit ended on a much more positive note than the one regarding her mother."
    "Seeing new sides of Yumi is always interesting, especially when they result in the color of her cheeks flushing to the point where they match her pajamas. "

    if bonus == True:
        "I hope to one day see that same level of redness in significantly less wholesome context."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ yumidorm35 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

                    ############################################
                    ##########        ROOM 2          ##########
                    ############################################

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
            if ayane_love >= 30 and dojo30 == True and ayanedorm30 == False:
                jump ayanedorm30
            if ayane_love >= 35 and dojo35 == True and day!= 5 and ayanedorm35 == False:
                jump ayanedorm35
            else:
                jump ayanedormgen
        "Have sex (Missionary)" if ayane_virgin == False and ayanenosex == False:
            jump ayanemissreplay
        "Have sex (Cowgirl)" if ayanelust10 == True and ayanenosex == False:
            jump ayanecowgirlrep

label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
    if sana_love >= 15 and sanadorm15 == False:
        jump sanadorm15
    if sana_love >= 20 and bar20 == True and sanadorm20 == False:
        jump sanadorm20
    if sana_love >= 25 and bar25 == True and beachvacation16 == True and sanadorm25 == False:
        jump sanadorm25
    if sana_love >= 30 and bar30 == True and day != 4 and sanadorm30 == False:
        jump sanadorm30
    if sana_love >= 35 and bar35 == True and day != 4 and sanadorm35 == False:
        jump sanadorm35
    if sana_love >= 45 and thirdreset3 == True and day != 4 and sanadorm45 == False:
        jump sanadorm45
    if sana_love >= 50 and sanadorm45 == True and bar45 == True and sanadorm50 == False:
        jump sanadorm50
    else:
        jump sanadormgen

label sanadorm5:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm:
    if yumi_love >= 5 and streets10 == True and yumidorm5 == False:
        jump yumidorm5
    if yumi_love >= 10 and yumidorm5 == True and yumidorm10 == False:
        jump yumidorm10
    elif yumi_love >= 5 and streets10 == False:
        play sound "knock.mp3"

        s "Hey Yumi, are you in there?"
        "..."
        "There's no answer."
        jump doorknock
    if yumi_love >= 15 and yumidorm10 == True and cafe20 == True and yumidorm15 == False:
        jump yumidorm15
    if yumi_love >= 20 and streets20 == True and yumidorm20 == False:
        jump yumidorm20
    if yumi_love >= 25 and streets25 == True and yumidorm25 == False:
        jump yumidorm25
    if yumi_love >= 30 and streets30 == True and yukidate1 == True and yumidorm30 == False:
        jump yumidorm30
    if yumi_love >= 35 and yumidorm30 == True and yumidorm35 == False:
        jump yumidorm35
...
```