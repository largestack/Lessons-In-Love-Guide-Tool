# Sketchy Basement
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe40&go=Go)



## Event preconditions
✅Rin love greater than or equal to 40

✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)



## Next events
* [Rin: Semantics](./rindorm40.md)

## Event properties
* ID: cafe40
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe

## Event code
File: \game\RinEvents.rpy
Code:
```python
...
label cafe40:
    scene cafeotoha1
    with dissolve
    play music "cafe.mp3"

    "I walk into the cafe first thing in the morning to suddenly remember that I am not the only person of importance in Rin’s life."
    "What a shitty way to start the day."

    if cafe35 == True:
        "Seated with her at the table appears to be the same girl we ran into at the park during her post-rejection blues."
    else:
        "Seated with her at the table is a girl around the same age as her, likely the one who she couldn’t stop talking about during the Christmas party."

    "The real question is whether or not I should leave the two of them alone or try to insert myself into the conversation."
    "I think back to what seems like aeons ago when I ran into a similar situation, but with Chika at the table next to Rin instead of this new girl."
    "Back then, Rin was barely able to hold a conversation on account of how nervous she was."
    "So...if something like that is happening again today, surely she’d want me to step in."
    "Right?"

    s "…"

    "Well-"
    "Only one way to find out, I guess."
    "Time to, once again, involve myself in the daily lives of [high_school] girls and see where I’m able to fit in."

    if cafe35 == False:
        scene cafeotoha2
        with fade

        r "Oh, Sensei! Good morning."
        r "If you need anything, Haruka’s manning the counter right now."
        q "Sensei? "
        q "You’re Rin’s teacher?"
        q "You look younger than she made you sound."
        s "...How did she make me sound, exactly?"

        scene cafeotoha3
        with dissolve

        r "I have no idea what Otoha’s talking about. "

        if bonus == True:
            r "I totally didn’t say anything about the gigantic age gap between us and about how you’re way too comfortable around [teenage]girls."
            o "Yeah, you walked right up to us. Show some restraint, dude."
            r "Yeah, Sensei. Show some restraint."
        else:
            r "I totally didn't tell her you were a wizard or anything."
            s "That was confidential! I trusted you!"

        "Why am I being ganged up on before I’ve even had the chance to do anything?"

    else:
        scene cafeotoha4
        with fade

        r "Oh, Sensei! Good morning!"
        o "Hey, it’s that guy from the park who hangs out with [teenager]s."
        s "I liked Rin’s greeting more."
        s "Good morning, you two."
        r "If you need anything, Haruka is manning the counter right now."
        r "If not, you’re free to chill with us, though."
        r "Or both. You’re not limited to just one of those two things."
        o "I’d probably prefer it if you’d buy something. Otherwise it seems like you just came here to hang out with Rin."

        scene cafeotoha5
        with dissolve

        r "Oh, he probably did. He does that a lot."
        s "Stop saying things that give her a bad first impression of me."

        scene cafeotoha6
        with dissolve

        r "{i}Second{/i} impression, Sensei. The first impression was when you were hanging out with Futaba and me in the park."
        r "Besides, we’re pals. I love that you come here to hang out."
        o "I still think it’s weird. But it is what it is, I guess. You do you, man."

    s "...That aside, isn’t it too early for you to just be hanging out at a table instead of working?"

    scene cafeotoha7
    with dissolve

    r "Normally, yeah. But I’m taking my break a little early since this is the only time Otoha is able to show up today."

    scene cafeotoha8
    with dissolve

    o "Wait, you’re doing this for {i}me{/i}? Dude, how much longer is your shift after this?"
    r "Like another seven hours or something. But it’s cool. I don’t need a break."
    r "I can drink coffee whenever I want, so I’ll just run on that until I collapse or something."

    scene cafeotoha9
    with dissolve

    o "Well shit, man. Now I feel really bad."
    r "I told you, it’s fine. I really don’t mind."
    s "What kind of life do you lead where nine in the morning is the only time you have to stop at a cafe?"

    scene cafeotoha10
    with dissolve

    o "I live pretty much as far away from this side of town as possible, so it’s kind of a journey every time I need to come down."
    r "Otoha takes vocal lessons in some sketchy girl’s basement not far from here."
    o "She’s not sketchy...she’s a professional musician."
    r "She just has a really sketchy basement. I saw pictures."
    o "Yeah, that much is definitely true."
    o "She’s been a big help, though. I can’t imagine where I’d be without her."

    if cafe35 == True:
        s "Right, you’re a musician."
        s "Still playing in that park we found you at?"
    else:
        s "You’re a musician?"
        o "Yup! Just like Rin here."
        r "Otoha is a million times better than me and I could never hope to achieve even an ounce of her talent or beauty."
        r "Also, I didn’t just mention her beauty. Forget that happened."
        r "Really, though. She’s so pretty."
        s "Please excuse Rin. She talks a little too much when she gets nervous."
        o "Yeah, that’s one of the first things I realized about her. I just ignore it at this point."
        r "Otoha used to play mini concerts every weekend at some park in the area Futaba and I used to live in."
        r "That’s how I met her."
        s "Used to?"

    scene cafeotoha11
    with dissolve

    o "Had to stop since I’ve been really busy lately."

    if bonus == True:
        o "After my[school] sunk into the ground out of nowhere, I started being homeschooled instead."
        o "And, weirdly enough, it’s actually a little harder being homeschooled than it is going to actual[school]."
    else:
        o "After my[school] sunk into the ground out of nowhere, I started spending all of my free time knitting socks for my cats, but all of the cats hate them."
        o "It's really stressful, to be honest. Sometimes I think about just ending everything right then and there."
        o "But then I see their sockless little paws and I'm like naaaaaaah."

    s "Yeah, I honestly can’t imagine anything easier than being in my class."
    r "Sensei hasn’t given us a single assignment in months. It’s awesome."
    o "I’m lucky if I can go a day without some ridiculous assignment."
    o "My parents are super strict about my education now that I’m not in[school] anymore."

    scene cafeotoha12
    with dissolve

    r "I’ve been trying to convince her to transfer into our[school] but she feels weird about moving into the dorms without having a roommate."
    s "Can’t she just stay in your room?"
    r "I mean...I think there’s a rule about having no more than two girls in one room-"

    scene cafeotoha13
    with dissolve

    r "Unless...we slept in the same bed and no one ever found out about it..."
    o "…"
    r "…"
    o "You good?"

    scene cafeotoha14
    with dissolve

    r "Huh?"
    r "Where am I right now?"
    s "So, you’re only in this part of town so you can go hang out and sing in some sketchy girl’s basement?"
    o "Some girl’s sketchy basement. Slightly different, but you get the gist."
    o "Rin and I have been talking a lot ever since bumping into each other in the park, but I don’t really have a lot of time to ever hang out or anything like that."
    o "So the only chances we have to meet up involve me getting up mad early and sacrificing sleep in the name of friendship."

    scene cafeotoha15
    with dissolve

    r "She’s awesome, right?! Coming all the way over here just to see me!"
    o "It’s not that big of a deal..."
    o "But yeah, I guess I can be kind of awesome at times."
    s "I come here to see you all the time."
    r "Yeah, but I see you so much that I’m starting to become immune."
    s "Can you...become immune to people?"
    r "Of course!"

    scene cafeotoha16
    with dissolve

    o "You two really spend {i}that{/i} much time together, huh?"

    if bonus == True:
        r "Yeah, but he’s only seen my boobs like once or twice so we’re probably not as close as you think we are."
        s "Why would you even say that?"
        r "Say what? What did I say?"
        r "I literally can’t remember. Am I having a stroke?"
    else:
        r "Yeah, but only because we were coworkers in our past lives. We worked at a cannery in Alaska, so we had plenty of time to get to know one another."

    o "I’m just going to pretend I didn’t hear that, so don’t even worry about it."

    "Good. I guess this Otoha girl is just as cool as she looks."
    "Which is pretty damn cool, not gonna lie."
    "Do you see how many rings she’s wearing?"

    scene cafeotoha17
    with dissolve

    r "Hey, umm...you wouldn’t happen to have any free time tonight or something would you?"
    r "It’s like...the weekend and stuff, so I can’t imagine your parents are making you study all day today."
    o "I might have some free time later on but like, I don’t really have the money to afford another bus trip."
    o "Maybe we could meet halfway? Like, walk around the mall for a little while or something?"
    r "Uhhhhhhhhhh...or literally anywhere else. Malls are weird anyway. Like, who likes malls?"
    o "What? I like malls. Plenty of people like malls."
    r "Yeah but like...there are so many...fluorescent lights and...shoe stores..."
    s "Chika doesn’t normally work nights if that’s what you’re worried about."

    scene cafeotoha18
    with dissolve

    r "Dad! Are you {i}trying{/i} to embarrass me?!"
    s "...Did you just call me Dad?"
    o "I definitely heard her call you Dad."
    r "Yes! Because you’re doing a really “Dad” thing right now!"
    o "So uhh...who's this Chika person anyway?"

    scene cafeotoha20
    with dissolve

    r "Her."
    s "How did you pull up a picture of her that quickly?"
    s "Also, where did your phone even come from?"
    r "Don’t ask questions you don’t want to hear the answers to, Sensei."
    s "But...I {i}do{/i} want to hear the answers."
    o "She’s hot."
    r "Painfully so."

    scene cafeotoha21
    with dissolve

    o "Why’s one person keeping you away from the mall, though? I don’t get it."
    r "Well...she’s not {i}keeping{/i} me away..."
    r "I’m...distancing myself for...personal reasons."

    scene cafeotoha22
    with dissolve

    o "Care to elaborate since you seem to actually understand Rin?"

    if rinbetrayed == True:
        r "I’m sure he’d be {i}thrilled{/i} to tell you all about it considering he played such a big role in everything that went down."
        s "I...should probably stay out of this, to be honest."
        o "But...you’re literally the one who brought it up."
    else:
        r "Leave my dad out of this."
        s "As much as I’d love to explain things to you, it would probably be best if Rin told you herself."
        o "Yeah...it doesn’t look like that’s going to happen."
        r "Not yet. I need time to prepare."
        r "And to...delete pictures."

    scene cafeotoha23
    with dissolve

    r "But...um, since I don’t want to go to the mall, maybe I could just come over to...your place or something?"
    r "I have some extra money for the bus and I {i}kind of{/i} know my way around that part of town anyway, so...I could just stop by tonight?"
    o "That’s sweet, but you don’t have to do that. It’s a crazy long trip to make that late at night."
    o "My house is kind of boring anyway, so I can’t imagine it would be any fun."
    o "How about you just text me tonight and we try to make plans sometime in the future?"
    o "Does that work?"

    scene cafeotoha24
    with dissolve

    r "Y-Yeah! Totally."
    r "I’ll text you all day and make like, all of the plans ever."
    o "Um...I mean, if you want to text me all day that’s fine. But I don’t think I’ll be able to respond right away a lot of the time."
    r "I will do my best to not think you hate me if you take too long to reply."
    o "Hey, if that’s what makes you happy..."
    o "I’ve gotta get a move on, though. There’s a sketchy basement with my name on it and drinking caffeine before singing really isn’t a great idea anyway."
    r "Yeah, totally! That’s a thing I definitely knew!"
    r "Um...have fun in the basement!"
    o "…"
    o "Yeah. I will...do just that."
    o "Bye, Rin."

    scene cafeotoha25
    with dissolve

    o "And see you, Sensei."
    o "Thanks for only moderately creeping up the place this morning."
    s "That’s what I’m here for."
    o "Wild."

    scene cafeotoha26
    with dissolve

    "Otoha grabs her cup of coffee off the table and chugs the entire thing down despite how bad caffeine apparently is before singing."
    "Which is also a thing I definitely knew."
    "And Rin is now beaming with so much excitement and energy that she doesn’t even feel the need to bring up Chika."

    r "Why the ever-living fuck did you bring up Chika?"

    "Oh. Nevermind, I guess."

    s "Your expression really does not match your tone right now."

    scene cafeotoha27
    with dissolve

    r "No, like really, though! Why did you do that?!"
    r "You totally knew why I didn’t want to go to the mall and you brought it up anyway."
    r "And don’t say it’s because you’re my dad and you were trying to embarrass me!"
    s "Yeah, that is definitely not a thing I was going to say. Stop calling me your dad."
    r "Fine! Then why were you being such a bad homie?"
    r "I’m just now starting to get over Chika and every time I hear her name it adds like one more week to the time it will take for that to happen."
    r "And now I’ve just added another week. Thanks a lot, Sensei."
    s "I don’t know. I guess seeing you with Otoha made me feel like you were a little closer to being over her."
    r "Dude, Otoha doesn’t even know I’m bi yet."
    s "I am...pretty sure she does."
    r "But I do such an awesome job hiding it!"
    s "…"
    r "What?! Why are you being so quiet all of a sudden?!"
    s "You literally told her that you wanted her to sleep in your bed and that she was beautiful like five minutes ago."

    scene cafeotoha28
    with dissolve

    r "That actually happened?!"
    r "I thought that was just in my head!"
    s "It absolutely was not."

    scene cafeotoha29
    with dissolve

    r "I’m such a creep. Why do you even like me?"
    s "Probably because I’m a creep, too."
    r "You really are. You’re a total weirdo."

    if bonus == True:
        r "Remind me to never flash you again."
        s "Absolutely not. I embrace all future flashing."
        r "Dude, weird. You just told me you want me to flash you."
        s "Yes. I am not hiding that."
        r "Gross. Super gross. You’re the worst."
        r "Get out of here, Dad. And stop going through my underwear drawer while I’m at[school]."
    else:
        s "No, stop. It's fine when I say it, but it hurts my feelings when you do it."
        r "Jeez. Grow up already, weirdo."

    scene black
    with dissolve2

    if bonus == True:
        "It isn’t long before Rin’s break comes to an end and I need to head back out into the street to find some other way to spend my time."
        "Even though she gave me shit about it, I think it’s safe to assume that Rin isn’t actually mad at me."
        "But a lot of that is probably due to the fact that it didn’t backfire."
        "Her friend seems really chill. The two of them would make a good couple."
        "So much so that I’m only mildly concerned about her becoming yet another barrier between Rin and me in the future."
    else:
        s "I don't like you anymore. Goodbye, Rin."
        r "Bye, Sensei! See ya later!"

    $ renpy.end_replay()
    $ cafe40 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Your daughter, Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label cafe45:
...
```

## Code that triggers this event
File: \game\RinEvents.rpy
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
    if rin_love >= 15 and cafe15 == True and day63 == False:
        jump rincafegone
    if rin_love >= 25 and rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False:
        jump cafe25
    if rin_love >= 30 and beachvacation16 == True and cafe30 == False:
        jump cafe30
    if rin_love >= 35 and rindorm35 == True and rininvite == True and cafe35 == False:
        jump cafe35
    if rin_love >= 40 and christmas7 == True and cafe40 == False:
        jump cafe40
...
```