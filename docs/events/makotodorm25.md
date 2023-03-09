# Bluejay
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotodorm25&go=Go)



## Event preconditions
✅Makoto love greater than or equal to 25

✅Event "[Makoto: Teacher's Pet](./makotofirsthall.md)" is completed (event=makotofirsthall)

✅Event "[Makoto: Service Charge](./pornshop25.md)" is completed (event=pornshop25)

✅trinity3track equal to True (unknown variable)

✅Event "[Miku: One. Two. Three.](./mikudorm30.md)" is completed (event=mikudorm30)



## Next events
* [Main: As Loud as a Whisper Can Be](./day214.md)
* [Maki: Maki Miyamura's Mom-Mode Mission](./makidate5.md)

## Event properties
* ID: makotodorm25
* Group: Makoto
* Triggered by label: makotodorm
* Triggered by branch label: makotodorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label makotodorm25:
    play sound "knock.mp3"

    "I knock on Makoto’s door and wait for her to answer. "

    play sound "static.mp3"
    scene tree3 with flash
    stop sound
    scene bluejayredux1

    "She appears."

    mak "Good evening, Sensei. To what do I owe the pleasure?"
    s "You owe nothing at all, Makoto. I’m just here to say hello to my favorite class representative."
    mak "And also the only class representative you have."
    s "Correct. But my opinion would not change even if {i}everyone{/i} was a class representative."
    mak "Likely story."
    mak "Anyway, I’m glad you showed up when you did."
    mak "I was about to embark on a little...journey. And I’d feel much more comfortable if you were there with me."
    s "A journey? What kind of journey are we talking about?"

    scene bluejayredux2
    with dissolve

    mak "Let’s just say I’m in the mood to do something...bad."
    s "You’re not planning on robbing a convenience store or murdering anyone, are you?"
    mak "{i}Worse...{/i}"
    mak "I’m planning on sneaking into[school]."
    s "You sick bastard."
    s "Why, though?"

    scene bluejayredux3
    with dissolve

    mak "Well, remember how you’ve found me on the roof a few times now?"
    s "Vaguely. That sounds like a thing that probably happened."
    mak "Well, it’s become a bit of a...happy place for me."
    mak "I go there when I need to think and, sooner or later, I find myself calming down."
    mak "It’s no different than somewhere like a lake or a...peaceful mountain top. Just a lot less...{i}serene.{/i}"
    mak "You obviously don’t have to come if you’re afraid of breaking a few rules."
    mak "But knowing that you care less about rules than you care about the melting of our polar ice caps, I assume you’ll be tagging along. Yes?"
    s "Hold on, why do you just assume I don’t care about the polar ice caps? That’s a weird assumption."

    scene bluejayredux1
    with dissolve

    mak "Was I {i}incorrect{/i} in assuming that?"
    s "Oh, no. I honestly don't care at all."
    mak "Exactly."
    mak "Come along with me then. I have a key to the roof, so it'll be less of a break-in and more of just...trespassing."
    s "Is it even trespassing if you have a key?"
    mak "I’m not sure. But if we wind up getting caught, I’ll be sure to ask."
    s "You do that, Makoto."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "The two of us walk down the same streets we’ve walked hundreds, if not thousands of times before."
    "Not together, obviously. But as ourselves."
    "Makoto and I will never go anywhere thousands of times together."
    "Something like that just wouldn’t make sense."
    "There’s no way around saying this, but she’s simply too good for me."
    "The more time I spend with her, though-"
    "The more I realize that there’s some sort of darkness growing within her."
    "Is that darkness due to me?"
    "Did I plant the seed?"
    "And will that seed consume her?"
    "Will vines sprout from deep within her body and twist around her entrails?"
    "Will they lift her up or pull her down?"
    "Will they make it harder for her to function as the diligent and responsible girl she is meant to be?"
    "Or will she find a way to cut all of that out of her and draw the light back in to where it once called home?"

    scene nightsky
    with dissolve
    play music "blueair.mp3"

    "I’m sorry."
    "I’m feeling particularly callous tonight."
    "And the fact that we’re surrounded by silence is only making me more aware of it."
    "Quiet. "
    "Quiet."
    "Quiet."
    "Everything is so quiet."
    "Say something."

    mak "Sensei?"

    "{i}Thank you.{/i}"

    s "Yeah? What’s up?"
    mak "Have you ever gone to[school] after dark before?"
    s "Yeah. With Maya."
    mak "Wait, {i}Maya?{/i}"
    mak "Why on Earth would it have been with her? That doesn’t make any sense at all."
    s "She needed help carrying something."
    mak "To[school]? In the middle of the night?"
    s "I don’t really get it either, but I’ve stopped questioning her actions. I'm pretty sure she's insane."
    mak "Well...shit. Here I was thinking I’d get to be the first one to embark on a rebellious delinquent-style journey with you."
    s "If this is your idea of what delinquents do, it’s a bit off."
    s "Someone like Yumi wouldn’t be caught dead sneaking {i}into{/i}[school]."
    s "You certainly have a strange way of being rebellious, Makoto."
    mak "Hah. I suppose I do. "
    mak "But you’ll have to forgive me since my mind isn’t all {i}here{/i} tonight."
    s "Thinking about your dad again?"

    scene bluejay1
    with dissolve2

    mak "Perhaps."
    mak "I’ve been thinking about a lot of things. "
    mak "In fact, I’ve barely been studying at all lately. "
    mak "Ever since Halloween, I’ve been slacking off. "

    if bonus == True:
        mak "It’s like you planted some sort of seed inside of me."
    else:
        s "You watched it, didn't you?"
        mak "Watched what?"
        s "Napoleon Dynamite."
        mak "..."
        s "Makoto, no. I told you it was dangerous."

    mak "It’s consuming my normal routines."
    mak "Turning me into a {i}slacker.{/i}"
    s "…"

    scene bluejay2
    with dissolve

    mak "Just kidding~"
    mak "I’m just a little tired, is all."
    mak "Tired of giving 100%% all of the time and getting like 4%% back in return."
    mak "So, in order to make up for my awesome overexertion of power, I’m taking a bit of a...vacation, if you will."
    s "And the first stop on said vacation is the roof of the[school]?"

    scene bluejay3
    with dissolve

    mak "This isn’t just the roof of the[school], though."
    mak "It’s the top of the world."
    mak "You can see everything from here."
    mak "You can see my house...You can see the dorms....You can probably even see over the barrier if you're tall enough."
    s "You mean like, outside of Kumon-mi?"
    mak "What else would I mean?"
    s "That’s...a good question."
    mak "Remember when we were able to leave, Sensei? Before the stupid space war started and whisked my dad and everybody else away?"
    mak "You’re lucky you got to stay."
    mak "And I guess, by association, I’m kind of lucky too."

    scene bluejay4
    with dissolve

    mak "The two of us might bicker constantly, but I want you to know that you really are important to me."
    s "What’s this all of a sudden?"
    mak "I think it’s called “having a moment.” You should probably just let it happen so I don’t feel awkward about spilling my feelings out in front of you."
    s "You do know I care about-"

    scene bluejay5
    with dissolve

    mak "I know."
    mak "Even if you make it really hard to believe sometimes...I know."
    mak "And the more we talk, the more I see those feelings of yours growing."
    mak "Sometimes, I feel like you’ve become a different person entirely."
    mak "Funny, huh?"
    s "You’re pretty different now from when I met you as well, Makoto."

    "I obviously don't know what the true beginning was like when {i}I{/i} met Makoto-"
    "But she’s definitely changed a bit from when I assumed this role."
    "The old Makoto would never retreat to the top of {s}the world{/s} the[school] in the middle of the night like this."

    if bonus == True:
        mak "Like I said, you planted a seed in me."
        mak "And maybe it's unrelated...Maybe it's not."
    else:
        mak "Vote for Pedro."
        s "Makoto, stop."

    mak "But I’m breaking now, and a certain {i}somebody{/i} is going to have to pick up the pieces."
    s "Why do you say you’re breaking?"
    s "It’s not uncommon to go through periods of time where darkness feels inescapable. "
    s "And if that’s what’s happening to you right now, you just...need to find some more light to bring things back to the correct color."
    mak "The correct color, huh?"

    scene bluejay6
    with dissolve

    mak "What color is your life, Sensei?"
    mak "If you had to paint the world one color, which one would you make it?"

    "What I want to say is that I wouldn’t paint it at all."
    "Despite all of the horrible colors in this world and how none of them seem to stand out to me, changing them would probably make things even worse."
    "No one wants to live in a vibrant paradise."
    "No one wants happiness to fall off of a tree like it's some sort of fruit."
    "We want misery- because it’s the only way we can ever feel like we’re getting anywhere."
    "I will lie to this girl."

    s "Blue."
    mak "Really?"
    mak "Blue is my color, too."
    mak "My eyes are blue. My bra is blue. My diary is blue."
    mak "Everything is blue."
    mak "Everything will always be blue."
    s "Okay, I'm starting to think you may like the color blue a {i}bit{/i} more than I do."

    scene bluejay7
    with dissolve

    mak "Hahaha! Probably."

    scene bluejay8
    with dissolve

    mak "Wanna try and take a guess at what my favorite animal is?"
    s "I’m going to go out on a limb here and say it’s a bluejay."
    mak "You’re so smart."
    s "I had plenty of hints."

    scene black
    with dissolve2

    "Makoto turns around and begins to climb up a ladder attached to the part of the building we came up through."

    mak "Hey, Sensei, you know how I said we’re at the top of the world a few minutes ago?"
    mak "Well, do you want to see the {i}top{/i} of the top of the world?"
    mak "I’ve always been afraid to go up this high, but I’m in the mood to take a bit of a leap of faith tonight."
    s "Probably not something you should say when you’re climbing to the top of a building."
    mak "Heheh~ No. Probably not. "
    mak "Are you going to come, though? Or are you going to stay down there like a loser?"
    s "No one calls me a loser and gets away with it."

    "I follow behind Makoto and move up the ladder."
    "She climbs very slowly despite her voice sounding confident and unwavering just seconds ago."
    "Her legs are shaking."
    "She must really be afraid of heights."
    "What a coward."

    scene bluejay9
    with dissolve2

    "We make it to the top of the top of the world and bask in the light of the moon as we overlook our temporary prison."
    "There is someone I know who would love this view."
    "{s}CORRECTION NEEDED{/s}"
    "There is someone I know who loves this view."
    "This is where she comes after the world ends."
    "It’s where she resets it."
    "But tonight-"
    "It’s just the roof of the[school]."

    mak "It’s even prettier than I imagined it would be up here..."
    s "I can’t say I particularly like being this high up, to tell you the truth."
    mak "Oh, I’m absolutely horrified right now. But it’s worth all of that fear being able to look out at the city like this with you."
    s "You’re just trying to lower my guard so you can push me off, aren’t you?"

    scene bluejay10
    with dissolve

    mak "Hmm...I guess that would be appropriate revenge for all of the torment you’ve put me through."
    s "I will not hesitate to push you off first if it really comes down to it."

    scene bluejay11
    with dissolve

    mak "Somehow, I’m not surprised."
    mak "You’ve always been the center of your own world."
    mak "Not like there’s a problem with that or anything. I’m kind of the same way."
    mak "The big difference in us, though, is that you willingly choose to put yourself first and I just do it instinctively."
    s "So what you’re saying is I’m an asshole and you’re just a victim of natural instinct. "

    scene bluejay12
    with dissolve

    mak "Precisely."
    mak "I’m a better person than you are. "
    s "I’m aware. Thank you for reminding me."

    scene bluejay13
    with dissolve2

    mak "There’s no need to thank me. "
    mak "I think you’re actually really amazing when it comes down to it."
    mak "I mean, you’ve made it {i}how many{/i} years into life without giving up on anything?"
    mak "I’m not even out of [high_school] and I’m already rethinking my career choice because of how exhausted I am all the time."

    if bonus == True:
        mak "And it doesn’t help that the only slightly-patriarchal figure in my life right now makes me do things like...jerk him off with a fake vagina."
    else:
        mak "And it doesn’t help that the only slightly-patriarchal figure in my life right now taught me how to swim."
        s "Is that...a thing I did?"

    scene bluejay14
    with dissolve

    mak "Oh, and just to clarify, that’s not an insult. I actually kind of liked doing that."
    mak "Which I guess might be part of the problem."
    s "..."
    mak "Point is, I’ve gone long enough with no guidance. I officially give up. "
    s "Wait, what?"
    mak "You heard me."
    mak "I give up."
    s "Just like that?"
    s "Why?"
    s "Are you really weak enough to give up just because you’re hitting a rough patch emotionally?"
    s "You said it yourself that your problems pale in comparison to some of the other girls, so why do something so drastic all of a sudden?"

    scene bluejay15
    with dissolve

    mak "Oh? "
    mak "Is that the original Sensei coming back from his metaphorical grave to give me a reality check?"
    s "If that’s what you want to call it, sure."
    s "I just didn’t think you were this weak."

    scene bluejay16
    with dissolve

    mak "Is this some sort of secret teacher strategy- talking down about people at their weakest in order to get them to turn around?"
    s "It’s a strategy I made up just now. And it’s going to work."

    scene bluejay17
    with dissolve

    mak "It’s not, though."
    mak "I’ve already figured out what I want to be instead."
    mak "It came to me for the first time just a few minutes ago."
    s "A few minutes ago? "
    s "What were we even talking about a few minutes ago?"
    s "What’s your new career choice, Makoto? Please enlighten me."

    scene bluejay18
    with dissolve

    mak "I want to be a bluejay."
    s "Well, good luck with that. I can't name one person who has successfully turned into a bird."
    mak "Doesn’t it sound amazing being free from everything, though?"
    mak "No responsibility...No expectations...Nothing to keep you grounded."
    mak "Nothing at all."
    mak "You just fly."
    mak "It’s easy to escape from darkness when you can always move directly toward the sun or the moon."
    mak "But for people like me who can’t seem to find happiness even when their situation isn’t all that bad to begin with, leaving the dark is impossible."

    scene bluejay19
    with dissolve2

    mak "It’s like..."
    mak "There’s this...shadow always looming over me."
    mak "And when I go to sleep, it finds its way inside. "
    mak "It sinks deep into my body and twists its shadowy fingers around my entrails."
    mak "It’s killing me from within and no one even knows about it other than you."
    mak "But, if I were a bird-"
    mak "I could just...fly away. "
    mak "Find something new."

    scene bluejay20
    with dissolve

    mak "You’re familiar with Emily Dickinson, correct?"
    mak "I know you used to write quite a bit, but I don’t know if I ever got your thoughts on classical poets."
    s "I’m familiar, yes."
    mak "Do you know the one that goes..."
    mak "Hope is the thing with feathers-"
    mak "That perches in the soul-"
    mak "That sings the tune without the words-"
    mak "And never stops at all..."
    mak "What do you think that poem means, Sensei?"
    s "Who cares? Emily Dickinson spent virtually her entire life locked inside of her room. She’s not someone you should be stealing life lessons from."
    s "Life’s not some sort of poem, Makoto."

    scene bluejay21
    with dissolve

    mak "Oh, I know that better than anyone. "
    mak "Life’s far too ugly to even be close to a poem. "

    "Is this really Makoto?"
    "Where is any of this even coming from?"
    "Ever since I met her, she’s done nothing but give everyone and everything her all."
    "But now, out of seemingly nowhere, I’m forced to talk her back onto the path she’s meant to take."
    "But, then again-"
    "These could all just be the ramblings of an upset [teenage]girl."
    "Plenty of people say things they don’t mean when overcome by emotions."
    "Just because Makoto is a lot more mature than everyone else doesn’t mean she’s exempt from that."
    "Yeah."
    "That’s all this is."
    "She was never serious about throwing her life away."
    "She’s just lashing out."
    "And since she’s just lashing out- I should do what I always do."
    "Admit it’s not my problem and move on."

    scene bluejay22
    with dissolve

    mak "See? You’re giving up too. That’s your patented “Not my problem” face."
    s "Stop knowing me so well. It's creepy."
    mak "I can’t. I’ve been watching you since the moment I laid eyes on you."
    mak "I even brought you to this extremely special place...to witness something extremely special with me."
    mak "The view up here is unlike anything you’ve ever seen, isn’t it?"
    s "…"
    s "It reminds me of the end of the world, actually."

    "I might as well say that much since there’s no way she’d ever believe me to begin with."

    scene bluejay23
    with dissolve

    mak "The end of the world?"
    s "Not the actual end of the world. Just some dream I had."
    s "A dream where, at the end of the[school] year, everyone disappeared and I was left to wander the streets alone."
    s "Having no idea what else to do, I turned to {s}God{/s} god. Something I’d never even consider doing under normal circumstances."
    s "In the end, I found myself in a place just like this, looking up at this same sky and thinking about how there isn’t anything like it anywhere else."
    s "That doesn’t mean I enjoy it, though."
    mak "You really have dreams like that?"

    "No."
    "But you don’t need to know that."

    scene bluejay24
    with dissolve

    mak "I guess I have to tell you a dream of mine in return then, huh?"
    s "If you want. It’s up to you."
    mak "Don’t get {i}too{/i} excited, now."

    scene bluejay25
    with dissolve

    mak "I’ve been having this one dream reoccur for pretty much my entire life, so I guess it would be easier for both of us if I just told you that one."
    mak "I’m together with my dad on a raincloud and we both have fishing rods."
    mak "Every thirty seconds, the cloud would empty itself out and, mixed in with all of the rainwater, were these rainbow colored fish."
    mak "My dad was great at catching them. But no matter how hard I tried to catch my own, the line would keep snapping whenever I hooked one."
    mak "At first I thought it was because I was too weak or inexperienced, but what I figured out after continuing to see the same dream for years and years is that-"
    mak "Well-"
    mak "It’s just a dream."
    mak "It doesn’t matter."
    mak "There are no rain clouds you can fish off of and there are no rainbow colored fish that drop out of them."
    mak "And now that my dad's out there among those stars, every aspect of that dream is just...that and nothing else."
    mak "It's all just a dream."
    mak "But, my God, do I get excited every time I hear his laugh when he hooks one of those fish."
    mak "Even if it’s just a dream...that sound is so...fucking real."
    s "…"
    mak "…"
    s "My dream was cooler."

    scene bluejay26
    with dissolve

    mak "Hahaha..."
    mak "There you go always knowing exactly what to say to girls again."
    mak "Maybe one day, I’ll be having dreams about you, too."
    s "I’m not much of a fisherman, so try to have dreams about us doing something different. "
    s "Like...racecar driving."
    mak "I’ll see what I can do."

    scene bluejay27
    with dissolve
    stop music fadeout 20.0

    mak "Can I...make a request from {i}you{/i}, Sensei?"
    mak "Since you’re now in my dream-queue, it seems only fair that I get to ask something of you in return."
    s "You’re just going to ask me to kiss you, aren’t you?"

    if bonus == True:
        mak "What gives you that idea?"
        s "Well...we haven’t kissed yet. And this seems like it's probably the best opportunity we’ll ever have for our first one."
        mak "Hahah~ It kind of does...doesn’t it?"
        mak "…"
    else:
        s "Because it would probably be best for the two of us to remain friends and not ever do anything like that."
        s "We can hug, though. Hugs are nice and wholesome."

    "Makoto pauses and stares so deeply into my eyes that it’s almost like she's seeing through me."
    "I’m not sure what’s taking her so long to ask, but I already know what’s coming."
    "It’s just a matter of her following through, I guess."

    mak "Sensei..."
    mak "Close your eyes..."
    s "Really? I don’t even get to see?"
    mak "Sometimes, you can see more with your eyes closed."

    "I feel like I’ve heard that somewhere before."
    "But where?"

    s "Fine. If that’s what you want."

    scene black
    with dissolve2

    "I close my eyes and wait for Makoto to go in for the kill."
    "A second or two later, I can feel her fingers begin to play with locks of my hair as her hand rests atop my head..."

    scene bluejay28
    with dissolve2

    mak "…"
    mak "Just so you know, closing your eyes was only the first part of my request."
    mak "The second part will be a little more complicated than that."
    mak "You see, Sensei-"
    mak "I need you to forget everything we said to each other tonight."
    mak "And everything we said to each other before that."
    mak "Because, a few minutes ago, when you were talking about that dream you had-"
    mak "I finally saw a light."
    mak "I can claw my way out of the darkness now."
    mak "And it’s all thanks to you."
    mak "You’ve done so much for me."
    mak "And I’m sorry I have to go and ruin it all."

    scene bluejay29
    with dissolve

    mak "Here’s hoping you can forgive me."
    mak "…"
    mak "…"
    mak "…"
    mak "See you."

    scene bluejay30
    with dissolve2
    $ renpy.pause(2, hard=True)
    scene bluejay31
    with dissolve
    $ renpy.pause(2, hard=True)
    scene bluejay32
    with dissolve
    $ renpy.pause(2, hard=True)
    scene bluejay33
    with dissolve
    $ renpy.pause(2, hard=True)
    scene bluejay34
    with dissolve
    $ renpy.pause(2, hard=True)
    scene bluejay35
    with dissolve
    $ renpy.pause(7, hard=True)

    play sound "static.mp3"
    scene black
    "//////////////////////////////////////////////////////////////////////////////////////////////"
    "/////////////////////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////////////////////"
    scene 1
    with flash
    scene 2
    with flash
    scene 3
    with flash
    scene 4
    with flash
    scene 5
    with flash
    scene bluejay36
    with flash
    stop sound

    mak "..."
    mak "Huh?"
    s "Makoto?"

    scene bluejay37
    with dissolve2

    mak "...Huh?!"
    s "What’s going on?"
    s "You said you were going to ask me for something and all you’ve done is just-"
    s "Wait, are you crying?"

    scene bluejay38
    with dissolve

    mak "But-"
    mak "I..."
    mak "Huh?..."
    s "…"
    mak "…"
    s "Okay. You know what? I think it’s time to get you out of here."
    mak "Y-Yeah..."
    mak "That’s...probably good..."
    mak "I’m not feeling well all of a sudden..."

    scene black
    with dissolve2

    "I take Makoto’s hand as soon as she makes it down the ladder."
    "She refuses to let go the entire way home."
    "I’m not sure what it is about her current situation that’s getting her down so badly, but I’m sure she’ll find her way out of it soon enough."
    "After all, her problems aren’t nearly as bad as they are for some of the others."
    "I’m sure she’s fine."

    $ renpy.end_replay()
    $ makoto_love += 3
    $ makotodorm25 = True

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikudorm35:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label makotodorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if makoto_love >= 5 and firsttimepornshop == True and makotofirsthall == True and makotodorm5 == False:
                jump makotodorm5
            if makoto_love >= 20 and day != 2 and makidate1 == True and pornshop20 == True and makotodorm20 == False:
                jump makotodorm20
            if makoto_love >= 25 and makotofirsthall == True and pornshop25 == True and trinity3track == True and mikudorm30 == True and makotodorm25 == False:
                jump makotodorm25
...
```