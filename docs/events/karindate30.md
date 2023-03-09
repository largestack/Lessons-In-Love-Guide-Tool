# Wrong Places/Wrong Times
Karin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karindate30&go=Go)



## Event preconditions
✅Karin love greater than or equal to 30

❌Event "[Karin: Emerald Eyes](./karindate25.md)" is completed (event=karindate25)

✅karinnumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: karindate30
* Group: Karin
* Triggered by label: callkarinafternoon
* Triggered by branch label: callkarinafternoon

## Event code
File: \game\KarinEvents.rpy
Code:
```python
...
label karindate30:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."
    "If she’s putting together another care package for someone this time though, I’ll probably just sit things out."

    if makotolust30 == True:
        "As much as I liked being able to help Makoto in a way that wasn’t being borderline raped by her, I really {i}do{/i} want to spend more time with Karin alone."
    else:
        "As much as I liked being able to help Makoto in a way that was actually conducive to caring rather than showing up and destroying a picture of her father, I really {i}do{/i} want to spend more time with Karin alone."

    "Also, I want to see if I can make her hang up the phone even faster this time."

    play sound "phonebeep.wav"

    ka "Hello? "

    play music "lifeismostlygood.mp3"

    s "Let’s go on a date."
    ka "PFFT!?!:!$$$$$?~!?~??~!!!!???)*)*)&&"
    s "Wow. You’re still on the line. Good job, Karin."
    ka "W-W-W-W-W-What did you just say?!"
    s "Let’s go on a date."
    ka "Together?!"
    s "No. Let’s go on two separate dates in different locations and then tell each other about them later."
    ka "Oh. Oh, okay. "
    ka "But, wait- I don’t know any other boys. Er...uhh...{i}men.{/i}"
    s "Good. Because I was just kidding when I said that and I do think that we should go on a date {i}together.{/i}"
    ka "UTHRIURHGUIHEIFUWEUIY#)(*$*$!!!!!!!!!!!"
    s "Yeah, I’m excited too."

    if karinlied == True:
        ka "But I...you know...words!"
    else:
        ka "But...wait. I thought you were interested in Kirin?..."
        ka "You didn’t mean to call her again, did you?"
        s "Karin, I’ve never accidentally called you while trying to talk to her. And who says I can’t be “interested” in more than one person?"
        ka "Are you..."
        ka "Wait! Does that mean what I think it means?! Because that sounded a lot like a thing I didn’t think you meant but now I think you might actually mean!"
        s "Well, there’s only one way to find out and it involves meeting up with me as soon as possible."
        ka "But I wouldn’t even know what to wear and-"

    s "Cool. I’ll send you an address. Meet me there in about an hour."
    ka "Wait! Sensei! I-"

    play sound "phonebeep.wav"

    "I hang up the phone after successfully inviting Karin out on a date."
    "And while I’m sure it will be less of a traditional “date” and more of an excuse for me to ogle at her surprisingly developed (And mildly intimidating) body for a few hours, I figure she’ll still have a good time."
    "With each passing day, my certainty of her interest in {i}me{/i} increases."
    "So as she begins to open herself up like a clam in search of salt, I disintegrate into trillions of molecules and spread myself out on the large wooden table in her family’s dining room."
    "Before long, I will feel her tongue."
    "Before long, she will taste the salt."

    scene karinurbandate1
    with dissolve2
    play sound "phonebeep.wav"

    ka "A...date..."
    ka "I’m going on...an actual date..."
    ki "Congrats. Don’t forget to pack condoms."

    scene karinurbandate2
    with hpunch

    ka "AH!"
    ki "Jesus. Overreact much? They’re basically just weird shaped balloons once you take away the dick."

    scene karinurbandate3
    with dissolve

    ka "Why do you know so much about...c...condoms?"
    ki "Uhh...because I’m not five?"
    ki "You gonna tell me who that was? Or am I just going to have to stalk your Instagram to see which girl’s been hitting on you this time?"

    scene karinurbandate4
    with dissolve

    ka "It wasn’t a girl, Kirin. I wouldn’t have agreed to a “date” if it was."
    ki "Stop saying “date” like it’s some sort of foreign concept. It’s completely normal for a guy and girl to go out on a date and not even-"

    if karinlied == False:
        scene karinurbandate5
        with dissolve

        ki "Wait! Are you going on a date with fucking {i}Sensei?{/i}"
        ka "Would it be a problem if I was?..."
        ki "Yes! He’s {i}my{/i} fucking teacher! Find your own adult to suck off if you’re that curious about men all of a sudden."

        scene karinurbandate6
        with dissolve

        ka "J...Just because he’s interested in you doesn’t mean that I can’t talk to him too! "
        ka "There will be no s...sucking! We’re just going to spend time together and talk! Like friends, but...he’s a lot older and I’m...not fun!"
        ki "Well...good! Because he’s mine and I won’t let you take {i}him{/i} from me too!"
        ki "Also, what is this about him being interested in me?! Please explain it to me in vivid detail!"

        scene karinurbandate7
        with dissolve

        ka "Ask him yourself. I have to go get ready for my {i}date.{/i}"
        ki "Maybe I will. And good luck {i}getting ready-{/i} whatever the fuck that means. I can’t even {i}remember{/i} the last time you put on makeup."
        ka "Maybe I’m just...more confident in my face than...you are in yours? Jerk."

        scene karinurbandate8
        with dissolve

        ki "Our faces aren’t even that different!"
        ki "Let me go instead! I’m not doing anything today! And the fact that my older sister is going to be out with {i}my{/i} man just doesn’t fucking sit well with me!"
        ka "If he’s {i}your{/i} man, I guess you won’t have anything to worry about."
        ka "Also, Mom says it’s your turn to vacuum the house. So you {i}will{/i} have something to do today."

        scene karinurbandate9
        with dissolve

        ki "Are you fucking kidding me?!"
        ki "Since when do you just walk away when I’m arguing with you?! I’m the one who’s supposed to walk away!"
        ka "Can’t hear you! Trying to...find a good makeup tutorial!"

        scene karinurbandate10
        with dissolve

        ki "That better not be my Youtube you’re logged into, you bitch! You’ll fuck my algorithm!"

    else:
        scene karinurbandate11
        with dissolve

        ki "Wait. Are you going on a date with fucking {i}Sensei?{/i} My teacher?"
        ka "I’m sorry Kirin, but I’m not the type to kiss and tell."
        ki "You’re not the type to kiss at all."
        ka "Yeah. Even saying that made me want to curl up into a ball and throw myself out of the window."

        scene karinurbandate12
        with dissolve

        ki "Well, then why the fuck are you going out on a date with a guy?! Let alone {i}that{/i} guy?!"
        ki "How do you expect things to go when he wants more than you’re willing to give?!"
        ka "I have no idea what {i}things{/i} you think Sensei expects from me, but he’s been nothing but kind to me so far and has never once tried to force me out of my comfort zone."
        ka "I think that’s...probably why I was able to say yes just now. With anyone else, I’m sure I would have just...you know, {i}actually{/i} thrown myself out of the window."

        scene karinurbandate13
        with dissolve

        ki "Can...Can I go instead?"
        ka "Instead?..."
        ki "Yeah. Like, you can...call out sick or something."
        ka "I am no expert, but I don’t think dates work that way. And besides, I..."
        ka "I {i}want{/i} to go..."
        ki "Since when do you have literally {i}any{/i} interest in boys, though? "

        scene karinurbandate14
        with dissolve

        ka "It’s less an interest in boys and...more an interest in {i}him...{/i}I think."
        ka "I don’t know. My feelings are kind of all over the place right now...and it sounds hard to believe, but my heart is currently beating a billion times faster than it ever did during soccer."
        ka "Besides, I...I’m sure he was only using the word “date” to mess with me. It’s not like Sensei would ever actually {i}want{/i} to date me, you know? Our parents wouldn’t ever allow it either."

        scene karinurbandate15
        with dissolve

        ki "I’m sure they’d make an exception for {i}you{/i} as long as you asked."
        ka "Kirin...can you maybe try to be happy that {i}I{/i} am really happy right now? Because that would mean a lot to me."
        ki "..."
        ka "..."
        ka "Okay."
        ka "Well, I’m going to go get ready. But Mom told me to tell you it’s your turn to vacuum the house."
        ki "Yeah, of course she did. "

        scene karinurbandate10
        with dissolve

        ka "Can you help me with my makeup? I have no idea what I’m doing."
        ki "Just watch a fucking Youtube video or something."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene karinurbandate16
    with dissolve2

    ka "Umm...h...hello..."
    s "Woah."

    scene karinurbandate17
    with dissolve

    ka "It doesn’t suit me, does it?"
    s "It suits you fine. Maybe a little {i}too{/i} fine- which is an added benefit for me since now the chances of you being mistaken for a high school student have been all but eliminated."
    ka "But...But I {i}am{/i} a high school student."
    s "Not while we’re in public, you’re not."

    scene karinurbandate18
    with dissolve

    ka "I think I can...probably remember that..."
    ka "I didn’t keep you waiting too long, did I? I didn’t really expect to have to come all the way over to the urban district, so...I might’ve left a little later than I probably should have."
    s "It’s no big deal. I figured there was a decent chance that you were going to chicken out and send Kirin in your place or something anyway."

    if karinlied == False:
        scene karinurbandate19
        with dissolve

        ka "Would you...have preferred that?"
        s "Why would I personally invite you if it was your sister I was after?"
        ka "I don’t know...this is all just so crazy and...sudden..."
        ka "Kind of like a...a...dream..."

        scene karinurbandate20
        with dissolve

        ka "Oh God! This {i}is{/i} a dream, isn’t it?! This whole day has been a dream and I am going to wake up in five minutes and still have no idea how to tie the ribbon thing on my dress!"
        s "Or...that’s not going to happen and we’re going to spend the rest of the afternoon hanging out together."
        ka "That sounds exactly like what dream-Sensei would say!"
        s "You sound pretty familiar with this “dream-Sensei” guy."
        ka "You should know because you are him!"
        s "Karin, it’s really me. Like, the {i}real life{/i} me."
        ka "I don’t know if I can believe you."

        scene black
        with dissolve

        s "Okay. I guess I’ll just leave, then."
        ka "Wait! I believe you now! Don’t leave me here alone! What if someone hits on me?! I’m not prepared for that!"

    else:
        scene karinurbandate21
        with dissolve

        ka "She actually...tried to come in my place and...I thought about letting her, but..."
        ka "I was...a little too excited..."
        ka "I’ve never really...gone out with anyone like this before..."
        s "Well, I’m glad you didn’t let her come because this is the exact side of you I’ve been hoping to see for a long while now."

        scene karinurbandate22
        with dissolve

        ka "Stop..."
        s "I’m serious. I’ve always thought you-"
        ka "No, like...really stop...I think I’m about to have a heart attack..."
        s "With all the cardio you do? Doubt it. Just accept my compliments and tell me I look handsome as well or something so we can get this show on the road."

        scene karinurbandate23
        with dissolve

        ka "You look..."
        ka "You..."
        ka "..."
        s "..."
        ka "Tall."

        scene black
        with dissolve

        s "Close enough. Good job, Karin. "
        ka "Wait! Sensei, where are you going?! I don’t even know what the plan is yet!"

    "I walk off in the direction opposite where Karin came from, but not because I have a specific location in mind."
    "Is inviting someone out on a date despite not having a concrete plan of what to do if they accept a little unorthodox? I guess. "
    "But, honestly? With the way Karin looks right now, I kind of {i}want{/i} to be seen in public with her rather than spend the afternoon inside of a dimly lit movie theater or something."
    "Who knows? Maybe we’ll find a park or something and I can nod my head at all of the other women who walk by and stare at us for reasons that I’m sure are more complicated than me actually having a penis."
    "Those are pretty rare around here nowadays. "
    "But I digress."

    scene karinurbandate25
    with dissolve

    "Karin quickly catches up to me and takes her place by my side, leaving a little less space between us than I expected from her."
    "It is in this moment that I decide to let her in on the fact that I do not have a plan for this outing so that she doesn’t wind up getting depressed when we start walking around in circles."

    s "Karin, I have bad news for you."
    ka "I knew it. You {i}did{/i} want Kirin to come instead of me, didn’t you?"
    s "Stop saying that. I was just going to tell you that this is about to be the most boring date of your life because, despite being notoriously bad at making plans, I continue to do just that for reasons I don’t understand."
    ka "Oh, that’s okay. It’s also the most exciting date of my life, so you can be happy knowing that the bar is impossibly low. "
    s "I have never been happier to hear those words."

    scene karinurbandate24
    with dissolve

    ka "And I don’t think I’ve...ever been happier to be invited out before..."
    s "..."
    ka "..."
    s "Please, proceed. I want to hear more about how awesome you think I am."
    ka "Well, it’s just...you know..."
    ka "Ever since the soccer team disbanded and you stopped being our coach, I’ve been seeing you less and less while my sister still gets to see you all the time..."
    ka "So whenever she talks about you, I...start to kind of miss you, I guess..."
    ka "I miss you randomly showing up to practice and...watching over all of us to make sure we don’t get hurt."
    s "Yup. That is exactly why I was watching all of you. Good catch."

    scene karinurbandate25
    with dissolve

    ka "That was probably weird, right? Hearing that I...you know...missed you?"
    s "Not really since you’re already falling in love with me."

    scene karinurbandate26
    with dissolve

    ka "L-"
    s "Okay, maybe not {i}love-{/i} but you definitely feel something, don’t you?"
    s "I can’t really imagine you “missing” me without that being the case."

    scene karinurbandate27
    with dissolve

    ka "Well, it’s...true that I did miss you...but I don’t know if there are any...uhh...what do you call them?"
    s "Feelings?..."
    ka "Yeah! I don’t know if there are any {i}feelings{/i} involved in that! "
    ka "I just got so used to you being around that...once you stopped being around as much, I started to get sad and want to see you more."
    s "Yeah. So, to hearken back to what I was just saying, you like me."

    scene karinurbandate28
    with dissolve

    ka "S-S-S-S-S-S-S-STOP SAYING THAT! HOW ARE YOU NOT EMBARRASSED?!"
    s "Because it’s not a big deal. I literally invited you out already knowing this about you."

    scene karinurbandate29
    with dissolve

    ka "How do you know things about me before even I do?!"
    s "Because I understand this subject a lot better than you do. And that’s totally fine. Move at your own pace or whatever and I’ll just...try to match it."

    scene karinurbandate30
    with dissolve

    ka "If...that really {i}is{/i} what it is, though...isn’t that {i}bad?{/i}"
    ka "Would it even be okay for me to feel things like that for you?..."
    s "I don’t think there are any feelings that are just naturally {i}bad{/i} unless you’re the type of person to act on them. But even then, {i}this{/i} feeling wouldn’t ever be on the bad side."
    ka "I’m sorry, I just...I’m having a really hard time wrapping my head around why you’d say that."
    s "What don’t you understand?"
    ka "Just...you know..."
    ka "Don’t you see me as a kid in your eyes?"

    if karinlied == True:
        s "Didn't we already talk about this when you made sushi a while ago? I don't see you that way at all."
        ka "Yeah, but..."
        ka "You could be lying..."

    s "I literally asked you out on a date today."
    ka "Yeah, but...you can go on dates like this without wanting anything out of them, can’t you?"

    if karinlied == False:
        s "I’ve also confirmed my interest in your sister who is both younger {i}and{/i} smaller than you."

        scene karinurbandate31
        with dissolve

        ka "Don’t bring her up anymore. This is {i}my{/i} date."
        s "Sorry. Please continue."

        scene karinurbandate30
        with dissolve

    ka "I don’t know...I have this problem where I overthink a lot and every time I remember who you are and who {i}I{/i} am, I start to feel like this is all going to fall apart and that’s...really scary."
    ka "At least if things fell apart now, it’s not like the damage would be really bad. And I still have no idea what I’m doing when it comes to...uhh...{i}co-educational{/i} relationships..."
    s "Just “relationships” is fine."
    ka "Yeah. That. Me not knowing what I’m doing makes me feel like I’m just going to, like...knock everything over and cause a huge mess."
    ka "And I just don’t really want to make a mess like that in front of you or...do anything that will prevent you from wanting to see me anymore."
    ka "Which is why I probably {i}do{/i} feel the way you said I feel but it’s not like I can {i}tell{/i} you I feel that way because then I'll know that I {i}do{/i} feel that way and that feels scary."
    s "Well, it’s clear that your brain is already going in circles right now, so these words might not sound like anything important to you, but-"
    s "You have nothing to be afraid of."

    scene karinurbandate32
    with dissolve

    ka "And...you really don’t see me as a kid?"
    s "To be honest, I don’t think many people do. You both look and {i}act{/i} much older than you are, which is really all that matters to me."

    "(It doesn’t.)"

    ka "Thanks, Sensei..."
    ka "I do have one question, though."
    s "Sure. You can ask me anything."
    ka "Okay...so..."
    ka "Don’t get mad, but..."
    ka "Can we maybe...{i}not{/i} walk in circles for the rest of our date?"
    ka "I’m getting really hungry..."

    scene black
    with dissolve2

    "Karin and I spend the rest of our afternoon inside of various air-conditioned buildings so she can refill her energy stores and keep herself from sweating- a thing she is apparently very concerned about today."
    "And while I did initially claim that I wanted to remain in public and nod at other women or whatever, the heat forces me to once again act in opposition to myself as I, too, change stances."
    "Fortunately, every building we walked into, from patisserie to pop-up shop, was packed with people."
    "And I found myself, more often than not, actually thinking of Karin as my girlfriend rather than a pure soul who just keeps wandering into the wrong places at the wrong times."
    "We enjoy our day together."
    "I replay it in my head as I collapse onto my mattress and remove my belt."

    $ renpy.end_replay()
    $ karindate30 = True
    $ karin_love += 5
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon
...
```

## Code that triggers this event
File: \game\KarinEvents.rpy
Code:
```python
...
label callkarinafternoon:
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
    if karin_love >= 5 and day103 == True and karindate5 == False:
        jump karindate5
    if karin_love >= 10 and mollycafe1 == True and karindate10 == False:
        jump karindate10
    if karin_love >= 15 and day264 == True and karinlied == True and karindate15 == False:
        jump karindate15
    if karin_love >= 20 and day355 == True and karinsoccer20 == True and karindate20 == False:
        jump karindate20
    if karin_love >= 25 and makiinv3 == True and karindate25 == False:
        jump karindate25
    if karin_love >= 30 and karindate25 == True and karindate30 == False:
        jump karindate30
...
```