# Like Noodles in the Wind
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen25&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 25

✅Event "[Main: All is Bright. All is Beautiful.](./secondbeach18.md)" is completed (event=secondbeach18)



## Next events
None

## Event properties
* ID: ramen25
* Group: Tsuneyo
* Triggered by label: ramenshop
* Triggered by branch label: ramenshop

## Event code
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramen25:
    scene tsuneyogreenonion1
    with fade
    play music "kashiwagi.mp3"

    t "Sigh."
    s "You’re not supposed to {i}say{/i} “sigh,” Tsuneyo. You’re supposed to just...actually do it."
    t "Sensei, when you look at this knife...what do you see?"
    s "A knife."
    t "Look closer."
    s "…"

    scene tsuneyogreenonion2
    with dissolve

    s "It’s still a knife."
    t "Precisely."

    scene tsuneyogreenonion3
    with dissolve

    s "What?"
    t "Sometimes, what you see is what you get."
    t "And other times, you get a knife."
    s "Tsuneyo, what the fuck are you talking about?"
    t "Knives, idiot. "
    t "I had a thought, but it went somewhere else."
    t "This would not be an issue if you were more entertaining."
    s "Well forgive me for coming all the way across town in the cold to spend time with you."
    t "I can not forgive you. But I can make you a bowl of delicious soup that will warm both your heart and your soul."

    "As you can see, I decided to spend the night hanging out at Tojo Ramen with Tsuneyo. "
    "And despite the way she’s slowly waving a knife around, it’s clear that she is happy to see me."
    "Well, “happy” is probably a bit of an exaggeration."
    "But she was just standing around before I got here and is now capable of doing her job- the one thing in life she appears to be confident in."

    s "Just make me whatever you feel like making. I don’t care."
    t "I don’t feel like making anything. Are you okay with starving?"
    s "{i}You{/i} don’t feel like getting...closer to noodles or whatever?"

    scene tsuneyogreenonion4
    with dissolve

    t "I will not be told to get closer to Noodles by the one man who stays as far away from him as possible."
    s "Not bird-noodles. Noodles-noodles. "
    s "It’s unlike you to not want to cook."

    scene tsuneyogreenonion5
    with dissolve

    t "As a wise man once said...even the best fall down sometimes."
    s "That wasn’t a wise man. That’s the chorus from Howie Day’s 2003 hit single, “Collide.”"
    t "And what a wise man he was."
    t "But who said it does not matter even half as much as {i}what{/i} was said, Sensei."
    t "I’m afraid that I am just lacking the same motivation and excitement that you would normally come to expect from a lively, energetic girl like myself."
    s "Yes. Because when I think of Tsuneyo Tojo, I immediately think “lively.”"
    t "If only I could be more like this knife."
    s "I know there’s a metaphor in there somewhere, but I’d appreciate it if you could just tell me what it is so I don’t have to use my brain."
    t "Sharp. And made of steel. This is the me who never was. The me who is not."
    s "If this is another comedy routine, I'm going to go ahead and do you a favor by asking you to scrap it. "

    scene tsuneyogreenonion6
    with dissolve

    t "Gone...like noodles in the wind. Flying about and causing destruction everywhere they roam."
    t "This is the Tsuneyo Tojo you see before you. A shell of her former crab."
    s "What the hell happened to you overnight?"

    scene tsuneyogreenonion7
    with dissolve

    t "Is this what they call “depression?” Should I see a doctor?"
    s "I highly doubt that. Why don’t you just tell me what’s going on?"
    s "I can’t guarantee that I can help or anything but, sometimes, talking about stuff is all you need to feel a little better."
    s "Also, if I’m on better terms with you, you won’t feel the urge to stab me with that knife you’re still waving around."
    t "How did you know about that urge? Did I mention it out loud in the heat of my sadness?"

    "You know, maybe I should call it an early night and head back home before Ami needs to identify my body at the local morgue?"

    s "Just tell me what’s wrong. That’s the least you can do to make up for not serving me while you’re still open."
    s "It’s either that or I leave you a bad Yelp review."

    scene tsuneyogreenonion8
    with dissolve

    t "Don’t you dare! Everyone knows that a restaurant’s success is entirely dependent on the thoughts of various inexperienced consumers who went through the effort of actually creating a Yelp account!"
    t "I shall turn {i}you{/i} into ramen, you bastard!"
    s "Okay. On that note, I’m just going to-"

    scene tsuneyogreenonion1
    with dissolve

    t "Fine. I will talk."
    t "But it is very sad. Please do not cry when you hear how horrible things are."
    s "I’m sure that I’ve heard worse than whatever it is you’re going through."
    t "Sigh."
    s "…"
    t "Sensei..."
    t "It appears that the restaurant is out of green onions."
    t "Not to be mistaken with the Green Onion of the second floor. She has not yet come to this restaurant."
    s "And...that’s why you’re giving up on everything?"
    t "One item being out of stock is a symbol of my failure as the acting manager of this business."
    t "First, it is the green onions. Then, it is chopsticks."
    t "Then, next thing I know, everyone has to grab their noodles with their fingers and eat them the way birds eat worms."
    s "Sure. Except birds don’t have fingers and use their beaks to eat."

    scene tsuneyogreenonion8
    with dissolve

    t "Oh, so {i}now{/i} you care about what birds do? How dare you?"
    s "Is that really all that’s bothering you? Running out of one thing?"

    scene tsuneyogreenonion1
    with dissolve

    t "I was prepared to adapt to the situation at first..."
    t "But as the hours went by and no customers entered the store, I realized that my failure must have already spread throughout the city."
    t "I’m afraid it is too late for me now."
    s "No one’s come in all day?"

    scene tsuneyogreenonion3
    with dissolve

    t "If they have, they are either invisible or extremely sneaky. And not hungry."
    t "We have experienced slow days in the past, but never anything like this."
    t "Though, I am prepared to experience happiness once more if you offset the lack of profit by purchasing everything on the menu."
    s "You know...I {i}would{/i}, but I was kind of hoping for something with green onions."

    scene tsuneyogreenonion9
    with dissolve

    t "Of course. Another reminder of my inadequacy makes itself known before the doors are closed for the night."
    t "Tojo Ramen is no more. This is the end."
    s "Oh, stop being dramatic."

    scene tsuneyogreenonion10
    with dissolve

    t "Dramatic?! Me?! The world is crashing down right now and you have the audacity to demand such a thing?!"
    t "Where do you get off?!"
    s "Jesus. There’s no need to yell."

    scene tsuneyogreenonion3
    with dissolve

    t "I apologize. I was attempting to show the difference between true drama and what you had labeled as drama, but my acting skills were so good that you must have gotten scared."
    s "Tsuneyo, you do realize there is a very easy way to solve your problem of not having onions, right?"
    s "I’m sure customers won’t magically appear again once you obtain them, but it’s not like they are out of reach forever."
    t "Not forever. But we do not receive our next shipment of produce until two days from now."

    if bonus == True:
        t "It is highly probable that I will have to sell my body to make up for the loss in profit we face during this time."
    else:
        t "It is highly probable that I will have to sell my holographic Charizard one of these days."

    s "There’s no way you’re losing that- wait."
    t "For what? Why am I waiting?"
    s "Just out of curiosity..."
    s "How much would you be selling it for?"

    if bonus == True:
        t "I am not sure. I do not even know what the process of selling one’s body entails. I just know that it is meant to generate a great amount of revenue. "
        s "Oh. Well, uhh...that’s probably not an alternative you’ll have to worry about. Especially with this incredibly smart proposition I am about to...propose."
        t "If you are attempting to purchase me, I will give you a 5%% discount. "
    else:
        t "Six trillion dollars. But I will give you a 5%% discount."

    s "A: Don’t even bother offering discounts that small. And B: Let’s go get you more green onions."
    t "Impossible. Produce delivery day is still 48 hours off. You are out of line, sir."
    s "I’m telling you that you don’t have to wait. You can just go to the convenience store and buy enough to hold you over for a day or two."
    s "Aren’t you supposed to be amazing at this? I’m surprised you didn’t think of that."

    scene tsuneyogreenonion11
    with dissolve

    t "It did not even occur to me."
    t "I finally understand where the word {i}convenience{/i} in “convenience store” comes from. "
    t "They are able to operate outside the jurisdiction of the Produce Delivery Administration. "
    s "Yup. That’s exactly why they are called that."
    s "The only issue is that you’ll have to close the store while you’re out so people don’t wind up coming in and robbing the place."

    scene tsuneyogreenonion1
    with dissolve

    t "That is a fair price to pay. It is not as if anyone will enter the restaurant when it already reeks of failure to begin with."
    t "Now, we just need to locate one of the stores."
    s "There’s one that Noriko works at not far from here. We can just go there."

    scene tsuneyogreenonion11
    with dissolve

    t "Another convenience. Things are already beginning to turn around."
    t "Please give me a moment to check with my father and see if such a task is allowed."
    s "Do you really need permission? Aren’t you in charge of the place while he’s...sick?"

    scene tsuneyogreenonion3
    with dissolve

    t "I am also worried that this may be a trap and that you are going to kidnap me and throw me into traffic."
    s "That’s not what human trafficking means, Tsuneyo. "
    t "That may just be what you want me to think."
    t "I will return shortly."
    t "Please help yourself to some chopsticks while you wait."

    scene black
    with dissolve2

    s "And do...{i}what{/i} with them?..."

    "………"
    "……"
    "…"

    scene tsuneyogreenonion12
    with dissolve2

    "Tsuneyo returns downstairs several minutes later and proceeds to shut off a bunch of the equipment in the restaurant."
    "It looks like she got permission to just close entirely rather than temporarily."
    "Now that I think about it, I’m not even really sure what time Tojo Ramen stays open until."
    "But given the fact that I was their first customer of the day on account of the invisible, yet noticeable aura of Tsuneyo’s “failure,” I can’t imagine anyone else was coming tonight."
    "We make our way through the old district as a series of homeless, decrepit onlookers gaze at us with a mix of curiosity and what could only be interpreted as desperation."
    "What they’re desperate {i}for{/i}, I have no clue."
    "But I try not to think about it because..."
    "Well, it’s fucking creepy."

    t "I have never walked around this area at night before. "
    t "It is quite different than it is during the day."
    t "The people seem rather lively."

    scene tsuneyogreenonion13
    with dissolve

    s "{i}This{/i} is lively to you?"
    t "Compared to normal, I would say yes."
    t "Though these villagers likely lack both the physical and mental fortitude they possessed when they were younger, you can still sense the curiosity dwelling within them."
    s "I mean, it’s not really “sensing” it if they’re looking right at us."
    t "Where else would you ask they look instead?"
    t "It is not a crime to simply watch."
    s "That kind of depends on what you’re watching, I think."
    t "If you spend too much time looking down on how others look at you, you will miss out on many of the beautiful things life has to offer."
    t "Branches...Leaves...The wide part..."
    s "Those are all just different parts of a tree. I’m sure there is more in life that you think is beautiful."

    scene tsuneyogreenonion14
    with dissolve

    t "Of course."
    t "Those are just the first things that came to mind."
    t "My father has always kept trees close to his heart, so I assume I inherited that love from him."
    t "And these people- the ones staring at us as we venture forth toward produce-"
    t "Even they are more lively than he is now."
    t "They can stand...and speak without the assistance of a machine."
    s "I knew he couldn’t walk, but...he can’t speak anymore either?"
    t "Not the way you and I can."
    t "We are special. Gifted, even."
    t "But one day, that gift will be taken away from us."
    t "And we will wish in those final moments that we had not pushed so many of life’s beauties aside."
    t "So do not look at these people with unease clouding your mind. Look at them as worse or older versions of us."
    s "You do realize that way of wording it sounds even worse than the one I used, right?"

    scene tsuneyogreenonion15
    with dissolve

    t "I would rather be acknowledged as a worse version of someone else than not acknowledged at all."
    t "Meet with your fears and learn that they are nothing worth fearing at all."
    t "Do not avert your gaze. For they will stop existing the moment you wish them to."
    t "Keep them alive. Because it is possible that one day, you will be in their shoes..."
    t "Staring at a man and a woman making their way down the street- remembering when that used to be you."
    s "…"
    t "…"
    s "So, when do I get to meet your father?"
    t "I do not think you ever will."
    s "Why not? That whole speech made it sound like you really want old people to be happy for whatever reason."
    s "And, who knows? Maybe he’d like my company?"
    t "My father is a man full of pride."
    t "He does not wish to be seen in his current state."
    t "So, unless that changes, I will respect his wishes and continue to deliver quality noodle dishes to all of his loyal customers when I am not too busy failing them."
    s "Well, here’s hoping that obtaining the {i}one{/i} missing ingredient in your store is enough to magically remind everyone that you exist again."
    t "Thanks, bro."

    if bonus == True:
        t "If that does not work, I will look further into the process of body sales."
    else:
        t "If that does not work, I will look further into the selling my shiny rectangle with the final evolution of Charmander on it."

    s "Sure. As long as I’m the first person who gets a quote."
    t "You already received a quote earlier. From the wise man, Howard Daylight."
    s "Not...that kind of..."

    scene black
    with dissolve2

    s "Oh, fuck it."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen25 = True
    stop music fadeout 15.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    jump ramen25p2

label ramen25p2:
...
```

## Code that triggers this event
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramenshop:
    if tsuneyo_love >= 0 and ramen1 == False:
        jump ramen1
    if tsuneyo_love >= 5 and ramen1 == True and ramen5 == False:
        jump ramen5
    if tsuneyo_love >= 10 and ramen5 == True and tsuneyodorm5 == True and ramen10 == False:
        jump ramen10
    if tsuneyo_love >= 15 and christmas7 == True and ramen15 == False:
        jump ramen15
    if tsuneyo_love >= 20 and tsuneyodorm20 == True and ramen20 == False:
        jump ramen20
    if tsuneyo_love >= 25 and secondbeach18 == True and ramen25 == False:
        jump ramen25
...
```