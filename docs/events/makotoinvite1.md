# Declaration of War
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotoinvite1&go=Go)



## Event preconditions
✅Event "[Makoto: Quid Pro Quo](./makotolust5.md)" is completed (event=makotolust5)

✅Event "[Main: Slope Intercept Form](./day77.md)" is completed (event=day77)



## Next events
* [Makoto: Studious Teen Virgin](./makotoinvite2.md)

## Event properties
* ID: makotoinvite1
* Group: Makoto
* Triggered by label: makotoinvite
* Triggered by branch label: inviteover

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label makotoinvite1:
    play sound "phonebeep.wav"

    "I tap on Makoto’s name in my phone and wait for her to answer."
    "I figure that the two of us know each other well enough at this point that it will be fine for me to start inviting her over."
    "Of course, there is one glaring issue with that- and its name begins with the letter A."
    "If you said Alexander Graham Bell...you’d be wrong."
    "Because the answer is Ami."
    "Ami is the glaring issue."

    if invitetip == False:
        call invitetip from _call_invitetip

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    mak "Hello?"

    play music "normalday.mp3"

    s "Hey, Makoto. What are you up to?"
    mak "I’m just getting ready for work. Why? Did something happen?"
    s "Why are you assuming something happened?"
    mak "Well, you know I have work, so I doubt you’d be calling to invite me over or something."
    s "Does that mean you can’t come?"
    mak "Wait, wha-?!"

    if bonus == True:
        "I can hear a stack of things falling over in the background. Probably dildos or something because she works in a porn shop."
        "The thought of a stack of dildos falling on top of Makoto is almost enough to make me smile and I have to prevent myself from doing so in order to keep up my manly illusion."
    else:
        "I can hear a stack of things falling over in the background. Probably books because Makoto is a smart girl who loves to read and learn."

    mak "You...You’re inviting me over?!"
    s "I am. Are you able to get your mom to cover for you or something?"
    mak "Um...uhh! Hold on! I’ll go check!"

    "The sound of things falling over is quickly replaced by the sound of Makoto stomping up the stairs to where I imagine her mother is."
    "This must be the case because there is no other discernible reason for her to be using stairs right now."

    mak "Mom! I need you to watch the store!"
    mak "I...have to study!"

    if pornshop15 == True:
        maki "What? Can’t you just study in the shop? That’s what you always do."
        mak "Not today! Today is...different!"
        maki "But I’m so tiiiiiiiiiiiiired~"
        mak "Mom! Please! "
        maki "...UGH OKAY. "
        maki "I should probably take inventory anyway..."
        mak "THANK YOU."

    else:
        q "What? Can’t you just study in the shop? That’s what you always do."
        mak "Not today! Today is...different!"
        q "But I’m so tiiiiiiiiiiiiired~"
        mak "Mom! Please! "
        q "...UGH OKAY. "
        q "I should probably take inventory anyway..."
        mak "THANK YOU."

    "Makoto quickly runs back down (Or up? Probably down) the stairs before bringing the phone back to her ear."

    mak "*Ahem*"
    mak "Sensei? It appears that I will be able to come over after all."
    mak "As it turns out, I wasn’t even scheduled to work tonight. What a wonderful coincidence."
    s "But I just heard-"
    mak "Can you send me your address please?"
    mak "I can probably find it if I check the[school]-register, but this way seems a lot less weird."
    s "Yes. {i}A lot{/i} less weird."
    s "And also, expect a fight when you get there."
    mak "...Is that code for roleplay or something?"
    mak "I knew it was strange that you were inviting me over out of nowhere."
    s "No, I just mean that I can’t imagine Ami will take kindly to seeing you in the house."
    mak "I see."
    mak "Should I bring a weapon?"
    s "Do you...own a weapon?"
    mak "I can find one."
    s "Uhh, no. I think it’s fine. "
    s "Just...come over whenever you’re ready."
    mak "Will do! See you soon!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and start making my way home."
    "It would be pretty horrible if Makoto gets there first, so I need to...prep Ami in the meantime."
    "………"
    "……"
    "…"

    play sound "dooropen.mp3"

    s "I’m back..."

    scene makotofirstvisit1
    with dissolve

    a "Oh, welcome home!"
    a "Would you like dinner now? Or perhaps a bath instead?"

    scene makotofirstvisit2
    with dissolve

    if bonus == True:
        a "Or maybe...me?"
    else:
        a "Or maybe...your freedom?"

    s "None of the above."
    a "Aww, Sensei~ That’s so-"

    scene makotofirstvisit3
    with dissolve

    a "Wait, what?!"
    s "Ami, how much do you love me?"
    a "Obviously a lot!"
    s "Then I’m going to need you to listen very carefully."

    scene makotofirstvisit4
    with dissolve

    a "Is something going on?...You’re scaring me."
    s "It’s only going to get worse."
    a "Should I...sit down?"
    s "No. Stay right there."
    s "What I am about to say is going to shock you. But I need you to know that it won’t change anything between us. Okay?"
    a "Um...yeah...Of course."
    a "Are you sure everything is-"
    s "Sometime in the next few minutes-"
    s "Makoto is coming over."
    a "…"
    s "…"
    a "…"
    s "…"

    scene makotofirstvisit5
    with dissolve

    a "What?"
    s "Now, I need you to stay calm-"
    a "It’s so we can kill her, right?"
    a "You’d obviously never be stupid enough to invite {i}her{/i} to {i}our house{/i} unless it was to give me an early Christmas present...RIGHT?"
    s "It’s...to study."
    a "To {i}study{/i}? Do you really think I’m going to buy that? You’re barely even a teacher."
    s "No, I mean it. It’s just...for {i}me{/i} to study...Not her."

    "I decide to say the first thing that comes to mind."
    "Realistically, I probably could have just lied and told Ami that we were having the house fumigated or something and made her go back to the dorm but..."
    "Well, where’s the fun in that?"

    scene makotofirstvisit6
    with dissolve

    a "So, let me get this straight..."
    a "You invited Makoto over to {i}our house{/i} because {i}you{/i} apparently need help {i}studying{/i}?"
    s "Yes. And what’s with all of the italics?"

    scene makotofirstvisit7
    with dissolve

    a "Does it make you feel weak? Needing the help of a [teenage]girl?"
    s "You and I both know that Makoto is no normal [teenage]girl. She’s superhuman."
    a "More like super-stupid."
    s "Good one."

    play sound "doorbell.mp3"

    "…"

    a "Oh good. That must be the superhuman."
    a "Why don’t you answer the door, Sensei?"
    a "You must be eager to {i}learn{/i}, right?"
    s "I need you to promise me that we won’t have to hide a body by the end of the night."
    a "I’m obviously {i}not smart enough{/i} to pull off a murder, so I doubt that will be necessary."
    s "Good. I’m glad you understand."

    scene makotofirstvisit8
    with dissolve

    a "THAT WAS SARCASM, YOU JERK! I’M PLENTY SMART!"

    scene black
    with dissolve

    "I move to the door to let Makoto in. "
    "Right before I open it, I look back at Ami to make sure she hasn’t gone to the kitchen and grabbed any sharp utensils..."

    play sound "dooropen.mp3"

    s "Hey. Thanks for coming to {i}help me study{/i}..."
    mak "Help you study? What are you-"
    mak "Oh! Y-Yes! Are you...prepared for knowledge?!"
    s "{i}What the Hell is that? Just act natural.{/i}"
    mak "{i}Leave me alone! I’ve never been in a boy’s house before! I’m nervous!{/i}"
    a "CLASS...PRESIDENT..."
    a "!!!!!!!!!!!!!!!!!!!!!"

    "Oh boy. Here we go."

    scene makotofirstvisit9
    with dissolve

    a "You’ve got some real nerve showing up here, you know?!..."
    mak "Oh. Hello there, Ami. I seem to have forgotten you lived here."
    a "I don’t just {i}live{/i} here! I take care of my [uncle] here! We’re practically inseparable!"

    "Not true. We’re pretty separable."

    mak "Is that so? Because he didn’t even mention your name when {i}inviting me over{/i} today."

    "Also not true. I specifically mentioned that Ami lives here and that this exact thing would likely happen."

    a "That’s really funny because he’s never mentioned your name literally ever in the entire time I’ve known him."

    if bonus == True:
        a "Actually, that’s wrong. He did say “Wow, that Makoto girl sure is ugly!” this one time while I was washing his back in the bath."

        "Again, not true. That exchange never happened."
        "Why must girls always lie when fighting with one another?"
    else:
        s "That is only because you keep my mouth taped shut while I am home."
        a "Shut up, my little pogchamp."
        s "Sorry, Ami."

    scene makotofirstvisit10
    with dissolve

    if bonus == True:
        mak "Oh? Then perhaps I should wash his back tonight and the two of us can have a little discussion about you..."
    else:
        mak "Oh? Has anyone ever told you that taping the mouth of someone you love shut might actually just make them love {i}you{/i} less?"
        a "What?!"

    mak "And how your creepy obsession with your [uncle] is teetering on the verge of [incest] which, I’ll have you know, is illegal. Especially with someone who isn’t even-"
    a "Eyes up here, devil-woman."
    a "You will look at me when I am talking to you."
    a "Do I make myself clear?"

    scene makotofirstvisit11
    with dissolve

    mak "Oh, Ami! I forgot you were even there. Sorry about that."
    a "You didn’t forget me! You were just talking about me!"
    a "We are arguing! Forgetting me during a time like this isn’t even possible!"
    mak "Wait, who are you again?"
    mak "A maid? Gardener?"
    mak "If you don’t mind, I’d like to be left alone with my teacher."
    mak "He and I have {i}a lot of ground to cover{/i} tonight."

    scene makotofirstvisit12
    with dissolve

    a "You...thirsty...little...bitch..."

    "Oh, wow. Ami’s even angrier than normal this time."
    "I mean, of course something like this would be bound to happen with Makoto encroaching on her home-turf..."
    "But I’m starting to worry that the two of them might actually start hitting each other if I don’t step in."
    "…"
    "Actually, that might be fun to watch."
    "Wait."
    "No."
    "I really shouldn’t let that happen."
    "If anything happens to Makoto while she’s here, I could get in trouble."
    "Makoto’s a smart girl, but I’m pretty sure that even she would have trouble explaining to her mother why she’s coming home with a black eye after {i}studying{/i}."

    scene makotofirstvisit13
    with dissolve

    a "Sensei..."
    s "No, Ami. You can’t hit her."

    scene makotofirstvisit14
    with dissolve

    a "NGH! WHAT IS THIS WORLD COMING TO?!"
    mak "Thank you for protecting me, Sensei."
    mak "To be fair, I don’t think I’d need any protection from Ami considering her arms are essentially oversized noodles, but I thank you nonetheless."

    scene makotofirstvisit15
    with dissolve

    a "My arms are not oversized noodles! They’re strong and ready to fight for what they love!"
    a "Come at me, wench!"
    mak "Sensei, where do you keep her leash? I’m thinking it might be safer for all of us if we just chain her up for a little while."
    s "Uhh...I don’t have a leash. Let’s see if this works."
    s "Ami, go to your room."

    scene makotofirstvisit16
    with dissolve

    a "No!"
    s "I have exhausted every trick known to me. I’m sorry, Makoto."
    mak "It’s fine."
    mak "I suppose it wouldn’t be the worst thing in the world if all three of us were to...study together."
    mak "All that matters to me is that I get to spend time with you, Sensei...It doesn’t bother me that we’re not alone."

    scene makotofirstvisit17
    with dissolve

    a "And you never {i}will{/i} be alone. Not as long as I live."
    a "Makoto...Miya-whateveryourlastnameis...We are at war."
    mak "It’s Miyamura. And I accept your declaration of war, Ami Aragofuckyourself."
    s "Hey, wait a minute. She and I have the same last name. That’s kind of insulting to me as well."

    scene makotofirstvisit18
    with dissolve

    mak "Oh, of course. I’m so sorry."
    mak "I’d obviously never ask {i}you{/i} to go fuck {i}yourself{/i}, Sensei."
    a "I don’t like the way you said that, Class President."
    a "But since I’m an obedient [niece] who will {i}always{/i} do {i}whatever{/i} her [uncle] {i}wants her to do{/i}, I’ll stand down for the time being."
    a "So go on. Study. Teach whatever it is you came here to teach him."

    if bonus == True:
        a "But know that I’ll be sitting on his lap the entire time."
        s "No, Ami. You will not be sitting on my lap the entire time."
    else:
        a "But know that there's no point in teaching anyone anything when we are all fated to be miserable up until the time of our death!"

    scene makotofirstvisit19
    with dissolve

    a "THERE IS NO GOD!!!!"

    scene black
    with dissolve

    "Makoto, Ami and I take a seat at the dining room table and, somehow or another, Makoto is able to freestyle-lecture us about the American Civil War."
    "Why {i}that{/i} is the first thing she comes up with to solve the issue of our fake {i}studying{/i} session, I have no idea."
    "But it happens nonetheless."
    "Hopefully, she and I will be actually able to spend some time alone here soon."
    "But while Ami is around, I...can’t see that ever working out."
    "Eventually, it gets late and Makoto decides to head home."
    "I try to see her out but Ami pushes me away and then {i}literally{/i} pushes Makoto out of the house."
    "Either way, I still feel like the two of us managed to grow closer."
    "Even if it came at the cost of Ami yelling at me for the next half an hour after that."

    $ renpy.end_replay()
    $ makoto_love += 3
    $ makotoinvite1 = True
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotoinvite2:
...
```

## Code that triggers this event
File: \game\MakotoEvents.rpy
Code:
```python
...
label makotoinvite:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump inviteover
    if makotoinvite1 == False:
        jump makotoinvite1
...
```