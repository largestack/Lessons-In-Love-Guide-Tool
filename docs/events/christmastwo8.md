# Dohoonkabhankoloos
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo8&go=Go)


Part of event chain [Love Set to Max](./christmastwo7.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo8
* Group: Main
* Triggered by label: christmastwo7

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo8:
    scene christmaskaraoke1
    with dissolve2
    play music "amisings.mp3"

    "A scene not at all dissimilar from many I’ve witnessed in the past- accompanied by scent of various baked goods and...alcohol?"
    "Oh well. I guess if my students are going to start recreationally drinking, it’s better if I’m around them or-"

    play sound "static.mp3"
    scene dodgingsnowflakes18 with flash
    scene christmaskaraoke1 with flash
    stop sound

    s "..."

    "Anyway, it looks like Yasu is doing fine, so I will now label my mission from Touka as complete and hope she does not misplace my present and make me look worse than I already am."

    if bonus == True:
        "Which is pretty bad since I’ve already had sex with a decent portion of this room."
    else:
        "Which is pretty bad since I’ve already secretly hugged a decent portion of this room."

    t "I am impressed by your ability to accurately replicate this song, Strawberry Princess."
    t "Every time I have attempted to sing, it has ended in tragedy. "
    t "I believe the Emerald Guardian has said something about multiple notes being required, while I only know one of them."
    ya "..."

    "Ami doesn’t respond to Tsuneyo on account of her undying desire to always be the center of someone’s attention and just keeps singing away at some song I’m sure I’ve heard playing in her room before."
    "The song doesn’t really have anything to do with Christmas, but it’s not like I’m complaining about that."
    "Frankly, Christmas music joins the ranks of things like the obligation to buy presents or...bright lights as yet one more characteristic that makes this time of year hard to deal with."

    ya "..."
    s "..."

    "Speaking of things that are hard to deal with, maybe I {i}should{/i} try and see if Yasu is at least...conscious."
    "She’s been standing as still as a statue for as long as I’ve been looking at her- which is a vast departure from her seemingly inherent desire to always wander around when she’s not busy “praying.”"
    "Oh. Maybe that’s it."
    "Maybe this is just another example of some ridiculous religious practice that I neither want to nor have the mental capacity to understand."
    "Yeah. That’s it."
    "My mission really is complete after all."

    ya "..."
    s "..."

    "Okay, I’m going to go talk to someone else before staring at her any longer begins to rot my brain."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene christmaskaraoke2
    with dissolve

    ay "Sensei! What a pleasant surprise! I totally haven’t spent the entire day waiting for you to get here or anything!"
    s "The entire day? You were literally at my house this morning."

    scene christmaskaraoke3
    with dissolve

    ay "Yeah, about that! Why did you lock your door?! I wanted to come say good morning!"
    s "To prevent you from sneaking into my bedroom in the middle of the night, obviously."

    scene christmaskaraoke4
    with dissolve

    ay "Ohhhh, I see. You were just worried you wouldn’t get any sleep on account of-"
    s "Ahem."

    "I clear my throat and make an obvious gesture toward Karin, who is becoming increasingly uncomfortable with the direction this conversation is beginning to head in."

    scene christmaskaraoke5
    with dissolve

    ay "On account of all of the Christmas movies we were supposed to watch together, obviously!"
    ka "Ah! You guys were going to watch Christmas movies?! I used to watch those with Kirin all the time before she..."

    scene christmaskaraoke6
    with dissolve

    ka "Decided she didn’t like me anymore..."
    s "..."
    ay "Uhh..."
    ay "You can...watch them {i}with{/i} us next year?"
    s "Ayane, why are you making plans for next Christmas in the middle of the current one?"

    scene christmaskaraoke7
    with dissolve

    ay "I panicked! You saw how sad she looked!"
    ay "Besides, you never know when time might get all weird and like...start over or something!"
    ka "I...would love watching movies with you guys, but...I don’t know if I’d...want to watch them in...S...S...S-"
    s "Sensei’s room. Ayane, what did you just say?"

    scene christmaskaraoke8
    with dissolve

    ay "Hm? The time thing?"
    s "Yeah. Say it again."
    ay "That...we never know when time might start over?"
    ay "I wasn’t being serious, but...you look really interested all of a sudden."
    s "So it’s just a random thought that popped into your head? There’s no...deeper meaning or anything?"

    scene christmaskaraoke9
    with dissolve

    ka "Are...you interested in time travel, Sensei?"
    ka "If...time travel is even what we’re talking about, I mean. I’m having an admittedly hard time following right now."
    s "Not particularly. Ayane just said something that sounded a little strange to me, is all."

    "Especially considering the last time there actually {i}was{/i} a reset, Ayane showed up halfway through only to subsequently disappear a few minutes later."

    scene christmaskaraoke10
    with dissolve

    ay "I say strange things all of the time. It’s like, a cornerstone of my bubbly, rambunctious personality. How come this one is the one you single out as being “too weird?”"
    ay "All things considered, I think it’s one of the more...tame things I’ve said."
    s "What if I told you that you’re not far from the truth, though?"

    scene christmaskaraoke11
    with dissolve

    ay "Are you asking me what I’d do if we only had a brief amount of time left before the world started over? Because the answer is simple, Sensei!"
    ay "I’d make you mine and stop worrying about other people getting in the way! And spend every single second with you until my random time prediction came true!"
    ay "Then, I’d do it all over again from the beginning, knowing full-well that the world is on a repeating cycle!"
    ay "Like I said, it’s simple! What else would you expect me to do in a world where the two of us are infinite?"
    s "Maybe freak out a little more about the idea of circular time but, you know, I realize now that this was just wishful thinking on my part."

    scene christmaskaraoke12
    with dissolve

    ay "I’m not sure where this sudden fascination with the weird things I say came from, but I’m just going to chalk it up to you falling more in love with me if that’s okay."
    ka "And I’m...also here still..."
    s "Would you like to share your thoughts on the concept of time, Karin? Quietly, though, so Maya doesn’t overhear anything and suddenly get invested."

    scene christmaskaraoke13
    with dissolve

    ka "I’ve...never really thought about it..."
    ka "And I definitely didn’t expect to be talking about it at a Christmas party, but..."

    scene christmaskaraoke14
    with dissolve

    ka "I think...time is..."
    ka "..."
    ka "Uh..."
    ka "..."
    ka "Neat?..."
    s "..."
    ay "Well said, Karin! I think my infinite love story was a little more interesting, though. But I’m sure that if you keep working hard, you’ll find someone you love as much as I love Sensei one day."
    ay "Then, you can have your own infinite love story!"

    scene christmaskaraoke15
    with dissolve

    ka "HAHAHAHA! L-L-L-LOVE! FUNNY JOKE, AYANE!"
    ay "..."

    scene christmaskaraoke16
    with dissolve

    ka "Why...did I just yell that?"
    ay "Umm...anyway, what do you plan on doing for the rest of the night, Sensei? Just going to walk around and maaaaybe think of your favorite rich girl all night or something?"
    s "I already talked to Touka today. I don’t have to think about her anymore."

    scene christmaskaraoke17
    with dissolve

    ay "Hey! That’s mean! I didn’t realize this was a category I actually had to compete in! I love you way more than Touka ever will!"
    ay "I’ve even been holding onto this crisp, refreshing bottle of Coca-Cola for you ever since I got here!"
    s "...Why?"
    ay "To prove my love!"

    scene christmaskaraoke18
    with dissolve

    kaay "Nothing says love like sharing a Coke."
    s "..."

    scene christmaskaraoke19
    with dissolve

    s "Okay. Well, I’m going to go see how a significantly shorter group of girls is doing and...I guess I’ll see you two around."
    ay "Okay! We’re not going anywhere, so feel free to drop by whenever you want."
    ay "Also, if that whole time thing really does start happening and you want to embark on our epic journey of romance and {i}handholding{/i}, please don’t hesitate to contact me!"
    ay "Ayane Amamiya is open 24/7 when it comes to her beloved teacher slash future husband."
    ka "And...uhh...I will...also be here..."

    scene black
    with dissolve2

    "I step away from Ayane and Karin and help myself to a crisp, refreshing Coca-Cola on the way across the room."
    "The group of girls crowding around the karaoke machine has since increased in size with Uta and Touka (Who managed to slip inside without me noticing) forming a small semi-circle around my [niece]."
    "It will only be a matter of time until Ami is forced to stop singing and surrender the microphone to one of the others, though."
    "And even though the amount of attention she’s receiving right now should sustain her for the next several hours or so, I’m sure she’ll find another way to feed off of all of our energy soon enough."

    scene christmaskaraoke20
    with dissolve2

    mi "Merry Christmas, Sensei! Thank you for another year of making sure I don’t have to learn anythin’ in class!"
    s "{i}Another{/i} year?"
    mi "Hm? S’at a weird thing to say?"

    scene christmaskaraoke21
    with dissolve

    sa "I think he...means since...he’s only been our teacher for one..."
    mi "Really? I guess time really does fly when ‘yer havin’ fun, then."
    s "Speaking of fun, do you know what {i}I{/i} think would be fun, Miku? Not looking at Touka all night."

    scene christmaskaraoke22
    with dissolve

    mi "But you {i}love{/i} lookin’ at girls! ‘Specially ones with massive dohoonkabhankoloos."
    s "I like staring at all girls equally, thank you very much. I just mean that {i}you{/i} in particular shouldn’t look at her."

    scene christmaskaraoke23
    with dissolve

    mi "Uh...you mind if I ask why? Or is that gonna somehow ruin all of the fun you think I’ll have ignorin’ a classmate?"
    s "She’s just carrying a thing you’re not allowed to see. It wouldn’t have been an issue if I had just followed the rules- but rules are for losers."
    mi "I still don’t get it, but I’ll trust ya. Whaddya want me to do if she tries to talk to me, though?"
    s "I don’t know. Talk about being poor or something. That might scare her away."
    sa "But...Touka has been...getting a lot better about...um...accepting us...non-rich people..."
    s "You’re all getting better at all sorts of things, but you’ll still always have your weaknesses."
    mi "Uh-oh. Sensei’s goin’ into life lesson mode. Put back on your earmuffs, Sana."

    scene christmaskaraoke24
    with dissolve

    s "I’m not going into {i}any{/i} mode. I just think it’s beneficial to never expect anyone to fully recover from the things that bring them down."
    s "It’s why I’d never send Sana out to buy lunch for me and why I’d never put you in a loud-"
    s "Wait, how are you doing right now, Miku?"

    scene christmaskaraoke25
    with dissolve

    mi "You’re sure askin’ me a lot of questions tonight, Sensei. You sure you don’t wanna shoot some of ‘em Sana’s way as well?"
    s "I just mean with all of the noise. It’s pretty loud in here and you seem fine."

    scene christmaskaraoke26
    with dissolve

    mi "O-Oh! You mean with that..."
    mi "Yeah, I’m doin’ okay. Makoto and I got here a little after everybody else, so I haven’t been puttin’ up with it for long."
    mi "Don’t know what that means for later, but...I’m all good right now. Peachy as a...peach."
    s "Where {i}is{/i} Makoto, actually? It’s rare to see you two separated at parties and I haven’t seen her yet."

    scene christmaskaraoke27
    with dissolve

    sa "I...umm...think she went into the bedroom with...Nodoka and...Miss Imai."
    s "I was really worried about the context of that sentence until you said Imani was there, too."

    if bonus == True:
        "Now, I’m just even more excited."
        "Just kidding."
        "I don’t know how Imani feels about sexual contact with students, but I’m hoping her opinion isn’t {i}too{/i} far off from mine or it might be a little too hard for the two of us to really understand one another."

    s "Wait, why is Imani here? Who invited her?"
    mi "Do you not want her to be here or somethin’, Sensei?"
    mi "Think she might get in the way of you spendin’ some alone time with my BFF or somethin’?"
    s "I’m just surprised she came on such short notice. Or...how she even knew about it in the first place."
    sa "You...know you can just...ask her...right?"
    s "I’m really not liking your attitude tonight, Sana."

    scene christmaskaraoke28
    with dissolve

    sa "Wh-What attitude?! I haven’t done anything!"
    s "Are you raising your voice at me right now?"
    sa "No! Yes! I don’t know!"
    s "Sana, I’m really going to need you to calm down."

    scene christmaskaraoke29
    with dissolve

    sa "Mm!"
    mi "Sensei! The heck do ya think you’re doin’?! You made Sana cry and you’ve only been here for like ten minutes!"
    s "Sana, why are you crying? I thought it was obvious I was just kidding."
    sa "I...just am!"
    sa "It’s no big deal!"
    s "Do you need me to-"
    sa "No thank you!"
    s "But I didn’t even-"
    mi "Sensei, let me field this one. You go hang out with Makoto and maybe plant a big wet one on those luscious lips of hers right in front of the new teacher."
    mi "Really just assert your dominance. Alpha style."
    s "Great idea, Miku. I’m sure randomly kissing someone like that wouldn’t have any repercussions whatsoever."

    scene christmaskaraoke30
    with dissolve

    mi "What do drums have to do with this?! Get over there and mingle, coach! Do what ya came here to do! Talk to girls and conquer hearts!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "Fine. But I’m only doing this because it’ll make it look like you made Sana cry instead of me."
    mi "Ain’t nobody gonna think that, Sen-"
    ay "Miku! Why is Sana crying?! What did you do?!"
    mi "I...ahh! Crap!"
    mi "Sensei! Come back!"

    "Farewell, Miku."
    "Hello, everyone else."

    $ renpy.end_replay()
    $ christmastwo8 = True

    jump christmastwo9

label christmastwo9:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
s "And also very fun."
    to "But Futaba is {i}very{/i} kind and you never take advantage of her! Is this class warfare?! Is this how your people “eat the rich?!”"
    s "Touka, don’t yell or you’re going to startle the bear."

    scene welcometoxmastwo24
    with dissolve

    to "Oh no! I’m so sorry, little-"

    scene welcometoxmastwo25
    with hpunch

    to "Wait! You’re doing it again right now! Taking advantage of my kindness!"
    f "I’m...not saying Sensei is in the right here, but...you should have known better than to think a stuffed bear would have feelings, Touka..."

    scene welcometoxmastwo26
    with dissolve

    to "Technology is advancing quite rapidly, Futaba. And I do not know what sorts of toys the middle class has access to."
    to "I don’t think it’s foolish to believe that one day, all little boys and girls will be able to play with stuffed animals that can think and feel just like you and me."
    f "I think...that sounds kind of terrifying."
    s "So is this just how you two are spending Christmas? Standing out in the hallway talking about robot uprisings?"

    scene welcometoxmastwo27
    with dissolve

    to "This is the very first uprising we’ve discussed, actually."
    f "We were talking about more...normal stuff before you showed up, Sensei..."
    to "That is correct. Futaba and I seldom interact with one another and, as it turns out, we have quite a bit in common."

    if bonus == True:
        s "Like how you’re the two most well-endowed girls in the class?"
    else:
        s "You know, I'm glad this game was heavily censored. It's made for some really memorable moments- wouldn't you agree?"

    scene welcometoxmastwo28
    with dissolve

    to "You are a truly horrible man."
    f "Was that really necessary?..."
    s "Don’t tell me Touka’s turned you against me, has she?"

    scene welcometoxmastwo29
    with dissolve

    if bonus == True:
        f "I’m not against you! There’s just more we have in common than...that thing you said we have in common!"
    else:
        f "Censorship is bad!"

    s "Well, I hope you two enjoy hanging out in the hallway and talking about how my only mission in life is tormenting Tamamo."

    scene welcometoxmastwo30
    with dissolve

    to "Touka! And what am I supposed to do with this bear?!"
    s "Just hold onto it until it’s time for the Secret Santa thing. "
    to "But that’s your responsibility!"
    s "Touka, it’s actually customary for a student to hang onto a stuffed animal for the teacher during a class Christmas party. It means that I think you show the most promise in life."

    scene welcometoxmastwo31
    with dissolve

    to "Is...Is that so?"
    f "No, Touka. Please don’t listen to him."
    s "I believe in you, Toriko. Please take care of that gift that I will once again remind you is for someone else."
    s "Now, if you’ll please excuse me-"

    scene welcometoxmastwo32
    with dissolve

    to "Wait, Sensei- I will continue holding onto this bear for you, but could you please do me a favor and see how Yasu is doing?"
    to "I’ve been attempting to have her “roam free” tonight, and I am worried about the effects that this mysterious “karaoke machine” are having on her."
    s "Is...Yasu singing in there?"
    to "She is not. But she has been staring in awe ever since the machine was turned on."
    to "I even attempted to boop her nose, but there was no effect at all."
    s "I’m sure she’s fine, but I’ll make sure to confirm whether or not she’s slipped into a coma for you if that’s all it takes to have you hold that present for the rest of the night."
    s "Do you need me to check on your roommate as well, Futaba?"
    f "It would {i}probably{/i} be better if you didn’t, actually. Her and Otoha have been...very close ever since last night."
    s "Oh yeah?"
    f "Yes, but...I don’t think I should really give you any more info than that..."
    s "Works for me. I’ll just go...hang out with everyone else then, I guess."
    s "I’ll see you two around. And don’t lose the bear."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I make my way into the hotel room only to be bombarded by the sound of loud feedback spilling out of a small karaoke machine placed near the TV. "
    "It mixes in with a handful of scattered conversations that I’m unable to discern due to the sheer amount of them happening simultaneously."
    "It’s noticeably louder than last year’s party, but I guess that’s to be expected when the student count has nearly doubled."
    "Anyway, a familiar voice takes the place of the feedback and, within a matter of seconds, a new sound fills the room and serves as my cue to begin mingling."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ christmastwo7 = True

    jump christmastwo8
...
```