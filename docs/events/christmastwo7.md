# Love Set to Max
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo7&go=Go)


Part of event chain [Engulfed](./saralust20intro.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo7
* Group: Main
* Triggered by label: saralust20intro

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo7:
    scene wintersky
    with dissolve2
    play music "stpartynight.mp3"

    "This year’s Christmas party is taking place in the same exact hotel as the last one so, after finishing up at Sara’s, I catch a bus across town in an effort to give my body its own sort of Christmas present."
    "Being someone who doesn’t exactly enjoy exercising on even normal days of the week, I figure that today being Christmas should be enough of an excuse to at least exempt me for now."
    "Besides, I spend enough of my normal days walking as-is."
    "And I still need to find somewhere to buy Miku a present- a thing I have decided to do because ruining two Christmases in a row is a little {i}too{/i} on brand for me and I want to mix things up."
    "As such, I make my way into the first discount store I find and quickly begin perusing their varied selection of goods in hope of uncovering some sort of treasure a [teenage]girl might enjoy."
    "If you ever find yourself Christmas shopping for someone you have a moderate amount of care for, I recommend bringing along a game plan- because things aren’t going too great for me right now."
    "Originally, I thought I could just get off with buying a soccer ball or something- but I know for a fact that Miku already has like seven thousand of them."
    "Okay, maybe that’s an exaggerated fact- but I know damn well she has a lot."
    "After searching around for nearly ten minutes and not being able to find {i}anything{/i}, I come across a rack of toys and stuffed animals clearly not meant for someone Miku’s age."
    "However-"
    "Miku is extremely immature and often acts like a real child, so this is enough to justify, at least in my head, purchasing something from this section of the store."
    "I am sorry in advance to Miku, who may or may not think this potentially used stuffed bear is an adequate present. "
    "But, if you really think about it, any present is an adequate present when you’re not obligated to give someone something."
    "So Miku should find solace in the fact that I went out of my way to do this rather than just leaving her with absolutely nothing."

    s "..."

    "I think for a moment about getting something for Maya as well, seeing as she left the last party empty handed because of me."
    "But then I remember that I bought her a scarf that she wears every day- so I have already been forgiven for that misdeed."
    "And it’s not like she’s ever bought anything for {i}me{/i}, so the idea of buying her anything at all is one that’s simply just taking up unnecessary space in my head."
    "And I need all the space I can get right now, seeing as I am about to embark on yet another survival mission in trying to navigate a Christmas without tragedy."
    "An entire school sunk into the ground last time."
    "I can only imagine what wonders await me this year."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene welcometoxmastwo1
    with dissolve2

    "The first pair I encounter upon arriving is none other than Chika, dressed in the same outfit she wore to the last party, and Tsubasa, wearing...what she always wears."
    "I do notice the distinct lack of a demon clinging to her leg, though, so I guess her younger daughter stayed at home this year instead of-"
    "Wait, why is Tsubasa even here?"

    s "Ahem."

    scene welcometoxmastwo2
    with dissolve

    c "Ah! Sensei! Merry Christmas!"
    tb "Merry Christmas. And thank you again for always taking care of my daughter."

    scene welcometoxmastwo3
    with dissolve

    tb "Or {i}daughters{/i}, I suppose."
    c "Oh, stop. You don’t have to go that far. "
    tb "Of course I know I don’t {i}have{/i} to, dear. But, honestly, you’re much more bearable than Tsukasa is. And she lived inside of me for nine months."
    s "What are you doing here, if you don’t mind me asking?"

    scene welcometoxmastwo2
    with dissolve

    c "Tsubasa agreed to look after Chinami tonight so Yumi and I could come to the party!"
    s "So Chinami is upstairs right now? Is that safe?"
    c "She’s actually with Yumi at the moment, but they should be getting here soon. That’s why I’m waiting down here."
    tb "And {i}I’m{/i} waiting down here because I’m worried I may kill my youngest daughter tonight."

    scene welcometoxmastwo4
    with dissolve

    s "That’s...yeah, okay."
    c "Are you sure you’re okay with watching Chinami, too? She’s a good girl, but...well, she’s never really been around anyone her age before. So she might wind up getting a little hyper."
    tb "I’m sure it will be fine. Tsukasa’s spent most of her life in the manor, so she doesn’t have any experience with girls her age either. "

    scene welcometoxmastwo5
    with dissolve

    tb "And I can assure you that I’ve made sure the room is properly sanitized and free of anything that could harm the poor girl. You have my word that your future sister-in-law will be safe in my hands."

    play sound "static.mp3"
    scene imissyoumore with flash
    scene welcometoxmastwo6 with flash
    stop sound

    c "Sensei?"
    s "Yeah? What’s up?"
    c "You okay? You just froze up for a second."
    s "Hm? I’m fine. "
    s "Anyway, have you seen Miku around? I have to give her this present thing."

    scene welcometoxmastwo7
    with dissolve

    c "Oh, is {i}that{/i} who that’s for? I was wondering why you were just carrying a stuffed animal around."
    c "Aren’t you supposed to like, wrap it, though?"
    s "Chika, you should know by now that I never wrap anything."

    if bonus == False:
        "Wrapping paper is just so outrageously overpriced that I can't justify it."

    scene welcometoxmastwo8
    with dissolve

    tb "Oh my."
    c "Wha- Sensei?!"
    s "Really, though, have you seen her?"

    scene welcometoxmastwo9
    with dissolve

    c "I’m sure she’s upstairs with everyone else, but...I think we’re all doing the Secret Santa exchange as a group."
    s "Then what am I supposed to do with this unwrapped present? I can’t just stick it in the pile with all of the wrapped ones. People will know I’m the one who bought it."
    c "Well...I mean...you...kind of did that to yourself?"

    "Some {i}girlfriend{/i} you are."

    scene welcometoxmastwo10
    with dissolve

    tb "Chika darling, I’m going to head back upstairs before my daughter burns down the entire hotel. But feel free to bring Chinami up once your Yakuza friend arrives."
    c "Sounds good! Thanks again, Tsubasa! I’ll be sure to make it up to you sometime!"

    scene welcometoxmastwo11
    with dissolve

    tb "And {i}you{/i} be sure to treat my surrogate daughter well. Especially if you’re so against {i}wrapping things.{/i}"
    s "Oh, actually. On that note, can I ask you something?"

    scene welcometoxmastwo12
    with dissolve

    c "What could you possibly have to ask her on that note?!"
    tb "Me? Of course. What’s the matter?"
    s "Touka’s bed-"
    c "What about Touka’s bed?!"
    tb "Touka’s bed? You mean the one with rapid sleep technology? What about it?"
    s "Nothing. You actually just answered it. Thank you, Tsubasa."
    tb "I’m confused. But, that often is the case when it comes to communicating with people in the outside world."

    scene welcometoxmastwo13
    with dissolve

    tb "Anyway, do enjoy your Christmas together. I’ll be right down the hall if either of you need me."
    tb "Also, if you hear screaming, please do not tell anyone you saw me here."
    s "Understood. See you later, Tsubasa."

    scene welcometoxmastwo14
    with dissolve

    "Tsubasa makes her way down the hall, leaving Chika and I alone in the lobby."
    "Instead of pressing forward like I expect her to, though, Chika remains at a distance and awkwardly stares at me, waiting for me to speak."
    "Unfortunately for her, I am very bad at starting conversations, so I kind of just stand there as well."

    s "..."
    c "..."
    s "..."
    c "..."
    c "So, uhh..."
    c "..."
    c "Heeeeeeeey..."
    s "Why are you being so awkward?"
    c "I’m sorry. I’m just redirecting every single impulse in my body away from kissing you and it’s making things really hard for me."
    s "You know, Chinami said something to me a little while ago about you not getting enough sleep lately. Is that because of me? Because of what I said about slowing down?"

    scene welcometoxmastwo15
    with dissolve

    c "That little-"
    c "How does Chinami keep finding time to tell you the only things I don’t want her to tell you?"
    s "Just answer the question, Chika."

    scene welcometoxmastwo16
    with dissolve

    c "..."
    c "Yeah...it’s true."
    c "It’s not your fault, though. Just trying to like, reset my brain and stuff."
    c "If only love was like...some kind of knob you could just turn down whenever you wanted."
    c "I feel like I’m stuck on max settings all the time, and it’s kind of driving me crazy."

    scene welcometoxmastwo14
    with dissolve

    c "Please don’t worry about me tonight, though. I already made a promise to myself to give you as much distance as possible."
    c "This way, even if people did think there was something going on between us, they’ll think it’s over tonight."
    s "But are {i}you{/i} going to be okay with that?"

    scene welcometoxmastwo17
    with dissolve

    c "Absolutely."
    c "I’m stronger than I look, Sensei. I’ve dealt with my dad leaving...my mom dying...taking care of Chinami all by myself...tons of stuff!"
    c "Staying away from my boyfriend should be a walk in the park for someone like me!"
    s "Well, on that note, I’m going to go find something to do with this stuffed animal so I don’t have to hold it all night."
    s "Also, please try to sleep more. I know {i}me{/i} being the one to say that might feel like a slap in the face since I’m the one who caused it, but-"

    scene welcometoxmastwo18
    with dissolve

    c "I’m fine. Don’t worry about me, Sensei."
    c "Buuuuuut...you could maybe make me feel a {i}little{/i} bit better if you tell me you love me before going upstairs?"
    c "I think that might help hold me over a little."

    "I sigh to myself, knowing that I basically walked into this by not leaving the second I had an opening-"
    "But no one is around and...it {i}is{/i} Christmas, so..."

    s "I love you."

    scene welcometoxmastwo19
    with dissolve

    c "And I love you!"
    c "Now go on! Get out of here before I can’t hold back the urges anymore! Go, Sensei! Go!"

    scene black
    with dissolve2

    "Without saying anything else, I leave Chika behind and make my way to the elevator."
    "I got the room number from Ami earlier, so I already know where I’m headed."
    "I feel a little bad for just leaving Chika downstairs like that, but...I mean, I have twenty girls in my class. "
    "And even if she says she’ll be staying away from me to the best of her ability, I’m sure I’ll see more of her later."

    if chikalust10 == True:
        "Like...maybe on some bench outside of the hotel or something."

    "........."
    "......"
    "..."

    scene welcometoxmastwo20
    with dissolve2

    to "Good evening, Sensei. And a very merry Christmas to you as well."
    f "Merry Christmas, Sensei."
    s "Likewise."
    s "Here, Touka. Take this."
    to "Take what? What requires taking?"

    scene welcometoxmastwo21
    with dissolve

    to "Ah! An adorable plush bear! "
    to "Sensei! Is this a gift for me?!"
    s "Nope. I just need you to hold it."

    scene welcometoxmastwo22
    with dissolve

    to "Oh. Why, yes. Of course."
    f "I think...we were supposed to wrap our Secret Santa presents, Sensei..."
    s "You know, I’m getting really tired of everyone telling me how to live my life."
    s "If I want to put the minimal amount of effort into someone’s gift, I am free to do that."
    f "Okay, but...why are you making Touka hold it?"
    to "Because his entire purpose in life is to torment me, Futaba. It is exactly as I was telling you earlier."
    s "Is this just what you girls do? Talk down about me while I’m not around?"

    scene welcometoxmastwo23
    with dissolve

    to "Pardon me, Sensei, but I had mainly positive things to say about you! Which is quite surprising, may I add, since you seem to have labeled me as some sort of enemy!"
    s "I don’t think you’re an enemy. It’s just easy to take advantage of your kindness. "
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

label christmastwo8:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
scene christmasthrees22
    with dissolve

    sar "Ngh...mmf....mmm!"
    h "You’re a...fucking slut, Sara...offering to...let your best friend watch you get fucked..."
    h "You’re a fucking...filthy slut...you know that? Do you like being a little fuck toy?"
    sar "Haru...chan..."
    h "I bet you do, Sara...I bet you...fucking do..."
    h "Is that why you got all dressed up this morning? To make yourself prettier when...you know deep down...how fucking ugly you are?"
    s "Haruka, chill."

    scene christmasthrees23
    with dissolve

    sar "Harder! Fuck me...harder!"
    h "Why would I chill? She likes it."
    h "Can’t you feel it, Sensei? I bet she’s...tensing up...really hard right now...isn’t she?"
    sar "That’s...because I’m...gonna cum..."

    scene christmasthrees24
    with dissolve

    h "Of course you’re gonna cum, you little whore. Go ahead...do it..."
    h "Cum for Sensei...take that thick fucking cock and...cum all over him..."
    sar "AHH! AHHHHH! FUCK!"
    s "I-"
    sar "Don’t...talk! Just...fuck me! Fuck me harder! Don’t...hold back! I...deserve it!"
    h "That’s right...lean into it...give...Sensei all of...your desperate little pussy, Sara..."
    sar "It’s all yours...[saramaster]...I’m all yours..."

    scene christmasthrees25
    with dissolve

    sar "I’m...all yours!"
    h "Hah...oh god...oh fuck...now...I’m gonna cum too..."
    h "Ahh~ Yeah...fuck fuck fuck...holy...fuck..."
    sar "Ahh!!.....HAH!!!!!....AHHHHHH!!!!!"

    with sexfade
    with sexfade
    scene christmasthrees26
    with cumflash
    with hpunch

    sar "AAAAAAAAAAAAAAAAAHHHHHAHahAHHAHAAHHaaaaahhhaaa!!!!!!!"

    "I erupt at the same time Sara climaxes and...probably at the same time as Haruka?"
    "It’s hard to tell with the latter due to the earth shaking orgasm coming from the other party."
    "Sara’s lower body twitches as I empty myself out inside of her."

    scene christmasthrees27
    with dissolve

    "Once the initial excitement of the three-way mutual orgasm stops, though, Sara goes silent."
    "She’s done that in the past, but it’s normally just because the two of us went a little too hard."
    "And that...wasn’t the case today."
    "But, then again, Haruka also got caught up in the moment and said a lot of...hurtful things to her, so I’m assuming this could just be a result of that."
    "I know that’s just the sort of thing that Haruka is into when it comes to dirty talk, but I honestly have no idea how Sara responds to that- even after witnessing it."
    "And it’s not like I can just ask her for her thoughts on the matter since she’s..."
    "Crying?"

    s "..."
    h "Hah...hah...oh my god...oh my god...wow..."
    h "That was...one of the best I’ve ever had and...I did it all myself..."
    sar" Nnf...mm...mmn~"
    s "..."

    scene black
    with dissolve2

    "I slide myself out of Sara and, just like she wanted, the remnants of our actions begin to ooze out of her."
    "Neither her nor Haruka open their eyes for the next several minutes."
    "They don’t respond when spoken to either."
    "So..."
    "I guess the only thing left for me to do is leave the room?"
    "I still have to buy Miku a Christmas present for tonight after all and-"

    s "..."

    "Maybe {i}Miku{/i} would want to watch Makoto and me go at it sometime?"
    "That....sort of {i}gift{/i} worked really well on Haruka."

    s "..."

    "No."
    "I’ll just buy her a soccer ball or something."

    $ renpy.end_replay()
    $ haruka_lust += 1
    $ sara_lust += 3
    $ saralust20 = True
    stop music fadeout 5.0

    "{i}Sara’s lust has increased to [sara_lust]!{/i}"
    "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo7
...
```