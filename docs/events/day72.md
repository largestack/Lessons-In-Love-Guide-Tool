# Weight Limit
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day72&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 72

✅Event "[Main: The 'S' Word](./day70.md)" is completed (event=day70)



## Next events
* [Main: Secret Ingredient](./day80.md)
* [Futaba: Great Burdock Leaves](./futabanew2.md)

## Event properties
* ID: day72
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day72:
    scene weightlimitredux1
    with dissolve
    play music "happyandplotting.mp3"

    "Gym class has ended for the day and I’m staying after with Ami to help clean the place up."
    "Normally, this would be the part where all of the girls run off to the showers, but a certain {i}incident{/i} today has prompted me to select at least one person to clean brain matter off of the floor."
    "And what better person to collect brain matter than my niece?"
    "Now, I'm sure you're looking for an explanation...and I will give you one. But whether you decide to believe it or not is up to you."
    "While dropping by the gym to get something out of the storage room, one of the[school]’s janitors was pelted in the head by a dodgeball."
    "Normally, a grown man would be able to shrug something like this off and just get on with his day after a minute or two."
    "However-"
    "This particular dodgeball had been moving at the speed of a major league player’s fastball."
    "And while I'd like to say the janitor died on impact, he writhed in pain for a full five minutes or so before going silent."
    "There was blood everywhere."
    "And of course {i}I{/i} had to be the one to clean it up on account of us now being down one janitor."

    scene weightlimitredux2
    with dissolve

    a "It's crazy that this isn't even the first time something like this has happened, huh?"
    s "It's not?"
    a "No. This is like the third janitor Ayane has accidentally killed this year."
    s "How does she have that much arm strength? And why hasn't she been put in jail yet?"
    a "I don't know. She's rich, so that probably has something to do with it."
    s "Fair enough."

    scene weightlimitredux3
    with dissolve

    a "So, where should I be putting all of these mats?"

    if day68 == True:
        s "The storage room. Just try not to pay any attention to any stains on the floor."

        if bonus == False:
            s "I spilled my apple juice in there the other day and I didn't tell anyone about it because I was scared I'd get in trouble."

        a "Um...okay?"

    else:
        s "The storage room is fine. Just make sure you don’t leave any of them out again. The staff got pissed off that we didn’t do a great job last time."
        a "Mhm! I’ll make sure to get everything this time. Don’t you worry, Sensei."

    s "Before you go, though- there's something I've been meaning to ask you."

    scene weightlimitredux4
    with dissolve

    a "There is? What is it?"
    s "Well...it's less of a question and more of a demand."
    a "Sensei, if you want a hug that badly, all you have to do is ask."
    s "I don't need a hug, I need you to do me a favor."
    a "Hugs can be favors too, Sensei."
    s "Ami, I don't want a hug."
    a "I think you do, but sure. Go on with your non-hug related favor."
    s "It's about the cooking competition thing with Ayane."
    a "You mean about how I’m going to beat her so badly that she’ll stop cooking for the rest of her life?"
    s "Well, no. But I admire the confidence."
    a "Of course I’m confident. I know everything you like. I’ve trained my whole life for this."

    if bonus == True:
        a "I’m not gonna lose just cause Ayane wants to raise an army of children with you."
    else:
        a "I’m not gonna lose just cause Ayane thinks she likes you more than me."

    s "That’s great. But what I'm referring to is the imbalance in terms of judges."
    a "But...you're the only judge, aren't you?"
    s "No. Sana is coming as well and she'll be serving as a secondary judge."

    scene weightlimitredux5
    with dissolve

    a "What? Since when? Why hasn't anyone told me about this?"
    s "I may have...forgotten to mention it. But it's happening."
    a "Won’t she be biased, though? Her and Ayane are really close."
    s "Right. But I’m biased toward you since I eat your food literally every day."

    scene weightlimitredux6
    with dissolve

    a "So...what should we do?"
    s "Obviously, we need to call in a third judge."

    scene weightlimitredux7
    with dissolve

    a "A third judge..."
    a "Well, umm...I guess I could see if Maya wants to come over?"
    s "Great. That’s exactly who I had in mind."

    scene weightlimitredux8
    with dissolve

    a "Is that why you don't want to hug me? Because your mind is fully consumed by Maya?"
    s "If I say yes, will you still make me dinner every night?"
    a "I will. But I can't guarantee there won't be poison in it."
    s "Harsh."
    a "So, is the favor complete? Can I go back to cleaning now?"
    s "Yes, you may proceed. And thanks for being so understanding, Ami."

    scene weightlimitredux9
    with dissolve

    a "Any time. I'll wind up winning no matter how many judges we have, so I'm not worried at all."
    a "Don't feel pressured to wait up for me if I take too long, Sensei! I've gotta shower after this anyway."

    scene weightlimitredux1
    with dissolve

    "Ami runs off and images of the forbidden territory known as the girls' shower room consumes my mind and prevents me from cleaning at all for the rest of the period."

    scene black
    with dissolve2

    "As I sit with my hands still caked in the dried blood of a custodial worker, I think of a land where breasts roam free."
    "A land where no harm befalls anyone..."
    "The closest thing to Heaven this earth can offer."

    s "..."

    "And I am stuck out here..."
    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    if bonus == True:
        jump showersx
    else:
        scene black
        with dissolve2
        stop music fadeout 5.0

        "Guess the event ends here and that nothing else happens..."

        $ renpy.end_replay()
        $ day72 = True

        "………"
        "……"
        "…"

        jump afterschoolevent

label day77:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
...
```