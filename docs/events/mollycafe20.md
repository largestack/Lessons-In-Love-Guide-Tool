# The Legacy of Thaum Pt. II
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollycafe20&go=Go)



## Event preconditions
✅Molly love greater than or equal to 20

✅Event "[Molly: Onward to Valhalla](./mollycafe15.md)" is completed (event=mollycafe15)

✅Event "[Molly: Unpaid Promotion](./mollydorm15.md)" is completed (event=mollydorm15)



## Next events
* [Molly: Ahead of the Curve](./mollydorm20.md)

## Event properties
* ID: mollycafe20
* Group: Molly
* Triggered by label: mollycafe
* Triggered by branch label: mollycafe

## Event code
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe20:
    scene seconddnd1
    with fade
    play music "breeze.mp3"

    "I swing open the door to the cafe and quickly stumble onto the fact that tonight will be exponentially louder than I expected."
    "And considering I came here to see Molly, the expectation for noise was already pretty high."
    "Is it really okay for them to be playing this in the cafe, though? I can’t imagine Haruka signed off on this."

    mo "Ohoho~ It appears we have ourselves a new player!"
    mo "Take a seat, Sir! I shall help you create a character!"
    s "Uhh, no. I’m good. "
    s "I didn’t realize you all had plans to play here tonight."
    a "But I literally texted you about this exact thing happening."
    s "Yes, but I stopped reading the second I saw words I didn’t understand."

    scene seconddnd2
    with dissolve

    a "What if what I had to say was important?!"
    a "What if I was being kidnapped and didn’t have time to think of words you like?!"
    s "Then you’d probably be in someone’s trunk right now."
    mo "Are you sure you don’t want to play, Sir? We could use someone with your alignment."
    s "My...what?"
    mo "Neutral evil, Sir. That’s how I see your character."
    ay "Evil? Absolutely not. "
    ay "Sensei is lawful good. He’d never do anything to hurt anyone and always stands up for what is right."

    scene seconddnd3
    with dissolve

    f "I don’t think he’s {i}lawful{/i} good but maybe...neutral good? "
    f "His intentions aren’t always clear but I don’t think he’s a bad guy."
    a "Ayane! Stop saying you’re in love with my [uncle]!"
    r "How do you see yourself, Sensei? "
    s "I don’t even know what you’re talking about."
    sa "That’s okay...neither did Tsuneyo and...we helped her figure it out."
    s "Tsuneyo? Is she here?"
    t "Behind you."

    scene seconddnd4
    with dissolve

    t "My alignment is noodle evil."
    mo "{i}Neutral evil{/i}, Kendo Princess."
    t "Noodle evil."
    s "Do you understand what they’re talking about?"
    t "Almost. I seem to have everything very slightly wrong."
    s "That adds up."
    mo "She’ll be able to play once she starts following the rules."
    t "She’s right. I am very bad at this game."
    s "Well, I guess the two of us can watch together as long as you don’t get drunk and pass out on me again."
    t "I will do my very best."

    scene seconddnd5
    with dissolve

    m "If anyone wants my input, I think Sensei is chaotic evil. The absolute worst kind of person."
    s "And I think you’re a nerd."

    scene seconddnd6
    with dissolve

    m "Why does everyone keep calling me a nerd?!"
    mo "Ooooh, a critical hit!"
    mo "I’m giving Sensei advantage on his next attack as a special bonus for getting Maya to yell."

    scene seconddnd7
    with dissolve

    m "Tch!"
    ay "It’s okay, Maya. I don’t think you’re a nerd."
    ay "But I do want you to know that a certain rogue might sneak into your room at night and assassinate you for calling her true love evil."
    f "So...you watched the game on the beach...right, Sensei?"
    f "The one I wasn’t around for."
    s "I tried to. All I remember is a mushroom."
    mo "Well, never fear, Sir! For I shall be giving a recap of our exploits thus far shortly!"
    sa "We’ve played...a few more times since then and...you’ve missed a lot."
    r "Sana had her arm chopped off."
    sa "And then I...beat a man to death with it..."
    s "…"
    a "Yeah, Sana doesn’t really mess around when it comes to D&D. "
    s "…"
    s "Okay, well I’m going to sit down now."

    scene seconddnd8
    with fade

    t "They never chose an alignment for you."
    t "Allow me to do it instead."
    t "I declare you..."
    t "True noodle."
    s "I declare you weird."
    t "I declare my feelings hurt."
    t "Please never talk to me again."
    s "Can I treat you to ramen to win you back?"
    t "…"
    s "…"

    scene seconddnd9
    with dissolve2

    t "I will not allow myself to be bought off like this."

    scene seconddnd10
    with fade

    mo "Okay! That’s enough idle chit chat! The time has come for our journey to continue!"
    mo "We only have two hours until the Magistrate of Mammaries returns to the cafe and scolds all of us for taking up an entire section of the store without buying anything!"
    r "I’m a big fan of the nickname you chose for Haruka. It's very fitting."
    ay "Don’t you think it would be a little better for Futaba, though? I think hers are bigger."
    a "Futaba, what size bra do you wear? Like X?"
    f "I...don’t think it goes that high..."
    mo "Enough!"

    scene seconddnd11
    with dissolve

    mo "When we last left off, we discovered that a powerful Illithid by the name of Thaum had emerged from the Underdark with a small army of thralls at their disposal."
    mo "The party, sensing it had to unite or face a rather untimely and premature level two demise, banded together to force back the thralls."

    scene seconddnd12
    with dissolve

    mo "But not before the loss of Zagull Throat Spear’s arm. "
    mo "Without anyone able to help Zagull regenerate said arm and Thaum retreating to do more evil psion stuff..."
    mo "The party headed to the nearby city of Frostford for some much needed rest and...hopefully an experienced healer."

    scene seconddnd13
    with dissolve

    mo "Despite its name, Frostford is a coastal, port city that is home to one of the biggest alchemical colleges in all of the land."
    mo "So it’s no surprise when you see the streets lined with [young]alchemists, their noses buried deep in books, studying their hearts out to prepare for upcoming exams."
    mo "It’s the end of a semester and the city is bustling with uncertainty and energy. "
    mo "The perfect time to talk to anyone you want or, better yet, ask them anything you’re still curious about."
    mo "Your party still has no clear goal as you took a wrong turn and ran into Thaum long before you were supposed to, so things could really go anywhere from here."

    scene seconddnd14
    with dissolve

    mo "So, what do you guys wanna do? "
    mo "Like I said, there’s no goal right now and you still don’t know why you all woke up next to one another, so it’s probably a good idea to go out and find a...reason to exist or something."

    scene seconddnd15
    with dissolve

    r "Sana, how important is it for you to get your arm back?"
    sa "I..."
    sa "I kind of like only having one arm..."
    sa "It makes me look strong and...I’m able to wield my greataxe with one hand."
    mo "You’ll still have disadvantage though, so...just saying."
    r "Okay, but what matters more to you? Looking cool or killing people?"
    sa "That’s...umm..."
    r "Actually, don’t let Sana think about that. What would {i}Zagull{/i} want?"

    scene seconddnd16
    with dissolve

    sa "Zagull will...bathe in the blood of his enemies no matter the circumstances!"
    sa "He only needs one arm to drain the life from his opponents!"

    scene seconddnd17
    with dissolve

    a "Well...while Nithhala and Zagull are trying to figure out the arm thing, do you think maybe the rest of us should head to a tavern or something?"
    m "Is your wizard also an alcoholic?"

    scene seconddnd18
    with dissolve

    a "What? No. Just...that’s where you normally go to pick up quests and stuff."
    f "That’s true. Innkeepers always seem to know the latest gossip in fantasy novels."

    scene seconddnd14
    with dissolve

    mo "So you three are going to head to the tavern?"
    m "Yes. Arborea needs to get her fix."
    a "I do not! I’m just looking for some sort of goal so we don’t wander around town until we grow old and die!"
    mo "Oooookay! Arborea, Urrheak and Xessaxia-"
    mo "You’re lucky enough to come across a signpost pointing you directly toward the tavern immediately after entering the city limits."
    mo "It appears to be only a short walk from here, so you should be able to get there in no time at all."

    scene seconddnd19
    with dissolve

    mo "Nithhala and Zagull, are you going to the tavern as well?"
    r "Huh? Oh, yeah. We’ll go."
    r "Zagull isn’t convinced that he wants his arm reattached yet."
    sa "But Zagull {i}could{/i} go for a tall glass of mead! Bahahaha!"
    mo "Okay! So the five of you begin to make your way to the tavern-"

    scene seconddnd20
    with dissolve

    ay "Wait a second, I haven’t said what I wanted to do yet."
    mo "Oh, sorry. Lots of people. Trying to keep track of everything."
    mo "What is Lidearel doing?"
    ay "…"
    ay "She’s gonna go with everyone because she gets lonely easily."
    ay "But she’s also going to try and pickpocket the first man she sees."
    mo "You see a lot of men. It’s a relatively busy city."
    ay "Are there any gnomes?"
    mo "There are not."
    ay "Tieflings?"
    mo "Apart from Nithhala? No."
    ay "I’m just going to try to pickpocket Nithhala then."
    r "Dude."
    ay "I won’t keep anything. I just want to assert dominance."
    r "Steal from Zagull. He’s only got one arm."
    ay "Yeah but that arm is bigger than my entire body. I’m going to pickpocket Nithhala."

    scene seconddnd21
    with dissolve

    r "…"
    sa "This is fun..."
    r "Easy for you to say. You killed someone with your arm."
    mo "I mean...it's kind of an unwritten rule to not do things like this...but roll sleight of hand, I guess."

    ay "Woo! Just gonna grab my dice and..."

    play sound "dice.wav"

    ay "That’s an...18."
    mo "Oof. Okay. Rin, roll perception to see if you catch her."
    r "Why? We all know what it’s going to be."
    mo "So you’re just going to ignore her pickpocket attempt?"
    r "Ugh, fine."

    scene seconddnd22
    with dissolve

    r "Sana. "
    sa "...Yes?"
    r "Can you blow on my dice for good luck?"
    sa "Is that...a thing people do?"
    r "I think so?"
    sa "...Um."

    scene seconddnd23
    with dissolve

    sa "{i}Hoooo...{/i}"
    r "..."
    r "So cute..."

    scene seconddnd24
    with dissolve

    r "OKAY! Thanks, Sana! With your blessing, there’s no way I can lose!"

    scene seconddnd25
    with dissolve
    play sound "dice.wav"

    r "…"
    sa "…"
    r "…"
    sa "…"

    scene seconddnd26
    with dissolve

    sa "There there..."

    scene seconddnd27
    with dissolve

    mo "Nithhala rolled a 5 for anyone who didn’t see. Which means Lidearel is able to successfully reach her hands into Nithhala’s pockets and find..."
    ay "Woo! What did I get?!"
    mo "Absolutely nothing."
    mo "You didn’t start with any items and Nithhala’s bag is completely empty."

    if bonus == True:
        mo "Since you rolled an 18, though, we can assume that you just successfully groped her without being noticed."
    else:
        mo "Since you rolled an 18, though, we can say that you managed to like...steal a button off of her outfit or something."
        r "Noooooooo my button!"

    ay "Oh. Well, that’s better than nothing, I guess."

    scene seconddnd28
    with dissolve

    t "Are you having a good time?"
    s "Are you?"
    t "I think so. "
    t "Everyone else is having a good time, so I think I’m supposed to be having one as well."
    t "I’m very confused, though."
    s "You and me both."
    s "What’s so fun about deciding success based on dice rolls?"
    t "Perhaps there is a certain ingrained desire in all of us to allow chance to rule our lives?...So that we do not have ourselves to blame when things don’t go our way."
    s "…"
    t "Or maybe they just like dice."
    t "I don’t know. I’m not allowed to play."

    scene seconddnd29
    with dissolve

    mo "So, after Lidearel feels up her tiefling companion, she and the rest of the group make their way to the local tavern."
    mo "It’s a large building situated in the center of the city with an ornate wooden archway towering over a beautiful pair of dwarven, hand carved doors."
    mo "But, before you’re able to enter, the doors swing open and out flies a young, half elf woman."
    mo "She falls flat on her face, but quickly regains her composure and scurries backward."
    mo "Her clothes are tattered and torn...and look as if they haven’t been washed even once in her life."

    scene seconddnd30
    with dissolve

    mo "{i}Back! Back, I say!{/i}"
    mo "{i}You’re...you're all here to laugh at me as well, aren’t you?!{/i}"
    mo "{i}That’s all they ever do in this town! Laugh, laugh, laugh!{/i}"

    scene seconddnd31
    with dissolve

    mo "The woman brandishes a golden dagger with a silver inlay on the handle, one that looks far too valuable for her to own, and points it directly at Arborea."
    a "Wait, me? What did I do?"
    mo "Is that {i}in{/i} character or out of character?"
    a "Oh. Uhh, both I guess?"
    mo "Cool. I’m just going to keep roleplaying then."

    scene seconddnd32
    with dissolve

    mo "{i}You...You think I don’t know who you are?{/i}"
    mo "{i}You’re the same woman who turned me away in the last tavern!{/i}"
    mo "{i}None of you ever listen! Thaum is...Thaum is coming!{/i}"

    scene seconddnd33
    with dissolve

    f "Surely, you jest. "
    f "If you speak of the mind flayer, we made quick work of him on our way into town."
    mo "{i}Then...Thaum is...dead{/i}?"
    f "Nay, just forced back. But his army reduced to mere nothing."
    a "The Satyr speaks the truth. "
    a "You must have me confused with someone else."
    a "I’ve never even come to this town before."
    m "Bacawk."

    scene seconddnd34
    with dissolve

    mo "You...you know the aarakocra can speak common as well, don’t you? "
    mo "You don’t always have to talk like a bird."
    m "Urrheak never learned common."
    mo "R...Right..."
    mo "But anyway..."

    scene seconddnd35
    with dissolve

    mo "{i}If...if what you say is true and the first line has already been pushed back...then...{/i}"
    mo "{i}Then it’s only a matter of time before...{/i}"

    scene seconddnd36
    with dissolve

    mo "The woman takes several steps back, tripping over a park bench and tumbling into the cart of a food vendor."
    mo "But just as the vendor is about to cry out in a fit of rage after having his product destroyed, the woman violently grips her head and begins ripping out large clumps of her hair."
    mo "She lets out a pained scream as if she’s being consumed from the inside out."

    scene seconddnd37
    with dissolve

    mo "{i}NGAHHHHH! I...I CAN FEEL HIM!{/i}"
    mo "{i}STAY...BACK! I CAN’T...FIGHT IT ANY LONGER!{/i}"
    mo "{i}I...I-{/i}"
    mo "{i}Blahhhhhgababababababa!{/i}"

    scene seconddnd38
    with dissolve

    mo "The woman suddenly turns into a mushroom. Go ahead and roll for initiative."

    scene seconddnd39
    with dissolve

    t "The fungus returns!"
    t "Run, friends! Escape while you still can!"
    s "Are there any enemies in this game other than different types of mushrooms?"
    t "One can only hope. "
    t "They won’t last much longer at this rate."
    s "And neither will I."
    s "I’m going to head out."

    scene seconddnd40
    with dissolve

    t "What?"
    t "But then who will I talk to?"
    mo "What’s this I hear about heading out?"

    scene seconddnd41
    with dissolve

    mo "Are you not having a good time, Sir?"
    mo "I’m sorry. If I’d have known you’d be appearing tonight, I wouldn’t have scheduled our next session when I did."
    s "Oh, I’m not asking you to call it off or anything."
    s "Don’t let me get in the way of your fun. This sort of thing just isn’t for me."
    mo "Do you...not even want to try? "
    mo "There are plenty of things I never expected to like that I absolutely love now...And I never would have known that if I didn’t give them a chance."

    if bonus == True:
        mo "Granted, they’re all different doujinshi tags and that doesn’t really apply to this conversation, but I’m sure you know what I mean."
        t "I don’t. Please explain."
        mo "When you’re older, Kendo Princess."
        t "Yes, Emerald Guardian. I understand."

    s "Maybe some other time. I’m just going to head out now, though."
    s "As for Tsuneyo-"
    mo "She’ll be fine. "

    scene seconddnd42
    with dissolve

    mo "Come sit at the table with us. We’re starting combat in a minute or two and I’ll try teaching you how that works again."

    scene seconddnd43
    with dissolve

    mo "Sorry you didn’t have fun, Sir. "
    mo "I was hoping it would be exciting enough for everyone, but it seems I may have failed you."
    s "Again, don’t be too hard on yourself. It’s just a personal interest thing."
    s "Maybe some other time."
    mo "Okay. Maybe some other time..."

    scene black
    with dissolve2

    "I get up off the stool and say goodbye to all of the girls, exiting the cafe and starting my journey back."
    "I hope Molly doesn't take my early departure too personally."
    "I understand why she’d be upset that I’m not interested in the same things as her but, at the same time, she should have probably realized that by now."
    "Liking different things is fine, though."
    "It gives me more time to..."
    "Aimlessly wander around town and think about all of the other things I could have done with my night."
    "Oh well, I guess."
    "At least all of the girls seem to be having a good time."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe20 = True
    stop music fadeout 5.0

    "{i}Molly's affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe25:
...
```

## Code that triggers this event
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe:
    if molly_love >= 0 and mollycafe1 == False:
        jump mollycafe1
    if molly_love >= 5 and mollycafe1 == True and mollycafe5 == False:
        jump mollycafe5
    if molly_love >= 10 and mollycafe5 == True and mollydorm5 == True and mollycafe10 == False:
        jump mollycafe10
    if molly_love >= 15 and christmas7 == True and mollycafe15 == False:
        jump mollycafe15
    if molly_love >= 20 and mollycafe15 == True and mollydorm15 == True and mollycafe20 == False:
        jump mollycafe20
...
```