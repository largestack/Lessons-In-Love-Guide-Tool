# Sober-ish
Haruka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukadate20&go=Go)



## Event preconditions
✅Haruka love greater than or equal to 20

✅Event "[Main: War's End](./dormwar17.md)" is completed (event=dormwar17)



## Next events
* [Haruka: Unfiltered Tap Water](./harukainvite3.md)

## Event properties
* ID: harukadate20
* Group: Haruka
* Triggered by label: callharukanighthang
* Triggered by branch label: callharukanighthang

## Event code
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukadate20:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "It’s been a little while since the two of us have actually done anything and-"
    "Wait."
    "{i}Have{/i} we actually done anything?"
    "I feel like every time the two of us hang out it’s either at her house, the cafe, or my place."
    "Not that I have a problem with that, but..."
    "I can’t imagine it’s entirely fulfilling for her."

    play sound "phonebeep.wav"

    h "Hey, what’s up?"
    s "Hey. What are you doing tonight?"
    h "Probably crying and eating ice cream again. You know how it is."
    s "Want to come out and do something?"
    h "Can you wait like...two hours? I’m still at work."
    s "Still? Don’t you normally get off before dinner?"
    h "Normally, yes. But it’s been really busy and I didn’t want to leave Molly and the other part timer alone, so..."
    s "Because you were worried about her or because you wanted to keep your store from exploding?"
    h "Yes."
    s "But there were two-"
    h "Hey! Why don’t you come hang out here in the meantime? Your [niece] and her friend are here too."
    s "…"

    "I mean, it’s not like I have anything else going on, so..."

    s "Sure. I’ll start heading over now."
    h "Cool! I’ll see you soon, then."

    play sound "phonebeep.wav"

    "I hang up the phone and begin walking over to the cafe."
    "It seems that my awesome and spontaneous plan of actually going out and doing something for once is basically trashed since Haruka can’t escape work yet, but at least I’ll still get to see her."

    if bonus == True:
        "Teenagers are great and all because...yeah. But it’s still a nice break being able to hang out with someone my age who...shares the same interests as I do."
        "Frankly, there aren’t many girls out there like that."
        "At least not that I know of."
        "As always, my hands find their way into my pockets and my legs find their way ahead of themselves, bringing me closer to my destination with each and every step."

    "………"
    "……"
    "…"

    scene harukadatetwenty1
    with dissolve
    play music "cafe.mp3"

    h "Hey! That was quicker than I expected!"
    s "Hey, Haruka. Hey, everyone else."
    a "Lumping me in with “everyone else” and addressing the cafe lady by her name makes it sound like you aren’t here to see me."
    s "How would I have even known you were here?"
    a "You mean you’re not constantly watching the GPS tracker on my phone to see where I’m hanging out like I do with you?"
    s "I’m sorry, what?"
    h "Do you need anything? Coffee? Tea? A new [niece]?"

    scene harukadatetwenty2
    with dissolve

    a "I will destroy everything you love."
    h "Joke’s on you. I have nothing left but this cafe."
    s "I’m fine, thanks. I didn’t really come here to buy anything."

    scene harukadatetwenty3
    with dissolve

    h "Okay. But know in the future that I have the right to refuse service to anyone I want. And if you’re just going to loiter around the place, I won’t let you inside anymore."
    s "Well if that’s the kind of business you’re running, I’ll just have to excuse myself."

    scene harukadatetwenty4
    with dissolve

    h "Wait, no. Take me with you."
    h "I don’t want to be here anymore. I’ve been on my feet since this morning and my back is literally killing me."
    s "Gee, I wonder why."
    h "Yes, boobs. They are things I have. "
    h "Point is, I’m in pain. Please help."

    if bonus == True:
        s "I mean...I guess I could hold them for you and...take some of the weight off of your back or something."

        scene harukadatetwenty5
        with dissolve

        h "If that is what must be done for the sake of my spinal health..."
        a "Do I even need to say anything here?"
        s "You don’t. I’m pretty sure Maya’s look says enough for the two of you combined."
    else:
        s "Well, I'm not a fucking doctor, Haruka. What do you expect me to do?"

    m "You’re disgusting."

    if bonus == False:
        m "You should have gone to medical school."

    s "Thank you for explaining exactly what the look entails, Maya. I would have had no idea otherwise."

    if bonus == True:
        m "Since when do you even talk to anyone your age? This entire scenario is weird."
    else:
        m "You are such a disappointment. I can't believe I ever liked you."
        s "You what?"

    mo "You really don’t have to stay around any longer, Haruka. I’m fine on my own now."

    scene harukadatetwenty6
    with dissolve

    h "I know I don’t {i}have{/i} to...but I’d feel bad otherwise. The kitchen’s an absolute wreck right now."
    mo "I’ll just stay a little later to help the other girl clean up back there. Go out and enjoy yourself. "
    mo "It’s the least I can do after you helped me out during the great cafe calamity."
    a "Cafe...calamity? Is something wrong, Molly?"

    scene harukadatetwenty7
    with dissolve

    mo "Nope! Just trying to take advantage of my high persuasion to fend off the Magistrate of Mammaries and earn some extra gacha money while I’m at it!"
    mo "Besides, I have you two to help me if things get crazy again! And you are forced to do so as I determine the fates of your D&D characters!"
    m "It was only a matter of time until she started using this as leverage for blackmail."
    mo "Silence, Urrheak!"
    m "Scraw."
    a "I don’t mind helping, but...if you let the Magistrate of Mammaries leave, she’ll take Sensei with her and that is bad."
    h "Can we...stop using that ridiculous nickname?"
    a "Silence, boob lady."
    mo "While it may be true that the two of them will spend more time together based on this decision, I have disabled rollback and am incapable of changing courses at this point in time!"
    mo "Besides, side characters need love too!"
    h "I’m a...side character?"
    s "You’re all main characters to me, Haruka."

    scene harukadatetwenty8
    with dissolve

    a "But I’m the {i}main{/i} main character. Right, Sensei?"
    mo "I’m afraid that position belongs to me, Strawberry Songstress. Molly MacCormack is the ultimate heroine, after all."
    s "I’m actually going to give the main heroine spot to Maya for being so silent and disinterested in the position."
    m "Oh, good. Exactly what I wanted. Great."
    h "So...uhh...I guess I have the night off now?"
    s "I guess you do. "
    s "Does this mean we’re going to actually do something for once?"

    scene harukadatetwenty9
    with dissolve

    h "Do something? Us?"
    h "But we never do anything. Not doing anything is kind of our thing."
    s "There’s always...the bar, I guess?"
    h "I mean...I have a change of clothes in my office..."
    h "But Sara and I just got into an argument about which Avenger is the hottest and I’m currently mad at her."

    scene harukadatetwenty10
    with dissolve

    mo "Ooooh, who was your choice?! Iron Man?! Thor?!"
    h "{i}Black Widow.{/i}"
    mo "{i}Nice.{/i}"
    s "I have no idea what’s going on, but I was thinking maybe some bar that isn’t owned by Sara."

    scene harukadatetwenty11
    with dissolve

    h "Are you sure? She could really use the business."
    s "She’ll figure it out."
    s "I say we take advantage of my newfound desire to do something and go to the urban district."

    scene harukadatetwenty12
    with dissolve

    h "All the way over there? Are you serious?"

    if bonus == True:
        mo "Good luck with your bonus CG, Sensei."

    a "That makes it sound like a date! You never take me to the urban district! I wanna go!"
    s "It’s not a date. Haruka and I are just friends. "
    h "I suddenly feel like a college kid about to go bar hopping again."
    s "Just don’t get so drunk that I have to carry you home."

    scene harukadatetwenty13
    with dissolve

    h "Challenge accepted! I’ll go get dressed right now."

    stop music fadeout 10.0
    scene black
    with dissolve2

    "Haruka thanks Molly one more time before heading to her office to change out of her work clothes."
    "She comes back a few minutes later and the two of us say goodbye to the rest of the girls, who have already started debating some geeky stuff I couldn’t be bothered to listen to."
    "It’s clear that at least Ami is uncomfortable with the idea of me going out with Haruka, but Ami is uncomfortable with pretty much everything I do, so that’s to be expected."
    "Either way, Haruka and I wind up boarding a bus to the urban district and, in less than fifteen minutes, we’re wandering the streets..."

    scene nightsky
    with dissolve
    play music "samhain.mp3"

    "We wind up stopping at whichever bars we can find inside of the concrete jungle as the night ticks on and on."
    "I don’t know if it’s just all of the walking that’s keeping her sober-ish, but Haruka doesn’t seem fazed at all even after the fourth bar. "
    "In fact, about two or three hours of drinking go by before I start to see any signs of inebriation in her at all. And even {i}I’m{/i} feeling a little buzzed at this point."
    "None of it feels out of the ordinary, though."
    "In fact, if you get rid of all the conversation, it hardly even seems like I’m out with {i}anyone{/i} right now."
    "I don’t have to watch what I say (Which I never do anyway, to be completely fair) and I don’t have to mind what I do."
    "We’re just two human beings spending more money than we probably should, and more time in new places than we typically would."
    "It’s...a strangely good night."
    "One that I doubt I’d ever be able to recreate with someone like Sara or Maki."
    "…"
    "Maybe I...actually like doing things every once in a while?"

    scene harukadatetwenty14
    with dissolve

    h "Ah! Is that snow? Do you see snow, Sensei?"
    h "Quick, look up. Before it melts."
    s "It’s just frozen rain. It’ll be gone before the weather even has a chance to get hotter."
    h "Oh, shut up. Don’t be such a buzzkill now that all of the bars are closing. Get excited about something for once."
    s "I’m not going to get excited about the water cycle, Haruka."

    scene harukadatetwenty15
    with dissolve

    h "Fine then. You pick. "
    h "What do you want to talk about?"
    h "Girls? Boys? Us?"
    s "Us?"
    h "Yeah, us."
    h "I can’t be the only one thinking about how much fun tonight’s been, right?"
    h "Like, I’m all for wrapping myself up in[teen]drama, but spending time away from it for a change and just...not focusing on anything with you has been pretty awesome."
    h "Even with Sara and stuff, it’s hard to really feel like...I don’t know, detached?"
    s "Detached from what, exactly?"
    h "Everything, dude."

    scene harukadatetwenty16
    with dissolve

    h "Like, it feels like...the rest of the world’s been deleted and that the urban district is all that’s left."
    h "And that we no longer have anything to actually worry about, so we’re just being ourselves and...enjoying it in the simplest way possible before everything comes back tomorrow."
    s "Well, I’m glad you managed to have a good time."
    s "I’d be lying if I said I wasn’t having fun as well."

    scene harukadatetwenty17
    with dissolve

    h "Exactly! You’re the first guy since my husband that I’ve been able to feel like this with."
    h "Which isn’t me hitting on you, by the way. That’s not what I’m getting at here."

    scene harukadatetwenty18
    with dissolve

    h "I’m just glad that we did this tonight. "
    h "Like, if you never called, I’d probably still be cleaning the cafe right about now."
    s "It’s been several hours and I highly doubt the girls are still there."
    h "Okay, whatever. I still want to thank you for saving me at least an hour of cleaning."
    h "You’re thankful too, right? For having me, I mean."
    s "Are you fishing for compliments now?"
    h "I’m not...{i}not{/i} fishing for compliments?"
    h "I don’t know. I’m a little drunk, but I’m basically just trying to say that it’s nice having somebody who feels like a real friend rather than just someone I’ve known for a bunch of years."
    h "Sara and Maki are great, but...there’s never anything new with them."
    h "And whether they want to believe it or not, they both kinda settled down and had kids and..."
    s "And you never stopped being young."

    scene harukadatetwenty19
    with dissolve

    h "I...don’t know if I’d go that far."
    h "I feel like, on at least some level, no one ever stops being young."
    h "It’s why even tiny things like going to bars or talking about the cute girls who served us at those bars can make us feel younger, even if it’s for just a little while."
    h "And I’m sure Sara and Maki feel plenty young, too. "
    h "Sara...probably {i}too{/i} [young]at times. But her circumstances are a lot less normal than Maki’s, as weird as that is."
    h "If anything, it’s probably more like Sara has yet to grow up."
    h "People like you and me on the other hand...who are in that weird position of being old but not {i}that{/i} old...and having just started our careers and whatnot-"

    scene harukadatetwenty20
    with dissolve

    h "It’s...cool."
    h "I don’t know. I’m probably just happy that there’s someone I can relate to who doesn’t also want to paint my nails."
    h "Is this getting weird? I feel like I’m doing all of the talking and that I might be making a big deal out of something that’s just like, totally normal for you."
    s "No, I think you more or less explained how I’m feeling. "
    s "You just did it a lot more...positively, which I guess I’m thankful for."

    scene harukadatetwenty21
    with dissolve

    h "Of course."
    h "Positivity is something I definitely struggle with sometimes, but when I’m not too busy beating myself up over things that aren’t in my control or-"

    if bonus == True:
        s "Or fantasizing about your employees."
        h "Or fantasizing about my employees, thank you for that- "
    else:
        s "Churning butter?"
        h "How did you know about that?"
        s "Edcuated guess."
        h "Well, you are correct. That is a hobby of mine."

    h "When I’m not too busy doing either of those things, I really try. You know?"

    if harukasex == True:
        scene harukadatetwenty22
        with dissolve

        h "And..."
        h "Well, it goes without saying but..."
        h "Sometimes I fail..."
        h "And I do things that no one should ever do just because I’m impulsive or-"
        s "Haruka, you really don’t have to-"
        h "No, hold on. "
        h "Sometimes I do things like that because...because I’m only human. "
        h "And...and all humans can be forgiven if they’re regretful enough."
        s "Are you regretful?"

        scene harukadatetwenty23
        with dissolve

        h "…"
        h "I want to be."
        h "It’s just...a lot harder when there are nights like this, where the takeaway is that...maybe I was never ready to settle down at all?"
        h "I don’t know."
        h "Just...thanks, I guess."
        s "For what, exactly?"
        h "For kind of...brute forcing me into realizing that I don’t understand why I do certain things or...or feel certain things."
        h "And for giving me moments where I don’t have to deal with any of that and can just...have fun instead."

    else:
        scene harukadatetwenty18
        with dissolve

        h "Actually, you don’t even have to answer that."
        h "I know you know."
        h "You’ve had...several opportunities to push me into things that would be bad for our relationship, and you haven’t taken any of them."
        h "In fact, you’ve even gone out of your way on nights like tonight to remind me that it’s okay to just...let myself go in ways that aren’t totally self-destructive."
        h "And, weirdly enough, I feel less alone tonight than I have in a long time."
        h "So, thank you...really."

    scene harukadatetwenty24
    with dissolve

    s "There’s no point in thanking me."
    s "Just live however you want and let whatever is going to happen just...happen."
    h "Sure, there might not be a point in it...but I’m still going to thank you anyway."
    h "Even if none of that had ever happened and this was the first time we’d hung out, I’d still thank you."
    s "Why, though? I haven't even done anything."
    h "That's not true."

    if bonus == True:
        h "For example...Tonight, you helped me remember that being [young]isn’t everything by choosing to go out with me instead of spending your time with three hormonal [teenager]s."
        s "Two hormonal [teenager]s and one weird shrine maiden."

        scene harukadatetwenty25
        with dissolve

        h "If you think for a second that third girl doesn’t get under the covers and finger herself at least once a week, boy do I have news for you."
        s "…"
        h "…"
        h "What?"
        s "Nothing. I like that image."
        s "I just can’t help but feel like she’s listening in and judging me at every moment, so I’m being careful to not inadvertently upset her."
        h "Well...whatever. You get what I'm saying."
    else:
        h "But I guess it makes sense that the man who defeated Dr. Badguy would be so humble."
        s "You helped too. Never forget that."

    scene harukadatetwenty24
    with dissolve

    h "We...should probably start heading back now, though."
    s "We’re already heading to the bus stop. Where did you think we’ve been walking this whole time?"
    h "I don’t know. I haven’t really been paying attention."
    s "That or you’re actually just a lot more drunk than you're letting on."
    h "You’ve seen me drunk. This isn’t drunk Haruka. "
    h "Drunk Haruka would have taken that thing about the third girl a lot further and then gotten way too excited."
    s "I kind of wish you {i}were{/i} drunk now."
    h "Heheh..."
    h "If only there were still some bars open..."

    scene black
    with dissolve2

    "Haruka and I make it to the bus stop a few minutes later and get on board."
    "I get off at her stop despite it being miles away from my home."
    "I’m not sure why."
    "But I say goodbye to her without so much as a parting hug and begin my journey back to the house."
    "The alcohol wears off somewhere around the halfway point and I become uncomfortably cold."
    "That discomfort feels a lot less serious, however, when I realize it’s nothing compared to what Haruka must feel every time she sees me."
    "What an interesting dynamic the two of us have."

    $ renpy.end_replay()
    $ haruka_love += 1
    $ harukadate20 = True
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label harukainvite3:
...
```

## Code that triggers this event
File: \game\HarukaEvents.rpy
Code:
```python
...
label callharukanighthang:
    if harukanumber == True and day89 == False:
        "I think I should probably get to know Haruka a little better before calling her."
        jump callnight
    if haruka_love >= 0 and day89 == True and harukadate1 == False:
        jump harukadate1
    elif haruka_love >= 0 and haruka_love <= 4 and harukadate1 == True and harukadate5 == False:
        play sound "phonebeep.wav"

        "I tap on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer."
        "..."
        "I hope she doesn't still feel weird about what happened at the bar the other night."
        "Oh well...I guess I'll just have to...keep visiting her at the cafe or something for now."
        jump callnight
    if haruka_love >= 1 and haruka_love >= 5 and harukadate1 == True and harukadate5 == False:
        jump harukadate5
    if haruka_love >= 15 and harukadate10 == True and harukadate15 == False:
        jump harukadate15
    if haruka_love >= 20 and dormwar17 == True and harukadate20 == False:
        jump harukadate20
...
```