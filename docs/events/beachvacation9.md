# Summer and Winter (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Legacy of Thaum Pt. I](./beachvacation8.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation9
* Group: Main
* Triggered by label: beachvacation8
* Chain sources: beachvacation8
* Chain sources path: beachvacation8

## Official wiki page

[Summer and Winter](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation9&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation9:
    "I tried to sleep that night but couldn’t."
    "Something about the crashing of the waves as they attacked the coast tore me from my rest. "
    "The bed became a ship."
    "And I became lost at sea."
    "So I did what all good captains do-"
    "Abandoned ship and got the Hell out of there."

    scene nightsky
    with dissolve
    play music "thesleepingcity.mp3"

    "That whole thing about “going down with the ship” never made any sense to me."
    "I mean, who wants to die for a boat?"
    "If you’re going to die, do it for something wonderful. "
    "Like a girl you love or an idea you believe in."
    "Dying for a boat is just a waste of a life."
    "But I guess there’s no harm in thinning out the crowd if some people are naive enough to believe that there is honor in a death at sea."
    "Honor has no value in the real world."
    "Nothing has value in the real world."
    "But that’s because there is no real world."
    "There’s only this place, whatever this may be."
    "Wherever this may be."
    "Which is likely somewhere at the edge of the world."

    scene sanaatnight1
    with dissolve2

    "I come across a small girl as I make my way down the beach, still fighting away the idea that I should be in bed right now."
    "It’s roughly 3 AM. The girls have probably been long-done with their game at this point."
    "I figured Sana would be in bed, but..."
    "Well, you can clearly see that isn’t the case."
    "The ocean is gentle tonight."
    "Every so often, I watch the tide tickle her feet before running away again."
    "I wonder if the water is cold?"
    "…"
    "It probably is."
    "There has to be {i}something{/i} cold in this burning world."

    scene sanaatnight2
    with dissolve

    sa "Huh?..."

    "Oh."
    "She’s spotted me."

    if bonus == True:
        "I guess my game of “Spy on the loli” is coming to an end."

    "That’s fine, though."
    "It’s been a little while since Sana and I were alone together."
    "This is a good chance to figure out what it is that brought her out here this late."
    "I hope, if only for a moment, that it’s not to go down with the ship."

    sa "What...are you doing here?"
    sa "I thought you went to sleep."
    s "I did."
    s "Well, I tried to at least. The water kept me up."

    scene sanaatnight3
    with dissolve

    sa "Me too. "

    if ayanesleepover == True:
        sa "It feels a little weird sleeping in an unfamiliar bed, doesn’t it?"

        if bonus == True:
            s "...Yeah."

            "I hope she’s not talking about the night I slept in Ayane’s bed..."
            "I still don’t really know the best way to talk about that."
        else:
            s "If I don't have my trusty pillow and blanky, it's virtually impossible for me to fall asleep."

    else:
        sa "I kind of...need things to be really quiet in order to fall asleep..."
        sa "I always have."

    s "Mind if I stay here and talk to you for a bit? Not like there’s anything else to do right now."
    sa "Yeah...that’s fine. "

    scene sanaatnight4
    with dissolve

    sa "And sorry for not...asking for permission to go out at night like this."
    sa "Even if you’re going to say something like “Do whatever you want” or “I don’t really care.”"
    s "Wow, that’s exactly what I was going to say."
    sa "I figured..."

    scene sanaatnight3
    with dissolve

    sa "My mom is the same way."
    sa "She lets me do pretty much anything I want."
    s "Yeah, that sounds about right. Sara seems like a pretty lenient mother."

    scene sanaatnight5
    with dissolve

    sa "She is."
    sa "There was...this one time I got lost in a grocery store when I was little..."
    sa "And I was crying and looking around for her and..."
    sa "Well, I didn’t find her until almost thirty minutes later because she went home without me."
    s "That’s not lenient, that’s just negligent."

    scene sanaatnight6
    with dissolve

    sa "Yeah...it sounds a lot worse now that I say it out loud..."

    scene sanaatnight5
    with dissolve

    sa "She was really upset about it, though."
    sa "I remember her crying and...saying how sorry she was for pretty much the rest of the day after that..."

    scene sanaatnight3
    with dissolve

    sa "But...I was really little back then, so...it doesn’t really matter anymore."
    sa "At the very least...I don’t think I’ll be getting lost in a grocery store again any time soon."
    s "It would be concerning if you still got lost in grocery stores at your age."

    scene sanaatnight6
    with dissolve

    sa "I’m glad you think so, but there are plenty of people who still think I’m a lot younger than I actually am."
    s "I mean, can you really blame them, though? You’re what, like 4’11?"
    sa "Even shorter...I’m 4’10."
    s "{s}Jesus Christ.{/s}"
    sa "Don’t remind me..."
    s "Where do you even buy your clothes?"
    sa "I just asked you to not remind me and now you’re...asking me where I buy my clothes?"
    s "...Maybe I just want to get you a present?"
    sa "I’m kind of worried about what a present from you would be like..."
    s "Rude. I’m a perfectly wholesome adult male, I’ll have you know."

    scene sanaatnight3
    with dissolve

    if bonus == True:
        sa "You say that now...but I’m pretty sure I’m catching onto what you’re really like, Sensei..."

        "I really hope that isn’t true."

        sa "Besides...I hear a lot about you from Ayane."

        "I really hope that isn't true either."

        sa "It’s like you’re a different person when you’re with her than you are with me..."
        sa "Is it...okay if I ask you why?"
    else:
        sa "And I...am a health inspector."
        sa "You know the truth about me, Sensei...so it's only fair that you...stop changing who you are when you're with me..."
        sa "The same way I've stopped hiding the real me when you're around..."

    "She’s absolutely correct."
    "I {i}am{/i} a different person when I’m with her."
    "Just like I’m a different person with everyone else."
    "There isn’t a single person in this world who acts the same with everyone they meet."
    "You adapt."
    "You change yourself to fit better into whatever situation you throw yourself into."
    "Such is the way of the chameleon, and such is the way of me."

    s "There are a few reasons for that."
    s "You and Ayane are completely different people. I’ve also known her a lot longer."
    s "So Ayane and I are obviously going to act a little closer. Just like how I am with Ami."
    s "Ayane’s basically a member of the family at this point."
    sa "I see..."
    sa "I think...she’d be really happy to hear that."

    scene sanaatnight7
    with dissolve

    sa "She’s...almost like...family for me as well."
    sa "I met her during a...really bad part of my life..."

    scene sanaatnight3
    with dissolve

    sa "I wasn’t always this quiet, you know."
    sa "I was actually really talkative when I was little."
    sa "I used to get my mom into a lot of trouble."

    scene sanaatnight6
    with dissolve

    sa "Which is probably another reason the grocery store fiasco was so scary...I thought she was just giving me away for being too rowdy..."
    sa "Actually, I’m going to stop bringing that up now because I feel even dumber every time I add on to it."
    s "I’ll be sure to ask Sara about it the next time I see her, just in case you’re leaving anything out."

    scene sanaatnight8
    with dissolve

    sa "P-Please don’t! She hasn’t brought it up in years and I’m...hoping she forgot about it!"
    s "Do you really think a mother would forget about something like almost losing her daughter?"
    sa "N-No! But I can still hope!"
    s "Okay, okay. I won’t bring it up. But if she ever does, I’m not stopping her."

    if saradate1 == True:
        scene sanaatnight4
        with dissolve

        sa "Oh yeah...You and her are...friends, now...right?"
        s "Is that weird for you?"
        sa "Um...A little bit. I won’t lie."
        sa "She...hasn’t had any male friends for a long time...so seeing her get close to you is kind of...concerning."
        s "What, are you worried we’re going to start dating or something?"

        scene sanaatnight9
        with dissolve

        sa "Yeah."

        "I meant that in a joking sort of way but it seems like Sana took it seriously."
        "I’m surprised she answered so honestly, though."
        "Is she already comfortable enough to share her actual feelings with me?"

        sa "It would be...really weird if you two started dating."

        if bonus == True:
            s "Why do you say that?"

            scene sanaatnight10
            with dissolve

            sa "Well cause...you know...you’d be doing stuff that couples do..."
            sa "And not only would it be with my mom, I’d have to figure out what to say to Ayane as well..."
            sa "She really likes you and I think...she’d be really scared if you ever dated someone your age."
            s "So...she’d be okay with me dating someone her age?"

            scene sanaatnight6
            with dissolve

            sa "Weirdly enough, I think she’d be more okay with that..."
            sa "Because to her, it would mean she still has a chance."
            sa "I think what she’s most afraid of is you just...forgetting about her."
            sa "But I know you wouldn’t do that..."
            sa "You’re kinder than that, whether you believe it or not."

            "No I’m not, Sana."
            "You don’t know half of it."
            "It doesn’t matter how nice you are to someone if your end goal is to sleep with them."
            "But of course-"
            "I won’t fault you for not realizing that yet."
            "I’ll be here for you until my veins run dry."
        else:
            s "Well, I have no intention of ever starting that sort of relationship with her, so you don't have to worry."

    else:
        scene sanaatnight6
        with dissolve

        sa "Please...don’t do that either..."
        sa "I think it would be best if everyone just...forgot all about grocery stores...forever."
        s "But then where would we buy our groceries?"
        sa "We wouldn’t. We’d all just die."
        s "Are you really that embarrassed by that story?"
        sa "I swear it didn’t sound even half as stupid in my head...it was actually a really sad memory."

    "A gust of wind sweeps across the beach and, for a brief moment in time, I’m able to see both of Sana’s eyes."
    "They reflect the moonlight back into the sky, but not before giving me chills."
    "Though, that could just be the wind."
    "I didn’t catch much of her face, but I did spot a tiny glimpse of...emptiness?"
    "Longing?"
    "There’s something she wants, but can’t have."
    "I wonder what it is?"

    scene sanaatnight7
    with dissolve

    sa "Can you feel that, Sensei?"
    s "Yeah, it’s called wind."

    scene sanaatnight6
    with dissolve

    sa "That’s not what I meant..."
    sa "I meant the temperature."
    sa "It's finally starting to get colder."

    scene sanaatnight7
    with dissolve

    sa "Summer is leaving us."
    sa "Pretty soon, we'll even have snow."
    sa "I wonder what else this winter will have in store for all of us?"
    s "Do you like the winter, Sana?"
    sa "I do...I was born in winter. It brings back good memories."
    sa "I also don’t like the heat."
    s "Neither do I. Here’s hoping that the two of us can manage to stay sane until-"
    s "Wait, don’t we have to deal with Fall before we get to winter? That didn’t even occur to me."

    scene sanaatnight3
    with dissolve

    sa "There is no Fall in Kumon-mi."
    sa "Just like there is no Spring."
    sa "All we have are summer and winter."
    sa "I’m...surprised you haven’t realized that until now."

    "I know it’s been scorching hot ever since I was reborn here but...I never realized that was due to it being a six month Summer."
    "How does that even work?"

    if ayanesleepover == True:
        s "Do you mind if I say something relatively corny right now?"
        sa "Go ahead...I’m listening."
        s "Have you ever realized that you and Ayane are kind of like summer and winter?"

        scene sanaatnight11
        with dissolve

        sa "Pfft! What the heck?"
        sa "I knew something corny was coming but...that sounds like a line from a movie."

        scene sanaatnight12
        with dissolve

        sa "I...I know what you mean, though."
        sa "Ayane is hyper and outdoorsy and loves adventure and I’m..."
        sa "Well, I’m Sana Sakakibara."
        sa "The quiet girl who doesn’t talk to anyone and spends all of her free time playing video games and eating melon bread."
        sa "So I...can see why you’d think of us like the seasons."

        scene sanaatnight7
        with dissolve

        sa "Since you had your turn, I’ll say something corny now too..."
        sa "Summer and winter...kind of need each other, don’t they?"
        sa "Without one, the other basically wouldn’t exist."
        sa "The only reason we look forward to seasons changing is because we get tired of the one we have now."
        sa "So..."

        scene sanaatnight12
        with dissolve

        sa "So even if you like the Summer right now, you’ll look forward to me eventually, right?"
        s "…"
        sa "…"

        scene sanaatnight13
        with dissolve

        sa "Oh God! That probably sounded really weird, didn’t it?"
        s "Was that a confession, Sana?"
        sa "No! I just meant that I...I don’t know!"
        sa "It just sort of came out! I’m obviously really bad at being corny!"

        scene sanaatnight14
        with dissolve

        "I take a seat next to Sana and move closer to her."
        "She doesn’t try to get away."
        "Months ago, I feel like even coming within a few inches of her would have sent her sprinting down the beach."
        "But now-"
        "All she does is turn her head to the side and let out cute noises of embarrassment."

        sa "Ngh..."
        sa "I...can’t believe I said something that stupid..."
        s "It wasn’t stupid. It was cute."
        sa "No, it was very stupid. Very, very stupid."
        sa "You should forget you ever heard it."
        s "I don’t know if I’ll be able to do that."
        sa "Please do that. Or, at the very least, never repeat it to Ayane."
        sa "She’d think I was trying to...win you over...or something..."
        s "Weren’t you?"
        sa "No. You’re my teacher. That’s weird."

        if bonus == True:
            s "I don’t think it’s that weird."
            sa "Of course you don’t. You...sleep in girls’ beds with them and stuff..."
            s "…"
            sa "…"

            scene sanaatnight15
            with dissolve

            s "Is that a thing we need to talk about?"
            sa "Is...that a thing you {i}want{/i} to talk about?"
            s "It sounds like it’s bothering you a little."
            sa "Of course it’s...bothering me a little."
            sa "I spent the whole night expecting you to...come visit me at the bar and..."
            sa "I come home to find you cuddling with Ayane..."
            sa "It was...really weird..."
            s "Would it have been better if I just let her stay by herself and cry her eyes out?"

            scene sanaatnight14
            with dissolve

            sa "Of course not...You...You did the right thing."
            sa "But that doesn’t make it...not weird for me..."
            sa "It would be the same thing if I...found you in bed with my mom or something..."
            s "If you ever find me in bed with your mom, I want you to know it’s probably her fault and not mine."

            scene sanaatnight16
            with dissolve

            sa "Yeah...it probably would be..."
            sa "But...still..."
            sa "I thought I was okay with it, but for some reason, I just can’t...stop thinking about it..."
            sa "It’s probably because I know how much she likes you and..."
            sa "Well, I don’t really know how {i}you{/i} feel, but I can’t imagine it’s...easy for a boy to turn down a girl like her if she’s...you know..."
            s "Didn’t I tell you nothing happened that night?"

            scene sanaatnight15
            with dissolve

            sa "Mhm...but..."
            sa "You never said anything about other nights."
            sa "And I don’t even want to ask because...I feel like it’s just better if I stay in the dark..."

            "I feel that way too..."
        else:
            s "You're right. It would be weird."
            s "In fact, even mentioning it is making me want to throw up in my mouth."
            sa "..."
            s "Don't ever flirt with me, Sana."

        scene sanaatnight14
        with dissolve

        sa "…"
        s "…"
        sa "I’m sorry...I didn’t mean to start complaining..."
        sa "We’re on vacation...so we should be talking about happier things..."
        sa "Or just...not talking about anything and...watching the stars together..."
        sa "That would be nice...wouldn’t it?"
        s "…"
        sa "…"
        s "Yeah."
        s "We can just watch the stars together."

        scene sanaatnight17
        with dissolve

        "And so we watched the stars, like any two people awake at 3 AM would."
        "We sat there in silence, letting the cicadas off in the distance fill in the silent spaces that conversation would normally take up."
        "And somehow or another, it felt like we were bonding."
        "I’m glad Sana was able to look past the situation with Ayane and get over it so easily."
        "She handled everything maturely and responsibly-"
        "Without even shedding a tear."

        scene nightsky
        with dissolve2

        "Sana and I get up off of the ground almost 30 minutes later and head back to the inn together."
        "I always forget how much taller I am than her until I see her right next to me."

        if bonus == True:
            "But that’s part of what makes me so attracted to her."
            "Call me a creep or whatever, but it makes sense in my eyes."
            "Even if I’m not devoted entirely to her, I’m happy that we can spend so much time together."
        else:
            "I am such a big boy now."

        sa "Um...S-Sensei?"
        s "Yeah?"
        sa "You..."
        sa "You didn’t hear anything while we were watching...the stars...did you?"
        s "All I heard were the cicadas."
        sa "Okay...good."
        s "...?"
        sa "Let’s...um-"
        sa "Never mind..."
        sa "I’ll...do my best to...try and forget..."

        scene black
        with dissolve2

        "O world."
        "In our final moments-"
        "Please remind us how it feels to be wanted without another unwanted in return."
        "And when we sleep-"
        "Gift us happy dreams."
        "Of places where nothing bad can ever happen."
        "And of a love so pure-"
        "It destroys the world."

        $ renpy.end_replay()
        $ beachvacation9 = True
        $ sana_love += 1
        stop music fadeout 5.0

        "{i}Sana’s affection still manages to rise to [sana_love] despite spending the night worrying about what you do to her best friend while she is away!{/i}"
        "{i}Oh, the tricks our hearts manage to play on us!{/i}"
        "........."
        "......"
        "..."

    else:
        s "Well, either way, I’m glad we won’t have to deal with this heat anymore."

        scene sanaatnight3
        with dissolve

        sa "Me too...I’m excited to wear sweaters and hide under blankets and stuff."
        s "Yeah, those sound like two very 'Sana' activities."
        sa "You think you know me so well..."
        s "Nah. You just have a certain air to you. That’s all."
        sa "Well I hope it’s a chilly one...cause if one more hot breeze comes to get me and blows sand into my eyes I’m...taking the first bus out of here."

        scene nightsky
        with dissolve

        "Sana and I get up off the ground a few minutes later and head back to the inn together."
        "I always forget how much taller I am than her until I see her right next to me."
        "But that’s part of what makes me so attracted to her."
        "Call me a creep or whatever, but it makes sense in my eyes."
        "I feel a certain obligation to protect her from anything that would hurt her...Even if those things would make my life easier or better in the long run."

        sa "Um...S-Sensei?"
        s "Yeah?"
        sa "I...Umm..."
        sa "I’m glad you couldn’t sleep tonight."
        s "…"

        scene black
        with dissolve2

        s "Me too."

        $ renpy.end_replay()
        $ beachvacation9 = True
        $ sana_love += 1
        stop music fadeout 5.0

        "{i}Sana’s affection has increased to [sana_love]!{/i}"
        "........."
        "......"
        "..."

label endofbeachvac9:
    $ totaldays += 1
    $ day += 1
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
    else:
        "ERROR"

    "{i}[totaldays] days have passed...{/i}"

    if ami_lust >= 10:
        jump amilust10
    else:
        jump amilust10skip

label amilust10:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```