# Girl-Talk
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day65&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 65

✅Event "[Sana: Carry Me Home](./bar15.md)" is completed (event=bar15)

✅Event "[Rin: Nothing Was Missing, Except Me](./cafe20.md)" is completed (event=cafe20)



## Next events
* [Main: Milk, Eggs, and Water](./day89.md)
* [Main: Stronger I Become](./day91.md)
* [Sana: Scouting Mission](./bar20.md)
* [Rin: Good Day, Humans](./cafe25.md)

## Event properties
* ID: day65
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day65:
    scene street_noon
    with dissolve2
    play music "justbehappy.mp3" fadein 5.0

    s "{i}Hah...{/i}"

    "And so another[school] day comes to a close."
    "Originally, the plan was for me to go to karaoke again with Ami, Ayane, and Maya but..."
    "Well, one of the three (And I’m sure you can guess which one) succeeded in un-inviting me this time."
    "As it turns out, Maya can be incredibly persuasive when she wants to be."
    "I guess I must just be immune to her powers or something, though, because she hasn’t managed to dissuade me from visiting her yet."
    "But, either way, now I’m alone and wandering the streets, trying to find some way to kill the time."
    "I’ve gotten bored of choosing between the dorms, the bar, and the porn shop (Seriously, when am I
    going to have something else to do after class?) and so now I’m just..."
    "Who the fuck even knows?"
    "I’m just walking around. Life is good."
    "And by good I mean passable."
    "That’s right."
    "Life is passable."
    "You heard it here first."

    sar "Ooooh, who is that cute boy I spot off in the distance?"
    s "Hm?"

    scene sides1
    with dissolve

    "I turn around to find Sara and...Haruka hanging out at the same bistro that Ami and Maya frequent?"

    s "Hey. What’s going on?"
    sar "The two of us are just catching up on old times. Fancy meeting you here~"
    s "Likewise...Hey, Haruka. What’s up?"
    h "Hey! I’m surprised you two know each other."
    s "I was actually just thinking the same thing."

    if sarasex == True:
        scene sides7
        with dissolve

        sar "{i}He’s the one I was telling you about on the phone...{/i}"
        h "{i}Huh? The one you were telling me about on the-{i}"

        scene sides2
        with dissolve

        h "Ah-"

        scene sides3
        with dissolve

        h "..."
        sar "..."
        s "..."
        s "You didn’t..."

        scene sides4
        with dissolve

        sar "Whaaaat? Girls talk about stuff~ Are you embarrassed of me?"
        h "Mm..."

        "Haruka’s clearly flustered or embarrassed or...shocked. I don’t know. Haruka is something."
        "I hope this doesn’t change her opinion of me too much."

        scene sides5
        with dissolve

        if bonus == True:
            sar "If it makes you feel any better, I only had good things to say~"
            h "Yeah...{i}very{/i} good things..."
            sar "Are you jealous?"
            h "N-no! I’m just surprised! You would be too if you found out two people you see all the time have been...you know."
            sar "Having sex?"

            scene sides6
            with dissolve

            h "You haven’t changed at all since [high_school], have you?..."
            s "You two went to [high_school] together?"
        else:
            sar "Why do you look so flustered? You're a really good hugger."
            s "Well {i}excuse me{/i} for being sensitive, Sara. I was under the impression that was a {i}private{/i} hug."
            sar "Oh, quit being a baby."

            scene sides6
            with dissolve

            h "You haven’t changed at all since [high_school], have you?..."
            s "You two went to [high_school] together?"

        scene sides9
        with dissolve

        sar "We sure did."

    else:
        scene sides7
        with dissolve

        sar "He’s my daughter’s [high_school] teacher."
        h "Oh, really? She must be in the same class as one of my employees then."

        scene sides8
        with dissolve

        sar "Oooh is that so? Can you tell us if those two are friends or not?"
        sar "I haven’t heard Sana talk about anyone other than you and the blonde girl, so I’m starting to worry that she’s a bit of a wallflower."

        "Strange that she mentions that..."
        "Sana and Rin sit right next to each other and I feel like the two of them would get along if they actually talked."
        "I know both of them play games and...wear mostly black so like..."
        "They’d be destined to be good friends, right? Is that how it works?"

        s "I don’t think they are. But maybe I’ll try to push them together if I ever have the chance."
        sar "Please do! Sana needs all the help she can get."
        sar "She definitely seems a little more outgoing lately thanks to you, though..."

        scene sides9
        with dissolve

        h "Yeah, Rin too when she’s not...you know."
        s "Oh, I know..."
        s "How do you two know each other, by the way?"
        sar "High school!"
        s "Really? Were you in the same class or something?"
        sar "Not quite."

    scene sides7
    with dissolve

    sar "Haru was a few years ahead of me but the two of us used to hang out with some of the same people."
    sar "And now we’re both running small businesses. Who’d have thought things would turn out like this?"

    scene sides10
    with dissolve

    sar "Of course Haruka’s is taking off while mine is imploding, though..."
    h "Oh, stop. We’re not taking off...Besides, I’m sure the bar will get better in no time at all."
    sar "Please spend all of your money there. I need it."
    h "Well...I can’t spend {i}all{/i} of my money there...I still have bills and whatnot."

    scene sides11
    with dissolve

    sar "Sensei~ Tell Haru-chan to be nice and spend all of her money on me..."
    h "Um...Why do you call him Sensei?..."

    scene sides12
    with dissolve

    sar "You should try it! It’s actually pretty fun. It makes me feel [young]again."
    h "You {i}are{/i} young, though..."
    sar "Just do it! Come on! I promise, you’ll love it."

    scene sides13
    with dissolve

    "Haruka makes eye contact with me, trying to figure out if this is an acceptable thing for her to do or not."
    "Frankly, I don’t care."
    "I’ve gotten used to everyone calling me Sensei over the last few months anyway."

    h "Umm...S...S-"

    scene sides14
    with dissolve

    h "Nope. Can’t do it. We’re like the same age. It feels weird."
    sar "Come on! It’s like roleplay! I thought you were into stuff like that!"

    scene sides2
    with dissolve

    h "S-Sara! What the fuck?!"
    sar "Hehehe~ Woops..."

    scene sides3
    with dissolve

    h "Please forget that you just heard that. It’s not true. I swear."
    s "Really? I don’t think there’s any shame in roleplay. It can actually be kind of fun at times."
    sar "Oh-ho-ho...What an interesting development this has turned out to be..."

    if amisroom5 == True:
        scene sides15
        with dissolve

        k "Greetings once more, attractive human females. How is-"

        scene sides16
        with dissolve

        k "Ah! It’s you again!"
        k "Hamburger Man!"

        scene sides17
        with dissolve

        h "Hamburger Man?..."
        s "I ordered a hamburger from some diner she works at once."
        k "You said strange things to me!"
        s "I did no such thing..."
        k "You did!"
        s "I did not..."
        k "You did!"

        scene sides18
        with dissolve

        sar "My, you’re pretty popular around here, aren’t you?"
        s "I guess so..."

    else:
        scene sides15
        with dissolve

        k "Greetings once more, attractive human females. Is there anything else I can get for you?"

        if bonus == True:
            "A girl, probably a few years older than Ami, crouches down at the table and checks on Sara and Haruka, albeit in a rather...strange manner."
            "I’m surprised that this place would hire someone with a tattoo as huge as that on her chest."
            "Not that I have anything against tattoos, it's just sort of frowned upon in Japan."
        else:
            "What a friendly looking girl she is. I hope she is normal."

    scene sides16
    with dissolve

    sar "I think we’re okay for now, Kaori. Please keep up the good work."
    h "I’m okay, too. Thanks, though."

    scene sides19
    with dissolve

    k "You! With the face. Order food now."
    s "All of us have faces..."
    k "Your face is different! It interests me!"
    k "Now order food so that I may receive money from my employer that I can
    then use to purchase normal human objects like a “spatula” and a “dog-food.”"
    s "{i}A{/i} dog-food?"
    k "Yes. I can not obtain a “dog” until I have the nutrients required to nurture it."
    s "Why are you putting quotation marks around everything?"

    scene sides20
    with dissolve

    k "Order food or perish..."
    s "…"
    k "…"
    s "I’ll have a burger."

    if amisroom5 == True:
        k "..."
        k "Of course you will..."

    else:
        k "…"
        k "Kaori will collect this item for you...Please prepare the currency you will use in exchange for it."
        s "Thanks..."

    scene sides21
    with dissolve

    s "..."
    h "She’s a little, uhh, eccentric...don’t you think?"
    sar "I like her. I think she’s fun."
    s "I don’t know if I’m fully convinced that she’s human yet."
    h "Same. I like her tattoo, though. I wish I could pull off something like that."

    scene sides22
    with dissolve

    sar "You totally could. Maybe not a spider but like...I don’t know. A sparrow or something?"
    h "No way. My boobs are too big. It would look like a pterodactyl."
    h "Maybe I could get something on my thigh, though...That might be cute."

    scene sides21
    with dissolve

    h "What do you think? Do you like tattoos on women?"

    menu:
        "Absolutely":
            s "Oh, definitely. I love them."
            h "Really?"
            s "Yup. If you want one, I say go for it. You’re already attractive, so I imagine a tattoo would make you even hotter."

            scene sides11
            with dissolve

            sar "Hey...I want attention too, you know."

        "Not really":
            s "Ehh...I’m not really a fan. I think girls are more attractive when they don’t modify their bodies."

            scene sides11
            with dissolve

            sar "{i}Boo...{/i}"
            h "Hahaha...I think they can work on certain people. I just don’t think I’m cut out for one."

    scene sides21
    with dissolve

    sar "Aaaaaanyway, I hate to be the bearer of bad news but Haru and I still have a bunch of girl-talk we need to be doing, so I
    think it might be time for you to shoo."
    s "Did you just...shoo me?"

    if sarasex == True and bonus == True:
        sar "Heheh~ I’ll make it up to you. Don’t worry..."
        s "…"
        s "I’m going to hold you to that."

    else:
        sar "Mhm~ What are you gonna do about it?  "
        s "…"

    h "Umm...I’m sorry for Sara’s...{i}directness.{/i}"
    s "You don’t need to apologize. I’m just happy knowing her daughter hasn’t taken after her."

    scene sides11
    with dissolve

    sar "Sensei is always so mean to me~"

    scene sides10
    with dissolve

    sar "Tell him to stop, Haru-chan..."
    h "I...don’t think he’s going to listen to me..."

    scene black
    with dissolve2

    "I hang around until my burger arrives and then promptly have it boxed to take home."
    "It’s weird how two of the only people my age that I’ve associated with in Kumon-mi happen to be old friends from[school]."
    "I think they work well together, though. Albeit in a strange sort of way."
    "I wonder what the two of them were like back then?..."

    $ renpy.end_replay()
    $ day65 = True
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    jump endofweekday

label day68:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
...
```