# Love Me to Pieces
Uta event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utamaid5&go=Go)



## Event preconditions
✅Uta love greater than or equal to 5

✅Event "[Uta: Abuse of Power](./utamaid1.md)" is completed (event=utamaid1)

✅Day of week is a weekend



## Next events
* [Sana: Purest Intentions](./bar35.md)
* [Uta: The VIP Treatment](./utadorm5.md)

## Event properties
* ID: utamaid5
* Group: Uta
* Triggered by label: utamaid
* Triggered by branch label: utamaid

## Event code
File: \game\UtaEvents.rpy
Code:
```python
...
label utamaid5:
    scene utamaidfive1
    with fade
    play music "maidcafe.mp3"

    "I arrive at the maid cafe and find that it’s actually kind of busy for some reason tonight."
    "So busy that I don’t even have to deal with the inner struggle about whether to ring the bell or not as Uta immediately notices my presence and greets me at the entrance."

    scene utamaidfive2
    with dissolve

    u "Maaaaaasteeeeeeer~"
    u "Welcome baaaaaaack~"
    s "Are you crying right now?"
    u "I’m just so...{i}sniff{/i}...happy to see you..."
    u "It has nothing to do with how I’ve been on my feet for a million years...I’m totally fine..."
    s "Why not take a break or something?"

    scene utamaidfive3
    with dissolve

    u "Ugh...Spoken like a true non-customer-servicey-person..."
    u "I can’t just take a break when we’re this busy."
    u "We’re having a crazy sale thingy this weekend to try and bring in more customers-"
    u "And, on top of that, I’ve gotta train a new maid as well. I’m beat. I didn’t even get to have lunch today."
    s "Is that even allowed? Aren’t you a-"
    u "Part-time employee? You bet your butt I am. But that doesn’t change how I’ve gotta step up when there are...steps that need to be...stepped up."
    u "Or something."
    s "This is not the Uta-chan I know. That Uta-chan wouldn’t get so easily stumped by her own words."

    scene utamaidfive4
    with dissolve

    u "The Uta-chan you know and love is no more. She’s with her grandpa now."
    s "Can you stop bringing up your dead grandpa all the time, please?"
    u "Alas. I miss him dearly."

    scene utamaidfive5
    with dissolve

    u "Hey. You wouldn’t wanna put on a uniform and help me out by any chance, would you?"
    s "That might be the worst thing anyone has ever asked of me."
    u "So is that a no? Even though you love me to pieces?"
    s "There isn’t anyone I love enough to wear a costume like that."

    if bonus == True:
        u "Not even if it’s one I wore? "
        u "You wouldn’t put it on and think something lewd like “Uta-chan’s beautiful, bare skin touched this fabric. I can’t contain myself!” or something like that?"
        s "Okay, I’m definitely bad- but I’m not {i}that{/i} bad."
    else:
        s "Okay, you know what? I {i}do{/i} want to wear it. I just...shouldn't do that anymore."
        u "Anymore?"

    s "Also, there is no chance in hell that something you wore would ever fit me."

    scene utamaidfive6
    with dissolve

    u "That’s it. You and Io both hate me. She wouldn’t wear the costume either and she’d probably look even cuter in it than you would."
    s "I don’t think the “probably” is needed there. She’d look much better than me in a maid outfit."
    u "Now Uta-chan’s friend is being praised instead of Uta-chan. What a horrible day."

    play sound "dishes.mp3"

    s "…"

    fv "Ah! Shit!"
    fv "Um...U-Uta?..."
    u "I hope we never have to do something like this sale ever again..."
    s "Careful, Uta. You’re breaking character."
    u "I hope we never have to do something like this sale ever again, Master..."
    s "Better. Hang in there."
    s "Can I just take a seat wherever?"
    u "Of course, Master..."

    scene utamaidfive7
    with dissolve

    u "But...if you want my recommendation-"
    u "There’s this really cute girl over in the corner that would love your company if you’d be so obliged."
    u "And she hasn’t even placed her order yet, so you’ll probably be served faster if you sit with her as well."
    s "Beautiful girl?"

    scene utamaidfive8
    with fade

    s "Oh, Io is here."
    u "That’s right, Master!"
    u "The cute and cuddly bathhouse girl you know and love, Io Ichimonji. Slender, soft, and ripe for the plucking!"
    s "Aren’t you supposed to be upselling desserts and not actual human beings?"
    u "If she’s going to auction me off, I’m gonna auction her off! This is war!"

    scene utamaidfive9
    with fade

    u "Come on, Master. Don’t you think she looks all lonely over there by herself?"
    u "I’m sure she’d love a little bit of company. "
    u "Also, if you sit with her, I can kill a bunch of birds with a rock and have the new maid come out and take {i}both{/i} of your orders at once."

    "So it was just about efficiency..."

    u "I was planning on just testing things out with Io since she’s a friend of mine and won’t leave any bad reviews-"
    u "But two friends at the same time? This is a gold mine I can’t let slip away."
    s "…"
    u "What’s wrong? Why the silent treatment all of a sudden, Master?"
    u "Does Io make you nervous?"
    s "I kind of...you know."
    u "…"

    scene utamaidfive10
    with dissolve

    u "Ah! Master!"
    u "Were you upset because you wanted {i}me{/i} to be your maid, no matter what?"
    s "You are the only maid that matters to me, Uta-chan."
    u "Really?"
    u "Even though your [niece] works here?"
    s "Oh."
    s "Right..."
    u "Don’t worry. I won’t tell her you like me more."

    "That’s really comforting to hear from a girl who introduced herself to the class with “I will probably let things about you slip on accident. Don’t hate me for it.”"

    s "Thanks..."

    scene utamaidfive9
    with dissolve

    u "You don’t need to worry, though, Master. I’ll be right there with the new girl."
    u "I’ll shadow her while she takes your order so I can be sure she’s taking care of you just as well as I would."
    u "Well, maybe not {i}just{/i} as well. There’s no one that likes caring for you as much as your faithful Uta-chan does~"
    s "God I love you."
    u "Then go sit with Io and wait for me to come over there. "
    u "I’ll be back soon, kay? I’ve already kinda talked to you over here for too long."
    u "But this was the closest I had to a break all day, so at least I can be happy I got to spend it with you~"

    scene black
    with dissolve

    "Uta winks at me, doing a twirl as she skips away to the kitchen."
    "I need to squeeze past a few other customers who had pulled their chairs out a bit too far on my way to Io-"
    "But I eventually make it there and...I guess I startle her as she jumps up in surprise the second I sit down."

    scene utamaidfive11
    with dissolve

    i "Oh my God...Hey. "
    i "You scared the crap out of me."
    i "I thought you were just some random person sitting down at the table with me for a second."
    s "Hey Io. Independent as ever, I see."

    scene utamaidfive12
    with dissolve

    i "Nahh. Just bored. "
    i "Thought I’d come see Uta since I didn’t have anything else to do tonight."
    i "You’re here for the same reason, I guess?"
    s "Yeah. I think I’m starting to develop a bit of a maid addiction."

    scene utamaidfive13
    with dissolve

    i "Really? You don’t seem like the type who would be into that...cutesy sort of thing."
    s "You don’t either but...here we are."
    s "A maid cafe is actually on the list of places I’d least expect to see you given your apparent distaste for girls."

    scene utamaidfive12
    with dissolve

    i "I wasn’t planning on staying long. Was just going to eat and then probably go out for a walk or something."
    i "I think Uta said something about needing my help, too, but I have no idea what it’s about."
    s "I think I do. "
    s "She’s training a new girl and I think she wants us to be her first test subjects."

    scene utamaidfive14
    with dissolve

    i "Oh."
    i "Uhh..."
    i "Want to order for me?"
    s "…"
    s "Really?"
    i "Have you ever dealt with an inexperienced employee before? It’s awkward and uncomfortable and I already have a hard time dealing with Uta’s fake maid personality."
    s "To be honest, she seems mostly the same to me."
    i "Nuh-uh. Hearing her call herself Uta-{i}chan{/i} makes me cringe harder than some crummy 80’s slasher film."
    s "Weird comparison but I think I get it."
    fv "Wait, already?! I thought I was just doing backroom stuff today?"
    u "You can’t hide from customers forever, Osako! The floor is where all the real money is!"

    scene utamaidfive15
    with dissolve

    s "Osako?"

    "Isn’t that my karate instructor’s name?"

    i "Someone you know?"
    s "…"
    s "No way. The only person I know with that name is a total badass and would never work somewhere like this."

    u "Uta-chan hidden technique...maid-push! Aaaaand-"
    u "...Ngh!"
    u "Why aren’t you moving?! I pushed you as hard as I could!"
    fv "I didn’t even feel anything..."
    u "No, really!"
    u "Are you wearing some sort of...vest?...Why the heck is your body so hard?"
    u "What is on you, Osako-chan?!"
    fv "That’s just how my body is, okay?! There’s no need to touch me..."
    fv "I’ll go out there and try but...I still don’t have any idea what I’m doing and I-"
    fv "Well..."
    u "Worried about the way you look?"
    fv "…"
    u "Don’t worry. The guy at your table’s a real go-getter and I’m sure he’ll think you’re beautiful."

    scene utamaidfive16
    with dissolve

    i "Ooooh. A real go-getter, huh?"
    s "I don’t go and get anything. It just comes to me with minimal effort."
    i "Uh-huh. Likely story."
    i "Try not to flirt too hard while you’re with another girl, Sensei."
    i "And don't forget to order for me."
    s "Am I still doing that?"
    i "I wouldn’t have it any other way."

    scene utamaidfive17
    with dissolve

    fv "Um...Good evening...Master..."
    fv "Are you ready to..."
    fv "…"
    fv "Oh...you’ve gotta be kidding me."

    scene utamaidfive18
    with dissolve

    os "Why? Why are you here?"
    os "Hanging out with [high_school] girls during the afternoon isn’t enough, you need to do it at night, too?"
    s "I could be asking you the same question. Why are you even working here?"

    scene utamaidfive19
    with dissolve

    os "Job security, okay? I still don’t have a guarantee in writing from that damn rich family that I’ll be keeping my instructor job, so I’m...weighing other options."
    s "And...a maid cafe was in that list of options?"

    scene utamaidfive20
    with dissolve

    os "Yeah...I bet I look really out of place up here, huh?"
    s "Wait, I didn’t mean it like that. I think you look-"

    scene utamaidfive21
    with dissolve

    u "Oof. Bad move, Master."
    u "Osako-chan was finally brave enough to come say hi to you and you cut her down just like that."
    u "For someone who spends so much time with girls, you really have no idea what to say to them, do you?"

    scene utamaidfive22
    with dissolve

    os "It’s fine. I spend so much time bossing this guy around that he’d probably greet me that way no matter how I looked."

    scene utamaidfive23
    with dissolve

    u "Bossing him around?!"
    u "Master is an M when I thought he was an S this whole time?!"
    os "S?..."
    os "M?..."
    os "What does that even mean?"
    s "I think she’s misinterpreting our relationship."

    scene utamaidfive24
    with dissolve

    i "I believe she is. Sensei is clearly an S."
    u "Io! I forgot you were even here!"
    os "What’s with all these letters?..."
    i "I didn’t plan on joining in on this conversation, but I don’t mind fighting for Sensei’s honor when he is clearly not an M."

    if bonus == True:
        scene utamaidfive25
        with dissolve

        os "Dude...are you really stringing along these ones, too?"
        os "Ayane alone isn’t enough?"

        scene utamaidfive26
        with dissolve

        u "Ah! So the girl in the bath was Ayane! I knew it!"
        u "I need to add that to the list!"
        s "Please don’t add anyone to any list, Uta."
        os "You...bathe with her?"
        os "Please tell me you two are related in some way."
        s "Would that really make it any better at this point?"
        i "Sure. As a bathhouse employee, I can confirm that there are plenty of co-ed family members that bathe together all the time."
        i "Granted, some of them have gotten up to some pretty raunchy stuff without realizing there are cameras, but not {i}all{/i} of them are like that."
        i "Just...most."
        s "Thanks, Io. That really helps."
        i "Really? Because it doesn’t sound like it would after hearing it out loud."
        s "I was being sarcastic..."

    scene utamaidfive27
    with dissolve

    os "Um...Uta? Can I go back into the kitchen now?"
    u "Huh? But you haven’t even taken their orders yet."
    os "Are they still going to order after all of this? I would just leave if I were in their shoes."

    scene utamaidfive28
    with dissolve

    s "Io and I will both have whatever today’s special is."
    u "Why are you ordering for Io?! Are you two dating now?!"
    u "What happened in the three minutes you were alone together?!"
    i "What happened is I told him he could order for me. We’re not dating."
    u "Really?! Cause you never know with this scoundrel!"
    os "Alright, so...I feel really awkward right now, but I heard your order and...I think that means my job is done."
    os "I’ll go tell the kitchen staff and..."
    os "Um..."

    scene utamaidfive29
    with dissolve

    os "If you could...not tell anyone else in the dojo about me working here on the side, that would be kind of awesome."
    s "Deal. As long as you don’t tell Ayane you saw {i}me{/i} here either. She gets jealous pretty easily."
    os "Consider it done. "
    u "Yes. {i}Consider it done{/i}, indeed."
    s "Do you even know what we’re talking about, Uta?"
    u "No. I’m too busy scowling at you."
    u "Does it look intimidating? Do you {i}fear{/i} Uta-chan?"
    s "I'm utterly terrified."

    scene utamaidfive30
    with dissolve

    i "Hey, I don’t work here so correct me if I’m wrong, but..."
    i "Don’t you two need to, you know, get back to work? "
    i "There’s a huge line of people at the door right now."
    u "Ah! Osako-chan! Retreat! "
    u "If we’re quick enough, they might think this is just a normal restaurant and not a maid cafe!"
    os "Uhh...no. I think they’re all pretty sure this is a maid cafe."
    u "Either way! Run! Now!"

    scene black
    with dissolve2

    "Uta grabs Osako by the sleeve and pulls her into the back room."
    "Roughly thirty seconds later, Uta is pushed back out onto the floor by someone who I imagine is her supervisor and proceeds to handle everyone all on her own."
    "That poor girl."
    "Customer service really seems rough- especially in a place like this."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utamaid5 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utamaid10:
...
```

## Code that triggers this event
File: \game\UtaEvents.rpy
Code:
```python
...
label utamaid:
    if uta_love >= 0 and day247 == True and utamaid1 == False:
        jump utamaid1
    if uta_love >= 5 and utamaid1 == True and day > 5 and utamaid5 == False:
        jump utamaid5
...
```