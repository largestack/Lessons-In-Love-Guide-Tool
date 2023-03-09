# 1999 PC Classic, Rollercoaster Tycoon
Io event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=iospecial30&go=Go)



## Event preconditions
❌Event "[Uta: After the Rain](./utamaid25p2.md)" is completed (event=utamaid25p2)

✅Day of week is Saturday

❌Event "[Io: Heartbreak & Harmony](./iodorm25.md)" is completed (event=iodorm25)



## Next events
* [Tsukasa: National Tsukasa Day](./tsukasaspecial1.md)

## Event properties
* ID: iospecial30
* Group: Io
* Triggered by label: saturdaymorning
* Triggered by branch label: saturdaymorning

## Event code
File: \game\IoEvents.rpy
Code:
```python
...
label iospecial30:
    play music "phonering.mp3"

    s "..."
    s "..."
    s "..."

    "I wake up to the sound of my phone ringing and the day quickly gets off to a rocky start."
    "Thankfully, phones can’t ring forever. So any second now, this is going to stop and things are going to return to the way they should be at..."

    s "7:00 AM..."

    stop music
    play sound "phonebeep.wav"

    "I press a button to ignore the call and-"

    play music "phonering.mp3"

    "Oh, come on."

    stop music
    play sound "phonebeep.wav"

    s "Hello?"

    play music "acoustic.mp3"

    i "Hi! Did I wake you?"
    s "Yes. Goodbye."
    i "Wait, don’t hang up yet! I have awesome news!"
    s "Can the news not wait until, like...two hours from now?"
    i "I mean, it probably {i}could.{/i} But do I really seem like the type with enough self control to be able to abstain for that long when there’s something I clearly want to tell you about?"
    s "Nope. Anyway, talk to you later."

    play sound "phonebeep.wav"

    "I hang up the phone and-"

    play sound "phonering.mp3"

    "You’ve gotta be fucking kidding me."

    scene bedroom_day
    with dissolve
    play sound "phonebeep.wav"

    i "Stop ignoring me and let me share my awesome news with you! If you still don’t think it’s awesome, you can ignore me forever and forget we ever even met."
    i "Except not really because my self-esteem is already pretty horrible and a blow like that would be the final nail in the coffin that is Io."
    s "Just tell me what the news is."
    i "I don’t have to work today!"
    s "..."
    i "Awesome, right?!"
    s "Is that seriously it?"
    i "Pretty much, yeah!"
    i "But it’s {i}because{/i} of that that I figured you and me could spend some time together! If that’s not too presumptuous and you don’t already have other plans, which I figured you might."
    i "But that’s just one of several reasons I’m calling you as early as this! I didn’t want someone else beating me to the punch and stealing you away before I even get a shot."
    s "I’m surprised you’re actually the one reaching out to {i}me{/i} this time when I’m pretty much always the one who finds you first. But I guess your reasoning makes sense."
    i "Hey, the only reason I don’t call you more often is that I’m still like 85%% sure you’re only pretending to like me. But Uta says I should be more assertive if I’m ever going to get what I want, so hi."
    i "Anyway, can we hang out? I have something for you."
    s "You do?"
    i "Yes. Well, kind of. I found it at a garage sale. But you’ll love it. Maybe. Or not. Probably not, now that I think about it. But I will, so I still want to give it to you."
    s "Just come over. I’m pretty sure Ami has work today."
    i "Come...come over? Like...to your house?"
    s "Yes. But I’m going back to sleep until you get here, so goodbye."
    i "Wait! I don’t know where you live!"
    s "Ask Uta."
    i "Why does Uta know where you live?!"

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "I hang up the phone and collapse back onto the bed."
    "I’m not sure if I’m going to be able to get any sleep now that I’ve been torn from my slumber for more than five minutes, but it’s worth a shot."
    "And hey, if Io lacks the self confidence or assertiveness to come over here (Which I figure there is a 50%% chance she will), I’m sure that just staying in bed will be enough to at least partially rejuvenate me."
    "I close my eyes, unsure of how the day is going to proceed..."

    scene bedroom_day
    with dissolve2
    play sound "doorbell.mp3"

    "But when I open them roughly two hours later to the sound of my doorbell being repeatedly pressed, I figure it out."

    play sound "doorbell.mp3"

    s "..."

    play sound "doorbell.mp3"

    s "..."

    play sound "doorbell.mp3"

    s "Well, at least she gave me an extra two hours."

    scene black
    with dissolve2

    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene iocomesover1
    with dissolve2

    i "Wow! It’s just as normal as I thought it would be!"
    s "Thank...you?"
    i "Ooooh, and your TV is huge! Do you get all of the sports channels? Or any of the American ones?"

    scene iocomesover2
    with dissolve

    i "Well, not like we’ll have any time to watch anything anyway. Not with what I’ve got planned for the two of us."
    s "Oh?..."
    i "You know it."
    i "Are you ready for the ride of your life, Sensei?"
    s "If I knew that’s what you were calling about, I wouldn’t have asked you to wait two-"

    scene iocomesover3
    with dissolve

    i "Because it’s time for the 1999 PC classic, Rollercoaster Tycoon!"
    s "..."
    i "Sweet, right?"
    s "..."

    scene iocomesover4
    with dissolve

    i "What’s wrong? Are you not interested in the 1999 PC classic, Rollercoaster Tycoon?"
    s "Are you going to refer to it by that lengthy title every time?"
    i "It’s a relic of the past. I thought repeatedly saying its release year might unlock some core memories for you that lead to the two of us playing it until it gets dark and I have to go home."
    s "I’m not that interested in video games, Io."
    i "Not even the 1999 PC classic-"
    s "Not even the 1999 PC classic, Rollercoaster Tycoon."

    scene iocomesover5
    with dissolve

    i "But I spent like 500 yen on this!"
    s "That’s not even that much."
    i "Also, you still haven’t taken me to an amusement park so it’s very considerate that I would bring the amusement park to {i}you{/i} instead! This is significantly cheaper and only like, three degrees less fun!"
    s "I mean...I {i}guess{/i} we can play if you’re that excited about it. But are you really content with just spending all of our time together playing video games? "

    scene iocomesover6
    with dissolve

    i "Yeah."
    s "There’s nothing else you’d rather do instead?"
    i "Not really."
    i "Everything else sounds exhausting. And every time Uta and I have played games like this together, it’s been a total blast."
    s "There’s {i}really{/i} nothing you’d rather do?"
    i "Nope."
    s "{i}Nothing?{/i}"

    scene iocomesover7
    with dissolve

    i "You’re being a real creep today, Sensei."

    "I sigh to myself and think back to what Uta said at the love hotel the other day."
    "And while I’m still not sure exactly how accurate that assessment of hers is (Ignoring the fact that she probably knows more about Io than I do), I’m not about to just come out and {i}ask{/i} Io about it."
    "If she wants to play the 1999 PC classic, Rollercoaster Tycoon, then..."
    "Well, I guess the two of us are going to play the 1999 PC classic, Rollercoaster Tycoon."

    scene black
    with dissolve2

    i "Oh! Which one is your room? I don’t want to accidentally walk into Ami’s and have my eyes singed by how pink and girly everything probably is."
    s "It’s the one on the left."

    play sound "dooropen.mp3"

    i "Cool! That means- ah! My eyes! They burn! You lied to me!"

    "I lead Io to my {i}actual{/i} room after destroying her eyesight, which she takes as an invitation to immediately run up to my table and start playing with my things."

    scene iocomesover8
    with dissolve2

    "Granted, she is the one who {i}created{/i} the thing she is currently playing with. But still, touching other peoples’ belongings is rude."

    i "You kept it! You kept it and didn’t throw it in the trash even though it was made by a trash person who previously put and is currently putting her trash hands all over it!"
    s "I wouldn’t just throw away something you made for me."
    s "Even that wardrobe thing is still around here somewhere. I just had to move it out of the bedroom since it was taking up way too much space."
    i "That’s fine! A 50%% success rate combined with a 0%% garbage rate is way better than I thought I’d get, so thank you!"
    i "How you doing, little guy? Is Sensei treating you well? "
    i "Have you seen him doing anything weird under the blanket? Or does he make you turn away for that?"
    s "Please don’t talk to my robot that way."

    "Not after the things he has seen..."

    scene iocomesover9
    with dissolve

    i "Can he play with us? He is technically one of my offspring, so there’s no way he doesn’t also enjoy the 1999 PC classic, Rollercoaster Tycoon."

    if robotname.lower() in ["1999 pc classic, rollercoaster tycoon"]:
        s "You know, despite him not being able to talk, I knew from the get-go that he loved that game."
        s "Which is exactly why I decided to name him after it."

        scene iocomesover8
        with dissolve

        i "You didn’t!"
        s "I certainly did."
        i "How are you doing, 1999 PC Classic, Rollercoaster Tycoon?!"
        i "Are you having fun?! Are you having a good time?!"
        s "I also taught him Spanish so he has no idea what you’re saying."
        i "That’s fine. He can just be confused along with the rest of the people who had to go into the code to find this additional dialogue since no one would ever actually name him 1999 PC Classic, Rollercoaster Tycoon."
        s "Anyway, back onto the topic of whether or not he can play-"

    s "I guess. But I have no idea if he’ll enjoy it or not."
    s "Or...if he’s even capable of enjoying anything because he is an inanimate hunk of wood."
    i "For now! But in about 99 years, he’ll be very mad that you said that."

    scene black
    with dissolve2

    "Io takes the robot over to my desk and places him down beside my laptop."
    "Thankfully, the laptop is old enough to still have a disc drive, so Io pops the 1999 PC classic, Rollercoaster Tycoon into the tray and, after an outdated installation screen, she loads up the game."

    scene iocomesover10
    with dissolve2

    "I think to myself as she goes over the basics that this is really similar to the way Niki acts whenever she comes into my room."
    "The only difference is that I don’t [[yet] have an extensive sexual history with Io and that she actually tries to include me rather than just seizing my things for her own personal gain."
    "We play for an hour or two. And when I say {i}we{/i}, I mean {i}me-{/i} as Io vehemently refuses to play at all in favor of trying to get me addicted."
    "And while her efforts are in vain for the majority of time I spend pressing buttons on this rectangular machine, I do begin to reevaluate that when she begins teaching me the {i}secrets{/i} of this game."

    i "So, yeah. If you just delete parts of the tracks on your rollercoasters, you can send all of your guests flying to their deaths."
    i "What I like to do is position them so that the carts go flying into the water, causing everyone to drown."
    i "It’s kind of like how in the 2000 PC classic, The Sims, you could delete the ladder on your swimming pool and laugh as all of the characters you created slowly drown to death."
    s "Why are you so experienced when it comes to games that existed before you?"
    i "Because I am a contrarian and refuse to live the same type of life as my peers, electing to instead participate in activities that others would call outdated or boring so no one tries to connect with me."
    i "Oh. And there’s also a Zoo Tycoon where you can make lions eat all of your guests."

    scene iocomesover11
    with dissolve

    s "I think you might have a problem."
    i "Sensei, if it weren’t for outlets like this where I can get all of my inner rage out in peace, I would probably be in jail for literal murder."
    s "I highly doubt you’d have the resolve to actually kill someone."

    scene iocomesover12
    with dissolve

    i "Well, thanks to extremely outdated PC hits, we’re probably not going to find out any time soon."
    i "Besides, going to jail would mean that I don’t get to spend time with you anymore. And days like this are quickly becoming my favorite reason to continue existing."
    s "I’ll admit this isn’t as bad as I thought it would be."
    s "Still probably not how I’d choose to spend my time, though."

    scene iocomesover13
    with dissolve

    i "Well, we’ve done what I’ve wanted to do for like, two hours already. So if there’s something you had in mind, we could try that instead."
    i "As long as it doesn’t involve going out, because there is no way I’m going to be into that today. Or...any day."
    i "Unless you’re absolutely insistent that we should. In that case, I’d probably make an exception. But even then, I’d only be pretending to be okay with it in order to make you happy."
    s "I wish you’d learn to be antisocial in fewer words."
    i "Me too. Incessant self deprecation can be really tiring."

    scene iocomesover14
    with dissolve

    s "Anyway, I didn’t have any concrete plans. I just figured that whatever was going to happen in here would involve a little less murder and a little more...intimacy."

    scene iocomesover15
    with dissolve

    i "Oh...Hahah...Yeah..."
    i "Yeah, I...I don’t know. It’s just...still my first time over and..."
    i "You know, just barging into your room to play games without really thinking about any of the consequences or how that would look is starting to sound like a pretty amateur move."
    s "You were excited. It happens. Besides, for someone who spends virtually their entire life {i}thinking,{/i} you kind of suck at it. So this is to be expected."
    i "Yeah. You’d think that after years and years of repeated failure and endless misery that maybe my brain would self-correct and cause me to act a little less shitty, but alas."
    i "Is, uhh..."
    i "Is...{i}intimacy{/i} really your go-to when people come over here, though? Cause, like...there’s no way I’m the first, right?"
    s "You’re the first girl to ever come into this room, Io."

    scene iocomesover16
    with dissolve

    i "Can you at least make your lies sound {i}a little{/i} convincing so I can trick myself into believing them?"
    s "You were going to beat yourself up no matter what I responded with right there. I know you. Avoiding that topic entirely is the best way to prevent that from happening."

    scene iocomesover17
    with dissolve

    i "I mean...we don’t have to {i}avoid{/i} it. Avoiding things makes stuff awkward. And if we keep avoiding stuff, we’ll wind up just sitting here in silence for the rest of the day and that sounds like it would bore you."
    s "I can turn the game volume up. At least it wouldn’t be silent then."

    scene iocomesover18
    with dissolve

    i "J...Just for clarity’s sake, what did you mean by “intimacy?”"
    s "..."
    i "Should I not have asked that? Did I just make a mistake?"
    i "Because different people have different definitions of that word and I think I might just be misinterpreting {i}your{/i} definition of it and turning this into a thing when it’s not a thing at all."
    s "Just assume that my definition of the word is whatever {i}your{/i} definition of the word is. That sounds like the easiest way to end this."
    i "If our definitions of that word are the same, then I {i}am{/i} turning this into a thing- because I’d be totally fine with intimacy if it’s like, Io intimacy....Iontimacy. Sorry. That wasn’t funny. Sorry."
    s "Even though we have the same definitions, I feel like I should ask you what your brand of intimacy is."
    i "Uhhhhhh..."

    scene iocomesover19
    with dissolve

    i "Like..."
    i "Cuddling?..."
    i "Or something?..."
    s "Why are you getting so flustered? We’ve “cuddled” in your room several times before, haven’t we?"
    i "Yes...but also no? Never like this, at least. Never in {i}your{/i} room. And never when we’re...so alone."
    s "Are you nervous?"

    scene iocomesover20
    with dissolve

    i "Yes, but only that you’ll realize you don’t want anything to do with me anymore."
    s "That’s not going to happen."
    i "Do you promise?"
    s "Sure. If promising that somehow reassures you, I’ll promise it as often as you want."
    s "I’m not going anywhere. And no, I’m not just saying that because I live here."
    i "You won’t leave even if I’m full of disappointments?"
    s "If I was going to abandon you, I would have done it already. I’m in this for the long haul at this point."

    scene iocomesover21
    with dissolve

    i "The...long haul..."
    s "..."
    i "..."
    s "..."
    i "..."

    scene iocomesover22
    with dissolve

    i "W...Wow! Your bed looks so...comfortable..."
    i "Is it okay if I...lay down on it for a little while to test it out?"
    s "What are you doing?"

    scene iocomesover23
    with dissolve

    i "Oooooh...so...good. Or...soft. Or something..."
    i "If only I...had someone to cuddle with me. Then I’d...{i}really{/i} be able to form a solid opinion on the...marketability of this...mattress..."
    s "Io-"
    i "Yes, I’m awkward! I’m sorry! That was your cue! We played enough of the 1999 PC classic, Rollercoaster Tycoon and now it’s time to do what you want so you won’t hate me!"
    s "I’m not going-"
    i "I also just want to cuddle now and am only saying things like that because it’s too hard to admit and accept the truth!"
    s "..."
    i "What?!"
    s "Nothing. Just thinking that I probably should have asked for three hours instead of two."

    scene black
    with dissolve2

    "I close the laptop and make my way over to the bed, climbing over Io so I can take my place behind her as the big spoon."
    "How things came to this when I already accepted that they {i}wouldn’t,{/i} I have no clue."

    scene iocomesover24
    with dissolve2

    "But I’m glad that they did- for the sensation of this paperthin bundle of contradictions that smells vaguely of blueberry shampoo pressing up against me fills me with my {i}own{/i} set of contradictions."
    "The acceptance I felt just moments ago begins a painful metamorphosis into doubt. But not just the doubt of myself- the doubt of everyone around me."
    "We can not predict the future. And even those who think they know each other most can be hazy on the details if they have not pried in the right places at the right times."
    "Would Uta have been able to predict that Io would not hesitate in calling me to bed?"
    "Would she have been able to predict that her fingers would crawl inside of my sleeve and pull me closer to her?"
    "That she’d trust me so much she’d close her eyes just minutes after hearing about my anticipation and expectation of intimacy?"
    "Of course not."
    "Because Uta doesn’t know Io as well as she thinks she does."
    "But I do."
    "I do, because Io is me."
    "I know what Io wants, because I am Io."
    "We are one and the same- two broken people who have given up on themselves and must now find solace through the embrace of the opposite sex."
    "Would she truly have come here without the expectation that we’d end up like this?"
    "Would she truly give in so easily?"
    "She likes me."
    "She likes me and she wants to be intimate with me."
    "I want to be intimate with her."
    "I want to take her {s}costume{/s} shorts off."
    "I want to be intimate with her."
    "I want-"

    i "This is..."
    i "The most peaceful I’ve felt in a really long time, Sensei..."
    i "I really wish you’d let me be your girlfriend."
    s "..."
    i "..."

    scene iocomesover25
    with dissolve2

    s "Maybe one day."
    i "Sensei?..."

    "She likes me."
    "She likes me and she wants to be with me."
    "I want to be with her."
    "She will tell me to stop if she wants me to stop."

    s "Does this room smell strange to you?"
    i "Does...huh? Strange how?"
    i "Do you not like blueberries? I can wear something else if you-"
    s "It’s like Spring."
    i "Spring?..."

    scene iocomesover26
    with dissolve2

    i "Um-"
    s "Why doesn’t it exist anymore?"
    i "Uhh..."
    s "Why do I remember a season we don’t have?"
    s "Why do I remember the scent of what can not exist anymore?"

    scene iocomesover27
    with dissolve

    i "..."
    s "Why do you think that is?"

    stop music
    play sound "static.mp3"
    scene imissyoumore with flash
    scene iocomesover28 with flash
    stop sound
    play music "allofthesounds.mp3"

    "SHE LIKES ME"
    "SHE LIKES ME AND WANTS TO BE WITH ME"
    "SHE WILL TELL ME TO STOP IF SHE DOES NOT WANT THIS"
    "SHE WILL TELL ME TO STOP"

    scene black
    stop music

    "I WILL NOT STOP"

    play sound "static.mp3"
    scene happy4 with flash
    scene happy2 with flash
    scene happy6 with flash
    scene iocomesover29 with flash
    stop sound

    i "Okay! Uhh...I just remembered that, umm..."
    i "My day off is, uhh...actually {i}tomorrow...{/i}hahah..."
    s "What just-"

    scene iocomesover30
    with dissolve

    i "It’s...It’s fine! Really! It’s not you! I’m just...kind of weird when it...yeah..."
    i "But, uhh...I had a lot of fun today! I’m sorry I had to go and ruin it at the end..."

    scene iocomesover31
    with dissolve

    i "And...uhh..."
    i "It was...a lot of fun and...wait- I already said that."
    i "Uhh..."

    scene iocomesover30
    with dissolve

    i "I love you! Or...umm...like you! Whichever one I said the...last time and..."
    i "And..."
    i "Please don’t hate me..."

    scene iocomesover32
    with hpunch
    play sound "doorslam.mp3"

    "Io runs out of the room."

    scene black

    "I catch up on sleep."

    $ renpy.end_replay()
    $ iospecial30 = True

    "{i}Io’s affection does not increase.{/i}"
    "{i}You scared her.{/i}"

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label saturdaymorning:

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if ((totaldays >= 220) and (day220 == False) and (chap1point >= 90) and (happypoint >= 10 or (happypoint + happymiss == 10)) and (chikapoint >= 13) and
        (yumipoint >= 12) and (ayanepoint >= 18 or (ayanepoint + ayanemiss == 18)) and (sanapoint >= 14) and (makotopoint >= 16) and (mikupoint >= 13) and
        (rinpoint >= 16 or (rinpoint + rinmiss == 16)) and (futabapoint >= 19 or (futabapoint + futabamiss == 19)) and (amipoint >= 14 or (amipoint + amimiss == 16)) and
        (mayapoint >= 12) and (mollypoint >= 6) and (tsuneyopoint >= 6) and (sarapoint >= 5 or (sarapoint + saramiss == 5)) and
        (harukapoint >= 6 or (harukapoint + harukamiss == 6)) and (karinpoint >= 3) and (kirinpoint >= 3) and (kaoripoint >= 3) and (makipoint >= 2) and (chinamipoint >= 2) and (day == 6)):
            jump day220
    if day == 6 and totaldays >= 370 and day355 == True and karindate20 == True and chinamidate20 == True and utadorm20 == True and sanadorm50 == True and osakodojo1 == True and kirindate25 == True and secondbeach1 == False:
        jump secondbeach1
    if totaldays >= 464 and christmastwo20 == True and day == 6 and mayafestival1 == False:
        jump mayafestival1
    if utamaid25p2 == True and day == 6 and iodorm25 == True and iospecial30 == False:
        jump iospecial30
...
```