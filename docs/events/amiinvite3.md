# Best Friends Forever
Ami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amiinvite3&go=Go)



## Event preconditions
✅Event "[Maya: Stop Looking For Answers](./shrine35.md)" is completed (event=shrine35)

✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)



## Next events
* [Main: The Price of Experience](./day344.md)

## Event properties
* ID: amiinvite3
* Group: Ami
* Triggered by label: amiinvite
* Triggered by branch label: inviteover

## Event code
File: \game\AmiEvents.rpy
Code:
```python
...
label amiinvite3:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "I’m not really feeling like doing anything exciting tonight and, not to say that Ami isn’t exciting or anything, but I kind of just want to hang out at home."
    "And considering that inviting anyone else over would likely result in more stress than relaxation, my [niece] is the first person that comes to mind for a quiet night in."

    play sound "phonebeep.wav"

    ay "Sensei! Did you know there is a heart next to your name in Ami’s phone?"

    "The chance for a quiet night dies immediately after being born."

    a "{i}Ayane! Give me my phone back!{/i}"
    ay "Whoops! Sorry, Sensei! Here’s Ami~"

    "A minor scuffle bleeds through the receiving end of the telephone and Ami eventually finds her correct place in the conversation."

    a "Hey. What’s up?"
    a "If you’re just calling to let me know that you’re going to be out late, that’s fine. Ayane is sleeping over anyway."
    s "I was actually going to see if you wanted to hang out with me tonight."
    a "Ayane! Something came up and you have to go home!"
    s "Ayane can stay. It’s fine."
    a "Is it really, though?"
    ay "{i}Hey! I heard that!{/i}"
    s "Just hang out there and I’ll come meet up with you guys."
    a "Wait! Sensei..."
    s "What? What’s wrong?"
    a "Um..."
    a "I was just wondering if..."
    a "Can you buy us ice cream on the way home?"
    s "…"
    s "Are you kidding?"
    a "I love you! Bye!"
    ay "{i}Me too! I love-{/i}"

    play sound "phonebeep.wav"

    "Ami hangs up the phone and my quiet night in has suddenly turned into one more rollercoaster in the amusement park that is life."

    scene black
    with dissolve
    stop music fadeout 5.0

    "I slide my phone into my pocket, replacing it with my wallet before checking how much cash I have on me."
    "And, before I know it, I find myself in the check out line of a convenience store with several pints of ice cream in my hands."
    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    play music "thesleepingcity.mp3"

    s "I’m home..."

    "I don’t know how I managed to go from “cool guy breezing his way through a brand new life” to “generic [uncle] buying ice cream for girls,” but here we are."

    if bonus == True:
        if ami_virgin == False:
            "Granted, I’m also having sex with both of these girls, so I guess I’m not entirely normal."
        else:
            "Granted, I’m also having sex with one of these girls, so I guess I’m not entirely normal."

    "Either way, I toss the bag directly into the freezer and make my way into the living room to find Ami and Ayane already in their pajamas."

    scene amiayanesleepover1
    with dissolve2

    a "Welcome home, Sensei!"
    ay "Where are our goodnight kisses?"
    s "Are you two already going to sleep?"
    ay "Will you kiss me if I say yes?"
    s "…"
    s "Any response to that, Ami? "

    if ami_virgin == False:
        a "Will you kiss {i}me{/i} if I say yes?"
    else:
        a "Yes. Even think about it and I will sew your mouth shut for the rest of eternity."

    s "I’m not kissing anyone."
    s "In fact, the only reason I came back at all was to unwind."
    a "And to spend time with your beloved [niece]."
    ay "And her best friend. Me."
    s "Yes. I’m here to spend time with both of you."
    s "I’m pretty sure the ice cream delivers that message pretty well in the event of my words somehow managing to fall flat."
    a "Thank you! I thought for sure you were gonna be like, “Bahhh ice cream is exhausting” and then just come home without any."

    scene amiayanesleepover2
    with dissolve

    a "Ayane’s been freakin’ out about ice cream all day so we were probably just gonna go get some ourselves if that happened."
    ay "Not {i}all day{/i}...Just for the last ten hours or so."
    a "Yeah. All day."
    s "How come it’s just you two tonight?"

    scene amiayanesleepover3
    with dissolve

    a "What do you mean?"
    ay "Are Ami and I not allowed to hang out alone anymore?"
    ay "Is it because you’ve seen us kiss?"

    if bonus == True:
        a "Please don’t bring up the kiss, Ayane."
        ay "Ami has very soft lips. They’re like two little lemon-flavored pillows."
    else:
        s "Ew, no."

    scene amiayanesleepover4
    with dissolve

    a "Can you cut it out, please?!"
    ay "I love you, Ami! Let's kiss again for Sensei! "

    if bonus == True:
        s "What I was getting at is that there’s normally a third girl with you. "
        s "The one with the hair and the...weight of the entire universe on her shoulders."
    else:
        s "Staaaaaaaaahhhhhhhp."

    scene amiayanesleepover5
    with dissolve

    a "Oh, Ayane and I just wanted it to be the two of us tonight. "
    a "It’s not like we didn’t {i}want{/i} Maya here or anything, but sometimes it’s good for it to just be us two so we can talk about old times and stuff."
    s "You’re [teenager]s. There are no “old times” for you."

    scene amiayanesleepover6
    with dissolve

    a "Maybe not {i}old{/i} times...but times the two of us spent together that no one else knows about."
    a "Isn’t it fun to have secrets like that with someone, Sensei?"
    s "I wouldn’t really know. "
    s "Besides, I’m sure that any “secret” I have would be found out by you two almost immediately."

    scene amiayanesleepover7
    with dissolve

    a "That’s right. So don’t even think about hiding stuff from the original Sensei Love Squad."
    ay "I wouldn’t say “immediately...” but yeah. We’d find out eventually."

    if sarabar20 == True:
        s "Oh, right. Didn’t you have something you wanted to talk to me about, Ayane?"

        scene amiayanesleepover8
        with dissolve

        ay "Oh! Uhh...yeah! Soon!"
        ay "Not right now, though! This isn’t really the best time..."
        a "What did you have to talk to Sensei about? You never said anything to me."
    else:
        ay "Oh, and...umm...Sensei?"
        s "Yes, Ayane?"
        ay "If it's okay with you...there's something I'd like to talk about with you soon."
        ay "Obviously not tonight, but...yeah."
        s "Sure. Can I ask what this is about?"

    scene amiayanesleepover9
    with dissolve

    ay "Just...some stuff..."
    a "About?"

    if bonus == True:
        ay "About..."
        ay "Boobs."
        a "…"
        ay "…"
        a "Please don’t talk to my [uncle] about boobs. Even if you are an honorary member of the original Sensei Love Squad."
        s "Okay, I didn’t want to ask the first time I heard it, but this is the second time it’s been mentioned within sixty seconds."
    else:
        ay "Necklaces made out of-"
        s "So, anyway-"

    s "What exactly is the “Sensei Love Squad?”"

    scene amiayanesleepover10
    with dissolve

    a "A two person organization me and Ayane formed to put all of the followers in their places!"
    ay "That’s right! "
    ay "Ami and I have spent years fighting for your affection and we will not stand for random pink haired girls walking into your life and trying to take you from us!"
    ay "Even if you’ve technically known those random pink haired girls longer than you’ve known me!"
    a "And even if those girls happen to be extremely nice!"
    ay "And pretty!"
    a "But with horrible taste in clothes!"
    ay "But still very pretty!"
    s "No one is going to {i}take{/i} me from anyone. I’m not property."

    scene amiayanesleepover11
    with dissolve

    ay "Not {i}yet{/i}..."
    a "Ayane..."

    scene amiayanesleepover12
    with dissolve

    ay "But really, though! I have no idea what her deal is!"
    ay "I’ve known Ami since elementary[school] and I’d never even heard of that Noriko girl until she walked into class."
    a "My memory from all the way back then isn’t really good...so I can’t really think of when I would have seen her either."
    s "She remembers you, though. And so does her sister."

    scene amiayanesleepover13
    with dissolve

    a "Niki remembers {i}me{/i}?!"
    s "Well, she remembers that you exist. I don’t know if you two ever met."
    ay "Isn’t it weird that I’ve never met her if you’ve known her for that long, though?"
    ay "I spent almost every night here once my mom left and...if you two really go back that far..."
    ay "I just don’t get it."
    s "It’s a confusing situation. I don’t really think I fully understand it yet either, to be completely honest."

    scene amiayanesleepover14
    with dissolve

    a "I remember when he used to tutor and stuff, and he definitely started doing it more around the time we became friends."
    a "What I'm confused about is how someone can just happen to {i}lose{/i} somebody they claim to care about for as long as she {i}lost{/i} Sensei."
    a "Wouldn’t that mean like, she doesn’t love him at all? It’s not like we’ve lived anywhere other than here and the old district."
    a "Do {i}you{/i} think you’d ever lose Sensei for that long? Because I know {i}I{/i} wouldn’t."
    ay "Well...circumstances are different for everyone, but..."

    scene amiayanesleepover16
    with dissolve

    ay "No."
    ay "I don’t think that would ever happen with me. I wouldn't let it."
    a "Exactly. Which is why I’ve decided that Noriko doesn’t love you at all and only I do."
    ay "And me."
    a "And Ayane by default, I guess. But she’s too needy and you’ll never pick her."

    scene amiayanesleepover15
    with dissolve

    ay "You’re being a lot meaner than normal about this today..."
    a "You think so? Cause it seems kinda like you’re just not fighting back as hard as you normally do."

    scene amiayanesleepover16
    with dissolve

    a "Either way, Noriko might be nice and related to one of my favorite pop stars, but that doesn’t mean that I think she’s at all deserving of your time, Sensei."
    a "I don’t know when you “disappeared” on her, but I know that you’ve been here for me for as long as I’ve needed you."
    a "So I am obviously your favorite and everything I say goes."
    s "Is that how this works?"
    a "Yup! I {i}worked{/i} for the love you give me. It’s not fair if you give the same amount to people just because they want it."
    ay "I don’t think “love” is something you should have to work for, but I do know I love you."

    scene amiayanesleepover17
    with dissolve

    a "Ayane! I-"
    ay "And you too, Ami."
    ay "I love both of you guys. You’re pretty much the only family I have now."

    scene amiayanesleepover18
    with dissolve

    ay "And sure, you might have a few extra years on me in time spent with him."
    ay "And sure, you might get to wake up in the same house as him every day while I have to wake up on the other side of town."

    scene amiayanesleepover19
    with dissolve

    if bonus == True:
        ay "And sure, he might get to see you walk around the house naked all the time and force you to cook him breakfast in nothing but an apron!"

        "Oh, that’s a good idea. I should do that."

        ay "But I am a better cook with nicer boobs and just as much, if not even more love to give!"
        ay "And sure, I-"
        a "Please don’t keep going. That’s more than enough, Ayane."
    else:
        ay "And sure, he might get to eat your french toast more often than he eats mine!"
        a "Ayane, stop. Nobody likes your french toast. You use low quality bread and not enough cinnamon."

    scene amiayanesleepover20
    with dissolve

    ay "Fine. But you have to tell me you love me too."

    if bonus == True:
        a "After you literally just made the one comparison that no growing girl should ever make to another one?"
        ay "Want me to massage them for you? I heard it helps them grow."

    scene amiayanesleepover21
    with dissolve

    a "I love you too, okay?! Just keep your hands off of me and my boyf-[uncle]!"
    ay "Boyf[uncle]?"
    a "You know what I mean!"
    ay "I don’t. Please explain, Ami."
    s "This love squad or whatever really knows what it wants, huh?"

    scene amiayanesleepover22
    with dissolve

    a "Of course. And no matter what it is you might think, there is no one that wants your approval more than the two of us."
    ay "We even formed a whole organization to prove it. The first board meeting is next Saturday."
    a "Some stuff has clearly happened with your past that you either can’t share with us or just...don’t want to-"
    ay "And we’re okay with that. Kind of."
    ay "It really depends on what kind of stuff happened and what you’re willing to do to make it up to us."
    a "But at the end of the day, you’re {i}my{/i} Sensei. "
    ay "{i}Our{/i} Sensei."
    a "I said what I said."
    ay "Fine. But then I get to be {i}his{/i} Ayane."
    s "…"
    a "…"
    ay "…"
    s "Why are you two just staring at me? I told you I’m not going anywhere and that all I wanted to do was relax tonight."
    s "I did not sign up for a longform discussion on who wants or deserves me the most."
    s "Also, your ice cream is getting cold. Go eat it."
    ay "That is literally the point of ice cream, Sensei. Are you so far removed from happy things that you can’t even remember that?"

    scene black
    with dissolve2

    "The short answer: Yes."
    "The slightly longer answer: Yes. But it’s a little more complicated than that."
    "It’s not that I am entirely devoid of joy or “far removed from happy things.”"
    "It’s that I’ve come to associate them with the subsequent misery that so standardly follows them soon after."
    "Without joy, there can be no sorrow. And without sorrow, there can be no joy."
    "It’s a multi-tool of a saying that coerces you into either thinking “Things will get better” or “Things will get worse.”"
    "But what help does a cycle like that do?"
    "The first of those two things makes sense and is likely why the damn idea was ever brought up in the first place."
    "But if you hold those lines of text up to a mirror, the opposite side of that mirror fills up with the concept of perpetual joy being nothing short of impossible."
    "And so there is no need to look forward to those happier moments in life-"
    "Because things can only get worse from that point on."
    "Think nothing, but feel everything."
    "Distract yourself with sensations when emotions will not do the trick anymore."
    "For there are several sensations in this world that are worth any amount of pain they cause in result."
    "Praise be."

    scene amiayanesleepover23
    with dissolve

    a "Oh good...You’re still awake."
    s "I’m happy to see the love squad continued bonding after I retired for the night."
    a "Ha ha ha."
    a "She just sort of passed out like this."
    a "Do you think you could go get my blanket for me? I don’t want to wake her."
    s "Aww, look at my [niece] being such a caring and adorable best friend."

    scene amiayanesleepover24
    with dissolve

    a "Yeah..."
    a "Ayane’s been pretty stressed out lately."
    a "You already know she’s not the type to talk about her feelings and I think it’s starting to catch up to her."
    s "Is she going to be okay?"
    a "Are you worried?"
    s "Of course. I’d worry about you the same way."
    a "She’ll be okay. "
    a "She just needs some rest."

    scene black
    with dissolve2

    "I grab Ami’s blanket out of her room and bring it to her moments later."
    "Not wanting to move, she asks me to drape it over her and tuck the two of them in, to which I oblige because, as I mentioned earlier, I’m now nothing more than a generic [uncle]."

    if bonus == True:
        if ami_virgin == False:
            "A generic [uncle] who routinely fucks both his [niece] and her best friend, and wants nothing more than their unending happiness."
            "Their unending happiness and the chance to screw them both at once eventually."
            "I go to sleep."
        else:
            "A generic [uncle] who routinely fucks his [niece]’s best friend and proceeds to smile and act like nothing ever happened while tucking the two of them in."
            "I love Ami. I really do."
            "But a part of me hopes that she dreams of what I do to Ayane when she falls asleep tonight."
            "I go back to my room and pass out to the idea of her waking up from that dream."

    $ renpy.end_replay()
    $ amiinvite3 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon

label amimaid30:
...
```

## Code that triggers this event
File: \game\AmiEvents.rpy
Code:
```python
...
label amiinvite:
    if amiinvite1 == False:
        jump amiinvite1
    if amiinvite1 == True and amiinvite2 == False and amiinvite2miss == False:
        jump amiinvite2
    if amiinvite3 == False and shrine35 == True:
        jump amiinvite3
...
```