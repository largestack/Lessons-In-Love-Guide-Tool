# Blackout
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen20&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 20

✅Event "[Tsuneyo: Fucking...Or What it Means to Live](./tsuneyodorm20.md)" is completed (event=tsuneyodorm20)



## Next events
* [Yuki: Rule #1](./yukidate1.md)
* [Touka: A Brief Moment in Time](./toukastreets5.md)
* [Yasu: Transference](./church1.md)

## Event properties
* ID: ramen20
* Group: Tsuneyo
* Triggered by label: ramenshop
* Triggered by branch label: ramenshop

## Event code
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramen20:
    scene blackout1
    with dissolve
    play music "kashiwagi.mp3"

    "I decide to drop by the ramen shop to check on Tsuneyo and grab a quick bite to eat."
    "But judging by the way she’s staring at me, I think it’s safe to assume that she is not very happy with my decision to do this."
    "I want to say she's only looking at me like this because I ordered a plate of curry instead of ramen tonight, but the scowl has been there since before I even ordered."

    s "Did I do something to offend you?"
    s "Is this about driving customers away again?"

    if bonus == True:
        t "I followed your advice and asked the Emerald Guardian to remind me of what sex is."
        t "Why did you allow me to say so many things about fucking?"
        t "Now everyone thinks I am a harlot."
        s "Not everyone. Just Uta and Yumi’s mom."
        t "Word gets around about girls like me. It won’t be long before the whole class knows."
        t "Also, those aren’t noodles in front of you."
        t "Why are you doing this to me?"

        "Ahh, so I guess the curry was part of it after all."

        s "On the bright side, it looks like you were able to learn more about modern dialogue. So all was not lost, right?"
    else:
        t "No. I am just angrily recollecting the video of the Marine who threw a puppy off of a cliff in 2008."
        s "I don't think I ever saw that."

    t "Fuck you."
    t "Not literally, though. I understand what that would mean now."
    t "It sounds very painful."
    s "And you’re not completely opposed to using that word even though you understand it now?"
    s "Color me impressed."
    t "I hope you choke on your non-noodle food and die."
    s "Why even sell it if you don’t approve of it as a product?"
    t "My father has informed me that it must remain on the menu for as long as he is alive."
    t "And with his days among us numbered, the days of this curry’s existence are numbered as well."
    t "The time for reckoning is upon us."
    s "You’re sounding more and more like Molly every day."

    scene blackout2
    with dissolve

    t "That is worrying to hear."
    t "With the things the other girls say about her, I’m beginning to believe the Emerald Guardian is not as omniscient as I initially thought she was."
    t "She is but another fruit that has fallen off the tree of life, and I am the lowly earthworm feeding off of her decaying corpse."
    s "Now you’re sounding less like Molly and more like a serial killer."

    scene blackout3
    with dissolve

    t "Well {i}you’re{/i} sounding like a little bitch."
    s "…"

    scene blackout4
    with dissolve

    t "I apologize if I didn’t use that word correctly."
    t "I heard the delinquent girl with mother issues call you that and you seem to fear her."
    s "First off, that was harsh. "
    s "Yumi’s issues with her mom are a private matter that only those two and sometimes myself are allowed to get involved in."
    s "Secondly, I am not {i}afraid{/i} of Yumi."
    t "But she defeated the Green Onion in a battle of arm strength so easily."
    t "What if you are next?"
    s "I'm curious to know about what chain of events would possibly lead to that."
    s "I’m really not afraid of Yumi, though."
    t "But I sense fear when you two are in close proximity to one another."
    t "Is it possible that you are the one {i}she{/i} fears instead?"

    if bonus == True:
        play sound "static.mp3"
        scene yumi10 with flash
        scene blackout4 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene wherethesidewalkends25 with flash
        scene blackout4 with flash
        stop sound

    s "I don’t think so. "
    s "I’m pretty sure she’s almost finished getting over the one thing I’ve done that {i}would{/i} scare her."
    t "What did you do?"
    s "That’s not really any of your concern."
    t "It’s not?"
    s "It’s not. "
    t "Interesting."
    t "I think you may be misunderstanding the purpose of this restaurant, Sensei."
    s "Are noodles...not the purpose of this restaurant?"
    t "They are the first purpose."
    t "But this store is much more than just noodles to myself and many others."

    scene blackout5
    with dissolve

    t "Tojo Ramen is a special restaurant where people from all walks of life can gather to consume pork broth and air out their worries."
    t "It is a place where people are free to speak their minds without worrying about persecution from others."
    t "A calm, quiet sanctuary in an otherwise dead section of the world."
    t "So, if there are things you wish to confess, there is no better place to do so than here."

    scene blackout6
    with dissolve

    t "Anything you say or do at this counter will never leave the restaurant so long as you do not want it to."
    t "Such is the promise of Tojo Ramen."
    s "It’s starting to make a little more sense why this has become a hangout spot for the Yakuza."
    s "Also, you should smile more. You look really cute right now."

    scene blackout7
    with dissolve

    t "It’s not me, it’s the noodles."
    s "…"
    s "No, it’s you."
    t "Noodles."
    s "…"

    "I guess it makes sense that this place could also serve as a haven of sorts for some people."
    "Late night restaurants with swarms of locals and nostalgic atmospheres are not exactly a foreign concept."
    "In fact, there’s probably a Tojo Ramen in every city in the world."
    "Now, on the other hand, I highly doubt there is a Tsuneyo Tojo in every city in the world."
    "She’s certainly proven to be...one of a kind so far."
    "But when you grow up in a place like this, breaking the necks of fowls and listening to tattooed men confess crimes between 300 Yen beer refills-"
    "I guess there’s not much of a chance to ever learn how the real world works."

    scene blackout8
    with dissolve

    t "How was the speech?"
    t "I memorized word-for-word what my father would say when he was still well enough to converse with others."
    s "He can’t even talk?"
    t "He can make noise, but the only one who understands him is me."
    s "Is it okay for me to ask what’s wrong with him, exactly?"
    t "It is not. "
    t "You shouldn't worry about that."
    t "All you have to do is enjoy your noodle-less dinner and speak what’s on your mind."
    s "Easier said than done. "
    s "Japanese men aren’t exactly known for being open and honest about their feelings- and I’m pretty sure I talk even less than most of them."
    t "My father is the same way."
    t "Or {i}was{/i} the same way."
    t "He doesn’t say much of anything anymore. But he does not need to."
    t "All he needs to do is recover. "
    t "And hopefully live forever so I can continue to avoid perpetual sadness like I have done for the rest of my incredibly boring life."
    s "Here’s to avoiding perpetual sadness, I guess."
    t "A strange toast, but one that I enjoy."
    t "I would drink to it if alcohol did not make me fall asleep the second it comes into contact with my tongue."

    "I reach for the spoon and finally take a bite of the curry Tsuneyo laid out in front of me some time ago."
    "It’s good, but it doesn’t measure up to the quality I’ve gotten used to from the ramen."
    "I guess Tsuneyo just doesn’t put the same level of care into this dish as she does the others."

    scene blackout9
    with dissolve

    t "Do you regret your decision now?"
    s "You mean do I regret ordering curry?"
    t "Yes. You have a face that says “It’s good, but doesn’t measure up to the quality of the ramen.”"
    s "That’s...exactly what I was thinking. But I don’t regret my decision."
    s "If I wanted ramen, I would have ordered ramen."
    s "Not everyone wants ramen every night, Tsuneyo."

    scene blackout1
    with dissolve

    t "When I told you it was okay to confess horrible things here, I did not mean {i}that{/i} horrible."
    t "I’m still interested in hearing why the delinquent girl is afraid of you."
    s "Listen, I’m glad that this place is the sort of restaurant where I can {i}air out my worries{/i} but...that’s not the type of person I am."

    scene blackout10
    with dissolve

    t "And I am not the type of person who is accustomed to looking death in the eye, yet I have been doing just that since our discussion in my room."
    t "Growing up means leaving your comfort zone. "
    t "It is why I come to[school] and why I learn. "
    t "Or...try to learn."
    t "Perhaps it is time for you to grow up as well, Sensei."
    s "When did you get so mature?"
    s "Go back to talking about noodles and cracking stand-up jokes."

    scene blackout11
    with dissolve

    t "Do not provide me false hope."
    t "We both know that I am unfit for comedy. "
    s "You’re unfit for most things, to be completely fair."

    scene blackout10
    with dissolve

    t "It’s true."
    t "I will die here the same way my father will."
    t "The only difference is that there will be no one to make sense of the borderline inaudible noises I make as I dissolve into the ground."

    stop music
    play sound "imscared.mp3"
    scene black

    ":)"

    "I instinctively jump back in my seat after a loud bang shakes the restaurant. "
    "I have no idea what it was, but it appears to have cut the power as well."

    t "Oh dear."
    s "“Oh dear?” "
    s "That’s all?"
    s "Are you not scared right now?"
    t "Why would I fear the darkness? I do not have darknessophobia."
    s "I just thought your reaction would be a bit stronger than “Oh dear.”"
    t "This is not the first time this has happened."
    t "The machines keeping my father well require a large amount of energy."
    t "Sometimes, the power goes off as a result of that."
    s "Do you have a generator or...a backup power source or anything?"
    t "We do. It should turn on down here momentarily."
    t "In the meantime, please excuse me while I go check on my father."
    t "He will likely die if the backup power has not yet turned on upstairs either."
    s "Do you want me to co-"
    t "No. "
    t "You must stay down here."
    t "He’s very adamant about remaining unseen. "
    t "Please continue to enjoy your noodle-less curry, though."

    play sound "footsteps.mp3"

    "I hear Tsuneyo get off of the stool next to me and make her way over to the door."
    "I’d have probably felt a little better if I was able to go with her but, then again, I’m not sure I’d enjoy seeing her half-dead father."
    "I’m just hoping the lights-"

    play sound "static.mp3"
    scene blackout12
    with flash
    stop sound
    play music "sanctuary.mp3"

    "The backup power source comes on and everything turns red."
    "Well, mostly everything."
    "My curry is still a mixture of brown and white."
    "Coincidentally, those are also the colors of Tsuneyo and me."
    "And when placed together on the same plate or, in this very specific circumstance, a restaurant-slash-confessional, things seem to work out pretty well!"
    "I insert my spoon into Tsuneyo and me and shovel the two of us into my mouth."
    "We taste delicious."
    "I spit out my food just so I can eat it again."
    "They should turn the lights off in here more often."
    "Maybe then I’d feel comfortable enough to admit that Yumi is only scared of me because I came within two steps of [raping] her in broad daylight."
    "Does a beautiful sunset count as broad daylight?"
    "Or is it vague daylight or something else comparable at that point?"
    "…"
    "I spit my food out a third time before the consistency becomes too gooey to enjoy anymore."

    if bonus == True:
        "I begrudgingly swallow it in the same fashion that delinquent begrudgingly swallowed my saliva all those {s}days? weeks? years?{/s} ?????? ago."
        "Where it happened wasn’t far from here."
        "Tsuneyo was right when she mentioned how this part of town is mostly dying."
        "I wonder if there’s a blackout in the surrounding buildings as well."
        "I could get away with so many things if I wasn’t so busy consuming myself."
    else:
        "I should have someone teach me how to chew one of these days."

    play sound "footsteps.mp3"
    "The footsteps leak back into my head but I’m unable to see where they’re coming from."
    play sound "footsteps.mp3"
    "It’s almost like ghosts threw some shoes on and started pacing around the place- "
    play sound "footsteps.mp3"
    "Hoping to score one last sip of broth before returning to Heaven or Hell or whichever other make-believe afterlife they were fortunate or unfortunate enough to find an apartment in."

    play sound "static.mp3"
    scene blackout12
    with flash
    stop sound

    s "…"

    "I feel...strange."
    "Kind of like I’m losing track of time."
    "How long has the power been off?"
    "Tsuneyo hasn’t come back downstairs yet, has she?"
    "I slide my phone out of my pocket to check the time."
    "And, of course, it appears to be dead."
    "Just my luck."
    "I could have sworn it was on nearly full battery before coming here, but it wouldn’t be the first time I’ve been wrong about that."

    s "…"

    "Part of me wants to just get up and leave since it’s starting to get extremely cold, but-"
    "Not only would I feel bad for abandoning Tsuneyo before even paying for dinner-"
    "I kind of..."
    "Can’t get out of my chair."
    "I mean, maybe I can, but-"
    "I don’t want to."
    "I’ve become content in my spot at the counter."
    "Tojo Ramen really is a special place."
    "I haven’t felt this at-home in quite some time."

    play sound "static.mp3"
    scene blackout13
    with flash
    stop sound

    t "Oh. You’re still here."
    s "Tsuneyo?"

    scene blackout14

    t "Ah-"
    s "How long were you gone for?"

    scene blackout15
    with dissolve

    t "Half an hour. "
    t "I assumed you just went home."

    "Has it really been that long?"
    "I feel like the power’s only been off for a few minutes."

    s "Is your dad okay?"
    t "He’s fine."
    t "The backup power upstairs starts immediately in the event of an outage. "
    t "The reason it takes so long to reach the ground floor is that my father requires almost all of it."
    t "Electricity can be very lazy."
    s "Do you know when the power will be coming back on?"
    t "That depends on {i}how{/i} lazy the electricity wants to be."
    t "There are many wires, so I assume it will take quite some time to catch up."
    t "Do you want a box for your curry?"
    t "I see that you haven't even touched it since I left."
    s "Oh, sure. I-"

    "I look down at the plate of curry to find that..."
    "I must have inadvertently...drawn a smile in the sauce?"

    s "Hey, you didn’t...play with my food while the lights were off, did you?"
    t "Food is for eating, not playing."
    t "If you want to play with food, choose a different restaurant. You are not welcome here."
    s "Just...get me a box. I don’t want to play with my food."
    t "I understand."
    t "The food is on the house today as apologies for the inconvenience and loss of power."
    s "Oh, cool. Thanks a lot. You didn’t have to do that."
    t "It was my father’s idea. "
    t "He could sense that there was a guest downstairs."
    t "I personally think we should have charged you for insulting us by ordering that stupid dish."
    s "You really don’t like curry, do you?"
    t "I love it."
    t "Please never order it again."
    s "…"
    t "…"

    scene black
    with dissolve2

    "Tsuneyo grabs me a box near the register and I shovel the rest of my dinner inside, placing it in a bag she lays out next to me as I do so."

    t "Tojo Ramen sincerely apologizes for the loss of power during your visit tonight."
    t "Please accept this coupon for 23%% off of your next check."
    s "Why not just round up to 25%%?"
    t "I don’t make the rules, just the noodles."
    s "Well...thanks, I guess."
    t "No, thank you."
    t "Please come back soon."
    t "We are grateful as always for your business."

    "I tie the handles of the plastic bag into a knot and exit the store."
    "It’s snowing out."
    "I wind up throwing away my curry in the first garbage bin I find."
    "I don’t know why."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen20 = True

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"

    scene smile
    with dissolve4
    $ renpy.pause(5, hard=True)
    scene black
    with dissolve4
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen25:
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
...
```