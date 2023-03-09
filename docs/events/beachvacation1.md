# What's Done is Done
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation1&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 174

✅Event "[Main: Lifting the Curse](./day154.md)" is completed (event=day154)

✅Event "[Ami: Back Out in the Heat](./amidorm15.md)" is completed (event=amidorm15)

✅Event "[Futaba: Legs of a Dying Spider](./futabadorm15.md)" is completed (event=futabadorm15)

✅Event "[Main: Scientific Research](./day79.md)" is completed (event=day79)

✅Event "[Makoto: Egg Tooth](./makotonew3.md)" is completed (event=makotonew3)

✅Event "[Kirin: Partners in Crime](./kirindate1.md)" is completed (event=kirindate1)

✅Event "[Tsuneyo: Snake Venom](./ramen1.md)" is completed (event=ramen1)

✅Event "[Molly: The Dark Entity](./mollydorm10.md)" is completed (event=mollydorm10)

✅Event "[Rin: Sock Fetish](./rindorm25.md)" is completed (event=rindorm25)

✅Event "[Sana: Supermom](./bar10.md)" is completed (event=bar10)

✅Day of week is Saturday



## Next events
None

## Event properties
* ID: beachvacation1
* Group: Main
* Triggered by label: saturdaymorning
* Triggered by branch label: saturdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label beachvacation1:
    scene bedroom_day
    with dissolve2
    play music "normalday.mp3"

    s "...Ngh."
    s "What time is it?"

    "I roll out of bed and clumsily reach for my phone on the end table and confirm that I've woken up significantly later than normal today."
    "It’s almost 10:00AM and I haven’t even gotten out of bed yet."
    "Normally, Ami would barge in and prevent me from sleeping in like this, but...I guess she has other things to do today?"
    "What gives?"
    "I would have invested in an alarm clock if I knew my [niece] would be this unreliable."
    "That’s right. This is all her fault."
    "I should go give her a piece of my mind."

    scene lr_day
    with fade

    "I walk out into the living room only to be met with another horrible reality. "
    "Breakfast isn’t ready either."
    "Is Ami dead?"
    "That is the only possible thing I could think of given these circumstances."

    play sound "knock.mp3"

    s "Ami, are you dead?"
    ay "Oh, Sensei is finally up!"


    if bonus == True:
        "Oh. I guess Ayane is over. "
        "I mean, that at least {i}kind of{/i} explains the lack of an alarm or breakfast...but I’m still not entirely convinced."

        ay "Sensei! Come in and hang out with us!"
        a "What? Wait a second! Don’t you dare-"

        "I decide to do what any sane man would do and barge into my [niece]’s room despite her plea for privacy."
    else:
        s "Good morning, Ayane. Would you be willing to inform me of whether or not Ami is okay? I do not want to barge in uninvited and am relying on you for an answer to my concern as I trust you dearly."
        ay "She is getting dressed right now, so please wait in the living room until that process is complete!"
        s "I understand and will do just that. Thank you for your help and I hope you have a blessed day."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        jump mayachangex
    else:
        "........."
        "......"
        "..."
        "{i}Several minutes later...{/i}"

label restofmayachange:
    scene beachintro28
    with dissolve

    ay "What’s everybody else saying? Are they there yet?"
    a "Umm...Well, Molly sent me a picture of a hermit crab, so I’m pretty sure her and Rin are there."
    a "Futaba, I haven’t heard from. And I don’t have Makoto’s number saved because I want her head to explode."
    ay "Yeah, that sounds about right."

    scene beachintro29
    with dissolve

    a "We’re gonna leave soon, right?"
    a "It would be a waste to start our vacation off halfway through the day when we’re only going to be there for two nights."
    s "I don’t even know where we’re staying yet."

    scene beachintro30
    with dissolve

    ay "Makoto and I took care of that already. She reserved the place and I used my credit card to pay for it."
    ay "We wound up getting two rooms but I hear the place is big, so we can probably all fit in one."

    scene beachintro31
    with dissolve

    if bonus == True:
        ay "The second room is just to be safe."
    else:
        ay "The second room is the one we're keeping all of the worms in."
        s "Neat."

    a "…"
    a "Why are you winking?"

    scene beachintro32
    with dissolve

    ay "No reason, my precious best friend. "
    ay "I promise you that the second room will only be used if we’re all unable to cram ourselves together in the first one."
    m "Or we could do the logical thing and have Sensei sleep in the second room."

    if bonus == False:
        s "Ew, no. There are worms in there."

    sa "I...agree with Maya..."

    if bonus == False:
        s "Sana wtf"

    sa "I’m not really comfortable sleeping in the same room as a boy..."

    if bonus == False:
        s "I am not comfortable sleeping in the same room as worms."

    scene beachintro31
    with dissolve

    ay "Don’t listen to them, Sensei. You can sleep in the bed with me."
    m "You mean the same bed Ami and I will also be sleeping in? Yeah, pass."

    if bonus == False:
        s "I will also pass. That sounds rather unsightly."

    ay "That’s fine. Maya can sleep on the floor and you can sleep between Ami and me."

    scene beachintro33
    with dissolve

    a "Well...I’d feel a little bad about Maya sleeping on the floor, but..."
    m "…"

    scene beachintro34
    with dissolve

    m "You’re kidding, right?"

    scene beachintro35
    with dissolve

    a "Or we could stick to the original plan and have you...not do that."
    ay "I don’t mind sleeping in the other room with Sensei."

    scene beachintro31
    with dissolve

    ay "There are two beds in there so it’s not like we’d be doing anything weird either."
    a "You’re winking again..."
    ay "Sorry. It’s just a reflex at this point."

    scene sky
    with dissolve2

    "The five of us decide to get up and go shortly after that."
    "We walk to the bus stop together and all manage to fit in the same row of two seats."
    "Ami forces Ayane away from me and takes a spot beside me while the other three sit across from us."
    "The bus ride to the beach takes about fifteen minutes."
    "Ayane tells me that Makoto will take me to the cabin/resort/whatever the hell we’re staying at once we all meet up there."
    "So I guess for now it’s just...managing to survive the trip to the beach?"

    scene black
    with dissolve
    stop music fadeout 10.0

    "………"
    "……"
    "…"

    "{i}Welcome to the first special update for Lessons in Love!{/i}"
    "{i}Over the next two days, all events will play in succession.{/i}"
    "{i}You will not have free time to do as you please, but you’ll still be able to raise your affection with everyone over the course of vacation.{/i}"
    "{i}So sit back, relax, and enjoy this mostly-wholesome beach adventure!{/i}"

    $ renpy.end_replay()
    $ beachvacation1 = True

    "………"
    "……"
    "…"

label beachvacation2:
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
    if totaldays >= 102 and day == 7 and day96 == True and mayadorm15 == True and letterttrack == True and howifeeltrack == True and day102 == False:
        jump day102
    if totaldays >= 174 and day154 == True and amidorm15 == True and futabadorm15 == True and day79 == True and makotonew3 == True and kirindate1 == True and ramen1 == True and mollydorm10 == True and rindorm25 == True and bar10 == True and day == 6 and beachvacation1 == False:
        jump beachvacation1
...
```