# Lavender's Blue
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach14&go=Go)


Part of event chain [Hot Water](./makotolust20.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: secondbeach14
* Group: Main
* Triggered by label: makotolust20

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach14:
    play sound "static.mp3"
    scene dust with flash
    stop sound
    stop music

    "Nothing lasts forever."
    "But there are several things that last a very long time."
    "I hope you are one of them."

    play sound "static.mp3"
    scene lavender1
    with flash
    stop sound
    play music "undersea.mp3"

    ya "Grasping at straws! Whichever ones we can reach!"
    ya "Curling our fingers around them like the necks of tiny birds and stripping them of their skin!"
    ya "Pressing our lips to the plastic and {i}sucking.{/i} Sucking as if our life depends on it!"

    scene lavender2
    with dissolve

    ya "But nothing ever finds its way into our mouths."
    ya "Not a single drop of water, nor stray insect seeking moisture. Crawling in through the tube and down into your intestines. "
    ya "Turning your body into a home when home is nowhere else."

    scene lavender3
    with dissolve

    ya "And then dying because it's never able to find its way out."

    play sound "static.mp3"
    scene dust2 with flash
    scene dust3 with flash
    scene dust4 with flash
    scene dust5 with flash
    scene lavender4 with flash
    stop sound

    ya "HELLO"

    play sound "static.mp3"
    scene lavender5
    with flash
    stop sound

    ya "Hello."
    s "Hey, Yasu. Why aren’t you dressed in your swimsuit like everyone else?"

    scene lavender6
    with dissolve

    ya "Why, because nightfall is just moments away."
    ya "We were fortunate enough to have His Holiness intervene and provide us several hours of warmth, but his power can only do so much in the winter time. "
    ya "Once the sun is gone, he will slumber once more. "
    ya "And everything will go back to being a heaping pile of shit."
    s "Well, at least your religion is cool enough to let you swear."

    scene lavender7
    with dissolve

    ya "{s}Hehashehehahehfsduijhvboidfbipkfgbhnujfgbpofdgbvoi{/s} Haha, you’re so funny. "
    s "That aside, I guess it {i}is{/i} about time to start thinking about lunch. "

    if makotolust20 == True:
        s "I lost a few hours to an...interesting get together with Makoto, so I didn’t even realize that morning was over until just a few minutes ago."
    else:
        s "I lost a few hours when I fell asleep in my room, so I didn’t even realize that morning was over until just a few minutes ago."

    scene lavender8
    with dissolve

    ya "Lunch?"
    s "Yes. As I just said, I didn’t realize how quickly the morning went by and-"
    ya "Sensei, were you not listening to me?"
    ya "I said nightfall is just moments away. "
    ya "There will be no lunch until tomorrow, when all returns to form. "
    s "Is your weird god just...skipping over the afternoon as payment for making it warm or something?"

    scene lavender9
    with dissolve

    ya "Yes! Isn’t it wonderful?"
    s "No. And if his powers go away once night comes or whatever, why would he make night come {i}sooner{/i}?"
    ya "The answer to that is simple."
    ya "Because everything hurts a little less when you are asleep."
    s "…"
    s "That’s..."

    play sound "static.mp3"
    scene lavender10
    with flash
    stop sound

    ya "King of all kings! Child of man!"
    ya "Show us how fleeting it is to be!"
    ya "O world! In our final moments, grant us the serenity to accept that your word is law!"
    ya "That all outcomes in all worlds flow into you! And in return, you into us!"
    ya "Let the night come!"
    s "Yasu-"

    play sound "static.mp3"
    scene lavender11
    with flash
    stop sound

    ya "It is here!"
    s "What?..."
    ya "Do you see?!"
    ya "Do you feel His power?!"
    ya "Wrapping around your feet and dragging you into his mouth?"
    ya "Only those fortunate enough will be swallowed whole- and as all I say is prophecy, all you see is true!"
    ya "All you feel is true! Your experiences! "

    if bonus == True:
        ya "The [young_girls] you fill with your unblessed seed! Forever contaminating them until they elect to be cleansed!"
    else:
        ya "It all comes falling down!"

    play sound "static.mp3"
    scene lavender12
    with flash
    stop sound

    ya "I CAN FIX YOU"

    play sound "static.mp3"
    scene lavender11
    with flash
    stop sound

    ya "I can fix you."
    ya "The same way I can fix them."
    ya "I can fix everything."
    ya "Each and every day is a collection of time...but what do we do when time runs out?"
    ya "O...if only it were as simple as filling a room full of clocks so that time would last forever."
    ya "Maybe then, we would understand how insignificant our existence is."

    play sound "static.mp3"
    scene dust5 with flash
    scene dust4 with flash
    scene dust3 with flash
    scene dust2 with flash
    scene lavender13 with flash
    stop sound

    ya "I can not see the moon, nor would I be able to reach it if I could."
    ya "But if my body ever became colossal, I would swallow it whole like a prescription pill."
    ya "Not because I believe I need to be cured, but because those unwilling to search deep within themselves for the answer to everything-"
    ya "Those people do not deserve such beauty."
    ya "Ahh."
    ya "Perhaps the reason I can’t see it is because the moon itself is unworthy of me."
    ya "Can you see it, Sensei?"
    ya "Can you see the moon?"
    s "…"
    ya "…"

    "As much as I want to say something witty right now, I think there might be an actual problem with Yasu."

    "It’s obviously not the first time she’s been this...emphatic about religion, but it’s the first time I’ve felt like she might {i}actually{/i} do something dangerous."
    "What that would be, I have no idea. "
    "But I can’t just let her stand out here in the dark, yelling things to herself."

    s "…"

    "Ugh. Time to be a real adult."

    s "Yasu, come on. Let’s go find Touka and the rest of the girls."
    s "I’m sure they’re all currently freaking out about the immediate switch to night, so you might be able to calm them down by...telling them about the...power or whatever."
    ya "None of them will know."
    s "I’m sorry?"
    ya "To everyone else, this will have been a normal day. "
    s "Oh, okay. So {i}I’m{/i} the only one who had to miss out on lunch. Thank you, mysterious lunch-hating god."
    s "Now, come on. We can’t just stand out here."
    ya "Shh. Listen closely."
    ya "Off in the distance. "
    ya "Do you hear that?"
    s "Hear what? What are you talking about?"
    ya "The sound of another thread."

    scene black

    ya "A string snapping."

    $ yasu_love += 1

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "………"
    "……"
    "…"

    scene lavender14
    with dissolve2

    t "Emerald Guard- "
    t "No...Molly."
    t "Nightfall has already come and you’ve yet to leave your futon."
    t "If you are not feeling well, I would be happy to borrow this resort’s kitchen to make you soup."
    mo "For the last time, Kendo Princess...soup isn’t going to make me feel better."
    mo "If I’m dragging {i}you{/i} down as well, feel free to go out and have fun with the rest of the girls."
    t "But...I don’t share the same bond with them that I do with you."
    t "I believe the best thing for me to do is remain by your side until you are feeling better."
    mo "Well...you’re probably gonna be here for a while then. I’m not sure if this debuff is one that will come off so easily."
    t "Can I...at least get you a drink?"
    t "Humans can go a surprisingly long time without food, but just several days without water is enough to kill a man."
    t "And while you are not a {i}man{/i}, I believe the same rule applies to women."

    scene lavender15
    with dissolve

    mo "Feckin’ Hell. ‘Least my roommate will always be on my side."
    t "You...are still upset about Nithhala?"

    scene lavender16
    with dissolve

    mo "I just..."
    mo "Ngh..."
    mo "I just want her to...acknowledge me, you know?..."
    t "I am having a hard time understanding your feelings for her. But if you are worried that she does not like you, I would disagree."
    t "The two of you are together rather often for characters with opposing viewpoints and backgrounds."
    t "If she truly did dislike you, I can’t imagine she would continue-"

    scene lavender17
    with dissolve

    mo "I’m not talkin’ about the feckin’ backgrounds, Tsuneyo! I love her!"
    mo "I love her and she doesn’t love me! That’s all you need to know! "

    scene lavender18
    with dissolve

    t "…"
    mo "Ngh...I’m sorry...I...I just..."
    t "I do not understand love or how it works..."
    t "But I do understand that I would have struggled greatly without your help in getting adjusted to life outside of noodles. "
    t "And because of that, I believe that anyone who does not return those precious feelings of yours is making a terrible mistake. "
    t "I will go get you water and a bar of protein. Please at least have something to drink. "

    scene lavender19
    with dissolve

    mo "Tsuneyo...I’m really sorry..."
    mo "Can you maybe just go for a walk or something and come back later? I promise I’ll be...a little better then..."
    mo "I just want some time to be by myself and get my mind off of things..."
    t "…"
    t "I understand."
    t "Please do your best to get rid of your debuff. "
    t "I will be near water if you need me."

    scene lavender20
    with dissolve
    play sound "slidedoor.mp3"

    mo "Ngh..."
    mo "There’s water everywhere, idiot..."

    scene black with dissolve2

    "………"
    "……"
    "…"

    scene lavender21
    with dissolve2

    mo "{i}*Sniff*{/i}"
    mo "Is it really that late already?..."
    mo "I really {i}have{/i} been in bed the entire day."
    mo "Haven’t even logged in to do my dailies yet. Gonna be up all night at this rate."
    mo "Stupid Rin. Making me cry for like the...millionth time instead of...coming over to cheer me up or something."
    mo "Some best friend she is."
    mo "Too wrapped up in some girl with...stupid hair to even realize that I like her."
    mo "Just kidding. Otoha’s hair is nice. But she probably hasn’t even realized that Rin only dyed {i}hers{/i} so that they could match."
    mo "Stupid...stupid Rin. Being all...stupid."
    mo "..."
    mo "I should probably apologize to Otoha for flipping out on her."

    scene lavender22
    with dissolve
    play sound "slidedoor.mp3"

    r "…"
    mo "…"
    mo "Rin?"

    scene lavender23
    with dissolve

    r "Oh, hey. I didn’t think you were awake."
    r "Have you seen my phone by any chance? I think I left it in here when I dropped by earlier."
    mo "You...came by earlier?"

    scene lavender24
    with dissolve

    r "To meet up with Otoha and Nodoka, yeah. You were dead asleep, though, so you probably didn’t even realize it. "
    mo "No...I had no idea..."
    mo "I’ve actually been...here all day because of-"

    scene lavender25
    with dissolve

    r "Molly, come on. We can talk about our fight or whatever {i}after{/i} the beach."
    r "I’ve gotta keep my mind clear tonight, and getting into this now would just make things worse."
    mo "Rin-"
    r "Have you seen my phone or not?"
    mo "…"

    scene black with dissolve2

    "………"
    "……"
    "…"

    scene lavender26
    with dissolve

    mo "…"
    r "…"
    r "What? Why are you looking at me like that?"
    mo "I’m...trying to figure out the best way to say this..."
    r "Say what? Because that kind of makes me think it has nothing to do with my phone."
    r "Which {i}then{/i} makes me think that it’s going to be about our argument and how we both pushed each other's buttons."
    r "And now I’m going to spiral into thinking about a whole bunch of stuff I’m trying to put off until {i}after{/i} my plans tonight."
    mo "Could..."
    mo "Could you maybe...{i}cancel{/i} those plans?..."
    mo "For me?"
    r "…"

    scene lavender27
    with dissolve

    r "Molly, what is this?"
    mo "What...do you mean?"
    r "I mean you’re acting weird by even your standards. And you’re kind of the queen of weirdness sooooo, that’s kind of saying a lot."
    mo "I..."

    scene lavender28
    with dissolve

    mo "Tell me more about...what you think of me..."
    r "Uhhhhhhhhhhhhh...what?"

    scene lavender29
    with dissolve

    mo "Let’s just...talk."
    mo "No one is going to come back here for a while, so...we can talk about...all kinds of stuff..."
    r "…"
    mo "…"
    r "Can I have my arm back, please?"
    mo "…"

    play sound "static.mp3"
    scene lavender30
    with flash
    stop sound

    r "Yo, what the fuck?!"
    mo "Why don’t you look at me like a normal girl?! "
    mo "Why do you get nervous around everyone except me?!"
    r "What the fuck are you-"
    mo "Kiss me!"

    scene lavender31
    with dissolve

    r "Jesus, Molly! What the fuck is your problem?!"
    mo "You! You’re my problem! "
    mo "We’re alone! Get nervous! "

    scene lavender32
    with dissolve

    r "I don’t have time to get nervous when I have to fucking wrestle a tiny Irish girl off of me!"
    r "Let go!"
    mo "I don’t want to! I want you to...to cancel your plans! And spend time with me instead!"
    r "Get the fuck away from me, dude! This is so weird!"
    mo "No! "
    r "Yes!"
    mo "No!"
    r "Fucking...yes!"

    scene black
    play sound "thump.mp3"

    "It’s funny how love works sometimes."
    "Out of nowhere, you just start falling."
    "Then, before you even know it-"

    play sound "static.mp3"
    scene lavender33 with flash
    stop sound

    "You wind up on the ground."
    "Not dead, but not entirely alive either."
    "In fact, the vast majority of falls wind up with something or someone getting damaged in some way."
    "And despite having {i}her{/i} fall cushioned, I think we all know who took more damage from this one."
    "Love’s not only funny, but ironic."
    "Or, at least it is this time."

    mo "Cancel your plans...stay with me..."
    r "And do what?!"
    mo "Anything."
    mo "I just...want you here..."
    r "Yeah! I can fucking see that! But you’re being a total creep about it and I have shit to do!"

    scene lavender34
    with dissolve

    mo "Can’t you do it later? I need you right now."
    r "What in the everloving fuck are you on, dude? "
    mo "Good question..."
    mo "Um..."
    mo "Desperation?..."

    scene lavender35
    with dissolve

    r "Molly...get the fuck off of me."
    r "I don’t know what you want, but-"
    mo "How do you not know? How much more obvious do I need to make it?"
    mo "Just kiss me and...and see that-"
    r "I already fucking kissed you."
    r "And hey, guess what? I didn’t like it."
    mo "But...why?..."
    r "Because."
    r "You."
    r "Are."
    r "My."
    r "Friend."
    r "And if you want to {i}keep{/i} being my friend, you will get the fuck off of me right now."
    mo "But..."
    r "Molly. I don’t want to fucking hear it. "
    mo "But I..."
    r "I know what you’re going to say and...again...I don’t want to hear it."
    mo "…"

    play sound "static.mp3"
    scene lavendermisc
    with flash
    stop sound

    "Lavender's blue, dilly, dilly "
    "Lavender's green "
    "When I am king, dilly, dilly "
    "You shall be queen"
    "Who told you so, dilly, dilly "
    "Who told you so? "
    "'Twas my own heart, dilly, dilly "
    "That told me so."
    "Lavender's green, dilly, dilly "
    "Lavender's blue "
    "If you love me, dilly, dilly "
    "I will love you"

    scene black

    "A series of dots."

    scene lavender36
    with dissolve

    mo "Rin! I’m sorry! For yelling at Otoha and...and for tackling you!"
    mo "And for being an all around bad friend tonight! But...I can’t help it! "
    mo "I just want you to be happy! That’s all!"
    mo "I don’t want this to make things weird! I want to take it all back!"
    mo "I-"
    r "Chill."

    scene lavender37
    with dissolve

    r "I get it. "
    r "In fact, if there is literally {i}anything{/i} I get, it’s this exact thing."
    r "But..."

    scene lavender38
    with dissolve

    r "I don’t like you, Molly."
    r "And I {i}really{/i} don’t like how you acted tonight. It was fucking creepy and totally unlike you."

    scene lavender39
    with dissolve

    mo "I’m such an idiot...I’m such an idiot...I’m such an idiot..."
    r "Don’t...go beating yourself up about it..."
    r "You did a shitty thing, but...you’re a good friend when you’re not...jumping on me and shit."
    mo "I’m so sorry, Rin...I really am...Please please please please please don’t hate me..."

    scene lavender40
    with dissolve

    r "I won’t..."
    r "But...I think the two of us could probably use a little space for now..."
    mo "Oh my God...I’m sorry...I’m so, so sorry..."
    r "Yeah, you’ve mentioned that."
    r "Listen, I’m just gonna...go now. But it’ll be okay."
    r "I won’t tell anyone what happened and if anybody asks why we’re not talking or whatever, we can just...use the D&D thing as an excuse."
    r "Which...also makes a lot more sense now, by the way. So...sorry."
    r "That must have been a...really shitty position to be in."

    scene lavender41
    with dissolve

    mo "{i}*Sniff*{/i}"
    mo "Well...DMing is a tough job as-is, so..."
    r "…"
    mo "…"
    mo "Good luck, Rin..."
    r "Thanks..."
    r "Gonna need a...hell of a lot of it."

    scene black
    with dissolve2

    "Landing on the ground and not having your insides splattered all over the cement means that you can still pick yourself back up and start walking again."
    "Probably not right away because of all of the bone fragments that would need to be removed-"
    "And, who knows? Maybe you’ll need a new bionic leg or something like that."
    "But as long as you’re alive, you can keep on going."

    $ renpy.end_replay()
    $ secondbeach14 = True

    jump secondbeach15

label secondbeach15:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
"Well...okay."

    scene makotolusttwenty34
    with hpunch

    mak "Aaaaahhhhot! This water is...the worst!!!"
    mi "Uh..."
    mi "You know what? Maybe I’ll...go ask ‘em to turn it down a bit. You seem to be having a pretty...rough time."
    mi "You sure you’re okay? You’re normally really good with hot water."

    scene makotolusttwenty35
    with dissolve

    mak "Yup!...All good here!"
    mak "But you can...definitely go tell the...desk people a...thing..."
    mi "Uhh...yeah. Let’s see...where was the desk again?"

    scene makotolusttwenty36
    with dissolve
    play sound "water1.mp3"

    mak "Oh my...fucking god..."

    scene makotolusttwenty37
    with dissolve

    mak "Ahh...hahh...ah!"
    mak "Hurry up and...fucking cum already!"
    s "Oh, I’m probably not going to. "
    mak "Why the fuck not?!"
    s "Because you stopped jerking me off as soon as I started touching you."
    s "Besides, underwater handjobs are nice, but I don’t think they're nice enough to really finish the job."
    s "You can just go ahead and-"

    scene makotolusttwenty38
    with dissolve

    mak "Ahh! Fuck! Oh my...god!"

    "Makoto lets go of my cock and uses both of her hands to press down against the one I’m using to finger her."
    "Her efforts don’t really do much because of the angle, but I humor her by amping up the speed and plunging away at her insides, not caring about the sound of the splashing at this point."

    mak "I’m gonna cum...I’m gonna cum..."
    mak "I’m...ah..."

    with sexfade
    with sexfade
    scene makotolusttwenty39
    with cumflash
    with hpunch

    mak "Ahh~ [makotomaster]...[makotomaster]..."
    mak "Hah...hah........ahh~"

    "Despite the build up, Makoto’s climax is one of the more gentle ones I’ve seen come out of her."
    "It’s really just a series of high pitched squeaks and moans and, before long, the two of us go back to treating it like none of this ever even happened."

    scene makotolusttwenty40
    with dissolve
    play sound "water1.mp3"

    mak "Well, then. "
    mak "That was the...opposite of how I thought this was going to turn out."
    s "You got over the fact that I wasn’t going to cum a little too easily. That hurt my feelings."
    mak "I wonder how long Miku is going to be gone for. This water really is a little too hot."
    mak "Though, I’m sure my body heat has been rising from other things as well, so..."
    mak "I’m sure it’ll get better."
    s "…"

    scene black
    with dissolve2

    "In the end, I wind up having to leave the hot spring with an erection."
    "And due to the fact that getting out at the same time as the girls would have revealed a dramatic lack of clothing on my part, I had to stay in a lot longer than I anticipated."
    "Am I upset that I had to use essentially what was my entire morning on this? A little."
    "But it’s not like there are a limited number of beach trips or anything."
    "Time is meaningless in Kumon-mi. The only thing it changes is the weather."
    "And even then, we managed to get a few hours of sunshine and warmth in the middle of the winter."

    play sound "water1.mp3"

    "I shrug to myself and exit the hot spring, grabbing my clothes out of a small locker at the door."
    "Then, without a plan on how to spend the rest of my day-"
    "I simply go back outside to see what awaits me there."
    "I’m sure that whatever it is will be more interesting than being alone."

    $ renpy.end_replay()
    $ makoto_lust += 1
    $ makotolust20 = True
    stop music fadeout 5.0

    "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
    "………"
    "……"
    "…"
    "…"
    "…"
    "I miss feeling whole."

    jump secondbeach14
...
```