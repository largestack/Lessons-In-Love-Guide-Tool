# Take Me Anywhere
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo4&go=Go)


Part of event chain [Immernachtreich](./halloweentwo3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloweentwo4
* Group: Main
* Triggered by label: halloweentwo3

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label halloweentwo4:
    "Noriko and I slip out of the party undetected and head toward the Amamiya family pond (An actual thing they have because...rich people)."
    "On the way, I think back to the last conversation I had there."
    "It was when the[school] year was about to end (Ha) and Molly and Tsuneyo were worried about transferring into another class."
    "Well, this time around, the year is somewhere near halfway done because time is weird and, to be honest, it seems like they’re not worried at all anymore."
    "I don’t know if they’ve just gotten accustomed to...time traveling or...looping or whatever other thing I wish Maya was here to try and explain to me right now-"
    "But if they’re not worried, I see no reason to worry myself."
    "Maybe that’s what Noriko called me out here for?"

    scene norikosadhalloween1
    with dissolve2
    play music "closeto.mp3"

    s "…"

    "Or maybe it’s something entirely different."
    "I mean, at this point, now that I’m back in Noriko’s life, I can’t imagine anything as simple as transferring classes dragging her down."
    "In fact, I’m pretty sure she’d transfer into any other class I ask her to because she’s just...{i}that{/i} desperate to please me."
    "So, what is it?"
    "I visualize a box of puzzle pieces and dump them onto an imaginary kitchen table somewhere in the corner of my mind."
    "The scent of a fresh baked pie being removed from the oven invades my nostrils alongside a nostalgic remembrance of some tacky patterned wallpaper."
    "Were they diamonds that I was always so caught up in staring at back then?"
    "Circles?"
    "Flowers?"
    "Something reminds me of something. But that something dies when Noriko opens her mouth to speak."

    n "So...I want to preface this by saying that I’m not actually crazy, and if it seems like I am while talking to you...I’m sorry."
    s "Well, that’s not a great start to whatever talk we’re about to have."

    scene norikosadhalloween2
    with dissolve

    n "I’m sorry I had to pull you away from the party, but I’m like...really about to freak out right now."
    n "I’m really scared. Like really really scared. But not of like...scary stuff, you know? It’s not scary stuff, but it’s still stuff that scares me. Get it?"
    s "Uhh..."

    scene norikosadhalloween3
    with dissolve

    n "Okay! Bad start. Shit. Uhh. Fuck."
    n "Okay. Okay okay."
    n "I’m scared, but not like...that something is {i}going{/i} to happen. It’s more like something-"
    s "Here’s an idea. Why don’t you just tell me what you’re-"

    scene norikosadhalloween4
    with dissolve

    n "Are you getting back together with Nee-chan?!"
    s "Woah, what?"
    n "She was in a really good mood when I went to pick up this outfit today and like...she’s never {i}that{/i} happy."
    n "So of course I asked and I was all like, “What’s got you so jumpy and bubbly?” and then she avoided the question, which means she wanted to keep something from me."
    n "And so I instinctively asked about you because you’re the only thing and-"

    scene norikosadhalloween5
    with dissolve

    n "And oh god please don’t, Sensei. Please. Please please please."
    s "…"
    n "I’m trying my best to not cry about it because like, come on, you’re not {i}mine{/i}. Like, this entire thing is about you not being mine. And you have never {i}been{/i} mine."
    n "But please no no no. Not like this. Don’t pick Niki over me again. "
    n "Is both okay? She’ll probably be against it if I’m the one who asks, but if you talk to her, she’ll-"

    scene norikosadhalloween6
    with dissolve

    n "Fuck! No! Don’t leave me! Don’t! I’ll do anything! Anything you want! Just not her!"
    s "Noriko, calm down."

    scene norikosadhalloween7
    with dissolve

    n "Okay. Whatever you want, Sensei."
    s "I’m not getting back together with your sister."
    s "She’s not even allowed to have a boyfriend with her job, and I’m not really someone who would {i}work{/i} as a boyfriend either way."

    scene norikosadhalloween8
    with dissolve

    n "But she would drop that for you! She wouldn’t even have to think about it!"
    n "She loves you just as much as I do! Which is why knowing you two are starting to move in on each other again is too much!"
    n "I can’t keep losing you to the people I’m closest to! I can’t take it anymore!"
    s "No one is losing anyone, Noriko."

    scene norikosadhalloween9
    with dissolve

    n "You’re going to leave me again! You’re going to run away with her and I’ll only see you at family reunions! "
    n "I’m not ready! I need more time to show you what I can do! Who {i}I{/i} am now! "
    n "It’s easy for Nee-chan because {i}everyone{/i} knows who she is, but NOBODY knows about me! Especially you!"
    n "I want you to know me!"
    n "Please, please please please, don’t-"
    s "Do I need to slap you or something to get this crying to stop? What am I supposed to do here?"

    scene norikosadhalloween10
    with dissolve

    n "I’d probably like it if you slapped me, so I don’t think that will work."

    if bonus == True:
        s "Why is it Niki specifically that’s causing you to act like this when you {i}have{/i} to know by now what’s going on with me and...multiple other people?"
    else:
        s "Weird. Also, how come you're okay with me hanging out with everybody else but not Niki? She is a good hug recipient."

    scene norikosadhalloween11
    with dissolve

    n "You don’t {i}love{/i} them. And if you get back with Nee-chan, you’ll {i}love{/i} her. She’s amazing and will give up literally everything for you."
    n "Which is why you need to stay away."
    n "But don’t assume that me saying you “need” to do anything is me trying to control you. You’re free to do whatever you want but oh my god please don’t."
    n "Please please please please please. Not yet. Not yet not yet not yet."
    s "Did Niki tell you {i}specifically{/i} what happened? Or are you just trying to piece things together on your own?"
    s "Because I’m not really sure how to tackle this conversation unless I know how serious you think things are."
    n "Well...she didn’t tell me {i}specifically.{/i} But why would she when she knows that {i}I{/i} want you as well?"
    n "All I know is that she’s being very positive out of literally nowhere and it is causing my brain to go haywire because oh my god I love you so much."

    if bonus == True:
        s "I fingered her."
    else:
        s "I hugged her."

    scene norikosadhalloween10
    with dissolve

    n "Mm!"

    if bonus == True:
        s "It happened after one of her concerts."
        s "I went to her hotel room, one thing led to another, and I gave her an orgasm so hard that she may have lost a few brain cells."
    else:
        s "It was a really good hug."
        s "I put my arms around her and she put her arms around me and then I kind of jumped a little because it felt so warm and I got really happy."

    n "Wh...Why are you telling me in such detail?..."

    if bonus == True:
        s "Because that’s all it was. Just a spontaneous, sexually charged encounter that meant a lot more to her than it probably did to me."
        s "You’re freaking out over nothing."
        s "If fingering someone meant forming a relationship, I’d be dating way more than just Niki right now."
    else:
        s "Because it was just a hug, you fucking psycho."

    scene norikosadhalloween9
    with dissolve

    n "You really promise it’s no more than that?! Not...that you have to promise or anything! You’re free to do-"
    s "And stop saying all of that “I’m free to do whatever I want” stuff. I know that."

    scene norikosadhalloween11
    with dissolve

    n "I’m sorry...I really am...It’s just...I heard one thing and my brain turned it into a bigger thing and now I can’t stop thinking back to when you two used to be together and how nice everything was until..."
    n "Until it wasn’t..."

    if bonus == True:
        n "I don’t want to go back there again. I don’t want to have to watch you two from the closet. I want it to be me this time. I want {i}her{/i} to watch instead."
        s "I mean, not that I’m opposed...but is that last part really necessary?"
    else:
        n "I don’t want to go back there again."
        s "Then...don't?"

    play sound "static.mp3"
    scene norikosadhalloween12
    with flash
    stop sound

    n "Do it to me now."
    s "Woah, what?"

    if bonus == True:
        n "Right now. Finger me. "
        n "Or more. Do whatever you want."
        n "Make me cum harder than you did for my sister."
        n "I’m ready. I can’t fall behind Nee-chan again. And I can't let you fall {i}for{/i} her again."
    else:
        n "Right now. Hug me "
        s "But you have so much exposed skin. What if I accidentally touch some of it?"

    n "I mean it. Right now."
    s "Noriko-"

    if bonus == True:
        n "Finger my tight little pussy until you’re able to feel all those years of sexual repression dripping down your big, strong hands."
    else:
        n "Hug me and tell me I'm the huggy girl."

    s "Noriko..."

    scene norikosadhalloween13
    with dissolve

    n "What?! Why is it okay to do it to her but not me?! "
    n "If you say something about me feeling too much like a little sister-"

    if bonus == True:
        s "It’s not that. I have no qualm with giving you as many orgasms as your malnourished body can handle."
    else:
        s "It’s not that. I just worry that you're so malnourished that the hug may hurt you."

    scene norikosadhalloween14
    with dissolve

    n "I’m not malnourished, I’m just vegetarian."
    s "I can see your ribs."

    if bonus == True:
        n "So if you have no qualms with giving me multiple orgasms and you’re okay with me being vegetarian, what’s the problem?"
        s "You’re crying and desperate and we are like fifty feet away from a door literally any one of your classmates could walk through at any moment."
    else:
        n "Is it because we're only a few feet away from stairs?! I know how much you hate hugging near stairs!"
        s "I don't want to fall and get hurt on them. It is a real danger that I think about."

    scene norikosadhalloween13
    with dissolve

    n "Then take me somewhere else! Every second I have to sit through knowing you’re closer to Nee-chan when {i}I’m{/i} the one who never gave up looking for you is literally Hell!"
    n "I tried so hard! So so so so hard! And I have nothing to show for it!"
    n "Take me! Anywhere! I’m ready!"
    s "Noriko..."
    mak "Ready for what, exactly?"

    play sound "static.mp3"
    scene norikosadhalloween15 with flash
    stop sound

    mi "You doin’ okay, Noriko?..."
    mi "Me and Makoto could hear ya screamin’ from halfway down the driveway. And it’s a pretty big driveway."
    n "I...uh..."
    mak "You’re not planning on leaving, are you? The party just started."
    n "No...um..."

    scene norikosadhalloween16
    with dissolve

    n "I’ll...talk to you later..."
    n "And...sorry..."

    scene norikosadhalloween17
    with dissolve

    "Noriko runs off and, as much as I want to take a moment and try to think about what just happened, it looks like I now have to explain things to Makoto and Miku."

    if bonus == True:
        "And while I rarely turn down the opportunity to brag about my past sexual escapades with an idol, I hardly think right now is the time."

    mi "Aww...I don’t think I’ve ever seen her look that sad before."
    mak "What on earth did you do to that poor girl, Sensei?"
    s "I think this time, it was closer to something I {i}didn’t{/i} do."
    s "But, I guess that all started from something I {i}did{/i} do, so..."

    scene norikosadhalloween18
    with dissolve

    mak "Are you drunk right now? Or are you just extremely bad at explaining yourself in tense situations?"
    s "The latter."
    mak "Well, no matter what caused Noriko to break down like that, standing around here won’t change it. "
    s "Are you actually telling me to chase after her?"
    mak "Of course not."

    scene norikosadhalloween19
    with dissolve

    mak "I’m just saying that it might be nice to get out of the cold for a bit."
    mak "It’s harder to make the right decisions when you need to focus on staying warm."
    mak "And whatever comes next, whether it be cheering her up or not, will very likely not happen out here."

    "I sigh to myself and accept that, for the millionth time, Makoto is right."
    "And also that Miku makes a surprisingly cute prince."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "The three of us stop talking about the Noriko situation altogether, understanding that things are already awkward enough, and head back up the stairs into the Amamiya residence."
    "I scan the halls on the way to the party room for a sign of Noriko but, unfortunately, it appears that I’ve lost all trace of her within the labyrinth of wealth."
    "You know, it’s a little funny."
    "She prefaced her little rant with the prospect of sounding crazy but, in terms of getting a coherent point across, I think she did pretty well."
    "Well, after all of the panicked ranting was out of the way, I mean."
    "But it’s not like you can blame a girl her age for panicking at the prospect of losing someone. "
    "Or losing {i}to{/i} someone."
    "But, like I said to her, the chances of any fire being rekindled between Niki and I just..."
    "It’s not going to happen."
    "That fuse burnt out a long time ago."
    "It’s both fortunate and unfortunate that I was not there to remember it."
    "………"
    "……"
    "…"

    scene norikosadhalloween20
    with dissolve
    play music "letsfuckingo.mp3"

    "Anyway, back to the party."

    play sound "static.mp3"
    scene norikosadhalloween21 with flash
    stop sound

    s "Jesus Christ."
    ya "Praise be."

    scene norikosadhalloween22
    with fade

    s "How the fuck did you do that?"
    ya "Do what?"
    s "Just...appear out of thin air."

    scene norikosadhalloween23
    with dissolve

    ya "Air?"
    s "You know...that invisible stuff floating around that we need to breathe in order to survive."
    ya "There are so many invisible things floating around us at all times. Are they all “air?”"
    s "Molly! Come over here. I think I found you a drinking partner."
    ya "The consumption of unblessed alcohol serves only to cloud the mind. I must remain alert at all times if I ever hope to become all that I am meant to be."
    s "I hereby bless all alcohol or whatever."

    scene norikosadhalloween24
    with dissolve

    ya "Silly Sensei~ You can’t bless anything. "
    ya "Even if you’re among those just inches away from safety, your consciousness is still far too clouded to turn {i}anything{/i} into anything else."
    s "Yasu, where is your guardian?"

    scene norikosadhalloween25
    with dissolve

    ya "Guardian?"

    play sound "static.mp3"
    scene norikosadhalloween26 with flash
    scene norikosadhalloween25 with flash
    stop sound

    ya "Whatever do you mean, Sensei?"
    ya "Why should I, the purest of the pure and an angel in training need a guardian at all when the very thought of Him guards me from all that is unblessed?"
    s "Wait...Yasu, I think I just-"

    play sound "static.mp3"
    scene norikosadhalloween27 with flash
    scene norikosadhalloween25 with flash
    stop sound

    ya "You just what? Doubted the guidance that I have so kindly provided you? Avoided a touch of wisdom from that which remains untouched?"
    s "No, I just-"

    play sound "static.mp3"
    scene norikosadhalloween28 with flash
    scene norikosadhalloween25 with flash
    stop sound

    ya "Living a life full of doubt will do nothing but make some decisions much, {i}much{/i} harder than others."
    ya "Where you rest your head at night. What direction you face when you sleep. All things that matter more than you would imagine in determining even the smallest of details."
    s "No, Yasu. There is literally a...ghost or something. She’s-"

    play sound "static.mp3"
    scene norikosadhalloween29 with flash
    scene norikosadhalloween25 with flash
    stop sound

    ya "There are no {i}ghosts{/i}, Sensei. Just the remnants of those who left this plane without accomplishing their goal."
    s "Yes. Us normal human beings refer to those as “ghosts.”"
    ya "Oh. Then I’m sorry for misunderstanding."
    s "…"
    ya "…"
    s "…"
    ya "…"

    play sound "static.mp3"
    scene norikosadhalloween30 with flash
    stop sound

    to "Hi!"
    ya "Touka! Wherever have you been?"
    to "Just making some adjustments to my makeup."
    s "Is that really you under there?"

    scene norikosadhalloween31
    with dissolve

    to "It is! Don’t I look absolutely splendid?!"
    s "I mean...yeah. But it’s not really what I imagined you coming as."

    scene norikosadhalloween32
    with dissolve

    to "Heheh! It may come as a surprise, but the truth is that I absolutely adore both Halloween {i}and{/i} horror!"

    "Doesn’t Sana like horror films too?"
    "Wait..."
    "Sana and Touka both need new friends..."

    s "…"

    "I feel like I’m so close to figuring something out, but I can’t put my finger on what it is..."

    ya "Touka? Can I ask you a question?"

    scene norikosadhalloween33
    with dissolve

    to "Of course, Yasu! Whatever do you require?"
    ya "What is “Halloween?”"
    to "…"
    ya "…"
    u "Sensei!"

    scene norikosadhalloween34
    with fade

    s "Thank you for always showing up exactly when- oh my god, you are adorable."

    scene norikosadhalloween35
    with dissolve

    u "Nyaa~"
    i "Please kill me."
    s "You should have dressed up too, Io."

    scene norikosadhalloween36
    with dissolve

    i "Why? Halloween is just one more holiday on the long list of consumer-unfriendly, corporate scams exacted for the sole purpose of profiting off of people who don’t know any better."
    i "It’s not only damaging to the lower middle class and anyone else who feels pressured to participate in the name of inclusion, but fundamentally silly and, as far as I’m concerned, a waste of time."
    i "Besides, this isn’t even how we celebrate Halloween in Japan. We should all be getting drunk and sauntering across Shibuya crossing right now. "
    s "Molly? I found you another drinking partner."

    scene norikosadhalloween37
    with dissolve

    u "{i}Hisssssss...{/i}"
    i "Don’t worry, Uta. I don’t think any less of you for feeding the money you make off of conning people into multi-billion dollar corporations who don’t care about whether you live or die. "

    scene norikosadhalloween38
    with dissolve

    u "{i}HISSSSSSSSSSSSSSSS!!!{/i}"
    i "Awwww, I love you too~"
    s "Where can I file adoption paperwork? I suddenly want a pet."

    scene norikosadhalloween39
    with dissolve

    u "This kitty’s not up for adoption, nyaa~"
    u "But if you’re still interested in providing a forever home for a cute lil’ fuzzball, may I interest you in our latest kitty over there to your left?"

    scene norikosadhalloween40
    with fade

    s "To my-"
    t "…"
    s "…"
    t "Prepare to die, bro."

    scene norikosadhalloween41
    with dissolve

    u "No, no, Tsunecchi! You’ve gotta add “Nyaa~” to the ends of your sentences. How else will anybody know you’re supposed to be a cat?"
    t "I apologize. I thought the cat paws, cat tail, and cat whiskers would have given it away."
    t "I understand now, the error of my ways."

    scene norikosadhalloween42
    with dissolve

    u "Still lookin’ for a little friend to take home and cuddle up with, nyaa?~"
    u "This one might take a little while to warm up, but she’ll be sittin’ in your lap and purrin’ her heart out before you know it, nyaa!~"
    s "I’m in. Ami is going to be so happy that we finally have a cat."
    t "Nyaaaaat a chance, bro."

    scene norikosadhalloween43
    with dissolve

    u "Uhh...Almost, Tsunecchi. We’ll get you there."
    t "I thought my purrrrrformance was purrrrrrfect, nyaa~"
    i "Oooookay, I’m gonna step outside before I get diabetes."
    i "Wanna come with me, Sensei?"
    s "Sure. I’ve already been pulled outside once today. One more time won’t hurt."

    scene black
    with dissolve2
    stop music fadeout 20.0

    $ renpy.end_replay()
    $ halloweentwo4 = True

    jump halloweentwo5

label halloweentwo5:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
c "True. But it’s not like you haven’t already seen me naked, soooo...I see no problem. Do you?"
        s "Not...really."

    scene letspartygogogo35
    with dissolve

    c "Oh! You didn’t see Yumi on the way over, did you?"
    c "I know you came with Sana, so I’m not sure if you like, bumped into her on the way and knew if she was coming or not."
    s "Why not just text her? "
    c "I’ve obviously texted her already if I’m asking you, Sensei. She just didn’t respond and I want to make sure she’s not being a brat again."
    s "Maybe she’s just...taking longer than normal to change into her costume?"

    scene letspartygogogo36
    with dissolve

    c "Yeah, I’m sure her “Antisocial [teenage]birthday girl” costume is a lot harder to put on than my...gypsy dancer or whatever this outfit is supposed to be."
    s "You don’t even know?"

    scene letspartygogogo37
    with dissolve

    if bonus == True:
        c "Nope. I just saw it at the Halloween store and thought it might make you horny, so I bought it."
        s "Ahh, yes. A respectable strategy."
        c "Is it working? "
    else:
        c "Nope. I searched the entire Halloween store for a clown costume to try and make you happy, but I couldn't find any and had to panic pick this."
        s "Well...at least you tried."
        c "Say, why do you like clowns so much anyway?"

    scene letspartygogogo38
    with dissolve

    s "How would you like to find- actually, nevermind. Hold that thought."
    c "Awwww boo~"
    n "Um...do...do you have a sec?"

    scene letspartygogogo39
    with dissolve

    s "Yeah. This is the part where everyone comes up to me and says hi, so say your piece now while you still have the screen time."
    c "Oh. My. God."
    c "Is...Is...Is..."
    c "Is that...Niki’s actual...stage outfit from the “Be My Fire” tour?"
    n "Oh...yeah. She let me borrow it for Halloween."
    s "Niki wore {i}that{/i}?"

    scene letspartygogogo40
    with dissolve

    c "Yes! But only {i}three{/i} times before it was discontinued for being too out of line with what her production company wanted her image to be!"
    c "It’s super, {i}super{/i} rare! Like, you can’t even find videos of it online anymore because they were all taken down!"
    s "Then...how do you even know about it?"

    scene letspartygogogo41
    with dissolve

    c "Never underestimate a true fan, Sensei. I know everything about Niki. {i}Everything.{/i}"

    if bonus == True:
        "I doubt you know that she’s a virgin who I recently fingered in a hotel room."
        "But that’s good. Because if you did know that, both of us would likely be dead."

    n "Uh...sorry to kill the mood and stuff, but is it okay for me to steal Sensei for a minute or two?"

    scene letspartygogogo42
    with dissolve

    c "Aww! But I just got him!"
    n "It won’t be long...I just have to ask him something."
    s "Can you not just ask it here?"

    scene letspartygogogo43
    with dissolve

    n "I...can’t..."
    n "I’m sorry. It needs to be in private."
    c "{i}Hah...{/i}Do you accept this invitation, Sensei?"
    s "I accept this invitation, Chika. Thank you for becoming my new, unofficial secretary. Please don’t tell Makoto."
    c "Just...okay. Yeah. Whatever."
    c "I’ll...let you know if I hear back from Yumi."

    scene letspartygogogo44
    with dissolve

    "Chika disappears back into the crowd of party goers, leaving Noriko and me on the outskirts of the room, seemingly unnoticed by everyone else for the time being."
    "I’m not really sure what this could be about, but she definitely looks a little more serious than normal."
    "So...whatever the problem is, I hope it’s nothing big."

    n "Come outside with me for a sec."
    s "Oh. Sure."

    scene black
    with dissolve2
    stop music fadeout 25.0

    $ renpy.end_replay()
    $ halloweentwo3 = True

    jump halloweentwo4
...
```