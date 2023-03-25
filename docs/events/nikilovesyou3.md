# How To Make Love Stay (Niki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The End of the Tour](./nikilovesyou2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Niki: What it Takes to Move Forward](./nikilovesyou1.md)
* [Otoha: King Midas](./otohaspecial15p1.md)

## Event properties

* Id: nikilovesyou3
* Group: Niki
* Triggered by label: nikilovesyou2
* Chain sources: nikilovesyou2
* Chain sources path: nikilovesyou2

## Official wiki page

[How To Make Love Stay](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikilovesyou3&go=Go) for more details.

## Event code

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikilovesyou3:
    if _in_replay:
        play music "glasswalker.mp3"

    scene nikilovesyou1
    with dissolve2

    ni "I’m going to make tea. Do you want any?"
    s "I’m fine."
    ni "Are you sure? Is there anything {i}else{/i} you want? Water? Something a little harder to take the edge off?"
    s "I’m okay. Thank you."
    ni "Okay. I’ll be right back, but make yourself at home. Should be easy since you {i}did{/i} basically live here when we were kids."
    s "Okay..."
    s "Thanks."

    scene nikilovesyou2
    with dissolve
    play sound "dooropen.mp3"

    "After leaving the place where everything went dark, we return to Niki’s childhood home."
    "She collected a key from under the welcome mat to use on the door and said her parents don’t mind if she still crashes here from time to time."
    "They kept her room the same- and while I can’t currently remember its layout from any legitimate memories, I remember bits from when it was forced into my head a little over a year ago."
    "This is where she must have written me those letters — the prison I locked her in when I left her behind."
    "I can only imagine how many tears have been shed on the very bed I’m sitting on — how many times I’ve been cursed and ridiculed without so much as sparing a thought over her."
    "Akira."
    "The name rings out in the back of my head."
    "Who {i}knows{/i} that name?"
    "Ami surely does, yet she’s never said it to me."
    "I’m sure Maya knows too...maybe even Ayane."
    "Have they been saying it all along? Have I been blocking it out?"
    "It’s one word- it shouldn’t make me feel this different."
    "But I don’t deserve a name. I feel {i}real{/i} now. I’m suddenly a person instead of just a title, and...I shouldn’t be gifted something so valuable when everything else is already wrapped around my fingers."
    "The weight of five forbidden letters presses down on my neck and there is nothing I can do but hang my head in response."
    "Something plays on the television, but I can’t focus enough to see what."
    "All I can think is of what will happen next."
    "There is only one way I have ever known comfort — and I am here alone with a girl who wants nothing more than to comfort me."
    "But is {i}this{/i} the way it’s meant to be?"
    "Is {i}this{/i} what she envisioned under luxury blankets in fancy hotels, whispering my name into the dark corner of a room while doing to herself what I was not present to do?"
    "I have never whispered her name."
    "I have never whispered anyone’s."

    play sound "static.mp3"
    scene nikilovesyou3
    with flash
    stop sound

    se "That’s not true. You used to whisper {i}my{/i} name all the time. Just because I {i}made{/i} you doesn’t mean it doesn’t count."

    "I’m seeing things."
    "Things I am not meant to see."
    "This isn’t how it’s meant to be."

    se "I wonder what would happen if you reached out and touched me right now?"
    se "Do you think I’d feel it?...Do you think {i}you’d{/i} feel it?"
    se "You still {i}can{/i} feel, right? You don’t miss me so much that you’re {i}physically{/i} numb now too, I hope."

    "Can you see her too?"
    "Are you even there at all?"

    se "You can’t ignore me forever, Akira."
    se "The harder you try to forget me, the more I’ll want to show up."
    s "..."
    se "Akiraaaa~"
    s "..."
    se "Aki-kun~"
    se "Doff thy name! And for that name which is no part of thee, take all myself."
    se "O nature, what hadst thou to do in hell, when thou didst bower the spirit of a fiend in moral paradise of such sweet flesh?"
    s "You’re mixing monologues..."

    scene nikilovesyou4
    with dissolve

    se "Ah! He speaks!"
    se "Quick, tell me you love me before you fuck your ex-girlfriend. It should be easy. You’ve done it plenty of times before."
    s "..."
    se "Ugh. You’re such a Montague sometimes."

    play sound "static.mp3"
    scene black
    with flash
    stop sound
    play sound "dooropen.mp3"

    ni "Hey, back. Sorry. Slide over a bit."
    s "Yeah...sure."

    play sound "static.mp3"
    scene nikilovesyou5
    with flash
    stop sound

    ni "You sure you don’t want anything? You’re probably dehydrated after walking around all day."
    s "I’ll be fine. But thanks."

    scene nikilovesyou6
    with dissolve

    ni "Okay...You know where the kitchen is if you wind up changing your mind."
    s "..."
    ni "What are you watching? Who’s the girl with the pink hair? And what’s that weird grey stuff they’re eating?"
    s "I don’t know. I haven’t been paying much attention."

    scene nikilovesyou7
    with dissolve

    ni "Do you want to take a nap? I can leave you alone if you want. My parents won’t mind if you stay the night. We’re well past the age where it would be weird."
    ni "And Noriko doesn’t come by much anymore, so you wouldn’t have to worry about her finding you here and getting the wrong idea or something."
    s "{i}Would{/i} it be the wrong idea?"

    scene nikilovesyou8
    with dissolve

    ni "You tell me. You were nearly catatonic on the way over. I’m in big-sister mode right now because I figured I should be gentle, but I can swap back to ex or childhood friend if you like."
    s "Just be yourself. There doesn’t need to be a “mode.”"

    scene nikilovesyou9
    with dissolve

    ni "Uh...maybe “mode” was the wrong way of putting it? It’s not an act or anything. All of those “modes” are real parts of who I am. I just didn’t want to overstimulate you or...something."
    s "..."
    ni "Maybe I should have just made you tea after all?"
    s "I really don’t deserve you, Niki...You’re better than this. You know you are."

    scene nikilovesyou10
    with dissolve

    ni "Better than what? Being there for someone who needs me? Someone I’ve made it {i}pretty{/i} apparent I’d do anything for today?"
    ni "I’m not {i}above{/i} you just because I unlocked compassion in my skill tree and you skipped over that in favor of...penis size or something."
    s "Worthy investment. Compassion gets you nowhere."
    ni "It got you into my room."
    s "It’s equally plausible penis size got me into this room."

    scene nikilovesyou11
    with dissolve

    ni "Pfft...Are you feeling a little better now? Your less miserable side is starting to show."
    s "My head hurts. My legs hurt. I’m exhausted. I’m congested. But on the bright side, I can formulate thoughts again. And that’s a good sign, I guess."

    scene nikilovesyou12
    with dissolve

    ni "You’ve gotta start somewhere."
    ni "Just please forgive me if I start crying once you’re a little more stable. I was holding myself together for your sake and that dam is bound to burst sooner or later."
    s "Please don’t cry for me, Niki. It’s not worth it."
    ni "You know that dude Noah who built the ark to put all those animals on? Pretty sure he did that sometime around when you ran out on me when he caught wind of how much I’d been crying."
    s "Niki-"
    ni "The polar ice caps aren’t actually melting. Sea levels rose because you broke my heart. Global warming really is one big conspiracy."

    scene nikilovesyou13
    with dissolve

    s "I’m really not in the mood to laugh right now."
    ni "Are you ever?"
    s "No. But now I’m really not in the mood."
    ni "Oooh, are you gonna do something about it?"
    s "Not if you’re still in big-sister mode. That would be immoral."
    ni "I’ve moved back into best friend mode over the last several sentences. The transition to ex is still pending."
    ni "Idol-Niki’s not off limits either if that sort of thing will cheer you up."

    scene nikilovesyou14
    with dissolve

    s "I think where you are now is good. Especially since I’m not really sure how I’d even fare around idol-Niki."

    scene nikilovesyou15
    with dissolve

    ni "Ohoho? Not afraid I’d steal your heart with my captivating style and mature brand of wholesome cuteness?"
    s "Oh, okay. That’s not nearly as tempting as I thought it would be."

    scene nikilovesyou16
    with dissolve

    ni "I’m sure you’d think otherwise if I didn’t look like a zombie right now. I doubt even half of that Facebook group would think I’m cute in this condition."
    s "I think you’re plenty cute. I just like your actual personality more."

    scene nikilovesyou17
    with dissolve

    ni "Holy crap. That was like, totally adorable. You’re not allowed to say nice things like that to me. It’s weird."
    s "If I’m not allowed to be nice to you and and I’m not allowed to be mean to you either, what do want me to be?"

    scene nikilovesyou18
    with dissolve

    ni "Happy."
    s "I can’t be happy {i}to{/i} you. That didn’t make sense in context."
    ni "I don’t give a fuck if it makes sense or not. You can say whatever you want to me and I’ll probably give you shit for it because I’m just so {i}used{/i} to giving you shit at this point."
    ni "But the truth is, as long as you don’t feel like the world is caving in around you, I’ll be fully content and fully willing to overlook {i}any{/i} corny compliment you toss at me."
    s "Why are you touching my face?"
    ni "Because it’s a good face and I {i}like{/i} it."
    s "Like it in a less-touchy way or something is going to wind up happening that you’ll regret in the morning."

    scene nikilovesyou19
    with dissolve

    ni "What’s that? You want me to touch you more? I mean...I {i}guess{/i} if you insist."
    s "Niki..."
    ni "We can do it if you want."

    scene nikilovesyou20
    with dissolve

    s "What?..."
    ni "...?"
    s "Do what?"
    ni "Sex."
    ni "Is that not what you were talking about when you said “Something I’ll regret in the morning?”"
    s "It was, but...I kind of figured you wanted the first time to be special since the only times you’ve ever mentioned it being a possibility were...Christmas-related."
    ni "Was today not special to you?"

    scene nikilovesyou21
    with dissolve

    s "It was miserable..."
    s "I felt things I haven’t felt in years and still haven’t really processed them."
    s "We’re both upset and both exhausted...and, with all due respect, you look like you need about a week's worth of sleep in order for your eyes to go back to normal."
    ni "I didn’t ask if today was {i}fun.{/i} I asked if it was {i}special.{/i}"

    scene nikilovesyou22
    with dissolve

    ni "We went on a mini-tour of our entire history together that ended with you confronting something you’ve been avoiding for almost a decade."
    ni "We sat on a hill with a nice view and talked about the past and the future...visited the spot where we built our secret base...and the tree we carved our names in."
    ni "And now we’re back in the room where we shared our first kiss."
    ni "Sure, we might look a little worse for wear...and we might be tired and sweaty from walking all day...and you might not even be able to get it up in your current mental state."
    ni "But, Akira..."
    ni "I don’t think I’ve ever wanted you more than I want you right now."
    s "..."
    ni "How about you?"
    ni "Do you want me too?"
    s "..."
    ni "..."
    s "Will you really never leave me?"

    scene nikilovesyou23
    with dissolve

    ni "I don’t think I’d be able to if I tried."
    s "You’ll stay by my side even when you find out all the awful things I’ve done?"
    ni "You’d have to get rid of me by force. I’d never leave on my own."
    s "I don’t believe you..."
    ni "What can I do to prove it?"
    s "..."
    ni "Akira..."
    ni "What can I do to prove it?"

    scene black
    with dissolve2

    s "Give me all of you."

    "........."
    "......"
    "..."

    scene nikilovesyou24
    with dissolve2

    s "Are you sure that’s how you want to do this?..."
    ni "Oh, please. As if you’re in the state to take things into your own hands."
    ni "Let me do all the work. It’ll be your reward for doing such a good job today."
    s "All I did was follow you around..."
    ni "That’s right...but you never tried to leave."
    ni "You confronted the past head-on. And as your childhood friend, I’m very proud of you..."
    ni "As your ex-girlfriend, I’m very proud of you..."
    ni "And no matter what I become next, I’ll {i}still{/i} be proud of you."
    ni "Now, sit still and let me lose my virginity before I die of old age."

    scene nikilovesyou25
    with dissolve2

    "After a moment of lying there with my cock pressed up against her waist, Niki reaches down and begins to stroke me."
    "Getting hard wasn’t an issue...I knew it wasn’t going to {i}be{/i} an issue the moment she unlocked the door."
    "But I didn’t know if it would come to this."
    "Or perhaps it would be better to say I didn’t {i}want{/i} it to come to this."
    "A girl like her, who’s done so much just to prop me up throughout the years, should not settle for me at my worst when she deserves me at my best."
    "But here I lie as she, once again, goes out of her way to do something that will make {i}me{/i} feel better — utterly unwilling to accept the fact that it’s something she wants as well."
    "This room is held together by a lifetime's worth of memories and all I can do in this moment is try and force a few away so we fall through a hole in the floor before we climb too far up."
    "She kicks down the ladder."
    "She shows me how weak I am."

    ni "Jesus fucking Christ, what the Hell have I gotten myself into this time?"
    ni "You really did dump all of your stats into this thing, didn’t you?"
    s "Compassion is for suckers..."
    ni "Are you ready?"
    s "I think the real question is if {i}you’re{/i} ready."
    ni "Yeah...but I’m gonna move a little slow at first. Just until I get used to it."
    s "Good luck. It’s going to hurt."

    scene nikilovesyou26
    with dissolve

    ni "No it’s not."
    ni "I’ve waited for this moment for {i}far{/i} too long for it to hurt."

    scene nikilovesyou27
    with dissolve

    ni "Ngh?!"
    ni "Hah!...Okay...no...it hurts...you were right..."
    s "Just move slow like you said...you’ll get used to it..."
    ni "Hngh!...Mhm...I can do this...this...this is nothing..."

    "Niki lowers herself onto my shaft and I’m immediately enveloped by a remarkable warmth."
    "There’s a slight resistance that disappears almost immediately as she fills herself with me in one motion."
    "Her hips do not rock and her body does not bounce — but she uses her legs to lift herself very gently up before gliding very gently back down."
    "An inch or two at a time. That seems to be all she’s focusing on for the time being. But I have no complaints about that as just being inside of her is enough to drive a man insane."
    "The tips of her fingers refuse to part ways with my cock as she uses them to steer me deeper into her, all while letting out staggered yelps of lustful anguish."

    ni "Akira...why...ngh...do you have to be so big?...You’re making this...really hard for me..."
    s "On the bright side...you feel amazing..."

    scene nikilovesyou28
    with dissolve

    ni "Yeah?...I do?..."
    ni "It’s not too...cramped in there?...Cause I’m feeling...um...pretty {i}full...{/i}"
    ni "I don’t know if I can take the whole thing just yet..."
    s "It’s just right...don’t worry..."
    ni "Okay...I’ll take your word for it..."
    ni "I’m gonna try...and move a little faster now...okay?"
    s "Do whatever you want...you’re in control..."
    ni "I’m in control..."

    scene nikilovesyou29
    with dissolve

    ni "I’m in control...I’m in control..."

    scene nikilovesyou30
    with dissolve2

    ni "Hah! Oh...mmf! That’s deep. {i}Fuck,{/i} that’s deep."
    ni "Oooh wow. Fingering does not prepare you for this."
    s "Just relax..."
    ni "Shut up. I’m the one who should be saying that to you. I told you I would handle it, so...hah...let me...fucking handle it."

    "She’s rocking now, but I’m unsure if it’s because she’s starting to get used to this or she’s just too stubborn to continue taking things at her own pace."
    "Either way, the feeling of her body weight pressing down on me as she rhythmically pulls my cock back and forth is one of the most thrilling sensations I’ve ever felt."
    "Her hands press down on my chest as she uses them to keep herself balanced, diverting every bit of energy and willpower to slowly riding me."
    "I can feel myself throbbing inside of her, and I think she can feel it as well as she begins to press harder in response."
    "Her breaths grow louder and her legs begin to shake, so I rest my hands on them to keep her steady."

    scene nikilovesyou31
    with dissolve

    ni "Hah...hah...does...it still feel good?..."
    s "Even better than it did before..."
    ni "Really?...You’re not just saying that?..."
    s "Really...the way you’re rocking your hips is...surprisingly intense..."

    scene nikilovesyou32
    with dissolve

    ni "Hah...yeah?...You mean...like this?..."
    ni "The key is...keeping up a steady rhythm...I’m a dancer, so...it comes easy..."
    ni "It also...hngh...helps...distract me from...the pain..."
    s "Look at you, talking like you’re already an expert..."
    ni "Akira......Akira.......Akira~"
    ni "I’m so happy...this is...{i}so{/i} long overdue..."
    s "Starting to enjoy yourself a little?"
    ni "Hah...heheh...maybe a {i}little...{/i}but I’m more turned on by the idea than...ngh...how it actually feels..."

    scene nikilovesyou33
    with dissolve

    s "Then maybe try...getting more into the {i}idea?...{/i}"
    ni "Hah...ngh...and...how can I do that?..."
    s "Looks like you’re still wearing...some extra clothing..."
    ni "If you want to see my tits just ask. You don’t need to manipulate me into it."
    s "Then...shirt, please..."

    scene nikilovesyou34
    with dissolve

    ni "Hah...hah...your wish...is my command..."
    ni "Mmf...mngh...heheh...you know...I think that actually worked...I do feel...a little hotter all of a sudden..."

    "As Niki lifts her shirt and exposes herself, she begins to ramp up her movement and is now full-on riding me the way she was {i}meant{/i} to be."
    "I don’t know if it can be entirely attributed to her dancing skills and sense of rhythm, but the way she rocks her body makes her look like an experienced porn star rather than a girl in the throes of her first time."
    "That, combined with the smug grin creeping across her face and the light bouncing of her breasts as her nipples harden creates an extremely lewd image that I’m more than privileged to see."

    ni "Hah...hah...is it me or...did you just get harder?..."
    s "I definitely got harder...I think you have a knack for this..."

    scene nikilovesyou35
    with dissolve

    ni "Ngh...mmf...you’re not so bad yourself..."
    ni "I’m surprised you let me handle this and haven’t tried pushing me down yet. I thought you’d hate being the submissive type."
    s "I’m enjoying myself a little too much right now to be worried about something like that..."
    ni "Hah......ahh......I’m glad....you deserve it....after today...."
    ni "Now please...enjoy yourself even more as...your childhood friend...squeezes your big cock dry..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nikilovesyou36
    with dissolve2

    ni "Hah! Ngah!....Ahh! Akira...Akira!"

    "We’ve been having sex for around forty-five minutes now."
    "I’ve somehow miraculously abstained from finishing so far but there is no conceivable way I will be able to last much longer."
    "The bright side is that Niki seems to be enjoying herself now — and it’s not just because of the “idea” anymore."

    ni "Ooooh {i}God{/i} I love your dick...I love your dick so much...oh {i}fuck,{/i} Akira...it feels so fucking good inside me..."
    s "Niki...I can’t take much more..."

    scene nikilovesyou37
    with dissolve

    ni "Ahhh...really?...But I’m finally having fun..."
    ni "You can’t hold out for just a {i}little{/i} while longer?..."
    s "Uhhhhh..."

    scene nikilovesyou38
    with dissolve

    ni "Mnf...it’s fine...you can cum..."
    s "Inside?"
    ni "I’m...hah...surprised you even asked...how...hah...considerate of you..."
    s "Inside it is..."
    ni "Go ahead...I wouldn’t...have it any other way..."

    "Instead of increasing her pace or the force with which she slams her waist downward, Niki elects to keep up the same exact pattern and motion she’s had going for ten minutes now."
    "But this is no time to be applauding her stamina and endurance-"
    "It is a time to cement her as one more cornerstone in this waste of a life that I’ve been living."
    "It’s something I should have done when we were younger."
    "But I was far too weak and far too confused back then."
    "I’m not saying I don’t still have those traits now."
    "But it wasn’t until today that I realized just how much I need her."

    stop music fadeout 15.0

    ni "Akira..."
    ni "{size=+10}{i}Akira...{/i}{/size}"
    ni "{size=+20}{b}Akira!!!{/b]{/size}"

    "She gave me a name."

    with sexfade
    with sexfade
    scene nikilovesyou39 with cumflash
    with hpunch

    ni "AAAAAAAHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    scene black
    with dissolve2

    "I spend the night in her bed."
    "I fall asleep in her arms."
    "We make love again in the morning."

    $ renpy.end_replay()
    $ nikilovesyou3 = True
    $ niki_love += 10

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "{i}Who is it you truly belong with?{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    scene street_day
    with dissolve2
    jump satmorningmenu
...
```

## Code that triggers this event

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
scene memorylane17 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane21 with flash
    scene memorylane22 with flash
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane21 with flash
    scene memorylane22 with flash
    scene memorylane23 with flash
    stop sound
    $ renpy.pause(5, hard=True)

    s "This..."
    s "This is where it happened..."
    ni "That’s right."
    ni "This is where your world was ripped away from you."

    play sound "static.mp3"
    scene imissyoumore with flash
    scene everythingg with flash
    scene memorylane24 with flash
    stop sound

    ni "You can’t only open yourself up to the good memories, you have to let the bad ones in too."
    ni "You’ll never move on if you just keep ignoring the things that make you hurt. You have to {i}work{/i} if you ever want to get better. Only then will you be able to look back on the past without breaking into a million pieces."
    ni "But I promise you, and I mean this with {i}all{/i} of my heart, I will be there {i}every...single...step{/i} of the way."
    ni "You’re not alone..."
    s "..."
    ni "{i}Look at me.{/i}"

    scene memorylane25
    with dissolve2

    ni "{i}You’re not alone.{/i}"
    ni "{i}Okay?{/i}"
    ni "No matter how horrible you become...or how much work it takes to get you through a single day without feeling sorry for yourself..."
    ni "I will be here. I’ve {i}always{/i} been here. "
    ni "You’re my best friend in the whole entire world...and I am so...{i}so{/i} sorry you had to go through what you did..."
    ni "But..."
    ni "I don’t want to watch you suffer anymore..."
    ni "I want my friend back..."
    s "..."
    ni "Will you please stop running? Both literally {i}and{/i} figuratively?"
    s "..."
    ni "Please?..."
    s "You really won’t leave?"
    ni "Of course not. Never."
    s "No matter what I become?"

    scene memorylane26
    with dissolve

    ni "No matter what you become."
    s "Why?..."
    ni "Because I’m a fucking idiot."
    ni "But I’m {i}your{/i} fucking idiot. And you’re my big, melancholic doofus. "
    ni "So let’s go be stupid together...far away from the places that make us hurt."
    ni "Let’s go somewhere quiet...and comfortable..."
    s "..."
    ni "{i}Let’s go home, Akira...{/i}"

    scene black
    with dissolve2

    "Akira..."
    "That’s...my name."
    "My name is Akira."
    "..."
    "I’m a good boy."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ nikilovesyou2 = True

    jump nikilovesyou3
...
```