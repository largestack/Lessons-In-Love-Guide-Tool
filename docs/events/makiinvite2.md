# Special Occasions (Maki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Traveling Lube Dealer](./makiinvite1.md) (Maki) is completed)

* Event [Metal in Microwaves](./halloweentwo13.md) (Main) is completed)



## Next events

None

## Event properties

* Id: makiinvite2
* Group: Maki
* Triggered by label: makiinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->makiinvite->makiinvite2

## Official wiki page

[Special Occasions](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makiinvite2&go=Go) for more details.

## Event code

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label makiinvite2:
    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and wait for her to answer."
    "Seeing as last time she came over we didn’t exactly get to spend too much time together, I’m thinking that today might be a good chance to turn that around."

    if bonus == True:
        "Unless she brings another suitcase full of sexual accessories again. "
        "Actually, if she {i}is{/i} going to bring a suitcase full of sexual accessories again, today is probably the best day to do that on account of Ami being out with some of the other girls."
    else:
        "Unless she brings another suitcase full of lotion again. "

    "I’ll just let Maki field this however she wants to and we’ll see where things go from there."

    play sound "phonebeep.wav"

    if bonus == True:
        maki "Gangbang hotline! Maki-"
        s "Is this just how you answer the phone now?"
        maki "Well, with so many gangs and so little banging, I’m just trying to contribute in the only way I know how."
        s "Cool. Are you free right now?"
        maki "Would you like to set up another lotion sales meeting? I’m still waiting on your [niece]’s initial down payment to get the ball rolling."
        s "I would like to set up a normal get together without any briefcases or short girls with vendettas against taller, attractive women."
        maki "Aww~ You really think I’m tall?"
        s "Are you coming or not?"
        maki "Makotoooooooo?"
        mak "{i}What? What do you want?{/i}"
        maki "I forgot I had an important SALES MEETING tonight. Are you able to watch the store for me?"
        mak "{i}Sure, but...why did you say SALES MEETING like that?{/i}"
        maki "No reason! Love you!"
        maki "Sensei?"
        s "Still here."
        maki "I shall be over shortly. Just have to pack the briefcase."
        s "...Sounds good. "
    else:
        maki "Phone stuff!"
        s "Wanna come over?"
        maki "K!"

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone and begin to walk a little faster than normal on the way home so Maki doesn’t wind up there before me again."
    "Even if Ami isn’t home right now, I’d feel weird about some woman in a vest just hanging out outside of my house when my neighbors...exist."
    "Come to think of it, I’ve never even talked to my neighbors."
    "Or...seen them."
    "But I’d like to keep that up for as long as possible, so...here’s to walking a little faster than normal, I guess."
    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    scene makisecondinv1
    with dissolve
    play music "acoustic.mp3"

    maki "Yo!"
    s "Woah. Look at you."
    maki "Tall, right?"
    s "I was thinking something more along the lines of...handsome?"
    s "Is calling a girl handsome offensive in some way?"

    if bonus == True:
        maki "Not when that girl has pegged her husband more times than he’s pegged her. "
        s "Thank you for reminding me of that. "
        maki "Don’t mention it."
    else:
        maki "To some! But I kind of like it!"

    scene makisecondinv2
    with dissolve

    maki "So, what’s the plan? I was actually feeling energetic enough to put on nice clothes today, so I kinda want to do something out in public so people can see how hot I am."
    s "Just dress like this more often and everyone can see that all the time."

    scene makisecondinv3
    with dissolve

    maki "But getting dressed is haaaaaaard. That’s why I only do it on special occasions."
    s "Special occasions?"

    "Does she think today is...special for some reason?"

    scene makisecondinv4
    with dissolve

    maki "Oh! Uhh...huh."
    maki "I mean...I don’t think it’s...{i}not{/i} special spending time with you?"
    maki "Even though both of my closest friends {i}and{/i} my daughter seem to be closer to you than I am and...woah. Weird."
    s "What’s weird, exactly?"

    scene makisecondinv5
    with dissolve

    maki "Was I...trying to impress you?"
    s "...You don’t know?"
    maki "Not a clue. But I’ve got the suspenders on and I barely ever even broke these out when I was married."
    s "Well...thank you, I guess?"

    scene makisecondinv6
    with dissolve

    maki "{i}Ahem{/i}. Yes, don’t mention it. All in a day’s jerk."
    maki "Err, work."
    s "…"

    scene makisecondinv7
    with dissolve

    if bonus == True:
        maki "I said work. You know, like a blowjob."
    else:
        maki "I said work. You know, like an accountant."
        s "..."

    scene makisecondinv8
    with dissolve

    if bonus == True:
        maki "No, Maki. Bad. {i}Not{/i} blowjob. {i}Normal{/i} job. The less fun kind that end with paychecks instead of cumshots."
    else:
        maki "No, Maki. Stop talking about accountants. He'll think you're schizophrenic."

    s "You doing okay over there?"

    scene makisecondinv9
    with dissolve

    if bonus == True:
        maki "Is it hot in here or do I just want to fuck you?"
    else:
        maki "Is it hot in here or is it just the opposite of cold?"

    s "Well, based on how it’s the same temperature as always in here and...your sudden inner struggle to speak normally, I’m going to guess it’s the latter."

    if bonus == True:
        maki "The nice clothes are beginning to make sense."
    else:
        maki "Fuck, dude."

    if makibj == True or harukalust10 == True:
        if bonus == True:
            s "So...what now? Do we have sex?"
            s "I mean, it would make sense for that to finally happen since we are both adults with a great appreciation for it who just...haven’t done it with each other for whatever reason."
            maki "I will not lie in saying that I am immensely intrigued by the idea of something as large as your penis inside of me. "
            maki "I mean, it also helps that you’re hot, too. But this is really all about the dick."
            maki "It is a very good dick. A real pornstar sized schlong. A big ole baseball bat boner. Just a straight up colossal cock."
            s "…"
            s "Thanks."

            scene makisecondinv10
            with dissolve

            maki "It’s just..."
            maki "I don’t know. It feels weird. You’re my daughter’s teacher."
            s "So...the other stuff wasn’t weird, but actually having sex is?"
            maki "Maybe? I just feel like if Makoto found out, it wouldn’t end well for either one of us."
            maki "I’m sure it’s just a[school]girl crush and that it’ll all fade away on its own...I had one of those too. But like...it would break her heart if she found out about it."
            s "We can just...not let her find out?"

            scene makisecondinv11
            with dissolve

            maki "I think you’re misunderstanding how perceptive Makoto is. I don’t really know if I’ll be able to hide it."
            maki "I’m not that...bright, you know? Like I’m not stupid, I’m just...too open. Or something."
            maki "But {i}my god{/i}, that dick."
        else:
            s "So...do you want me to turn the temperature down or something?"
            maki "Yes. Please do that."

    elif makibj == False and harukalust10 == False:
        if bonus == True:
            s "So...what now? Do we have sex?"

            scene makisecondinv10
            with dissolve

            maki "I...don’t know?"
            maki "This is...weird."
            maki "I mean...I’m sure I knew in the back of my mind that something like this was a possibility when you started inviting me over."
            maki "Not to mention your porn addiction completely revealing that you’re not the more “wholesome” kind of guy."
            s "It’s not an {i}addiction{/i}, Maki. I just go there to hang out with you and your daughter."

            scene makisecondinv12
            with dissolve

            maki "Do you mind if I ignore the daughter part so I can keep living in blissful ignorance that you’re not coming to a porn shop to hang out with my [high_school]er?"
            s "Yes. In fact, I’d prefer that you do just that as mentioning Makoto there was an accident and definitely not why I go there."

            "It looks like our secret lives to fight another day, Makoto. "
            "You’re welcome."

            scene makisecondinv13
            with dissolve

            maki "R-Right! Yeah. Of course you go there to see me. But like...being addicted to porn isn’t bad, you know?"
            maki "I mean, I am! And I’m just fine! It’s not like I’m getting dressed up to go tell my daughter’s teacher I want to have sex with him or anything. "
            maki "Like, who in their right mind would do that?"
            s "Are you going to trick yourself into thinking you don’t want it now?"

            scene makisecondinv14
            with dissolve

            maki "Hah...I don’t know."
            maki "It just feels kind of...wrong. You’re my daughter’s teacher."
            s "And that makes it wrong?"
            maki "It’s wrong because of how she feels about you."
            maki "I’m sure it’s just a[school]girl crush and that it’ll all fade away on its own...I had one of those too. But like...it would break her heart if she found out about it."
            s "..."

            scene makisecondinv11
            with dissolve

            maki "I’m sorry. I’ll stop. I’m taking things too far this time and I apologize."
        else:
            s "So...do you want me to turn the temperature down or something?"
            maki "Yes. Please do that."

    "Well...it looks like the time has come for me to make yet another decision that can make or break a relationship."

    if bonus == False:
        "I had no idea Maki took the temperatures inside of houses so seriously."
        "But if she wants it turned down, then..."
    else:
        "Well, maybe."
        "I think Maki’s interest in sex is great enough that more opportunities may arise, but..."
        "Is that really the relationship I want to have with her?"
        "Makoto’s fragile enough as-is. If she finds out that I’m fucking her {i}mother{/i}, the last person she has left in this city, what will that do to her?"
        "She may act mature, but I know for a fact now that there’s a darker side to her. And converting a playful relationship with her parent into something more is just..."

    scene makisecondinv15
    with dissolve

    maki "I’m, uhh...not liking the sudden silence, Sensei."
    s "Because you’re worried about how it will impact our future?"
    maki "I don’t think much will change with us no matter {i}what{/i} we decide to do here. We’re adults and adults just...do things like this sometimes."

    if bonus == True:
        maki "It’s more that just long stretches of silence make me feel weird, especially when they happen shortly after admitting that I kiiiiiinda wanna fuck my daughter’s teacher."
        s "And I kind of want to fuck my student’s mother."
    else:
        maki "That's right. Sometimes, adults adjust the thermostat."
        s "And other times..."
        maki "They adjust it together..."
        s "..."
        maki "..."

    scene makisecondinv16
    with dissolve

    maki "So...is that it, then? We’re doing it?"
    s "I mean..."

    "I sigh to myself and try to figure out what I want to do here."

    menu:
        "I can’t do that to Makoto":
            if bonus == True:
                s "…"
                maki "…"
                s "We shouldn’t."

                scene makisecondinv17
                with dissolve

                maki "Yeah..."
                maki "Yeah, you’re right."
                maki "No matter how much we want to, we have to think about Makoto."
                maki "We can’t risk breaking her heart just because we can’t keep our pants on."

                scene makisecondinv18
                with dissolve

                maki "But, uhh...that’s just how we are! You know?!"
                maki "Always thinking about dicks and...pussies...and...spontaneous blowjobs under your office desk after I drop Makoto’s lunch off at[school]."
                s "…"
                s "Is it too late to change my choice?"

                scene makisecondinv19
                with dissolve
            else:
                s "…"
                maki "…"
                s "We shouldn’t."
                s "What would Makoto think?"
                maki "Probably nothing. She'd have no idea."
                s "But what if she {i}did?{/i}"
                maki "Good point."

            "Maki goes silent for a moment and makes eye contact with me for longer than she ever has before."

            if bonus == True:
                "And even though the topic at hand is sexual in nature, I feel as if she’s actually trying to connect with me on a level that isn’t just physical this time."

            "I can’t tell what her gaze is saying, but I can feel that there’s a lot more to it than just one more fleeting moment in a life of many for her."
            "How many others has she given this look to in the past? "
            "Am I among the few?"
            "Am I perhaps the only one who’s ever gotten this look?"
            "I don’t know."
            "And, unfortunately, I don’t think I ever will now."

            maki "Yeah."
            maki "It’s too late."
            maki "But we..."
            maki "We can stay friends."
            s "…"
            maki "…"

            scene makisecondinv20
            with dissolve

            if bonus == True:
                maki "But...don’t get mad when I go home and fuck myself to the {i}fantasy{/i} of having sex with you!"
                maki "I can do that as many times as I want and both you {i}and{/i} Makoto can’t do anything to stop it."
                s "I...did not plan on stopping you."
                maki "Rub one out in my honor tonight, would you?"
                maki "Or don’t. I don’t care."

                scene makisecondinv21
                with dissolve

                maki "I’m...uhh...gonna head out, though?"
                s "Already?"
                maki "Yeah...I feel like I might try and make a move on you if I don’t, so..."
                maki "This is for both ours and Makoto’s safety."
                s "…"

                scene black
                with dissolve

                s "I understand."
                s "Have a good night, Maki."
                maki "You too!"
                maki "And...remember to lock the door while you...yeah."
                maki "See ya."

                play sound "dooropen.mp3"

                "Maki exits the house quicker than I’ve probably ever seen her move before, but I don’t really blame her."
                "Things kind of got a little awkward once the two of us decided to cast aside our sex drives in favor of someone who wasn’t even around."
                "It’s...kind of weird, now that I think about it."
                "Since when do I care about what other people think?"
                "And, even weirder, since when do I let that dictate who I do and don’t have sex with?"
                "I don’t know."
                "But..."
                "One thing I do know-"
                "Is that I know who I’m thinking about when I rub one out tonight."

                $ renpy.end_replay()
                $ makiskip = True
                $ maki_love += 1
                $ makiinvite2 = True
                stop music fadeout 10.0

                "{i}A string snaps- but Maki’s affection still increases to [maki_love]!{/i}"
                "{i}Who do you think you’re helping?{/i}"
                "………"
                "……"
                "…"

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat
            else:
                maki "But you can't get mad at me when I go home and change the temperature of my {i}own{/i} thermostat!"
                s "Why would I get mad about that?"
                maki "Because!"
                maki "Anyway...bye!"

                scene black
                with dissolve

                "Maki exits the house quicker than I’ve probably ever seen her move before, but I don’t really blame her."
                "The temperature really {i}is{/i} uncomfortable now that I think about it."
                "Hopefully she doesn't refuse to come over from now on."

                s "..."

                "I wonder if Ami knows how to fix the air conditioner?"

                $ renpy.end_replay()
                $ makiskip = True
                $ maki_love += 1
                $ makiinvite2 = True
                stop music fadeout 10.0

                "{i}A string snaps- but Maki’s affection still increases to [maki_love]!{/i}"
                "{i}Who do you think you’re helping?{/i}"
                "………"
                "……"
                "…"

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

        "Fuck the mother of a girl who’s always there for you" if bonus == True:
            jump makisecondinvx
        "Adjust the temperature and then hug Maki" if bonus == False:
            s "If I turn the thermostat down, will you agree to hug me?"
            maki "I thought you would never ask."
            s "Asking would be weird. I prefer hugs to happen naturally."
            maki "But you literally just asked me if I would agree to a hug."
            s "Do you want the temperature turned down or not?"
            maki "I'm sorry. Please turn the air on. I am melting."

            scene black
            with dissolve

            s "That'll teach you to never mess with me again."

            "I turn the air on."
            "Maki gets cold five minutes later and asks me to turn it back off."
            "Girls are so exhausting."

            $ renpy.end_replay()
            $ makiinvite2 = True
            $ makisex = True
            $ maki_lust += 3
            stop music fadeout 8.0

            "{i}Maki’s lust has increased to [maki_lust]!{/i}"
            "{i}You can now invite her over after[school] and on weekends!{/i}"
            "………"
            "……"
            "…"

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label sadgirls3:
...
```

## Code that triggers this event

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label makiinvite:
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump inviteover
    if makiinvite1 == False:
        jump makiinvite1
    if makiinvite1 == True and makiinvite2 == False:
        jump makiinvite2
...
```