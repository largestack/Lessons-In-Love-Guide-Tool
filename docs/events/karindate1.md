# Further and Further (Karin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Karin love greater than or equal to 0

* karinnumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: karindate1
* Group: Karin
* Triggered by label: callkarinafternoon
* Triggered by branch label: callkarinafternoon
* Triggered by path: callkarinafternoon->karindate1

## Official wiki page

[Further and Further](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karindate1&go=Go) for more details.

## Event code

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label karindate1:
    "Maybe I’ll see what Karin is up to?"
    "I know that she spends virtually all of her time doing stuff for her
    different teams or clubs or whatever, but now that I’m her “coach,” maybe I can find my way in?"

    if bonus == True:
        "To her life, I mean. Not her."
        "Well, yes her. But not right now."
        "Unless she wants it."
        "Whatever. You know what I mean. "

    play sound "phonebeep.wav"

    "I select Karin’s name in my phone and wait for her to pick up."
    "Given how embarrassed she was to even give me her number, I imagine she’ll let it ring a few times before-"

    play sound "phonebeep.wav"

    ka "Hello?"
    s "Oh, hey."
    s "I wasn’t expecting you to pick up right away."
    ka "Oh! Uhh...hahah, yeah. I just kind of had my phone out and, you know...answered it. Yeah."
    s "...Right."
    s "Well, anyway, what are you up to right now?"
    ka "Me? I was about to go to the park. Why?"

    "Knowing that Karin would probably drop her phone if I asked her to “hang out” right now, I
    decide to get creative and start making use of my newly appointed position."

    s "Do you mind if I tag along?"
    ka "Huh? Why?"
    s "You’re going there to jog or run or something like that, right? That sounds like a thing you would do."
    ka "Uh-huh..."
    s "Well, I’d like to sort of see you in action if I’m going to be in charge of you from now on."
    ka "In action?! Like, alone?? Can’t you just come watch us play at the field or-"
    s "One on one sessions are good for establishing relationships with your team. "
    s "And seeing as I already know Miku pretty well, you’re second in line."

    if kirindate1 == True:
        ka "Second? But, didn’t you and Kirin hang out the other day?"

        "...Did Kirin really tell her about that?"
        "Why?"

        s "We did. But that wasn’t related to the team. This is."
        ka "Well...um...it does feel a little weird...but I guess I can see where you’re coming from."
        ka "Do you want to just meet me there? Do you need me to bring anything for you? Water, maybe?"
        s "I’ll be fine. Are you going to the park near the[school] or a different one?"
        ka "The[school] one. I’ll leave now if you’re going to head over there."
        s "Sounds good. I’ll see you soon."
        ka "Uh-huh! See you soon!"

        play sound "phonebeep.wav"

    else:
        ka "Really? I mean, I guess that’s reasonable since I’m co-captain but..."
        ka "I don’t know. Is it weird if I’m kind of...maybe a little happy to hear that? Hahaha..."
        s "It’s not weird at all. I’m excited to get to learn more about you."
        ka "Ah-! Yeah! I’m excited to learn more about me too! Ah, wait! I meant you! I already, um, know about...me...And-"
        ka "Actually, is it okay if I just hang up now and meet you at the park?"
        ka "I’m going to the one by the[school] and I’ll start heading over now if you’re ready."
        s "Sure thing. I’ll see you soon, then."
        ka "Uh-huh! See you soon!"

        play sound "phonebeep.wav"

    "I hang up the phone and slide it back into my pocket, wondering if Karin is
    going to make {i}me{/i} jog as well today."
    "…"
    "I really hope not."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene karinjogs1
    with dissolve2
    play music "retrospect.mp3" fadein 10.0

    "I arrive at the park near[school] and find Karin standing near the fountain waiting for me."
    "The sun peers through the trees as it begins to set and finds its way onto her well-toned, yet still
    seemingly delicate body."

    ka "G-Good evening! "
    ka "Thanks for coming out to watch over me today..."

    scene karinjogs2
    with dissolve

    ka "Oh, wait! I meant watch me! Not watch over me! I can take care of myself!"
    s "I know what you meant, don’t worry."
    s "In a sense, I might even need you to watch over me today."

    scene karinjogs3
    with dissolve

    ka "Huh? What do you mean by that?"
    s "I’m not sure what Miku told you about me, but I don’t know much about sports."
    s "I actually think it’s a little strange that she wanted someone like me to be your coach despite that."
    s "It seems like the two of you take this pretty seriously, so I’ll try not to get in the way too much."

    scene karinjogs4
    with dissolve

    ka "You don’t have to worry about that...Miku and I are already grateful
    that you’re going out of your way for us."

    "Well, it’s not like I {i}chose{/i} to go out of my way. I was dragged into this by force."

    ka "It’s okay if you don’t know much about sports. I...wouldn’t really mind teaching you."

    scene karinjogs5
    with dissolve

    ka "We just...kind of need a teacher to be present in order to keep playing."
    ka "That’s...one of the several reasons I was surprised to hear you actually trying to get involved today..."
    s "Speaking of involvement, would you mind telling me a little about what you do here?"

    scene karinjogs3
    with dissolve

    ka "Nothing special, really. I just come here a couple times a week to run laps around the park. "
    ka "It’s normally pretty quiet here on weekends since no one stops by on the way home from[school]."

    scene karinjogs5
    with dissolve

    ka "On weekdays, though, I normally just wind up training with Miku or some of the
    other girls. It’s not often that I’m alone. So this is a little weird for me."
    s "Well you’re already doing better than you normally do, so I’m proud of you."

    scene karinjogs6
    with dissolve

    ka "Well, it’s not like I have a choice anymore, is it? You’re my coach."
    ka "If I can’t get over a hurdle as small as just looking you in the eyes, there’s no way I’ll be able to climb over anything else."
    ka "Just...try not to come too close too quickly or something because I probably won’t be able to prevent myself from having some weird reaction."
    s "Noted. We should be practicing social distancing anyway in case some weird disease ever starts going around."

    scene karinjogs7
    with dissolve

    ka "Hahah...Yeah, I guess we probably should..."

    "Karin’s smile somehow manages to light up the world even in the midst of the sunset."
    "She’s a mix of a lot of different great qualities, so I’m glad to see that she’s not
    as...inherently weird as a lot of the other girls I’ve been dealing with lately."

    s "So...are you ready to start?"

    scene karinjogs8
    with dissolve

    ka "Yeah. I just need to run, right? Are you going to run with me?"
    ka "You’re not really dressed for the task, so maybe you can just keep times for me instead?"
    ka "I can’t imagine it’ll be very fun, but at least you won’t have to get all sweaty that way."
    s "That sounds good to me."

    "I pull my phone out of my pocket and open up the stopwatch app."

    ka "Just hit the “lap” button every time I pass you, okay? That’s how I normally time myself. Just...with a tree instead of a teacher."
    ka "You don’t need to tell me my individual times. Just let me know how much faster or slower I am on each pass."
    ka "Endurance is important, so I need to make sure I’m able to keep up with myself more than anyone else."
    s "Roger that. Official coach duties commencing now."

    "I hit the start button on the stopwatch and immediately send Karin spiraling into panic."

    scene karinjogs9
    with dissolve

    ka "Ah- Sensei, wait! You didn’t even count me down! Start over!"
    s "No can do. Clock is already running. Go, Karin, go!"

    scene karinjogs10
    with dissolve

    ka "Ahh! Okay! I’m going!"

    scene karinjogs11
    with dissolve

    "Karin quickly takes off into a sprint to make up for a few seconds worth of lost time."

    scene black
    with dissolve

    "I follow behind her until the two of us are safely out of the center of the park, watching
    as she gradually moves further and further away."
    "The way she runs is a lot different than Miku."
    "Every step that Karin takes seems carefully calculated, whereas Miku seems
    more like a girl who just had one too many energy drinks and was told to run as fast as she can."
    "………"
    "……"
    "…"

    scene karinjogs12
    with dissolve

    ka "How was...that one?"
    s "Thirty seconds under your last. You’re not starting to lose steam, are you?"

    scene karinjogs13
    with dissolve

    ka "Of...course not! Watch me...closely this time!"

    scene karinjogs14
    with dissolve

    "Karin leaves me in the dust once again with a look of determination that could
    rival some of the fiercest athletes."
    "She's really fast despite her size. She’d probably even be able to
    beat Miku if she were several inches shorter and a lot less...busty."
    "………"
    "……"
    "…"

    scene karinjogs15
    with dissolve

    ka "And...that one?"

    "I look down at my phone again to realize that Karin has actually beaten the time of her first lap."
    "I was so caught up in admiration that I didn’t even realize she was giving it her all that time."

    s "Fifteen seconds up."
    ka "From the last one or from the best one?"
    s "The best one. Did you want to call it now? Or do you have a few more in you?"

    scene karinjogs16
    with dissolve

    ka "Heh...I could do this all day..."

    scene karinjogs14
    with dissolve

    "Once again, Karin takes off down the path, looking no slower than she did when she
    started almost twenty minutes ago."
    "How the hell is she able to keep up that pace for so long without even looking phased?"
    "If I were in her shoes, I’d be basically crawling right now."
    "………"
    "……"
    "…"

    scene karinjogs17
    with dissolve

    ka "Hah..."

    "Karin comes to a stop several feet away from me after what I imagine is her last lap."

    ka "Okay...Now I’m done."
    s "I thought you were planning on going all day?"
    ka "Nah...I was...starting to feel bad for you. "
    ka "You looked bored."
    s "I wasn’t bored at all. If anything, I was actually having a good time watching you."
    s "You’re really impressive, Karin. I think I get why you’re so involved with athletics now."

    scene karinjogs18
    with dissolve

    ka "What?! No no no! I’m not that impressive. I just practice a lot."
    s "Isn’t that the same thing? Most people don’t become great at anything without practicing."
    ka "Well, yeah, but like...I don’t know. Getting compliments from you feels weird. Hahaha..."
    s "Well you better get used to it, because I’m pretty sure this is going to be a regular occurrence from now on."

    scene karinjogs19
    with dissolve

    ka "You...want to do this again?"
    ka "I thought you were just trying to get acquainted with everyone on the team?"
    ka "Isn’t it unfair to spend more time with me when there are other girls who need more help?"

    "Karin makes a good point. But something she doesn’t yet understand is that I’m not just doing this because I’m trying to be a good coach."
    "I want to get closer to {i}her{/i} specifically. If I didn’t, I wouldn’t have called her out here today."
    "But that’s not something she needs to know yet."
    "Who even knows how someone as inexperienced and nervous around men would handle it if she were to hear something like that?"

    s "I definitely want to do this again."
    s "Unless...you didn’t have fun hanging around me today?"

    scene karinjogs20
    with dissolve

    ka "What?! O-Of course I had fun! I had a lot of fun! So much fun! It was
    great! It was awesome! It was...It was-"

    scene karinjogs21
    with dissolve

    ka "Oh God! I’m forgetting how words work!"
    s "Well, believe it or not, I had fun too. And I’m really looking forward to doing this again."
    ka "Fun?! You had...but you...the stopwatch...ahhh!"

    "Translation (Projected): Did you really have fun today, Sensei? All you did was stand around with a stopwatch..."

    s "Okay, okay. Calm down. Catch your breath."
    s "Need me to rub your shoulders?"
    ka "Shoulders?!"
    s "They’re the things your neck and your arms are connected to."

    scene karinjogs22
    with dissolve

    ka "I know what they are! I’m just suddenly nervous again for some reason!"

    scene black
    with dissolve2

    "Karin takes another several minutes to calm herself down and get her eyes to go back to normal."
    "I offer to walk her home (With only the purest of intentions) but she respectfully declines since a
    few of her friends are already waiting for her at her family’s apartment."
    "It’s strange."
    "Even though all I did was manage a stopwatch this afternoon, I feel suspiciously content."
    "Maybe I just really like when girls get nervous around me? "
    "The confidence boost is definitely nice, but-"
    "I don’t know."
    "What am I even saying?"
    "I should just get on with my day..."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate1 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label karindate5:
...
```

## Code that triggers this event

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label callkarinafternoon:
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
...
```