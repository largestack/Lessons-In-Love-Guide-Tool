# Breaking Character (Otoha)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Otoha love greater than or equal to 20

* Event [White People](./otohaspecial15p2.md) (Otoha) is completed)



## Next events

None

## Event properties

* Id: otohadate20
* Group: Otoha
* Triggered by label: cafe
* Triggered by branch label: cafe
* Triggered by path: cafe->otohadate20

## Official wiki page

[Breaking Character](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohadate20&go=Go) for more details.

## Event code

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
label otohadate20:
    scene otohadarkness1
    with fade
    play music "brighterdays.mp3"

    "In my efforts to head over to the cafe for another randomized beverage, I encounter a familiar face at the counter — one not presently obscured by a new, alternative haircut that would be subsequently discarded."
    "That person’s name is Otoha Okakura and she is hiding something from me."
    "But at least she’s smiling today and not hitting anyone. "
    "One step at a time."

    s "Hello. One order of lesbians, please."

    scene otohadarkness2
    with dissolve

    r "Hot and with cream?"
    s "Y-"
    o "Don’t even think about answering that question."
    s "Just black, please."

    scene otohadarkness3
    with dissolve

    r "I’ll keep an eye out for you."
    o "Here to hit on my girlfriend again?"
    s "Or you. Are you having trouble holding that guitar with your fragile girl muscles? Would you like a big, strong man like myself to take over?"

    scene otohadarkness4
    with dissolve

    o "I think my fragile girl muscles can take it. You can pay for my drink though if you want me to ignore your blatant sexism."
    s "You never bought anything for all of those Europeans. "
    o "There were too many of them and I didn’t have any cash on me. Now, fork it over. You owe me."
    s "For {i}what?{/i} You’ve done literally nothing for me."
    o "No, but Rin probably has. Which means that {i}I{/i} kind of have by extension since we’re a package deal now."
    r "Just without the package."
    s "That-"
    r "Because we’re girls."
    s "That is-"
    r "Girls don’t have dicks."
    s "Yes. Thank you, Rin. That is not how that works, Otoha."
    o "Yeah, you’re right. I just feel bad getting free stuff all the time and thought it would be nice if I stopped inadvertently draining Haruka’s bank account."
    s "Please don’t solicit me for items you would otherwise receive for free. Thanks."

    scene otohadarkness5
    with dissolve

    r "Speaking of Haruka, I’ve been talking to her more about setting up that open mic thing we discussed if you’re still interested."
    r "I figure something like that might be good for the band too whenever we, like...actually have music."
    r "But you could always do your solo stuff. My mom wants to play too now that I’m no longer capable of hiding this place."
    s "Rika plays guitar?"

    scene otohadarkness6
    with dissolve

    o "Dude, Rin’s mom can play {i}everything.{/i} She’s like a grown up Noriko with boobs and additional talent in place of all the rebellious little sister energy."
    r "She’s okay. I’ve heard better."
    s "Be nice to your mom, Rin."

    scene otohadarkness7
    with dissolve

    r "Shut up, Dad! If you need me, I’ll be in my room!"
    s "I take it she’s still hanging around the dorm then?"
    o "That...would be an understatement. Rin and I barely ever get to be alone in her room anymore so we’ve had to chill in mine. "
    s "That doesn’t sound so bad."
    o "Yeah, until you remember that my roommate wants to have sex with anything that moves. Including but not limited to both Rin {i}and{/i} me."
    s "I...can come keep her busy?"

    scene otohadarkness8
    with dissolve

    o "I think we’re good. Right, R- why did I even ask?"
    r "It’s probably best if I don’t say anything right now. I might squeak. "
    o "Keep it in your pants, okay? You’re at work."
    s "So, what? You’re just hanging out here instead of the park today? Aren’t you missing out on...money or exposure or whatever it is you’re normally shooting for over there?"

    scene otohadarkness9
    with dissolve

    o "I’ve got lessons today. In fact, I should probably start heading over to them now. I just wanted to drop by and see how Rin was doing first."
    o "You two can have fun without me, though. I’ll be-"
    s "Nah, I’ll come with you."
    o "Nah, you won’t."
    s "No, I will."
    o "Mmmm...no thanks. I’m good."
    s "I insist."
    o "Wow, you really just don’t know how to take no for an answer, do you?"
    s "If you start crying, I can probably hold myself back."
    o "Oh, okay. That’s not a creepy thing to just slip in there out of the blue. Cool."
    r "Want something for the walk over, Sensei? Latte? Cappuccino? Copyrighted frozen beverage?"
    s "Just mix a bunch of random syrups into one cup and give me that. That is what I want."
    r "One black coffee, coming right up."

    scene otohadarkness10
    with dissolve

    o "Interesting order."
    s "I think I discovered just now that the only way to get what I want at this store is to ask for the exact opposite. This is a major breakthrough and you should be happy for me."
    o "Are you really coming to my lessons again?"
    s "Yeah. I want to bang your teacher when you guys are done."
    o "Thank you for sharing that absolutely vital information with me. I don’t know what I would have done if I had to leave practice {i}without{/i} knowing you two were about to have sex on the couch I eat lunch on."
    s "Just trying to be the best friend I can, Otoha. You know I’d {i}never{/i} hide anything from {i}you{/i}, right?"

    scene otohadarkness11
    with dissolve

    o "Hahah...hah..."
    o "Time to go."

    scene otohadarkness12
    with dissolve

    r "Ah, wait! Otoha! Are you still coming over later? Futaba’s parents sent her a Ouija board and I want to communicate with the ghost of the fifth floor."
    s "The what?"
    o "Yeah! I’ll be there. Is it still cool if Nodoka tags along?"
    s "What ghost of the fifth floor?"
    r "Cool! See you later, then! Have fun at practice!"

    scene black
    with dissolve2

    s "Stop introducing new subplots. There are already too many."
    r "Sensei! Your coffee. Here."
    r "Take care of my woman, you hear me?"
    r "Just not in a sexual way because I would cry and I’m on a solid no-crying streak right now."

    "I take the cup from Rin and have to break into a mild jog to catch up with Otoha who, of course, is attempting to lose me."
    "Despite my desire to have sex with her teacher, though...there {i}is{/i} also the desire to find out more about what’s going on in that prodigal head of hers."
    "If she’s working herself to the bone...and coming within inches of asking {i}me{/i} for advice when she has plenty of other people to fall back on..."
    "I assume that things are either very bad or..."
    "Or I’m the only person who would be able to help her for some reason?..."
    "........."
    "......"
    "..."

    scene otohadarkness13
    with dissolve2

    "We make it to the sketchy basement to find that Niki is not yet here."
    "And while this does delay the amount of time before my penis will be inside of her, it gives me a solid opportunity to relate to Otoha instead."

    s "You know, I was a teenager once too."

    scene otohadarkness14
    with dissolve

    o "Woooooooow. You don’t say."

    "I have successfully related to Otoha. "
    "I will now press her for secrets."

    s "What did you try to tell me at the cafe the other day?"
    o "Stop having sex with people half your age."
    s "The other thing."
    o "You’re a bad influence."
    s "Keep going. You’ll get there eventually."
    o "Rin has nice boobs."
    s "Not what I was aiming for but we can stick with that topic. That sounds good."
    o "Don’t take this the wrong way, but I think it would be best for both of us if we didn’t use our time alone in this sketchy basement to talk about boobs."
    s "And you say {i}I’m{/i} the lame one."

    scene otohadarkness15
    with dissolve

    o "It’s weird Niki’s not here yet. She’s never late."
    s "She probably got called into work or something. I’ll give you your lessons today. Open your mouth."

    scene otohadarkness16
    with dissolve

    o "Please never tell me to open my mouth again."
    s "I can’t teach those who are unwilling to learn."
    o "I’m going to sit on the couch and wait for my actual teacher now. Not the guy she’s boning."
    s "I will join you on that couch because it will bring us closer together."
    o "On second thought, maybe I’ll stand."
    s "Me too. Standing sounds better."
    o "..."
    s "..."

    scene otohadarkness17
    with dissolve

    o "Ugh...I hate it when you come here."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadarkness18
    with dissolve2

    "An awkward [[yet expected] silence fills the room as both of us struggle to think up any conversation topics and are probably still thinking about Rin’s boobs."
    "What I want to do is probe Otoha more about whatever this thing she needs help with is but, unfortunately, it’s starting to seem like time will be the only thing to squeeze that out of her."
    "That’s fine, though. I doubt whatever it is is eating her alive and she seems way better today than she did the last time I saw her."
    "In fact, the only notable change at all is the reduced amount of red highlights in her hair. "
    "Why she didn’t remove them all, I don’t know. Because to me, it feels like she’s just caught in the middle of a transition like this-"
    "Like she got halfway through changing up her look and hesitated. "
    "I’m probably overthinking it. That happens sometimes. "
    "I just hope that, whenever the rest of her hypothetical transition ensues, it’s painless."
    "It would be a real shame if she had to take {i}more{/i} out on someone just trying to help."

    s "Otoha."
    o "Don’t do it."
    s "I was wondering-"
    o "I’m telling you, Sensei. Don’t do it. "
    s "What was that thing you-"

    scene otohadarkness19
    with dissolve

    o "Listen, man. I should have never said anything in the first place. I was sleep deprived when I said I needed your help and..."
    o "I thought more about it and you’re definitely the {i}last{/i} person who’d be able to help me. Talking to you would only make things worse."
    s "So things are bad?"

    scene otohadarkness20
    with dissolve

    o "..."
    o "Yeah."
    s "Do you think they’re going to get better on their own?"
    o "I don’t know..."
    o "I just wish people would let me breathe sometimes."
    o "I feel like my entire life right now is as Otoha of “Otoha & Rin.” And that’s {i}fine.{/i} Rin’s a great girl. Really great. I just want to feel more like...an individual sometimes. Not half of something bigger."
    s "That does sound kind of suffocating. I have no idea how you want me to help you, though."
    o "That’s not what I needed help with. It’s just kind of...how things got started, I guess."
    o "But ever since they {i}did{/i}, I-"

    stop music
    play sound "imscared.mp3"
    scene otohadarkness21
    with hpunch

    o "KYAH!"
    s "..."
    o "..."
    s "Kyah?"

    scene otohadarkness22
    with dissolve

    o "Leave me alone! That was super loud! I’m allowed to get scared!"
    s "Sounded like something might have exploded."
    o "Like...are we under attack? Is this space war stuff? Are we finally going to die?"
    s "Probably just one of those transformer things outside. I’m sure the power will come back on as soon as it’s repaired."
    s "On the bright side, pun not intended, we’ve still got Niki’s collection of tacky neon anime sign things. "

    scene otohadarkness23
    with dissolve

    o "I can barely see anything, though. "
    o "Can’t you, like...be a man and go fix it yourself or something?"
    s "Way to perpetuate gender roles by assuming I just know how to fix electrical stuff, Otoha. I have no idea how to do something like that."
    o "I don’t like the dark...it creeps me out."
    s "Yeah. I can tell on account of you willingly touching me. That has never happened before."
    s "It’s also incredibly out of character and very adorable. Which is why I am enjoying this thoroughly right now."

    scene otohadarkness24
    with dissolve

    o "Well, congratulations on taking pleasure in my suffering! I really appreciate that!"
    s "Any time. And if you’d like to come closer, I will welcome you with open arms."
    o "Can’t you just go and take a look at the breaker thingy? There’s one on the other side of the room. "

    scene otohadarkness25
    with dissolve

    s "Where it’s even darker than it is over here? And with zero knowledge of what I’d even have to look {i}for?{/i} This isn’t a good plan."
    o "Do you have a better one?"
    s "Yeah. We sit here and wait for the power to come back on."
    o "What if it doesn’t?"
    s "Then this is where we die."

    scene otohadarkness26
    with dissolve

    o "I don’t want to die with you! I don’t even like you that much!"
    s "Wow, okay. Why don’t you let go, then?"
    o "Because if I let go, you’ll disappear and I’ll be all alone and I will cry and scream and it will suck! Go try and do electrical stuff. If you die, at least it will be as a hero."
    s "And what are you going to do while I cross the abyss that is this basement, Otoha? Aren’t you afraid I’ll disappear?"
    o "Not if...I come with you? I can just hold your sleeve like this. That works, right?"
    s "That is a horrible idea."
    o "Why?"
    s "Because the only way that scenario could end would be with one of us tripping and then the other one falling on top in what would become a cliche anime-style almost-kiss moment. "
    s "Then, to complicate things even further, the power would come back on as soon as that happens and Niki would walk in to find us still laying on the ground together."
    o "That is ridiculous. There’s no way that will happen."
    s "Otoha, I am positive that will happen. I have protagonist powers."
    o "No, you’re just a selfish wannabe loner who bangs teenagers. "
    s "Teenagers who like me for no discernible reason. Even you’re cozying up right now and we were at odds just a short while ago."
    o "I’m not “cozying up!” I’m scared! Go make the lights come back!"
    s "Okay. But I am telling you that there is literally only one way this scenario can possibly end."
    o "Whatever! Just go!"

    scene black
    with dissolve2

    s "Okay. But don’t say I didn’t-"
    o "Ahh!"

    play sound "tackle.mp3"
    scene otohadarkness27
    with hpunch

    o "Ngh..."
    s "See? Not even two seconds. I told you this would happen."

    scene otohadarkness28
    with dissolve

    o "My legs weren’t working! If I had known that before trying to get up, I would have just made you carry me!"
    s "How are you {i}that{/i} scared of the dark? You’re in high school. Grow up."

    scene otohadarkness29
    with dissolve

    o "At least if I grew up, you wouldn’t be attracted to me anymore!"
    s "Don’t argue, Otoha. It will lead to us making out. "
    o "No it won’t! Just because you got lucky with guessing {i}one{/i} thing doesn’t mean another is going to happen when-"

    play sound "imscared.mp3"
    scene otohadarkness30 with hpunch

    o "KYAH! WE REALLY ARE UNDER ATTACK!"
    s "Make that two things."
    ni "Otoha..."

    scene otohadarkness31
    with dissolve

    o "How is that even possible?! We would have heard you coming down the stairs!"
    ni "Would you like to explain to me why you’re on the floor with my ex-or-maybe-not-ex-boyfriend? And then, would you like to explain to me why it looks like you’re trying to take his pants off?"

    scene otohadarkness32
    with dissolve

    o "Okay, the falling part is one thing, but there’s no way this coincidence would get even worse than-"
    o "..."
    ni "I’m waiting..."

    scene otohadarkness33
    with dissolve

    o "Just kill me..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadarkness34
    with dissolve2
    play music "brighterdays.mp3"

    ni "So...let me get this straight."
    ni "The power went out...and you’re a fucking pussy...so you made a dude with no technical know-how waltz across a dark room to play with an electrical panel...and then you fell on him because, again, pussy."
    o "..."
    ni "..."
    o "Yes."
    ni "Otoha-"

    scene otohadarkness35
    with dissolve

    o "I...I know how it must look! And I...know that recent events may have also led you to believe that is the type of person I am! But this was totally different from that! This was an accident!"

    scene otohadarkness36
    with dissolve

    s "Recent events?"
    o "Nothing! Go wait outside!"
    s "Niki?"
    ni "No clue. I’ve already purged whatever Otoha is referring to from my memory. You’ll have to hear it from her."
    s "Otoha?"
    o "I..."
    o "Uhh..."

    scene otohadarkness37
    with dissolve

    o "Practice time?..."
    ni "..."
    o "..."
    ni "..."

    scene otohadarkness38
    with dissolve

    ni "Bad girl."
    o "Niki, wait! It really wasn’t like that!"
    ni "You keep your hands off of my man. Got it? You are here to {i}learn,{/i} not fornicate."
    ni "I know firsthand how hard it is to keep hormones in check at your age, which is why I am being so lenient with you. "
    ni "But if you touch him again, I will cut your fingers off. Rings and all."

    scene otohadarkness39
    with dissolve

    s "Not the rings. That’s where she gets her powers."
    ni "Akira..."

    scene otohadarkness40
    with dissolve

    o "Akira?..."
    s "Hah...great. Now Otoha has {i}another{/i} secret of mine while I still don’t have any of hers. Thanks, Niki."
    o "Your name is Akira?"
    ni "Why are you keeping your name a secret from your students?"
    o "Yeah, why are you keeping your name a secret from your students?"
    o "I'm not the only one who knows, am I?"
    s "That...is a good question. Let me get back to you on it."
    o "Your name..."
    o "Is kind of cool."

    scene otohadarkness41
    with dissolve

    s "You’re only saying that because you want to get in my pants."
    o "Aaaaand you ruined it."
    ni "Otoha. Practice is cancelled today. "

    scene otohadarkness42
    with dissolve

    o "What? Why? "
    ni "Because I have a sudden urge to remind your teacher that there is only one female in his life that he should be putting his hands on and that female is me."
    ni "Now scram or you will see something you may never forget."
    o "Niki-"

    scene otohadarkness43
    with dissolve

    ni "Mm~"
    o "Wha- seriously?! I’m still in the room!"
    s "Mm...Niki...I don’t..."

    scene otohadarkness44
    with dissolve

    ni "Mnch...shut the fuck up and kiss me..."
    o "..."
    s "But..."

    scene otohadarkness45
    with dissolve
    play sound "dooropen.mp3"

    ni "Mngh.....hmnn......mm~"
    s "..."

    "Welp, now that Otoha’s gone, I see no reason to not keep doing this."

    scene otohadarkness46
    with dissolve

    ni "Mnh! Mm...Akira......mmnh!"

    scene black
    with dissolve2
    play sound "zipper.mp3"

    ni "Lay down on the couch..."
    "........."
    "......"
    "..."

    scene otohadarkness47
    with dissolve
    play sound "phonebeep.wav"

    r "{i}Hello? Otoha? Is everything okay? I thought you’d be practicing right now.{/i}"
    o "Yeaaaaaah...about that. Practice is cancelled today and I suddenly don’t have anything to do."
    r "{i}What? What about Sensei? Weren’t you with him?{/i}"

    scene otohadarkness48
    with dissolve

    o "He is...currently having sex with my teacher."
    r "{i}Oh..."
    r "{i}Yeah, I guess that tracks."
    r "{i}What are you gonna do, then? Go home? Come back to the cafe? I can go on break early if you want."

    scene otohadarkness49
    with dissolve

    o "No, it’s fine. Don’t worry about it. I’ll just go home and take a nap or something."
    r "Okay! I’ll get back to work then. Text me if you get bored or whatever."
    o "I will."
    o "And...Rin?"
    r "Yeah? What’s up?"
    o "..."
    r "Otoha?"

    scene otohadarkness50
    with dissolve2

    o "I love you."

    scene black
    with dissolve2
    stop music fadeout 10.0

    $ renpy.end_replay()
    $ otohadate20 = True
    $ otoha_love += 1
    $ niki_lust += 1

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "{i}Niki’s lust has increased to [niki_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
    if rin_love >= 20 and ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False:
        jump cafe20
    if rin_love >= 15 and cafe15 == True and day63 == False:
        jump rincafegone
    if rin_love >= 25 and rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False:
        jump cafe25
    if rin_love >= 30 and beachvacation16 == True and cafe30 == False:
        jump cafe30
    if rin_love >= 35 and rindorm35 == True and rininvite == True and cafe35 == False:
        jump cafe35
    if rin_love >= 40 and christmas7 == True and cafe40 == False:
        jump cafe40
    if rin_love >= 45 and rindorm40 == True and cafe45 == False:
        jump cafe45
    if rin_love >= 50 and secondbeach18 == True and cafe50 == False:
        jump cafe50
    if otoha_love >= 20 and otohaspecial15p2 == True and otohadate20 == False:
        jump otohadate20
...
```