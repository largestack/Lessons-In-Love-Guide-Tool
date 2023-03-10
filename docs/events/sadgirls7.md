# Parallelogram (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Rolling Stop](./sadgirls6.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Makoto: A Beautiful Mind](./sadgirls8.md)

## Event properties

* Id: sadgirls7
* Group: Makoto
* Triggered by label: sadgirls6
* Chain sources: sadgirls6
* Chain sources path: sadgirls6

## Official wiki page

[Parallelogram](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls7&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label sadgirls7:
    play sound "static.mp3"
    scene makotoyay1 with flash
    stop sound
    play music "heartbeat.mp3"
    $ renpy.pause(10, hard=True)

    "When I was younger, I watched a woman’s head split open after a collision with the concrete."
    "I was clutching my mother’s hand as if it were a life raft and I was lost in the ocean."
    "She pulled me inside to shield me from learning about death long before I was meant to."
    "In hindsight, I wish she wouldn’t have."

    $ renpy.pause(5, hard=True)
    scene makotoyay2
    with dissolve4

    "It happened outside of the grocery store."
    "We kept on shopping, ignoring the blare of the sirens — so loud that they overtook the music on the store radio and became the soundtrack to our trip for the day."
    "There is one moment I can recall where the sirens perfectly aligned with the tune of a song."
    "Like a parallelogram, they combined and stretched out forever — past the dying woman and deep into the street..."
    "Off into the horizon...leaving a wake of intangible destruction as it went."
    "I followed the lines until their very end, but only in my mind as my hand still rested in that of my mother’s and I wasn’t old enough to wander off on my own yet."
    "I understand why now."
    "For when the lines ended, I was met with nothing more than pitch black."
    "And a single white clock, dissolving into nothingness."

    scene black
    with dissolve2

    "I look down while I’m walking now."
    "Just to make sure no lines cross over me."

    scene makotoyay3
    play music "warblewarblewarble.mp3"

    "I recall another hand, far bigger than that of my mother’s."
    "With a large, clock-colored eraser pressed between its thumb and its forefinger, it reached off into the distance and started rubbing away the remnants of an unreadily dispatched soul."
    "But each line it erased only became longer at the end without attention."
    "And each fleck of rubber that peeled and fell off of the eraser while it attempted to fulfill its only purpose was replaced with a sprouting sunflower."
    "It was in that moment that it dawned on me. "
    "The idea that the most beautiful of things can still grow in the shadows of all that is evil."
    "And it is for that reason that I call myself what I do today."
    "For that hand was yours."
    "And that flower was me."

    stop music
    play sound "static.mp3"
    scene makotosadagain1
    with flash
    stop sound

    maki "Uhh...Makoto?"
    mak "What?"
    maki "There’s someone here to see you."

    play sound "static.mp3"
    scene makotosadagain2
    with flash
    stop sound
    play music "lastdailysong.mp3"

    mak "Sorry, but I’m not accepting any visitors right now. Please ask whoever it is to go away."
    s "Even if it’s me?"
    mak "It doesn’t make a difference who you are. I said I’m not accepting visitors."

    scene makotosadagain3
    with dissolve

    s "Well, I tried."
    maki "Did you really, though?"
    mak "{i}Tried?{/i}"
    mak "Tried what?"
    mak "Did you think bringing him here would cheer me up?"
    mak "Do you think I’m an inconvenience because I’m not handling this as well as you? Is that what’s going on here?"

    scene makotosadagain4
    with dissolve

    maki "What? Of course not. You’re not an inconvenience at all. I just hate seeing you like-"
    mak "Get out."
    maki "Makoto, please. I brought him all this way here to-"
    mak "Not him. You. Leave."

    scene makotosadagain5
    with dissolve

    s "You shouldn’t talk to your mother like that."
    mak "Oh? Are {i}you{/i} my dad now? Hooray. Everything is good again. "
    mak "Let’s all hold hands and forget that the last one is never coming back."
    s "I get that you’re upset. But you need to apologize to-"

    scene makotosadagain6
    with dissolve

    maki "It’s fine, really.  You don’t have to worry about it. "
    maki "I kind of figured something like this was going to happen anyway."

    play sound "static.mp3"
    scene makotosadagain7
    with flash
    stop sound

    mak "{i}Hey, now.{/i} What’s that supposed to mean?"
    mak "Have I become so predictably horrible as a daughter that you just expect me to turn you away now?"
    mak "Or do you think that {i}maybe{/i} I’d just have an easier time grieving without being reminded every thirty seconds that my father is dead?"
    maki "You know that’s not-"
    mak "Why are you still here? I asked you to leave. "
    mak "I’ll humor you and let Sensei try to “snap me out of this.” But if I were in your shoes, I’d probably use that time to prepare myself because, chances are, your daughter’s never coming back either."

    play sound "static.mp3"
    scene makotosadagain8
    with flash
    stop sound

    maki "That’s not true..."
    maki "You’re still you...and all of this is just temporary."
    mak "Oh, give me a fucking break with the cliche consolation lines like “all of this is temporary” and “things will get better.” "
    mak "At least Sensei will be able to come up with more creative ways to remind me of why I shouldn’t be crying during the saddest day of my life. Right, Sensei?"

    scene makotosadagain9
    with dissolve

    maki "Makoto! You’re not the only one who lost someone, you know?! He meant just as much to me as he did to you!"
    mak "Yeah? That’s good to know. It was hard to keep track of {i}who{/i} meant {i}what{/i} to {i}who{/i} with all of those extra people always coming in and out of the house."

    scene makotosadagain10
    with dissolve

    maki "That...didn’t have anything to do with-"
    mak "Yeah, yeah, yeah. Explain it later. I’m done dealing with you for now. Bring on the next contestant. "

    scene makotosadagain11
    with dissolve

    s "Do you intend to shit talk me as well when I’m {i}also{/i} here to help you?"
    mak "You’re here because you were fucking kidnapped, weren’t you? This isn’t something {i}you{/i} would plan."
    mak "You’d tell me to get the fuck over it and learn how to deal with things on my own because that’s what I’m supposed to do! Isn’t it?!"
    s "No. That’s-"

    play sound "static.mp3"
    scene makotosadagain12
    with flash
    stop sound

    mak "Isn’t it?!?!"
    s "...As I was trying to say, no. This is different from all of those other times. Different enough that I’ve had a hard time thinking of anything {i}but{/i} this since I walked into that bathroom."
    mak "Oh, good! If all it took was a fucking {i}death{/i} for you to start worrying about me, perhaps I should have killed someone myself!"
    maki "That’s not what he’s saying, Makoto!"
    mak "Why are you still here?! I told you to leave!"

    scene makotosadagain13
    with dissolve

    s "I’ll take it from here, Maki. I remember the way out, so I can just come meet you in the shop when I’m done."
    maki "Good. She was starting to test my patience anyway."
    mak "Hallelujah! Praise fucking be!"

    scene makotosadagain14
    with dissolve

    maki "I just want you to feel better, Makoto. "
    maki "I’m sorry if I went about it the wrong way."

    play sound "dooropen.mp3"
    scene makotosadagain15
    with dissolve

    "Maki leaves the room, exhibiting a surprising amount of self control by not slamming the door on her way out."
    "I understand that we all have our own ways of processing grief...and I understand even better just how much Makoto cared for her father."
    "But even then, I can’t help but feel like she’s being extremely unfair to a woman who’s been bending over backwards and sidelining her own grief just to deal with {i}this.{/i}"
    "If I were a parent in this scenario, I’d simply let my child rot."
    "So I guess it’s good that I’m not."
    "And that I won’t ever be."
    "Because it wouldn’t be fair to subject someone to that."
    "Now, please excuse me as my hypocrisy reigns supreme once more."

    s "Does being a bitch to your mother like that really make you feel any better?"

    play sound "static.mp3"
    scene makotosadagain16
    with flash
    stop sound

    mak "A little bit, yeah."
    s "Why? You do realize she’s taking this just as badly as you are, right?"
    mak "Dressed like {i}that?{/i} Yeah, I don’t think so. You needn’t look any further than the clothes we’re wearing to tell she doesn’t give a shit."
    mak "Wanna know what I really think, Sensei? "
    mak "{i}I{/i} think she’s dressed like that because she wants somebody to fuck her so hard that she just {i}forgets{/i} my dad."
    s "Seriously?"
    mak "What? It wouldn’t be the first time I’ve heard her getting her brains screwed out by some random guy."
    mak "Want a shot? She’s fresh on the market. And her clothes are already halfway off. Saves you some of the hassle."
    s "Sounds good, actually. I’m sure that hearing me go to town on your mother while you’re stuck inside of your room will do plenty of good for your current state of mind."
    mak "But what about {i}your{/i} state of mind, Sensei? What if you’re not able to get it up for someone who’s already done growing?"
    s "..."

    scene makotosadagain17
    with dissolve

    mak "Oh well. Whatever. Just don’t come crying back to me when her insides are a little too “beat up” for you."
    mak "I can’t speak from experience since you’re the only man who’s ever put his dick in me, but I’m pretty sure she might be a little too stretched out to appeal to your...{i}tastes{/i} by now."
    s "Okay...can I sit? And can we talk about something that doesn’t involve sex? "

    scene makotosadagain18
    with dissolve

    mak "Wow! If I hadn’t already picked out my funeral dress, I might have thought it was my birthday after hearing that."
    mak "Welcome to the party, Sensei. The seat at the head of the table is free now. "
    mak "My legs have grown since my dad last sat in it. So if we’re careful, I might even be able to give you a stealthy footjob while my mom tricks herself into believing we’re a big, happy family again."
    s "Would you rather I just leave?"
    mak "Do you want the honest answer to that? Or do you want to sit down {i}regardless{/i} of what I want because it makes you feel better about yourself?"

    scene black
    with dissolve

    s "I’ll sit. Thanks. "
    mak "Ooooh, look at you. Breezing right past my subtle digs at your character like they don’t actually hurt. Sure wish {i}I{/i} could do that."

    "I take a seat beside Makoto, expecting her to slide away, but she doesn’t move at all."
    "In fact, she grows silent the second I’m closer to her- locking her hostility inside of a box, as temporary as it may be."
    "As I look down at her, I wonder if the disparity in size between us is the primary reason for her newfound silence."
    "I wonder if she feels safer now that there’s someone who could envelop her entire body in a single embrace just one foot away."
    "I wonder if that type of embrace is something she longs for in this moment."
    "Or if it would send her spiraling even further into a pit that she will never return from."

    scene makotosadagain19
    with dissolve2

    s "..."
    mak "..."
    s "Do you want to talk? Or would you rather sit here in silence?"
    mak "I’m not sure. I’m new to this whole “dead dad” thing."
    s "I see that, at the very least, you get your sense of humor from your mother. She said something eerily similar yesterday morning."
    mak "Wow, it’s almost like we’re related or something."
    s "..."
    mak "..."
    s "You don’t actually dislike her, do you? "
    mak "What do {i}you{/i} think about her, Sensei? You know, since you two are such close friends now."
    s "I like her a lot, actually. She reminds me of this one girl that’s been following me around like a puppy since the school year began."
    mak "Ami, because of how annoying she is? Ayane, because it seems as if she’s always in heat?"
    s "I’m talking about you, obviously."
    s "And, for the record, you are also very annoying and have a surprisingly high sex drive."
    mak "Yeah well, when you grow up surrounded by rubber cocks and screams of pleasure, you tend to find yourself getting interested in certain things at a very unhealthy age."
    mak "Apart from that, though, my mother and I are nothing alike. We never have been."
    s "Well...spend a little more time focusing on {i}her{/i} rather than everything else and maybe you’ll change your mind."

    scene makotosadagain20
    with dissolve

    mak "Did she pay you to say that? Is that part of your {i}mission{/i} today?"
    s "If she did pay me to say that, you two would be even more alike. Because I distinctly recall you paying Miku on at least one occasion to...try to get me to fall for you or something."
    mak "A decision that very well paid off in the fact that my hymen is now just as present as my father."
    s "If you really think that had any bearing on my decision to ultimately sleep with you, I think there’s a lot you don’t understand about this relationship."
    mak "Well, it’s not as if you make it easy to understand. "
    mak "But, for the purpose of both humoring you and finding {i}humor{/i} of my own, please tell me exactly {i}what{/i} you think I have in common with my mother."
    mak "Because apart from our apparent shared sex drive and our looks, I struggle finding anything at all."
    s "Well, there’s the dark sense of humor you both use to try and push some of the sadness away..."
    s "There’s the overabundance of love you both have for Miku..."
    s "But more than just those, there’s this...compulsion you both have to never look weak."
    s "Maki doesn’t look as fine as she does because she’s immune to this. She looks that way because she’s focusing everything she has on {i}you{/i} right now."

    scene makotosadagain21
    with dissolve

    s "Weren’t you crying {i}together{/i} when I walked into that bathroom?"
    mak "How should I know? I can’t remember anything about the day I found out. And all I remember from the day after is crying so hard that I threw up."
    s "Well, she was. And before that, she burst into the classroom searching for you with a look I have never seen from her before."
    s "It wasn’t sadness, either. It was urgency. Like the only thing that mattered in that moment was finding you so you wouldn’t have to hear the news from some staff member in an office."
    s "Everything after that has been a marathon of unrestrained compassion for a daughter that she loves who can’t even find it in her to {i}return{/i} that love right now."
    mak "..."
    s "Now, as one more person carrying the impossible, ingrained burden of never showing how I really feel, I obviously get that there’s a good reason for it. Which is why I’m not suggesting that you {i}change{/i} that part of you."
    s "I just think you’re smarter than actually believing your mom is completely unaffected by this."
    mak "Maybe I am."

    scene makotosadagain22
    with dissolve

    s "..."
    mak "Maybe I {i}am{/i} smart enough to understand that..."
    mak "{i}But isn’t everything so much easier when you have someone else to blame?{/i}"

    scene makotosadagain23
    with dissolve

    mak "Isn’t it great knowing that the weight on your shoulders can just be passed on to someone else?! That burdens can become lighter whenever we want them to?!"
    s "It’s not {i}whenever we want.{/i} It’s whenever we can find someone willing to take that weight."
    s "And in your case, you’re just lucky that you have someone who’d sacrifice the last bit of sanity in them so you can be one step closer to smiling."
    mak "Lucky..."
    mak "Me...lucky..."
    mak "Me...the girl who just lost her one and only hero..."
    mak "I’m lucky..."
    mak "I’m so lucky..."
    s "Okay...{i}lucky{/i} definitely wasn’t the best word choice on my part. But I’m sure you understand what I mean, don’t you?"

    scene makotosadagain24
    with dissolve

    mak "Of course I understand, Sensei. "
    mak "I’m {i}smart...{/i}remember?"
    mak "Though, I suppose I’m not the {i}smartest{/i} anymore."
    mak "But I wouldn’t {i}be{/i} that smart if I wasn’t trying to impress someone."
    mak "And before you go drowning yourself in narcissism again, allow me to clarify that I’m not talking about {i}you.{/i}"
    mak "The reason I worked so hard all those years...why I nearly {b}KILLED MYSELF{/b} trying to become the best person I could be..."
    mak "It was all for him."
    mak "It was all to make him proud."

    scene makotosadagain25
    with dissolve

    mak "{i}How am I gonna do that now?{/i}"
    mak "How am I supposed to keep being the best person I can be when the one thing {i}making{/i} me that person isn’t here anymore?"
    mak "I’ve got nothing left. "
    mak "And don’t tell me I have {i}you...{/i}or my {i}mom...{/i}because {i}you{/i} don’t love me...and she didn’t either until she had to."
    mak "My dad is dead. The one thing keeping me going is dead. "
    mak "Shouldn’t I just die too?"
    mak "Maybe then, my mom wouldn’t have to hold in her tears. And you could have Nodoka become your new assistant since she’s already better than me."
    mak "It would all be better without me. The whole fucking world. "
    mak "I’m nothing but a burden to everyone. "
    mak "There’s no one left that I want to live for."
    s "Then why not live for yourself?"

    scene makotosadagain26
    with dissolve

    mak "Because that’s fucking stupid."
    s "How? That’s what I do."
    mak "Yeah? And how’s that working out for you?"

    scene makotosadagain27
    with dissolve

    s "Fine, I guess."
    s "I’ve spent the last couple days slowly losing my grip on reality while worrying about you, but it’s not like I’m waking up every morning thinking about how I want to die."
    s "I’m just...having trouble getting to sleep. Which, all things considered, isn’t really that big of a problem compared to what some of the people I care most about are going through."

    scene makotosadagain28
    with dissolve

    mak "You really worried that much?"
    s "Does that surprise you?"
    mak "..."
    mak "A little."

    scene makotosadagain29
    with dissolve

    s "I guess that’s fair."
    mak "..."
    s "..."

    "I recall an earlier thought — one about my hypocrisy reigning supreme as I leave a girl to rot."
    "And like clockwork, it will reign supreme once more right now."
    "Just this time, it will be in paradoxic contradiction to itself as my hypocrisy is squared until it comes full circle."

    s "Have I ever helped you with {i}anything?{/i}"
    mak "..."
    s "Because all this time, I’ve been telling myself that what I’ve been doing for you was what was best. But I don’t know if I ever actually believed that or if I just...{i}made{/i} myself believe it."
    mak "..."
    s "I guess what I’m asking is...do you need something different from me? Or...{i}want{/i} something different from me?"
    s "Should I be less of an asshole? {i}More{/i} of an asshole?"
    s "I’m just not sure with you."
    s "I think I’m normally pretty good at reading people but, for a while, it’s felt like every time I’ve tried to do that with {i}you,{/i} I’ve come up with nothing."
    s "I’m obviously not...trying to take the place of your father or anything. But I think having one more person on your side is something that could really benefit you right now."
    s "Especially if you’re not going to let your mom be one of those people."
    mak "..."
    s "..."

    scene makotosadagain30
    with dissolve

    mak "Sensei..."
    mak "Have you ever lost someone you loved?"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene makotosadagain30 with flash
    stop sound

    mak "Someone that meant the world to you?"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene anormaldoor with flash
    scene makotosadagain31 with flash
    stop sound

    mak "Does it ever get better?"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene anormaldoor with flash
    scene spiderbug with flash
    scene makotosadagain32 with flash
    stop sound

    mak "What can I do to make this all feel better?!"

    $ renpy.end_replay()
    $ makoto_love += 1
    $ sadgirls7 = True

    if makoto_lust >= 30:
        jump makotolust30
    else:
        jump makotolust30skip

label makotolust30skip:
    stop music
    scene black

    s "Nothing."

    play sound "dooropen.mp3"

    "I exit Makoto’s bedroom and head directly for the stairs."

    play sound "glass.mp3"

    "On the way down, I knock one of the picture frames off of the wall."
    "Curiosity gets the better of me and I stare down at the mess I have made."
    "Beneath the cracked glass is a photo of a little girl in a fisherman’s cap."
    "She rests on the shoulder of a man that is no more."

    play sound "dooropen.mp3"

    maki "Hey! How’d it go? Is everything okay with-"
    s "I knocked one of your pictures off the wall."
    s "It was an accident."
    maki "Huh? Oh. Yeah, that’s fine. I can just get another frame. What I’m more worried about is how Makoto-"
    s "I couldn’t help her."
    s "But she might be a little more open to listening to you now."
    maki "Really? What did you say?"
    s "I can’t remember."
    maki "But-"
    s "Don’t worry about driving me back. "
    s "I suddenly feel like walking."

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}Neither of the girls understand why you left.{/i}"
    "{i}But you do...don’t you?{/i}"

    $ makotolust30skip = True
    $ yumiblock = True
    $ makotoblock = True
    $ mikublock = True
    $ nodokablock = True
    $ makiblock = True

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label makotolust30:
...
```

## Code that triggers this event

File: (install folder)\game\MakiEvents.rpy

Code:
```python
...
maki "I think..."
    maki "Okay. So, you’re obviously the only male authority figure left in her life now. And one that she admires greatly."
    maki "But even with that, I don’t think she’ll ever see you as anything more than her teacher or...maybe a schoolgirl crush."

    "I think it’s a lot more than just a {i}crush{/i} at this point..."

    maki "That girl just...does better with people like you than people like me. It’s a respect thing."
    maki "Like, how is she going to be consoled by someone she automatically associates sex jokes and dildos with? "
    maki "Each time I try to hold her hand, she’s probably thinking “Wow, this hand has touched so many sex toys.”"
    s "I haven’t seen Makoto since Friday, but I’m pretty sure that is not what she’d be thinking."

    scene makidrive19
    with dissolve

    maki "I don’t {i}know{/i} what she’d be thinking, though. I {i}never{/i} know what she’s thinking because her brain is on another level than mine."
    maki "She’s stubborn. She needs someone on the {i}same{/i} level as her to talk to or she’s just going to keep circling the drain."
    s "With all due respect, I think Makoto is several levels above me as well."
    maki "She might be. But I don’t think she sees it that way."
    maki "To her, you’re a role model. Someone she aspires to be. Someone she’ll actually {i}listen{/i} to because you’re not just a joke to her."
    maki "You’re not {i}me.{/i}"
    s "..."

    scene makidrive20
    with dissolve

    maki "Oh, and if you’re having second thoughts about this, I’m not giving you a ride home. I am out of other options and turning to you is pretty much my last ditch effort."
    s "Have you considered {i}time?{/i}"

    scene makidrive21
    with dissolve

    maki "Well, obviously! But time alone doesn’t cure anything when it feels like the walls are closing in around you."
    maki "I need her to feel safe. I need someone to stop those walls from closing in and I’m not strong enough to hold them back on my own."
    s "For what it’s worth, I think you are. But fuck it. I’ll give it a shot. "
    s "If this doesn’t work though and your daughter just winds up becoming even {i}worse{/i} due to something I said, you owe me free porn forever."
    maki "That’s so much porn!"
    s "Yes. I have a problem."
    maki "Okay, fine. But don’t go screwing this up on purpose just to fuel your addiction. "

    "So either Makoto cheers up or I get free porn forever. At least I can’t lose anymore."

    s "Deal. Pleasure doing business with you."
    s "Maybe I’ll even throw in an added bonus of trying to cheer {i}you{/i} up if whatever methods I use on Makoto actually work."

    scene makidrive22
    with dissolve

    maki "Oh, come on...You don’t have to worry about me. "
    maki "I’ve got two close friends who can cheer me up when I need it. You’re here for my daughter."
    s "I am. But I’m here because {i}you{/i} brought me. Which means that you deserve something too."

    scene makidrive23
    with dissolve

    maki "Then I’d like to sacrifice my reward for an additional serving of Makoto’s happiness."
    s "You know...you’re a pretty great mom for someone who thinks they’re a pretty {i}shitty{/i} mom."
    maki "Tell me that again when I don’t feel pressured to rely on a third party to console my daughter because I suck at it."
    maki "And then again when I stop being creeped out by how {i}off{/i} she looks when she’s grieving."

    "..."
    "Wait..."

    scene makotoflashback with fade

    mak "Until everything melts down and reforms into one disturbing mass of flesh, complete with twelve smiles. "
    mak "One for each girl in class that you [masturbate] to while all alone in bed at night."

    scene makidrive23
    with fade

    "Oh no."

    s "Uhh..."
    maki "Welp! Time to go. Makoto’s not going to cheer {i}herself{/i} up."
    s "On second thought, maybe I’ll-"

    play sound "dooropen.mp3"
    scene black
    with dissolve
    stop music fadeout 20.0

    maki "Nope! No more procrastinating. We’ve talked for long enough."
    s "But what if I’m also creeped out by her?"
    maki "You’re like three times her size. What do you possibly have to be afraid of?"
    s "You sell whips. What do {i}you{/i} have to be afraid of?"
    maki "Are you suggesting that I {i}whip{/i} my daughter? I’m into some weird shit, Sensei, but that’s just crossing a line."
    s "Hah..."

    "Maki leads me up a dark staircase, but it’s not dark enough to conceal the array of framed photos hanging on her wall."
    "They’ve all been turned backwards."

    $ renpy.end_replay()
    $ maki_love += 3
    $ sadgirls6 = True

    "........."
    "......"
    "..."

    jump sadgirls7
...
```