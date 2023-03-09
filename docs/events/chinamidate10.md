# Giant Pool of Jell-O
Chinami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chinamidate10&go=Go)



## Event preconditions
✅Chinami love greater than or equal to 10

✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)

✅chinaminumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: chinamidate10
* Group: Chinami
* Triggered by label: callchinamimorning
* Triggered by branch label: callchinamimorning

## Event code
File: \game\ChinamiEvents.rpy
Code:
```python
...
label chinamidate10:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "It’s still a little early, so I imagine Chika is getting ready to leave for work right about now."
    "I don’t think I’ll ever come to terms with how strange the idea of me calling her little sister is, but it’s definitely getting less...weird over time."
    "Kind of."
    "I don’t know. Chinami is strangely fun to be around at times."
    "Even if that strange sense of fun comes from the fact that she may or may not be some sort of super-genius disguising herself as a little girl."
    "I’m calling your bluff, Chinami. You’re up to something."

    play sound "phonebeep.wav"

    ch "Good morning, future dad!"
    s "Good morning, Chinami. I am not your future dad."

    if bonus == True:
        ch "But big sis says she’s pregnant with your baby."
        s "That is literally impossible."
        ch "No! You two kissed and that’s how babies happen!"
        s "First, don’t ever say anything like that around Yumi."
        s "Second, you know damn well that isn’t how babies are made, Chinami."
        ch "No one will tell Chinami where they really come from so she has to keep guessing until she gets it right."
        s "Or Chinami can just drop it."
        ch "And never get a little sister? No way, future dad!"
        ch "Hold my sister’s hand and get her pregnant!"
        s "Wrong again."
        ch "Rats!"
        s "Is Chika home right now?"
        ch "Big sis left a few minutes ago. She looked extra pretty today."
        ch "The perfect kind of look for getting knock-"
        s "I’m going to hang up now."
        ch "Wait! Chinami wants you to come visit!"
        ch "She is very bored and promises to not talk about babies!"
        s "…"
        s "Fine. I’m on my way."
        s "I’m leaving the second you start saying things like that again, though."
        s "There are two girls you’re very familiar with who would kill me if I was anywhere near a discussion of that nature."
        ch "Blah blah blah."
        ch "Chinami doesn’t understand what the big deal is, but she’s got a meeting coming up, so you better hurry before the doors are closed for good!"
        ch "Bye-bye, future dad!"
    else:
        ch "Yes you are! Chinami comes from the future, so she knows!"
        s "I'm sure you do, Chinami."
        ch "Are you going to come over and play now?"
        s "..."
        ch "Chinami comes from the future, so she knows you are!"
        ch "Bye bye!"

    play sound "phonebeep.wav"

    "Chinami hangs up the phone and I’m suddenly left wondering why I even called her in the first place."
    "All of those things I said about how she’s fun to be around-"
    "They were all lies."
    "She’s out to destroy me. "
    "I know she is."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene chinamibalcony1
    with dissolve
    play music "happyandplotting.mp3"

    ch "Greetings, mortal! It is I, Chinami!"
    s "Good morning, Chinami. "
    ch "Lucky for you, Chinami’s meeting just ended."
    ch "She has all the time in the world now."
    s "Who was your meeting with, exactly?"
    ch "So, you know how Chinami Corp is the leading distributor of giraffes and giraffe paraphernalia in all of Japan?"
    s "...Yes."
    s "Also, since when has your vocabulary expanded to include those words?"
    ch "Chinami has had five thousand years to practice vocabulary. It was only a matter of time."
    s "Right, right. Please proceed with your giraffe stuff. Sorry for interrupting."

    scene chinamibalcony2
    with dissolve

    ch "It’s okay. Chinami understands that not everyone can be as business savvy as her."
    ch "You see, future dad, Chinami Corp has acquired another company this morning."
    ch "It was a big acquisition! One that will make Chinami so much money that she can start making microtransactions in her pig game!"
    s "I don’t follow gaming, but I’m pretty sure microtransactions aren’t at the point where you need to own a company to make them yet."
    ch "You’d be surprised."

    scene chinamibalcony3
    with dissolve

    ch "Wanna buy an elephant? It would make Chinami very happy and the recent merger has added them to the Chinami Corp catalogue!"
    s "No. Chinami Corp still hasn’t even given me the giraffes I accidentally ordered."

    scene chinamibalcony4
    with dissolve

    ch "Pweeeeeeeeeeeease?~"
    s "…"
    ch "…"

    "Your tricks won’t work on me, demon."

    s "I hope I didn’t come all this way just for you to try and sell me things again."
    s "It’s not exactly a short walk, you know."

    scene chinamibalcony5
    with dissolve

    ch "Chinami doesn’t know. The only time she’s allowed to go outside is when she’s with big sis Chika."
    ch "She used to be allowed outside with big sis Yumi, but not since the peanut incident."
    s "The what now?"
    ch "Chinami is very allergic to peanuts and big sis Yumi let her eat some since she’s reckless and mature."
    s "It’s not very mature to feed peanuts to someone who is allergic to them."
    ch "It’s Chinami’s fault, too. She knew she was allergic and didn’t tell big sis Yumi about it."
    s "Were you trying to get yourself killed?"
    ch "No! Chinami just likes nuts! "

    "There is a glaring issue with that statement but explaining {i}why{/i} would just cause me even more of a headache."
    "I should write down to never give her anything with nuts, though. That seems like a big deal."
    "Is this what being a parent feels like?"

    s "No. Parents don’t take notes on their kids."
    ch "Future dad? Are you talking to yourself?"
    ch "Do you need to take notes on Chinami even though you’re not married to big sis Chika yet?"
    ch "Do you need the Chinami Corp quarterly spending report?"
    s "Where in the world are you learning all of these business terms?"
    ch "Chinami has gotten really into the stock market lately and it’s opened a big can of worms!"
    ch "But big sis Chika wouldn’t let Chinami invest in GME and now they’re still poor instead of swimming in a giant pool of Jell-O. "
    s "You have a strange perception of what it is like to be rich."
    ch "Are you telling Chinami that you {i}wouldn’t{/i} swim in a giant pool of Jell-O?"
    s "I am. That doesn’t sound fun, it just sounds difficult."
    ch "Future dad, can Chinami ask you a question?"
    s "As long as it isn’t about something that’s going to get me in trouble."
    ch "What is Jell-O?"
    s "Why do you want to swim in a pool of something if you don’t even know what it is?"
    ch "I heard it on TV."
    s "It’s a...weird water based dessert thing that’s kind of...bouncy. It’s actually pretty gross."
    ch "Can we make Jell-O one day or is it only for rich people?"
    s "It’s actually really cheap so...sure."

    scene chinamibalcony6
    with dissolve

    ch "Hooray! Chinami is gonna eat a bouncy dessert with her new dad!"
    s "It will have to wait for another day, though. I obviously didn’t bring any with me this time."

    scene chinamibalcony7
    with dissolve

    ch "It’s okay~ Chinami had other plans for today."
    ch "And she asked big sis Chika already, who said it’s okay as long as Chinami puts her scarf on first."
    s "Your scarf? Why?"
    s "I’m not allowed to take you outside, am I? Not even Yumi is allowed to do that."
    ch "Because big sis Yumi tried to assassinate Chinami."
    ch "You’re not an assassin, are you?"
    ch "Please don't kill Chinami! She loves you!"
    s "Not...that I’m aware of."
    ch "Then everything is okay!"

    "I’m not sure how I feel about this."
    "I felt weird enough even walking around the mall with Chinami."
    "Taking her outside, especially in this part of town, seems like an accident waiting to happen."
    "There’s no way I could let myself be responsible for something like that."

    s "I don’t think it’s a good idea for you to go outside, Chinami."

    scene chinamibalcony8
    with dissolve

    ch "But...but Chinami got permission."
    s "Even {i}if{/i} Chinami got permission, what if something bad happened to you?"
    ch "You would protect Chinami because you love her."
    s "I have never once said I love you, Chinami."

    scene chinamibalcony9
    with dissolve

    ch "Two dads in a row don’t love Chinami! Is she doomed to live a life of sadness?!"
    s "Okay, fine. I love you. Just...don’t bring up how your real dad didn’t ever again. "

    scene chinamibalcony10
    with dissolve

    ch "So this is what love feels like..."
    ch "Her real dad is missing out on something big!"
    s "Right..."

    scene chinamibalcony4
    with dissolve

    ch "Can Chinami really not go outside, though? She was very excited..."
    s "She can’t. "
    s "I don’t even know my way around this part of town. "
    s "And if Yumi ever saw me walking around with you, she’d-"

    scene chinamibalcony11
    with dissolve

    ch "Wait."
    ch "Chinami thinks she may have left out an important detail."
    ch "Chinami didn’t expect to walk around the town."
    ch "She just wanted to stand on the balcony for a little while and then get cold and go back inside."
    s "Oh."
    s "Why did you need to ask for permission to stand on the balcony?"
    ch "Because Chinami tried to climb the railing once when she was little and almost fell down and died."
    ch "Now Chinami asks every time just to be safe."
    s "Just to clarify, when you asked your sister for permission, did you say anything about me being here?"
    ch "Not today. Chinami thought you were just coming over for business reasons."
    s "Please assume from this point forward that I will {i}never{/i} be coming here for business reasons."
    ch "That’s okay. Chinami no longer has any use for you because of the merger."
    ch "She wishes you good luck with your future endeavors."
    s "…"

    "You know, I’m kind of thankful Chinami can’t go to a regular[school]."
    "I can’t imagine there are many other girls her age (5,000) that would know how to deal with her."

    s "Go put your scarf on, Chinami. We’ll go stand on your balcony for a little while if that’s really what you want to do."

    scene chinamibalcony12
    with dissolve

    ch "VICTORY FOR CHINAMI! THERE {i}IS{/i} A GOD!"

    scene black
    with dissolve2

    "Chinami sprints into the bedroom and pulls open a drawer, removing a long white scarf out of it and wrapping it around her neck."
    "She closes the drawer with so much force that the picture of her mother falls over."
    "Chinami gasps in shock as this happens and then apologizes to the picture as if it still has the potential to feel."
    "She sits it upright once again, among a circle of candles, before running toward the back door and sliding it open, stepping aside for me to meet her out there."

    scene chinamibalcony13
    with dissolve

    ch "Wow! "
    ch "Chinami has been stuck inside for so long that she forgot what the sun even looks like!"
    ch "It hurts so much more looking at it from outside instead of behind the window!"
    s "Please don’t stare directly at the sun, Chinami. You’ll go blind."
    ch "Blindness-shmindness! Gimme those UV rays! Chinami finally feels alive!"
    s "How long has it been since you’ve been out here? This is a hell of a reaction."

    scene chinamibalcony14
    with dissolve

    ch "Chinami last went outside three days ago."
    s "That is nowhere near long enough to warrant this type of reaction."
    ch "Everything seems longer when you’re stuck inside, future dad."
    ch "Even forty-five minute TV shows feel more like an hour!"
    ch "And since Chinami has to study at night, the day time is the only time she gets to be a free woman."

    scene chinamibalcony15
    with dissolve

    ch "But one day, Chinami is gonna have her very own house and she’ll be able to stand on the balcony without asking permission."
    ch "And she’ll also have a horse, and a dog, and a plasma screen television, and a pool full of Jell-O."
    ch "And she’ll come visit you...and big sis Chika...{i}and{/i} big sis Yumi every single weekend."
    s "Yumi is going to be there too?"

    scene chinamibalcony16
    with dissolve

    ch "Of course!"
    ch "You have to marry both of them so you can be Chinami’s full dad instead of her half dad."
    ch "And then you can marry Chinami too and we can all move into my house with the horse and the Jell-O pool."
    s "You do realize you don’t have to marry someone to live with them, right?"
    ch "But you’re a boy and we’re all girls. Obviously we’d have to get married to live together. Isn’t that the rule?"
    s "Again, no. That is not the rule."
    ch "So you love all of us but don’t want to marry us? Are you cheap, future dad? "
    ch "Is it because you spent all of your money on our phones?"
    ch "Is that why Chinami can’t make microtransactions?"
    s "It has a little more to do with there being...different types of love."
    ch "That sounds too adult for Chinami to understand. She’d rather talk about quarterly sales reports and GME’s impact on the modern economy."

    scene chinamibalcony17
    with dissolve

    ch "But she still hopes you’ll marry one of her sisters one day."
    ch "They both like you a lot. "
    ch "Big sis Yumi, too. Even though she likes to pretend she doesn’t."
    ch "And Chinami likes you just as much! She’s really happy every time you come over to visit."
    ch "You talk to her like a normal girl and not a baby. She appreciates that."
    ch "{i}I{/i} appreciate that."

    scene chinamibalcony18
    with dissolve

    ch "Thank you for spending time with me."
    ch "Come over and play more, kay?"

    scene black
    with dissolve2

    "I always feel a little strange when Chinami stops referring to herself in the third person."
    "But I need to remember that she’s a lot smarter than she lets on."
    "She really takes after her sister in that regard."
    "The one {i}actually{/i} related to her. Not the one who can’t even be bothered to come to[school] every day."
    "I guess the Chosokabes are just...naturally smart and wholesome."
    "It’s really unfortunate that they were dealt the hand they were."
    "But I guess that just gives me even more incentive to keep spending time with them."
    "Even if I have to keep coming all the way to the worst part of Kumon-mi to see them, their excitement every time I arrive makes it all worth it..."

    $ renpy.end_replay()
    $ chinami_love += 1
    $ chinamidate10 = True
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label chinamidate15:
...
```

## Code that triggers this event
File: \game\ChinamiEvents.rpy
Code:
```python
...
label callchinamimorning:
    if chinami_love >= 0 and chinamidate1 == False:
        jump chinamidate1
    if chinami_love >= 10 and christmas7 == True and chinamidate10 == False:
        jump chinamidate10
...
```