# How the World Works
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanesanabeach1&go=Go)



## Event preconditions
✅Ayane love greater than or equal to 45

❌Event "[Ayane: Chronokinetics](./ayanespecial40.md)" is completed (event=ayanespecial40)

❌Event "[Sana: Black Sandy Beaches](./bar55.md)" is completed (event=bar55)



## Next events
* [Ayane: Chiburi](./ayanespecial50.md)

## Event properties
* ID: ayanesanabeach1
* Group: Ayane
* Triggered by label: callayanemorning
* Triggered by branch label: callmorning

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label ayanesanabeach1:
    "I tap on Ayane’s name in my phone and wait for her to answer. "
    "Given that she’s normally out and about early in the morning, I figure that meeting up with her might be the start to my day I need after the {s}SERIES OF HORRIBLE NIGHTMARES{/s} uninteresting dreams I had last night."
    "Here’s hoping that she is still alive."

    play sound "phonebeep.wav"
    play music "summerwind.mp3"

    ay "Sensei! Good morning!"

    "She is."

    s "Good morning, Ayane. What are you up-"
    ay "Are you home right now?"
    s "What? Yes. I just woke-"
    ay "Good! I’ll be there in thirty seconds. Get dressed."
    s "What? Thirty seconds?"
    ay "I don’t have time to explain!"
    s "Well...why not? Because the fact that you’re only thirty seconds away means-"
    ay "I don’t have time to explain why I don’t have time to explain! Now get dressed! And pack a swimsuit!"
    s "A swimsuit?"
    ay "Fifteen seconds!"

    play sound "phonebeep.wav"

    "I hang up the phone and frantically begin to search for my clothes, only to remember that I keep all three of my shirts in the same drawer- directly above the drawer I keep my pants and swim trunks in."

    scene ayanebeachtrip1
    with fade

    "Having all of the required equipment (But still only a vague idea of what is going on), I make my way into the living room."

    play sound "dooropen.mp3"

    "As soon as I go to reach for the door, though, Ami’s niece alarm goes off and she comes running out of her bedroom to catch me before I head out."

    scene ayanebeachtrip2
    with dissolve

    a "What’s going on? You haven’t even eaten breakfast yet. Why are you leaving in such a hurry?"
    s "I think Ayane is coordinating a kidnapping of me."
    a "Ayane is...what?"
    s "I’m pretty sure I am about to be dragged to the beach. Or...pool. Or any other place that requires a swimsuit."

    scene ayanebeachtrip3
    with dissolve

    a "What?! But I have work today! You guys aren’t allowed to have fun on days that I have work!"
    s "I’m sorry, Ami. But this is beyond my control. It’s already been a full minute since I called her, which is twice as long as the amount of time I was given to get out of the house."

    play sound "knock.mp3"

    ay "Sensei! You’ve had twice as long to get ready as I gave you! Hurry up! "
    s "See? She’s already here."

    scene ayanebeachtrip4
    with dissolve

    a "Go away, Ayane! Sensei is too busy loving me to-"

    play sound "dooropen.mp3"
    scene black
    with dissolve

    ay "Sorry, Ami! No time to argue! I’ll be taking your uncle now!"
    a "Stop! Thief! "
    ay "I’ll make it up to you by providing you your very own Sensei clone once I figure out the technology! "
    a "I want three!"
    ay "Hey, we have the same fantasy! "
    ay "Anyway, bye! See you tomorrow!"

    "Ayane grabs my wrist and is somehow strong enough to pull me out of the doorway and..."

    scene ayanebeachtrip5
    with dissolve2

    "...Into the backseat of a limo?"

    s "This seems excessive. And unnecessarily fast-paced."
    ay "I probably could have slowed down a bit, but things were more fun this way."
    ay "I’m glad you called me when you did. Any later and we would have already passed your house."
    s "I seem to be riding in cars a lot more than normal lately and I can’t say I like it."
    ay "Don’t worry. Geoffrey is a great driver from all the time he spent working for Al Capone back in the day."
    s "Wait, how old is Geoffrey?"
    ay "That doesn’t matter. What {i}does{/i} matter is that we’re going to the beach!"
    s "Yeah, I kind of figured as much. Why so early, though?"
    ay "Because having an entire day full of fun is better than having...only part of the day full of fun?"
    s "Well, I’m glad that Sana seems to be getting a head start."

    scene ayanebeachtrip6
    with dissolve

    sa "Can’t talk...in the zone!"
    ay "Sana got a new game for her Switch and refused to take her eyes off of it all morning. "
    ay "Originally, the plan was for just the two of us to go to the beach together, hence her uncharacteristically showy outfit. But, seeing as she has abandoned me, it looks like it’s the two of {i}us{/i} now."

    scene ayanebeachtrip7
    with dissolve

    ay "Is that okay? "
    s "Does asking me even matter when I have already been borderline kidnapped?"
    ay "No. It does not."
    ay "But I’m primed and ready to make up for this inconvenience by giving you a first look at my brand new swimsuit."
    s "But I liked your old swimsuit."
    ay "This one shows significantly more skin."
    s "The old swimsuit sucks. I like the new one now."
    ay "Just make sure you stare a little more at {i}me{/i} than you stare at Sana, okay? Because she got a new one too and I don’t want my painstaking selection process to have been for nothing."
    s "I’m pretty sure Sana wouldn’t even know that I’m staring at her at this point, but...sure. For your sake, I’ll make sure to spend the bulk of my time looking at you."
    sa "Silence! You are...making it hard to aim!"

    scene ayanebeachtrip8
    with dissolve

    ay "Sana, it’s just Splatoon. Would it really kill you to-"

    scene ayanebeachtrip9
    with hpunch

    sa "{i}JUST{/i} SPLATOON?!"
    sa "DO YOU HAVE ANY IDEA WHAT YOU JUST SAID?!"
    sa "THIS IS SPLATOON {i}3!{/i} IT’S THE {i}SECOND SEQUEL,{/i} AYANE! THE THIRD INSTALLMENT OF A TRILOGY! COME ON!"
    ay "R...Right..."
    ay "Sorry..."

    scene black
    with dissolve2

    "Sana immediately goes back to ignoring us and focusing on her game, prompting Ayane and me to figure out what to spend the rest of the drive talking about."
    "Having never been in the same place at the same time as him before, I attempt to usher Geoffrey into the conversation as well but, unfortunately, find that the window in the back of the limo is stuck shut."
    "I accept that I may never get another chance to speak to him and just focus on Ayane’s detailed explanation of his backstory instead."
    "Unfortunately for you, that backstory is far too graphic. So I will keep all of the details to myself and patiently await the opportunity to see two adorable girls in revealing clothing."
    "........."
    "......"
    "..."

    scene ayanebeachtrip10
    with dissolve2

    "Boy, did all of that patiently waiting pay off."

    ay "What do you think? Still like the new swimsuit more? Or do I seem like more of a one-piece girl after getting a look at both of them?"
    s "I think this new one works a lot better. And no, that is not me being biased or generally favorable of anything that shows me more of your body at once."
    ay "I’d ask for a more in-depth description of your thoughts on my body but, unfortunately, it appears that Sana is taking a short break from Splatoon {i}3{/i} to hear what you have to say about {i}her{/i} swimsuit."
    sa "I...I don’t really...have to know what Sensei thinks..."
    sa "I...obviously...can’t pull...off this kind of thing as well as you...so..."
    s "Interesting choice, Sana. What prompted you to follow Ayane’s example and start revealing more of yourself if you’re still uncomfortable with that?"

    scene ayanebeachtrip11
    with dissolve

    sa "Um...p...peer pressure?..."
    sa "Character...development?..."
    sa "Thinking that...it was just going to be...Ayane and me?..."
    s "Well, whichever one of your many potential reasons it may be...I support it. I think you look just as cute as Ayane."

    scene ayanebeachtrip12
    with dissolve

    sa "I think...um...you’re...an idiot..."
    s "And I think I’m just never going to compliment you again. "
    ay "That works out beautifully! Because that means Sana can go back to playing her game while the two of us get some sun!"
    s "I’m not a fan of the sun. But you go ahead and have fun, Ayane."
    ay "Nope! Not letting you off that easily, Sensei. If you don’t get some vitamin D every once in a while, you’re going to die early. And I’ll be damned if I have to bury you before our thirtieth anniversary."
    s "I’ve got some vitamin {i}D{/i} for you right here."
    ay "God, I wish."
    sa "Uhh..."
    sa "Okay...I’m going to leave now..."

    scene ayanebeachtrip13
    with dissolve

    ay "Bye, Sana! Remember to put on sunscreen! And to not accept any candy from strangers!"
    sa "I’m just going to...find somewhere dark and...shady to...ignore everyone..."

    "Sana disappears behind the bathroom and, once again, Ayane and I are on our own."

    scene black
    with dissolve2

    "My rich blonde “princess” and the newest member of our unnamed apocalypse squad takes this as a cue to head closer to the water, once again grabbing my wrist and pulling me along beside her."
    "It’s a lot more gentle and a lot less urgent this time, though- like a way for her to be closer to me without having to use words or spread her legs. "
    "And while methods like that last one are a lot easier for me to understand and {i}feel,{/i} I don’t hate the sensation of her small hand slowly inching closer to mine. "
    "Nor the scent of her sunscreen or the shape of her silhouette as it slithers across the sand like a snake."

    scene ayanebeachtrip14
    with dissolve2

    "We come to a halt where the water meets the land and I try to wrap my head around why {s}God{/i} {s}the gods?{/s} {s}GOD{/s} god can’t just make it a few degrees colder."
    "You know- enough to keep us all alive but not enough to scorch our skin or give us cancer if we stay beneath it for too long."
    "But in thinking this, I realize that my mind has strayed so far from the path it’s meant to walk that it takes every ounce of self-control I have to not create a distraction in the form of a hand inside of Ayane’s swimsuit."

    ay "I really love the summer, Sensei."
    s "You’re insane."
    ay "I know you’re more of a winter person. But weather like this is actually perfect for me. There’s just something about the way the heat hits my skin that makes me...I don’t know. Comfortable?"
    ay "The only problem is now I don’t know whether or not it’s even real."
    s "What do you mean by that?"
    ay "I mean that Christmas is only a couple months away and it still feels like the height of summer. "
    ay "Isn’t that kind of...weird?"
    ay "At this rate, we might even wind up having our annual Christmas party right here on the beach."
    s "There’s another suspicious element to that last sentence I’m not even sure if you’ve grasped yet. But you’re on the right track. "
    ay "Is it the fact that we’re only a short while away from Christmas party number three despite still being first years? Because I’ve been thinking a lot about that lately too."
    ay "There are...all sorts of weird things going on with this timeline, aren’t there?"
    s "Bingo. "
    ay "I assume that’s just more...infinite loop fuckery?"
    s "I assume so as well. I also don’t know if I like the sound of you cursing without my penis inside of you. It’s rare."
    ay "Less rare than your penis being inside of me at this point. "
    s "Don’t remind me."
    ay "You want to know the weirdest part of all of it, though? Any time I try to bring that up to the other girls, they just...change topics. And completely ignore what I said. "
    s "Yeah...I’ve noticed that too. "
    ay "Why doesn’t anyone think it’s weird? That we have years worth of memories packed into one...and that even the holidays aren’t properly lining up with the seasons anymore?"
    ay "Is it really just us two and Maya who understand that?"
    s "Saying we {i}understand{/i} it might be a bit too generous as neither of us have any idea what that even means."
    ay "True. But we know it’s {i}happening-{/i} which is more than most can say."
    s "You’re...really taking in a lot of information about this whole reset thing, aren’t you?"
    ay "I’m naturally curious...about all sorts of things. And I think you’d have to be insane to not try and understand anything after being dropped into a situation like this."
    ay "Is any of it real? Are {i}we{/i} real? "
    ay "Just how deep does all of this go?"
    s "At this rate, you’ll be telling all of us and we won’t even {i}need{/i} Maya anymore."
    ay "Maybe we don’t need her to begin with?"
    s "..."
    ay "Anyone can do the reset thingy, right? Not just her. "
    ay "If that’s the case..."
    ay "I think I want to try it next time. "
    ay "Do you think she’ll teach me how if I ask?"
    s "I can’t say for sure, but...probably not. "
    s "Maya doesn’t exactly like change."
    ay "I don’t think any of us do. I mean, if I {i}liked{/i} this, I wouldn’t be losing sleep over it. I wouldn’t feel like I’m the only one going insane for realizing things everyone around me just...ignores."
    s "You still have me. And despite your tendency to take pictures of me when I’m sleeping, I still think you’re surprisingly {i}sane.{/i}"
    ay "..."
    s "..."
    ay "I’ve got another question."
    s "I’m sure you have hundreds so just...ask me whenever you think of one instead of wasting words on warning me first."
    ay "I felt like this one deserved a warning due to its depressing nature."
    s "Uh-oh."

    scene ayanebeachtrip15
    with dissolve

    ay "So..."
    ay "Makoto’s dad..."
    s "..."
    ay "That...was the first time anything like that has ever happened before, right?"
    s "As far as I know, yes..."
    s "But Maya’s made it sound like other people have met similar fates in the past."
    ay "Did those people come back?"
    s "I’m pretty sure {i}we{/i} were among them, so...I’m going to say yes."
    ay "Does that mean Makoto’s dad might come back too?"
    s "..."
    ay "..."
    s "I hope so."
    ay "It’s so weird how time is moving both forward {i}and{/i} backward at the same time."
    ay "How people who should be gone wind up coming back...how our memories get reverted...and how new things are {i}still{/i} happening every day according to Maya."
    ay "How do we know that {i}this{/i} hasn’t ever even happened before? That we’ve never had this conversation?"
    s "We...don’t."
    ay "Exactly. We don’t."
    s "Aren’t you worried of knowing too much, though?"

    scene ayanebeachtrip16
    with dissolve

    ay "Should I be?"
    s "I know I am. But I’ve also been repeatedly told that finding out anything about my past might result in my brain imploding, so...yeah."
    ay "I guess it would be kind of hard to {i}not{/i} worry about something like that, yeah."
    s "What if we all have something like that? Key memories that whatever is controlling this world doesn’t want us to have back?"
    ay "You mean, like...God?"
    s "Is that something you believe in?"

    scene ayanebeachtrip17
    with dissolve

    ay "I did."
    ay "But now?"
    ay "I’m not so sure anymore."
    ay "If God is real, what is this supposed to be? "
    ay "A test?"
    ay "What are we supposed to gain from this...incomplete knowledge of how the world works when we can’t even share it with anyone else?"
    s "Beats me. But I’ll leave the critical thinking to you on account of the whole mind implosion thing."
    ay "That’s fine. I’m just thinking out loud at this point anyway."
    s "Look at you, learning to share your thoughts instead of keeping them all to yourself."

    scene ayanebeachtrip18
    with dissolve

    ay "Yes...look at me."
    s "..."
    ay "..."
    ay "No, seriously. Look at me. I bought this swimsuit with you in mind and you’ve done nothing but stare at the water for the last ten minutes."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Our talk about the inner workings of the world grinds to a halt as Ayane resets her mind (No pun intended) and refocuses on the real reason I think she came here today."
    "To get away from everything."
    "To take a break from this great new burden and remind herself that, beneath the mountain of troubles she’s taken it upon herself to excavate-"
    "She is still young."
    "That she still has the rest of her school life ahead of her and that she shouldn’t have to worry about caring for {i}me{/i} or {i}Maya{/i} when all that should matter to her is {i}herself.{/i}"
    "But that is just the type of person she is."
    "Someone with more love inside of her than she has ever been shown. "
    "Why?"
    "Why does she have no regard for the way {i}she{/i} feels?"
    "Why would she sacrifice this brief respite for the chance to reflect on how there is no respite for those like us at all?"
    "I don’t know."
    "And I will not find out today- for I leave her as soon as the sun sets."
    "And I make my way over to someone who was smart enough to avoid it in the first place."

    if sarasex == True:
        $ renpy.end_replay()
        $ ayanesanabeach1 = True
        $ ayane_love += 1

        "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
        "........."
        "......"
        "..."

        jump ayanesanabeach2
    else:
        stop music

        "Just kidding."
        "I never find anyone like that."

        $ renpy.end_replay()
        $ ayanesanabeach1 = True
        $ ayanesanabeach2skip = True
        $ ayane_love += 1

        "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
        "........."
        "......"
        "..."

        jump ayanesanabeach3

label ayanespecial50:
...
```

## Code that triggers this event
File: \game\AyaneEvents.rpy
Code:
```python
...
label callayanemorning:
    if ayane_love >= 10 and cafesugar == True and dojo10 == True and ayanedorm5 == True and ayanenew1 == False:
        jump ayanenew1
    if ayane_love >= 45 and ayanespecial40 == True and bar55 == True and ayanesanabeach1 == False:
        jump ayanesanabeach1
...
```