# The Devil Incarnate
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day5&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 5



## Next events
None

## Event properties
* ID: day5
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day5:
    scene newdreaming1
    with dissolve2
    play music "normalday.mp3"

    a "So, are you back to normal yet or is your brain still being stupid?"
    s "I don’t think “being stupid” is the right way to describe what is currently happening to my brain-"
    s "But if you’re asking if I have somehow miraculously remembered everything that has ever happened to me within the last 48 hours, the answer is no."
    a "Well, did you have a good weekend at least? I’m sure that must have helped {i}a little bit,{/i} right?"
    s "It...certainly helped me realize that I don’t really have anything to complain about and that my life seems pretty good here."

    scene newdreaming2
    with dissolve

    a "Well, it didn’t get that way overnight, you know? We worked super hard to get to where we are now and I’m not about to let early onset dementia take that away from us."
    s "I don’t have dementia, Ami."
    a "Silly, Sensei. Nobody ever {i}knows{/i} they have dementia. You clearly do and should just listen to me since I know more about you than even you do."
    s "You know, when I woke up this morning, it didn’t really occur to me that being gaslit by my niece on the way to school was a possibility."

    scene newdreaming3
    with dissolve

    a "Anything is possible in Kumon-mi, Sensei!"
    s "Again, not really the response I expected or wanted to hear."

    "I’m on my way to school with Ami to start my first {i}full{/i} week as a teacher. "
    "Friday went by pretty well for the most part but, of course, that was just one day. And for all I know, this whole {i}teaching{/i} thing could actually be pretty hard."
    "Despite sharing her...hesitations in terms of my “new” teaching methods, I doubt Makoto is the type to report me to any of the higher-ranking school officials-"
    "So the biggest issue right now is really just getting to know everyone and making sure I’m able to get through each day without dramatically ruining everything."
    "{i}How{/i} I’d go about ruining everything when I’m so focused on not drawing any attention to myself, I have no idea."
    "But these are teenage girls we’re talking about- violently seizing all over the floor during the most impressionable times of their lives. "
    "I can’t remember if there’s any truth to it, but I believe that the best thing to do during times like this is to just let the seizure play out and not do anything to stop it."
    "That’s not medical advice or anything- just the words and insight of a man who, at this point in time, has but one goal in life-"
    "To have sex with as many of his students as possible."
    "And to not get caught in the process of that."

    scene newdreaming4
    with dissolve

    "But, of course...every plan has obstacles. "
    "And it appears that one of those obstacles is now walking to school with me as well."

    a "Morning, Maya! I figured you’d be halfway to school already. I didn’t expect you to come meet up with us along the way."
    m "Am I interrupting “family time?”"
    a "You’re not interrupting anything. Me and Sensei were just-"
    s "Sensei and I."

    scene newdreaming5
    with dissolve

    a "What? School doesn’t start for another half hour. Can’t you wait until I switch shoes to start teaching me grammar?"
    s "Sorry. I’m just trying to look cool in front of Maya so she stops thinking I am the devil incarnate."
    m "If the devil existed, I {i}do{/i} imagine he’d look something like you."
    m "But I also want to make it clear that correcting Ami’s grammar is very low on the list of “things that I think will make you cool.”"
    s "Can I know what’s at the top of the list, by any chance?"

    scene newdreaming6
    with dissolve

    m "Not talking to me."
    s "I’m upset with myself for walking into that."
    a "I’m starting to doubt whether you lost your memories at all after hearing the two of you go at it like that first thing in the morning..."
    s "Don’t worry, Ami. You’re not the only one here inherently doubting who I am as a person."

    scene newdreaming7
    with dissolve

    "You {i}are{/i}, however, the only person here who believes that I am who I say I am."

    a "Umm...anyway! {i}Sensei and I{/i} were just talking about how he spent his weekend and whether or not this little brain slump of his will stop him from doing his best in school."
    m "Interesting. I didn’t realize he had a “best.”"

    scene newdreaming8
    with dissolve

    a "Hey, why did you come all the way over here to meet up with us if you’re just going to spend the whole walk being mean to Sensei?"
    m "Apologies. I do agree that I might be a little harsher than normal this morning. "
    m "I just haven’t been sleeping well lately and this is something that I am apparently just going to do in order to compensate for that."
    a "Does...insulting my uncle give you energy or something?"
    m "No. But it does help me sleep a little better at night knowing that {i}someone{/i} is actively calling him out for being the type of person he is."
    s "I liked this walk better when it was just Ami and me."

    scene newdreaming9
    with dissolve

    a "Ami and {i}I!{/i} Ha!"
    s "Wrong."

    scene newdreaming10
    with dissolve

    a "What?! Why?!"
    s "Ask me again in half an hour when I am getting paid for this."
    a "Is my love not payment enough?!"
    s "Will your love put food on the table?"
    a "It does every single morning! I’m basically your personal maid, you know!"
    s "Huh. I guess we’ll have to get you a uniform then."

    scene newdreaming11
    with dissolve

    m "Uhh...ew?"
    a "I mean...I don’t really have any money. But if you wanted to buy me one, I don’t think I’d have a problem wearing it around the house."

    scene newdreaming12
    with dissolve

    m "Uhh...{i}ew?{/i}"
    a "What? It’s not fair if you’re the only one who gets to wear a cute costume all the time."
    m "The miko dress is not a {i}costume.{/i} It’s something I literally have to wear when tending to the shrine."
    a "Why, though? Will the gods smite you if they see you wearing your normal clothes or something?"

    scene newdreaming13
    with dissolve

    m "Who knows? Gods {i}do{/i} have a history of creating asinine rules and then dishing out punishment to those who refuse to abide by them."
    m "Frankly, being {i}smitten{/i} by them would solve a multitude of problems for me when my existence is nothing short of {i}Hell{/i} to begin with."
    a "Wow. You really {i}haven’t{/i} been sleeping well, have you?"

    scene newdreaming14
    with dissolve

    m "No...I really haven’t."
    m "I keep having these...strange dreams lately. And it’s as if they’re getting even stranger as the days go by."
    a "Dreams? What kind of dreams?"
    m "They’re hard to describe. It’s like reality, but..."
    m "Upside down?"
    a "..."
    s "..."
    a "Yeah, I don’t get that at all."

    scene newdreaming15
    with dissolve

    m "I didn’t expect you to."
    m "This sort of thing always happens around the start of a cycle. I wouldn’t worry too much about it."
    a "Cycle? Do you mean...semester?"

    scene newdreaming16
    with dissolve

    m "Yes, that."
    m "I really should be sleeping more, shouldn’t I?"
    a "I guess so. But you already sleep, like...way more than everybody else I know. So maybe this is some kind of medical thing?"
    a "Or, even worse- what if you and Sensei {i}both{/i} have dementia?"
    m "Yeah, I...don’t really think that’s what’s going on here."
    s "Maybe Maya would sleep a little better if you stayed at the dorms a little more often?"

    scene newdreaming17
    with dissolve

    a "What? But why would I do that?"
    s "Because...you’re her friend? And you probably love her or something?"
    a "But I also love you! And my bed at home is way comfier than the one in our stupid dorm room."
    a "Besides, it’s not like I {i}never{/i} stay there. I just think it’s easier staying with you since I don’t have to walk all the way back just to cook you breakfast in the morning."
    s "Do you...{i}have{/i} to cook me breakfast every morning?"

    scene newdreaming18
    with dissolve

    a "Do you think you can survive without me?!"
    m "I think what Sensei is saying is that you should spend more time worrying about yourself rather than him."
    a "Bring back the old Sensei! This one isn’t dependent enough!"
    s "I’m plenty dependent and would be more than happy to eat your food every morning. But Maya might also need your help too."
    m "I would like to amend my previous sentence. I no longer believe Sensei wants you to think more about yourself, but that he is simply just trying to sound “cool” again."
    a "He’s cooler when he loves me!"

    scene newdreaming19
    with dissolve

    m "I will concede that I would be happy to eat a fresh breakfast every morning as well, though. So perhaps he’s onto something even if he’s being insincere about it?"
    a "Why don’t you just move in with us, then? We’ve slept in the same bed before. I don’t mind."

    scene newdreaming20
    with dissolve

    m "{i}I{/i} mind. It’s bad enough having to walk with him to school. I don’t want to be waking up next to him as well."
    s "You do realize that Ami and I sleep in different beds, right?"

    scene newdreaming21
    with dissolve

    a "I mean..."
    a "We don’t {i}have{/i} to..."
    m "This might make me sound like a bit of a broken record, but...uhh..."
    m "{i}Ew?...{/i}"

    scene black
    with dissolve2

    "The three of us continue on our way to school and manage to avoid further disgusting Maya for the rest of the morning."
    "A large part of that was likely due to the fact that she stopped focusing on the two of us and paid more attention to her phone, but I will take what little victories I can get when it comes to her."
    "Regardless, the rest of the school day passed by without anything notable happening and, before I knew it, I was back on the streets without an idea of what to do with the rest of my day..."

    $ renpy.end_replay()
    $ day5 = True
    $ maya_love += 1
    $ ami_love += 1
    stop music fadeout 7.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label day7:
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
...
```