# Two Months of Nothing (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Approximation](./slumberreset2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: yumislumber1
* Group: Yumi
* Triggered by label: slumberreset2
* Chain sources: slumberreset2
* Chain sources path: slumberreset2

## Official wiki page

[Two Months of Nothing](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumislumber1&go=Go) for more details.

## Event code

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label yumislumber1:
    if tsuneyoslumber3 == False:
        scene mayanebench30
        with dissolve

    play sound "phonebeep.wav"

    "I tap on Yumi’s name in “my” phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    y "Uhh...hello?"
    s "Hey."
    y "Who the fuck is this?"
    s "Your teacher. I’m calling you from my new secret phone number."
    y "Um...congrats?"
    y "The fuck you want? Why you callin’ me?"
    s "Maybe I just miss you?"
    y "And maybe I’ve gotta find someone willin’ to give me one of those lobotomy things so I can forget I ever heard that. Later."
    s "Wait. On a serious note, are you busy right now?"
    y "Yeah."
    s "With what? You’re unemployed and don’t have a house."
    y "And you’re a fucking douche nozzle! I’m hanging up now!"
    s "Stop whatever it is you’re doing. We need to meet up and continue our conversation from last night. It’s important and...apparently {i}time{/i}-sensitive."
    s "That was a hilarious pun that you won't understand. But hopefully, you will soon."
    y "Can't. Chinami's got a fever. You want me to leave her alone so I can come talk to {i}you{/i} about my random ass memory issues?"
    s "Chinami’s sick?"
    y "Yeah. And I’m stuck at {i}your girlfriend’s{/i} house watchin’ her until the mall closes and Chika comes back home."
    s "Great. I’ll meet you there."
    y "The fuck you will! Were you not payin’ attention when I told you Chinami’s sick?! She needs rest!"
    ch "{i}Is that Chinami’s papa?! The new one, not the one who abandoned her!{/i}"
    y "No! It’s the fucking...bank."
    ch "{i}Did Chinami’s recent deposit clear?{/i}"
    s "I’ll see you soon, Yumi."
    y "Don’t you fucking-"

    if tsuneyoslumber3 == False:
        scene black
        with dissolve

    play sound "phonebeep.wav"
    stop music fadeout 10.0

    "I hang up the phone and begin to make my way over to the second half of town."
    "Thankfully, I am no longer completely bewildered in terms of my location and am able to make it to the bus stop without any issues at all."
    "And while I’d normally just bite the bullet and walk there, I’m admittedly a little worried about Chinami and would like to make sure I see her at least one more time before she dies. "
    "I kid, of course. Kind of."
    "I don’t know."
    "Maybe Maki’s morbid sense of humor has just rubbed off on me after all the time I spent with her during Makoto's tragic arc."
    "Regardless, I double check the bus schedule on my new backup phone and take a seat on the bench, waiting patiently for it to arrive and carry me toward my current goal."
    "Here’s hoping Yumi likes sleepovers."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene yumicurtain1
    with dissolve2
    play music "normalday.mp3"

    s "Hey, I’m here."
    y "Yeah, I can see that! The Hell do you think you are, just walkin’ into somebody else’s house?!"
    s "In my defense, it’s not like you didn’t know I was coming."
    y "That doesn’t make it okay! Go back out there and knock or ring the bell like a normal person!"
    s "But if I do that, you’ll lock me out."

    scene yumicurtain2
    with dissolve

    y "Tch. Was hopin’ that would work."
    s "On the bright side, I’m glad to have made it before visiting hours ended. How’s the patient?"

    scene yumicurtain3
    with dissolve

    y "Chinami, how are you?! "
    ch "Chinami is fine! Hi, Papa!"
    s "Where did you get such a huge privacy curtain? That’s like, straight out of a hospital."

    scene yumicurtain4
    with dissolve

    y "Probably because it {i}is{/i} straight out of a hospital. Shit’s been here longer than I have. "
    y "Pretty sure they’ve had it ever since Chinami was born on account of her whole immune thingy."
    ch "Chinami used to spend a lot of time behind her safety curtain, but now she only has to use it some- {i}ack!..keh...{/i} "

    scene yumicurtain5
    with dissolve

    y "Hey! Go back to sleep! You know you ain’t gonna get any better if you get all excited and sh...and crap."
    s "That really isn’t much better, Yumi."
    ch "Chinami is fine! She just swallowed a bug!"

    scene yumicurtain6
    with dissolve

    y "Just ignore her. She’ll go back to sleep if we don’t pay any attention."
    s "Is keeping her here okay? Wouldn’t it be better to take her to a hospital or something?"

    scene yumicurtain7
    with dissolve

    y "With what money? Tsukasa ain’t paid me yet and you know damn well how much Chika’s got."
    s "I’m sure the Tsukiokas wouldn’t mind fronting the bill if it meant keeping Chinami healthy."
    y "It’s fine. Shit like this ain’t all that uncommon. Just a normal cold or somethin’. I’ve been givin’ her medicine and her fever’s already started to break and whatnot."
    s "Good. It’s not every day I get to see you being responsible. I like this side of you, Yumi."
    y "Only side of you I like is the...one outside of this apartment."
    s "Good one. "
    y "Suck my left nut. Why are you even here? What do you want?"
    s "I told you on the phone, didn’t I? We need to resume our conversation from last night."

    scene yumicurtain8
    with dissolve

    y "Probably better off just startin’ from the beginning. Shit confused me so much I can barely even remember what it is we were talkin’ about."
    y "Somethin’ with the last two months, right?"
    s "Right. Did you try talking to anyone else about that after I ran off last night?"
    y "Only person I have to talk to is Chika and it seemed like everything was pretty fuckin’ normal from her point of view. Meanin’ it’s probably only me who-"

    scene yumicurtain9
    with dissolve

    y "Wait! You didn’t give me your fuckin' memory disease, did you?!"
    ch "Yay! Chinami won’t be alone in the safety curtain! She’ll make room for big sis Yumi right now!"
    s "I didn’t give you a {i}disease{/i}, Yumi."
    ch "Aww, rats..."
    s "But just because you’re not terminally ill doesn’t mean this is something we can ignore. "
    s "Well...I guess technically we {i}could{/i} ignore it and it wouldn’t make much of a difference to you. But it would be a big help for me and a couple other people if you could at least listen for a little while."

    scene yumicurtain10
    with dissolve

    y "Okay. So {i}you{/i} want {i}me{/i} to take time out of {i}my{/i} life so that {i}your{/i} life can get better or some shit...while I don’t benefit at all. Am I hearin’ that right?"
    s "More or less."
    y "Gotcha."
    y "Welp, you know where the door is."
    s "Yumi, come on. Just hear me out."

    scene yumicurtain11
    with dissolve

    y "Ahhhhh, fine! But the second this gets too friggin’ weird I’m calling Gary!"

    scene black
    with dissolve

    s "Great. Thank you — wait, who’s Gary?"

    "........."
    "......"
    "..."

    scene yumicurtain12
    with dissolve2

    "I help myself to a pot of coffee left out on the kitchen table and quickly come to understand that this was definitely not made anytime within the last six hours."

    y "You gonna microwave that shit or just pretend it’s drinkable?"
    s "I made this bed and I now have to lie in it. But that is beside the point."
    y "Mhm. And the point is?"
    s "..."
    s "How do you feel about sleepovers?"

    scene yumicurtain13
    with dissolve

    y "Why do you exist?"
    s "Actually, it’s funny you should ask because that’s a big part of why I’m here today."
    y "It’s like every single thing you say makes shit ten times more confusing."
    s "Then I’ll fulfill your greatest wish and shut up while you do your best to recollect the last two months of your life."

    scene yumicurtain14
    with dissolve

    y "Looks like we’re both gonna shut the fuck up, then. Cause that’s exactly what I was tryin’ to do all last night ever since you pointed shit out and I’ve got nothin’."
    y "If you know what’s goin’ on with me, fucking spill it. Because all the shit I keep hearin’ about the space between Halloween and Christmas is makin’ my head spin."
    y "Didn’t think much of it at first, but I straight up can’t even picture any of it when I try to. It’s like all that time was just fuckin’...ripped outta my mind or somethin’."
    y "That what it’s like for you too? You know, with all your memory shit."

    scene yumicurtain15
    with dissolve

    s "More or less. Just it’s a lot more than two months for me and I also, occasionally, do things like black out and force myself on teenage girls."
    y "Those “blackouts” have somethin’ to do with it too? That shit ain’t gonna start happenin’ to me next, is it?"
    s "I have no idea. And I’m probably not even the right person to lead a conversation like this since I have very little understanding of how {i}anything{/i} works."
    s "But you’re an outlier right now...so I do know that the logical course of action would be trying to figure out {i}why.{/i}"
    y "The fuck is an “outlier?”"
    s "Something that skews what’s meant to be an average."
    s "For example, if we calculated the mean age of everyone in class, {i}I{/i} would be the outlier since I’m way older than all of you and would force that mean upward."

    scene yumicurtain16
    with dissolve

    y "Good. So you {i}do{/i} understand that. Now think long and hard about why that makes you such a fucking creep."
    s "I have plenty of time to think about how horrible of a person I am. But, for reasons I am mostly incapable of explaining, you might not have equal time to do the same when it comes to this."

    scene yumicurtain17
    with dissolve

    y "Huh? I ain’t gonna, like...die or some shit, am I?"
    s "Nothing that serious, no."
    y "Then what? My memories just gonna, like...come back or something?"
    s "They might."
    y "I ain’t seein’ what the big deal is, then."
    s "Would you see the “big deal” if I told you those two months may have never even happened in the first place? And that everyone’s memories of it were just false?"
    y "Uhh...no. But I {i}would{/i} call you a fucking lunatic."
    y "If everybody’s got memories of those months and it's just you and me who don’t, wouldn’t {i}we{/i} be the ones...in the wrong or whatever?"
    s "This is less about who is wrong and who is right and more about {i}why{/i} we’re in the position we’re in."
    s "Isn’t it strange knowing there could be something different about you, Yumi?"

    scene yumicurtain18
    with dissolve

    y "Not...really."
    y "I’ve been different my whole fuckin’ life, man. And I’ve been hearin’ all about it since the first time I knocked somebody’s lights out in daycare."
    y "Might’ve wound up a better person if somebody looked after me now and then, but I’m well adjusted to not fitting in already."
    s "This is different, though. This is-"
    y "No shit it’s different. This is like, some...borderline supernatural shit."
    y "But if {i}you’ve{/i} got no idea why this is happenin’ and everybody {i}else{/i} is just gonna be weird if we try and talk about it, the Hell’s the point in even trying in the first place?"
    y "Can’t say I’d feel the same way if I lost as much time and memory as you, but it’s just two months. And those two months weren’t really all that bad from what I understand."
    y "Wound up back in school, didn’t I? That’s gotta be a plus, right?"
    s "Is that what you wanted, though? I thought you were planning on dropping out?"
    y "I..."
    y "I don’t know. Last I remember, I was still trying to figure shit out."
    s "I’m surprised you’re okay with the universe just deciding things for you, then."

    scene yumicurtain19
    with dissolve

    y "Nobody decided shit for me. The only person who chooses what I’m gonna do is myself."
    s "Then what will you do if this happens again?"
    s "What will you do if there’s {i}another{/i} huge leap in time that just sets you on autopilot until you’re eventually spat back out into the world?"
    y "Fuck if I know. But as long as I’m not blackin’ out and doin’ shit like-"
    s "Maybe that {i}is{/i} what happened in those two months."
    s "Maybe {i}both{/i} of us blacked out and things just...didn’t go as poorly as they could have."
    s "We were together, weren’t we? It’s possible."
    s "One second, everything was normal. Or at least as normal as it {i}could{/i} have been with me admitting all of that stuff about masturbating to you and whatnot-"

    scene yumicurtain20
    with dissolve

    y "Stop bringing that up!"
    s "And the next second, two months of our lives were gone."
    s "If you’re okay with that happening again, fine. Disregard everything I’m saying and just keep living life the way you always do."

    scene yumicurtain21
    with dissolve

    s "But if you want to take some control back into your {i}own{/i} hands...and don’t want to have any more time taken away from you...why not try and figure this out with me?"
    y "The fuck you bein’ all serious for? It’s makin’ me uncomfortable."
    t "'Sides, the Hell can {i}we{/i} do about this in the first place? You might be smart or whatever, but you ain’t a doctor."
    s "No, I’m not. Nor am I whatever type of scientist handles time travel or...even a {i}teacher{/i} most of the time."
    s "But I’m someone who won’t think you’re insane when you want to talk about things you don’t particularly understand."
    s "I don’t know if I can {i}help{/i} you, per se...but I might be able to help you feel a little less alone."
    y "..."
    s "Which is why I need you to sleep at my house."

    scene yumicurtain22
    with dissolve
    play sound "dooropen.mp3"

    y "Of fucking course that’s what it all comes down to. No idea why I let you just keep talkin’ me into a fuckin’ corner for so long."
    y "Hell of a charade, I’ll give ya that much. But if you’re really gonna try and {i}win me over{/i} or whatever-"
    c "Sensei? What are you doing here?"

    scene yumicurtain23
    with dissolve

    y "B-Better question...what are {i}you{/i} doing here? I thought you had work?"
    c "I was able to get somebody to cover for me. Did {i}you{/i} invite Sensei over?"
    y "Course not. Dude just fuckin’ waltzed in as if he owned the place."

    scene yumicurtain24
    with dissolve

    c "So...you’re {i}not{/i} having an affair?"
    y "Obviously not! No!"

    scene yumicurtain25
    with dissolve

    c "Great! Then it should be totally fine if I do this!"
    y "Do what? What are-"

    $ renpy.end_replay()
    $ yumislumber1 = True

    jump yumislumber2

label yumislumber2:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
with dissolve

    ay "Is there more to it than just literally disappearing?"
    m "Very. I’m basically desensitized to it by now but, if you’re willing to give it a shot and don’t mind seeing something you will very likely never forget unless you’re fully reset, fine. We can have a “slumber party.”"
    m "But good luck trying to get Yumi and Tsuneyo to agree to it. And good luck finding a place to actually have it since getting Ami involved is basically asking to be cut off from engaging in any real conversation."

    scene mayanebench22
    with dissolve

    ay "I’d say we can use my house, but I know for a fact Geoffrey wouldn’t let me have a sleepover with Sensei. He’s been very protective ever since Todd disappeared."
    ay "But yeah...getting Yumi and Tsuneyo to agree to something like that does sound hard when we’re not really close to them."
    s "I’m not really close to them either, but...I’ll see what I can do. "

    scene mayanebench23
    with dissolve

    m "Will you find us a place to sleep as well? Preferably one we don’t have to pay for since I am currently broke and Ayane’s card is being declined everywhere."
    ay "Yup! Turns out that while the three of us were being tossed through time, my credit card was being tossed through every single terminal in Kumon-mi! "
    ay "I’m cut off from spending anything until next month when the bank sorts everything out."
    s "Wonderful. That extremely inconvenient coincidence is basically forcing me to reveal something I was {i}hoping{/i} I’d be able to keep quiet for a full twenty-four hours. But fuck me, I guess."
    ay "I would if could, Sensei. I would if I could."
    m "And what exactly do you have to reveal? A second home that none of us know about?"
    s "Yes."
    m "Funny. What {i}actually{/i} is it?"
    s "A second home that none of you know about."

    scene mayanebench24
    with dissolve

    m "What? When? Why?"
    ay "Wait a minute...who drew your name for Secret Santa this year?"
    s "Touka."

    scene mayanebench25
    with dissolve

    ay "Mystery solved. Detective Ayane has successfully closed another case."
    m "She got you a {i}house?{/i}"
    s "An apartment, technically. And you two are now the only people who know about it other than her and Makoto."
    m "Wow. And I thought my cube-shaped watermelon was a good present."
    m "So...what then? You’re just going to lure two girls you’re not particularly close with to a secret apartment and keep them there until the world breaks?"
    s "Up until last night, I would have said that scenario sounds more plausible than the two of us kissing. And yet..."

    scene mayanebench26
    with dissolve

    m "{i}Please{/i} stop bringing that up..."
    ay "What are we going to do about Ami? If all three of us leave her alone, she might explode. In fact, she might be exploding right now and none of us would even know."
    m "I’ll think of something for Ami..."
    m "For now, we need to focus on getting the other two girls on board. "
    m "I’m not sure how many nights we have left, so it’s important we figure this out as soon as possible or we’ll run the risk of their minds getting wiped along with their...potential recognition of the loops."
    s "I’d contact one of them right now, but my phone’s dead."

    scene mayanebench27
    with dissolve

    ay "Here. Take this one."
    s "I’m not going to just take your phone, Ayane. Even if it {i}is{/i} a backup and you have ten more of them in your dorm room."
    ay "It’s not just a “backup.” It’s an identical, up-to-date copy of your phone. Complete with all of your contacts and a suggestive picture of our class representative with a vibrator in her mouth."
    ay "Why {i}that{/i} is your background and not me, I don’t know. And I don’t {i}want{/i} to know. "
    s "Well, speak for yourself because {i}I{/i} would like to know why you have an identical copy of my phone including but not limited to my contacts and Makoto wallpaper."
    ay "Sometimes, I get bored and send myself text messages from fake-you while waiting for real-you to text me instead."
    s "Ayane-"
    ay "I have a problem. I know. But at least that problem is love and not drugs."
    m "Uhh..."
    s "..."
    ay "Oh, and in case you were wondering, I don’t have any of your text or call records. Apparently, having those copied as well would have been an invasion of privacy and is against the law."
    s "I think my privacy has already been invaded, but thanks. I’ll be taking that now."

    scene mayanebench28
    with dissolve

    ay "Happy to help! And don’t worry about giving it back. I have three more at home."
    s "That’s...great."
    m "Well...good luck, I guess? You’re very likely going to need it."
    ay "Be in touch after you hear back from Yumi and Tsuneyo. Like Maya said, the sooner we can get them on board, the better."
    ay "Also, maybe...don’t look at any of the messages that phone has sent to my number. I’ve been going kind of crazy these past few months in more ways than I’d like to admit."
    s "I’ll do my best, Ayane..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mayanebench29
    with dissolve2

    "I get a safe distance away from Maya and Ayane before unlocking my “new” phone with, you guessed it, the same exact passcode I use for my {i}real{/i} phone before making sure all of my contacts are there."
    "Worryingly, they are. And while I’m extremely concerned as to how Ayane got her hands on my data in the first place, I don’t really have time for that right now."
    "If the next reset really is as close as Maya says, I need to act quickly. "
    "So, without a clear idea in mind about {i}what{/i} I’m going to say when I call...I scroll through a list of names and wind up landing on-"

    $ renpy.end_replay()
    $ slumberreset2 = True

    menu slumberphonemenu:
        "Yumi" if yumislumber3 == False:
            jump yumislumber1
...
```