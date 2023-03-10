# Bleed (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Little Miracles](./chikaonsen1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: chikaonsen2
* Group: Chika
* Triggered by label: onsenbegin
* Chain sources: chikaonsen1
* Chain sources path: chikaonsen1->chikaonsen1

## Official wiki page

[Bleed](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikaonsen2&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label chikaonsen2:
    if bonus == False:
        scene noonsky
        with dissolve
    else:
        scene chikaonsen1
        with dissolve2

    play music "gentle.mp3"

    "The mixture of cold air and hot water is one of the single most under appreciated sensations in the entire world."
    "Especially for a girl who so easily gets goosebumps."
    "So, there she sits, watching steam rise off the surface of the water-"
    "Counting the bumps on her arms and then submerging them until they’re gone, acutely aware of how easy it is to control certain changes in our bodies."
    "She will undergo one more dramatic shift in that regard soon."
    "Because roughly two hundred feet away from here lies a bath for the opposite sex, currently housing a man she has fallen helplessly in love with over the last several[school] years."
    "Or perhaps it’s more like hundreds."
    "Thousands, maybe?"
    "What if, by some stretch of the imagination, she’s been slowly falling in love over the course of millions of[school] years?"
    "And what if, by an even larger stretch of the imagination, this isn’t the first time at all?"
    "How many onsen tickets have there been? "
    "And what has happened on those respective visits?"
    "Can we truly surmise that this is the first of all of them?"
    "One more deviation in an incessantly deviating timeline doesn’t seem so far fetched now, does it?"
    "Please forgive me."
    "I get lost in thought during times like these."
    "I’d like to take a moment and blame it on the mixture of temperatures."
    "I don’t get goosebumps the same way this girl does, but I {i}do{/i} see the beauty in life when it so rarely shows up on a silver platter."
    "And even though the girl in front of us doesn’t see things the same way I do-"
    "She does see things."
    "She sees a world much brighter than us."
    "A world where even those who are lost in the dark are able to crawl out as long as they persist and shed a little blood."
    "Bleed, you beautiful girl."
    "Bleed and feel alive."
    "Bleed and remind yourself that you are loved-"
    "Even though everyone else you’ve ever loved has already left you."

    tb "Is this spot taken?"

    if bonus == True:
        scene chikaonsen2
        with dissolve

    c "Oh, Tsubasa! I didn’t realize you were-"

    if bonus == True:
        scene chikaonsen3
        with dissolve

    c "Woah."
    tb "Hm?"
    c "You’re uhh...pretty stacked."
    tb "Just try not to stare too much or you’ll go blind."

    if bonus == True:
        scene chikaonsen4
        with dissolve

    c "Oh, sorry! Just...took me by surprise there."
    c "You’re like, super beautiful. "
    c "Is that a weird thing to say when we're both totally naked and sitting next to each other in a hot spring?"
    tb "Not at all. In fact, I’m flattered."

    if bonus == True:
        scene chikaonsen5
        with dissolve

    tb "Unfortunately, I’m married. So I can’t exactly reciprocate your feelings, dear."
    tb "I also can’t imagine your boyfriend would be very fond of you abandoning him on your getaway for someone like me."

    if bonus == True:
        scene chikaonsen6
        with dissolve

    c "Oh, he’s not my boyfriend."
    c "Though...I did accidentally call him that in[school] the other day. Which was like, super embarrassing."
    tb "Embarrassing why? "
    tb "Are you ashamed of him for some reason?"

    if bonus == True:
        c "No, no. Not at all. But like, he’s still my teacher and there’s a pretty huge age gap between the two of us."
    else:
        c "No, no. Not at all. But like, he’s still my teacher. And also the huggy boy."

    c "So I’ve gotta try like, really really hard to not be clingy when all I wanna do is just hold his hand all day every day."

    if bonus == True:
        scene chikaonsen7
        with dissolve

    tb "Ahh, yes. Being [young]and in love."
    tb "I wish I could have experienced something like that at least once in my life."
    tb "Treasure it while you can, dear."
    tb "Before you know it, you’ll be old and raising kids...thinking to yourself, “Where did all the time go?”"

    if bonus == True:
        scene chikaonsen8
        with dissolve

    c "Wait, aren’t you married?"
    c "Do you not love your husband, Tsubasa?"
    tb "Can you keep the answer to that question a secret?"
    c "Of course. Who would I even tell?"
    tb "For all I know, you could be a spy he sent here for this exact reason. "
    tb "Though I doubt a spy would have stared so blatantly at my breasts for as long as you did."
    c "I could be a really perverted spy. You never know."
    tb "I suppose that’s true. But I also suppose that even if you are a spy, hiding the truth from you wouldn’t do much this far into life."

    if bonus == True:
        scene chikaonsen9
        with dissolve

    tb "My husband is...a good man."
    tb "But he’s not a man I chose for myself."
    tb "I do love him, but...I don’t think I’ve ever been {i}in{/i} love with him."
    tb "We both come from wealthy families and our marriage was arranged from the moment we were born."

    if bonus == True:
        scene chikaonsen10
        with dissolve

    tb "And between you and me, he can {i}not{/i} perform. Like, at all."

    if bonus == False:
        tb "And no matter how many times I tell him to put down the clarinet, he just refuses to do so."

    c "I...don’t really know what I’m supposed to say to that."

    if bonus == True:
        scene chikaonsen11
        with dissolve

    tb "Have you and your not-boyfriend made it that far yet, dear?"

    if bonus == True:
        c "We’ve done other stuff but...haven’t gone {i}all{/i} the way yet."
        c "We were kind of about to, but then my heart started going crazy and I wanted to take a minute or...thirty to prepare myself."
    else:
        c "We’ve done other stuff but...haven't played the clarinet yet..."

    if bonus == True:
        scene chikaonsen12
        with dissolve

    tb "Oh! This means I’ll get to be around for your first time! Splendid!"

    if bonus == False:
        tb "I've hidden clarinets in every room, so you'll surely be able to find one if you look hard enough!"

    tb "If you wind up wanting someone to talk to afterward, come over to my room. I’d love to hear all about it! Tsukasa and I are in #3."
    c "You want to...hear all about my first time?"
    tb "Of course! In vivid detail!"
    c "Tsubasa...are you actually a deviant?"

    if bonus == True:
        scene chikaonsen13
        with dissolve

    tb "What? No. Of course not. I just-"
    tb "Don’t normal girls like talking about things like that?"
    c "I mean...not in {i}detail{/i}. "
    tb "Oh dear. It seems I’ve said something horribly inappropriate then."

    if bonus == True:
        scene chikaonsen14
        with dissolve

    c "Pfft! It’s fine. No need to get all apologetic about it."

    if bonus == True:
        scene chikaonsen15
        with dissolve

    c "I’ll probably wind up spending the rest of the night with my not-boyfriend afterward, but I’ll definitely come visit if something changes."
    tb "So you’ve decided to follow through after all? It’s not an invasion of privacy for me to ask that much, is it?"
    c "Nah, you’re fine. "
    c "And yeah. I’m gonna do it."
    c "I love him, so-"
    tk "Do what?"

    if bonus == True:
        scene chikaonsen16
        with dissolve

    tk "What are you going to do with the man you love, Miss? He looks too old for you."
    c "Oh...Tsukasa. You’re here too..."
    tb "Tsukasa. Chika and I are talking about {i}adult{/i} matters right now. It’s not something you should be listening in on, dear."
    tk "I can listen. I’m an adult. Please, carry on."

    if bonus == True:
        scene chikaonsen17
        with dissolve

    c "I mean...I guess it’s fine as long as we leave out all the...explicit language, right?"
    tb "Whatever you’re more comfortable with, dear."
    tb "Even if it’s just talking about love in general, feel free to vent."
    tb "Being a mother is a full-time job for me, so I like to think I’m a pretty good listener."
    tb "Not that I think your mother has done a poor job, of course. She must be truly wonderful if she’s managed to raise a girl like you."

    if bonus == True:
        scene chikaonsen18
        with dissolve2

    c "…"
    c "Mhm."
    c "She did great."
    tb "…"
    tk "…"
    tb "Oh dear..."
    tb "I’ve said something insensitive again..."
    tk "What happened to your mother, Miss?"

    if bonus == True:
        scene chikaonsen19
        with dissolve

    tb "Tsukasa!"
    c "She’s not around anymore. "
    tk "So your father takes care of you all by himself?"
    c "He’s...not around either."
    tb "Tsukasa! Leave the two of us alone and I’ll have your father buy you anything you want!"
    tk "If your mother and father are both gone, who takes care of you? Your butler?"
    c "I take care of myself. I’m craaaaazy strong. Like a superhero."
    tk "Superheroes don’t exist. You should be old enough to understand that."
    c "Heheh~ Yeah, I guess I should."

    if bonus == True:
        scene chikaonsen20
        with dissolve

    tk "I do agree that you’re really strong, though."
    tk "If {i}I{/i} had to take care of myself, I’d eat nothing but candy. And Papa always says that candy makes you fat and ugly."
    tk "And you’re not fat and ugly at all, Miss. You’re almost as pretty as I am and I still have both of my parents!"

    if bonus == True:
        scene chikaonsen21
        with dissolve

    tb "Tsukasa! This is your final warning!"
    tb "Leave the two of us alone or we’ll be going home {i}tonight{/i} instead of tomorrow!"
    tk "Eek! Mother is angry!"
    tk "It was nice talking to you, Miss!"

    if bonus == True:
        tk "Have fun doing things I’m not old enough to talk about!"
    else:
        tk "Have fun playing the clarinet!"

    if bonus == True:
        scene chikaonsen22
        with dissolve

    "The youngest of the three leaps out of the water and heads back to her room, leaving the concerned mother alone with a makeshift orphan."
    "They bleed together."

    tb "I am...so sorry for her behavior."
    tb "She’s been a total troublemaker ever since she was born. I can’t even tell you how many of our maids have quit because of her."

    if bonus == True:
        scene chikaonsen23
        with dissolve

    c "It’s fine. Really. It’s my fault for tearing up anyway."
    c "This is supposed to be a getaway, not some place for me to bawl my eyes out in front of somebody else’s mom."
    c "Thanks for even taking the time to talk to me."
    c "It..."
    c "It helps."

    if bonus == True:
        scene chikaonsen24
        with dissolve

    tb "You don’t have to thank me at all, dear. It’s my pleasure. "
    tb "I’ll be more considerate in the future before saying things like that."
    tb "Now...back to the topic of love."

    if bonus == True:
        scene chikaonsen25
        with dissolve

    c "You’re really excited to talk about all this love stuff, huh?"
    tb "Can you blame me for wanting to hear about something I was never able to experience on my own?"
    c "Course not. I’m just not really sure where to start since my experience with “love” is just as limited as my experience with...the other thing."
    c "Like, I didn’t even receive my first confession until a few months ago."

    if bonus == True:
        scene chikaonsen26
        with dissolve

    tb "Your teacher confessed?! Chika, that’s wonderful!"
    tb "What are you waiting for?! Get back to your room and-"
    c "It was...actually a girl."
    c "A girl confessed to me."
    c "One of my friends."
    tb "…"
    c "…"

    if bonus == True:
        scene chikaonsen27
        with dissolve

    tb "…"
    c "…"
    tb "Perhaps I’m just too old to talk to [young]people anymore."
    tb "I’m making far too many mistakes for just one conversation."

    if bonus == True:
        scene chikaonsen28
        with dissolve

    c "You don’t have to blame yourself for that one. The way I said it was kind of misleading, I guess."
    c "I’m actually really glad you asked since I...haven’t really had anyone to talk about it with."
    tb "Well...if you’re fine with me continuing to make things horrible..."
    c "You’re not making anything horrible. This is actually really fun."
    tb "So...this {i}girl{/i} then...you said she was a friend of yours?"
    c "Yeah. We’ve known each other since middle[school]."

    if bonus == True:
        scene chikaonsen29
        with dissolve

    c "She’s really nice and super funny, but in like a...“not trying to be funny” sort of way."
    c "Like she’s a total nerd who talks way too much and makes herself look like an idiot and you kinda just wanna...hug her and pat her head."
    c "And she’s sooo pretty and like, doesn’t even realize it. It’s actually kind of annoying."
    c "But it’s not all good stuff. She has her problems too. "
    c "I mean, we all have our problems I guess. But hers just seem to come out of nowhere, so she can never even prepare for them."
    c "I don’t know if she knows that {i}I{/i} know that. But it’s kind of hard to not pick up on somebody’s tics after being around them for so long."
    tb "It seems to me like you really like this girl."
    c "I do. She’s amazing."
    c "And if she told me about it sooner, before I met the guy I’m here with today..."
    c "I probably would have given it a shot."
    tb "And this “guy.” Sensei? Is he aware of this?"
    c "…"
    c "Maybe?"
    c "Probably?"

    if bonus == True:
        scene chikaonsen30
        with dissolve

    c "I don’t know."
    c "I’d kind of prefer him to not get involved since it’s between her and me."
    c "If he knows, he knows. But it’s not like I’m going to vent to him about it when it will only make things more confusing than they already are."
    c "There are...a {i}lot{/i} of girls who seem to like him just as much as I do."

    if bonus == True:
        scene chikaonsen31
        with dissolve

    c "And I’m secretly a bitch, so I want to keep all of them as far away as possible."
    c "It’s better that things stay simple. "
    c "He’s not the type who likes drama so, if I can, I’m gonna avoid drudging it up by all means necessary. "
    c "He’s like, really protective of the other girl, so I don’t want to risk him trying to get the two of us together or anything like that."
    c "The more he thinks of me, the better. You know?"

    if bonus == True:
        scene chikaonsen32
        with dissolve

    tb "You really do love him, don’t you?"
    c "Sooooo much. Like, a gross amount of love."
    tb "Have you told him yet?"

    if bonus == True:
        scene chikaonsen33
        with dissolve

    c "Told him what? That I love him?"
    c "No...I mean..."
    c "I mean, he probably already knows."
    c "Right?"
    tb "He’s a man. He won’t know unless you tell him."
    c "I don’t know, Tsubasa. I feel like I make it pretty damn obvious."
    tb "Well...here’s a new question, then."
    tb "What are you waiting for?"
    tb "You want to keep those other girls away from him, don’t you? "
    tb "Wouldn’t telling him you love him help with that?"
    c "I feel like it could go either way. "
    c "Like, he’d either be really happy to hear it or he’d think I was moving too fast and try to distance himself from me."
    tb "Forgive me if this is one more thing I’m not fully comprehending due to lack of experience but-"
    tb "Do you really think you’d fall in love with someone who would run away after hearing that?"
    tb "Have some more faith in yourself. You’re a bright, beautiful [young_girl] with a great future ahead of you."

    if bonus == True:
        scene chikaonsen34
        with dissolve

    c "Tsubasa..."
    c "I really don’t know how to thank you for all of this."
    c "I’ve never been able to talk about stuff like this with anyone before...and that advice was like, exactly what I needed."
    tb "You don’t need to thank me at all, dear."
    tb "Just go back to your room and give the man you love that WAP."
    c "…"
    tb "…"
    c "…"
    tb "…"
    c "I’m sorry, what?"

    if bonus == True:
        scene chikaonsen35
        with dissolve

    tb "Did I not use that term correctly? "

    if bonus == True:
        tb "I often turn on the radio when I have time to myself. And I’ve been hearing that word thrown around by [young]people in sexual contexts."

    c "That’s..."
    c "I mean...you’re not {i}wrong{/i}...it was just a really weird time to say that..."
    c "I...I’m not sure how I feel about it."

    if bonus == True:
        scene chikaonsen34
        with dissolve

    tb "Well, whatever the case...I think we both know you’ve overstayed your welcome here."
    tb "The poor man is probably still up there waiting for you."
    tb "And, I’m sorry if this suggestion is insensitive-"
    tb "But if you wind up being too scared to follow through-"

    if bonus == True:
        scene chikaonsen36
        with dissolve

    tb "Or perhaps you just want to talk to a mother-"
    tb "You know where to find me."
    c "Yeah..."
    c "Probably sounds weird and corny, but like...I kinda feel like fate brought the two of us together today."
    c "I try my best but...not having my mom around to talk about stuff like this with can be really overwhelming."
    c "So hearing from you that I’m not just rushing into things is..."
    c "It’s a big help."
    c "Thank you."
    tb "I don’t know much about fate, but I {i}do{/i} know that I’m happy to have helped you. "
    tb "It’s okay to be scared. And it’s okay to worry about things like this."
    tb "But if {i}you{/i} think you’re ready for your first time...and {i}you{/i} think you’re ready to tell the WAP man you love him-"
    c "Please don’t call him the WAP man, Tsubasa."
    tb "Then all you need to do is follow your heart."
    c "Yeah..."
    c "Yeah. I think this bath has gone on for long enough."
    c "Are you getting out, too?"
    tb "Oh, heavens no. The longer I can relax and not have to deal with Tsukasa, the better."
    tb "Good luck, though."
    tb "I’ll be here if you need anything."

    scene black
    with dissolve2

    "Sometimes, bleeding freely {i}isn’t{/i} ideal."
    "Sometimes, it’s better to have someone there beside you, holding your wound closed and making sure bacteria doesn’t find its way in."
    "Someone to apply a tourniquet."
    "Relying on people like that is fine if you find yourself caught in a pinch."
    "Does it make you stronger? No."
    "But it doesn’t make you weaker either."

    stop music fadeout 10.0

    "Be happy!"
    "Find your place in the world!"
    "And if one does not exist, create your own!"
    "Just know-"
    "That even if everything goes according to plan-"
    "And all of the puzzle pieces in all of your world fit into place-"
    "You will still bleed."

    "{i}Chika has acquired a new mother!{/i}"
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ chikaonsen2 = True

label chikaonsen3:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```