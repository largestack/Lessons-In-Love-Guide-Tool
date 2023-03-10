# Nothing Was Missing, Except Me (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 20

* Event [Imprinting](./ayanenew1.md) (Ayane) is completed)

* Event [Window of the Waking Mind](./cafe15.md) (Rin) is completed)

* Event [Missing](./day50.md) (Main) is completed)



## Next events

* [Main: Girl-Talk](./day65.md)
* [Main: A Proper Introduction](./day150.md)
* [Yumi: Worse Comes to Worst](./yumidorm15.md)
* [Rin: Delirium](./rindorm20.md)

## Event properties

* Id: cafe20
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe
* Triggered by path: cafe->cafe20

## Official wiki page

[Nothing Was Missing, Except Me](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe20&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe20:
    scene cafetwentyredux
    with dissolve

    s "…"
    r "…"

    "Rin spots me from behind the counter but, instead of calling out to me, she just...turns around."
    "No. She turns around and {i}pretends to start cleaning something.{/i} Which is an obvious sign that she doesn't want to talk to me...but why?"
    "I can't recall doing anything wrong, but I guess it's in my nature to sort of do things like that without realizing."
    "She's one of the last people I'd expect to just avoid me, though."

    s "..."

    "Or maybe it's something that doesn't involve me at all?"

    scene black
    with dissolve2

    "Maybe, in my selfish obsession with all things flowing into me, I just expected it to be."
    "And meanwhile, she's drowning in a different lake."
    "........."
    "......"
    "..."

    scene cafesad1
    with fade
    play music "lastdailysong.mp3" fadein 8.0

    r "{i}Mm...{/i}"
    s "Rin?"
    r "Oh, S-Sensei! Fancy...meeting you here."
    r "How are you doing this morning? Everything good? Have any...cool dreams or something?"
    s "I’m fine."
    s "The real question is how are {i}you?{/i}"
    r "Oh, you know...Pretty good. Can't complain."
    s "I see."

    "Obviously, I know that's not true."
    "It's not like Rin to just...hide away."
    "At the same time, though...what do I even know about her to begin with?"
    "It's not like I've experienced what becomes of her in times of crises before. This could just be par for the course."
    "But, if that's the case, why do I still feel compelled to push further when that is likely the last thing she wants me to do?"

    play sound "static.mp3"
    scene happy9 with flash
    scene cafesad1 with flash
    stop sound

    s "How was your doctor’s appointment the other day?"
    s "I never got a chance to ask you."
    r "Uhh...pretty good, I guess. Blood pressure is fine. BMI is fine. You know the deal."
    s "Good to hear."
    s "Would you mind turning around by any chance? It feels kind of weird talking to the back of your head."
    r "Yeah...about that..."
    r "I actually...kind of {i}would{/i} mind. I don’t look so great today."
    s "I’m not here to judge a beauty pageant."
    r "That's good, because I wouldn't even make it past auditions looking like this."
    s "Just turn around, Rin."
    r "Why do I have to?..."
    s "Because I don't care what you look like right now."

    scene cafesad2
    with dissolve

    r "But that doesn't mean it isn't weird for me..."
    r "I just don’t want you to think anything’s going on or whatever because I know you were already worrying and stuff."
    r "So like, if you want to just order something and leave your money on the counter, that’s-"
    s "Rin. Turn around."
    r "…"
    r "Okay, but if you run away, my feelings will be really hurt."
    s "I won’t run."
    r "…"
    r "Then..."

    play sound "static.mp3"
    scene cafesad3
    with flash
    stop sound

    r "Good morning..."

    "..."
    "She wasn’t kidding when she said she didn’t look good today...It looks like she hasn’t slept in weeks."
    "She’s drenched in sweat and her eyes are swollen so badly that she can't even fully open them."

    s "Good morning, Rin."

    scene cafesad4
    with dissolve

    r "So, uhh...how bad is it?"
    s "It’s, uhh..."
    s "Let’s just say you’ve had better days."

    scene cafesad5
    with dissolve

    r "{i}Mm...{/i}"
    r "I feel fucking gross...I haven’t even showered in like a week."
    s "Are you really okay to be working right now?"

    scene cafesad3
    with dissolve

    r "Yeah, I'm good..."
    r "Besides, I can't let Haruka run the place by herself since the only other girl on the schedule for this morning called out today."

    scene cafesad6
    with dissolve

    r "Oh, and if you could forget you ever saw me like this, that would be nice. Thanks."
    s "I’m not sure if that’s possible."
    s "Are you...really okay?"

    scene cafesad3
    with dissolve

    r "Well, it’s not like you’ve been believing me even when I say yes, so..."
    s "…"

    "The two of us stand there in silence for an uncomfortable amount of time before I feel the need to speak up again."
    "I doubt she'll bite, but I at least need to cast some sort of lure that might tempt her to...go home or..."
    "I don't know. I should probably learn literally anything about fishing before attempting to make fishing analogies."

    s "You should ask to go home. I’ll work the rest of your shift for you if I really have to."

    scene cafesad5
    with dissolve

    r "Sensei...I know you’re worried, but you really don’t have to do that..."
    r "I’ve been through much worse and you don’t even know the drinks...this job isn't something you can just jump into, you know."
    r "You need tons of training and..."
    r "I’ll be okay."
    r "I promise. I just need a few minutes to-"
    s "Stop saying you’re going to be okay when you have no idea if that's true or not."

    scene cafesad7
    with dissolve

    "Rin stops speaking and jolts up in surprise."

    r "Huh?..."
    s "I’m not going to pretend to know how you feel or even...what's going on. But I'm pretty damn sure that forcing yourself to stay out in public isn’t going to help."
    s "Get out of here. Go lay down. Try to get some rest. Do literally anything."
    r "I'm not-"
    s "When was the last time you slept?"
    r "That's..."

    scene cafesad4
    with dissolve

    r "Um...three days ago?"
    r "Four, maybe?..."
    r "A week?"
    s "Why? What’s keeping you awake?"
    r "That’s not exactly easy to answer, Sensei..."
    r "And I don’t really want to talk about it so..."

    scene cafesad3
    with dissolve

    r "If you could like...maybe just give me a little space or something..."
    s "Will that help you?"
    r "Well...it won’t {i}hurt{/i} me..."

    "The sound of hurried footsteps rounding the corner suddenly interrupts our conversation."

    scene cafesad8
    with fade

    h "Rin, please go home...Molly is going to come in and work for you."
    r "Molly? Seriously? There's no way you and Molly can work an opening shift yourselves. That's only slightly better than you working alone."
    h "I'll figure it out. And Rin, if you’re ever not feeling well...please let me know."
    h "I can’t make you work when you’re like this."

    scene cafesad8r
    with dissolve

    r "I can do it, though! Really!"
    r "I just...didn’t have time to do my makeup this morning!"
    h "And you look beautiful even without it. That’s not why I’m sending you home."
    h "I don’t want you to have to worry about helping customers on top of whatever else is going on right now."
    h "So do as your teacher says and go get some rest, okay? "

    "Was...Haruka listening this entire time?"

    h "We’ll talk more about your schedule as soon as you’re feeling better."
    h "Until then, I'm going to have to take you off."

    scene cafesad9
    with dissolve

    r "Ngh-!"

    "Rin clenches her teeth, frustrated by the sudden realization of her weakness not just to her peers, but to herself."
    "Why she wants to keep picking at a wound before it's even had the chance to scab over, I don't know."
    "But watching that won't do any of us good and will only make the healing process that much harder if it's ever given the opportunity to start."
    "Before us lies a girl on the verge of breaking and all we can do is attempt to cushion the blow as she's hurled from the twenty-third story of a building we can't see the top of."
    "I say, as if I made any sort of difference at all."

    scene cafesad10
    with dissolve

    r "I’m sorry, Haruka..."

    scene cafesad11
    with dissolve

    r "I’m sorry, Sensei..."
    r "I'll..."

    scene cafesad11r
    with dissolve

    r "I’ll get better soon! I promise!"

    scene black
    with dissolve2

    "Rin quickly grabs her things from underneath the counter and runs out of the store in the direction of the dorms."
    "I hope she's able to get some sleep once she arrives but, at this point, who's to say if she will?"
    "Haruka lets out a heavy sigh as if the weight of the world has been lifted off of her shoulders before turning her attention to me and displaying an expression halfway between exhausted and distressed."
    "For a moment, it's almost like looking into a mirror."

    scene cafesad12
    with dissolve2

    h "..."
    s "Are you going to be okay with just you and that Molly girl?"
    h "Not a chance in hell...But you saw Rin. I couldn’t just let her stay here in that condition..."
    h "I swear, she can be so...fucking stubborn sometimes...Is she like that in[school] too?"
    s "Not that I’ve seen. She zones out in class a lot but, most of the time, she's extremely energetic."
    h "I see...I take it that she hasn't told you the specifics then either?"
    s "She won’t tell me anything."
    s "All I know is that sometimes she ‘thinks things she shouldn’t.’"

    scene cafesad13
    with dissolve

    h "Don't we all kind of do that from time to time, though?"
    s "Maybe. It's hard to tell exactly what she meant by it since she just sort of stopped talking about it a few seconds later."
    s "I’ll go and check on her soon, though."

    scene cafesad14
    with dissolve

    h "Good...I think she’d like that."
    h "She talks about you a lot, you know?"
    h "Ever since you started coming to the cafe. Now, every time you show up she gets really excited and won't shut up about you for like, an hour afterward."

    "I didn't realize there was even an hour worth of things to say about me?..."

    h "Honestly, I’ve never seen her get that way with anyone before. Not even that blonde girl she has a crush on."
    s "Oh. You know about that too?"

    scene cafesad15
    with dissolve

    h "Of course. I mean, she hasn’t {i}told{/i} me or anything. But it’s not like she’s doing a great job of hiding it."
    s "Yeah, I guess she does get a little panicky whenever something involving Chika comes up."
    h "Ahh, right. Right. Chika was her name. Thanks for reminding me."
    h "I promise that I won’t tease her about it when she’s back to normal."
    s "We can tease her about it together. I’m sure she'll be back to her normal routine in no time at all."

    scene cafesad14
    with dissolve

    h "Yeah...I’m sure we will..."

    "Haruka pauses for a moment."
    "Her eyes scan the room, but not in a way that makes it look like she's searching for customers or tables to be cleaned."
    "It's a way that makes it seem like she's about to do something she doesn't want anyone to know about."

    scene cafesad16
    with dissolve

    h "Hey...so this might sound a little weird or something...but do you think you could maybe let me know whenever you {i}do{/i} check on Rin?"
    h "Just so I can know for sure she's fine."
    s "Why would that sound weird? And sure. I can try. I can’t guarantee I’ll be here every day, though."
    h "Well, yeah. That's the part where it gets kind of weird since...I was going to ask that you take down my number and just...text or call instead."
    s "Sure. I can do that."

    scene cafesad17
    with dissolve

    h "Oh, really?! C-Cool! Yeah...Yeah, that’s totally great."
    h "Let me...uhh...let me get a pen or something. I'll be right back."

    scene cafesad17r
    with dissolve

    "Haruka...seems to forget that physically writing down phone numbers isn't necessary anymore and sets off to find a {i}pen or something.{/i}"
    "She's able to find one without much effort and then proceeds to scribble down her number on the back of a napkin."
    "There’s a slight hesitation between each digit, as if she’s trying to convince herself it’s okay to be doing this."
    "Of course, I think it is."
    "Though I may be immensely biased."

    scene cafesad14
    with dissolve

    h "Okay, here you go."
    h "I’m kind of busy during the day, so....if I don’t answer right away, it’s nothing personal."
    s "Got it. I’ll be sure to let you know if anything happens with Rin."
    s "That aside, do you want me to hang around until Rin's cover gets here?"
    s "Because I told her earlier that I wouldn’t mind helping out a bit if necessary, but I can't guarantee I will be of any {i}actual{/i} help whatsoever."
    h "No, no, no. It’s fine. I’ve worked alone before. I actually think it’s kind of relaxing."

    scene cafesad15
    with dissolve

    h "Just go cheer up my employee already. She needs it."
    s "Works for me."
    s "It was nice talking to you, Haruka."
    h "You too. I look forward to...further communication."
    s "..."

    scene cafesad16
    with dissolve

    h "I'm sorry. I have no idea why I said it like that."
    s "Yeah, that was weird."
    s "Anyway, see you later."
    h "Y-Yeah...Later."

    scene black
    with dissolve2

    "I leave the cafe without ever purchasing a drink."
    "It wouldn't be the same if it wasn't Rin who made it."

    $ renpy.end_replay()
    $ cafe20 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label rincafegone:
    scene cafesad14
    with dissolve
    play music "cafe.mp3" fadein 3.0

    "Rin isn't working today, so I wind up talking to Haruka instead."
    "We make idle chat about a few random things, but wind up spending the bulk of the conversation
    talking about Rin herself."
    "It seems like Haruka might be even more worried about her than I am."
    "I hope everything turns out okay. My mornings just aren't the same without the rush brought on by coffee-roulette."

    scene black
    with dissolve

    "Haruka tells me that she'll let Rin know I dropped by the next time she sees her."
    "I should keep checking back until my normal barista is on her feet again..."

    $ rin_love += 1
    stop music fadeout 3.0

    "{i}Rin later finds out that you stopped by and her affection increases to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe25:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
    if rin_love >= 20 and ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False:
        jump cafe20
...
```