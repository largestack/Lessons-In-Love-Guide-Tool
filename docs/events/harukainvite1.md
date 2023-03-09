# Shades of Green
Haruka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukainvite1&go=Go)



## Event preconditions
✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)



## Next events
* [Haruka: Roses](./harukainvite2.md)

## Event properties
* ID: harukainvite1
* Group: Haruka
* Triggered by label: harukainvite
* Triggered by branch label: inviteover

## Event code
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukainvite1:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "I’ve been to her place several times now, so I figure it’s about time to show her the same sort of hospitality she’s shown me."
    "That and I feel kind of bad since she’s always talking about how lonely she is and whatnot."
    "But hey, we’ve been gradually getting closer with one another lately. "
    "And she’s one of the few people I know that I don’t feel strange about being seen in public with."
    "Sure, Ami will likely react the same way she reacted when Sara came over for the first time, but it’s not like I’m going to just avoid everyone because of that."
    "Besides, Ami and Sara {i}did{/i} get along by the end of that visit."
    "I’m sure something similar will happen with Haruka."

    play sound "phonebeep.wav"

    h "Hey! What’s up?"
    s "Hey, Haruka. Do you have any plans tonight?"
    h "Does eating an entire pint of ice cream count as a plan?"
    s "Not really, no."
    h "Then I’m totally free. Why?"
    h "Do you want to hang out?"
    s "I do. How would you feel about coming over to my place for a change?"
    h "Your place? Isn’t that on like, the opposite side of town?"
    s "Don’t you have a car?"
    h "Yeah but...gas."
    s "That sounds like a very minor struggle compared to me taking the bus to your place all the time."
    h "Then you should get a car, too!"
    s "But...gas."
    h "Hahaha~ Okay, okay. I’ll come over."
    h "Can you text me the address?"
    s "Sure thing. See you soon."
    h "Yup! See you!"

    play sound "phonebeep.wav"

    "I hang up and immediately type out my address to Haruka, who responds with a quick thumbs-up."
    "From this point on, the night becomes a mission with the objective of only partially ruining Ami’s life rather than full on destroying it."

    scene black
    with dissolve
    stop music fadeout 5.0

    "You see...in her eyes, each new woman that shows up is another obstacle separating the two of us."
    "And, in addition to being much closer to my age, Haruka possesses one other thing that is sure to set Ami off almost immediately."
    "………"
    "……"
    "…"

    scene harukafirstinvite1
    with dissolve
    play music "normalday.mp3"

    s "Your boobs really {i}are{/i} huge, Haruka."
    h "Dude. What kind of greeting is that?"
    h "You haven’t even said hi yet."
    s "Sorry. I wanted to, but it’s been getting a lot harder keeping my thoughts to myself lately."
    h "That sounds like something that could get you into serious trouble someday. "
    h "Like, what if I got super offended by that and stormed out of here?"
    s "Would you have preferred if I called them small?"

    scene harukafirstinvite2

    h "I would have preferred if they were never the conversation topic to start off with."
    s "Oh, okay. I think I’m starting to see the issue."

    scene harukafirstinvite3
    with dissolve

    h "I sure hope so. I kind of directly pointed it out for you."
    h "It’s one thing to stare, which you’ve...very obviously been doing this entire time, but coming out and talking about them isn’t exactly polite."
    h "Like, you don’t see me walking in and being like “Wow...Your shoulders are so broad and you’ve got the figure of an ancient roman warrior.”"

    if bonus == True:
        h "“And your hands look like the perfect size for...grabbing a girl by her wrists and...”"
    else:
        s "Please say things like that when you walk in. They will make me feel better about myself. Between you and me, I am very insecure."

    scene harukafirstinvite4
    with dissolve

    h "Yeah I’m just gonna stop talking before I say something else that makes me sound like a creep."

    if bonus == False:
        s "This is why I am so insecure."

    s "Looks like I’m not the only one having trouble keeping my thoughts to myself."
    h "I spend so much of my time inside the cafe that I’m beginning to struggle in the outside world."
    h "I think it might be time for an intervention or something."
    h "Please save me from myself, Sensei."
    s "Uhh, sure."
    s "Where do you want to start?"

    scene harukafirstinvite5
    with dissolve

    h "What do you mean? "
    h "Do you not have a plan or anything for tonight?"
    s "I've gone to your house a bunch of times and {i}you've{/i} never had a plan. We always just sit there and watch TV."
    h "Duh. That’s my default setting. "
    h "If nobody drags me out of the house, I’ll just do that every day for the rest of my life."
    h "I kind of need somebody to lead the way or I’ll turn into a giant, pink blob who can recite all nine seasons of The Office by heart."
    s "That show isn’t even funny. "
    h "The only people who say that are contrarians or those who think they’re somehow too good for it because it doesn’t appeal to their {i}superior intellect{/i}."
    s "This sounds like a topic you feel very strongly about."
    h "I’m tired of people pretending The Office isn’t funny. They should all die."
    s "…"
    s "Okay, well anyway...I guess we can just watch TV since that seems to be the entirety of your comfort zone. "
    s "But there is something I should warn you about beforehand."
    h "You don’t have one of those doors that I’m not supposed to open under any circumstance, do you?"
    s "What? No. "
    s "Why would you assume that?"

    scene harukafirstinvite6
    with dissolve

    h "If there’s anything I’ve learned from all that time I’ve spent in my “comfort zone,” it’s that the people you {i}don’t{/i} expect to have secret doors are always the ones that actually have them."
    h "But...I guess you seem kind of like you’d have one. So that means there shouldn’t be one here after all."
    s "Did you make the insult extremely elaborate on purpose or was that just accidental?"
    h "A mixture of both, I guess?"

    scene harukafirstinvite7
    with dissolve

    h "So, what’s the thing you need to warn me about? "
    h "You’re not just renting this place out from some creepy old guy who’s going to walk out of his room in nothing but his boxers, are you?"
    s "Again with the strange assumptions..."
    s "The warning is that I’m not sure where my [niece] is today and she could come home at any moment."

    scene harukafirstinvite8
    with dissolve

    h "Then why didn’t we just chill at my place?"
    h "I’m going to feel really awkward if she just comes in and sees us hanging out when I’ve never even met her before."

    play sound "dooropen.mp3"
    scene harukafirstinvite9
    with dissolve

    a "Who are you and why are your boobs so big?!"
    h "See? This is totally weird for me now."
    s "Ami, this is Haruka. She’s a friend of mine."
    a "That still doesn’t answer the second question!"

    scene harukafirstinvite10
    with dissolve

    if bonus == True:
        h "Is mentioning the size of someone’s chest a thing your entire family just...does for some reason?"
        s "I guess. But I do it out of interest and Ami does it out of jealousy."
    else:
        h "If she continues, I am going to melt her."
        s "Please don't."
        h "I have special melting powers."
        s "Haruka no."

    a "People like you make me sick..."

    if bonus == True:
        a "Using their bodies to seduce my [uncle] when everyone is FULLY AWARE that he likes smaller girls like me!"
        h "Really? Is that true?"
        a "Yes! The smaller, the better!"
        s "Okay, moving right along."

    scene harukafirstinvite11
    with dissolve

    h "I don’t think she likes me very much."
    s "She’s like an animal. She’ll warm up to you the more she sees you."
    a "I’ve seen her plenty of times. That’s the cafe lady."

    if bonus == True:
        a "Rin always talks about how great her boobs are."

    scene harukafirstinvite12
    with dissolve

    h "Okay, people seriously need to find other things to say about me. This is getting obnoxious."
    s "At least none of them are hiding their true feelings."
    h "I kind of wish they would."

    if bonus == True:
        h "Though, it {i}is{/i} nice hearing that secondhand affirmation from Rin. Thank you, Sensei’s [niece]."
        a "She doesn’t even know my name..."
        s "I’m pretty sure I’ve told it to her before."
        s "She’s likely just being rude to you since you’re being rude to her."

    scene harukafirstinvite13
    with dissolve

    a "What ever happened to Sara?! She was much nicer to me and her boobs were way smaller!"
    a "Did you cast her aside for a discount on coffee?! We have coffee at home!"
    h "Sara’s been here already?"
    s "Yeah, I invited her over a while back. "
    h "I see..."
    s "Ami, if you want to see Sara, you can just go visit her at the bar."

    if bonus == True:
        a "And do what?! Drink Shirley Temples and talk about what things were like in the old days?!"
        a "I’m not even old enough to drink, jerk!"
        s "Then go with Molly. That’s never stopped her."
    else:
        a "No one likes me! I have no one to go with!"
        s "Molly likes you, I think."
        a "Molly has work so I {i}can't{/i} go with her!"

    scene harukafirstinvite14
    with dissolve

    h "She’s off today, so you probably could."

    if bonus == True:
        h "Molly got paid this week and I’m pretty sure Sara wouldn’t mind selling to anyone underage as long as it meant profit for her."
        a "I appreciate the tip but I don’t even like alcohol and I definitely do not feel safe leaving your awesome boobs alone with my [uncle]."
        h "Wow...[teenage]girl chest-envy really is alive and well, huh? "
        h "It’s a shame, too. You’re such a cute girl. "
        h "Having boobs this size would make your proportions all weird and your [uncle] probably wouldn’t even talk to you anymore."

        scene harukafirstinvite15
        with dissolve

        a "M-My proportions would obviously change along with them!"
        a "Nobody gets huge boobs without...the rest of their body growing, right?!"

        scene harukafirstinvite16
        with dissolve

        a "But...wait. Uta’s boobs are still growing and she’s even shorter than me..."
        a "Would I really...look weird if..."
        s "I can’t believe I’m saying this, but let’s stop talking about boobs for a second."

        scene harukafirstinvite17
        with dissolve

        h "Hah...{i}Finally{/i}..."
    else:
        a "Nevermind! Maybe I {i}will{/i} go with Molly!"

    scene black
    with dissolve

    "Ami kicks her boots off at the door and tosses her scarf onto the couch, immediately taking a place beside Haruka right after."

    if bonus == True:
        "Likely to protect me from the allure of her huge boobs."

    scene harukafirstinvite18
    with dissolve

    a "How long is she staying for?"
    h "As long as I want. Right, Sensei?"
    a "I’m not asking {i}you{/i}, cafe lady. I’m asking my [uncle]."
    s "As long as she wants."
    a "And that car parked outside of the house, is {i}that{/i} hers too?"
    h "Yup! That’s mine."
    a "I’m asking-"
    s "Yes. That is Haruka’s car."

    scene harukafirstinvite19
    with dissolve

    a "Hah. Owning a car in an urban area like Kumon-mi? Sounds a lot like overcompensation to me."
    h "Nah. I just had some extra money to spare and needed a way to commute back and forth between {i}my own apartment{/i} and my {i}independently owned business{/i}."
    a "Joke’s on you. I’m perfectly content living with my [uncle] and working part time at a place with super cute outfits instead of ugly green visors."

    scene harukafirstinvite20
    with dissolve

    h "Hey! That shade of green was the result of an informed decision based on years of experience in marketing and service!"
    h "Green and brown are earthy colors that create a relaxing atmosphere! "
    h "Also, your sweater is like the same exact shade of green as the one in the cafe!"

    scene harukafirstinvite21
    with dissolve

    a "Nuh-uh! How can you even {i}get{/i} a business license if you can’t tell the difference between your ugly shade of green and OLIVE?!"
    s "Wow. You two are getting along even better than I thought you’d be."

    scene harukafirstinvite22
    with dissolve

    a "What do you see in this woman, Sensei?"
    s "I-"
    h "If you say my boobs, I’m going to kill you."
    s "...I wasn’t going to say that."
    s "I was going to talk about how down to earth and chill you are."

    scene harukafirstinvite23
    with dissolve

    s "Ami, you don’t have to like Haruka, but what will being mean to her do at this point?"
    s "The two of us are already friends, so it’s not like you’re going to get in the middle of that."
    a "But if I’m mean to her and make her feel really weird, she won’t want to come back and hang out with you again."
    h "She’s got a point. This isn’t very fun."
    s "Yeah, but then that would just mean I’d be going to her place instead. Doesn’t that sound even worse?"
    a "You wouldn’t..."
    s "I already have."

    scene harukafirstinvite24
    with dissolve

    a "You have?!"
    s "Of course. It’s not like I just saw her at the cafe one day and said, “Hey, wanna head back to my place?”"
    a "Isn’t that exactly how adults meet each other nowadays?!"
    h "I mean, that’s {i}kind of{/i} what happened."
    h "I gave him my number under the pretense of checking on Rin when she was feeling down, but I really just wanted him to call me so we could get to know each other."
    h "Looks like my plan worked out really well, huh? "
    h "I’m already meeting the family and everything."
    h "Is there a dog I can pet anywhere? A cat?"

    scene harukafirstinvite25
    with dissolve

    h "Should I just pet this thing instead? She seems kind of feisty."
    h "She doesn’t bite, does she? Cause if she does, I’ll sue."
    a "That head is reserved for my [uncle]! I didn’t give you permission to touch me!"
    h "I’m bigger and stronger than you. Try and stop me~"

    scene harukafirstinvite26
    with dissolve

    if bonus == True:
        a "Sensei! Stop her! I’m being sodomized!"
        s "Where did you even learn that word?"
        h "Please. If I was sodomizing you, {i}you’d know it.{/i}"
    else:
        a "Sensei! Stop her! I am melting!"
        h "Feel my wrath, accountant."

    s "Haruka, that’s terrifying."
    h "What? She started it."
    h "I’m just trying to enjoy my time as an intruder here since we were so {i}rudely{/i} interrupted."
    a "I literally live here! Nothing I do is an interruption!"

    scene black
    with dissolve2

    "Haruka and I spend the next couple hours talking in the living room while Ami sits on the couch across from us, staring at her the entire time."
    "Despite the death glare, however, Haruka remains completely unfazed- which I’m sure makes Ami even angrier."
    "I guess there was no way this visit could have ended as successfully as the one with Sara, but it definitely...could have been worse, I guess?..."
    "No one died. And that’s really all I can ask for when it comes to things like this."

    $ renpy.end_replay()
    $ harukainvite1 = True
    $ haruka_love += 3
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label harukainvite2:
...
```

## Code that triggers this event
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukainvite:
    if harukainvite1 == False:
        jump harukainvite1
...
```