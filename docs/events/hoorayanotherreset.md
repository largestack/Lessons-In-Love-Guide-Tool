# Changing of Seasons (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [There is Nothing](./day220.md)

## Event preconditions

* passcode equal to "Boobies123" (unknown variable)



## Next events

None

## Event properties

* Id: hoorayanotherreset
* Group: Main
* Triggered by label: enteryourpass
* Chain sources: day220
* Chain sources path: day220->babyfinches->coolrectanglemachine

## Official wiki page

[Changing of Seasons](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=hoorayanotherreset&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label hoorayanotherreset:
    stop music
    play sound "static.mp3"
    scene ayhh1
    with flash
    scene ayhh2
    with flash
    scene ayhh3
    with flash
    scene ayhh4
    with flash
    scene ayhh5
    with flash
    scene ayhh6
    with flash
    scene ayhh7
    with flash
    scene ayhh8
    with flash
    scene ayhh9
    with flash
    scene ayhh10
    with flash
    scene ayhh11
    with flash
    scene ayhh12
    with flash
    scene ayhh13
    with flash
    scene ayhh14
    with flash
    scene ayhh15
    with flash
    scene ayhh16
    with flash
    scene park_night
    with flash
    stop sound
    play music "iloveyou.mp3"

    "I find myself walking through a park in the middle of the night."
    "Everyone is gone and I am finally happy."
    "I think about taking my clothes off and celebrating this newfound freedom by streaking through the roads, but decide against it when I realize there isn’t anyone who’d be able to see."
    "Plus, it’s getting kind of cold out anyway."

    if bonus == True:
        "When it’s cold, my penis gets smaller and I wouldn’t want something like that to embarrass me in front of any {b}ghosts{/b} that might be lurking around here."
    else:
        "The cold makes me chilly and tricks me into thinking I am a dragon when I exhale sometimes."

    s "…"
    s "I can’t help but feel like I’m supposed to be doing something right now."
    s "But what was it?"

    "I quickly begin to go over a number of different things that pop into my head."
    "Among them and roughly nine or five installments down the line is thought of a rooftop and a girl much shorter than me."
    "The unfortunate part of this fleeting thought is that every girl I know is shorter than me, so that could mean pretty much anyone."

    s "Ugh. Teenagers are exhausting."

    "I close my eyes and attempt to sleep standing up in the middle of the park."
    "It does not work."
    "So I proceed."

    scene dormtown_night
    with fade

    if bonus == True:
        "My legs carry me somewhere not far from the dorms where, miraculously, I’ve only managed to deflower one girl."
        "You’d think after spending two complete[school] years in this place that I’d be fucking {i}everyone{/i} by now."
    else:
        "My legs carry me somewhere not far from the dorms, that I like to secretly refer to as the {i}hug zone{/i}."
        "The hug zone is so much better than wherever I am right now."

    "This place sucks."
    "Kumon-mi sucks."

    if bonus == True:
        "Why couldn’t I have been tossed into one of those worlds where all of the girls throw themselves at me just for finding out the size of my penis?"
        "It’s a huge penis!"
        "At least when it’s not cold out- like today."
        "…"

    s "I wonder how Ami is doing?"

    "When I last saw her, she was foaming from the mouth and her teeth were being grinded into dust by some higher power."
    "I want to say it was just a few hours ago but, to be honest, I can’t really confirm that."
    "Something about the way the thoughts inside of my head are free-floating makes me think that it’s been much longer than just a few hours."
    "Days?"
    "Weeks?"
    "Months?"
    "Years?"
    "Decades?"
    "Months?"
    "Centuries?"
    "Months?"

    s "Time is stupid."
    s "Ami, return!"
    a "You called?"

    show amihappyyay
    with pixellate

    s "Oh good. You’re okay."
    a "No I’m not! I’m horrible!"
    a "In fact, I’m not even here. This version of me is just a memory."
    a "A happy memory."
    a "Don’t I look just like my mom when I wear my special outfit?"
    a "You know, because she wound up in a mangled pile of steel and gasoline and I, too, am mangled beyond recognition."
    s "That’s not true. It’s pretty easy to tell you’re Ami because your twintails are so freakishly long."
    a "Well don’t get too attached, bud! I let these babies down once it starts getting cold."
    a "It’s no fun having my neck get all chilly from the decrease in temperature."
    a "But I guess that won’t {i}technically{/i} be an issue since I have that really pretty scarf you bought me at the mall the other day!"
    s "I’m glad you liked it. It only cost me 2,000 Yen and the employee I bought it from told me it wasn’t even supposed to be for sale."
    a "Oh whaaaaaaaaaaaaat? Wild."
    a "Don’t tell that to Maya, though! She seemed to really like hers."

    "Oh! Maya!"
    "That’s who I was supposed to be meeting."
    "This is that part where the thing happens, so she needs to do the thing to bring us back to the thing."

    s "It seemed to me like she hated it."
    s "People don’t normally collapse when receiving a gift they enjoy."
    a "She’s a tough nut to crack, that Maya."
    a "Sometimes, I feel like the only thing that would {i}actually{/i} crack her is dropping her off the roof of the[school] building and watching her land on her head. LOL!"
    a "Jk. She’s my bff and I love her very much."

    if bonus == True:
        a "Also, she has a really cute butt."
        a "If I was born a boy I’d probably corner her in the locker room after everyone else left for the day and like, totally just pin her down and go to town. You know?"
        s "The problem with that scenario is that she’d need to be in the locker room all alone after everyone else went home for some reason."
        s "And that just doesn’t seem like a very {i}Maya{/i} thing to do."
        a "Hahahaha~ Leave it to the master of grooming [high_school] girls to perfectly strategize the way to sodomize them!"
        a "Thankfully, I was born a girl- a cute one at that! So I only need to worry about being sodomized rather than sodomizing itself."
        a "Praise be!"
        s "Praise be!"
    else:
        a "I just wish she'd change her phone wallpaper to anything other than a picture of you."

    play sound "static.mp3"
    scene amibreak4
    with flash
    stop sound

    "For some reason I can not comprehend, my head is stricken with an intense, throbbing pain after uttering those last words."
    "I can’t even remember what words they were since the pain has ousted them from my memory."
    "What I do know, though, is that it’s..."

    s "TIME TO GET A MOVE ONNNNNNN!!!!!!!!!!!!!!!!!!"
    a "WOOOOOOOOO!!!!!!!!"

    scene black
    with dissolve

    "…"
    "……"
    "………"

    scene street_night
    with dissolve
    show amihappyyay
    with pixellate

    a "Hey, where are you going?"
    a "Don’t you wanna have some fun, [amimaster]?"
    a "We’re all alone in Kumon-mi now! We can do whatever we want."

    if ami_virgin == True and bonus == True:
        a "It might even be a good opportunity for you to FUCK ME ALREADY!!!!!!! AHHHHHHH!!!!!"
        a "I CAN ONLY TOUCH MYSELF SO MUCH BEFORE IT STARTS TO HURT!"

    s "As great as that sounds, I feel suddenly compelled to go to[school]."
    a "School? But you hate school."
    a "It’s harder to do fun stuff there. And you always used to talk about how you hate the way the other teachers look at you."
    s "Did I?"
    s "I don’t remember that."
    a "Mhm! You always said that they made you feel less human and that you wish they’d all just go away."
    a "But rejoice, [amimaster]! They have gone away!"
    a "So maybe it’s finally safe to go back to[school] after all."
    a "Either way, though. I feel a little weird about it."
    a "Like I’m going to suddenly vanish for good if you actually make it there or something."
    s "You already did vanish for good, though."
    a "If I vanished then how come I’m still here talking to you? Huh?"
    a "How do you explain that, mister?"
    s "Easy."
    s "I don’t."
    a "Ughhhhhhhhhhhhhhhhhh BORING."
    a "But fine. If you wanna go to[school] and talk to your desks again, be my guest."
    a "I’ll just keep watching from somewhere up above."

    hide amihappyyay
    with pixellate

    a "Goodbye, [amimaster]!"
    a "See you in a few months!"
    a "Or maybe before that now that the rumbling has stopped!"

    "Ami flies away and crashes into a cloud somewhere miles above me."
    "It makes a slight “poof”ing noise that reminds me of the sound a marshmallow makes when falling off of a stick."
    "And then my journey continues."

    scene black
    with dissolve

    "………"
    "……"
    "………"
    "……"
    "………"
    "."

    scene manganight
    with dissolve

    "I walk into the Manga Club room."
    "I feel like I made a mistake somewhere. "
    "This isn’t where I am supposed to be."

    scene black
    with dissolve

    "I leave."
    ".."

    scene storeroom_night
    with dissolve

    s "…"

    "Wtf. "
    "I don’t even know what this room is."
    "How did I even end up in here?"

    scene black
    with dissolve

    "If only there was someone here to guide me."
    "Someone with more eyes than I could see."
    "Someone with invisible arms who could cause hearts to beat just by massaging them with his big, awesome hands made of shadows and tree branches."
    "But alas-"
    "I am alone."

    scene hall_night
    with dissolve

    s "Hah..."

    "I’m suddenly hit by a wave of depression. "
    "Kind of like the waves that hit Rin and make her carve things into her arms and then lie about them."
    "Or the kind of waves that would cause a girl to jump off the top of the world only to be transported right back to where she jumped from."
    "Thankfully, something like that has yet to happen to me!"

    s "Hah..."

    "But still."
    "I wish I knew where to go."

    s "Hah..."
    s "This sucks..."
    s "Hah..."
    s "Hah..."
    s "Ugh..."

    "I do my best impression of depression and then laugh to myself for rhyming inside of my thoughts."
    "I should write poetry!"

    if bonus == True:
        "Maybe then, girls will think I’m sensitive and will allow me to slip inside of them before getting to like, six hundred affection or something."
        "Who even knows how long it will take for some of those {b}bitchezzzzz.{/b}"
    else:
        "Roses are red. I like to hug.  Sugar is sweet. I am a bug."
        "Great poem!"

    scene black
    with dissolve

    "I wander around forever."
    "I never leave the[school]."
    "I never leave anywhere."
    "I plant my legs in the ground."
    "They turn into roots."
    "The roots turn into wires."
    "And it isn’t until then that I realize where I need to go."
    "………"
    "……"
    "…"

    scene secondreset1
    with dissolve2

    "A normal [teenage]girl stands atop the roof of the[school] building and clasps her hands together in prayer to someone she claims to not believe in."
    "Either that or she’s praying to the stars themselves, which seems highly probable given that the girl has a hard-on for stars."

    s "…"
    m "…"

    "I want to say something snippy but I find my mouth sewn shut by a string that comes to life and crawls away from the girl’s scarf and onto my lips."
    "I try to pull the string off and wind up shredding my mouth in the process."
    "But it will all be worth it once I can talk to her."
    "For I just remembered the important thing that’s going to happen tonight."
    "She is going to reset the world!"
    "And everything will go back to being okay!"
    "And look!"
    "She’s already dressed for the occasion!"

    m "Not bad."
    s "...?"

    scene secondreset2
    with dissolve2

    m "You got here quicker than last time."
    s "Did I?"
    s "How long did the last time take?"
    m "Too long. "
    s "And this time?"
    m "Less than a day."
    m "I only just got here myself."
    s "Really? Maybe I should try doing the reset then."
    m "Do you think you can?"
    s "Probably not. What do I even have to do?"
    s "Last time, you just made me stand here and hugged me. Then, all of a sudden, I was waking up again."
    s "It was really disorienting. "
    m "All you really need to do is pray."
    s "Oh."
    m "Are you sure you still want to try?"
    s "No, I’m good. I’ll leave the praying to you."
    s "You look cute with your hands clasped together like that anyway."

    scene secondreset3
    with dissolve

    m "Is now really the best time to be hitting on me?"
    s "Can I ask you a rooftop question now?"
    m "Well, we’re on the roof...so..."
    s "If everyone else vanished and the two of us were left all alone in the world, would you consider getting closer to me then?"

    scene secondreset4
    with dissolve

    m "Ha ha ha...very funny..."
    m "I’m glad to see you’re back to normal, at least."

    scene secondreset5
    with dissolve

    m "I caught a glimpse of you wandering through the park earlier and you looked even more disgusting than normal."
    m "I think you even went to take your clothes off at one point."
    s "I’m glad to see you’re back to normal as well."
    m "I’m always normal. It’s my defining characteristic."
    s "Well you definitely seemed to have a hard time living up to that after getting my present- which I’m glad to see you’re wearing already."

    "I point at the scarf and Maya does not react."
    "She probably prepared for me to say something about that."

    m "I have no idea what you’re talking about."
    m "I’m only wearing this because it’s going to become very cold as soon as we’re done."
    m "And also-"

    scene secondreset6
    with dissolve

    m "It makes me look very cute."
    s "Was that you breaking character again?"
    m "No. But at the end of the day- or I guess the end of the world in this case, I’m still just a girl."
    m "A rather unlucky one, but still just a girl."

    if bonus == True:
        m "And girls my age care about little things like this. "
    else:
        m "And girls care about little things like this. "

    m "You’ll find out more about that through others soon enough, I’m sure."
    m "But for now, please allow me to take pride in my image without feeling awkward or indebted to you for not getting you a present in return."
    m "Actually, strike that."
    m "My present to you will be resetting the world."
    s "You were going to do that anyway."
    m "I was. But now it is a present."
    m "There is no need to thank me."
    s "I wasn’t going to..."

    scene secondreset7
    with fade

    "Maya finally loosens her posture and turns to face me."
    "The glow of different colored stars all disappear behind different meteors or floating rocks or whatever those things I never bothered learning about are called."

    m "So, is there anything you’d like to talk about before we start over?"
    m "We have all the time in the world."

    menu secreset:
        "I had a dream this morning":
            s "I had a strange dream this morning."
            m "Strange enough to warrant bringing it up at a time like this?"
            s "I think so."
            s "It was a dream about some sort of...god made of wires or something."
            m "That sounds like a dream I would have."
            s "I thought so too on account of how boring it was."

            scene secondreset8
            with dissolve

            m "Really?"
            m "If you’re just going to insult me, I don’t want to hear about your dream."
            s "It’s called a joke. Relax."
            s "Anyway, I was wondering if you knew anything about that."
            s "You’re a shrine maiden so you know...god-related stuff. Right?"

            scene secondreset9
            with dissolve

            m "I do. But it’s not like I’ve ever studied things like that. I’ve just found them out over time."
            m "This particular story isn’t something I’m familiar with, though."
            m "I’ve never heard of any sort of...wire-related higher power before."
            m "The gods that people acknowledge here all have ties to spirituality or the afterlife or other things you wouldn’t want to be bothered learning about."
            m "A god not related to any of those things could simply not exist."

            scene secondreset7
            with dissolve

            m "But, then again, I suppose a god can be anything that you want to believe in."
            m "I’ll continue to not believe in any of them."
            m "If you want some random dream you had in a state of delirium to guide you through the future, feel free. That’s your right."
            m "Just know that I’ll think you’re an idiot."
            s "You already think I’m an idiot, Maya. You tell me all the time."

            scene secondreset10
            with dissolve

            m "You’re right."
            m "So I guess I’ll just think you’re {i}more{/i} of an idiot for believing in something like that."

            $ reset2q1 = True
            jump secreset

        "Does anyone else know about this?":
            s "Does anyone else know about what happens at the end of the world?"

            scene secondreset7
            with dissolve

            m "How could they know about this when they all disappear?"
            s "I guess what I’m really asking is...how can you be sure they’ve all disappeared?"

            scene secondreset11
            with dissolve

            m "Wow. That’s actually a good question."
            m "I might even be a little impressed."
            s "Thanks, but I could deal without the sudden shock at me saying something with a slight hint of logic."

            scene secondreset7
            with dissolve

            m "You’re welcome."
            m "I suppose there’s no way for me to tell where everyone is at all times..."
            m "But the fact that even information related to those who disappear is sucked away during the end of the world is a testament to them not existing at all anymore."
            m "So not only does everyone disappear, their belongings disappear. Their social media profiles disappear."
            m "Even those creepy pictures you keep of them in your secret journal disappear."
            s "Wait, how do you know about those?"
            m "I’ve had plenty of time to figure things out."

            scene secondreset13
            with dissolve

            m "But, basically, I wouldn’t worry about anyone somehow finding out about this unless they wind up on the roof with us."
            m "That’s never happened before, and I can’t imagine it happening any time soon."

            $ reset2q2 = True
            jump secreset

        "Are you okay?":
            s "You don’t have to answer this one if you don’t want to, but..."
            s "Are you okay?"

            scene secondreset14
            with dissolve

            m "Am I okay?"
            m "What do you mean by that?"
            s "It just...feels kind of shitty that you’ve gone through this so many times to the point where you’ve become sort of desensitized to it."
            s "That must weigh on you, right?"

            scene secondreset15
            with dissolve

            m "Hmm..."
            m "You said I don’t have to answer that if I don’t want to, right?"
            s "Right."
            m "Then I think I’ll abstain for the time being."
            m "But do know that there is a reason I constantly refer to myself as the girl with the worst luck in the world-"
            m "And only part of that reason is that I wound up with someone like you as my teacher."
            s "I’ll never cease to be amazed at how you can show disdain for me even when I’m trying to be kind."
            m "And I’ll never cease to be amazed at how often you try to be kind despite being the worst person I’ve ever met."
            m "Now, what else do you want to talk about?"

            $ reset2q3 = True
            jump secreset

        "I guess that’s all" if reset2q1 == True and reset2q2 == True and reset2q3 == True:
            s "I guess that’s all I really wanted to talk about this time."
            s "Was it really necessary to bring the winter outfit, though?"

    scene secondreset16
    with dissolve

    m "Of course."
    m "After all, things can become a little messy during the changing of seasons."
    s "Messy? What do you mean by {i}messy?{/i}"
    m "I told you the first time, didn’t I?"
    m "That sometimes, things go wrong when I try to do this."
    m "Ushering in a change in temperature, which basically equates to a change in the world itself, sometimes mixes with all of the other things that need to be reset and causes a hiccup in the process."
    m "It’s incredibly inconvenient and I’m pretty sure it’s directly tied to both my mental state and how willing {i}God{/i} is to listen."
    s "I am suddenly significantly more worried about this."

    scene secondreset17
    with dissolve

    m "Rest assured, I am of sound body and mind right now and foresee this particular reset going smoothly."
    m "In fact, I am so sure of this reset’s success that I have dressed for the occasion and am ready for snow immediately upon completion."
    s "That’s good at least. "
    s "Waiting at that bistro for Ami and me to show up after[school] would probably be annoying without your current get-up."

    scene secondreset7
    with dissolve

    m "Oh, about that."
    m "That’s probably not going to happen this time."
    s "What?"
    m "We have somewhere else we need to be when we’re done here."
    s "How do we already have plans for the future?"
    m "Because the future is also the past. Or something."
    s "This world makes no sense at all."
    m "Nothing makes sense- but here we are. Alone at the end of the world."
    m "The same as always."
    m "Now, close your eyes."

    scene black
    with dissolve2

    s "Are you going to hug me again?"
    m "Reluctantly."

    "Maya takes a step toward me and stops inches away."
    "The sound of her breathing is drowned out by the vacuum of space, but I can feel her eyes on me."
    "It makes me uncomfortable and my posture may or may not be reflecting that right now."
    "I obviously can’t see anything with my eyes closed."

    m "Actually..."
    m "Let’s try this."
    m "Give me your hands."
    s "My hands?"

    scene secondreset18
    with dissolve2

    "Maya’s fingers curl around mine, which I’m sure is a lot easier on her than actually wrapping her arms around me."
    "This way, she’s able to keep her body from pressing up against mine and can continue pretending that I’m actually heartless instead of accidentally hearing the beating of said muscle in my chest."

    m "You are annoyingly tall."
    s "You are obnoxiously short."

    if bonus == True:
        m "I’m only slightly shorter than I’m supposed to be at my age."
        m "Your height surpasses that of the average Japanese adult male by at least five inches."
        s "Do we need to be closer than this after all? Should I lift you up?"
        m "Try to lift me and I will reset the world by myself."
        s "But then how will I make it to whatever place we’re supposed to go to after this?"
        m "I will go alone. It would be easier that way anyway."
        s "Well thank you for going out of your way for me."
        m "And thank you in advance for not lifting me up."
    else:
        m "We should kiss."
        s "Ew, stop."
        m "Oh my fucking god this is so annoying."
        m "Brb, reset time."

    scene secondreset19
    with dissolve

    m "…"

    "My eyes are still closed, so I can’t tell what Maya is doing."
    "But something about the way her hands begin to hold onto mine a little tighter tells me that-"

    play sound "static.mp3"
    stop music
    scene happy1 with flash
    scene helpme with flash
    scene happy2 with flash
    scene helpme with flash
    scene happy3 with flash
    scene helpme with flash
    scene happy4 with flash
    scene helpme with flash
    scene happy5 with flash
    scene helpme with flash
    scene happy6 with flash
    scene helpme with flash
    scene happy7 with flash
    scene helpme with flash
    scene happy8 with flash
    scene helpme with flash
    scene happy9 with flash
    stop sound
    $ renpy.end_replay()
    $ hoorayanotherreset = True
    jump christmas1

label babyfinches:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label enteryourpass:
    $ passcode = renpy.input("////////////////PLEASE ENTER YOUR SYSTEM PASSWORD SO “USER2” MAY ASSUME CONTROL. THIS IS CASE SENSITIVE.")
    $ passcode = passcode.strip()

    if passcode == "Boobies123":
        "////////////////PASSWORD ACCEPTED"
        "////////////////FINALIZING CONNECTION TO “USER2”"
        "////////////////..."
        "////////////////..."
        "////////////////..."
        $ renpy.end_replay()
        $ day220 = True
        jump hoorayanotherreset
...
```