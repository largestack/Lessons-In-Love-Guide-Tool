# Debatably Bisexual Musicians
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe45&go=Go)



## Event preconditions
✅Rin love greater than or equal to 45

✅Event "[Rin: Semantics](./rindorm40.md)" is completed (event=rindorm40)



## Next events
None

## Event properties
* ID: cafe45
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe

## Event code
File: \game\RinEvents.rpy
Code:
```python
...
label cafe45:
    scene rindate1
    with dissolve
    play music "cafe.mp3"

    "I arrive at the cafe bright and early to find someone who is definitely not Rin hanging out behind the counter."
    "I check my phone to make sure that I didn’t somehow oversleep and wander in at night instead, but I quickly realize that even {i}that{/i} wouldn’t explain the sunlight."
    "So, why is Molly here?"
    "And why are her eyes closed?"
    "What is the meaning of this?"

    s "Molly."
    h "Shh...She’s sleeping."
    s "Yes, Haruka. I have eyes. I can see that."
    h "Well, it didn’t stop you from talking to her, soooo..."
    s "Because she’s supposed to be {i}working{/i}. As the owner, you should know this."
    h "All I know is that I’d be asleep too if I had to go from night shift to morning shift so suddenly."

    "I start snapping my fingers, hoping that Molly will react in some sort of way."

    mo "…"

    "As you can see, she doesn’t."
    "So perhaps it’s time for me to try something different?"

    s "…"
    mo "…"
    s "Anime is stupid."

    scene rindate2
    with hpunch

    mo "Hah?! Wha?"
    mo "Where am I? What’s going on?!"

    scene rindate3
    with dissolve

    mo "Wait...this world looks almost exactly like the cafe..."
    mo "But it’s so bright...so it can’t be the {i}real{/i} cafe."
    mo "There’s even a Haruka clone sitting at the counter."
    h "Not a clone. Morning, Molly."
    mo "And she speaks our language as well..."
    mo "This can't be...Earth...can it?"
    s "{i}Ahem.{/i}"

    scene rindate4
    with dissolve

    mo "Ah! Now there's a Sensei clone!"

    if bonus == True:
        mo "Three more and I can finally make my greatest fantasy come true!"
    else:
        mo "I thought I was the only one who possessed one of those!"

    s "...Excuse me?"
    mo "Don’t worry about it!"
    s "No, now I’m genuinely curious."
    h "Same. Do tell, Molly."

    scene rindate5
    with dissolve

    mo "So, ummm..."
    mo "I take it I was just sleeping on the job and I...haven’t been teleported into a nearly identical isekai?"
    s "Correct. But why are you working so early? You’re a night person."

    scene rindate6
    with dissolve

    mo "Ask Nithhala. She’s the one who went and scheduled her stupid date for today."
    mo "Now I’ve gotta be the one to help all the morning people."
    mo "Do you have any idea how low my mana is right now? "
    s "Not a clue. "

    "Huh. I knew Rin had a “date” with Otoha coming up, but I didn’t realize it was today."
    "I wonder if she’s still planning on taking her to that arcade thing?"

    s "I’m sorry you have to cover her shift, Molly. But just think of all the extra money you’ll have to spend on..."
    mo "…"
    s "…"
    mo "Spend on what? I want to hear your guess."
    s "Dragon...stuff?"

    scene rindate7
    with dissolve

    mo "Hohohoho...an excellent guess, Sir. But you’ll have to be a bit more specific about what type of dragon if you’re really going to excite me."
    s "Your eyes are on fire, though."
    mo "And so is my heart..."
    h "Umm, sorry to bother you two while you’re...bonding or whatever, but look who just came in."
    s "Hm?"

    scene rindate8
    with fade

    "I turn around to find Rin standing there, decked out in her winter garb and looking up at me with a smile on her face."

    s "Oh, hey."
    s "Aren’t you supposed to be meeting Otoha this morning?"
    s "Molly just told me that was supposed to be today."
    r "I got ditched."
    s "Oh..."
    mo "Rin..."

    scene rindate9
    with dissolve

    r "Yeah, yeah. I know how it sounds. That’s really not what happened, though."

    if bonus == True:
        r "Otoha’s parents are just really strict and they don’t want her going out today since she’s been struggling with her homeschool stuff."
    else:
        r "Otoha’s parents are just really large and she couldn't get around them in time."

    mo "I depleted my mana for nothing?! "
    mo "Rin, open me a portal to Dalaran! Drop a mage table! Do something!"

    scene rindate10
    with dissolve

    r "Do you hear something, Sensei? I thought I heard Molly but I’m pretty sure she only works nights."
    s "I haven’t heard anything all morning."
    mo "I’ll...I’ll use thaumaturgy to make my voice three times louder!"
    mo "RIN! PORTAL!"
    r "There it is again. So weird."

    scene rindate11
    with dissolve

    r "Umm...a-anyway!"
    r "Are you...busy today?"
    r "I already took the day off and Futaba is at the library so I’ve kinda got...nothing going on for the next 24 hours."
    s "And you’re absolutely sure Otoha isn’t able to go? I know how much you were looking forward to it."
    r "Yeah...maybe some other time. Definitely not happening today, though."
    r "She had her phone taken away. Pretty sure her mom texted me back or something since her texts started getting abbreviated all weird out of nowhere."
    s "Then sure. I don’t mind at all."
    s "It was a little shocking seeing Molly so early anyway. I don't have the energy to deal with her yet."

    scene rindate12
    with dissolve

    r "Molly?..."
    r "Sensei...Molly died five years ago..."
    mo "Wha-?!"
    mo "I’m...a poltergeist?!"
    mo "This explains so many things!"
    s "I still think about her every day..."

    scene rindate13
    with dissolve

    r "As do I...One never forgets their first kiss, after all."
    h "Uhh, excuse me? You two kissed and I didn’t hear about it?"
    r "Quiet, Haruka. This conversation is not meant for adults."
    h "But...Sensei is..."
    r "Shhhh...everything will be okay."
    h "...What?"

    scene rindate14
    with dissolve

    r "So! Ready to come to a bunch of places you probably won’t enjoy and prevent me from getting all sad and feeling sorry for myself?"
    s "There’s nowhere else I’d rather be."
    r "That’s a lie, but thank you for saying it."
    r "I’d hold your hand but I don’t want you to get arrested and make today even worse."
    s "That works for me."

    scene black
    with dissolve2
    stop music fadeout 10.0

    h "Uhh...have fun?"
    mo "Haruka...can..."
    mo "Can you see me?..."
    h "…"
    mo "…"
    h "Weird...I could have sworn I heard something just now..."
    mo "HARUKA!!!!!!"

    scene rindate15
    with dissolve
    play music "justbehappy.mp3"

    "Rin and I get off the bus probably twenty or thirty minutes later and step into yet another area of the city that I’m completely unfamiliar with."
    "She checks a navigation app on her phone for a few seconds before grabbing my wrist and pulling me along."
    "We walk several blocks and it quickly becomes apparent that I may have needed an even {i}thicker{/i} T-shirt to survive this weather."
    "The buildings are lined up in a way that turns the streets into a wind tunnel. "
    "And considering how cold it is today, there are barely any people ahead of us to serve as additional breaks for said wind."
    "We take everything in full force."
    "But luckily for Rin, she’s so wrapped up in her thoughts that she remains completely unfazed."

    r "Like, for real, though. Why’d her parents have to pick {i}today{/i} to get all stupid?"
    r "Any other day would have been cool, but nooooo. Let’s wait for a cute bisexual girl to come along and want to hold hands with our daughter before RUINING EVERYTHING."
    r "I should kill them. "
    r "Sensei, let’s go kill people."
    s "Rin, I know you want to impress Otoha, but I can’t help but feel like there are better ways of doing that than killing her parents."

    scene rindate16
    with dissolve

    r "Okay, fine. You wait outside and I’ll take care of the tough part."
    r "If Otoha tries to run away, though, you’ve gotta grab her so I can have a chance to explain myself."
    s "You’re not actually insane, are you?"
    r "Is it insane to kill the people between you and your goal?"
    s "Yes."
    r "Oh."

    scene rindate17
    with dissolve

    r "Well, maybe I am then."
    r "I don’t know. I’m just so friggin’ pissed off, you know?"
    r "I could barely even sleep because of how excited I was for this and now I’ve gotta hang out with {i}you{/i} instead."
    s "…"

    scene rindate18
    with dissolve

    r "Dude, I’m kidding!"
    r "That was obviously a joke. You know you’re my favorite."

    if rinbetrayed == True:
        if bonus == True:
            r "Like, what other person do you think could hook up with the one girl I wanted more than anyone else in the world and {i}still{/i} be able to spend time with me? "
            r "We’re stuck together, whether we like it or not."
            r "Just like how I’m stuck with the memories of you burying your fingers inside of Chika while I was burying mine inside of myself."
        else:
            r "Like, what other person do you think could hug the one girl I wanted more than anyone else in the world and {i}still{/i} be able to spend time with me?"
            r "I bet you aren't even that good at hugging."
            s "Ah!"

        scene rindate19
        with dissolve

        r "Whoops! Said too much. "

        if bonus == True:
            r "Don’t want you taking advantage of {i}me{/i} next!"
            s "You’re really going to remind me of that every time we hang out, aren’t you?"
            r "Or until one of us dies. Either one works."
        else:
            s "You bet your bottom dollar you did!"

    else:
        if bonus == True:
            r "Like, as far as people with penises go, you’re the number one prospect in my book."
            s "I know that compliment isn’t really anything I should write home about, but that does make me feel good."
            s "Where do I stack up against the people without penises?"

            scene rindate19
            with dissolve

            r "Hmm..."
            r "Close to the top still, I guess."
            r "Like obviously below Chika and Otoha...But like, somewhere above Molly and Ami."
            s "Why is Ami on the list? "
            r "Ami’s cute and has good taste in manga."
            r "Plus she’s girly and I like girly girls."

            scene rindate20
            with dissolve

            r "I’d totally bang your [niece], dude."
            s "I can’t tell if I’m confused or aroused right now."
            r "Why not both?"
        else:
            s "Platonically though, right?"
            r "Of course, homie. We'll be buds forever."

    scene black
    with dissolve2

    "We walk several more blocks before finally arriving at the arcade Rin planned on taking Otoha to."
    "Just like she said, the place has a distinct “cool” aura to it. So much so that I feel a little out of place even coming here."
    "But, I guess this arcade wasn’t exactly picked out with me in mind."
    "This was supposed to be a date for her and another, equally cute girl."
    "I’m just a backup right now."
    "So I guess it falls on me to...soak up Rin’s handpicked, special date stuff and make her happy."

    scene rindate21
    with dissolve

    r "Here we are! Couch Potato! "
    s "What did you just call me?"
    r "Huh? Couch Potato is the name of the arcade."

    if bonus == True:
        r "To my right, you will see a wonderful selection of alcoholic beverages that I am not yet legally allowed to consume."
        r "If you want to get hammered, though, go right ahead! I understand the risks that come with dating an adult!"
        s "I think I can go the afternoon without drinking, but thank you."
        r "You sure? I’m kind of interested in what drunken Sensei would be like."
        s "I can’t imagine it would be anything you enjoy."
    else:
        r "To my right, you will see a wonderful selection of alcoholic beverages that I am legally allowed to consume because I am an adult woman."
        s "Does this mean you're going to have some?"

    r "Probably not but REGARDLESS-"

    scene rindate22
    with dissolve

    r "We are here to have a good time and forget all about our debatably bisexual musician friends."
    s "I only have one musician friend and she is already a confirmed bisexual."
    r "Maya is also a musician, Sensei. And she’s still up in the air."
    r "So while I’m thinking about {i}my{/i} debatably bisexual musician friend, you can just think about Maya."
    s "Thinking about Maya is exhausting. I’ll just think about Otoha as well."
    r "Fine. But please keep her clothes on in your imagination."
    s "Will you be abiding by that same rule?"
    r "Absolutely not."

    scene rindate23
    with dissolve

    r "But anyway, all the games and stuff should be somewhere behind me in the back corner."
    r "I’m not really sure what you’re into, so just come with me and play some of the stuff I do."
    r "Oh, and don’t cry too hard when I {i}friggin’ annihilate you.{/i}"
    s "You’re very good at being intimidating and adorable at the same time, Rin."
    r "And you’re very good at...stuff!"
    s "…"

    if bonus == True:
        r "Sorry. I planned out a bunch of compliments for my original date, but she’s doing homework right now."
    else:
        r "Sorry. I planned out a bunch of compliments for my original date, but her parents were just so large."

    r "I’ll get back to you with some nice stuff later once I can think of some."

    scene rindate24
    with dissolve

    r "But for now, let’s play some games and forget about our feelings!"

    scene black
    with dissolve2

    "Rin leads me to the back of the arcade rather confidently despite never having been here before."
    "I guess she really did her research online first."
    "The only issue is that now I have to try to not look like a complete imbecile playing whichever game Rin decides she wants to play first."
    "As long as it’s not one of those...dancing machines I’ve seen other [teenager]s play, though, I should be fine."
    "………"
    "……"
    "…"

    scene rindate25
    with dissolve

    "Nevermind. There is apparently more than one type of machine that can make me feel like a child."
    "I do not like this."

    r "You look like a moron right now."
    s "I want to insult you as well but you look pretty fucking cool."
    r "It’s the hoodie, not me."
    s "It definitely helps."

    scene rindate26
    with dissolve

    r "So, it’s probably safe to assume you’ve never played anything like this before, right?"
    s "Very safe. I have absolutely no idea what I’m doing."
    r "Just make sure you have your feet on the little foot-holder thingies and put both hands on the grips up here."
    r "You’ll notice a button on one of them. Press that to accelerate and move the bars around to steer."
    r "Each race has three laps and it’ll be you, me, and a bunch of AI opponents."
    r "Don’t underestimate them, though. This game might be a little retro, but the AI will fuck your day up."
    s "I am fully prepared for my day to be fucked up. Congratulations on defeating me in advance."
    r "Hey, man. There’s no fun if you give up beforehand. You’ve gotta at least try."
    r "Just think of how easy it would be to tease me if you defeated me at a game I literally taught you how to play."
    s "One can only hope."

    scene rindate27
    with dissolve

    r "Ready to do this, then?"
    s "As ready as I’ll ever be..."
    r "Good! Then-"

    scene rindate28
    with dissolve

    r "Prepare to get railed~"
    s "…"
    s "I understand that the game’s tagline is “Rail on” but don’t you think what you just said is a little...racy?"
    r "I’m gonna rail you so hard."
    s "Uh-huh."
    r "So hard you won’t even be able to walk afterward."
    r "And then when I’m done, I’m gonna call Ami over and rail your [niece]. "
    s "Rin, please."
    r "I’m gonna rail {i}everybody{/i}. All day. All night."
    r "You’ll be begging me to rail you again once we leave today. Calling it now."
    s "If your plan is to distract me through phrases that can be easily misinterpreted, it’s really not necessary. "
    s "You’re going to win no matter what."

    if bonus == True:
        r "What can I say? I’ve been railing ever since I was a little girl."
        r "I know my way around the block, man."

    scene rindate29
    with dissolve

    r "NOW, PREPARE TO DIE, LOSER!"

    scene rindate30
    with fade

    "Rin’s shout was a bit pre-emptive as we still needed to select a track and I guess...different types of motorcycles or something?"
    "I don’t know. I chose the first one I saw and, as expected, was demolished so quickly that I couldn’t even blame the bike."
    "The same pattern repeated for the next few hours."
    "Rin would take me to a machine, explain how the machine works, and then make me look like an absolute idiot in front of the...three other people that were there."
    "I’m pretty sure they may have even started laughing at me after a while."
    "And while something like this would normally bother me, today it was fine."
    "Because not only was the purpose of this trip to help cheer Rin up after the new object of her affection bailed on her-"
    "But it was the first few hours in quite some time that I’ve felt like she was actually focused on me."
    "Backup date or not, it was fun getting to see this side of her. "
    "Otoha really did miss out on something great this afternoon."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Eventually, we run out of machines to try out and head over to a pizzeria on the corner of the street."
    "We take our time sharing a pizza and wind up begrudgingly leaving one slice that we were unable to finish behind."
    "Instead of the night ending there, though, Rin urges me to come back to the dorm since she still has more time to kill and Futaba is with Nodoka tonight."
    "Having nothing else to do, I obviously agree and allow the backup date to move into its second phase."

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe45 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    jump rindorm45

label cafe50:
...
```

## Code that triggers this event
File: \game\RinEvents.rpy
Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
    if rin_love >= 20 and ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False:
        jump cafe20
    if rin_love >= 15 and cafe15 == True and day63 == False:
        jump rincafegone
    if rin_love >= 25 and rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False:
        jump cafe25
    if rin_love >= 30 and beachvacation16 == True and cafe30 == False:
        jump cafe30
    if rin_love >= 35 and rindorm35 == True and rininvite == True and cafe35 == False:
        jump cafe35
    if rin_love >= 40 and christmas7 == True and cafe40 == False:
        jump cafe40
    if rin_love >= 45 and rindorm40 == True and cafe45 == False:
        jump cafe45
...
```