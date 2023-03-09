# Anglerfish
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo5&go=Go)


Part of event chain [Take Me Anywhere](./halloweentwo4.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloweentwo5
* Group: Main
* Triggered by label: halloweentwo4

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label halloweentwo5:
    i "Well hooray for me getting to be second place! It is truly an honor to be graced by your presence. "
    s "Just make sure you don’t start crying or something because it would be really exhausting having to navigate that twice within such a short period of time."
    i "Oh, don’t you worry about that. I’ll bottle my feelings up and cry when I’m alone, like any other civilized human being would do."

    "Once again, I find myself being dragged away from the party by a girl with a visible ribcage."

    if bonus == True:
        "Granted, I haven’t seen Io without a shirt on to confirm this yet, but I have a hard time believing that she, like many other girls I commonly associate with, couldn't benefit from eating slightly more."
        "I suppose that’s a conversation for another day, though."
        "Because Io and I being alone together means things will go one of two ways."
        "She’ll either self-deprecate and say a bunch of depressing stuff while still managing to keep a smile glued to her face-"
        "Or she will, once again, invite me to an amusement park."
        "The truth remains to be seen."
    else:
        "I really wish these girls would eat more. They're going to hurt themselves."

    scene ioyuminight1
    with dissolve2
    play music "comfort.mp3"

    "The secret third option, and one of the rarest for Io, is that she’ll elect to remain completely silent and gaze off toward the sky, likely thinking about how much she hates girls or something."
    "I don’t recall the forecast being cloudy with a chance of misery tonight, but I suppose no weather pattern can be discernible 100%% of the time."
    "Besides, the silence provides a nice break from the music inside- even if it’s at a noticeably lower volume than it had been the previous year."
    "It’s good to know that some of the girls are looking out for some of the others."
    "It’s worse knowing that some of them aren’t looking out for anyone at all."

    i "How do you feel about Halloween, Sensei?"
    s "Is this a trick question? Because based on what you said just a few minutes ago, I feel like I might not be {i}allowed{/i} to like it."
    i "I’m genuinely curious. "
    i "I’m already set in my ways, but I’ll understand if you think there’s a little more to it than just slutty costumes and sugary treats."
    i "Or, alternatively, those may be the {i}exact{/i} reasons you like it, and there won’t be anything more to it in your eyes either."

    if bonus == True:
        s "I think...Halloween is the ideal time for me to be the lecherous, cynical observer I was born to be."
    else:
        s "You know, as someone who dabbles in sewing, I just really appreciate the detail of finely crafted costumes. That's why I like Halloween so much."

    scene ioyuminight2
    with dissolve

    i "So it’s the costumes and {i}not{/i} the sugar that does it for you. Got it."

    if bonus == True:
        s "I don’t think that should come as much of a surprise."
        i "It doesn’t. I mean, I’ve more or less figured out what you place at the top of your priority list by now."
        s "And you still invite me outside to be alone? Brave move."
    else:
        s "Right."
        s "I hope that you can grow to accept that part of me, Io."

    scene ioyuminight3
    with dissolve

    i "You don’t have to like {i}everything{/i} about a person if you’re going to...you know, {i}like{/i} them."

    if bonus == False:
        s "=/"

    i "Sometimes you just get desperate and settle for less than the complete package because you realize the bundle you’re looking for just...doesn’t exist."
    i "Or maybe it’s discontinued or something. I don’t know."

    if bonus == True:
        i "But it’s not like I’m going to like you any less for fantasizing about girls in slutty outfits."
        i "For a lot of people, that’s the only way they can find value."
        i "They give up on themselves and put their body on display like some sort of perverted art exhibit and wait patiently as all sorts of people approach them and make their offers."
        i "Which, then, allows us to separate them into two {i}more{/i} categories."
        i "Those willing to {i}accept{/i} offers...and those too scared to do so. "
        i "Or, I guess there’s a third category as well in the fact that some people are just seeking the sort of validation you can only get from knowing you got someone to orgasm."
        i "But those people are the worst of the three, and even knowing they exist is enough for me to write off their presence on this stupid, boring planet."

    "So, it appears that it’s going to be another night of depressing observations (Light on the self-loathing) after all."
    "That’s fine, though."
    "This is her default state. "
    "And if the pattern is going to break, there needs to be something or {i}someone{/i} who personally breaks it."
    "Io is far too tired of moving to ever break anything on her own."

    s "I don’t have a wordy response for you or anything, but I’m glad that the type of person I am hasn’t been enough to push you away yet."

    scene ioyuminight4
    with dissolve

    i "So am I."
    i "Sure, I know that a lot of it might just be me intentionally fusing into you the way an anglerfish would while mating."
    i "Do you know about that? How the males are just parasites who just feed off the females’ nutrients after fusing with them and turn into little, fishy sperm factories?"
    s "Correct me if I’m wrong here, but are you calling yourself a...fish sperm factory right now?"

    scene ioyuminight5
    with dissolve

    i "Heheh..."
    i "Even that might be a little generous."
    i "At least the female in the anglerfish scenario has something to gain from the presence of a parasitic male."
    i "What do you gain from me?"
    i "And, if I attach myself to you, much like I already have...how will your life become better?"
    i "I have nothing of value for you, Sensei. I have nothing to give."
    s "You don’t have to {i}give{/i} me anything."
    s "We’re not fish. And I certainly don’t intend to reproduce with you."
    i "Well...that’s a relief, at least."

    scene ioyuminight6
    with dissolve

    i "Thanks for following me out here, by the way."
    i "I thought that after not really making an effort to hang out with me at the beach, you’d already gotten bored or something."
    i "But I realize now that it was probably just me overanalyzing things and thinking I was higher up on your list of people to spend time with than I actually am."
    s "That weekend felt like it just kind of flew by anyway. We’ll hang out more soon."
    i "Amusement park? I’m contractually obligated to ask at this point."
    s "I don’t remember ever signing this contract."

    scene ioyuminight7
    with dissolve

    i "That’s cause there was never a signature involved. "
    i "You “signed” it when you held my hand underneath the stars just blocks away from where I waste away my youth."
    i "Blocks away from where you walked into my life. "
    i "First, with a random blonde. Then, with my best friend."
    i "But now...you come there for me."
    i "And once an anglerfish fuses with its partner, it stays there for life. "
    i "Even when you get tired of me feeding off of your energy because I’m too weak to find any on my own...even then, I won’t leave you."
    i "So do whatever you want with me in complete disregard for what I want myself and-"

    scene ioyuminight8
    with dissolve

    i "Wait, why do you look so exhausted all of a sudden? Am I talking too much again?"
    s "I’m just trying to figure out what the rationale behind tonight's suspiciously composed breakdown is."
    i "Umm...a cry for attention because I waited all night in your room at the beach for the chance to see you only to go home empty handed?"
    i "A desperate plea for a reason to wake up tomorrow disguised in the form of an education lecture of deep sea fish?"
    i "You can spin this any number of ways, but it really won’t wind up detracting from how strange it is on a sheer conceptual basis- no matter which way you go with."
    i "Also, I’m terrified that you’ll stop being attracted to me if I don’t do anything to put myself out there the way that gyaru or the annoying green-eyed soccer player do."
    i "There wasn’t really a reason for me to drop that part in there, but I’m on a roll tonight, so yeah. Just gonna get that out of the way."

    if bonus == True:
        s "The costumes aren’t what make me attracted to people, Io. I’ve already told you I’m attracted to you before."
    else:
        s "This is getting kind of weird and I want to go back inside and drink fruit punch with all of my friends."

    scene ioyuminight9
    with dissolve

    if bonus == True:
        i "I know. But the average train of events in the case of you being attracted to me would lead to you wanting to take things further. "
        i "And without me ever making an effort to actually {i}do{/i} that, the attraction you have toward me might begin to fade."
        i "We already know I serve no purpose in simply being around you. So if your attraction, or the last beacon of hope in the soon-to-be warzone that is our relationship, goes away...what’s left?"
    else:
        i "I know. But without me ever making an effort to actually {i}talk{/i} to you like this, I can't expect to ever grow any closer to doing the hug thing."

    s "I wouldn’t say you haven’t made an effort. "

    scene ioyuminight10
    with dissolve

    i "I would."
    i "Liking someone is confusing for someone like me."
    i "There are all of these things that someone like you would call childish floating around inside of my head, like...wanting to hold hands. Or wanting to rest my head on your shoulder."

    scene ioyuminight11
    with dissolve

    i "But..."
    i "Anything more than that is just..."

    if bonus == False:
        s "Wait, but hugs would count as more than that and you just said-"

    y "Hm? The fuck you two doing out here?"

    scene ioyuminight12
    with dissolve

    "The conversation screeches to a halt as Yumi, once again, shows up to the Halloween party fashionably late."

    if bonus == True:
        "And, just like with Io here, her anti-costume policy reigns supreme in keeping me at the same level of lewd fantasization I always am regarding her."

    scene ioyuminight13
    with dissolve

    y "This guy harassin’ you?"
    s "Yumi, come on."
    y "Ain’t talkin’ to you, dick. Talkin’ to...whatshername."
    i "Io Ichimonji."
    y "Right, yeah. Weren’t we supposed to fight for the dorm war or whatever the fuck that was?"
    i "The contest was just about avoiding being {i}in{/i} the contest."
    y "Oh, right. Yeah. That shit sucked."
    s "Yumi, would you mind letting the two of us-"

    scene ioyuminight14
    with dissolve

    i "Actually! Uh...I should probably go eat something."
    i "I took some anxiety meds before I came here and I’m not really supposed to be doing that on an empty stomach."
    i "Anyway, sorry for being really confusing and probably making you like me less. Please forget anything I said that may have pushed you in that direction and...remember that I..."
    i "Nevermind."
    i "See you."

    scene ioyuminight15
    with dissolve

    s "…"
    y "The fuck?"

    scene ioyuminight16
    with dissolve

    y "How the hell’d you manage to scare away a girl that’s not me? Thought that shit just...never even happened to you."
    s "I think you’re the one who scared her away. Everything was fine until you showed up."
    s "Well, maybe “fine” is the wrong word. But it was certainly better than it is with her just...not being here, I guess?"

    scene ioyuminight17
    with dissolve

    if bonus == True:
        y "Well, gee. Sorry for {i}showing up{/i} and preventing you from adding one more notch in your fuckin’ belt."
    else:
        y "Well, gee. Sorry for {i}showing up{/i} and preventing you from adding one more notch in your hug belt."

    y "Shit’s gonna get so heavy soon enough that you’ll need a second belt to even hold that one up."
    s "That aside, Chika was looking for you earlier. She said you wouldn’t text her back or something."

    scene ioyuminight18
    with dissolve

    y "Yeah. About that."
    y "Chinami wanted to fill up the pool again and the fuckin’ twerp dropped my phone into the water."
    s "I knew that girl was secretly evil."
    y "It wasn’t a big deal or whatever since I’ve heard that you can just put it in rice to fix it as long as you do it quick, but then I had to wait for the rice to cook and it was a whole fuckin’ thing."
    s "You-"
    s "You’re not...supposed to {i}cook{/i} the rice, Yumi..."

    scene ioyuminight19
    with dissolve

    y "What? You bein’ serious right now?"
    s "You’re supposed to use uncooked rice so it can absorb the water..."
    y "…"
    s "You really didn’t know that?"

    scene ioyuminight20
    with dissolve

    y "Wha...How the fuck was I supposed to know that when I didn’t have a phone to look it up?!"
    s "Oh my god..."
    y "What?! I can’t be the first person to make that mistake! "
    s "I’m going to have to buy you a new phone now, aren’t I?"

    scene ioyuminight21
    with dissolve

    y "You don’t have to do shit. I’m not your fucking...girlfriend that you need to buy presents for or whatever. I’m my own person and I’ll figure it out."
    s "Oh, right. That reminds me. "
    s "I have something for you."

    scene ioyuminight22
    with dissolve

    y "What?"
    y "You...do?"
    s "Yeah. Hold on."

    scene ioyuminight23
    with dissolve

    "I reach into my blazer and pull out the package that Yuki handed me earlier."
    "I still have no idea what’s inside of it, but it was light enough for me to forget about it until being reminded, so it’s probably just a shirt or scarf or something like that."

    y "What the?..."
    y "Why?..."
    s "Hm? It’s your birthday, isn’t it?"
    s "There aren’t many days of the year that it’s normal to get presents, but I’d imagine that today is one of them where you should make an exception."
    y "But..."
    y "You and me...we’re..."
    s "Oh, sorry. This isn’t from me. I didn’t get you anything."

    scene ioyuminight24
    with dissolve

    y "Huh?"

    "Yumi snatches the present from me as I take a step back to give her room to open it."
    "I probably should have prefaced this exchange by saying from the start that the gift was from her mother, but it’s out of my hands now."
    "Like, literally. I am no longer holding onto the present."

    s "Remember how I told you your mom was working at a bar now?"
    y "…"
    s "Well, she managed to scrounge up enough to get you this, I guess."
    s "I saw her earlier when I went to pick up decorations with Sana and she asked me to give it to you."
    y "…"
    s "I have no idea what’s inside, but-"

    scene ioyuminight25
    with dissolve

    y "Just go."
    s "…"
    y "…"
    s "Yumi, if you want me to get you something-"

    scene ioyuminight26
    with dissolve

    y "I don’t! Now get the fuck away from me!"
    s "…"
    y "Now!"

    scene black
    with dissolve2

    s "Okay."

    "I turn around to head back to the party, leaving Yumi on her own."
    "The same way she always is."
    "………"
    "……"
    "…"

    scene ioyuminight27
    with dissolve

    y "…"
    y "…"
    y "…"

    scene ioyuminight28
    with dissolve

    y "{i}*Sniff*{/i}"

    scene ioyuminight29
    with dissolve

    y "…"
    y "…"
    y "…"

    scene ioyuminight30
    with dissolve
    play sound "waterdrop.mp3"

    "{i}*Plop*{/i}"

    scene black
    with dissolve2
    stop music fadeout 6.0

    $ renpy.end_replay()
    $ halloweentwo5 = True
    $ yumi_love += 1

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    play sound "phonebeep.wav"
    "{i}You've received a new picture message from Haruka!{/i}"

    jump amilust20intro

label amilust20intro:
    scene amilusttwenty1
    with dissolve2
    play music "amiamiami.mp3"

    a "Sensei, what the heck is going on?! "
    a "This is the second time in a row a girl has invited you outside and then immediately come back in looking all sad!"
    a "You’ve barely even spent any time at the party! You’re not giving me enough chances to be cute around you!"
    s "Yes, god forbid you spend any less than 50%% of the day trying to show me how cute you are."
    s "Besides, I’m sure both Noriko and Io are fine now. Neither situation was a really big deal and I am now ready to get back to mingling."

    scene amilusttwenty2
    with dissolve

    a "It’s hard to tell with Io since she always looks mostly the same, but I really don’t think Noriko is doing too well after whatever it is you guys talked about."
    a "I tried asking her what was wrong a few minutes ago while you were outside and she just looked at me and then ran off to the bathroom."
    a "You didn’t say anything mean to her, did you?"
    s "Since when do you care so much about Noriko?"
    a "Since...I don’t know?"
    a "I guess I don’t really care any more about her than I do my other friends, but she’s always nice to me...so the least I can do is be nice back."
    s "Then you probably should have chased after her instead of waiting for me to come back inside."

    scene amilusttwenty1
    with dissolve

    a "I was gonna! "
    s "But?"

    scene amilusttwenty3
    with dissolve

    a "Well...Ayane’s house has a lot of hallways and if I wound up getting lost, I’d prefer to get lost next to you..."

    scene amilusttwenty4
    with dissolve

    a "B-Besides! There’s not really anything I can do for Noriko! Especially if it’s something involving you!"
    a "And...also! If it {i}is{/i} something involving you and I’m there for it, I can make sure she doesn’t use the opportunity to make any dirty moves and try stealing you away from me!"
    s "You’ve certainly thought a lot about this for something that happened just a short while ago."

    scene amilusttwenty5
    with dissolve

    a "What should we do, Sensei?"
    a "If she really {i}is{/i} sad, we can’t just leave her crying her eyes out in the bathroom. We’ve gotta do something."
    s "Well...at least it’s not outside this time. I haven’t even had time to get adjusted to the heat in here because of how often I keep getting pulled away."

    scene amilusttwenty2
    with dissolve

    a "You’ll come with me, then?"
    s "Sure. Which way did she run off to?"
    a "Down that hallway behind you. But that hallway turns into another hallway. And there are more hallways that you can get to from {i}that{/i} hallway."
    s "So what you’re saying is that we’re about to get very lost."

    scene amilusttwenty6
    with dissolve

    a "Yeah! Like I said, that’s why I waited for you."
    a "Of course I wanna help Noriko, but not if it means I wander into some secret trap all by myself or something and never see you again."
    s "Just...show me which direction she ran off in and I guess we’ll...go fix someone’s broken heart or something."
    a "On it!"

    scene black
    with dissolve2

    "Do I expect a trip to the bathroom with one of Noriko’s biggest rivals to help her get over her sudden increase in anxiety even the slightest? Of course not."
    "But if she really is still crying about this, I should probably do something."
    "I don’t want {i}anyone{/i} crying for an extended period of time. And while I know that sounds extremely thoughtful and generous of me, it really isn’t."
    "Noriko is an important figure in my life- just like...what do they call themselves again? The Sensei Love Squad?"
    "The girls that are always at my house."
    "They’re all important to me."

    if bonus == True:
        "Now, I just have to figure out how to talk about this without letting Ami realize that I recently fingered her favorite idol and role model."
        "But, if you really think about it, none of this would have ever happened if Niki didn’t steal my shirt."
        "This really is all her fault."
    else:
        "I really hope that they live happy, peaceful lives after college."

    scene amilusttwenty7
    with dissolve
    play sound "knock.mp3"

    a "Noriko, are you in there?"
    s "Wow. That sounded just like you were knocking on an actual wooden door."
    a "Shh. I think I heard something."
    s "…"
    a "…"
    a "Okay, maybe not."
    s "Now what, then? Do we just...go back to the party and call this mission a failure?"

    scene amilusttwenty8
    with dissolve

    a "No way! We can’t quit now! Not until we find her!"
    s "But...she’s not here?"
    a "Then we’ll check another bathroom! Rich people always have a crazy amount of bathrooms, don’t they?!"
    s "...Maybe?"

    scene amilusttwenty9
    with dissolve

    a "Onward, [uncle]! To the next bathroom!"
    s "…"

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene amilusttwenty7
    with dissolve
    play sound "knock.mp3"

    a "Norikoooo? Helloooo? "
    a "If you’re in there and you’re feeling sad, now is a good time to tell us because my legs are getting tired!"
    s "We’ve only walked down two hallways, Ami. You’re being dramatic."

    scene amilusttwenty9
    with dissolve

    a "No I’m not! That’s already more hallways than our house has! I’m not used to this!"
    s "Well she’s clearly not here either, so we might as well try another one."

    scene amilusttwenty10
    with dissolve

    a "Hah...yeah...I guess so..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene amilusttwenty11
    with dissolve
    play sound "knock.mp3"

    a "Uhh...Noriko?"
    a "Is {i}this{/i} the one?..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene amilusttwenty12
    with dissolve
    play sound "knock.mp3"

    a "Hello?...Anyone home?..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene amilusttwenty13
    with dissolve
    play sound "knock.mp3"

    a "Noriko! Where the fuck are you and why does this house have so many identical bathrooms?!"
    s "Ami, this might be a strange question, but you’re sure these have all been {i}different{/i} bathrooms, right?"

    scene amilusttwenty14
    with dissolve

    a "What do you mean?"
    s "I just mean that...isn’t it possible we’ve been going in circles?"
    s "We’ve been walking around these halls for like ten minutes now and have seen like...twenty identical bathrooms."
    s "What if we’re just...circling back around to the same one over and over again?"

    scene amilusttwenty15
    with dissolve

    a "Hah...you’re right..."
    a "This is pointless."
    a "I think I understand now why you never try to do anything nice for anybody. This is exhausting and we haven’t even {i}found{/i} Noriko yet."
    s "I’m telling you, she’s probably fine. "
    s "Noriko’s strong and independent and...whatever. Even if she’s freaking out about me and her sister right now, she’ll calm down soon enough."

    scene amilusttwenty16
    with dissolve

    a "Wait, did something happen with you and Niki? Is that why she was crying?"
    s "Nope. I never said that."
    a "But I just-"
    s "Nope. Time to get back to the party."

    "If we can even find our way back at this point..."

    scene amilusttwenty17
    with dissolve
    play sound "knock.mp3"

    a "Norikoooooo, come onnnnnnnn..."
    s "Knocking on the same door more times isn’t going to just make her appear, Ami."
    a "I know that...but this is such a boring ending to what I thought was going to be a fun Halloween adventure."
    s "I agree. But at least you got to spend it with me. I’m sure that should hold you over for the rest of the night, right?"

    scene amilusttwenty18
    with dissolve

    a "Can you kiss my hand? It hurts from all of the knocking."
    s "I can not."
    a "Do you hate me now? Is that what’s happening here?"
    s "I do not."

    scene amilusttwenty19
    with dissolve

    a "Darn it..."

    "Ami stops knocking for a moment and rests her arm against the door of one of many identical bathroom stalls we’ve encountered tonight."
    "And given that she spends most of her free time either reading manga or watching TV with Ayane, it’s probably safe to say this is the most exercise she’s gotten in a while."

    if amifingered == True and bonus == True:
        "Well, non-sexual exercise, at least. "
        "But I feel like counting all of that stuff is a little unfair since she is known to get quite into it."

    scene amilusttwenty20
    with dissolve

    a "Um...Sensei?"
    s "Yeah? What’s up?"
    a "Do you..."
    a "Do you maybe want to..."

    if ami_lust >= 20:
        jump amilust20
    else:
        s "…"
        a "…"

        scene amilusttwenty21
        with dissolve

        a "A-Actually...don’t even worry about it!"
        a "It was just going to be a stupid suggestion anyway."
        s "What? If there’s something on your mind-"

        scene amilusttwenty22
        with dissolve

        a "There’s not! Let’s just...try and find our way back to the party before we have to spend the rest of our lives in different bathrooms."
        s "Oh. Uhh...sure. "
        s "After you, then."

        scene black
        with dissolve2
        stop music fadeout 20.0

        "Ami exits the bathroom and we wind up confirming that they really were all different rooms and that we weren’t just going in circles."
        "Of course, we’re far too lost at this point to be able to find our way back, so she winds up texting Ayane asking for directions."
        "I’m not sure how she managed to do it, but Ayane figured out where we were right away and set us back on the path toward junk food and costumes I do not recognize, but appreciate greatly."
        "It’s unfortunate that we weren’t able to find Noriko, but..."
        "I’m sure that wherever she is, she’s doing okay..."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ amilust20skip = True

        jump halloweentwo6

label amilust20:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
to "Heheh! It may come as a surprise, but the truth is that I absolutely adore both Halloween {i}and{/i} horror!"

    "Doesn’t Sana like horror films too?"
    "Wait..."
    "Sana and Touka both need new friends..."

    s "…"

    "I feel like I’m so close to figuring something out, but I can’t put my finger on what it is..."

    ya "Touka? Can I ask you a question?"

    scene norikosadhalloween33
    with dissolve

    to "Of course, Yasu! Whatever do you require?"
    ya "What is “Halloween?”"
    to "…"
    ya "…"
    u "Sensei!"

    scene norikosadhalloween34
    with fade

    s "Thank you for always showing up exactly when- oh my god, you are adorable."

    scene norikosadhalloween35
    with dissolve

    u "Nyaa~"
    i "Please kill me."
    s "You should have dressed up too, Io."

    scene norikosadhalloween36
    with dissolve

    i "Why? Halloween is just one more holiday on the long list of consumer-unfriendly, corporate scams exacted for the sole purpose of profiting off of people who don’t know any better."
    i "It’s not only damaging to the lower middle class and anyone else who feels pressured to participate in the name of inclusion, but fundamentally silly and, as far as I’m concerned, a waste of time."
    i "Besides, this isn’t even how we celebrate Halloween in Japan. We should all be getting drunk and sauntering across Shibuya crossing right now. "
    s "Molly? I found you another drinking partner."

    scene norikosadhalloween37
    with dissolve

    u "{i}Hisssssss...{/i}"
    i "Don’t worry, Uta. I don’t think any less of you for feeding the money you make off of conning people into multi-billion dollar corporations who don’t care about whether you live or die. "

    scene norikosadhalloween38
    with dissolve

    u "{i}HISSSSSSSSSSSSSSSS!!!{/i}"
    i "Awwww, I love you too~"
    s "Where can I file adoption paperwork? I suddenly want a pet."

    scene norikosadhalloween39
    with dissolve

    u "This kitty’s not up for adoption, nyaa~"
    u "But if you’re still interested in providing a forever home for a cute lil’ fuzzball, may I interest you in our latest kitty over there to your left?"

    scene norikosadhalloween40
    with fade

    s "To my-"
    t "…"
    s "…"
    t "Prepare to die, bro."

    scene norikosadhalloween41
    with dissolve

    u "No, no, Tsunecchi! You’ve gotta add “Nyaa~” to the ends of your sentences. How else will anybody know you’re supposed to be a cat?"
    t "I apologize. I thought the cat paws, cat tail, and cat whiskers would have given it away."
    t "I understand now, the error of my ways."

    scene norikosadhalloween42
    with dissolve

    u "Still lookin’ for a little friend to take home and cuddle up with, nyaa?~"
    u "This one might take a little while to warm up, but she’ll be sittin’ in your lap and purrin’ her heart out before you know it, nyaa!~"
    s "I’m in. Ami is going to be so happy that we finally have a cat."
    t "Nyaaaaat a chance, bro."

    scene norikosadhalloween43
    with dissolve

    u "Uhh...Almost, Tsunecchi. We’ll get you there."
    t "I thought my purrrrrformance was purrrrrrfect, nyaa~"
    i "Oooookay, I’m gonna step outside before I get diabetes."
    i "Wanna come with me, Sensei?"
    s "Sure. I’ve already been pulled outside once today. One more time won’t hurt."

    scene black
    with dissolve2
    stop music fadeout 20.0

    $ renpy.end_replay()
    $ halloweentwo4 = True

    jump halloweentwo5
...
```