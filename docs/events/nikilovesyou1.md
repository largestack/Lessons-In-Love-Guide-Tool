# What it Takes to Move Forward (Niki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Niki love greater than or equal to 20

* Event [A Thousand Years](./slumberreset5.md) (Main) is completed)

* Day of week is Saturday

* Event [How To Make Love Stay](./nikilovesyou3.md) (Niki) must not be completed)

* nikinumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: nikilovesyou1
* Group: Niki
* Triggered by label: callnikimorning
* Triggered by branch label: callmorning
* Triggered by path: callmorning->callnikimorning->nikilovesyou1

## Official wiki page

[What it Takes to Move Forward](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikilovesyou1&go=Go) for more details.

## Event code

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikilovesyou1:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "And given that mornings are really the only time I can reliably see her, I’m looking forward to a rather peaceful and jovial conversation."

    play sound "phonebeep.wav"

    ni "Die."

    "My hopes are shattered and my day is ruined."

    s "What did I do to deserve this?"
    ni "Uhh, well, to {i}start-{/i} you completely fucking ditched me on Christmas. Does that ring any bells?"
    s "No, but it does {i}jingle{/i} some."
    ni "I’m hanging up now."
    s "Wait, stop. I want to see you."
    ni "Ooooh, okay! Yeah! Because I’m yours to just leave on hold until you’re done wandering around with everyone else! Sounds great! See you in ten?"
    s "Niki, come on."

    play music "starvingtodeathoutofreachofthesun.mp3"

    ni "Who turns down a date with a superstar?! You know damn well how big of a deal I am now! I had a blue check mark before they were uncool and easily obtainable!"
    s "And I’m very proud of you for that even if I don’t know what it means. "
    ni "I thought we were going to spend that day together!"
    ni "And sure you may have technically never...{i}said{/i} that, but you sure as hell didn’t stop me when I spent a month and half talking about it and planning things out!"
    ni "If you knew you weren’t going to come, why did you let me get my hopes up?! I canceled my Christmas concert for you!"
    s "Your concert wasn’t canceled, though. I watched it on TV with the girls."
    ni "I {i}un-{/i}canceled it when Noriko told me about your stupid fucking party. So unless you’re calling me to apologize for that, I don’t want to hear it."
    ni "Also, I know damn well that you “watching it” means it was probably just on in the background while you were being a fucking tool or something."
    s "That’s true, but everyone else really seemed to like it."
    ni "{i}Hah...{/i}Goodbye, [nikitemp]. I have things to-"
    s "I would have gone with you if I had the choice."
    ni "..."
    s "..."

    "There’s a silence on the other end of the phone as Niki attempts to figure out what that means. "
    "But I’m sure she’s not going to immediately jump to the possibility that there was a two-month gap in time, so I know I’m going to have to explain myself."
    "Which, apart from feeling like the choice was made for me, is probably the reason I called her in the first place."
    "Maybe, buried somewhere in the back of my mind, I was {i}also{/i} looking forward to spending Christmas with her."

    ni "..."
    s "..."

    "Or maybe that’s just me rationalizing why something else I’ve done has led to someone getting hurt again."
    "Even if this wasn’t entirely my fault."

    ni "What does that mean...“if I had the choice?”"
    ni "Are you not an adult? Can you not make your own decisions?"
    s "Something...happened. Something complicated. "
    s "But I’ll make it up to you. We can go on a date today. An {i}actual{/i} date, not another...sausage-focused breakfast trip."
    ni "I can’t {i}go{/i} on actual dates. I’m an idol, remember? I’d be crucified if anyone saw us."
    s "But we’ve been to that restaurant-"
    ni "We’ve been to “that restaurant” because I rented the entire place out. And, despite how it may seem, I’m not always 100%% willing to go to the moon and back for you."
    s "Then...you can come here. Or I can come there. I don’t know."
    s "But I want to see you."
    ni "..."
    s "..."
    ni "I look like shit, just FYI. I haven’t been sleeping well."
    s "Why not?"
    ni "Because loving someone without being loved back is a lot harder than you think. "
    s "Niki-"

    play sound "phonebeep.wav"

    ni "This address. Be there in one hour. If you’re not, I’m deleting your number from my phone and then throwing it into the ocean."
    s "There’s no need to delete my number if you’re just going to throw your phone into the-"

    play sound "phonebeep.wav"

    s "...and, she’s gone."

    scene black
    with dissolve2

    "I really would have gone with her if I had the chance."
    "It was difficult to say in the moment since there were two other girls there beckoning the same exact gesture out of me, but..."
    "Niki was there first."
    "Not just that day, but in general."
    "She’s been there from the start and even if there are parts of me that don’t {i}specifically{/i} remember what makes our relationship so different- I know it is."
    "And I know that there must be a future out there where I do more than just disappoint her every waking hour of every day."

    s "..."

    "I’m just not sure if {i}this{/i} is that future."
    "But there are several things in life that I’ve accepted I will never understand-"
    "One of them is what it takes to move forward."
    "Another is what happens when I get there."

    "........."
    "......"
    "..."

    scene nikitired1
    with dissolve2

    s "A playground?"
    ni "I {i}want{/i} to say I picked a place where you wouldn’t hit on anyone else but, honestly, who the fuck even knows at this point?"
    s "Just...going to ignore that. You look-"
    ni "Horrible? Exhausted? I am. Thanks for noticing. And thanks for drawing attention to it."
    s "You’re not going to make today easy for me, are you?"
    ni "I’ll become nicer as the day goes by. You’ve already managed to earn yourself a few points by not making me wait. "
    s "I did it for your phone. As someone paying for several concurrently, I understand how expensive replacing them can be."
    ni "How very generous of you. "
    s "I’m sorry about Christmas, Niki."

    scene nikitired2
    with dissolve

    ni "Same. That’s two Christmases in a row where I would have let you fuck me only to find out you’d rather mingle with a bunch of teenagers instead. Hope they liked the show."
    s "If it’s any consolation, there are very few things in life that I would rather do than fuck you."
    ni "Join the club. "
    ni "Like, really. There’s an actual club for that. “Let me fuck Niki Nakayama” on Facebook or something. Depressing amount of members. And here {i}you{/i} are, squandering the opportunity."
    s "If you really do know me as well as you say, that shouldn’t come as much of a surprise. You and Noriko have both made it sound like I’ve been kind of an asshole for...basically forever."

    scene nikitired3
    with dissolve

    ni "You have. But that doesn’t mean it isn’t still a fucking pain in the ass."
    ni "Do you really think I’d keep giving you chances if I didn’t at least {i}kind of{/i} understand what it is that makes you tick? Fuck no. Not in a billion years."

    scene nikitired4
    with dissolve

    ni "But you’ve gotta give me a fucking {i}break,{/i} {b}[[REDACTED ~ NOT YET READY]{/b}. "
    ni "Loving you as much as I do is {i}hard.{/i} And it’s like every single step you take is in the wrong direction, and that makes {i}me{/i} have to turn around all the time just so you don’t get lost."
    ni "You’ve gotta give me {i}something.{/i} A {i}single{/i} step toward the future. I’m doing all I can here."
    ni "It’s not even about me. I’m worried about {i}you.{/i} "
    ni "Ever since {b}[[REDACTED ~ MORE UNNECESSARY INFORMATION]{/b}, you’ve been a fucking blubbering mess."
    ni "I get that you probably {b}[[REDACTED ~ UNIMPORTANT]{/b}, but it’s time to move on. You can’t just stay a teenager forever because you’re afraid of growing up. Do you understand?"
    s "..."

    scene nikitired5
    with dissolve

    ni "..."
    ni "I’m sorry. "
    ni "I’ve been holding that in for a while, but it’s mostly just me being mad. I didn’t mean it."
    s "It’s fine if you did. "
    s "There aren’t many people who’ve been as straight with me as you were just now."
    ni "There aren’t many people who understand you. And, not gonna lie...you don’t make it easy."

    scene nikitired6
    with dissolve

    ni "But we’re {i}friends{/i} before anything else, you know. "
    ni "That’s how this all started, after all."
    ni "Just...two kids who met by chance one day."

    scene nikitired7
    with dissolve

    ni "She was a bossy nerd who spent all of her free time watching cartoons...and he was a quiet boy who always looked like he was one step away from being snapped in half."
    ni "At first, he made her feel a little uncomfortable. "
    ni "But the more she saw him here, the more she knew she was going to wind up being responsible for him one way or another."
    s "{i}Here?{/i} So...this is-"

    scene nikitired8
    with dissolve

    ni "Mhm."
    ni "This is where it all began."
    ni "And if you didn’t show up today, it’s where it would have ended."
    s "..."
    ni "..."
    s "I’m here, Niki."
    ni "Yeah..."
    ni "You are..."
    ni "And still one step away from being snapped in half all these years later..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nikitired9
    with dissolve2

    s "Where are we now?"
    ni "A hill."
    s "No deeper meaning to it this time? Not the hill where we first held hands or something to that effect?"
    ni "I think you fingered me here once. But other than that, I don’t think it’s particularly important. Nice view, though."
    s "Yeah...you can’t even see the wall from here."
    ni "Feels like it’s visible pretty much everywhere nowadays, doesn’t it? Makes you realize how trapped we are."
    s "I’m sure you have ways of getting out. You’re a famous pop-star and all. The world outside of Kumon-mi needs you."
    ni "There are other Niki Nakayamas in other parts of the world. I’m sure they’ll be fine. "
    ni "There’s somebody I’ve gotta stay here and look after anyway."
    s "You don’t {i}have{/i} to, Niki. I’ll get by on my-"
    ni "Hm? I’m talking about Noriko, obviously. You can go fuck yourself."
    s "Wow. Okay. Fuck you too, then."
    ni "Haha! I’m kidding, calm down. Noriko’s way more independent than you. She’ll be fine on her own."
    ni "I give her a lot of shit since she’s my sister, but I really do think she’ll wind up an amazing woman someday."
    s "I...think so too. She really amazes me sometimes."
    ni "I’d be surprised if she didn’t. She tries harder around you. Always has, always will. "
    ni "But I guess that’s to be expected when you’ve been filling the “cool older brother” role in her life ever since she was little. “Cool” being a word I’m using lightly, of course. {i}I{/i} don’t think you’re cool at all."
    s "Were we ever like that?"
    ni "Like what? Siblings?"
    s "Yeah."
    ni "Mmm...no. Not really."
    ni "There may have been a short period of time where I felt like an older sister to you, but it didn’t last long. Especially when I found out you were older than me."
    ni "We’ve always been close, though. Other people from the neighborhood would always tell me how weird it was when they’d see me walking around without you. Not sure if you ever got that."
    s "Not sure if I’d remember even if I did."
    ni "Yeah...there’s that too."
    s "..."
    ni "..."
    ni "You know, Noriko’s a lot older now. If you’re starting to feel a little differently about her-"
    s "Are we really doing this?"
    ni "Hold on. Let me finish."
    s "There’s no possible way that topic can end on a good note."
    ni "Why not? You’re not already messing around with her, are you?"
    s "Niki-"
    ni "Oh my God, relax! I’m kidding."
    ni "I’m just saying...she’s still in the process of learning how to see you as something other than a brother...but it’s okay if you start to see her as a woman, you know."
    ni "She’s not going to be a kid forever. She barely even copies me anymore. She’s her own person and deserves to be treated as more than my little sister."
    s "..."
    ni "I really love her. Like, a lot. "
    s "I can tell...I can’t wait to let her know you said that."
    ni "Please don’t. It’s still embarrassing even if it’s true. "
    s "Why bother telling me then? You know I’m just going to tease you about it."
    ni "{i}Because,{/i} {b}[[REDACTED ~ REPEATED USAGE OF PROHIBITED WORD]{/b}, you’re one of the few things in this world that can actually hurt her."
    ni "Even if she’s strong, she’s still growing. And since she’s in the process of finding herself, it means there are going to be a bunch of pieces scattered around that she needs to collect."
    ni "I’m sure some of those pieces are in your hands...and that’s why I feel like it’s my duty to tell you, as her sister and {i}not{/i} your psycho ex-girlfriend-"
    s "Don’t hurt her. Got it."
    ni "Not that. Well, yes that. But there’s something more as well."
    ni "{i}Help{/i} her. "
    ni "Even the most independent of us need a hand from time to time. Noriko’s amazing, but she’s no exception to that. And there are things you can do for her that I simply...can’t."
    ni "It sucks, but it’s the truth. "
    ni "The two of us have watched you forever. You’ve helped both of us learn all sorts of things about ourselves without even trying."
    ni "I’m old and decayed and set in my ways at this point, but she’s still young and full of life. And now that you’re back, she’s following your lead again."
    s "You’re 29, Niki. You’re not “decayed.”"
    ni "Maybe not {i}physically,{/i} but my brain is fried from having to balance all of this idol stuff with all of this {i}you{/i} stuff."
    s "Is my existence really causing you that much stress?"
    ni "Oh {i}fuck{/i} yeah. I found a grey hair last week and cried for twenty minutes. But that’s more on me than it is on you."
    ni "I just want you to be happy. That’s all. "
    ni "It doesn’t have to be {i}with me{/i} if you don’t want it to be."
    ni "I love you — and I don’t mean that in a romantic way this time. "
    ni "Please talk to me if there is ever anything you need. "
    s "Anything?"
    ni "If you ask me for a blowjob right now, I swear to God."
    s "I mean...if you’re offering..."
    ni "{b}[[REDACTED ~ FURTHER OFFENSES MAY RESULT IN UNEXPECTED SIDE EFFECTS. PROCEED WITH CAUTION.]...{/b}"
    s "I’m kidding."
    s "I’ll try and lean on you a little more, but don’t blame me if a lot of it sounds crazy because it most assuredly will."
    ni "I’ve been unhealthily obsessed with same boy for like two thirds of my life. I can handle crazy. "
    s "Well, I wouldn’t blame you if you couldn’t. A lot of what’s been happening to me lately isn’t really all that believable."
    ni "Only one way to find out, I guess."
    s "..."
    ni "..."
    ni "Thanks for calling me today. This is the most productive talk we’ve had ever since...you know."
    ni "Between all of the panic attacks and migraines you give me on a weekly basis, it’s easy to forget how nice the good times can feel."
    ni "And how so many of the best moments in my life have been little things like this — where the two of us just sit under a tree and...talk."
    s "..."
    ni "We’ve come a long way, haven’t we?"
    s "Seems like it."
    ni "Growing up kind of sucks, huh?"
    s "Everything sucks. Accepting that is the first step of obtaining true adulthood."
    ni "Said the perpetual manchild to the thirty-year old virgin."
    s "Hey, you’re not thirty yet. There’s still time."
    ni "Pfft. Yeah, sure. I’m starting to think I’ll die a virgin at this rate."
    s "Not if I have anything to do with it."

    $ renpy.end_replay()
    $ nikilovesyou1 = True

    jump nikilovesyou2

label nikilovesyou2:
...
```

## Code that triggers this event

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label callnikimorning:
    if niki_love >= 0 and nikidate1 == False:
        jump nikidate1
    if niki_love >= 10 and secondbeach18 == True and nikidate10 == False:
        jump nikidate10
    if niki_love >= 20 and slumberreset5 == True and day == 6 and nikilovesyou3 == False:
        jump nikilovesyou1
...
```