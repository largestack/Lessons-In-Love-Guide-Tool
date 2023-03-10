# Cute Girls and Stuff (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 20

* Event [See You in the Morning](./beachvacation16.md) (Main) is completed)

* Event [FLAVOR BEAM!](./mayadorm25.md) (Maya) is completed)



## Next events

* [Ami: Divergence](./amidorm20.md)

## Event properties

* Id: amisroom20
* Group: Ami
* Triggered by label: amisroom
* Triggered by branch label: amisroom
* Triggered by path: amisroom->amisroom20

## Official wiki page

[Cute Girls and Stuff](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amisroom20&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amisroom20:
    scene cutegirlredux1
    with dissolve
    play music "amiamiami.mp3"

    "I step out into the living room after deciding to spend the morning with Ami."
    "I feel like it’s been quite a while since the two of us have done anything other than just lounge around the house together, so maybe she’ll actually want to get out today?"
    "There’s only so much I can take of being stuck inside the house with a cute girl who will cook and clean for me and-"
    "…"
    "Wait, why am I complaining again?"

    a "Good morning, [amimaster]. Are you done narrating your thoughts inside of your head and ready to pay attention to me?"
    s "I guess so."
    a "Did you sleep well?"
    s "Well enough. How about you?"
    a "Really good, actually! And I’m glad you’re finally up because I was just thinking that it’s been a while since the two of us did anything fun together."
    s "Ami, are you able to read my mind? Because this is starting to get weird."
    a "Yup! I'm a mind reader. And right now, you're thinking that you want to take me shopping."
    s "On second thought, why don't I just sit on the couch and have you cater to me for the rest of the day? "

    scene cutegirlredux2
    with dissolve

    a "That’s what I always do, though!"
    s "And you're very good at it."

    scene cutegirlredux3
    with dissolve

    a "Flattery will get you nowhere, [amimaster]."
    s "Oh, come on. We both know that's not true."

    scene cutegirlredux4
    with dissolve

    a "Are we really not going to do anything today?"
    s "What exactly do you even need to go shopping for? "
    s "Please explain to me in detail why I must use my hard-earned money on things that you require."

    if bonus == True:
        a "Because...you’re my legal guardian and I don’t have a job?"
    else:
        a "Because I am your accountant and I'm telling you that it is the right move financially."

    a "I can’t just stay in the same clothes forever, you know."
    s "Well, it hasn’t seemed like a problem so far."

    scene cutegirlredux2
    with dissolve

    a "It’s a huge problem! A colossal one!"
    a "How am I supposed to know you love me if you never pamper me?!"
    a "And also, your money isn’t hard-earned at all! You never even do anything!"
    a "You’re the worst teacher ever!"

    if bonus == False:
        s "How {i}dare{/i} you?"

    s "Are you throwing a temper tantrum right now?"
    a "Are YOU throwing a temper tantrum right now?!"
    s "I just want to eat breakfast."

    scene cutegirlredux3
    with dissolve

    a "No. You just want to hate me and take advantage of my undying love for you."
    s "I'm not {i}taking advantage of you,{/i} Ami."
    a "You only like me because I’m a good cook and I do your laundry."

    if ami_lust > 10 and bonus == True:
        a "And also because I touch your penis sometimes."

    s "Well...I mean, that’s not {i}entirely{/i} inaccurate."

    scene cutegirlredux5
    with dissolve

    a "So, what better way to make it up to me than by taking me to the mall and letting me look at a few things?"
    a "We don’t actually need to {i}buy{/i} anything. "
    a "I can just stare at all of the cute clothes I {i}could{/i} be wearing if my [uncle] actually cared about me."
    s "Can you at least make breakfast first?"
    a "Yes, but only if you promise to go with me right now and not wait until after you're done eating to change your mind."
    s "Stop being so perceptive. I don't like it."

    scene cutegirlredux6
    with dissolve

    a "Yay! You didn't say no, which means that you're okay with it!"
    s "Those words would not hold up in court, you know."
    a "Sure they would! Now go get dressed while I make you breakfast."
    s "Ugh, fine. I’ve already accepted that I’m not going to be able to talk you out of this anyway."

    scene black
    with dissolve

    "I head back into my bedroom and put on the same outfit I put on every day, wondering if maybe {i}I{/i} should splurge on some new clothes as well."
    "I ultimately decide against it, though, because if either one of us is going to actually benefit from some new clothes it's Ami."
    "Say what you want about the lack of variety in my wardrobe, but I am a young-ish adult male who has already won over a multitude of girls without having to do much-"
    "And Ami is one of those girls, who I'm sure wants to look even prettier for a better chance at coming out of love-gauntlet in first place."
    "Unfortunately, things like that don't come without a cost. And in this case, that cost is going to be my money."

    scene sky
    with dissolve

    "Unless...I use today to convince her that it might be time to get a job of her own."
    "I remember her telling me in the past that she had a secret source of income, but I subsequently found out that source of income was one of my credit cards when the bill showed up in the mail."
    "That source of funding has been cut off, leaving her with nothing to her name except the clothes on her back and the various manga she acquired through low level identity theft."
    "The only issue I can think of when it comes to her getting a job is the whole part where she'd need to separate from me."
    "So I'll just have to figure out how to spin things in a way that makes it sound like this would be good for both of us."
    "If I'm able to do that, then-"

    a "Sensei! Are you ready yet? Or are you thinking stuff again?"
    s "I am always thinking stuff. That is what it means to have a brain."
    a "Well, use your brain to finish putting your clothes on because breakfast is ready and I want clothes!"
    s "…"

    scene black
    with dissolve2

    "I sigh to myself while sliding off my shirt, wondering if a day will ever come where I need to start doing things for myself."
    "…"
    "I hope not."
    "That would suck."
    "………"
    "……"
    "…"

    scene amimall1
    with dissolve2

    "Ami hangs her arm over the railing, overlooking a surprisingly low amount of people for a weekend morning."
    "She smiles as I take my place next to her, but doesn’t pay much attention to me right away."

    a "You know I was only half-messing around with you this morning, right?"
    a "I know you would have caved and brought me here anyway if all I did was ask nicely. "
    a "Sure, you might be a freeloader who never really does anything around the house, but you care about me and buy me food and that’s all that matters."
    s "I have no idea whether that's a compliment or an insult."

    scene amimall2
    with dissolve

    a "Can it not be both?"
    a "I kind of like how lazy you are. It gives me more excuses to spend time with you and validates my purpose in this world as a caring and attentive [niece]."
    s "That’s right, Ami. Which is why I’ve decided to do something very special for you today."

    scene amimall3
    with dissolve

    a "Special? What do you mean?"

    "I reach into my pocket and pull out a wrinkled 1,000 Yen note and hold it out toward her."

    s "This is yours. Don’t spend it all in one place."

    scene amimall4
    with dissolve

    a "Wow! Sensei! I didn’t think you’d actually-"

    scene amimall5
    with hpunch

    a "Hey, wait a second! That's only 1,000! What the heck am I supposed to buy with that?!"
    a "I can’t even get a skirt with that much!"
    s "You can buy socks. Those are cheap, right?"
    a "I don’t need socks! I have a million socks!"
    s "This is literally all I have on me."

    scene amimall6
    with dissolve

    a "Nuh-uh! I know from past experience that you have a credit card."
    s "What happened to the whole “You don’t need to actually buy me anything” bit from earlier? Can we go back to that?"
    a "I was obviously just being polite when I said that. You need to get me at least {i}something{/i}."
    s "Why don’t you just get a job if you’re so concerned about money?"

    scene amimall7
    with dissolve

    a "Umm...Aren’t {i}you{/i} my job?"
    s "I guess I kind of am. But why not get a second one, then?"

    scene amimall8
    with dissolve

    a "Hmm..."

    "Ami looks over the railing as a trace of concern spreads across her face."
    "If I know her well enough (Which I’m pretty sure I do), she’s probably thinking about whether or not it’s worth sacrificing her time with me in exchange for material goods."
    "And if I know her even better than that (Which I’m pretty sure I do), I expect her to come out and say that she’d rather stay with me than-"

    scene amimall9
    with dissolve

    a "What kind of job do you think I should look for?"
    s "Wait, what?"
    a "What? You said I should get a second job, so the least you can do is help me think of one."
    s "I thought your love for me was going to trump your desire for material goods. That's how this played out in my head."
    a "Obviously, my love for you will always come first."
    a "But I’m still a girl who wants cute stuff and tickets to concerts and blah blah blah and you won’t give me more than 1,000 Yen because you hate me."

    if bonus == True:
        s "I don’t hate you, I just...don’t know the standard cost of clothing for a girl your age."
        a "You’d think that years of buying clothes for a girl my age would have ingrained that into your memory by now."
    else:
        s "I don't hate you. I just feel as if you might be taking advantage of my lack of knowledge in the economic space."
        a "..."
        a "But I make you breakfast and stuff."
        s "Good point."

    s "Ami, if you get a second job, who is going to make me breakfast in the morning?"
    a "Who said I’m going to work mornings?"
    a "You can’t go making my schedule for me when I don’t even have a job yet."
    a "Especially when we don’t even know what my job is going to be."

    "A job for Ami, huh?..."
    "There is {i}one{/i} thing that pops into my mind, but I’m not really sure if she’d go for it or not."
    "In fact, the only reason it popped into my mind at all is that I kind of just want to see how she’d look in the uniform."

    s "What about a maid cafe? "
    s "There’s one nearby, isn’t there?"

    scene amimall10
    with dissolve

    a "There is but...why do {i}you{/i} know about it?"
    a "That place is still kind of new and I thought Maya, Ayane and me were the only ones who went there."

    "What I can’t tell Ami is that Maya {i}is{/i} the reason I know about it."
    "I’ll just let her assume it was Ayane that told me or something."

    s "How I know about it doesn’t matter."

    scene amimall11
    with dissolve

    a "Hey, hold on a second, dearest [uncle]."
    a "You disappear for most of the day on weekends and I never really ask where you go."
    a "Combine that with how you don’t want to give me money and..."
    s "...And what?"

    scene amimall12
    with dissolve

    a "You’re addicted to maid cafes, aren’t you?!"
    s "…"
    s "Excuse me?"

    scene amimall13
    with dissolve

    a "I mean...I guess that would make sense given how much you like cute girls and stuff. But I didn’t think you’d be spending {i}every waking moment{/i} there."
    s "I think there’s some sort of misunderstanding. I’ve only been there-"

    scene amimall14
    with dissolve

    a "Wait...but if you spend every waking moment there..."

    scene amimall15
    with dissolve

    a "If I was hired at the maid cafe, I’d get to spend every waking moment with you!"
    s "..."
    a "And I already know everything you like! So your service would be amazing and you’d be forced to give me all of your money!"
    a "I love this idea!"

    if bonus == True:
        a "I love it so much that I’m going to ignore your newly-discovered maid fetish!"
    else:
        a "I love it so much that I’m going to ignore how much you apparently like maids!"

    s "I mean...I don't know if I'd call it a {i}fetish...{/i}"

    scene amimall16
    with dissolve

    a "Any fetish you have is fine with me, Sensei."
    s "I really don't like how nonchalantly you said that."
    a "Would you want to come with me soon and see if they’re hiring or something?"
    a "I’d feel a lot more confident about applying if you’re there with me."
    s "Aren’t you worried that I’m going to spend all of my money on the other maids while we’re there?"
    a "No. Because if you even talk to them, I will cut your fingers off and feed them to ducks."
    s "Joke's on you, ducks are primarily herbivores and probably wouldn’t even eat human fingers."
    a "Joke's on you, I raised an army of carnivorous ducks and have been hiding them behind the dorms. "
    a "They’re ready to eat your fingers at a moment’s notice."

    if bonus == True:
        s "I have several questions but I’m going to ignore them and replace them all with the thought of you calling me Master."
    else:
        s "I knew there was something weird about those ducks."

    if bonus == True:
        scene amimall17
        with dissolve

        if amimaster == "Master" or amimaster == "master":
            a "That’s exactly what I’ve been calling you for a while now. "
            a "Don’t tell me you’re thinking of things like {i}that{/i} in the middle of the mall...are you, Master?"
            s "I plead the fifth. This conversation is supposed to be about you getting a job."

        else:
            a "You know I’d be okay with calling you that regardless, right?"
            a "If that's really your end-goal, we can just skip the job part if you want~"
            s "If we skip that part, you’ll be unemployed forever."

    scene amimall18
    with dissolve

    a "What if I’m not good, though?"
    a "I really only know how to take care of you, not other men."
    s "There aren’t even that many men left in Kumon-mi. "
    s "If any of them hit on you, just...say you’re into girls and tell them to go away or something."
    a "I’m pretty sure that sort of thing would get me fired from a maid cafe."
    s "Probably. But there’s always a chance they could just think that’s your archetype or something."

    scene amimall19
    with dissolve

    a "Oh! You mean like a...tsundere maid?"
    s "Sure. Let's go with that."

    scene amimall20
    with dissolve

    a "I-Idiot...It’s not like I even want to be a maid or anything..."
    s "See? You'll be just fine. You've already got the character down better than Yumi and she's been doing this for years."

    scene amimall21
    with dissolve

    a "You better not be implying that Yumi actually likes you or something, [amimaster]..."
    s "Of course not. Yumi doesn't like anyone. That's why I said you have the character down {i}better{/i} than her."

    scene black
    with dissolve2

    a "Likely story...Now I have to add another name to my list."
    s "List? What list?"
    a "Don't you worry about it, Sensei."
    a "Don't you worry at all..."

    "Ami and I walk around the mall for a little while longer as we go over other possible scenarios that might occur if she actually gets a job at a maid cafe."

    if bonus == True:
        "The one that sticks out in my head amongst the others, however, is that she could walk around the house wearing the costume."
        "Is this something a typical adult male should be excited about when concerning his [teenage][niece]? Probably not."
        "But I am no typical adult male. "
        "Trading away my morals has allowed more space within me think about things others would not dare think of."
        "And it’s that exact thought process that makes me go from worrying about a distinct lack of Ami around the house to eagerly awaiting her prospective future in the workforce..."
    else:
        "It sounds like a rather lucrative business, which would allow her to grow her income exponentially and provide a more comfortable retirement for her."
        "And, as her pogchamp, I should be respectful and understanding of that."


    $ renpy.end_replay()
    $ amisroom20 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label amisroom25:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amisroom:
    if ami_love >= 0 and firsttimeamisroom == False:
        jump firsttimeamisroom
    if ami_love >= 5 and amisroom5 == False:
        jump amisroom5
    if ami_love >= 10 and amisroom10 == False:
        jump amisroom10
    if ami_love >= 15 and amidorm15 == True and amisroom15 == False:
        jump amisroom15
    if ami_love >= 20 and beachvacation16 == True and mayadorm25 == True and amisroom20 == False:
        jump amisroom20
...
```