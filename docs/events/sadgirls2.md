# The World Outside The Walls (Haruka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Whispers of the World](./sadgirls1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: sadgirls2
* Group: Haruka
* Triggered by label: sadgirls1
* Chain sources: sadgirls1
* Chain sources path: sadgirls1

## Official wiki page

[The World Outside The Walls](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls2&go=Go) for more details.

## Event code

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label sadgirls2:
    scene makoffice0
    with dissolve2

    "I return to my office and collapse into my chair."
    "It is the only comfort I have felt since the day began, and will remain the only comfort I feel for some time to come."
    "As the world outside the walls jams its knife into the back of Kumon-mi, the bleeding begins in the form of a death."
    "A death that, up to this point, I had assumed was probable...yet denied the possibility of it as it’s atypical for the contents {i}outside{/i} of a container to slowly ooze their way back in."
    "What I want at this moment is to make some sort of analogy about how something like this is akin to ripping a bandage off. "
    "But this particular case feels more along the lines of unraveling a meter’s worth of gauze from a wound so infected that the final layer of fabric sticks to the holder’s skin and refuses to come off at all."
    "So as Makoto bleeds just like the walls of this city and everything it holds, I wonder which domino is the next to fall."
    "And I wonder what else it will topple when it finally does."

    play sound "phonering.mp3"

    "When I look down at my phone, the necessity of wonder dies quicker than Makoto’s father. "
    "The only thing left is discerning if this particular fatality is one that I should be afraid of-"
    "Or if it is one that I should revere."

    play sound "phonebeep.wav"

    s "Hello?"

    if harukasex == False:
        h "OH MY GOD!"
        s "Hey. Are you doing okay?"
        h "{i}OKAY?!{/i}"
        h "I’m doing way better than just {i}okay,{/i} dude!"
        h "My husband is still alive! "
        s "What? Really?"
        h "Yeah! I just got an automated call thingy from...whatever branch he was drafted by and it said that he’s perfectly fine and that his unit never even saw combat!"
        h "I didn’t get to speak directly to him, though- which kinda sucks because it’s been literally years since I’ve heard his voice. But still! This is amazing!"
        h "Anyway, yeah! I just needed somebody to freak out to about this and Maki didn’t answer the phone, so you’re officially the first to know!"
        s "Yeah...uhh..."
        s "So, the reason Maki didn’t answer is probably-"
        h "AAAAAHHHH! "
        h "Sorry for interrupting but I just can’t stop screaming! "
        s "Yeah...I can see-"
        h "I’ve gotta call Sara next! This is the best day ever!"
        h "Anyway, sorry for calling you while you’re at work and stuff! We can hang out soon and I can tell you more about it!"
        s "Haruka-"
        h "AAAAAAAAHHHHH! I’M SO FUCKING RELIEVED! HOLY SHIT!"

        play sound "phonebeep.wav"

        s "..."

        "Haruka hangs up the phone without giving me the chance to explain that things might not be this bright and joyous for everyone."
        "And that her experience is the exact inverse of what her closest friend is going through."

        scene black
        with dissolve2

        "I want to be happy for her. "
        "But there’s too much going on in my head right now to pump out such an emotion."
        "Especially after witnessing firsthand one more contrast between the light and the dark and the effects they may have on those caught within them."
        "I abandon the fleeting relief I have on Haruka’s behalf in favor or something more in line with what I often find myself focusing on."
        "And before I know it..."

        scene bedroom_night
        with dissolve2

        "I’m back at home in my bedroom."
        "I can’t even remember coming here."
        "I never heard back from Miku after telling her where to find her friend."
        "I never heard what happened to Yumi...or if Nodoka was able to walk out of school on her own."
        "The day just disappeared."
        "And I can’t tell if I should interpret that as a gift or if I should be angry that it was robbed from me."

        $ sadgirls2skip = True

    else:
        h "..."
        s "..."
        s "Haruka?"
        h "I..."
        h "Uhh..."
        s "..."
        h "I really need you right now..."

        "Reverence pours over me as if I’m caught in a downpour as the culling of another competitor makes its presence known through a small, electronic rectangle."
        "This is not the first time I have been brought joy by such a device- but it is the first time that I have felt some form of joy {i}today.{/i}"
        "How unfortunate that it must come at the expense of someone close to me."

        h "I know that you’re at work right now..."
        h "But if you can leave early, I-"
        s "Yeah. I’ll leave right now."
        h "You..."
        h "You’re just going to come?"
        h "You’re not even going to ask what happened?"
        s "There’s no need."
        s "I already know."
        s "And I’m sorry for your loss."
        h "..."
        s "..."
        h "Sensei..."
        h "I haven’t lost anything..."
        h "My husband is still {i}alive...{/i}"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene harukatalk1
        play music "justbehappy.mp3"
        $ renpy.pause(10, hard=True)
        scene harukasgoodday1
        with dissolve4

        s "..."
        h "..."

        "I arrive at Haruka’s house to console her about the fact that she is now a confirmed adulterer and can no longer hide behind the guise of her husband being deceased."
        "This means that on at least several occasions, while she was busy cleaning my semen out of her, her husband was wondering what she was up to."
        "If only he knew that some man he never met was providing a level of sexual gratification to his woman that he could never provide himself. "
        "I wish I could have spoken to him on the phone as well."
        "I wish we all could have had a nice conversation together."
        "I wish to hear the muffled voice of a desperate wife wishing her husband safe travels as she attempts to move her tongue in the correct ways despite my massive length pressing down upon it."
        "I wish to hear the concern of the absent party when he realizes what might be going on behind his back."
        "But more than anything-"
        "I wish to share these feelings with Haruka, who I am sure is thinking the exact same thing right now."

        h "I have to kill myself."
        h "It’s the only thing I can do to make up for what I’ve done."

        play sound "laugh1.mp3"

        s "Hold your horses, Haruka! There’s no need to go that far!"
        s "I’m sure you can just apologize to him and that everything will be a-okay!"
        s "If he {i}really{/i} loves you, he won’t care how many men empty themselves inside of your vagina."
        s "You can fuck the whole city if you want to!"
        s "I just don’t really see any reason for that when we both know that my cock is the only one that will ever satisfy you at this point."
        h "What am I supposed to do?"
        s "You mean now that you can’t just imagine he doesn’t exist anymore?"
        h "..."
        s "Maybe try the opposite?"
        s "For all we know, imagining your husband is in the next room over while I fuck your brains out might make your next climax even more enjoyable."
        h "..."
        s "Not sold? Okay. Then how about we kidnap one of my students and let him repeatedly fuck them to make up for all of the times I’ve fucked {i}you?{/i}"
        s "They’re significantly tighter than you and their sex organs probably can’t take the same level of a beating but, let’s face it, there’s no way that guy can go as {b}hard{/b} as I can anyway."
        h "..."
        s "I’ll even let you pick which girl it is since I know you’re desperate for a chance to force their lips around your clitoris as well."

        scene harukatalk2
        play music "andlove.mp3"
        $ renpy.pause(6, hard=True)
        scene harukasgoodday1
        with dissolve4

        h "I have to kill myself."
        h "It’s the only thing I can do to make up for what I’ve done."

        "I dramatically turn away, wiping the sweat from my brow as I recall the moment Haruka and I first met."
        "I was a mere EMT in training back then...trying my hardest to make a positive change in the world."
        "Or at least...that’s how things were before I saw her- standing there on the opposite side of the guardrail on the Golden Gate Bridge."

        s "Do you remember when we first met?"
        h "..."
        s "You said something similar back then..."
        s "How you wanted to die..."
        s "But as a dove flew overhead, you realized you were scared."
        s "I still remember the way your hands trembled as you desperately gripped that railing."
        s "I remember the moment you slipped...and I reached out {i}my{/i} hand to prevent you from falling."
        s "Do you think it mattered in that moment who you were pledged to?"
        s "Or was I simply in the right place at the right time? The same way I was when you needed me in the bedroom all those years later."
        h "..."
        s "Come to me, Haruka."
        s "Come to me and let me save you again."

        scene harukatalk3
        play music "ihaveto.mp3"
        $ renpy.pause(6, hard=True)
        scene harukasgoodday1
        with dissolve4

        h "I have to kill myself."
        h "It’s the only thing I can do to-"
        s "Don’t say that, Haruka! Never say that!"
        s "We can figure this out together!"

        scene harukasgoodday2
        with dissolve2

        h "We...can?"
        h "It’s not too late?..."
        s "It’s never too late, Haruka! This is only the beginning!"
        s "We can start over...we can build a new life!"
        s "I know things might be hard...but things are always hard! That’s just the way this messed up world is!"
        s "But together?...You and me?..."
        s "We can fix it."
        h "Sensei..."
        s "Also..."
        s "I am pregnant."

        scene harukasgoodday3
        with dissolve2

        h "Pregnant?"
        h "Is..."
        h "Is it-"
        s "Who else could it possibly belong to?"

        scene harukasgoodday4
        with dissolve2

        h "We...we have to think of a name!"
        s "I’ve already chosen one..."
        s "It’s BigBoy420x69..."

        scene harukasgoodday5
        with dissolve2

        h "My father’s gamertag..."
        h "You remembered..."
        s "How could I ever forget?"
        s "If it wasn’t for that, we never would have met..."
        s "We never would have fallen in love..."
        s "And we never would have won the 2003 state hockey championship together despite both of us playing with broken arms."

        scene harukasgoodday6
        with dissolve2

        h "Hahah..."
        h "Sometimes...it’s like I can still feel the puck in my hands..."
        s "It was crazy they let you get away with that since you weren’t even the goalkeeper."
        h "In a way, though...weren’t we both goalkeepers?"
        h "We made a plan...and we stuck to it...no matter how hard that plan became."

        scene harukasgoodday4
        with dissolve

        h "And here we are...six million years later, still immortal and about to have our first child."
        h "I don’t even care that I’m married anymore. I know now that I want to be with you."
        s "Haruka..."
        h "BigBoy420x70..."
        s "Ha..."
        s "I see you remember {i}my{/i} gamertag as well..."

        scene harukatalk4
        stop music
        $ renpy.pause(6, hard=True)
        scene harukasgoodday1
        with dissolve4
        play music "sensei.mp3"

        h "I have to kill myself."
        h "It’s the only thing I can do to make up for what I’ve done."
        s "..."
        h "All this time...I knew I was doing something wrong...but I kept doing it anyway..."
        h "I kept doing it anyway because I’m a horrible person. "
        h "Because I’m lonely."
        h "Because waiting stopped being possible the moment someone else I was attracted to wandered into my life."
        h "I’m pathetic."
        h "Why would anyone ever want to marry me?"

        scene harukasgoodday7
        with dissolve

        h "I mean, it’s not like I have any talents or positive qualities. I’m not even a nice person. I make everything about myself because I’m too narrow minded to worry about how anyone else feels."

        scene harukasgoodday8
        with dissolve

        h "I bet it’s the tits, right? It’s gotta be the tits. That’s all I’ve got. "
        h "Just my fat, fucking tits that I show off in front of men that I’m not even married to in hopes that they’ll push me down and fuck me before I have a chance to think about how wrong it is."
        h "It was only a matter of time until I cheated, wasn’t it? This is who I really am. A worthless, disloyal bitch in heat who gives up the second there’s any sort of pressure."
        s "..."
        h "Why aren’t you saying anything? Do you get off to listening to me degrade myself? Is that why you do it all the time? Because you like me realizing how worthless I am? Is that it?"
        s "..."

        scene harukasgoodday9
        with dissolve

        h "Fucking say something! I didn’t invite you over here thinking that you’d just fucking stand there listening to me!"
        s "Why did you invite me over then?"
        s "Because you thought I could make you feel better?"
        h "There’s nothing that can make me feel better about this!"
        h "I just found out my husband is alive! I’m supposed to be happy right now! But I’m so fucking selfish that all I can think about is how I’m going to get out of this!"
        s "And the answer you settled on is killing yourself? What’s that going to do?"

        scene harukasgoodday10
        with dissolve

        h "If you’ve got a better solution, I’d love to hear it. Because I’m {i}also{/i} too selfish to die. I just think that would be the easiest and least shameful way out of what I’m going through right now."
        s "You do realize you have it a lot better than a ton of other people in your position right now, right?"
        h "Do I? So a ton of other people {i}also{/i} let random dudes routinely fuck them in a bed their husband paid for before shipping off to fight in a war?"
        h "Cause if that’s the truth, then yeah. Maybe I will feel a little less bad."
        h "But right now? I feel like stapling my fucking vagina shut so I don’t accidentally let another cock inside of it when I get too lonely."
        s "I think you’re overreacting to this, Haruka."

        scene harukasgoodday1
        with dissolve

        h "I think you should mind your own fucking business."
        s "I only came here because you told me you needed me. But the last five minutes make it sound more like you need a therapist."
        h "Excuse me?"
        s "Unless you want to just keep using my dick as therapy, I mean. Because that was working pretty well until you heard about your husband."
        h "Are you telling me that the key to coping with how much of a slut I am is continuing to be a slut?"
        s "I’m telling you that you’re making a huge deal out of something that should be {i}good{/i} news for you."
        s "The way you’re rambling on makes it sound like you’d rather deal with burying your husband than telling him you fucked some other guy."
        h "Maybe I would? I mean, we both kind of just assumed he was dead already, didn’t we?"
        h "But now that he’s not, we’re fucked. We’re fucked because we keep fucking. It’s a big fucking mess."
        s "Then let’s stop fucking if you don’t want to. It’s as easy as that."

        scene harukasgoodday11
        with dissolve

        h "It’s not “as easy as that!” I can’t just erase all of the horrible things I’ve done by not doing them anymore! That’s fucking ridiculous!"
        s "Is that the problem? Or is the problem that you still {i}want{/i} to do those horrible things because you’ve gotten addicted to them?"

        scene harukasgoodday12
        with dissolve

        h "I’ve {i}what?{/i}"
        s "Would you rather go back to fucking yourself every night? Or keep fucking me until he gets back? Because we both know which option you like more."
        h "Addicted?..."
        s "Yeah. I think that’s the case."
        s "I think that if you really felt bad about what you were doing, you would have stopped this a long time ago."
        h "..."
        s "Again, if you want to stop, {i}we can stop.{/i} I’m not forcing you into this relationship. And given your circumstances, I don’t even really think what you did was all that wrong."
        s "You went years without hearing anything. I’m sure your husband will understand if you slipped up a little because some other guy wanted to fuck you while you were desperately horny."
        h "Desperate..."
        h "Addicted..."
        h "You..."

        scene harukasgoodday13
        with dissolve

        h "This is {i}your{/i} fault!"
        s "Oh, come on."
        h "No, it is! You talked me into sleeping with you when I was on the fence about it! You took advantage of my feelings and turned me into a fucking cheater!"
        h "I didn’t do anything wrong at all! It was all you!"
        s "Does blaming me make you feel better about yourself?"

        scene harukasgoodday14
        with dissolve

        h "Of course! I have nothing to feel bad about now that I realize I was forced into this."
        h "Just wait until my husband finds out about the man who stole his faithful and devoted wife. You’re gonna be in biiiiiiig trouble."
        s "Sure. Is there anything else you want to say? Or are we done here?"

        scene harukasgoodday15
        with dissolve

        h "I don’t know. {i}Are{/i} we done here? Or is there anything {i}you{/i} want to say to try and win me back before you have to walk away from my pussy forever?"
        h "Not that I {i}can{/i} be won back, of course. I just want to see you squirm with your {i}own{/i} sense of desperation now that the girl you tried {i}so{/i} hard to screw doesn’t want to screw you anymore."
        s "I actually don’t need this as much as I think you do. There are plenty of-"

        play sound "static.mp3"
        scene harukasgoodday16
        with flash
        stop sound

        h "Bullshit! Not with tits like these, there aren’t!"
        s "Seriously?"
        h "I can see it in your eyes! You’re barely able to hold yourself back right now!"
        h "Holy shit! Look at how insatiable you are! It’s no wonder you forced me into sex while I was missing my husband!"
        s "Okay. I’m going to leave now. But it was fun coming over here just to watch you try and completely dodge the blame for your actions. We should do this again sometime."

        scene harukasgoodday17
        with dissolve

        h "What? You’re leaving? But you haven’t even gotten to the good part yet. You know you can’t leave until you get what you came here for."
        h "You’re a pathetic, horny loser who-"

        scene black
        with dissolve

        s "See you at the cafe, Haruka."
        h "Get the fuck back here! Don’t walk away from me!"

        play sound "static.mp3"
        scene harukasgoodday18
        with flash
        stop sound

        s "Why not?"
        h "Because...you can’t leave yet! You haven’t gotten what you came here for!"
        s "I came here for a few reasons."
        s "The first was to try and hear you out...and to listen to you talk down on yourself because, let’s face it, you {i}are{/i} a bad person."
        s "You’re just not nearly as bad as you think. And you can still make this right if you actually {i}want{/i} to."
        s "The second reason I came was to figure out if you actually {i}do{/i} want to. But now, I understand that you’d rather just push the blame on someone else. "
        h "That’s not..."
        h "Wait...I didn’t mean it like-"
        s "I don’t really care {i}how{/i} you meant it. You’re an adult. So confront your issues like an adult and stop getting other people involved in them."
        h "[harukamaster]. Stop. Don’t go yet. Seriously."
        s "If you don’t want me to go, give me a reason to stay."
        h "I..."
        h "I...umm..."

        play sound "static.mp3"
        scene happy1 with flash
        scene happy9 with flash
        scene happy8 with flash
        scene happy7 with flash
        scene harukasgoodday19 with flash
        stop sound

        h "AAAAAAAAAAAAAHHHHHHHHHHHHHHHHHH!!!!!!!!!"
        h "I DON’T...KNOW WHAT...TO DO!!!"
        h "I LOVE MY HUSBAND! I LOVE HIM SO MUCH! BUT..."
        h "BUT I DON’T WANT YOU TO LEAVE!!!"
        h "AND I KNOW THAT MAKES ME A BAD PERSON! I’M HORRIBLE! UNFAITHFUL! "
        h "BUT I DON’T KNOW WHAT ELSE TO DO!!!"
        h "WHAT IF HE NEVER COMES BACK?! I DON’T WANT TO KEEP BEING ALONE!"
        s "I know. You just want someone to kill the loneliness-"

        scene harukasgoodday20
        with dissolve

        h "That’s not it either!"
        h "Just {i}someone{/i} isn’t good enough! It has to be {i}you!{/i}"
        s "I don’t-"
        h "I wasn’t lying when I told you I needed you! I do! I just...don’t know how!"
        s "..."

        scene harukasgoodday19
        with dissolve

        h "You can hate me if you want! I already hate myself! Just...don’t leave me yet! Not yet! Please!"
        s "..."
        h "PLEASE!!!!!!!!!!"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene bedroom_night
        with dissolve2

        "Despite her pleas for me to stay, I wound up leaving Haruka."
        "Though, not for good- as I may have contemplated for a moment."
        "My desire to stay can be traced to more than just how sexually compatible we are, though."
        "The truth is that I enjoy being needed. And, for some reason, she’s decided to latch onto me like some sort of sea lamprey, using her teeth to scrape away at what’s left of me so that {i}she{/i} can flourish."
        "Or maybe a leech would be a better-suited metaphor."
        "She’s something grotesque, yet anatomically interesting in the fact that there’s much I’ve left to learn about her body."
        "But, for the moment, I think it’s best if she suffers in silence. "
        "Especially considering those who have it worse."

        $ sadgirls2 = True

    play sound "phonering.mp3"

    s "..."

    play sound "phonebeep.wav"

    s "Hello?"

    "I hear a sigh on the other end of the phone- likely as a result of me answering too quickly and not giving the caller a chance to prepare her opening statement."
    "I wait, as I have a feeling that what comes next will be the handful of sleeping pills I take before bed tonight."

    maki "I..."
    maki "I wanted to say I’m sorry for yelling at you earlier."
    maki "A lot happened."
    maki "A lot that...I’m sure you figured out when you walked into the bathroom."
    s "You don’t have to apologize. I shouldn’t have followed you."
    maki "You were just worried. I understand."
    maki "Telling Miku where we were was a good move, though. She was able to cheer Makoto up a lot better than I was. "
    s "I’m sure that’s not-"
    maki "Listen, uhh..."
    maki "Can we meet up in the morning? Maybe at the cafe? "
    maki "This isn’t really something I should keep you in the dark about."
    s "I don’t really think it’s necessary to get me involved with your family matters."
    maki "It is when my daughter is one of your students."
    maki "Because there’s no way in hell that this isn’t going to have a huge impact how she is in school. And it’s something I need to know you’ll be able to handle."
    s "Then, sure..."
    s "We can meet up."
    maki "Thanks. "
    maki "Anyway, uhh...goodnight, I guess. Not that I’ll be able to sleep much. "
    maki "I just..."
    maki "Yeah."
    maki "I’ll see you tomorrow."

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "Maki hangs up the phone without giving me a chance to say goodnight."
    "But as I climb into bed, it is not her that I think about."
    "It is her daughter."
    "And the fact that she now has no choice but to fall further into me than she already has."
    "So far that even I might lose track of her."

    $ renpy.end_replay()
    stop music fadeout 10.0

    "{i}When you fall asleep, you dream of a bluejay.{/i}"
    "{i}Its beak breaks and you must help it preen its feathers.{/i}"
    "{i}The keratin tastes like the outermost layer of a coconut.{/i}"
    "........."
    "......"
    "..."

    jump sadgirls3

label sadgirls4:
...
```

## Code that triggers this event

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
"A tidal wave crashes into me and forces me back."
    "But as I turn around to watch it disappear along with the rest of the ocean, I’m reminded that this is all just a metaphor I’ve been using to make myself feel better."
    "And that the harsh reality is that I’ve just walked into a private conversation in which the lives of two people who mean something to me are violently dismantled."
    "But when I make an effort to leave, my shoes scuff the floor. "
    "And the abruptness of the sound makes it difficult for me to find another metaphor to cling to."

    play sound "static.mp3"
    scene fatesealedinradiowaves16
    with flash
    stop sound

    maki "I told you not to follow me!"
    s "I didn’t mean to-"
    maki "Leave! Get out!"
    s "I’m sorry. I didn’t know-"
    maki "I said get out! "
    maki "You have nothing to do with this!"

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "She’s right."
    "I have nothing to do with this."
    "Which is why I don’t have a problem with just walking away."
    "Which is why I don’t spend the next five minutes standing outside of a bathroom door in a hall I seldom visit."
    "Which is why I hear none of what comes next."
    "I’m already somewhere else."

    play sound "static.mp3"
    scene fatesealedinradiowaves17
    with flash
    stop sound

    maki "Hey! Hey! Listen to me!"
    maki "We’re going to get through this! Together! You and me!"
    maki "I know it’s not what you want, but I’m right here! Okay?! I’m right here and I’m not going anywhere!"
    maki "Mommy’s got you!"
    maki "I’ll read your report cards. I won’t really know what they mean, but I’ll read them! Okay?"
    maki "And...I’ll learn to sew! Or something! In case you ever rip your uniform! "
    maki "I’ll do whatever you need! And that includes being proud of you! Because it might not seem like it sometimes, but I am! I am so...{i}so{/i} proud of you."
    mak "I want my dad! "
    mak "I want my daddy!"

    scene fatesealedinradiowaves18
    with dissolve

    maki "I know, baby. I know you do. I want him too. But it’s just us now...and that’s okay!"
    maki "That’s okay because it’s been {i}just us{/i} for a few years anyway, and we’ve been doing great!"
    maki "I’m not saying things will be easy. This is going to be the hardest thing you’ll ever have to go through. But don’t think for a second that you’re alone."
    maki "We’re in this together. We can cry {i}together.{/i} "
    maki "We can miss him {i}together.{/i}"
    mak "It’s too soon! I wasn’t ready!"
    mak "I never got to say goodbye! I never got to say goodbye!"
    maki "We can still talk to him! And wherever he is, he’ll hear us! But for now, just..."
    maki "Just rely on me, baby. Cry as much as you want and I’ll be right here to hold you tight."
    mak "Mom! Tell me it’s not real! Tell me this is all just a nightmare! And that when I wake up, Daddy will be home and we’ll all go on a big trip together!"
    maki "We can still go on a trip! You and me! Mother and daughter! To anywhere you want! Anywhere at all!"
    mak "I want to see my dad!"

    play sound "dooropen.mp3"
    scene fatesealedinradiowaves19
    with dissolve

    maki "Didn’t I tell you stay out of-"

    scene fatesealedinradiowaves20
    with dissolve

    maki "Miku..."
    mi "Maki...Sensei told me where you were but..."
    mi "He wouldn’t tell me what happened..."
    maki "It’s..."
    maki "We can talk later, sweetheart. Makoto needs to-"
    mak "Daddy’s gone! "

    scene fatesealedinradiowaves21
    with dissolve

    mi "No..."
    mi "Makoto, I..."
    maki "Oh, fuck it. Come join us on the floor. You’re basically my second daughter anyway."
    mi "Okay...but...ummm...I’m probably gonna cry too..."
    maki "I really don’t care. She needs all the love she can get right now and I just..."
    maki "I guess what I have isn’t enough..."

    scene black
    with dissolve2
    stop music fadeout 25.0

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ sadgirls1 = True

    jump sadgirls2
...
```