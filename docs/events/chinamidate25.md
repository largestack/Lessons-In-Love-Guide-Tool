# Death Trap (Chinami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chinami love greater than or equal to 25

* Event [Jeeves Tsukioka XIII](./tsukasaspecial1p2.md) (Tsukasa) is completed)

* chinaminumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: chinamidate25
* Group: Chinami
* Triggered by label: callchinamimorning
* Triggered by branch label: callchinamimorning
* Triggered by path: callchinamimorning->chinamidate25

## Official wiki page

[Death Trap](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chinamidate25&go=Go) for more details.

## Event code

File: (install folder)\game\ChinamiEvents.rpy

Code:
```python
...
label chinamidate25:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."

    play sound "phonebeep.wav"
    play music "happyandplotting.mp3"

    ch "Good morning!"

    "And given the fact that she is near constantly glued to her phone, she answers after only half a ring."

    s "Good morning, Chinami. You sound...livelier than normal for this time of day."
    ch "Chinami is excited because her business partner is coming over today! And Chinami heard that you were supposed to come as well!"
    s "Was that today?"
    ch "It was!"
    s "Wow, what a convenient coincidence. Is Chika still around?"
    ch "Big sis Chika is going on a top secret mission. Chinami is unfortunately unable to tell you any more than that since the details are classified."
    s "No Yumi either?"
    ch "Big sis Yumi hasn’t come over in a little while. Chinami is starting to get worried, but she knows she’ll come back one day."
    s "So-"
    ch "Chinami thinks you should take the hint and just come over already! These questions aren’t helping anybody!"
    s "There’s no need to get impatient. I was just about to head there."
    ch "Nuh-uh. Chinami felt another question coming. That’s all you adults ever do. Just talk, talk, talk! You never look at the big picture!"
    s "Correct me if I’m wrong, but I’m pretty sure I am the only adult you know."
    ch "This is exactly what Chinami is talking about! You just don’t know when to stop talking!"
    s "Okay. I’m hanging up now."
    ch "Wait! Can you bring doughnuts? You can’t have a business meeting without doughnuts and Chinami might die if she gets them on her own."
    s "Nope. But I’ll see you soon."
    ch "So rude!"

    play sound "phonebeep.wav"

    "I hang up the phone and begin my journey over to Chika’s place."

    scene black
    with dissolve2

    "Why she’d ask {i}me{/i} to bring over food when I am both not her intern and significantly poorer than the other people she has coming over, I don’t know."
    "But expecting rational decisions out of isolated girls who spend the majority of their day slaughtering cartoons is probably not a thing I should be doing in the first place."
    "Either way, I board a bus to the old district instead of pushing my luck and trying to have Touka and whichever one of her drivers she chose today pick me up along the way."

    play sound "dooropen.mp3"
    scene chinamiplayshouse1
    with dissolve2

    "Which, of course, means that I show up later than the other two as public transportation is only reliable around 50%% of the time."
    "But on the bright side, Touka is wearing what has quickly become my favorite outfit of hers. And one that will make “babysitting” exponentially harder to do as my focus lies elsewhere."

    tk "Chinami! What’s that thing?!"
    ch "Chinami believes that is called a “stove!” It’s where big sis Chika cooks Chinami’s eggs."
    tk "Your sister cooks for you? Is that even allowed?"
    ch "Big sis Chika is the {i}only{/i} person who cooks for Chinami. Big sis Yumi has tried, but she isn’t very good."

    scene chinamiplayshouse2
    with dissolve

    tk "How come you never cook for me? Shouldn’t you try acting a little more like Chinami’s sister?"
    to "Can I start by covering your mouth so you can’t speak anymore?"
    tk "You’re lucky you’re my sister or I’d have you fired."
    s "You should really come up with a different solution for all of your problems than just firing people."

    scene chinamiplayshouse3
    with dissolve

    ch "Papa!"
    tk "Jeeves!"
    to "Oh, Sensei. You’re so late that I assumed you just forgot about our plans."
    s "Me? Forget? No way."
    ch "Chinami had no idea Papa’s real name was Jeeves! He looks like more of a Philip to her."
    tk "Philip Jeeves Tsukioka the Fourteenth!"
    s "Wasn’t it thirteen last time?"
    tk "I had to let another one go. Good butlers are just impossible to come by nowadays."

    scene chinamiplayshouse4
    with dissolve

    ch "Chinami doesn’t see any doughnuts. Who do you think you are, showing up so unprepared?"
    ch "Chinami even had to give a tour of her whole house all by herself! Do you have any idea how much work that was for her?!"
    s "If you stood in the doorway behind you, you probably wouldn’t have even had to move."
    ch "This is why Chinami needed you here. CEOs are not trained for small jobs like that. Chinami has far better things to do."
    tk "Chinami! Can we eat more cereal? It may be the last time I ever see it, so I want to cherish the experience!"

    scene chinamiplayshouse5
    with dissolve

    ch "Big sis Chika says only one bowl a day! Otherwise, Chinami will get fat and no man will ever love her!"
    tk "Can we play with your toys, then?"
    ch "Chinami doesn’t have any toys. But she will show you the super cool phone her Papa bought for her. It’s her most prized possession."

    scene chinamiplayshouse6
    with dissolve

    "Chinami and Tsukasa scurry off to the bedroom, leaving Touka and me alone in the other half of the apartment."

    to "Thank you...truly. This is not something I would have been able to do on my own."
    s "Not good with kids either?"
    to "It’s less that and more...umm...how should I put this-"
    s "The apartment?"
    to "It is an utter crime that people are allowed to live in such places."

    scene black
    with dissolve2

    "Touka follows the other two girls into the living room, prompting me to do the same as I don’t want to be the one to clean up the spilled milk and cereal all over the kitchen table."
    "Granted, I probably {i}will{/i} be the person to do just that before the day ends as I’m not sure if Touka and Tsukasa even understand the concept of cleaning on their own instead of having a maid do it for them."

    scene chinamiplayshouse7
    with dissolve2

    "I guess I could always just make Chinami do it, though. It’s about time she learned some responsibility rather than just manipulating me into doing her dirty work."

    to "What even is this strange piece of furniture? A...sculpture? I’ve never seen anything like it before."
    s "Me neither, but it’s been here since I started coming and I just haven’t had it in me to question it."
    ch "That’s the TV antenna from the room below us! Nobody lives there anymore, but Chinami heard the whole place will fall apart if we try to remove it!"
    ch "So please be careful! Chinami doesn’t want to be homeless!"

    scene chinamiplayshouse8
    with dissolve

    to "I don’t think I can do this, Sensei. This place is as good as a death trap. I’m not even sure if I’ll be able to sleep knowing this poor girl will be spending the night here."
    to "Oh. And to clarify, I meant poor in regard to the amount of pity I feel for her. That was not me suggesting how much better off I am. "
    to "Though...saying that out loud may have just had the opposite effect."
    to "What I’m trying to say is-"
    s "I get it, Touka. The apartment sucks. But it’s all the Chosokabes can afford, unfortunately."
    tk "Hey, Chinami. What’s that over there?"
    ch "That’s called a “television!” Big sis Yumi found it on the street and sometimes the picture even stays clear for ten whole minutes!"
    tk "Not that. The thing next to it."
    ch "Oh! Chinami will show you!"

    scene black
    with dissolve2

    "Chinami runs over to the same table she ran to the first time I ever came here..."
    "And lifts up the same photo frame she showed me before thinking about castles became a near daily occurrence."

    scene chinamiplayshouse9
    with dissolve2

    ch "This is Chinami’s mom! Isn’t she pretty?"
    ch "Chinami wants to look like her when she gets older. But she thinks big sis Chika will probably look more like her than Chinami will. "
    tk "Do you look more like your dad or something?"

    scene chinamiplayshouse10
    with dissolve

    ch "Chinami doesn’t really know what her dad looks like. But maybe!"
    ch "If Chinami didn’t have this picture of her mom, she probably wouldn’t know what she looked like either. She’s been gone for a long time."
    tk "I see."
    tk "So you don’t really know what it’s like to have parents at all, huh?"
    to "Tsukasa, don’t ask questions like that! It’s extremely insensitive."

    scene chinamiplayshouse11
    with dissolve

    ch "Chinami doesn’t mind! Her mom still watches over her while big sis Chika and her teacher give her all the love she needs to survive."
    ch "She does wish she was still alive, though. And she wishes her dad was still here too, but big sis Chika gets angry whenever Chinami says that, so she doesn’t say it much."

    scene chinamiplayshouse12
    with fade

    to "I am beginning to believe that everything about today has been carefully designed to reduce me to tears. It is a miracle I haven’t cried yet."
    to "It’s no wonder you chose Chika over me during the first annual Super Mega Ultimate Dorm Wars. No high end restaurant nor plate of foie gras could compete with this..."
    to "This...heart wrenching, unreserved look into the lives of those less fortunate than me. Or even {i}you,{/i} for that matter. "
    to "How do things get to this point for some people while so many others live life completely unaware of the dire straits our fellow man can wind up in for no good reason at all?"
    s "Can I say something about living inside a bubble without you making some sort of allusion to the Tsukioka bubble wrap empire?"

    scene chinamiplayshouse13
    with dissolve

    to "Not anymore, you can’t. Now, that’s going to be the only thing I can think of."
    tk "Onee-chan! Jeeves! Play with us!"

    scene chinamiplayshouse14
    with dissolve

    to "Play with you how? There’s hardly any room to do anything here and Chika advised that we must not take Chinami outside. "
    tk "Let’s play house so Chinami can know what it’s like to have a family!"
    to "Tsukasa! Please don’t say such insensitive things!"
    ch "It’s okay! Chinami wants to play too! She thinks it sounds fun and has never played a game with this many people before!"
    ch "She is afraid she will mess up, though! So please tell her if she’s doing anything wrong!"
    to "H...How exactly does one play “house?”"
    s "We have two girls with a skewed perception of standard family dynamics, one girl with virtually {i}no{/i} perception of that, and me. There is no way this is going to end well."
    tk "It’ll be fine! Chinami and I will be sisters and you two can be the parents!"

    scene chinamiplayshouse15
    with fade

    to "P-Parents?! Us?!"
    s "Where else did you think this was going?"
    to "I had {i}assumed{/i} that I was going to be your daughter as well. I have no idea how this game works."
    s "You can call me “daddy” if you want. I don’t mind."

    scene chinamiplayshouse16
    with dissolve

    to "Of course {i}you{/i} don’t mind. But that’s absolutely not something I want to be calling you in front of my little sister."
    s "So what I’m hearing is it would be okay if we {i}weren’t{/i} in front of your little sister."
    to "That is what you are hearing because that is what you {i}want{/i} to hear. The reality is-"
    ch "Chinami says stop flirting and play already! "
    tk "I think we’re already playing. Those two seem to have gotten in character rather quickly. Wouldn’t you agree, Chinami?"
    ch "Oh! Chinami has no clue. She’s never seen real parents talk to each other before."
    s "What am I supposed to call you?"
    to "“Touka” would be a good place to start, but even that seems to prove challenging for you the vast majority of the time."
    s "How about “darling?” Does that work?"
    to "I suppose, so long as it never leaves this room."
    tk "Jeeves! Uhh...I mean...Papa! We want attention! Give us attention!"
    ch "Chinami wants to eat peanuts!"

    scene black
    with dissolve2

    s "I don’t care how badly Chinami wants to eat peanuts when peanuts will kill her."
    tk "Mother! Chinami is having suicidal thoughts and must be talked back from the brink of death!"
    to "Why did we immediately jump to the hardest possible part of parenting?! I’ve only been a mother for thirty seconds! I’m not prepared for this!"

    scene chinamiplayshouse17
    with dissolve2

    "The four of us take a seat on the bed (You know, the way real families always do) and just...start staring at one another."
    "In other news, this game sucks."

    scene chinamiplayshouse18
    with dissolve

    "But at least it gives me another opportunity to gaze down at what is at least temporarily and fictionally mine. "

    tk "Mother. Mother. Father is staring at your chest."
    to "He does that, dear. It’s not something that can be helped."
    ch "Mommy, can I ask you a question?"
    to "Of course, Chinami. What is it?"
    ch "How come Chinami doesn’t look like either one of her parents?"

    scene chinamiplayshouse19
    with dissolve

    to "Father?"
    s "There can only be one explanation."
    s "Your mother is having an affair."

    scene chinamiplayshouse20
    with dissolve

    to "What?!"
    ch "Mommy, why?!"
    tk "Is it with the gardener?! I’ve seen the way you’ve been looking at him!"
    to "You’re already turning the whole family against me?! It hasn’t even been five minutes!"
    s "You did this to yourself, darling. All I ever did was love you."

    scene chinamiplayshouse21
    with dissolve

    ch "Tsukasa, what is an affair? Chinami was just playing along, but she doesn’t really know what that word means."
    tk "I’m pretty sure it’s when a mom or dad starts spending time with somebody else’s mom or dad. Which might explain why you don’t look like them, Chinami."

    stop music fadeout 10.0

    tk "What we need to do now is find your real dad! And we can start by making a list of all of the men Mother is seeing behind Father’s back!"
    s "Just how many others are there, Touka? Tell me."
    to "Hah..."
    to "I really hope Chika’s day is going better than mine so far..."

    scene black
    with dissolve2

    "{i}Meanwhile, Chika’s day...{/i}"

    $ renpy.end_replay()
    $ chinamidate25 = True
    $ chinami_love += 1
    $ touka_love += 1

    jump yumichikaspecial1

label chinamidate30:
...
```

## Code that triggers this event

File: (install folder)\game\ChinamiEvents.rpy

Code:
```python
...
label callchinamimorning:
    if chinami_love >= 0 and chinamidate1 == False:
        jump chinamidate1
    if chinami_love >= 10 and christmas7 == True and chinamidate10 == False:
        jump chinamidate10
    if chinami_love >= 15 and day355 == True and chinamidate15 == False:
        jump chinamidate15
    if chinami_love >= 25 and tsukasaspecial1p2 == True and chinamidate25 == False:
        jump chinamidate25
...
```