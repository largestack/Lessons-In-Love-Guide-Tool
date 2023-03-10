# Three Afloat On One Raft (Maki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Food Groups](./day351.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Maki: Thank You For Your Business](./makidate15.md)

## Event properties

* Id: makiday351
* Group: Maki
* Triggered by label: dressingafter
* Chain sources: day351
* Chain sources path: day351->day351->dressingx

## Official wiki page

[Three Afloat On One Raft](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makiday351&go=Go) for more details.

## Event code

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
label makiday351:
    scene makimalldate1
    with dissolve
    play music "mall.mp3"

    s "So...what exactly was it you wanted to talk to me about?"

    "Maki and I walk silently through the halls of the mall for a short while and I can’t help but notice her looking a little distracted."
    "I don’t know if that’s just her tell for wanting me to buy her something but, if it is, she is in for a very rude awakening."

    if bonus == True:
        maki "Nothing in particular. I just figured you’d rather be spending time with someone who’s actually your age than following around a bunch of [teens]."
        s "…"

        scene makimalldate2
        with dissolve

        maki "It’s one thing to fill up on[teen]porn but, as a former [teenager] myself, I can confirm that almost all of them are confusing and irritating and-"
        s "Exhausting."
        maki "Yes. That as well."

        scene makimalldate3
        with dissolve

        s "Are you sure it’s okay to be saying that when you have a [teenage]daughter, though?"
        maki "Are you afraid she’ll jump out from behind a mannequin and call me a bad mother or something?"
        s "Well it’s not like you two really have the best relationship to begin with, right?"
    else:
        maki "Nothing in particular. I just confused you for someone else and, by the time I realized who you were, it was too late to back down."
        s "Oh."
        s "Anyway, how are you and Makoto?"

    scene makimalldate4
    with dissolve

    maki "Makoto and me? I think our relationship is great."
    maki "It’s true that I have a hard time deciding how to tackle certain things, but as long as I have you as my stand-in husband until mine stops fucking aliens, I think everything will turn out just fine."
    s "Woah there. I never agreed to this whole “stand-in husband” thing."

    scene makimalldate5
    with dissolve

    maki "Not five minutes into our marriage and you’re already asking for a divorce? "
    maki "Is it because you have to go to space? Because I’m already used to that and don’t mind at all."

    if bonus == True:
        maki "Enjoy your alien sex."
        s "Every day, your existence somehow manages to make me even more impressed by the head your daughter has on her shoulders."
        maki "Well as long as it’s up there and not pressed between someone’s knees, I’m totally happy."
        s "I would like to take this opportunity to reiterate my previous statement."
    else:
        s "I thoroughly enjoy it when you make jokes about your husband disappearing and abandoning your family to hug aliens."

    scene makimalldate6
    with dissolve

    maki "Jokes aside, I’m glad that Makoto seems to be going back to her old self as of late."
    maki "Actually, strike that. She seems truly happy for the first time since her father left as of late."
    s "Really? Because she kind of suffered a crushing defeat during her dorm wars contest thing and I thought it might get to her."

    scene makimalldate7
    with dissolve

    maki "Did you talk to her about it?"
    s "I didn’t see any reason to. That’s not something I should really get involved in."
    maki "Well {i}I{/i} did, so ha."
    s "Wow. Look at you being a real mom."
    maki "I’ll have you know there’s not any minute of any day that I’m not a mom before anything else."
    maki "It’s just a little difficult when your child imprints on your significant other instead of you."

    scene makimalldate8
    with dissolve

    maki "But I digress."
    maki "Makoto’s knowledge test thing crashing and burning may have even been good for her in a way."
    maki "I don’t want to call it a wake up call or a...rude awakening or...any other phrase that involves waking up-"
    maki "But it’s kind of good to get the shit kicked out of you every once in a while."
    s "Are you asking me to mug your daughter?"
    maki "You’ll have to go through me first, Sensei."

    if bonus == True:
        s "That doesn’t sound very hard."
        maki "We’d probably get turned on while wrestling and wind up taking each other’s clothes off."
        s "You know, maybe I {i}will{/i} mug your daughter after all."
    else:
        s "I will destroy you, Maki Miyamura. I know at least three cool karate moves."
        s "Hi-ya."

        "I show her one of my cool karate moves. She is very impressed."

    scene makimalldate9
    with dissolve

    maki "Ahh, the things we do for love."
    s "Please don’t love me. There is not a single person we know who would approve of this relationship."
    maki "Miku might."
    s "Miku is on Team Makoto now."
    maki "As in she’s rooting for you to fall in love with my daughter?"
    s "It appears that way."

    if bonus == True:
        maki "It appears that a spanking may be in order then."
        s "For me or for Miku?"
        s "I don’t really want to be spanked."
        maki "That’s what my actual husband thought at first."
        s "Be careful. Anything you say right now may one day be used against Makoto to embarrass her in front of class."
    else:
        maki "I am not too worried about that. Makoto was born with a tragic disease that causes her to immediately explode if she ever falls in love."
        s "As her teacher, this is something I should have been informed about. "
        maki "I didn't want to embarrass her."
        s "It may be too late for that. I am going to tell everyone so they can properly prepare themselves in the event of her demise."

    scene makimalldate10
    with dissolve

    if bonus == True:
        maki "Oh please. She’s such a daddy’s girl that she could have walked in on me spanking him and still pinned the whole thing on me just...being too dominant."
        maki "But to everyone's surprise, I'm actually an innocent and pure sub at heart."
        s "Yeah, I don’t believe that for one second."
        maki "…"
        s "…"
    else:
        maki "Have you ever touched a deer? They are very soft."
        s "Are they? I had no idea."
        maki "My mom gave birth to one shortly after me. It was on the news and everything."
        s "I do not believe this."

    scene makimalldate11
    with dissolve

    maki "Okay, fine. I was lying. "

    if bonus == True:
        maki "But in my defense, being dominant is basically where all of my experience is. "
        maki "I haven’t really gotten many chances to play out any of my submissive fantasies because of my husband’s love for spanking and petplay."
        s "Having someone like you as a pet does sound like it would have its perks."
    else:
        maki "Or was I?"
        s "So...was he like, just a regular member of the family after that? I don't understand the lineage her."

    maki "Oh, no. He was the pet."
    maki "We had a leash and everything."
    s "…"
    maki "…"

    scene makimalldate12
    with dissolve

    s "Anyway."

    if bonus == True:
        maki "I’m sorry, Makoto. It looks like your classmates may soon find out that your father had a very different side than the one you grew up with."
    else:
        s "I don't think I want to talk to you anymore."

    scene black
    with dissolve2

    "Maki and I do a lap or two around the mall and manage to avoid contact with the group of girls I split up with earlier."
    "I’m not sure if the three of them have already gone home, but it’s starting to get dark and Maki is showing no signs of ending our gathering just yet."
    "I pull out my phone to text Ami about missing dinner but realize that she’s likely still with Ayane anyway-"

    if bonus == True:
        "So it looks like I’ll be able to dodge all suspicion entirely tonight and get to continue hanging out with a MILF."
        "Nice."
    else:
        "Darn it. This means I have to keep hanging out with Maki."

    scene makimalldate13
    with dissolve

    maki "Hey...can I ask you something?"
    s "You’re just going to ask anyway, aren’t you?"
    maki "Yeah. You said something that kind of made me upset earlier and I wanted to bring it up again before I hate myself for letting it go."
    maki "You don’t actually think I’m a bad mother, do you?"
    maki "Because I’ve exhausted pretty much every resource available for Makoto. She’s just too annoyingly smart to really {i}need{/i} someone like me."
    s "I didn’t really mean that. I was just using your words against you, really."
    maki "I don’t remember ever calling myself a bad mother. That hurt."
    s "No. But you said that you might try to approach things more like a friend at times. "
    s "And there’s also the issue of your...complicated relationship dynamic with your husband."

    if bonus == True:
        maki "Spanking your husband makes you a bad mom?"
        s "What? No. The whole open relationship thing."

    maki "What does that have to do with Makoto?"
    s "Well...can you really say her environment was “normal” growing up?"

    scene makimalldate14
    with dissolve

    maki "I can, actually."
    maki "Do you think we let her run around the store and use vibrators as rattles? Let her watch gangbang videos in the backroom while we kept an eye on the front?"
    maki "Do you think she was present for all of the times her father insisted on bringing a new girl home?"
    maki "Or do you think I, as a competent but slightly confused mother, would have kept my little girl away from that as best as I could?"
    s "I think that Makoto is perceptive enough to figure things out even when they’re not right in front of her."
    s "And I think that she’s the type of person to measure her circumstances against those of others to try and figure out what “normalcy” is."
    maki "So I’m a bad mother because my daughter is a genius?"
    s "I already told you I didn’t mean that."
    maki "Well then apologize. "
    s "…"
    maki "…"

    scene makimalldate15
    with dissolve

    maki "Hey. If you’re going to be my stand-in husband, you’re going to have to realize when you’re in the wrong."
    s "I never agreed to-"
    maki "You don’t have to. Makoto’s already chosen you as her stand-in daddy, so now it’s all on you to live up to it."
    s "…"
    maki "…"

    if bonus == True:
        s "Can you call me daddy again please?"
        maki "Daddy."
        s "A little softer this time."

        scene makimalldate16
        with dissolve

        maki "{i}Daddy...{/i}"
        s "Now do it like you’re about to cum."

        scene makimalldate17
        with dissolve

        maki "Ahh! Daddy! Yes! Yes!"
        s "Wow."

        scene makimalldate18
        with dissolve

    maki "Teehee~"

    if bonus == True:
        s "There are a bunch of people looking this way now."
        maki "Of course there are. I just came on a bench in a mall."
        s "Did you actually-"

        scene makimalldate19
        with dissolve

        maki "God, no. If it were that easy, I’d literally never leave home. "
        s "Well it was very convincing and I hope for your husband’s sake that he never fell victim to your deceit."
        maki "If he knew the amount of times he’d been deceived, I really {i}would{/i} need a new husband."
        s "I’ll be sure to keep it a secret if he ever returns from the alien orgy."

        scene makimalldate20
        with dissolve

        maki "{i}If{/i}, huh?..."
        s "Oh. I didn’t mean it like-"
        maki "No, no. I get it. I just don’t like hearing it out loud."
        maki "The truth is that...and don’t tell Makoto I said this-"
        maki "But...I don’t really want to wind up waiting forever."
        maki "I miss my husband. I really do."
        maki "But there’s a point where you have to sort of just accept that things might not turn out how you wanted them to turn out."
        maki "It’s painful not hearing from someone for years. Especially someone you spent so many years {i}with{/i}."
        maki "But I can’t do everything on my own."

        scene makimalldate21
        with dissolve

        maki "I’m not like Sara or Haruka. I’m willing to accept my shortcomings and don’t want them to weigh me down."
        maki "I’ve got a genius daughter to take care of. And, like you said earlier, she’s perceptive enough to realize things I don’t want her to."
        maki "The second I start killing myself by working even harder is the second she starts killing herself as well."
        s "Well-"
        s "And this isn’t me agreeing to be Makoto’s new father-"
        s "But I’ll wind up supporting you in whatever you decide to do."
    else:
        s "Makoto is my student and I have no intention of making any adjustments to our relationship at any point."

    scene makimalldate22
    with dissolve

    maki "Oh my God. Did you just agree to become Makoto’s new father?"
    s "Maki, I specifically stated-"

    scene makimalldate23
    with dissolve

    if bonus == True:
        maki "Makoto’s going to be so happy that she won’t even mind hearing me yell “Daddy” over and over from the back room all night!"
        s "No, I very much think she would mind that."
    else:
        maki "Makoto is going to be so happy."
        s "Maki no."

    scene makimalldate24
    with dissolve

    maki "Thank you, Sensei."
    maki "Not for the father thing, but for the support. "
    maki "You’ve done so much for Makoto and me in such a short time that I can’t help but feel like we owe a lot of ourselves to you."

    if bonus == True:
        s "Is that-"

        maki "For once, I don’t mean that sexually."

        "Damn it."

    maki "I mean that, in some way or another, you just being you is enough to keep Makoto afloat."
    maki "And Makoto being afloat means that I get to be afloat."
    maki "And before we know it, we’re all on the same raft together."

    if bonus == True:
        maki "Floating past nudist colonies and shielding that pure girl’s eyes from the things you and I as perverts see in our dreams."

        "I’m glad that Makoto is also smart enough to not reveal to her mother that she’s in an ongoing illicit relationship with her teacher."
        "I figure that must be difficult to do, but so many of my students are missing parents that it’s honestly hard to say."

    scene makimalldate25
    with dissolve

    maki "I’m not suggesting anything here, but..."
    maki "Even if my husband does wind up coming back, I hope you’ll stick around."
    maki "If not for me, then for Makoto."
    maki "She really needs you."
    s "…"
    s "I’ll see what I can do."

    scene black
    with dissolve2

    "Of course I have no intention of just skipping town and abandoning the Miyamuras...but it’s not like I could even if I wanted to."
    "The truth is that even though Maki and Makoto couldn’t be further apart in terms of personality, they’re still two of three cerberian heads. "
    "The third, however, has been severed and is now floating somewhere out in space."

    if bonus == True:
        "Maybe fucking aliens, maybe not."
        "There’s no way of knowing."
        "But at least I know that the other two heads are [[probably] safe for the indeterminate future."

    $ renpy.end_replay()
    $ makiday351 = True
    $ maki_love += 1
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makidate15:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
f "Huh?...Oh! Sorry...I’m just trying to figure out who she reminds me of..."

    scene impromptumalltrip42
    with dissolve

    maki "Maki Miyamura. I’m Makoto’s mother."
    f "Oh! That’s it!"
    f "It’s so nice to meet you. I’m Futaba, a classmate of hers."

    scene impromptumalltrip43
    with dissolve

    if bonus == True:
        maki "And you? With the surprisingly nice rack?"
    else:
        maki "And you? With the surprisingly nice skin?"

    u "Oh..."
    u "Uta Ushibori. It’s nice to meet you."

    scene impromptumalltrip44
    with dissolve

    maki "You really lucked out with {i}this{/i} class, huh?"
    mi "Sensei’s a hot commodity and has tons of girls just throwin’ themselves at him! "

    if bonus == True:
        mi "It’s crazy he hasn’t been fired yet!"
        maki "That just means he’s doing his part as a responsible adult and not acting inappropiately toward girls out of his age group."
        s "Correct me if I’m wrong, but I distinctly remember Nodoka and you having an in-depth conversation about anal sex at the bar recently."
        maki "Heh. You used “in-depth” and “anal” in the same sentence."
        f "I...suppose Makoto inherited only her mother’s looks and not her personality."
    else:
        mi "Unfortunately for all of 'em, all he ever wants to do is hug!"

    maki "Are you free right now, by any chance?"
    s "I...think so?"
    s "I came here to-"

    if bonus == True:
        mi "Watch us strip!"
    else:
        mi "Steal jewelry from JC Penny with all of us!"

    s "{i}Help you choose clothing.{/i} But now that it’s done, I think I have some time to spare."
    maki "Perfect. Because I’ve actually been wanting to talk to you about something lately and this seems like too good of an opportunity to just let it slip."

    if bonus == True:
        maki "Heh. Slip. Like from being wet."

        scene impromptumalltrip45
        with dissolve

        mi "Ah! I get it now! {i}That’s{/i} the kinda wetness you guys were sayin’ is dirty!"
        mi "I’m gonna have to wash my mouth out, aren’t I?!"

    scene black
    with dissolve2

    "Maki quickly whisks me away and the two of us part ways with the girls I came here with."
    "I feel a little rude about leaving them behind just as it seemed that Uta was about to try and make new plans-"
    "But I see all of them basically every day."
    "And, like Maki said, this opportunity seemed too good to just let slip."
    "………"
    "……"
    "…"

    scene impromptumalltrip46
    with dissolve2

    u "…"
    u "…"
    u "…"
    mi "Uta? You comin’ with us? Or are you just gonna stand there like a weirdo?"

    scene impromptumalltrip47
    with dissolve

    u "Oh! Hahah!"
    u "Must’a zoned out for a second!"
    u "What do you guys wanna do now?"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ day351 = True
    $ uta_love += 1
    $ miku_love += 1
    $ futaba_love += 1
    stop music fadeout 9.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump makiday351
...
```