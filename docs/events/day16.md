# Operation: Fallen Angel (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 16

* Event [The Unwavering Bravery of Ayane Amamiya](./firsttimedojo.md) (Ayane) is completed)



## Next events

* [Main: Cleaning Duty](./day36.md)

## Event properties

* Id: day16
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day16

## Official wiki page

[Operation: Fallen Angel](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day16&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day16:
    scene black
    with dissolve2

    "Time: 11:30 AM \n
    Location: Soccer Field \n
    Mission: Operation Fallen Angel"
    "........."
    "......"
    "..."

    play music "happyandplotting.mp3"

    scene newfallen1
    with dissolve2

    ay "Okay, Sana! Just like we practiced! Are you ready to do this?"
    sa "Umm...not really..."
    ay "Well, too bad! Because everything you have done in life so far has led up to this very moment!"
    ay "This might be the only chance you ever get to show everyone that you have the potential to be an Oscar winning actress!"

    scene newfallen2
    with fade

    sa "But...I don't even want to be an actress..."
    ay "What? But I think you'd be so great at it. All of our practices so far have gone really well."
    sa "Ayane...I don’t really know if this is a good idea..."
    sa "Sensei is smart, so...he'll probably see right through this..."

    scene newfallen3
    with fade

    ay "That's exactly why we've gotta sell it. But with how flawlessly our three practices have been, I doubt that will be an issue."
    sa "Is three...really enough? Maybe we should...practice a little more before...actually trying this..."
    ay "Sana, I need you to understand something for me."
    ay "If I have to wait even one more day to get closer to Sensei, I am going to literally blow myself up and take the entire school with me."
    sa "Please don't...my Switch is in there..."
    ay "Sana, we can do this. Just act natural."

    scene newfallen4
    with fade

    sa "That's a lot easier said than done..."
    ay "It’ll be fine! Don’t worry about it."

    scene newfallen5
    with hpunch
    play sound "whistle.mp3"

    s "Okay...I blew the whistle, so...I don't know. Go play sports or something."
    ay "Oh God. This is it. This is it. How do I look?"
    sa "Um...normal?..."
    ay "But I'm normally pretty, right? Sana, answer me. We're running out of-"

    scene newfallen6
    with hpunch

    sa "AYANE HAS FALLEN! THIS IS A TRULY TRAGIC EVENT!"
    ay "What?! Oh God! I wasn't ready!"
    sa "IS ANYONE HERE STRONG ENOUGH TO CARRY A YOUNG GIRL TO THE NURSE'S OFFICE?!"
    mi "I think I can probably-"
    sa "IS ANYONE {i}ELSE{/i} HERE STRONG ENOUGH TO CARRY A YOUNG GIRL TO THE NURSE'S OFFICE?!"

    scene newfallen7
    with fade

    ay "I am dying! Could this be the end for me?! But I am still so young!"
    sa "I MAY NEVER WALK AGAIN!"

    scene newfallen8
    with dissolve

    ay "Sana, no! That one was my line!"
    sa "AYANE MAY NEVER WALK AGAIN!"

    scene newfallen7
    with hpunch

    ay "I may never walk again!"
    s "What’s going on? What happened?"

    scene newfallen9
    with dissolve

    ay "Sensei?...Is that you?..."
    ay "Your voice sounds so...distant..."

    scene newfallen6
    with hpunch

    sa "THE LIGHT IS FADING FROM HER EYES!"
    s "Okay Sana, I’m going to need you to step aside for a moment."

    scene newfallen9
    with fade

    s "What happened? I feel like I looked away from you for one second."
    ay "As flattered as I am to know that you are always watching me, I really don't know..."
    ay "It is as if one moment I was talking about the decline of our current economy with Sana...and the next..."
    ay "The next thing I know...I can’t feel my legs..."
    ay "Sensei...am I going to die?"
    s "Maybe? I have no idea."
    ay "Can you...prevent me from dying?"
    s "I can carry you to the nurse’s office. That {i}is{/i} what you two were yelling about, isn't it?"
    ay "And you're always listening as well..."
    ay "I knew I could count on you, Sensei..."

    scene black
    with dissolve2

    "Knowing full well that something suspicious is going on, I lift Ayane off of the ground and bring her body close to my chest in a princess carry."
    "That does not stop a certain someone from carrying on the performance, however."

    scene newfallen10
    with fade

    sa "AYANE! WHY?! YOU WERE SO YOUNG AND HAD SO MUCH LEFT TO DO!"
    sa "I CAN ONLY HOPE THERE IS ENOUGH ROOM IN HEAVEN FOR ONE MORE ANGEL!"
    s "Sana is-"
    ay "Don't pay any attention to Sana. I am the one in need of medical assistance."
    s "Right..."
    ay "I'm sorry for being so heavy, Sensei...making you work this hard during gym class is something I will never be able to live down."
    s "You’re like 80 pounds."

    scene newfallen11
    with dissolve

    ay "Then that's 80 whole pounds worth of inconvenience for you..."
    s "..."
    ay "Sensei...what will I do if I can never walk again?"
    ay "Will you carry me everywhere for the rest of your life?"
    s "Absolutely not."
    s "I could push you around in a wheelchair from time to time, though."
    ay "I will take what I can get..."

    scene black
    with dissolve2

    "I carry Ayane into the nurse’s office, expecting to find...you know, a {i}nurse...{/i}but no one is there at all."
    "Which quickly makes it even more apparent that this was all some coordinated effort to get the two of us alone in here."
    "And while having Ayane pull a stunt like that doesn’t surprise me, the cooperation of Sana does."
    "Granted, calling Sana’s overacting “cooperation” might be a little generous, but it’s strange considering that she’d comply with a demand that very clearly...looks wrong."
    "I’m sure some of the other girls are thinking the same thing right about now. And I’m sure that’s something I should be worrying about."

    ay "..."

    "But I have a hard time worrying about anything at all while I’m so distracted by the intense gaze coming from the girl I’m carrying and her soft skin, still warm from soaking up the sun."
    "When I bring her to the back of the nurse’s office and close the curtain around us, the facade fades and she returns to her normal self."

    scene newfallen12
    with dissolve
    play music "behindabathroom.mp3"

    "Or perhaps her normal self never went into hiding at all."
    "Perhaps Ayane’s normal self {i}is{/i} pulling theatrical stunts to create small windows of opportunity for the two of us to climb through."
    "Perhaps she likes me so much that she’s willing to risk the way she appears to her classmates just so that I can whisk her away and lay her down on some presumably unfamiliar bed."
    "Perhaps that’s exactly what I like about her."
    "It’s hard to tell."
    "Because even if I can make lofty assumptions about the type of person she truly is and how every aspect of her somehow revolves around me-"
    "I know that the true center of gravity that she and all of the others are revolving around is somewhere far away from here."
    "And that they’re all just aimlessly drifting around at this point."
    "But that will not stop me from attempting to lasso her into my gravitational pull."
    "And that will not stop me from imagining the horrible things I’m imagining right now."

    ay "You didn’t buy that at all, did you?"
    s "I knew what was going on from the start."
    ay "Guess Sana’s Oscar is out of the question after all."
    s "What else did you expect when you cast the silent recluse in such a dramatic role?"
    ay "I couldn’t think of anyone else who would have helped me do what I was trying to do. It had to be Sana."
    s "Because she’s...okay with your incessant pursuit of me?"
    ay "I think it’s closer to that she doesn’t really understand right now."
    ay "She obviously knows I like you. {i}Everybody{/i} knows that much. But I don’t think Sana’s ready to acknowledge how {i}you{/i} feel just yet."
    s "Are you saying {i}you{/i} know how I feel?"

    scene newfallen13
    with dissolve

    ay "I’m saying that you walked right past a bed that {i}wasn’t{/i} curtained off so you could bring me in here."
    s "I just figured you’d want {i}medical assistance{/i} in private."
    ay "Sensei...can I ask you something?"
    s "Sure. Just ask quietly since we don’t know if anyone is listening in right now."
    ay "It’s only a matter of time until they start asking similar questions, but sure. I’ll stay quiet."
    s "What do you want to know, Ayane? It’s not often you let down the bubbly, eccentric persona to act all...serious like this."

    scene newfallen14
    with dissolve

    ay "I know. Having you hold me for so long made me want to start saying things that will get you to hold me again. So I’m sorry for just forcing this on you out of the blue."
    ay "The initial intention and the whole point of this stunt was to create an opportunity where I could kiss you."
    ay "And I’m still probably going to do that. "
    s "Oh?"

    scene newfallen15
    with dissolve

    ay "But what I want to ask {i}before{/i} I do that is..."
    ay "When did you start seeing me as a {i}girl{/i} and not just a “girl?”"
    s "I’m sorry, what?"
    ay "I know you don’t need that explained to you. The Sensei I love is smarter than that."
    s "You should probably clarify anyway as this could spiral out of control if I somehow misinterpret the situation and say the {i}wrong{/i} thing."

    scene newfallen16
    with dissolve

    ay "Fine...Fine. Okay."
    ay "What I’m asking is..."

    scene newfallen17
    with dissolve

    ay "Wait, do you want me to word it in just the...super blunt way? Or the way where I kind of tiptoe around what I’m trying to say, but still heavily imply it?"
    s "Just be blunt. It’ll save both of us some time."
    ay "Okay."
    ay "Then, when did you start thinking about me, like...sexually? Not just as Ami’s friend who hangs out at your house all the time."
    ay "Was it after the bathroom incident? Before that? I just want to know when."
    ay "Because I have been watching the way you look at me closely for years...and it wasn’t until recently that those looks started...you know, looking like they...look now."
    s "Am I allowed to counter that question with another question?"
    ay "Is it the same question as mine?"
    s "..."

    scene newfallen18
    with dissolve

    ay "Heheh...of course it is."
    ay "Unfortunately, I don’t really know when that started happening on my end. It was probably just a...natural development since I didn’t know where else to aim my hormones."

    scene newfallen17
    with dissolve

    ay "The bathroom incident definitely made it worse, though. I didn’t even sleep that night, did you know that?"
    s "I didn’t. Nor would I have expected it after you literally ran away."

    scene newfallen19
    with dissolve

    ay "Can you blame me?! Not only was that thing the size of my torso, but I told everybody I’d be back in a couple minutes!"

    scene newfallen20
    with dissolve

    ay "There’s also a huge difference between fantasizing about things and actually {i}doing{/i} them."
    ay "And I think if I’m acting weird and not like normal Ayane right now, it’s because that is finally starting to set in."
    ay "Seeing the way you look at me change as I grow up is, like...tricking my brain into thinking that a relationship like that is actually possible."
    ay "All this time, I’ve been saying all of that stuff about being in love with you in a joking manner because, frankly, the thought of anything ever coming from it {i}was{/i} just a joke to me."
    ay "Not in the sense that I didn’t want it, but in the sense that it just seemed impossible."

    scene newfallen21
    with dissolve

    ay "But now?"
    ay "Now, any time I say any of that stuff, it’s not really a joke at all. It’s a wish. And it’s a wish that seems more and more possible every time we’re alone together like this."
    ay "Now, at the risk of me saying anything else embarrassing, can you please tell me when your...thoughts on me started changing? "
    ay "And if they haven’t and I’m just an idiot, can you rip the bandage off while we’re in here? "
    ay "Because at least there’s disinfectant everywhere and I can...prevent this wound from getting infected or something."
    s "..."

    "Sure, let me just respond to a question I don’t have an answer for."
    "There {i}is{/i} no {i}one{/i} moment where the way I look at Ayane has changed from my perspective."
    "I have always viewed her in the light she assumes I’m viewing her in. And it’s not at all dissimilar from the one that lights up everyone else as well."
    "I have no reason to view her as “Ami’s friend” because, to me, she has always been the beautiful girl I see before me."
    "Of course, I can’t tell her that either. Because not only would it dispel my illusion as a vulture gorging himself on the scraps of relationships left behind by another animal-"
    "But it would damage her."
    "And I don’t want to risk this beauty being damaged in any form."
    "So, much like escorting her into a private section of the nurse’s office instead of keeping her out in the open-"
    "I will take the safe route."
    "And any bandages we have on ourselves will stay right where they are."

    s "I don’t really know either, Ayane."
    s "It just...kind of happened..."

    scene newfallen22
    with dissolve

    ay "I see..."
    ay "I guess we’re not all that different then."
    ay "..."
    s "..."
    ay "Welp, I guess that means there’s only one thing left to do."

    scene newfallen23
    with fade

    "Ayane brings herself closer  and I can feel the weight of years worth of unrequited feelings slipping into my nostrils and suffocating me with the invisible mass of a love I don’t deserve."
    "Of a love I wouldn’t call {i}love{/i} in the first place."
    "This is nothing more than hormonal lust consuming her like it’s the physical manifestation of a parasitic fungus trying to take control of her entirely."
    "Is she strong enough to fight it off?"

    ay "You have no idea how long I’ve wanted to do this."

    "Or has life simply become so worthless to her that she’d rather surrender herself entirely to the promise of someone or something acting out in her stead?"

    s "You’re right."
    s "I really don’t."

    scene newfallen24
    with dissolve2

    "Our lips meet and spores spread throughout her trembling body."
    "We remain stuck like that for somewhere between thirty seconds and two minutes."
    "I lose track of time as I must focus everything I have on not killing the host body before the fungus does."
    "If she does this to herself, it won’t be my fault."

    scene newfallen25
    with dissolve2

    "Which is why I do not run once her lips part."
    "Which is why my hands travel without obstacle to the mounds on the front and the back of her growing body."

    play sound "slidedoor.mp3"

    a "Hello? Is anyone in here?"

    "Which is why I do not stop even when our existence is threatened."
    "The worst that can happen is that we’re crushed underfoot. And if that {i}were{/i} to occur, we’d simply wind up as something else after an indeterminate amount of time."
    "I can tell she’s still growing."
    "I can tell there are still more spores to spread."

    a "Sensei?..."
    a "Ayane?..."
    a "Anybody?..."

    scene black
    with dissolve2

    "We remain behind the curtain with our tongues entangled until a girl who would break if she caught us disappears."
    "The thing is, Ami could have opened up that curtain at any moment. "
    "But she didn’t."
    "I don’t know if she’s just {i}that{/i} absentminded...or if she was afraid of what she would find. "
    "But we live to see another day."
    "I can’t guarantee it will be a brighter one-"
    "But we will see it nonetheless."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ day16 = True
    stop music fadeout 6.0

    "{i}Ayane's affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label day20:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

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
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
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

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
...
```