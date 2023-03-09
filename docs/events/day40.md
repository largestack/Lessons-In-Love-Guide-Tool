# Saved by the Bell
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day40&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 40



## Next events
None

## Event properties
* ID: day40
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day40:
    scene hall_day
    with dissolve
    play music "10c.mp3" fadein 3.0

    s "{i}*Sigh*{/i}"

    "I’m at school early again at Makoto's behest since there is apparently a lot I need to catch up on in terms of grading."
    "How? I have no idea. In fact, I'm beginning to suspect that she might be assigning work behind my back."
    "But at least I'm able to handle it all online through some virtual gradebook thing she told me about."
    "Or at least I'm {i}supposed{/i} to be able to handle it online. It's kind of hard to do that without knowing my login credentials."
    "So, here I am wandering the halls of the school and waiting for someone to reset my password so I can actually {i}do{/i} my job."
    "I swear, it's like this school doesn't even {i}want{/i} me to teach sometimes..."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "I make my way into the classroom to kill some time as it apparently takes a full hour to make my new login stuff."
    "I initially planned on using that time to try and figure out a way to ask Makoto to just handle this for me..."
    "But a certain someone who decided to show up early today causes me to throw those plans out of the window as soon as I set foot inside the room."
    "........."
    "......"
    "..."

    scene chikaclass1
    with dissolve

    c "Sensei? What are you doing here so early?"
    s "Losing faith in our educational system when I should probably be losing faith in myself instead."
    c "Woah. That's kinda deep for this early in the morning."
    s "The real answer is that I'm supposed to be doing grading stuff. Unfortunately, circumstances have arisen in which I am unable to do that."
    c "Does this mean we all get A's for doing literally nothing?"
    s "No. It means that you all have blank grades for the foreseeable future. A's are what you {i}would{/i} have if I remembered my password."
    s "What are you doing, though? You don't normally come here this early, do you?"

    scene chikaclass2
    with dissolve

    c "Not all the time. Just when I have to catch up on stuff."
    s "Can't you {i}catch up on stuff{/i} at the dorms? Why do you have to come all the way over here?"
    c "Probs cause Yumi was in a bad mood this morning and I didn't want to smack a bitch."
    s "Yumi in a bad mood? How can this be?"
    c "Hahah...I know, right? When has {i}that{/i} ever happened before?"

    scene chikaclass3
    with dissolve

    c "You know..."
    c "I'm sure it might be hard for you to believe, but she isn’t {i}always{/i} like that."
    c "Yumi can actually be pretty chill when she's not surrounded by, like...school and people and all that stuff."
    c "She's just got a really short fuse and gets triggered way too easily. And whenever she does, it takes like, forever for her to come back down."
    s "Well, what {i}triggered{/i} her this time?"

    scene chikaclass4
    with dissolve

    c "Ummm..."
    c "Waking up?"
    s "Chika, that's not a short fuse. That is the complete absence of a fuse."
    c "I know, I know. And usually I'm able to tell what it is. But she was like, super pissed the whole weekend and I still don't really get why."
    c "Like how am I supposed to cheer her up if she won't even tell me what's wrong?"
    s "No clue. Which is why I've pretty much just given up on trying to understand her in the first place."

    scene chikaclass5
    with dissolve

    c "Well, I can’t really blame you for doing something like that..."
    c "But I do think that {i}you{/i} might be able to break through to her if you try hard enough."
    s "I think you might be misunderstanding my relationship with her."
    c "Well, isn't it possible that you might be misunderstanding her a little bit too?"
    s "I mean...I guess?"
    c "The thing with Yumi is..."

    scene chikaclass6
    with dissolve

    c "Well, things for her haven't exactly been {i}easy.{/i} Let's just go with that."
    c "Honestly, even saying that much is more than she'd want me to tell you."

    scene chikaclass5
    with dissolve

    c "But, basically...she’s not just super mad all the time just because she thinks it makes her look cool or whatever."
    s "So what, though? It’s not like she’s the only person in the world going through tough times."
    s "Her not having it easy shouldn't allow her to talk down on everyone else."
    c "I know it probably sounds like an excuse...and I'm not saying that I think that she should get away with all of the stuff she does."
    c "I just don’t want you thinking she’s some sort of lost cause."
    c "Like...if anyone was gonna break through to her, I think it would kinda {i}have{/i} to be you."
    s "Aren’t you her best friend? Why can’t you ‘break through to her?’"

    scene chikaclass2
    with dissolve

    c "Listen...I love the girl. But if I was gonna be the saving grace she needed, I would have already broken through by now."
    c "I’m here to be her friend and support her, but what she needs is something a lot bigger than that."
    c "And you seem pretty big to me, Sensei."

    "I want that to be a euphemism but, based on the context of this conversation, I'm pretty confident it's not."

    c "Like...what are you? 6’2 or something?"

    "I have now confirmed that it's not."

    s "Something like that. I'm not really the type to keep track of numbers."
    c "Better be careful who you say stuff like that to, you know. The wrong person might...misinterpret that."
    s "Maybe I want them to?"

    scene chikaclass7
    with dissolve

    c "Ooooh...are you always this spicy in the morning? Or did I just happen to catch you on a good day?"
    s "I like to think of it as less {i}spice{/i} and more of a...complete lack of a moral compass."

    scene chikaclass2
    with dissolve

    c "Don't put yourself down like that. I know there's a great guy somewhere in that approximately 6'2ish body of yours."

    scene chikaclass8
    with dissolve

    c "And I know you just told me you don't keep track of numbers, but do you think you could help out with this algebra stuff?"
    c "I know you don't want to teach during the school day anymore, but...school {i}technically{/i} hasn't started yet. So it should be okay, right?"
    s "What happens if I say it's not?"
    c "I don't know. I'll probs just get held back again or something."
    s "Again? You’ve been held back before?"

    scene chikaclass1
    with dissolve

    c "Wait, you didn't know that? I figured that would have been something they told you in the beginning of the year."
    s "Oh. Well, uhh...I probably just forgot it then."

    "Or...never learned it in the first place."

    s "What happened, exactly? If you're here early just to study and your attitude isn't that bad-"

    if chikadorm15 == True:
        scene chikaclass5
        with dissolve

        c "Just...you know. The whole Chinami situation makes keeping up with school pretty tough sometimes."

        if bonus == True:
            c "It's not exactly easy taking care of a kid at my age and whatnot."
        else:
            c "It can just get a little overwhelming sometimes..."

    else:
        scene chikaclass5
        with dissolve

        c "I just..."
        c "I sorta had some stuff I needed to take care of. That's all."
        c "It’s not a big deal, really."
        c "And it’s gotten a lot easier to manage in the last year, so..."

    scene chikaclass8r
    with dissolve

    c "But hey, if worse comes to worst and I {i}do{/i} get held back again...maybe you'll be my teacher a second time?"
    s "Well, let’s hope it doesn’t come to that."
    s "Also, if you ever need help with anything outside of[school]...I'm not entirely opposed, you know."

    scene chikaclass9
    with dissolve

    c "Oh, no no no no no! I wasn't trying to ask for help or anything! You really don’t have to worry about me! I'm fine!"
    c "I’ve got everything totally under control. Seriously."
    s "I’m sure you do. I’m just saying it’s okay to ask for help if you need it."

    scene chikaclass10
    with dissolve

    c "Well...thanks, Sensei..."
    c "I’ll try to remember that..."
    s "Works for me. Just don't burn yourself out."
    c "Hey, umm..."
    c "Do you mind if I ask you a, like...super weird question?"
    s "I...guess?"
    c "Okay, so like..."
    c "What made you decide to get all...cool this far into the school year?"
    c "Like...you were totally different in the beginning of the year. Now, you're turning into somebody that pretty much {i}all{/i} of us admire."
    s "That's probably just one of the results of letting all of you slack off whenever you want."
    c "No...No, I think it's more than that."
    c "It's more like...you're a completely different-"

    play sound "bell.mp3"
    scene chikaclass11

    "The bell chimes and saves me from having to answer a very difficult question."

    c "Wow...has it really been an hour already?"
    s "And I {i}still{/i} don't have my new password. I think it might be time for me to find a new teaching job."

    scene chikaclass12
    with dissolve

    c "Ha. Good luck with that. I can't imagine any other schools in Kumon-mi accepting your {i}methods{/i} as easily as this one."
    s "For what it's worth, the {i}school{/i} hasn't accepted anything. It's just you girls who know about that."
    c "Well, doesn't that make me feel special?..."

    scene black
    with dissolve2

    "After a few minutes, the rest of the girls begin to filter in and yet another day of school begins."
    "Chika never gets my help with algebra, but I'm sure she'll be fine on her own."

    if chikadorm15 == True:
        "She's already managed much harder things, after all..."
    else:
        "But, hey...if she doesn't-"
        "I don't think I'd mind having her in my class for one more year."

    $ renpy.end_replay()
    $ day40 = True
    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "………"
    "……"
    "…"

    jump afterschoolevent

label day44:
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
...
```