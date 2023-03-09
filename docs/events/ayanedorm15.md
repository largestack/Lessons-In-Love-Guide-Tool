# First Words
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanedorm15&go=Go)



## Event preconditions
✅Ayane love greater than or equal to 15

✅Event "[Ayane: Less Like the Vulture](./ayanedorm10.md)" is completed (event=ayanedorm10)



## Next events
* [Ayane: Endless Torment](./dojo20.md)

## Event properties
* ID: ayanedorm15
* Group: Ayane
* Triggered by label: ayanedorm
* Triggered by branch label: ayanedorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label ayanedorm15:
    play sound "knock.mp3"

    s "Hey, Ayane. Are you-"

    scene firstwordsredux1
    with fade
    play sound "dooropen.mp3"

    s "...free?"
    ay "Sensei? What a crazy coincidence! I totally haven't been jumping out of my chair every time I heard footsteps in the hall at all."
    s "Well, how lucky of me to have shown up the one time you decided to do that."
    ay "I'll wait until you finish speaking to open the door next time."
    s "I appreciate that. But anyway, do you want to hang out and maybe get some of that obsessive, slightly overbearing energy out of your system?"

    scene firstwordsredux2
    with dissolve

    ay "Heck yeah I do! And for future reference, you don't even need to ask! I {i}always{/i} want to hang out."

    scene firstwordsredux3
    with dissolve

    ay "The only thing is that we can't really hang out {i}here{/i} this time."
    s "Did your air conditioner break or something?"

    if day != 5:
        ay "Huh? No, it’s nothing like that. Sana just fell asleep early."
    else:
        ay "Huh? No, that’s not it. I’ve just been cooped up in there for too long and I want to get some air."

    scene firstwordsredux1
    with dissolve

    ay "Did you want to maybe go for a walk with me, though? We don't normally do stuff at night and I want to know how it feels to go adventuring alongside my future husband."
    s "I will agree only if you stop calling me that."
    ay "That's fine. I guess we can just hang out in the hall instead."
    ay "I just sure hope nobody hears all of the intimate details I am going to loudly bring up in conversation."
    s "Okay then. I guess we're going out after all."

    scene firstwordsredux4
    with dissolve

    ay "Yay! I only needed one threat!"
    s "Just try not to bring up any of those {i}intimate details{/i} outside either. I'm sure it looks bad enough for someone my age to be escorting a school girl in the middle of the night."
    s "The last thing I need is those people also hearing...whatever sort of stuff you planned on sharing."

    scene firstwordsredux5
    with dissolve

    ay "Got it. I'll be on my best behavior."
    s "Can you maybe be on someone else's best behavior instead? Because yours is still a little much at times."

    scene firstwordsredux6
    with dissolve

    ay "Hey! Have some more faith in me! I haven't even tried dragging you into a dark alley yet!"
    s "Do you see now why I asked you to behave?"
    ay "Because you hate fun but you love {i}me{/i} and want to make sure that nothing complicates our already complicated relationship?"
    s "..."
    ay "Yes? No?"

    scene black
    with dissolve
    stop music fadeout 15.0

    s "Let's just go."

    "Ayane and I leave the dorms together and walk a few blocks down the street to an area with a few local businesses- all of which have already closed down for the night."
    "Thankfully, the dorms are located in one of the nicer parts of town, so we're able to move around without ever feeling unwelcome or unsafe."
    "Not that I have much to fear being one of just several males in a world that, at least to me, is full of pretty much all small girls."
    "For Ayane's sake, though, I'm glad."
    "Despite how much she annoys me at times, I'd really prefer to keep her alive."
    "Because not only am I enjoying her presence the more time I spend with her-"
    "But she is very fun to have sex with, and I would like to continue doing that."

    scene ayanewalk1
    with dissolve2
    play music "wewereangels.mp3"

    ay "...and so I told the cashier, ‘I don’t care what the limit is! I’m buying them all!’"
    s "What are you going to do with that many hermit crabs?"
    ay "I don't know. That's a problem for future Ayane. "
    ay "I'll probably just keep them all in my room back at home and ask my butler to look after them."
    ay "Did you know that he has a PhD in neuroscience?"
    s "Then why exactly is he a butler?...And what does that have to do with hermit crabs?"

    scene ayanewalk2
    with dissolve

    ay "Beats me, but I'm glad he's around since I have no idea how I would have survived these last few years without him."
    s "Have things really been that tough over there?"
    ay "They've been things. Let's talk more about hermit crabs."
    s "I'm running out of hermit crab related banter, Ayane."

    scene ayanewalk3
    with dissolve

    ay "Then I guess we'll just have to talk about how much we love each other."
    s "..."

    "Keeping up with Ayane in conversations is always a bit of a struggle."
    "I don't want to say something like {i}she's not normal{/i} when, underneath it all, I think she kind of is."
    "It can just be a little exhausting trying to make sense of her train of thought when mine is constantly running way behind schedule."

    scene ayanewalk3r
    with dissolve

    ay "So, joking aside, how do you like this part of town?"
    ay "You've been spending a lot more time over here lately, so you've got to have at least {i}some{/i} sort of opinion on it, right?"
    s "It's...fine, I guess. Most of my time over here is spent inside of your room, though."

    scene ayanewalk4
    with dissolve

    ay "Well, {i}I{/i} like it here a lot."
    ay "And it might sound a little weird saying this at my age, but I don't think I'd mind spending the rest of my life here if it really came down to it."
    ay "Kumon-mi is kind of like the perfect city, isn't it? New things are always popping up...the weather is always great...and there's this huge sense of community since no one can leave or enter anymore."
    s "Do you have a problem with people from other cities or something?"

    scene ayanewalk3
    with dissolve

    ay "Of course not. I love everyone equally. And besides, Maya comes from outside of Kumon-mi and I'm with her basically every day."
    ay "I just like how we're all kind of...part of something, you know?"
    ay "This is where I was born."
    ay "It's where I met you."
    ay "That alone is enough to make me want to stay here forever."

    "We keep walking as the night grows darker and an abundance of clouds begin to appear."
    "I doubt it will rain since that's just...not a thing I've ever seen around here, but I guess my subconscious disagrees as my own set of clouds begins to take shape within my stomach."
    "A gust of wind attacks us and I catch a whiff of some sort of flowery fragrance Ayane is wearing."
    "I can't pinpoint it, but it has a sort of calming effect that makes me feel like I'm being wrapped in an oversized blanket."
    "The problem with this is that it's the middle of summer-"
    "And this is one of the very few occasions where I would prefer not to be touched."

    scene ayanewalk5
    with dissolve

    ay "Can I ask you a really random question?"
    s "{i}How{/i} random, exactly?"
    ay "Do you remember what your first words were?"
    s "Like, from when I was a baby? Of course not. There's no way I'd remember something like that."
    ay "Maybe {i}you{/i} wouldn't, but your parents probably would."
    ay "I've never heard Ami mention grandparents, though, so I guess finding out might not be possible..."
    ay "If I had to guess, though...I’d say your first word was ‘Mama.’"
    s "And why is that?"
    ay "Maybe because...you’re so good with girls?"
    s "That might be true now, but I can't imagine I was this good with them when I was a baby."
    ay "That's a good point. You've gotta remember that this is just a hunch, though. I am more than willing to accept defeat if you are able to confirm it was something else."
    s "How about you, then? What were your first words?"
    s "You're good with me for the most part. So working off of your logic, wouldn't that mean yours would be like, {i}Dada{/i} or {i}Daddy{/i} or something?"

    scene ayanewalk6
    with dissolve

    ay "..."

    "Ayane becomes uncharacteristically quiet and I immediately recall her mentioning something about the slowly dissipating relationship between her and her father."
    "I don't think she worded it as eloquently as that, but given this reaction, I doubt I'm far off from the truth."

    ay "Um..."
    ay "Yeah..."
    ay "Yeah...I'm pretty sure that...was my first word."
    s "…"
    ay "…"
    s "We can talk about something else now, if you want. I should have thought before saying that."

    scene ayanewalk1
    with dissolve

    ay "Oh, you don’t have to worry about me. I’m okay."
    ay "Just...a little nostalgic."
    ay "But it'll pass."
    ay "In the meantime, though, do you think that we can maybe stop at a convenience store or something? "
    ay "I’m still banned from a few of them, but I'm pretty sure there’s one close to here that we can still buy stuff from."
    s "What exactly did you do to get banned from so many convenience stores?"

    scene ayanewalk7
    with dissolve

    ay "That's for me to know and you to never find out!"
    s "..."

    scene black
    with dissolve2

    "Ayane and I wind up walking around for an hour or two before I bring her back to the dorm."
    "She was perfectly fine for the rest of our outing, so I guess the whole thing with her dad wasn’t as big of an issue as it may have seemed at first."
    "That’s good."
    "I’m not sure how I’d handle seeing Ayane as anything but...{i}Ayane.{/i}"
    "So I'll just...keep trying to avoid that line of questioning for as long as I can."
    "Change is scary, even if it's only temporary."
    "So I'll do everything in my power to change absolutely nothing."
    "And continue to absorb this brand new life- impurities and all."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanedorm15 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanedormgen:
    play sound "knock.mp3"

    "..."

    ay "Come in!"

    scene black
    with dissolve
    scene ayanedormgen
    with dissolve

    "Ayane and I spend the night hanging out in her dorm."
    "She proceeds to tell me all about the 'master plan' she's made for our lives together and I decide to
    go along with it for the sake of conversation."
    "To be honest, there's no way I'm ready to start seriously talking about the future right now."
    "But she looks so happy whenever {i}she{/i} does that it would be borderline painful to stop her..."

    $ ayane_love += 1
    stop music fadeout 5.0

    scene black
    with dissolve

    "{i}Ayane's affection has increased to [ayane_love]!{/i}"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanadormgen:
    play sound "knock.mp3"

    "..."

    sa "Umm...You can come in..."

    scene black
    with dissolve
    scene sanadormgen
    with dissolve

    "Sana and I spend the night hanging out in her dorm."
    "She seems a little more comfortable in here than she does in the bar."
    "The two of us wind up browsing through a bunch of indie games she has on her Xbox to kill some time with."
    "She eventually decides to load up a multiplayer one and proceeds to mop the floor with me in it."
    "I don't mind losing, though, as long as it means she's having a good time..."

    scene black
    with dissolve

    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana's affection has increased to [sana_love]!{/i}"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanemissreplay:
    play sound "knock.mp3"

    ay "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"
    "..."

    if bonus == True:
        jump ayanemissreplayx
    else:
        $ ayane_lust += 1
        stop music fadeout 5.0

        "{i}Ayane's lust has increased to [ayane_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label ayanebjreplay:
        play sound "knock.mp3"
        "..."

        ay "Sensei?! Is that you?"
        ay "I memorized the sound of your knocking!"
        ay "That's you, right?!"

        "I can hear Ayane hop off of the bed and race to the door."
        "She tries to pull it open, but my hand is already on the handle so she can't."

        ay "Hey! I know it's you! Let me open the door!"
        s "Are you going to attack me if I do?"
        ay "Yes!"
        s "..."
        s "Okay, fine. I kind of wanted to be attacked anyway."
        ay "Hooray!"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump ayanebjreplayx
        else:
            $ ayane_lust += 1
            stop music fadeout 4.0

            "{i}Ayane's lust has increased to [ayane_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label sanadorm20:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
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
...
```