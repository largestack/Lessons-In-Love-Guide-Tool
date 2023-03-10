# Friends (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Imaginary Veins](./beachmas2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachmas3
* Group: Main
* Triggered by label: beachmas2
* Chain sources: beachmas2
* Chain sources path: beachmas2

## Official wiki page

[Friends](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas3&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label beachmas3:
    scene beachmasthree1
    with dissolve2
    play music "summerwind.mp3"

    a "Oh, good! You’re back. I was just about to stop what I was doing and chase after you for once again talking to my friends without inviting me along."
    ay "We were just having another...emergency meeting to plan your next birthday party."

    scene beachmasthree2
    with dissolve

    a "Wow...you guys are really getting the ball rolling early this time, aren’t you?"

    "Ayane and I make our way back to the rest of the girls while Maya ventures off to do...Maya stuff. "
    "But considering the fact that none of them greeted either of us with concern or confusion tells me that, in our recent “absence,” things have stayed at least somewhat normal."
    "And that is something I can say with confidence given just how many “Sensei, are you okay?”s I have gotten succeeding my {i}blackouts{/i} over the past couple years."
    "But now comes that hard part — figuring out exactly how much we missed and what may have happened within that time."

    ay "So, Halloween. Am I right?"

    "Okay. Or Ayane’s just going to get right to work with the completely normal and not at all suspicious beach conversation topic of a holiday that may or may not have just happened."

    mo "No, I don’t believe you are."
    a "First my birthday, now Halloween? Why are you acting like you’ve gone back in time all of a sudden?"
    a "If this is another inside joke you guys have thought up while I wasn’t around, I’m-"
    ay "Oh, no. Just...thought I’d break the ice. "
    s "Maybe break the ice with something a little more relevant and {i}natural{/i} next time."

    scene beachmasthree3
    with dissolve

    ay "My bad! Just...can’t wait for whatever the next holiday is! Which could really be {i}anything{/i} with how many lesser-known, weirdly specific holidays there are nowadays."
    mo "Have you been microwaving any bananas lately? Are there secret government agencies on your trail? Because I can help you. I just need to know {i}how.{/i}"
    a "At least you’re acting normal, Sensei. Sudden and suspicious disappearances become a lot {i}more{/i} suspicious when {i}both{/i} people who disappeared are suddenly acting...you know. Suspicious."
    sa "Didn’t...um..."
    sa "Wasn’t...Maya...with you as well?"
    a "Hey, yeah. Where’d Maya go? They just opened some new stalls further down the beach and we were supposed to go buy some stuff for tonight. "
    s "Beats me. She’s probably off preparing for the date we’re going on later."

    scene beachmasthree4
    with dissolve

    mo "Pardon me for asking, Sir- but did you perhaps finish the rest of our routes and then proceed to erase our recollection of them? Because I always assumed the Maya route would be the last to unlock."
    a "There will be no Maya route. Or a Molly route. Or a Sana route or an Ayane route. Or any route other than an Ami route. "
    a "I am the only heroine Sensei needs and he is smart enough to never choose anyone else. Isn’t that right, Sensei?"

    menu:
        "I pledge to only play the Ami route":
            s "Sure."

    scene beachmasthree5
    with dissolve

    a "See? I’m the only one good enough for him and that’s how things will always be forever and ever and ever and-"
    mo "I suppose there are worse choices to be made. I’m no stranger to gunning it for the incest route if the heroine is likable. And Ami seems like good heroine material at the end of the day."
    sa "Uh...how about we...don’t talk about...weird things like that? "
    a "Is it really {i}weird,{/i} though? Because I don’t see how it’s any different from a more standard kind of-"
    s "Ami, stop it."

    if amifingered == True:
        "As interested in hearing about your undying love for me as I {i}always{/i} am, I find it hard to carry on with this conversation while Ayane looks so...melancholically resigned and mildly complacent."
    else:
        s "People are going to start saying things. "
        a "Oh no. Whatever would we do if that were to happen?"

    scene beachmasthree6
    with dissolve

    ay "G...Getting things back on track, would anyone happen to remember what day it is?"
    mo "What track are you even on exactly? Because your entire appearance today has made it sound like you’re playing Crash Team Racing while the rest of us are cruising down Rainbow Road."
    a "Hm? It’s Monday."
    ay "If it’s Monday...why aren’t we in school? "
    s "What part of this is {i}natural{/i} to you?"

    scene beachmasthree7
    with dissolve

    mo "I’ve got it! You {i}have{/i} completed Ayane’s route! "
    mo "And the only reason she’s acting so strangely today is because her memories are slowly leaking back into her due to the sheer power of her love for you! "
    mo "There’s no need to tell me I’m right. I already know I am."
    s "You’re not. But strangely enough, I’m not really 100%% confident in saying that."
    a "Uhh...we’re not in school because we’re on Winter break, obviously."

    scene beachmasthree8
    with dissolve

    ay "How is that obvious?! We’re at the beach and it’s gotta be like...ninety-five degrees!"
    mo "Why are you using Fahrenheit? We live in Japan."
    a "It’s obvious because the calendar says it’s winter, so it’s obviously winter. I don’t see why you have to be so weird about it."
    a "Plus, even if it {i}wasn’t{/i} winter, we’d still have off for Christmas tomorrow. "

    scene beachmasthree9
    with dissolve

    ay "C...Christmas is tomorrow?!"
    s "I guess I’ll be the one to just slip in the fact that Christmas is always in winter and that what Ami said just now didn’t really make any sense."
    mo "Should we maybe take the bubble wrap princess back to the inn? I’m worried that she may hurt herself in her confusion."
    sa "I...can go back with you if you want..."
    sa "I’m...kind of...hot out here anyway..."
    mo "You certainly are in that swimsuit. I mean what? I didn’t say anything."
    sa "And I...didn’t {i}hear{/i} anything..."

    scene beachmasthree10
    with dissolve

    ay "No...I’m...I’m good. I just didn’t really sleep that well, I guess. So sorry if I wind up periodically saying more suspicious-sounding things throughout the day. Which is...apparently Christmas Eve."
    a "Really? We slept in the same bed and I don't remember you waking up even once. But, then again, it wouldn’t be the first time you snuck out of bed without me realizing it."

    scene beachmasthree11
    with dissolve

    ay "Uhh...one last question. If tomorrow is Christmas, how come we’re at the beach {i}now?{/i} "
    ay "Don’t we normally hang out at that hotel in the urban district for Christmas? And...don’t we normally come to the beach {i}before{/i} Halloween?"
    a "Do we? I don’t know. Things seemed pretty normal to me. "
    a "The only complaint I have is that we still don’t know what the grand prize from the Dorm Wars is apart from the fact that it’s just Sensei."
    s "Am I not just rooming with the winning floor again?"

    scene beachmasthree12
    with dissolve

    a "No. Imani didn’t like that idea and she said you should just stay with her instead."
    s "Okay. And where is Imani being forced to sleep after you all joined hands and rejected that suggestion together?"
    a "Our room. Tied up in the corner."
    s "Oh well. Safer your room than the one is Kirin is in, I guess."
    s "How does that affect the Christmas party, though? If we’re still having one, that is."
    a "I told you earlier, didn’t I? That’s going to be in our room as well. All the fun stuff is happening in the first floor's room since it’s bigger."
    a "And also because we’re the superior floor that loves you more. "

    if dormwar2floor2win == True:
        mo "And yet...{i}my{/i} floor is the one that emerged victorious. How strange."
        a "Are you suggesting something, Molly?"
        mo "Oh, no. No..."
        mo "Just the fact that our floor will undoubtedly have the better h-scenes due to our more extreme personalities. "
        ay "{size=-15}Well, you’ll certainly have {i}more{/i} of them at this rate.{/size}"

    "Well...I guess that solves the “{i}Where are we in time?{/i}” question."
    "But if nearly a full two months have passed since the ending of the Dorm Wars...just what {i}else{/i} has happened within that time?"
    "And, better question, what happened between {i}Yumi{/i} and me? Because I was talking to her when the sudden transition came and..."
    "And if the way she looked is any indicator of how that must have gone from her perspective, there’s no doubt she’d be confused."
    "..."
    "I should...probably go and find her."

    s "Uhh...have any of you seen Yumi, by any chance?"

    scene beachmasthree13
    with dissolve

    a "Was being with her all morning not enough?"
    s "What?"
    mo "I believe Arborea is referring to the mass amount of affection points you have been grinding with her lately."
    sa "It’s true that you...have been spending more time with her than normal lately..."

    "Ayane and I exchange a glance of mutual confusion as to what this must mean, but it doesn’t detract from the fact that I need to see her {i}now{/i} to clear all of that up."

    s "I-"
    a "No one’s seen her since you scared her off a little while ago. And I wouldn’t bother chasing after her if I were you."
    s "Well, you’re {i}not{/i} me. And I’m free to chase whoever I want to chase after."

    scene beachmasthree14
    with dissolve

    a "Hey, don’t be mean! I’m only saying that because you’ve seemed really exhausted lately and I worry about you."
    a "I know it’s {i}my{/i} job to take care of you, but if you don’t start taking {i}some{/i} sort of care of yourself,  you’ll wind up-"
    s "Yeah...I know. I just-"
    a "..."
    sa "..."
    mo "..."
    s "I’ll see you guys later on..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene beachmasthree15
    with dissolve2

    to "Yasu, please be careful. You know I don’t like it when you go in the water without your floaties."
    to "It was hard enough getting you to stop nearly drowning yourself in the bathtub and the last thing I want to spend this holiday season doing is planning a funeral for a body lost at sea."
    mak "Hey, let’s not bring up funerals."

    scene beachmasthree16
    with fade

    to "Oh my! I’m so terribly sorry, Makoto. It simply slipped my mind and I will do my best to make sure it doesn’t happen again."
    mak "It’s whatever."
    mak "Dwelling on it won’t help me move on at all but, at the same time, hearing anything that {i}reminds{/i} me of it just makes me feel like shit again."
    mak "How fun and exciting it is to have a never-ending connection to misery that I can, in no way, learn how to subvert or move past. Yippee. "

    scene beachmasthree17
    with dissolve

    to "I will not attempt to understand what you’re going through, but I’m certain that your pain is not “never-ending.”"
    mak "Yeah, it seems like everybody is sure of that but me. "
    mak "It’s weird. I always figured Makoto 2.0 would be more fun and outgoing and...less of a bitch. "
    mak "But if anything, I’ve just turned into a fatalistic version of myself who struggles even caring about all of the things she used to throw herself at every single day."
    to "Trauma works in mysteriously terrible ways, I’m afraid. "

    scene beachmasthree18
    with dissolve

    to "But, Makoto...you’re wrong in referring to this stage of your life as a new you. "
    to "We are but a sum of the experiences we have and the hardships we endure. And I’m positive that many years from now, you’ll look back on this time and accept it as something that made you {i}you.{/i}"
    mak "Thanks. I hope you’re right. I just can’t really see things like that right now, I guess."

    scene beachmasthree19
    with dissolve

    to "And that’s fine. All good things take time."
    to "Besides, there are plenty of people who would be happy to lend you a hand if you ever desire to reach out for one."
    mak "There are three. Miku, my mom, and Sensei. And more often than not, Sensei winds up making everything worse."
    to "You know he’s not trying to, though."
    mak "I know. "
    to "Also, there’s a fourth person right beside you. "

    scene beachmasthree20
    with dissolve

    mak "Thanks again, but you don’t actually mean that. You’re just saying it out of pity and obligation because you feel bad for the girl with the dead dad."
    to "That’s not true at all. In fact, I’ve always admired what you do for the class. "
    to "And if it weren’t for the worksheets you would make me when I first transferred in, I can’t say I’d even {i}be{/i} here right now."
    to "But I’m happy I am. Which means that part of that happiness should belong to you as well. "
    to "You’ve not only earned it, but {i}need{/i} it more than anyone right now."

    scene beachmasthree21
    with dissolve

    mak "That’s..."
    mak "That’s actually one of the nicest things anyone has ever said to me."
    to "If that is true...that is very sad."
    mak "It really is, isn’t it?"
    to "Makoto...forgive me if this is too forward. Or if this is not how the process normally goes as I’m still mostly unfamiliar with it-"
    to "But I’d very much like to be friends with you if that is something you’d have any interest in."

    scene beachmasthree22
    with dissolve

    mak "I’m also not that familiar with the process...but I’d like that too."
    mak "It’s a breath of fresh air talking to someone who I don’t feel like I’m {i}responsible{/i} for in some way."
    to "That does sound tiring, yes. And also dissuades me from burdening you with the plea for advice I was just moments away from requesting."
    mak "Is it about the present you got for Sensei? The one you told me about earlier? "
    to "It is. "
    to "Seeing as you returned last year’s present to me, I was wondering if I had perhaps gone a bit...overboard as well this year."
    mak "Do you want my honest answer? As a friend?"
    to "If you’d be so inclined."

    scene beachmasthree23
    with dissolve

    mak "I think you’re fucking insane."
    to "Hah...that’s what I was worried about."
    to "Gift-giving truly is my weakest point, I suppose."
    to "The thought that went into it, though-"
    mak "I’m sure the thought is great, yeah. "
    mak "I just don’t really think you understand quite {i}what{/i} you’ve done yet."
    to "Should I maybe exchange it for something else?"
    mak "Is that even possible?"
    to "Anything is possible when you are as wealthy as I am."

    scene beachmasthree24
    with dissolve

    mak "I’ll leave that up to you, then."
    mak "I just..."
    mak "I probably wouldn’t tell anyone else about it if I were you..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ beachmas3 = True

    jump beachmas4

label beachmas4:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
scene yumisawathing24
    with dissolve

    y "Huh?"
    c "It’s one thing to not like someone. But seizing every opportunity you get to shit on them even when they’re not relevant is like, a major red flag."
    y "What are you saying?"

    scene yumisawathing25
    with dissolve

    c "I’m saying that if you {i}do{/i} like the same person as me...that you better fucking tell me about it instead of just locking it away."
    y "But why would-"
    c "Because if you do the latter, it’s going to blow up in your face {i}and{/i} mine and we’re never going to recover from it."

    scene yumisawathing26
    with dissolve

    y "Dude, I’m not-"
    c "To clarify before you get mad, I’m not accusing you of anything. "
    c "I’m just telling you, as a friend, that the right thing to do is to be honest with me. Because I’ve always been honest with you."
    y "..."
    c "Also, I was only half joking about my threesome offer a while ago."

    scene yumisawathing27
    with dissolve

    y "Why do you always have to ruin everything like that?"
    c "Just the kind of girl I am, I guess."

    scene yumisawathing28
    with dissolve

    c "But for real, what are you doing over here while everybody else is off having fun?"
    y "I think not having fun is more fun than having fun most of the time. "
    c "That was a weird sentence."
    y "Probably just need to cool off or some shit. I don't know."
    c "Somebody said they saw you talking to Sensei before you stormed off. That have anything to do with it?"
    y "Maybe. Probably. Who knows?"
    c "I see."
    c "So, let me just circle back to the masturbation thing then-"

    scene yumisawathing29
    with dissolve

    y "I’d really prefer you didn’t."
    c "I’m kidding. If you don’t mind, though, I’m down to hang out here and “not have fun” with you for a little while longer. "
    c "I’ve gotta do some brainstorming for Sensei’s present anyway as I’m still not really sure what the best way to pull it off is."
    y "You planning some sort of romantic grand gesture or some shit? Sounds gross."

    scene yumisawathing30
    with dissolve

    c "Something like that. Not a Secret Santa thing, though. Just a normal ole romantic present exchanged between student and teacher. "
    y "Think he’ll actually get {i}you{/i} something this year?"
    c "I hope..."
    c "Though, he does already pay for my phone...and {i}your{/i} phone, so yeah."
    y "Don’t remind me. "

    scene yumisawathing31
    with dissolve

    c "Speaking of Secret Santa, though...who’d you get? Anyone fun? Are you excited?"
    y "Excited for...giving a gift? The fuck do you think I am? Course I ain’t excited. That’s money I could be usin’ on myself."
    c "I hope it’s Nodoka. That would be hilarious."
    y "Close. I got Futaba. Easy to shop for, though. Probably just gonna grab some random book at a gas station or some shit."
    c "She’s been getting pretty into romance novels lately from what I’ve heard."
    y "Wow. Exciting. "
    c "Hey, I’m just trying to help you out since you’ve got like, twenty-four hours left to actually buy something and I know you always wait until the last minute."
    y "Yeah...Actually, instead of hanging out here, why don’t we just get on the bus and head back early? Can go...{i}shopping{/i} or some shit. You like that, right?"
    c "I do and nice try. "
    c "I’ll come with you to the convenience store, but we’re coming back after that. I want to spend more time with that one guy you’re always bringing up. What was his name again?"

    scene yumisawathing32
    with dissolve

    y "Do you even {i}know{/i} his name?"
    c "Honestly? I’m not even sure if Ami does. I’ve been waiting for her to slip and it legit never happens."
    y "And you haven’t thought of...you know...asking?"
    c "Nope. I’m in too deep now. Just gotta ride the wave until I figure it out."

    scene black
    with dissolve2
    stop music fadeout 10.0

    c "Anyway! I guess I should get dressed. Not sure if the convenience store will let me in half-naked."
    y "Make sure you knock before going into the bedroom. Learned my lesson earlier."
    c "Oooooh who’d you get to see? Anyone exciting?"
    y "The fuck does that even mean?"
    c "Hey, I’m just saying...if I opened that door and, like...Tsuneyo or Imani were getting dressed in there, I’d probably hang around for a little while."
    y "Uhh...yeah, I ain’t really sure if you would."

    $ renpy.end_replay()
    $ beachmas2 = True

    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    jump beachmas3
...
```