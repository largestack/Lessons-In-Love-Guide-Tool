# She's Always a Woman (Sara)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sara love greater than or equal to 20

* sarasex equal to True (unknown variable)

* Event [What Was](./day271.md) (Main) is completed)

* Event [The Inside of a Triangle](./sanadorm40.md) (Sana) is completed)



## Next events

None

## Event properties

* Id: sarabar20
* Group: Sara
* Triggered by label: sarasbar
* Triggered by branch label: sarasbar
* Triggered by path: sarasbar->sarabar20

## Official wiki page

[She's Always a Woman](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sarabar20&go=Go) for more details.

## Event code

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label sarabar20:
    scene barsaraayane1
    with dissolve
    play music "calmbar.mp3"

    "I decide to spend a totally normal night at the bar where nothing can possibly go wrong."

    scene barsaraayane2
    with dissolve

    ay "What’re ya drinkin’ stranger?"

    "I fail miserably."

    s "Whiskey on the rocks. No ice."
    ay "Comin’ right up, champ."
    s "Ayane, don’t agree to that. It’s literally not possible."
    ay "I ain’t Ayane, bud. I’m Efrosinia Aleksandrova, Russian spy."
    s "You are equally bad at that job as well, then."
    s "Where are the people who actually work here?"

    scene barsaraayane3
    with dissolve

    sa "I...tried to stop her...but..."
    sa "My mom is...stronger than I am..."
    ay "You still want that orange soda, champ?"
    s "Ayane, please take off that uniform."

    scene barsaraayane4
    with dissolve

    ay "Here? Shouldn't we wash the counters first?"
    sa "I think...there are bigger issues than the counters..."
    s "You guys didn’t hire Aya-"
    ay "Efrosinia."
    s "You guys didn’t hire Efrosinia, did you?"

    scene barsaraayane5
    with dissolve

    sa "No..."
    sa "Well...not really..."
    sa "Ayane and I were hanging out and...my mom asked if we could come help her with something..."
    ay "Efrosinia. But yes."
    ay "Sana and I are going to fix this bar, Sensei. Watch."
    s "How? You haven’t even served me yet and I’m literally the only customer."
    sar "I didn’t ask for their help to serve customers, Sensei. I need them for marketing stuff."

    scene barsaraayane6
    with dissolve

    s "Woah. When did you get there?"
    sar "I just sat down a second ago. Don’t freak out."
    s "Okay, good. I would have felt bad if I ignored you in favor of a younger girl wearing the same outfit."

    scene barsaraayane7
    with dissolve

    ay "Wait, Sensei! It’s me, Ayane!"
    ay "I’m not Efrosinia at all! Notice me! Not Sana’s mom!"
    sar "Ayane...why don’t you take off that uniform now, dear?"

    scene barsaraayane8
    with dissolve

    if bonus == True:
        ay "Why is everyone so horny tonight?! "
        ay "Fine! But only if Sensei is participating as well!"
    else:
        ay "But this is where all of my power is stored!"

    s "Sorry, Sana. Would you mind leaving a little early tonight?"
    sa "Huh?...What?..."
    sa "I...zoned out for a second..."
    sa "What are you doing with those two that I can’t...be around for?"
    sa "Whatever it is...I’m sure I could contribute in...some way..."

    scene barsaraayane9
    with dissolve

    ay "Really? I didn’t think you were ready for that yet."
    sar "Oh, my sweet Sana. I love you, but I think you should stay out of this."

    if bonus == True:
        ay "That’s right. Sensei is an adult who-"
    else:
        ay "Does anyone want to make a bone neck-"

    scene barsaraayane10
    with dissolve

    sar "You too, Ayane."
    sar "You can keep the outfit as payment for helping me out, though."
    ay "Thank you! It’s extremely cute and I will handle it with care!"

    if bonus == True:
        ay "I promise I won’t use it for anything naughty either!"
        sa "Na...naughty?..."
        sar "Sana, would you mind taking your friend upstairs and helping her put her normal clothes back on since she seems so against doing it on her own?"
        sa "Oh...um...yes, but..."

    sa "Do you still need me around tonight?..."
    sa "Because Ayane and I were..."
    sar "Not anymore, dear. I already told you everything I wanted to tell you."
    sar "The two of you are free to leave whenever you want since I’ll be closing any minute now."
    sa "Oh...okay..."
    sa "Umm...afro...xena?"

    scene barsaraayane11
    with dissolve

    ay "Ayane is fine now, Sana..."
    ay "And I’m coming."

    if bonus == True:
        ay "Sensei...even though she’s beautiful...remember who it is that’s carrying your child."
    else:
        ay "Sensei...if you get a minute-"
        s "No."
        ay "Ugh. FIne."

    scene barsaraayane12
    with dissolve

    "Sana takes Ayane upstairs and I find myself alone at the bar with Sara once again."
    "She takes a sip from her glass of wine, looking me directly in the eyes before saying-"

    if bonus == True:
        sar "Congratulations on the child."
        s "There is no child, Sara."
        sar "Are you sure about that?"
        s "Yes. I would have noticed if Ayane was pregnant."
        sar "Mhm~"

        scene barsaraayane13
        with dissolve

        sar "But what about me?"
        s "First off, yes. I would have noticed that as well."
        s "Secondly, put down the fucking wine if you’re pregnant, you maniac."

        scene barsaraayane14
        with dissolve

        sar "Relax, relax. There is no baby, so I’m free to get as drunk as I want."
    else:
        sar "Sometimes, I wonder if this is all actually real or if this is just some kind of crazy dream."
        s "You have an alcohol problem."

    scene barsaraayane15
    with dissolve

    sar "And, this might come as a surprise, but that isn’t very drunk at all tonight."
    s "Reaching out to [younger_girls] for help with marketing...watching your alcohol intake..."
    s "What happened to you?"
    sar "Do you want the sad answer or the really sad answer?"
    s "Give me the sad answer."
    sar "If I don’t start turning things around for this place pretty soon, I’m going to wind up losing it."
    s "Oh, yeah. I feel like we’ve established this before."
    s "What was the really sad answer?"

    if bonus == True:
        sar "That I actually am pregnant and am about to lose not only the bar and my home but my daughter and my liver as well."
        s "Yeah, that sounds a lot more serious."
    else:
        sar "That I'm actually a ghost and that this building is the only thing keeping me tied to reality."
        s "Wooooooooah."

    scene barsaraayane16
    with dissolve

    sar "Hah...I really can’t do it anymore, Sensei."
    sar "I’m getting desperate."
    sar "I used to love running this place, and I used to be so good at it."
    sar "Mine and Sana’s cuteness can only take us so far without any males around."
    sar "Maybe I just need to hire an attractive man to bring in a lot of women and-"

    scene barsaraayane17
    with dissolve

    sar "…"
    s "…"
    sar "…"
    s "No."
    sar "Not even to help little ole’ me?"

    if bonus == True:
        s "None of the girls I would attract are even old enough to drink yet."
        sar "I don’t mind bending the rules a little bit as long as I can pay rent."

    s "I can’t believe someone like you was ever allowed to run a bar in the first place."

    scene barsaraayane15
    with dissolve

    sar "Anybody can run a bar as long as they can bring in customers."
    sar "I just apparently suck at attracting female ones."
    s "So you think enlisting the help of a wallflower and an...{i}Ayane{/i} is going to help?"
    sar "I don’t expect Sana to be able to do much. But isn’t Ayane the heiress of her father’s bubble wrap company?"
    sar "She must know at least {i}something{/i} about marketing, right?"
    s "I mean...she’s definitely a lot smarter than she lets on."
    s "Maybe she can just get her father to invest in the business or something like that?"

    if bonus == True:
        sar "Ooooh maybe he’s one of those creepy dads who’s super into his daughter? "
        sar "And if I give her a job here, outfit and everything, he’ll show up and spend lots of money..."
        s "I don’t think I’m supposed to let you exploit my students like that."

        scene barsaraayane17
        with dissolve

        sar "You’re right. I should just ask her to wear it back home and seduce her father with it the old fashioned way."
        s "Sara..."

        scene barsaraayane15
        with dissolve

        sar "What? She doesn’t have to {i}do{/i} anything. Just...twirl around a couple times and say something like, “I love you, Daddy~”"
        sar "That would work on you, wouldn’t it?"
        s "Yes, but I’m a horrible person. "
        s "Besides, Ayane’s father doesn’t really pay much attention to her from what I understand. "

        scene barsaraayane18
        with dissolve

        sar "Why didn’t you tell me that before I started rambling on about seducing him! Now {i}I{/i} feel like a horrible person, too!"
        s "I liked the picture you were painting and wanted to imagine it firsthand. "

        scene barsaraayane19
        with dissolve

        sar "Mm! I knew you liked her in the barmaid outfit more than me! I could tell right away!"
        sar "The only way you can make it up to me is by getting a job here and helping me attract new customers."
        s "Again, I’m going to refuse."
        sar "What if I give you Sana?"
        s "…"
        s "Like, in what context?"
        sar "Like you marry me and become her new step-dad."
        s "Would you really be okay with someone marrying you just to get to your daughter?"
        sar "It depends on the ring!"
        sar "Also, it happens in soap operas all the time. I’m basically prepared for it at this point."
        sa "Um...prepared for...what?"
    else:
        s "That is a good idea. I will begin preparing a Powerpoint presentation immediately."
        sar "I can finally use my Shark Tank voice."

    scene black
    with dissolve

    "Sana and Ayane come back downstairs in their normal clothes and stop halfway between the counter and the door."
    "Sara and I hop off of our stools to meet them and, within a matter of seconds, things proceed to get even more difficult."

    scene barsaraayane20
    with dissolve

    sar "Sana, hypothetically, if Sensei promised to save the bar in exchange for you becoming his property-"
    s "Weird way to say “stepdaughter.”"
    sar "Would you do it?"

    scene barsaraayane21
    with dissolve

    sa "Property?!"

    if bonus == True:
        ay "You can’t have Sana! She’s mine! And I’m yours! "
        sar "Do I get to have anybody?"
        ay "No! You just exist, Sana’s mom!"
        sar "You know my name, Ayane..."
        ay "Not anymore I don’t!"
        sa "What...would I do as...pro...property?..."
        s "Your mom is kidding."
        s "What she really wants to know is how you’d react to her and I getting married."
    else:
        sar "Did I say property? I meant personal secretary."

    scene barsaraayane22
    with hpunch

    sa "That’s even worse!"

    "...It is?"

    ay "Fine! I concede! Take Sana! Just don’t get married!"
    sar "Wow. "
    sar "Those are...uhh...quite the reactions..."
    s "We’re not going to. Sara’s just desperate for a new method to turn the bar around."

    scene barsaraayane23
    with dissolve

    sar "It’s a little more than {i}just{/i} turning the bar around, you big jerk."
    sa "Hah...my heart...so fast..."
    ay "Well...umm...I {i}am{/i} really thankful for the outfit, Sara. And for always being so nice to me."

    if bonus == True:
        ay "So if there's any way I can help without relinquishing the hand of the man before me, I will do my best."
    else:
        sar "Any time, yo."

    scene barsaraayane24
    with dissolve

    ay "And...umm...Sensei-"

    if amiinvite3 == False:
        ay "If you wouldn’t mind, I’d like to maybe talk to you about something soon. "
        ay "If that’s okay. "
        s "Hm? Yeah. That’s fine."
        s "Good luck with whatever weird marketing stuff the two of you are planning on doing."
        sa "I honestly...have no idea..."
        sa "But I’ll...do my best..."
    elif thirdreset3 == True:
        s "Yeah? What's up?"
        ay "Um..."
        ay "Try not to stay too late. Ami might get jealous."
        s "Oh."
        s "Uhh...okay."
    else:
        ay "We...still need to talk about that thing I wanted to talk about..."
        s "Hey, I'm waiting on you. I am ready for this whenever."
        ay "R-Right..."
        ay "Well, then...okay. Soon."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene barsaraayane25
    with dissolve

    sar "Hah...[teenager]s are exhausting..."
    s "Tell me about it."
    sar "To think they’d be so opposed to two consenting adults having some sort of relationship together...What gives?"
    s "I think it’s less about you having a relationship and more about who you’d be having it {i}with{/i}."

    scene barsaraayane26
    with dissolve

    sar "Have you always been this popular with girls, Sensei?"

    if saradate10 == True:
        sar "I mean...you did date {i}the{/i} Niki Nakayama, so I guess you must have been."

    s "For as long as I can remember at least."

    "I manage to make myself sound cool and be completely honest at the same time."
    "Memory loss has its perks."

    sar "All the more reason to come work for me."
    s "Sure. But what can you pay me?"
    sar "I can pay you in love~"
    s "Is there a bank around here where I can trade love for cash? Because I have a [niece] to take care of."
    sar "Isn’t your [niece] the one taking care of you?"
    s "Yes, but I’m the one funding everything."
    sar "She’s not rolling in maid cafe money yet?"
    s "I don’t think- Wait, why do you know about the maid cafe?"
    sar "Oh, I go there for lunch sometimes. The prices are great and the girls are adorable."
    s "I...didn’t think you were the type to go to places like that."
    sar "Of course I am. Everyone likes maid cafes, Sensei. And anyone who says they don’t is a liar."
    s "Well, if all else fails, you could always get a job there. At least you’d still get to wear a nice outfit."
    sar "I’m not going to let this place fail."
    sar "I’ve decided."
    s "Well, I’m glad to see you taking a step in the right direction, but you should probably come up with a solid gameplan first."
    sar "I’m trying, aren’t I?"
    sar "I’m asking for help and throwing ideas out there. It’s just that none of them are very good yet."
    s "You’re also closing the bar early. How does that help at all?"
    sar "It’s just for one night."
    s "It’s not, though. You’ve been doing this a lot lately."
    s "You did the same thing when I walked Sana home that one time."
    s "You’re not going to bring in any new customers if your hours aren’t reliable."

    scene barsaraayane27
    with dissolve

    sar "..."
    sar "You..."
    sar "You think I don’t know that?"
    s "If you know it, then do something-"

    scene barsaraayane28
    with hpunch

    sar "It’s really fucking hard, okay?!"
    sar "Do you have any idea how depressing it is just sitting here for hours on end hoping literally {i}anyone{/i} shows up?!"
    sar "It used to be fine! I used to actually make money! "
    sar "Now I can’t even make it through one night without trying to figure out which bills I have to stagger to keep all of my shit on!"
    sar "I’m tired! I’m sad!"

    scene barsaraayane29
    with dissolve

    sar "And the man I like is barely doing anything to help."
    s "…"
    sar "…"
    sar "I’m sorry for yelling. And I know it’s not your responsibility."
    sar "But I’m in deep...deep trouble...and..."

    scene barsaraayane30
    with dissolve2

    sar "And I have nobody else to rely on..."
    sar "I need you to be more than just a friend for me right now. I need you to whip me into shape."

    if bonus == True:
        sar "And also just whip me. That sounds fun too."
        s "You’re not very good at crying, are you?"
        sar "I’m much better at it when I’m by myself."

    "Sara’s makeup begins to smear as her tears drip down her cheeks."
    "There’s no sobbing or heavy breathing or anything like that. Just a single, blank stare and an occasional sniffle. "
    "It’s like she’s waiting for me to say some magic words and make all of the unfortunate circumstances she’s found herself in vanish."
    "I can’t do that."
    "I can’t do anything but watch her cry and pretend to know how to help her."
    "She’ll see through that, though."
    "She might act like a [teenager], but she isn’t one."
    "She’s an adult who’s experienced adult things."
    "She’s someone who’s been burned before and it wouldn’t be right for me to burn her again after the two of us have been spending so much time together."
    "I guess this is just one of those rare occasions where honesty will need to do the trick."

    s "I don’t know what to do, Sara."
    s "I have zero experience with running a bar."
    sar "I can train you. Believe it or not, I’m still really good when I’m not drunk."
    s "I can’t work here. You know that."
    s "I already have a job."
    sar "I can’t lose this place...I have so many memories here. "
    s "I don’t want you to lose this place either. "

    "I stand up from my stool, ready to drop a cool one-liner and make a dramatic exit."
    "But it isn’t until I stand up that I realize that I don’t have any lines. "
    "And that any exit I make while she’s in this condition will be dramatic by default."

    scene black
    with dissolve2

    "So I do the only thing I know how to do."
    "I comfort her physically."
    "I bend down and wrap my arms around her, letting her cry into the fabric of my shirt."
    "It is right then that the sobbing begins."
    "She was doing such a good job at holding back, too."
    "Oh well."
    "It’s not bad to let people break as long as you’re there to make sure none of the pieces fall into a storm drain."
    "You could also collect them and put them into a box."
    "There are many, many things you can do with the shattered remnants of one’s well-being."
    "Especially remnants as colorful as this woman’s."
    "I will protect them from every storm drain in the world."

    sar "I’m sorry..."
    sar "It’s been...a really bad day..."
    s "It’s fine."
    s "I don’t know how I can help you."
    s "But I’ll try to pay more attention for your sake."
    sar "Thank you..."
    sar "That means...the world to me..."

    "I wind up having to carry Sara upstairs and put her to bed the same way I’ve done many nights before."
    "Just this time it’s from crying so hard that she gave herself a migraine and not the compulsive consumption of alcohol."
    "Goodnight, Sara."
    "Goodnight, everything."
    "I go home."

    $ renpy.end_replay()
    $ sara_love += 3
    $ sarabar20 = True
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sarabar25:
...
```

## Code that triggers this event

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label sarasbar:
    if sara_lust >= 5 and sarasex == True and saralust5 == False:
        jump saralust5
    if sara_love >= 20 and sarasex == True and day271 == True and sanadorm40 == True and sarabar20 == False:
        jump sarabar20
...
```