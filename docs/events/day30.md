# Drowning
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day30&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 30

✅Event "[Rin: The Flavor of Love](./cafesugar.md)" is completed (event=cafesugar)



## Next events
* [Rin: Window of the Waking Mind](./cafe15.md)

## Event properties
* ID: day30
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day30:
    scene drown0
    with dissolve
    play music "cafe.mp3"

    "And so ends another uneventful day as a school teacher."
    "I’ve gotta say, the fact that I've made it this far without being fired or reprimanded is either extremely impressive on my end, or extremely worrying on the school's."
    "But hey, the fact that none of the staff members have caught on to the person I really am yet is definitely good for me."
    "It also shows that, for whatever reason, the girls have some level of trust in me. "
    "I guess it's a little strange that Yumi hasn't ratted me out to the higher ups, but...well, I guess she hasn't really had the time {i}to{/i} do that with all of her absences."
    "For all she knows, this might be how Sensei has been doing things all along."

    scene drown1
    with fade

    "I step into the cafe for a quick drink in the midst of my aimless wandering and hope that there is someone or something in here with the potential to entertain me for the rest of the day."
    "And, noticing two students of mine no more than twenty feet away from me, I realize that I have once again accidentally manifested exactly what I have been looking for."

    scene drown2
    with dissolve

    c "Woah, Sensei?! What are you doing here?!"
    r "Wait, really? He’s never here this late."

    scene drown3
    with dissolve

    c "Sensei! Come hang out with us! We were actually just talking about you!"

    scene drown5
    with fade

    s "Were you?"
    c "Yeah! Nothing super interesting, though. Just how we're happy to have you as our teacher and not any of the other ones."
    s "Does that have anything to do with how I've given up on assigning schoolwork?"
    c "I mean...that definitely helps!"
    s "So, what are you up to? It's not every day I see you two together."

    scene drown6
    with dissolve

    c "Right? I was just telling Rin that the other day that we need to hang out more."
    r "Hahah...I'm Rin."
    r "That's...a thing that I was told."
    s "I’m not...interrupting anything, am I?"
    c "No way! Not at all!"
    c "Besides, shouldn't you be {i}trying{/i} to hang out with us after that whole {i}let's be friends{/i} thing?"
    c "Friends don't just walk past other friends, Sensei. That'd be like, totally messed up."
    s "Hey, I agree. I just didn't want to be interrupting a date or anything."

    scene drown7
    with dissolve

    c "Hahahah! A date?!"
    c "I guess it does kinda look like that, doesn't it?!"
    r "{i}Please don't leave me.{/i}"

    "Something tells me I probably shouldn't leave Rin right now."
    "It's her. She's the one who tells me that."

    s "Well, I’m happy to hang out here if you two are okay with it. And I guess just...tell me to leave if you wind up wanting to be alone or something."

    scene drown8
    with dissolve

    c "I think we'll be okay. But it's nice knowing that you'd support us if things were a little different, Sensei."
    r "Hahah...hah..."
    s "Everything okay, Rin?"

    scene drown9
    with dissolve

    r "Huh? What? Yeah. I'm good. Green as a cucumber."
    c "Isn't it {i}cool{/i} as a cucumber?"

    scene drown10
    with dissolve

    r "It {i}is{/i} kind of cool in here, isn't it?! Should I turn the heat up? I know it's summer and that it will conflict with the air conditioner, but if that's what you-"
    c "What? No. I meant, like...the phrase. Isn't the phrase {i}as cool as a cucumber?{/i}"

    scene drown10r
    with dissolve

    r "Hahah! Yeah! They {i}are{/i} pretty cool, aren't they?!"

    "Wow."
    "Rin is...not very good around Chika, is she?"

    scene drown11
    with dissolve

    c "You know...maybe Sensei's onto something? You {i}have{/i} seemed kinda weird ever since we got here. Are you sure everything is okay?"
    c "You don’t like, feel uncomfortable hanging out with me...do you?"

    scene drown12
    with dissolve

    r "What?! No! Of course not! It's not like that at all!"
    r "I’m just...really tired!"
    r "I didn’t sleep much last night and I’m like, totally running on fumes right now."
    c "You sure it’s not me? I know I can be kinda chatty sometimes, but that's just because-"
    r "Totally sure! You’re not doing anything wrong! You’re great, in fact! So great! Way better than I am!"
    r "And, umm..."
    r "Uhh!"

    scene drown13
    with dissolve

    r "{i}Help.{/i}"

    "I think you might be a little past helping right now, Rin...But I'll do my best."

    s "Wow. I sure am hungry right now. If only there was some place to get food around here..."

    scene drown13r
    with dissolve

    r "Yes! Food! I will go find us food!"
    r "I work here, so I know where we keep all of it!"
    r "Three foods, coming right Chika!"

    scene drown13r2
    with hpunch

    r "Up! Coming right up! Not Chika. Chika is you! Not coming at all!"
    c "Uhhh..."
    r "Okay, bye! Thank you!"

    scene drown15
    with dissolve

    c "..."
    s "..."

    scene drown16
    with dissolve

    c "It’s me, isn’t it?"
    c "I like, totally wasn’t picking up on her cues or anything. I’m talking way too much again, I know it."
    c "God...I told myself I would do this and everything. I'm so disappointed in myself right now."
    s "I don’t really think that’s the problem, Chika."
    c "Then what is it? There's no way she's just {i}tired,{/i} right? She's yelling way too much for someone who's {i}that{/i} tired."
    c "She was totally fine at[school], too...She didn't start acting weird until we got here."
    c "It’s like the second we’re alone, some...{i}switch{/i} flips and she turns into a completely different person."
    c "I just don't want it to be my fault, you know? I thought this would be fun."
    s "Well, are {i}you{/i} having fun?"

    scene drown17
    with dissolve

    c "I mean...I {i}wanna{/i} say yeah..."
    c "But, like...I can’t help but feel like I’m just bothering her right now."
    c "I’ve known Rin for years now and the two of us haven’t ever really...{i}hung out{/i} before."
    c "I don't know. I just feel like it's supposed to feel a lot more...natural than this."
    c "I've gone out with plenty of girlfriends before and none of them have ever acted this...{i}out of place{/i} with me. Is it our styles, maybe?"
    c "I know we don't have that much in common, but it's not like I'm totally uninterested in any of the stuff she's into. I just don't know much about it. And-"
    s "Chika, I get it. And I think you're worrying too much."
    s "I’m sure everything will work out as long as neither of you make a big deal out of it."
    s "She’s probably just having an off day or something."

    scene drown16
    with dissolve

    c "I really hope that’s all it is..."
    c "I've always, like..."
    c "Kind of wanted to be friends with her and stuff. She's so...unique."
    s "..."
    c "..."

    scene drown18
    with dissolve

    r "Okay, I'm back...sorry about that."
    r "I...forgot to ask what everyone wanted, so...I just ordered a bunch of stuff that we can all split."
    r "My manager said it's on her today, too...so...I guess that's kind of cool. Right?"
    c "Yeah...Yeah, that's totally fine."

    scene drown19
    with dissolve

    c "Hey, Rin?"
    r "Hm? What's up?"
    c "I’m sorry if I was...making you feel uncomfortable or anything. I just-"

    scene drown20
    with dissolve

    r "What? Chika, no! I’m totally fine."
    r "Like I said, I'm just tired. I...get like this sometimes. I just needed to reset really quick, that's all."
    r "Plus, as soon as my coffee cools down and I can get some caffeine into my system, I'm sure I'll be right as a cucumber."
    c "I'm pretty sure it's right as r-"
    c "You know what? Forget it. I'm glad you're feeling better. But just...let me know if I wind up annoying you, okay?"

    scene drown21
    with dissolve

    r "Yeah..."
    r "Yeah, I can do that."
    r "I'm sorry too. For...making things awkward and stuff. And...and for all of the cucumber analogies."
    r "I can assure you that I don't spend any more time thinking about cucumbers than the average girl."
    r "Probably even less, to be honest. They're all weird and..."
    r "And bumpy..."
    r "And...uhh..."
    c "...And cool?"
    r "..."
    c "..."

    scene drown22
    with dissolve

    r "Pfft!"

    scene drown23
    with dissolve

    r "Hahah...hahahah!"
    c "{i}Thank you, Sensei. Let me know if there's anything I can do to make it up to you, okay?{/i}"

    scene black
    with dissolve2

    "I wind up leaving the cafe before any of the food arrives so the two of them can spend some more time together."
    "It's pretty clear what was going on here today, but..."
    "Well, let's just say there's no need for me to get in the way right now. Not while everything is still so fresh..."
    "And certainly not before I know either of them well enough to even {i}want{/i} to get myself caught in the early stages of the mess this may become."
    "I'll remain on the sidelines for now. I don't have to start every single game."
    "But...when I do-"
    "I'll be sure to make an impact."

    $ renpy.end_replay()
    $ rin_love += 1
    $ chika_love += 1
    $ day30 = True
    stop music fadeout 7.0

    "{i}Rin's affection has increased to [rin_love]!{/i}"
    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "{i}Before I know it, the day has come to an end and I am on my way home.{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label day33:
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
...
```