# Somewhere I Belong (Imani)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Imani love greater than 0

* Event [Don't Hold Back](./wakanaspecial15.md) (Wakana) is completed)

* imaninumber equal to True (unknown variable)



## Next events

* [Imani: A Hairline Fracture](./imanidate5.md)

## Event properties

* Id: imanidate1
* Group: Imani
* Triggered by label: callimaninight
* Triggered by branch label: callnight
* Triggered by path: callnight->callimaninight->imanidate1

## Official wiki page

[Somewhere I Belong](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=imanidate1&go=Go) for more details.

## Event code

File: (install folder)\game\ImaniEvents.rpy

Code:
```python
...
label imanidate1:
    play sound "phonebeep.wav"

    "I tap on Imani’s name in my phone and wait for her to answer, hoping that her constant, overly-friendly banter with me isn’t just her brand of fucking around."
    "We’ve hung out after work several times before, but never without the company of someone else. So I guess tonight is the night I find out if she’s cool with that or not."
    "If not, I’ll just...find something else to do instead."
    "But if she {i}is,{/i} I can finally begin the process of figuring out how to sleep with her."
    "Watch out, Imani. I’m coming for you."

    play sound "phonebeep.wav"
    play music "summerwind.mp3"

    ima "Yo, Senpai! What’s goin’ on?"
    s "Hey. What are you doing tonight?"
    ima "Well, right now, I’m busy grading papers for the work {i}I{/i} assigned to everyone while you were sleeping in your office the other day."
    s "What kind of work are you giving our students behind my back?"
    ima "I just told them to write two pages about shit they think is cool. "
    ima "Did you know both Ami {i}and{/i} Ayane wrote about you? I’m worried they may have copied each other’s work."
    s "Stop doing that and hang out with me instead."
    ima "{i}Just{/i} you?"
    ima "Is this a booty call? "
    s "...Could it be?"
    ima "Mmm...we probably shouldn’t. I like whatever we have going on right now."
    ima "Best to keep stuff professional in the least professional way possible, you know?"
    ima "Plus, I don’t want you holding my job hostage in exchange for being at the beck and call of your endless libido."
    s "It’s not {i}endless.{/i} I have a recharge period."
    ima "Well, don’t count on me to drain that battery of yours. "
    ima "If you {i}do{/i} want to come over and get comfortable, though, I’d probably open the door for you."
    s "I’m getting mixed signals here. People don’t normally invite me over unless they want to have sex with me."
    s "Or...need help making soup."
    ima "I like soup."
    s "Just send me your address, I guess."
    ima "Right-o. Comin’ at you, brother. "
    s "Don’t call me that."
    ima "Nii-chan?"
    s "Slightly better."
    ima "Daddy?"
    s "Again with the mixed signals."
    ima "Don’t keep me waiting, Senpai-Niichan-Daddy. It’s sooooo lonely over here."

    scene black
    with dissolve
    play sound "phonebeep.wav"

    "I hang up the phone before I fall victim to the never-ending games of my student teacher and patiently await her address so I can be led on some more."
    "I half expect it to be similar to Wakana’s or Kaori’s address based on how regular convenient coincidences have become in my life, but am sorely disappointed when I see that it’s not."
    "In fact, it’s an address I don’t recognize at all. And after plugging it into my phone, I realize it’s on the outskirts of the old district, not far from the bar we went to the other day."
    "That’s...good for her, I guess. She can kill time getting drunk and stumbling home while I am forced to kill time by walking all over town."
    "And occasionally fucking a teenager or two."
    "But unless Imani is keeping one as a prisoner, I can’t imagine anything like that is going to happen tonight..."
    "........."
    "......"
    play sound "doorbell.mp3"
    "..."

    ima "Yo! Is that you, Senpai? Or is that an assassin sent by the government to eliminate me?"
    s "Both."
    ima "Shit, what a twist."
    ima "Come on in. Door’s unlocked."

    play sound "dooropen.mp3"
    scene imaniapt1
    with dissolve2

    "I make my way into Imani’s apartment, which feels more like a large closet than an actual living space."
    "It’s situated in a two story building with about twenty other rooms and is clearly meant to be some sort of affordable housing unit."
    "But I guess it’s better to have something like this than it is to be sleeping on the streets or...in the changing room of a spa."

    ima "Heya. Congrats on being my first ever visitor. I’d say we should christen the place, but I’m afraid I’d find out I’m a 6/10 lay as well."
    s "You’re still not over that?"
    ima "How would {i}you{/i} feel if somebody gave you a 6/10 when it comes to kissing?"
    s "I think I’d be more curious about their prior experience and grading scale than whatever my score is."
    ima "Fair enough. Pull up a seat, I guess. Not like there are many of them in here, though."

    scene imaniapt2
    with fade

    s "I think my bedroom is larger than your apartment."
    ima "Did you come here to brag?"
    s "No. But I’m pretty sure that it’s something that’s going to just naturally happen at several points tonight."
    ima "I know it’s small, but I don’t mind. All that really matters is just having a place to sleep and work and, as you can see, both of those things are entirely possible within these walls."
    s "Where’s your cat?"
    ima "Cat?"
    s "And your parrot?"
    ima "Parrot?"
    s "Didn’t you-"

    scene imaniapt3
    with dissolve

    ima "Did I mention having either of those things?"
    s "Unless I’m going insane, I’m pretty sure you did."
    ima "I was probably just fucking with you. I don’t have any pets. "
    ima "Well, except for the cockroach who keeps trying to get into bed with me at night. But I think he’s just got the wrong idea about the two of us."
    s "Why would you lie about owning a cat? Who does that?"
    ima "Me, I guess. I probably thought it was funny. Just do yourself a favor and never believe anything I say unless it makes me look cooler."
    s "I think a parrot would make you look a little cooler."

    scene imaniapt4
    with dissolve

    ima "Hey, if I start saving up for one now, I might finally be able to afford one by the time I retire. "
    s "It’ll be before that. Just think of how much money you’re saving by living here."
    ima "Lay off the slander and sit down. It’s starting to feel like you’re only here to observe me and not to actually chill."

    scene imaniapt5
    with fade

    s "You’re not going to make me help you grade things, are you? Because Wakana has tried to do that before and I still get a little nervous every time I go to see her now."
    ima "Sure you’re not getting nervous because you want to bang her?"
    s "That’s not really something I’d ever get nervous about. "
    ima "Look at me, my name is Sensei. I’m confident and sexually active. I don’t feel {i}feelings{/i} the way “normal” humans do."
    s "Look at me, I’m Imani. I’m a huge fucking bitch."

    scene imaniapt6
    with dissolve

    ima "You offend me. I’m a medium-sized bitch at most."
    ima "But no, I’m not going to make you help me grade anything because I am awesome and have already finished."
    ima "I also know {i}much{/i} more about what everyone in the class is actually into now."

    scene imaniapt7
    with dissolve

    ima "For example, did you know that the role of women in Yasu’s religion is to basically just lie there and let a dude spray his baby batter inside of her?"
    s "I did. And, just for the record, these assignments of yours aren’t things that need to be filed away or...scanned in, are they? "
    s "Because that and the ones written about me aren’t things I want anyone other than you getting their hands on."
    ima "Aww, are we close enough now that you don’t mind {i}me{/i} knowing how creepy you are?"
    s "Like you’ve said before, we make a good team. And I think a lot of that is due to how easy it is for me to talk to you without feeling like I’m being judged."
    ima "Oh, I judge you all the time. I’ve just also judged everyone else and have somehow, after several loops and twists, reached the conclusion that you're not out to hurt anybody."
    ima "Except me, that is. I’m pretty sure being mean to me gets you hard. But, in order to keep this professional, I promise to not bring up your penis again for the rest of the night."
    s "Thanks, Imani. I understand how difficult that must be for you since I figured you're almost always fantasizing about it."
    ima "Not always. Just whenever you leave the room. Gotta keep my guard up when you’re around, you know? Don’t wanna get pregnant and feel the wrathful gazes of nineteen jealous teens. "
    s "Anyway, if you’re not grading anything right now, what are the notebooks for?"

    scene imaniapt8
    with dissolve

    ima "These? A little independent studying."
    s "What’s the point of studying if you’re already a teacher?"
    ima "{i}Student{/i} teacher, technically. I’ve gotta put in a certain amount of work before I’m able to become a full-on teacher. They {i}should{/i} be counting what I do for you as overtime, though."
    s "Yeah, I feel like I’ve all but taken the backseat at this point."
    ima "Works for me. I get to do what I like to do and you get to do what {i}you{/i} like to do."
    ima "Just maybe toss in a platonic massage every once in a while to keep me loose and ready to go."
    s "Sure. How does right now sound?"
    ima "Bad. I’m not done studying yet and we both know that any sort of massage in a room as small as this would end with one of us on top of the other."
    s "Oh no. Whatever would we do in a situation like that?"
    ima "Back on track, Senpai. I will not allow you to seduce me while I’m already being ruthlessly penetrated by the intangible dick that is academia. And two dicks at once? Noooo thank you!"
    s "Must be some pretty intense studying if there’s an intangible penis inside of you right now."
    ima "It’s gotta be if I’m ever going to teach in college. Don’t want some punk who’s only a little younger than me getting snippy and acting like he knows more than I do."
    ima "Of course I say that now, still years away from any job like that...but still."
    s "You want to be a college professor?"

    scene imaniapt9
    with dissolve

    ima "Mhm. Mainly for transfer students, I think. People who don’t natively speak Japanese and stuff like that."
    s "What do they speak in Ghana?"
    ima "English."
    s "Really?"
    ima "What did you expect? German?"
    s "I’m not sure. I’ve just heard there were a bunch of languages in Africa and figured it would be something I hadn’t heard of before."
    ima "English is the official language, but I can speak Twi as well."
    ima "Which means there are three languages I’m fluent in. Which is nothing compared to the, like...ten that Touka’s mom can speak, but hey. Still pretty impressive."
    s "Can you say something in Twi?"
    ima "Medɔ wo."
    s "What does that mean?"
    ima "It means learn the fucking language, Senpai."
    s "Is Twi a naturally rude dialect or are you just an asshole?"
    ima "I’m just an asshole. But I’m {i}your{/i} asshole, Senpai. At least until someone else is willing to hire me."
    s "So if you were offered a college job, you’d leave right now?"
    ima "Of course. "
    s "Wow."
    ima "What? You think I’d throw away my dreams just because I met you? Come on, you know me better than that. "
    s "You could have let me down a little softer, at least."

    scene imaniapt10
    with dissolve

    ima "I’d keep in touch, obviously. It’s not like I’d just erase you from my mind the second I’m not your underling anymore."
    ima "This is probably going to sound really depressing since this is the first time you’re coming over and we’ve only known each other for a little while, but..."
    ima "You’re kind of my best friend. "
    s "Really? Me? Not Wakana? "
    ima "I like Wakana a lot. "
    ima "I just like you more."

    scene imaniapt11
    with dissolve

    ima "Plus, I get to see you for almost seven hours, five days out of every week."
    ima "And you’re easier to talk to. {i}And{/i} you wouldn’t abandon me at a table to go bang your girlfriend in the bathroom. Probably."
    s "Not going to lie, I probably would. "
    ima "Okay, sure. But you’d probably invite me as well and it’s the thought that counts."

    scene imaniapt12
    with dissolve

    ima "Point is, it would take a lot more than just losing a best friend for me to start rethinking my future. Even if we were like, lovers or something...I’d still probably choose myself over you if it came down to it."
    ima "This is a goal I’ve had for myself since I was a kid, you know. It’s not something that’ll be so easily shaken."
    s "What made you want to become a teacher?"

    scene imaniapt13
    with dissolve

    ima "Honestly...the money. "
    s "Rough. "
    ima "Yuuuuup. Mini-Imani figured that teachers, as important as they are, were paid handsomely and able to live on their own without any financial problems at all."
    ima "Boy, do I wish I could travel back and time slap that little girl upside the head."
    ima "Would’ve tried becoming a doctor or something if I knew I’d be living in a box at my age."
    s "It’s interesting that money’s what led you down this path in the first place. I feel like most people become teachers to, like...help children or something."

    scene imaniapt14
    with dissolve

    ima "I don’t even like kids. They’re loud...obnoxious...and always {i}sticky{/i} for some reason. "
    ima "Teenagers are fine because the stickiness kind of wears off after a while. But they’re still not {i}ideal{/i} as looking at them reminds me that I’m getting older and getting older fucking suuuuucks."
    ima "Plus, being the youngest of seven, I never really had many chances to play with or talk to anybody {i}younger{/i} than me. So I'm just not used to it."
    s "I’m sorry, {i}seven?{/i}"

    scene imaniapt5
    with dissolve

    ima "Three brothers, three sisters. All older. All in Ghana."
    s "Why aren’t any of them here with you?"
    ima "They can’t be."
    s "What do you mean they {i}can’t{/i} be?"
    ima "I mean I’m the only one with Japanese blood."
    s "You-"

    scene imaniapt15
    with dissolve

    ima "They’re all technically {i}half-{/i}siblings. "
    ima "I have a different biological father. But my {i}actual{/i} father was a good man and insisted I was just as much {i}his{/i} child as the rest of them- even knowing where I really came from. "
    ima "So I got to grow up in a house with a bunch of people I was only {i}half-{/i}related to, still feeling like a bit of an outcast even though I was welcome there."
    ima "Having seven kids is hard to afford, though...so we scraped by, but never had {i}much{/i} money."
    ima "I don’t know. I thought that maybe striking it rich one day would help me {i}buy{/i} my rightful place in the family. But somewhere along the way, I started actually liking the idea of teaching."
    ima "No one else in my family has ever made it to college, so the fact that I have is just-"

    scene imaniapt16
    with dissolve

    ima "Oh, crap. I’m like, hardcore unloading on you right now, aren’t I? "
    s "It’s fine. I had no idea about literally...any of that."
    ima "The condensed version is that I’m always going to feel out of place and that I want to prove to both my family and myself that I belong. The end. Imani backstory complete."
    s "I’m sure there’s a lot more to you than just that, Imani."

    scene imaniapt17
    with dissolve

    ima "Of course there is. But there’s no reason I should be unpacking my entire childhood right now when I’ve yet to even unpack my boxes."
    ima "You’ll learn more as time goes by...naturally. Without it coming in the form of some spontaneous info-dump only partially relating to a question you asked. "
    ima "There are over seven billion people on this planet and somehow, we were lucky enough to wind up with each other."
    ima "That should be enough for now."

    scene imaniapt18
    with dissolve

    ima "Let’s just enjoy the fact that we-"
    s "You know you’re blushing, right?"

    scene imaniapt19
    with dissolve

    ima "I’m what? No, I-"
    ima "Shit."
    ima "You’re right."

    scene imaniapt20
    with dissolve

    ima "Mind looking away for a minute or two while I repeatedly remind myself that we’re just friends and that anything more than that could jeopardize the first real relationship I’ve ever had in this country?"
    s "I think you might be unloading again."
    ima "You know, I knew this was gonna happen too. I’m going over to your place next time."
    s "You think you’ll be any safer there?"
    ima "Than in an oversized shoebox where our knees have been touching this entire time? Probably."
    s "Didn’t realize your knees were your weak spot."
    ima "Probs because I figured it was something you didn’t {i}kneed{/i} to know."

    scene black
    with dissolve2

    s "Okay, I’m leaving."
    ima "Hey, you don’t have to {i}completely{/i} bail! I just want my face to go back to its normal, beautiful color! The color that {i}doesn’t{/i} make it look like I want to bang my boss!"

    "Imani settles down and prevents me from leaving. "
    "Thankfully (For her, at least. I still don’t really care), she figures out how to restrain herself from exposing any additional info and the rest of the night passes by filled with our typical, mindless banter."
    "I learned a lot about her tonight- intentional or not...but there’s still plenty I don’t understand yet."
    "And I can’t help but wonder if I'll be able to fill in the blanks before she inevitably leaves me."

    $ renpy.end_replay()
    $ imanidate1 = True
    $ imani_love += 1
    stop music fadeout 6.0

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label imanidate5:
...
```

## Code that triggers this event

File: (install folder)\game\ImaniEvents.rpy

Code:
```python
...
label callimaninight:
    if imani_love > 0 and wakanaspecial15 == True and imanidate1 == False:
        jump imanidate1
...
```