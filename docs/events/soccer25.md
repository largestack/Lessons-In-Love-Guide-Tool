# Thighs On-Demand (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 25

* Event [Moments Like This](./mikudorm15.md) (Miku) is completed)

* Event [Kadrillionbilliontrillion](./halloween14.md) (Main) is completed)



## Next events

* [Miku: Scaredy Cat](./mikudorm25.md)

## Event properties

* Id: soccer25
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield
* Triggered by path: soccerfield->soccer25

## Official wiki page

[Thighs On-Demand](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=soccer25&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccer25:
    scene black
    with dissolve

    "………"
    "……"
    play sound "slidedoor.mp3"
    "…"

    scene mikushed1
    with dissolve2
    play music "retrospect.mp3"

    "Somehow or another, Miku and I find ourselves in the storage shed once again."
    "And when I say “Somehow or another,” what I really mean is that we’re in here on clean-up duty."
    "Being miles ahead of the rest of the team (With the one other exception being Karin), it’s okay for Miku to miss out on practice every once in a while."
    "The only issue is that the atmosphere is a little strange given exactly what went down the last time Miku and I were here together."

    mi "So, uhh, good thing we got the goalie to step in and protect the storage shed from any rogue balls this time, right? Hahahaha..."
    s "Are you going to be okay?"
    s "I have literally no idea what I’m doing as a soccer coach but maybe it would be better for Karin and I to swap places until the clean-up is done?"
    mi "Naaaah...It’s totally fine. I mean, it’s not like there’s even much to clean up or anything."
    mi "We’ve just gotta collect all the spare balls and bring ‘em out for...kicking practice and stuff."
    s "Isn’t all of soccer practice just...kicking practice?"

    scene mikushed2
    with dissolve

    mi "‘Course not! We’ve also got runnin’ practice and defensive drills and all of that other stuff you should be figurin’ out since you’re our coach now."

    if bonus == True:
        s "I’m really only here for the thighs."
    else:
        s "I’m really only here for the bump in my salary."

    scene mikushed3
    with dissolve

    if bonus == True:
        mi "Yes, yes. All because Master Miku tapped into ‘yer real feelings and brought the true Sensei outta hidin’ to come touch a bunch of girls."
        s "Right. Even though I haven’t technically done any touching yet."
        mi "That sounds like a you-problem, Sensei. Pretty sure ya can just walk up to anybody and start rubbin’ em and they’ll be all like “Wow, thanks! I needed that!”"
        s "I’m pretty sure I’d get in a lot of trouble if I actually did that."
    else:
        mi "And the cute girls!"
        s "Yes, you are all cute. But I am a teacher and a coach first and foremost. I express no interest in or desire to pursue anything else with any of you."

    mi "Nuh-uh. You-"

    scene mikushed4
    with dissolve

    "I go to take a step forward to prove my point and Miku’s eyes immediately grow about six sizes larger."

    mi "Stay back, heathen! My thighs are fine! I haven’t even run yet!"
    s "See what I mean? If {i}you're{/i} reacting like this, how do you expect the other girls to react?"

    scene mikushed5
    with dissolve

    if bonus == True:
        mi "The other girls probably have experience in the sexy-department and the only experience {i}I{/i} have are those pop-ups that show up when ya illegally stream anime."
    else:
        mi "Badly! Like when I ask them torrent anime for me cause the connection in my room sucks!"

    s "Illegally streaming things is bad, Miku. You should know this."
    mi "I know, I know."
    mi "Illegally piratin’ anything is bad and should be punishable by death. "
    mi "Just kill me now, why don’t ya?"
    s "Especially when it’s something you can get for the price of a coffee."
    mi "You’re really makin’ me feel like crap, Sensei."
    mi "I just can’t stop thinkin’ about how hard the people who made all that stuff work only to have it stolen by someone as impatient and immature as me. "
    mi "I hereby promise to never pirate anything again. "

    if bonus == True:
        s "Good. Now, back to thighs."

        scene mikushed6
        with dissolve

        mi "Oh, right. That’s what we were talkin’ about."
        s "Are you sure you don’t want to seize this rare opportunity of us being alone in the shed to get a massage, Miku?"
        mi "A massage sounds pretty good but I’ve been feelin’ kinda weird around you ever since the whole dry-humpin’ incident."
        s "Makoto has brainwashed you. No humping was involved at all."

        scene mikushed7
        with dissolve

        mi "I...became a woman that day..."
        s "You really didn’t."

        scene mikushed8
        with dissolve

        mi "Anyway, we can save all that thigh-touchin’ stuff for some other time. We’ve gotta job to do and that job involves balls."
        s "Please go on."
        mi "Just gotta reach around and grab some until I can’t hold anymore."
        s "You’re making this a euphemism on purpose, aren’t you?"
        mi "Hm? Euphe...UFO?"
        mi "Ya’ hear something out there, Sensei? Should we go check?"
        mi "Space war is ragin’ on and on and we never know when the aliens might come down and enslave us."
        s "Yeah, I’m pretty sure we don’t need to worry about something like that."
        s "Let’s just focus on cleaning this place up before Karin comes in and yells at us."
    else:
        s "I am glad that we have reached that understand. Now, in order to maintain a healthy, clean environment, I propose that we commense cleaning this room immediately."

    scene mikushed9
    with dissolve

    mi "Roger that!"
    mi "Cleaning-rangers...go!"

    scene black
    with dissolve

    "Miku and I proceed to tidy up the storage shed, setting aside any spare soccer balls we can find to bring out to the field."
    "I’m not sure how all of these balls wound up in such strange places, and I’m beginning to think that someone might be intentionally placing them in weird locations to get a rise out of us."
    "What a weird prank that would be if it were true."
    "There’s even a ball inside of a bucket."
    "Why?"
    "Who puts a soccer ball in a bucket?"

    mi "Sensei! Can ya try reachin’ up on top of this shelf and grabbin’ those for me, please?"
    s "Huh? How did those even get up there?"
    mi "Beats me but it’s our duty to get ‘em!"
    s "There’s no way I can reach those. You’re going to have to get on my shoulders."
    mi "Guhh, fine! Kneel down and let me get on top of ya."

    "………"
    "……"
    "…"

    scene mikushed10
    with dissolve

    mi "Holy heck! Is this what it feels like bein’ a tall person?!"
    mi "This is friggin’ awesome! I could finally kick Karin’s butt!"
    s "Can you reach the soccer balls, Miku?"
    mi "Probably, but I’m kinda just enjoyin’ bein’ up this high. "

    scene mikushed11
    with dissolve

    mi "Lemme stay up here for a little while longer and soak-in the fact that I’ll never actually be this tall."

    if bonus == True:
        s "Have you given up on your growth spurt?"
        s "What happened to getting boobs as big as Futaba’s?"

        "Miku squeezes my head with her thighs in order to stabilize herself."
        "It’s awesome."
        "That’s all I have to say about the matter."

        scene mikushed12
        with dissolve

        mi "Stupid gigantic monster-boobs. Just who does that girl think she is? "
        mi "Imagine if I had bazongas like that? You probably wouldn’t even be able to hold me up here."
        mi "They’re probably like six thousand pounds. "
        s "Having fun up there?"

        scene mikushed13
        with dissolve

        mi "I think so. I’m not squeezin’ ya too hard, am I? "

        "{i}You’re not squeezing me hard enough.{/i}"

        s "I’m fine. "
        s "In fact, I’m surprised you’re even okay with staying up there given how hesitant you were to have me touch your thighs like five minutes ago."
        s "Why is something like this okay but that wasn't?"

        scene mikushed14
        with dissolve

        mi "Because this was necessary! We've got a job to do!"
        mi "And it’s not like I’m gonna pop a boner and stab the back of your head with it or somethin’!"

        scene mikushed15
        with dissolve

        mi "And...ngh...Watch how hard you’re grabbin’ onto my legs! That feels...really weird!"
        s "I thought your thighs were fine? They feel pretty tight to me. Maybe we should loosen them up?"

        "I dig my fingers deeper into Miku’s thighs and need to reposition my legs to ensure that we don’t topple over."
        "Granted, there’s a mattress right behind us so, if we do fall, it will probably be fine."
        "But I’d like to avoid the low chance that I actually crack her skull open and cause her to bleed out in front of me."
        "That would be a huge bummer."

        scene mikushed16
        with dissolve

        mi "S-Sensei! Stop it!"
        mi "I might look strong but I’m delicate! Super fragile! Gonna die if ‘ya keep touchin’ me like that!"
        s "You’re the one that’s taking forever to grab the balls."
        mi "I’m not ready to grab your stupid balls! I’ve been tryin’ to tell you that!"
        s "The soccer balls, Miku."

        scene mikushed17
        with dissolve

        mi "Uhh...Oh."
        mi "Well that’s your fault for sayin’ somethin’ so easy to misunderstand."

        scene mikushed18
        with dissolve

        "I can feel Miku lean forward to try and grab the balls on top of the shelf."
        "The tightness of her legs around my face eases up a bit and is replaced with the feeling of her stomach pressing against the back of my head."
        "When she’s unable to reach even then, she inches her body forward until she’s basically grinding against my neck."
    else:
        s "Sure, Miku. I understand your desire to be tall and will respect your decision to stay atop my shoulder for a slightly extended amount of time."

    scene mikushed19
    with dissolve

    mi "For real, though...who the heck puts soccer balls in such hard-to-reach places? This is madness."
    s "Just grab them unless you want me to start gripping you harder again. "

    scene mikushed20
    with dissolve

    mi "Y-Yes sir!"

    scene black
    with dissolve2

    "Miku manages to finally get the balls off of the shelf and quickly hops off of me the second I begin to lower my knees."

    scene mikushed21
    with dissolve

    mi "Well that was an...interesting sensation."
    mi "I had no idea just ridin’ on somebody’s shoulders could give me so many butterflies."

    if bonus == True:
        s "Did you not get butterflies when riding on my waist before the Halloween party?"

        scene mikushed22
        with dissolve

        mi "Not like this! This was way different for some reason!"
        s "Sounds to me like you’re becoming aware of your womanly desires, Miku."
    else:
        s "Is this your first time experiencing altitude sickness?"

    scene mikushed23
    with dissolve

    mi "Nuh-uh. I’m the same as always."
    mi "How do your shoulders feel, though? I was kinda up there for a while."
    s "They’re fine. You’re even lighter than you look, which is already pretty light to begin with."

    if bonus == True:
        mi "You sure you don’t want me to rub ‘em for a little bit or somethin’?"
        mi "I don’t mind. I give Kirin shoulder massages all the time. I’m pretty good from what I hear, too."
        s "So I’m not allowed to massage you but you’re allowed to massage me?"

        scene mikushed24
        with dissolve

        mi "Of course ‘yer allowed! Just not...today! "
        mi "Besides, ya already got a good enough feel while I was up on your shoulders, didn’t ya?"

        scene mikushed25
        with dissolve

        mi "Let ‘yer old pal Miku pay ya back for all of the weird ways you made her body feel today!"
        mi "Even the coach needs to relax every now and then, ya know?"
        s "…"
        mi "…"
        s "Sure, Miku."
        s "Do what you must."
    else:
        mi "Nonsense! Prepare yourself for a platonic shoulder massage!"
        s "But I do not want-"
        mi "I hope you are prepared!"
        s "I am not."

    scene black
    with dissolve

    "The two of us walk over to a stack of mats in the corner of the room and Miku literally pushes me onto them."
    "This is not an exaggeration. "
    "I need to use my hands to catch myself in order to prevent landing on my face and she laughs almost maniacally as she gets behind me and starts massaging my shoulders..."

    scene mikushed26
    with dissolve

    if bonus == False:
        s "Someone help."

    mi "Yes, yes! Surrender to my above-average shoulder massage skills!"
    mi "Feel the burn, Sensei! Feel the burn!"
    s "I can’t tell if you’re going for a supervillain vibe or an 80’s exercise video vibe."

    scene mikushed27
    with dissolve

    mi "Me neither. But it feels good, right?"

    if bonus == True:
        mi "Your shoulders are super stiff. When was the last time anyone helped ya relieve some tension?"

        "I’m going to go out on a limb here and assume she only means shoulder-related tension."
        "I’ve definitely had tension released in other ways on several occasions."

        s "Probably never, to be honest."
    else:
        s "I have never felt this scared in my life."

    scene mikushed28
    with dissolve

    mi "Never?! No wonder why ya feel like a friggin’ brick wall up here."

    "Miku’s fingers dig into the gaps in my shoulder blades and begin to work out what feels like aeons worth of knots."

    if bonus == True:
        "She actually {i}is{/i} surprisingly good at this."
        "I guess small hands don’t really matter much when you subject yourself to hours of athletic training every day."

    scene mikushed29
    with dissolve

    mi "Sorry for sittin’ on top of ya before, Sensei. Had no idea your muscles were so...bleh."
    mi "Even if I’m little-boy sized, it probably put more unnecessary strain on your body."
    mi "You’ve gotta take care of yourself, ya know? What good will you do any of us if ‘ya wind up gettin’ paralyzed and can’t leave the house anymore?"
    s "I’m not sure how going without shoulder massages could cause paralysis, but I’ll try to keep that in mind."
    mi "Good!"
    mi "Also, please don’t tell Makoto about this cause I’m pretty sure she’ll chop my head off even if this is just a wholesome shoulder rub."
    mi "I think she likes you, Sensei. Like, {i}likes you{/i} likes you."
    s "Wow, I wonder what gave you that idea."

    scene mikushed30
    with dissolve

    mi "Did you know she keeps a picture of you in her wallet?"
    mi "I saw it the other day when I was goin’ through her bag lookin’ for some spare change to buy a drink with."
    s "You shouldn’t be snooping through other peoples’ things, Miku."
    mi "Probs shouldn’t be giving my teacher a massage either but here I am."
    s "Yup. Here you are."

    if bonus == True:
        s "I’ll remember this when it comes time for me to cash in on the thigh-rubbing I was promised when I agreed to fill the coaching job."

        scene mikushed31
        with dissolve

        mi "Go rub one of the Kanda girls if you want thighs on-demand. I’m fine with just doin’ things like this for now."
        mi "I can’t be lettin’ things get any weirder between us when my best friend is literally walkin’ around with a mini-Sensei in her wallet."

    scene black
    with dissolve2

    "The pressure Miku applies to my shoulders eases up just seconds after she says that."
    "One minute later, the massage comes to an end and she proceeds to sit there with her hands on my back until we both get up at exactly the same time and start tossing all of the balls we collected into a bin."
    "The sunlight singes my eyes when we step outside after being trapped in the dark for so long."
    "And then, just as always, I watch Miku go on to completely dominate the other girls on the field before I step away from practice and get on with my day."

    $ renpy.end_replay()
    $ miku_love += 1
    $ soccer25 = True
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label soccer30:
...
```

## Code that triggers this event

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccerfield:
    if miku_love >= 0 and firsttimesoccerfield == False:
        jump firsttimesoccer
    if miku_love >= 5 and soccer5 == False:
        jump soccer5
    if miku_love >= 10 and soccer10 == False:
        jump soccer10
    if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
        scene soccerfield
        with dissolve
        "I show up at the soccer field to try and talk to Miku but she immediately runs off and starts talking to one of the other girls."
        "Am I...being avoided?"
        "I should probably try visiting her dorm sometime to figure out what's going on with her..."
        jump saturdayafternoon
    if miku_love >= 15 and day83 == True and mikudorm10 == True and soccer15 == False:
        jump soccer15
    if miku_love >= 20 and soccer15 == True and soccer20 == False:
        jump soccer20
    if miku_love >= 25 and mikudorm15 == True and halloween14 == True and soccer25 == False:
        jump soccer25
...
```