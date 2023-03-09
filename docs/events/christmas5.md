# Bottled Dreams
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmas5&go=Go)


Part of event chain [Disappointing Everyone](./christmas4.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmas5
* Group: Main
* Triggered by label: christmas4

## Event code
File: \game\script.rpy
Code:
```python
...
label christmas5:
    play sound "dooropen.mp3"

    mo "LADIES AND GENTLEMEN..."
    mo "WELL, ALL LADIES. SEEING AS THE ONLY GENTLEMAN IN THE ROOM HAS WALKED IN ALONGSIDE ME, MOLLY MACCORMACK."
    s "Is this really necessary?..."
    mo "How would you all like a chance..."
    mo "To make your dreams come true?"

    scene spinthebottle1
    with dissolve2
    play music "stpartynight.mp3"

    s "What is going on right now?"
    mo "Friends. Companions. Stray adventurers looking to stable your pets-"
    mo "I hold in my hand the key to everything you have ever wanted."
    mo "And I speak not of an elixir that will turn you into the Molly MacCormack you all saw on Halloween."
    mo "In fact, this bottle holds nothing at all."

    scene spinthebottle2
    with dissolve

    mo "NOTHING BUT DREAMS."

    "God I hate Christmas."

    scene spinthebottle3
    with fade

    ay "Wow, Molly seems passionate. Even by her standards."
    sa "Um...bottles can’t actually hold dreams, can they?..."
    sa "I don’t know what she’s talking about."
    ay "Me neither. But I guess we can just wait to see how this plays out."

    scene spinthebottle4
    with fade

    m "Oh no."
    m "He let Molly choose."
    a "Let her choose what? The present he forgot about?"
    a "I mean, it’s better to get her opinion than just letting him get something on his own, isn’t it?"
    a "At least she’s a girl."
    a "It’s better than 700 Yen worth of pocket change."
    m "Yeah, we’ll see about that."

    scene spinthebottle5
    with dissolve

    mo "Now, I suppose you’re likely wondering how a bottle can hold dreams."
    ay "Sana, she read your mind! It’s one of her powers!"
    sa "Shh! I’m listening!"
    mo "Under most circumstances, thoughts like that would make sense. I mean, it’s just a bottle. How can it hold anything other than milk or Guinness?"
    s "Bottles hold more than-"
    mo "Silence, Sir. You have entrusted the present you forgot about to me, so I must take it in my own hands to make the dreams of one lucky girl (Preferably me) come true!"
    a "And she flat out just told everyone he forgot..."
    s "Really, Molly?"

    scene spinthebottle6
    with dissolve

    mo "Friends, take a look around you."
    mo "We’re all gathered here, listening to Western Christmas music, eating food from a Western food chain, celebrating a Westernized holiday..."
    mo "Wouldn’t you say it would be beneficial to {i}all{/i} of us if we were to break out another classic Western game in..."
    mo "{i}Spin the bottle{/i}?..."

    scene spinthebottle7
    with fade

    c "So {i}that’s{/i} your game, Molly MacCormack."
    c "Failure is not an option, Chika."
    c "You will spin the bottle. And you will win."
    f "…"
    c "…"
    c "I know you’re looking at me, Futaba."
    c "You heard nothing."
    f "Yeah..."
    f "Um...good luck?"
    c "I don’t need luck. Victory will be mine."

    scene spinthebottle8
    with fade

    sa "Um...Ayane? "
    sa "What happens when you spin the bottle?"
    ay "It’s a game Western [teens] used to play in like, the 80’s."
    ay "Someone goes up and spins the bottle and they need to kiss whoever the bottle points at when it’s done spinning."

    scene spinthebottle9
    with dissolve

    sa "They have to...what?"
    ay "I’m just as worried as you. Well, probably more worried. "
    ay "If anyone spins the bottle, they have almost a 10%% chance of having it land on Sensei."
    ay "If I see anyone but me kiss him, I will literally explode. "
    ay "I hate the thought of it so much that I even broke out percentages. "
    ay "Did you know I’m actually smart, Sana? I bet you didn’t know that."
    sa "K...Kiss?..."
    sa "But...I don’t...want to kiss...anyone here..."
    ay "Well, that’s reassuring for me at least. Thank you for being such a good girl."
    sa "I want to go home..."

    scene spinthebottle10
    with fade

    mak "Sensei! What is the meaning of this?!"
    mak "Why are you forcing such a lecherous game on us instead of actually getting a {i}real{/i} present?!"
    s "I know what you’re thinking, but it really wasn’t me this time."
    mak "So you {i}didn’t{/i} forget to buy a present for someone?"
    s "Okay, that part was me. But the bottle thing was all Molly."
    mak "Likely story."
    mak "What are you going to do if someone spins it and it lands on you?"

    if bonus == True:
        s "…"
        s "Well I mean, I {i}have{/i} to abide by the rules at that point, right?"
    else:
        s "Probably cry or something."

    scene spinthebottle11

    mak "{i}Excuse me?{/i}"

    if bonus == True:
        mi "You’re really gonna just lock lips with somebody smack-dab in the middle of our Christmas party?"
        mak "As if I’d ever let that happen..."
        mi "Yeah, even I don’t like the sound of that and I normally just let stuff like this happen."
        s "How often have you been faced with scenarios like this, Miku?"
        mi "Heck if I know. Just don’t friggin’ kiss anybody in the middle of our party."
    else:
        s "Yeah. That sounds really stressful and now I'm kind of nervous."
        s "Thanks for ruining Christmas, Makoto."

    scene spinthebottle12
    with fade

    t "Can one bottle truly possess so much power?"
    t "Leave it to the Emerald Guardian of the Crystal Forest to make all of our dreams come true. "
    ka "K...K...Kiss..."
    ki "Hehehe~ Looks like this party has a chance to get interesting after all. Way to go, Irish girl."
    ka "Ki...Ki...Kirin..."
    ka "It is...past our b-b-b-bed time..."

    if bonus == True:
        ka "We need to be heading...home...before...one of us gets...p...p...pregnant."
    else:
        ka "Not that we actually have bedtimes or anything since we're in college. But yeah."

    ki "No way, sis. We can’t leave now. We finally got to the good part."
    t "If the bottle lands on me, I can finally go to Virginia."
    ki "…"

    scene spinthebottle13
    with dissolve

    ki "What?"

    scene spinthebottle14
    with fade

    "Molly walks up to the table, bottle in hand, and prepares to make the first spin."

    if bonus == True:
        "I accompany her, crouching down to get a better look at the spin because, let’s face it, I’m excited too."
        "There’s literally no way I can lose this game."
        "But I should probably be sure she’s okay with putting what I assume is her first kiss entirely in the hands of fate."
    else:
        "I accompany her, worried that she is about to do something that will make future events significantly more upsetting."

    s "Are you sure you want to do this?"
    mo "Of course, Sir."
    mo "You have bestowed upon me the chance to make my dreams come true. To finally become the lead heroine! And in front of everyone else at that!"
    mo "I accept my fate regardless of the outcome, for if there are higher powers out there, they shall truly force the two of us together!"
    mak "You two? Really? Yeah, not happening."
    ki "Good luck, Irish girl! "
    ki "If you spin it really softly, it’s sure to land on Sensei!"
    ka "D...DON’T...SPIN!"
    ka "BOTTLES ARE...BAD!"
    t "Good luck, Emerald Guardian. If we have to kiss, please be gentle."

    scene spinthebottle15
    with dissolve

    mo "Molly MacCormack requires no luck. She has been putting all of her points into that since the beginning of time."
    mo "I carry with me the heart of my homeland! The luck of the Irish!"
    mo "And so I put this in the hands of the fae! Gift unto me a dream come true!"

    scene bottlespin1
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin2
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin3
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin1
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin2
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin3
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene spinthebottle16
    with dissolve

    mo "…"
    ay "Phew. It landed on Rin."
    sa "Does this mean...Molly and Rin are going to kiss?..."
    t "But they’re on opposite factions. It would never work."
    mo "It’s fine, Kendo Princess..."
    mo "If this is what fate has in store for me, I must accept."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene spinthebottle17
    with dissolve2

    mo "…"
    r "Uhhhhhhhhhhhhhh..."
    r "What?"
    r "What are you doing?"
    r "Why are you touching me?"
    r "Is there something on my face? Are you checking to see if I have a fever?"
    mo "No, Rin..."
    mo "I’m simply moving the way the world dictates that I must move."

    scene spinthebottle18
    with dissolve

    r "Hmm...okay, okay."
    r "I speak Molly, so I should be able to figure out what that means."
    r "You walked in here yelling something about fate..."
    r "And a bottle that carried...dreams..."
    r "And now you’re here...and you’re...moving the way...the world...dictates?..."
    mo "…"
    r "…"

    scene spinthebottle19
    with dissolve

    r "DON’T YOU DARE, MOLLY!"
    r "IT’S JUST A GAME! YOU DON’T ACTUALLY HAVE TO-"

    scene spinthebottle20

    mo "FOR IRELAND!"
    r "NO! NOT FOR IRELAND!"

    scene spinthebottle21
    with dissolve

    r "MMMMMM!!!!!"
    mo "Chu~"

    scene spinthebottle22
    with dissolve

    r "WHY?!"
    mo "We are now bonded for life."
    r "THAT ISN’T HOW KISSING WORKS!"
    r "I WAS SAVING MY LIPS FOR SOMEONE ELSE!"

    scene spinthebottle23
    with dissolve

    mo "AM I NOT GOOD ENOUGH FOR YOU?!"
    r "YOU’RE NOT MY TYPE! YOU KNOW THIS!"

    scene spinthebottle24
    with fade

    f "…"
    c "…"
    f "…"
    c "…"
    c "Did that really just happen?"
    f "Yeah..."
    c "Does...this mean Rin is over me now?"
    f "I don’t think so...this kind of happened against her will?"
    c "Aren’t we supposed to call the police if something like this happens?"
    f "I...don’t know."
    f "I’ve never dealt with this before."

    scene spinthebottle25
    with fade

    ay "Okay, okay. Time to let a real warrior spin."
    s "You too?"
    ay "The chance of having to kiss a girl can not outweigh the sub-10%% chance I have to kiss you in front of everyone, Sensei. "
    ay "This is a risk I must take, beloved future-husband. And I need you to believe in me."
    s "Okay, but I believed in Molly and she wound up kissing Rin."
    ay "I saw. It was pretty awesome."
    s "Well, good luck I guess."
    mak "I can’t believe I’m actually letting this happen right now."

    scene bottlespin1
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin2
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin3
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin1
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin2
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene bottlespin3
    with dissolve
    $ renpy.pause(0.3, hard=True)
    scene spinthebottle26
    with dissolve

    a "…"
    ay "…"

    scene spinthebottle27
    with dissolve

    a "Huh. "
    a "That looks like it’s pointing right at me."
    m "Probably because it {i}is{/i} pointing right at you."
    a "That can’t be true. It would mean I have to kiss Ayane."
    ay "Well...I guess this is less awkward than having to kiss Yumi or something."
    s "On the bright side, at least it won’t be the first time you two have kissed."

    scene spinthebottle28
    with dissolve

    a "What are you talking about?! Ayane and I have never-"

    scene spinthebottle29
    with hpunch

    "Ayane jumps over the table to get to Ami and quickly pulls her body toward her, locking her into a kiss."
    "Sana, who I assume had instinctively followed Ayane out of sheer habit, is now frozen solid and unsure of what to do."

    if bonus == True:
        "And, in other news, I suddenly have an erection."

    sa "Why...are all of my friends...kissing other girls?..."
    m "Hah..."
    m "Christmas is exhausting."
    a "…"
    ay "…"

    scene spinthebottle30
    with fade

    t "So beautiful."
    t "I wish them a happy life together."
    ki "…"
    ki "I’ll be right back."
    ki "I’m gonna go do something."

    scene spinthebottle31
    with fade

    mak "Don’t you fucking dare."
    s "But I need to make dreams come true."
    mak "Sensei..."
    s "I’m sorry, Makoto."
    s "I can’t let Molly down on Christmas."

    menu spinbottle:
        "Spin hard":
            scene bottlespin1
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin2
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin3
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin1
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin2
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin3
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene spinthebottle33
            with dissolve2

            c "Ah!"
            c "It landed on me! "
            s "Weren’t you just halfway across the room two seconds-"
            c "I’ve been here the whole time."

            scene spinthebottle34
            with dissolve

            c "You have to kiss me now, right? That’s how this works?"
            c "Why aren’t you kissing me yet?"

            scene spinthebottle35
            with dissolve

            mak "Again, don’t fucking dare."
            s "But she won fair and square. I need to give her something."
            mak "How about an actual present because, you know, it’s {i}Christmas{/i}?"
            s "Can we at least...take a walk together or something?"
            mak "Through the halls of a hotel? Romantic."
            c "I’ll go on a walk!"
            c "I mean I obviously wouldn’t actually {i}kiss{/i} Sensei, especially in front of the entire class- so a walk is fine!"

            scene spinthebottle36
            with dissolve

            mak "You literally {i}just{/i} complained about him taking too long to kiss you."
            c "That never happened. You need to get your ears checked."
            mak "Whatever. Go for your stupid walk. "

            if bonus == True:
                mak "But be back in ten minutes or I’m calling security and telling them there’s an older man taking advantage of a[school] girl."
            else:
                mak "But be back in ten minutes or I'm setting the building on fire and killing everyone inside."

            c "Twenty minutes and I promise not to tell anyone what I found in your locker that one time."
            mak "…"

            "Wait, what was in Makoto’s locker? Now I’m kind of curious."

            mak "Fine. {i}Twenty{/i} minutes. But no more. Got it?"
            c "Got it! Thanks class prez!"

            scene black
            with dissolve2
            stop music fadeout 10.0

            "Chika springs up faster than I’ve ever seen her move before and throws the door open, dragging me along before Ami and Ayane are able to snap out of their post-kiss...depression?"
            "They definitely did not look very happy."
            "But hey, if them being sad for a little while is the only negative aftereffect of getting to watch them kiss, I’m completely fine with it."
            "………"
            "……"
            "…"

            $ renpy.end_replay()
            $ christmas5 = True
            jump chikalust10intro

        "Spin soft":
            scene bottlespin1
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin2
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin3
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin1
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin2
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene bottlespin3
            with dissolve
            $ renpy.pause(0.3, hard=True)
            scene spinthebottle32
            with dissolve2

            if bonus == True:
                m "…"
                s "…"
                mi "…"
                m "Absolutely not. "
                m "Spin it again."
                s "Fine..."
            else:
                m "Omg yes"
                s "Wait, no. I meant to spin harder."
                m "What? No. Please."

            jump spinbottle

label chikalust10intro:
    play music "love.mp3"

    "Chika and I make our way down the halls of the hotel as she skips happily beside me, humming the tune of whatever Christmas song was just on the radio to herself."
    "I think about reminding her of my distaste for the holiday, but ultimately let her decide to do her thing since she is apparently on the opposite end of the spectrum."
    "It’s fine to like Christmas, but trying to infect others with your feelings on the matter is no better than trying to convince a life-long normal person to not eat meat."
    "Opinions are best when they’re kept isolated, which is why I will continue to ignore my thoughts and let everyone else be happy instead."

    scene chikalustten1
    with dissolve2

    c "Oh, Sensei! I forgot to tell you."
    c "Chinami and I got you a present since you’re always going out of your way for us."
    c "It’s nothing big since we’re still kind of low on money, but we hope you like it anyway."
    s "Speaking of Chinami, are you really leaving her alone on Christmas?"
    s "That seems unlike you."

    scene chikalustten2
    with dissolve

    c "We watched some movies and stuff together earlier. She’s asleep right now."
    c "So I guess {i}technically{/i} she’s alone on Christmas, but she’ll probably never even realize it since we’ll be back before she even wakes up."
    s "Fair enough. "
    s "Can I ask you something else, though?"
    c "Sure. What’s up?"
    s "Why are we holding hands right now?"
    c "Because I won you. You are my prize."
    s "I’m no expert on spin the bottle, but I’m pretty sure the person who spins is the one who technically “wins.”"

    scene chikalustten3
    with dissolve

    c "Nope! I’m the winner. And if you’re not going to kiss me in front of everyone, the least you can do is hold my hand."
    s "Okay but if anyone sees us, you’re taking the blame."

    scene chikalustten4
    with dissolve

    c "Of course. I planned on that anyway. "

    "And I’m assuming she planned on “winning” as well considering she basically leapt in front of the bottle as it stopped spinning."
    "If it was even a little off to the side, I imagine she would have pushed Maya over as well."
    "But hey, at least it’s proof that her affinity for me is actually genuine. "
    "Which isn’t to insinuate that it’s not like that with the others."
    "But Chika really does feel like an actual girlfriend at times."
    "It’s weird."

    scene chikalustten5
    with dissolve

    c "Hmm...Do you think anyone would care if we snuck outside for a bit?"
    s "I don’t think anyone would even know."
    c "Even better~"
    s "Is it, though? It’s freezing out and all you’re wearing is...that."
    c "I’ll be fine if it’s only for a few minutes. Besides, if I get cold, you can just warm me up."
    c "I’ll take the blame for that if we’re caught as well, so don’t even worry about it."
    s "You seem unusually confident tonight."
    c "Probs because I got the present I wanted most."
    s "…"
    c "…"

    scene chikalustten6
    with dissolve

    c "I’m talking about this cute handbag I got for myself before I left work yesterday."
    c "You’re the present I wanted second-most, though. So don’t feel too bad."
    s "I hope to one day be as essential as an accessory to you."
    c "And I hope to one day {i}be{/i} an accessory to you. "

    scene chikalustten7
    with dissolve

    c "Wait. That makes it sound like I’m okay with being some sort of mistress."
    c "What I meant to say is I just want to stay with you for a really long time. Kay?"
    s "Are we going outside or what? The door is right in front of us."

    scene chikalustten8
    with dissolve

    c "How come you never say anything cute back to me?"

    scene black
    with dissolve2

    "Chika and I make our way outside and walk around the perimeter of the hotel, stopping at an old bench leaned up against the brick walls."
    "The grass is overgrown and the exterior, particularly in the back, doesn’t match the high expectations the inside set-"
    "But the girl next to me manages to offset any flaws on the outside of the hotel by just being so fucking cute."

    if chika_lust < 10:
        "Unfortunately, an employee from the hotel decided to go out for a smoke break and told us that we weren’t allowed to be back here."
        "We spent the rest of our very special twenty-minutes together arguing that there shouldn’t be a bench here if people aren’t allowed to sit on it."
        "The argument changes nothing and we hang our heads as we make our way back to the hotel room."
        "But even though nothing really came of the meeting, Chika and I still manage to become a little bit closer."
        "It wasn’t much, but I’m glad we got to spend some of Christmas together."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ chikalust10miss = True

        stop music fadeout 5.0
        jump christmas6

    else:
        jump chikalust10

label chikalust10:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```