# Sad Girl Special
Kaori event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kaoridate15p2&go=Go)


Part of event chain [To Die, To Sleep](./kaoridate15.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: kaoridate15p2
* Group: Kaori
* Triggered by label: kaoridate15

## Event code
File: \game\KaoriEvents.rpy
Code:
```python
...
label kaoridate15p2:
    scene kaorimaidcafe1
    with dissolve
    play music "maidcafe.mp3" fadein 3.0

    k "…"
    s "…"
    k "This establishment is what I imagine the inside of a strawberry feels like."
    s "Exciting, right?"
    k "Where are we, Friend?"
    s "This is a maid cafe. "
    k "I hope they wash their hands before making our food because maids are known to get very dirty."
    s "Right, because they normally clean."

    if bonus == True:
        k "And perform unspeakable acts on anyone willing to pay them enough money."
        k "Are you going to make me watch you do something strange?"
        k "If it will make our friendship stronger, I am willing. But I may make strange noises out of interest and/or fear."
        s "You know, I didn’t think you knew about those kinds of maids."

    s "This isn’t that kind of place, though. The maids here just...say and do a bunch of cute stuff."
    s "Do you remember Ami? "
    k "The pretty girl with the red hair that you were trying to sell the first time you came to the doughnut diner?"
    s "I wasn’t trying to {i}sell{/i} her..."
    k "Do you think she would be friends with John? I have more wealth-paper than I expected to have at this point in the day and I would like to make a purchase if so."
    s "You can’t buy my-"
    s "Actually, how much are you willing to spend?"
    k "I have 50,000 yen moneys right now."
    s "You were going to pay 50,000 yen for chickens?"

    scene kaorimaidcafe2
    with dissolve

    k "I was going to pay for {i}friendship{/i}."
    s "…"
    s "Okay, fine. You can have her."
    s "Make sure she still comes over to cook me breakfast in the morning, though."

    scene kaorimaidcafe3
    with dissolve

    k "My happiness has increased!"

    scene kaorimaidcafe4
    with dissolve

    k "But my sadness is still immeasurable because she may be pretty, but does not have any feathers..."

    scene kaorimaidcafe5
    with dissolve

    a "Um...Sensei?"
    s "About time. I had to seat myself because you and Uta were yelling about stuff in the kitchen."
    a "Well...she brought her beetle to work and..."
    a "Actually, that doesn’t matter. Why are you with the spider waitress?..."
    a "And why does she look so upset?..."
    s "She just purchased you because she needs a friend for her chicken and is also currently in mourning."
    a "…"
    k "Woe is the Queen of Spiders."

    scene kaorimaidcafe6
    with dissolve

    u "Master...what’s the meaning of all these weird expressions at one table?"
    s "So, my companion here just purchased Ami because she needs a friend for her chicken and is also currently in mourning."
    u "…"
    a "…"

    scene kaorimaidcafe7
    with dissolve

    u "Works for me!"
    u "You two on a date or somethin’? Gonna take her back to your place and give her the good ole push and pray?"
    u "She check in with her mom yet?"
    a "Kaori, if Sensei invites you to his house, make sure you say no. Okay?"

    if bonus == True:
        k "Of course. If there is anything I have learned about this man, it is that he sells girls your age to the black market and that many of them are likely stored in his very home."
        a "That’s absolutely true and you should never go there. Save yourself."
    else:
        k "I will never go to Hamburger Friend's house. It is likely filled with mustard and other unfavorable condiments."

    s "Okay, okay. That’s enough badmouthing me for one afternoon."
    s "I come to you two with a mission that I was not able to complete myself."

    scene kaorimaidcafe8
    with dissolve

    u "A mission? That you needed to come here for?"
    s "Kaori is upset and I am very bad at dealing with sad people."
    a "She’s not...upset because of something you did, is she?"
    k "Friendburger told me the worst knock knock joke I’ve ever heard and then asked me to pretend he was dead."

    scene kaorimaidcafe9
    with dissolve

    u "{i}That{/i} was how you tried to cheer up a sad girl?"
    s "...It was the other way around. The “pretend I’m dead” part came first."
    a "I am somehow not surprised at all."
    u "Master, Master, Master...That’s not even close to what you’re supposed to do when somebody leans on you for help."

    scene kaorimaidcafe10
    with dissolve

    u "You’ve gotta approach her real nice and soft-like..."
    a "Mhm, mhm."
    u "Then you’ve gotta look deep into her eyes, like there’s nobody else in the whole wide world."
    a "Mhm!"
    u "And then grab her face as hard as you can and plant one right on her lips."
    u "And if she opens her mouth, that means it’s okay to slip in a little tongue."
    a "Right! And-"

    scene kaorimaidcafe11
    with hpunch

    a "Wait, no! Are you kidding me?! "
    a "That’s not even close to what he should be doing to cheer people up!"
    a "Forcing things like that on girls is assault! I should have you arrested for even suggesting that, Uta-chan!"
    s "Wow, keeping the “chan” in and everything. You’re getting good at this, Ami."
    a "I’ll get fired if I break character!"
    k "Tongue? Mouth? Open? Character?"
    k "I’ve never done this kiss move before. What if I sneeze?"
    u "Heheheh...girls. Am I right?"
    s "What does that even mean?..."
    u "{i}You’re racking up new ladies so quickly that you should know exactly what it means, Master.{/i}"
    u "{i}How many bases have you two touched yet? Three? Four? Five?{/i}"
    s "{i}You should ask your roommate about how baseball works before referring to it in a sexual manner.{/i}"

    scene kaorimaidcafe12
    with dissolve

    k "My body is prepared!"
    k "I will accept the tongue now!"
    s "Could you two just step aside for a second and-"
    a "Not a chance, {i}Master.{/i}"
    a "I doubt she’s even upset in the first place. "
    a "You’re just playing some sort of trick on Uta and me because you know we have to go along with it."
    a "I can see through you, {i}Master.{/i}"
    s "She really is upset, though. She’s dealing with death for the first time in her life."

    scene kaorimaidcafe13
    with dissolve

    u "Do you know what you want to eat yet, Princess Kaori?"
    k "One chicken sandwich please."

    "Or...maybe she’s over it already?"

    a "Oh..."
    a "I thought that {i}in mourning{/i} thing was just you exaggerating...I didn’t realize she-"

    scene kaorimaidcafe14
    with dissolve

    if bonus == True:
        k "Do not waste your worry feelings on me, pretty strawberry girl! Just come to my house and rub some cock and everything will be okay!"
    else:
        k "A euphemism once stood here!"

    a "...Excuse me?"
    u "I think she’s talking about a chicken."
    u "Or at least I {i}hope{/i} she’s talking about a chicken."

    scene kaorimaidcafe15
    with dissolve

    u "Or do I?..."
    a "How about we just...do what we normally do here and make you feel all...welcome and warm inside?"
    k "Friend already told me this was not that kind of establishment. But if you think that will make me feel better...okay!"
    k "I already prepared my body so I will not interfere with your job. I understand that you need to make yen moneys just like everyone else."
    a "Yes...by {i}serving you food and saying nice things to you because anything else would be illegal.{/i}"

    scene kaorimaidcafe16
    with dissolve

    u "Oh, that’s not true."
    a "It’s...not?"
    u "Nope! We can do {i}special{/i} stuff for the customers whenever we want as long as they’re willing to pay for it."

    scene kaorimaidcafe17
    with dissolve

    a "We can?! What?!"
    u "Yeah. I do it for Sensei all the time. He’s basically addicted."

    scene kaorimaidcafe18
    with dissolve

    a "He is?!"
    u "Yeah. You should see the look on his face whenever I finish. It’s {i}adooooorable.{/i}"
    u "I’ve even done it for Maya a few times but she doesn’t seem to be as big of a fan. Except for the one time I did it for them together. "
    u "She pretended to not like it, but I know she did."

    scene kaorimaidcafe19
    with dissolve

    a "AAAAAAHHHHHHH!!!!!"
    s "She’s obviously talking about the flavor beam, Ami."
    a "I FIGURED THAT OUT ALREADY BUT IT’S STILL-"

    scene kaorimaidcafe20
    with dissolve

    a "Wait, what do you mean “for them together?” Did Sensei come here with Maya?"
    u "Ah! No! That never happened! "
    u "Just part of the joke! I’ve never seen them together even once!"
    s "I’m sorry, Kaori. Things are normally a little more...focused than this."
    k "I am very confused but having a large amount of fun!"
    s "Well I’m glad you’re no longer being pushed down by the weight of mortality on your..."
    s "Do you have a special word for shoulders?"
    k "What is a shoulder?"
    s "The thing your shoulder tubes are attached to."
    k "Ooooooooh. A {i}shoulder.{/i}"
    s "...Yes."

    scene kaorimaidcafe21
    with dissolve

    u "So, uhh...anyway! Princess Kaori! We’re not really supposed to do this but...I know just the thing to perk you right up!"

    if bonus == True:
        k "I don’t know if I’m prepared enough to handle special services from two maids at once!"
        u "Uhhhhhhhhhh that’s not what I’m talkin’ about!"
    else:
        k "I knew I would receive at least one extra chicken today!"
        u "Uhhhhhhhhhh that’s not what I’m talkin’ about!"

    u "I was gonna ask if you wanted to try on one of the outfits that Ami and I are wearing. "

    scene kaorimaidcafe22
    with dissolve

    u "Sometimes, when I’m feelin’ down...I throw this thing on and look at myself in the mirror and think, “Woah! I can be this cute?!”"
    u "And then I do a little twirl and a jump thingy and...boom! I stomp those negative emotions into the ground!"
    k "I don’t know...the spider will get out if I become a maid."
    u "That’s totally fine. I’ve got a beetle in the back and they can be friends or something! Just put the little guy in a cage and-"
    s "She’s talking about a tattoo."
    a "Yeah...it’s a really big one too. I remember it."
    a "We’d have to be careful not to let any customers see it."
    u "We can be quick about it if you really wanna try, Princess Kaori. This is a special favor from Uta-chan and Ami-chan that we’re not even gonna charge ya for!"
    u "We can call it the...sad girl special!"

    scene kaorimaidcafe23
    with dissolve

    k "..."
    s "...?"
    s "Do you want me to...give you permission or something?"
    k "If I return as Kaori-chan, will you still be my friend?"
    s "Of course. In fact, I’ll probably like you even more."
    s "I don’t know if bringing you here gave it away or not, but I kind of have a thing for maids."
    u "Yeah, you’ve got a real problem, Master. But that’s why we like you so much."
    k "…"
    k "Just for a few hundred seconds then..."

    scene black
    with dissolve

    "Uta grabs Kaori by the wrist and pulls her down the hall into the restroom. "
    "Ami follows slowly behind, looking back at me once before disappearing in there as well."
    "The two maids exit the restroom three separate times, each time bringing either a new piece of the costume or a replacement for one that didn’t fit and..."
    "After a few minutes go by..."

    scene kaorimaidcafe24
    with dissolve

    s "Oh my God."
    a "Okay...that’s long enough, right?"
    u "Are you in love yet, Master?"
    k "Loveburger?!"
    s "That looks really good on you, Kaori."
    u "Kaori-{i}chan{/i}. She’s a part of the family now."
    s "You don’t...work here now, do you?"
    k "I don’t...think so?"
    k "Do I...look strange?"
    s "I literally just told you that you look good."
    k "Does good mean strange?"
    s "Good means good, Kaori-chan."

    scene kaorimaidcafe25
    with dissolve

    k "Th...Thank you...Master!"
    u "Ah! You called him Master and everything! You’re a natural, Kaori-chan!"
    k "Some restaurants require you to address human customers with special human names so I am...just adapting..."
    u "That’s a great human answer! I’m so proud of you!"

    "Uta really is good at caring for people, huh?"

    a "Okaaaaay...that’s definitely long enough..."

    scene kaorimaidcafe26
    with dissolve

    u "Us maids can’t really make your troubles go away for good...but we can always help you feel a little better while you’re here."
    u "So if you ever find yourself wanting a place to relax and forget about stuff, you know where to find us. Kay?"
    u "And also remember that real change comes from within! "
    u "If you’re ever gonna get over whatever hurdle you’re havin’ trouble jumpin’, throw on a cute costume, do a little twirl, and boom!"
    u "Suddenly you’ll be able to jump a lot higher."
    k "Thank you, tiny raspberry child. This building is very far from the building that I sleep in, so I will likely not come often."
    k "But I will remember you and your soft hands for the rest of my human life."

    scene kaorimaidcafe27
    with dissolve

    u "And you..."
    s "Huh? What about me?"

    if bonus == True:
        u "You just worry about keepin’ {i}your{/i} hands to yourself."
        u "This precious angel here’s just like me."
        s "A total flirt who’s secretly too nervous to ever actually do anything?"
    else:
        u "You can just shut the fuck up for a second and let me do my job."
        s "Uta, you deliver some of the most inconsistent customer service I've ever had."
        s "Kaori is my buddy and an angel and I am trusting you with her body. If you're going to get all nervous and start being mean-"

    scene kaorimaidcafe28
    with dissolve

    u "No! I mean she’s delicate and you’ve gotta treat her with care!"
    u "You think I’m nervous?!"
    k "An...angel..."
    k "That sounds nice..."
    s "Are you feeling better now?"
    k "Yes..."
    k "And I am also ready to return to my normal clothes because this outfit is very thin and I am very cold."

    scene black
    with dissolve2

    "The three girls return to the restroom and get Kaori dressed up in her winter clothes again."
    "Thankfully, no other customers showed up in the time she’d been out in the open, so there was no commotion surrounding her tattoo or anything like that."
    "Eventually, Ami and Uta-"
    "Or, excuse me, Ami-chan and Uta-chan show up with a whole spread of food to cheer Kaori up that we’re even given a discount on."
    "It seems like a great gesture at first, and I go through the entire meal feeling rather appreciative for the two of them-"
    "But as Kaori and I begin to head back outside, I notice a handwritten sign on the door advertising the exact “discount” they gave us as a lunch special."
    "I don’t know why I expected any less given the type of establishment this is...but at least I got to see Kaori get dressed up completely free of charge."
    "And that’s worth more than pretty much any discount out there..."

    $ renpy.end_replay()
    $ kaoridate15p2 = True
    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "………"
    "……"
    "…"

label kaoridate15p3:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```