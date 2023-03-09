# The Moon is Beautiful
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation7&go=Go)


Part of event chain [Three Girls in a Line on the Beach](./beachvacation6.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: beachvacation7
* Group: Main
* Triggered by label: beachvacation6

## Event code
File: \game\script.rpy
Code:
```python
...
label beachvacation7:
    scene chikasunset1
    with flash
    stop sound
    play music "love.mp3"

    c "Oh, hey! "
    c "I was wondering when you’d show up."

    "I make my way back to the beach after taking a short nap and immediately stumble upon Chika sitting on top of a picnic table, consumed by the light of the setting sun."
    "The laughter and conversation of some of the other girls can be heard off in the distance, but it doesn’t seem that any of them are aware of my presence yet."
    "I guess it wouldn’t hurt to spend a little time catching up with {i}this{/i} girl since she’s just now getting here, though."

    s "Hey. How’s Chinami? "

    scene chikasunset2
    with dissolve

    c "Good, good...Yumi’s gonna be heading back in a few minutes, so she doesn’t have to spend the night alone."
    c "She was taking a nap when I left so, if we’re lucky, she might not experience the lack of company at all."
    s "I’m guessing bringing her along wasn’t in the cards, then?"

    scene chikasunset3
    with dissolve

    c "Right...Too many girls close together...unknown inn...you know the deal."
    c "I can’t really do anything that would put her at risk...and even getting her here seemed damn near impossible."

    scene chikasunset4
    with dissolve

    c "Besides, I wouldn’t want her wearing that silly dog mask for an entire weekend either."

    if mall15 == True:
        s "Yeah...I can’t imagine that would match well with her swimsuit."
        c "Neither can I, Sensei...Neither can I."
    else:
        s "...Dog mask?"
        c "You’ll find out soon enough."

    c "Either way, I’m glad I was able to make it out."
    c "I love the beach. And this is the first time I’ve ever even been on vacation...even if it is only for a couple days."
    s "Well, I’m glad I’m here to experience it with you."

    scene chikasunset5
    with dissolve

    c "Yeah..."
    c "Me too..."
    s "…"
    c "…"

    "A moment of silence goes by as the sun strays further and further from our eyes."
    "Within moments, it will disappear beyond the horizon, swapping places with its lunar counterpart and drenching the beach in blue."
    "So amidst the dying sun, Chika and I-"

    scene chikasunset6
    with dissolve

    y "Yeah, sorry to interrupt whatever the fuck is going on over here, but I’m heading out."
    y "Can you give me the key?"
    c "You didn’t bring yours?"
    y "I forgot it. I’m kind of used to wearing more clothes than this, so you’re gonna need to cut me some slack this time."

    scene chikasunset7
    with dissolve

    c "Well, did you at least enjoy your free time today?"
    y "No. It was fucking exhausting."
    y "It was hot as shit, I’m sweaty, and people kept trying to talk to me. "
    c "Yeah, that’s normally how these things go."
    y "Whatever. I just want to go home and sleep. Can you just give me the fucking key so I don’t have to deal with this anymore?"
    y "Last bus leaves in like twenty minutes and if I have to sleep in a room with eleven other girls I’ll literally just kill myself."

    scene chikasunset8
    with dissolve

    c "It's in my bag..."
    y "Which bag? You have like nine."
    c "The purple one. It’s with all the other girls' bags near the bathroom."
    y "Cool, thanks."
    c "No problem. Anything else you need before you go?"
    y "…"
    y "There any food at the apartment? I haven’t eaten all day."
    c "Yeah. You can take whatever as long as you leave enough for Chinami to eat breakfast in the morning."
    y "Duh. Have fun being a fucking {i}social butterfly{/i} or whatever it was."
    s "Have a safe trip home, Yumi."

    scene chikasunset9
    with dissolve

    y "…"
    s "…"
    y "Yeah..."
    y "Thanks."
    y "See you."

    scene chikasunset10
    with dissolve

    "Yumi turns away from us and heads toward the pavilion, reaching into Chika’s bag and pulling out her key to salvation."
    "She disappears into the bathroom with a white plastic bag in tow and gets dressed, coming out and walking toward the bus stop just a minute or two later."
    "The entire time, Chika and I don’t say anything."

    c "Did you...see that just now?"
    s "See what? Her getting dressed?"
    s "Because I doubt I'd be able to see into the bathroom from here even if I-"

    scene chikasunset11
    with dissolve

    c "No, doofus. The way she said goodbye to you."
    s "You mean with disdain and resentment?"

    if bonus == True:
        c "I mean without being rude or telling you she’s going to rip your dick off."
    else:
        c "I mean without saying anything about beating up old people."

    c "Isn’t that like, a huge improvement?"
    s "Oh...Yeah, I didn’t even notice that. That seems like a pretty big deal."
    s "I wonder if she’s doing okay?"

    scene chikasunset12
    with dissolve

    c "What was she like on her own? Did she just sort of...sit around and do nothing all day?"
    s "I haven’t been around for a good portion of it, but I think so."
    s "Having Yumi on her own in a social setting probably isn’t the best idea right now."
    c "That’s exactly why I was so insistent on her coming."
    c "She needs to actually talk to people if she’s ever going to stop being so bitchy all the time."
    c "I’m kinda surprised she even came, to be honest. This was the first time she’s ever actually taken one of my suggestions."

    scene chikasunset4
    with dissolve

    c "Maybe she just wanted to see you?"
    s "That is definitely not the reason. I only had one conversation with her today and it basically ended with her calling Futaba a beached whale."

    scene chikasunset13
    with dissolve

    c "Oh my fucking God! Are you kidding?! She's even doing that {i}here?!{/i} On vacation?!"
    c "I don’t know how many times I need to tell her to be nice to her! It’s fucking unbearable."
    c "What the hell did Futaba even do?! She’s like, the nicest girl in class."
    s "Beats me. Yumi quieted down in the end, though. Maybe even looked a little upset."
    s "I didn’t think much of it, though. Not going to spend time trying to cheer someone up who’s literally doing things to make themselves miserable in the first place."

    scene chikasunset14
    with dissolve

    c "Wish I could do that..."
    c "I always feel like I need to cheer people up no matter what and it’s like, not even possible 90%% of the time."
    s "That’s life. Sometimes, you just need to let people tire themselves out through sadness."
    c "That's like, mega depressing."
    s "Just try not to fall into the same slump as Yumi and you'll be fine."
    c "Yeah..."
    c "I'll try."

    scene black
    with dissolve2

    "A few minutes go by as Chika and I make idle chit-chat about her job at the mall and her plans for tomorrow."
    "Apparently, she isn’t much of a swimmer but loves the sun, so she’s going to be “decompressing” and sunbathing for the bulk of the day."

    if bonus == True:
        "It sounds boring to me, but as long as I get to see her lounging around in her bathing suit, she’s free to do whatever she likes."
    else:
        "I hope she has a very relaxing night because she deserves it."

    "Eventually, two more familiar faces wander into the frame and start heading our way, prompting Chika to hop off of the table and meet them."
    "........."
    "......"
    "..."

    scene chikasunset15
    with dissolve

    c "Futaba, Sensei told me about Yumi and I just want to say I’m so, so sorry..."
    c "I honestly think you’re one of the cutest girls ever and I will never understand why she’s so mean to you. It makes zero sense."
    f "Oh...It’s okay. It’s not your fault."

    scene chikasunset16
    with dissolve

    c "It’s at least {i}kind of{/i} my fault. I’m the one who talked her into coming and then she went and did something like that."
    c "If you ever need someone to help deal with her, please just let me know."
    c "There’s obviously not much I can do to get her to stop, but I can at least pull her hair or something if she gets to be too annoying."

    scene chikasunset17
    with dissolve

    r "{i}Pull her hair?...{/i}"
    f "…"

    scene chikasunset18
    with dissolve

    f "It’s okay, Chika. Really."
    f "I’m getting a little better at dealing with things like that."

    scene chikasunset19
    with dissolve

    f "Thanks to...a certain someone."
    s "…"
    c "…"
    s "Who? Me?"
    f "Of course. You’ve done so much for my confidence in just a short time that it’s...almost kind of crazy."

    scene chikasunset20
    with dissolve

    r "Really? {i}This{/i} guy of all people? How does that work?"
    s "Rin, I think you’re forgetting that I know things about you that I could ‘accidentally’ let slip at any moment."

    scene chikasunset21
    with dissolve

    r "I take it back! Sensei is the greatest! So great! Such a cool dude!"
    c "What sort of things does Sensei know about you that I don’t, Rin?"

    scene chikasunset22
    with dissolve

    r "Nothing! He knows nothing! "
    c "Do I spy hearts in your eyes?"
    r "I don't even have eyes!"
    c "I bet Sensei knows who you’re crushing on, doesn’t he?"

    scene chikasunset22r
    with dissolve

    r "What?! Wh-Why would you ever think something like that?!"
    c "Cause I’m a girl, duh. We can smell these sorts of things from a mile away."
    r "We can?!"
    c "Well, {i}I{/i} can, at least. And that face says it all."
    c "That's the face of a girl in love."

    scene chikasunset23
    with dissolve

    r "Wow it’s...suddenly getting a lot hotter out here, isn’t it?"
    r "Hahahah...Wow! So hot! Maybe I need to sit down or...drink water or...sit down?"
    c "You said “sit down” twice."
    f "Sensei...would it be okay if I pulled you aside for a second? There’s something I want to talk about."
    s "Oh. Uhh...yeah. We can do that."
    f "Great...thanks."

    scene black
    with dissolve2

    "Futaba walks with me toward the trees, leaving Chika and Rin behind to talk on their own..."
    "........."
    "......"
    "..."

    scene chikasunset24
    with dissolve

    f "Maybe it’s for the best if we let the two of them be alone for a little while, don’t you think?"
    s "…"
    f "…"
    s "You know, don't you?"
    f "Of course I know. Rin is basically my sister."

    scene chikasunset25
    with dissolve

    f "I've had my suspicions for a while, but...she's been making things a lot more obvious ever since high school started."
    f "I'm pretty sure she's just...accepted that I know by now. But it's not like we've ever had a conversation or anything."

    scene chikasunset24
    with dissolve

    f "I also...had a feeling you knew as well, given how close you two have become."
    s "Yeah well, like you said, it's not like she does a particularly good job of hiding it."
    f "She really doesn’t..."
    s "So I guess...the two of us will just hang out over here for a while and let them do their thing?"
    f "Unless you have a problem spending time with me, of course."
    s "I think I’ve made it quite apparent that I very much enjoy spending time with you."

    if bonus == True:
        f "You have...but please try to keep it in your pants for now since we don’t know how long Rin will be able to last on her own."
        s "I will do my very best..."
    else:
        s "Now, about the egg tossing competition-"

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    scene chikasunset26
    with dissolve2

    "Oh, how horrible it is to be unloved."
    "To love those who can not understand. "
    "And to forgo the love of oneself in pursuit of that."
    "All three gods disappear and leave yet another poor soul to fend for itself as the day becomes the night."

    play sound "static.mp3"
    scene chikasunset27
    with flash
    stop sound

    c "So, are you going to tell me who it is or am I going to have to guess?"
    r "Umm...preferably neither."
    c "What? So Sensei can know but I can’t? "
    r "Well...he kind of just found out in the heat of the moment...or whatever."

    if chikadorm20 == True:
        scene chikasunset28
        with dissolve

        c "Wait...it’s not {i}him{/i} is it?"

        scene chikasunset29
        with dissolve

        r "Huh? No. I didn’t mean it like that."
        r "I meant that he just kind of found out on his own. It’s not like I planned on telling him or anything."
        c "Oh okay, okay. Just making sure."

        scene chikasunset30
        with dissolve

        c "In a sense, that’s kind of how he found out for me as well."
        r "You..."
        r "You have someone you...like?"
        c "Maybe..."
        c "Why should I tell you when you won’t tell me, though?"

        scene chikasunset31
        with dissolve

        r "My situation isn’t exactly normal..."
        c "What, and mine is?"
        c "We can’t help who we fall in love with. "
        c "Kinda like that one poem you wrote back in middle[school]."

        scene chikasunset32
        with dissolve

        r "You...You remember that?!"
        c "Of course I remember that. It was, like...one of the cutest poems I've ever heard."

        scene chikasunset33
        with dissolve

        c "And the way you got all nervous when the teacher made you recite it. Adorable. Top ten Rin moment."
        r "Why are you ranking my moments?!"

        scene chikasunset31
        with dissolve

        c "Listen...the point is that I’m not going to judge you no matter {i}who{/i} it is. "
        r "Yeah...I don’t know about that, Chika..."
        c "No, no. I mean it. I know you probably don’t think of me as a good friend or anything like that, but I’ve wanted to get closer to you ever since I heard that poem."
        c "I feel like you’ve got all these feelings you keep bottled up that are just dying to get out."
        c "Which probably sounds a little crazy since we’ve never really shared anything like that."
        c "But...I’ve always seen myself as a pretty good judge of character. And if you ever {i}do{/i} want to open up to me a little more...I’d be happy to listen."

        scene chikasunset34
        with dissolve

        c "Not sure if I’ll be able to tell you who I’m crushing on, though. That one’s kind of a big deal..."
        r "...Yeah."
        r "So is mine."

    else:
        scene chikasunset35
        with dissolve

        c "Wait, is it that Molly girl who just transferred in?"
        r "Molly?! Why would you think that?!"
        c "I don’t know. I saw you two talking earlier and it looked like you were really close."
        r "We are close! But like, not {i}that{/i} close!"
        r "We just play games together and work at the same place."
        r "Molly’s a great friend but like...{i}totally{/i} not my type."

        scene chikasunset36
        with dissolve

        c "Oh? What {i}is{/i} your type, then?"
        r "Well, that’s...kind of a secret too."
        c "Really? You won’t even tell me what kind of person you’re into?"
        c "I get not wanting to come out and say {i}who{/i} you like, but I’m pretty sure you can at least tell me who you’d generally go for."
        r "Uhh...I mean, I guess. But it’ll probably sound really weird."
        c "Why would it sound weird?"
        r "Because my type is basically the same type of person that...you know...{i}you{/i} are and stuff..."

        scene chikasunset37
        with dissolve

        c "What?! Seriously?!"
        c "That’s like...a huge surprise!"
        r "It...is?"
        c "Yeah! I’m like, the complete opposite of you, right? Like, our styles don't match at all."
        c "Maybe that whole opposites attract thing is true after all?"
        r "Wait a second. Umm..."
        r "You don’t think it’s weird that I basically just...you know..."
        r "Came out to you?"
        c "What? No. Why would I care about that?"
        c "I was more surprised that you said you were into girls {i}like me{/i} than the fact that you're into girls to begin with."

        scene chikasunset38
        with dissolve

        r "So...you’re really not weirded out?"
        c "Of course not. What year do you think it is, Rin? It's not like girl on girl relationships are {i}unheard{/i} of."
        c "Like, there are tons of girls I think are super pretty."
        c "Take Niki for example- I've got posters of her all over my wall and if, for some weird reason, she ever wanted to hook up with me?...{i}Oh boy.{/i} You don't even know."
        c "I’ll admit that I've never really thought about being in a {i}relationship{/i} with a girl...but I don’t think I’d be opposed if the right one came along."
        c "I’m on the side of just “go for whoever you want to go for” and if it doesn’t work out then, hey...at least you tried. You know?"

        scene chikasunset39
        with dissolve

        c "N-Not that I have any experience in the matter or anything like that..."
        c "It’s just...you know...how I feel and stuff."
        r "...Yeah."
        r "Yeah, I totally get it."
        r "I'm..."
        r "I'm really happy to hear that, actually..."
        c "…"
        r "…"

    mo "PAGING RIN ROKUHARA. RIN ROKUHARA, PLEASE REPORT TO THE TINY IRISH GIRL."

    scene chikasunset40
    with dissolve

    r "Huh?"
    c "Plans tonight?"
    r "Not as far as I can re-"

    scene chikasunset41
    with dissolve

    r "Oh crap! I totally do have plans tonight! I completely forgot!"
    c "Well, don’t let me hold you up if your friends are waiting for you."
    c "I think I’m gonna hang out under the moon for a little while longer anyway. "

    scene chikasunset42
    with dissolve

    c "It’s really beautiful tonight, don't you think?"
    r "..."
    c "..."
    r "Yeah..."
    r "The moon is beautiful..."

    "If this were a happy story, a shooting star would pass over them."
    "The girl on the left would confess her feelings to the one on the right."
    "And the two of them would kiss."
    "But this is not a happy story."
    "There are no happy stories."
    "And so they will break apart."
    "Just as all things do."
    "But at least the moon is beautiful."

    mo "RIN! WHERE THE HECK ARE YOU? WE’VE GOT DRAGONS TO SLAY."

    scene chikasunset43
    with dissolve

    c "Jeez. Sounds like your plans are even crazier than I thought."
    r "Ugh...Why {i}tonight{/i} of all nights?"
    c "Probs cause the dragons would kill us all if you waited until tomorrow."
    r "Please don’t add to my current embarrassment, Chika. I’m drowning enough as-is."
    c "Heheh...Go slay your dragons, Rin."
    c "We can talk more tomorrow."

    scene black
    with dissolve2
    stop music fadeout 5.0

    r "Yeah..."
    r "I’d like that."

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ beachvacation7 = True

label beachvacation8:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```