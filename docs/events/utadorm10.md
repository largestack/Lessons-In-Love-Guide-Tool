# Shawshank Redemption (Uta)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Uta love greater than or equal to 10

* Event [The VIP Treatment](./utadorm5.md) (Uta) is completed)

* Day of week is not Tuesday



## Next events

* [Ami: Third Place](./amimaid30.md)
* [Main: Operation: Firestarter](./day318.md)

## Event properties

* Id: utadorm10
* Group: Uta
* Triggered by label: utadorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->utadorm->utadorm10

## Official wiki page

[Shawshank Redemption](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utadorm10&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label utadorm10:
    play sound "knock.mp3"

    "I knock on Uta’s door and wait for her to answer."
    "Some pop song with noticeably poor audio quality leaks through the door and into the hall, causing me to immediately second-guess my decision to spend time here."

    u "Somebody there? I thought I heard a knock."
    s "It’s me. Turn your music down."
    u "Oh! That’s a great impression of my grandpa, Sensei!"
    u "At least before the cancer spread to his brain and he lost the ability to speak."
    s "…"
    s "Okay, well that’s all the time I have for tonight. See you, Uta."
    u "Whaaaat? No! Come inside! "
    s "After listening to you kill the mood like that, it’s going to take some serious convincing to-"

    if bonus == True:
        u "I’m not wearing any paaaaants~"
    else:
        u "I've got a trampoliiiiiiine~"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I immediately open the door and second guess why I’d ever debated going home in the first place."
    "I mean, Uta is clearly just trying to cope with a horrible tragedy by making light of it and it would be totally wrong of me to abandon her in that state."
    "The poor thing is probably in tears as we-"

    scene utastretch1
    with dissolve

    u "Coolio! That was just as effective as I thought it was gonna be."

    if bonus == False:
        s "Where is the trampoline"

    u "What’s up? You bored?"
    u "Wanna stretch with me?"

    if bonus == True:
        s "Only if I can take off {i}my{/i} pants as well."
        u "Hmm...No thanks. Please leave them on."
        u "I understand that I am an adorable, small girl who you’d love to get down and dirty with, but I {i}really{/i} should be focusing on stretching right now."
        s "Why aren’t you wearing any pants anyway? "
        u "Because I’m {i}stretching{/i}, duh."
        s "Can’t you...do that with pants on?"
        u "I guess, but where’s the fun in that? Why have a dorm if I can’t take my pants off whenever I want?"
        u "You really are old, aren’t ya?"

        "I mean...the first thing I said after knocking was to turn the music down..."
        "Maybe I {i}am{/i} getting old after all?"
    else:
        s "No. Stretching hurts my back. I am frail and dying quickly."

    u "Sensei, I was only kidding. There’s no need to look so down all of a sudden."
    s "Sorry. I just feel like my midlife crisis could kick in at any moment."

    if bonus == True:
        u "Don’t think of that boring ole’ stuff. Just focus on me. But not in a perverted kinda way."
        s "Probably best to put pants on before asking me to make such a dramatic mindset change."

        scene utastretch2
        with dissolve

        u "Nope! Never putting pants on ever again. "
        u "Oh, how wonderful it is to be young."

    scene utastretch3
    with dissolve

    "Uta extends her body as far as it will go, letting out a high-pitched, satisfied squeak in the process before taking a step closer to me."

    u "Stretching complete. Now I’m finally ready for my real mission."

    if bonus == True:
        s "What sort of mission doesn’t require pants?"
        s "Wait. Don’t tell me-"
        u "Don’t tell you what? That I’m finally open for business? Not a chance, Sensei."
        u "Just because I’m pantless and stretchy and telling you I’m ready doesn’t mean I want to get it on."
        s "This is a misunderstanding I really should be forgiven for having."
        u "Forgiveness isn’t necessary at all. If anything, I should be apologizing to you for putting you in such a difficult situation."

        scene utastretch4
        with dissolve

        u "But, then again, you’re the one who sprinted in here the second I announced the no-pants thingy, so I guess you kinda {i}are{/i} a little to blame."

        "The closer Uta gets to me, the harder it is to resist the carnal desire to lift her up and throw her over several piles of clothing and her pet rhinoceros beetle."
        "But, as you can see, there are several things about the scenario that make it slightly less erotic."
        "Besides, it’s kind of fun being the one to actually get teased for once."
        "I spend so much time tapping into the nervousness of some of the other girls that having someone like Uta around to string me along is sort of...weirdly exciting?"
        "Completely unsatisfying and dramatically blue balling as well-"
        "But also exciting."
        "Kind of."
    else:
        s "Is it an assassination mission?"
        u "Yes."
        s "Who are you going to kill?"
        u "I am going to kill loneliness."
        s "Like that one HIM song?"
        u "Exactly like that."

    scene utastretch5
    with dissolve

    u "Hey, question."
    u "I still don’t know a lot of the girls all that well and I know that you do, so like-"
    u "I’m not really sure about how...personal I should be with all of 'em."
    u "My last[school] didn’t have a lot of people in it and the whole dorm-life thing is still new to me, but I don’t wanna be some sorta outcast like Io is going for."
    u "Like, how am I supposed to become friends with everybody?"
    u "Should I just be myself or should I try and hold back a bit?"
    s "I think the location of your pants during this process plays a bigger role than you think it does."

    scene utastretch6
    with dissolve

    u "Girls don’t care if other girls don’t wear pants, Sensei."
    s "That can not possibly be true."

    if bonus == True:
        u "No, no. It really is. We’re not as reserved as you weirdo boys- always too nervous to take off each other's shirts in the locker room and just friggin’...rub each other's bodies from head to toe."
        s "What are you even talking about?"

        scene utastretch7
        with dissolve

        u "Wouldn’t {i}you{/i} like to know?"
        s "I just don’t want you to get the wrong impression of me and think that I’m on some mission to remove the clothing of other males."
        u "And rub their bodies from head to toe."
        s "Yeah, still way off."

        scene utastretch8
        with dissolve

        u "Really? Not even a little bit? "
        u "Where’s all the fun in that?"
    else:
        u "Yo, fuck off and stop trying to convince me that reality is all just some crazy dream, Sensei."
        s "What?"

    s "Uta, this might come as a bit of a shock to you, but I-"

    scene utastretch9
    with dissolve

    u "Ah! Here?! Are you...proposing?!"
    u "Sensei! It’s so sudden! I don’t know what to say!"
    s "In what world would any of this conversation have possibly led up to that?"
    s "Also, why would you not immediately say no if that were the case?"
    u "Is it the case?! Do you really love me that much?!"
    s "My answer to this question is highly dependent on whether or not you’re wearing your maid outfit."

    scene utastretch10
    with dissolve

    u "Damnit, Uta-chan! You were too powerful!"
    u "It only makes sense that this sad, lonely man would fall for you after all of the good times you have shared with him."
    u "And now the {i}real{/i} Uta Ushibori must be the one to carry the cross. To accept the lifelong burden of love!"
    s "Why does it suddenly sound like this is turning into a yes?"

    scene utastretch11
    with dissolve

    u "U-Um...I’m not very good at many things but...if you’ll have me, then..."
    s "What is happening right now?"

    scene utastretch12
    with hpunch

    u "I do!"
    s "…"
    u "…"
    u "Not want to marry you!"
    s "There it is."

    scene utastretch13
    with dissolve

    u "Heheheh~"
    s "Are you really able to blush on command like that? That was impressive."
    u "Oh, no way. I just actually thought about what it would be like to be married to you and my brain made it seem real {i}way{/i} too quick."
    u "We had a dog and a house and everything. "

    scene utastretch14
    with dissolve

    u "Oh, and Io lived in a shed in the backyard. Her rent is due on the 1st every month."

    if iofirsthall == True:
        "I guess the tradeskill thing never worked out for her, huh?"

    s "Weird marriage fantasy aside, I don’t think any of the girls would mind if you just acted like yourself around them."
    u "Oh, right. I forgot that’s what we were talking about. "
    u "You really think that, though? Io says all this stuff about how girls are toxic and like, I guess I’ve kinda seen that in some people at the cafe."
    u "But I like to think everyone is nice overall. At least until something happens to change them."
    s "You’re an optimist and Io is a pessimist. It’s as simple as that."

    scene utastretch15
    with dissolve

    u "An optimist? Isn’t that like, an eye doctor?"
    s "…"

    "Oh, right. "
    "I suddenly remember what Makoto said about Uta’s grades being pretty horrible."

    scene utastretch14
    with dissolve

    u "Oh well. I don’t wanna learn anything when I’m already in comfort-mode."
    u "Sensei, wanna go take a trip to the water station thingy with me?"
    u "I’m super thirsty and don’t have anything to drink until Io gets back from work tonight."
    s "I mean, I’m fine with it but-"

    if bonus == True:
        u "Why are you trying so hard to get my pants back on when all you ever do is try to get them off? Choose a side, Sensei."
    else:
        u "NO BUTS ALLOWED. IT'S WATER TIME."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        "That is...a very good point."
        "The amount of restraint I’ve shown tonight is actually kind of concerning to me."
        "Hell, all it took was a beetle and some clothes to break my train of thought earlier."
        "And now I’m casually walking through the halls of a dorm with a girl who still isn’t wearing any pants."
        "Wait, what?"
    else:
        s "Oh. Uhh...okay?"

    scene utastretch16
    with dissolve

    u "Heheheh~"
    u "I feel like the guy from Shawshank Redemption right now."
    u "Just instead of escaping from jail through the sewers I escaped my dorm room through the sewers of your...mind."
    s "What?"

    scene utastretch17
    with dissolve

    u "I’m being myself! Just like you told me to!"
    u "Thanks, Sensei! It’s been a real eye-opening experience. I hope the other girls also understand your philosophy."

    scene utastretch18

    u "Oh, look! Here come two of them now!"
    s "There is no possible way this can work out in my favor."

    scene utastretch19
    with dissolve

    mo "Wha-"
    t "Legs."
    u "Hey, guys!"

    if bonus == True:
        u "Sensei convinced me that it’s okay to take my pants off. Isn’t that great?"
    else:
        u "Sensei tried to stab me with a fork earlier!"
        s "What"

    scene utastretch20
    with dissolve

    mo "He did what?!"
    mo "Explain yourself, heathen!"

    if bonus == True:
        mo "You dare tread these sacred halls and remove the...sacred kilt off of the...royal maid of...the..."

    scene utastretch21

    mo "GAH! I CAN’T EVEN THINK STRAIGHT!"
    mo "WHAT HAVE YOU DONE WITH HER PANTS?!"
    s "This is going to sound very hard to believe, but all I did was show up."
    u "No, no, Sensei! That’s not true at all!"

    if bonus == True:
        u "You taught me {i}so many things{/i} today."
        mo "SIR! EXPLAIN THE EMPHASIS SHE PLACED ON “SO MANY THINGS.”"
        s "I would love to but this is not the first time she has emphasized the most suggestive part of a sentence before. "
        s "She actually won’t stop and it’s becoming rather difficult to deal with."
    else:
        s "I do not understand what I am supposed to be doing right now."

    t "I am also having difficulty dealing with this situation."

    scene utastretch22
    with dissolve

    u "Hey! Maybe you two should stop wearing pants as well? We could form a little club!"
    u "It would be something us second floor girls could have in common that those {i}losers{/i} downstairs don’t!"
    u "Sensei even volunteered to sponsor the club and be its formal advisor!"
    s "I did no such thing."

    scene utastretch23
    with dissolve

    u "Sensei! Wanna sponsor our no-pants club?"

    if bonus == True:
        s "Absolutely."
        "My libido returns. All I needed was more girls."
        "It hasn’t been growing weaker. It has only been increasing in strength."
    else:
        s "Absolutely not."

    mo "I-I’M ALREADY IN THE MANGA CLUB! I CAN NOT TURN MY BACK ON MY COMRADES!"
    t "I’m in the ramen club."
    s "Is that actually a club we have at[school]?"
    t "I am the only member and the club room is my father’s restaurant."
    s "That’s not a club. That’s just your job."
    t "Fuck you."

    scene utastretch24
    with dissolve

    u "Heheh~ Having floormates is fun!"
    u "I guess it {i}is{/i} fine to be myself after all. "
    u "We don’t need pants to have good time! All we need is-"
    mo "PANTS! OR A SKIRT OR...SOMETHING!"
    mo "THERE COULD BE...GIRLS WHO ARE ALSO INTO GIRLS AND...HAVE A HARD TIME...NOT STARING!"

    scene utastretch25
    with dissolve

    t "Ahh, yes. The Lebanese."
    s "Lesbians, Tsuneyo. Lebanese are people from Lebanon."
    t "An entire country where it is fine to love whoever you want. What a magical place."
    u "You can stare if you want, Molly! Sensei’s been staring all night and I don’t care at all."
    mo "I never said I was talking about myself! The...Kendo Princess here...loves girls! It’s true!"
    t "I don’t think I am Lebanese but my mother comes from Egypt. Is that nearby?"
    s "Kind of? I’m not that familiar with geography from that part of the world."
    t "Then perhaps I am Lebanese after all."

    scene black
    with dissolve2

    "I decide that it might be best for everyone if I just slowly back away while all of their eyes are closed."

    if bonus == True:
        "Part of me wanted to stick around and wait to see if anymore pants/skirts came off but, judging by Molly’s reaction and Tsuneyo’s...inaction, I can’t see that happening."
        "Either way, it was nice seeing Uta finding the courage to strike up a conversation with some of the other girls on her floor."
        "It was also nice seeing her without her pants on."
        "I hope to do more of that in the future."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm10 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadorm15:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label utadorm:
    if uta_love >= 5 and utamaid5 == True and utadorm5 == False:
        jump utadorm5
    if uta_love >= 10 and utadorm5 == True and day != 2 and utadorm10 == False:
        jump utadorm10
...
```