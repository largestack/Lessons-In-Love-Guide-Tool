# Hormones Running Wild
Miku event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=soccer15&go=Go)



## Event preconditions
✅Miku love greater than or equal to 15

✅Event "[Main: Parasite](./day83.md)" is completed (event=day83)

✅Event "[Miku: You and Me and the Night](./mikudorm10.md)" is completed (event=mikudorm10)



## Next events
* [Miku: Coach](./soccer20.md)

## Event properties
* ID: soccer15
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield

## Event code
File: \game\MikuEvents.rpy
Code:
```python
...
label soccer15:
    scene sky
    with dissolve
    play music "highspeedprinter.mp3"

    "I show up at the soccer field to see how Miku’s practice is going."
    "It's another early day, so I wouldn’t be surprised if it was just her here right now."
    "I slowly make my way across the school grounds, listening close for the sound of a whistle or...anything to signify that practice is in session-"

    mi "Sensei! Over here!"

    "But the noise I hear before anything is Miku's voice, calling out to me before I even know where she is."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mikukarin1
    with dissolve2

    mi "Heya! Come to watch us kick some balls around again?"
    s "As long as they’re not mine."
    ka "...............ah."
    s "Good morning to you as well, Karin."
    s "Is Miku making you carry her around the field as training or something?"
    ka "That...That wasn’t the plan, but..."
    mi "We’re just helpin’ each other stretch so that we’re all loosened up when it comes time for the main event later!"
    s "Is what you're doing really going to loosen Karin up? Shouldn't you...maybe switch positions every thirty seconds or something?"

    scene mikukarin2
    with dissolve

    ka "I think I might be a little too heavy for Miku to carry like this..."
    mi "Karin’s gettin’ plenty loose by bendin' over like this, Sensei!"
    s "Can you say that again, but in a more seductive voice?"
    mi "I've never tried a seductive voice before, so I'm gonna say no!"
    mi "I guess this is more like strength training for her, though. But hey, if I get a chance to ride a friend, I'm gonna ride a friend."
    ka "I'm also not sure if this...even counts as strength training since Miku is by far the lightest girl on the team..."

    scene mikukarin3
    with dissolve

    mi "Hey! Less talkin’ and more stretchin’! If you lose focus, you’re gonna drop me and I’m gonna break my ankles!"
    mi "I need my ankles to do...ankle stuff! Like running and...jumping! And..."
    mi "Ankle stuff!"
    ka "I'm going to try and stay quiet so...Miku can keep doing ankle stuff..."
    s "Miku, you should be nicer to the girl who’s keeping you suspended in mid-air right now."

    scene mikukarin4
    with dissolve

    mi "Hey! Who do ya think you’re talkin’ to?! I’m the captain of this ship and if I say starboard you better do whatever the heck that means!"
    s "Isn’t that just a part of the ship?"
    mi "That's it! You're walkin' the plank!"
    ka "Sorry, S...Sensei...Miku is unusually fired up today..."
    s "Any reason why?"

    scene mikukarin5
    with dissolve

    mi "Oh! That’s right! I totally forgot to tell ya, but we’re havin’ a full-on practice game between the girls later on."
    mi "We’re probably gonna be here all day so if you wanna stick around and watch, you totally should!"
    s "Maybe. We'll see how I feel once the afternoon rolls around."
    s "You really have enough players for a practice game, though?"
    mi "Well, normally we wouldn’t. But Karin’s on the softball team too, so she pulled some strings and got a few of them to agree to play!"
    s "You’re on two teams at once, Karin? Isn’t that a little tiring?"

    scene mikukarin6
    with dissolve

    ka "Oh, no! Not at all!"
    ka "I love pretty much all sports, so I figure out how to make it work."
    ka "Sure, it can be a little tiring at times...but it's not like there's really anything else I have to do other than studying."
    ka "Plus, my body was...kind of built for stuff like this, so it’s a lot easier on me than it would be on someone like my sister."
    mi "Where is Kirin, by the way? I thought she was gonna show up early too?"

    scene mikukarin7
    with dissolve

    ka "Who even knows? That girl is always doing her own thing."
    ka "It’s going to get her into trouble one day, I just know it..."
    s "Karin, are you really okay just...continuously balancing Miku like that? You’ve barely moved since I got here."

    scene mikukarin8
    with dissolve

    ka "Oh, right. Miku is on my back. I totally forgot."
    mi "Am I..."
    mi "Am I really that light?..."

    scene black
    with dissolve2

    "Karin arches her back and forces Miku to dismount."
    "Fortunately, Miku does not fall and her ankles remain intact, ensuring that she will still be able to do {i}ankle stuff{/i} in the near future."
    "Whatever that means."

    scene mikukarin9
    with dissolve

    mi "Sorry Karin, I’d offer to lift you up and stuff, but I’m pretty sure you’d crush me."
    ka "I don't weigh {i}that{/i} much...And you can't just {i}only{/i} train cardio, Miku. You need to be training your entire body."

    scene mikukarin10
    with dissolve

    mi "I know, but...You’re just so muscley that there’s no way I’d be able to even get you off the ground! It'd be a lost cause!"
    s "Didn’t you try to pick me up the other day? I’m bigger than Karin."

    scene mikukarin11
    with dissolve

    mi "Yeah and how well did that work out? It was more like a backwards bear hug than anything else."

    scene mikukarin12
    with dissolve

    mi "I’m sure Karin could do it, though! She’s probably even stronger than you, Sensei!"
    mi "You should look at her abs!"
    mi "Karin! Lift up your shirt and show Sensei what you’re working with!"

    scene mikukarin13
    with dissolve

    if bonus == True:
        ka "W-w-what?!? N-n-no way!"
        ka "There’s...There's no way I could ever do something like that! Not in a gazillion years! Is gazillion even a number?!"
        ka "Would Sensei even {i}want{/i} to see something like that?! Because I sure as heck wouldn't if I was him! No way! Nuh-uh!"
        s "Not gonna lie, I kind of want to see."
    else:
        ka "Whssashshshahshashahshshshshshshabbbbabbbbbbbbbba!!!!!"
        s "Bless you."

    scene mikukarin14
    with dissolve

    ka "Why?!"
    ka "Also, is it just me or am I really loud right now?!"
    mi "Hehehe..."
    mi "This...{i}This{/i}, children...is the scent of love."

    scene mikukarin15
    with dissolve

    ka "L-L-L-L-L-LOVE?!?!?"
    ka "Miku! W-What are you talking about?!"
    mi "Sensei, as ya can see, Karin ain't very good with boys. She has this thing where whenever she tries to talk to one, she gets all...broken."
    ka "Miku! What do you think you’re telling him?! H-H-He doesn’t want to hear-"
    s "Not gonna lie, I kind of want to hear."

    scene mikukarin16
    with dissolve

    ka "Why are you doing this to me?!"
    ka "Do you like watching me suffer?!"
    s "Of course not. I just think you’re really cute when you get flustered and I’d like to see a little more of that side of you."

    scene mikukarin17
    with dissolve

    ka "C..."
    ka "..."
    ka "Huh?"
    ka "..."
    ka "C..."
    ka "What?"
    ka "What did you say?"
    ka "What’s-"
    ka "Where am I?"

    if bonus == True:
        mi "Ahh, youth..."
        mi "Sunburn...sweat...hormones running wild..."
        mi "What a time to be alive."
    else:
        s "Kumon-mi."

    ka "C..."
    ka "C...C...C...C..."
    s "Wow, she really {i}is{/i} bad with boys."

    scene mikukarin18
    with dissolve

    mi "Duh! Ya think your old pal Miku would lie to ya about something as silly as that?!"
    mi "We’re brothers in arms, Sensei! We’re gonna take on the world!"
    s "What does that have to do with the way Karin handles men?"

    scene mikukarin19
    with dissolve

    mi "Idunno. But it’s fun, right? Just look at how her eyes get all squinty whenever she doesn’t know what to say."
    ka "C...C...C...C..."
    s "Cute."

    scene mikukarin20
    with dissolve

    ka "MMMMMMMMMMMMM!!!!!!!"
    s "Wow. This {i}is{/i} actually kind of fun."

    if bonus == True:
        s "What do you think would happen if I touched her?"
        mi "Like I’ve been sayin’! If you become our coach, you could probs even rub those monster-thighs whenever ya want! Doesn’t that get your blood pumpin’?!"
        s "Yes. Though, not in a way that is exactly safe or acceptable in the middle of a soccer field."
        mi "Hm? Whatcha talkin' about?"
        s "Nothing. Just don't look down."

        scene mikukarin20r
        with dissolve

        mi "Well, of course I'm gonna look down if ya-"

        scene mikukarin21
        with dissolve

        mi "WOAH! WHAT THE HECK IS GOIN' ON DOWNSTAIRS?!"
        s "Something that will very likely kill Karin if she breaks out of her trance state."

    else:
        s "If I was not dedicated to educating women like you two, I may even contemplate asking her on a date to see if her behavior toward me adjusts in any form."

    scene mikukarin22
    with dissolve

    ka "C...C...C...C..."
    mi "I..."
    mi "I suddenly feel...kinda dizzy..."
    s "Want me to take you to the nurse's office?"

    scene mikukarin23
    with dissolve

    mi "To do what?! I ain't goin' anywhere with ya 'til you take the friggin' rocket launcher out of your pants!"
    s "I can assure you that the last thing you want right now is for me to remove {i}anything{/i} from my pants."
    s "Or the first. I don't really know with you yet."

    scene mikukarin24
    with dissolve

    mi "Somehow...gettin' even...dizzier..."
    ka "C...C...C...C..."

    "Well, then. This has certainly turned into a strange situation."

    if bonus == True:
        mi "Sensei...will I ever be able to see again?..."
        mi "We've got the...practice game today and...I've gotta..."
        ka "G-game?..."
        ka "Oh...right...we have a game..."
        ka "We need to...practice...for the..."
        ka "For the game..."
        s "Karin, open your eyes."
        ka "I can't...I closed them too tightly and now they are shut forever."
        mi "Aren't guns...illegal in Japan, Sensei? Where'd ya...get your hands on one that size?..."
        s "You know what? I think maybe you two need a little time to recharge."
        ka "To...recharge..."
        ka "Y...Yeah..."
        ka "Miku...let's go...recharge..."
        mi "Yeah...Yeah, we've...we've gotta...do the thing..."
        s "That's right. Go do the thing and I'll..."
    else:
        mi "I think we are under attack!"
        s "It must be a part of the space war. They are dropping chemicals on the soccer field causing the two of you to act strange."
        s "I will now go and defeat the aliens."
        s "If I do not return, please tell my accountant I appreciate her."
        mi "Good luck, Sensei! You'll need it!"

    scene black
    with dissolve2

    "I'll go do something about the cause of all of your problems..."

    if bonus == True:
        "I leave the two incredibly hormonal soccer team members to their own malfunctioning devices and attempt to get on with my day."
        "I just...wind up taking a quick trip to the nearest restroom first."
    else:
        "I activate my super legs and jump into space."
        "I land on a space ship and destroy ten aliens before having to jump back down."
        "I can only hold my breath for so long."

    $ renpy.end_replay()
    $ soccer15 = True
    $ miku_love += 1
    stop music fadeout 4.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label soccer20:
...
```

## Code that triggers this event
File: \game\MikuEvents.rpy
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
...
```