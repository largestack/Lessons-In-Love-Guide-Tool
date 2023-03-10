# Remove Curse (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Mating Season](./chikalust25.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwartwo14
* Group: Main
* Triggered by label: chikalust25skip
* Chain sources: chikalust25
* Chain sources path: chikalust25

## Official wiki page

[Remove Curse](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo14&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label dormwartwo14:
    "{i}Roughly fifteen minutes later...at a bar with a horrible name...{/i}"

    scene girlsreturntobar1
    with dissolve2
    play music "10c.mp3"
    $ dorm2war2points += 1

    n "Ladies and...oh. I guess Sensei isn’t here yet. So...just ladies, then!"
    n "Please feast your eyes on the amazing...outstanding...and only {i}mildly{/i} incorrigible...Kirin Kanda! "
    ki "That’s right, that’s right. It is I, Kirin Kanda, who has located the trophy and brought home one more point to the lovely ladies of the second floor."
    ki "Please hold your applause as I already know how great I am. But, if any of you find yourself absolutely {i}needing{/i} to congratulate me in some way, please note that I will always accept massages. Thank you."
    a "And please don’t feast your eyes on me...Ami Arakawa. The loser."
    ay "They...{i}did{/i} have an unfair advantage with Noriko on their team considering that she’s from the area and whatnot..."

    scene girlsreturntobar2
    with dissolve

    n "But it was not {i}me{/i} who found the treasure, it was Kirin! All by herself without any assistance at all!"
    ki "That’s right. I didn’t find this because of Noriko. I found it because of my deep connection to Miku and my ability to sniff out her scent from miles away."
    n "Exactly. But, to be fair, Miku’s so far into gyarudom right now that anyone could smell her perfume from miles away."
    mak "Please leave Miku alone as it’s her first time doing such things and that there will likely be several mistakes."

    scene girlsreturntobar3
    with dissolve

    n "How’d things go on your end, Ayane? I mean...you obviously didn’t find the trophy, but...did you guys have fun, at least?"
    ay "Uhh..."

    if amifingered == True:
        ay "I’m not sure. {i}Did{/i} we have fun, Ami?"
        a "Losing is never fun. Especially when losing means you get to spend less time with your uncle and that everybody is going to hate you now."
        ay "Okay. Then I guess we did not have fun...no."

    else:
        ay "I mean...{i}I{/i} had fun. But I think Ami’s a little down in the dumps since she wasn’t able to earn a point for us."
        a "Once again, the enemy has won while I have been forced to stand on the sidelines and pretend to be happy for them."
        ay "I don’t think anyone’s expecting you to pretend that, Ami."
        a "Good. Because I hate Kirin and Noriko now and I want their floor to collapse."
        ay "You realize we’d probably be killed if that ever happened, right?"
        a "Yes. But at least we’ll die {i}together.{/i}"

    scene girlsreturntobar4
    with dissolve

    mak "As exciting as it is to watch you all talk about how much fun you had, I’m going to need to see that trophy."
    ki "Why? Do you really think I would have gone to the effort of buying a fake one just to win some contest?"
    mak "No...I need to give it back to Miku."
    ki "{i}I{/i} will give it to Miku. Or rather, I will sell it back to her for a small price. Finders keepers."
    mak "Fine. Then I {i}do{/i} need to verify it’s the correct trophy as, even at the height of my disinterest in this year’s war, I still want to win...And what’s left of my life is still ruled by proper protocol."
    ki "Well, if any of us were having fun, we’re sure not now. Thanks for dragging the mood down, Makoto."
    mak "You’re very welcome. Now, please bring that here as I would like to go home."

    scene black
    with dissolve

    n "Home? You’re leaving already? "
    n "Don’t we still have a handful of competitions left?"

    scene girlsreturntobar5
    with dissolve

    mak "We do. But I’m not needed for any of them and I’ve already fulfilled my purpose in orchestrating and finalizing the scavenger hunt."
    mak "And seeing as the scavenger hunt is now over, so is my job. Thank you for relieving me of what little responsibility I had this year. It’s been fun. Except for the fact that it hasn’t."
    ki "You know I was just fucking around when I said you were dragging the mood down, right? It’s not like I actually want you to leave."
    n "Yeah, stick around for a little while. You can hang out with us."

    scene girlsreturntobar6
    with dissolve

    mak "That’s very kind of you, but I’ll have to respectfully decline. My sleep schedule has become rather unpredictable lately and I’m still in the process of getting things back to normal."
    mak "As such, I’ve found it best to just capitalize on every opportunity where I actually {i}want{/i} to sleep."
    mak "That said, I will likely fail and find myself back here before the night’s end. But, for now?...No thank you."
    n "You try taking sleeping pills or anything? My sister had insomnia for a while and seemed to do a little better on those."
    mak "Do you...actually have any?"
    n "Yeah. I’ve got a whole pharmacy in my bag. "
    mak "I see no bag."
    n "Sorry. I {i}normally{/i} have a whole pharmacy in my bag. But right now, I’ve just got all of my essentials strapped to my upper thigh. Pocket knife, tampons, pills, 4x7 pictures of Sensei...you name it, I’ve got it."

    scene girlsreturntobar7
    with dissolve

    ki "You’re like some kind of prison contraband dealer."
    n "Thanks! I really appreciate that."
    mak "Yeah, I’m good on thigh-pills. But thanks for the offer. "
    ki "What else do you have down there?"
    n "Cell phone...glasses...second pocket knife...a bag of gummy bears...normal stuff."
    ki "How do you even walk with all of that on you?"
    n "I normally don’t. I am doing this for the sake of the costume and if something happens to chafe or cut my leg, I’ll just deal with it until I get back to the dorm and can patch myself up."

    scene girlsreturntobar8
    with dissolve

    ki "You gonna be able to wait that long? Cause I’m pretty sure that’s happened already judging by the blood trickling down your leg."
    n "That’s fine. I brought bandages too."
    mak "Maybe...apply one before you wind up staining the carpet."
    n "Don’t need to! Brought shampoo for carpets as well in case something like this happened!"

    scene girlsreturntobar9
    with dissolve

    ki "How fucking big are your thighs?!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene girlsreturntobar10
    with dissolve2

    m "Oh, welcome back. How did your scavenger hunt go?"
    a "Let’s avoid that topic altogether for now. In fact, better question- how did {i}your{/i} contest go? Please tell me you won."
    m "I won."

    if maidwarmaya == True:
        scene girlsreturntobar11
        with dissolve

        a "Oh, thank god. I was worried that you were going to be too embarrassed to actually do any maid stuff."
        m "You underestimate what I am willing to do for food."
        ay "The buffet tickets were really that important to you, huh?"
        m "Yes. Not to mention that being a maid is almost {i}excruciatingly{/i} easy and that the return on this investment makes it one of the best decisions I have ever made."

    else:
        a "Oh, thank god. I was worried that-"
        m "Unfortunately, I won by so much that I actually wound up losing."

        scene girlsreturntobar12
        with hpunch

        a "What?! How is that even possible?! That makes no sense!"
        m "It makes perfect sense when you remember who the judge of this competition is and how passionately he enjoys making my life hell."
        ay "Are you saying Sensei only voted against you because...he wanted to piss you off?"
        m "That is precisely what I am saying. And I’d likely be quite torn up about it if being a maid wasn’t the actual easiest thing I have ever had to do."

    scene girlsreturntobar13
    with dissolve

    a "Wait...{i}easy?!{/i} What do you mean {i}easy?!{/i} I work my butt off at that place!"
    m "Doing what? The same exact things you do at home but {i}without{/i} the actual “maid-like” parts? Because I’d call house-Ami more of a maid than maid-Ami."
    m "So long as you know how to talk and appeal to people, being a maid in a cafe is as simple as snapping your fingers and learning to draw a heart on a plate of eggs."

    scene girlsreturntobar14
    with dissolve

    a "Were you...actually good, though? Like...did you really do...maid-like stuff in front of Sensei?"
    m "Why? Are you jealous?"
    a "Yes, but I don’t know if I’m jealous of you for being the one to serve him or jealous of {i}him{/i} for being the one you served."
    ay "I would like service from maid Maya as well, please."

    scene girlsreturntobar15
    with dissolve

    m "It’s {i}Moe Moe Maya,{/i} thank you very much."
    a "Wow...you actually {i}did{/i} do it, didn’t you?"
    m "Again, the lengths I am willing to go to for food are quite dramatic."

    if amifingered == True:
        m "But that’s enough about me. Please tell me how-"

        scene girlsreturntobar16
        with dissolve

        a "I told you I don’t want to talk about that."

        scene girlsreturntobar17
        with dissolve

        m "I’m sorry?"
        a "Me and Ayane walked around the old district looking for a trophy that we never found."
        a "Nothing else happened and we’re done talking about it now."
        m "..."
        a "..."

        scene girlsreturntobar18
        with dissolve

        m "Ayane, do {i}you{/i} have anything you’d like to add? Or should I just assume that this is one more thing the two of you don’t want me to know for some reason?"
        ay "You say that...as if you’ve never kept anything from us..."
        m "..."
        a "..."

        scene girlsreturntobar19
        with dissolve

        m "Very well, then. Forget I asked in the first place. It’s not as if I care about anything that goes on on that side of town anyway."
        ay "Why is it you...avoid going over there in the first place, Maya? It’s not like-"
        m "Sorry, but if you two aren’t going to answer questions, I have no reason to answer any directed toward me."
        m "Now, if you’ll please excuse me, I’m going to go stand off to the side of the room and remember the good old days when my friends did not intentionally exclude me from things."

        scene girlsreturntobar20
        with dissolve

        ay "Oh...okay. See you later, then."
        a "Hah..."
        ay "I can’t tell if we actually pissed her off or if she’s just being tsundere again."
        a "Probably both. But at least it’s her being left out this time instead of me."

        scene girlsreturntobar21
        with dissolve

        ay "Huh? What do you mean?"
        a "I mean that you two have been talking to each other alone and coming to school alone and doing a bunch of other stuff {i}alone{/i} lately and it makes me feel bad!"
        a "We’re supposed to be the Sensei Love Squad! Not the “Secretly Exclude One Person From Everything Important” Squad!"
        ay "I’d hope so. That’s a really long name for a squad."

        scene girlsreturntobar22
        with dissolve

        a "Ugh. I’m just tired, I think. Today was emotionally draining and I didn’t expect you to find out about that thing that you found out about until later."
        ay "I didn’t realize you...expected me to find out at all."

        scene girlsreturntobar23
        with dissolve

        a "You were always going to find out. I just figured I would have {i}known{/i} when you found out since I didn’t think Sensei would just openly tell you about it."

        scene girlsreturntobar24
        with dissolve

        a "But the fact that he did means that he just loves me even more than I thought he did! I mean...why else would he openly profess all the things we do together to someone {i}else{/i} who loves him?"
        ay "Uhh...Ami?"
        a "What? Are you going to tell me {i}you’re{/i} sleeping with him too? Because we both know that would never happen if he loves {i}me{/i} as much as he obviously does."
        ay "Uhh..."

        scene girlsreturntobar25
        with dissolve

        ay "You know what? I’m thirsty."
        ay "Let’s go see if Sara can make us anything non-alcoholic."
        a "Okay, Ayane. Whatever you want!"

        scene black
        with dissolve2
    else:
        scene black
        with dissolve

        m "But that's enough about me. Tell me how things went for you guys."
        a "Well, it all started when-"

    "........."
    "......"
    "..."

    scene girlsreturntobar26
    with dissolve2

    t "Is something the matter, Emerald Guardian? It is not like you to call for a guild meeting with only two members."
    mo "Can we drop the act for a second, Tsuneyo?"
    t "Act?"
    mo "I’ve gotta be mean to you for a minute and it’s gonna be mighty hard doing that with you calling me by my codename."

    scene girlsreturntobar27
    with dissolve

    t "I’m confused. Have I done something to anger you? Because I don’t believe I have acted out of the ordinary in any-"
    mo "The bloody hell was that last night?"
    t "I believe the technical term is “Standing up comedy.” It is short for “Stand-up comedy,” which is a style of telling jokes that-"

    scene girlsreturntobar28
    with dissolve

    mo "I obviously mean about the “jokes” you told. Those weren’t jokes {i}at all.{/i}"
    mo "Do you have any idea how hard I worked to patch things up with the Herald of...with {i}Sensei?{/i}"
    mo "Were you trying to ruin that? Do you not want me near him for some reason you have not yet disclosed to me?"
    mo "You are supposed to be my best friend. I’m supposed to be able to trust you. You should have known how uncomfortable that would have made me and-"

    scene girlsreturntobar29
    with dissolve

    mo "And..."
    mo "Oh..."
    t "Are you referring to the jokes about the semen?"
    mo "..."
    t "Molly?"

    scene girlsreturntobar30
    with dissolve

    mo "Huh? Yeah. Those are the ones."
    t "I understand. But I did not think bringing those things up in such a setting would lead to such a reaction from you."
    t "There are many comedians who draw upon real life experiences to-"
    mo "Have you not learned compassion in all of our time together?"
    mo "Have you not learned the things that make me worried or uneasy? Or scared or nervous? Or any of that? Any of the things I have finally begun to move {i}past{/i} feeling on a daily basis?"
    mo "Why would you wake those up? And for {i}laughs{/i} no less..."
    mo "Am I a joke to you?"
    mo "Or are you just {i}pretending{/i} to be oblivious right now?"
    t "..."
    mo "Tsuneyo...talk to me."

    scene girlsreturntobar31
    with dissolve

    t "I am not good at that."
    mo "What, and I am?"
    mo "There are too many skill trees in life to spec into all of ‘em...and there are gonna be times when we’ve gotta dig into our spellbook and put stuff we forgot we even had onto the hotbar."
    mo "What I’m trying to say is...just because we’re not good at certain things doesn’t mean we can avoid them forever if the mechanics of a fight call for them."
    mo "It’s either that or we just give up. And if there is anything I have learned from my time in Elden Ring, it is that Malenia is not going to just kill herself."
    mo "Peer into that inventory and see what you’ve got, Tsuneyo. Because there’ll always be something that’ll help...and whatever that something is is a little different for everybody."
    t "I do not understand any of what you just said, but I will do my best to explain my actions."
    t "One year ago, my inattentiveness and disregard for your safety led to you being harmed."
    t "And while you have chosen to believe that you were not harmed at all, it does not change what I saw and my thoughts on what may have happened that night."
    t "If I had only been there sooner, I could have prevented-"
    mo "It’s not your job to take care of me, Tsuneyo."

    scene girlsreturntobar32
    with dissolve

    t "But it is when you can not take care of yourself."
    t "Were you in the right state of mind to make decisions that night? Or were there multiple “debuffs” and “status effects” that disallowed you from acting of your own volition?"
    t "You are the first person other than my father that I have ever connected with. And it is my duty to protect you."
    mo "How are you going to protect me from something that already happened?"

    scene girlsreturntobar33
    with dissolve

    t "By not letting it happen again."
    mo "That’s not what you did."
    mo "All you did was reawaken the uncertainties of that night in not just me, but in Sensei as well."
    mo "I’m sure this will sound hard to believe, but I think that...he was just as much of a victim in that as I was."
    mo "No one paid closer attention to him in the coming days than I did. Not even Ami. And the way he acted was not of a man who did something malicious, but of a man who had something malicious done to {i}him.{/i}"
    mo "What if I was the one who forced his hand? And what if all of those “jokes” you told reminded him of that?"
    mo "There’s far too much unknown about that night to justify telling stories about it. But even if all {i}was{/i} known, it would not be your story to tell."
    t "..."
    mo "You really disappointed me, Tsuneyo..."
    mo "I didn’t think that would ever happen with you."

    scene girlsreturntobar34
    with dissolve

    t "I apologize for my actions...but I can not rid my mind of the horrible state I saw you in that night."
    t "And saying what I did seemed like the only way to make it so I wasn’t the only one who knew anymore."
    t "The idea of anyone harming you is too much for me to bear. And I believe that anyone who does so should have to pay a price."
    t "But...as it appears my words were truly just taken as mere “jokes,” you don’t have anything to worry about..."
    mo "I do, though. I have to worry about you doing that again."
    t "Molly..."
    mo "Tell me you {i}won’t.{/i}"
    mo "You can protect me all you want from things that haven’t happened yet, but don’t try rewriting the past and turning matters I have already settled into ones much greater than they wound up being."
    t "I don’t trust him with you anymore."
    mo "Do you trust {i}me?{/i}"
    t "Of course."
    mo "Then trust the {i}me{/i} who trusts {i}him.{/i}"
    t "..."
    t "What?"
    mo "That quote works better in its original context and phrasing but, what I’m trying to say is just...let me decide things like this for myself."
    mo "I wouldn’t care so much about my relationship with Sensei if he was not an important person to me."
    mo "And, as another person who is very important to me, you have to understand that."
    t "..."
    mo "..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    t "I will do my best."
    t "Please continue to be kind to me in the future."
    mo "Of course..."
    mo "And please let {i}me{/i} continue to dress you up in different outfits."
    t "Okay. But please stop groping me when I do so."
    mo "Please don’t tell me how to live my life."

    $ renpy.end_replay()
    $ dormwartwo14 = True

    "........."
    "......"
    "..."

    jump dormwartwo15

label dormwartwo15:
...
```

## Code that triggers this event

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
tb "Is such a thing even possible? That sounds-"

    play sound "doorslam.mp3"
    scene poorgirldoggystyle32 with hpunch

    tb "What on earth am I doing?! I’m no peeping tom! I’m a distinguished woman of utmost importance who..."

    scene poorgirldoggystyle33
    with dissolve

    tb "Who has not had sex in a very long time."
    c "{i}Ah! Ah! Ah! Yeah! Just like that! Just...like that!{/i}"
    tb "I’m just making sure they don’t break anything. There are very expensive items in that room."
    c "{i}AAAAAAAHHHHHH FUCK IT’S SO BIG!{/i}"
    tb "Oh, who am I kidding? I haven’t seen anything this exciting in ages."

    scene poorgirldoggystyle34
    with dissolve

    tb "I suppose watching for a little while won’t hurt."
    to "Watching what, Mother? Is something happening in my room?"

    play sound "doorslam.mp3"
    scene poorgirldoggystyle35
    with hpunch

    tb "No."
    to "I see."
    to "In that case, would I be able to enter? I left my-"
    tb "Whatever you need, go buy a new one."
    to "But-"
    tb "Right now. That is an order."
    to "But Mother, you always say-"

    scene black
    with dissolve

    tb "Oh, how about I go with you?! That sounds like a fun bonding experience, doesn’t it?!"
    to "It does! But...I have the next Dorm War contest to attend and-"
    tb "Here’s an excellent idea! How about you tell me all about it on the way out of the grand foyer?!"

    "........."
    "......"
    "..."

    scene poorgirldoggystyle36
    with dissolve2

    c "Hah...hah...hah...hah...hah..."
    c "That was...the greatest thing...that has ever happened to me..."
    s "You’re just high on the afterglow right now. Pretty soon, you’re going to realize that your costume is ruined and that your surrogate mother just watched you have an orgasm."

    scene poorgirldoggystyle37
    with dissolve

    c "Yeah...that was weird. But it’s not like she didn’t already know about us after the onsen."
    c "Plus, she’s my {i}surrogate{/i} mother. Which means it’s a lot less weird for her to watch me getting fucked than if my {i}actual{/i} mom did."
    s "I think we’d have much bigger problems on our hands if your actual mother was watching us have sex as that would imply the existence of zombies."
    c "Ugh...what the fuck am I gonna do about my costume?"
    s "Save it. This outfit is a treasure and I will not let it go to waste."

    scene poorgirldoggystyle38
    with dissolve

    c "Yeah. I was way more into that than I thought I’d be. Even the barking part. It was like...{i}primal.{/i}"
    c "I felt like you were gonna tear me in half."
    s "I don’t think I could if I tried. You’re pretty indestructible in the bedroom."
    c "That’s not true. I almost ran out of steam at the end."
    s "And yet you had two more orgasms afterward."

    scene poorgirldoggystyle39
    with dissolve

    c "I’ll be damned if I let my man out of the bedroom before he finishes. That’s like, a cardinal sin or something."
    c "Sure, it wasn’t a full three gallons of cum. But-"

    scene black
    with dissolve
    stop music fadeout 7.0

    s "Okay. I’m putting my clothes back on now."
    c "Heheh...fine. I’m gonna lay here for a while and...uhh...dry out. But if you see Tsubasa, can you ask her to bring me a towel or something?"
    s "Just a towel and not a change of clothes?"
    c "Oh, no way. I’m totally wearing this outfit to the bar tonight. I’ve just gotta clean it up first."
    s "I think you’re gravely misinterpreting how...wet it is."
    c "And I think you’re gravely misinterpreting how much of a turn on it will be knowing I’m standing in front of all of my friends wearing the outfit you just came all over~"
    s "Again...you have a problem."

    $ renpy.end_replay()
    $ chikalust25 = True
    $ chika_love += 1
    $ chika_lust += 2

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}Chika’s lust has increased to [chika_lust]!{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo14
...
```