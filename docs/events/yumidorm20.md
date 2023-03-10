# Great Expectations (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 20

* Event [Token Tsundere](./streets20.md) (Yumi) is completed)



## Next events

* [Yumi: A Place Like This](./streets25.md)

## Event properties

* Id: yumidorm20
* Group: Yumi
* Triggered by label: yumidorm
* Triggered by branch label: yumidorm
* Triggered by path: yumidorm->yumidorm20

## Official wiki page

[Great Expectations](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumidorm20&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm20:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "…"
    "I knock on Yumi’s door, hoping that she’s hanging out in her room rather than wandering around Kumon-mi selling stolen candy to children."
    "It’s something I’ve never had to worry about with any of the other girls, but is a real concern to me now following our last lunch-outing."

    y "Yeah. What?"
    s "It’s me. Can I come in?"
    y "You’re not going to pretend to be a delivery guy this time?"
    s "No, I think we’ve passed that point in our relationship."
    s "Also, we have important things to discuss regarding the amount of food that you will be eating in the future."
    y "Weird fuckin’ way to say you’re ready to teach me interview shit, but sure. Whatever."
    y "Door’s open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I make my way into Yumi’s room to find her sitting on her bed in her pajamas, scribbling something into a notebook..."

    scene yuminotebook1
    with dissolve

    s "You know, I didn’t really think you were going to be taking this interview thing so seriously that it would warrant a notebook."
    y "That was the plan, but I ran out of lead after the ‘b’ in ‘job’ so I guess I'm shit outta luck now."
    s "You can’t even afford pencil lead?"
    s "Don’t they give that out for free in the[school]?"
    y "Beats me. When the fuck am I ever in[school] to begin with? How would I even know?"
    y "'Sides, I wouldn't even know where to go for it if that was true."
    y "Shit, this isn’t even my pencil. I took it off Chika’s table."
    s "You’re a mess, Yumi."

    scene yuminotebook2
    with dissolve

    y "Yeah, and you’re a fucking dick but you don’t see me complaining about it!"
    s "I see you complaining about that literally every time we’re next to each other."
    y "Well...stop being a dick, then!"

    "Maybe I should bring Yumi a few pencils or something if I can ever remember to do that?"
    "Despite how hard she’s apparently trying to find work, I can’t imagine this whole ramen shop situation is going to end in success either."
    "And if she’s actually going to apply herself, the least I can do as the person basically orchestrating all of this is to provide some of the tools she needs."
    "{i}If{/i} I can remember, of course. Which remains to be seen."

    s "Okay, I’ll stop being a dick and go directly into teacher-mode if that's how you want to do this."

    scene yuminotebook3
    with dissolve

    y "Didn't even realize that was a setting you had."
    y "Why the fuck did it take so long to activate it?"
    s "It’s still in test-mode, so apologies in advance if this doesn’t work out how I intend it to."
    y "I highly doubt it will, but go ahead. Do your thing."

    "I clear my throat and crack my knuckles. Then, teacher-mode activates."

    s "The most important part of a job interview is the first impression. Do you know what that means?"

    scene yuminotebook4
    with dissolve

    y "Uhh...probably like...bowing and shit. Right?"
    y "And aren’t you supposed to bring a gift or something as well?"
    s "That’s advanced stuff. "
    s "All {i}you{/i} really need to worry about is not tensing up so much."
    s "And also not threatening to kill anyone."

    scene yuminotebook5
    with dissolve

    y "This is already stupid."
    y "The fuck do you mean by “not tensing up so much?” Am I really that...tense looking?"
    s "I actually don’t think I’ve ever seen you look relaxed before."
    s "Even now, you’re wearing pajamas and I still feel like you’re ready to attack me."

    scene yuminotebook2
    with dissolve

    y "Well, excuse me, but the guy in my room has an established track record of attacking me! So, yeah! Of course I’m going to be fucking ready to defend myself! "
    s "The only thing I’m going to attack you with is {i}knowledge{/i}."

    scene yuminotebook6
    with dissolve

    y "The fact that there are people I know who go out of their way to talk to you is abso-fucking-lutely mind boggling."
    s "I agree. But it is what it is and we must accept it."

    scene yuminotebook7
    with dissolve

    y "That aside, I've got a question. The fuck am I supposed to do if I get asked that fuckin' “Where do you see yourself in ten years” question?"
    s "I’d probably start by telling the interviewer where you see yourself in ten years."
    y "Yeah, yeah. I get that. But I’m supposed to like, {i}lie,{/i} right?"
    s "Is...your answer to that question not good?"

    scene yuminotebook8
    with dissolve

    y "The fuck do {i}you{/i} think?"
    y "I’ll be lucky if I’m not in fuckin' jail in ten years. Can’t you just give me the right answer?"
    s "There’s not really a right answer to that question. Only wrong ones."
    y "Well, give me an example of a wrong one, then."
    s "I probably wouldn’t mention the jail thing, to start."

    scene yuminotebook2
    with dissolve

    y "Besides the jail thing! I obviously know I’m not supposed to say that!"
    s "Just avoid any scenario that makes you look bad. Be vague or something."
    s "Tell them your dreams. Aspirations. Any of those things that normal girls have."

    scene yuminotebook3
    with dissolve

    y "Sorry for not being a fucking “normal girl.” Not everyone knows what they want to do with their life, you know?"

    if bonus == True:
        y "We can’t all just fuckin’...become [high_school] teachers and spend our days fingerbanging our students."
        s "I had no idea you were so interested in my career."

        scene yuminotebook2
        with dissolve

        y "I’m not interested in your fucking career! Obviously, I don’t want to be a teacher!"
        y "I’m just sayin’ that you shouldn’t expect a girl my age to have fucking everything figured out!"

        "It’s been a long time since I was Yumi’s age, but she’s right."
        "Perhaps I’m being a little too hard on her?"
        "Your first part-time job should be as simple as just...knowing the ‘right’ answers to interview questions."
        "So trying to coax even more out of her is essentially hopeless at this point in time."
        "She needs to learn how to crawl before she can walk. And she needs to fail repeatedly in order to do either of those two things."
        "But even with that being said, I can't just abandon her in the middle of a busy road and hope she dodges traffic without the ability to move herself in any direction."
        "I'll help her cross for now."
        "I'll help her so if she ever does get hit, I won't have myself to blame for it."

        s "Just try saying something like...”In ten years, I hope to be settled into a career that I can grow and advance with.”"
        s "Or talk about how you’re going to go to law[school] or something. I’m pretty sure that takes around fifty years to complete, though."
    else:
        s "Maybe you can become a lawyer or something?"

    scene yuminotebook9
    with dissolve

    y "Me? A lawyer? That’s rich."
    y "Would kill to see the look on my dad’s face if that ever happened."
    s "Does he not have great expectations for you or something?"

    scene yuminotebook10
    with dissolve

    y "Would {i}you{/i} have great expectations with a daughter like me?"
    y "Isn’t Ami like, already a fucking homemaker in her freshman year of [high_school]? She’s way ahead of the game."
    y "I can’t even make an omelette."
    y "Fuck, I can’t even {i}afford{/i} an omelette."
    y "I’ve got no interests. No talent. No work experience. No work {i}ethic.{/i} I’ve gotten into more fights than I can even remember."
    y "Course my dad doesn’t have great expectations of me. Why would he when I ain't given him a reason to?"

    scene yuminotebook11
    with dissolve

    y "But now that I know what to tell my interviewer, I’m as good as gold."
    y "If you’ve got weaknesses, just fuckin’ hide ‘em from people until you get what you want out of ‘em."
    s "…"
    y "…"

    scene yuminotebook7
    with dissolve

    y "What? Why are you all fuckin’ quiet all of a sudden?"
    s "Sorry. I'm just not really used to relating to anything you say and that actually made sense to me."

    scene yuminotebook3
    with dissolve

    y "Well, don't relate {i}too{/i} much, dickweed. I’m nothing like you. I’m nothing like anyone."
    y "I’m my own fuckin’ person and, if you don’t like it, you can get the fuck out of my room."
    s "That probably wouldn’t be a good idea. Interviews are normally more than one question and I’m pretty sure that one won’t even be asked since it's extremely cliche."

    scene yuminotebook8
    with dissolve

    y "Wait, for real? I thought that was like, one of the textbook interview questions."
    s "It used to be. But now, most businesses you'll be applying to just want to test your people-skills or something like that."

    scene yuminotebook2
    with dissolve

    y "Well, then why the fuck have we been rambling on about the other question for so long?!"
    s "You seemed pretty dead-set on finding out an acceptable answer so I just kind of went along with it."

    scene yuminotebook12
    with dissolve

    y "Jesus, fuck. This is so fucking stupid..."
    y "Are you sure my TV business won’t work out? "
    y "Maybe I just need to figure out how to get my hands on some of the newer models or something."
    s "You should really stop calling that a business, Yumi."
    s "Besides, for this next interview, I’m pretty sure all of your questions are just going to be about noodles."
    s "Practicing conventional interview tactics will help you further down the road, but..."
    s "Well, let’s just say that Tsuneyo isn’t the most conventional person out there."

    scene yuminotebook6
    with dissolve

    y "How much is there to know about fucking {i}noodles{/i}? They’re noodles."
    s "Just talk about how great they are or something. I’m sure that will get her attention."
    y "I feel like you’re setting me up for failure."
    s "I wouldn’t have come all the way over here just to torment you."
    y "You absolutely would have come all the way over here to torment me. That’s literally all you ever do."
    s "Wanting to torment you and wanting to see you are two different things."

    scene yuminotebook13
    with dissolve

    y "Yeah, whatever. Fuck you."
    y "But thanks for the noodle tip...which is a weird fucking sentence now that I've said it out loud."
    y "I’ve just got a feeling this interview thing is going to be weird as shit, so I’m not gonna get my hopes up or anything like that."
    y "The sooner I get an actual job, the sooner the two of us can split and not have to go back and forth like this anymore."
    y "Shit’s fucking exhausting. I just want it to end."

    "Those words probably would have packed a lot more punch if she hadn’t been looking away, slightly blushing while saying them. "
    "Despite her constant beratement of me, I can’t help but feel like Yumi doesn’t hate this as much as she’s letting on."
    "Obviously, there’s still a fair bit of {i}very{/i} warranted disdain regarding some of my actions with her in the past, but..."
    "We’ve gotta be getting somewhere. Right?"
    "I just hope she doesn’t wind up exploding again if this ramen shop thing doesn’t go as planned."
    "The important part is not getting her hopes up too high, which is something I may have let happen last time- so I'm glad to hear she's attempting to avoid that."
    "And hey, who knows? Maybe if Yumi just...continuously tells Tsuneyo how great noodles are, Tsuneyo won’t know how to refuse?"

    s "If you want this partnership to end that desperately, try {i}this{/i} out during your interview."
    s "But keep in mind, this strategy will work literally nowhere else. "

    scene yuminotebook10
    with dissolve

    y "Just tell me the fuckin’ strategy. We’ll worry about other interviews when it comes time for them."
    s "The only words you are allowed to say during your entire meeting are..."
    s "“I love noodles.”"
    y "…"
    s "…"
    y "Yeah, I’m not doing that."
    s "Yumi, you have to trust me on this."
    y "I really don’t. That’s a horrible plan."

    scene yuminotebook12
    with dissolve

    y "I’ll just fuckin’ figure something else out. You’re clearly just trying to sabotage me again for the sole purpose of getting to spend more time with me or some shit."
    y "In fact, I doubt you want me to get a job at all. You’re just trying to add me to your gross-ass harem and this is your idea of the...easiest way to do that. "

    scene yuminotebook11
    with dissolve

    y "But get this, douchebag. Each time I fuck up an interview, I come one step closer to nailing the next one. "
    y "Pretty soon, you won’t have a reason to see me anymore. "
    s "And I’ll have some extra cash as well since I won’t be buying you lunch every weekend. "
    y "Exactly. It’s a win-win situation. "

    scene yuminotebook13
    with dissolve

    y "So how about you do us both a favor and just...get out of here."
    y "I need to figure out a way to handle this that doesn’t make me look like a complete fucking moron."
    s "Sure, Yumi. But I really think you should at least consider-"

    scene yuminotebook2
    with hpunch

    y "I SAID GET THE FUCK OUT!"

    scene black
    with dissolve2

    "Okay, so it looks like Yumi isn’t going to take my noodle suggestion."
    "Joke's on her, though. "
    "I know Tsuneyo, and I know what she wants to hear."
    "And I’m not sure if someone with Yumi’s narrow-mindedness will be able to figure that out in such a short period of time."
    "But, either way-"
    "I still feel like we got somewhere tonight."
    "Even if I’m walking home significantly earlier than I planned."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ yumidorm20 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumidorm25:
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
    if yumi_love >= 10 and yumidorm5 == True and yumidorm10 == False:
        jump yumidorm10
    elif yumi_love >= 5 and streets10 == False:
        play sound "knock.mp3"

        s "Hey Yumi, are you in there?"
        "..."
        "There's no answer."
        jump doorknock
    if yumi_love >= 15 and yumidorm10 == True and cafe20 == True and yumidorm15 == False:
        jump yumidorm15
    if yumi_love >= 20 and streets20 == True and yumidorm20 == False:
        jump yumidorm20
...
```