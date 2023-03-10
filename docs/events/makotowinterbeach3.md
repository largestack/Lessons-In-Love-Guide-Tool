# I'm Not Here (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Humans With Hollow Bones](./makotowinterbeach2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: makotowinterbeach3
* Group: Makoto
* Triggered by label: makotowinterbeach2
* Chain sources: makotowinterbeach2
* Chain sources path: makotowinterbeach2

## Official wiki page

[I'm Not Here](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotowinterbeach3&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label makotowinterbeach3:
    play music "undersea.mp3"
    scene clearnightsky
    with dissolve2

    "Neither Makoto nor I say anything for the first few minutes of our walk down the coast. "
    "The reason for this being that, in the transition to night, the sky seems to have turned rather extravagant."
    "Not to say it isn’t extravagant to begin with. I mean, it blankets the entire world. "
    "Strike that, it blankets the entire universe."
    "But I suppose at some point it stops being the sky and turns into space."
    "I’m sure there’s a scientific answer to when exactly that is, and I’m sure Makoto knows it because she’s a fucking genius-"
    "But I don’t care enough to ask. "
    "Because whatever the answer is wouldn’t make much of a difference to me."
    "And it wouldn’t fill the gaps in conversation so noticeably empty that we can hear each other breathing over the light movement of the ocean water. "
    "In a drama film, or even something less moving like a romantic comedy, this would be a moment for our hands to gently brush up against one another."
    "There would be a closeup of our fingers awkwardly tangling together before becoming laced and locking into place."
    "But instead, we walk shoulder to shoulder, not coming into direct contact because: A - We’re not allowed to this weekend, and B - We don’t want to."
    "Or at least I don’t want to."
    "I don’t know what Makoto wants...And I think I’ve made that pretty apparent over the last half day..."

    scene makotounderstars1
    with dissolve2

    mak "Sensei...don’t you think this is a little strange?"
    s "Not really."
    mak "I guess it could just be me but...the sky seems rather...colorful tonight."
    mak "Do you really not see it?"
    s "I see it. "
    s "It reminds me a little of the end of the world."

    scene makotounderstars2
    with dissolve

    mak "Huh. I guess it {i}is{/i} like something out of a movie. But I don’t know if I’d compare it to something like the world ending."
    mak "I feel like that would be a little more...red."
    s "Hey, do you remember what we were talking about right before we left by any chance?"

    scene makotounderstars3
    with dissolve

    mak "That’s a weird question. Why do you ask?"
    s "I feel like we’re forgetting something important."
    mak "I don’t feel like that, but...weren’t we discussing your poor treatment of me?"
    mak "Unless you’re referring to the Miku situation, because we discussed that as well."
    s "But nothing else? Nothing that was mentioned right before your head started hurting?"

    scene makotounderstars4
    with dissolve

    mak "What’s this all about? Why would you wait until we’re completely isolated to start being weird?"
    mak "You should at least do these things in front of Miku so I can have {i}some{/i} form of protection in the event of you going postal."
    s "When have I ever gone “postal” before? "
    s "I just wanted to see if there was something we’re forgetting."
    mak "Well, either you’re going insane or simply misremembering, because there are only a few things left I wanted to talk to you about this weekend."
    s "We’re not done with that already?"

    scene makotounderstars5
    with dissolve

    mak "Of course we’re not done..."
    mak "I have to catch up on months of you dismissing me. That can’t be done over the course of one or two hours."
    s "How many hours will it take, exactly?"
    mak "Why? If you’re worried about leaving Miku on her own, I’m sure she’ll be fine. "
    mak "The inn is a lot quieter than our dorm is, after all."
    s "That’s not it. But while we’re on the topic, if we come back to the room and find her hair all over the floor, I’m not going to be of much assistance."

    scene makotounderstars6
    with dissolve

    mak "You’re not very good with crises, are you?"
    s "I’m not."
    s "It’s rather unfortunate as well since they seem to be following me around lately."
    mak "Well, when you live your life getting closer than you’re supposed to with [teenage]girls, things like that are going to happen."
    mak "I suppose you should just be thankful that I’ve been nothing but stable and unobtrusive thus far."
    s "Sure. Except for that one time your mind broke and I slammed you up against a locker."

    scene makotounderstars7
    with dissolve

    mak "I’m sorry, what? "

    if bonus == True:
        mak "Is this one of your weird, perverted fantasies? Because I already told you no sex and I will not be lured into wanting it in the middle of the beach."
        s "It happened."
        mak "..."

    s "It was right before the Christmas party, if I'm remembering correctly."
    mak "That’s simply not possible. "
    mak "I haven’t used my locker since the[school] year started."
    mak "I don’t even think I remember my combination."
    s "Well then where do you keep all of your stuff?"

    scene makotounderstars8
    with dissolve

    mak "Your office."
    mak "I mean, that {i}is{/i} where most of my time is spent, after all."
    mak "It’s not like I have much anyway. Just my shoes and my gym clothes, really. "
    s "You’re...keeping your gym clothes in my office?"
    mak "Don’t worry. I keep them hidden, so it’s not like anyone is going to find them."
    s "Good. Because I have no idea how I’d even begin to explain that."
    mak "I give you permission to tell anyone who happens to find out that you’re just obsessed with me. I don’t mind."
    mak "It’s not like I’m all that popular in the first place, so I don’t have much to lose."
    s "What do you mean you’re not popular? "

    scene makotounderstars9
    with dissolve

    mak "I mean that since {i}someone{/i} I know spends all of his time goofing off and not managing his class, the fact that I {i}do{/i} makes me unpopular by default."
    mak "It’s less a matter of people disliking me and more just...being annoyed by me for ensuring that they don’t slack off too much before standardized testing."
    mak "I’ve even been confronted by a few of them before due to how close people seem to think we are with one another."

    scene makotounderstars10
    with dissolve

    mak "Which, not to make you feel bad or anything, was kind of a slap in the face when I know our relationship has been almost entirely one-sided."
    s "I-"
    mak "There’s no need to reiterate your position, Sensei. You took care of that back in the room."
    mak "Kind of."
    mak "And besides, things are going to get better from now on. That’s why I’m telling you all of these things."
    mak "What’s in the past will always remain in the past. There’s no point in digging any of it up again if it’s just going to make you feel upset."
    mak "There’s enough misery in this world for everyone to help themselves to seconds. Taking any more of that would just be greedy."
    s "You know, any time I start to think about how different you are, I feel like one thing you say drags you back to my level."
    mak "Good. There’s that equal footing I was talking about earlier."
    mak "If we’re on the same level, you won’t be able to look down on me. And I won’t feel the unending pressure of having to look up to you."
    mak "Everyone wins."
    mak "Well, almost everyone."
    mak "Frankly, there are several girls I’m quite worried about when it comes to how many helpings of misery they’re piling onto their lunch trays."
    s "Would you mind explaining what you mean by that?"
    mak "What I mean is that not everyone is smart enough to really understand what you’re doing here, Sensei."
    mak "And that there are plenty of people who would sooner do something stupid than confront you with their issues as I’m doing right now."
    mak "You should be happy I’m not one of those people."
    s "And how should I feel about the others?"

    scene makotounderstars11
    with dissolve

    mak "I suppose that depends on how far things have already gone with them."
    s "...Which means?"

    if bonus == True:
        mak "Which means that if you’ve already done with them as you’ve done with me, it’s going to be exponentially harder for them to confront the hardships that are certain to befall them."
    else:
        mak "Have you...hugged anyone in the class, Sensei?"
        s "..."
        mak "How could you?"
        s "I'm sorry. I just really like hugs."

    scene makotounderstars12
    with dissolve

    mak "The amount of pain in this world is unfathomable at times. "
    mak "And you’re like a vessel flying over all of us, leaking that pain out and letting it drip into our mouths as we stare up at beautiful, colorful, world ending skies."

    scene makotounderstars13
    with dissolve

    mak "Sensei-"
    mak "What would it take to have you drop all of them and be with only me?"
    mak "Pardon me for my sudden selfishness, but I’m genuinely curious about whether something like that would even be possible."
    mak "I deserve it, don’t I? "
    mak "Is there anyone you know that has done as much for you as I have?"
    s "I mean...Ami has been cooking and cleaning for me since-"

    if bonus == True:
        play sound "static.mp3"
        scene imissyou13 with flash
        scene makotounderstars13 with flash
        stop sound

        "There is someone else."

        play sound "static.mp3"
        scene norikofirstvisit27 with flash
        scene makotounderstars13 with flash
        stop sound

        "There are so many people."

    play sound "static.mp3"
    scene howifeel2
    with flash
    stop sound

    ho "HELLO AGAIN"
    s "dolyl kpk fvb jvtl myvt?"
    ho "IT HAS BEEN A LONG TIME SINCE WE LAST MET"
    ho "I HAVE MISSED YOU"
    a1 "Missed you very much! "
    a2 "Like swallowing nails!"
    a1 "The girl has been crying this whole time!"
    a2 "Why do you run from her?!"
    a1 "Run from everything!"
    a2 "Coward!"
    a1 "Sinner!"
    a2 "Look at her!"

    ho "DO NOT LISTEN TO THEM"
    ho "LISTEN ONLY TO ME"
    ho "HOW MANY HANDS DO CLOCKS HAVE"
    s "zv thuf ohukz. hss vm aolt pucpzpisl."
    ho "WRONG"
    ho "THERE ARE THREE HANDS"
    ho "ONE FOR SECONDS"
    ho "ONE FOR MINUTES"
    ho "ONE FOR HOURS"
    ho "YOU THINK TOO MUCH ABOUT THE WRONG HANDS"
    ho "AND FOCUS NOT ON THE CORRECT ONE"
    s "zluk tl ihjr."
    ho "BACK WHERE?????"
    ho "WHY GO ANYWHERE BUT HERE?????"
    ho "I CAN GIVE YOU EVERYTHING"
    ho "I CAN BE EVERYTHING"
    ho "AND YET YOU LOOK AWAY"
    ho "SUCH A WEAK HUMAN"
    a1 "So weak!"
    a2 "Pathetic!"
    a1 "Flay the skin from his body!"
    a2 "Lay him out to dry at the height of the world!"
    a1 "Inject the stars she loves so much into his eyes!"
    a2 "Drink the fluids! Drink the fluids!"
    ho "SILENCE"
    a1 "{s}ssssssssssssssssssssssssssssssssssssssss{/s}"
    a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"
    ho "THE SNOW CAN ONLY LAST SO LONG"
    ho "GOODBYE"

    play sound "static.mp3"
    scene makotoclass with flash
    scene makotolocker7 with flash
    scene bluejay38 with flash
    scene makotoistired23 with flash
    scene makotobeach with flash
    stop sound

    mak "I should have expected as much."
    mak "Asking you to give up the others for someone like me is laughable when I’ve only just started to spread my wings."
    mak "But they’ll continue to spread, Sensei."
    mak "They’ll spread so wide that they’ll cover the world and block out the sun."
    mak "They’ll block out everything."
    mak "And then you’ll {i}have{/i} to look at me."
    s "…"
    mak "…"
    mak "But, for now-"
    mak "I suppose there’s nothing else I can do."

    "I’m not here."
    "Well, I {i}am{/i} here."
    "But I’m not here."
    "I feel far away from something."
    "I feel hands on my shoulders, pulling me backwards."
    "I feel frayed wires wrapped around my ankles, scratching me enough to draw blood but not to sever my Achilles tendons."

    mak "...Huh."
    mak "Do you feel that, Sensei?"
    s "Feel what?"
    mak "A...minor earthquake, maybe?"
    mak "I thought I felt the ground shaking, but it was probably just a wave crashing down or something."

    "The ocean is still, though."
    "There are no waves anywhere to be found."

    mak "Oh, I did a little more digging on this Yasu Yasui character, by the way."
    mak "I don’t know why it never occurred to me to just ask the other girls from Kumon-mi Academy, but several of them knew her. "
    mak "Namely Uta and Noriko."
    s "Figures that the talkative ones would know her. "
    mak "I suppose. Neither of them seemed to know her all that well, though."
    mak "Apparently, she didn’t attend normal classes on account of her...behavior. So I’m now worrying that we really {i}will{/i} have another Yumi on our hands before we know it."
    s "Did they say anything about how cute she is by any chance?"
    mak "Really? You’re going to ask that now? After I {i}just{/i} finished telling you about how I want you to look at me more?"
    s "This doesn’t count as me being mean, does it?"
    mak "It...kind of does."
    s "Oh. Well then I guess I can just find out when she transfers in."
    mak "I...guess so."
    mak "Can I ask you one more thing before we head back, Sensei?"
    s "You weren’t kidding about wanting to talk a lot this weekend, were you?"
    mak "No, I was not. But there’s been something else on my mind that I haven’t really had a chance to ask you about."
    s "And what is that?"
    mak "Well...I looked into Noriko’s background after she transferred in and wound up speaking with her parents."
    s "Well that’s not creepy or an invasion of privacy by any means."
    mak "Can you let me finish, please?"
    mak "I wound up speaking with them and they definitely remember you, so her story checks out."
    mak "But I..."
    s "...You what?"
    mak "I also looked into Maya as well because...I was curious about their apparent...{i}connection{/i} with one another."
    mak "Maya spends a good deal of time at your house, correct? I know her and Ami are close, so it would only make sense if she did."
    s "Yeah. It’s basically a second home for her, I guess."
    mak "I thought so...But would you have happened to speak with any of her family in the past, by any chance?"
    mak "Because all of the phone numbers on record for her are either disconnected or simply made up. "
    s "For Maya?"
    mak "Yeah. I mean, it’s possible that it’s just outdated paperwork, but...it seems strange."
    s "All I really know is that she’s not originally from here."
    mak "Ahh. Well I suppose that would probably explain it."
    mak "Sometimes, files get mixed up when students switch municipal districts, so it probably just got lost in the shuffle somewhere."
    mak "It’s no big deal, I suppose. I’ll just ask her for updated information soon."
    mak "Oh, and is it true that you dated Niki Nakayama?"

    if otohapark1 == True or saradate10 == True:
        s "Yeah, that’s true."
        s "Want me to call her and confirm that for you? She loves when I do that."
        mak "What? No. That won’t be necessary. I have no reason to doubt you since I heard it directly from Noriko’s parents."
        mak "But that’s really surprising. I didn’t take you as the type to be into nice, pretty girls like her."
    else:
        s "Yeah, that’s true."
        mak "That’s really surprising. I didn’t take you as the type to be into nice, pretty girls like her."

    s "Pretty, sure. But I can assure you that Niki is anything but nice."
    mak "Really? But she seems so kind on TV."
    s "She’s kind of like what would happen if Yumi became really stuck up and started chewing unhealthy amounts of bubblegum."
    mak "Wow. I guess that whole thing about celebrities not being who you expect them to be is true then."
    s "Anything else you were curious about or can we start heading back now? It’s getting cold."
    mak "We can start heading back. "
    mak "We’re going to have to be quiet when we walk in, though, since Miku is probably asleep by now."
    s "Already? I figured she’d be the type to stay up until like 3:00 AM."

    if bonus == True:
        mak "Oh, lord no. She’ll be out like a light. But she wakes up very easily, so we’ll need to be really quiet while getting dressed."
        s "I guess that means there’s no chance for a nightcap then?"
        mak "Are you seriously this horny all of the time? I think you might have some sort of condition, Sensei."
        mak "We should take you to the doctor once we get back home."
        s "My feelings for you are not a sickness, Makoto."
        mak "Ugh..."
        mak "At least wait until we get back to the dorm to say things like that..."
    else:
        mak "Nope. And Makoto sleepy so we leave now."
        s "Sensei sleepy too. I want my jammies."

    scene black
    with dissolve2

    "Makoto and I make our way back to the inn."
    "Halfway there, snow begins to fall."

    $ renpy.end_replay()
    $ makotowinterbeach3 = True
    $ makoto_love += 1
    stop music fadeout 10.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    jump mikuwinterbeach1

label makotowinterbeach4:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```