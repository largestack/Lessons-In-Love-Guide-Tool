# Third Place (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 30

* Event [Shawshank Redemption](./utadorm10.md) (Uta) is completed)

* Event [Purest Intentions](./bar35.md) (Sana) is completed)



## Next events

* [Ami: The Big Sleep](./amidate35.md)

## Event properties

* Id: amimaid30
* Group: Ami
* Triggered by label: amimaidhub
* Triggered by branch label: saturdaymorning
* Triggered by path: saturdaymorning->amimaidhub->amimaid30

## Official wiki page

[Third Place](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amimaid30&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amimaid30:
    scene amimaidthirty1
    with fade
    play music "maidcafe.mp3"

    "I arrive at the maid cafe bright and early to see how Ami’s doing."

    a "Wow! You’re here bright and early!"

    "See?"

    scene amimaidthirty2
    with dissolve

    a "Did you wind up skipping the breakfast I made for you this morning or something?"
    s "You made me breakfast this morning?"
    a "Yeah, I wrapped it up and left it on the table for you. "
    a "I didn’t really have time to write a note or anything because I was running late for work, but I figured you’d have just...understood that it was there for you and not somebody else."
    s "Honestly, I didn’t even notice."

    scene amimaidthirty3
    with dissolve

    a "Oh well! I’ll just assume that since you’re here, it meant you missed me so much that you ran right over as soon as you woke up!"
    s "Yeah, let’s go with that. "
    s "Is Uta-chan working now?"

    scene amimaidthirty4
    with dissolve

    a "Or you only came here to toy with my feelings!"
    a "Am I not good enough for you all of a sudden? Why Uta-chan and not your beloved [niece]?"
    s "Because Uta-chan would never put on a face like that while she’s at work. "
    s "And here I was thinking you were finally beginning to get the hang of your new job..."

    scene amimaidthirty5
    with dissolve

    a "I {i}am{/i} getting the hang of my new job! I’m really good at this!"
    s "Great. Then you can start chipping in on bills soon. The one for our phones has been getting pretty high lately."

    "Though, there is a very good reason for that."

    scene amimaidthirty6
    with dissolve

    a "What? How? I thought we had unlimited data and all that stuff?"
    s "Long story. Point is, now that I know you have a stable job that you’re doing well at, it’s time to start growing up financially as well."

    scene amimaidthirty7
    with dissolve

    a "Ooooooooor you can keep paying all the bills and I can use the money I make at work to do all sorts of fun things with you."

    if ami_virgin == False and bonus == True:
        a "Or {i}to{/i} you, depending on the mood we’re in."
        s "I am both intrigued and scared at the same time now."
        s "I guess there’s no harm in letting you use your money how you please."
    else:
        s "...I guess that’s also a fine way to spend your money."

    s "I’m a little surprised you don’t want to spend it on yourself, though. Wasn’t that the whole reason you got a job in the first place?"

    if bonus == True:
        a "Kind of. It’s been an interesting change of pace and I’d be lying if I said I wouldn’t rather spend my time pleasing you and you only-"
    else:
        a "Kind of. But I've been dumping all of my earnings into non-profit organizations in an effort to make the world a better place."
        s "Awwwww."

    a "But being able to buy clothes is nice too. "

    scene amimaidthirty1
    with dissolve

    a "And so I was kinda wondering if you’d wanna maybe come to the mall with me soon and...help me pick out a new swimsuit for the next time we go to the beach."
    s "Ami, it’s the middle of winter."
    a "So what? Even if it’s freezing cold out when we go to the ocean, we’re still going to wind up swimming."
    a "What’s the point of having a vacation at the beach if you’re not going to go swimming?"

    if bonus == True:
        a "Plus, the swimsuit I have now is really...childish anyway."
        a "And if I’m gonna start doing grown-up stuff like working and living at the dorm, I’m gonna need to look the part."
        a "The days of the one piece are over, Sensei! The days of bikini Ami are about to begin!"
        s "Are you sure you’re going to be able to find one that...you know...{i}fits?{/i}"
        a "…"
        s "Because I think the one piece might actually be a better bet until you...grow in a little more."
        a "…"
    else:
        a "Sometimes, the sound of the ocean helps me stay focused while filing your returns."
        s "In that case, I support the trip. Thank you for explaining your position to me."

    scene amimaidthirty8
    with dissolve

    os "Hey, is there anything I can be doing to help out while there are no customers here? I feel weird just standing around."
    a "…"
    s "I’m a customer."

    scene amimaidthirty9
    with dissolve

    os "Please don’t look at me."
    os "Also, did you say something mean to Ami? She looks kinda...frozen."
    s "How am I supposed to talk to you if I’m not allowed to look at you?"
    os "Just look the other way or something, I don’t know."

    scene amimaidthirty10
    with dissolve

    a "Hah..."
    a "Even {i}those{/i} would be a gift from God right now."
    os "...?"
    s "Think, Osako."
    os "…"

    if bonus == True:
        scene amimaidthirty11
        with dissolve

        os "You didn't say what I think you did to her...did you?"
        a "You can just hang out, Osako-chan...I don’t really know what to do when it’s dead either."
        a "And no one ever really comes until the afternoon anyway..."

        scene amimaidthirty12
        with dissolve

        os "Okay...sounds good, I guess."
        os "And, uhh...hang in there? Mine didn’t start showing up until senior year of [high_school] and..."
        os "Why am I even telling you this? I’m just going to go...re-wash dishes or something."
    else:
        os "No clue."
        os "Anyway, bye. My appearance in this event is over now."

    scene amimaidthirty13
    with dissolve

    "Osako leaves the table and I suddenly have to figure out a way to make Ami feel better."
    "Thankfully, this is the easiest possible task that could ever fall into my lap."

    s "I love you and you’re adorable."

    scene amimaidthirty14
    with dissolve

    a "Ah! I love you too!"
    a "What were we just talking about? Did Osako-chan need help with something?"
    s "Nah, she’ll be fine."

    play sound "dishes.mp3"
    scene amimaidthirty14
    with hpunch

    os "Shit!"
    s "See?"
    a "Oh well. Uta drops stuff all the time so we can just add it to the list. Our manager is really forgiving about that kind of stuff."
    s "Well that’s reassuring. Having a manager that gets on your case all the time doesn’t sound like a thing I’d be able to handle."

    scene amimaidthirty15
    with dissolve

    a "You handle {i}me{/i} just fine, though. And I kinda feel like your manager sometimes, you know?"
    a "Sure, that bitch Makoto is the one always making sure you do your work and stuff-"
    s "You can’t just casually call her a-"
    a "But {i}I’m{/i} the one making sure you get up on time and make it to[school]."
    a "And I’m the one who gets to hold your hand and help you make all the correct decisions for things that actually matter."
    a "We’ve got a special bond that no one else could ever hope to replicate! So I’m not just a manager, I’m a...super manager!"
    s "I’m sure that will look great on future job applications."

    scene amimaidthirty16
    with dissolve

    a "Future applications?"
    s "Yeah. You can’t just stay at the maid cafe forever, right?"

    "I mean, it’s not like she can ever really get a “real” job at this rate, though. So I guess technically she can stay here forever."
    "But still, I should at least {i}try{/i} to push her in the right direction every once in a while."

    a "I wasn’t planning on staying here forever."
    s "Well then what’s your goal once you get out of [high_school]?"

    scene amimaidthirty17
    with dissolve

    a "To wait on your every beck and call."
    s "Why did I expect for even a moment that you were going to say something else?"

    if ami_virgin == False:
        a "I have no idea. I’ve done nothing but force myself on you from the get-go and that’s just a thing you’re going to have to deal with for the rest of forever."
    else:
        if bonus == True:
            a "I have no idea. I’ve done nothing but try to get you to notice me as more than a [niece] from the get-go and you still think you can avoid my love."
        else:
            a "I have no idea. Maybe I'll try expanding my accounting firm internationally? Of course, I'd remain local myself, though."

        s "Ami-"
        a "Don’t {i}Ami{/i} me, Mister. "
        a "I’ll be with you forever, even if you don’t want me there."

    scene amimaidthirty18
    with dissolve

    a "But right now, I’m Ami-chan! Third most popular maid in the entire cafe!"
    s "I’m assuming Uta is one of those two but...has Osako already overtaken you in the rankings?"
    a "Oh, no. I’m talking about someone completely different. But I’ve vowed to not speak of who number one is at the risk of losing my job."
    s "You can’t just say something that interesting and not follow up on it."
    a "Sure I can!"
    a "Besides, I don’t know if she’s ever coming back anyway, so we’ll just kinda have to wait and see I guess."
    s "…"
    s "Is it someone I know at least?"

    scene amimaidthirty19
    with dissolve

    a "Maybe! But do you really think I would tell you-"

    if amipatgasm == True:
        s "If you tell me, I’ll pat your head."

        scene amimaidthirty20
        with dissolve

        a "Wait, no! You can’t pat my head! We found out last time that weird things happen when you pat my head!"
        a "If you’re going to do that again, we need to at least go home or-"
        s "Are you sure? Because I’ll do it right here."
        a "Sensei!"
        a "If you really want to know, just...keep coming back!"

    else:
        s "If you tell me, I’ll pat your head."

        scene amimaidthirty21
        with dissolve

        a "Hmm...that does seem like a fair trade, but still. I can’t do it."
        a "You’ll just have to...keep coming back until you find out for yourself."

    s "Are you challenging me to come to the maid cafe every day for the rest of my life?"

    scene amimaidthirty22
    with dissolve

    a "Perhaps I am."
    a "And yes, I know that this means you might go broke. But that’s okay! "
    a "The two of us could move into some strange abandoned building and live out the rest of our days taking donations from strangers or waiting for government assistance!"
    s "Well I definitely don't need to know who the secret maid is {i}that{/i} much."

    scene amimaidthirty23
    with dissolve

    a "Of course you don’t, because I’m the only maid you’ll ever need anyway."
    a "I will admit that I was very jealous when I found out you wanted to marry Uta-chan-"
    s "Want. Not wanted. The desire is still there. "
    s "She will be mine."
    s "Oh, yes."
    s "She will be mine..."
    a "No. Because {i}I{/i} will be yours. "
    a "You haven’t spent as much time with me here as you have with her yet, but I’m like a walking trash receptacle for your love!"
    s "Please be a little kinder with the things you say about yourself. You are a reflection of me and-"
    s "Actually, yeah. That much is fine if you’re a reflection of me."
    a "...As I was saying! I spent years and years and years and years turning into Mega Ami so you wouldn’t look at people like Uta-chan."

    if bonus == True:
        a "And if I find out it’s just because of her stupid boobs I’m skipping out on a new bathing suit and saving up for implants!"
    else:
        a "But if Uta's vigorous treadmill routine has made her attractive enough for you to ackowledge her over your dear CPA, maybe I'll get a treadmill too?"

    s "Please don’t do that. I like you just the way you are."

    scene amimaidthirty18
    with dissolve

    a "Exactly!"

    if bonus == True:
        a "So, with that out of the way, come with me to the mall and appreciate my depressingly tiny chest as I try on new bathing suits for you!"
        s "No more one piece?"
        a "No more one piece."
        s "Well, I’ve seen you naked before, so that’s not too drastic of a change."
        a "Exactly! It’ll be just like me walking around the house in my underwear. Just if you get excited, everyone around you will notice and not just me!"
        s "I still think it’s insane you’re even considering doing something like this when it is literally snowing out."
        a "The snow can only last so long! And youth is not eternal!"
        a "Appreciate me while you can, Sensei. Because you never know when I’m gonna hit my growth spurt and become a sultry, sexy [niece] rather than a cute one."
        s "Doubtful. Right now, I think sultry and sexy are the two words I would literally never describe you with."

        scene amimaidthirty24
        with dissolve

        a "I can be sexy if I want to be! Just look at my costume!"
        s "Again, that’s more “cute” than it is sexy. "
        a "What do I have to wear to be sexy?!"

        scene amimaidthirty25
        with dissolve

        os "Ami, what are you freaking out about? Isn’t he your [uncle]?"
        os "Why do you have to look-"
        a "Shut up, Osako-chan! Tell him I’m sexy!"
        os "...No?"

        scene amimaidthirty24
        with dissolve

        a "Well...maybe I’m not sexy {i}yet!{/i} But you just wait!"
        a "You’ve got a long time left with me, Mister! And I’m not gonna be your little girl forever!"
        a "Well, I will always be your little girl! But I’ll eventually be a...big little girl! With boobs and...allure!"
        a "And you will love me!"
        os "...Okay, I’m gonna step outside for a bit."
        os "Let me know if you need help or anything..."

    scene black
    with dissolve2

    if bonus == True:
        "Instead of bringing me anything to eat, Ami spends the next twenty minutes lecturing me about things I should and should not say to her."
        "Of course, Ami’s entire thing is that she’ll accept me unconditionally no matter what I do, so it goes in one ear and out the other."
        "But hey, even when she’s incessantly ranting about her inferiority complex, she still manages to be cute about it."
        "Is she annoying? Sure. "
        "But she’s family."
        "And I don’t really have a problem saying that now."
        "It’s family’s job to be annoying, so I can’t really foresee that ever going away."
        "Granted, I can’t see her ever “growing up” either but, chances are, I won’t ever have to."
        "So I should just accept my [niece] in all of her current, non-sexy perpetual glory."
        "For she is but a trash receptacle-"
        "And I am a man walking down the streets of a busy neighborhood, clutching an empty can and waiting for a place to toss it out."
        "Also, even though I’ve seen her naked around the house before, I’m weirdly excited to see Ami try on new swimsuits."
        "But if she winds up getting a cold as a result of stripping down to that much bare skin in the middle of winter, I’m having her pay for her own medical bills."
    else:
        "The meeting is cut short when a group of electricians shows up to rewire some stuff."
        "They try telling me about it since I am a man and appear to be knowledgable about wires, but I really have no idea what they're talking about and just nod at them a bunch of times to try and hide that."
        "Eventually, I wind up paying for the necessary repairs because I am a good guy."
        "Everyone thanks me and tries to lift me in the air to celebrate, but I don't like how their hands feel, so I make them stop."

    $ renpy.end_replay()
    $ amimaid30 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label amidate35:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amimaidhub:
    if ami_love >= 30 and utadorm10 == True and bar35 == True and amimaid30 == False:
        jump amimaid30
...
```