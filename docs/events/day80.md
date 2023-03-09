# Secret Ingredient
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day80&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 80

✅Event "[Main: Weight Limit](./day72.md)" is completed (event=day72)



## Next events
None

## Event properties
* ID: day80
* Group: Main
* Triggered by label: saturdaymorning
* Triggered by branch label: saturdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day80:
    scene showdown1
    with dissolve
    play music "happyandplotting.mp3" fadein 5.0

    sa "…"
    s "…"

    scene showdown2
    with fade

    m "…"
    m "Okay...can someone explain to me what’s going on here?"
    m "I was under the impression that I was going to the movies with Ami."
    a "We {i}are{/i} going to the movies! I just need to kick Ayane’s butt in a cooking competition first!"
    ay "Oh, please! As if I’d let you win a competition as important as this!"
    ay "This might be the only chance I ever get to directly compete against you for Sensei's heart! I will not let you take this from me!"
    a "Sensei doesn’t want your bubble wrap empire, Ayane!"
    ay "Neither do I so that's just one more thing we have in common!"

    "So, here we are...The ultimate showdown between Ami and Ayane- two [teenage]girls giving all they have to impress three of us (But mostly me) with their cooking."
    "I'm a little worried about giving Ayane access to so many knives during a battle in which my {i}love{/i} is the prize...but I figure I’ll be able to step in if she does decide to get all...’Ayane.’"

    scene showdown3
    with fade

    sa "Um...thank you again...for inviting me over..."
    sa "I’m sorry to...intrude like this..."
    s "It's fine. Make yourself at home."
    m "And what is {i}this?{/i} When did you two start warming up to one another? Why are so many strange things happening today?"

    scene showdown4
    with dissolve

    sa "U-Umm...Sensei...has been coming to the bar I work at recently and..."
    sa "He’s been helping me...get more comfortable around other people..."

    scene showdown5
    with dissolve

    m "Is that so?..."
    m "I didn’t realize he was actually capable of instructing anyone in ways that don't directly benefit him."
    s "Everyone benefits from a more talkative Sana. She is a welcome investment of my time."
    m "Sana, blink twice if you are being forced to comply against your will."
    sa "I'm...not a hostage! Sensei has...actually helped a lot!"
    sa "I’ve only cried a couple times so far!"

    scene showdown6
    with fade

    s "Was telling her that part really necessary?"
    m "So...because you’ve only cried {i}a couple times{/i}, you think he’s doing a good job?"
    s "See? Now she's just going to use that against us and you're never going to learn how to talk."
    sa "I'm sorry...I...I..."
    m "Sana, if you really want help when it comes to communicating, let me handle it. I can guarantee you I'll be of more assistance than him."

    scene showdown7
    with dissolve

    s "We're trying to teach her how to {i}talk{/i} to other people, not how to make them feel insignificant and unwelcome."
    sa "I...think Sensei...is doing a good job...and um...I think...I'm going to stay...with him..."
    m "You will regret this decision, but it is yours to make."
    sa "Did...um...something happen between you two?..."
    sa "You seem...a little different outside of school..."
    a "Don’t mind them, Sana! Those two are never going to get along. Me and Ayane have already accepted it."

    "Ami calls out from the kitchen and sums up the relationship between Maya and me pretty perfectly."
    "I don’t know if I’d go as far as saying that we’ll {i}never{/i} get along, though..."
    "Maya will {i}have{/i} to warm up to me some day, right?"
    "…"
    "Right?"

    scene showdown2
    with fade

    m "How much longer do we need to wait until this {i}competition{/i} actually begins? I'm starving and I envisioned myself with several buckets full of popcorn by now."
    a "You're gonna have to ask Ayane. She's the one who's supposed to be going-"
    ay "Silence! And fear no more, Maya! For the first course of several unbelievable courses is about to be served..."

    scene showdown8
    with fade

    ay "We’ll be starting today off light and indulging in our wonderful culture with a staple of nearly every Japanese dish...rice."
    ay "While it may not be the most {i}exciting{/i} food item you will be eating today, it's important to remember that good rice can elevate a dish to unbelievable levels!"
    ay "And even though it may {i}seem{/i} simple, there are countless different ways to use it and even more ways to-"
    m "I'm sorry, is the monologue part of the dish? Or am I allowed to eat now?"

    scene showdown8r
    with dissolve

    ay "You may eat! But please remember to like, comment, and subscribe if you enjoy it!"

    scene showdown9
    with dissolve

    sa "Subscribe to...rice?..."
    s "This seems like a lot of rice, Ayane. I don't really think any of us want to fill up on-"

    scene showdown10
    with fade

    m "Seconds, please."
    s "..."
    sa "..."
    m "..."

    scene showdown11
    with dissolve

    m "...What?"

    scene black
    with dissolve2

    "Ayane’s rice is...well, rice."
    "It’s cooked properly and not seasoned in any way."
    "It’s just...a typical side dish you'd receive at a restaurant alongside miso soup."
    "That said, I couldn't really find any issues with it either. So I guess this sort of...simplistic form of cooking is in line with how Ayane likes to do things."

    scene showdown12
    with dissolve

    a "Hi, everyone! Did you all enjoy Ayane's first dish? Or do you think it was super boring and that she should get locked inside of a shed somewhere?"
    ay "Hey! You can’t ask questions like that in the middle of the competition! It’s unfair!"
    ay "Sensei! Deduct points from her score!"
    a "Please ignore the loud noises coming from the kitchen. Our ice machine broke and has been making a strange whining sound all morning."
    ay "Ami! You know I hate it when you compare me to industrial appliances!"

    scene showdown13
    with dissolve

    a "Anyway! Please enjoy my version of Ayane’s super boring dish but with an extra special ingredient! Thank you very much for your time and remember to vote Ami!"

    scene showdown14
    with fade

    sa "..."
    s "..."
    m "What?..."
    m "Why are you both looking at me?"
    s "We want to watch how you eat."
    sa "I’m...also curious..."
    m "Why?..."

    scene showdown16
    with dissolve

    sa "I...don’t know..."
    sa "It’s just...kind of impressive, don’t you th-"

    scene showdown10
    with hpunch

    m "Seconds, please."

    scene showdown17
    with fade

    sa "Wha-"
    s "We looked away for too long..."
    sa "It...was only a couple seconds..."
    m "I honestly don't understand what you two are so riled up about. I'm just doing the same thing I always do."
    sa "You are...{i}always{/i} like this?..."
    s "Just leave it alone, Sana. She's a monster..."

    scene black
    with dissolve2

    "Ami’s rice is...also rice."
    "However, just like she hinted at, there’s an extra special ingredient in it."
    "And that ingredient?..."
    "Is love."
    "Just kidding. It’s salt."
    "Ami must have salted the rice before bringing it to us, which I greatly appreciate since I put salt on virtually everything."
    "And just like that, we have our first example of her directly catering to my tastes without thinking about what the other judges will think."

    scene showdown18
    with dissolve2

    sa "So...what do you think, Sensei?...Which one was better?..."
    s "Ami, without a doubt. "
    s "Ayane’s rice was probably cooked a little better. But without any seasoning, I just can't say I'd choose it over Ami's."
    ay "Sensei! You know that salt is bad for your heart, don't you? For the sake of your health, I think you should lay off."

    if bonus == True:
        ay "How do you expect to raise our children with your sodium levels through the roof?"
        a "Stop trying to raise a family with my [uncle]!"
    else:
        ay "If you do not be careful, I will be making necklaces out of {i}your{/i} bones soon! Hahaha."
        a "Stop trying to turn my client into a necklace!"

    ay "No!"
    s "…"
    sa "...Uhh."
    sa "Anyway...I think I liked...Ayane’s more..."

    scene showdown5
    with dissolve

    m "I’m also going to choose Ayane for this round."
    m "I didn’t particularly favor either dish. I just don’t want to vote for the same person he does."
    a "Maya! That’s not how this works!"
    m "I am an unbiased judge. Please continue on with the competition."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene showdown8
    with dissolve

    ay "So! Now that I've already won the first round, I’ll be counting on you guys to support my love- err...{i}food{/i} at least one more time to lock in a victory for me!"
    ay "For the main course, we have a-"

    scene showdown19

    ay "Wait...Sana? What’s wrong?"

    scene showdown20
    with dissolve

    sa "..."
    ay "What happened? Did I do something wrong?"
    m "Uhh..."
    s "I’m surprised you haven’t heard about this story, Ayane."
    ay "Story? What story?"
    s "Sana has a traumatic experience when it comes to spaghetti."
    ay "What? How does that even happen?"
    sa "I...can't do this..."
    s "It’s a long story."
    sa "Sp...sp...sp..."
    m "Uhh..."
    m "I’m just going to eat now."

    scene black
    with dissolve2

    "Despite Sana’s disposition toward the dish, Ayane’s pasta is quite nice."
    "I'm not sure if it's something that I could eat every day. But it's definitely something I wouldn't mind ordering again if this were a restaurant."
    "I think it's pretty safe to say Ayane has already lost one voter for this round, though..."

    scene showdown20r
    with dissolve

    sa "…"
    s "Are you okay?"
    sa "I’ll be fine..."

    scene showdown20r2
    with dissolve

    m "I can’t believe this is a sentence I am about to say, but..."
    m "Can you tell me the spaghetti story?"
    s "You're ready for the spaghetti."
    m "Please never say that again."

    scene showdown12
    with dissolve

    a "Sorry guys, but the spaghetti story is going to have to wait!"
    a "What I just laid out in front of you will be your second main course for the night- and I'm sure it goes without saying, but it's better than stupid spaghetti."
    sa "Spa-!"

    scene showdown21
    with dissolve

    "Sana’s eyes light up when a plate of omurice shows up in front of her."
    "Omurice is-"

    play sound "dooropen.mp3"
    scene showdown21r
    with dissolve

    ay "Hm? Molly? What are you doing here?"
    mo "My hearthstone was off cooldown and I heard that Ami was making omurice, so I figured I'd drop by and pick some up!"
    mo "Here's a weebnote for you, Ayane- did you know that omurice is a Japanese comfort food made up of an omelette and, you guessed it- rice?"
    ay "...Yeah. Yeah, I knew that."
    mo "Did you also know that it’s a staple in not only many diners, but also places like maid cafes?"
    ay "Yup."
    a "Oh, hi Molly. I made an extra serving for you and put it in a container on the counter. You can just give it back to me in school, okay?"

    scene showdown21r2
    with dissolve

    mo "Thanks, Ami! Grats in advance on completing your quest for your uncle's heart!"

    play sound "dooropen.mp3"
    scene showdown21r3
    with dissolve

    ay "Well, that was weird."
    sa "This..."
    sa "This is...one of my favorite foods..."
    s "My vote is for Ami."

    scene showdown21r4
    with dissolve

    ay "Huh? But you haven't even eaten it yet. How can cheap diner food like that beat homemade pasta?"
    s "Ayane, I don’t think you understand."
    s "Ami’s been spending the last two months practicing this exact dish."
    s "I don’t know where her fascination with it came from, but I can assure you that she has all but perfected it."
    sa "I’m...going to start eating now..."

    scene showdown22
    with dissolve

    m "Yeah...sorry, Ayane."
    m "You're going to lose this one."

    scene black
    with dissolve

    "As expected, Ami’s omurice is out of this world."
    "It’s kind of like eating a pillow if pillows were made of eggs and covered in ketchup."
    "Weird comparison, I know. But I promise you, there is nothing more comfortable than this very dish..."

    scene showdown23
    with dissolve

    sa "I pick Ami."
    s "You know...maybe there {i}is{/i} a god after all?"

    scene showdown2
    with dissolve

    m "I can’t...not vote for it..."
    m "Even though it’s the same thing you picked..."
    m "Why is this happening to me?"
    a "Yay! This means I win round two!"
    ay "Don’t jump for joy just yet, Ami! We still have the dessert round!"
    ay "And I know exactly what these three need in order to finish this competition the right way!"

    scene showdown24
    with dissolve

    ay "Ladies and gentlemen! Ayane-fans around the world!"
    ay "Feast your eyes on a timeless classic!"
    ay "{i}You{/i} know it! {i}I{/i} know it! We {i}all{/i} know it!"
    ay "It’s-"

    scene showdown25
    with hpunch

    ay "One very large banana!"
    sa "…"
    s "…"

    scene showdown26
    with fade

    m "What the fuck is this?"

    scene showdown27
    with dissolve

    ay "Okay, so...I was kind of hoping that I would beat Ami in the first two rounds so I didn’t have to worry about dessert."
    ay "I’m...not really great at baking or...cooking any of that sweet stuff, so..."
    ay "The giant banana was really the only option."

    scene showdown26
    with fade

    m "How?"
    m "Why?"
    m "I have so many questions."

    scene showdown25
    with dissolve

    sa "What...are we supposed to do with it?"
    ay "Eat it like any other banana!"
    ay "Peel it! Dice it! Share it with friends!"
    ay "Go bananas!"
    m "I fucking hate you, Ayane."
    s "I don't think I want to eat this."
    sa "Yeah...I don’t really trust it..."

    scene black
    with dissolve2

    "Ayane wound up having to drag the banana outside while Ami finished preparing her desserts..."

    scene showdown12
    with dissolve

    a "Okay! So, I decided to do something fun for the dessert round and made something special for all three of you!"

    scene showdown29
    with dissolve

    a "For Sana, an entire box of doughnuts! And for Sensei, some leftover ice cream we had in the freezer!"
    a "It might not be much, but it still beats the giant banana! Ami wins!"
    a "Oh. And for Maya-"

    scene showdown30
    with hpunch

    m "!!!!!!!"
    m "I can’t move."
    s "Is Maya...actually smiling right now?"
    a "The easiest way to Maya's heart is with a watermelon. Remember that, Sensei."
    m "Ami, I can’t move. Help."
    a "She’s also easily paralyzed by excitement whenever someone surprises her with one!"
    m "I can’t feel my legs."
    a "It’s actually kind of cute, isn't it? She's like one of those goats that faint whenever they get scared."
    m "Ami, help. Please."
    m "Feed it to me."
    m "Feed me the melon."

    scene black
    with dissolve2

    "In the end, Ami was the clear winner of the first ever Arakawa vs Amamiya cookoff."
    "Would Ayane have had a chance if she had actually made a dessert? Maybe."
    "But I guess we’ll never know, will we?"
    "There is still one thing on my mind, though."
    "And it’s something I just can’t seem to shake no matter how hard I try."

    stop music

    "Just where the hell did Ayane find a banana that large?..."

    $ renpy.end_replay()
    $ day80 = True
    $ ami_love += 1
    $ ayane_love += 1
    $ sana_love += 1
    $ maya_love += 1
    stop music fadeout 6.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label day83:
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

    scene bedroom_day
    with dissolve2

    "{i}[totaldays] Days have passed...{/i}"

    if totaldays >= 24 and day24 == False:
        jump day24
    if totaldays >= 60 and day56 == True and aminew1 == True and aminew2 == False:
        jump aminew2
    if totaldays >= 80 and day72 == True and day80 == False:
        jump day80
...
```