# That One FMK Scene
Noriko event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=convenience25&go=Go)



## Event preconditions
✅Noriko love greater than or equal to 25

✅Event "[Noriko: Homes for the Homeless](./norikodorm20.md)" is completed (event=norikodorm20)



## Next events
* [Noriko: Loxosceles Reclusa](./norikodorm25.md)

## Event properties
* ID: convenience25
* Group: Noriko
* Triggered by label: convenience
* Triggered by branch label: afterschoolmenu

## Event code
File: \game\NorikoEvents.rpy
Code:
```python
...
label convenience25:
    scene thatonefmkscene1
    with fade
    play music "noriko.mp3"

    "I make my way across town and over to the convenience store because, apparently, I feel like punishing my legs for simply existing."
    "Could I have taken the bus? Yes. But buses are overcrowded with weird people this time of night- and god forbid someone lumps me in with one of them."
    "I’m a totally normal guy with totally normal hobbies and interests."

    if bonus == True:
        "Anyway, here are two [teenager]s who want to have sex with me that I am now going to hang out with."

    s "Hello, normal human [teenager]s."
    n "Hello, normal human teacher."
    ki "Hello, really fucking weird powercouple from like six million years ago."

    scene thatonefmkscene2
    with dissolve

    n "Would it kill you to just go with the flow every once in a while, Kirin?"
    ki "When this flow involves making myself sound like an idiot, yeah. Yeah, I think that would kill me, Noriko."
    s "Sorry, Noriko. It looks like we’ll have to speak normally so Kirin can be included in this conversation."

    scene thatonefmkscene3
    with dissolve

    if bonus == True:
        ki "Hooray! Now I get to hear you two flirt with each other more instead of just going into the bathroom and banging it out like we all know you want to."
        s "I mean, I’m game if Noriko is."
        n "I don’t think you wanna bang one out in the bathroom, Sensei. This is a convenience store in the old district. It probably hasn’t been cleaned in ages."
        s "Isn’t...cleaning it part of your job?"
        n "Probably. But it’s not like I really {i}need{/i} this job, sooooo..."

        scene thatonefmkscene4
        with dissolve

        n "Maybe we could use the walk-in, though?!"
        n "It’s full of drinks and stuff right now, but since most of them are still boxed, it gives us plenty of options for different surfaces to repopulate the planet on."

        scene thatonefmkscene5
        with dissolve

        n "Oh, sorry! Did I say repopulate the planet? What I really meant was to repopulate the planet. No- to repopulate the planet. No, I mean-"
        ki "Seriously, if you’re going to be this horny all the time, just take the fucking plunge."
        ki "Do you have any idea how exhausting it is having to deal with this when losing your virginity is even easier than opening up a pickle jar?"

        scene thatonefmkscene6
        with dissolve

        n "You just have weak hands. Opening a pickle jar really isn't hard."
        ki "Yeah, and neither is getting fucked. So just shut up and screw the teacher already."
        n "You lost your virginity in a love hotel and then cried for hours once you came back to the dorm."
    else:
        n "Maybe. But Kirin is a loser who cried for the entire night after the two of you went bowling together."

    scene thatonefmkscene7
    with dissolve

    ki "I did not {i}cry!{/i}"
    s "You cried?"

    scene thatonefmkscene8
    with dissolve

    ki "No! Are you even listening?!"
    n "Sensei, I know it may not seem all that impressive to you, but I have never in my life struggled when it comes to opening a pickle jar."

    if bonus == False:
        "I don't know why Noriko just decided to tell us that, but I am proud of her regardless."

    s "That’s actually very impressive. Even I’ve struggled with that before."
    n "Well then it looks like you could use a trusty ole’ Noriko around the house full time, huh?"
    ki "Don’t just ignore me! I didn’t cry!"

    scene thatonefmkscene9
    with dissolve

    if bonus == True:
        n "Yes, Kirin. You are very strong and brave and independent and would never cry over something like prematurely giving away your virginity in some random motel you can’t even remember the name of."
        ki "I..."

        scene thatonefmkscene10
        with dissolve

        ki "I...don’t even think it had a name..."
        n "You don’t remember the name of the motel where you deflowered my roommate, do you?"
        s "I don’t like when you ask me questions like that with a smile on your face. And I like it even less knowing there’s probably a knife in your pocket."
        n "How else am I going to defend myself if I get attacked on the way home?"
        n "If anything, I think that {i}all{/i} [teenage]girls should carry knives with them at all times."
        n "Do you have any idea how drastically that would impact the amount of both reported and {i}un{/i}reported sexual assaults?"

        play sound "static.mp3"
        scene yumi14 with flash
        scene mikuthighs25 with flash
        scene lavendersgreen26 with flash
        scene thatonefmkscene10 with flash
        stop sound
    else:
        n "Yes, Kirin. You are very good at bowling and Sensei didn't absolutely destroy you when you two went out together."

    s "Let’s talk about something else."

    if bonus == True:
        ki "Agreed. Something that has absolutely nothing to do with virginity or...knives or whatever."
    else:
        ki "Agreed. Something that has absolutely nothing to do bowling or whatever."

    scene thatonefmkscene11
    with dissolve

    n "Do you want to go hang out outside? The fire’s probably still going."
    s "Fire? In a residential area?"

    scene thatonefmkscene12
    with dissolve

    ki "Are you a cop or something now?"
    n "Residential areas are the best place to start fires."
    n "Besides, it’s safely contained in a trash can. And if there’s anything I’m confident about, it’s starting and maintaining fires."
    s "I don’t really think that’s a good thing to be confident about."

    if bonus == True:
        n "The only thing {i}Kirin’s{/i} confident about is her ability to perform fellatio."
    else:
        n "The only thing {i}Kirin’s{/i} confident about is her ability to tip over cows without getting hurt."

    ki "There are...other things."
    s "Like?"
    ki "…"
    ki "You know."
    ki "Stuff."
    s "Well, I’m glad you’ve found at least {i}one{/i} thing you can be passionate about."

    scene thatonefmkscene13
    with dissolve

    ki "Same."
    n "…"
    n "Uhh..."
    n "I just want to take a second to remind you guys of the poor conditions of the bathroom and suggest that maybe you {i}don’t{/i} look at Sensei that way."
    ki "What way? This is just how I look at Sensei."
    n "Yes, Kirin. That is exactly the problem."

    scene thatonefmkscene14
    with dissolve

    if bonus == True:
        ki "Jesus Christ, Noriko! Just fuck him already! Things would be so much more exciting in this group if you’d just fucking catch up so we can have threesomes and stuff!"
    else:
        ki "Jesus Christ, Noriko! Just fucking tip one over yourself already if you're going to keep getting jealous!"

    n "I will! Soon!"
    s "You will? When?"

    scene thatonefmkscene15
    with dissolve

    n "Woah! It’s suddenly time for my break! Who could have foreseen such an inconvenient ceasefire to a conversation I was definitely prepared to have tonight?!"

    if bonus == True:
        ki "I’m starting to think you secretly have a dick and you’re just afraid to fuck Sensei because he’ll find out about it."
        s "If I were Noriko, I’d be more worried about {i}you{/i} finding out about it."

        scene thatonefmkscene16
        with dissolve

        ki "True. Noriko having a dick would solve virtually all of my problems."
        s "What would Noriko having a penis do for your inferiority complex?"

        scene thatonefmkscene17
        with dissolve

        ki "Ha."
        n "Noriko doesn’t have a penis! And Noriko is going outside to hang out by the fire now!"
        ki "Kirin is following."
        s "And I am refusing to talk in the third person, but I will follow you two regardless as I have nothing else to do and nowhere else to be tonight."
    else:
        s "Kirin. Noriko is a vegetarian. She does not want to harm farm animals the same way you do."

    scene black
    with dissolve2

    "Noriko flips the open sign around and locks the door before leading the two of us through a small store room and into an alleyway."
    "It’s the exact sort of alley you’d expect to see in the worse half of town, filled with trash bags, broken bottles, and rats (Both dead and alive)."
    "And while I’d like to say that I’m surprised Noriko is okay with hanging out around stuff like that..."
    "I’m really not."
    "In fact, I’m {i}not{/i} surprised to say that she doesn’t seem fazed by them at all."
    "And as she steps over the carcass of an animal that was once filled with life, I’m reminded once again of how truly unique and...overwhelmingly strange she is."
    "………"
    "……"
    "…"

    scene thatonefmkscene18
    with dissolve

    n "Oh, sweet! We’re just in time for Nee-chan’s interview!"
    s "Interview?"
    n "She’s appearing on some variety show tonight to promote her next album."
    n "It’s really cool that she still does stuff like this even though it’s gotten to the point where just...slapping her name on something will guarantee it sells out in minutes."
    ki "Noriko, I’ve said this before and I’ll say it again now."
    ki "I want your sister to do things to me."
    n "She’s so pretty, isn’t she?"

    if bonus == True:
        s "You seem weirdly okay with Kirin wanting to have sex with your sister."
        n "Well, I’m weirdly okay with her wanting to have sex with the guy I’m in love with and that is a significantly worse thing to accept."
    else:
        s "You seem weirdly okay with Kirin wanting to hug your sister."
        n "It's just a hug. It's not like it really matters."

    s "Fair point."

    scene thatonefmkscene19
    with dissolve

    if bonus == True:
        n "Besides, when you’re the little sister of a celebrity, you get used to how many people wack off to her."
        n "I had to set all of my social media accounts to private just so people would stop sending me cum tributes of her."
        n "Do you have any idea how many ugly looking dicks there are out there, Sensei? Because it’s a lot."
        s "Thank you for informing me, Noriko. I’m sure this information will be vital at some point."
        ki "Have you really fucked this girl, Sensei?"
    else:
        n "Besides, when you’re the little sister of a celebrity, you get used to how many people want to hug her."
        ki "Have you really hugged this girl, Sensei?"

    scene thatonefmkscene20
    with dissolve

    if bonus == True:
        s "{i}Actually{/i}, Kirin. No. No, I have not."
        ki "You fucked {i}me{/i} before an idol? Cool."
        ki "Seriously, though. Stop waiting. Hurry up and fuck her."
        n "Kirin..."

        scene thatonefmkscene21
        with dissolve

        ki "Oh. Right."
        ki "Yeah, nevermind. Maybe don’t fuck her yet. I don’t know."
    else:
        s "Uhhhhhhhhh maybe?"

    scene thatonefmkscene22
    with dissolve

    tv "Hello and welcome back! If you’re just tuning in now, {i}boy{/i} do we have a surprise for you."
    tv "Joining us today is the one...the only...Niki Nakayama, here to promote her new album, “Watermelon Fantasy!”"
    ni "Hihi! Thank you all so much for inviting me back! It’s been a while since I’ve done anything like this...so I’m really, {i}really{/i} nervous..."
    ni "If any of you are watching at home, I hope you’re cheering me on! It might be hard, but I’ll do my best! Teehee~"
    s "She sounds completely different on television."
    n "That’s just her idol voice. She switches back and forth so easily at this point that it’s kind of absurd."
    tv "So, Niki...Can you tell us a little more about this new album? There’s been a lot of buzz lately about some of the singles being a little more...{i}serious{/i} than what your fans are used to."
    ni "Hmmm...I don’t think any of the songs are any more or less serious than the rest of my music!"
    ni "I’m still the same Niki I’ve always been...and I’m putting just as much heart into my music as I have in the past."
    tv "I’m glad you brought that up! Because it seems like “the past” has been a theme in your music since your debut- but no one really knows anything {i}about{/i} that past."
    ni "…"
    ni "Is there a question there, or...?"
    tv "I was just hoping you’d be able to tell us more about your origins. What was the “old” Niki like? And this...man you’re always talking about in your songs-"
    ni "Completely made up and not real at all. Next question, please."
    tv "O-Oh! Okay then! For my next question, I’d-"
    ni "Oh no! I’m so, so sorry! But I just remembered I have something {i}super{/i} important I have to do back in the studio!"
    tv "If you could just answer this last-"
    ni "Anyway! Thanks for listening, everyone! Make sure to buy Watermelon Fantasy!"
    tv ".................Aaaand, I suppose we’ll be right back after these messages from our sponsors!"

    scene thatonefmkscene23
    with dissolve

    n "Oh, Nee-chan..."
    ki "Is that it? That was the whole interview?"
    n "She gets a little nippy when people ask about stuff from the past."
    n "But, in her defense, one of the stipulations in her contract for appearances like this is avoiding topics that could cause her to talk about it."

    scene thatonefmkscene24
    with dissolve

    n "Idols are supposed to be sort of like...idealized humans. And once that illusion is shattered and people start to realize they’re just...normal girls at heart, their popularity starts to fade."
    n "Nee-chan’s already a lot older than most other idols out there, so she needs to hang on really tightly even if she’s leagues ahead in popularity."
    ki "Huh. You know a lot about that sort of thing, don’t you?"
    n "I’ve been working as an assistant of hers since she started. You just kinda...pick up on stuff after a while."

    scene thatonefmkscene25
    with dissolve

    n "You should tune into one of the streams sometime, Sensei!"
    n "People who donate exorbitant amounts of money can even try to have Niki read their comments out loud! Imagine how she would feel if you were one of those people!"
    s "How exorbitant are we talking here?"
    n "So exorbitant that I probably shouldn’t even say it out loud."

    if chikalust20 == True:
        ki "I think Sensei’s been a little busy making guest appearances on {i}other{/i} streams in order to watch any of Niki’s anyway."

        scene thatonefmkscene26
        with dissolve

        n "Hm? What other streams?"
        s "Yeah, am I supposed to understand what you’re talking about here? Because I don’t."
        ki "So you {i}didn’t{/i} give Chika the go ahead to stream one of your recent sexual encounters?"

        scene thatonefmkscene27
        with dissolve

        n "Uhhhhhhhh what?"
        s "Yeah...{i}what?{/i}"
        ki "During the beach trip. She started live streaming in the middle of the night while I was hanging out with Miku."
        ki "And I’ve heard enough dick sucking in my time on the Internet to recognize it when I hear it."
        s "…"
        n "…"

        "{i}She was recording that?{/i}"
        "I mean, I know she sent me a picture, but..."

        ki "If you’re worried about anyone else seeing or hearing it, I wouldn’t."
        ki "It was a pretty busy night for everyone and I {i}think{/i} it was only Miku and I who caught it before she deleted it."
        ki "And even then, Miku had no idea what was happening."
        ki "So, at least for now, it looks like your secret’s safe with me. And Noriko too, I guess."
        n "I mean...it could have been something else?"
        s "Yeah. It was definitely something else. I have no idea what you’re talking about."
        n "See? Your perverted mind probably just...found something that didn’t exist or whatever because that’s what you wanted to hear."

        scene thatonefmkscene28
        with dissolve

        ki "Then how about we play a little game and see if we can figure out if there {i}is{/i} any more to our lovable teacher’s relationship with Chika."
        n "Game? What kind of game?"

    else:
        n "Oh! And Chika shows up in there sometimes! I’ve definitely seen her name floating around in the chat before."
        n "She {i}really{/i} likes the heart emoji."

        scene thatonefmkscene29
        with dissolve

        if bonus == True:
            ki "She’s probably gotten off to Niki more often than {i}you{/i} have, and chances are she's actually sucked your dick before."
            s "Niki? Or Chika?"

            scene thatonefmkscene30
            with dissolve

            ki "I was {i}referring{/i} to Niki. But if there’s something going on between you and the friendly neighborhood gyaru, I’d be interested in hearing about it."
            ki "At the very least, it would make that possessive little demonstration of hers during the Halloween party make a lot more sense."
            n "…"
            s "I’m not admitting to anything. I just wanted some clarity so I could better understand what you were talking about."
            ki "Reaaaaaaaally?"

            "Obviously not. But I’m not going to come out and say, “Yes. I regularly receive oral sex from the girl who sits next to Noriko,” when Noriko looks like {i}that.{/i}"

            s "Really. Now, let’s move on."
        else:
            s "Oh! I have a fun idea. How about we all talk about our favorite emojis?"

        scene thatonefmkscene28
        with dissolve

        ki "Actually! How about we play a little game instead?"
        n "Game? What kind of game?"

    scene thatonefmkscene31
    with dissolve

    if bonus == True:
        jump fmkx
    else:
        ki "Hopscotch!"
        ki "I drew a bunch of squares with sidewalk chalk while the two of you weren't paying any attention."
        s "I hope you know that I used to be the hopscotch champion back in elementary school."
        ki "Are you challenging me, Sensei?"
        n "What does the winner get?"
        ki "The winner gets to hug Sensei."
        s "But what if I win?"
        ki "You have to hug yourself, obviously."
        s "But that is so lonely..."

        scene black
        with dissolve2
        stop music fadeout 10.0

        "The three of us proceed to play a friendly game of hopscotch, but I am unable to win because Kirin kept throwing cans of soda at me as I was trying to jump."
        "Noriko lost before me, though, since she didn't understand the rules and started treating it like a game of Twister."
        "Fucking amateur."

        ki "Take that, Sensei!"
        s "Kirin the game is over."
        ki "Oh, sorry."

        $ renpy.end_replay()
        $ convenience25 = True
        $ kirin_love += 1
        $ noriko_love += 5
        $ chikakill = True
        $ norikomarry = True

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "………"
        "……"
        "…"

        jump kirinspecial25
...
```

## Code that triggers this event
File: \game\NorikoEvents.rpy
Code:
```python
...
label convenience:
    if noriko_love >= 0 and norikofirsthall == True and convenience1 == False:
        jump convenience1
    if noriko_love >= 5 and norikodorm5 == True and mollydorm15 == True and convenience1 == True and convenience5 == False:
        jump convenience5
    if noriko_love >= 25 and norikodorm20 == True and convenience25 == False:
        jump convenience25
...
```