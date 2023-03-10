# Torrential Downpour. Child of Man. (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Alderaan](./secondbeach9.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: secondbeach10
* Group: Main
* Triggered by label: secondbeach9
* Chain sources: secondbeach9
* Chain sources path: secondbeach9

## Official wiki page

[Torrential Downpour. Child of Man.](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach10&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach10:
    scene childofman1
    with dissolve2
    play music "sleepsong.mp3"

    "The stars sink into the sea sometime after the sky goes to sleep."
    "It’s silent."
    "But I find solace in the sensation of sand on the soles of my shoes."
    "And while the slight semblance of my soul slips into the surface, it still seems as if a siren song is summoning me forward."
    "So I go."
    "I go. I go. I go. I go. I go."
    "But where?"
    "And when did the sun set? "
    "{i}Why{/i} did the sun set?"
    "And who is the siren?"
    "I press my hands together and glance down to see my fingers interlocking with one another, emulating the sensation of something I have not felt in quite some time."

    if bonus == True:
        "Of course I’ve felt flesh on flesh- but not in a way that amounted to any more than just that."

    "Even those I am closer with than I am to my own reflection mean nothing when there is a complete lack of understanding."
    "And if there is anything I understand, it’s that."
    "Everything else is ephemeral. "
    "It’s gone just as quickly as it appears."
    "Whether it be a night sky or a trip to a beach, it all fades into nothingness and leaves a trail of destruction clinging to life behind it as it goes."
    "It goes. It goes. It goes. It goes. It goes."
    "But where?"
    "And when did I become someone whose silhouette does not attach itself to the shoreline?"
    "No shadow on the ground nor reflection in the water."
    "Typical."
    "I replace “ephemeral” with “ethereal” in my head and let the winter air, laced with water droplets from waves I can’t even see, jump onto my skin and my shirt."
    "It somehow makes me feel a little less lonely."
    "I don’t even remember how I got here."
    "Or when I got here."
    "I’m assuming this means I zoned out again but, apparently, was not fortunate enough to bump into anyone to snap me out of it this time around."
    "Oh well."
    "I’m sure I’ll find someone sooner or later."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene childofman2
    with dissolve2

    s "…"

    "I find something."
    "It’s not something I understand at first glimpse...nor is it something I understand after several more glimpses."
    "But it appears to be some sort of sanctuary."
    "Did I say sanctuary?"
    "I meant to say {s}restaurant{/s} sanctuary."

    s "…"

    "I give up on whatever it is I want to say and direct my full attention to discerning the structure before me-"
    "But the lingering scent of pork broth and what I think is fried chicken invades my nostrils and forces me into a state of mild confusion in which I can’t even fully recall how I wound up here."
    "I attempt to approach the building, but my legs stiffen up."
    "And then, something extraordinary happens."

    p1 "Hear ye, hear ye."
    p1 "We, the council of plants, have called upon this meeting to discuss the probability of furthering the development of one-"
    p1 "Uhh...am I reading this correctly?"
    p1 "The name I have here is “Sensei Arakawa.”"
    p3 "We couldn’t figure out his full name, so we just put what all of the girls have been calling him."
    p2 "Wasn’t it Steve? I could have sworn the tomboy one called him that recently."

    if bonus == True:
        p4 "Which tomboy? The one who rips her hair out? Or the one he almost [rape]d on the bridge that one time?"
    else:
        p4 "Which tomboy? The one who rips her hair out? Or the one he hugged on the bridge that one time?"

    p2 "The first one, with the hair."

    if bonus == True:
        p3 "God, I want to lick her thighs."
        p4 "Of course you do, you fucking lolicon."
    else:
        p3 "Wait, hold on. I just remembered I die in this event and I don't want to go through that again. It was horrible."

    p1 "Order, order."

    if bonus == True:
        p1 "As exciting as it would be to sit here and discuss our sexual fantasies, we must now take into consideration the fact that the beach trip is halfway over and barely anything has been accomplished."
    else:
        p1 "As exciting as it would be to sit here and discuss saving our dear brother's life, we must now take into consideration the fact that the beach trip is halfway over and barely anything has been accomplished."

    p2 "Well, what exactly were we hoping to accomplish again? We’re just plants. It’s not like we can actually...you know, “further development” or whatever."
    p1 "No, we certainly can not. But we can-"
    p3 "Woah woah woah. Wait a second. Isn’t that him right there?"
    p4 "Oh, shit."
    p2 "What do we do?"
    p1 "Just...just stay quiet. It’s not like he can hear us or anything."
    s "Hello."
    p4 "…"
    p3 "Did he just fucking say, “Hello?”"
    p2 "He totally just said, “Hello.”"
    s "Why are all of you plants talking about me?"

    if bonus == True:
        p3 "Umm, better question. Who’s got the tighter pussy? Makoto or Chika?"
    else:
        p3 "Umm, better question. Who’s a better hugger? Makoto or Chika?"

    p4 "Chika 100%%. Makoto’s a little tramp, remember?"

    if bonus == True:
        p2 "Yeah. There’s no way a girl can grow up around that many sex toys and not do a little bit of experimenting if you know what I’m saying?"
        p1 "That only has a {i}slight{/i} bearing on a girl’s vaginal tightness, idiot."
    else:
        p2 "Dude, no. Not in this version she's not."
        p3 "Yeah! Sensei is the huggy boy now! Everyone is safe until they're not!"

    p1 "This is exactly what the narrator was talking about in “Something Everyone Knows and Ignores.”"

    if bonus == False:
        p3 "Wait, no it's not. I think you have to read that event again."

    p4 "Ughhhhhhh please no. That fucking alphabet song {i}just{/i} stopped being stuck in my head."
    p2 "A! Apple!"
    p3 "B! Banana!"
    p1 "Order, order!"
    s "Can someone please explain to me where we are right now? Or...why you guys can talk?"
    p1 "Uhh...how should we put this-"
    p4 "It’s all a hallucination, isn’t it?"
    s "A hallucination?"
    p2 "Uhhh yeah! None of this is actually happening right now! You’re just dreaming!"
    p3 "Buuuuut if this {i}wasn’t{/i} a dream, you’d find yourself standing at a ramen shop at the edge of the world!"
    p4 "No, idiot. The edge of the world is the roof. Do you even fucking read the events?"
    p2 "Petition to kick out Plant #3 from the group?"
    p1 "No petition necessary."
    p1 "Plant #3...we, the Plant Council, in accordance with Plant Law...find you guilty on all counts of being entirely unlikable and mildly annoying."
    p3 "Wait! No! I can’t get kicked out! I have saplings to feed!"
    p2 "Sorry, man. That’s just the way the chrysanthemum crumbles."
    p3 "That’s not even a plant! It’s a flower!"
    p4 "Plants, flowers, what’s the difference?"
    p3 "A lot! For starters, plants-"

    play sound "static.mp3"
    scene childofman3 with flash
    stop sound

    "The cactus turns into a skull and the meeting adjourns."

    p4 "Good fucking riddance. I bet that guy wasn’t even a Plantreon supporter."
    p2 "He was. I bumped into his wife at Whole Foods a few weeks ago and we talked about it for a little while."
    p2 "Really nice family. I’m actually feeling kind of bad now."
    p4 "Petition to remove Plant #2 from the Plant Council?"
    p1 "Petition denied."
    p2 "Asshole."
    s "Can someone please tell me what’s going on?"
    p4 "Dude, just go into the shop. You weren’t even supposed to stop and talk to us."
    s "I mean, it’s not every day I bump into a group of inanimate objects having a conversation with one another."
    s "Let alone a conversation about “furthering my development.”"
    p1 "Ugh, great. Now I have to file an I-35 and explain to the {i}Supreme{/i} Plant Council why there was another deviation."
    p2 "There sure have been a lot of those lately...Do you think it’s something we should worry about?"
    p4 "I’m sure it’s fine. It’s just his memories trying to come back or whatever, isn't it?"
    p1 "Whatever it is, it won’t do us any good to continue discussing it while he’s right there listening."
    s "?????????????????"
    p1 "Anyway! This concludes the ninety-seventh gathering of District 23’s Plant Council!"
    p1 "Please remember to keep everything discussed here classified from any and all interested parties, and feel free to help yourself to a croissant on the way out."
    p4 "Croissants are for girls."
    p2 "Hah. I get it."

    play sound "static.mp3"
    scene childofman4
    with flash
    stop sound

    s "…"

    "I stare blankly at a set of chairs before me."
    "There is a skull on one of them."
    "I feel like I’m forgetting something."

    scene black
    with dissolve2
    scene inmemorium
    with dissolve2
    $ renpy.pause(4, hard=True)
    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene childofman5
    with dissolve2

    if bonus == True:
        "I walk into the strange building to be met with the surprising sight of one girl I’ve had sex with and one girl I’m going to have sex with."
    else:
        "I walk into the strange building to be met with the surprising sight of one girl I’ve hugged and one girl I’m going to hug."

    "Their names are Makoto and Touka and they are both relatively unpopular, each for different reasons."
    "But I’m glad to see that they’ve found company in one another."

    s "Hey, you two. How are things?"
    to "…"
    mak "What do you mean, “How are things?” What is wrong with you?"
    s "I’m sorry?"
    to "Sensei...you’ve been standing there looking...lost for a fair amount of time now."
    mak "And let’s not gloss over the fact that you played out an entire plant-based roleplay scenario of sorts."

    if bonus == True:
        mak "Did Noriko drug you again? Because I explicitly told her to not do that."
    else:
        mak "Did Noriko give you another potion? Because I explicitly told her to not do that."

    s "Plant...roleplay?"
    to "There was a fatality and everything. It was actually rather touching in a...very strange sort of way."
    s "Nevermind that. Would one of you mind telling me where exactly we are right now?"

    scene childofman6
    with dissolve

    to "Oh, this old place?"
    to "It’s just an extra restaurant my family had lying around."
    to "I informed my father that there weren’t many options for us to choose from for dinner, so he had this one airlifted over."
    mak "I envy the sort of life that leads to you having “extra” restaurants lying around."
    to "I actually quite like this one despite its rather drab decor and strange scent."
    mak "It’s not really strange. That’s just kind of...how ramen smells."

    scene childofman7
    with dissolve

    to "Is that so?"
    to "I don’t typically eat things this inexpensive, so I was unaware it was commonplace."
    s "So you two are just...hanging out at a secret ramen shop Touka’s family had airlifted in the middle of the night?"

    scene childofman8
    with dissolve

    to "That’s not all, Sensei. Makoto was actually helping me study."
    s "Study? You {i}do{/i} realize we’re on vacation, right?"
    mak "Neither of us had anything else to do, so..."
    to "I also find learning to be quite fun! And since swimming is out of the question given the weather, it only made sense for us to seize this opportunity to get something done."
    s "Wow. If only someone who cared a little less about studying would show up right about now..."
    c "Woah..."
    c "What...is this place?..."

    scene childofman9
    with dissolve
    play sound "cheer1.mp3"

    "A hidden audience erupts into applause as Chika finds her way into the secret Tsukioka ramen shop at the edge of the world that isn’t actually the edge of the world maybe."

    c "…"
    to "Oh, Chika! You showed up after all."

    stop sound fadeout 3.0

    c "…"
    mak "I’m assuming this is where our study-session concludes then?"
    c "…"
    to "Oh, don’t be silly. I’m sure Chika also sees the value in utilizing free time to become a better, more knowledgeable, person."
    to "Isn’t that right, Chika?"
    c "…"
    mak "Chika? Hello?"
    c "…"
    s "Hey."

    scene childofman10
    with dissolve

    c "Oh! Hey!"
    c "I didn’t realize you were here too, Sensei."
    s "Don’t worry, even I didn’t realize I was here until a few minutes ago."

    play sound "laugh1.mp3"

    c "Oh, you. You’re so funny. No wonder you and I are-"
    s "Two people with a totally normal relationship not worth mentioning to anyone else?"

    if bonus == True:
        scene childofman11
        with dissolve2
    else:
        scene white
        with dissolve2

    stop sound fadeout 2.0

    if bonus == True:
        "Chika’s clothes dissolve into nothingness, but her scarf remains intact because she would get cold otherwise."
    else:
        "Chika’s clothes reform into a clown costume and I do a little jig to celebrate."

    "A fish stares up at me from the ground outside of the restaurant, gasping for breath but incapable of breathing because...uhh, water."
    "I don’t know the sciencey explanation for it."
    "It’s reverse drowning."

    s "Makoto, can you explain what the fish is doing?"
    mak "Fish? What fish?"
    to "Could he be referring to one of our bowls of cheap commoner noodles?"
    c "I could stand here and stare at you for the rest of eternity and not regret even a second of it."
    s "But what about Chinami?"
    y "Hm? What’s this about Chinami?"

    play sound "static.mp3"
    scene childofman12
    with flash
    stop sound

    s "Yumi?"
    y "Uhhhhhh yup. That’s my name, asshole."
    s "What are you doing here?"
    y "I work here, asshole."
    s "Since when?"
    y "Since you helped me get a job here. Remember, asshole?"
    s "I don’t remember that at all."
    y "Really? You don’t remember the entire arc about my mom and me reconnecting? And me discovering that I’m a product of her being knocked up while unconscious, asshole?"
    y "Do you even pay any attention to me at all, asshole?"
    y "Or are you just here to kill the pain, asshole?"
    s "Pain?"
    s "What pain?"
    c "Senseiiiiiiii~ Look at meeeeeeee~"

    if bonus == True:
        scene childofman11
        with dissolve

        "I look at Chika."

        scene childofman13
        with dissolve

        "And then I look back at Yumi again."
    else:
        s "No."

        play sound "static.mp3"
        scene childofman13 with flash
        stop sound

    y "Hey, asshole."
    y "Do you remember all of those detentions you used to give me back before you regained your own body (If that is what is actually happening here), asshole?"
    s "I don’t."
    s "I don’t remember anything from before the first time I “woke up” in[school] again."
    y "There was something you said to me during one of those that really stuck with me, asshole."
    s "And what was that?"
    y "That I was wasting my potential, asshole."
    s "And that stuck with you?"
    y "Yeah. But not in a good way, asshole."
    y "Because, from my perspective, there was never any potential there, asshole."
    y "I’ve been nothing but an abomination of failures stitched together since the moment I popped out of my junkie mom, asshole."
    y "And having some guy who knows nothing about me pretend to know my potential was even worse than the time you [[redacted]."
    y "Asshole."

    play sound "static.mp3"
    scene childofman14
    with flash
    play sound "alert.mp3"

    maktouk "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    six "I missed you."
    s "...Maya?"

    play sound "static.mp3"
    scene childofman15
    with flash
    stop sound

    mak "Maya?"
    to "Is everything okay, Sensei?"
    to "You’ve been standing there looking...lost for a fair amount of time now."
    s "I..."
    s "Wait, has...Chika been here? Or Yumi?"
    mak "Neither of those two have been-"

    scene childofman16
    with dissolve

    c "Woah..."
    c "What..."
    c "What is this place?"

    scene childofman17
    with dissolve

    c "Oh, this is where you were? I’ve been looking all over for you."
    c "Why haven’t you been answering your phone?"
    s "My phone?"

    "I slide my phone out of my pocket to find that I have several missed calls and an entire string of text messages from Chika spanning over the course of the last three hours."

    mak "How did..."
    mak "How did you know she would be here?"
    s "Is there an emergency or something?"
    c "No, I..."

    scene childofman18
    with dissolve

    c "I just...you know..."
    to "Whatever brought you here, Chika, I do implore you to sit down and try these lower middle class ramen noodles! They are absolutely splendid!"

    scene childofman19
    with dissolve

    c "Oh! Thank you!"
    c "I was starting to think I wouldn’t be having dinner at all tonight."
    c "Do you think it’d be okay if I packed some up for Yumi as well? Girl didn’t even eat breakfast today."

    scene black
    with dissolve2

    "I take a seat at the counter and order from one of the Tsukioka family servants or...employees or something."
    "He doesn’t speak at all, but he nods after I place my order and brings me a fresh bowl of soup just minutes later."
    "Before I know it, the girls and I are choking down piping hot lower middle class ramen noodles."
    "They’re good."
    "Not Tojo Ramen good, but still good."
    "I think mine had cactus in it."
    "………"
    "……"
    "…"

    scene childofman20
    with dissolve2

    "We leave the secret ramen shop and Makoto and Touka proceed to have some sort of formal, smart person conversation that I can’t be bothered to pay attention to."
    "Instead, I focus my gaze on stars sinking into the sea and find myself getting lost in a sea of my own."
    "Not of water, but of skepticism and a heavy dose of regret."
    "Not the type of regret that results from making a poor decision, but the kind that comes from feeling like you’ve wasted too much time."
    "But that shouldn’t be an issue for me."
    "I have as much time as the world can offer."
    "But still-"
    "I feel like yet another chunk of my life has been ripped away from me."
    "Or out of me."
    "Something is missing."

    c "Sensei?"

    scene childofman21
    with dissolve

    s "Yeah?"
    c "You okay?"
    s "I’m fine. Why do you ask?"
    c "Obviously cause you look...not okay."
    s "Whatever it is will pass. I’m probably just tired."
    c "Long day?"
    s "Yes and no."
    s "Mostly yes, I think."
    c "Anything I can do to make you feel better?"

    if bonus == True:
        s "Not with those two around."
    else:
        s "A hug would be nice."

    scene childofman22
    with dissolve

    c "I see, I see."
    c "Come with me then."
    s "Come with you where?"
    c "I don’t know. Just come."
    s "But-"
    c "They’re talking about smart person stuff. They won’t even realize we’re gone."
    s "I’m pretty sure they’ll still realize if-"
    c "Shush."
    c "On the count of three, we turn around and start walking toward the woods."
    s "Chika..."
    c "One..."
    s "…"

    scene childofman23
    with dissolve

    c "Two..."
    s "{i}Hah...{/i}"

    scene black
    with dissolve2

    c "Three."

    "………"
    "……"
    "…"

    scene childofman24
    with dissolve2

    mak "Wait, where did Sensei and Chika go? Weren’t they just here?"
    to "I believe so...but I don’t recall them ever leaving."
    to "Perhaps they forgot something at my spare restaurant?"
    mak "…"
    mak "Perhaps."

    scene black
    with dissolve2

    mak "Let’s just head back to the inn, I guess..."

    $ renpy.end_replay()
    $ secondbeach10 = True
    $ plantcouncil = True
    stop music fadeout 10.0

    "………"
    "……"
    "…"

    jump chikalust20intro

label chikalust20intro:
    scene chikawoods1
    with dissolve2
    play music "asobeatsex2.mp3"

    "I follow Chika into the woods."
    "The sound of small sticks and branches cracking underneath her feet gets lost in a cacophony of various insect noises, and I wonder to myself why it is they’re so rowdy in the midst of winter."
    "Or at least what I imagine is the midst of winter."
    "All things considered, it could very well be the tail end as it’s certainly a little warmer now than it was when I woke up this morning."
    "That’s not saying much, though, given that it was still snowing when I left home with the girls."

    c "Hmm hmm hmm~"
    c "Hm hm hm hm hmmm~"
    s "Someone’s in a good mood."
    c "Of course I’m in a good mood. "
    c "It’s exhausting watching you run around with a bunch of other girls when I’m the only one with the privilege of seeing the...more {i}interesting{/i} side of you."

    if bonus == True:
        s "Are you...referring to my penis as “the more interesting side of me?”"
        c "Hey, what can I say? Penises are still brand new to me or whatever."
        c "I can’t help but be curious about the stuff I don’t fully understand yet."
        s "If there is anything you have proven to me so far, it is that you definitely understand my penis."
        c "Heheh~ He’s such a good boy."
        s "Please don’t personify it, though. I don’t know how to feel about that."
        c "Hmm hm hmmm~"
        c "Hmmm hmm hmm hmmmm~"

    "Chika goes right back to humming, leading me further and further into the forest as if she knows exactly where she’s heading."
    "We’re far enough in at this point, though, that I begin feeling a bit uneasy."
    "And even the moonlight crawling in through the trees isn’t enough to really push away the overwhelming darkness surrounding the two of us."

    c "Hmm hmm hm~"
    s "Chika?"
    c "Yeah?"
    s "Would you mind telling me where we’re going?"
    c "Why do you wanna know?"
    s "Because we’ve been walking for a while now and I’m not really in the mood to get lost."
    c "Heheh~"
    c "We need to go far enough that no one will be able to hear you scream."
    s "…"
    s "What?"

    play sound "static.mp3"
    scene chikawoods2 with flash
    stop sound
    stop music


    c "Because I’m going to kill you."
    s "…"
    c "…"
    s "Please don’t."
    c "Don’t kill you?"
    s "Correct. Don’t do that."
    c "Why not?"
    s "The fact that I need to give you a reason is somehow scarier than the prospect of you killing me itself."

    scene chikawoods3
    with dissolve
    play music "asobeatsex2.mp3"

    c "Don’t worry. I wouldn’t actually kill you."
    s "I appreciate that."

    if chika_lust >= 20:
        jump chikalust20

    else:
        scene chikawoods4
        with dissolve

        c "I just wanted to go somewhere private for a little while. "
        c "But I guess we {i}are{/i} getting a little too far in, aren’t we?"
        s "I’m honestly surprised there’s a forest this size right off of the beach to begin with."
        c "Really?"
        c "Cause I think I heard something once about how there wasn’t a beach here at all back in the day."
        c "It used to be just trees and trees and trees as far as anyone could see."
        c "It wasn’t until later on when tourism started going up that they decided to tear a lot of them down and build the beach we’ve been staying on."
        s "It hasn’t always been there?"
        c "I mean, it’s not like I was alive back then to confirm anything. I just remember hearing something about it."
        c "I’m pretty sure everything down to the sand itself was purchased and brought here."
        c "Well, everything except the water of course. That was always there."
        c "It’s just the surrounding areas that weren’t as...beachy as they are now."
        s "Interesting."
        c "Heheh~ Bet you didn’t think you were going to be getting a history lesson out here, did you?"

        if bonus == True:
            s "I had a feeling this was going to be a lot more sexual than that, yes."
            c "Hmm...I can’t say I’m a big fan of doing anything sexual when there are bugs all over the place."
        else:
            s "I had a feeling we were about to hug."
            c "With all of these bugs all over the place? Ew."

        s "There are some risks worth taking, Chika."

        if bonus == True:
            c "Well take them yourself. If I’m sucking you off and a beetle lands on my shoulder, I’ll never want to do anything sexual ever again."
            s "That is an extremely dramatic overreaction."
            c "Sorry, Sensei. If I knew you wanted a piece of this, I would have gone literally anywhere else."
            s "Just assume that I always “want a piece,” Chika."
            c "Heheh~ Show me that more often, then."

        c "Just...not while we’re surrounded by creepy, crawly stuff."

        scene black
        with dissolve2

        "Chika and I turn around and head back toward the shore. "
        "Once we get to more familiar territory, we decide to split up before heading back to the inn so people don’t get suspicious of the two of us showing up together."
        "I allow Chika to go back first and spend the next ten minutes or so kicking sand into the water- drawing pictures with the tips of my shoes and letting the tide overtake them."
        "I’ve never been much of an artist, though...so it’s like my hideous creations are simply being put out of their misery."
        "Once a fair amount of time goes by, I decide it’s my turn to head over to the inn as well."
        "I’ll be cashing in on the dorm war sleepover tonight, so I’m hoping that whatever happens next doesn’t really get {i}too{/i} out of hand."
        "But, then again, I’ll be inside a room full of girls who [[mostly] want to win my love, so I highly doubt it will be all that easy."
        "Either way, I draw one last picture that turns into one last sacrifice before making my way into the inn..."

        $ renpy.end_replay()
        $ chikalust20skip = True
        stop music fadeout 5.0

        if dormwarfloor1win == True:
            jump secondbeach11floor1
        else:
            jump secondbeach11floor2

label chikalust20:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
os "And the first turtle shell box thing I ever encountered was some poetry assignment we had in[school]."

    scene mollyosako35
    with dissolve

    os "She loved poetry."
    os "Well, still loves. It’s one of her favorite things."
    os "But...dorky old me back then was like...what if I memorized something she’d like and...maybe made eye contact with her or something while reading it? "
    os "So I did. Eye contact and all."
    os "And the second her eyes met mine...it became an addiction."
    os "I started finding every fuckin’ turtle shell I could get my hands on, frantically pushing buttons and moving from one place to the next trying to get her to notice me."
    os "If I’d never started taking that approach..."
    os "Well, I don’t really know if I’d be here today."

    scene mollyosako36
    with dissolve

    mo "You...contemplated suicide?"
    os "What? Oh. No. Sorry. I just meant that...we literally came here today together."
    os "And she’s here as a chaperone, so..."
    mo "Chap-"

    scene mollyosako37
    with dissolve

    mo "Are you Miss Watabe’s girlfriend?!"
    os "I am. "
    os "But I never would have become that without working for it."
    mo "Wow..."
    mo "You are...not at all what I was expecting."
    os "Yeah...I get that a lot."

    scene mollyosako38
    with dissolve

    os "This, uhh...{i}undisclosed friend{/i} of yours..."
    os "Does she have a name?"
    mo "She doesn’t exist. But if she did, her name would likely be something like...Ren or...Ran..."
    os "Well, whatever her name {i}would{/i} be, some people just won’t understand things unless you tell them."
    os "And if you want her to know, that might be what you have to do."
    mo "What do I do if I {i}don’t{/i} want her to know?"
    os "Why wouldn’t you want her to know?"
    mo "Because I’m not her type."
    mo "And it might make things weird."
    os "Aren’t things weird now?"
    mo "Only because I made them that way."
    os "Then you’ve got two options. Either apologize and move past it-"
    os "Or make things even weirder and hope that she’s a weird enough person to not inherently hate it."

    scene mollyosako39
    with dissolve

    mo "She {i}is{/i} pretty weird..."
    mo "Or would be if she actually existed. Which she doesn’t."
    os "I’m sure."
    os "At the end of the day, all you can really do is try. Maybe it works out, maybe it doesn’t."
    os "But if you’re already wandering down the beach crying and talking to strangers, I think it’s safe to say that, as-is, things {i}aren’t{/i} working out."
    os "And that, personally, I’d try to do something about it."
    mo "…"
    mo "Thank you, Miss Watabe’s girlfriend."
    os "Osako. "
    mo "Thank you, Osako."
    os "Don’t mention it, random upset foreigner girl."
    mo "Molly."
    os "Don’t mention it, Molly."

    scene mollyosako40
    with dissolve

    os "Now, if you’ll please excuse me, I’d like to silently stare at the stars reflecting off of the water for a little while longer before heading back to my room."
    os "But if you ever need someone to talk to and there isn’t a beach around to bump into randoms, Ayane’s a good bet as well."
    os "She can be a little pushy, but she’s got a good heart."
    mo "I know..."
    mo "Her wisdom is rather high for a rogue as well."
    os "Sure. Whatever that means."
    os "You’re welcome to stay here, you know. Being broody and reflective is surprisingly helpful at times like this."

    scene mollyosako41
    with dissolve

    mo "I suppose a fair bit of brooding won’t do any harm if it’s only occasional."
    mo "Though, it’s hard for me to look up at the stars without grieving over the destruction of Alderaan."
    mo "Oh. Alderaan is-"
    os "Star Wars. I know."
    mo "Rip in peace, Alderaan."
    mo "Rip in peace..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ secondbeach9 = True
    stop music fadeout 7.0

    "………"
    "……"
    "…"
    "{i}Somewhere else...{/i}"

    jump secondbeach10
...
```