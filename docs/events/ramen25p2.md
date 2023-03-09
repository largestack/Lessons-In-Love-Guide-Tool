# Green Onions and Contraceptives
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen25p2&go=Go)


Part of event chain [Like Noodles in the Wind](./ramen25.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Tsuneyo: Things Like Stairs](./ramen30.md)

## Event properties
* ID: ramen25p2
* Group: Tsuneyo
* Triggered by label: ramen25

## Event code
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramen25p2:
    "After a fair bit of walking, Tsuneyo and I finally make it to the convenience store."
    "I try not to think about it often since the place as a whole still makes me feel strange, but the second half of town is surprisingly large."
    "Not only that, but it appears to have virtually everything the better half does."
    "Just...worse versions of it."
    "And as I think that to myself, I realize that Tsuneyo’s outlook on how I should be viewing people isn’t really as bad as it sounded at first."
    "In fact, it’s probably safe to say that virtually everything out there is a better or worse version of something that already exists."
    "Which calls into question-"
    "What am I better or worse than?"

    scene screenplayonion
    with dissolve2
    play music "noriko.mp3"

    "I guess the answer to that would be everything and nothing."
    "If I do not know what I am supposed to compare myself to, there is no way I can lose."
    "But the fact that I’ve made it this far in this body, which I’m coming to learn may {i}actually{/i} belong to me, sure says something about the competition."
    "I think."
    "For all I know, the reason I’ve made it this far is because I’ve been exponentially worse."
    "But I have a suspicion that there aren’t many other versions that, at the very least, Maya has attack-hugged following the end of a wintry beach trip."
    "So...take that, other Senseis. I guess."
    "I don’t know. I’m thinking too much again."
    "Here is Noriko."

    play sound "static.mp3"
    scene norikotsuneyocon1
    with flash
    stop sound

    n "Sensei!"

    play sound "static.mp3"
    scene norikotsuneyocon2 with flash
    stop sound

    n "Sensei and Tsuneyo!"
    n "What brings you two in here so late at night?"
    t "Good evening, fellow citizen. I have come in search of onions. Green variety."

    scene norikotsuneyocon3
    with dissolve

    n "Uhh...Tsuneyo? It’s me. Noriko."
    t "I said green, damn it."

    scene norikotsuneyocon4
    with dissolve

    n "...Back corner with the rest of the produce stuff."
    t "Your assistance has been valuable to me."

    scene norikotsuneyocon5
    with fade

    if bonus == True:
        s "Sorry about that. She made a mistake that could send her restaurant spiraling into bankruptcy and leading her into a life of prostitution within the week."
        n "I don’t really think there’s a big market for prostitution right now."
        s "Why do you know? What have you been doing behind my back?"
    else:
        n "It's a shame that she'll never know I only have one year left to live."
        s "I'm sorry, what?"

    scene norikotsuneyocon6
    with dissolve

    n "Ah! Genuine concern for my well-being!"

    if bonus == True:
        n "I have waited years and years for this validation!"
        n "Rest assured, Sensei! The only person who gets to lay their hands on this body is you! "
        n "Or any girl you happen to bring into the mix who you also want to touch my body! That’s okay too!"
        n "I just want to be loved! "
        n "Violently!"
        s "That’s nice, Noriko. "
        s "I think you’re supposed to comment about why I’m here with Tsuneyo, though."
    else:
        s "Well, fucking yeah. You just told me you're going to die."
        n "I'm not. I just wanted to see what you would say."
        n "Funny joke, right?"
        s "No. That's not funny at all."
        s "Just...ask me why I'm here with Tsuneyo so we can get on with this, please."

    scene norikotsuneyocon7
    with dissolve

    n "Why? You already came here with Touka and that was like, fifty times weirder."
    n "Tojo Ramen is right down the road, yeah? I’m smart enough to put two and two together."
    s "I mean...it was down {i}several{/i} roads. But it appears that you get the gist."

    scene norikotsuneyocon8
    with dissolve

    t "I require further assistance."

    scene norikotsuneyocon9
    with dissolve

    s "Tsuneyo, what’s-"
    t "These are not onions at all."

    if bonus == False:
        t "This is candy."

    n "AHHHHHHHHH!!!!!!!!"

    play sound "thump.mp3"

    "Noriko bursts into hysterical laughter, collapses, cracks her head open on the counter, and dies."
    "Tojo Ramen goes out of business and Tsuneyo spends the rest of her life working at the convenience store instead."

    scene sky
    with fade

    "And me?"
    "Well..."
    "Let’s just say I found my own place in life."
    "I retired from teaching and started a nonprofit organization meant to help [teenage]girls in need."
    "Seven years later, I was elected the new prime minister of Japan after the borders opened back up."
    "But I still think back on those days I spent at [kumon_mi_high] sometimes."
    "And, if I listen closely-"
    "I can still hear the echoes of laughter that would ring out in the halls of the dorm."
    "Oh, what wonderful times those were."

    if bonus == True:
        n "Tsuneyo...you should probably put those back."

        scene norikotsuneyocon10
        with fade

        t "Why?"
        n "Well...for one, they aren’t onions. And that’s what you came here for. Remember?"
        t "I do not intend to purchase these. I am just curious about their purpose."
        s "They are vegetable covers."

        scene norikotsuneyocon11
        with dissolve

        t "Vegetable covers?"
        s "Yeah. You place them around longer vegetables or fruits like bananas or cucumbers and it keeps them fresh longer."
        s "They even have a coating on the outside that keeps germs away."
        t "Will they fit around a green onion?"
        s "Sure. Why not?"
        t "Then perhaps I will buy some for the walk home. Tonight is a good night."

        scene black
        with dissolve

        "Noriko snatches the condoms away from Tsuneyo and explains to her what they actually are, which disappoints me because I was curious if they really would fit a green onion or not."
        "And, of course, Tsuneyo reacted like this once she realized I lied to her..."

        scene norikotsuneyocon12
        with dissolve

        t "You have deceived me yet again. You are truly a man to be feared."
        s "I didn’t deceive you. I was just setting you up for the opportunity to be lectured on safe sex and other forms of contraceptives."
        n "Next week, we’re going to talk about birth control!"
        t "This man will be dead next week. And so will I if I do not return to the restaurant."
        s "I didn’t realize it was a matter of life and death now."
        t "Everything is a matter of life and death. Green onions...contraceptives...even the ground we walk on."

        scene norikotsuneyocon13
        with dissolve

        t "But life is stronger than death! So life will win!"
        t "And the ground will remain the ground!"
        t "Flavor will prevail!"
        n "…"
        s "…"
        n "Yaaaaaay~"

    scene norikotsuneyocon14
    with dissolve

    t "I am ready to return home now."

    if bonus == True:
        t "I feel as if my impromptu speech did not leave the impression I was hoping it would."
        s "I really don’t even understand what the point you were trying to get across was."
        t "Something about the connection between food and the desire to survive and grow."
        s "Yeah, I can’t really say that came across at all."
        t "I will continue improving my speech when I am not busy destroying my father’s legacy."
    else:
        s "Are you sure you don't want to buy the candy?"

    t "For now, it is best that we return to Tojo Ramen, where noodles reign supreme and hearts are 50%% off the third Sunday of every month."
    n "I love chicken hearts. When I was little, I used to bite into them and pretend that I was eating the heart of a baby."

    scene norikotsuneyocon15
    with dissolve

    t "Those things are not as close in size as you believe them to be, but I still invite you to dine at Tojo Ramen on the third Sunday of every month for 50%% off of strange childhood memories."
    n "Better idea! How about I come along now?"
    t "Now? "
    n "Yeah! Nobody’s come in all night, so I’m pretty sure I can close without getting in trouble."

    scene norikotsuneyocon16
    with dissolve

    t "Business has been slow here as well?"
    n "Not {i}slow{/i}. Non-existent. No clue what’s going on, but it’s been super boring."
    n "I’d much rather hang out with you two. "
    s "You’re sure it’s okay to leave?"

    scene norikotsuneyocon17
    with dissolve

    n "Nope! But it’s not like I really need this job anyway. I just wanted some extra money to buy more nice underwear and stuff."

    if bonus == True:
        n "Especially since I have an official history of giving pairs to you now."
        s "Oh, right. That’s a thing you did."
    else:
        n "Especially since you wear the same kind, Sensei. It's just one more thing we have in common."

    t "You wear women’s underwear? That is disgusting."

    if bonus == True:
        s "I don’t-"
    else:
        s "Leave my hobbies out of this, Tsuneyo."

    t "Never talk to me or my son again, pervert."
    s "…"
    t "…"
    n "Yaaaay! Field trip!"

    scene black
    with dissolve

    "So...it appears that the time has come for me to head back to Tojo Ramen with Tsuneyo {i}and{/i} Noriko."
    "It’s not really how I expected the night to go, but at least Tsuneyo got what she came for."

    scene norikotsuneyocon18
    with dissolve2

    "Or...at least that’s what I would say if she didn’t only buy two bundles of them."

    s "Are you sure that’s going to be enough?"
    t "No. But it is the first time I am acting against the wishes of the Produce Delivery Administration and I don’t want to step too far out of line."
    n "I hate those guys."
    s "Wait, they’re a real thing? I thought that was just Tsuneyo being Tsuneyo again."
    t "I am always Tsuneyo, you bastard. How dare you question the legitimacy of my existence."
    s "Tsuneyo-"

    scene norikotsuneyocon19
    with dissolve

    t "Get leeked, bro."
    s "...Why?"
    n "You know, Tsuneyo, we haven’t really talked about it before...but I’m kind of a rival of yours in a way."

    scene norikotsuneyocon20
    with dissolve

    t "If this is about me becoming a romantic candidate for our teacher, you do not need to consider me a rival."
    t "That is something I am not interested in now...and likely never will be."
    s "Thanks."
    n "Not about that. About the whole restaurant thing."
    n "It’s not really {i}near{/i} here, but my family actually owns and operates a Chinese restaurant that does decently well, if I’m remembering correctly."
    n "So we both come from families who work in food service and stuff."
    t "Are you challenging me?"
    n "Not really. I’m just-"

    scene norikotsuneyocon21
    with dissolve

    t "Get leeked. "
    n "...Why?"
    s "I don’t like this new habit of yours."
    t "I do not like being challenged by the same person who sold me the produce I am going to serve to customers."
    t "For all I know, she poisoned these ingredients to put my family’s restaurant out of business. "
    t "I know your games, Pink Psion of...Pinkness! "
    t "I can’t remember your name!"
    n "It’s actually just...Noriko..."

    scene norikotsuneyocon22
    with dissolve

    n "Besides, I’m not trying to challenge you. I’m just trying to draw similarities and stuff."

    scene norikotsuneyocon23
    with dissolve

    n "You’re one of the few girls in the class that I’m not really close with yet. So I thought it might be easier to get to know you if you realize we have something in common."
    t "I understand now and apologize for leeking you."
    n "It’s whatever. It happens."
    s "Does it?"
    t "Your family’s restaurant...do they make their own noodles?"
    n "I...think so?"

    scene norikotsuneyocon24
    with dissolve

    t "Excellent. This is all I needed to hear."
    t "Any restaurant who takes the time to create such a thing can not be called a rival of mine."
    t "The true goal after all is spreading joy throughout the world in the form of thin wheat or rice tubes for people to swallow."
    t "As long as this mission is being accomplished, it does not matter who profits in the end."

    scene norikotsuneyocon25
    with dissolve

    t "My father started Tojo Ramen with one goal in mind...to make people smile."
    t "As such...I, too, want to make people smile."
    s "A good place to start would be not slapping them with vegetables."

    scene norikotsuneyocon26
    with dissolve

    t "Smile. I command it."
    s "Were you not listening to what I just said or do you actually just hate me?"
    n "Tsuneyo, don’t leek Sensei. He’s physically incapable of smiling. It’s not fair."
    s "Noriko is right. I don’t think my facial muscles work that way."
    s "Also, if I knew this journey was going to be for the purpose of buying you weapons, I would not have come. "
    t "Anything is a weapon if you try hard enough."
    n "Tsuneyo’s right. If the world were to end tomorrow and zombies started popping up or something, you’d use anything you can get your hands on as a weapon."
    s "Even a leek?"
    n "Hey, it’s working for her."
    n "Also, what if leeks {i}are{/i} the weakness of zombies and just...nobody’s figured it out yet because no one in their right mind would use one?"
    n "We could be onto something here."
    t "Listen to the Psion, bro. Accept the leek as punishment for your various misdeeds."
    s "Sigh."
    n "...Did you just {i}say{/i} “sigh?...”"

    scene black
    with dissolve2

    "The three of us move through the streets on the way back to Tojo Ramen and, despite the great amount of glares we received on the way {i}to{/i} the convenience store, nothing happens on the way back."
    "And I doubt it’s because Noriko makes us somehow look {i}less{/i} suspicious, so I just chalk it up to it being past all of the old, homeless peoples’ bedtimes or something."
    "Either way, we make it back to the ramen shop, leeks in tow, and prepare to head inside."
    "………"
    "……"
    "…"

    scene norikotsuneyocon27
    with dissolve

    n "Thanks for letting us come over so late, Tsuneyo. I’m sure you’re normally closing up by now."
    t "I’m sorry?"
    n "...Am I misunderstanding what’s happening right now?"

    scene norikotsuneyocon28
    with dissolve

    t "Tojo Ramen is already closed for the night. "
    t "Please do not tell Yelp."
    n "Then...why did you let us just walk you all the way back without saying anything?"
    t "I said many things. The most popular of which was, “Get leeked, bro.”"
    s "You did say that several times. "
    n "Can we at least get like...a drink of water or something?"
    t "I apologize, but water is for paying customers only."
    t "Please return tomorrow when we are open and have replenished our stock of green onions."
    n "But the...stock is replenished now..."

    scene norikotsuneyocon29
    with dissolve

    t "Thank you for helping me conquer the Produce Delivery Administration and restore my father’s legacy."
    t "I am sure that everyone will forgive my transgressions and return to purchasing noodles from me right away."
    s "Except for right now, you mean. Because...you won’t let us buy any."
    t "Read the sign, bro."
    n "But...the sign just says “ramen.”"

    scene norikotsuneyocon30
    with dissolve

    t "Oh."
    t "I suppose it does."
    n "…"
    s "…"
    t "Goodnight."

    scene norikotsuneyocon31
    with dissolve

    "Tsuneyo goes back into Tojo Ramen, leaving Noriko and me alone in the cold..."

    n "Sigh."
    s "…"
    s "Sigh, indeed."

    scene black
    with dissolve2

    "The two of us wind up taking a bus back to the area surrounding the dorms and grab something to eat over there. "
    "I walk Noriko back to her room once we’re done and the two of us part with a hug that I did not anticipate or even really want in the first place."

    if bonus == True:
        "But hey, things like that are bound to happen when someone is in love with you."
        "And it’s not like hugs are unenjoyable or anything."
        "They’re just..."
        "Weird."
        "I walk the rest of the way home thinking about how strange the concept of hugging is and how I would have much preferred a parting blowjob instead."
    else:
        "Just kidding. Hugs are my drug. I wish I could hug everything in the world."
        "I hug a pole on the way home and tell it I love it."
        "It's warm and feels nice against my face skin."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ noriko_love += 1
    $ ramen25p2 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen30:
...
```

## Code that triggers this event
File: \game\TsuneyoEvents.rpy
Code:
```python
...
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
...
```