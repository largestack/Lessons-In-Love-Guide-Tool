# Before the Sun Comes Up
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanespecial2&go=Go)


Part of event chain [Sayonara](./thirdreset3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: ayanespecial2
* Group: Ayane
* Triggered by label: thirdreset3

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label ayanespecial2:
    scene postrthree1
    with dissolve

    s "Huh?"
    m "…"
    s "Where did Ayane go?"
    m "..."
    m "If I had to take a guess-"
    m "I’d assume she was sent back to the beginning."

    scene postrthree2
    with dissolve

    s "The beginning of what?"
    m "Everything, obviously."
    m "That her mind was “factory restored” the same way it is every time you swap places with another “you.”"
    m "Then again, that’s just an assumption."
    m "I figure it’s equally probable that she’s just asleep in her dorm room right now- entirely unaware of everything that transpired tonight."
    s "And you’re just okay with that?"
    m "Of course."
    m "It’s part of the cycle."
    m "Even if I weren’t “okay with it,” there’s nothing I’d be able to do."
    m "Everyone stopped being real to me a long time ago."
    m "They’re more like puppets with...invisible hands or something inside of them now."
    m "I imagine it’s hard to understand given that you’ve only gone through this three times."
    s "Well...we need to go check on her then, right?"
    m "Is that what you want to do?"
    m "Or would you rather go home and collapse into bed?"
    s "You should be more worried about this."

    scene postrthree3
    with fade

    m "Perhaps I should."
    m "But have you begun to take into consideration exactly {i}why{/i} Ayane may have made it to the roof tonight?"

    if bonus == True:
        s "I was sort of hoping you would be able to tell me."
        m "It could be a number of things."
        m "But the reason that’s sticking out in my mind the most is so vile that I have an issue with even coming out and saying it."
        s "What does that-"
        m "It means that you’re disgusting."
        m "Do you understand?"
        s "That I’m disgusting?"
        m "Yes."
        s "Well...you certainly remind me enough."
        m "Good. "
        m "Can you maybe try to be {i}less{/i} disgusting in the future then?"
        m "Not only for your sake- but for my sake and the sake of everyone else unfortunate enough to become involved with you in any manner other than student and teacher."
        s "What happened to the Maya from like, an hour ago? The one who laid out a picnic for me?"
    else:
        s "..."
        m "..."
        s "Oh no. It was the hug."
        m "Can you maybe try to be {i}less{/i} disgusting in the future?"
        m "Not only for your sake- but for my sake and the sake of everyone else unfortunate enough to become involved with you in any manner other than student and teacher."
        s "What happened to the Maya from like, an hour ago? The one who laid out a picnic for me?"

    scene postrthree4
    with dissolve

    m "Gone with the reset, I suppose."
    m "Also, your blanket is gone."
    m "Sorry."
    s "…"
    m "…"
    m "Well, I guess we better head back to the dorm."
    m "It’s not like I really have anywhere else to go anyway."
    s "Maya, if Ayane really {i}is{/i} gone-"

    scene postrthree3
    with dissolve

    m "You and I will be the only ones to know."
    m "To everyone else, she’ll be exactly the same as she’s always been."
    m "And any memories that overlap in confusing ways will be rewritten or recontextualized in her mind to make perfect sense to everyone around her."
    m "Do you understand?"
    s "No."
    m "I didn’t think so."

    scene black
    with dissolve

    m "Now, come."
    m "If you’re so curious about her wellbeing, it’s probably best for you to find out firsthand exactly what’s happened."
    s "…"

    "The two of us leave the roof together."
    "As we move through the halls of the[school], I find an assortment of strange items dumped haphazardly onto the stairs and several halls barricaded with boxes."
    "When we make it outside, I notice that the weather has suddenly turned colder than it’s been in quite some time."
    "Maya tightens her scarf and sighs to herself."
    "I slide my hands into my pockets."
    "………"
    "……"
    "…"

    scene postrthree5
    with dissolve2
    play music "undersea.mp3"

    m "You can go on ahead."
    s "You’re not coming with me?"
    m "It’s nearly 3:00 AM. I won’t be as easily forgiven for waking anyone up as you will be."
    s "What are you going to do instead, then? Your room is right across the hall from Ayane's."
    m "It appears that we left in such a hurry that I may have forgotten several things in several places."
    m "If you’re still here by the time I return, which I truly hope you won’t be, I implore you to ignore my presence entirely and let me sleep."
    m "I am incredibly tired and depressingly frustrated."
    s "That sounds like more or less how you always are."
    m "It does, doesn’t it?"
    m "Anyway, goodbye."

    scene postrthree6
    with dissolve

    "Maya blows right by me as if we hadn’t just lost a close friend and restarted the world together."
    "I guess it’s possible that she’s just one of those people who internalizes her problems and-"

    s "…"

    "What am I doing?"
    "I need to go upstairs..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene postrthree7
    with dissolve

    "I make it to the room despite a pit in my stomach, which I imagine has already begun to sprout roots and transform into a tree, beckoning me to return home instead."
    "I stand there for what must be a total of five minutes, hoping to hear something- anything on the opposite end."
    "Of course, it’s the middle of the night right now. And even if Ayane were in there, I doubt she’d be conscious enough to make any noise."

    s "…"

    play sound "knock.mp3"

    "I knock on the door, hoping that if anyone {i}does{/i} wake up, it’s a resident of this dorm room."
    "I might be incredibly popular with all of the girls on this floor (Save Yumi), but even I can’t imagine having an easy time explaining to them exactly why I’m-"

    play sound "dooropen.mp3"
    scene postrthree8
    with dissolve

    sa "{i}Uaaaahhh~{/i}"

    scene postrthree9
    with dissolve

    sa "Sensei?..."
    sa "What are you...doing here?..."
    s "Hey, Sana. Sorry to wake you up."
    sa "It’s okay..."
    sa "Did you...need something?"
    s "Yes, actually."
    s "I was just wondering if Ayane was around."
    s "Do you think you could wake her up for me?"
    sa "Ayane?..."
    s "Yeah. I just wanted to make sure she’s okay."
    sa "Sensei..."

    play sound "static.mp3"
    scene postrthree10 with flash
    stop music
    stop sound

    sa "Who is Ayane?..."
    s "...What?"

    "It’s...not possible that she just...disappeared completely, is it?"
    "No."
    "No, that can’t be right."
    "Maya didn’t even factor that into any of the possibilities that-"

    ay "Sensei?..."
    ay "What are you doing over here this late?"

    play sound "static.mp3"
    scene postrthree11 with flash
    stop sound
    play music "lastdailysong.mp3"

    s "..."

    "If I believed in God, I’d thank him right now."

    s "What are {i}you{/i} doing here this late?"
    ay "I live here."
    s "Yes, but why are you walking around at 3:00 AM? Shouldn’t you be asleep?"

    scene postrthree12
    with dissolve

    ay "Sleep is for the weak!"
    ay "3:00 AM is the perfect time for a late night trip to the convenience store when you’re just too strong to sleep!"

    scene postrthree13
    with dissolve

    sa "Nguh..."
    ay "Sensei...you didn’t...wake up Sana just to check on me, did you?"
    s "The ideal scenario would have been you answering the door, but yes. It appears that I did wake up Sana to check on you."

    scene postrthree14
    with dissolve

    ay "And I’m guessing this is the first time you’ve ever seen her immediately after waking up in the middle of the night."
    s "Uhh, yes. That is not a thing I have really had the chance to do before."
    ay "Well...she can be a little...delusional when that happens."
    s "She didn’t even remember who you were."
    ay "If anything, I’m surprised she {i}did{/i} remember you."
    sa "Sleep...now..."

    scene postrthree15
    with dissolve

    ay "Yes, Sana. Sleep now."
    ay "Let’s get you inside..."

    scene black
    with dissolve2

    "Ayane gently guides Sana back into the bedroom, leaving her standing in the middle of the floor before sliding off her boots and her skirt."
    "I notice a small puddle beginning to form near the door as a result of residual snow meeting its demise at the hand of a heated room."
    "She returns to Sana and strokes her hair for a moment before leading her to the bed."

    if bonus == True:
        "If Sana wasn’t mostly unconscious at the moment, it would probably look as if the two of them were getting ready to do something interesting."
        "Something that, for some reason, isn’t having the same effect on me that a lesbian fantasy typically would."

    ay "Sensei, come sit with me for a little while."
    s "…"

    scene postrthree16
    with dissolve2

    "I take a seat beside Ayane and notice, even in this unlit room, two swollen, reddish circles surrounding her eyes. "
    "If I ask her now what caused them, she’ll deflect."
    "The same way she does every time I ask her anything."
    "Even when we were on the roof, when she was doing everything she could to pour a tiny bit of her heart out-"

    s "The roof..."
    ay "The roof?"
    ay "What roof?"
    s "Ayane, where were you tonight?"
    ay "What are you talking about? I was with you, remember?"
    ay "I was being weird and kept trying to talk about stuff that...didn’t really come out the way I wanted it to."
    s "And where was Sana? "
    ay "Wasn’t she just here?"
    s "No, she was at my house."

    scene postrthree17
    with dissolve

    ay "Sana was?"
    s "And Ami. And Molly. And Tsuneyo."
    s "There was a sleepover that you were supposed to come to, but you decided against it because you wanted to talk to me instead."
    ay "Why would I ever turn down a sleepover? I love sleepovers."
    ay "Couldn’t I have just talked to you-"

    scene postrthree18
    with dissolve

    ay "Actually...I probably couldn’t have talked to you at your house since there was all that stuff about Ami."
    ay "But...I don’t remember anything about a sleepover."
    ay "And I can’t really figure out why Sana would be here if there actually {i}was{/i} one."
    s "…"

    "So-"
    "It looks like Ayane hasn’t been completely “factory restored.”"
    "But...I’m not understanding why it’s suddenly as if the last day has just been entirely rewritten."
    "And it’s not like I can even ask Maya about it since she is mad at me for yet another reason beyond my comprehension."
    "But where do Ayane’s memories end?"
    "Why can she recollect her first trip to the roof, but not her second? And-"
    "Wait, didn’t she say “What roof?”"

    s "Ayane, where did we meet up tonight?"

    scene postrthree19
    with dissolve

    ay "Sensei...is everything okay? You’re acting really weird..."
    s "Just tell me where we met tonight."
    ay "We met at the same park we went to with Sana the other day."
    ay "And we talked about Ami and...and your memories and..."
    ay "Is this...another example of that?"
    ay "Are you...misremembering, maybe?"
    ay "I didn’t realize it was this bad..."

    "I’m not the one misremembering anything this time."
    "It’s you."
    "You’re the one who forgot."

    s "We met on the roof of the[school]."
    ay "I don’t even have a key to the roof of the[school]..."
    s "That’s-"

    "Wait..."
    "Yeah."
    "How did we meet there anyway?"

    s "This next part might make me sound a little crazy, but I need you to listen closely and answer as honestly as possible."
    ay "Sure...yeah. Anything for you."
    s "By any chance, do you remember {i}anything{/i} about going to the roof with Maya tonight? And...resetting the world and...anything like that?"

    scene postrthree20
    with dissolve

    ay "…"
    s "…"

    "We let the silence overtake us for a moment."
    "It’s hard to tell if Ayane is genuinely trying to remember or just...trying to figure out if I need immediate medical attention, but..."
    "Whatever the cause for the silence is-"
    "I hate it."

    ay "I don’t remember anything like that..."
    ay "All I remember is that I called you to meet up...and then we did...and then I went home."
    s "But..."
    s "But that doesn’t explain why you were walking around at 3:00 AM with dark, red circles around your eyes."
    s "And I don’t buy that whole “sleep is for the weak” thing. "
    s "What else happened?"

    scene postrthree21
    with dissolve

    ay "What else?..."
    ay "I guess it’s my turn to sound a little crazy then, huh?..."
    ay "The truth is...I tried to sleep, but..."
    ay "But I had this really weird dream."
    ay "A dream that I...can’t quite remember anymore."
    ay "And...when I woke up..."
    ay "I felt like I’d lost something."

    scene postrthree22
    with dissolve

    ay "Something really, really important to me and...and I couldn’t even put my finger on what it was."
    ay "Which made me kind of hate myself a little bit."
    ay "Like there was some really big thing that was just...stripped from my mind as if it never even existed..."
    ay "If it was so important, how come I forgot it so easily?"
    ay "None of it made sense..."
    ay "And...I didn’t want to call you about it since I already bothered you enough tonight..."
    ay "But...the fact that you’re back before the sun comes up kinda shows me that...maybe I didn’t bother you as much as I thought I did..."

    scene postrthree23
    with dissolve

    ay "Do you think this is what I was talking about when I told you I’d need a little more attention soon?"
    s "I have no idea."
    ay "Yeah...and it's kind of funny cause, like..."
    ay "Neither do I..."
    ay "I’m...really confused all of a sudden..."
    ay "My stomach kind of hurts a little too..."
    ay "Is this anxiety? Do I have anxiety now?"
    s "I highly doubt it. You probably just need to get some rest."
    ay "How am I supposed to rest when you came all the way here to see me, though? "
    ay "It wouldn’t be right for me to just kick you out when you're this worried."
    s "Ayane-"

    scene postrthree24
    with dissolve

    if bonus == True:
        ay "Do you wanna at least have sex first? "
    else:
        ay "Do you wanna at least hug first? "

    ay "I’d feel a little better about going to sleep if I gave you a little reminder to take with you when you go."
    s "Sana is literally asleep on your lap right now."

    if bonus == False:
        s "The hug would disturb her."

    ay "She won’t wake up. It’ll be fine."
    s "She woke up after one knock on the door. It won’t be fine."

    if bonus == True:
        s "Besides, I can’t touch you while you’re crying anyway. That’s one of the rules on my...incredibly short list of them."

    scene postrthree25
    with dissolve

    if bonus == True:
        ay "Okay, okay. We won’t have sex."
        ay "But I owe you at least one blowjob in the future as payment for coming to make sure I was okay tonight."
        ay "I still don’t really know what it is that made me cry like this, but I’m sure it’ll be okay soon enough."
    else:
        ay "Okay, okay. No hugs, then."

    ay "I probably just need some sleep like you said."
    s "Then...I guess I’ll go home, then."

    scene postrthree26
    with dissolve

    ay "Are you sure you don’t want to sleep here?"
    ay "My bed is huge. All three of us could fit if we snuggled a little bit."
    s "Maybe some other night. I’m kind of curious about whether anyone else from the apparent “made up slumber party” is still at my house or not."
    ay "Well, if they are, feel free to give me a call. I don’t wanna miss out on the fun even if it’s almost time for[school]."
    s "Oh, shit.[school]."
    s "I didn’t even realize it was Sunday."
    ay "On the bright side, I doubt you had any tests planned or anything like that."
    s "Jokes on you, Ayane. Tomorrow is the day I’m going to become a real teacher."
    s "Well, {i}today{/i} technically, I guess."
    ay "Whatever you decide to do, I'll support it."
    ay "I love you, Sensei. And thank you for coming to see me again tonight."
    ay "I feel a lot better now..."

    scene black
    with dissolve2

    "I leave shortly after that."
    "I don’t understand anything at all."
    "What happened this weekend?"
    "Why did Ayane show up to the roof? And why did she immediately forget it?"
    "This isn’t even resetting. "
    "It’s rewriting things that {i}did{/i} happen with things that didn’t."
    "If they even...did happen?"
    "I don’t know anymore."
    "Not that I ever did, but-"
    "…"
    "But at least I’m still here."
    "And I guess that’s really the most important thing of all right now."
    "…"
    "Huh."
    "I feel like I may have lost something too."

    $ renpy.end_replay()
    $ ayanespecial2 = True
    $ ayane_love += 5
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if ami_lust >= 15:
        $ totaldays += 1
        $ day -= 6
        if day == 1:
            hide sunday onlayer date
            show monday onlayer date
        jump amilust15
    else:
        $ amilust15skip = True
        jump advancetomon

label ayanelust20:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
ay "I told you! All I did was walk..."
    m "But why {i}here{/i}?"
    m "What led you to the roof of the[school] specifically?"
    ay "I..."

    scene picnicinspace25
    with dissolve

    ay "What..."
    ay "What was it again?"
    m "…"
    s "Maya, do you have any idea-"
    m "Yes."
    m "But we don’t have the time to talk about it now."

    scene picnicinspace26
    with dissolve

    ay "I’m so...confused..."
    ay "Why did I come here and..."
    ay "And where is everyone else?"
    m "You’ll see them again in no time at all."
    m "Just think of this all as one elaborate dream."
    m "And, if it ever happens again, we can talk about it a little more."
    ay "A...dream?..."
    s "Just do what Maya says and everything should turn out fine."
    m "Hopefully."
    s "Hopefully."

    scene picnicinspace27
    with dissolve

    ay "I’m really scared, Sensei..."
    s "Would coming a little closer help you feel better?"
    ay "Yeah, but...what about Maya?..."
    m "It’s extremely out of character for me to suggest something like this, but I think a group hug is in order."
    m "We’ll take a moment to catch our breath and then figure out how we’re going to handle this together..."

    scene black
    with dissolve2

    "So that’s what the gameplan is."
    "I can already tell that Maya is just going to go through with the reset once the three of us are in physical contact with one another."
    "I still don’t fully understand how this process works but, if the “proper method” includes a simple embrace, adding one more person to the mix wouldn’t do anything bad, would it?"
    "And...even if it does, there’s always the chance that none of us will ever find out about it."
    "Everything is going to be okay."
    "…"

    scene picnicinspace28
    with dissolve2

    m "Keep your eyes closed, Ayane."
    ay "Okay..."
    ay "I’m using Sensei’s shirt to dry my face, so I wouldn’t really be able to see anything anyway."

    "Ayane claws at my shirt and clips some of my skin in the process."
    "She’s trembling as if she were a dying animal on the side of the road, soaking wet after smacking off the windshield of a car and being tossed into a nearby rain-filled pothole."
    "And I’d like to say that Maya is the complete opposite-"
    "But the truth is that she’s trembling as well."
    "Less like roadkill and more like a very subtle earthquake, though."
    "Like there’s something happening beneath her that’s-"

    ay "Is..."
    ay "Is the ground...shaking right now?"
    m "It’s all in your head."
    m "Sensei, are your eyes closed as well?"
    s "…"
    m "…"

    scene picnicinspace29
    with dissolve

    s "Yeah."

    stop music
    play sound "static.mp3"
    scene 5 with flash
    scene 4 with flash
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene tree3 with flash
    scene happy9 with flash
    scene happy8 with flash
    scene happy7 with flash
    scene happy6 with flash
    scene happy5 with flash
    scene happy4 with flash
    scene happy3 with flash
    scene happy2 with flash
    scene happy1 with flash
    scene picnicinspace30 with flash
    stop sound
    $ renpy.pause(5, hard=True)

    $ renpy.end_replay()
    $ thirdreset3 = True

    jump ayanespecial2
...
```