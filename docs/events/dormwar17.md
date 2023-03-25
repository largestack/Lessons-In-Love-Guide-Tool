# War's End (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Princess & The Pauper](./chikalust15.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Futaba: Skin](./futabadorm40.md)
* [Haruka: Sober-ish](./harukadate20.md)
* [Main: Record Breaker](./day333.md)
* [Uta: Happier Things](./utamaid10.md)
* [Io: Turn On The Lights](./bathhouse10.md)

## Event properties

* Id: dormwar17
* Group: Main
* Triggered by label: chikalust15
* Chain sources: chikalust15
* Chain sources path: chikalust15

## Official wiki page

[War's End](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar17&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar17:
    scene warsend1
    with dissolve
    play music "justbehappy.mp3"

    u "Rise and shine, maggots! We might not have[school] today, and the war might be over, but don’t think for a second that means you can rest!"
    mak "You can rest. And you’re all free to leave as soon as our announcement is over."
    mak "In fact, I should probably take roll call since it looks like we’re missing a few of..."

    scene warsend2
    with dissolve

    mak "Wait, why are the only girls missing from my floor?"
    mak "Where is Ayane? And Maya? And Yu-"
    mak "Well, I understand why Yumi is missing, so disregard that part please."

    scene warsend3
    with dissolve

    a "Maya’s still recovering from the test of courage and Ayane wasn’t feeling well this morning."
    a "But I can probably get them to watch on Facetime if-"
    u "Facetime?! More like {i}no{/i} time! We’ve gotta get this show on the road, Ami!"
    a "Well...yes. I understand that. But they’re members of our team and-"
    mak "Just...recap them after the announcements are over, Ami. It appears that {i}certain{/i} people would like to make the most of their day off from[school]..."

    scene warsend4
    with dissolve

    u "You talkin’ about me, Makoto?"
    mak "{i}You?{/i} Noooo. Why ever would I do that?"
    u "You wanna throw hands? Cause I’m ready to go right now."
    mak "Throw...what?"
    mak "Did you even sleep last night? You seem incredibly hyper for even your standards."
    u "Not even a little! I’m gonna spend the whole day under the covers and there ain’t anything you can do to stop me!"
    mak "…"
    mak "So, the results."

    scene warsend5
    with dissolve

    u "Right! Results!"

    if ayanelust15 == True or futabalust15 == True or chikalust15 == True:
        u "So, if you’ve been keepin’ track of the normal score and your team is losing, don’t fret just yet! Cause we’ve got a bit of a surprise for you!"
        mak "We...certainly do, as it appears that some of our classmates have taken it upon themselves to conduct their own “bonus” competitions with Sensei as the judge."

        if bonus == True:
            mak "I can only fathom what that must possibly mean."

        scene warsend6
        with dissolve

        a "The heck is a “bonus competition?!” I didn’t sign off on this!"
        n "We were allowed to have our own competitions and no one told me?!"
        n "I demand we do the entire contest over! And I also demand to be included in the date war this time!"
        a "I am in agreement with Noriko!"
        a "Who would have even had a bonus competition like that?!"

        if futabalust15 == True and bonus == True:
            scene warsend7
            with dissolve

            no "Heheheh..."
            f "Nodoka..."
            no "{i}Who{/i} indeed, Futaba. Who indeed..."
            f "I would very much appreciate it if you would purge that night from your memory."
            no "Is this Eternal Sunshine all of a sudden? I can not simply conduct targeted purges of certain aspects of my memory, Futaba. Let alone the ones I cherish most."
            f "Please don’t consider that one of your most precious memories, either."
            no "Was it not as enjoyable for you as it was for me?"
            f "It...wasn’t {i}not{/i} enjoyable, I guess."
            no "Is this an invitation for further {i}contests{/i} in the future?"
            f "..."
            no "...?"
            f "We should...probably listen to the results."

        scene warsend5
        with dissolve

        u "Doesn’t matter who it was! All that matters is that it happened!"
        u "And for the safety of those involved, we have decided not to reveal any names!"
        a "Reveal the names!"
        n "Oust the betrayers!"
        u "Silence!"

        scene warsend8
        with dissolve

        u "The Super Mega Ultimate Dorm War has finally reached its end."
        u "And the first ever winners are..."

    else:
        u "So, we had a pretty standard ten match brawl. No bonus points awarded. No secret contests. Nothing like that."
        u "Just good ole’ fashioned one-on-one fights for our teacher’s body!"
        mak "Yes, how incredibly “ole’ fashioned.”"

        scene warsend8
        with dissolve

        u "Ladies and gentlemen...the results of the first ever Super Mega Ultimate Dorm War are in."
        u "And the winners of the event are..."

    mak "Wait."
    u "…"
    u "What am I waitin’ for, Makoto?"
    mak "…"
    mak "Can I do it?"
    u "Forreal? We really doin’ this right now?"
    no "Perhaps just let the captain of the winning team announce the results?"
    n "Yeah, that seems fair to me."
    mi "Agreed! Let the winning team do the talkin’! They worked for it!"
    u "Then..."
    mak "In that case..."

    if dorm1warpoints > dorm2warpoints:
        scene warsend9
        with dissolve
        $ dormwarfloor1win = True

        mak "The winning team is the first floor!"
        u "You fought a good fight, Makoto."
        u "Really showed us second floor girls that we’re gonna need to step up our game if we wanna take over the place."
        mak "I’m incredibly humbled to be the captain of such a great team, and I sincerely appreciate how hard all of you fought in order to win this for us."
        mak "Yes, we may have Sensei now. But what matters even more than that is that we have each other. And-"
        a "Booooooooo! Only a glasses-faced loser would pretend that Sensei isn’t the true prize of this competition!"

        scene warsend10
        with dissolve

        mak "I...was just trying to give a humble victory speech..."
        mak "But if you want to play it that way...sure, Ami. Let’s rub it in their faces."

        scene warsend11
        with dissolve

        mak "Take that, Uta! We get Sensei and you don’t! How does it feel, you little bitch?!"
        u "Holy heck, Makoto. No need for the friggin’ power trip."
        u "Just take your heckin’ win and go celebrate or somethin’. No need to hurt my feelings."

        scene warsend12
        with dissolve

        mak "I apologize. That was very unprofessional of me."
        mak "Floor one girls, please take the rest of the morning to celebrate our hard earned victory."
        mak "And please do not follow in my footsteps. Be kind to the losing team, for they are only human. And we are a machine."

    elif dorm2warpoints > dorm1warpoints:
        scene warsend13
        with dissolve
        $ dormwarfloor2win = True

        u "Floor two wins!"
        u "Woohoo! Good job, girls!"
        mak "Hah..."
        mak "We really should have vetted the competitions a bit better. There were several that clearly favored your floor and-"
        u "Yeah, yeah. Excuses, excuses. Just accept that my girls are better than your girls and call it a day, prez."
        u "Everybody! Y’all worked your friggin’ butts off and deserve this more than anybody I’ve ever met!"
        u "I am glad to be called your leader! And I, Uta Ushibori, hereby solemnly swear to be the captain for the second dorm war as well when the time comes!"

        scene warsend14
        with dissolve

        mak "Wait, we’re doing this again?"
        u "Heck yeah we are."
        u "Even if we all wind up in different classes or get our rooms switched or whatever else happens in this[school], we should all agree to meet here this time next year!"
        u "Same teams! Same captains!"
        u "And probably the same champions because we’re the best and you’re stupid!"

        scene warsend15
        with dissolve

        mak "There’s no need to get hostile over it."

        if bonus == True:
            mak "Besides, winning Sensei’s company for the night in a room packed to the brim with girls is the equivalent of letting a hungry coyote roam free in a chicken coop."
            n "I see no problem with this! Let that coyote roam! Let him roam all over me!"

        a "AAAAAAAAAAAHHHH!!!!!!!!!!!"
        u "You see, Makoto...we all know the dangers of letting Sensei stay in the room with us. And yet we fought for him anyway."
        u "Why do you think that is?"
        mak "Because you’re a bunch of impure lunatics?"
        u "Because {i}we{/i} like him more than you guys. So ha."
        mak "I can guarantee you that is absolutely not the-"
        u "Results beg to differ, Makoto. So why don’t you go take a hike or start practicin’ for next year or something?"
        u "You're obviously gonna need it."
        mak "You’ll regret this, {i}Uta...{/i}"
        u "We’ll see about that, {i}Makoto...{/i}"

    elif dorm1warpoints == dorm2warpoints:
        scene warsend16
        with dissolve
        $ dormwartie = True

        uam "Both teams win!"

        scene warsend17
        with dissolve

        a "…"
        n "…"
        a "So..."
        n "What now?"
        mi "The heck are we gonna do to solve this?!"
        mi "You sayin' we have to do the whole dorm war over?!"
        ki "Are we...all sleeping in the same room now?"
        t "Twenty girls and one man in the same room seems-"
        ki "Fun? Agreed."

        scene warsend8
        with dissolve

        u "Makoto and I will both admit that we never saw this coming!"
        mak "I mean, it was an obvious possibility given that we had ten separate contests...so I wouldn’t say that I believed it was {i}impossible.{/i}"
        u "Blah blah blah math stuff."
        u "Point is, we’re gonna have to have some sort of tiebreaker."
        u "So Makoto and I are gonna arm wrestle and-"
        mak "We are not."

        scene warsend18
        with dissolve

        mak "We’re probably just going to have Sensei personally choose the team that he believed performed the best overall."
        u "You sure? Cause I think the arm wrestling thing is a lot more exciting."
        mak "I mean...what else would you suggest we do? Have another competition that would only exist as the result of a tie?"

        scene warsend19
        with dissolve

        mo "Absolutely not!"
        mo "If you lock an entirely new event behind such a specific set of circumstances, there are going to be thousands of entitled players who will complain about it!"
        mo "It is our job as visual novel heroines to prevent this from happening at all costs because God forbid anyone misses one friggin’ scene in a game longer than life itself!"
        no "But Molly, by that logic, wouldn’t even this outburst of yours constitute such a thing?"
        no "Surely there are dimensions out there where we didn’t tie and this conversation never even happened."
        mo "Of course! And there are hundreds of other examples of our dialogue changing as a result of our actions as well, and no one complains about them because they feel natural and are not advertised!"
        mo "It’s almost like some developers factor in replayability or player influence into their products when what we {i}really{/i} want is a streamlined experience that feels bland, impersonal, and fragmented!"
        sa "Um...may I...weigh in?"
        no "Of course, Sana. Feel free. This is an open forum after all."
        sa "I...I think that...players should just accept that...visual novels are meant to be...personal experiences where...where decisions feel important..."
        sa "And...and I wouldn’t really care about...things happening differently because...because it just means I made them that way..."
        mo "But, Sana! What about the {i}completionists?!{/i}"
        mo "Are you suggesting that we upset a very small demographic of overly vocal players because we want things to make {i}sense?{/i} That is absurd!"

        scene warsend20
        with dissolve

        u "How about we just all agree that anyone immature enough to complain about such a thing should be focusing on improving themselves rather than crying about a video game?"
        mak "Well said, Uta. It’s not like the majority of those players are contributing to the game’s development anyway."
        u "Right! So they should just trust in the creator! Because if anyone knows what a game is supposed to be, it’s the person making it."
        mak "Agreed on all counts."

        scene warsend21
        with dissolve

        u "So fuck you if you are that person!"
        mak "Yeah. Now go get a real girlfriend or something and stop getting so offended when cartoon girls don’t do exactly what you want them to do."
        u "Yeah, nerd!"
        mak "Uta, do you know what I just realized?"
        u "What’s that, Makoto?"
        mak "That somewhere out there, there’s going to be someone who has no idea what we’re talking about feeling very confused right now."
        u "Oh, jeez. You’re right. They’re probably just tryin’ to get on with their day and choose a winner or something and we’re gettin’ all preachy!"
        mak "True. But chances are they pirated the game anyway so they can fuck right off."
        t "Did someone say pirate?"
        mak "Oh well. It is what it is, I suppose."
        mak "The fact is that it’s never possible to please everyone, so you should follow your heart and do what you think is best, even if you know it’s going to make some people mad."
        u "Unless that decision involves literally hurting people, which is something you should never do!"
        mak "That’s right."
        mak "Be kind, drive responsibly, stay hydrated, and all of that other positive advice people normally give out to rid themselves of responsibility for the actions of those who can not think for themselves."
        u "Amen!"
        mak "Amen."

        scene warsend17
        with dissolve

        a "…"
        n "…"
        a "Okay, but...who wins?"
        u "I guess we’ll find out when the time comes to sleep over at the beach!"
        mak "For now, though...let’s just all be happy that we’re together. And that we’re all winners in at least that respect."
        u "Right!"
        u "Except for Molly!"
        mo "STOP DOING THAT, DAMN IT!"

    scene black
    with dissolve2

    "I catch up with the girls shortly after the winning floor is announced and breathe a sigh of relief knowing that this has finally come to an end."
    "Don’t get me wrong, it’s great watching a bunch of cute girls fight over you, but it’s {i}not{/i} great not having any time to myself to actually...act as I please and whatnot."
    "I suppose that doesn’t matter right now, though."
    "I still have the rest of Monday off to do whatever I want and..."
    "And I guess that means I’ll just...kick things off with more of the same."
    "………"
    "……"
    "…"

    if chikalust15 == True:
        scene warsend22
        with dissolve

        c "Good...morning...Sensei..."
        to "Guh..."
        s "Good morning, you two."
        s "How are you feeling?"
        c "My head...feels like it’s going to explode..."
        to "Chika...if it’s not a bother...could you please quiet down?"
        s "So...just out of my own curiosity...do either of you two remember what happened last night?"
        c "I...remember...drinking a lot at the bar and..."
        c "And everything after that is just..."
        to "I...drank last night?..."
        to "Wait...yes...yes, I do remember that..."
        c "We didn’t...do anything stupid, did we?..."
        s "Nope. Nothing at all. You two made it back to the hotel and then safely went to sleep without doing anything else afterward."
        c "Okay, but...that doesn’t really explain why we were both...hugging Nodoka when we woke up."
        s "She is a lovable girl. I’m sure you just...naturally gravitated to her."
        to "I...I don’t think...I should consume alcohol anymore..."
        to "Does...does it always feel like this afterward?..."
        s "Only if you do it correctly."
        s "I’ll leave you two alone, though. You clearly don't need to be bothered right now."
        c "Okay...thanks..."
        c "I think...I’m just gonna go home and sleep anyway..."
        to "And I..."
        to "I think I...need to go to the doctor..."

        scene black
        with dissolve

        "I walk away from two incredibly hungover girls who, thankfully, seem to have zero recollection of their actions last night."

        if bonus == True:
            "I’m pretty sure Chika {i}probably{/i} would have been okay with it, but..."
            "I feel like Touka wouldn't have been able to even look at me if she knew how “improper” her actions were last night."
            "Fortunately, our relationship survives another day and I find myself heading over to a frozen fountain to speak to someone who clearly doesn’t want to be here..."
        else:
            "I should buy some coffee and water for them if I get a minute after the closing ceremony."

        "………"
        "……"
        "…"

    scene warsend23
    with dissolve

    s "Morning, Io."
    i "Morning, Sensei."

    if dormwarfloor2win == True:
        i "My team won, in case you were wondering."
        i "No thanks to me, obviously."
        s "Doesn’t really matter if you were involved as long as you won."
        s "Looks like we’ll be staying in the same room for the beach trip, I guess."
        i "I’m probably not going to go. It doesn’t really sound like my sort of thing."
        s "Oh."
        s "Well, yeah. I guess that makes sense, then."
        s "Maybe we can do something on our own soon, then?"

        scene warsend24
        with dissolve

        i "Just us? You’re not inviting your girlfriend?"
        s "Io-"

        scene warsend25
        with dissolve

        i "I’m joking, sorry."
        i "Yeah...I’d be really happy to see you more, if that’s okay with you."
        i "And...sorry for sneaking in again. I wasn’t really thinking of how much trouble that could cause you when I did it."
        i "I swear to never tell another hotel employee that you’re my father ever again."
        s "Thank you for making such a strange and specific promise to me. I really appreciate it."
    elif dormwarfloor1win == True or dormwartie == True:
        i "My floor lost, in case you were wondering."
        i "Also, looks like Yuki’s daughter was able to “cooperate” before I was."
        i "No surprise there, of course."
        s "You should have come to the bar last night. It was..."
        s "Well, I don’t want to say {i}fun.{/i} But it was certainly interesting."

        scene warsend25
        with dissolve

        i "I can’t even function around girls in[school]. You really think I’d be better in a party setting where they’re all trying to talk to me and get me to “come out of my shell?”"
        s "No. But I would have accepted if you wanted to follow me around and cling to my sleeve or something."
        i "Yeah, I’m sure your “girlfriend” would have loved that."
        s "Io-"
        i "A joke, obviously."
        i "Though, I do think you should probably hurry up and toss her aside or she’ll just wind up going crazy and stalking you when you finally {i}do{/i} break up."
        s "She’s actually a really nice girl, Io."
        i "And I’m not?"
        s "Sure. You’re nice too."
        i "Well now you’re just lying to me. We all know that isn’t true."
        s "Okay, fine. You’re not nice to other girls. But you’re nice to me and that’s pretty much all that matters in my book."
        i "Unless I start belittling them and you have to scold me for it."
        i "You’re really striking out this morning, Sensei."

    scene warsend26
    with dissolve

    u "Io! Are you finally going to stop avoiding me now that the dorm war is over?!"
    i "Yes. I am finally going to stop avoiding you now that the dorm war is over."
    i "Did you have fun?"
    u "I had a lot of fun! But I would have had {i}more{/i} fun if you were there!"
    i "I {i}was{/i} there. I just wasn’t really doing anything."

    scene warsend27
    with dissolve

    u "That’s exactly the problem..."
    u "I wanted to do something fun with you..."
    i "Then let’s do something fun now."
    i "My aunt is working today, so I don’t have to hang out at the bathhouse."
    i "I’m also really hungry, soooooo..."

    scene warsend28
    with dissolve

    i "Maybe Sensei might want to come with us and finally get breakfast with me?"
    s "You’re not going to drag me to an amusement park afterward, are you?"
    u "I’m not tall enough to ride most of the rides, but I can hold your stuff and watch if you guys want to go on the adult ones."
    s "We’re not going to the amusement park, Uta."
    i "Sensei hates rollercoasters."
    s "I like food, though. So, sure. I’ll come get breakfast with you."
    s "After that, I’m going back home to take a nap, though."
    s "It’s surprisingly draining having to judge a series of strange [high_school] competitions."
    i "You’re really starting to sound old, Sensei."
    u "Come on, grandpa. It’s time for your chemo."
    s "Uta, please stop saying things like that..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "We manage to slip away from the gathering without anyone else seeing us and head over to some random diner none of us had been to before."
    "Everything there was exceedingly average, but it was still an enjoyable outing regardless."
    "Sure, Uta talked way more than anyone should ever talk...but it complemented the type of person both Io and myself are."
    "And weirdly enough, all of it felt completely natural."
    "The two of them make a strange combo, but the fact that they’re able to get over things like Io constantly disappearing and avoiding Uta as if it’s routine really shows a lot about their friendship."
    "Or what I imagine their friendship to be."
    "I’m sure things are a lot more complicated than that."
    "But I guess that’s something I’ll learn in time."
    "For now-"
    "I’m just glad I can finally relax."

    play sound "dooropen.mp3"
    scene bedroom_noon
    with dissolve

    "I walk into the bedroom and instinctively search for the air conditioner I’d grown used to over the last two nights."
    "It’s not there."

    scene black
    with dissolve

    "I go to sleep warm."

    "{i}Congratulations on completing the first ever Super Mega Ultimate Dorm War!{/i}"
    "{i}As soon as you wake up, everything will go back to normal and you’ll be able to act on your own again.{/i}"
    "{i}Thank you for surrendering two days of your seemingly infinite time in Kumon-mi.{/i}"

    $ renpy.end_replay()
    $ dormwar17 = True

    "………"
    "……"
    "…"
    "I wake up just as the sun begins to set."
    "What do I want to do with the rest of my day?"

    jump asmenu

label day333:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
s "I sincerely thank you for the massive erection you have given me, but I am not nearly drunk enough to have reciprocative inebriated sex with you next to a girl with a minor concussion."
    c "And you call yourself a penis."
    s "I have never once called myself that."
    to "Oh dear...I...suddenly feel...very nauseous."

    scene chikatoukafun21
    with dissolve

    c "And I...suddenly feel...very sleepy..."
    c "Guh..."
    s "Oh no."
    c "Goodnight...Sensei..."

    scene black
    with dissolve2

    "Chika passes out and...I am suddenly at a loss for exactly how I am supposed to handle this situation."
    "The two of them are passed out, half naked, and incapable of walking."
    "And what’s even worse is that I didn’t even get to choose a winner yet."
    "But that’s okay."
    "Because an amazing idea just popped into my head."

    play sound "phonebeep.wav"
    "I slide my phone out of my pocket and tap the name of the only person I can trust at a time like this."
    "……"
    "…"
    play sound "phonebeep.wav"

    s "Hey. "
    s "I need your help with something. "
    s "And I need you to never breathe a word about this to anyone else."

    "………"
    "……"
    "…"

    scene chikatoukafun22
    with dissolve

    no "…"
    s "…"
    no "Long night?"
    s "I...didn’t know who else to call."
    no "You certainly made the correct decision."
    no "Just...to address one of the several elephants in the room, though..."
    no "These two {i}were{/i} conscious when they arrived, correct?"
    s "I know what you’re thinking and no. I did not do this."
    no "Then...I shall treat them as life-sized dolls and dress them back up before dragging them home."
    s "Would you...also be okay with informing them of who the winner is?"
    no "Is...is the real winner not you?"
    s "This was far from a victory for me."
    s "The real winner is..."

    menu:
        "Chika wins":
            $ dorm1warpoints += 1
            $ chikalingeriewin = True

            s "Chika. "
            s "She deserves it after the show she put on."
            no "You know, it would be really nice if you’d invite me to these sorts of “shows” before they happen from now on."
        "Touka wins":
            $ dorm2warpoints += 1
            $ toukalingeriewin = True

            s "Touka. "
            s "She..."
            s "She did her best."
            no "I’d imagine her best would involve {i}slightly{/i} less underwear."

    no "But yes. I will tell her."
    no "And, Sensei..."
    s "Yes, Nodoka?"
    no "I want you to know that you never cease to amaze me."
    s "Yeah..."
    s "Thanks..."

    scene black
    with dissolve2
    stop music fadeout 5.0
    $ renpy.end_replay()
    $ chikalust15 = True
    $ chika_lust += 1

    "{i}Chika's lust has increased to [chika_lust]!{/i}"
    "………"
    "……"
    "…"

    $ totaldays += 1
    $ day -= 6
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
    else:
        "ERROR ADVANCING DAYS"

    "[totaldays] Days have passed..."

    jump dormwar17
...
```