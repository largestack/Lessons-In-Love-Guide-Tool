# Maki Miyamura's Mom-Mode Mission (Maki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maki love greater than or equal to 5

* Event [Bluejay](./makotodorm25.md) (Makoto) is completed)

* Event [Beautiful Porn Salesman](./makidate1.md) (Maki) is completed)

* Event [Life is a Tomato](./bar25.md) (Sana) is completed)



## Next events

* [Main: As Loud as a Whisper Can Be](./day214.md)

## Event properties

* Id: makidate5
* Group: Maki
* Triggered by label: pornshopmaki
* Triggered by branch label: pornshopmaki
* Triggered by path: pornshopmaki->makidate5

## Official wiki page

[Maki Miyamura's Mom-Mode Mission](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makidate5&go=Go) for more details.

## Event code

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label makidate5:
    scene makiseconddate1
    with dissolve
    play music "citylife.mp3"

    "I show up at the porn shop to find Maki leaning up against the counter, admiring a large DVD display of several fully-nude women being gangbanged by a minimum of three men each."
    "It’s the first and only time I imagine I will ever see something like this, so I take a deep breath and focus on her in all of her immensely perverted beauty."

    maki "…"
    s "…"
    maki "I know you’re there, Sensei."
    s "Sorry. I was just thinking about how nice it is to see someone fully absorbed in their element."
    maki "That’s right. This is exactly where I belong."

    if bonus == True:
        maki "Surrounded by sex toys and all thirty-seven volumes of “Totally Anal.”"
        s "How do you even make that many volumes of something that sounds so simple?"
    else:
        maki "A totally legitimate DVD store."

    scene makiseconddate2
    with dissolve

    if bonus == True:
        maki "I can give you a discount if you want to find out."
        s "No, I think I’m okay. Not much of an anal person."
        maki "Neither am I but that doesn’t mean it’s not a nice surprise every once in a while."

    s "Right. Anyway, what are you up to?"
    s "No Makoto tonight?"

    scene makiseconddate3
    with dissolve

    maki "No Makoto for a little while, I’m afraid."
    s "What? Why?"
    maki "I’m not really sure, to be honest."
    maki "She’s seemed really...out of it lately."

    scene makiseconddate4
    with dissolve

    maki "You wouldn’t happen to have any idea why, would you?"
    s "Not a clue. She seemed fine the last time I saw her."
    maki "Huh...That’s really weird."
    maki "Normally I’d at least be able to tell what’s troubling her, but things are a little different this time."
    maki "Worst part is I can’t even ask her father. He was always much better at hearing her out than me."
    maki "I try my best but I normally just wind up making jokes and...she’s not the biggest fan of things like that."
    s "..."

    scene makiseconddate5
    with dissolve

    maki "Oh, am I talking too much? "
    maki "I didn’t mean to start ranting but there’s not really anyone I can go to when I need to vent, so you’re kind of just caught in the crossfire right now."
    s "What about Sara or Haruka? "
    s "I don’t mind listening but the two of them would probably be much better to vent to than me."

    scene makiseconddate6
    with dissolve

    maki "Sara...kind of sucks when it comes to talking about real-life stuff."
    maki "You guys are close so I’m sure you’ve heard about her son, right?"
    s "Yeah. Her daughter’s told me in the past that she doesn’t really like talking about it. "
    s "Still have no idea what happened, though."
    maki "Specifics don’t really matter. What {i}does{/i} matter is that she’s the same way about everything."
    maki "Just starts running away once things get real. "
    maki "And Haruka is kind of the opposite. "
    maki "She dives headfirst into problems, which is fine. But she normally spins things to be more about her and starts...relating a little too much..."

    scene makiseconddate7
    with dissolve

    maki "So, here we are. Maki Miyamura’s porn-shop-turned-counseling-corner."
    maki "Thank you for seeing me today. Am I able to sit wherever I’d like?"
    s "Yes. Please take a seat next to the lube. "

    if bonus == True:
        maki "Actually, I think I’d rather stand. The best lubricant is the kind you generate with your body."
        s "That’s fine as well. I’m on the same page as you in the lube department."
    else:
        s "I have years of experience as a guidance counselor, so I am sure I will be able to help you in some way."

    scene makiseconddate8
    with dissolve

    if bonus == True:
        maki "Thanks, by the way. "
        maki "I know I’m kind of just springing this on you out of nowhere when you want to go home and jerk off, so I really do appreciate it."
        s "It’s cool. I’m actually a guidance counselor for the[school] as well."
        maki "Oh, good. So I can blame you for my daughter not feeling well, then?"

    s "Did I say guidance counselor? I meant janitor."

    scene makiseconddate9
    with dissolve

    maki "Oh, come on. I’m kidding."
    maki "I wouldn’t actually blame you for something like that."

    scene makiseconddate8
    with dissolve

    maki "Makoto is brilliant, but she’s more stubborn than anyone else I’ve ever met."
    maki "I’m not sure where she got this weird drive to be the best from, but her father was kind of similar in [high_school]."
    s "You two started dating in [high_school]?"
    maki "Oh God, no. He was super popular and I was just some nerdy girl who sat with other nerdy girls at the nerdy girl lunch table."

    if bonus == True:
        maki "We met again in college and by that time I’d gotten pretty hot. So one thing lead to another and we actually kind of fell in love."
    else:
        maki "We met again a few years later and by that time I’d gotten pretty hot. So one thing lead to another and we actually kind of fell in love."

    scene makiseconddate10
    with dissolve

    maki "Or something like that, at least."
    maki "A lot of people seem to have a problem with us seeing other people, but neither of us really felt the same way."
    maki "My husband’s always been a bit of a player. And I was just happy that people started to think I was pretty somewhere along in life."

    scene makiseconddate11
    with dissolve

    maki "Also, I’m sure you’ve realized this by now, but I’m kind of a pervert."
    s "You? A pervert? {i}No...{/i}"
    s "Didn’t you say you could live without sex when we hung out at the cafe, though?"
    maki "Yup. And I still stand by that. "

    if bonus == True:
        maki "But it’s fun and it feels good, so why abstain when I’ve got a choice not to?"
        s "Agreed. Though, I doubt I’d be able to live as long as you without sex."
        s "I think I’ve become pretty dependent on it, to be honest."
        maki "Well as long as you’re not screwing my daughter, you’re free to do whatever you want."

        "About that..."

        s "Not even with your supervision?"

        scene makiseconddate12
        with dissolve

        maki "Hmm...interesting proposition."
        s "Is that really all it took for you to cave?"
        maki "Well I’d feel much more comfortable as long as I knew she was being treated well."
        maki "And I have to admit that it would be rather cute to see that diligent facade of hers crumble under intense pleasure."
        maki "And of course I’m sure you know I’m also joking right now and that I will happily be the outlet to absorb your sexual frustrations if the need arises."

        scene makiseconddate13
        with dissolve

        maki "Besides, I’m just the mature version of her anyway. "
        maki "You see petite girls for eight hours a day pretty much every day. I’m sure you’d welcome the thought of someone closer to your age and size."
        s "You seem extremely cocky all of a sudden, Maki."
        maki "Heh. Cock."
    else:
        s "As do I. I think sex becomes a sort of crutch for a lot of people when, in all actuality, it's nothing but a grossly personal act that does nothing but consume short bursts of time that could be better spent on furthering one's education."
        maki "You sound just like my daughter."

    scene makiseconddate14
    with dissolve

    maki "On a serious note, though..."
    maki "Please do let me know if you hear anything from Makoto."
    maki "I try to hide it around her, but I really do care about her."
    maki "And if there’s anything in this world that’s troubling her, I will do absolutely anything to make it stop."

    "My mind travels back to a conversation I’ve had with Makoto in her dorm recently."
    "I remember her saying something about how her mom has never really been the...{i}mom{/i} type, exactly."
    "Couldn’t all of that be remedied by Maki just...not intentionally hiding the way she feels about her daughter?"
    "Why is it so hard for some people to realize that all they need to do is be themselves?"

    s "Have you tried talking to her?"

    scene makiseconddate15
    with dissolve

    maki "You mean like...with words?"
    s "…"
    maki "…"
    s "Yes?"

    scene makiseconddate16
    with dissolve

    maki "Didn’t I already tell you she has a hard time talking to me?"
    maki "She’s a daddy’s girl. All she’s ever known her whole life is crumbling in the arms of a strong male figure. "
    maki "She can’t crumble in my arms because my boobs are too big and they’ll hurt her neck when she tries to squeeze me."
    s "Maybe just try a little harder then?"
    s "There are only a handful of reasons I can imagine Makoto keeping her troubles away from you."

    scene makiseconddate17
    with dissolve

    maki "Really? What are they?"

    "I guess I’ll lead in with the one Makoto has openly admitted to me in the past."
    "It’s not my place to fix her problems, so at least getting her mom to understand how to force them out into the open might benefit her in some way."
    "If something is really wrong with Makoto, Maki is surely able to do more for her than I can as some guy she’s only known for a few months."

    s "Well, the first reason is that she might want you to act a little more like a mom than a...Maki."
    maki "But I’m more experienced at being a Maki than I am at being a mom."
    maki "I’ve been a Maki for my entire life."
    s "Maybe try to be a Makoto instead?"
    maki "Be a Makoto..."
    maki "Hmm..."

    scene makiseconddate18
    with dissolve

    maki "The square root of 16 is 4."
    maki "I pretend to hate porn and I’m secretly self-conscious about my breasts."
    maki "I slept in the same bed as my parents up until I was nine years old."
    s "If you’re going to just keep revealing her secrets to me, I feel a little strange about listening."
    s "Please text them all to me instead so I can memorize them and use them as weapons against her."
    s "The part about the square root was pretty spot on, though."

    scene makiseconddate8
    with dissolve

    maki "Thanks. I have years of practice."
    maki "So, what’s the next reason? You said you had a few."
    s "The next would be something like..."
    s "Maybe she feels a little self-conscious around you?"

    scene makiseconddate5
    with dissolve

    maki "Around me? Why would she feel that way?"
    s "Well, you said it yourself, didn’t you?"
    s "You’re a more mature version of her with more experience and...chest-size."
    s "And by mature I mean only in age. If we’re going by personality, Makoto is much more mature than you are."

    scene makiseconddate19
    with dissolve

    maki "Hey! I take offense to that!"
    maki "I’m an adult! I do adult things like pay the water bill and check the mail!"
    s "You don’t need to be an adult to check the mail."
    maki "You do in my house!"
    maki "It would be really bad if Makoto checked the mail one day and found a sex toy I ordered or something!"
    s "She literally sells sex toys every single day."

    scene makiseconddate4
    with dissolve

    maki "Do you really think that could be an actual issue?"
    maki "If my own daughter was...intimidated by me, I’d feel like a complete failure."
    maki "All I want is for her to be happy and if she can’t even feel happy about {i}herself{/i} around me then I must have royally screwed up somewhere..."
    s "I’m not saying that’s what’s happening. It’s just a possibility."
    maki "I hope that’s not it..."
    maki "Is there anything else you think it could be?"
    s "There is one more thing- and it’s something most girls her age need to just toughen up and deal with."
    maki "And what’s that?"
    s "Well, basically what I just said."
    s "She needs to toughen up and deal with whatever is going on personally."
    s "Everyone goes through rough patches in life and Makoto is probably just going through something like that."
    s "She misses her dad. Maybe it’s just...father-withdrawal or something."

    scene makiseconddate17
    with dissolve

    maki "So..."
    maki "You’re saying to just wait it out and let her get over it?"
    s "Yeah. Pretty much."
    maki "…"
    s "…"
    maki "Aren’t you supposed to be a guidance counselor?"
    maki "That’s horrible advice."
    s "What?"
    maki "I know I haven’t been the most...motherly figure I could be, but no one in their right mind would ever just abandon their daughter and let them deal with hardships on her own."
    maki "If something is wrong, it’s a mom’s job to help her fix it."

    scene makiseconddate2
    with dissolve

    maki "Which is why I’ll probably sit down with her soon and figure out if there’s something the two of us can do as mother and daughter."
    maki "In a roundabout way, the horrible portion of your advice actually helped me figure something out!"
    maki "Was that your goal all along?"

    "…"
    "I actually thought that advice was pretty good."

    s "Yup. You got me."
    s "Talk to Makoto and let me know how it goes."
    maki "Will do!"
    maki "It’s time for Maki Miyamura’s Mom-Mode Mission!"
    maki "Like that alliteration, Sensei?"
    maki "I learned what that word means from my daughter. She’s so smart, isn’t she?"
    s "…"
    s "Yes, Maki. "
    s "She’s brilliant."

    scene black
    with dissolve2

    if bonus == True:
        "The conversation gradually drifts back into normal territory and, before long, Maki and I are conversing about sex positions and famous porn-stars."
    else:
        "The conversation gradually drifts back into normal territory and, before long, Maki and I are conversing about how exactly soda manufacturers get the soda into cans."

    "It’s slightly odd counting those two things as “Normal territory” but, with a girl like her, there isn’t much {i}abnormal{/i} territory."
    "I do hope she’s able to coax Makoto out of her shell soon, though."
    "I haven’t exactly noticed her acting any differently other than the walk back to her dorm after we went up to the roof, but..."
    "That just seemed entirely random."
    "Maybe it would be worth asking her about it myself?"

    $ renpy.end_replay()
    $ makidate5 = True
    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makidate10:
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
...
```