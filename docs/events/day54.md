# The Sakakibara Diet
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day54&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 54



## Next events
None

## Event properties
* ID: day54
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day54:
    scene hall_day
    with dissolve
    play music "normalday.mp3"
    play sound "slidedoor.mp3"

    "I exit the teachers’ lounge and make my way into the hall, avoiding eye contact with anyone I don’t know."
    "Despite how ‘comfortable’ I’ve gotten around my class, I still feel slightly odd surrounded by students I haven’t met yet."
    "I keep subconsciously thinking they’re going to realize I’m not {i}actually{/i} a teacher and call the cops on me or something."
    "Obviously, the likelihood of that happening is very slim. But the thought is still there and that alone is enough to cause a bit of unrest in this misguided head of mine."

    scene black
    with dissolve2

    "I round the corner and duck into the cafeteria to grab a quick bite to eat before the second half of the day begins."
    "Not wanting to wait in line for hot food, I buy a few snacks out of a vending machine and begin to head back to class."
    "As is customary around here, though...I’m flagged down before I’m able to do that."
    "........."
    "......"
    "..."

    scene ayalunch1
    with dissolve2

    ay "Sensei! Do you want to eat lunch with us today? Everybody else went out to eat in the courtyard, so it'll just be Sana and me."
    s "What? Why didn't you two go with them?"
    sa "It's...too hot out there..."
    sa "I would...probably die..."
    ay "What Sana said. I don't want her death to be on my hands, so I've decided to take one for the team and eat in here instead."
    ay "I'm glad I did, though! Because this decision meant I got to see your face! And that your face will now join us for lunch!"
    s "I mean...I was planning on going back to the teacher’s lounge and eating in there."
    ay "But?"
    s "...But I guess I can hang out here instead."

    scene ayalunch2
    with dissolve

    ay "Woohoo!"
    sa "Umm...yay?..."
    s "Yay indeed, Sana. Yay indeed..."
    sa "Are you...not that hungry, Sensei?...All you have on your tray are...snacks..."

    "Sana takes a quick glance at the minor haul I was able to procure today before taking a sip of her ramune."

    scene ayalunch2r
    with dissolve

    mo "Uh-oh! Looks like it's weebnote time!"
    s "What? Where did you come from?"
    mo "Weebnote: Ramune, otherwise known as Japanese soda, is actually quite different from its American counterpart!"
    mo "One of the key differences is the focus on more fruity flavors, some of which are very unusual by Western standards."
    mo "You also need to carbonate them yourself by punching a tiny ball into an equally tiny hole. It’s mildly sexual and majorly delicious!"

    scene ayalunch2r2
    with dissolve

    sa "That's weird...I could have sworn I...heard someone just now..."
    ay "Nope! I definitely didn't pay anyone to stand behind that board and shout out facts about Japanese culture to the void."
    mo "My gacha addiction lives to fight another day!"
    s "...Anyway, you don’t seem to have that much either, Sana. All I see is bread and rice."
    s "Are you on an all-carb diet or something?"

    scene ayalunch3
    with dissolve

    sa "Umm...no...I just...need the energy..."
    s "For {i}what?{/i}"
    sa "Umm...uhh..."
    sa "Living?..."
    ay "Sana doesn’t eat a lot, but whenever she does it’s pretty much all carbs."
    ay "Or candy."

    scene ayalunch4
    with dissolve

    sa "I have a problem..."
    s "I can see that. Your diet's even worse than mine."
    s "But, then again, I do have Ami making me breakfast and dinner pretty much every night and she forces me to eat vegetables."

    scene ayalunch5
    with dissolve

    ay "Sensei! Did you know I can cook too?"
    ay "Sana, tell Sensei how good of a cook I am."

    scene ayalunch6
    with dissolve

    sa "Well...um..."
    sa "Ayane has...definitely cooked for me before, but..."
    s "...But what?"
    sa "Umm..."
    sa "I’m...trying to think of the nicest way of saying it..."

    scene ayalunch7
    with dissolve

    ay "Don’t mind her, Sensei. She’s just a little traumatized from having to eat broccoli one time."
    sa "Food...shouldn’t look like a tree..."
    s "Sana's kind of got a point, Ayane. It really shouldn't."
    s "In fact, I kind of like the idea behind the Sakakibara diet."
    s "If it were possible, I’d probably survive purely off of garlic bread anyway."

    scene ayalunch8
    with dissolve

    ay "What? Why garlic bread of all things?"
    s "Well..."
    s "It’s got garlic...and bread..."
    s "What more could you want out of a dish?"
    sa "It...can also have cheese too...and cheese is good..."
    s "See? Sana understands."
    sa "I...will also survive off of garlic bread...if Sensei is going to do it..."
    ay "Well...what about pasta? That’s got garlic in it. And noodles are normally made out of bread or...wheat or something. Right?"
    ay "Do you want to try some of mine? I’ve only had a little."
    s "No thanks. It's garlic bread only from now on and that's just not...bread enough."
    ay "Neither am I but you don't see {i}me{/i} complaining."
    s "Ayane, please. There is a child present."

    scene ayalunch8r
    with dissolve

    sa "No there's not! Ayane is only a little bit older than me!"
    s "I'm going to have to see your ID, Sana. I'm not sure if I buy that."
    sa "I don't have an ID!"
    s "And why is that?"
    sa "Because I'm too y-"

    scene ayalunch8r2
    with hpunch

    sa "B-Because I don't want one!"
    s "..."
    sa "I'm not a child!"
    ay "If you're not a kid, can you explain the joke I just made to us?"

    scene ayalunch8r3
    with dissolve

    sa "No...I'm...taking a break from this conversation..."

    scene ayalunch8r4
    with dissolve

    ay "Seriously, though. You should really try {i}my{/i} cooking sometime, Sensei. I can promise you that I'm just as good as Ami is. Maybe even better!"
    s "I...don't know about that, Ayane. Ami is my personal chef and is fully aware of my tastes. I have a hard time imagining how you'd be able to beat her."

    scene ayalunch8r5
    with dissolve

    ay "Ami definitely knows her way around the kitchen...that I will concede."
    ay "{i}But I know my way around your heart...{/i}"
    s "Yeah, I still don't see how that would help you win in a cook-off."

    scene ayalunch8r6
    with dissolve

    ay "Oh! A cook-off! That's a great idea, Sensei!"
    s "It wasn't really an idea. Just...kind of a thing I happened to say."
    ay "Well, now it's an idea! A competition between friends and rivals! Not just for your stomach...but for your heart!"
    sa "Is...Is Ami competing for your heart too, Sensei?..."

    if bonus == True:
        "More than you know, Sana...."

    s "You'll...have to ask her that question. I refuse to speak about her motives."
    sa "I...uhh..."
    sa "Oh..."
    s "Do you think you'll be competing as well, Sana? I'd feel weird not letting you join in on this as well since you were here for the conception of it."
    sa "..."
    s "...Sana?"
    sa "Sorry...I was just...trying to picture myself cooking and..."
    sa "It was just...darkness..."
    s "Okay, so maybe Sana {i}won't{/i} cook, then."

    scene ayalunch7
    with dissolve

    ay "Either way, I swear I’ll have you try my food eventually, Sensei."
    ay "I don’t even care if I have to force-feed it to you."
    s "Please don’t."
    ay "Actually, I think I’d prefer feeding you that way. It sounds like a nice bonding experience."
    s "No. It doesn't."
    ay "Anyway, it's settled. One day soon, Ayane Amamiya will be cooking a gourmet dinner for both Sensei {i}and{/i} Sana. This time with no broccoli."

    scene ayalunch10
    with dissolve

    sa "Huh?...Why am I...suddenly a part of this?..."
    ay "You've been a part of it the whole time, silly."
    sa "Where would this...even take place?...There's nowhere to cook at the dorm..."
    ay "Sensei’s house, obviously."
    s "Are you just inviting yourself over without talking to Ami first?"

    scene ayalunch11
    with dissolve

    ay "Of course. I do that all the time. She won’t care."
    ay "In fact, she’ll probably be happy so many people are over at once!"
    sa "Sensei’s...house?..."
    s "Is there a problem, Sana?"
    sa "No, just..."
    sa "Is it...really okay?...For me to come over?"
    s "Sure. I don't mind."
    s "Just don't blame me if Ami tries to kill either one of you for soaking up some of her alone time with me."
    ay "Don't worry, Sensei. Avoiding certain death in situations like that is one of my very many specialties."
    s "I...guess that's that then."

    scene ayalunch12
    with dissolve

    ay "That is that, indeed!"
    ay "The first annual ‘Ayane cooks for everyone including her future husband!’ event has been confirmed for...some time in the undetermined future!"
    sa "Umm...congratulations...on your engagement..."
    sa "I think...you'll make a good wife..."

    scene black
    with dissolve2

    "The rest of the lunch period goes by pretty much the same way."
    "Ayane and Sana are an...interesting combination."
    "I don’t think I’ll ever fully understand how the two of them wound up together, but..."
    "I'm kind of glad that they did."

    $ renpy.end_replay()
    $ day54 = True
    $ ayane_love += 1
    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Ayane's affection has increased to [ayane_love]!{/i}"
    "{i}Sana's affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label day56:
...
```

## Code that triggers this event
File: \game\script.rpy
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
...
```