# Scientific Research
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day79&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 79

❌Day of week is Friday

✅Event "[Chika: A Castle for Everyone](./chikadorm15.md)" is completed (event=chikadorm15)



## Next events
* [Main: What's Done is Done](./beachvacation1.md)
* [Chika: A Dog that Doesn't Do Math](./mall15.md)

## Event properties
* ID: day79
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day79:
    scene street_noon
    with dissolve
    play music "lifeismostlygood.mp3" fadein 3.0

    "Ahh, Friday...the best true weekday of the-"
    "Well...week."
    "With over 48 hours on the clock starting right now to do whatever I want, I begin to wonder exactly what the best use of my time would be."
    "But as I make my way down the street, slightly exhausted from another eventful day as a professional educator, I spot several familiar faces..."

    scene beachday1
    with fade

    c "Oh, hey! What are you doing over here?"
    s "I mean...{i}I'm{/i} on my way back from school...which is what I assumed two out of three of you would also be up to. So why are you already dressed in your casual clothes?"
    s "The last bell only rang like...half an hour ago."

    scene beachday2
    with dissolve

    ch "Chinami doesn’t go to[school] so she can do whatever she wants!"
    s "Good for you, Chinami."

    "I gaze at Chika, slightly confused by both the clothing situation as well as why she’s allowing her sister out in public given her whole immunodeficiency thing."

    c "Don't look at me like that, Sensei. I know what you're thinking."

    scene beachday3
    with dissolve

    c "The reason I'm not still in my uniform is...I actually left a couple hours early so I'd have time to meet up with Yumi and Chinami."
    c "You were asleep when I left so you probably just...didn't notice."
    s "Do you guys have plans to go somewhere?"
    y "That’s right. We have plans. So how about you do us a favor and-"

    scene beachday4
    with dissolve

    ch "Hey! No being mean! Chinami doesn't want to be friends with mean people!"
    y "What? I'm not being mean. I just-"
    ch "Leave big sis Chika’s boyfriend alone or he won’t come say hi to Chinami anymore!"

    scene beachday5
    with dissolve

    c "Chinami...I told you he isn’t my boyfriend. He’s mine and Yumi’s teacher."
    ch "Yumi goes to[school]? Chinami had no idea."
    c "Chinami, for the last time, please start saying “I” instead of “Chinami.”"
    ch "But “I” isn’t Chinami’s name. “Chinami” is."
    y "Of course I go to friggin' school, Chinami...Just...not as much as everyone else."

    scene beachday7
    with dissolve

    c "You’re, uhh...probably having a hard time following this, aren’t you?"
    s "It's less that I'm having a hard time following and more that you three are just an...interesting group."
    s "It seems like even Yumi is trying her best to behave around Chinami. I haven’t heard her curse at me once so far."

    scene beachday8
    with dissolve

    y "You’re lucky there’s a kid around. Even I ain't messed up enough to be a negative influence on someone like her."
    ch "Yumi is Chinami’s second big sister! She visits all the time and brings me candy and other fun things!"
    s "Is that so?..."
    y "What? Why do you look so surprised?!"
    c "To get back on track, the three of us made plans to go to the beach today."
    s "The beach? Isn’t it a little late for that? The sun's going to be setting any minute."
    c "That’s exactly why we need to go {i}now.{/i} If we went any earlier, there would be too many people and it wouldn’t be safe for Chinami."
    c "The beach will be dead in, like...thirty minutes. So this is really the only time we can go."
    y "That’s right. So you should probably start heading back home to your-"

    scene beachday10
    with dissolve

    ch "Come with us!"
    c "Chinami?"
    y "Wait, hold on a second. He can’t come, he’s a-"
    ch "Chinami wants to show him her new bathing suit!"
    c "Chinami...I’m sure Sensei is super busy and-"
    s "I’ll come."

    scene beachday11
    with dissolve

    c "Huh? Wait, really?"
    s "Sure. I didn’t have much planned for the rest of the day anyway."

    if bonus == True:
        "Plus, who would I be to deny the sight of two and a half adorable girls wearing swimsuits? This opportunity doesn't present itself every day."
        "I didn’t even realize Kumon-mi had a beach until a few minutes ago."
        "So not only am I going to be gifted with a rare and wonderful sight, I’m {i}also{/i} going to find out more about the surrounding area."
        "This is basically a scientific research trip. And as the teacher for the majority of these girls, I’d be foolish not to go."
    else:
        s "But only if Yumi is okay with it. I know my presence can be rather irrtating to her at times and I'd be happier if she could enjoy herself at the beach."

    y "Oh hell no! Not a chance! No way am I going to wear a bathing suit in front of this creep!"

    if bonus == False:
        s "=/"

    ch "Chinami will!"
    c "Are you really sure, Sensei? I don't want you feeling like a chaperone or whatever."
    s "It's fine if it's for scientific research, right?"
    y "Scientific research my ass! You just want to perv out on us!"

    scene beachday12
    with dissolve

    c "So what? You look hot as hell in your bathing suit, Yumi. What do you have to lose?"
    y "Are you seriously okay with this guy having his eyes all over you?!"
    c "Yeah, kind of."
    y "What?! The hell is going on with you lately?!"

    scene beachday13
    with dissolve

    c "Sensei...if you're {i}really{/i} sure you have the time, two of us would love to have you."
    y "Yeah. And the third one is currently thinking about whether or not she should swim out into the ocean to never be seen again..."

    scene black
    with dissolve2

    "The bus shows up several minutes later and, like Chika predicted, there’s barely anyone on it."
    "As it turns out, the beach is only about fifteen minutes away."
    "I have no idea how I didn’t know this until now, but that’s definitely interesting. "
    "It seems that Kumon-mi has pretty much everything that anyone could ever want in it..."
    "………"
    "……"
    "…"

    scene beachday14
    with dissolve2

    c "So, Sensei...Are you excited to see Yumi and me in our swimsuits? Is your heart pounding?"

    if bonus == True:
        s "You seem pretty eager to show yourself off, Chika. If I didn't know any better, I might think you're trying to seduce me right now."
        c "Seduce you? Me? Of course not. I just want to spend some quality time with my teacher, my best friend, and my sister. What's seductive about that?"
        s "Nothing when you put it that way, no. But that smug grin and concern for my heart rate is telling another story."
    else:
        s "No."

    scene beachday15
    with dissolve

    y "Uh...the two of us are gonna go get changed, so make sure Stalky McGee over there doesn’t follow us in."
    s "What kind of immature nickname is that?"
    ch "Does this mean big-sis will be Chika McGee once they get married?"
    y "Please hurry up. I don't want to deal with this on my own."
    c "Sounds good, Yumi. I'll be right in."

    scene beachday16
    with dissolve

    c "Sucks you didn’t have time to go home and grab your bathing suit. Was looking forward to seeing my teacher shirtless."
    s "I’m sure there will be plenty more opportunities to see me shirtless. I wouldn’t worry too much."
    c "Heheh...oh yeah?"
    c "Lucky for you, you’ll get your first opportunity to see {i}me{/i} like that in just a few minutes."
    c "Hope I don't...{i}disappoint...{/i}"

    scene beachday18
    with dissolve

    "And just like that, Chika disappears into the women’s restroom."
    "I can hear Chinami’s giggling bouncing off of the tiled walls and finding its way back onto the beach...as if gently reminding me that the act of following them here is much more perverse than it seems."

    scene beachday19
    with fade

    "I move closer to the water and look out toward the horizon."
    "Sure, it's getting a little late in the day, but it’s still surprising seeing a beach empty- especially since there are still mats and chairs laid out."
    "I'm not sure what kind of person just...leaves all of their stuff lying around a place like this, but I guess it doesn't make any sort of difference to me."

    if bonus == True:
        "I’m just here to hang out with cute girls and get some ‘research’ done."
    else:
        "Now, where are all of the seashells?"

    scene black
    with dissolve2

    "I close my eyes and listen to the sounds of the girls' voices blend in with the wind and the water, hoping that they don't wind up taking too long in there..."
    "………"
    "……"
    "…"

    scene beachday20
    with dissolve

    c "Hey~"
    c "Did you miss me?"
    s "…"
    c "…"

    "Jesus Christ."

    s "Wow."
    c "You like?"

    scene beachday21
    with dissolve

    c "We just started selling these at the mall and I kinda {i}needed{/i} to buy one since my old swimsuit is way too small for me now. I look hot, right?"
    s "I’m kind of at a loss for words, to be honest. Well, at least words that wouldn't land me on some sort of list."
    c "I won't tell if you don't~"
    c "I'm gonna go lay out and try to tan for a bit before {i}all{/i} of the sun is gone, but feel free to come by and spend some more time with me if you like."

    scene beachday19
    with dissolve

    "Chika suddenly walks off and begins to lay out a towel and, in case you were wondering, she looks equally as attractive from behind."
    "Another minute or so passes by before I hear the second set of footsteps closing in on me from behind."
    "They’re a bit more aggressive than the first ones- almost like someone is angrily kicking their way through the sand."
    "That in mind, I’m assuming these footsteps belong to..."

    scene beachday23
    with dissolve

    y "…"
    s "…"
    y "Where did Chika go?"
    s "Chika? Who's that again?"

    scene beachday24
    with dissolve

    y "Don’t play dumb with me, asshole. You know exactly who Chika is."
    s "Sorry. I was just so distracted by your beauty that I momentarily forgot anyone else in the world existed."

    scene beachday25
    with dissolve

    y "You...fucking pervert!"
    y "I specifically kept my shirt on so I wouldn’t have to listen to shit like that!"
    y "Just tell me where the fuck Chika went! I need to know where she wants me to put her stupid fucking bag!"
    s "Chika? Who’s that?"

    scene beachday26
    with dissolve

    y "FUCK IT! I’LL FIND HER MYSELF!"

    scene beachday19
    with dissolve

    "And just like that, Yumi vanishes as well...which only leaves {i}one{/i} more girl..."
    "I begin to trace lines in the sand with my shoe as I wait for Chinami to come out of the restroom."
    "I’m honestly a little surprised the other two let her stay in there by herself."
    "I mean, it’s not like she’s [young]enough to need {i}constant{/i} supervision, but it still seems to me like Chika and Yumi are used to coddling her."
    "Oh well. I’ll just be the nice guy and wait for her to-"

    ch "Chinami is here now!"
    s "What? Where?"
    ch "Behind you!"

    scene beachday28
    with fade

    ch "If Chinami was an assassin, you would be in big, big trouble right now!"
    s "I don't know. I think I could take you."
    ch "That's just what Chinami wants you to think."
    ch "Now call her cute and tell her that her swimsuit is the best one here!"
    s "Chinami is cute."

    "But after seeing the last two swimsuits, I can not, in good faith, declare Chinami the winner of this battle."

    scene beachday29
    with dissolve

    ch "Yay!~"
    ch "Chinami picked this one out for herself! Isn’t her taste super cool?"
    s "You are definitely your sister's...sister."
    ch "That is how sisters work, so yes!"

    scene beachday29r
    with dissolve

    ch "Big sis Chika says Chinami isn't big enough to wear a bikini yet, but I promise to show you once I am, okay?"
    s "Sure, but...please don't rush. I think you're fine the way you are."

    scene noonsky
    with fade

    "Just like the other two, Chinami wanders off and starts doing her own thing."
    "I can’t imagine being able to fairly split my time between all three of the girls since the sun is already beginning to set..."
    "So I think I’m going to have to choose one and just focus on them, unfortunately..."
    "I wonder who that should be though?..."

    menu:
        "Spend time with Chika":
            if bonus == True:
                scene beachday30
                with dissolve

                "I slowly walk up to Chika from behind, trying my best to keep my presence unrecognized."
                "Part of me wants to just stare at her until she realizes I’m here but-"
                "Actually, that’s exactly what I’m going to do."
                "She looks too good from this angle to not take advantage of the opportunity."

                s "…"
                c "…"
                s "…"
                c "…"
                s "…"
                c "Enjoying the view?"
                s "I'm not sure if I'm meant to assume that you're talking about the ocean or...something else."
                c "We both know you're not paying any attention to the ocean..."

                scene beachday31
                with fade

                "I step to the front of Chika and take a seat on her towel as well."

                s "It appears I have been caught red handed."
                c "Am I not cute enough from the front for you?"
                s "Of course you are. I just don't get many opportunities to look at you from that other angle."

                scene beachday32
                with dissolve

                c "Well forgive me for not creating more opportunities for you to stare at my ass."
                s "It's fine. Just do your best to create more in the future and everything will turn out okay."

                scene beachday33
                with dissolve

                c "Aww, how sweet of you."
                s "I feel like you're supposed to be sarcastic right now, but that smile seems genuine so I can’t really tell if you are or not."
                c "I guess I'm being a {i}little{/i} sarcastic...but I also understand that boys will be boys and that if there is an ass, you're probably going to stare at it."
                s "Right. And you know {i}all{/i} about boys, don’t you?"

                scene beachday31
                with dissolve

                c "Okay, well now you're just being rude."
                c "I might not be the most experienced when it comes to dating, but it’s not like I don’t {i}understand{/i} boys or whatever."
                c "You’d be surprised at how many articles I’ve read on how to appeal to them and...you know. That sort of thing."
                s "Oh yeah? Trying to capture someone’s heart?"

                scene beachday34
                with dissolve

                c "{i}Maybe~{/i}"
                c "But how about you, Sensei? I know we’ve talked about it before...but has anyone been catching your eye lately?"
                s "Well...I chose you today, didn’t I?"

                scene beachday31
                with dissolve

                c "You did...but my competition was my little sister and a girl who constantly tells you she wants to rip your penis off."
                c "I don’t know if this is a victory I can take pride in."
                s "You should. In all honesty, I probably would have picked you before anyone else anyway."

                scene beachday35
                with dissolve

                c "Oh come on...you don't mean that."
                s "After seeing you from that...previous angle, I think it would be kind of hard to choose anyone else."
                s "At least not until I calm down."
                c "…"
                s "…"

                scene beachday36
                with dissolve

                c "Mm..."

                "Uh-oh."

                c "I was hoping for a more romantic answer, you know."
                c "You’re lucky I let you stare that long in the first place, Sensei. And even {i}more{/i} lucky that I haven't tossed our little lingerie modeling plan out of the window to punish you."
                s "Anything but that. It’s all I have left to look forward to in life."

                scene beachday32
                with dissolve

                c "Aww, really? You poor thing."
                c "I guess you’re just going to have to be a good boy and remain patient, then. And keep hanging out with me, of course."
                c "Also if you wanted to buy me flowers or...do other romantic things, that would be cool too."
                c "And who knows? If you're lucky, maybe I’ll even give you a little something in return?"
                s "Does that mean what I think it means?"
                c "I wonder..."
            else:
                scene sky
                with dissolve

                "I start to make my way over to Chika, but get distracted by how pretty the sky is."

                s "Wow. The clouds sure are beautiful today."
                c "Would you say they're as beautiful as m-"
                s "Chika, be quiet. I am looking at the clouds."
                s "You will scare them away."
                c "But...but it's my part of the event! You're supposed to-"
                s "The clouds, Chika! Think of the clouds!"

            scene black
            with dissolve2

            if bonus == True:
                "Chika and I bask in the sun for another thirty minutes or so before Yumi starts complaining about wanting to go home."
            else:
                "I stare at the clouds for another thirty minutes or so before Yumi starts complaining about wanting to go home."

            "It seems like a bit of a waste to only come to the beach for around an hour, but I guess with the current Chinami situation, that’s really all we can do."
            "Besides, it’s not like it was a far drive."
            "And I got to spend some time with Chika because of it, so I’m not complaining at all."
            "In fact, all things considered, today was a pretty good day..."

            $ renpy.end_replay()
            $ day79 = True
            $ chika_love += 1
            stop music fadeout 4.0

            "{i}Chika’s affection has increased to [chika_love]!{/i}"
            "………"
            "……"
            "…"

            jump endofweekday

        "Spend time with Yumi":
            scene beachday37
            with dissolve

            "I manage to find Yumi slouched up against the wall of a nearby restroom after wandering around looking for her for several minutes."
            "The only thing is, she’s fallen asleep...which means that she may very well misunderstand the situation if she wakes up right now."

            y "…"
            s "…"

            scene beachday38
            with dissolve

            y "Mm..."

            "Oh no. How could this have happened?"

            scene beachday39
            with dissolve

            y "...Mm?"
            s "Hey. Did you have a nice nap?"

            scene beachday40
            with hpunch

            y "W-W-W-W-What the fuck do you want?! And why are you just standing there like a creep?!"
            y "You didn’t try to touch me while I was sleeping did you?! Because I swear to God I’ll fucking murder you!"
            s "Calm down...I didn’t touch you. I just wanted to see what you were up to."
            y "Bullshit! Like you’d try and talk to {i}me{/i} while Chika’s right over there!"
            s "Nope...came straight for you. I’m actually surprised at how quickly you fell asleep."

            scene beachday41
            with dissolve

            y "Yeah, well...I don’t fuckin' like the heat."
            s "Then why don’t you take your shirt off?"

            scene beachday40
            with dissolve

            y "I don't know! Why don't {i}you{/i} fucking kill yourself?!"
            s "Oh, come on. Am I really bad enough for you to wish death upon?"
            y "Fuck yes you are!"

            "I move to sit down next to Yumi and-"

            scene beachday42
            with dissolve

            y "Why do you suddenly think you're allowed to sit next to me?!"

            "And that happens."

            s "It’s a public beach, I can sit wherever I want."
            y "Bullshit! This is the only spot with any shade! I need to be here or I’ll fucking die!"
            s "Then I guess you’ll just have to put up with me."

            scene beachday43
            with dissolve

            if bonus == True:
                y "You some kinda masochist or something? Do you get off on girls being mean to you?"
            else:
                y "The fuck, dude? Do you actually, like, {i}enjoy{/i} girls being mean to you or something?"

            s "Maybe a little bit. Aren’t you the same, though?"

            scene beachday44
            with dissolve

            y "Huh? What? The fuck you talking about?"
            s "I don’t know if you’ve realized this, but you tend to blush a lot whenever the two of us are arguing."

            scene beachday45
            with dissolve

            y "I...I do not!"
            s "You’re doing it right now."
            y "The only reason I’m turning red is because being around you makes my blood boil!"
            y "It makes me want to...I don't know! Fucking kill somebody!"
            s "Really?"
            y "Yes, really!"
            y "Now, get the hell away from me before I actually do something about it!"
            s "Hmm..."

            "Ignoring her demand, I lean up against the wall Yumi is slouched against, bringing the two of us mere inches apart."
            "At least at first. Yumi instinctively slides away the second my back touches the wall."

            s "You look cute when you’re about to kill someone, have I ever told you that?"
            y "What?! No! Who the fuck says something like that?!"
            s "Do you not like being called cute or something?"
            y "Not by {i}you{/i} of all fucking people!"
            s "So it would be fine if someone else called you cute?"

            if bonus == True:
                y "No! None of it would be fine! It’s just worse hearing it from someone constantly imagining me with my clothes off!"
                s "I mean...I don't do it {i}constantly...{/i}"
            else:
                y "No!"
                s "You're right. Everyone is unnattractive and undesirable."
                s "Anyway, want to hug?"

            scene beachday46
            with dissolve

            y "THIS IS EXACTLY WHY I DIDN’T WANT YOU FUCKING COMING HERE TODAY!"
            y "I’M JUST GOING TO GO FUCKING DIE IN THE SUN! ANYTHING IS BETTER THAN THIS SHIT!"
            s "Wait...stay a little longer."

            "I call out to Yumi as she’s pushing herself off the ground."
            "She stops moving, but I’m sure it’s more of a reflex than her actually wanting to stay."

            scene beachday47
            with dissolve

            y "What?...And this better be good."
            s "Can I tell you one thing without you getting mad at me and calling me a pervert or an asshole or something?"
            y "Probably not, but just fucking say it so I can leave."
            s "Okay, well-"
            s "I really {i}do{/i} think you're cute, Yumi. I'm not just lying to get your shirt off."

            scene beachday46
            with dissolve

            y "FUCK YOU! I’M LEAVING FOR REAL THIS TIME!"

            scene black
            with dissolve2

            "Yumi springs off of the ground and angrily marches over to where Chika is sunbathing. "
            "She complains about wanting to go home and, after a bit of prodding, manages to convince her."
            "It gets dark several minutes later, so Yumi’s desire to leave wasn’t completely unfounded."
            "But, despite her storming off on me and spending yet another 50%% of her dialogue on insults, I feel like the two of us managed to become slightly closer."

            $ renpy.end_replay()
            $ day79 = True
            $ yumi_love += 1
            stop music fadeout 4.0

            "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
            "........."
            "......"
            "..."

            jump endofweekday

        "Spend time with Chinami":
            scene beachday49
            with dissolve2

            "Not knowing how to choose between Yumi and Chika, I decide to play it neutral by spending time with Chinami."

            if bonus == True:
                "Is this the appropriate thing for a man my age to be doing? Absolutely not. But it’s not like I have any ill intentions in doing so."
                "At least...not yet."
                "I like to tell myself that I haven't fallen far enough to consider something like that, but..."
                "Sometimes, you don't realize how deep you've fallen until you start trying to climb your way back up."
            else:
                "At least I know she won't bully me or say anything bad about clowns."

            s "Hey, Chinami. What are you up to?"
            ch "Playing in the sand!"
            ch "Chinami doesn’t know how to swim, so she likes to just watch the water and look for seashells."
            s "That’s...nice. Have you found any yet?"
            ch "Nope! I found three hermit crabs, though. Wanna know what I named them?"
            s "Sure."
            ch "Hermit Crab 1, Hermit Crab 2, and Hermit Crab 3."
            s "Were those really the most interesting names you could come up with?"

            scene beachday50
            with dissolve

            ch "Are they not good?..."
            s "Well, uhh...Actually, they’re fine. They’re...very creative."

            "I guess I probably shouldn't be pointing out the flaws in a child's minimalist approach to naming sea creatures."

            scene beachday51
            with dissolve

            ch "Umm..."
            ch "Can Chinami ask you a question?"
            s "Hm? Sure. What’s up?"
            ch "Why are you spending time with Chinami instead of her big sisters?"
            s "I don't know. I just...am."
            ch "Does this mean you like little girls?"
            s "..."

            "I'm not sure what expression crosses my face when Chinami says that, but I'm almost certain it's not a good one."
            "I’m sure she doesn’t mean anything by it, but the wrong answer here could...have some pretty hefty repercussions if she tells anyone else about it."
            "As such, I quickly glance over to make sure Chika or Yumi aren’t listening in and getting the wrong idea."

            s "Chinami...you shouldn’t say things like that."

            scene beachday52
            with dissolve

            ch "How come? Is liking little girls bad?"
            s "In this context, probably."
            s "In fact, there are very few contexts in which that would not be bad."
            ch "What is a {i}context?{/i}"
            s "Context is like...a particular situation. But yeah, don't ask people that anymore."

            scene beachday53
            with dissolve

            ch "Hmm...Chinami doesn't really get it. But you’re an adult, so Chinami has to listen to you."
            s "Exactly. Good girl, Chinami. Always listen to adults unless they tell you to do something weird."
            ch "Big sis told me about people who try to lure girls like me into big, white vans and sell them on the black market. Is that what you're talking about right now?"
            s "Did...Chika really tell you something like that?"

            "Chinami shakes her head and continues digging her fingers into the sand."

            scene beachday52
            with dissolve

            ch "Big-sis Yumi did. She’s worried that somebody might take me someday, so she’s training me in self-defense and teaching me about all sorts of bad people."
            s "Has...she said anything about me?"
            ch "Mhm. That’s when she first told me the van thing."
            s "..."
            ch "She said you might try to steal me away and be really mean to me, but you seem nice!"

            scene beachday49
            with dissolve

            ch "So Chinami has decided it’s okay to get in your van!"
            s "Uh..."
            ch "What's wrong? Did Chinami make a bad decision?"
            s "Okay, well...let me preface this by saying to please never get in {i}anyone's{/i} van."
            ch "Not even yours?"
            s "{i}Definitely{/i} not mine."
            s "I don’t even own a van, Chinami. Nor do I think it would be safe for me to buy one given what you just told me."

            scene beachday53
            with dissolve

            ch "Chinami is confused again. If you don’t want a van, you don’t have to get one."
            ch "That's what the bus is for. And the bus is fun!"

            scene beachday49
            with dissolve

            ch "The seats are really big and squishy and Chinami doesn’t need to wear a seatbelt."
            s "Chinami always needs to wear a seatbelt."
            ch "She does?"
            s "Absolutely. And make sure you tell Chika and Yumi about that so they know I’m not trying to corrupt you."
            ch "Okay! Chinami wants you and big sis to get married, so she’ll do whatever you tell her to do!"
            s "Please stop saying things that can be so easily misunderstood..."

            scene black
            with dissolve2

            "Chinami and I talk for a little while longer before Chika stops sunbathing and comes to hang out with us."
            "Apparently, she felt bad that I had become a self-appointed babysitter all of a sudden..."
            "And so the three of us built sandcastles until Yumi decided that she had had enough of the beach and wanted to go home for the day."

            if bonus == True:
                "All in all, I had a surprisingly good time...even if a good portion of it was spent talking to a girl probably a third of my age..."
            else:
                "All in all, I had a surprisingly good time...even if a good portion of it was spent talking to a wizard."

            $ renpy.end_replay()
            $ day79 = True
            stop music fadeout 4.0

            "………"
            "……"
            "…"

            jump endofweekday

        "qzɟlǝz dɹʞlʎ" if ayane_love > 2000:
            stop music
            play sound "static.mp3"
            scene beachday31 with flash
            scene newroom15 with flash
            scene connect with flash
            scene beachday45 with flash
            scene newroom15 with flash
            scene connect with flash
            scene beachday49 with flash
            scene newroom15 with flash
            scene connect with flash
            scene xbeachdayx1 with flash
            stop sound
            play music "isingforyou.mp3"
            $ renpy.pause(10, hard=True)

            q "Uhhhhhhh.................."

            "Girl appear before me. Don't know her."
            "Gotta ask question."

            s "?????????????"
            q "..."
            q "So..."
            q "Umm..."

            scene xbeachdayx2
            with dissolve

            q "Shit. What am I supposed to do about this?"
            s "????????????????????"

            "Question gets more question mark because more confuse."

            scene xbeachdayx3
            with dissolve

            q "You, uhhh...feeling okay there, buddy?"
            q "Wanna take a seat? Maybe help yourself to a nice hot bowl of ramen?"
            q "Getting some more carbs in your system might help give you the energy you need to get back to the real event or...or something."
            s "RRRRRRRRRRRRRRRRRRRAMENNNNNNNNNNNNNNNNNNNNN"
            q "Yeah, yeah! Ramen!"
            q "I've gotta say, you showing up here unannounced like this is, uhh..."
            q "Well, let's just say I'm not sure if I'm supposed to be {i}impressed{/i} or {i}worried{/i} or {i}terrified{/i} or...I don't know."
            q "Throw some other adjectives out there for me."
            s "Horny!"

            "Say favorite adjective because good word and want sex girl."

            scene xbeachdayx4
            with dissolve

            q "Yeah, uhh...no thanks. Definitely not what I was looking for."

            scene xbeachdayx5
            with dissolve

            q "But, uhh....oh! I know!"
            q "This just means that we can get to know each other a little better!"

            scene xbeachdayx2
            with dissolve

            q "Or...wait. No it doesn't since you're probably not going to remember any of this anyway."
            q "And on top of that, {i}I'm{/i} not even supposed to be here either..."
            q "See, this is exactly why I've been pushing for a dedicated cafeteria for so long. This same thing happened to Shiori like, not even a month ago."
            s "GIVE RAYMOND NOODLES"

            scene xbeachdayx5
            with dissolve

            q "Ramen! {i}Ramen{/i} noodles. Got it? Say it with me. Ra-"
            s "RAYMOND NOODLE"

            scene xbeachdayx6
            with dissolve

            q "God I hate Fridays."

            "I start pound table anger because girl noodle want sex give"
            "Where other girl"
            "Was beach a minute ago and now not beach but still beach"
            "Ughhhhh"

            scene xbeachdayx7
            with dissolve

            q "Okay...uhh...shit."
            q "Yeah, so...I'm only supposed to do this when I {i}really{/i} have to and I've got no idea if this constitutes one of those times or not...so...let's just hope it works, I guess?"
            q "Can you...uhh...close your eyes for me? Just for a second."

            scene black
            with dissolve2

            q "Good b- wait. Nope. Didn't mean to say that."
            q "Anyway! Uhh...spin around!"
            q "Jump up and down!"
            q "Shout the name of your favorite pizza topping!"
            s "Pepperon-"

            stop music
            play sound "static.mp3"
            scene beachday31 with flash
            scene newroom15 with flash
            scene connect with flash
            scene beachday45 with flash
            scene newroom15 with flash
            scene connect with flash
            scene beachday49 with flash
            scene newroom15 with flash
            scene connect with flash
            scene bedroom_night with flash
            stop sound

            "I had a good day at the beach with Chika, Yumi, and Chinami."
            "Now, it is time for bed."

            scene black
            with dissolve2

            $ renpy.end_replay()
            $ day79 = True

            "........."
            "......"
            "..."

            jump advancetosat

label day80:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
...
```