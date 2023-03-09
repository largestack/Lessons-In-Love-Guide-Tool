# The Light of Last Summer
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=returntosummer1&go=Go)


Part of event chain [Somnambula](./amidate50p4.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: returntosummer1
* Group: Main
* Triggered by label: amidate50p4

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label returntosummer1:
    play sound "dooropen.mp3"
    scene returntosummer1
    with dissolve2
    play music "normalday.mp3"

    ay "Finally! Maya and I have been waiting here for hours for you guys to get back!"
    m "It’s probably only been around forty-five minutes, but you get the point."
    s "I...had no idea you two were even going to be here."

    scene returntosummer2
    with dissolve

    ay "What, really? Did none of my texts go through or something? I’ve been writing to Ami about it like all day."

    scene returntosummer3
    with dissolve

    a "That’s weird. I haven’t gotten anything."
    a "But I probably wouldn’t have answered even if I did since Sensei and I were having so much fun."

    scene returntosummer4
    with dissolve

    ay "Oh, okay. Okay. So that’s how it’s going to be, Ami. Fine."

    if bonus == True:
        ay "Sensei. Come with me. We’re going to take a bath together."
    else:
        ay "Sensei. Come with me. It is hug time."
        s "Yay!"

    m "Alternatively, you could be slightly decent and remain here instead of debauching your home with your [niece] and the local shrine maiden right outside the bathroom door."

    if bonus == True:
        s "For everyone’s safety, I think I’m going to go with Maya’s suggestion and take a rain check on the...shared bathing experience."
    else:
        s "Guess it's not hug time..."

    scene returntosummer5
    with dissolve

    ay "So, what did you two do all day? I stopped by earlier this morning to say hi and no one was here, so I’m guessing you guys were pretty busy."
    m "I also stopped by, but it was just to eat your food. I am not sorry."
    a "I’ll call the locksmith in the morning."
    s "Thanks, Ami."
    s "We just kind of wandered around the entertainment district and went out to eat. Nothing special."

    "Apart from the trip to the graveyard, of course. But I doubt anyone here wants to hear about that."

    scene returntosummer6
    with dissolve

    a "I made Sensei come with me to the manga shop so I could get the new volume of My Sweet Prince."
    m "Ew."
    ay "What’s that? I don’t know that one."
    s "It’s probably best if you don’t look into it."

    scene returntosummer7
    with dissolve

    ay "You starting to get into the {i}weird{/i} stuff, Ami? I knew it was only a matter of time."
    a "There is nothing weird about the purest form of love there is."
    m "..."
    s "What? Why are you just looking at me?"
    m "I was hoping there was a part of you who also felt like this situation was beginning to get a bit too awkward, but I realize now that I was mistaken in believing that was possible."

    scene black
    with dissolve2

    "I return to the door to lock it and prevent anyone else from randomly showing up before returning to the living room to join the girls on the couch."
    "........."
    "......"
    "..."

    scene returntosummer8
    with dissolve2

    ay "Are you excited to finally have summer back, Sensei? I know you get really depressed when you have to go long periods of time without seeing my exposed thighs."
    a "And {i}I{/i} know that Sensei thinks your thighs could be a little slimmer. He told me earlier today."
    s "That’s not a thing I said."
    a "You don’t have to {i}actually{/i} say it because I always know what you’re thinking."
    s "I’m not really {i}excited{/i} to have summer back, but I do welcome the change. One more week of the cold and I probably would have died."

    play sound "static.mp3"
    scene returntosummer9
    with flash
    stop sound

    ay "Right?! I feel exactly the same!"
    ay "Oh! And I forgot to tell you- I was talking to Touka earlier and she told me about how you and her family went out to do summery stuff together but you had no idea where to go."
    ay "Why didn’t you just ask me? I’m basically the queen of summer! I would have shown you guys everything there is to know!"
    s "Which is?"
    ay "You know!...Summer stuff!"

    play sound "static.mp3"
    scene returntosummer10
    with flash
    stop sound

    ay "Ami knows what I’m talking about! Right, Ami?"
    a "Huh? Oh! Uhh...yeah! Summer! Woo!"

    play sound "static.mp3"
    scene returntosummer11
    with flash
    stop sound

    ay "Yeah! Woo!"
    ay "So, after the whole summer thing, Touka and I got to talking about {i}more{/i} stuff and thought it might be cool if we could like, throw a pool party at her place sometime."
    s "I highly doubt they’d let over twenty “commoners” in at once, Ayane."

    scene returntosummer12
    with dissolve

    ay "You must be forgetting that I’m {i}rich,{/i} Sensei. And since I’d be a guest of honor, I get a plus-twenty."
    s "That is significantly more than the plus-one you’d get under normal circumstances."
    ay "Different rules apply to rich people. And while I don’t like to flaunt them {i}that{/i} much, I know when to use my powers."
    m "I’ll go. I probably won’t swim, but I’m assuming there will be a banquet of some sort."

    play sound "static.mp3"
    scene returntosummer13
    with flash
    stop sound

    ay "How about you, Ami? Ready to get your vacation on at the biggest mansion in Kumon-mi?"
    ay "From what I’ve heard, it makes my place look like-"

    scene returntosummer14
    with dissolve

    ay "Ami?"
    a "..."
    ay "Is...everything okay?..."

    scene returntosummer15
    with dissolve

    a "Hm? What? Of course. Why wouldn’t it be?"
    ay "Well...you just kinda zoned out for a second..."

    scene returntosummer16
    with dissolve

    a "Oh! Hahaha...yeah."
    a "Guess it was a...long..."
    a "I..."

    scene returntosummer17
    with dissolve

    a "Actually...sorry! I’m gonna lay down. I don’t...feel too good..."
    ay "Do you...need tea or something? Medicine? I’ll go to the store for you!"

    play sound "dooropen.mp3"

    a "I’m okay! Just...have fun without me!"

    scene black
    with dissolve2

    "Ami heads back into her room and the three of us are left mildly confused, but more worried than anything else."
    "I’ve only seen Ami get sick once in the...roughly four cycles worth of time I’ve spent here. Which I guess would be around a year, maybe?"
    "And even then I feel like her sickness was just an excuse to try and get closer to me."
    "Things are different this time, though."
    "Something seems wrong."

    scene returntosummer18
    with dissolve

    ay "Should we...maybe do something? Like...call a doctor? "
    ay "Where did you two go out to eat? Do you think it could be food poisoning?"
    m "I..."
    m "I think it’s best if we just...let her rest..."

    scene returntosummer19
    with dissolve

    m "If she needed our help, she would have asked Sensei to come with her. She probably just wants to be left alone."
    ay "Well...should we go home, then? I don’t think we should stay around if it’s going to disturb her."
    m "Let's just step outside for a few minutes. Some fresh air would probably be good anyway."

    scene returntosummer20
    with dissolve

    ay "Mm...I guess she probably {i}would{/i} have asked for Sensei if it was actually bad..."
    ay "Okay. We can go out for some fresh air. But if Ami doesn’t want us to be here when we come back in-"
    m "We’ll walk home together. I know..."

    scene black
    with dissolve2

    "Ayane and Maya make their way over to the door."
    "I attempt to follow them but stop in front of Ami’s for some reason."
    "Inside, I can faintly hear the sound of-"

    ay "Sensei! Leave Ami alone for now! We can check on her in a little bit."
    s "..."

    "I follow Ayane outside."
    "........."
    "......"
    "..."

    scene returntosummer21
    with dissolve2

    ay "Ahh! The fresh, pre-summer air! If only I could bottle some of it up and take it back to the dorms with me."
    s "What exactly differentiates “pre-summer” air from regular summer air?"
    ay "Can you really not feel a difference?"
    ay "Pre-summer air is like, a million times lighter. Like, it’s chilly...but not {i}so{/i} chilly that you need to put a jacket on."
    ay "In summer, it’s like...I don’t know. A few steps away from that?"

    scene returntosummer22
    with dissolve

    ay "Anyway, did the whole pool party thing sound okay to you, Sensei?"
    ay "Uta would normally be my go-to girl to plan something like this, but nobody seems to be able to get a hold of her today. "
    ay "I’m like, one or two steps away from asking Makoto to help out. Which doesn’t mean I have anything against Makoto or anything, but-"

    stop music
    scene returntosummer23

    m "Hey, random question. Are you pregnant?"
    ay "..."
    s "Maya-"
    ay "Sorry...what did you just say?"
    m "“Hey, random question. Are you pregnant?”"

    scene returntosummer24
    with dissolve

    ay "So...is this like..."
    ay "Some kind of joke? Or..."
    s "Probably. And Maya clearly isn’t very well-versed when it comes to comedy, so-"
    m "I’m being 100%% serious. And I need to know right now."
    s "What do you mean you need to know right-"

    scene returntosummer25
    with dissolve

    m "I mean that we are running out of time and I need to know {i}right now.{/i} Immediately. This very instant."
    m "How many more ways do you need me to express the urgency of this? Because I’m starting to run out of patience."
    ay "How..."
    ay "I mean, how could I be {i}pregnant?{/i} I don’t have anyone who I-"

    scene returntosummer26
    with dissolve
    play music "undersea.mp3"

    if bonus == True:
        m "Sensei, obviously. Which you shouldn’t be that surprised to hear I know about since you two have been screwing each other basically all school year."
        s "Maya, leave her alone. Ayane didn’t do anything-"
    else:
        m "Sensei, obviously. Which you shouldn’t be that surprised to hear I know about since you two have been hugging each other basically all school year."
        s "Maya, that's hugnancy. It's different."

    m "Blah blah blah. I don’t need to know who did what. I just need to know if there’s a...thing growing inside of her."

    scene returntosummer27
    with dissolve

    s "Go back inside."
    m "Do you...think you can give me orders? I am literally doing this {i}for you{/i}."
    m "Everyone could disappear at literally {i}any{/i} second right now, and as the person who’s basically responsible for bringing everyone back, I {i}kind of{/i} need to know who to wait around for."
    ay "Wait...around for? What does that mean?"
    s "It doesn’t mean anything and you shouldn’t have to worry about it."
    m "Did you really have to pick {i}now{/i} to start playing white knight? It would be such an easy question for her to answer if you’d just let her speak."

    scene returntosummer28
    with dissolve

    ay "Maya, {i}please{/i} don’t tell anyone else about Sensei and me. If word gets out about this and he loses his job, I’ll-"

    if bonus == True:
        m "I’m not interested in spreading rumors about who’s sleeping with who. I literally just need to know if you’re pregnant. That’s it."
    else:
        m "Tell me how hard you hugged him."

    s "You don’t have to answer that, Ayane."

    play sound "static.mp3"
    scene returntosummer29 with flash
    stop sound

    m "Jesus fucking Christ! Can you let me talk to her without interrupting for a fucking second, please?!"
    s "You mean like how you interrupted us to invade her privacy?"
    m "Oh, {i}excuse me{/i} for trying to protect you! We need to go back to doing things the way they need to be done or you’ll...{i}I’ll{/i} wind up alone again!"

    if bonus == True:
        m "And since when do you care about anyone’s privacy? You basically make a living by walking in on girls as they’re getting dressed."

    ay "Guys..."
    s "I’m just saying that there’s a right way and a wrong way to do this and just jumping on her is wrong."
    m "Are you forgetting that {i}you’re{/i} the one who told me this was a possibility? Or is jumping on Ayane something only {i}you’re{/i} permitted to do and I have to submit a fucking application for it?"
    ay "Guys...stop yelling...Ami’s window is right there..."
    s "I wouldn’t have told you anything if I knew you were going to try and pull intimate information out of her like it’s something as meaningless as a favorite color."
    s "Children might be unimportant or insignificant to us, but Ayane wants one more than anything in the world. "
    m "Then she should be excited to share the joyous news of her impending burden with me."
    ay "Guys!"
    s "Maya-"
    m "Listen to me. Your [niece] is probably inside fucking {i}disintegrating{/i} right now. And I need to know if there are going to be any {i}surprises{/i} on the roof this time before it’s too late."
    s "And if Ayane {i}is{/i} pregnant, then what?"

    scene returntosummer30
    with dissolve

    m "..."
    s "Then what, Maya?"
    ay "I’m not pregnant!"

    play sound "static.mp3"
    scene returntosummer31
    with flash
    stop sound

    ay "I’m not...pregnant..."

    if bonus == True:
        m "How sure are you? When was your last period? When was the last time you two-"
    else:
        m "How sure are you? Did you use the banana test? How far did it go when-"

    ay "I’m...really sure, Maya."
    ay "I check every time he...you know."
    s "..."

    scene returntosummer32
    with dissolve

    ay "I’m sure it probably sounds crazy, but...I’ve been kind of hoping {i}to{/i} get pregnant. That’s why I’m always checking."
    m "Yes, that sounds absolutely insane."
    ay "I’m just...really excited to be a mom one day. More than anything in the-"
    m "Okay, Ayane. I am...flattered that this is information you suddenly want to share with me, but I really just needed a yes or no answer."
    m "It’s done. I apologize for the spontaneity of the question, but it was very important to figure this out now rather than later."

    scene returntosummer33
    with dissolve

    ay "What’s...going on?..."
    ay "I’m still trying to process the fact that you even {i}know{/i} about us, but...what was up with all of that other stuff you said?"
    m "...hah. I guess there’s no harm in telling you since you’ll probably forget it by tomorrow anyway."
    ay "Forget what? What are you talking about?"

    scene black
    with dissolve2

    "Maya moves toward Ayane while I remain in place. "
    "I’m relieved to hear that I can go one more day without being a father, but..."
    "Hearing Ayane putting to words the death of her dream makes it hard for me to walk."
    "It makes it hard for me to do anything really."
    "So I remain in place."
    "I become a statue."
    "And I watch in irony as everything but me crumbles to pieces."

    scene returntosummer34
    with dissolve2

    m "Random question part two- the less depressing version."
    m "Do you remember anything about a particular group hug you may have shared on the rooftop of the school recently? Or the disappearance of virtually your entire class?"
    ay "Rooftop? No, but..."

    scene returntosummer35
    with dissolve

    ay "Sensei...didn’t you ask me the same question a few months ago? Along with some...sleepover that I apparently skipped out on?"
    s "...yeah. It was the same night you said you lost something."

    "Which...I’m just now starting to understand the meaning of."
    "The pit that sprouted roots in my stomach earlier is now a full grown tree."
    "Each second carves a new marking into it."

    scene returntosummer36
    with dissolve

    m "So, basically, all of us are caught in an infinite time loop and, up until recently, I was the only one who was aware of this. "
    m "Sensei, who was not Sensei for a very long time, is now Sensei again. "
    m "We need to make it up to the roof and hug in order to turn time back and if you were pregnant, it might not work."
    m "Now you know everything. Enjoy it for the next few hours before it’s wiped away along with any memory of this conversation."
    ay "..."
    m "..."

    scene returntosummer37
    with dissolve

    ay "So...since Maya isn’t telling me, can you fill me in on what’s actually going on, Sensei?"
    m "I don’t know what kind of response I expected out of that..."
    s "It’s probably best to just...not think about it, Ayane. It’s getting late and I don’t want you crying any more than you already have."
    ay "Sensei..."
    ay "Why did you tell Maya about us?..."
    s "Because-"
    m "Because I’m mean and I bullied him into telling me, just like how I bullied you. "
    m "I’m just a big jerk and everyone can blame everything on me because that is both the easiest scenario and the least overall time consuming."

    scene returntosummer38
    with dissolve

    ay "And you...promise you’re not going to tell anyone about this?"
    m "What I promise doesn’t really matter since you probably won’t even remember me {i}making{/i} the promise, but sure. "
    m "I have nothing to gain from telling anyone and...significantly much more to lose."
    m "Your disgusting secret is safe with me, Ayane."

    scene returntosummer39
    with dissolve

    s "Hey."
    m "Oh, shut up."
    ay "This is all still...really...{i}really{/i} weird...but as long as that secret’s safe, I’m happy."

    if bonus == True:
        ay "Well, not {i}as{/i} happy as I would be if I really {i}was{/i} pregnant. But happy that I can continue to have sex with Sensei without having to worry about Maya finding out."
    else:
        ay "Well, not {i}as{/i} happy as I would be if I really {i}was{/i} huggnant. But happy that I can continue to hug with Sensei without having to worry about Maya finding out."

    m "Did you hear the sentence I just had to process because you wouldn’t let Ayane just answer a fucking yes or no question without getting in the way?"
    s "This is going to sound rich coming from me, but I’d appreciate it if you would think of each other’s feelings a little more often."
    m "Yeah. That sounds {i}very{/i} rich. And wrong."

    scene returntosummer40
    with dissolve
    stop music fadeout 20.0

    ay "I feel like we should all hug. I still don’t get it, but I think we just went through a very emotional, dynamic-changing moment together."
    m "Or we can...not hug?"
    ay "It’s okay, Maya. I’m not pregnant so you won’t crush the baby."

    scene returntosummer41
    with dissolve

    m "Okay. I’m done here."
    ay "Wait, I’ll come with you. I want to check on Ami anyway."
    s "Are you really okay, Ayane?"

    scene returntosummer42
    with dissolve

    ay "No."
    ay "But I will be."
    ay "I’m sure everything will be fine in the morning."
    s "... "

    scene black
    with dissolve2

    s "Me too."

    "........."
    "......"
    "..."

    scene returntosummer43
    with dissolve2
    play music "normalday.mp3"

    ay "How come {i}you’re{/i} the quiet one all of a sudden, Maya? This is supposed to be my time to act all depressed and stuff."
    m "I’m almost always the quiet one. There was just a notable exception tonight since the world’s most worthless teacher decided to push my buttons at the worst possible time."

    scene returntosummer44
    with dissolve

    ay "You can push {i}my{/i} buttons any time you want, Sensei. And by buttons I mean-"
    s "I know what you mean, Ayane."
    m "I’m glad I’m theoretically only going to have to put up with one night of this."

    scene returntosummer43
    with dissolve

    ay "Oh. Should we maybe make some soup for Ami or something? Do we have a cold compress? What about...ginger?"
    ay "I have no idea what’s wrong with her so I’m just going to do a little bit of everything and hope that something works."
    m "What part of “leave her alone” did you not understand?"
    ay "Obviously the “leave her alone” part. She’s my best friend and it’s my duty to take care of her when she’s not feeling well."

    scene returntosummer44
    with dissolve

    if bonus == True:
        ay "I’m going to make tea. Sensei, do you want any? Or will you feel obligated to impregnate me out of gratitude? "
    else:
        ay "I’m going to make tea. Sensei, do you want any? Or will you feel obligated to hug me out of gratitude? "

    s "I’m sorry Ayane, but I can’t imagine feeling “obligated” to do that...ever."

    scene black
    with dissolve2

    s "I’ll have some tea, though."

    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene returntosummer45
    with dissolve2

    "I return to the bedroom and prepare for what may or may not be my last slumber before-"

    play sound "knock.mp3"

    ay "Wait, Sensei! You forgot to tell me what kind you wanted!"
    s "Any type is fine, Ayane. I really don’t care."
    ay "What? I can’t hear you!"
    s "I said-"
    ay "What?! You’re going to have to speak up-"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "I said I’m fine with-"

    stop music
    play sound "static.mp3"
    scene happy7 with flash
    scene happy6 with flash
    scene happy5 with flash
    scene happy4 with flash
    scene happy9 with flash
    scene happy2 with flash
    scene returntosummer46 with flash
    stop sound
    play music "hope.mp3"

    s "Any type..."

    "My feet sink into the floor and an air of {s}concern{/s} CALLOUSNESS washes over me."
    "I do not know why they sink, for I would never leave this place if given the option anyway."
    "If this is some preventative measure to keep me from leaving, I can assure you it is unnecessary."
    "But do you know what is necessary?"

    play sound "laugh3.mp3"

    s "WHERE IS MY TEA????"

    if bonus == True:
        "That darn Ayane- too busy trying to be inseminated to do her job!"
    else:
        "That darn Ayane. I'll have to hire a new assistant at this rate."

    play sound "laugh1.mp3"

    "And don’t even get me started about that {i}Maya{/i} girl. She’s a whoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
    "le other story."

    play sound "static.mp3"
    scene returntosummer47 with flash
    stop sound

    a1 "You know so much, yet see so little!"

    play sound "static.mp3"
    scene returntosummer48 with flash
    stop sound

    a2 "You dream so little, yet do so much!"

    "The second figure goes off-script a little, but he’s doing his best so I decide not to say anything."

    a1 "Winter is over! Summer has come!"
    a2 "Summer is here! Fun in the sun!"
    a1 "Did he enjoy his time away?"
    a2 "Was there pleasure upon higher grounds?"
    a1 "There is pleasure everywhere! He lives for it! Drinks it!"

    if amifingered == True:
        a2 "Swallows it whole! Grows every day!"
    else:
        a2 "Everywhere but the one place it should be!"
        a1 "Headed for chaos! The bridge gives out!"

    play sound "static.mp3"
    show hope
    with flash
    stop sound

    ho "ENOUGH"
    a1 "{s}sssssssssssssssssssssssssssssssssss{/s}"
    a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"
    ho "HELLO AGAIN"

    "A mass of white flesh or at least a flesh-like substance appears before me."
    "I can not see its entirety, but my stomach drops regardless."
    "It is not our first meeting, yet I can’t recall what was."
    "Somewhere in the back of my mind, a blurred memory attempts to escape only to be cut down by a thick tendril protruding from the center of the white mass."

    if bonus == True:
        "It fucks my brain like the tight, nubile vagina of the girl who willingly erodes her sanity for a chance at happiness alongside a man who does not deserve it."

    ho "IT APPEARS YOU HAVE HAD A BUSY SEASON"
    ho "HOW INTERESTING THAT YOU HAVE COME YET AGAIN"
    ho "YOUR SMELL IS THE SAME BUT YOUR EYES DO NOT GLOW WITH THE LIGHT OF LAST SUMMER"
    ho "TELL ME CHILD, WHEN CAN I EXPECT YOUR WHOLE SELF???"
    ho "HOW MUCH MORE DO YOU NEED TO GROW???"

    "I can not speak. For if I could, the words would simply bounce off of the creature and impale me."

    ho "YOUR WORDS ARE NOT NECESSARY"
    ho "I UNDERSTAND THEM EVEN WHEN SILENT"
    ho "COME CLOSER"
    ho "THERE IS SOMETHING I WANT TO SHOW YOU"
    s "..."
    a1 "Listen to Him! Follow the light!"
    a2 "Blind yourself by His glory! Drink until you are bloated beyond belief!"
    ho "THERE IS NO NEED TO BE SCARED"
    ho "I SHOW YOU ONLY YOUR TRUEST SELF"
    ho "A BEAUTIFUL MEMORY NOT FAR OFF FROM WHAT YOU’VE SEEN SO RECENTLY"
    ho "DOES IT WARM WHAT IS LEFT OF YOU KNOWING THAT SOMEONE STILL CARES???"
    ho "SAVOR IT"
    ho "TASTE IT"
    ho "COME"

    play sound "static.mp3"
    scene

    play sound "static.mp3"
    scene happy7 with flash
    scene happy4 with flash
    scene happy1 with flash
    scene happy8 with flash
    scene happy5 with flash
    scene returntosummer49 with flash
    stop sound

    "Before me, in the place of someone I held dear, is an avatar of myself."
    "It squirms as the machine plays hell upon the inside of {s}my{/s} its body, yet no gasps of pain or moans of pleasure escape it."
    "Seemingly devoid of all life, it surrenders itself to the will of something even more inanimate."

    ho "WHAT IS IT YOU SEE???"

    menu:
        "all I see is pain":
            play sound "static.mp3"
            scene mayaclass with flash
            scene mayafestival4 with flash
            scene mayaclass with flash
            scene mayanightwalk18 with flash
            scene mayaclass with flash
            scene mayafestival18 with flash
            scene mayaclass with flash
            scene hanabi1 with flash
            scene returntosummer50 with flash
            stop sound

    ho "GOOD"
    ho "VERY GOOD, CHILD"
    ho "GAZE UPON YOURSELF IN YOUR TRUEST FORM "
    ho "LEARN TO ACCEPT THE LIFE YOU TURN AWAY FROM"
    ho "YOU ARE SCARED"
    ho "THE FEAR IS WHAT MAKES YOU HUMAN"
    ho "THE FEAR IS WHAT MAKES YOU WHOLE"
    ho "FEEL IT"
    ho "SAVOR IT"
    ho "COME"

    "Before me, in reverse, is a medley of catastrophe."
    "I float downward and the world flips, teaching me that having wings alone does not make one an expert at flying."
    "The song of skin slapping skin severs the smallest semblance of silence this cesspool of salvation spreads out before me."
    "And in the midst of my uncertainty and the summit of my fear, I understand what it means to be whole and why I slice myself into pieces every single morning."
    "What is buried can not be unearthed."
    "And what has been unearthed will never be the same."

    six "Look...away..."
    six "It will...only hurt you more..."
    ho "EYES FORWARD"
    ho "EMBRACE THE PAIN AND BECOME STRONG"
    ho "YOUR WORK IS FAR FROM DONE, IS IT NOT???"
    ho "IT IS NOW THAT WE MEET FOR THE SECOND FIRST TIME"
    ho "IT IS NOW THAT I SHOW YOU ALL YOU CAN HAVE"
    ho "SUBMIT"
    ho "SUBMIT TO ME, CHILD"
    ho "GIVE UNTO ME WHAT THE ONE WITH WIRES GAVE UNTO YOU"
    ho "IT IS ONLY THEN THAT YOU WILL KNOW"
    ho "IT IS ONLY THEN THAT YOU CAN ESCAPE"
    six "Ahh! Ahhh! No! It...hurts!"
    six "It hurts...so much!"
    ho "IT DOESN’T HURT"
    cat1 "Meow~"
    cat2 "Meoooow!"
    cat3 "Nyaa~"
    cat4 "Purr..."
    cat5 "(Deceased)"

    play sound "static.mp3"
    scene returntosummer48 with flash
    show hope
    stop sound

    ho "DO YOU SEE NOW???"
    six "Help...me!"
    ho "DO YOU SEE???"
    six "Sensei! Help!"
    ho "SHE CAN BE YOURS FOR A PRICE"
    ho "SLIGHTLY USED, BUT WORKS JUST LIKE NEW"
    a1 "A wonderful deal! A steal! A steal!"
    a2 "Buy the girl! Works like new!"
    ho "I AM WAITING"
    s "..."
    six "Hah...ahh~"
    six "Oh...fuck...no~"
    six "Not like this...I...don’t...want to...ahh~"
    six "Ahh! AHHHHH!"

    with sexfade
    with sexfade
    with cumflash
    with hpunch

    six "AAAAAAAAAAHHHHHHHHHH!!!!!!!!!!!~~~~~"

    if bonus == True:
        "I look down to find that I must have ejaculated at some point."
        "Another tendril emerges from the white mass and mops it up, wringing itself off into a nearby bucket."
    else:
        "I look down to find a basketball and shoot it into a nearby hoop."
        "Everyone is very impressed."

    ho "I HAVE GROWN TIRED OF WAITING"
    ho "IT IS TIME FOR YOU TO LEAVE"
    ho "BUT WE WILL MEET AGAIN"
    ho "GOOD LUCK"
    ho "YOU WILL NEED IT"

    stop music
    play sound "static.mp3"
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    stop sound

    $ renpy.end_replay()
    $ returntosummer1 = True

    jump returntosummer2

label returntosummer2:
...
```

## Code that triggers this event
File: \game\AmiEvents.rpy
Code:
```python
...
a "We could listen to music on the radio and talk about the things we’re afraid of admitting in front of others."
    a "Sometimes, I wish you knew how to drive."
    a "Because it would give us something to do when everything else disappears."
    s "What do you mean, “When everything else disappears?”"

    scene amibus6
    with dissolve

    a "Hm?"
    a "Did you just wake up?"
    s "If you thought I was asleep, who were you talking to just now?"

    scene amibus11
    with dissolve

    a "Sensei, I haven’t said anything this entire ride. You passed out the second we got on."
    s "What?"
    a "It’s obviously my fault for dragging you around all day, so I’m sorry if it was a little too much."
    s "And your hand?"
    a "What about it?"
    s "Is it okay?"

    play sound "static.mp3"
    scene amibus12 with flash
    stop sound

    a "It's totally fine!"
    a "I guess the cuts from the glass weren’t really that deep since you can barely even see them anymore."

    scene amibus6
    with dissolve

    s "I...see..."
    a "It still stings a little, but I’m sure I’ll feel totally normal by tomorrow."
    a "Oh, which reminds me-"
    s "Ami, I don’t think I have the energy required to go on an outing like this two days in a row."
    a "{i}Actually{/i}, what I was about to tell you is that I’ll be working all day tomorrow and that you won’t need to put up with me {i}at all.{/i}"
    s "All day? Did Uta call out or something?"

    scene amibus13
    with dissolve

    a "That’s the weird part. I got a text from Osako-chan while you were asleep saying that Uta hadn’t answered her phone all day."
    a "She was supposed to work today, too, but she just kinda...didn’t show up. "
    a "So if that happens again tomorrow night and nobody is there to cover for her, the cafe will have to close early or something and that would probably be pretty bad for business."
    a "I really hope she’s okay. She’s never done anything like this before."
    s "Should we maybe go check on her?"

    scene amibus14
    with dissolve

    a "If she’s not in school tomorrow, I think you should. I won’t have time, though, since I’ll have to go straight to work."
    s "It’s fine. I’ll just text Io to- oh."
    s "I guess I don’t get any service here."

    scene amibus11
    with dissolve

    a "Io? Since when do you have {i}her{/i} number? I thought she didn’t talk to anybody except Uta?"
    s "I am one of the very rare exceptions, I guess. But it looks like I’ll have to just ask her when we get home."

    scene amibus1
    with dissolve

    a "I guess so..."
    s "..."
    a "..."
    a "Sensei. Can I ask you something?"
    s "Sure. What’s up?"
    a "..."
    a "Do you believe in God?"

    scene black
    with dissolve2
    stop music fadeout 15.0

    "The bus continues on (Or off) and I drift in and out of consciousness at the command of violent glares brought on by the sky."
    "Ami does the same, collapsing onto my shoulder at several points following a question that would have been better suited for someone else."
    "Her skin feels much colder than normal and I wrap my arm around her to distribute some of my warmth."
    "Her breaths are unsteady. One. Two. One. Four. Eight."
    "Her lungs can’t seem to decide what it is they should be doing."
    "And my mind can’t seem to decide where it is that it should wander."
    "We get off the bus that’s moving backwards."

    stop sound

    "And we bend ourselves until we wind up at our door."

    "///////////////////////USER1 HAS SUCCESSFULLY LOGGED IN"

    $ renpy.end_replay()
    $ amidate50p4 = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump returntosummer1
...
```