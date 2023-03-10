# Watching TV Alone (Haruka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Haruka love greater than or equal to 15

* Event [Performance Review](./harukadate10.md) (Haruka) is completed)



## Next events

None

## Event properties

* Id: harukadate15
* Group: Haruka
* Triggered by label: callharukanighthang
* Triggered by branch label: callharukanighthang
* Triggered by path: callharukanighthang->harukadate15

## Official wiki page

[Watching TV Alone](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukadate15&go=Go) for more details.

## Event code

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label harukadate15:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "We talked recently about spending some time together at her place and watching movies or something along those lines, so I figure now is as good a time as any to make that dream a reality."
    "And when I say “dream,” I mean it very loosely as my dreams are much more exciting."
    "When I actually have them, that is."
    "Lately, I haven’t been having-"

    play sound "phonebeep.wav"

    h "Hey! What’s up?"
    s "Oh, hey. Nothing really."
    s "Are you free tonight?"
    h "As a matter of fact, I am. Sara just bailed on me and Molly is “managing” the cafe tonight."
    s "And you’re sure the cafe is going to be okay?"
    h "Nope! But I really don’t want to think about work right now."
    h "Come over and let’s do stuff. "
    h "I’d offer to pick you up but I’m feeling really lazy and don’t want to leave right now."
    s "Wow. Thank you for the kind offer, but I will walk."
    h "I know you will!"
    h "See you soon!"

    play sound "phonebeep.wav"

    "Haruka hangs up the phone and, before I know it, I’m walking to her place."

    scene nightsky
    with fade
    play music "love.mp3" fadein 10.0

    "The walk to Haruka’s is always kind of annoying."
    "I should probably invest in a car sooner or later, but..."
    "I don’t know."
    "I’ve gotten kind of familiar with these streets over my time here."
    "I’m memorizing them quicker than I’ve memorized anything, I think."
    "Besides things that are meant to be memorized like phone numbers or addresses. "
    "You know what I’m talking about."
    "The process of remembering things that you are only {i}kind of{/i} supposed to remember."
    "Like streets or the names of distant relatives."
    "Like how many beeps the microwave makes after it finishes blasting radiation into a frozen TV dinner."
    "These are things we memorize subconsciously as opposed to consciously."
    "But the more time I spend here, the more I move from the former form of memorization to the latter."
    "I want to memorize these streets."
    "I feel I’ll be spending a concerning amount of time traversing them if nothing goes horribly wrong in the near future."

    play sound "doorbell.mp3"

    "I arrive at Haruka’s place after what seems like half an hour and ring the bell."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    h "Hey! How was your walk?"
    s "Unnecessary."

    scene harukaalone1
    with dissolve

    h "Well, on the bright side, you get to see me now. So that’s at least slightly rewarding, right?"
    s "Slightly, yeah."
    h "Awesome. I’m almost worth a thirty minute walk. "
    h "I’ve gotta say this is personally better than I ever thought I’d do, sooooo hooray for Haruka!"
    s "I’ve only been here for ten seconds and the self-esteem issues are already coming out. "
    s "Tonight is going to be a blast."

    scene harukaalone2
    with dissolve

    h "Hey, you knew what you were signing up for and you still came either way."
    h "I even gave you the chance to say “No, I don’t want to walk all the way over there,” and yet, here you are. "

    scene harukaalone3
    with dissolve

    h "So, since you’re here, I guess it’s finally time we find something to do, huh?"
    s "What would the gameplan have been if I never came?"
    h "I told you at the cafe, didn’t I? Probably ice cream and crying."
    s "You can still eat ice cream if you want."

    scene harukaalone1
    with dissolve

    h "I’d have to run out and buy some."
    h "Want me to cry instead?"
    s "Not really. I never know what to do around girls when they cry."

    scene harukaalone4
    with dissolve

    h "Uhh, how often are you around crying girls?"
    s "Often enough for this to be an actual thing I have learned about myself."
    h "Fair enough. What you do on your own time isn’t really my business."

    scene harukaalone5
    with dissolve

    h "Know what {i}is{/i} my business, though?"
    s "What, Haruka?"
    h "Koi Cafe."
    s "…"
    h "Get it?"
    h "Cause like-"
    h "…"
    h "Yeah."
    s "…"
    s "Okay, well it’s been fun. I’ll see you later."

    scene harukaalone6
    with dissolve

    h "Oh, come on! That was good!"
    h "Here, come sit down. It’s no fun just standing near the door and listening to me tell jokes."

    "Well, she’s right about that, at the very least."

    scene black
    with dissolve

    "Haruka walks over to her sofa, grabbing the TV remote off the table in front of her and turning up the volume on whatever program she was watching before I got here."
    "I walk back to the entryway and kick my shoes off after I realize I forgot to remove them before taking my place next to her on the couch."

    scene harukaalone7
    with dissolve

    h "So, welcome to a day in the life of me."
    h "When I’m not making cappuccinos or bossing around a bunch of mini versions of myself, I’m doing this."
    h "Sitting on a couch and contemplating what sort of person I am while watching Gordon Ramsay make children feel bad about themselves on Master Chef Junior."
    s "You lead an interesting life, Haruka."
    h "Don’t tease me."
    h "Even before my husband was drafted, it was like this- just with two bodies on the couch instead of one."
    s "So you weren’t happy even when he was around?"

    scene harukaalone8
    with dissolve

    h "I never said that."
    h "When you love someone, you can do things like just sit on a couch with them and watch Gordon Ramsay yell at children and it will feel like the most fun you’ve had in forever."
    h "It isn’t until they’re gone that you realize how depressing it is to be watching TV alone."
    s "This conversation got serious much quicker than I expected it to."

    scene harukaalone9
    with dissolve

    h "Hahaha...yeah. Sorry about that. I’ve just...gotten so used to doing things like this with him that I find myself reliving those days any time I turn on Netflix."
    h "Which sounds kind of shitty to say since he’s still alive-"

    "Maybe."

    h "But...yeah. Let’s talk about something else. Like..."

    scene harukaalone10
    with dissolve

    h "Like, what’s it like being a[school] teacher?!"
    h "That sounds like a lot more fun than what I do."
    s "You’re only saying that because you’re apparently hot for [teenage]girls."
    h "Yup. You got me. "
    h "Now tell me what it’s like."

    "Huh."
    "How I feel about teaching..."

    s "It..."
    h "...?"
    s "It kind of sucks."
    h "…"

    scene harukaalone11
    with dissolve

    h "That...is not the answer I expected."
    h "Why would you say that?"

    if bonus == True:
        h "With how much I’ve heard about you in[school] from Rin, I always kind of thought you liked your job."
        h "You know, the whole touching youths thing."
        s "Just to clarify, which sort of “touching youths” are you referring to right now?"

        scene harukaalone12
        with dissolve

        h "The not-creepy one this time."
        h "Aren’t you interested in making differences in these girls lives or something like that?"
        h "How’d you get into teaching in the first place?"
        s "It just...kind of happened."
        h "So you just kind of happened to go to[school] for years to become a teacher and then just kind of applied for a teaching job?"
        s "No I mean it literally just kind of happened."
        s "You wouldn’t get it."
        h "Try me."
        s "It involves time travel."
    else:
        s "There aren't enough vending machines."

    scene harukaalone13
    with dissolve

    h "Okay, never mind. "
    h "It’s clear you’re not going to be serious, so we can just move on to something else."

    "Oh well."
    "Can’t say I didn’t try."

    scene harukaalone14
    with dissolve

    h "You know, I used to have a crush on my [high_school] teacher when I was around Rin’s age."

    if bonus == True:
        h "Granted, I was too much of a coward to ever tell him that. And it’s not like I would have expected anything to have happened even if I did."
        s "Worried about the age gap thing?"
        h "More like there just...wasn’t anything notable about me."
        h "I was just a normal girl living a normal life and studying just like any other normal person until, one day, I met the guy who I would end up marrying."
        s "And suddenly we’re back at your husband."
    else:
        s "Ew. Stop being so inappropriate all the time. You always share way too much and it makes me uncomfortable."

    scene harukaalone15
    with dissolve

    h "Fuck! Sorry. I didn’t mean to. It just keeps happening."

    if bonus == True:
        s "It’s fine. If it was that big of a deal, you wouldn’t keep inviting me over."
    else:
        s "It’s fine. If it was that big of a deal, I would have just left."

    scene harukaalone16
    with dissolve

    h "Yeah...You’re...probably right about that."
    h "And besides, we’re just friends so..."
    h "It’s not like I love you or anything like that."
    h "You’re just...keeping me company."
    h "That’s all."

    if harukasex == True:
        "Haruka justifies her betrayal of a man who has not yet been confirmed dead in the only rational way she’s able to think up."
        "She pretends the touch of my hands and the length of my cock are only temporary respites given to a woman in grief despite her unmeasurable levels of uncertainty."
        "I can see through her."
        "Anyone could if they’d just open their eyes."
        "She is horrible- just like me."
        "We fit each other well."
        "Physically and non-physically. "
        "She knows it too."
        "It’s one of the many reasons she continues to cry nearly every time we fuck."

    else:
        "That’s right."
        "As it stands, all I am to Haruka is a friend."
        "Could I change that if I truly applied myself?"
        "Probably."
        "But would it be right to do so?"
        "Who knows?"
        "It’s not really my place to say."
        "If she thinks betrayal is the path that will make her feel whole, it’s a path she’s likely to take with or without me."
        "All I can really do for the time being is continue to be near her."
        "To quell the unending loneliness of a woman unloved."

    s "Right. We’re just friends."

    scene harukaalone17
    with dissolve

    h "Exactly! Which is why it’s cool for us to do stuff like hang out on my couch and just...talk or...whatever it is we’re doing now."
    s "Right."
    s "Now, your relationship with {i}Maki{/i} on the other hand..."

    scene harukaalone18
    with dissolve

    if bonus == True:
        h "Ugh. She’s so hot, though!"
    else:
        h "But she is so good at hugging!"

    h "And he already signed off on that so it’s totally okay!"
    h "Besides, it really {i}does{/i} only happen on rare occasions when we’re drunk."

    if harukalust10 == True and bonus == True:
        h "And you know firsthand what kind of wonders she can work with her tongue!"
        s "This is very true. That was most definitely not her first time."
        h "Probably her millionth!"
        s "Okay now that just can’t even be possible."

    h "Maki’s...a different type of animal compared to someone like me."

    if bonus == True:
        h "She’s like this crazy sex goddess and I’m some girl who was too scared to even touch herself until senior year of [high_school]."
    else:
        h "She’s like this crazy hug goddess and I'm just some girl who violently attacks anyone who tries to hug me."
        h "It's probably because I didn't have any hugs for the first ten years of my life."
        s "It is true. You are very bad at hugging."

    h "I get nervous around her and just kind of...follow her lead."
    s "Were you really that late of a bloomer?"

    if harukasex == True:
        scene harukaalone19
        with dissolve

        h "I’ve only ever been with two guys before..."
        h "That includes kissing, too."
        h "Well, not counting girls."

    else:
        scene harukaalone19
        with dissolve

        if bonus == True:
            h "My husband is the only guy I’ve ever been with..."
        else:
            h "My husband is the only guy I’ve ever hugged..."

        h "I’ve never even kissed anyone else."
        h "Well, not counting girls."

    s "If it’s any consolation, the amount of girls you kiss makes no difference to me."
    s "Feel free to shoot for the world record if you want."
    s "I will support you every step of the way."

    scene harukaalone20
    with dissolve

    if bonus == True:
        h "Even when I start coming for all of the girls in your class?"
        s "Start with Rin. I frequently worry that she’ll explode if she doesn’t find an outlet for her pent-up lesbian energy soon."
        h "How about we share her?"
        s "Deal. Sign me up."
    else:
        h "Thank you, Sensei. That is very nice of you."
        s "Rin would also probably support you every step of the way. She loves you, Haruka. You are very important to her."

    scene harukaalone21
    with dissolve

    h "I’m gonna tell her you said that~"
    s "Fine by me."
    s "Also, what is the meaning of this?"
    s "I don’t have Rin’s number yet and I feel like I’m much closer to her than you are."
    h "She works for me, dude. I need her number to send her pictures of the schedule."
    h "Do you want it?"
    s "I hope you mean her number and not a picture of the schedule."
    h "What, so you don’t want to come work for me?"
    s "I can’t say I do."
    s "I’ll accept a phone number, though."
    h "Fine. Here."

    "Haruka begins listing the digits of Rin’s phone number and I carefully type them into my phone."

    $ rinnumber = True

    "{i}Congratulations! You have received Rin’s phone number in an extremely roundabout way!{/i}"
    "{i}You can now call her to hang out on afternoons, but she will likely be confused when she realizes she never personally gave you her number!{/i}"

    s "This is a big victory for me."

    scene harukaalone22
    with dissolve

    h "Well I’m sorry to be the bearer of bad news but I’ve got a big loss for you coming up next."
    s "What? What happened?"

    if bonus == True:
        h "So when I told Rin just now that we were talking about sharing her-"
        s "You actually told her that? I thought you were kidding."
        h "Well, what I {i}really{/i} said was, “Would you date your teacher?”"
        s "Why? You completely removed yourself from the equation and this was entirely your idea."
        h "I’m testing the waters. Just be happy I gave you her number."
        s "Haruka, what the fuck?"
        h "Well anyway, all she texted back was the upside down smile emoji."
        s "That could mean anything."
        h "Mmm...I think in this case it means “I’d rather date you, Haruka. You’re so pretty and your boobs are great.”"
        s "You sound like a grown-up version of my [niece]."
    else:
        h "I accidentally texted Molly instead."
        s "Nooooooooooooooo..."
        h "What is wrong?"
        s "My accountant does not want me conversing with Molly."

    scene harukaalone23
    with dissolve

    h "Wanna give me {i}her{/i} number in exchange for Rin’s?"
    s "I don’t think she’s your type. And also no."

    scene harukaalone24
    with dissolve

    h "Fine. Looks like I’ll just have to send Rin a wink emoji and forever ruin your chances of romancing her."
    h "I’ve been around these girls long enough to know how they operate and-"

    scene harukaalone25
    with dissolve

    h "Woah!"
    s "Woah what? What happened?"

    if bonus == True:
        s "Did Rin say something else?"

    scene harukaalone26
    with dissolve

    if bonus == True:
        h "No, but Molly did."
        s "You texted her too?"
        h "It was a group text with the two of them."
        s "You didn’t even do it privately?..."
        s "What did Molly say?"
        h "Six eggplant emojis and then water droplets."
        s "…"
        s "Is that good? That sounds good."
        h "Too good. You should be worried."
        s "Well, at least I went one for two."
        h "…"
        s "…"
        h "You’re gonna tell me if anything happens, right?"
    else:
        h "Rin has been kidnapped by a secret, evil organization!"
        s "We must rescue her immediately."
        h "I agree! We must!"

    scene black
    with dissolve2

    if bonus == True:
        s "Probably not."
        h "And you call yourself my friend..."

        "Haruka and I hang out for a while longer and she continues to lecture me on the meanings of different emojis."
        "I immediately forget all of them because it is a stupid conversation topic and I honestly just don’t care."
        "Eventually, I wind up walking home-"
        "And once again thinking about how nice it would be to memorize these streets."
    else:
        "Haruka and I put on our superhero costumes and take off down the street using our cool grappling hooks and rocket boots."
        "We bust into the secret lair of Dr. Badguy and get our friend back after a super intense fight Selebus didn't have time to capture CGs for."
        "It was really awesome, though. I wish you could have been there."

    $ renpy.end_replay()
    $ harukadate15 = True
    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label harukainvite1:
...
```

## Code that triggers this event

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label callharukanighthang:
    if harukanumber == True and day89 == False:
        "I think I should probably get to know Haruka a little better before calling her."
        jump callnight
    if haruka_love >= 0 and day89 == True and harukadate1 == False:
        jump harukadate1
    elif haruka_love >= 0 and haruka_love <= 4 and harukadate1 == True and harukadate5 == False:
        play sound "phonebeep.wav"

        "I tap on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer."
        "..."
        "I hope she doesn't still feel weird about what happened at the bar the other night."
        "Oh well...I guess I'll just have to...keep visiting her at the cafe or something for now."
        jump callnight
    if haruka_love >= 1 and haruka_love >= 5 and harukadate1 == True and harukadate5 == False:
        jump harukadate5
    if haruka_love >= 15 and harukadate10 == True and harukadate15 == False:
        jump harukadate15
...
```