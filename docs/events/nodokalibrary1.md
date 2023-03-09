# Cracks in the Armor
Nodoka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nodokalibrary1&go=Go)



## Event preconditions
✅Nodoka love greater than or equal to 0

✅Event "[Otoha: Conversations Outside of a Girls’ Dorm](./otohadorm1.md)" is completed (event=otohadorm1)



## Next events
* [Nodoka: Coloring Book](./nodokalibrary5.md)

## Event properties
* ID: nodokalibrary1
* Group: Nodoka
* Triggered by label: nodokalibrary
* Triggered by branch label: saturdayafternoon

## Event code
File: \game\NodokaEvents.rpy
Code:
```python
...
label nodokalibrary1:
    scene nodokafirstlib1
    with fade
    play music "morningmoon.mp3"

    "I make my way to the library a bit later than I normally do and am immediately greeted by a rare sight."
    "Sleeping on the job, Futaba? Really?"
    "What if someone needs a book?"
    "The world will spiral into chaos if you’re not there to check library cards and type names into your outdated computer."
    "I take my phone out of my pocket and begin to file a formal complaint to the[school] when I hear a familiar voice call out to me."

    no "Beautiful, isn’t she?..."

    scene nodokafirstlib2
    with fade

    no "A wild Fukuyama, at rest in her natural habitat...entirely unaware that she is being studied by two of the most practiced researchers in all of Kumon-mi."
    s "Indeed. Let us watch her closely and use this opportunity to educate future generations about her mannerisms and...tendencies or something."
    s "I don’t know. Just throw some smart person lingo into the mix and assume I said that."

    if bonus == True:
        no "Educate future generations? Sensei, are you forgetting that we are here on a mission to discover the mating process of the wild Fukuyama?"
        s "Uhh, yes. I was definitely forgetting that."

        scene nodokafirstlib3
        with dissolve

        no "Look at you, slacking off on our first day in the wilderness. Can you not tell when a creature is in heat simply by looking at them?"
        s "She just looks tired to me. But I’ll keep that in mind for when she wakes up. Have your camera ready."
        no "My camera is always ready, good sir. "
        no "In fact, why bother waiting at all? The Fukuyama is known for its love of copulating with fully-grown human males."
        s "Is there...a secret side of Futaba that I am unaware of?"
        no "Does the thought of her stripping down to her birthday suit and prancing around Kumon-mi in search of the ultimate satisfaction disturb you?"
        s "Yes."
    else:
        no "Just look at the way she breathes. Using both of her lungs. How majestic."
        s "You know, some of the things you say really disturb me sometimes."
        no "I'm going to wear someone else's skin one day."
        s "This is exactly what I'm talking about."

    scene nodokafirstlib4
    with dissolve

    no "Hmm...Yes. Yes, that disturbs me as well."
    no "Return to the Jeep and grab the net. We shall capture this one and keep it as our personal specimen. "
    no "Everyone wins."
    s "I just came from the Jeep and...I’m sorry to say, but it appears that we’ve forgotten our net, Nodoka."
    no "Well that’s no good at all. Without a net, we won’t be able to move into the second phase of any of our seven different strategies, Sensei. That net was extremely important."
    no "Luckily, the Fukuyama is a predictable creature and can be found in this exact location every single weekend."
    no "So I suppose more opportunities will arise as long as we remain vigilant."

    scene nodokafirstlib5
    with dissolve

    no "Now, what would you like to discuss with our daily quota of research out of the way?"
    s "Anything, really. "
    s "I remember you mentioning that you’ll be spending some time here from now on, so...here I am, I guess."
    no "Did you miss me?"
    s "So much that I took up a job as a wildlife researcher just to get closer to you."
    no "But you are my teacher...and I am your student. Think of how immoral this is, Sensei."

    if bonus == True:
        no "Nevermind how primally satisfying it would be to pin me down and take me on the desk of the teacher’s lounge."
        s "The teacher’s lounge actually doesn’t have any desks. It’s just couches."
        no "How unfortunate. I’ve always wanted to be taken on a[school] desk."
        s "If only we knew where to find any of those..."
    else:
        s "You are right. I apologize if it appeared that I was insinuating anything unsavory."
        s "If only we could forget all of that and remain good buddies for the rest of eternity."

    scene nodokafirstlib6
    with dissolve

    no "Yes...if only."

    "Nodoka places her book down on the desk and I try to sneak a peek at whatever it is she’s been reading."

    if bonus == True:
        "I stop caring when I realize it isn’t anything pornographic. But I guess the chances are that she pulled whatever it was from one of the bookshelves here and..."
        "Well, I don’t think this[school] carries much porn."
        "I wonder if there is anything I can do that could change that?"
    else:
        "All of the pages are blank, though, and I quickly go back to thinking she's a big ole weirdo."

    no "Are you thinking what I’m thinking, Sensei?"

    if bonus == True:
        s "You know, I really wouldn’t be surprised if I was."
    else:
        s "I highly doubt it."

    scene nodokafirstlib7
    with dissolve

    no "Excellent. Then let us pick up where we left off before you ran away without saying goodbye the other night."

    "Oh. I guess we weren’t thinking the same thing after all."

    no "I believe I owe you an apology for making you feel uncomfortable. "
    no "I got a little ahead of myself."

    if bonus == True:
        no "I’d like to say it won’t happen again, but saying that would make me a liar. And you seem to be the type to value honesty."
        no "When it’s given to you, I mean. Not when you need to dish it out to others."
        s "That is surprisingly perceptive."
        s "But yes, there’s not really any point in lying to me. "
        no "But there {i}was{/i} a point in lying to me about your...pure intentions. Was there not?"
        no "Why do you think I began to grill you so vigorously about the things you wanted to do to me within earshot of the others?"
        s "Because you’re weird and horny?"
    else:
        no "I just forgot how important top 8's are to some people."
        s "Just stop being such a weenie and it won't be a problem."

    scene nodokafirstlib8
    with dissolve

    no "Wrong!"

    if bonus == True:
        no "I’m weird and horny {i}and{/i} a good girl who just wants to protect all of her companions."
        s "Do you really think I’m leading any of them on or something?"
    else:
        no "Being a weenie is fun. I will be a weenie forever."
        s "Besides, I don't think any of the girls think I would omit them from my top 8."

    scene nodokafirstlib9
    with dissolve

    no "I {i}think{/i} that a particular creature the two of us were sent here to study thinks that. And so I, too, must think that by association."
    s "…"

    if futabalust10 == True:
        "Futaba did mention thinking something was going on between Chika and me at the Christmas party but...I’m pretty sure she’s not equating it to me leading her on, is she?"
        "She just realizes that there are a lot of people who happen to be into me the same way she is."
        "And she didn’t even seem that opposed to it when she told me..."

    else:
        "Would Futaba really think something like that?..."

        if bonus == True:
            "I mean, it would probably make sense if she did given how quickly things progressed between the two of us. "
            "She’s a smart girl...so I get why she would feel that way."
            "But to think those feelings were so apparent that even Nodoka would pick up on them..."

    no "You’re manipulating Futaba, aren’t you?"
    s "It’s a little confusing seeing you ask that question with a smirk on your face."
    no "Apologies. I have a natural smirk. I’m actually very upset with you if that’s what you're doing."
    no "I’m not telling you to drop everything you’re doing and devote yourself to her. She’s mine of course."
    no "But she should at least know that she isn’t the only one you’re seeing."

    if futabalust10 == True:
        if bonus == True:
            s "I think she already {i}does{/i} know that, to tell you the truth."
            s "She voiced her concerns about how one of the girls was acting around me during our Christmas party."
            no "Which one? The tiny, black haired one in the back of the classroom?"
            s "...Sana?"
            s "Why would you assume I was talking about Sana?"
            no "Because that would be the most exciting answer, obviously. "
            no "I mean, think about the size difference."
            s "That’s definitely not the person Futaba was talking about."
            s "But the point is that she’s perceptive enough to...understand the situation at hand here."
            no "So then why get mad at {i}me{/i} for asking what that situation was? "
            no "All you had to do was come out and say, “I’m here to have sex with Nodoka and everyone else and there’s nothing anyone can do to stop me.”"
        else:
            s "I can hug whoever I want and you will never stop me."
            no "Then you need to come out and admit you are a huggy boy so we can all stop pretending you aren't."

    else:
        if bonus == True:
            s "Why does she need to know that?"
            no "Because she deals with enough bullshit from people commenting on her weight and demeanor."
            no "I don’t want her to be slowly crushed by assuming the man she’s yearning for is only using her for her supple, youthful body."
            s "Not to turn the tables or anything, but why flirt with me so openly if you’re worried about her being hurt?"
            no "Obviously because {i}I’m{/i} in heat as well. "
            no "And when push comes to shove and I am forced to choose, I will obviously take care of myself before anyone else."
            no "But that doesn’t mean I will simply abandon her in the springtime of her youth."
            no "This could have all been solved so easily by simply coming out and saying, “I’m here to have sex with Nodoka and everyone else and there’s nothing anyone can do to stop me.” the other night."
        else:
            s "I can hug whoever I want and you will never stop me."
            no "Then you need to come out and admit you are a huggy boy so we can all stop pretending you aren't."

    s "Yeah, that’s definitely not something that I think I’m ready to say yet."
    no "It’s true, though. Isn’t it?"
    s "Nodoka, as someone who appreciates girls as much as I do, I’m sure you understand."
    no "Absolutely. There is not a body in that classroom that I don’t want all up in my business."

    if bonus == True:
        no "But I’m not pushing all of them into different rooms and asking that they keep their schedules open while I take turns individually dishing out orgasms."
    else:
        no "But, unlike you, everyone already knows I am a huggy boy."

    s "Nodoka-"

    scene nodokafirstlib10
    with dissolve

    no "I’m not going to say anything. "
    no "Frankly, I only care about two people out of seventeen right now after excluding myself from the count."
    s "Two? Weren’t you starting to get close to Rin, though?"
    no "Her company is fun and she is a nice girl. But that doesn’t mean I care enough about her to prioritize her in any way."
    no "I make people work to get on my good side. That way, they’re less inclined to abandon me and leave me with nothing."
    s "I feel like {i}I{/i} didn’t have to work very hard to get on your good side."

    scene nodokafirstlib11
    with dissolve

    no "You think you’re on my good side?"
    s "I do."
    no "What gives you that idea?"
    s "The fact that you’re slowly but surely showing me some cracks in your armor."
    no "Cracks are just cracks, Sensei. They’re not really weak points until you bash or stab them a few more times."

    if bonus == True:
        no "If you really want to get my armor off, all you need to do is save up enough Nodoka points."
        no "Unfortunately, you missed out on a large sum of them by not eating my pizza the other night."
        s "I’m pretty sure it wasn’t, but I’m going to interpret “eating my pizza” as a euphemism. "
        no "Do it. That makes the idea of the four girls who remained upstairs eating pizza all night significantly more exciting."
    else:
        no "Also, you missed out on a fuckin' good ass pizza the other night."
        s "Ugh I knew it."

    scene nodokafirstlib12
    with dissolve

    no "And say goodbye for real next time. Making me have to wait to apologize was a real cliffhanger."
    s "I figured someone as well-read as you would {i}like{/i} cliffhangers."
    no "Not when they involve me."

    scene nodokafirstlib13
    with dissolve

    no "Which is why I’m taking countermeasures to prevent that from ever happening again."
    s "Countermeasures? What are you talking about?"

    scene nodokafirstlib14
    with dissolve

    no "Take down my number and let me bother you whenever I want to procrastinate or apologize for more things I’m going to do in the future."
    s "Just how difficult are you planning on making my life?"

    if bonus == True:
        no "As difficult as I can make it without entering into a formal relationship with you."
        s "Wow. Are you rejecting me before I’ve even asked you out?"
        no "A - You will never ask me out without some serious character development on your end."
        no "B - I have to keep myself open for when Futaba becomes a lesbian."
        no "It’s unfair that you get to play with her breasts recreationally and I have to do it by force."
        s "I want to say you should probably stop doing that, but I enjoy the mental image of it, so feel free to continue."
        no "I will do just that."
        no "Oh, and Sensei?"
        s "Hm? "
        no "You {i}are{/i} on my good side."
        no "My distaste for cliffhangers compelled me to let you know that before you wander off to flirt with someone else."
        s "Funny story, I’m about to do that right now."
        s "I’ll be thinking of you the entire way there, though."
        no "And I’ll be watching you very closely as you walk away. "
        no "You have an excellent figure for someone your age. "
        s "I’m not even that old..."
    else:
        no "On a scale of one to ten? Probably like an eight."

    scene black
    with dissolve2

    "I quickly exchange numbers with Nodoka and slide my phone back into my pocket."

    if bonus == True:
        "As I leave the library, I feel the looming gaze of a perverted, semi-sociopath on my back."
        "Just seconds after turning the corner, a noise leaks out of my pocket and the relationship I have with Nodoka grows even stranger."

        play sound "phonebeep.wav"

        "{i}Nodoka has sent you a picture message!{/i}"

    $ renpy.end_replay()
    $ nodokanumber = True
    $ nodoka_love += 1
    $ nodokalibrary1 = True
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label nodokalibrary5:
...
```

## Code that triggers this event
File: \game\NodokaEvents.rpy
Code:
```python
...
label nodokalibrary:
    if nodokablock == True:
        "I don't really think I want to see Nodoka right now..."
        jump satafternoonmenu
    if nodoka_love >= 0 and otohadorm1 == True and nodokalibrary1 == False:
        jump nodokalibrary1
...
```