# Crazier Things Have Happened (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 30

* Event [First and Second](./dojo30.md) (Ayane) is completed)



## Next events

None

## Event properties

* Id: ayanedorm30
* Group: Ayane
* Triggered by label: ayanedorm
* Triggered by branch label: ayanedorm
* Triggered by path: ayanedorm->ayanedorm30

## Official wiki page

[Crazier Things Have Happened](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanedorm30&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm30:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Ayane’s door and wait for her to-"

    ay "Come in!"

    "...answer."

    ay "That’s you, right, Sensei?"
    ay "I had music on so I couldn't hear the {i}whole{/i} knock, but I muted it as quickly as possible and the part of the knock I {i}did{/i} hear definitely sounded like it came from you."
    s "You’re fucking weird, Ayane."
    ay "Come inside and love me! I look cute right now!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I wonder what she means by looking cute {i}right now{/i}."
    "Ayane is the type of girl to think that she looks cute pretty much all the time, so it probably means she’s trying on a new outfit or just-"

    scene ayanewinterprev1
    with dissolve

    "Completely ready for Christmas?"

    play music "love.mp3"

    ay "Hey!"
    ay "What do you think?"
    s "You look...festive."
    ay "Of course I look festive. I’m getting ready for Christmas."
    ay "It’s already starting to get cold so I was trying on some old stuff to see if it still fits."

    if bonus == True:
        ay "Thankfully, it doesn’t seem like I’ve grown much since last year. "
        ay "My Christmas bra didn’t fit, though, so I’m just wearing my normal one right now."
        s "You had a Christmas bra?"
    else:
        s "I will remain silent for I do not want you to believe you have gained weight."

    scene ayanewinterprev2
    with dissolve

    if bonus == True:
        ay "And underwear. I love Christmas~"
        s "I’m a little upset I don’t get to see exactly {i}how much{/i} you like Christmas."
        ay "I’m sure you will soon enough. I’ve just gotta buy some new stuff and then you can make sweet, passionate love to Christmas-Ayane as much as you want."
        s "So is this just what you’re doing tonight? Playing dress up by yourself and waiting for winter to come around?"
        ay "I {i}was{/i} waiting for you to come around as well, but it looks like that part is finally over."
    else:
        ay "Wow! So kind!"

    s "What would you have done if I didn’t show up?"

    scene ayanewinterprev3
    with dissolve

    if bonus == True:
        ay "Cry and [masturbate], probably."
    else:
        ay "Probably just hang out with my chicken or something."

    s "You live an exciting life, Ayane."

    scene ayanewinterprev4
    with dissolve

    ay "What can I say, Sensei? When God gives you lemons you FIND A NEW GOD."
    s "Cool."
    s "Anyway, have you heard anything else about the dojo situation?"

    scene ayanewinterprev5
    with dissolve

    ay "Huh? Why do we have to talk about depressing stuff while I look like a Christmas elf?"
    ay "These are my happy clothes and we’re supposed to talk about happy things while I’m wearing them."
    s "I did not receive an email or notification about this."

    scene ayanewinterprev6
    with dissolve

    ay "Your notification is coming from the real me right now. "
    ay "Don’t worry about the dojo thingy. I talked to my dad about it and he’s going to see what he can do. "
    ay "Probably."
    s "Did you actually talk to him or are you just saying that?"

    scene ayanewinterprev7
    with dissolve

    ay "…"
    s "…"
    ay "Wanna watch Despacito on loop with me?"
    s "Not particularly."

    scene ayanewinterprev8
    with fade

    "Ayane ignores the fact that I do not want to watch Despacito on loop and sits down at her desk, pressing the play button on a video just seconds later."

    ay "You know, Sensei, it’s kind of rude to pry into other people’s business when it doesn’t concern you."
    ay "I love you so I’m not mad, but you need to be careful about doing that with other people."
    s "How does the dojo thing not concern me? I’m there just as much as you are."
    ay "I know. But what I talk about with my dad doesn’t have anything to do with you."
    s "That’s Ayane-speak for you haven’t been able to ask him at all, have you?"

    scene ayanewinterprev9
    with dissolve

    ay "Come on...I have a hard enough time lying to you as-is."
    ay "If you know I’m not telling the truth about something, you should just let it go for my sake. "
    ay "I already told you there’s no way my dad would agree to something like buying an entire dojo while we already have one."
    ay "And even if he tried to, we'd just be outbid by the Tsukiokas."
    ay "Our only hope is talking that Touka girl out of her decision and I’m pretty sure no one’s ever said no to her in her life."
    s "Well you’re probably right about that. I just don’t see the need for you to lie about something as simple as talking to your dad."

    scene ayanewinterprev10
    with dissolve

    ay "Neither do I, but I keep doing it for some reason. "
    ay "Do you think I’m going crazy, Sensei?"
    s "You’ve been crazy since I met you."
    ay "Good crazy, though. Right? "
    ay "As long as I’m the good kind of crazy, I don’t care."
    ay "But the second I start doing things like using my wealth and influence to solve my problems instead of dealing with them the old-fashioned way, please slap me."
    s "Wasn’t that our exact strategy for the dojo situation?"

    scene ayanewinterprev11
    with dissolve

    ay "At first, yeah."
    ay "But there’s one thing Touka said that’s been kinda popping into my head every now and then and I think it might wind up being our ticket out of this drama."
    ay "Remember when she mentioned that her father might be okay with {i}me{/i} training with her due to our families being kinda rich and stuff?"
    s "Yes. And I also remember her distinctively saying I would not be welcome."
    ay "Right. BUT..."

    scene ayanewinterprev12
    with dissolve

    ay "What if we dress you up in a nice suit and slick your hair back and make you look all rich and fancy and stuff?"
    s "Touka’s already seen the real version of me."
    ay "Oh. True."
    ay "Well, then that just means we’ve gotta win her over by showing her you’re not the peasant she seems to think you are."
    s "But I {i}am{/i} the peasant she seems to think I am."

    scene ayanewinterprev13
    with dissolve

    ay "But you’re {i}my{/i} peasant and I don’t wanna do karate stuff without you."

    if bonus == True:
        ay "It won’t be the same getting all touchy-feely with some other girl instead of you."
        s "Touka’s pretty. I’m sure you’d still enjoy it."

        scene ayanewinterprev14
        with dissolve

        ay "Nope. The only person who is allowed to touch me is you. "
        ay "Anyone else that tries will be getting a swift pro-wrestling style dropkick to the face. And that includes spoiled, rich girls like Touka."
        s "What’s this? Does Ayane Amamiya finally have a real rival other than master Arakawa of the Arakawa clan?"
    else:
        s "Why are you calling me a peasant now? Am I not good enough for you anymore?"

    scene ayanewinterprev15
    with dissolve

    ay "Maybe~ Do you think I should get Todd involved in {i}this{/i} battle as well?"
    s "Only if you don’t mind having a murder charge on your hands."
    ay "At this point, I’d probably accept the risks that come with murder if it means staying together with you."
    s "Are you a yandere now?"
    ay "Call that dojo-thief Touka pretty one more time and I will be."
    s "I will be sure to not do that."
    s "This is kind of weird, though. I don’t think I’ve ever heard you badmouth someone before."

    scene ayanewinterprev16
    with dissolve

    ay "I try not to."
    ay "And I mean, it’s not like Touka is really doing anything {i}wrong{/i}. She just...doesn’t understand other people, I guess."
    ay "If you spend so much time thinking you’re better than everyone, it only makes sense to start naturally believing everybody owes you stuff."

    "That’s something I disagree with entirely."
    "I don’t think there’s any sort of justification for putting yourself on a pedestal, especially one that directly inconveniences others."

    ay "I, like...don’t think she’s a bad person or anything. I’m just really nervous right now."
    ay "If we start having to hang out at my house instead, my dad or Geoffrey will wind up noticing that something’s probably going on between us."

    if ayanelust10 == True:
        ay "And you already know how I feel about risking that after the Kirin incident, so..."

    else:
        ay "I’m all for risky business and whatnot, but probably not {i}that{/i} risky. "
        ay "I’d like to keep my family out of this for as long as possible."
        ay "Or at least until we get married. After that, it’s obviously fine."
        s "…"

    scene ayanewinterprev17
    with dissolve

    ay "A-Anyway, just sitting here and talking about it isn’t going to save us. We need to actually do something or we’re going to be screwed."

    if bonus == True:
        ay "And not the good kind of screwed that ends with our clothes on the floor. The bad kind."

    s "Yeah. I talked to the instructor after you left last time and even {i}she{/i} had no idea what was going on."

    scene ayanewinterprev18
    with dissolve

    ay "Thinking back to what Touka said about how her dad would be hiring the best instructor in Kumon-mi means we’ll probably lose Miss Osaka too."
    ay "We’ll need a new dojo {i}and{/i} a new instructor."
    ay "I don’t know. I’ll look Touka up on Spacebook or something and see if she’s willing to compromise there."
    ay "Maybe she can give us like...just Saturdays to ourselves. Who knows?"
    s "You’re really thinking a lot about this, huh?"

    scene ayanewinterprev19
    with dissolve

    ay "Uh-huh."
    ay "Things haven’t been going well for the Amamiya dynasty lately."
    ay "Damn Tsukiokas. Who would have thought the only family around with more money than mine would do something to directly inconvenience me?"
    ay "What kind of cliche plot development is this?"
    s "I don’t know. Let’s just hope it doesn’t devolve into some sort of class-warfare thing that makes you forget about my existence entirely."

    scene ayanewinterprev20
    with dissolve

    if bonus == True:
        ay "As if I could forget about the man I admired for years and ultimately lost my virginity to."
    else:
        ay "As if I could forget about the man who bought me lemonade that one time so many years ago."

    s "Hey, crazier things have happened."
    ay "That’s right. Like our first Christmas together. "
    ay "Remember that?"

    "God damnit."
    "Every time Ayane brings up something from the past, I feel like I’m going to let her down by not remembering it. "
    "I know that so many of these memories mean the world to her and it’s incredibly irritating that the only ones I can share are the ones we've made during my time here."
    "Don’t get me wrong, I’m all for the vast majority of these memories-"
    "But the wholesome ones like tales of Christmas past or fried-chicken parties are things I’d love to burn into my mind as well."
    "I’m sorry, Ayane."

    s "Would you be able to remind me? My memory’s a little foggy."

    scene ayanewinterprev21
    with dissolve

    ay "Really?! Ami and I have been so embarrassed about it all these years and you...don’t even remember?..."
    s "I’m sure I will once I hear it..."

    scene ayanewinterprev22
    with dissolve

    ay "I don’t even know how you forgot..."
    ay "You know..."

    if bonus == True:
        ay "When you...found the two of us...kissing...and stuff."
    else:
        ay "When you...found the two of us...building a robot with the potential to destroy all human life..."

    "I’m sorry, what?"

    scene ayanewinterprev23
    with dissolve

    ay "B-B-B-But...we were both really little and were just playing around!"

    if bonus == True:
        ay "We both wondered what it would be like to actually kiss for real and...you just happened to walk in at the {i}worst{/i} possible time."

        "Another memory I’m heartbroken to have not inherited."
        "This has been arguably the most devastating one so far."

    s "Right, right."
    s "I remember now."

    scene ayanewinterprev24
    with dissolve

    ay "Y-Yeah...Hahahah..."
    ay "So...that’s proof that... crazier things have definitely happened..."

    scene black
    with dissolve2

    "Ayane and I sit at her computer and she goes on to talk about more Christmas-related memories from our rather extensive past together."
    "I wish that I could have been there for them."
    "But, on the bright side, I’ll likely get to experience my first Christmas with her soon."
    "And I’m sure that will come with several memories we’ll go on to talk about in the coming years."
    "…"
    "If I’m ever able to make it to them."

    ay "Oh, Sensei!"
    ay "Before you go, I have a present for you."
    s "A present?"
    s "What do you-"

    if bonus == True:
        scene ayanewinterprev25
        with dissolve2

        ay "Chu~"

        "Ayane wraps her hands around my neck as I turn toward her and pulls me forward, pressing her lips against mine."
        "I can feel the weight of her body pressing against me as she runs her fingers through my hair. "
        "Our mouths do not open."
        "We do not breathe."
        "We just kiss for roughly seven seconds before splitting apart again."
        "And then we say goodbye."

        scene black
        with dissolve2

        "And then kiss three more times. "
        "Ayane clearly isn’t good at letting me go."

        if day == 6 or day == 5:
            ay "Are you going to come see me tomorrow?"
            s "Maybe. I’ll let you know then."
            ay "Okay~"

        else:
            ay "I’ll see you in[school] tomorrow, Sensei~"
            ay "I’ll miss you."
            s "Just get some rest and I’ll talk to you then."
            s "No stalking the other rich girl on social media."
            ay "You can’t buy me, hotdog man."
            s "What?"
            ay "Nothing."

        ay "Goodnight, Sensei~"
        s "Right..."
        s "Goodnight, Ayane."
    else:
        scene black
        with dissolve

        ay "Here. A new pair of socks."
        s "Rejoice. Socks."

        "Ayane hands me socks. They are fuzzy and warm."
        "I can't wait to wear them."

    $ renpy.end_replay()
    $ ayanedorm30 = True
    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanadorm35:
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
            if ayane_love >= 30 and dojo30 == True and ayanedorm30 == False:
                jump ayanedorm30
...
```