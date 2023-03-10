# Sisters (Niki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Loxosceles Reclusa](./norikodorm25.md) (Noriko) is completed)



## Next events

* [Niki: Dear You](./nikiinvite2.md)

## Event properties

* Id: nikiinvite1
* Group: Niki
* Triggered by label: nikiinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->nikiinvite->nikiinvite1

## Official wiki page

[Sisters](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikiinvite1&go=Go) for more details.

## Event code

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikiinvite1:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "And, of course, I prepare myself for the worst since she is very rarely able to make any time for me given her incredibly busy schedule as a famous person or whatever."
    "In fact, even if she {i}does{/i} answer by some stretch of the imagination, I doubt she’ll be willing to accept an invite over to-"

    play sound "phonebeep.wav"
    play music "remember.mp3"

    ni "Hey. What’s up?"
    s "Oh, you answered."
    ni "What? Were you starting to think I’m too good for you now or something?"
    s "I wonder what would have given me that idea. "
    ni "I would have given you that idea- because I {i}am{/i} too good for you now."
    s "This is a fun conversation."
    ni "It truly is. "
    ni "Anyway, what are you doing right now?"
    s "I’m working up the courage to invite you over, but your idolic presence is so commanding and intimidating that I’m having trouble finding the words."
    ni "Wow, are you actually going to tell me where you live after all of these years away?"

    if bonus == True:
        s "If I say yes, will you come over and have sex with me?"
    else:
        s "If I say yes, will you come over and hug me?"

    ni "What, like now? Fuck off. No."
    ni "I’ll come say hi, though."
    s "You’re actually able to?"
    ni "I’m taking the night off, so yeah."
    ni "Just text me the address and I’ll have my driver take me."
    ni "Oh- and before I forget, is Ami home?"
    s "I...think so?"
    ni "Even better. See you soon."

    play sound "phonebeep.wav"

    s "…"

    scene black
    with dissolve

    "Welp, it looks like Niki {i}is{/i} going to come over after all. "
    "As I type out my address to her, I think to myself about what it must be like to have people willing to wait on your every beck and call."
    "But, then I remember that Ami exists and realize that Niki just isn’t that special after all."
    "No amount of drivers or bodyguards can live up to the calming, yet mildly intimidating presence of a red-haired [niece]."
    "………"
    "……"
    "…"

    scene girlsnightin1
    with dissolve
    play sound "doorbell.mp3"

    "The doorbell rings shortly after I take my shoes off and I pat myself on the back for making it here in time."
    "I can only imagine how Ami would have reacted if she answered the door to find her icon just...standing there."

    play sound "doorbell.mp3"

    ni "Stop monologuing and open the fucking door."
    s "Well, that’s just plain rude."
    n "Sensei! Let us in!"

    "What? Noriko is here too?"

    if bonus == True:
        "I mean, as much as I love the idea of taking both Nakayama sisters’ virginities at once, I didn’t think that would be in the cards today."
        "But, even with the prospect of that being slightly possible, I have now obtained all of the motivation I need to let them in."
    else:
        "What a pleasant surprise! The more, the merrier!"

    play sound "dooropen.mp3"
    scene girlsnightin2
    with dissolve

    ni "Hi. Your neighborhood sucks. "
    s "Thanks. Why did you even need my address if Noriko was coming? She could have just shown you the way."
    n "I didn’t even know I was coming until a little while ago."
    ni "Also, I had no idea that you routinely invited my little sister over to your house."
    s "I mean...I wouldn’t call it {i}routinely{/i}."

    scene girlsnightin3
    with dissolve

    if bonus == True:
        n "This is where Sensei made me into a woman!"
        n "If you guys are gonna have sex, make sure you dig your nails into his back really hard. That's his favorite."
    else:
        n "This is where Sensei does his laundry!"
        n "I know this because there is a secret tube inside of his dryer that sends me one of his socks every time he uses it."

    ni "Very funny. "
    s "I’m confused."

    scene girlsnightin4
    with dissolve

    ni "About what, exactly?"

    if bonus == True:
        s "Why Noriko came. And why she’s carrying your bags. And why I don’t remember making her into a woman or the sensation of her nails against my skin."
        n "Maybe I drugged you? It certainly wouldn’t be the first time."
    else:
        s "Well, the sock thing for starters."

    ni "Ooookay. Now {i}I’m{/i} confused."

    if bonus == False:
        s "Niki it literally just happened."

    ni "The bags just have some stuff I brought over for Ami. Mostly old clothes and extra merchandise that I didn’t have a use for anymore."
    n "And also a bunch of stuff that she bought because she wants Ami to like her."

    scene girlsnightin5
    with dissolve

    ni "Noriko! Shut the fuck up or I’m not paying you for this!"
    n "Yes, Nee-chan. Anything you say. "
    s "You actually bought stuff for Ami? Even I don’t buy stuff for Ami."

    scene girlsnightin6
    with dissolve

    ni "Yeah, well you’re an asshole and I’m a thoughtful and caring person."
    ni "Where is she, by the way? "
    s "She’ll be here any second now. The scent of females probably set off an alarm in her brain and caused her defense mode to start."
    a "Sensei! Are there girls here?! You know how I feel about you inviting-"

    scene girlsnightin7
    with dissolve

    a "Ah! Niki! My queen!"
    a "My mind says attack but my heart says love!"
    ni "Hi, Ami! Are you free right now?"
    a "Me?! Yes! I am always free for you! I will kill for you! Just say the word!"
    n "Uhh...where should I put these bags? They’re getting kinda heavy."
    ni "Wonderful. Because I was hoping that the two of us would be able to get to know each other a little better if that’s okay with you."
    s "Wait, what?"

    scene girlsnightin8
    with dissolve

    ni "What’s wrong?"
    s "I mean...I just expected this to be a more private or personal invitation."
    ni "Private or-"

    scene girlsnightin9
    with dissolve

    ni "Wait- did you think I came here for {i}you?!{/i}"
    s "Well...considering I was the one who invited you..."
    ni "Oh, you sweet summer child. I’m just here to talk to Ami."
    s "Why am I the sweet summer child? I’m supposed to be the protagonist. "

    scene girlsnightin10
    with dissolve

    ni "Well then, Mr. Protagonist, why don’t you make yourself useful and go on a little side quest to the convenience store and get us some snacks while we have a bit of a girls’ night in?"
    a "A...girls’ night with...Niki?"

    scene girlsnightin11
    with dissolve

    n "And Noriko! I’m here too!"
    ni "Do you like french fries, Ami? We stopped at a fast food place before coming over."

    scene girlsnightin12
    with dissolve

    a "I love you! I mean- I {i}love{/i} french fries!"
    s "But surely your love for me outweighs the chance to hang out with Niki and eat fast-"

    scene girlsnightin1
    with dissolve

    a "This way to the living room!"
    a "If I had known you were coming, I would have cleaned up first!"
    s "Didn’t you clean this morning?"

    scene girlsnightin13
    with fade

    ni "I’m sorry, were you not listening when I asked you to run along and leave us alone?"
    s "I was listening. I just assumed it was a joke on account of {i}this being my house.{/i}"
    n "I vote that Sensei stays!"
    s "See? Noriko and Ami both want me to stay."
    ni "Funny. I don’t remember Ami saying anything like that."
    s "It’s Ami. She doesn’t have to say it. It’s just always true. Right, Ami?"
    a "…"
    s "…"

    scene girlsnightin14
    with dissolve

    ni "Well, would you look at that?"
    s "Of all the times to betray me..."
    n "I tried, Sensei. I really did."
    s "Okay, I’ll go. But I’m taking Noriko with me."
    ni "No, you’re not. Noriko’s on the clock."
    n "She’s right. I am but a slave to the machine that is the idol industry right now."
    s "…"
    s "I won’t forget this, Niki."
    ni "Ooooh, so you won’t forget {i}this{/i}, but you’ll forget the five years we dated and how you ruined my life. I’m glad to understand your priorities a little better now."
    s "Hey, in a roundabout way, if it wasn’t for me-"
    ni "If you are about to take credit for all of the hard work I’ve invested into reforming myself, I’m just going to steal Ami and never give her back."
    s "But then who will do the dishes?"
    n "Oh! Me! Me! Noriko will do them!"
    ni "Goodbye, [nikitemp]. Walk slowly, because if you’re back in any less than two hours, I’m not undoing the chain lock."
    s "But the convenience store is only a few minutes-"
    ni "One more word out of you and it’ll be {i}three{/i} hours."
    s "…"
    ni "…"

    scene black
    with dissolve2

    "You know..."
    "This is really not how I planned on tonight going."
    "The next time I invite Niki over, I should make her clarify that she will be spending her time with {i}me{/i} rather than trying to poach my [niece]."
    "I begrudgingly exit the house- but as I glance back inside to see if Ami is maybe having second thoughts about letting me leave, I see nothing."
    "Just an empty space where my [niece] once stood, only to be stolen away by a girl with cotton candy hair."
    "First my shirt...now this?"
    "Ex-girlfriends really are terrifying..."
    "………"
    "……"
    "…"

    scene girlsnightin15
    with dissolve

    ni "Why do you look so nervous?"
    a "Um...because you’re Niki Nakayama and I’m just some random girl who can’t even get a high score on any of your songs in the karaoke booth?"
    ni "Okay, so...that might be who I {i}normally{/i} am. But right now, you can look at me as a...family friend."
    a "That’s...the part that’s hard for me to do, though."
    a "Even if you did date my [uncle] in the past, I don’t think I was really old enough to remember it."
    ni "And I wouldn’t expect you to. But since {i}I{/i} remember you, that’s really all that matters."
    n "Nee-chan owes you a big debt of gratitude for managing to keep Sensei on his feet after all these years."

    scene girlsnightin16
    with dissolve

    ni "I don’t give two shits about whether he’s on his feet or not. I just want to make sure that Ami is doing okay since I...feel bad that {i}he{/i} had to be her guardian."
    a "I’m doing great. I’ve actually never been happier."
    a "It’s true that things were really bad for a while, but we were there for each other when we had to be."
    a "And even if Sensei isn’t the best guardian and I had to get a job because he wouldn’t buy me things, I can tell he loves me."
    a "In fact, I can tell he loves me even more than {i}he{/i} thinks he loves me. "

    scene girlsnightin17
    with dissolve

    ni "That’s kind of just how it is with that guy. Never understood why, but it’s like he’s always kept how he really feels locked up so tightly that it looks more like he feels nothing at all."
    n "Is that why you’ve always bossed him around?"

    scene girlsnightin18
    with dissolve

    ni "I never {i}bossed him around.{/i}"
    n "Nee-chan, you are {i}still{/i} bossing him around. You just kicked him out of his own house so we could talk to Ami."
    ni "There’s a difference between bossing him around and having to make decisions for him! I’m sure Ami knows, but sometimes you {i}have{/i} to push him in a certain direction or he'll just get lost."
    n "And today...that direction was the convenience store."
    ni "…"
    ni "Okay. Maybe {i}that{/i} was bossy."

    scene girlsnightin19
    with dissolve

    ni "But I did it to get closer to Ami, so it was all worth it."
    a "I don’t understand, though...why do you want to get closer to me? It can’t just be because you think Sensei is a bad guardian or that...you want to thank me."

    if bonus == True:
        a "I just did what any other girl in my position would do because...Sensei’s the only family I have now."
    else:
        a "I just did what any other girl in my position would do because...Sensei’s the only client I have."

    ni "But he doesn’t have to be."

    scene girlsnightin20
    with dissolve

    a "Are you trying to marry him?!"
    n "Uhhhhhh..."
    ni "What? No. I’m not even trying to date him."

    if bonus == True:
        ni "I’m just trying to say that I wouldn’t mind if...there was suddenly a third Nakayama sister or something."
    else:
        ni "I’m just trying to say that I wouldn’t mind if...you helped me with my taxes as well..."

    ni "Even if we’re not as close to [nikitemp] as we used to be, he’s still an important part of our lives that’s never going to go away. And Ami deserves a lot more than just him."
    n "Why do you keep calling him [nikitemp]?"
    a "I was wondering that, too."
    ni "Unimportant. "

    scene girlsnightin21
    with dissolve

    ni "I just want to do my part for both an unofficial family member {i}and{/i} one of my biggest fans in letting her know that I’ll always be here for her."
    ni "Even when her [uncle] manages to fuck things up all over again, which he definitely will."
    n "I’ll be here, too. "
    n "Obviously, that’s probably not as cool as my sister saying it, but you really are like family to us."
    a "I...um..."
    a "I don’t really know what to say..."
    a "This is all really sudden and it feels kinda like a dream. "
    ni "Just a...convenient side effect of us growing up in the house next door to your [uncle]. "
    ni "I always wanted to do something like this if we ever wound up walking into your life again, so consider it my way of making amends for not being there earlier...when I wanted to be."
    a "…"
    ni "…"
    a "Are you sure you’re not trying to marry him?"


    scene girlsnightin22
    with dissolve

    ni "Uh...yeah."
    a "Because if you do, I won’t let you use your big sister powers to get rid of me."
    a "Marrying Sensei includes promising to look after me for the rest of my life, as I have sworn to be there for him whether he wants me to or not."
    ni "That’s...fine?"
    a "Don’t get me wrong, I’d still prefer that you {i}don’t{/i} marry Sensei. But if there is going to be anyone I would make an exception for, it’s you."
    a "As long as you also agree to the thing I said, I mean."
    n "What do you think? She seems like she’ll be even higher maintenance as a sister than I am and I {i}still{/i} steal your clothes without telling you sometimes."
    ni "I don’t care how “high maintenance” she is. I just want her to have somebody else to rely on."

    scene girlsnightin23
    with dissolve

    a "Well...I’m not sure {i}how{/i} I’m supposed to rely on you when I’m already happy with how things are..."
    a "But I...would like to see you more, if that’s okay."
    a "I don’t know if I’ll ever be able to look at you as family...but I know that you really do care about my [uncle] and...that I can’t ignore your past with each other no matter how much I want to."
    ni "Why would you want-"

    scene girlsnightin24
    with dissolve

    a "At the end of the day...I’m just happy to have you two on my side. "
    n "Your side as opposed to what?"
    a "Any side that wants to get rid of me."
    a "Sensei is my entire life- and neither of you think that’s a problem."
    ni "I mean...he’s not your {i}entire{/i} life, is he?"
    a "He is. And if either of you two hurt him, I will be very, {i}very{/i} unkind to you."
    a "If you are okay with that...then I’m okay with letting you two in."

    scene girlsnightin25
    with dissolve

    ni "Any objections, Noriko?"

    if bonus == True:
        n "To a life of nothing but pleasing Sensei? Do you even have to ask?"
    else:
        n "Do you even have to ask?"

    ni "I hate that I don’t."
    ni "Besides, I doubt it’s even possible to hurt him at this point."
    ni "If anything {i}does{/i} hurt him, he’ll just rationalize it in whatever twisted way his weirdo brain wants to come up with and come out totally fine within a matter of days."

    scene girlsnightin26
    with dissolve

    a "It’s settled, then! "
    a "From now on, the two of you can come over as much as you like as long as you don’t touch my [uncle]!"
    n "A step in the right direction! Hooray!"
    ni "I’m happy to hear that, Ami. "
    ni "I really hope that the two of us can grow closer."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    scene girlsnightin27
    with dissolve

    a "Sensei! I have sisters now!"

    if bonus == True:
        n "Welcome home, Onii-chan! Wanna get in the bath together?"
        ni "I don’t think it’s been two hours yet."
        s "And yet the chainlock remains...unchained."
        ni "It has been brought to my attention that I may have been {i}slightly{/i} too bossy to you earlier- and for that, I apologize."
        ni "I will now allow you to continue using your house, but not before retreating to Ami’s bedroom and having her model all of the outfits I bought for her."
    else:
        n "We're going to Disneyland!"

    s "Can I come, at least?"
    ni "No. But you can put on a pot of coffee for us, if you’d be so kind."
    a "Niki bought me clothes! I’m going to be pretty!"
    s "You {i}are{/i} pretty, Ami. "
    a "Not pretty enough!"

    scene girlsnightin28
    with dissolve

    ni "Come on, Ami! Let’s get those clothes off!"
    a "Yes, Niki! Anything for you!"
    s "…"
    n "…"
    ni "NORIKO! BAGS!"
    s "I think you’re being summoned."

    if bonus == True:
        n "Yes. But, before I go, I would like to remind you that sometimes, fantasies don’t do the job and that you have at least one picture of my boobs in your phone to use however you want."
        s "I...certainly do. But why are you telling me this now?"
        n "So that you don’t think of what’s happening in Ami’s room and that you think of me instead!"
        n "I love you, Onii-chan! Forever and ever!"
    else:
        n "Yes. But, before I go, I would like to remind you that there are roughly 750 million pus cells in every litre of milk!"

    ni "NORIKO! GET THE FUCKING BAGS!"

    scene black
    with dissolve

    n "Coming, Nee-chan!"
    s "…"

    "I think it might be time for me to move out."

    $ niki_love += 1
    $ renpy.end_replay()
    $ nikiinvite1 = True
    stop music fadeout 6.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label nikiinvite2:
...
```

## Code that triggers this event

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikiinvite:
    if nikiinvite1 == False:
        jump nikiinvite1
...
```