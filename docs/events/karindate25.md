# Emerald Eyes
Karin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karindate25&go=Go)



## Event preconditions
✅Karin love greater than or equal to 25

❌Event "[Maki: Baby Steps](./makiinv3.md)" is completed (event=makiinv3)

✅karinnumber equal to True (unknown variable)



## Next events
* [Karin: Wrong Places/Wrong Times](./karindate30.md)
* [Tsukasa: National Tsukasa Day](./tsukasaspecial1.md)

## Event properties
* ID: karindate25
* Group: Karin
* Triggered by label: callkarinafternoon
* Triggered by branch label: callkarinafternoon

## Event code
File: \game\KarinEvents.rpy
Code:
```python
...
label karindate25:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."
    "Given the fact that I am no longer the coach of the soccer team and can no longer hide these impromptu afternoon meetings behind the guise of supervising her training, I decide to just...go for it when she answers."

    play sound "phonebeep.wav"
    play music "notabluearchivesong.mp3" fadein 3.0

    ka "Hello?"
    s "Let’s hang out."
    ka "AHHHH!!!"

    play sound "phonebeep.wav"
    with hpunch

    s "..."

    "Okay. Maybe I “went for it” a little too directly as Karin’s initial reaction was to just hang up."
    "Thankfully, I think I know her well enough at this point to predict that in several seconds, she’s going to call me back and apologize."

    s "..."
    s "..."
    s "..."

    play sound "phonering.mp3"

    "Knew it."

    play sound "phonebeep.wav"

    s "H-"
    ka "I’m so sorry! I don’t know what happened! I just...sometimes I press buttons! It’s a thing that happens!"
    s "Does this mean you’re okay with hanging out, then?"
    ka "AHHHH!!!!!!!!"

    play sound "phonebeep.wav"
    with hpunch

    s "..."

    play sound "phonering.mp3"

    s "..."

    play sound "phonebeep.wav"

    s "H-"
    ka "It happened again!"
    s "Should I proceed with inviting you to do something? Or would you rather we just skip that conversation altogether and decide on a place to meet?"
    ka "I...I’d love to come meet up with you! I just...umm...I’m kind of already doing something, so-"
    mi "{i}Karin, who’s that? And how come ya keep yellin’ at ‘em if ya actually wanna go meet up?{/i}"
    ka "It’s umm...uhh..."
    s "You can tell her, it’s fine."
    ka "It’s...It’s Sensei."
    mi "{i}What the heck? Sensei’s callin’ you? I ain’t gonna have to compete against two of my best friends now, am I?{/i}"
    ka "C...Compete?"
    s "It’s a long story."

    "And one that involves more fingering than I should probably include in a conversation with Karin at this point in time."

    ay "{i}Karin! Tell Sensei I love him! And that my unquenchable desire for him grows stronger every day!{/i}"
    ka "Uhh...Ayane says something about...unquenchable desire?"
    ima "{i}Ask him if he can watch my parrot while I go to the spa tomorrow!{/i}"
    ka "And Miss Imai has a parrot."
    s "I see. "
    s "This has been a very informative phone call. Thank you, Karin."
    ka "I’m...sorry I can’t do anything right now! The girls from the club made plans to put something together for Makoto today because of her dad, so..."
    s "Got it. I’ll be right over."
    ka "Wait, what? "
    s "Yeah. Are all of you at the pool right now?"
    ka "I mean, we are. Yeah. But I can’t imagine you want to spend your weekend on-"
    s "Sounds to me like you’re underestimating just how badly I want to see you."
    ka "AHHHHHHHHH!!!!!!"

    play sound "phonebeep.wav"

    "Karin hangs up again, but I saw it coming this time."
    "Without anything else to do today, I begin making my way over to the school to help with whatever the swim club has decided to “put together” for Makoto."
    "And while the thought of this is something that should hold the head of my day underwater long enough to drown it in a sea of my worries, my desire to stay {i}above{/i} water for now wins out in the end."
    "Because even if there’s one girl suffering beyond the reach of all of us right now, there are plenty more that aren’t."
    "Dragging the broken one back is a task that would prove impossible for just one person, but the efforts of a group will surely be much better in that regard."
    "And being a part of that, even if it’s only for a small amount of time, is sure to help me as well..."
    "........."
    "......"
    "..."

    scene karinmalltrip1
    with dissolve2

    mi "Welcome to the party, Sensei! I’ve only cried one time!"
    s "That sounds like a reasonable improvement from how you’ve been lately, so good for you."
    ima "There’s plenty of pizza if you want any, Senpai. Ayane’s butler did a hell of a job carrying all of it in here in just one trip."
    ay "He cooked it himself as well. If you showed up a few minutes earlier, you might’ve even finally got to meet him."
    ay "Also, do you not love me anymore? "
    s "What?"

    scene karinmalltrip2
    with dissolve

    ay "Oh, nothing. I just figured you would have called me instead of Karin given that she doesn’t even know about the rooftop apocalypse team yet."
    mi "The...what now?"
    ka "Hahahah...I’m sure he just...clicked on my name instead of my sister’s on accident..."
    s "Does it really matter who I called now that I’m spending time with all of you?"
    ay "Yes. Yes, it does."

    scene karinmalltrip3
    with dissolve

    ay "But {i}I guess{/i} I can overlook that since I also understand and appreciate just how wonderful Karin is. "
    ka "I don’t really know what this stuff about being wonderful is, but I’m glad you were able to come by and help."
    s "No need to thank me. I care about Makoto as well and I’m sure that whatever this is will do a lot more for her than I’ve been able to do on my own."
    s "It would be good to know exactly {i}what{/i} you’re putting together, though."
    ka "It’s just a little...care package thing. Cards...gifts...stuff like that. I don’t really know much about Makoto yet, though...so I haven’t been as helpful as I’d like."
    ima "She says, despite being the one to come up with this idea. "

    scene karinmalltrip4
    with dissolve

    ka "Well...when I sprained my ankle playing softball when I was little, the rest of the team did something like this for me and it...really made me feel a lot better."
    ka "Obviously what Makoto is going through is a million times worse than that, but...I still figured it might make her a little happy to get something from all of her friends."
    s "I don’t know if “happiness” is something she’s personally able to feel right now, but I do think she’ll appreciate the gesture."
    s "So, what can I do to help?"
    ima "You can get lost, that’s what."
    s "Wow. Fuck you too, Imani."

    scene karinmalltrip5
    with dissolve

    ima "No, like seriously. We’ve already got a lot of the things we need, but if we’re gonna stick to Karin’s plan and put together the world’s greatest care package, we’re gonna need a bunch of other stuff."
    ima "Plus, the other two girls and I have to go around collecting signatures from all of the {i}other{/i} girls anyway, which is a big ask on its own."
    s "The other {i}two{/i} girls? But there are four of you."
    ima "Yeah. But you and Karin are gonna go out on a date, obviously."

    scene karinmalltrip6
    with dissolve

    ka "D-D-D-D-DATE?!"
    ka "US?! "
    mi "Guh. Startin’ to make sense why Makoto’s always so stressed when it comes to Sensei seein’ other girls."
    ay "So that’s how it’s going to be, Sensei? You take me up on the roof just to leave me for Karin? Has this been your plan all along?"

    scene karinmalltrip7
    with dissolve

    ka "This was never a plan! I didn’t even know Sensei was coming! And I didn’t know I was leaving until thirty seconds ago!"
    mi "That’s just what she wants us to think, Ayane. Karin might look sweet on the outside...but on the inside? She’s just as conniving as the rest of ‘em."
    s "Are you proud of yourself, Imani? Sowing the seeds of destruction in your own club?"
    ima "Hey, my original gameplan before you showed up was to just take everybody to the mall {i}myself{/i} after collecting signatures. You being here just means things are getting easier for me too."
    ima "Plus, this’ll give you and Karin some of that “alone time” I’m sure you called her for and she’s a lot closer to being legal than everybody else you’re always hanging around with."

    scene karinmalltrip8
    with dissolve

    s "..."
    s "Can you all not look away like that?"
    ka "I...I...I guess if...the teacher says we have to go out...there’s...nothing I can do to prevent it!"
    s "You realize I’m a teacher too, right? And that Imani only exists to serve me?"

    scene karinmalltrip9
    with dissolve

    ima "Oof. Not cool, man. Not cool."
    s "What? You-"
    s "Oh."

    scene karinmalltrip10
    with dissolve

    ima "And to think that you were my {i}first.{/i} Does the heart of this fair maiden mean nothing to you?"
    ay "Imani too?! When will it end?!"
    ka "First what? I don’t get it."
    s "Okay, well...at the risk of Imani getting everyone here to turn against me, I suggest we head out. Especially since we apparently have to go all the way to the mall?..."

    scene karinmalltrip11
    with dissolve

    ima "Hey, if you can find everything on Karin’s list elsewhere, feel free. I just figured the mall would be cool  because they have everything."
    ima "It definitely doesn’t have anything to do with my desire to remain forever young and wander the halls with a bunch of high school girls."
    s "Yeah, I’m sure that much was just a complete coincidence. "
    ka "The list isn’t {i}that{/i} long, so...I’m sure we can finish quickly if you hate spending time with me."
    s "Why would I have called you at all if that were the case?"
    ka "Because Karin and Kirin are only one letter apart and...you have bad eyesight?"
    ima "Oh, and speaking of phones, take my number down so we can meet back up once you guys are done."

    scene karinmalltrip12
    with dissolve

    mi "What kinda smooth move is that, Miss Imai?! Just givin’ your number out like it’s a piece of friggin’ candy! Can’t ya see this guy is just gonna use ya as a booty call?!"
    ima "Hey, at least he’ll be saving money. All those carrier pigeons he’s been sending over to my place for analog booty calls are sure to get costly after a while. "
    ay "Sensei has never sent me a booty call pigeon..."
    mi "Pigeons ain’t even real! Birds are a conspiracy created by the government to watch us! Kirin showed me a video all about it!"
    s "Okay, Karin. Come on. We’re leaving before this gets even more ridiculous. "

    scene black
    with dissolve2

    "Imani takes my phone and adds her contact info to it, preparing herself for a lifetime worth of booty calls that I highly doubt would yield any form of success at this point in time."
    "Ayane and Miku go back to sulking as they pack things up and get ready to start soliciting signatures, while Karin and I awkwardly make our way out of the pool room and over to the nearest bus stop..."

    $ imaninumber = True

    "{i}Congratulations! You now have Imani’s phone number!{/i}"

    scene sky
    with dissolve

    "The bus arrives within minutes, sparing us from whatever sort of awkward conversation topics Karin was sure to come up with as we waited."
    "That doesn’t prevent things from still {i}being{/i} awkward, though, as we take our seats on the bus and she has to endure the inner struggle of either sitting {i}next{/i} to me or in the seat across the aisle."
    "Thankfully, she bites the bullet and sits beside me so we don’t have to shout over a row of empty space just to be able to communicate with one another."
    "{i}Less{/i} thankfully, we wind up not communicating at all on the way to the mall, prompting me to believe that I would have preferred even the most awkward of conversation topics over that."
    "Once we’re back on land, though, she opens up again."
    "I guess it’s only the thought of being trapped somewhere with me that eats away at her."
    "But despite my usage of the word “eat,” the form of consumption I’m referring to is not one of negativity."
    "What is being eaten away is that lingering sense of purity of hers and how she is one of the only girls I know at this point who would deny the opportunity to sleep in my bed."
    "For in those moments we are trapped, she is forced to come to terms with things she struggles to understand about herself."
    "And in those moments we are trapped, I must prevent myself from coming to terms with the things I understand about her."

    scene karinmalltrip13
    with dissolve2

    "We find ourselves on a bench I’m known to frequent, but never with her."
    "She sits where the other has, in older yet fresher skin as she looks up at me with a sense of unfamiliar unease deep inside of her emerald eyes."
    "I think about plucking those valuable gems from out of her sockets and pawning them off for one more gift to a girl more tainted than she is."
    "For it is those who feel the darkness creeping in that deserve the most-"
    "And it is those who have not yet been touched by it who must be left alone."

    ka "So...umm..."
    ka "I...guess I wasn’t busy after all?"
    s "In all fairness, it’s not like this is a particularly {i}happy{/i} outing. We’re shopping for a girl who lost her dad."

    scene karinmalltrip14
    with dissolve

    ka "Yeah..."
    ka "I wish there was something more we could do."
    s "I think what we’re doing now is plenty. Makoto seems like she wants to grieve in silence for the most part. So as long as she knows we’ll be here whenever she comes out of her cave, she’ll probably be fine."

    scene karinmalltrip15
    with dissolve

    s "Or not."
    s "Death is complicated."
    s "To some people, it’s like the world is falling apart. But to some others, it’s like nothing’s really changed at all."
    ka "What...is it like for you, Sensei?"
    ka "If that’s...something you’re okay with me asking."
    s "I’m more interested in hearing what it’s like for you, if you’re okay with {i}me{/i} asking."

    scene karinmalltrip16
    with dissolve

    ka "Unfortunately...that’s not really an easy question for me {i}to{/i} answer."
    ka "I’m kind of...terrified of it, really."
    ka "I don’t have any...{i}experience{/i} with death yet."
    ka "Well, other than my goldfish Benjamin who died when I was six years old. But I haven’t really thought about him again until right now and oh my God I am suddenly sad."
    s "Yeah. I think that’s kind of just...how it’s supposed to work after a while."
    s "Unfortunately, it’s not..."
    s "..."

    scene karinmalltrip17
    with dissolve

    ka "Sensei?"
    s "Unfortunately, it’s not like that for everyone. And we all have our own ways of facing it."
    s "I’m sure you’ll come to experience it someday. And I’m sure that, when you do, you’ll learn things about yourself that you’ve always feared learning."
    s "But I don’t think it’s something you should let suppress you. If you live in fear, you’ll miss out on a lot of the better parts of life."
    s "And while there aren’t many of those when you’re as jaded and cynical as I am, they still exist."

    scene karinmalltrip18
    with dissolve

    ka "Yeah...you’re probably right."
    ka "It just feels horrible not understanding what other people are going through because it’s like I can’t...help them as much as they need me to."
    ka "So sometimes I wish I {i}did{/i} understand. But I know that wishing that means something horrible would have to happen to me and..."
    ka "I guess I’m a little selfish in that sort of way."
    s "If your idea of selfishness is not wanting someone you love to die, I think you’re a lot more selfless than you believe."
    ka "..."
    s "..."
    ka "Umm..."
    ka "There are...other ways I’m selfish, you know..."

    scene karinmalltrip19
    with dissolve

    ka "Ways that are a lot less depressing and-"
    ki "Uhh...what the actual fuck is going on right now?"

    scene karinmalltrip20
    with dissolve

    ka "K...Kirin?"
    n "And Noriko! I am also here. Hi, Sensei."
    s "Hey. What are you two up to?"
    ki "Isn’t that what we should be asking you?"

    scene karinmalltrip21
    with fade

    "Karin gets off of the bench and marches over to Kirin with a look of determination I seldom see from her in situations like these."
    "It’s no joke to say she normally takes the backseat when dealing with her sister, but it seems that something about today’s {i}circumstances{/i} have made that very much not the case."

    ka "Is there a problem, Kirin?"
    ki "Problem? No. I’m just surprised to see a prude like you out and about with an older man."
    ka "You know that a girl and a b...{i}boy{/i} can go out in public without being like that, right?"
    s "I prefer “man,” but please, proceed."
    ki "Of course {i}I{/i} know that. But does Sensei know that?"
    ka "Do you think we’re on a date or something? Is that why you’re so jealous right now?"
    s "I mean...Imani {i}did{/i} say that-"

    scene karinmalltrip22
    with dissolve

    ki "Jealous? You think I’m {i}jealous?{/i} Of what?"
    ki "Just because there’s {i}one{/i} guy in your life that you can talk to without pissing yourself now doesn’t mean I’m suddenly going to be {i}jealous.{/i}"
    ki "But hey, if you want to keep enjoying your {i}date,{/i} go ahead. Noriko and I are going to go buy new underwear."
    n "We are? I thought we were going to the mov-"
    ki "Shut up, Noriko."
    ka "You want to know why we’re really here, Kirin?"
    ki "Yeah, sure. I’d {i}love{/i} to hear what sort of thing could get my sister out of the house and into the company of some fucking dinosaur."
    s "That was unnecessary."
    n "I agree. That was unnecessary. Sensei is in the prime of his life and you of all people should-"
    ki "Shut the {i}fuck{/i} up, Noriko."
    ka "Fine. Since you want to know, I’ll tell you."
    ka "Sensei and I are here to buy presents for Makoto. Who, in case you happened to forget, just lost her dad."

    scene karinmalltrip23
    with dissolve

    n "Hah..."
    ka "Yeah. Bet you feel like a jerk now, don’t you?"
    ki "That..."
    ki "Uhh..."

    scene karinmalltrip24
    with dissolve

    ki "Well, how was I supposed to know that?! There’s no way anyone would guess that on the first try!"
    n "Can we go to the movies now? I don’t like it when I have to skip the previews and you’re always making us show up late."
    ka "Apologize."
    ki "For what?! Assuming you two were {i}together?!{/i} Why are you even offended by that?!"
    ka "I’m not asking you to apologize to me. I’m asking you to apologize to Sensei for assuming he’d ever look at me that way."

    scene karinmalltrip25
    with dissolve

    n "I mean..."
    ki "Don’t fucking hit on my sister, Noriko."
    n "I’m not saying I {i}wouldn’t...{/i}"
    ki "Noriko-"

    scene karinmalltrip26
    with dissolve

    n "You say weird stuff about my sister like fifteen times a day! How is this fair?!"
    ki "Shut up! We’re leaving!"

    scene karinmalltrip27
    with dissolve

    n "Fine. Let me just tell Sensei I love him a few thousand times first. I love you. I love you. I-"
    s "Now’s probably not the best time, Noriko."

    scene karinmalltrip28
    with dissolve

    n "Just thought I’d remind you. That’s all."
    n "Is there anything you still need for Makoto? Kirin and I can pick something up after the movie."
    ka "Are you sure? Because the only things left are a little on the pricey side and-"
    n "It’s fine. Don’t even worry about it. Just tell us what to get and we’ll help out in any way we can."

    scene black
    with dissolve2

    "Karin returns to the bench to grab her list out of her bag and rattles off the names of different items in her Makoto Miyamura condolence care package."
    "Among them are a series of books that Miku and Maki compiled into a list, several packages of assorted fancy fruits, skin care products, and other things of that nature."
    "Kirin and Noriko note everything down in their phones before leaving the two of us alone and, knowing that they’ll be getting at least the skin care stuff, our trip is significantly shortened."
    "We leave the mall to meet back up with Imani and the others and, within the hour, I am removed from the group."
    "This time, however, I’m not paired with an attractive girl to spend the rest of the day with and am forced to go home alone to drown in my thoughts."
    "Among those thoughts are several visions of emerald eyes."
    "And how my desire to pluck them becomes greater each time they appear."

    $ renpy.end_replay()
    $ karindate25 = True
    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label karindate30:
...
```

## Code that triggers this event
File: \game\KarinEvents.rpy
Code:
```python
...
label callkarinafternoon:
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
    if karin_love >= 5 and day103 == True and karindate5 == False:
        jump karindate5
    if karin_love >= 10 and mollycafe1 == True and karindate10 == False:
        jump karindate10
    if karin_love >= 15 and day264 == True and karinlied == True and karindate15 == False:
        jump karindate15
    if karin_love >= 20 and day355 == True and karinsoccer20 == True and karindate20 == False:
        jump karindate20
    if karin_love >= 25 and makiinv3 == True and karindate25 == False:
        jump karindate25
...
```