# Four Hand Massage
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinsoccer25&go=Go)



## Event preconditions
✅Kirin love greater than or equal to 25

✅Event "[Kirin: Temporary Bliss](./kirindorm25.md)" is completed (event=kirindorm25)



## Next events
* [Kirin: Made Out of Nothing](./kirinspecial30.md)

## Event properties
* ID: kirinsoccer25
* Group: Kirin
* Triggered by label: soccerfieldkirin
* Triggered by branch label: soccerfieldkirin

## Event code
File: \game\KirinEvents.rpy
Code:
```python
...
label kirinsoccer25:
    scene kirinmassage1
    with fade
    play music "soda.mp3"

    "I decide for whatever reason to spend the morning with Kirin."

    if bonus == True:
        "And also Miku, apparently, seeing as Kirin is now knuckle deep inside of her in the least interesting way possible."
    else:
        "And also Miku, who is busy receiving a wholesome and friendly massage."

    mi "Aaaaaahh...yeahhhhh...that’s the stuff..."
    ki "What the hell have you been doing lately? Your shoulders are even more knotted than that creepy religious girl’s hair."
    mi "Oh...you know...a little of this...a little of...thaaaaaat..."
    s "Good morning, you two. "

    scene kirinmassage2
    with dissolve

    ki "Morning, Sensei. Don’t mind us. Just having a little quality time. Right, Miku?"
    mi "Can’t talk...melting..."

    if kirinspecial25 == True and bonus == True:
        s "Good for you, Kirin. Still being able to massage Miku like this given decisions you have made in the past."

        scene kirinmassage3
        with dissolve

        ki "Mmm!"
        mi "You...say somethin’, Sensei?..."
        mi "Can’t hear over the sound of...my body being turned into mush."
        s "Nope. Just happy to see you’re a trusting and loyal friend who’s still giving the benefit of the doubt to someone who doesn’t deserve it."
        ki "That’s right. Rationalize what {i}you{/i} have done by comparing it to what {i}I{/i} have done. Smart."
        s "I mean, it’s all in good fun. Right, Kirin? That {i}is{/i} what life is all about apparently."
        mi "You two are being...weird..."
        mi "How ‘bout we all just...lay down on this cloud together and...let our worries wash away?..."

    scene kirinmassage4
    with dissolve

    if bonus == True:
        ki "You like that, Miku? You like it when I do it right there?"
        mi "…"
        ki "You like having my fingers deep inside of you?"
        mi "…"
        ki "Too much?"
        mi "I feel like I’ve heard those lines in some kinda adult movie or somethin’."
    else:
        ki "Are you enjoying your platonic massage, Miku?"
        mi "Guhhhhhhhhhhhhhhhhhhhhhhhhhhhh..."

    s "Mind if I step in?"

    scene kirinmassage5
    with dissolve

    mi "And do what?!"

    if bonus == True:
        ki "Oooooh a four hand massage! Leave it to Sensei to turn my definitely-not-lewd massage into a definitely-even-less-lewd massage where we {i}really{/i} loosen Miku up!"
        mi "I just wanted the knots gone! I didn’t know this was gonna turn into a thing!"
    else:
        s "I think if I karate chop you as hard as I can, all of your knots will be defeated and leave."

    mi "W-Wow! My back suddenly feels a lot better! I don’t need any sort of-"

    scene kirinmassage6
    with dissolve

    mi "Ahh~"
    ki "What were you saying, Miku? You want me to stop?"
    mi "Oh god...I can’t..."

    if kirinspecial25 == True:
        "If Kirin is this good at giving massages, I’m surprised she wasn’t able to get Miku to just submit to her back when she tried to make a move."
        "Granted, I have no way of knowing if any of that story is actually true or not since Kirin is Kirin and...isn’t exactly honest 100%% of the time."
        "But there were way too many details for me to assume it was all fabricated."

    scene kirinmassage7
    with dissolve

    ki "As you can see, I’m a bit of a master when it comes to meticulous and aggressive finger movements."

    if bonus == True:
        s "Gee, I wonder why."
        ki "Hey, all I’m saying is there’s no way I’m the only person here with a masturbation problem."
    else:
        ki "It is because I used to play the piano."

    s "Oh, okay. I guess you’re just...not holding anything back in front of Miku anymore."

    scene kirinmassage8
    with dissolve

    if bonus == True:
        ki "Miku’s currently unable to comprehend anything you or I say because I put her into massage paralysis."
        s "There is no way that’s real."
        ki "Okay. True. But her comprehension is definitely at least halved. Here, watch this."
        ki "Mikuuuu...want me to help you cum?"
        mi "What? Come where? Where are we going?"
        s "That’s just normal Miku. She was going to interpret that sentence that way no matter the state she’s in."
        ki "Hmm...want me to say something a little harder to misunderstand then?"
        s "I won’t believe this secret talent of yours unless you do."
        ki "Okaaaay. But don’t be too surprised when you realize how awesome and talented I am."
    else:
        ki "Miku is currently unable to comprehend anything you or I say because I put her into massage paralysis."
        s "Good. Because she has always wanted to play the piano and knowing you can do that would make her feel sad."

    scene kirinmassage9
    with dissolve
    stop music

    if bonus == True:
        ki "{i}I sucked our teacher’s cock.{/i}"
        mi "Wha-?!"
    else:
        ki "{i}I can play the piano.{/i}"
        mi "Wha-?!"

    scene kirinmassage10
    with dissolve

    ki "Uhh...wait! You didn’t actually hear that, did you?"
    s "Kirin, what the fuck?"

    if bonus == False:
        s "Miku hates the piano."

    scene kirinmassage11
    with dissolve

    ki "She’s never broken out of it before! How was I supposed to know that {i}now{/i} would be the-"
    mi "Are you insane?!"
    s "Yeah, are you insane?"
    ki "Not...intentionally! I didn’t mean to-"

    if bonus == True:
        mi "What kinda fuckin’ lunatic shoves a whole rooster in her mouth?! Let alone one that belongs to our teacher!"
    else:
        mi "What kinda fuckin’ lunatic learns how to play the piano?!"

    scene kirinmassage12
    with dissolve

    ki "I couldn't help myself, okay?! It sounded fun and-"
    ki "..."

    play music "soda.mp3"

    if bonus == True:
        ki "...Did you say rooster?"
    else:
        ki "...Wait, why {i}do{/i} you hate the piano?"

    scene kirinmassage13
    with dissolve

    mi "Woah. Have we been at soccer practice this whole time?"
    mi "I’ve gotta find Karin and-"

    scene kirinmassage14
    with hpunch

    ki "God fucking damnit. "
    mi "Ahhhhhyeaaaaaah............right.............there..........."
    s "Okay, well, I think that’s enough borderline tragedies for the day. It might be time to maybe {i}stop{/i} massaging Miku."
    ki "Not gonna lie, I thought my heart was about to burst out of my chest."
    s "Really? You have one of those?"

    scene kirinmassage15
    with dissolve

    ki "Yes, actually. And despite what you may believe about me, there are a handful of things that can actually cause it to start beating a little faster every once in a while."

    if bonus == True:
        s "Well it’s...nice knowing that revealing your sexual relationship with a teacher to one of your close friends is one of the things that can make that happen."
        s "I don’t really know what I’m supposed to say here. But if you keep this up any longer, I fear for Miku’s health."
        mi "Heheh...hehe...haaaaah...fingers..."
        s "See? Next thing we know, she’ll lose what little cognitive ability she actually has and slip into a comatose state that neither of us will ever be able to wake her up from."
    else:
        s "That's exactly how I feel any time there is a curly fry inside my order of regular fries."
        ki "You know you can just order curly fries, right?"
        s "Tch. You just don't understand, Kirin."

    scene kirinmassage16
    with dissolve

    ki "Mikuuuuuu~ Are you going to go into a coma?"
    mi "The comma is...a punctuation...you use to...make pauses in...sentences...and...list stuff..."
    s "Great, she’s already back in first grade."

    if bonus == True:
        ki "Mikuuuuu~ If you {i}do{/i} go into a coma, do you want me to protect you when Sensei tries to fuck your unconscious body?"
    else:
        ki "Mikuuuuu~ Tell me what a canola is..."

    s "…"

    scene kirinmassage17
    with dissolve

    ki "Teehee~"
    s "How many times-"

    if bonus == True:
        scene kirinmassage18
        with dissolve

        ki "Yeah, yeah, yeah. {i}You didn’t do anything.{/i} But can you at least let me {i}believe{/i} you did since it's more fun that way?"
        s "There’s more to life than just-"

        play sound "static.mp3"
        scene beforewefall5 with flash
        scene yumis2 with flash
        scene kirinmassage19 with flash
        stop sound

        s "Than just..."
        ki "Psst. Want me to jerk you off? Spending so much time on Miku got me horny and I kinda wanna fool around for a little while."
        s "…"
        s "We’re in a gym full of other girls right now."
        ki "Then let’s call them all over and we can all take turns on you. Whoever gets you to cum first is the winner."

        if kirinbjcontest == True:
            ki "And, need I remind you, I have a 100%% win rate in contests like this. I’m trying to keep the win streak alive."
        if ayanebjcontest == True:
            s "Is this how you redeem yourself after losing the last contest?"
            ki "I don’t know. Depends on if you like me enough to cum for me or if you’re going to wait for another basic blonde bitch and cum for her instead. "
            ki "Ball’s in your court, Sensei. "
            ki "Like, literally. You’re the coach and there are balls all over the place in here."
            ki "Speaking of which, can I start jerking you off now? I’m bored."

        s "I’m good right now, Kirin."

        scene kirinmassage20
        with dissolve

        ki "Booooring."
        s "I’m sorry to disappoint you, but being reminded of a thing I’m not proud of kind of kills the mood for me."
        s "I just want to forget everything that did or...didn’t happen and just move on."

        scene kirinmassage21
        with dissolve

        ki "No wonder you’re all knotted up if you’re stressing over something like that."
        ki "Sexual stuff aside, I can definitely help you, you know. "
        ki "I have no fucking clue what you’re going to do about the Molly situation but, at the very least, you can let me help you relieve some of the tension."

        scene kirinmassage22
        with dissolve
    else:
        play sound "static.mp3"
        scene yumis2 with flash
        scene kirinmassage22 with flash
        stop sound

    ki "It’s exhausting being such a horrible person sometimes...isn’t it?"

    if bonus == True:
        s "…"
    else:
        s "Wait a second. Does my super secret background trauma involve canola oil now? Why did that just cause me to black out?"

    scene kirinmassage23
    with dissolve

    ki "Don’t you wish you had somebody who understood you? Who saw all of those “bad” things a little differently than everyone else?"
    ki "Someone who accepts you for who you are, even though who you are shouldn’t be allowed to exist in this world?"
    s "Kirin-"

    if bonus == True:
        ki "I was too forward the other night in the dorm."
        ki "Like, the sex was {i}amazing{/i} so I don’t regret it one bit. But somewhere between the multiple orgasms and stained bedsheets, I think my point may have gotten lost."
        ki "I don’t want you to think I’m telling you to just wander around the streets of Kumon-mi [raping] women and cumming on sleeping girls in cosplay and stuff."
    else:
        ki "I'm sorry for not appreciating your spin moves. They were really cool and you are so talented."

    s "Great. Thanks for clearing that up. You really are a good person."

    scene kirinmassage24
    with dissolve

    if bonus == True:
        ki "I’m {i}saying{/i} that if you {i}do{/i} find yourself getting lost and doing things you regret, it doesn’t make you any less human than you were the day before."
        ki "We all have lapses in judgement, and people shouldn’t be ostracized for giving into those lapses from time to time- even if the end result is something really, {i}really{/i} bad."
        ki "You think Molly would still be following you around like a puppy trying to get adopted if you {i}actually{/i} hurt her? No, of course not."
        ki "Whatever you {i}did or didn’t do{/i} clearly isn’t all that bad since she doesn’t even seem to care about it."
        ki "So take one for the team and just fucking talk to her if you’re going to get so down about it. Sure beats crying like a little bitch all day and having one of the soccer players massage you, doesn’t it?"
        s "…"
    else:
        ki "Do you think you could teach me how to do them some time?..."
        ki "I think that if I do one in front of my parents, they will finally understand that I am just as good as my sister..."
        s "..."
        ki "Sensei?"

    scene kirinmassage25
    with dissolve

    s "All things considered, you’re definitely good at shoulder massages."
    ki "Had to be good at {i}something{/i}, you know?"
    ki "For Karin and Miku, it’s soccer and...friendships."

    if bonus == True:
        ki "And for me, it’s shoulder massages and blowjobs. "
    else:
        ki "And for me, it’s shoulder massages and piano. "

    ki "And while that might not seem like a good list of talents to most people, look at who you came here to spend time with today."
    s "…"

    if bonus == True:
        ki "Are you done feeling sorry for yourself now? Or do you wanna rail me in the storage room really quick and get that last bit of negative energy out?"
        s "Maybe tomorrow. One last day of feeling sorry for myself should be enough to make up for anything I may have done at the Halloween party."
        ki "That’s the Sensei I know."
        ki "And Molly? What are you going to do about her?"
    else:
        ki "So, can I learn the spin move now?"
        s "Maybe tomorrow. I just remembered a thing involving Molly that didn't happen in this game and am obligated to address that."
        ki "What are you going to do about her?"

    s "You're not actually worried about her, are you?"

    if bonus == True:
        ki "No. But the sooner you figure out what actually went down, the sooner I can finger myself to it."
        ki "Also, I’m open to threesomes with literally any girl and she seems like one of the ones who might {i}actually{/i} be into it."
        s "So it’s all about what you want in the end."
        ki "…"
    else:
        ki "Of course I am. She is a good person and I only want good things to happen to her."
        ki "And also to me."
        s "So it’s all about what you want in the end."

    scene kirinmassage26
    with dissolve

    ki "That’s right."
    ki "It’s all about what I want."
    s "…"
    ki "…"

    "Kirin presses her head against my shoulder and stops massaging me long enough for me to realize that, underneath the mask, she’s just one more [teenage]girl in a sea of hundreds I see every day."
    "And while her outlooks may be twisted and remorse has no place in her personal dictionary, she’s still as fragile and full of blood as the rest of them."
    "Perhaps she’s even more fragile."
    "Perhaps that’s why she’s focused so intensely on protecting herself from everyone and everything, even those who are on her side."
    "It’s hard to say if I’m one of the people on her side or not."
    "But I know that, even if it's not in the most ideal way, she's helped me more than anyone lately."
    "I don’t particularly {i}want{/i} to talk to her about any of what I think I might be feeling, but...strangely enough, it seems like she might be the only person I {i}can{/i} talk to right now."
    "At least without feeling like I did something wrong."
    "Which I didn’t."
    "Nothing happened on Halloween."
    "And if it did..."
    "It wasn’t my fault."

    s "…"
    ki "…"
    ki "I’ve decided to quit the soccer team."

    scene kirinmassage27
    with dissolve

    s "What?"
    ki "Yeah."
    ki "Once summer comes around, I’m just...done."
    ki "I can’t do it anymore."
    s "…"
    ki "It was nice getting to be around Miku and...I guess Karin, too. But seeing how much better everyone is than me is really fucking exhausting sometimes."
    s "I don’t really know much about soccer, but...I don’t think it’s supposed to matter how good you are as long as you’re having fun."
    ki "Sure. But what if your brain directly links how fun something is to how good you are at it?"
    ki "How am I supposed to enjoy myself when even being next to most of these girls makes me feel like a fucking useless amateur?"

    scene kirinmassage28
    with dissolve

    if bonus == True:
        ki "Wanna start a blowjob club instead? That sounds fun, doesn’t it?"
        s "So fun that I can already feel myself getting fired."
        ki "At this point, you could probably fuck someone in the middle of class and get away with it. Like {i}everyone{/i} knows that you’re into [teenage]girls and you’re still here somehow."
        s "Even so, I think the blowjob club might be a bit of a pipe dream right now."
    else:
        ki "Wanna start a hug club? That sounds fun, doesn't it?"
        s "HUG CLUB?! SIGN ME UP RIGHT NOW."

    scene kirinmassage29
    with dissolve

    ki "Maybe I’ll join some other club then. "

    if bonus == True:
        ki "Our class has a lot of girls in the manga club, but...I don’t really think something like that would be a good fit for me."
        s "Maybe a part time job?"
        ki "I don’t think work is a good fit for me either since the only place I’ve actually worked at fired me."
        s "Oh, right. That was a thing."
        ki "I don’t know. I guess I’ll just figure shit out when it happens."
        ki "All I know is that I can’t do {i}this{/i} anymore...and that I’m kiiiiiinda proud of myself for lasting as long as I have."
        s "…"
        ki "Can you be proud of me too, Sensei?"
        ki "For managing to stay afloat in a sea full of people who keep using my head to hold themselves above water?"
        s "You’re really good at metaphors too, aren’t you?"
    else:
        s "NOOOOOOOOOOOOO! I WANT THE HUG CLUB!"

    scene kirinmassage28
    with dissolve

    ki "Ooh! Metaphor club! We’d both be great at that!"

    if bonus == True:
        s "…"
        ki "Hey, it’s just an idea. You vetoed the blowjob club so I’m kinda just grasping at straws here."
        s "Just..."
        s "Keep an eye out for things you might be interested in, I guess..."
    else:
        s "KIRIIIIIIIIIIIIIIIIIIIIINNNNNNNNN!!!!!!!!!!!"

    scene black
    with dissolve2

    "Kirin stays attached to me for the rest of the gym period, but none of the others seem to mind."
    "Apparently, she’s been doing this a lot lately- spending her time in the club helping others get over their stiffness instead of doing something to remedy hers."

    if bonus == True:
        "And while I’d like to say that it’s nice she’s looking out for her teammates like that, I think there’s a high likelihood she’s only doing it to try and get into their pants."
        "I can relate."
        "It’s still weird thinking about how it will be here without her, though."
        "Even if she doesn’t ever really {i}practice{/i}, I’ve grown familiar with her place atop the stage- basking in the sunlight pouring in through the oversized windows of the gymnasium. "
        "And I’m not all that interested in seeing how the stage looks without her there."
        "Sunlight on its own has never been worth admiring to me."
    else:
        "Also, she is mean and was only joking about the hug club >=("

    $ renpy.end_replay()
    $ kirinsoccer25 = True
    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    if ayanelust10 == False:
        $ kirinspecial30skip = True

    jump saturdayafternoon

label kirinspecial30:
...
```

## Code that triggers this event
File: \game\KirinEvents.rpy
Code:
```python
...
label soccerfieldkirin:
    if kirin_lust >= 5 and christmas7 == True and kirinlust5 == False:
        jump kirinlust5
    if kirin_love >= 15 and kirindorm10 == True and kirinsoccer15 == False:
        jump kirinsoccer15
    if kirin_love >= 20 and kirinsoccer15 == True and kirinsoccer20 == False:
        jump kirinsoccer20
    if kirin_love >= 25 and kirindorm25 == True and kirinsoccer25 == False:
        jump kirinsoccer25
...
```