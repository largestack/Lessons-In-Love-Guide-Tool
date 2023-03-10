# Fuck The Police (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 5

* Event [I See You](./streets10.md) (Yumi) is completed)



## Next events

* [Yumi: Yumi Revitalization Project](./yumidorm10.md)

## Event properties

* Id: yumidorm5
* Group: Yumi
* Triggered by label: yumidorm
* Triggered by branch label: yumidorm
* Triggered by path: yumidorm->yumidorm5

## Official wiki page

[Fuck The Police](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumidorm5&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm5:
    play sound "knock.mp3"

    "I knock on Yumi’s door, knowing well that she likely won’t respond."
    "But, on the off chance that she confuses me for a delivery man or something, maybe I’ll get to spend some time with her after all."
    "Even if it’s only for a few seconds..."

    y "Who is it?"

    "Yumi speaks through the door in a rather blasé sort of way. Not angry, not
    enthusiastic, just...disinterested."

    s "Uhh...delivery for Yumi Yamaguchi?"
    y "…"
    s "…"
    y "You think I don’t recognize your voice, douchebag?"
    s "I’m sorry miss, you must have me confused for someone else."
    y "Yeah? Then what are you delivering?"
    s "A...pizza?"
    y "I didn’t order a fucking pizza."
    s "Someone must have ordered it for you."

    play sound "thump.mp3"
    with hpunch

    "Yumi slams her foot or her fist or something against the door, shaking the walls of the entire dorm."
    "Weird. This place seems relatively new. Is the anger of a[school]-delinquent really enough to send it spiraling into disrepair?"

    y "Listen up, asshole. I don’t know what makes you think I’m going to let you in my room, but if you don’t leave right now, I’m calling the cops."
    s "You threaten to call the cops pretty much every time we associate and haven’t done it yet. I’m going to take my chances."
    y "Well...that’s just because I hate cops just as much as you! Fucking pigs can all get bent for all I care."

    if day == 3:
        s "Can you at least open the door? I’m starting to feel kind of uncomfortable out here."
        s "Especially with Chika right next to me."

        "I have no idea how she hasn’t noticed this exchange, yet..."

    else:
        s "Can you at least open the door? I’m starting to feel kind of uncomfortable out here."

    play sound "dooropen.mp3"
    scene ftpreduxangry
    with fade

    "Yumi aggressively storms her way out of the room and grabs the collar of my shirt."

    y "Just fucking...come with me if you need to talk to me that desperately. I don’t want people to think the two of us are friends."
    s "Won’t it also look weird if you’re dragging me through the halls?"
    y "Are you fucking coming or not?!"

    scene ftpreduxgone
    with dissolve
    stop music fadeout 5.0

    "Yumi lets go of my shirt and storms down the hallway. I’m left with no choice but to follow after her..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene yumioutside1
    with dissolve2

    "I wind up following Yumi several blocks away to a small shopping plaza that has already shut down for the night."
    "She comes to an abrupt stop in front of a restaurant, scans the area to make sure no one is around, and then proceeds to scream at me because she is Yumi and that is what she does."

    play music "yumiska.mp3" fadein 5.0

    y "What do you want?!"

    "The ska music starts playing again."

    s "Just wanted to see if you were in the mood to hang out."
    y "Why?!"
    s "Because I want to spend time with you."
    y "{i}Why?!{/i}"
    s "Because...uhh..."
    s "Sorry, what answer could I give right now that would make you the least mad at me?"

    scene yumioutside2
    with dissolve

    y "Jesus Christ, you’re out of your fucking mind."

    if bonus == True:
        y "Didn’t you get the hint after I freaked out on you about that fucking disgusting kiss you forced on me?"

    y "I don’t want to be around you. Ever."
    s "Then why didn't you just stay in your dorm?"

    scene yumioutside3
    with dissolve

    y "Because I didn’t want fuckin’ Chika or somebody else thinkin’ that we actually spend time together! Is that really so hard to believe?!"

    scene yumioutside1
    with dissolve

    if bonus == True:
        y "Isn’t it enough for you that you’re already fucking like...half the girls in our class?"
        y "Jesus, I wouldn’t even be surprised if you had your fucking [niece] groomed already."

        "To be fair, Ami doesn't really require much...{i}grooming.{/i}"

        s "I’m not ‘fucking half the class,’ Yumi...If I was, do you really think I’d be spending my time trying to talk to you?"

        scene yumioutside4
        with dissolve

        y "I don’t fucking know. Probably?"
        y "Don’t guys think of girls like fuckin’ trophies or whatever? That’s how it’s always seemed to me, at least."
        s "What do you mean by that?"
        y "I’ve just been hangin’ around mostly guys for years now and all they ever talk about is girls and shit. It’s annoying as fuck."

        "Oh, right. I forgot that was a thing."

    s "Do you have {i}any{/i} female friends other than Chika?"

    scene yumioutside1
    with dissolve

    y "Why does it fucking matter what kinds of friends I have? Why do you want to know?"
    s "I just think it sounds kind of lonely not really having anyone to talk to."
    y "And I think it's time for you to mind your own fucking business!"
    y "I’m perfectly fine on my own. Always have been, always will be."

    scene yumioutside4
    with dissolve

    y "Besides, why the fuck would some random ass dudes vanishing make shit any worse for me? If anything, life’s gotten kinda easier since they've been gone."
    y "Don’t gotta worry about all the bullshit like how I should be more ‘girly’ or whatever. Fuck that. I’ll be however I wanna be."
    s "Good. More power to you."
    s "Just don’t go causing too much trouble. I’m pretty sure Chika doesn’t have the money to bail you out of jail if you get arrested."

    scene yumioutside5
    with dissolve

    y "Pfft. Fuck gettin’ arrested. Ain’t no pig doin' shit about me. If they were gonna arrest me, I’d have been locked up years ago."
    s "For what? Picking the locks on those pachinko machines you told me about?"

    scene yumioutside1
    with dissolve

    y "Quit it with the fuckin' pachinko machines! I don't see {i}you{/i} out there strugglin' to make a fuckin' life for yourself! "
    y "I still don’t even get why you dragged me out here in the first place if we’re gonna just talk about which laws I break and shit!"
    y "Are you a cop?! Because you're acting a lot like a fuckin' cop right now."
    s "I would be an extremely bad cop."
    y "Yeah, well you're an extremely bad teacher too and that hasn't stopped you."

    if bonus == True:
        y "Listen dude, I already told you I’m not gonna fuck you. So just get the hell outta here and let me go home."
        s "I’m beginning to think you aren’t having fun tonight."

        scene yumioutside6
        with dissolve

        y "{i}I wonder if kickin’ him in the dick would give me enough time to get away...{/i}"
        s "I can hear you, Yumi."
        s "Just tell me what I can do to get on better terms with you."
        y "Well, you could stop callin’ me to your office for one."
        s "Hey. I may suck at being a teacher, but I can’t just {i}not{/i} do anything about you bullying the other girls."
        y "Right. Because you’re fucking them and need to keep ‘em happy so they’ll let you shove your gross-ass micropenis inside."
        s "Yumi, I can assure you that I do not have a micropenis."

        scene yumioutside1
        with dissolve

        y "Whatever, doesn't mean it's not gross."

    s "So other than letting you bully everyone, what else can I do?"

    scene yumioutside4
    with dissolve

    y "How am I supposed to know? I can’t just fuckin’ decide to like you when I’ve gotten so used to treatin’ you like this."
    y "Specially not with all the shit you've done to me."
    y "People don’t just fuckin' change overnight, man. You’re not some...magical fucking exception to that."

    "I beg to differ, but I'm not about to unload my weird circumstances onto Yumi when even I don't understand them yet."

    s "I know that people don’t change overnight. But I’ve been following you around for weeks now trying to get to know you."

    scene yumioutside1
    with dissolve

    if bonus == True:
        y "Right. And you also almost pushed me over a goddamn guardrail while mouth-[raping] me. Real good job of gettin’ to know me."
    else:
        y "Right. And you also hugged me when I didn't want you to. Real good job of gettin’ to know me."

    if chikadorm10 == True:
        s "Weird things keep happening in that part of town."
        s "And while I know that isn't an excuse, it-"

        scene yumioutside6
        with dissolve

        y "No, I'm calling bullshit. That {i}is{/i} an excuse."
        y "I’m not gonna fuckin' believe that you just...turn into somebody else based on what part of the city you're in. Get real."

    else:
        s "Again, I’m sorry about that. Something...came over me."

        if bonus == True:
            y "Yeah, it’s called a fuckin’ hard-on. Learn to control yourself."

    s "All I’m saying is that I think you wouldn’t hate me so much if you tried to talk to me without insulting me every once in a while."

    scene yumioutside4
    with dissolve

    y "Impossible. Just seeing you makes me feel sick to my stomach."
    s "Are you sure you aren’t in love with me? That could also cause you to feel a little-"

    scene yumioutside7
    with dissolve

    y "In LOVE with you?! Are you fucking drunk?!"
    s "No. I actually chose to visit the dorms {i}instead{/i} of the bar tonight."
    y "Well it sure fuckin’ sounds like you are! I don’t give a shit about {i}love{/i} or {i}feelings{/i} or ANY of that fucking nonsense!"
    y "That kinda shit is for Chika! You wanna hang around a girl who’s actually got a chance to fall for you? Hit {i}her{/i} up. Not me."

    if bonus == True:
        y "And shit, dude. For all I know, you could be fucking her already as well. God knows it might get her to fuckin' relax a little."

    if chikatownfirst == True:
        "I can...definitely see myself doing that soon enough. But there are other issues at hand here."

        if bonus == True:
            s "Yumi, I can promise you now that I have not fucked your roommate."
        else:
            s "Yumi, I can promise you now that I have not hugged your roommate."

    else:
        if bonus == True:
            s "Yumi, I can promise you now that I have not fucked your roommate."
        else:
            s "Yumi, I can promise you now that I have not hugged your roommate."

    scene yumioutside4
    with dissolve

    y "Whatever. Not like I fucking care since I know you want to."
    y "At least she’s smart enough to not let some assclown like you screw her over."
    y "Chika woulda cut your fuckin’ head off if you were to pull the same kinda shit you pulled with me."

    "In a rare moment of what seems like vulnerability, Yumi puts herself down in favor of Chika."
    "But why?"

    s "Are you saying that Chika is stronger than you?"
    y "That’s absolutely not what I fuckin’ said..."
    y "I’d kick Chika's ass in a fight, but that's not what this is about."
    y "She deals with shit much differently than I do. She’s always doin’ things head-on and I’m-"

    scene yumioutside8
    with dissolve

    y "...tch. Who the fuck even knows? Not like it matters."
    s "You sure you don’t want to go on with that? It sounded like you were going to finally start opening up to me for a second."

    scene yumioutside5
    with dissolve

    y "Heh. Dream on, asshole. That’s already more than you were supposed to get tonight."
    y "You’re lucky I pitied you enough to follow you out here."

    "Does she really not remember that she's the one who led {i}me{/i}?..."

    s "Yup. Sure am. That’s why I’m not going to push you any further tonight."
    s "You’ll come around to me eventually. I think I just need to keep annoying you until you break."
    y "It’s gonna take a lot more than just followin’ me around to break me, you know? I’m not like the girls you spend most of your time with."
    s "Exactly. Which is one of the many reasons I’m trying to get closer to you."
    y "Well, as long as none of those reasons are turning me into your pet or whatever the fuck you’re doing to all those girls-"
    y "I guess there are...worse things out there."

    if bonus == True:
        y "You’re still a little bitch, though. And I’ll cut your fucking dick off if you kiss me again."
    else:
        y "You’re still a little bitch, though. And I’ll cut your fucking hands off if you ever hug me again."

    s "Understood..."

    scene black
    with dissolve2

    "I try to walk Yumi back to the dorm, but she says something about how she’s
    old enough to walk three blocks on her own."
    "Already exhausted from being yelled at so much, I submit and give her a few
    minutes to get away before I leave as well."
    "Even though we weren’t able to have a clear discussion on any single topic
    for more than a minute or so, I feel like I learned a lot about her tonight."
    "I know that Yumi acts tough all the time...but it seems like she might actually be pretty vulnerable at the end of the day."
    "I just wonder what made her like that."
    "Or what {i}makes{/i} her like that."
    "I want to know more."

    $ renpy.end_replay()
    $ yumidorm5 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumidorm10:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm:
    if yumi_love >= 5 and streets10 == True and yumidorm5 == False:
        jump yumidorm5
...
```