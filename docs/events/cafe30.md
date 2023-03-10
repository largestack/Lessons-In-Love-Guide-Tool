# Nothing Was Different (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 30

* Event [See You in the Morning](./beachvacation16.md) (Main) is completed)



## Next events

* [Rin: Two Steps Back](./rindorm30.md)

## Event properties

* Id: cafe30
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe
* Triggered by path: cafe->cafe30

## Official wiki page

[Nothing Was Different](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe30&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe30:
    scene cafe_day
    with dissolve
    play music "cafe.mp3"

    "I arrive at the cafe as if it’s any other day."
    "Everything is completely normal and the bubbly girl behind the counter is going to force me to drink her latest concoction. "
    "We’ll chat for a bit and probably laugh about[school] and life or whatever else is on our minds."
    "Rin will bring up her roommate and how she’s been in a much better mood as of late."
    "And then she’ll pick up her guitar from behind the counter and play the other customers and myself a song she wrote about getting over her first heartbreak."
    "It will be a wonderful day."

    play sound "static.mp3"
    scene postbeach1
    with flash
    stop sound
    stop music

    "Just kidding. Everything is horrible."

    s "…"
    s "…"
    s "…"
    s "…"
    s "…"
    s "…"
    s "…"
    s "…"
    s "…"
    s "…"
    s "Rin?..."

    play sound "static.mp3"
    scene postbeach2
    with flash
    stop sound
    play music "cafe.mp3"

    r "Surprise!"
    s "Why were you hiding underneath the counter?"

    scene postbeach3
    with dissolve

    r "Uhh...probably because I look like I was hit by a bus."
    s "You look fine. Just a little...tired. "

    scene postbeach4
    with dissolve

    r "You’re just obligated to say that because you’re my friend."
    r "I looked in the mirror this morning. I know what I saw."

    scene postbeach3
    with dissolve

    r "Crazy, right? Imagine reacting like this to something as simple as being rejected. Hahah...Hahahaha..."
    r "But...I guess that’s just how brains work sometimes."
    r "You take one little thing and just blow it up and up and up until it’s way bigger than you."
    r "Then, all of a sudden, POP!"

    scene postbeach2
    with dissolve

    r "I think, right now, I’m probably a few more pumps away from the popping stage."
    r "So as long as I’m able to not keep pumping up the balloon, I should be able to get by. No sweat!"

    "While her description of life is a bit childish, it’s not completely inaccurate."
    "Learning how to deal with your problems is 10%% acceptance and 90%% damage control."
    "Why try to fix anything when you can just consistently avoid it until it becomes a much smaller problem?"
    "The passage of time {s}heals{/s} fixes all."

    s "True, but I wouldn’t say “No sweat” when you look like you’re burning up. "
    s "Maybe you should take your hoodie off?"

    scene postbeach5
    with dissolve

    r "B-But I like my hoodie! It’s...comfortable."
    r "And it gets really cold in the kitchen."
    r "I don’t want to freeze when I go back there and wind up having to miss[school] or anything."
    s "And you’re sure it’s not because you’re using it to hide something from me?"

    scene postbeach6
    with dissolve
    stop music fadeout 15.0

    r "Is that an accusation, Sensei?..."
    s "If that’s what you want to call it."
    s "You don’t exactly have the cleanest track record when it comes to {i}not{/i} hurting yourself."
    r "Harsh."
    r "I told you on vacation that I was done with stuff like that, didn’t I?"
    s "You did. But that was prior to you crying your eyes out for an entire night and vanishing before any of us even woke up."

    scene postbeach7
    with dissolve

    r "Well what else was I supposed to do?! Wake up and pretend nothing ever happened?!"
    r "My eyes were friggin’ swollen from crying and I had a headache."
    r "I wasn’t thinking clearly then and I’m not thinking clearly now either."
    s "What did Chika even say to you to make you want to avoid her so badly?"

    scene postbeach8
    with dissolve

    r "Uhh...well, I mean, she kind of...didn’t really say anything."
    r "But I could tell from the look in her eyes that there was no chance of it ever happening."

    play music "reversecafe.mp3" fadein 3.0

    r "Then, before long I felt my head spinning. "
    r "I kept thinking things about what it would be like to be with her."
    r "And how she might act when she’s alone with the person she loves."

    scene postbeach2
    with dissolve

    r "And then I thought of you...and how lucky you are to be able to catch the eye of someone as great as her."
    r "What’s it like, Sensei?"
    r "Gaining the affection of others without ever really doing anything to {i}earn{/i} it?"
    s "I can’t tell if you’re insulting me right now..."

    scene postbeach9
    with dissolve

    r "Not insulting you. Just an observation."
    r "You’re very important to me as well but, in some way or another, I feel like you’ve {i}always{/i} been important to me."

    scene postbeach2
    with dissolve

    r "I had a crazy dream the other night, Sensei. Do you want to hear about it?"
    s "{s}No{/s} Yes."

    scene postbeach9
    with dissolve

    r "It was a dream of a new world."
    r "Well, kind of."
    r "It was the same world as this one. But it was one where we got to redo all of our mistakes."

    scene postbeach10
    with dissolve

    r "Kind of like a reset button."

    scene postbeach2
    with dissolve

    r "And in that world, after Chika rejected me, I just kept pressing the button over and over..."
    r "And over and over and over and over and over and over and over and over and over and over and over and over until I found a world where she loved me!"
    r "It took a while, but it worked in the end. I also got to experience how good of a kisser she is. "
    r "It was really hot."

    scene postbeach11
    with dissolve

    r "But then, before any good stuff happened, I woke up. "
    r "How come dreams always end before we get to the saucy stuff? "
    r "The kiss felt so real...I wanted to know what the things that come next felt like as well."

    if bonus == True:
        if rinbetrayed == True:
            scene postbeach6
            with dissolve

            r "But I guess we can’t all be that lucky...can we, Sensei?"
            r "{i}You{/i} know what she feels like, don’t you?"
            r "Do you know how she tastes as well?"
            r "I bet it’s sweet...like candy."

            scene postbeach12
            with dissolve

            r "Hah..."
            r "It’s so unfair..."
            r "I woke up so hot, too..."
            r "I almost started rubbing up against you while you were asleep just to scratch the itch...but, you know."

            scene postbeach10
            with dissolve

            r "I remembered how you broke your promise to me and all of those naughty feelings just...went away."
            r "Poof!"
            r "Funny, right? Hahaha!"

        else:
            r "But I guess there’s just no way that would ever happen..."
            r "Not to me, at least."
            r "All I can really do is hope that the dream comes back and I can press the button a few more times."
    else:
        r "I want to know what it is like to hug."

    stop music

    s "Okay, you know what? Why don't we talk about something happier?"
    s "It might be best to just...get your mind off Chika entirely for a little while."

    scene postbeach12
    play music "cafe.mp3"

    r "Fiiiiine..."
    r "But if this is one of those things where you try to pick me up on the rebound, I think I’m going to have to ask you to wait."
    r "I’m glad that you feel that way about me, but I’m still getting over a broken heart and need time to mend my wings."

    if bonus == True:
        s "Oh, come on. Even I know not to make my move that early."
    else:
        s "Oh, come on. We all know that I'm only here to hug and that I don't want any sort of romantic relationship."

    scene postbeach10
    with dissolve

    r "That gives away that you’re planning on making a move eventually, you know."

    if bonus == True:
        s "I thought that was pretty apparent since the get-go."
    else:
        s "If that move is a hug, sure."

    scene postbeach2
    with dissolve

    r "You mean you’re fine with me even if I look like this all the time?"

    if bonus == True:
        s "If you looked like that all the time while seeing me, I’m pretty sure I’d question my validity as a romantic counterpart."

    scene postbeach10
    with dissolve

    r "How’s that saying go? If you can’t handle me at my worst, you don’t deserve me at my best?"
    s "This isn’t your worst. You’re at least able to hold a coherent conversation this time. "
    s "You just look like shit."

    scene postbeach9
    with dissolve

    r "How very kind of you."
    s "Is Haruka not here or something? I figured she wouldn’t let you work in that condition again."

    scene postbeach4
    with dissolve

    r "Uhh...About that."
    r "Please don’t tell her this time...I really need the money. I’m still able to do my job, too."
    r "This sad version of Rin is a little different than the last one."
    r "It’s one thing to experience heartbreak or disappointment or whatever, but it’s a lot different when you don’t know where those feelings are coming from."

    scene postbeach10
    with dissolve

    r "I was able to prepare for this kind of pain, I guess. I’m not being blindsided by my fear of mortality, I just...really like someone who doesn’t like me back."

    "I guess she makes a good point."
    "She might look like she was dropped from the tenth story of a building in the middle of a thunderstorm but...Well, at least she’s being mature about it."
    "There is still one thing that seems to contradict that, though."

    s "If you’re so prepared to deal with these feelings now, what exactly are you hiding beneath your hoodie?"

    scene postbeach13
    with dissolve

    r "Umm..."
    r "A crutch?"
    r "There’s obviously no point in lying to you since you’ve figured it out already but...I may have impulsively awakened a bad habit when I came home from the beach."

    scene postbeach14
    with dissolve

    r "But that’s all it is...A bad habit."
    r "Just a little kick in the back to say, “Rin, get yourself back into gear. You’re still alive.”"
    r "It’s no different than any other coping mechanism. It’s just leaning on something a little...unconventional to take some of the pain away."
    s "You are aware that there are plenty of people you can lean on instead, right?"
    r "Of course I am. Which is why I’m able to smile while talking to you right now."
    r "I’m...glad that you care about me. But that doesn’t mean I can just drop habits I’ve had for years. "

    "Years?"
    "Has she really been doing things like this for that long?"

    scene postbeach2
    with dissolve

    r "Hey! How about I take my break a little early and we go sit by the window or something?"
    r "It would be nice to...get my mind off stuff for a little while. "
    r "Do you want something to drink? I’ll actually make you whatever you want this time~"
    s "Nah, that’s fine. You can just make me another one of your weird concoctions. "

    scene postbeach15
    with dissolve

    r "Heheh~ You got it!"

    scene black
    with dissolve

    "I take a seat at a table near the window and watch as Rin starts pumping a few different syrups into a cup."
    "She looks a little lost behind the counter, but I imagine that’s more due to lack of sleep than incomparable misery."
    "Before long, another girl takes her place at the register and Rin joins me at the table..."

    scene postbeach16
    with dissolve

    r "So uhh...Yeah, sorry about the whole beach thing."
    s "Why would you need to apologize for that?"
    r "Because I’m pretty sure I held onto your hand so tightly that it may have turned blue while you were sleeping."
    s "Small price to pay for making you feel a little more comfortable."

    scene postbeach17
    with dissolve

    r "I guess, but that still doesn’t mean I can’t feel bad about it."
    r "I didn’t even tell Futaba where I was. Poor girl was worried sick. "
    s "How did Futaba even know? Didn’t she go home early?"
    r "There are other girls in our class, idiot. One of them probably asked if she knew where I was that night when I disappeared into your room."

    scene postbeach18
    with dissolve

    r "Thanks for locking the door to make sure no one could bother us, by the way."
    r "I don’t think seeing me hysterically crying on your bed would have left a good impression on anyone."
    s "Yeah, I have enough to deal with as-is. The last thing I need is someone thinking I’m taking advantage of you behind closed doors."
    r "The last thing {i}I{/i} need is you taking advantage of me behind closed doors."

    scene postbeach16
    with dissolve

    r "But I guess even someone like {i}you{/i} wouldn’t stoop that low. You care about me, after all."

    if rinbetrayed == True:
        r "Sure, you might have done the {i}one{/i} thing I asked you not to do, but that doesn’t mean you don’t also think I’m...cool or whatever."
        s "You’re really not going to let me live that down, are you?"
        r "Why would I? It was really fucked up."
        r "Friends don’t do that to each other."

        if bonus == True:
            r "You really think I can look at you the same way after finding out the girl I spent years fawning over probably pleasures herself while thinking about you?"
            r "Not really an easy thing to forget."
            s "…"
        else:
            s "I know, and I feel very bad. I will die filled with regret. I will never hug again."

        "Part of me wants to apologize, but I know it won’t do any good."

        if bonus == True:
            "I never understood why people apologize for things like this."
            "An apology isn’t just a magic set of words that can make your misdeeds vanish. It draws attention to them."
            "So it’s best to just ignore things like them entirely."
        else:
            "I am a bad boy."
            "I can not be redeemed."

    else:
        s "Someone like me? What is that supposed to mean?"

        if bonus == True:
            r "Just that you're a boy. You think with your penis instead of your brain."
            s "If I truly thought with my penis, your anti-perversion crying barrier wouldn’t have any effect."
            r "Ew, you get turned on by crying girls? Pervert."
            s "I’m not a pervert. I’m a man."
            r "Same thing. That’s why I like girls more."
            r "They’re only perverted like, 50%% of the time instead of 100%%."
            s "I’ll keep that in mind every other meeting we have."
        else:
            r "Just that you're the huggy boy and that everything you do is in the best interest of advancing your secret hug agenda."
            s "My hug agenda is very public. I don't try to hide that at all."

    scene postbeach19
    with dissolve

    pt "Umm...Rin? I’m sorry to bother you during your break, but could you help me with this for a second?"
    r "Huh? Yeah, hold on a sec."

    scene postbeach20
    with dissolve

    r "Sorry Sensei, but I’ll be right back..."
    s "It’s fine, actually. I’m probably going to head out now anyway."
    s "I just wanted to stop by and make sure you were doing alright. "
    s "You scared a few of the girls with the way you left, so I needed to make sure you didn’t go and do something stupid."
    r "Well, I did do {i}something{/i} stupid, but not as stupid as what you’re insinuating."
    r "But we can talk more about that soon, okay?"
    r "Futaba and I were probably gonna hang out in our room sometime in the near future and just...talk about stuff if you want to join."
    r "I’m sure she wouldn’t mind. It’ll probably all be about me anyway."
    s "Are you scheduling your own intervention?"

    scene postbeach21
    with dissolve

    r "It sounded a lot more normal in my head before you put it that way..."
    r "Just come hang out with us. It’ll be fun. "
    r "Depressing too, I imagine. But also fun."
    s "Sounds like a blast..."

    scene black
    with dissolve

    "I...apparently make plans to have a depressing, yet fun conversation with Rin and Futaba in the near future."
    "I really hope this doesn’t turn out to be one of those ‘group therapy’ sort of things but, if it does, I guess it will be warranted. "
    "Rin’s taking this a lot better than I thought she would, so there’s a chance this could just be the calm before the storm or something like that."
    "I should visit her dorm room whenever I can..."

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe30 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label cafe35:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

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
...
```