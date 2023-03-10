# Såsom i en Spegel (Kaori)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kaori love greater than or equal to 20

* Event [Everlasting Mercy](./mayafestival4.md) (Maya) is completed)

* kaorinumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: kaoridate20
* Group: Kaori
* Triggered by label: callkaorinight
* Triggered by branch label: callnight
* Triggered by path: callnight->callkaorinight->kaoridate20

## Official wiki page

[Såsom i en Spegel](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kaoridate20&go=Go) for more details.

## Event code

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label kaoridate20:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and-"

    play sound "phonebeep.wav"

    k "Friend! Help! A horrible thing has occurred!"

    "Okay. No time for a pre-phone call briefing, I guess."

    s "What’s wrong, Kaori?"
    k "It is John! He has disappeared! "
    k "He was here a moment ago, but the hardened rectangle of pre-cooked wheat strings I placed in a hot metal cylinder full of sky blood required my attention!"
    s "...What?"

    if bonus == True:
        k "My large cock has disappeared! But my dinner was delicious!"
    else:
        k "The chicken is gone!"

    s "Do you...want me to come over and help find him?"
    k "Coming over will not help! I have already told you he is not here!"
    s "I just meant that I can meet up with you and we can look for him together."
    k "Are my sight-spheres not good enough to see what is before them?! Will an additional pair be worth the effort?!"
    s "I don’t know, Kaori. I’m just trying to help."
    k "Then come quickly! Use your muscular movement tubes to drag you to the place I fall asleep in!"
    s "I am...on my way. I’ll see you soon."
    k "You’re welcome! Hello!"

    play sound "phonebeep.wav"
    stop music fadeout 5.0
    scene black
    with dissolve

    "I hang up the phone and begin making my way over to Kaori’s place."
    "I’m not exactly sure how a giant chicken just...disappears, but I highly doubt Kaori would be throwing as much of a fit as she is if it wasn’t true."
    "I’m also not sure if it’s possible for him to have just stepped outside on account of the whole “no opposable thumbs to open doors” thing, but I’m sure the two of us will manage to figure it out soon enough."
    "Or not and he’s already dead."

    if bonus == True:
        "But, and this may make me sound like Kaori for a moment, so I apologize in advance- cocks that large are strong and resilient."
    else:
        "But, and this may make me sound like Kaori for a moment, so I apologize in advance- wshwshwshwshwshwsh!!!"

    "And I’m sure he’s fine, wherever he is."
    "........."
    "......"
    "..."

    scene kaorislostcock1
    with dissolve2
    play music "sanctuary.mp3"

    k "AAAAAAAAAHHHHHHHHH!!!!!!!!!!!!!!!!!!!!"
    s "I’m great, thanks. And how are you?"
    k "JOOOOOOOOOOOHN!!!!!!!!!!!!!!"
    s "Weird emotion. I’m not sure if I follow."
    k "This is no time for joking, Friend! {i}Other{/i} Friend is lost and afraid somewhere! I am very lonely without him! And I do not want him to end up like the other chickens!"
    s "If it’s any consolation, I feel like the initial reaction to seeing a chicken of that size wouldn’t be to kill it, but to capture it and put it on display somewhere."

    scene kaorislostcock2
    with dissolve

    k "That is even worse! "
    s "Than death?..."
    k "John has fright of the stage variety! He is a living creature with human feelings and human desires! And most of those desires are not meant to be shared with others!"
    s "Ignoring your chicken’s apparent {i}human{/i} characteristics, standing around here won’t do us any good."
    s "I doubt he’s made it very far and, even if he has, he’ll be easy to spot. Now put your shoes on so we can go look for him."
    s "Unless you think standing around and yelling his name will make him come back."
    k "JOOOOOOOOOOOHN!!!!!!!!!!!!!!"
    s "Kaori, stop."

    scene kaorislostcock3
    with dissolve

    k "He is my only feathered friend, Friend! All of my other two friends do not have feathers- and I recently learned that one of them is an aunt and does not count as a {i}real{/i} friend!"
    k "It does not change the amount of feathered friends I possess either way, but I would still enjoy having more than zero of them!"
    k "Zero is the smallest number there is not counting the hyphen numbers!"
    s "I believe those are called negatives. "

    scene kaorislostcock4
    with dissolve

    k "{i}You{/i} are negative! I am trying to remain hopeful!"
    s "Kaori. Shoes."
    k "What are shoes?!"
    s "They’re...uhh..."
    s "Protective leg-hand containers?"

    scene kaorislostcock2
    with dissolve

    k "Why did you not just say so?! "
    k "We’ve spent all of these minutes allowing the clock to breathe while my cock runs rampant throughout the city! What if anyone saw?!"
    s "Kaori. Containers."
    k "JOOOOOOOOOOOHN!!!!!!!!!!!!!!"

    scene black
    with dissolve2

    "Kaori eventually calms down enough to put her {i}shoes{/i} on and follow me outside."
    "She has a tough time doing so on account of her trembling hands but, seeing as I’m a bit overdue when it comes to doing any good deeds, I help her get them on so we can begin our search."

    scene clearnightsky
    with dissolve2

    k "John! Where are you currently located?! Relay your coordinates to me so that our physical presences may rejoin in one location!"
    s "You can just say “Where are you?” you know."
    k "Do you believe that I have not tried this?! I have used so many different combinations of words! And yet, no chicken! Not even a peep!"
    k "Wait! Friend! Can you imitate a chicken noise? Maybe John has not returned because I can not properly speak his language?"
    s "I’m not going to make a chicken noise. What we need to be doing is thinking of places he might be."
    s "Did John have any...favorite hang out spots? Or...are there any places the two of you would visit together?"
    k "Well...he always came with me to the muggy laundry building to drown my clothes in soap sauce. But I do not think that is somewhere he would go of his own choosing."
    k "Perhaps he is visiting one of the many local shops of convenient purchasing? Or paying a visit to the dark alley full of kittens that we-"
    k "Wait! Chicken!"
    s "What? Do you see something?"
    k "No! Chicken, Friend!"
    s "..."
    s "What?"
    k "They always come home to roost! Just like the saying goes!"
    k "What if John became sick of our home and wanted to return to his old home?! For roosting purposes!"
    s "You think he returned to that alley we got him from?"
    k "I do not know where else he would possibly go! But the distance between here and there is great and I do not know if he can remember how to get there!"
    k "The brains of chickens are small and can not hold as many pictures of the past as the ones inside of our large, human heads. "
    k "Friend, that alley is dangerous. We can not let John return. I refuse to let him be cut down by the hands that slayed his brethren!"
    k "He only is my rock and my salvation! My fortress! I shall not be shaken!"
    s "Well, I have no idea where that place was, so you’re going to have to lead us there if you ever want to see your cock again."
    k "I remember where it is! Follow me, Friend!"
    k "John! We are coming!"
    k "Hang in there!!!"

    scene black
    with dissolve2

    "Kaori grabs my wrist and takes off toward the alley of mysterious chickens."
    "Or the alley that {i}used to{/i} house mysterious chickens, only to cut them down and teach Kaori about death long before she was prepared to learn."
    "As a relatively-functioning-ish adult, though, that’s something she needed to come to terms with as soon as possible."
    "You’d think that losing her entire family would be enough for her to really understand the gravity of something as terrible as death, but...nope."
    "I guess that John is the closest thing she’s had to family ever since starting her “new” life, though- which is a little strange to think considering she has {i}actual{/i} family now."
    "But John is clearly important to her."
    "And for her sake-"
    "I hope she doesn’t have to experience something as horrible as that a-"

    k "John! There you are!"

    play sound "static.mp3"
    scene kaorislostcock5 with flash
    stop sound

    k "What do you think you’re doing, coming back to this place?! You know the secrets it holds! The blood on its non-existent arm feet!"
    john "Bacawk. (Look no further, and do not follow- for I have felt the sands of time beneath my talons and know the weight they carry when burned into glass)."
    john "Bacawk. (This body ripens with meat of greater animals and strengthens me so. I can see things you would not believe.)"
    john "Bacawk. (Here, atop this precipice of all that is unholy, yet singed by the light of sacred soils...I beseech you please- let me be.)"
    john "Bacawk. (Let me walk the path that I am destined to walk. Drink in the blood of those that I have lost. Sleep in the comfort of the ghostly arms of a loved one.)"
    john "Bacawk. (All I ask is to be pure. All I ask is to be cleansed.)"
    john "Bacawk. (I have followed the light into naught but darkness. There is nothing here. There is nothing left to gain.)"
    k "I do not speak chicken, John! I can not understand what you want! But I know that this is not a safe place for you!"
    john "Bacawk. (You there. Human.)"
    s "..."
    s "What, me?"
    john "Bacawk. (Yes. You. The one who listens but seldom speaks. The thief who comes to steal and kill and destroy. He who understands.)"

    scene kaorislostcock6
    with dissolve

    s "I think “understands” is a little generous. I have no idea what you’re talking about right now."
    k "..."
    john "Bacawk. (Are you prepared for what has yet to come?)"
    john "Bacawk. (Tell me. When you gaze up at the sky and stare deeply into the lights of dead or dying stars, do you see a world that bends to fit your ideals?)"
    john "Bacawk. (Or do you see one that melts into unrecognizable form? Growing hotter by the day. Burning away its impurities so that those with higher tolerance may continue to walk unsinged.)"
    john "Bacawk. (I say these things to you so that you will have peace in me. In the world you have distressed. But be encouraged.)"
    john "Bacawk. (For I have conquered the world.)"
    john "Bacawk. (Which means that it must conquer me in return.)"
    k "Friend...you can understand what John is saying right now?"
    s "Not really. And even if I could find the words to translate, I can’t imagine you would really understand either."

    play sound "static.mp3"
    scene kaorislostcock7
    with flash
    stop sound

    s "I think the gist is that he’s going through some sort of mid-life crisis."
    k "But he is so young! And still growing!"
    john "Bacawk. (Foolish you are for keeping your eyes so unlocked- for they are soon to be taken from you.)"
    john "Bacawk. (It comes again in purest form. Tendrils dripping with the blood of my brothers and yet you stand here, idling. Waiting for the snow to melt.)"
    s "Most of the snow already melted a while ago. It hasn’t really been cold since Christmas."
    john "Bacawk. (It has, but it hasn’t. And you see, but you don’t.)"
    john "Bacawk. (When everything is gone, what will be left for us? When it treads our hallowed grounds, where will we be able to rest our feet?)"
    john "Bacaaaawk. (Or, excuse me- leg hands.)"
    john "Bacawk. (God is dead, human. But for how long will he remain that way? And who of equal value must die to bring him back?)"
    john "Bacawk. (I fear the answer, as should you. For the world as we know it could come toppling down as the result of one incorrect choice.)"
    john "Bacawk. (I am scared of what has yet to come. I am scared of what has happened. I am scared of what happens now.)"

    play sound "static.mp3"
    scene kaorislostcock8
    with flash
    stop sound

    k "He seems to be bacaaaawking a lot, Friendburger. If you can not find the words to explain his feelings, would you be able to write down what they look like?"
    s "Not really, since he’s now starting to sound all religious. That area isn’t really one of my strong suits."
    s "Also, I could just be imagining everything he’s saying because the idea of me being able to speak to animals when no one else can makes essentially no sense at all."
    k "Are you a religious person, Friend? Perhaps the god you believe in has gifted you the ability to understand the furry or feathered creatures of the world?"
    s "What an excellent usage of godly power."
    k "Can you ask John in his language if he will return home? I promise to be a better human chicken mother and friend to him."
    s "Did you understand that, John?"
    john "..."
    s "..."

    scene kaorislostcock9
    with dissolve

    k "Jonathan Chicken Kadowaki McChicken! You have caused the thin strips of hair above my sight sockets to slant at unreasonable angles too many times tonight!"
    k "I am the opposite of happy with you!"

    play sound "static.mp3"
    scene kaorislostcock10
    with flash
    stop sound

    john "Bacawk. (This was never what I wanted, but what I felt that I must do for my own protection.)"
    john "Bacawk. (As the temperature rises, so do my uncertainties.)"
    john "Bacawk. (I am not long for this world. Few of us are. And that has been all the more clear as of late.)"
    k "Friend, do you believe that John misses his family?"
    s "..."

    scene kaorislostcock11
    with dissolve

    k "John! I will find you another chicken to chicken around with while I am not house! Just please come back!"
    k "I can not go on without you! Who will I watch the cool rectangle machine with?!"
    john "... (...)"
    s "I...think he’s afraid of dying."
    k "He has chosen a strange place to return to in order to combat that!"
    s "I don’t think it has anything to do with you, but...maybe the time of year?"
    john "Bacawk. (A festival of tears has pitched its tents in the furthest corners of this city. We will all rue the day that-)"

    play sound "static.mp3"
    scene kaorislostcock12
    with flash
    stop sound

    john "BACAAAAAAAAAAWK! (zaf kqf za za za za za!)"
    john "BACAAAAAAAAAAWK! (zaf uz rdazf ar tqd!)"
    john "BACAAAAAAAAAAWK! (zaf nqradq etq [[REDACTED. DIALOGUE CENSORED DUE TO CHICKEN.])"
    k "John?..."
    k "What is he saying?"
    s "I...can’t understand him anymore."

    scene kaorislostcock13
    with dissolve

    john "..."
    k "..."
    s "..."
    john "Bacawk."

    scene black
    with dissolve2

    "John stares straight ahead for another moment before returning to Kaori."

    play sound "static.mp3"
    scene eggreturn with flash
    stop sound
    play music "letsfuckingo.mp3"

    "Then it becomes egg time again."
    "Please use the next 10 seconds to dance with egg."
    "You better do it!"

    $ renpy.pause(10, hard=True)

    "Okay, okay. Stop egg dance."
    "We talk now."
    "Pretty soon, a thing going to happen."
    "Are you prepared????"
    "Are scared????"
    "Stop scare! It’s OK!"
    "It’s all just lines!"

    play sound "static.mp3"
    scene kaorislostcock14
    with flash
    stop sound

    "There is nothing to fear, for fear is concept plucked from the brains of birds like a feather only to be subsequently implanted into your human brain to make you feel all weird and shit."
    "Sensei and Kaori go on a magic chicken ride back to Kaori’s apartment and none of this ever happened."
    "This was an imaginary event."
    "Please forget it after ten more seconds of egg dance."
    "Go find the nearest egg and kiss it. There might be a chicken inside!"
    "All chickens need love. That is the moral of today’s story."
    "This event never happened."

    $ renpy.pause(10, hard=True)

    play sound "static.mp3"
    scene kaorislostcock15
    with flash
    stop sound
    play music "sanctuary.mp3"

    k "Thank you very much for helping me find the cock again! It is almost like you are a cock expert!"

    if bonus == True:
        s "Yeah, that’s not {i}entirely{/i} inaccurate. But it isn’t how I’d..."
    else:
        s "Stop saying the C word in the Patreon version of the game."
        s "Besides, that's not how I'd..."

    s "Describe...what..."

    scene kaorislostcock16
    with dissolve

    k "Is there a problem, Friend? I know you as a person who normally finishes human sentences before becoming unloud."
    s "I just...don’t really remember coming back here."
    john "Bacawk."

    scene kaorislostcock17
    with dissolve

    k "John, shush."

    scene kaorislostcock16
    with dissolve

    k "Do you have a chicken brain, Friend?"
    s "What?"
    k "It is like I said. Chicken brains are small and they can not fit as many memories as human brains."
    k "If you can not remember how we got here, maybe it is possible that you have a chicken brain."
    s "By that logic, your brain would also be-"
    s "Wait. Actually, that might explain a lot."
    k "There you go again, leaving sentences without endings. How will anyone ever understand you if you do not seek to improve yourself?"
    s "I’ll get right to that, Kaori."
    s "Anyway, is there anything else I can do for you? Or are you ready to call it a night now that your pet is back?"

    scene kaorislostcock18
    with dissolve

    k "John is no pet, Friend! John is a “free-range” chicken with no rules or curfew as long as he listens to the rules and is home by mattresstime!"
    s "You know, I have a few issues with that sentence when thinking of all the trouble we went to tonight, but I’m going to abandon them in favor of getting some sleep."

    scene kaorislostcock15
    with dissolve

    k "Is that all you will abandon tonight?"
    s "What?"
    k "Will you be leaving anything else behind?"
    s "I’m not really sure what you mean by that."
    k "Then there is no need to answer."
    k "Goodnight, Friend! Thank you for the cock delivery!"
    s "..."
    k "..."
    s "Goodnight, Kaori."

    scene black
    with dissolve3
    stop music fadeout 5.0

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate20 = True

    "//////////////////////////USER2 HAS GONE OFFLINE"
    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kaoridate25:
...
```

## Code that triggers this event

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label callkaorinight:
    if kaori_love >= 20 and mayafestival4 == True and kaoridate20 == False:
        jump kaoridate20
...
```