# A Fair Trade (Maki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maki love greater than or equal to 10

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

None

## Event properties

* Id: makidate10
* Group: Maki
* Triggered by label: pornshopmaki
* Triggered by branch label: pornshopmaki
* Triggered by path: pornshopmaki->makidate10

## Official wiki page

[A Fair Trade](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makidate10&go=Go) for more details.

## Event code

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label makidate10:
    scene makifirstbj1
    with fade
    play music "citylife.mp3"

    "I stop by the porn shop to see if Maki is working and, luckily enough, it seems that Makoto has the night off."

    if bonus == True:
        "Either that or she’s in the back room unloading vibrators or something."
    else:
        "Either that or Makoto doesn't actually exist and is just someone I made up in my head."

    "Regardless, it looks like I’m going to get to spend some time with the older Miyamura tonight as long as the younger one doesn’t show up and ruin everything out of nowhere."

    if bonus == False:
        maki "Yo! Mind if I shoot a bunch of euphemisms at you really quick?"
        s "Yes, actually. I do mind."
        maki "Damn."
    else:
        maki "Yo! Long penis, no see."
        s "I think you mean “Long time, no see.”"
        maki "I said what I said."
        maki "How’s it hanging?"
        s "Is that another penis joke?"
        maki "Is that a {i}hard{/i} concept to grasp?"
        s "Okay, Maki. That one was bad. “Hard” is extremely vague and doesn’t always refer to a penis."
        maki "I know that, but it’s not like you have to be a dick about it."
        s "…"
        maki "…"
        maki "Come on. That one was good."
        s "Better than the others, at least."

        scene makifirstbj2
        with dissolve

        maki "So, what brings you in tonight, Sensei?"
        maki "Gangbang stuff? Teen stuff? Maybe this gigantic dildo behind me that I have to sell at a discount because the box was damaged?"
        s "What in the world would I do with that thing?"
        maki "Hey, I don’t know what you’re into. Even my husband got curious about-"
        s "I don’t want to hear wherever this is headed."
        maki "Suit yourself. It’s actually a really funny story."
        s "I’m sure it’s funny for you but I’m pretty sure I’d leave the conversation traumatized."

    scene makifirstbj3
    with dissolve

    maki "Really, though. Why are you here? What do you want?"
    s "...Are you trying to get rid of me or something?"
    maki "No, of course not. You just came straight up to me instead of browsing, so you’re probably not here to buy anything."
    maki "Makoto’s not working tonight. If you’re looking for her, I’m pretty sure she’s back in her dorm."
    s "Am I not allowed to come here to see you instead?"
    maki "I mean, you are."

    if bonus == True:
        maki "In fact, that would make me a little more comfortable than you continuously coming to a porn shop to hang out with my daughter."
    else:
        maki "I enjoy your company and think you're a really nice guy with only the best intentions for both myself and my daughter, a person who actually exists."

    s "Exactly. So why don’t the two of us do something tonight?"

    scene makifirstbj4
    with dissolve

    maki "Sure. We’re kind of dead the first few weeks after Christmas anyway. Everyone’s still playing with their new toys."

    if bonus == True:
        maki "Except Makoto, of course. Darn girl had the audacity to return the present I got her while I wasn’t paying attention."
        s "You...actually bought her a sex toy? I thought you were just joking when you said you were going to do that."
        maki "I don’t see an issue with that sort of gift."

        "Of course {i}you{/i} don't."

        maki "I didn’t get my first toy until I was out of [high_school]. Do you have any idea how much pent up stress I had by then?"
        maki "Do you know {i}anyone{/i} more stressed than Makoto? If there’s anyone that has a use for a vibrator, it’s her."
        s "I can’t tell if you’re a horrible mother or a great one."
        maki "That’s fine. Neither can my daughter."
    else:
        s "I got a train set."
        maki "Aww, that's cute. I'd buy one of those for Makoto, but she was on the naughty list this year."
        s "That just means you're a bad mom."
        maki "Maybe."

    maki "I like to think I’m pretty good, though."
    maki "Like, that whole thing with Makoto getting all weird recently just sort of boiled over after a little while and all I did was talk to her."
    maki "I’m sure you had something to do with it as well, but I’m going to go ahead and take most of the blame since it will make me feel better about myself."
    s "Sure, Maki. Go ahead and-"
    s "Wait, you remember Makoto acting weird?"

    scene makifirstbj5
    with dissolve

    maki "Why wouldn’t I remember that? It’s one of the last big conversations we had."
    maki "I opened up to you about not knowing what to do and you provided some bad advice that made me realize what I {i}actually{/i} had to do."
    s "Yeah, I remember. It’s just Makoto had no idea what I was talking about when I brought it up to her."
    maki "Huh..."
    maki "Now that you mention it, she seemed confused when I said something about it the other day as well."
    maki "Maybe she’s just shrugging it off because she knows we were worried about her?"
    maki "That seems like a pretty Makoto thing to do, right?"
    s "…"

    "There’s definitely something fishy going on, but I can’t tell how much of that is due to the weird reset rules and how much of it is coming from Makoto directly."
    "But if Maki can remember something that Makoto can’t..."

    s "I’m so confused..."

    scene makifirstbj6
    with dissolve

    maki "Yeah, me too."
    maki "But as long as she isn’t acting out or anything like that, all we can really do is keep checking in on her, right?"

    if bonus == True:
        maki "I swear, this whole thing could be solved so easily if her stupid father would stop banging space girls and just come home already."
    else:
        maki "I swear, this whole thing could be solved so easily if her stupid father would stop hugging space girls and just come home already."

    scene makifirstbj7
    with dissolve

    maki "Good thing she’s got you to step in and provide that much-needed dominant male authority she’s always been into."
    s "I think your overexposure to porn has caused that sentence to sound a little different to me than it should have."

    if bonus == True:
        maki "I’m sure adding “dominant” helped with that."
        maki "You thinking about dominating my daughter now, Sensei?"
        s "That’s a loaded question and I am not answering it."
        maki "Good call. I almost caught you."
        s "You won’t trick me that easily."

    scene makifirstbj8
    with dissolve

    maki "Really, though. Thanks for your help with the Makoto situation."
    maki "Without her father being around, it’s a little overwhelming having to step in and just handle everything alone- even if she’s way more independent than she has any right to be."
    s "Don’t worry about it. I’m just doing my job."
    s "I care about Makoto, too. It’s not like I {i}want{/i} her to be sad or anything like that."
    maki "I know. But you still went out of your way to help her. And for that, I owe you one."

    scene makifirstbj9
    with dissolve

    maki "So!"
    s "So what? What’s happening?"
    maki "As special repayment for your assistance in recent matters regarding my Makoto, I will add an additional 20%% to your existing store discount."
    s "Oh."

    scene makifirstbj10
    with dissolve

    maki "Oh what? That seems like a pretty good deal, doesn’t it? That’s almost 50%% off total."
    s "Yeah, it sounds good. I just figured your daughter’s well-being was worth a little more than a 20%% store discount."

    scene makifirstbj11
    with dissolve

    maki "What happened to “don’t worry about it?!” You were so fine with doing this for free a minute ago!"
    s "That was until you insulted me with that 20%% thing."
    maki "Well then what do you want instead? What’s your price?!"

    "Hmm..."
    "Something with equal value to Makoto's well being..."
    "What should I ask for?"

    menu makiblowmenu:
        "A blowjob" if bonus == True:
            jump makibjx
        "A hug" if bonus == False:
            s "One hug, please."
            maki "Like a normal hug or a bro hug?"
            s "Do you consider yourself my bro?"
            maki "Sure. I think it's safe to say we've got a bit of a bromance going on."
            s "I have always wanted a bro. The one I got was kind of a dick."
            maki "Well I am here for you now. Come on, bro. Bring it in."

            scene black
            with dissolve

            "Maki and I have a quick bro hug in which our minds connect and are filled with cool, manly stuff like football and guns. People who like those things are masculine and we are just like them."

            s "Anyway, it's past my bedtime and I have to go home now."
            maki "Aw, shucks. Okay."
            maki "Thanks for dropping by, though."
            s "Thank {i}you{/i} for the hug."

            $ renpy.end_replay()
            $ maki_love += 1
            $ makidate10 = True
            $ makibj = True
            stop music fadeout 5.0

            "{i}Maki’s affection has increased to [maki_love]!{/i}"
            "………"
            "……"
            "…"

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

        "Your daughter’s hand in marriage":
            s "I’ve thought long and hard about this, but-"
            s "There’s only one thing that would truly be worth Makoto’s well being to me."

            scene makifirstbj13
            with dissolve

            if bonus == True:
                maki "Wait a minute...you’re not about to ask me if you can fuck my daughter, are you?"
            else:
                maki "Wait a minute...you’re not about to ask me if you can hug my daughter, are you?"

            s "What? No."

            "Probably because I already have."
            "Sorry, Maki."

            s "I’m asking for her hand in marriage."

            scene makifirstbj14
            with dissolve

            maki "That’s even worse!"
            s "Okay, I’ve decided that you really are a horrible mother."

            if bonus == True:
                maki "Well, yeah! It’s one thing to just pull her aside for a quickie, but you’re asking if it’s okay to...pull her into your heart for a bunch of quickies in the future!"
                s "Okay, well it definitely sounds worse when you put it that way."

            scene makifirstbj15
            with dissolve

            maki "I’m not going to let you marry my daughter...especially while her father is still away."
            maki "Just take your discount and call it a day."
            s "Ugh...fine. Whatever."
            s "I’m not inviting you to the wedding once it happens, though."
            maki "Yeah, yeah. Fine."
            maki "Are we even now, then?"
            s "...Yeah. I guess so."

        "An “upgrade” for the store":
            s "Actually, Maki. There’s something I’ve been thinking this store is lacking as of late."

            scene makifirstbj12
            with dissolve

            maki "Lacking?"
            maki "What are you thinking of exactly?"
            s "Well, you see, this is a porn shop."
            maki "That’s right."
            s "And you know what all good porn shops should have?"
            maki "..."
            maki "Porn?"

            if bonus == True:
                s "I think you should install a glory hole."
                maki "A glory hole? Is that even legal?"
                s "I have no idea."
                maki "I’m pretty sure it’s not."
                s "Well, look at it this way. People have had sex in the store before, right?"
                maki "Obviously. What else do you think the back room is for?"
                s "Just build a box or something then. All you need to do after that is cut a hole in it and call it a day."
                maki "…"
                s "…"
                maki "So, my daughter’s well being {i}isn’t{/i} worth a 20%% discount, but...it’s worth a...glory hole?"
                s "I said what I said."
                maki "I mean...I guess I can...look into it?"
                maki "That’s not something I can just build on my own and it might be hard finding a contractor who has made that sort of thing before."
                maki "But your suggestion has been duly noted."
                maki "Are we even now?"
                s "Yes. We’re even now."
            else:
                s "One of those cool arcade machines with like a million games programmed into it."
                maki "Oooooooh, that would be cool."
                maki "Can you chip in, though? I might be a business owner, but I'm not exactly well off or anything."
                s "No. You have to buy it with your own money or I won't be shopping here anymore."
                maki "Okay, fine. I'll see what I can do."

    scene makifirstbj16
    with dissolve

    maki "Well, then..."
    maki "With that out of the way, I guess it’s about time that I start actually doing some work."

    if bonus == True:
        maki "I need to take inventory tonight and find out what to do with the {i}rest{/i} of the boxless dildos that came in."
        s "There are {i}more{/i} of them?"
    else:
        maki "I need to take inventory tonight and find out what to do with all of the extra copies of Napoleon Dynamite that came in."
        s "Dear god no."

    maki "It’s like a war zone, man. A god...damn war zone."

    scene black
    with dissolve2

    "Maki and I only talk for a short while longer before I take the hint and start heading home."
    "On the way back, I begin to think about what would have happened if I’d asked her for something else."
    "I mean, I liked what I chose a lot-"
    "But I can’t help but feel like I missed an opportunity."

    s "…"

    "Oh well, I guess."
    "It is what it is."
    "I’ll just figure out what to do with the rest of my spare time once I get home."

    $ renpy.end_replay()
    $ maki_love += 1
    $ makidate10 = True
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makibjanim:
        scene black
        with dissolve
        play music "citylife.mp3" fadein 3.0

        if bonus == True:
            "I show up at the porn shop to hang out with Maki and, within a matter of minutes, we get to talking about- you guessed it...porn."
            "She goes on to tell me stories about how awkward it was for her when she started watching things like that."
            "I, of course, struggle to believe this since she is the single most perverted person I have ever encountered."
            "But it's still interesting to think of her long before she turned into the monster she is today."
            "Eventually, we get bored of just talking and she grabs a random DVD for us to go watch in the back room."
            "We get bored of that shortly after as well..."
        else:
            "I show up at Maki's store, immediately hug her, and then leave."
            "She is very impressed by how bold I am"

        if bonus == True:
            jump makibjanimx
        else:

            $ maki_lust += 1
            stop music fadeout 4.0

            "{i}Maki's lust has increased to [maki_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label makiday351:
...
```

## Code that triggers this event

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label pornshopmaki:
    if makiblock == True:
        "I don't really think I should visit Maki right now..."
        jump satnightmenu
    if maki_love >= 5 and makotodorm25 == True and makidate1 == True and bar25 == True and makidate5 == False:
        jump makidate5
    if maki_love >= 10 and christmas7 == True and makidate10 == False:
        jump makidate10
...
```