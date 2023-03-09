# Christmas Miracle
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmas6&go=Go)


Part of event chain [Baby it's Cold Outside](./chikalust10.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmas6
* Group: Main
* Triggered by label: chikalust10x

## Event code
File: \game\script.rpy
Code:
```python
...
label christmas6:
    play music "christmasyay.mp3" fadein 5.0
    scene secretsanta5
    with dissolve

    "I walk into the room with Chika (Who immediately ducks into the bathroom to fix her makeup) and find that the rest of the girls have already started handing out presents."
    "I’m assuming there’s no way I’m actually exempt from giving someone a gift, so I guess this is the moment of truth where I just wait around to see who I disappoint."

    if chikalust10 == True and bonus == True:
        "Unless I actually {i}do{/i} wind up with Chika."
        "In that case, I’ll just use her first semi-public orgasm as my Secret Santa present."
        "Which would be kind of awesome because I didn’t even have to giftwrap it."

    m "What is with that face?"
    s "What face? What are you talking about?"

    if bonus == True:
        m "You have a disgusting expression that makes it look like you’re reflecting on something gross you’ve probably done."
    else:
        m "The really cute one you have plastered to your head."

    sa "I think...you look the same as always...Sensei..."
    m "Yes, I agree."

    if bonus == True:
        m "You always look like you’re caught in the middle of thinking something horrible."
        sa "That...isn’t what I said."

    s "Thank you for being so pure, Sana."
    s "And thank you Maya for..."
    m "…"
    m "For what? "

    if bonus == False:
        m "Loving you?"

    s "For always wearing clothes that accentuate your legs."
    s "You had me for Secret Santa, didn’t you?"
    m "…"

    scene secretsanta2
    with dissolve

    m "I’d have given you something much different if that were true."
    s "Oh yeah? And what would-"
    m "Anthrax."
    s "...Okay, so moving right along then. Shouldn’t you two be giving your gifts out instead of just standing around?"
    s "Who did you have?"

    scene secretsanta3
    with dissolve

    sa "I...had Chika but...she kind of disappeared into the bathroom so now I have to keep standing here awkwardly."

    "Shit. Looks like I {i}will{/i} be disappointing someone after all."

    s "What did you get her?"

    scene secretsanta4
    with dissolve

    sa "Well...I don’t really know her well so I...wound up just buying her some...girly stuff I found from the mall."
    sa "Rin helped me, but she kept trying to make me go over the spending limit."
    sa "She even offered using her own money, but...that just felt strange..."
    s "Yeah that sounds about right. "
    s "If there’s anyone who knows what Chika would like, it’s Rin."
    sa "R-Really? Not Yumi?"
    s "Nope. Definitely Rin. "

    scene secretsanta5
    with dissolve

    sa "I didn’t realize they were that close..."
    s "Sometimes I don’t think they’re close enough."
    sa "I...don’t know what that means."

    if bonus == True:
        s "Don’t worry. I’ll tell you when you’re older."
    else:
        s "I just think it would be great for both of them if they would just hug every once in a while."

    sa "…"
    sa "What?"
    s "And Maya? What about you?"
    s "Who’s the lucky recipient of whatever strange gift you decided to purchase?"
    m "Futaba. Also MIA."
    m "I think she went to get some water. Seeing everyone kiss seemed to really take a toll on her."
    s "Wait, don’t tell me that kept going after I left the room?"

    scene secretsanta6
    with dissolve

    if bonus == True:
        m "You missed out on an entire orgy. Poor Sana nearly had to go to the hospital."
    else:
        m "No. But Sana killed a housekeeper with her bare hands. It was sweet."

    sa "Wha-?!"
    sa "Th-th-th-th-that never happened!"
    sa "I’ve still never...k...k..."
    s "Good. Stay that way forever."

    scene secretsanta7
    with dissolve

    sa "For...ever?..."
    m "Joking aside. All of the debauchery managed to miraculously end the second you left the room."
    m "I wonder how that happened?"

    "Pretty sure Chika just brought all of it outside."
    "And that, I am thankful for."

    s "So...I guess since you two are the only ones standing around, it means one of you is the person I have to disappoint?"
    m "Oh, you had me. I’ve known the whole time."
    m "But I’m used to you disappointing me, so it’s fine that you didn’t get me anything."

    scene secretsanta8
    with dissolve

    s "Wait, you knew this whole time and you didn’t tell me?"
    s "I specifically asked {i}you{/i} earlier because I figured you’d know."
    s "Are you saying you lied to me back then?"
    m "I lie to you literally all the time. I don’t think this should come as that big of a surprise."
    s "Why, though? Don’t you want a present?"

    scene secretsanta9
    with dissolve

    m "Not really."
    m "But if this is about not looking like a complete jerk, you can just tell everyone that this scarf was an early Secret Santa present."
    m "But then again, I don’t think you care much about not looking like a jerk, so you can just disregard that."
    s "I really want to feel bad about myself for letting you down right now but being insulted is making that a little more difficult."

    scene secretsanta8
    with dissolve

    m "It’s fine. You hate Christmas anyway."
    m "Use my present money to get something for Ami or Ayane. You know- people who would actually like to receive presents from you."
    s "You liked the scarf so much that you literally collapsed."
    m "That never happened."
    m "I graciously accepted this accessory and politely bowed before walking away."
    m "The reset must have destroyed your memory."
    sa "R...Reset?"

    scene secretsanta9
    with dissolve

    m "It’s a long story."
    s "…"

    "Did she really just summarize the fact that we’ve literally reset the[school] year together {i}twice{/i} with “It’s a long story?”"
    "I mean, she’s not wrong but..."
    "That seems kind of anti-climactic."

    s "There’s really nothing I can do to make it up to you?"

    scene secretsanta10
    with dissolve

    m "To make it up to me? Hmm..."
    m "…"
    m "…"
    m "…"

    scene secretsanta11
    with dissolve

    m "Could you leave me alone forever?"
    s "Nope."
    m "Didn’t think so."
    m "Then no. "
    m "The best thing you could do right now, though, is stop drawing attention to the fact that the two of us are talking to one another."
    m "You’re an annoyingly popular character, so it will be quite troublesome if people begin to think I’m somehow close to you."
    s "Okay, but eventually I’m going to-"
    y "Umm..."

    "I feel a suspiciously light tapping on my shoulder after hearing Yumi interject."
    "And I say “suspiciously light” because I assume she is the one tapping me and I associate nothing but pent-up aggression with that girl."

    s "…"
    y "…"
    m "…"
    m "This is the part where you turn around."

    scene secretsanta12
    with fade

    "I turn around to find a rather timid version of the class delinquent hiding half of her face behind a brightly colored notebook."
    "And judging by the fact that this particular notebook has “Not a gift” written on it in black permanent marker, I think it’s safe to assume that it is, actually, a gift."

    y "...Yo."
    s "Yo."
    y "…"
    s "…"
    s "Is that for me?"

    scene secretsanta13
    with dissolve

    y "Not because I want it to be."
    y "I was just the last person to draw a name out of the stupid fucking hat and everyone probably threw your name back in because you suck so much."
    s "But you still got me something anyway?"
    s "I figured you would have just skipped something like this."

    scene secretsanta14
    with dissolve

    y "I wanted to but...Chika and Chinami found out and made me do this."
    y "It’s not like I bought anything or whatever, though. I just kind of...wrote you a note. I guess."
    s "…"
    y "…"
    s "Well, can I read it?"

    scene secretsanta15
    with dissolve

    y "No. Fuck off."
    s "So you wrote me a note that I’m not allowed to read and that is my Christmas present?"
    y "You can read it just..."
    y "My body won’t let me hand it over to you."
    y "Probably because it’s looking out for me and knows it will be a bad move if I show you anything that could even be confused for affection."
    s "Give me the hate letter, Yumi."

    scene secretsanta16
    with dissolve

    y "I-It’s not a hate letter!"
    y "It was going to be but the fuckin...Chosokabes kept makin’ me rewrite it until they approved it!"
    y "So this is the fifth letter! Or sixth! I don’t even remember! "

    scene secretsanta17
    with dissolve

    y "AAAAAHHH JUST FUCKING TAKE IT!"

    "Yumi gives up on hiding and literally throws the notebook at my chest."
    "I catch it with my impressively great reflexes and immediately retreat to the door to see what she could have possibly written about me."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene secretsanta18
    with dissolve2

    s "…"

    "This is actually weirdly touching."
    "Maybe it’s just the obnoxiously happy background music or the fact that she was so embarrassed about handing this over but..."
    "I actually like this present a lot."
    "It’s the perfect thing for someone like me who hates the holidays and can’t find a point for most material goods."
    "Sometimes, it’s good to just...hear what someone has to say from the heart."
    "And sure this might be a little more exaggerated or kind than how Yumi really feels-"
    "But the fact that she was able to write something like this down after what I did to her is really..."
    "Rewarding?"
    "Surprising, maybe?"
    "…"
    "Oh no. This isn’t one of those Christmas miracles, is it?"

    scene secretsanta19
    with fade

    y "…"
    y "Make fun of me and I’ll fucking kill you. Got it?"
    s "Thanks, Yumi. I really appreciate this."
    y "You appreciate me calling you “Not the worst ever?”"
    s "You know, I really do."
    y "Oh. Well...cool, I guess."
    s "…"
    y "Can you give me the notebook back now?"
    s "Wait, you need it back?"
    y "That’s the only notebook I own and I need it for[school]."
    s "You don’t even come to[school]."
    s "And I wouldn’t give you any notes to take even if you did."

    scene secretsanta20
    with dissolve

    y "J-Just give it back, okay?! It’s embarrassing for you to hang on to it!"

    if bonus == True:
        y "I don’t want you fucking...jerking off on it or something."
        s "I can’t believe I have to say this but I’m not going to jerk off on your Christmas present."
    else:
        y "I don't want you to like...hug it or whatever."
        s "I'm not going to hug the present, Yumi."

    y "Like I’d fuckin’ believe that! Give it back, asshole!"

    scene black
    with dissolve

    "Yumi moves toward me to try and grab the notebook forcefully, causing me to backpedal and make my way toward the door with a death grip on it."
    "This may seem like just a silly note to some, but for me- it is a symbol of progress."
    "A trophy that I must treasure."
    "I shall protect it in any way I can."
    "………"
    "……"
    "…"

    play sound "dooropen.mp3"

    c "Huh? What’s going on out here?"
    y "FUCKING...STOP...RUNNING!"

    scene secretsanta21
    with dissolve

    c "I go into the bathroom for five minutes and that’s all it takes for you to explode? What happened?"
    y "Chika! Tell him to give me back my notebook!"
    c "Your notebook?"
    c "Is this because of the Secret Santa thing?"
    y "Yes! Tell him he has to give it back!"
    c "But...he doesn’t."
    c "Do you not understand how presents work?"

    scene secretsanta22
    with dissolve

    y "He...gets to keep that?!"
    c "Of course~ "
    c "Besides, doesn’t it make you happy knowing he can pull it out and look at it whenever he wants?"
    y "Uhhhhhhh, no?!"
    y "If he keeps that then...where am I going to write all of my notes for[school]?!"
    c "You don’t even come to[school]."
    c "And Sensei wouldn’t give you any notes to take even if you did."
    s "See? That’s exactly what I said."

    scene secretsanta23
    with dissolve

    y "Stay the fuck out of this. This doesn’t concern you."
    s "This is literally {i}about{/i} me..."

    scene black
    with dissolve2

    "Yumi and Chika proceed to argue about how imperative it is that Yumi gets her notebook back."
    "We offer the compromise for me to just remove the page with the note on it but, of course, this was never about not being able to take notes for[school]."
    "I don’t know if Yumi’s afraid of looking weak or if she just thinks I’m going to...use this against her in some way-"
    "But I really do just want to keep it and tuck it away in some drawer to forget about and probably look back on for nostalgic value many years from now."
    "If I even make it to “many years from now.”"
    "But hey, months ago, I never would have even dreamed of getting an acknowledgement of how I’m not literally Satan from Yumi."
    "So if this can happen, literally anything can happen."
    "………"
    "……"
    "…"
    "A loud bang can be heard from outside as the walls of the hotel are dyed with bright, red light."
    "In addition to Christmas lights and decorations, it seems like fireworks are a thing I’m apparently going to have to deal with now as well."
    "One by one, girls begin leaving the room and heading outside, grabbing my sleeves and trying to get me to come with them."
    "There are two exceptions to this."
    "Well, I guess three technically."
    "The first two come in the form of Makoto and Miku, who leave the room in a hurry- likely to get Miku somewhere she won’t be able to hear anything."
    "I think about following them, but realize Makoto is probably better suited to dealing with Miku’s condition than I’ll ever be."
    "Instead, I remain in the room with the second exception to the sudden and intense interest in fireworks."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ christmas6 = True

label futabalust10intro:
    scene futabalustten1
    with dissolve

    f "Umm...Hi, Sensei."
    f "Is there a reason you’ve decided to hang out here instead of going downstairs with everyone else?"
    s "Wouldn’t the same go for you? "
    s "Go enjoy your youth or whatever it is someone in my position is supposed to say right now."
    f "Maybe in a bit. Things have been pretty...hectic in here tonight and I’m trying to avoid getting a headache."
    s "I get that. Molly’s little game sure shook things up a bit."

    scene futabalustten2
    with dissolve

    f "And of course I’m going to be the one who has to hear about it for the next month."
    s "A month? I don’t think it will take Rin that long to get over something as trivial as a little kiss."

    scene futabalustten3
    with dissolve

    f "Sensei! A girl’s first kiss is important!"
    f "It probably sounds silly to you, but a lot of people really care about that stuff."
    s "Are you one of those people, Futaba?"

    scene futabalustten4
    with dissolve

    f "I {i}was{/i}. "

    if bonus == True:
        f "Now we do naughty stuff all the time and I’m starting to think I’ll go the rest of my life without ever being kissed by anyone."
        s "Did I really corrupt you this much without ever kissing you?"
    else:
        f "But everything changed when the fire nation attacked..."
        s "=("

    if futaba_lust < 10:
        scene futabalustten5
        with dissolve

        if bonus == True:
            f "Some might say you haven’t corrupted me enough."
            f "I’m sure in some alternate timeline, my lust for you would be even higher and we’d wind up doing something pretty risky while everyone else was downstairs."
            s "Does that mean that isn’t going to happen in this particular timeline?"
            f "Mhm."
            f "Well, not today at least."
            f "But we can still hang out and talk for a little while before heading down."
            f "I’m curious to hear about whatever it is Yumi wrote in that notebook for you."

            scene black
            with dissolve2

            "Just as she suggests, Futaba and I spend the next five or ten minutes talking about the gifts we received tonight."
            "It turns out that Maya’s exchange with her wasn’t exactly lengthy and that she just handed her a gift card on her way out the door, but Futaba apparently doesn’t care for presents much anyway."
            "She talks about how she much prefers buying things for herself so she can be sure she’ll like something- and it’s really just the thought that counts at the end of the day."
            "And while some people might think giving someone a gift card has no thought to it at all, 100%% of the people in this room disagree- and that’s more than enough for me."
            "…"
            "Eventually, the two of us decide to head back downstairs to meet up with everyone else."
            "To avoid suspicion, I go to exit the room first while Futaba runs into the bathroom to adjust her makeup."
            "But, just as I reach for the handle, it opens on its own and someone rather peculiar steps in."
        else:
            scene black
            with dissolve

            "Futaba tells me all about how her mother was killed in a raid by the fire nation in an attempt to uncover the last water bender in her village."
            "Now Futaba has to help some kid with a weird tattoo save the world or something. I don't really know."
            "But she's clearly got a lot more important shit to deal with than hanging out with me, so I decide to leave her alone for the rest of the night."

        stop music fadeout 5.0

        "………"
        "……"
        "…"

        $ renpy.end_replay()
        $ futabalust10miss = True
        jump christmas7

    else:
        jump futabalust10

label futabalust10:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
c "Mm...oh god...[chikamaster]..."
    c "It’s not sex but...it’s close...right?..."
    c "Do you ...like when you can rub up against my...pussy like that?"

    "Her fingers move from touching herself to massaging the underside of my shaft."
    "And I say massage but it feels a little closer to a tickle."
    "Her fingers lightly graze the outline of my cock as it glides against her."
    "They constantly alternate between touching me and her as she gets caught in an endless struggle between which she cares more about in the moment."

    scene chikalustten14
    with dissolve

    c "Mm...mmm...[chikamaster]..."
    c "Can I...mmf...ask you something?..."
    s "Now?"
    c "Mmn...yeah..."
    c "Could I still be called...innocent if I...made myself cum while wearing a santa suit on a bench behind a hotel?..."
    s "…"
    c "Mn...mmm...ahm..."
    s "No..."

    scene chikalustten13
    with dissolve

    c "Mm...I...didn’t think so..."
    c "But...I’m pretty sure..."
    c "I’m...gonna do it anyway..."
    c "So...please excuse me..."

    scene chikalustten15
    with fade

    c "Oh...shit...yeah...definitely...going to cum..."

    "Chika breaks our kiss and arches her back to give her a better angle to touch herself in- something I guess she’s decided to abandon hiding from me."
    "If she was even hiding it at all in the first place, to be honest."
    "I start biting her ear and move my hands to her chest to help her along with the process."
    "Her body is covered in goosebumps."
    "So much so that I might actually worry a bit about her health."
    "But I guess some people are just more prone to things like that."

    scene chikalustten16
    with dissolve

    c "Hah~ Ahhh...yes...[chikamaster]..."
    c "My ears are...sensitive...and I...already..."
    c "Oh my god...it feels so good..."
    c "Gonna scream...can’t...hold it back..."
    c "If we...get caught...I’ll...take the...cock- I mean...blame~"
    c "Sorry...sorting out...thoughts in my..."
    c "Oh fuck..."
    c "[chikamaster]...yes...{i}yes{/i}..."

    "Chika’s grinding slows down once more and the pressure increases tenfold- like she’s trying to literally force me inside of her through my jeans."
    "And despite this being an impossible feat, she still manages to find enough pleasure to do this-"

    c "Ahh...ahhh..."
    c "Fuck...yes...yes yes yes..."
    c "…"

    scene chikalustten17
    with cumflash
    with hpunch

    c "AAAAAAAAAAAAAAAH!!!!~~~~~~"

    "Despite proclaiming that she was going to scream, Chika manages to keep her volume a full two steps or so behind ear-curdling."
    "She rocks hards against me as she cums and, lo and behold, her body goes limp moments afterward."

    scene chikalustten18
    with dissolve

    c "Hah...ahh......mm...hah..."
    c "It’s so...cold out here..."
    s "Did my body heat wear off?"
    c "It was...never enough...in the first place..."
    c "I just...wanted to...do sexy stuff with you..."
    c "Cause I like you..."
    c "But now...I’m just...cold..."
    s "…"
    s "So you don’t like me anymore?"
    c "I’ll like you more...once I’m warm again..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I pull Chika closer and wrap my arms around her."
    "Not because I feel the same way she feels about me, but because I don’t want her to get sick and accidentally kill her sister."
    "Also, she’s very cute."
    "Holding cute, half-naked girls close to me is something I’m kind of into, if you haven’t guessed."
    "…"
    "Eventually, after Chika regains her breath, the two of us head back inside and make our way upstairs."
    "But even when we get there, I notice that her goosebumps have yet to fade."

    $ renpy.end_replay()
    $ chikalust10 = True
    $ chika_lust += 1
    jump christmas6
...
```