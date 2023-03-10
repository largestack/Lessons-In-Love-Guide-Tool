# I See Everything (Nodoka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Nodoka love greater than or equal to 5

* Event [Coloring Book](./nodokalibrary5.md) (Nodoka) is completed)

* Day of week is a weekday

* Day of week is not Monday



## Next events

* [Futaba: C'est La Vie](./futabalust15.md)

## Event properties

* Id: nodokadorm5
* Group: Nodoka
* Triggered by label: nodokadorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->nodokadorm->nodokadorm5

## Official wiki page

[I See Everything](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nodokadorm5&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label nodokadorm5:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm2

    play sound "knock.mp3"

    "I knock on Nodoka’s dorm and wait for her to answer."

    o "Heeeeeey! Uhh...come in?"

    "Otoha answers instead."
    "Oh well. Close enough."

    s "Why does that invitation sound so skeptical?"
    o "Well, uhh...it’s kind of hard to explain."
    o "Nodoka, I’m inviting Sensei in. Is that okay?"
    no "Huh? What? Yeah? Yeah. Yeah that’s fine. Okay."
    o "The uhh...door is open, Sensei."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I open the door with a bit more caution than normal because I’m kind of used to either being invited in or {i}not{/i} being invited in and entering anyway."
    "It’s very rarely a gray area between those two things."
    "But I suppose there are plenty of gray areas surrounding Nodoka if her talk about colors in the halls the other day says anything about the type of person she is."

    scene nodokanodokanodoka1
    with dissolve

    o "Yo..."
    no "{size=-15}It’s wrong. It’s so wrong. Wrong wrong wrong wrong wrong wrong wrong wrong wrong wrong.{/size}"
    s "Uhh..."
    o "Don’t mind her. She’s just...doing a thing."
    o "And, uhh...sorry to be the bearer of bad news, but I’m actually on my way to visit my parents so..."
    o "Either leave now or figure out how to deal with an over caffeinated and barely attentive Nodoka."

    scene nodokanodokanodoka2
    with hpunch
    play sound "thump.mp3"

    no "{size=+15}{b}FUCK!!!{/b}{/size}"
    o "Jesus, calm down. You’re going to break your desk."
    s "Is this how Nodoka writes? Or...reads? "
    s "What is she even doing right now?"
    o "No clue but...you know what they say about geniuses."
    s "Do I? Because that definitely doesn’t ring any bells."

    scene nodokanodokanodoka3
    with dissolve

    o "Well...uhh..."
    o "Okay, see ya."
    s "What? Just like that? "
    o "Yeah, my parents are literally outside waiting to pick me up."
    s "Don’t you have any tips or anything?"
    o "There are no tips on handling Nodoka. You just...do stuff and hope she goes along with it?"
    s "Well that helps a ton. Thanks, Otoha. "
    o "I’m sorry, okay? But I really have to go."

    scene nodokanodokanodoka4
    with dissolve

    o "Nodoka? I’m heading out. I’ll be back later."
    s "…"
    o "Nodoka?"
    no "Huh? What? Yeah. Okay. Bye. See ya. "

    scene nodokanodokanodoka1
    with dissolve

    o "Umm...good luck?"

    scene nodokanodokanodoka5
    with dissolve
    play sound "dooropen.mp3"
    stop music fadeout 10.0

    "Otoha, who already had her shoes on and bag next to the door, slips past me and exits the room, leaving me alone with someone who I’m not even sure knows I’m here right now."

    s "Hey. Earth to Nodoka. "
    s "You feeling okay?"
    no "{size=-15}Everything is wrong.{/size}"
    no "{size=-15}This isn’t how anyone with even a shard left of sanity within them would word this.{/size}"
    no "IT DOESN'T MAKE SENSE!"
    no "IT IS INCOMPLETE!"
    no "THAT IS THE ONLY EXPLANATION!"
    s "Nodoka?"

    play sound "static.mp3"
    scene ayhh6 with flash
    scene nodokanodokanodoka6 with flash
    stop sound
    play music "amiawake.mp3"

    no "{size=-10}Hello{/size} Hello {size=+10}Hello!{/size}"
    no "What brings you here today, Sensei?"
    s "Woah."
    s "What dimension did you wake up in?"
    no "I beg your pardon? I woke up in the same dimension as always."
    no "Is there anything I can get for you? Coffee? Tea? Coffee?"
    s "You said coffee twice."
    no "Coffee it is! Stay right there! I’ll run down the hall and make you some! You won’t even realize I’m gone!"
    s "I don’t need anything right now, Nodoka. Is everything okay?"
    no "Hm? Yeah. Yeah everything is fine. Just a little tired, you know?"
    no "Sometimes you see so many words that all the words start blending together and then before you know it you’re reading the same word over and over and over and over again."
    no "Is there anything I can get for you, Sensei? Coffee? Tea? Coffee?"
    s "I...think you might need to slow down a bit."

    scene nodokanodokanodoka7
    with dissolve

    no "No! Going slow will only slow me down! I’ve gotta go fast if I wanna speed up!"

    if bonus == True:
        no "Teach me about sex!"
        s "I’m sorry, what?"
        no "Sex! What does the penis feel like when it’s inserted into a woman?!"
        no "I keep needing to guess and don’t want to appear amateurish to male readers!"
        no "I must appeal to everyone! Anyone and everyone! Everyone and some people! But only if some people means all people! All people!"
        no "Teach me!"
    else:
        no "How many sticks of gum can you fit in your mouth?!"
        s "I’m sorry, what?"
        no "Gum! The chewy stuff! How much of it can you chew?!"

    s "How much coffee have you had exactly?"

    scene nodokanodokanodoka8
    with dissolve

    no "Coffee? Do you want coffee? I can make you coffee. I make really good coffee."
    s "…"
    s "Okay, how many fingers am I holding up right now?"

    "I hold my hand in front of Nodoka, flashing two fingers in front of her to find out if she can even see straight."
    "She doesn’t have her glasses on and her pupils are like three sizes smaller than usual, so-"

    no "Fingers!"
    s "Yes. Good. How many?"

    if bonus == True:
        no "The more, the better! Shove your whole fist in there!"
    else:
        no "All of them!"

    s "Okay, I’m calling an ambulance."
    no "Two! Don’t call an ambulance! I’m good! Really good! Super good! So good!"
    s "Are you sure?..."

    scene nodokanodokanodoka9
    with dissolve

    no "Hah..."
    no "Yeah. Yeah, I’m fine."
    no "Just...got a little riled up there for a second. Apologies if that made you uncomfortable."

    scene nodokanodokanodoka10
    with dissolve

    no "I’m ready for a normal conversation now."
    s "You definitely don’t look like you’re ready for a normal conversation."
    no "Are my eyes doing the thing again? Have the dreaded bags returned?"
    no "Have my pupils shrunk to the size of dried, aged plums?"
    s "All of the above, actually. Is this a thing that happens often?"
    no "Extremely. Though, I’m typically good at not letting people see it."
    no "I appear to have reached a point in life where this is no longer doable, though."
    no "Just one of the cons of having a roommate, I suppose."

    if bonus == True:
        no "But I get to see her in her underwear every day, so it’s totally worth looking a little unkempt from time to time."

    s "Well...as long as you’re feeling okay, I guess."
    no "Never better."
    no "Hey, do you want to go for a walk or something? Maybe somewhere far away? Like far far far far away?"
    s "Are you...trying to escape someone? Or something?"
    no "Not particularly. I just get the urge to get out sometimes, you know?"
    s "I guess."
    s "I don’t really think we should go anywhere with you looking like that, though."
    s "I doubt I’d be able to keep up with you at this rate either."

    if bonus == True:
        no "Let’s go to that sex shop you’re banned from and buy a leash for you to pull me around on!"
        no "I’d never be able to escape that way! And even if I did, I’d come running home eventually because this is where all my stuff is!"
    else:
        no "Let’s go to the local DVD store and rent Napoleon Dynamite!"
        s "This has officially gone too far."

    scene nodokanodokanodoka8
    with dissolve

    no "Hey. Do you want to write a story together? That sounds fun, right?!"
    no "Oh, shit! Have you ever done mad libs?! Let’s do that! That’ll help get the energy out! Right?"

    "Well, at least I understand why Otoha got the hell out of here as fast as she could."
    "This is already starting to get exhausting and I’ve only been here for a few minutes."

    no "Senseiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii? Let’s play a gaaaaaaaaaaaaaaaaaaaaaaaaame."
    no "Come onnnnnnnnnnnn. Play with meeeeeeeeeeeeee."
    s "What happened to having a normal conversation, Nodoka?"

    scene nodokanodokanodoka12
    with dissolve

    no "Ahh, yes. Silly me. I did say I was going to do that, didn’t I?"
    no "Woah, weird. What’s this?"
    no "Sensei, do you ever see weird stuff when you close your eyes?"
    s "When I close my eyes? Not really."
    s "Unless you’re talking about dreaming."
    no "I guess it’s like a dream but also kind of not like a dream. But still a dream at the same time. You get it?"
    s "Nope."
    s "Are you seeing something right now?"
    no "…"
    s "…"
    s "Nodoka?"

    scene nodokanodokanodoka13
    with dissolve

    no "Nope!"

    if bonus == True:
        no "All I see is my hot teacher standing there gawking at me."
        no "I’m starting to feel a little self-conscious, actually. I don’t think I’m very pretty without my glasses on."
        s "I think you’d be adorable if your eyes were the right size."
        no "That’s very sweet of you. Take six hundred Nodoka points."
        s "Woah. Are you sure? I don’t think you meant to give me that much."
        no "Do you want me to take some away? Cause that just brought you way closer to tongue wrestling me before the end of the[school] year."
        s "I will gladly hang on to them for now."
    else:
        no "All I see is the color of the air!"

    s "It would be nice if you’d go back to normal, though. This is slightly uncomfortable for me."
    no "Comfort? Is comfort an issue?"
    no "Come with me! I know just the place!"

    scene black
    with dissolve

    "Nodoka swipes a notebook off of her table and runs over to her bed, jumping onto it and landing on her stomach."
    "Her long hair falls to her sides as she props her feet up in the air and waves me over."

    if bonus == True:
        "I decide to sit at the foot of the bed instead of on it because..."
        "Well, because I’m not feeling immoral tonight for some reason."
    else:
        "I decide to sit at the foot of the bed because I am a good guy and only view Nodoka as a student."

    scene nodokanodokanodoka14
    with dissolve

    no "Is this better? Are you comfortable now?"
    no "Wait, how are you supposed to be comfortable if you’re there on the floor?"

    if bonus == True:
        no "Come cuddle and do mad libs with me."
        no "We can’t tell Futaba until you open up about your openness, though, or my chances of playing with her boobs get way lower than I want them to be."
        s "I should probably stay right here for now."
        no "Is this one of those unclear consent situations? Because I’m sure I don’t look it, but I’m perfectly competent right now."
    else:
        s "The feeling of the wood against my legs makes me feel all tingly and comfortable."
        no "Wood!"
        s "I wanna play a trivia game. Do you like trivia?"

    no "Go on. Ask me anything you can think of. I’ll give you the right answer."
    no "I’m a prodigy, remember? A genius. I’m the smartest person you know. I see everything. I hear everything."
    no "Everything’s coming up Nodoka!"
    s "If you’re so smart, what’s the square root of 23?"
    no "4.7958. Next question."
    s "What were Thoreau’s last words?"
    no "Moose! Indian!"
    no "I don’t even like Thoreau and I know that."
    no "Isn’t that more of a trivia question than an actual question, though?"
    s "Uhh...when did Toyotomi Hideyoshi die?"
    no "September of 1598 but the Council of Five Elders didn’t inform the army until a month later when they were told to withdraw."
    s "And those five elders were?"
    no "Ieyasu, Hideie, Toshiie, Kagekatsu, and Terumoto."
    no "Also want to give a shout-out to my boy Kobayakawa Takakage as the VIP sixth member that nobody ever wants to talk about."
    s "And the electron configuration for Germanium?"
    no "[[Ar] 3d¹⁰ 4s² 4p²"
    s "What the fuck are you?"
    no "That one was actually kind of tough because I almost gave you the configuration for tin, which is [[Kr] 4d¹⁰ 5s² 5p²."

    if bonus == True:
        s "I can’t help but feel like your omniscience is being wasted on sex writing."

        scene nodokanodokanodoka15
        with dissolve

        no "Hehe~ Maybe when electron configurations and dead Japanese dudes can start giving people orgasms, I’ll be a little more interested in them."
    else:
        s "See? You're not so smart after all if you're almost making mistakes like that."

    scene nodokanodokanodoka16
    with dissolve

    no "Hey, how come you’re able to come up with questions like that off the top of your head but never want to teach anyone in class?"
    s "Eh. I guess I’m the same as you in a roundabout sort of way."
    no "I wouldn’t call it roundabout. We’re both smart people who prefer to talk about not smart stuff. Done."
    s "You are significantly smarter than me, so that comparison isn’t really fair to you."
    no "I mean, you knew all the answers to those questions too, didn’t you?"
    s "Definitely not the Germanium one. You could have said literally anything there and I would have believed you."

    scene nodokanodokanodoka17
    with dissolve

    no "You cheeky little bastard, you."

    if bonus == True:
        no "Also, would you mind explaining to me why we’re not cuddling yet?"
        no "I wouldn’t have playfully hopped onto my bed if I didn’t expect you to follow suit, Sensei."
        no "And I’ve more than proved how competent I am right now, haven’t I?"
    else:
        s "Nodoka. I would like to formally ask you for a favor."

    no "What more do you want from me?"
    s "A good night’s rest maybe? You look kind of insane right now."

    scene nodokanodokanodoka18
    with dissolve

    no "Insane?..."
    no "I’m sure it’s not that bad."
    s "When was the last time you looked in a mirror?"
    no "Two days ago? Three days ago? Four? Five? Six? Seven? Eight?"
    no "I don't like mirrors very much."
    s "And the last time you slept was?..."
    no "I don’t know. I haven’t been keeping track."
    no "I get tunnel vision and lose sight of things like that rather often."
    no "I was also particularly bothered by the way the air conditioner in this room sounds, so I had to get up to punch it on several occasions throughout the night."
    no "It's so high up, though. I nearly fell off of my chair and cracked my head open."
    no "Then there was also the matter of the tag on my pajama pants bothering me, so I needed to deal with that."
    no "But neither Otoha nor I had a pair of scissors so I needed to go acquire some and-"
    s "You know, maybe it would be best if you just went on a trip to the bathroom and took a look at yourself."

    scene nodokanodokanodoka19
    with dissolve

    no "Well...if you insist."
    no "But I can’t imagine it’s nearly as bad as you’re making it out to be."

    scene black
    with dissolve

    "Nodoka hops off of the bed, leaving her notebook behind as she heads to the bathroom."
    "In the time it takes her to do that, I succumb to the desire to invade her privacy and peer into the pages I’ve been watching her absentmindedly scribble into."
    "There are no words."
    "Just childish drawings of what looks like a house."
    "………"
    "……"
    play sound "dooropen.mp3"
    "…"

    scene nodokanodokanodoka20
    with dissolve

    no "…"
    s "I take it your trip went well?"
    no "I look like I crawled out of a well."
    no "I honestly have no idea how you’ve been able to look at me for as long as you have."
    s "I think you’re cute. Just...cuter when you don’t look like a monster."

    if bonus == True:
        no "I’d probably have sex with a monster under the right conditions."
    else:
        no "Some monsters are cute. Like Cthulu."

    s "What?"

    scene nodokanodokanodoka21
    with dissolve

    no "Just think of...all of the tentacles and..."
    s "..."
    no "..."
    no "Thank you for stopping by, Sensei."
    s "Are you feeling a little...calmer now?"
    no "Oh, not at all. I’ll probably go tonight without sleep as well."
    no "But there {i}is{/i} some solace in knowing that there’s someone else out there who can see beauty in horrible things."

    scene nodokanodokanodoka22
    with dissolve

    if bonus == True:
        no "So...if you’ll have me...I’ll be happy to continue being the girl you can flirt with in public that no one will get mad at you for since I do the same thing with everyone else."
        no "It’ll just mean a little more than normal with you than it does with them."
        no "And the tiny girl with the black hair in the back of the classroom."
        no "If you can get her to sign up for a threesome, I’d be more than happy to give you my-"
        s "Stop dragging Sana into your sexual fantasies and appreciate her for the timid angel she is."
        no "Timid angel by day. Closet nympho by night. I’m calling it now."
        s "I don’t know if you being right will upset me or elate me...but I’ll take you up on that bet."
        no "Winner has to do anything the other person says?"
        s "I feel like we both win if that’s the reward."
        no "Oh yeah? But you haven’t even heard what I’m going to make you do yet."
        s "You haven’t heard my plan either."
        no "I just admitted to wanting to have sex with a monster. I’m pretty sure I could handle whatever you throw at me."
        s "...Yeah, you probably can."
        s "Here’s hoping this bet doesn’t take the next...forever to resolve."
    else:
        s "The only beauty I see is in gardening."

    scene nodokanodokanodoka23
    with dissolve

    no "Want me to plant a seed for you?"
    s "What kind of seed?"

    if bonus == True:
        no "Maybe just warm her up a little so you can swoop in for the kill?"
        s "Please don’t do anything to her..."
        no "Fine. I’ll just stick with my dear, sweet Miss Watabe instead."
        s "Yeah. You do that, Nodoka. It’s going very well."
        no "God I want to be that skirt."
    else:
        no "Idunno. Some kind of flower maybe?"

    scene nodokanodokanodoka24
    with hpunch

    no "AH! YES! I FIGURED IT OUT!"
    s "Figured what-"

    scene nodokanodokanodoka25
    with dissolve

    no "YOU HAVE TO GO! LEAVE!"
    no "I MUST FOCUS!"
    s "…"
    s "Well, okay then."
    s "Goodnight, Nodoka."

    no "{size=-15}I see it...{/size}"
    no "{size=-15}I see everything...{/size}"

    scene black
    with dissolve

    "I exit the dorm room and make my way down the stairs, somehow knowing less about Nodoka than I did before visiting."
    "I doubt I’ll ever get to a point where I know exactly what’s going through her head, but-"
    "Well, at least it seems like an interesting place."

    if bonus == True:
        "Self-destructive, terrifying, and mildly arousing as well..."
    else:
        "Self-destructive, terrifying, and really fucking weird."

    "But certainly interesting."
    "I’m both jealous and afraid of how much time she gets to spend there."

    $ renpy.end_replay()
    $ nodoka_love += 1
    $ nodokadorm5 = True
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohadorm5:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label nodokadorm:
    if nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True and day != 1 and day != 5 and nodokadorm1 == False:
        jump nodokadorm1
    if nodoka_love >= 5 and nodokalibrary5 == True and day < 6 and day != 1 and nodokadorm5 == False:
        jump nodokadorm5
...
```