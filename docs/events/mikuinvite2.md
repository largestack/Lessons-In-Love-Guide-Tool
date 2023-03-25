# Fair is Fair (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Breakaway](./mikuinvite1.md) (Miku) is completed)



## Next events

None

## Event properties

* Id: mikuinvite2
* Group: Miku
* Triggered by label: mikuinvite

## Official wiki page

[Fair is Fair](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikuinvite2&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label mikuinvite2:
    play sound "phonebeep.wav"

    "I tap on Miku’s name in my phone and wait for her to answer."
    "And if there is any justice in this world, I will soon find out that she is alone and capable of coming over without the sentient purity ring that is Makoto Miyamura wrapped around her finger."
    "Unless Makoto has flipped stances in regard to her feelings on threesomes overnight. If that is the case, I will gladly welcome the two of them once again."
    "The thing is, the chemistry brewing between Miku and me is still a little volatile. It’s new and different...and so I can’t be condemned for my desire to experiment a little more."
    "And experimentation is never fun when it’s being supervised."
    "I am an adult, and if I want to prey upon the naiveté of a young girl in the comfort of my own home, I should be allowed to- actually, no. Makoto is right."
    "But that changes nothing because Makoto is almost always right and I’ve dodged most major consequences thus far. Further debauchery will not slow me down."

    play sound "phonebeep.wav"

    mi "Heeeeeeeeeeeeeey..."
    s "That’s a weird way to say hello."
    mi "Too many e’s?"
    s "A few. What are you doing right now?"
    mi "Uhh..."
    mi "Would it be weird to say I’ve been waiting for you to invite me over?"
    s "As in...you’re just sitting in your dorm room and waiting for me to give you the go ahead to come to my house?"
    mi "I was also watchin’ TV and stuff, but yeah. "
    s "That is kind of weird, I won’t lie."
    mi "Well I’m kinda...you know. And Makoto’s at work right now, so..."
    s "You realize you can call me as well, right? You don’t have to wait for me to give you the signal if there is sex involved."
    mi "Ain’t that...exactly {i}when{/i} I’m supposed to wait for the signal? Don’t think it’s safe to just show up at your door and ask you to take my skirt off."
    s "It is. Just make sure Ami’s not home."
    mi "You’re playin’ a dangerous game, Sensei. I might wind up movin’ in if you go and tell me stuff like that."
    s "I take it that means you’re coming over?"
    mi "Heh. Coming."
    s "Okay, if you really {i}are{/i} turning into Maki, you should try and suppress it so we can keep Makoto alive."
    mi "The only thing {i}I’ll{/i} be suppressing is your giant boner."
    s "I don’t think you understand what the meaning of “suppressing” is."
    mi "Yeah, there’s a lot I don’t understand. But what I {i}do{/i} understand is that I’m feelin’ some kinda way and you’re the only person who knows how to do anything about it!"
    s "I guess I’ll...see you soon then. "
    mi "I guess you will..."

    scene black
    with dissolve2
    stop music fadeout 5.0
    play sound "phonebeep.wav"

    "I hang up the phone and marvel at the fact that Miku has gone from a girl with almost no sexual feelings whatsoever to one who sits around her dorm room and waits for me to invite her over."
    "I guess that’s just the process for these girls, though. "
    "And while I can paraphrase that to make it sound like I’m just helping them {i}learn more about themselves{/i} or whatever way you want to spin it that could justify what’s about to happen...I won’t."
    "Right now, a high school freshman is on her way to my house because I am going to do things to her. And {i}she{/i} is going to do things to me."
    "This is happening because I let it."
    "And there is no way you can word it that makes it okay."
    "Please."
    "Stop watching me."

    play sound "static.mp3"
    scene 1 with flash
    scene 5 with flash
    scene mikuhjinv1 with flash
    stop sound
    play sound "dooropen.mp3"
    play music "asobeatsex2.mp3"

    mi "Heeeeeeeeeey..."
    s "Too many e’s again."
    mi "Sorry if I took a little longer than you expected. I wanted to run but I didn’t wanna get all sweaty if we were gonna...you know. "
    s "You know, I’ve turned a lot of girls on during my time here in Kumon-mi, but I think this might be the first time any of them have thought about literally running to me because of it."

    scene mikuhjinv2
    with dissolve

    mi "Something something...new Miku...something?"
    s "You have such a way with words sometimes."
    mi "And you’ve got such a way with...your...fingers?..."
    s "..."
    mi "Can you do the thing again?"
    s "You literally just got here. We’re not even in the bedroom yet."

    scene mikuhjinv3
    with dissolve

    mi "We’re doing it in the bedroom?!"
    s "Did you expect me to finger you on my kitchen table?"

    scene mikuhjinv4
    with dissolve

    mi "I...wouldn’t be against it."
    s "Is there something wrong with my bedroom, Miku?"
    mi "No! It’s just...you know. It feels more serious that way. And I still ain’t ready to, like...go all the way just yet. So I didn’t wanna make it feel like that’s what I was bankin’ on."
    s "So you’re horny enough to almost run to my house to get fingered, but not horny enough to have sex with me?"

    scene mikuhjinv5
    with dissolve

    mi "I don’t think the horny part’s the problem. The problem’s that I’m half your size and kinda sensitive down there. I ain’t really interested in gettin’ split in half just yet."
    s "That’s fine. I won’t rush you if that’s what you’re worried about. It’d be nice to have {i}something{/i} done for me eventually, though."
    mi "Like what?"
    mi "You want me to try puttin’ my fingers inside of you next?"
    s "Don’t even joke about that."
    mi "I ain’t jokin’. I’ve heard Maki say that kinda thing’s totally normal."
    s "That is not the scene I want to happen right now."
    mi "Well, what {i}do{/i} you want? Cause I might be horny as heck, but I still know that fair is fair and I’m the only one who’s gotten some so far."

    if kirinlust30 == True:
        "Well, that’s not {i}entirely{/i} true given what happened in my hotel room last Halloween, but...thankfully, it doesn’t seem like Miku remembers that."

    s "Do you want to talk more about that in my bedroom?"

    scene mikuhjinv6
    with dissolve

    mi "You and that heckin’ bedroom, man. Whaddya got against the kitchen table?"
    s "For starters, the fact that I eat off of it."
    mi "And I eat off of my bed but ya don’t see me makin’ ya finger me on the floor."
    s "Why are you eating off of your bed?"
    mi "It just happens sometimes, okay? But I ain’t here to talk about food- I’m here to do sexy stuff with my teacher. And if that kinda stuff {i}has{/i} to happen in your room, then...fine."
    mi "But I really ain’t ready to go all the way yet. For real. I need more...practice first."

    scene black
    with dissolve2

    s "I’m sure we can figure something out..."

    "........."
    "......"
    "..."

    scene mikuhjinv7
    with dissolve2

    "Miku entangles her arm with mine and I wind up walking her into my room like I’m some sort of escort. Or...{i}she’s{/i} some kind of escort. "
    "I don’t know. I’ve never needed to resort to that before. But I’m sure this is how things would look if one of us was an escort."
    "Despite her clear nervousness, she puts on a smile — likely because she still thinks she’s about to be fingered until my bedsheets are a soaking mess. But that is not the case."
    "Or...at least it’s not the case {i}yet.{/i} "
    "We’ll get there later, I’m sure. But for now, I really would like to capitalize on her ability to recognize when {i}fair is fair.{/i}"

    s "So..."
    mi "Soooo..."
    s "You ready to try something a little different?"

    scene mikuhjinv8
    with dissolve

    mi "Mhm..."
    mi "You’ll take it easy on me, right? I obviously wanna do somethin’ for {i}you{/i} when you’ve helped me a bunch of times, but I still ain’t really sure what’s goin’ on just yet."
    s "Thankfully, we’re in a good environment for me to teach you."

    scene mikuhjinv9
    with dissolve

    mi "Teach?! Was this just a trap all along?! Did Makoto put you up to this?!"
    s "Wow. You don’t even understand context, do you?"

    scene mikuhjinv10
    with dissolve

    mi "Oh. You mean {i}sex-{/i}teach. My bad. My brain sucks even more when I’m nervous and it gets harder for me to understand stuff right away."
    mi "But yes. Please teach me. I can’t promise I’ll be any good at what you want, but I’ll do my best."
    s "Good. Because there’s a reward in store for you when you succeed."
    mi "Thank friggin’ God because I’ve been tryin’ to do it myself all day and it just ain’t the same."
    mi "So, what’s on the menu? What can your old pal Miku do for ya this fine evening?"
    s "You can start by not referring to yourself as my “old pal” right before we make sexual contact."
    mi "Are we not friends anymore? I ain’t your girlfriend, am I?"
    s "That’s not what I- you know what? Forget it. Kneel down by the foot of the bed. "
    mi "Should I take my clothes off? "
    s "Stay the way you are now, actually..."
    s "I like that dress."
    s "I want to ruin it."

    scene mikuhjinv11
    with dissolve

    mi "Whaaat? No! I like this dress. It’s the only thing that makes me feel girly."
    s "That’s precisely why I want you to keep it on. "
    s "You’re cute dressed like that. Well, you’re cute always. But there’s something particularly alluring about the prospect of you sucking me off while you’re dressed that way."

    scene mikuhjinv12
    with dissolve

    mi "...Okay."
    mi "Just...remember. Take it easy on me, please. "
    mi "I’m still really nervous..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mikuhjinv13
    with dissolve2

    "Miku crouches down at the foot of the bed like I asked and waits patiently as I get into position in front of her."
    "I gesture her to slide forward, gently grabbing the back of her head and angling her closer to my dick, hoping she’ll take the initiative required to remove it from the fleeting residence that is my pants."
    "Instead of doing anything, however, she simply looks up at me with a sense of...childish innocence in her eyes that does nothing but make me want to paint her face white with my seed."
    "Keep looking at me like that."
    "Your purity gets me harder than anything."

    mi "So...do I take it out? Or do you do it? I ain’t all that familiar with blowjob etiquette."
    s "You can do it. I want to pay close attention to how you look after seeing it for the first time."

    if kirinlust30 == True:
        "“First” being a word I use lightly as, again...Valium."

    mi "Yeah...I guess I {i}haven’t{/i} seen it yet, have I? Closest I came was that one Halloween that landed the two of us in hot water."
    s "Do you still have that costume?"

    scene mikuhjinv14
    with dissolve

    mi "Why do you ask?..."
    s "You might suck at context, but I’m pretty sure that even you can understand that."
    mi "Remind me to bring it the next time I come over..."
    mi "But, for now..."

    play sound "zipper.mp3"
    scene mikuhjinv15
    with dissolve

    mi "Hoooooooly shit, it looks even bigger than it felt. And it felt like I was ridin’ a fallen redwood. "
    s "Your fear about being split in half is perfectly reasonable and I will not hold that against you."
    mi "Sensei, this is bigger than my head. How do you even stay conscious when this thing gets hard?"
    s "Probably willpower."
    mi "How the utter heck did Makoto and Kirin ever get this thing inside them? They ain’t even that much bigger than me."
    s "What? Since when do you know about Kirin?"

    scene mikuhjinv16
    with dissolve

    mi "I haven’t known for long. She told me during beachmas."
    s "{i}Why{/i} did she tell you during “beachmas?”"
    mi "Because...I may have accidentally spilled the beans that you finger me sometimes?"
    s "Miku-"

    scene mikuhjinv17
    with dissolve

    mi "I’ll be more careful in the future, I swear! I was just excited to talk about it since I like you so much!"
    s "Ugh, great. I obviously can’t stay mad when you go and say things like that."

    scene mikuhjinv18
    with dissolve

    mi "I totally get it, Sensei. All the worries in the world start goin’ away the second you get to spend time with somebody like this, right?"
    mi "And it only gets better once they start touchin’ you."
    mi "Feels kinda like the world is gettin’ flipped on its head, doesn’t it?"
    mi "And even if I ain’t ready to go as far as Makoto and Kirin did, I still wanna help you feel good after all the times you helped {i}me.{/i}"
    mi "Just...maybe don’t compare me to either of them until I have a little more experience, okay? "
    s "You’ll need a lot of practice...they have a pretty big lead, you know."

    scene mikuhjinv19
    with dissolve

    mi "Oh, we can practice whenever you want..."
    mi "Itadakimasu."

    scene mikuhjinv20
    with dissolve

    mi "Mm......mnch........mn~"

    "Miku drags the tip of her tongue across the head of my cock, stimulating the most sensitive area on my body with a surprising amount of delicacy and care."
    "Given the type of person she is, I figured she’d approach this a little more...relentlessly. But she starts off extremely slow and sensual and...honestly, it’s insanely hot."

    mi "Hmn...mmngh......hmnm..."

    scene mikuhjinv21
    with dissolve

    mi "Mngh...mm...am I doing okay so far?...Are you close to finishing?..."
    s "We’ve only been doing this for like five seconds."
    mi "That’s all it takes for me sometimes. I don’t know how penises work. This is my first time ever handling one."
    s "It’ll take a little while longer. Bear with me, please."

    scene mikuhjinv22
    with dissolve

    mi "Don’t say stuff like “Bear with me, please.” It makes it sound like I’m just putting up with this because I {i}have{/i} to, not because I {i}want{/i} to."
    mi "I like this part of you, Sensei...I want to make it feel good."

    "Miku...begins rubbing her cheek against my cock?"
    "She’s like a cat brushing up against its owner to try and coax it into petting her and, while that might not {i}sound{/i} very sexual, it’s that exact brand of innocence that drives me insane at times."

    mi "It’s really warm...is it always like that?"
    s "Your face is just as warm, I’m sure..."

    scene mikuhjinv23
    with dissolve

    mi "Sensei...can I tell you a secret?"
    s "Now?"
    mi "It’s not a random one. It’s related to what we’re doing."
    s "Sure...Go ahead."
    mi "It kind of...{i}excites{/i} me...how this has been in some of my friends."
    s "It...does? I feel like most people would have the opposite reaction to information like that."

    scene mikuhjinv24
    with dissolve

    mi "Amf...guess I’m just...special?..."
    s "Do you...like girls as well or something?"
    mi "Mmf...mm...no...it’s not that..."
    mi "It just...mmf...feels kinda like I’m...amf...winning right now..."
    mi "It’s fun...beating out the competition...makes me feel like...mnngh...I’m doing somethin’ right..."
    s "You’re...definitely doing something right. I’ll admit that much."

    scene mikuhjinv25
    with dissolve

    mi "Yeah?..."
    mi "You like it when I lick you like this?..."
    mi "You don’t mind me goin' really slow?..."
    s "You can do whatever you want so long as you keep looking like that..."
    mi "Like what?..."
    s "I don’t know...adorable?..."

    scene mikuhjinv24
    with dissolve

    mi "Girly?..."
    s "That too..."
    mi "Mmf...mmm...is it just...the dress making you say that?..."
    s "It’s a lot of things...but, for one, I didn’t imagine you’d be this delicate."
    mi "And I...amf...didn’t imagine your wiener would be the size of my head..."
    mi "I’ve gotta move like this or I’ll wind up suffocatin’."
    s "Can I make a request? Please don’t call it a “wiener” when we’re doing things like this?"

    scene mikuhjinv25
    with dissolve

    mi "Roger..."
    mi "Your “not old pal” Miku will take real good care of your huge cock...don’t you worry..."
    s "That’s no better than just saying “old pal...”"
    mi "Champion of Justice and Soccer, Miku Maruyama, will take good care of your huge cock...don’t you worry..."
    s "Maybe...less talking in general would be-"

    scene mikuhjinv26
    with dissolve

    mi "Chu~"
    mi "Chu....chu.....chu..."

    "Miku gives up on licking me for a moment and begins to shower me in soft kisses, each lasting no more than half a second. "
    "And despite these motions not being all that conventional in terms of bringing me to climax given that she’s no longer stroking me as well, I shouldn’t be feeling even {i}half{/i} as good as I actually am right now."
    "Yet...each time her lips connect with my cock, I feel like I’m holding myself back from pulling her forward and cumming down the back of her throat."

    scene mikuhjinv27
    with dissolve

    mi "Chu.....chu......you look really cute right now..."
    s "Me? You’re the one who looks cute..."
    mi "Mm-mm...you look cute too..."
    mi "Can I tell you another secret?"
    s "Only if it’s as good as the last one..."
    mi "I’m not wearing underwear today......chu~"
    s "So you’re an exhibitionist now?"
    mi "Chu.......a what?"
    s "Don’t worry about it. Just keep doing what you’re doing."
    mi "Can I tell you one more?..."
    s "..."
    mi "I can’t wait until you finger me...I’m kind of in Hell right now.......chu~"
    s "Yeah, well...you won’t be there for much longer at this rate..."

    scene mikuhjinv28
    with dissolve

    mi "Mmf...mmmngh...this ain’t as...hard as I thought it’d be..."
    mi "Is Miku Maruyama...actually a blowjob champion?..."
    s "Not without actually putting it in your mouth first..."
    mi "I don’t think I even have to...my original gameplan seems to be goin’ pretty well..."
    s "It wouldn’t hurt..."

    scene mikuhjinv29
    with dissolve

    mi "But if it’s in my mouth, I can’t keep kissing you."
    s "Miku..."
    mi "The tip’s the most sensitive part, right? Won’t you still cum if I just continue like this?"
    s "That’s not the-"
    mi "Sensei...can I tell you another secret?"
    s "...Go ahead."

    scene mikuhjinv30
    with dissolve

    mi "Then..."
    mi "I want you to cum on my face..."
    s "Wow. That’s a line I didn’t think I’d ever hear from you."
    mi "I think I’m a slut now."
    s "I don’t think that’s how being a slut works, Miku."
    mi "I don’t know. Kirin’s a slut and the only boy she’s ever done anything with is you."
    s "I don’t think it’s fair to put yourself on the level of Kirin just yet."
    mi "Does she do this too?"

    if kirinlust30 == True:
        "{i}You’ve literally done it together...{/i}"

    s "She might..."
    mi "Is she good?"
    s "Do you want the honest answer or the one that will make you happy?"

    scene mikuhjinv31
    with dissolve

    mi "Aw, man...she’s {i}really{/i} good, isn’t she? "
    s "Probably the best I’ve ever had since honesty seems to be the route you want to go down."
    mi "Darn it. And here I was thinkin’ I could beat her at this too. Gettin’ too cocky on my first time, I guess."

    scene mikuhjinv32
    with dissolve

    mi "Heh. C-"
    s "Don’t do it, Maki. Remember Makoto."
    mi "How good is {i}Makoto{/i} at this stuff? "
    s "Focus less on your friends and more on me. I was about to finish just a few seconds ago and am now beginning to-"

    scene mikuhjinv33
    with dissolve

    mi "Amf...mm...mngh...mnch...hngh...mmm!"
    s "Well, that was easy..."
    mi "The sooner you...finish...the sooner...{i}I{/i} get to feel good...and I...mmf...can’t wait any longer..."
    mi "I’ve been going crazy all day...I want you to play with me...I want you...I want you..."
    s "Look at me..."
    s "And keep saying that..."

    scene mikuhjinv34
    with dissolve

    mi "I want you..."
    mi "I {i}want{/i} you..."
    mi "{i}I want you...{/i}"

    with sexfade
    with sexfade
    scene mikuhjinv35
    with cumflash
    with hpunch

    mi "Mmm!"

    "The steady pace of Miku’s handjob-slash-licking combo meshed with a three word sentence that does {i}not{/i} pain me to hear winds up forcing an aggressive orgasm out of me."

    scene mikuhjinv36
    with dissolve

    "She stares down at my cock as she carefully empties it out, squeezing every last drop onto her face and tongue, clearly unsure of how long this typically goes on for."

    scene mikuhjinv37
    with dissolve

    "Fortunately for her, the duration of the male orgasm is not particularly long and her wish of having me ejaculate on her face is granted just a minute or two after its initial proclamation."
    "There’s no fanfare or immature Miku-esque commentary to accompany it either — just a smug smile from a girl who knows she did a good job."

    scene black
    with dissolve2
    stop music fadeout 10.0

    mi "Senseiiiii..."

    "And a girl who desperately wants me to finger her."

    s "Lie down."
    mi "Do ya have a towel or somethin’? Shouldn’t I wipe my face off first?"
    s "I told you to lie down."
    mi "I get that, but- ahh! What are you doin’?!"

    "I lift Miku up myself and toss her onto the bed."
    "I hike up her skirt."
    "And I finger her so violently that she destroys my mattress. "

    $ renpy.end_replay()
    $ mikuinvite2 = True
    $ miku_lust += 3

    "{i}Miku’s lust has increased to [miku_lust]!{/i}"
    "{i}You can now invite her over whenever you want!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday
...
```

## Code that triggers this event

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label mikuinvite:
    if mikuinvite1 == False:
        jump mikuinvite1
    if mikuinvite1 == True and mikuinvite2 == False:
        jump mikuinvite2
...
```