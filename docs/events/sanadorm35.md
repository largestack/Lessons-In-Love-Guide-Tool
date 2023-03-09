# Waiting for Anything
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm35&go=Go)



## Event preconditions
✅Sana love greater than or equal to 35

✅Event "[Sana: Purest Intentions](./bar35.md)" is completed (event=bar35)

✅Day of week is not Thursday



## Next events
* [Sana: Closer to Me](./bar40.md)
* [Sara: Uptown Girl](./saradate10.md)

## Event properties
* ID: sanadorm35
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm35:
    play sound "knock.mp3"

    "I knock on the door and wait for Sana to answer. "
    "She mentioned at the bar recently (And rather bluntly, if I do remember correctly) that she’s definitely been getting a little jealous of how often the people she's close to bring me up."
    "She also mentioned that she wants to learn karate, but I’m pretty sure that wasn’t true."
    "There is no way I can picture Sana doing karate, even if I close my eyes and rid myself of everything else."
    "Either way, spending more time alone with her is sure to help her feel a little better about our dynamic. "
    "And, who knows?"
    "Maybe we’ll wind up taking another huge step today?"

    ay "SENSEEEEIIIIIII! I KNOW YOUR KNOOOOOOOCK!!!!!!"

    "Or maybe Ayane is here and that won’t happen at all."

    ay "COME ON IN AND *hic* HANG OUT WITH USSSSSSSSS!!!!!"
    sa "Ayane...you don’t have to yell...Sensei is-"
    sar "Sensei!! The door is open!!"
    sar "Come inside!"

    if bonus == True:
        ay "HEH. YEAH SENSEI! {i}COME{/i} INSIDE."

    "And apparently Sara is here as well."
    "It appears that my plan to hang out with Sana away from the prying eyes of her best friend and her mother has...failed in the most dramatic way possible."
    "Also, they’re definitely drunk right now."

    s "…"

    "I’m going in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I push the door open to be immediately assaulted by the scent of white wine and perfume."
    "So basically it just smells like Sara’s room."
    "And that’s okay. It’s not a particularly bad combination of scents, it just..."
    "Well, it’s not something this room normally smells like."

    scene sanadormgirls1
    with dissolve

    sa "Um...hi, Sensei..."
    sa "You picked a...pretty bad night to come here..."
    sar "I think he picked the {i}best{/i} night to come here."

    if bonus == True:
        ay "Yeah. The best night to {i}come{/i} here."
        s "Are you going to pronounce that word the same way all night?"
    else:
        ay "Boooone necklaaaaaace?????????"
        s "What?"

    sar "Don’t question her, Sensei. That’s the best way to pronounce it."

    if bonus == True:
        s "Sara, aren’t you a little too old to be in here?"

        scene sanadormgirls2
        with dissolve

        sar "Aren’t you a little too {i}male{/i} to be in here? This is my daughter’s room, you know."
        sar "If you were looking for mine, you’re a couple miles off."
    else:
        s "Sara, aren’t you a little too old to be in here? Your college days ended long, long ago."

    scene sanadormgirls3
    with dissolve

    sa "Did you...um..."
    sa "Did you need something, Sensei?"
    ay "Course he doesn’t *hic* need anything, Sana. "
    ay "He’s here to look at our pajamas and give us lots of hugs and tell us how *hic* pretty we are."

    scene sanadormgirls4
    with dissolve

    sar "Oh. Well, if that’s the case, it’s fine that you’re here."
    s "You’d be...fine with me coming here to hug your daughter and tell her how pretty she is?"
    sar "As long as you do the same for me, sure."
    sar "Besides, we all know who has the best pajamas here."
    ay "Dass right...Me."
    sar "Obviously, I’m talking about myself. "
    sar "I’ll accept my first hug and compliment now."
    sa "I’m sorry I’m not dressed as..."
    sa "Well...that I’m not dressed like them."
    s "You’re dressed how you’re always dressed for bed."

    scene sanadormgirls5
    with dissolve

    ay "Sensei! Tell *hic* Sana that she should shed some layers!"
    ay "Sara and me are showing some skin and Sana looks like she’s ready for a trip to Antarctica."
    sa "I’d need...a few more layers for Antarctica..."

    scene sanadormgirls6
    with dissolve

    sa "And also...I’m not really comfortable...showing that much of my skin."
    sar "But you’re a spitting image of me and I’m an attractive, totally youthful woman who has yet to pass the age where it’s okay for me to hang out here."
    sa "I really...rather you wouldn’t, though..."
    ay "If *hic* Sara wasn’t here then how would we get the wine?"
    sa "We wouldn’t because we’re...you know..."
    s "I didn’t even know you drank, Ayane."
    ay "Course I *hic* do. Jusssss...not often..."
    ay "But this tastes like the kinda stuff Ami and I snuck out of your liquor cabinet a billion years ago that you never found out about. Remember?"
    s "How would I remember something I never found out about?"
    ay "Idunno. Figure it out, [ayanemaster]."

    scene sanadormgirls7
    with dissolve

    sa "…"
    sar "…"
    s "…"

    scene sanadormgirls8
    with dissolve

    sar "Uhh...anywho- "
    sar "Wanna tell my daughter here to loosen up a little bit?"
    sar "She seems to look up to you and she won’t take off her clothes {i}or{/i} drink tonight."
    sa "Mom!"
    sar "I swear, it’s like she’s not even my daughter sometimes."
    sa "I...I say weird things when I get drunk!"
    sa "I don’t want to wind up...doing something that will make the two of you mad..."

    scene sanadormgirls9
    with dissolve

    sar "Mhm, mhm. But that still doesn’t explain you being all bundled up. You don’t fit in."
    sar "We’re all about body positivity in this dorm, Sana-dear."
    sa "Don’t...make up dorm rules when you...don’t even live here."
    sa "You know I...feel weird when I’m not covered up..."

    scene sanadormgirls10
    with dissolve

    if bonus == True:
        sar "{i}She’s embarrassed because she doesn’t wear a big girl bra yet.{/i}"
    else:
        sar "{i}She's embarrassed because her skin turns translucent for three hours every night.{/i}"

    sa "Mom! Why are you even here?! "
    sa "Leave!"
    sa "Sensei doesn’t want to hear that!"
    ay "What do you *hic* mean he doesn’t wanna hear that? Sensei’s a major hot dog."

    if bonus == True:
        s "I think you mean {i}horn{/i} dog, Ayane."
        ay "No way. The hot dog’s the *hic* wiener lookin’ one, right? Dass what you are."
    else:
        s "Yes. I am food."

    ay "Just a big ole raw hot dog walkin’ all over the place like you *hic* think you’re all that."
    ay "Well *hic* I’ve got one thing to tell ya, buddy."
    ay "You {i}are{/i} all that and I love you very much."
    ay "Gonna *hic* stop talking now. Drank *hic* too much."

    scene sanadormgirls11
    with dissolve

    sa "Are you...trying to make me feel bad?..."
    sar "Of course not, dear. I’m just playing with you."
    sar "If you really want me to leave, I’ll leave."
    sa "Okay...then...leave."

    scene sanadormgirls12
    with dissolve

    sar "Oh. That backfired."
    sar "I didn’t think you were going to actually ask me to leave."
    sa "I don’t want to...but...I don’t want you to make me feel...immature."
    sa "I...I live on my own now..."
    sa "And if I...want to stay covered up...I can stay covered up..."

    scene sanadormgirls13
    with dissolve

    sa "R...Right, Sensei?"

    "What?"
    "Why am I suddenly the deciding factor in this?"

    if bonus == True:
        sa "Tell my...mom that...you’re just here to...talk to us and not...s...strip us."
        sa "And also...forget the...b...bra thing that you just heard..."

        "Unfortunately, I’m not sure if I can successfully do either of those two things."
        "Sana does have a point, though."
        "She’s already been feeling uneasy about how much time I spend with the other two. "
        "And it probably makes her feel even {i}more{/i} inferior with them sitting around half-naked, drinking wine while she’s bundled up in a giant hoodie with a soda."
    else:
        sa "Tell my mom that...you hate translucense..."
        s "..."

        "Sana does have a point. I have never liked translucense."

    s "I just wanted to see what you guys were up to."
    s "And Ayane’s asleep so it’s probably safe for me to say this now, but I wanted to hang out with {i}you{/i} tonight, Sana."

    if bonus == True:
        s "And no, that doesn’t involve stripping."

        "Unless you want it to."
        "Which you don’t, sadly."

    scene sanadormgirls14
    with dissolve

    sa "Wh...what?..."
    sa "You didn’t have to...say that..."
    sa "It’s okay if you came to see Ayane...I...I understand..."
    sar "No..."
    sar "He’s telling the truth. "
    sar "I know that look."
    sar "And as jealous as I am that he didn’t just call me instead, I think I understand."
    s "…"

    "I sure hope she doesn’t actually understand."

    scene sanadormgirls15
    with dissolve

    sar "Obviously, he’s a man, so it’s in his nature to want to protect something."
    sar "And since I’m such an independent, strong woman, he turned to the version of me who has yet to fully bloom since it’s the closest he could come."

    "Oh, good. She doesn’t get it."
    "That level of denial gives me serious Ami vibes, though."
    "Maybe I should worry about Sara?"

    sa "Well...umm...whatever the reason..."
    sa "It makes me really glad...hearing that you came here for me...Sensei..."
    sa "Even if you’re just saying that...because Ayane is asleep..."

    "I’m really not. I can’t help but understand why Sana would think that, though."
    "And even though her mother was wrong in the end, she did raise a good point."
    "Maybe I do have some inherent desire to protect Sana?"
    "In fact, I absolutely {i}do{/i} have something like that. And I’ve known it since I first walked into her bar."
    "But it’s hard to tell how much of that is the result of me simply knowing she {i}needs{/i} protection."
    "Even now, surrounded by the three people she’s more familiar with than anyone else, she feels cornered."
    "Not only by people physically bigger than her (In a number of ways) but by people more emotionally mature and more confident."
    "She’s on the back foot in her very own element."
    "It’s just like how I used to feel insignificant when my-"

    stop music
    play sound "static.mp3"
    scene yumis2
    with flash
    scene sanadormgirls16
    stop sound

    sa "...Sensei?"
    sar "Hey, are you okay?"
    sar "Your eyes suddenly got really wide out of nowhere."

    scene sanadormgirls17
    with dissolve

    sa "…"
    sa "It wasn’t...out of nowhere..."
    sa "It was after how I mentioned...him coming for Ayane."

    s "But, I-"

    stop music
    play sound "static.mp3"
    scene yumis2
    with flash
    scene sanadormgirls17
    stop sound

    "It’s suddenly harder to speak than it normally is."
    "My head hurts for some reason, but I’m not exactly able to pinpoint where."
    "It’s strange."
    "I feel like I was about to remember something."
    "But I guess it wasn’t important."

    play music "sweetvermouth.mp3"

    "I can even hear my favorite song crawl back into my head and confirm this."

    sa "A-Anyway!"
    sa "I...um...I talked to Ayane about maybe...coming to a karate class soon..."
    sa "But I’d...like for you to be there...too..."
    s "Oh, you were actually serious about the karate thing?"
    sar "Karate thing? What karate thing?"
    sar "My little Sana’s not thinking about learning a martial art, is she? "
    sar "Her bones will snap like twigs."
    sa "That’s...that’s why I need Sensei to be there..."
    sa "Because he’ll step in if someone...attacks me..."
    s "I think you’re misinterpreting how karate lessons normally go."
    sa "I don’t know...your...karate instructor got really loud...by the end of the night..."
    sa "She seems kind of scary..."
    s "The actual scary one was the woman next to her. I’m pretty sure she’s a serial killer."
    sar "Karate instructor? Serial killer?"
    sar "Did we actually have customers the other night?"
    s "Did you not notice a huge increase in sales? The serial killer drank like half of your stock."

    scene sanadormgirls18
    with dissolve

    sar "Oh! So {i}that’s{/i} where all that money came from! "
    sar "I don’t care if she was a serial killer! Get her to come back!"
    sa "Isn’t she just...a teacher?..."
    sa "If she was a serial killer, we’d...probably know..."
    s "If we knew, she’d be a horrible serial killer."
    sa "I...just think she’s...an alcoholic..."
    sar "So am I but I’ve never stooped to killing anyone."
    sar "Is my daughter really going to be doing karate with a serial killer?"
    s "Not a serial killer. The person {i}next{/i} to the serial killer."

    scene sanadormgirls19
    with dissolve

    sar "Oh. Well, that sounds a lot safer."
    sa "But umm...anyway...you’ll protect me...right, Sensei?..."
    s "There’s not really anything to protect you {i}from{/i} unless you’re planning on joining some fight club, but sure."
    sa "Maybe...I am?..."
    sa "What if I’m a really...strong fighter?"
    sa "Like...Zagull Throat Spear or...Stone Cold Steve Austin?..."
    s "I don’t know who either of those people are."

    scene sanadormgirls20
    with dissolve

    sar "Isn’t Stone Cold Steve Austin that one wrestler you used to watch on TV with-"
    sa "..."
    sar "..."

    stop music
    scene sanadormgirls21
    with dissolve2

    "My favorite song turns off again."
    "Today is bad."

    sa "...Mom?"
    sar "…"

    scene sanadormgirls22
    with dissolve2

    sa "Did you remember something?..."
    sar "…"
    sa "…"

    "It's good knowing that today is bad for other people, too."

    sar "..."
    sa "..."
    sa "Want to go for a walk?"

    scene sanadormgirls23
    with dissolve

    sar "Mm..."
    sar "..."
    sar "Mhm..."
    sa "Okay..."

    scene sanadormgirls24
    with dissolve
    play sound "dooropen.mp3"

    "Sana and Sara leave without acknowledging me, and I don’t blame them."
    "But I’m now faced with an empty head and an inebriated [high_school]er- two things that could mix horribly if I’d truly given up on everything."
    "Thankfully, I’m an outstanding citizen."

    if bonus == True:
        "A man with a moral compass that matches the size of his cock."
        "And I can put this girl to bed without defiling her."
    else:
        "I shall protect this girl as if she is a daughter to me."

    scene sanadormgirls25
    with dissolve

    ay "Sensei..."
    s "Oh. You’re awake."
    ay "I was never really asleep."
    ay "Are Sana and her mom going to be okay?"
    s "…"
    ay "…"
    s "I don’t know."
    ay "I see."
    s "…"
    ay "My head really hurts."
    s "How much did you drink?"
    ay "Two glasses."
    s "Lightweight, huh?"

    scene sanadormgirls26
    with dissolve

    ay "Shut up...you know I don’t normally drink..."
    s "I know, I know."
    ay "Can you help me to the bed?"

    if bonus == True:
        s "You mean the bed that’s right behind you?"
        ay "Or yours. Either one works for meeee~"

        "Something resembling a smile finds its way onto my face as Ayane trails off into a fit of childish laughter."

        s "Let’s put you to bed."
    else:
        s "Yes. But only because I care about your well-being and do not want you to hurt yourself."

    ay "Thank you...[ayanemaster]..."

    scene black
    with dissolve2

    "Ayane doesn’t take long to pass out."
    "The second her head hits the pillow, her eyes close and I’m suddenly alone again."
    "I wait around for a little while to see if Sana and Sara come back."
    "But I give up after twenty minutes of sitting awkwardly on the floor waiting for anything to happen."

    $ renpy.end_replay()
    $ sana_love += 1
    $ sanadorm35 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanadorm40:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
    if sana_love >= 15 and sanadorm15 == False:
        jump sanadorm15
    if sana_love >= 20 and bar20 == True and sanadorm20 == False:
        jump sanadorm20
    if sana_love >= 25 and bar25 == True and beachvacation16 == True and sanadorm25 == False:
        jump sanadorm25
    if sana_love >= 30 and bar30 == True and day != 4 and sanadorm30 == False:
        jump sanadorm30
    if sana_love >= 35 and bar35 == True and day != 4 and sanadorm35 == False:
        jump sanadorm35
...
```