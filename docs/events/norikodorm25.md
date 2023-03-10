# Loxosceles Reclusa (Noriko)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Noriko love greater than or equal to 25

* Event [That One FMK Scene](./convenience25.md) (Noriko) is completed)

* Day of week is not Wednesday



## Next events

* [Kirin: Temporary Bliss](./kirindorm25.md)
* [Main: Three Amigos](./christmastwo1.md)
* [Niki: Sisters](./nikiinvite1.md)
* [Niki: Dear You](./nikiinvite2.md)

## Event properties

* Id: norikodorm25
* Group: Noriko
* Triggered by label: norikodorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->norikodorm->norikodorm25

## Official wiki page

[Loxosceles Reclusa](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikodorm25&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label norikodorm25:
    play sound "knock.mp3"
    scene norikorestaurant1
    with dissolve

    "I knock on Noriko’s door and wait for her to answer."

    play sound "dooropen.mp3"
    scene norikorestaurant2
    with dissolve

    n "Sensei?"

    "But, to my surprise, she comes right on out and I don’t even have time to tell you about what I planned on doing here tonight."

    n "What’s up? What brings you over to my neck of the woods?"
    s "A better question is why were you so prepared to leave your room the moment I knocked?"

    scene norikorestaurant3
    with dissolve

    n "Would you believe me if I said I was just waiting around for you to show up?"

    if bonus == True:
        s "Yes, actually. You have proven to be rather...dog-like in the past."
        n "Bend me over and I’ll show you just how dog-like I really am. "
        n "I mean what? Who said that? Not me. I’m Noriko. A human girl."
        s "Well then, irrefutably human girl, what are you doing tonight?"
        n "Well, I {i}was{/i} going to go for a walk..."
    else:
        s "Yes, actually. You are unhealthily obsessed with me when my plan all along has been to set you on the right path toward a better future."

    scene norikorestaurant4
    with dissolve

    n "But {i}now{/i} I am going to change that plan entirely and invite you out to dinner!"
    s "You’re inviting {i}me{/i} out to dinner? How chivalrous."
    n "Chivalry is dead! Both sexes are on equal footing now and it’s okay for girls to ask guys out because relationships require equal effort on both ends and males should not be obligated to always strike first!"
    n "Also, I am hungry and there’s something I want to talk to you about!"
    s "Does it involve smashing the patriarchy?"

    if bonus == True:
        n "Is the patriarchy your penis?"
        s "In an extremely roundabout way...kind of?"
        n "Then...also kind of!"

        scene norikorestaurant5
        with dissolve

        n "To be completely honest, it really only {i}slightly{/i} involves your penis, but only as like a...concept. "
        s "You are inviting me out to dinner to discuss the concept of my penis?"
        n "In an extremely roundabout way...kind of?"
        s "Well, thankfully, that is one of a few topics I am incredibly well versed in. I hereby accept your invitation."
        s "Now, where are we going?"
    else:
        n "No."
        s "Oh."
        s "Then sure. I'm not a very good patriarch smasher anyway."

    scene norikorestaurant6
    with dissolve

    n "Soooo...you know that restaurant you went to with Nee-chan shortly after I found you and the hands on the clock of our romantic aptitude started ticking once more?"
    s "The hands of...what? Wait, are you talking about the place with the sausage fest?"
    n "No, no. I can’t eat sausage, remember? Vegetarian."

    if bonus == True:
        s "That is going to make the penis discussion very depressing for both of us."
    else:
        s "Oh, right. My apologies."

    scene norikorestaurant7
    with dissolve

    n "I’m talking about the fancier one. Where she opened up about her past and how she dealt with being apart from you and...all that stuff."
    s "You sure know a lot of what Niki and I talk about despite never really being there for any of it."
    n "Well, it’s not like she really has anyone {i}else{/i} to talk to about...anything. "
    n "And I guess she’s still just kind of used to talking to me about all you-related stuff since that’s how things were back in the old days too."

    scene norikorestaurant8
    with dissolve

    n "But now it’s my turn!"

    if bonus == True:
        n "It’s not fair that {i}she{/i} got to have you all to herself in some dimly lit, four star sex trap!"
    else:
        n "It’s not fair that {i}she{/i} got to have you all to herself in some dimly lit, four star restaurant!"

    n "The time has come for you to hear my side of the story!"

    scene norikorestaurant9
    with dissolve

    n "And...for me to maybe feel like I’m not just chasing after a ghost again..."

    scene black
    with dissolve2

    "I take a moment to ponder over what Noriko meant by that, and confirm to myself that it’s likely about that “disappearing act” I put on a while back."
    "I don’t know how many times she needs me to remind her that I don’t know anything about what happened back then, but..."
    "I guess it wouldn’t be harmful to learn more about how things were for her when hearing Niki’s side didn’t cause me to malfunction in any way."
    "Even now that I’m starting to become a little more hesitant to get filled in on details of the past (Thanks, Maya), I’m almost positive that it’s only details about {i}me{/i} that have the chance of frying my brain."
    "And, if Noriko wants me to know about {i}her{/i}, after all, it’s not like I can avoid this forever."

    if bonus == True:
        "Every single detail I can learn and memorize about her brings me one step closer to getting her shirt off again."
        "And that’s why I’m here, after all."
        "..."
        "That’s..."

    stop music

    "We {b}WALK{/b} to the {b}RESTAURANT.{/b}"

    scene norikorestaurant10
    play music "samhain.mp3"

    n "Wow...I knew this place would be kinda nice based on what she said, but...this is a little fancier than I was expecting."
    n "I would have worn my {i}nice{/i} clothes if I had known it was going to be a place like this."
    s "You? Nice clothes? Impossible."

    scene norikorestaurant11
    with dissolve

    n "Hey. Don’t go forgetting that I was always the one who wanted to dress up when we were younger. It was Nee-chan who was always trying to stay in sweatpants for as long as physically possible."
    n "Did most of that desire to dress up come from an overwhelming need to impress you? Of course. But even though I rarely do it anymore, I still like feeling pretty from time to time."
    s "Well you certainly pulled off that dress for your parents’ restaurant, so I can see it."

    scene norikorestaurant12
    with dissolve

    n "Do you think they have falafel here?"
    s "Probably not, Noriko. "
    n "They should have falafel here. I’m going to speak to the manager."
    s "Please don’t. The less attention I have for being on a date with a [teenage]girl, the better."
    k "Friend!"

    scene norikorestaurant13
    with fade

    if bonus == True:
        k "You have found yet another [young_girl] to waste away your days with! How exciting!"
    else:
        k "You have found yet another human female to waste away your days with! How exciting!"

    k "And this one looks just like the cotton candy girl! But spikier and less confident!"
    s "Kaori, how are you balancing those wine glasses on a plate you’re holding sideways?"
    k "It is not sideways! That is just what you imagine it to be! "
    k "The plate is a plate! And the glass tubes of fermented grape blood stand as tall as trees!"
    k "Drink them and you shall become them! Grapes!"
    s "Okay, Kaori."

    scene norikorestaurant14
    with dissolve

    k "Are you in trouble, {i}smaller{/i} cotton candy human?"
    n "I’m good! I was actually just wondering if you had falafel here, though. Or like...maybe portobello burgers or something? "
    s "Noriko, they don’t-"
    k "Spiced bean circles and cruelty free fungus burgers for the pink one! Thank you for your contribution to the animal kingdom!"
    s "Okay, then. I guess they do have...whatever you ordered after all."

    scene norikorestaurant15
    with dissolve

    k "Has your tongue signaled to your brain what it wants to taste yet, Friend?"
    s "I’ll have-"
    k "I understand! I will get that for you sooner than you can say “loxosceles reclusa!”"
    s "Loxosceles reclusa."

    scene norikorestaurant16
    with dissolve

    k "Ah! Too quick! Stop doing the words!"
    s "Loxosceles reclusa."

    scene norikorestaurant17
    with dissolve

    k "MY POWER WANES! I GROW WEAKER WITH EACH UTTERANCE!"
    k "GOODBYE FRIENDBURGER. ENJOY DEVOURING THE HAIR OF YET ANOTHER FEMALE."

    scene norikorestaurant18
    with fade

    n "Are you really going to eat my hair, Sensei?"
    s "What? No."
    n "Because you can if you want. I don’t mind."
    s "You definitely should mind. That’s not a normal thing people do."

    if bonus == True:
        n "No. But I was watching My Strange Addiction with Kirin the other day and there was this one guy who had sex with those giant blow up pool animals. "
    else:
        n "No. But I was watching My Strange Addiction with Kirin the other day and there was this one guy who was {i}really{/i} into those giant blow up pool animals. "

    n "All things considered, I think wanting to eat my hair is pretty normal by comparison. Besides, it grows back pretty quickly anyway."
    n "I think it’s the color. It sounds easier for pale skin to produce pink hair than it would be to produce like black or...brown or whatever."
    s "Why are you still talking about this?"

    scene norikorestaurant19
    with dissolve

    n "Becaaaaaaaaause...I’m nervous?"
    n "Obviously we’ve been hanging out a lot lately and...it’s starting to really set in that you’re {i}back{/i}...but this is the first like, {i}real{/i} date we’ve been on."
    n "I was doing okay until you called it that a few minutes ago, but ever since then I’ve just been like, “Holy shit. I’m on a date with Sensei. It’s finally happening.”"
    s "So obviously, the best course of action is to start a conversation about eating hair in order to make sure the date is a success."

    scene norikorestaurant20
    with dissolve

    n "Obviously. I mean, it’s better than bringing up something like politics or our stances on whether or not circumcision is cruel."

    if bonus == True:
        s "If that’s your idea of a segue into the “concept of my penis,” I would like to take this moment to commend you for near flawless execution."
    else:
        s "None of these are good conversation topics. Where is Kaori? I want the bill."

    n "I’m just trying to stop shaking, to be totally honest."

    scene norikorestaurant21
    with dissolve

    n "I learned this trick where if you stop crossing your arms and legs and just kinda sit up straight and regulate your breathing, it helps with nervousness."
    n "I figure if I just keep this up for the next three hours or so, I’ll finally be able to come out and ask you what I’ve been meaning to ask you since the beach."
    s "I highly doubt we’re going to be here for that long, so why don’t you just go ahead and start filling me in on your super secret backstory until then?"

    scene norikorestaurant22
    with dissolve

    n "Hah..."
    s "…"

    if bonus == True:
        n "You won’t be upset if there’s actually minimal penis in the story, would you? I know I lured you over here with promise of that being a big thing, but it’s really not."
        s "It definitely is."
        n "No, it’s-"

    scene norikorestaurant23
    with dissolve

    if bonus == True:
        n "Oh, like actual size. "
        n "Yeah. In that regard, it is {i}definitely{/i} a big thing."
        n "I just mean that the whole...sexually explorative yet still nervous Noriko isn’t as important as the...frantic lost sheep Noriko of the past."

    n "I’m sure Niki told you about how she went through that whole period of depression and reinvention stuff after you left, right?"
    s "Right. And it got significantly darker than I ever expected it to."

    scene norikorestaurant22
    with dissolve

    n "What happened with me really wasn’t all that {i}dark{/i} by comparison."
    n "If anything, it was probably one of the most active parts of my life."
    n "You see, I wasn’t like Nee-chan in the fact that you weren’t completely opposed to seeing me anymore like you were with her."
    n "And once you let me back into your life, I was ecstatic. "
    n "I saw an opportunity to try and pull you back, little by little, while getting closer to you at the same time and showing you that I was...smart."
    n "Smart and fun and lovable. Like a little sister cross bred with what I imagined your dream girl would be. And for a while, I felt like we really {i}were{/i} in a good place."
    n "So good that part of me wanted to forget you and Nee-chan were ever in love in the first place...and that you were like my secret prince or something along those lines."
    n "Little by little, your name stopped coming up back at home. Not just because Nee-chan couldn’t see you anymore, but because I wanted to keep you all to myself."
    n "So I’d wake up on the weekends, make myself look as pretty as I could, and wait patiently by the stairs for my parents to drive me over to that grody, crumbling building where you taught me so many things."
    n "It was like a second home. A castle, even. A place for my prince and me to be alone."
    n "And even if it wasn’t the most desirable looking building in all of Kumon-mi, I didn’t care. Because for a few hours every week, it was the most beautiful place in the whole wide world."

    play sound "static.mp3"
    scene norikorestaurant24 with flash
    stop sound

    n "Lots of girls came and went over that short period of time- probably due to a mix of exactly what you were teaching and where you were teaching it."
    n "And I would have been happy if things stayed that way forever."
    n "I would have waited until you got an actual teaching job and then enrolled at whatever[school] hired you, no matter how far away it was."
    n "But, of course, a nasty streak of poor luck landed somebody else in that same exact castle of ours."
    s "..."
    n "..."

    play sound "static.mp3"
    scene norikorestaurant25
    with flash
    stop sound

    n "I liked Maya. I really did. "
    n "I thought she was cool and...really, {i}really{/i} mature for her age."
    n "She reminded me a lot of you."
    n "And I guess she reminded {i}you{/i} of you too, since you took to her immediately."
    n "Soon enough, the castle for two turned into a castle for three."
    n "But every time I tried to move closer, the same way I’d been doing since I met you, it would be like you’d just move even further away in response."
    n "And then one day...you moved further away than I ever expected you to."
    n "It came out of nowhere and, I won’t lie, I was crushed."

    play sound "static.mp3"
    scene norikorestaurant24
    with flash
    stop sound

    n "But unlike Nee-chan, who was content wallowing in self-pity forever, I was going to do something about it."
    n "I took it upon myself to go out and find you because I didn’t think you’d ever leave if you really had a choice."

    play sound "static.mp3"
    scene norikorestaurant26 with flash
    stop sound

    n "I looked everywhere. Or at least as many places a girl with access to only public transportation and a capped data plan on her phone could look."
    n "But Kumon-mi’s a big fucking place, Sensei. And even bigger when you have no idea where you’re going."

    play sound "static.mp3"
    scene norikorestaurant26 with flash
    stop sound

    n "But then...I fucking found you."
    n "Out of the window of a bus in the old district, I caught you from the corner of my eye [[redacted] with [[redacted]."

    play sound "static.mp3"
    scene norikorestaurant27 with flash
    stop sound

    n "I begged the driver to stop so I could get off and chase you down and wrap my arms around you and ask you to come home."
    n "But of course, {i}she{/i} [[redacted]."

    play sound "static.mp3"
    scene norikorestaurant28 with flash
    stop sound
    stop music
    play music "soda.mp3"

    n "I couldn’t believe it. Here I was just inches away from finally finding you and [[redacted]."
    n "[[redacted]"
    n "{b}STOP PLAYING LESSONS IN LOVE{/b}"

    play sound "static.mp3"
    scene norikorestaurant29 with flash
    stop sound
    play music "shiningstarvocals.mp3"

    "///////////////////EVENT IS NO LONGER IN SYNC WITH EXPECTATIONS"
    "///////////////////PLEASE ENJOY THIS COMPLIMENTARY ADJUSTMENT AS A THANK YOU FOR YOUR CONTINUED SUPPORT AS WE ATTEMPT TO REPAIR YOUR CONNECTION"

    play sound "static.mp3"
    scene norikorestaurant30
    with flash
    stop sound
    play music "phonering.mp3"
    $ renpy.pause(10, hard=True)

    "Would you like to phone?"
    menu:
        "Phone":
            if bonus == True:
                play sound "static.mp3"
                stop music
                scene norikorestaurant2 with flash
                scene norikorestaurant26 with flash
                scene norikorestaurant31 with flash
                scene norikorestaurant32 with flash
                stop sound
                jump restofnorikorestx
            else:
                scene black

                "///////////////////EVENT FAILED"

                $ renpy.end_replay()
                $ norikodorm25 = True
                $ noriko_love += 3

                "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
                "………"
                "……"
                "…"

                if day >= 6:
                    jump endofsat
                else:
                    jump endofweekday
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label norikodorm:
    if noriko_love >= 5 and kirindorm10 == True and convenience1 == True and norikodorm5 == False:
        jump norikodorm5
    if noriko_love >= 10 and convenience5 == True and kirindorm20 == True and norikodorm10 == False:
        jump norikodorm10
    if noriko_love >= 20 and norikospecial20 == True and norikodorm20 == False:
        jump norikodorm20
    if noriko_love >= 25 and convenience25 == True and day != 3 and norikodorm25 == False:
        jump norikodorm25
...
```