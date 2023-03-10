# One to Seven (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 63

* Event [Delirium](./rindorm20.md) (Rin) is completed)



## Next events

* [Main: Stronger I Become](./day91.md)

## Event properties

* Id: day63
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day63

## Official wiki page

[One to Seven](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day63&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day63:
    play music "10c.mp3"
    scene daysixthree1
    with dissolve

    "You know, back when I woke up here for the first time and realized that I was going to be spending every day surrounded by teenagers...I don't think I understood exactly how {i}loud{/i} that was going to be."
    "I also don't think I understood exactly how long school days carry on for either. Because even though we're only one hour into this one, I am already clocked out for the day."
    "Granted, I double-punch my metaphorical time card every time I show up to school, so I guess you can say that I've been clocked out since I got here."
    "Either way, when I first decided to just take on this job instead of going out and finding a new one, I thought it would be kind of fun."

    if bonus == True:
        "I thought I’d spend my days flirting with [high_school] girls and manipulating them into eventually performing sex acts with and/or on me."
        "And while there is absolutely a semblance of truth to that, the overwhelming majority of my time is just...this."
    else:
        "I thought I’d spend my days playing air hockey with other teachers and occasionally bumping shoulders with a cute girl as I walk down the hall."
        "And while that is most definitely true, there's still a lot of downtime."

    "I can't even make it through a single morning without something exhausting happening."

    scene daysixthree2
    with dissolve

    ay "Sensei! Do you want any pizza?"

    "Do you see what I mean?"

    s "Ayane, it’s 9:00 in the morning."
    ay "So?"
    s "Where did you even get a pizza that early?"
    ay "I had Geoffrey make it and drive it over during homeroom. Did you not see the entire convoy of limos outside?"
    s "Why did you need an entire convoy for one pizza?"
    ay "I don't know. Ask Geoffrey."
    ay "Anyway, after the first slice, I realized I’m not even that hungry. So if you want any, just let me-"
    s "I don’t want any pizza, Ayane."
    ay "Okay. I'm just going to go back to stabbing it then."
    s "Sure. You do that."

    scene daysixthree1
    with dissolve

    "So...this is basically my life now."

    if bonus == True:
        "School is boring. So boring that I often think I wouldn't even bother showing up if there weren't so many skirts all over the place."
        "In fact, I can pretty confidently say at this point that is the {i}only{/i} reason I would understand someone keeping this job."
        "Maybe there is some real joy in teaching that I just don't understand (Likely on account of not having {i}tried{/i} that yet)..."
        "But overall, I'm going to give this job a 6/10. I'm much more suited for something like...what Makoto does."
        "Which is funny since she's much more suited for what I do."
        "I wonder if she'd be okay with switching every now and then?"
    else:
        s "I changed my mind. I want pizza now. I was just being stubborn."

    play sound "slidedoor.mp3"
    scene daysixthree3
    with dissolve

    "The sound of the classroom door sliding open pulls me away from a relatively unethical inner monologue."

    c "Hey! Long time, no see! You feeling okay now?"
    r "Hey! Morning, Chika. "
    r "And yeah! I'm totally fine. No worries here! Are you doing, uhh...you know...the word?"
    c "Good?"
    r "Yeah! Well...technically I think it's {i}well.{/i} But I'm just gonna assume you're both of those things so I don't sound any more awkward than I am sure I sound right now!"

    "Good..."
    "It looks like Rin’s {i}slump{/i} is over and she's finally ready to start coming to class again..."

    scene daysixthree4
    with fade

    r "Hey! Sorry I’m late! There was some little girl outside the[school] who lost her cat, so I was helping her look for it and whatnot."
    s "Rin...do you really think I care about you being late?"

    scene daysixthree5
    with dissolve

    r "Nope! But as a born-again student, I am obligated to inform you of my tardiness whenever possible."
    r "Please have mercy on my unfortunate soul and do not give me detention. "
    s "…"
    r "…"
    s "Welcome back, Rin."

    scene daysixthree5r
    with dissolve

    r "Thanks, Sensei. Believe it or not, you were a big help."
    s "Well, I’m glad you’re feeling better."
    r "Same."
    r "Let's just hope it lasts this time."

    scene daysixthree6
    with dissolve

    "Rin skips her way over to her desk and Futaba immediately turns her chair around to talk to her."
    "I’m sure Futaba knew that she’d be coming back soon, but it’s still cute seeing how excited she gets knowing that her friend is feeling better."
    "Or, at the very least, {i}acting{/i} better."
    "It's impossible to know for sure, isn't it?"

    r "Mornin', roomie! How lonely were you without me on a scale of one to seven?"
    f "Maybe...a six?"
    r "A six? Not a seven? Who are you and what have you done with my Futaba?"

    if bonus == True:
        r "Wait...don't tell me Sensei corrupted you while he was away, did he?!"
    else:
        r "Did you two start hugging while I was away?"

    r "Do you even need me anymore?!"
    r "What is my life coming to?!"
    f "Heheh...Okay, fine. A seven. "
    f "How are you feeling today?"
    r "Like a box of chocolates! Or...however the saying goes."
    f "It...doesn't go anything like that at all."
    r "Well, whatever. I’m feeling pretty good!"
    r "Oh, also- I talked to Haruka this morning and she said she's gonna start giving me overtime to make up for some of the cash I missed out on during my sad-Rin phase."
    r "Soooo...if you still want to go to that convention next month, I’m totally down."

    "Convention?"
    "If Futaba is the one who's excited to go, I’m sure it's some sort of...sci-fi convention or something."

    if bonus == True:
        "With conventions comes cosplay..."
        "And with cosplay comes the opportunity to see the two of them in potentially revealing outfits that I may never have an opportunity to see again."
        "This is a conversation I must now be a part of."
    else:
        "It's nice that the two of them have both the time and money required to enthusiastically participate in their hobbies."

    scene daysixthree7
    with fade

    r "Woah! Back already? I get that you missed me, but could you at least let me catch up with Futaba first?"
    f "Good morning, Sensei. How are you today?"
    s "I’m fine. I just came over to hear about whatever convention thing you two are talking about."

    scene daysixthree8
    with dissolve

    r "And now you're eavesdropping on our conversations?! What if we were talking about boys?! Then what, Sensei?! Then what?!"
    s "Then you should have been talking quieter. I could hear you two from the other side of the room. That basically makes me a part of the conversation as well."

    scene daysixthree9
    with dissolve

    r "{i}Psst, Futaba...{/i}"
    f "You...know he can still hear you, right?..."
    r "{i}Should we tell him about the thing? I wanna tell him about the thing.{/i}"
    f "Umm...I don’t see the harm in it...I just...don't know if he'd be interested..."

    scene daysixthree9r
    with dissolve

    r "Sensei, it has come to my attention that I am now able to inform you that Futaba and I will be attending a book convention. Please hold your applause."
    s "Why...would I applaud that?"

    "That's a little unfortunate...and significantly more boring than I was hoping for."
    "I don't have anything against books. And I'm sure there will be {i}some{/i} costumes there...but I doubt it will be on the level of a sci-fi or anime convention."

    r "Hey, man. Sometimes, people just want to clap. Figured you might be one of those people."
    f "I...normally have to drag Rin along to these conventions with me since...I buy too much and have trouble carrying everything."
    s "I'm not surprised, knowing you. What other stuff is there to do at a book convention, though? With all due respect, that sort of thing doesn't sound very...exciting."

    scene daysixthree9r2
    with dissolve

    f "You haven’t been to one, Sensei?"
    s "Not to my knowledge."

    if futabadorm15 == True:
        scene daysixthree10
        with dissolve

        f "That’s a little surprising..."
        f "I figured that...with being such a good writer and everything...you'd have gone to at least one."

        scene daysixthree11
        with dissolve

        r "..."
        s "...Is there a problem, Rin?"
        r "Problem? No. Just...have you guys been getting to know each other better lately?"
        s "We have. I’ve been helping Futaba with her self-confidence."

        scene daysixthree12
        with dissolve

        f "What he's {i}actually{/i} been doing is helping me with my writing...but I guess the...self-confidence is a side effect of that..."
        f "It's really just a lot of...story critique in the library and whatnot..."

        scene daysixthree13
        with dissolve

        r "Oh. Cool. Yeah. That's...really cool."
        s "..."

    else:
        scene daysixthree7
        with dissolve

        r "Dude, you should totally go to one! They’re a lot more fun than they sound, I promise!"
        f "Umm...I...actually think they sound really fun, so..."

    s "So where is this thing? It’s in Kumon-mi, right?"

    scene daysixthree14
    with dissolve

    r "I mean...it’s not like we can really go anywhere else."
    f "They change the venue every year, but I'm pretty sure it's being held somewhere in the urban district this year."
    f "I haven't checked in a little while since I was starting to think I wouldn’t make it this year."
    r "Cause of me, obviously. She's talking about me."

    scene daysixthree15
    with dissolve

    f "I-I didn’t mean it like that! I'm sorry! I-"
    r "Dude, it’s fine. I’m just kidding around."
    r "If I can’t laugh at the shitty parts of myself, there's pretty much no point in living at all. So just humor me when I say stuff like that. "
    r "Truth be told, if it weren’t for you and Sensei, I’d probs still be staring off into space in the dorm."
    r "So...thanks for being there for me and stuff."

    scene daysixthree16
    with dissolve

    f "Umm...I’m sure I can speak for both of us when I say this, but-"
    f "We’re glad to have been there for you."
    f "Sensei was really worried, you know? I don’t think I’ve ever seen him look like that before."

    scene daysixthree17
    with dissolve

    r "Oh?..."
    s "...What? Don't look at me like that."
    r "Were you really that worried about me, Sensei?"
    s "Do you think I would have visited you if I wasn’t?"
    s "I might be the world’s worst teacher, but even I get a bit mystified when one of my students suddenly disappears for an extended period of time."
    r "Tell the truth. You probably just missed my top-tier customer service and delicious custom beverages, right?"
    f "Oh yeah...Rin told me you volunteered to be her, umm...what did she call it?"
    f "Guinea pig?..."
    s "That’s correct. So if I suddenly die, please inform the police that she is a prime suspect."
    r "Oh please. As if I'd leave any evidence that could be traced back to me. Who do you take me for, Sensei?"
    s "A...psychopath?"
    r "A psychopath who {i}gets the job done...{/i}"
    s "You really worry me sometimes, you know."
    r "Obviously. Isn't that how this whole thing started?"
    s "So, Futaba...will there be any cosplayers at this book convention thing?"

    scene daysixthree17r
    with dissolve

    f "Is...cosplay something you're actually interested in, Sensei?"

    if bonus == True:
        s "I think I can safely speak for all men when I say {i}absolutely.{/i}"
        r "Dear diary...Today, I learned about one of my teacher's fetishes."
        s "I am not ashamed to admit this."
        r "Let me guess...you only came over here to find out if we’d be cosplaying...You don't care about those poor, little books at all."
        s "..."
        r "..."
        f "..."
    else:
        s "Maybe a little bit. I've always wanted to try on spandex but I'm self conscious about the size of my legs."
        r "Is it because you think they look like oversized Twinkies?"
        s "Wha- no! O-Of course not..."

    s "What an absurd accusation."
    f "Your face...says otherwise, though..."
    s "Futaba, don't go along with her. You're supposed to be the nice one."

    scene daysixthree18
    with dissolve

    r "Wait a second! Does that imply that I'm the mean one?!"
    r "Do you actually hate me now?! I thought we had a thing, Sensei! {i}I thought we had a thing!{/i}"
    f "I don’t think Sensei hates you, Rin..."
    f "You're just...not as nice as me. Which is fine. Because we all love you anyway."

    scene daysixthree19
    with dissolve

    r "And now I'm being consoled?! Just what kind of alliance did you two form while I was away?!"

    scene black
    with dissolve2

    "I wind up chatting with Rin and Futaba until the bell rings for lunch."
    "As it turns out, there are going to be {i}some{/i} cosplayers at the book convention they're going to, but neither of them plan on joining in this time."
    "Shame. I feel like even I would have shown up if things were a little different."
    "But I digress..."
    "At the end of the day, I’m glad that Rin seems to be back to her ‘usual’ self...whatever that means."
    "I just hope I don't have to see her break down again any time soon..."
    "For both her sake {i}and{/i} Futaba's sake."

    $ renpy.end_replay()
    $ day63 = True
    $ rin_love += 1
    $ futaba_love += 1
    stop music fadeout 4.0

    "{i}Rin's affection has increased to [rin_love]!{/i}"
    "{i}Futaba's affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump afterschoolevent

label day65:
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
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
...
```