# Somewhere Inside of a Dream
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayafestival1&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 464

❌Event "[Main: Glued to the Sky](./christmastwo20.md)" is completed (event=christmastwo20)

✅Day of week is Saturday



## Next events
None

## Event properties
* ID: mayafestival1
* Group: Maya
* Triggered by label: saturdaymorning
* Triggered by branch label: saturdaymorning

## Event code
File: \game\MayaEvents.rpy
Code:
```python
...
label mayafestival1:
    play music "goodmorning.mp3"

    "I hear a door open from somewhere inside of a dream."
    "Well, the door isn’t inside of a dream."
    "I am."
    "Or was."
    "I don’t remember much of it, just that something was there."
    "I guess I’ve never been adept at recalling things I experience while unconscious, though."
    "The scent of watermelon shampoo drifts closer to my bed, but I already had a feeling it was Maya who entered by the way the door sounded when it opened..."
    "Quiet and urgent, backed by a heavy dose of arrogance and the slightest hint of a sadness so great it could destroy the world."
    "I can’t wait to ruin her day."

    scene mayabday1
    with dissolve2

    m "Good morning."
    s "Good morning."

    "I’ve seen this before."
    "A slender girl in summer clothes, kneeling at my bedside- staring at me as I slowly return to the world."
    "Not breaking eye contact despite how much she may want to. Not climbing into the bed despite how much I may want her to."
    "She probably would under the right circumstances, but my arms are far too weak to grasp at them and I’m far too tired to find them anyway."

    m "I believe you’re supposed to say something to me right now."
    s "I’ll take my eggs over medium. Thank you."
    m "Something more celebratory."
    s "Happy anniversary, Maya. Here’s to a million more years or however long you’ve been wandering around inside of the bubble."

    scene mayabday2
    with dissolve

    m "Close enough, I guess."
    s "A smile this early? Are you sure it isn’t {i}my{/i} birthday instead of yours?"
    m "So you {i}did{/i} remember and were just electing to not say anything. I’m not surprised at all."
    m "Fair warning, I might smile at several points throughout the day. You can stare in silence, but please don’t draw attention to any of them."
    m "It will make it harder to convince myself I’m not having any fun."
    s "Don’t worry. I’ll just keep track of them all mentally and provide you with a final tally at the end."

    "Smile Count: 1"

    m "It’s going to be hard keeping track of anything if you don’t summon what little willpower you have inside of that body and get out of bed."
    s "Ten more minutes. You can climb in too if you want."
    m "I seem to have forgotten my pajamas."
    s "Borrow Ami’s."

    "Wait. Ami."

    s "Does-"
    m "She’s at work and doesn’t know I’m here. Don’t worry."
    m "Additionally, I may have eaten the breakfast she prepared for you in lieu of the birthday present you didn’t get me. "
    s "That’s because {i}I{/i} am the present."

    scene mayabday3
    with dissolve

    m "I wonder if there are any pawn shops open today that will accept a trade-in?"
    s "Hey. You’re the one who asked for this. "

    scene mayabday4
    with dissolve

    m "That’s right."
    m "Don’t make me regret it."

    "Smile Count: 2"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mayabday5
    with dissolve

    m "..."
    s "..."
    s "What?"
    m "You know, out of all of the iterations of you that I have seen in the past, I can’t say that any of them have ever gone furniture shopping."
    s "I didn’t buy this. Someone made it for me."
    m "You tricked someone into liking you so much that they handcrafted you a wardrobe?"
    s "I feel like the lengths you have gone to for me are much greater than a few planks nailed together."

    scene mayabday6
    with dissolve

    m "Yes, well...don’t be expecting a new coffee table from me anytime soon. "
    s "So is this just how we’re going to spend the first half of your birthday? Walking around my room and commenting on all of my things?"
    m "It’s been a while since I’ve actually looked around in here. I want to see how much has changed."
    s "That’s right. You must have spent a lot of time in here during our long history of you not being in love with me."

    scene mayabday7
    with dissolve

    m "Will that wardrobe fit a human body? Because I’m seriously considering crawling inside of it and dying right now."
    s "It will fit Uta and she has significantly more...{i}width{/i} than you."
    m "I take it her {i}width{/i} has been in there quite a few times by now, then?"
    s "Yes, but I was only there for one of them."
    m "You never cease to disgust me."
    s "I think that’s on you this time because I really have not done anything unsavory involving this closet."
    m "What a world we live in where you feel obligated to confirm to me the household objects you have {i}not{/i} desecrated."

    scene mayabday8
    with dissolve

    m "Now, please excuse me while I begin rifling through more of them."

    scene black
    with dissolve2

    "Maya paces around the room, inspecting a bunch of things and probably trying to find a new hiding spot for whatever fake journal she plants in here next."

    if bonus == True:
        "She even goes as far as checking under the bed to see if I’ve been hiding any porn under there. Thankfully, I’m smart enough to-"
    else:
        "She even goes as far as checking under the bed to see if I’ve been hiding my Pokemon cards under there. Thankfully, I’m smart enough to-"

    m "I assume you’re still keeping your stash under the mattress then?"
    s "Damn it."

    "Maya removes a small stack of {i}research material{/i} from underneath my mattress and begins to flip through everything, entirely unfazed by the matter."

    if bonus == True:
        m "I’m surprised Ami hasn’t found them yet. I can’t imagine she’d be very happy about-"
        m "Wait. What’s that?"
        s "What’s what? Because I haven’t looked at {i}all{/i} of those magazines yet, and if there’s anything in there that’s weird-"
        m "Not the magazines. What are those notes hanging up near your door?"
    else:
        m "Wow. Is that a holographic Charizard?"
        s "Please be careful with that. It is very expensive."

    "Maya shoves my {i}research material{/i} back underneath my mattress and makes her way over to the door..."

    scene mayabday9
    with dissolve

    m "..."
    s "..."
    m "How long have these been here, exactly?"
    s "I’m not sure. I don’t ever really touch anything on that wall."
    m "Who wrote this note?"
    s "The one about the password or whatever? I’m not really sure."
    m "Because it sounds like something I would say. And it’s signed by an MM."
    m "But I don’t recall ever writing this. And I know your password. It’s Boobies123."
    s "That it is, Maya. That it is."
    s "Anyway, is it possible that you just forgot you put this there? "
    m "It is {i}highly{/i} unlikely. Remembering is kind of my thing."
    s "I thought watermelons were your thing?"
    m "I have multiple things. I’m an incredibly complex girl."
    s "Sure are. I can’t say anyone else I know has ever messed with my...wall thing like this."
    m "I..."
    m "Wouldn’t be so sure of that."

    scene black
    with dissolve2

    m "I’m going to leave another note here. Don’t touch it."
    s "I already told you that I don’t really mess with that wall."
    m "Then continue not messing with it."

    "Maya grabs a sheet of paper and a pen off of my desk, scribbling something down before sticking it to the board along with all of the other apparent non-Maya notes."
    "After that, she immediately proceeds to exit the room without saying anything, so I guess the two of us are done hanging out in here for now."

    scene mayabday10
    with dissolve2

    "It’s still a little early for any sort of festival to start, so I’m not really sure how Maya intends to kill the next several hours."
    "Or why she showed up even half as early as she did."
    "But hey, she wanted to spend the day with me. So if she wants the {i}entire{/i} day, so be it."
    "I’m just glad Ami’s not here to see this because I can not imagine her taking it very well."
    "I’m also surprised that no one else asked me to this festival, but I guess my time would be better spent trying to figure out how to survive it with the person I {i}am{/i} paired with."

    s "So...do you actually like festivals, Maya?"

    scene mayabday11
    with dissolve

    m "Me? Of course. Why wouldn’t I?"
    s "I don’t know. Something just feels off about the idea of you liking {i}anything.{/i} All of your interests take me by surprise even when I know they exist."
    m "I think you’re just projecting. I’m a normal [teenage]girl who likes most things that other normal [teenage]girls do."
    m "Also, do you have any idea how much food is going to be at this place? Because it’s a lot."
    m "And despite how “surprising” my interests may be to you, I believe everyone has accepted my love for food."
    s "All I ask is that you don’t count on me winning you any prizes."
    m "Oh, that’s fine. I already know you don’t possess the ability to win at any sort of festival game. My expectations could be no lower."
    s "Well, now I just feel compelled to prove you wrong."

    scene mayabday12
    with dissolve

    m "Hah...you don’t have to do anything like that."
    m "I just want a normal day. I don’t get many of those."
    m "I want to eat. Walk around. Talk about things you’re not interested in and have you pretend that you are."
    m "But, most importantly-"

    scene mayabday13
    with dissolve

    m "I want to be the cutest girl at the entire festival."
    s "..."
    m "..."
    m "What?"
    s "Is that real? Is that what you actually want?"
    m "It’s less what I {i}want{/i} and more...me looking forward to experiencing it."
    m "There’s something rather liberating about being the envy of everyone when you can’t get in trouble for it."
    s "Well, I can definitely relate to that."
    m "No. That’s-"

    scene mayabday14
    with dissolve

    m "Wait. Ew. No. You {i}can{/i} relate to that. "
    m "Ugh. I think I’m going to be sick. Why did you let me say that?"
    s "Probably because, and this may upset you, so brace yourself- I can’t predict the future."

    scene mayabday15
    with dissolve

    m "Hah...the future. Right. I guess we should just talk about that now, then. So we don’t have to spoil the festival itself."
    s "Oh man. Is this one of your famous pre-reset lectures?"

    scene mayabday16
    with dissolve

    m "I’m going to ask you something right now, and I am going to be very direct about it."
    m "All you have to do is answer yes or no."
    s "I will do my best."
    m "Then-"

    if bonus == True:
        m "Is there {i}any{/i} way {i}at all{/i} that Ayane is pregnant?"
        m "Or any of the girls you’ve been sleeping with."
    else:
        m "Is there {i}any{/i} way {i}at all{/i} that Ayane is hugnant?"
        s "Hugnant?"
        m "It is when you are pregnant with happiness. It happens after unprotected hugging."

    s "Uhh..."
    m "Yes or no."
    s "It’s complicated."

    if bonus == True:
        m "It’s really not. You {i}do{/i} know how babies are made, correct?"
        s "No. Do you think you could show me?"

    m "I’m being serious right now."
    s "I get that. This is just a pretty random thing to be serious about."

    scene mayabday17
    with dissolve

    m "No. A “random” thing to be serious about would be polar bears or pogo sticks. This is a topic with direct relevance that, and I’m not kidding here, could screw {i}everything{/i} up."
    s "I don’t-"
    m "Let me ask you a question. Why do {i}you{/i} think Ayane made it to the roof last time? A feat that no one else has ever accomplished before. Why her?"
    s "That’s-"

    scene mayabday18
    with dissolve

    m "Too slow- I’ll tell you."

    if bonus == True:
        m "Because you two had sex and she got pregnant. Which means she was carrying {i}your{/i} DNA inside of her. Which means she was a temporary extension of {i}you.{/i}"
    else:
        m "Because you two hugged and she got hugnant. Which means she was carrying {i}your{/i} joy inside of her. Which means she was a temporary extension of {i}you.{/i}"

    m "Do you see where I’m going with this?"

    if bonus == True:
        s "You’re saying that Ayane was only on the roof because she was pregnant with my child...which, no offense, sounds a little ridiculous."
        m "What {i}isn’t{/i} ridiculous about this life we’re living?"
        s "That doesn’t-"
        s "If she were pregnant, what happened? Because she doesn’t look very pregnant anymore."
    else:
        s "But where did the hug goooooooooooooooo????"

    scene mayabday19
    with dissolve

    m "Gone with the reset, I suppose."
    s "What?"
    m "It wasn’t meant to be there, so it was disposed of. "
    m "I told you a long time ago. More than just memories can be altered by the shift in time. Physical attributes can be set back as well."
    m "I believe Ayane was rewritten to be the same exact person, just...without a parasite growing inside of her."
    m "So when I ask you if there is any possibility of it happening again, I need you to answer honestly."
    m "We may have gotten her back last time, but there’s no telling if it would work out that way again."

    if bonus == True:
        m "So before you go thinking about how awesome it would be to mate with your entire classroom and never have to worry about having children, consider the price you’d have to pay."
    else:
        m "So before you go thinking about how awesome it would be to hugh your entire classroom and never have to worry about getting anyone hugnant consider the price you’d have to pay."

    m "Potentially, of course."
    m "This, like everything else, is all conjecture."
    m "But when everything is new, conjecture is all we have."
    m "I don’t want anything to go wrong. "
    m "So I need you to start caring about everyone else a little more than you currently do."

    if bonus == True:
        s "You don’t need to beg me to keep me from fathering any children, Maya. I can assure you that is the last thing I want to do."
    else:
        s "Ughhhhhhhhhh can we go already?"

    m "You still haven’t answered the question. Is it-"
    s "Yes."
    s "It’s possible."

    scene mayabday20
    with dissolve

    m "I see."
    s "But I have no idea whether it’s true or not. So you’ll have to confront Ayane yourself if you want to know."
    s "Unless you’d rather just wait until we’re on the roof to find out, because there’s not much we can do at this point."
    m "..."
    s "..."
    m "..."
    s "Are you really sure that’s what it is, though? "
    m "Are you asking because you’re acknowledging the possibility that you may have planted your seed inside of others as well?"
    m "And, if that’s the case- are you confused by how only {i}Ayane{/i} has made it there?"
    m "Because these are things I’ve questioned myself as well. And I don’t know."
    m "I just don’t know."

    scene mayabday21
    with dissolve

    m "But I can’t think of any other reason why it would happen."
    m "And I've tried."
    m "The further we move into uncharted territory, the higher the potential is for risk."
    m "And I’m..."
    s "..."
    m "..."
    m "I’m finally starting to feel something again."
    m "I don’t want that to go away."

    "{i}A moment of silence.{/i}"

    s "Are you scared?"

    "{i}A crack in the glass.{/i}"

    m "Yes."

    "{i}A light in the attic.{/i}"

    scene mayabday22
    with dissolve

    m "Because I think that it might."

    scene black
    with dissolve2

    "{i}A dream of the past.{/i}"

    "The conversation drops dead after Maya’s revelation, but I must be forgiven for getting lost on this particular train of thought when the route-map is tangled up like wires."
    "I don’t want to believe her but, at this point, I feel like I have to- because {i}I{/i} can’t think of any other reason Ayane would have made it up there with us either."
    "The gap we accidentally create in our morning is subsequently filled by a collage of uncomfortable glances and scattered trips to the refrigerator."
    "Nothing is ever inside."
    "At least nothing that either of us want."
    "It ends, though- but I imagine that’s just because Maya wants to forget about this and focus on the rest of the day. "
    "She wants to eat. "
    "She wants to walk around. "
    "She wants to talk about things I’m not interested in and have me pretend that I am."
    "And strangely enough, I want to do all of those right now as well."
    "But we still have a few more hours of sunlight."
    "And many more unsuccessful trips to the refrigerator."

    $ renpy.end_replay()
    $ mayafestival1 = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Two hours pass.{/i}"
    "{i}Maya changes into her yukata in the comfort of her best friend’s bedroom.{/i}"
    "{i}She looks beautiful.{/i}"

    scene mayabday23
    with dissolve2

    "Smile Count: 3"

    s "Welp...it will definitely be hard for anyone to take you down in your pursuit of being the cutest girl at the festival."
    m "For today and today only, I’ll allow you to say that as many times as you want without fear of being insulted."
    s "It might be good to turn the cockiness down a little, though. Even if it is well warranted."
    m "It’s my birthday. I can be as cocky as I want."
    m "Now, let’s get out of here before Ami comes home. I’m hungry and don’t want to deal with her today."

    scene black
    with dissolve2

    s "Well, thank you for making the time for me..."

    "........."
    "......"
    "..."

    jump mayafestival2

label mayafestival2:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label saturdaymorning:

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if ((totaldays >= 220) and (day220 == False) and (chap1point >= 90) and (happypoint >= 10 or (happypoint + happymiss == 10)) and (chikapoint >= 13) and
        (yumipoint >= 12) and (ayanepoint >= 18 or (ayanepoint + ayanemiss == 18)) and (sanapoint >= 14) and (makotopoint >= 16) and (mikupoint >= 13) and
        (rinpoint >= 16 or (rinpoint + rinmiss == 16)) and (futabapoint >= 19 or (futabapoint + futabamiss == 19)) and (amipoint >= 14 or (amipoint + amimiss == 16)) and
        (mayapoint >= 12) and (mollypoint >= 6) and (tsuneyopoint >= 6) and (sarapoint >= 5 or (sarapoint + saramiss == 5)) and
        (harukapoint >= 6 or (harukapoint + harukamiss == 6)) and (karinpoint >= 3) and (kirinpoint >= 3) and (kaoripoint >= 3) and (makipoint >= 2) and (chinamipoint >= 2) and (day == 6)):
            jump day220
    if day == 6 and totaldays >= 370 and day355 == True and karindate20 == True and chinamidate20 == True and utadorm20 == True and sanadorm50 == True and osakodojo1 == True and kirindate25 == True and secondbeach1 == False:
        jump secondbeach1
    if totaldays >= 464 and christmastwo20 == True and day == 6 and mayafestival1 == False:
        jump mayafestival1
...
```