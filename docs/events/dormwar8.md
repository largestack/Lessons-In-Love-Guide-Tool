# Chaperone (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Ruthless Rhyme Rhomp! Rap Rampage!](./dormwar7.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar8
* Group: Main
* Triggered by label: dormwar7
* Chain sources: dormwar7
* Chain sources path: dormwar7

## Official wiki page

[Chaperone](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar8&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar8:
    scene warhotelarrival1
    with dissolve
    play music "shiningstarinstrumental.mp3"

    "Myself and the rest of the girls who were present at the maid cafe show up at the hotel to find three of the people who {i}weren’t{/i} waiting around in the lobby."
    "We proceed to make fun of them for being antisocial, rap hating buzzkills and then take their lunch money to go buy cigarettes and other cool kid stuff."
    "Just kidding. "
    "We do approach them, though."
    "Well, {i}I{/i} approach them."
    "The rest of the girls hurry into an elevator and pile up inside of it, probably breaking some sort of occupant capacity rule in the process."
    "The elevator breaks and everyone dies, making the second floor victorious by default because they have more people left alive."
    "Just kidding again."
    "I don’t know why, but I am feeling particularly ferocious right now."

    to "Oh, good. You’re here."
    to "Please make yourself useful and carry the rest of my luggage upstairs when you have a moment."
    s "No. "
    to "But...how will it get up the stairs if-"
    s "Why even bring luggage? Aren’t we only going to be here for one night?"
    mak "Two, actually."
    mak "We'll be staying over on Sunday as well since there is no[school] on Monday."
    mak "I tried to tell Touka to pack lightly due to how many people we'd have coming, but her mother apparently wouldn’t let her stay at the hotel unless she packed literally everything ever."
    s "The hell is she going to do with five bags over the course of two nights?"
    n "Should we really be judging Touka’s mom for her weird hotel standards when she’s the one paying for the place?"
    s "Probably not. But I can’t help but say I’m a little surprised she was okay with you coming here since I'm the only “chaperone.”"

    scene warhotelarrival3
    with dissolve

    to "She would have been okay with it regardless of whether a chaperone was present or not."
    to "This hotel is just one of many that falls under the umbrella my family holds over Kumon-mi’s hospitality industry, so we’re not put out at all by the three rooms we’re taking up tonight."
    to "Granted, we wouldn’t be put out at all even if we had to rent them out, but that is beside the point."
    s "Yes, you are very rich. We know."
    mak "Noriko and I will help you carry your things since Sensei is too “busy” to be bothered with such a difficult, labor intensive undertaking. "
    s "I can always count on you, Makoto."
    s "So, why the third room?"

    scene warhotelarrival4
    with dissolve

    to "Well, surely you didn’t expect all twenty of us girls to fit into one, did you?"
    s "No, but I did expect one of me to fit into either of the ones that you guys are sleeping in."
    to "That seems entirely inappropriate and I would very much appreciate you sleeping elsewhere."

    if bonus == True:
        s "Do you not remember the grand prize of this dorm war, Touka?"
    else:
        s "I agree, but as the prize of this competition, I don't believe my choice matters much."

    to "There is a prize? What is the prize?"

    scene warhotelarrival5
    with dissolve

    n "The winning floor gets to keep Sensei in their room during our trip to the beach."
    to "And...that’s a thing people actually {i}want{/i} to compete over?"
    s "Would you be more interested in competing over me if I helped carry your bags?"

    scene warhotelarrival6
    with dissolve

    to "Yes, actually. You’ve done nothing that would make me want to sleep in the same room as you thus far."
    to "In fact, the only sleep-related experience I have with you involves you making fun of my completely normal, circular bed."
    n "I volunteer to stay in Sensei’s room and-"
    mak "No."
    n "Then I would like to suggest that Sensei sleeps with the second floor girls and-"
    mak "No."
    s "Thank you for trying, Noriko. But Makoto wouldn’t let something like that happen on her watch."
    n "I’m sure she’d be fine with it if it was just you two in a room and not {i}me{/i} with you instead."

    scene warhotelarrival7
    with dissolve

    mak "I’ve essentially been Sensei’s personal secretary for as long as I’ve known him. The two of us staying in one room would be nothing short of professional."

    scene nightskysepia
    with dissolve

    "I faintly recall a time just like that in the recent past."
    "The wind was cold, the skies were bright-"
    "But alas, those times were fleeting."

    if bonus == True:
        "Just like condoms in the sand..."

    scene warhotelarrival7
    with dissolve

    mak "If it were {i}you{/i}, though..."
    n "…"
    n "What, Makoto?"
    n "Tell me what would happen if it were me."

    if bonus == True:
        n "I’ve had plenty of sleepovers with Sensei in the past and we’ve never done anything weird."
        mak "And how many of those sleepovers began with you giving him a sedative?"
    else:
        n "I’ve had plenty of sleepovers with Sensei in the past when we were neighbors and stuff."
        mak "And how many of those sleepovers began with you giving him a sleeping potion?"
        n "Only like...nine."

    to "I am very lost right now."
    s "As you should be. But hey, at least you’re being included in something."

    scene warhotelarrival8
    with dissolve

    n "Have you been feeling a little left out cause of how new you are or something?"
    to "Well...I’d be lying if I said I didn’t think being new was at least part of it. But it is nice getting to be around all of you in a more...casual setting."
    to "I just hope that whatever transpires tomorrow doesn’t become yet another obstacle in currying favor with all of you."
    s "What does that mean?"
    s "What’s Touka’s competition supposed to be?"
    mak "Deadly. Now, please retire to your room for the night so that we may all-"
    s "Nah. I’m going to go say hi to everyone in both of the rooms."
    mak "There is really no need for you to-"

    scene warhotelarrival9
    with dissolve

    n "We’re in Room 24, the first floor girls are in Room 25, and you’re in-"
    s "Room 23?"
    n "No. You’re down the hall in Room 44. I can see why you would have guessed that, though."
    s "Oh."
    s "Well, okay then."

    scene black
    with dissolve

    "I grab one of Touka’s bags to bring upstairs because manual labor is my middle name and start to head over to the elevator."

    to "Wait, Sensei. You’re forgetting these-"
    s "Good luck being a normal girl, Touka."
    s "And Noriko."
    s "And Makoto."
    s "Actually, you’re all pretty weird."
    s "Anyway, see you tomorrow."

    "I ride the elevator up to the second floor."
    "I could have probably just taken the stairs, but...it would have been really hard on account of this entire...single bag that I have."
    "Sidenote: I hope Ami was smart enough to pack literally anything for me, because I don’t even have my phone charger right now."
    "………"
    "……"
    "…"

    scene warhotelarrival10
    with dissolve

    c "Oh, hey! Look who it is!"

    "I drop Touka’s bag at the door because I get tired of carrying it and figure this is close enough."

    s "Hey. This is certainly an interesting combination of girls."
    c "Sana and I were just talking about her thing tomorrow."
    c "I was offering to help her with her hair, but it seems like she doesn’t really want to do anything special with it."
    s "So...Sana’s competition involves hair in some way?"

    scene warhotelarrival11
    with dissolve

    sa "I’m...sorry in advance for...disappointing you..."
    c "Oh, stop. You’re being too hard on yourself. You know we all think you’re adorable, right?"
    sa "Not...really."
    sa "I don’t really talk to most of you...so...there would be no way for me to...yeah."
    s "So...what is this contest exactly?"
    sa "A...nightmare."

    scene warhotelarrival12
    with dissolve

    c "I still don’t know if we’re allowed to tell you beforehand, but we’ve all kinda made an unspoken agreement to just...not say anything, I guess?"
    c "So you’ll just find out tomorrow."
    c "But if you vote for Sana, it would make me reaaaaaally happy~"
    s "And how would {i}you{/i} feel, Sana?"
    sa "Uhh...embarrassed?"
    s "That is not a winning attitude, [young]lady."

    scene warhotelarrival13
    with dissolve

    sa "I...I know that! But...I..."
    sa "I kind of...don’t want you to see me like that, so..."
    c "Hey! You’ll do great! Just keep your chin up."
    c "At least you’re actually {i}trying{/i}, unlike a certain roommate of mine."
    c "All Yumi has to do to beat Io is just...cooperate."
    c "Should be the easiest point ever, but nope!"
    s "Wait, so...what are those two doing exactly?"
    c "Cooperating. That's the whole contest. Like, literally."
    s "And...you're allowed to tell me about this contest, but not the other ones?"
    c "Yeah, because this one is dumb and barely even a contest at all."

    "Okay, so...I guess I shouldn't really bother thinking about {i}that{/i} matchup just yet..."

    if bonus == True:
        "But, for my own personal reasons, I’m going to imagine Sana's is a nude photo shoot of some sort until proven otherwise."
        "I mean, what else would she be so nervous about when she is a completely functional, highly social member of society?"
        "Do I think that would ever be approved by the council of [teens] that put this contest together? Probably not."
        "But Noriko also almost gave me a handjob in front of two of her classmates this morning, so it’s not {i}impossible{/i} and still matches the context."
        "Nude photo shoot it is."
        "Good luck, Sana."

    scene warhotelarrival14
    with fade

    "I make my way over to Maya next for some reason."

    m "What? Why now? I was about to lay down."
    s "Can I lay with you?"

    if bonus == True:
        m "No. Go away."
    else:
        m "Omg yes please I have waited for so many years."
        s "Just kidding."
        m "Why do you do this to me?"

    m "Also, have you seen Ami anywhere?"
    m "Or...even Ayane, for that matter?"
    m "Not having either one of them here makes me look weird. Like I don’t have any friends or something."
    s "I haven’t. But if you see Ami, can you ask her if she packed anything for me?"
    m "What could {i}you{/i}, of all people, possibly need?"
    s "A phone charger would be nice. Can’t say I expected to be spending tonight in a hotel."

    scene warhotelarrival15
    with dissolve

    m "Well, it’s never too late for you to go home."
    m "You’re essentially a dead opossum walking into a vultures’ nest right now anyway."
    s "You know, you’ve said some strange things before, but that one really sticks out to me for some reason."
    m "Well, think about it. You’re the “prize” of this competition and you’re showing yourself in front of a bunch of people trying to “win” you."
    s "You do realize who you’re talking to, right? That is the ideal situation for me."
    m "Who knows? I barely understand anything anymore."
    m "I’m just trying to have some fun before the next reset plunges Kumon-mi into the ocean or something and everything gets even weirder than it already is."
    s "Oooh, reset talk. Is it getting to be that time already?"

    scene warhotelarrival16
    with dissolve

    m "Why do you sound excited about that?"
    s "Because it means I get to spend more quality time watching the stars with my favorite shrine maiden."
    m "…"
    m "Can you just go find Ami, please?"
    s "I’ll tell her you’re looking for her if I see her."
    m "Thank you."
    m "Also, just a word of advice, you should probably lock your door tonight."
    s "Worried that Noriko is going to come get me?"

    scene warhotelarrival17
    with dissolve

    m "Why would I ever worry about you?"
    s "You’ve actually been worrying about me a lot lately, haven’t you?"
    m "Please leave. I don’t want to do this in a room full of people who I already need to constantly remind of how much I despise you."
    s "Okay, fine. But only because you asked so politely."
    m "Thank you. And goodnight."

    scene black
    with dissolve

    "I quickly greet the rest of the girls in the room (Except for Yumi, who won’t even look at me) and make my way back into the hall."
    "I notice Makoto coming back as I do and she informs me that she’ll be going back to the dorm to hang out with Miku instead of staying here with everyone else tonight."
    "She also hands me the key that I forgot to take after meeting her in the lobby and then quickly disappears into her room to, presumably, pack her things and head home."
    "Of course, I use that opportunity to sneak into the room of her enemy and see how they’re doing."
    "………"
    "……"
    "…"

    scene warhotelarrival18
    with dissolve

    no "At long last, the main course has arrived."

    if bonus == True:
        s "Yes, that is me. Food."
    else:
        s "Yes, I have your delivery right here."

        "I hand several bags of food to Nodoka and ask her to rate me five stars on Doordash."

    s "I’m a little surprised to find you awake, Nodoka. I thought you came back to the hotel after your contest to take a nap or whatever."
    no "Yes, yes. Accessing the part of my brain with all the fancy words can be quite exhausting."

    if bonus == True:
        no "But I’ll have you know that I got a full forty five minutes of sleep and am now ready to suggestively rub up against everyone in this room because “we’re just girls and no one will care.”"
    else:
        no "But I’ll have you know that I got a full forty five minutes of sleep and am now ready to count all of my hair."

    no "Would you like to join me, Sensei?"
    s "I would like nothing more, Nodoka."
    o "…"
    o "Are you two secretly related or something?"
    no "God I wish."

    if bonus == True:
        no "Growing up alone was rather depressing at times."

    s "So, how does it feel knowing that yours is the only dorm room with two winners right now?"
    o "I mean...pretty normal, I guess."
    o "We both wound up in contests that like, perfectly play to our strengths, so I kind of expected this to happen."
    s "It’s really depressing that your strength is not liking me."
    o "Depressing for you, maybe."

    if bonus == True:
        o "And I don’t {i}not{/i} like you. I just look at you as a...creepy adult male teacher."
        no "If it is any consolation, Sensei, those reasons are precisely {i}why{/i} I like you."
    else:
        o "And I don’t {i}not{/i} like you. I hate you. It's different."
        no "Otoha is just jealous because she keeps losing count of her hair and we don't."

    s "How are you two even friends?"

    scene warhotelarrival19
    with dissolve

    o "That’s a good question. How {i}are{/i} we friends? Like, when did that even happen?"
    no "Love works in mysterious ways, Otoha."
    no "Perhaps we’re simply drawn to each other like magnets?"
    no "Or perhaps, like a praying mantis, your pheromones have lured me to you and you’re just days away from biting my head off and feasting on my body?"

    scene warhotelarrival20
    with dissolve

    o "Yeah, so I have no idea."
    o "But I do know that Noriko’s been looking for you."
    s "Noriko? I just saw her downstairs."
    o "Well she’s in the bedroom now and she’s looking for you again."
    s "I guess that makes sense. She tends to search for me a lot."
    o "You two aren’t, like...you know."

    if bonus == True:
        s "Fucking each other?"
    else:
        s "Astronauts?"

    scene warhotelarrival21
    with dissolve

    o "Dude."
    s "What? That’s what you were getting at, wasn’t it?"
    no "Hi. I’m back and my interest is piqued."

    if bonus == True:
        no "I’m also very upset about missing this morning’s imouto contest after hearing how close things came to getting {i}really{/i} exciting."
        s "You should volunteer for that one in the next dorm war, Nodoka. I feel like you’d be a good little sister."
    else:
        no "Space exploration always gets me excited."
        s "I think you'd be a good astronaut, Nodoka."

    no "Oh, I’d be {i}very{/i} good."
    o "Okaaaaaaay, well I’m gonna go scour the halls for a vending machine or something."
    to "Oh! I..."
    to "Can I...come with you?"

    scene warhotelarrival22
    with dissolve

    o "Oh, uhh...sure? If you want."
    no "Until we meet again, Sensei. Until we meet again."
    to "Wait, Sensei is here? Sensei, where did you put my-"

    scene black
    with dissolve

    to "Oh. Okay...I can just...go find it."

    "………"
    "……"
    "…"

    scene warhotelarrival23
    with dissolve

    n "Ah! Onii-chan!"
    u "Onii-chan! Welcome home!"
    t "Onii...chan..."
    t "An older brother sounds nice."
    u "Come here to spend some time with the future winners of the first dorm war?"
    s "At this rate, it’s definitely possible. Your team has taken the last three rounds."

    scene warhotelarrival24
    with dissolve

    u "Of course we have. We’re a force to be reckoned with."
    u "Just wait until tomorrow when we {i}really{/i} start getting this competition locked down."
    n "That’s right!"

    if imoutoami == True:
        n "I may have dropped us the first round due to some of my tactics being a little...unusual, but I know the rest of the second floor girls can make up for me!"
    else:
        n "And with me winning the imouto contest, our lead is so big that it’s basically impossible for the other floor to catch up!"

        if bonus == True:
            n "Thank god for sedatives, right?!"
            s "No. I already told you that was bad. Don’t do that again."
        else:
            n "Thank god for potions, right?!"
            s "No. I already told you that was bad. Don’t do that again."

    u "So, Sensei! Since you’re here, that must mean you’re joining our slumber party, right?"

    if bonus == True:
        s "Will someone show up to kick me out if I say yes?"
        u "From this floor? Doubt it."
        u "But if you decide to take your pants off, remember that you aren’t allowed to touch me!"
        u "I might be off duty right now, but Uta-chan’s morals and limitations carry over to coed slumber parties as well!"
        n "You may touch me as much as you like, wherever you like!"
        s "You’re not going to get nervous again?"
        n "I’m nervous just thinking about it!"
        t "Touch me and you die."
        s "I know, Tsuneyo. You don’t have to worry about that."
    else:
        s "Yes. But only because I haven't figured out a way to escape."

    "{i}Yet...{/i}"

    scene warhotelarrival25
    with dissolve

    u "Tsunecchi, you can get a little closer, you know? You don’t have to sit all the way back there like some kind of loner."
    u "Like, I’m all up in Noriko’s bubble right now and she’s totally fine with it."

    if bonus == True:
        n "I bet Sensei would like it, too. Wouldn’t you, Sensei?"
        s "It is becoming more dangerous for me to remain standing up with each passing second."

    t "I’m afraid I can not do that, Green Onion."
    u "Whaaaaat? How come?"
    t "Because you both smell very nice and I would likely attempt to taste you."
    t "I am safer in the background."
    s "Okay, time to sit down."

    if bonus == True:
        "I take a seat at the foot of the bed to conceal Tsuneyo’s (And probably Uta’s?) eyes from being seared by the sight of a growing erection."
        "I’m not worried about Noriko, obviously, since she has already felt it on multiple occasions now."
    else:
        "My legs are so weak. I should try running on the treadmill soon."

    scene warhotelarrival26
    with dissolve

    u "Hey, you haven’t seen Io by any chance, have you?"
    u "We walked back from the rap battle together, but she disappeared the second she realized there were people already waiting in our room."
    s "She’s missing as well? That makes three total since Ayane and Ami are MIA too."
    n "Kirin too, I guess. But she’s probably just out for a walk or something. She does that a lot."
    n "I’m sure they’ll all find their way back soon enough."
    s "Maybe Io just went back to the dorm or something? That seems like an Io thing to do."

    scene warhotelarrival27
    with dissolve

    u "Not without telling me, but...I guess I’ve kinda been on her case all day."
    u "She’s kinda like a pet snake that doesn’t like being handled or something."
    u "Give her too much attention and it’ll just make her mad. Then, next thing you know, you’ve gotta have someone suck the venom out of your wound and it becomes a whole thing."

    scene warhotelarrival28
    with dissolve

    t "Snake venom..."
    t "I still need to try that...and now I know where to get some."
    s "Tsuneyo, didn’t we decide that snake venom ramen was a bad idea?"
    t "Fuck you in the rude way and not the literal way that I have now discovered the meaning of."
    u "Io doesn’t have real venom, Tsunecchi. She’s a human girl, just like you and me."
    t "What does it mean to be human, Green Onion?"
    t "{i}What does it mean to be?...{/i}"
    s "…"
    s "Okay, well I’m probably going to head over to my room now."
    s "Today was exhausting enough and if I am going to continue to be a completely unbiased and awesome judge, I need to get some rest."

    scene warhotelarrival29
    with dissolve

    u "Good call, Sensei! Just keep doin’ what you’re doin’ since my girls are in the lead!"
    u "And hey, even if you do wanna be a {i}little{/i} biased, that’s okay. Just make sure it’s second floor bias and not first floor bias. You know?"
    n "Goodnight, Sensei."

    if bonus == True:
        n "I’d offer to come hang out in your room with you, but I should probably give you some space on account of that whole drug thing, shouldn’t I?"
        s "Probably. I still have to figure out how I feel about that."
        n "Wanna just drug me next and make it an eye for an eye?"
        s "I would much prefer you to be conscious during our time together."
        n "Are you suuuuuuure?"
        s "…"
        s "{i}Yes?{/i}"
        t "Perhaps if the venom was cut with something citric like...lemon?"

    scene black
    with dissolve2
    stop music fadeout 30.0

    "I exit the room of the second floor girls and follow the signs in the hall directing me toward my room."
    "I’m not sure why mine has to be on the opposite end of the hotel, but I guess things will be a lot quieter that way."
    "The girls were loud enough in both of their rooms that it was easy to hear what was going on in the other one through the walls."
    "But I guess it was like that at the inn I went to with Chika as well and that was also owned by the Tsukiokas."
    "Maybe cutting corners on thinner walls is just something they do to save money or something?"
    "Who knows? I’m no rich person or financial genius."

    scene warhotelarrival30
    with dissolve
    play sound "dooropen.mp3"

    "But I {i}will{/i} graciously accept and benefit from their kindness or naivete."
    "I’d never be able to afford three separate hotel rooms on my teacher’s salary."
    "And it’s not like I can really ask for a raise either since I’m...you know."
    "Really bad at my job."
    "But I guess there would be no reason for me to ever go out of my way and get something like this in the first place."
    "This is fun."
    "It is."
    "But it’s not something a normal class would do."
    "And it’s probably not something I should be letting them do."
    "But who cares?"
    "Their lives belong to them and them only."
    "And in letting them realize that, they’ve centered themselves around me."
    "Each one of them is a celestial body orbiting around my existence."
    "I am the center of the solar system."
    "I will take."
    "And I will take."
    "And I will take."
    "And I will grow."
    "If life is nothing but a strange string of coincidences and being in places at the right time, I will be everywhere at once so that nothing is coincidental at all."
    "Time is unlimited."
    "Until it’s not."
    "But, right now-"
    "It is."

    if ayanelust10 == True and ayane_lust >= 15 and kirin_lust >= 15:
        "Which makes moments like this okay."

        $ renpy.end_replay()
        $ dormwar8 = True
        jump ayanelust15
    else:
        scene black

        "And since time is unlimited, no one will mind if I sleep."
        "I get on the bed and close my eyes."
        "But I can still hear the girls from all the way down the hall."
        "…"
        "They sound happy."
        "………"
        "……"
        "…"

        $ renpy.end_replay()
        $ dormwar8 = True
        jump dormwar9

label dormwar9:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
ay "And? What are you getting at?"
        ki "Hmm..."
        ki "Come here."
        ay "I don’t-"
        ki "Fine, I’ll just whisper it into your ear then."

        scene rapbattle32
        with dissolve

        ki "…"
        ay "…"

        "…"
        "…"
        "…"

        scene rapbattle33
        with dissolve2

        ay "…"
        ay "Are you kidding?"
        ay "Is this a joke?"

        scene rapbattle34
        with dissolve

        ki "Come on~ I think it sounds fun."
        ki "Just the once and I won’t bother you about it anymore."
        ay "That’s what you said last time."
        ki "I know, I know, but...well, you know how hormones work and all that."
        ki "Anyway, I’ll come pick you up when I’m ready. Sound good?"
        ay "Why are you doing this to me?"

        if bonus == True:
            ki "Cause I’m horny. Duh. "
        else:
            ki "Cause it's boring with only two players. Duh. "

        ki "Anyway, nice talking to you. And good job with your rapping and stuff."
        ki "See you tonight, Ayane."

        scene black
        with dissolve2

        "Welp, I guess that about wraps it up for the first day of competitions."
        "I have no idea what tomorrow is going to bring, but if it’s even a fraction as...exciting as it was today, I am going to have to call out of work on Monday to recuperate."
        "We all finish cleaning up the maid cafe within thirty minutes or so and then make our way through the cold of the night to the hotel..."

        $ renpy.end_replay()
        $ dorm2warpoints += 1
        $ dormwar7 = True
        stop music fadeout 5.0

        "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
        "………"
        "……"
        "…"

        jump dormwar8

    else:
        scene rapbattle29
        with dissolve

        ay "So, now that the final competition is over, should we start heading over to the hotel to meet up with the rest of the girls?"

        if bonus == True:
            u "Wanna come sleep in our room to celebrate my victory, Sensei?"
            ay "Ooooooor, you could come sleep in {i}our{/i} room to reward me for my generous concession. "
            u "But Ayane, what would people think after my totally serious virginity comment? "
            ay "Perhaps being under the supervision of nine other girls will be enough to dispel any rumors?"
            ay "Or, if Sensei wants to just give up on his career and be with me and me only for forever starting right now, it would also be a good time."
            s "Or, alternatively, the three of us could get our own room and celebrate by-"
            u "Nope!"
            ay "…"
            s "…"
            ay "I mean...{i}I{/i} didn’t say no..."
        else:
            s "Yes. I see no need for additional dialogue here."

        scene black
        with dissolve2

        "Everyone (Except me) works together to clean up the maid cafe and, within the next twenty minutes or so, we begin our journey to the hotel."
        "Thankfully, it isn’t {i}that{/i} far from where we are now, so the walk doesn’t take that long."
        "But anyway, I guess that wraps it up for the first day of competitions."
        "I have no idea what tomorrow is going to bring, but if it’s even a fraction as...exciting as it was today, I am going to have to call out of work on Monday to recuperate."

        $ renpy.end_replay()
        $ dorm2warpoints += 1
        $ ayanelust15skip = True
        $ dormwar7 = True
        stop music fadeout 5.0

        "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
        "………"
        "……"
        "…"

        jump dormwar8
...
```