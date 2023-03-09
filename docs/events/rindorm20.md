# Delirium
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm20&go=Go)



## Event preconditions
✅Rin love greater than or equal to 20

✅Event "[Rin: Nothing Was Missing, Except Me](./cafe20.md)" is completed (event=cafe20)

✅Event "[Main: Missing](./day50.md)" is completed (event=day50)



## Next events
* [Main: One to Seven](./day63.md)
* [Rin: Good Day, Humans](./cafe25.md)
* [Rin: Sock Fetish](./rindorm25.md)

## Event properties
* ID: rindorm20
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label rindorm20:
    play sound "knock.mp3"
    stop music fadeout 10.0

    s "Rin? Are you in there?"

    "…"

    "No answer, as expected."
    "I can't blame her for not wanting to be seen when our last run-in ended with her essentially being kicked out of work-"
    "But that doesn't mean I can't worry either."
    "I have a heart."
    "It may be shriveled and bruised and all sorts of worthless, but it still pumps blood. Blood that, as we speak, is draining from my face as the room around me goes cold."
    "Or at least gets a little colder."

    s "..."

    play sound "knock.mp3"

    "I knock again to no avail and, for a brief moment, feel as if my fist phases through the door."
    "Or perhaps that's just what I want it to do."
    "It would save me the effort of having to barge in a second time under premature pretenses- something that Rin wasn't exactly very happy about last time."
    "In all fairness, though...right now, she doesn't seem happy about much of anything."

    s "This is your last chance to answer the door, Rin."
    s "I'm going to come in if you don't open up for me."

    "..."
    "I jiggle the handle to make sure the door is unlocked and, thankfully, it is."
    "I worry that I might be disturbing her after her long bout with sleep deprivation finally came to an end, but I decide that it's more important right now to make sure she's breathing."
    "It's a morbid thought, but one I force myself to have as it will lessen the impact if she actually isn't."

    scene black
    with dissolve
    play sound "knock.mp3"

    "I knock one last time."
    "I pause."

    play sound "dooropen.mp3"
    scene black
    with dissolve

    "I turn the handle."
    "………"
    "……"
    "…"

    play music "lastdailysong.mp3"
    scene rinisfine1
    with dissolve2

    "Rin sits alone on her bed without acknowledging my existence."
    "The faint glow of her computer screen illuminates her pale skin as-"

    s "Rin?..."
    r "…"

    "As blood oozes from between her fingers and drips onto her leg."
    "I feel an obvious compulsion to approach her, but...what would I even do if I could get her to respond?"
    "What is the proper way to handle something like this? And how can I be so aware yet so lost at the same time?"

    s "Haruka...is worried about you, you know."
    r "…"
    s "…"

    "Again, nothing."
    "I grasp at the longest straw I can think of, hoping that it will be strong enough for me to pull the two of us to shore before we drown in this darkness."

    s "I saw Chika on the way over here."
    s "Did you know she's been looking for you?"
    r "…"
    s "…"

    "I see that lying won't help either."
    "My eyes focus once more on her arm, worrying about the state of the lacerations concealed beneath the same hand she'd used to make them."
    "It's funny, but it isn't- how what destroys can so quickly regret and rebuild."
    "And it hurts, but it doesn't- bathed in the light of static and watching in awe as what is beautiful breaks before me."

    scene rinisfine2
    with fade

    r "…"
    s "Hey...Rin. What's going on?"
    r "…"
    s "I'm...not really sure if this is just me exaggerating or not, but do you need to go to the hospital? Can you show me your arm?"
    r "…"

    "How am I supposed to get through to her if she doesn't even know I'm here?..."
    "I move closer and crouch down, expecting that she might look bigger when towering over me."
    "I'm wrong."
    "Her eyes are more swollen than they were the last time I saw her. And while the trace of tears is present in her eyes, none of them fall."
    "They cling to her eyelids like her fist clings to her wounds, never fully accepting why she is where she is or how she wound up there."
    "But, on the bright side, the air conditioner is turned on full-blast...so at least she’s not drenched in sweat anymore."

    s "Rin, talk to me."
    s "I came all the way here to see you. It's only polite if you at least say...hi or something."
    r "…"
    s "Do you...want to watch a movie? Or...listen to music? I can go get your laptop."
    r "…"

    "I’m clearly horrible at this."
    "I have no idea what to do to help her or...if she even needs help in the first place."
    "And I know that might sound like a horrible thing to say when someone is physically wounded, but...this doesn't look life threatening. She could very well have things under control."
    "{b}I just need her to speak and confirm that.{/b}"

    s "..."

    "Out of ideas, I reach out and poke her leg, hoping that a physical sensation will be enough to drag her back to reality."

    s "Rin. Snap out of it. I'm here."

    scene rinisfine4
    with dissolve2

    r "...Huh?"
    r "Sensei?"
    r "What are you doing here?"
    s "Wondering why you're just sitting here in the dark with blood dripping down your arm."
    r "..."
    s "Rin, where is Futaba? You shouldn’t be alone right now."
    r "Alone?..."
    r "But...you’re here..."
    r "I’m not alone at all..."

    "I sigh to myself and try and think up some solution, but wind up right where I started- the crossroads between not knowing anything and having seen too much."

    s "Do you want to talk?"
    r "...Talk?"
    r "About what?..."
    r "Did we have plans to hang out tonight?..."
    r "Sorry, but I don’t feel very good right now...I think we’ll...have to postpone..."
    s "I’m not going anywhere. I’m worried about you."
    r "You’re...always worried about me..."
    r "Why?"
    r "The worst is already over..."
    r "Now, I’m just sitting here..."
    s "I know. But I want to sit here with you."
    r "Pervert..."
    r "I’m not wearing any pants right now...of course you want to sit with me..."
    r "If I didn’t know any better...I’d think you were here with...ulterior motives..."
    s "I don't have any {i}ulterior motives.{/i} I just want to help you."

    "Even I know better than to do something like that in the state she’s in."
    "I feel like even saying the wrong thing could cause her to shut down right now."

    r "Everybody always wants to help...how come no one ever does?"
    r "Do you know, Sensei?...Why everything hurts so much?"
    s "That's not something anyone knows. It's just the way things are, unfortunately."

    scene rinisfine5
    with dissolve

    r "Yeah..."
    r "The way things are..."
    r "You know...you’re a good guy, Sensei..."
    r "Futaba gave me the letter you wrote for me..."
    r "It was really nice...Even if it was only three sentences long..."
    s "Not nice enough, apparently. I was hoping it might help you snap out of this."
    r "Snap me out of what?"
    r "{i}This{/i} is who I am."
    r "{i}This{/i} is the real me."
    r "Some days, I’m happy. Some days, I’m sad."
    s "The way you’re acting is a lot more than just {i}sad,{/i} Rin..."
    r "Then I guess it's something else..."
    r "Maybe I'm just tired?"
    s "When was the last time you got any sleep?"

    scene rinisfine6
    with dissolve

    r "Uhhhhhh..."
    r "I don't know. Rain check."
    s "Rin, come on. I can't imagine staying up is doing your...mental state any favors?"

    scene rinisfine5
    with dissolve

    r "My mental state?..."
    r "Is there something wrong with me, Sensei?..."
    r "Think carefully...before you answer..."
    s "Fun fact, telling me to think carefully before answering something just makes me not want to answer it."
    r "Oh no...But the suspense is killing me..."

    "I place my right hand on Rin's thigh with the desire to wipe away some of the blood, but I hesitate right before I come into contact with it."

    scene rinisfine6
    with dissolve

    r "Right now?...You really are a pervert, Sensei..."
    s "That's not what I'm doing, Rin. I'm just trying to...comfort you in one of the only ways I know how."
    r "Oh well...you can {i}comfort{/i} me however you like..."
    r "Just please leave my underwear on..."
    s "I was planning on it..."

    scene rinisfine7
    with dissolve

    "Rin closes her eyes."
    "Frankly, I’m hoping she falls asleep right now because at least that would be {i}one{/i} problem out of the way."
    "But no matter how long I stroke her leg for, she sits straight up...never once succumbing to the darkness contained behind her eyelids."

    scene rinisfine4
    with dissolve

    r "Hey, Sensei..."
    s "Yes?"
    r "Where do you think we go when we die?..."
    s "Is now really the best time to be asking that?"
    r "I'm just wondering...you don't have to answer..."
    r "It's just that...no one seems to agree on what happens...and I want to know what you think..."
    s "I don't know, Rin."
    r "You don't believe in Heaven?"
    s "Heaven? No. But...I guess that going somewhere else after you do is just as plausible as any of the other alternatives."
    r "Somewhere else?"
    r "But where?..."
    s "I don’t know. A different place? A different body?"
    s "Just...somewhere else."

    scene rinisfine5
    with dissolve

    r "A different body?"
    r "That sounds kind of nice."

    if bonus == True:
        s "Your body is perfectly fine, Rin."
        r "You really think so?"

        scene rinisfine8
        with dissolve

        r "Well, then what about these? Cause I, for one, don't think I'd mind if they got a little bit bigger."
        s "..."

        scene rinisfine9
        with dissolve

        r "What's wrong? You've already seen them once before. That should be enough to form an opinion, right?"
        s "Rin..."

        scene rinisfine9r
        with dissolve

        r "You know who has really nice boobs, Sensei? {i}Chika.{/i}"
        r "Sometimes, when the two of us are in the shower, it takes every ounce of self control I have to not just...reach over and grab them, you know?"
        s "..."

        scene rinisfine10
        with dissolve

        r "Are you having a hard time focusing with my tits out, Sensei?"
        r "I'll let you touch them if you promise to be gentle..."
        s "Rin, now really isn't the time to-"
        r "It’s probably hard to control yourself right now, isn't it?"
        r "Want to help me see if I can {i}feel?...{/i}"
        s "Not tonight...And definitely not until we do something about your arm..."

        scene rinisfine11
        with dissolve

        r "Oh, come on...it's not even that bad this time..."
        s "This time?"
        r "What, you think this is the first time I've ever done something like this?"
        r "Use your brain, Sensei. You didn't think my doctor's appointment the other day was for a {i}doctor{/i}-doctor, did you?"
        r "Were you worried that I was some kind of tragically ill heroine?...One who you'd inevitably grow closer to before my sickness came to claim me?"

        scene rinisfine12
        with dissolve

        r "Unfortunately for both of us, my {i}sickness{/i} already claimed me a long, long time ago..."
        r "Now, I'm just a fucked up mess of imbalanced chemicals- held together by thick wristbands, cover-up, and an overly-active sexual imagination."
        s "Does Futaba know?"
        r "About my overly-active sexual imagination? Yeah."
        s "About your cutting..."

        scene rinisfine13
        with dissolve

        r "Ahh."
        r "Not this time. But she knows it's happened before."
        r "Guess that makes three people now...You, Futaba, and the doctor."
        s "And what did the doctor say? Shouldn't they have done something to, like...prevent this? You just saw them the other day."
        r "The doctor said the same thing anyone else would...To just...not do it anymore."
        r "Like it's that simple."
        s "That’s it?"

        "Rin shakes her head in place of saying no."

        r "She gave me a few medications that are supposed to start helping me feel {i}better,{/i} but..."
        s "But what?"

        scene rinisfine14
        with dissolve

        r "But I don't like them."
        r "They make me feel all...fake and stuff..."
        r "Like it's somebody else's mind inside of mine..."
        s "…"

        scene rinisfine12
        with dissolve

        r "Oh. I guess I should probably pull my shirt down, huh?"
        s "...Yeah. That would probably be for the best..."

        scene rinisfine14r
        with dissolve
    else:
        scene black
        with dissolve

        r "Hey...why are you closing your eyes?"
        s "I had a feeling something inappropriate was about to happen."
        r "Heheh...you're funny."

        "Some stuff happens and it is ultimately revealed that Rin might have some issues that will be hard to address to the Patreon friendly copy of Lessons in Love."

    "Rin fixes her clothing and breathes a sigh that makes me feel like this is just one of many other times something like this has happened."
    "It's that sigh that makes what she says next so much harder to believe."

    r "Everything will be okay."
    r "I promise."
    s "I’m not sure if I believe that promise."
    r "When have I ever lied to you?"
    s "Well, you’ve lied about being okay probably ten times now."

    scene rinisfine14r2
    with dissolve

    r "Shit. You're right."
    r "Maybe I'm just fucked then?"
    s "Rin, come on."
    r "But really...I’ll try my best to not do stuff like this anymore..."
    s "And those aren't just empty words?"
    r "Sensei..."
    r "{i}Everything I said to you{/i} tonight was empty words."
    r "Why do you think I do this?...Because I like the colors?..."
    s "I don't-"
    r "I'm trying to bring the feelings back. I'm trying to shock myself back to the good Rin. The fun Rin."
    r "Because everything {i}this{/i} Rin has to say?...It's all completely empty."
    r "But I know you care...that still gets through."
    r "So I can tell you I will try..."
    r "But I never should have made it a promise."
    r "Thank you for catching me."
    s "If you can't promise me that...can you at least promise me something else?"
    r "I guess that depends on what you want..."
    s "What I want is for you to come to me first next time. Even if I can't help you, I want to at least try."
    s "And if you can't come to me, at least go to Futaba."

    scene rinisfine15
    with dissolve

    r "Futaba doesn't like blood."
    r "I also wouldn't want to bother her with something like this...not when she has her own stuff going on."
    s "Then come to me."

    scene rinisfine14r2
    with dissolve

    r "I'll do my best."
    s "Oh, and one more thing."
    r "You've sure got a lot of demands for someone who's supposed to be comforting me."
    s "This last promise is easy. I swear."
    r "Just tell me what it is."
    s "Sure. Then-"
    s "Get some fucking sleep."

    scene rinisfine16
    with dissolve

    r "Heh...heheheh..."
    r "I know you said it would be something easy, but...I wasn't expecting your final demand to be as simple as that..."
    s "Is your arm going to be okay? Makoto probably has a first aid kit that I can borrow if-"

    scene rinisfine14r
    with dissolve

    r "That won't be necessary...I normally just let everything close up while I sleep..."
    r "Thankfully, I think I should actually be able to now. I always get a little woozy after this kinda thing."
    s "So..."
    s "Wait. All that time you've been spending awake, unable to get to sleep-"

    scene rinisfine14r2
    with dissolve

    r "Could have been solved by just doing this earlier. I know."
    s "That's not what I mean."
    r "I know. It's probably hard to tell with my voice being the way it is right now, but I was joking."
    r "I hold back as long as I can."
    r "I really do."

    scene rinisfine16r
    with dissolve2

    r "It's just {i}really{/i} fucking hard, Sensei."
    s "I'm sure it is..."
    r "Thank you for worrying about me...Really...It means a lot..."
    r "But...if you don't mind-"
    s "I'll let you go to sleep. Don't worry."
    r "You don't...have to leave just yet, you know?"
    r "You can stick around as long as you want."
    r "Futaba is sleeping at her friend’s house again tonight, so she won’t be coming home."
    r "I just...I'm going to pass out...and I think I could sleep a little easier with you by my side."
    s "That's all you needed to say."
    s "I’ll wait right here until you fall asleep."

    scene rinisfine17
    with dissolve

    r "Okay..."
    r "I'm sorry for worrying you. I really am..."
    r "Goodnight, Sensei..."
    s "Of course."
    s "Goodnight, Rin."

    scene black
    with dissolve2

    "Rin falls asleep right away, but I stay in the room for another hour or so just to make sure she doesn’t wake back up."
    "I use the sleeve of my blazer to dry the blood off of her arm and her thigh."

    stop music

    "It feels strangely familiar."

    stop music fadeout 5.0
    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm20 = True

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    scene bedroom_night
    with dissolve

    "I immediately go to sleep when I get home. "
    "I hope tomorrow is a better day."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

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
    else:
        jump advancetomon

label futabadorm25:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == False:
        jump rindorm15
    if rin_love >= 20 and cafe20 == True and day50 == True and rindorm20 == False:
        jump rindorm20
...
```