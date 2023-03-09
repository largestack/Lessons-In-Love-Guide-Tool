# Fucking...Or What it Means to Live
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsuneyodorm20&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 20

✅Event "[Tsuneyo: Moe Fan Service](./tsuneyodorm15.md)" is completed (event=tsuneyodorm15)

✅Day of week is not Friday

✅Event "[Main: Caterpillar](./day247.md)" is completed (event=day247)



## Next events
* [Tsuneyo: Blackout](./ramen20.md)

## Event properties
* ID: tsuneyodorm20
* Group: Tsuneyo
* Triggered by label: tsuneyodorm
* Triggered by branch label: tsuneyodorm

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label tsuneyodorm20:
    play sound "knock.mp3"

    if bonus == True:
        "I knock on the door, hoping that Molly has decided to dress Tsuneyo up as another fictional character she’s attracted to tonight."
        "And while that situation is unlikely due to the fact that it has only happened one out of the many times I’ve been here, the dream lives on."
    else:
        "I knock on the door, ready to play Yahtzee."
        "I even brought orange juice for everyone to share."

    u "Come in!"
    s "…"

    "Uta? "
    "Did I knock on the wrong door?"
    "I take a step back to confirm that I did, in fact, knock on the door to room #6. "
    "So...unless the girls swapped rooms or roommates, it seems as if I have, once again, stumbled upon more than I’ve bargained for."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "…"

    scene tsuneyouta1
    with dissolve

    u "Ohohoh~ A late night visit from the teacher. "
    u "I knew something was going on when Tsuneyo asked me to come talk to her, but I didn’t think it would end like {i}this.{/i}"

    if bonus == True:
        u "To think my first time would be a threesome with two of the tallest people I know..."
    else:
        s "I am only here to play Yahtzee."

    u "What are you two planning on doing with little ole’ Uta?"

    if bonus == False:
        s "Play Yahtzee."

    t "Are you here to see Uta, Sensei?"

    if bonus == True:
        s "Why would I have knocked on {i}your{/i} door if I was here to see Uta?"
    else:
        s "I am here to play Yahtzee."

    u "Oooooh okay, so you were looking for solo action and want me to film it."

    if bonus == False:
        s "{i}Hah...{/i}"

        "I put Yahtzee down."
        "I will drink orange juice by myself in the dark later."

    u "I’ll go get Io’s camera. Hold on one sec."

    scene tsuneyouta2
    with dissolve

    t "Solo action?"

    if bonus == True:
        u "You know! Knockin’ boots. Bumpin’ uglies. The old fashioned beef injection."
        s "I didn’t like that last one at all."
        t "I think a beef injection sounds delicious."
    else:
        u "Yeah. It's when one person fills their pockets with as many beans as they can and tries to walk around without revealing them"
        t "..."

    scene tsuneyouta3
    with dissolve

    u "Hold on a sec, you really have no idea what I’m talking about? "
    u "You can’t be that innocent, can you?"
    t "I’m not innocent."

    if bonus == True:
        t "If injecting the beef is a crime, lock me away now."
    else:
        t "What does my innocence have to do with a pocket full of beans?"

    s "Tsuneyo’s lived a very sheltered life, Uta. Please do not corrupt her before I can."

    scene tsuneyouta4
    with dissolve

    u "Ooooh okay, okay!"
    u "The last half hour is startin’ to make a lot more sense to me now."
    t "I reached out to Uta for the sake of my father, as I know she has experience in caring for people."

    scene tsuneyouta5
    with dissolve

    u "Hope I didn’t talk your ear off with all of my advice."
    u "You sound really close to your pops and I’m startin' to get why."
    u "You don’t have anybody else, huh?"
    t "I’m afraid I do not. My mother has not been in the picture for quite some time."
    t "And if anything happens to my father, I will be more alone in this world than anyone has ever been before."
    u "Well, I sure hope everything turns out okay!"
    u "And if it doesn’t, I’ll ask my parents to adopt you once the barrier opens back up."
    u "Oh! You could be my little sister! Doesn’t that sound fun?"
    s "I think you’d be better suited to be the little sister, Uta.  "

    scene tsuneyouta6
    with dissolve

    u "Come on! I’ve always wanted a little sister and I’ve been stuck {i}being{/i} the little sister ever since I was born!"
    s "That is how being born as a little sister works, yes."
    t "You two seem very close."
    t "Do you fuck Uta the same way you fuck me, Sensei?"
    u "…"
    s "…"
    t "What?"
    u "{i}Isn't she supposed to be innocent?{/i}"
    u "{i}What have you done to this poor girl?{/i}"
    u "{i}Am I next?{/i}"
    s "{i}It’s a long story. She doesn’t know what that word means yet.{/i}"
    u "{i}You should tell her!{/i}"
    s "{i}But it’s so fun this way...{/i}"

    scene tsuneyouta7
    with dissolve

    u "Uhh..."
    u "You’re a real special girl, Tsunecchi."
    t "Tsuneyo."

    scene tsuneyouta8
    with dissolve

    t "Ah-"

    "She does that when she says her own name as well?..."

    scene tsuneyouta9
    with dissolve

    u "Tsunecchi is your nickname. It sounds more fun than Tsuneyo, don’t ya think?"
    t "I understand. In that case, I shall give you a nickname as well."
    u "Hit me! I’m ready for any nickname you give me!"
    s "I feel like you are going to regret those words very shortly."
    t "From this day forth, I will refer to you as...Green Onion."
    u "…"
    t "…"
    s "See?"
    u "Tsunecchi, why do you want to call me Green Onion?"

    scene tsuneyouta10
    with dissolve

    t "The Green Onion is a delightful addition to a bowl of ramen, just as you are a delightful addition to my life."
    t "It is also one of the key ingredients in Kansai based ramen, and you are from the Kansai region. "
    u "…"
    u "Those are actually really thoughtful and cute reasons."
    s "Yeah, there was a lot more thought put into that than I expected."

    scene tsuneyouta11
    with dissolve

    u "Okay! From this day forth, Uta Ushibori will be known as Green Onion!"
    s "You took to that way too easily. Defend your family name, Uta."

    scene tsuneyouta12
    with dissolve

    u "Any last questions for me before I go back to my room?"
    u "Io’s still waiting for me in there and I just realized I've been gone for a pretty long time."
    t "I have no additional questions at this time. "
    t "Thank you very much for your assistance, Green Onion."
    t "May flavor find its way home to you."
    s "What kind of goodbye is that?"
    u "And to you as well, Tsunecchi."
    s "You’re just going to go along with it?"

    scene tsuneyouta13
    with dissolve

    u "Heheheh...don’t stay up too late, you two."
    t "Do not worry, Green Onion. We will fuck each other as quietly as possible so that no one will be disturbed."
    u "…"
    s "You heard her, Uta. "
    u "Please explain what that means to her as soon as possible."

    play sound "dooropen.mp3"
    scene tsuneyouta14
    with dissolve

    "Uta leaves the room and I’m finally left alone with the girl I actually came here to see."

    t "Have I been using that phrase incorrectly?"
    s "To be completely honest...yes. As incorrectly as possible."
    s "But I don’t think you’d be very happy to hear what it actually means."
    t "I’m sure I can handle it. "
    t "If I am ever going to learn how to properly engage in conversation with my peers, I must know who I can fuck and when."
    s "Well, you see..."

    if bonus == True:
        s "“Fucking” someone means having sex with them."
        t "…"
        t "Can you remind me what sex is?"
        t "I remember hearing it from the blonde girl in our class, but that conversation contained many confusing things and I’m afraid I may have mixed some up."
        s "Just ask Molly when she gets home."
        s "Giving you a textbook explanation of sex would be a very surreal experience for both of us."
        t "I feel as if I have made a grave mistake that I will have a hard time severing from my memory."
        s "Probably, but that’s a bridge we’ll cross another day."
    else:
        s "Actually, nevermind. I'm not really sure what to say in the censored version that would make this okay."

    scene tsuneyouta15
    with fade
    stop music fadeout 25.0

    t "Hah..."
    t "There are so many things I do not understand."

    "Tsuneyo takes a seat on her computer chair and hugs her knees for what I imagine is comfort."
    "She already had to enlist the help of one of the most...outspoken members of the class tonight, so I’m sure she’s exhausted from having to talk for so long."
    "Or listen for so long."
    "But, then again, she deals with Molly on a daily basis...so maybe Uta wasn’t as much of a chore for her as I imagined she would be."

    s "Like what?"
    t "Like fucking...or what it means to live."
    s "If it’s any consolation, those two things are pretty interchangeable in my book."

    scene tsuneyouta16
    with dissolve
    play music "closeto.mp3"

    t "While Green Onion was able to provide me several useful tips for taking care of a loved one tonight, she also made things sound quite terrifying."
    t "I’m beginning to understand that my father’s time here may be coming to an end."
    t "He grows weaker day by day."
    t "It isn’t long before he’s unable to recommend me swimming tubes or teach me the proper ways to slaughter birds."
    t "I feel as if it were just the other day he was teaching me the difference between shio and shoyu."
    t "The fear of death you mentioned recently is starting to make sense to me."
    t "But it is not the act of death that torments me."
    t "It is the thought of what comes after."

    scene tsuneyouta17
    with dissolve

    t "I do not want my father to turn into a tree."
    t "You can not talk to trees. And they teach you nothing."
    t "Also, he will die in his room upstairs and a tree would be sure to crash through the floor and destroy the restaurant."
    t "What should I do?"
    s "Why ask me?"
    s "Death isn’t something I’m particularly good at dealing with. "
    s "And it’s not like I have all of the answers."
    s "Or...{i}any{/i} of the answers, for that matter."
    t "I do not expect you to. "
    t "But my father always told me adults are smarter than children."
    t "And though I may not possess the body of a child, my mind begs to differ."
    t "There is not a single day that passes by without me misunderstanding something. "
    t "I feel like an infant."
    t "I do not think I am suited for death."
    t "I don’t want to be alone."
    s "No one is {i}suited{/i} for death, Tsuneyo."

    scene tsuneyouta18
    with dissolve

    t "Ah-"
    s "Please don't “Ah-” me with that look on your face. It ruins the fun."
    t "It is a reaction. I can not help it."
    s "That aside...You should probably know that you’re never going to be alone."
    s "Do you really think Molly would abandon you or make you fend for yourself in the outside world?"

    scene tsuneyouta19
    with dissolve

    t "The Emerald Guardian does not like the outside world."
    t "She has informed me on many occasions that she is not particularly good at dealing with it and will avoid it by all means necessary."
    s "And that’s definitely true..."
    s "But she’s also experienced the death of a parent."
    t "That is correct. She told me about what happened to her mother."
    t "It sounded very hard."
    t "Will I go through the same thing?"
    s "Eventually, yes."
    t "…"
    s "A lot of the girls in class are missing a parent."
    s "In fact, barely any of them have both."
    t "Barely any of them have {i}none{/i} either. "
    s "Also a good point."
    s "If you think too much about the future, though, you’ll just run out of the present even quicker."
    t "…"

    scene tsuneyouta20
    with dissolve

    t "You are right."
    t "I must wait if I want to feel upset."
    t "I still have a job to do."
    t "My father has not yet given up on living, so I should not be giving up on him."
    t "I am a failure as a daughter."
    s "You’re not a failure..."
    s "In fact, I don’t even think what you were doing just now is giving up."
    s "You’re just confused."
    s "If you were giving up, you wouldn’t have reached out to Uta for help."
    t "I wish Green Onion was able to teach me how she remains so calm in the face of death."
    t "Her casualness on the subject makes me feel weak. Like there is much more for me to learn."
    s "She {i}is{/i} suspiciously casual about that and it is definitely concerning."
    s "But I don’t think you should worry too much about how other people would react to your situation."
    s "Just live each day as if it’s your last and you’ll be fine."

    scene tsuneyouta21
    with dissolve

    t "My last?!"
    t "Am I next?!"
    t "Why is life so cruel all of a sudden?!"
    s "It’s an expression, Tsuneyo. "
    t "Ah!"
    s "Your “Ah’s” are completely off tonight. It’s making me uncomfortable."

    scene tsuneyouta22
    with dissolve

    t "Perhaps it would be good if I just went to sleep early..."
    t "I have heard others mention that “beauty sleep” is good for them. "
    t "And I have learned recently through the art of photography that I, Tsunecchi Tojo, Warrior of Soup...am beautiful."

    scene tsuneyouta23
    with dissolve

    t "Probably."
    t "That is what the Emerald Guardian and the rest of her club told me, at least."
    t "And I have no reason to disbelieve them at this moment in time."
    s "Well, they’re right. You should listen to them more often."
    t "If I listened to them more often, we would not be talking right now."
    s "...Why?"
    s "What did they say to you?"

    if bonus == True:
        t "To stay away from you at all costs if I want to maintain my chastity."
        t "Unfortunately, I do not know what chastity is, so I am not too worried about this."

        "I imagine it was Maya who told her that..."
        "Though, I can see Ami saying it as well just to...thin out the competition."
    else:
        t "That I should go build the biggest sandcastle in the entire world."

    s "Okay, maybe {i}don’t{/i} listen to everything they say. But you can listen to the beautiful part."
    t "I am a free woman. You shall not tell me who I can and can not listen to."
    t "If you are looking for a fight, you have come to the right place."
    s "All I wanted to do was compliment you and now we have to fight?"
    t "You brought this upon yourself."
    t "Just as I will bring the pain upon your body."
    s "Okay then. I think it’s time for me to go."
    t "Running away from a challenge? "
    t "And you call yourself a man?"
    s "Yes."
    s "But, honestly, there’s a creeping feeling inside of me that’s saying you probably {i}would{/i} beat me in a fight and that would hurt my pride."

    scene black
    with dissolve2

    "I move toward the door and hear Tsuneyo get out of her chair."

    t "Wait."
    s "What’s up?"
    t "I feel as though I should thank you for listening to my problems."
    t "I was taught to never burden anyone, and my inability to function independently has led to me burdening you quite often."
    t "Please continue to nurture me."

    "Tsuneyo bows and I...can't help but feel out of place."
    "All I did was visit her room in hopes of seeing her in another costume."
    "I had no idea this would turn into...whatever it turned into."

    s "Of course."
    s "Though, I doubt what I’m doing could be called nurturing."
    t "If you think of a better word, please let me know."
    t "I’m looking forward to learning more from you."

    $ renpy.end_replay()
    $ tsuneyodorm20 = True
    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyodorm25:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label tsuneyodorm:
    if tsuneyo_love >= 5 and ramen1 == True and tsuneyofirsthall == True and tsuneyodorm5 == False:
        jump tsuneyodorm5
    if tsuneyo_love >= 10 and ramen10 == True and tsuneyodorm5 == True and tsuneyodorm10 == False:
        jump tsuneyodorm10
    if tsuneyo_love >= 15 and ramen15 == True and day != 1 and tsuneyodorm15 == False:
        jump tsuneyodorm15
    if tsuneyo_love >= 20 and tsuneyodorm15 == True and day != 5 and day247 == True and tsuneyodorm20 == False:
        jump tsuneyodorm20
...
```