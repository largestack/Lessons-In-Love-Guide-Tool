# A Thousand Years (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Mother's Milk](./mothersmilk.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Niki: What it Takes to Move Forward](./nikilovesyou1.md)

## Event properties

* Id: slumberreset5
* Group: Main
* Triggered by label: gscompletehooray
* Chain sources: mothersmilk
* Chain sources path: mothersmilk->mothersmilk->gstriviaround2

## Official wiki page

[A Thousand Years](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=slumberreset5&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label slumberreset5:
    scene youcanif
    play sound "mudwater.mp3"
    $ renpy.pause(16, hard=True)
    scene black
    $ renpy.pause(4, hard=True)
    play sound "static.mp3"
    scene ohnoyoureawakeagain1 with flash
    stop sound

    s "AAAAAAAHH! "
    s "HAH...HHHHAH........AH..."
    s "Hh......h..........h.........h......"

    scene ohnoyoureawakeagain2 with dissolve2

    s "Hah...hah....."
    s "..."
    s "..........."

    scene ohnoyoureawakeagain3
    with dissolve2

    s "Ngh..."
    s "Hah..."

    scene black
    with dissolve4

    "........."
    "......"
    "..."

    scene ohnoyoureawakeagain4
    with dissolve4
    play music "backwardsdancing.mp3"

    s "..."

    "The plan was a failure."
    "Not only was I alone when I opened my eyes, but I wasn’t even in the place they likely closed in."
    "As such, I’m here again."
    "It was easy this time."
    "I understood everything that was happening the whole way here."
    "And I understand everything now that I’ve arrived."
    "The world is going to end."
    "But I am going to be okay."
    "Because there are still things that I have to do."
    "And there is still something out there that wants to keep me alive."
    "I understand that now."
    "God is real."
    "He’s just abandoned us."

    play sound "static.mp3"
    scene ohnoyoureawakeagain5 with flash
    stop sound

    ay "Oh my {b}God...{/b}"
    ay "Sensei..."
    ay "Sensei!"
    m "..."
    s "Who’s ready for a field trip back to roughly two months into the school year?"

    play sound "static.mp3"
    scene ohnoyoureawakeagain6 with flash
    stop sound

    ay "Do you have any idea how long you’ve been gone?! I was worried sick!"
    ay "I thought I’d never see you again! Where were you? Where did you go?! Why did you leave?!"
    m "Was she like this when you couldn’t find {i}me{/i} as well?"
    s "Not even close."
    m "So it’s just you she’ll break down for. Got it."

    scene ohnoyoureawakeagain7
    with dissolve

    ay "How are you so calm?! You’ve been like this the whole time! I don’t get it! You love him too, don’t you?! Why aren’t you showing it?!"
    m "I’m calm because I’ve been through this more times than you could even imagine. One week is nothing."
    s "A week? You two have been here for an entire week?"

    scene ohnoyoureawakeagain8
    with dissolve

    m "Yes. And kudos to Ayane for not breaking down until the fourth day. She was actually rather stable and mostly bearable beforehand."
    s "I’m sorry to hear that. I obviously didn’t mean to keep you waiting that long."
    m "Just be happy the world hasn’t reset without you. Apart from that, I have some good news and bad news."
    m "The bad news is, unfortunately, it appears that both of our new companions have been left behind. Of course, that can not be said {i}definitively{/i} given what happened last time, but still."
    m "It’s probably safe to assume they won’t be joining us. "
    m "The {i}good{/i} news is that we did manage to learn that it {i}is{/i} possible for others to learn of the loops without any immediately negative consequences."
    m "We still don’t know just what prerequisites are required to {i}get{/i} the others to a point like that, but we know now that it is possible. Progress has been made and a celebration is in order."
    m "Or...will {i}be{/i} in order. I didn’t exactly pack a picnic this time and, even if I had, I’m sure none of the food would still be very edible."
    ay "It’s really you...right? You’re not some memory-wiped replacement of Sensei that Maya conjured up to get me to stop crying?"

    scene ohnoyoureawakeagain9
    with dissolve

    m "Just who exactly do you think I am? "
    ay "Someone who has {i}not{/i} made the last week very easy for me, that’s for sure."
    m "Get a grip. If you really are going to become a regular member of our rooftop get-togethers, you’re going to have to get accustomed to...prolonged leaves of apocalyptic absence from time to time."
    m "Of course, there’s no guarantee you’ll still be here once the world resets anyway, but I digress."
    s "Still holding onto your pregnancy theory even though Ayane made it here again despite an entire cycle of abstinence?"

    scene ohnoyoureawakeagain10
    with dissolve

    m "It’s not as if I surveyed you the entire time. You very well could have gone behind my back and created a secret child. I know exactly how insatiable the two of you are."
    m "But assuming I {i}do{/i} believe you, I’ll be holding onto my theory until the sun comes back up."

    scene ohnoyoureawakeagain11
    with dissolve

    m "Which could very well be any minute now that Sensei is-"
    ay "..."
    m "What? Why are you looking at me like that?"
    ay "You need to learn to be more sensitive with other people’s feelings."
    m "If I haven’t learned that trait by now, it’s probably safe to assume I’m either never going to, or...have just neglected to really {i}hone{/i} it."
    ay "I...am going to have...{i}so{/i} much sex next cycle. Just to spite you."
    s "I can’t help but be a little offended by that. I don’t think I’ve ever been used for revenge sex before."

    scene ohnoyoureawakeagain12
    with dissolve

    ay "Sensei...I’m so glad you’re back. This was somehow even worse than the first time I couldn’t find you — and that’s in no small part to understanding just what’s at stake now."
    ay "Next time the world is about to end, instead of a slumber party, I’m just going to tie myself to you. That way, you won’t be {i}able{/i} to get away and I won’t lose my very last bit of sanity."
    m "Can you tell her to stop rambling on about the {i}next{/i} cycle when we still don’t technically know if-"
    s "Knock it off, Maya. There’s no harm in letting her be a little hopeful. "

    scene ohnoyoureawakeagain13
    with dissolve

    s "If she’s going to have to get accustomed to “prolonged leaves of apocalyptic absence,” you’re going to have to get used to being wrong sometimes."
    s "You don’t know everything anymore. You’re in the same exact boat as us. So stop trying to sound all knowledgeable and just figure shit out along the way like a real human."
    m "Wow. "
    m "We almost kiss {i}one{/i} time and now you think it’s okay to talk to me like I am inferior to you. Real nice."
    s "What part of the “same boat” do you not get? You’re not {i}inferior.{/i} You’re on the same level as us."
    m "I don’t think you understand how boats work. Boats have captains...crewmen...other...boat-people. They’re not all on the same level just because they’re on a single seafaring vessel."
    s "Well, everyone on {i}this{/i} boat is on the same level. End of discussion."
    ay "I have a boat. I just can’t really get to it anymore on account of the wall."
    s "I said “end of discussion.” That means you too, Ayane."

    scene ohnoyoureawakeagain14
    with dissolve

    ay "Got it. "
    ay "I like the side of you that puts Maya in her place. Any time {i}I{/i} try to do that, she just makes me feel really bad about myself."
    m "I have not been {i}put in place.{/i} I just see no point in continuing to argue about a topic as stupid as boats when the world is about to end."
    s "It’s really weird that we’ve gotten to a point where sentences like that aren’t all that strange."

    scene ohnoyoureawakeagain15
    with dissolve

    m "Yeah..."
    m "It really is."
    ay "Aww...damn it."
    ay "How am I supposed to stay mad at you when you look like that? "
    ay "This calls for a group hug! We can celebrate with that instead of a picnic."

    scene ohnoyoureawakeagain16
    with dissolve

    m "Oh? Are you already forgetting that something like that is exactly how we get {i}out{/i} of this mess?"
    ay "Of course not. It just feels a little less formal if we’re doing it because we love one another and not because God likes watching people hug or something."
    m "I couldn’t have said it better myself."
    ay "You definitely could have. That wasn’t my greatest line."
    m "You said it, not me."

    scene ohnoyoureawakeagain17
    with fade

    ay "Alright! Bring it in, everybody! Time for another field trip through time!"
    m "Wait, before we go back...there’s something I want to say."
    ay "Is it that you actually love me and that you’re only mean all the time because you’re putting on a brave face?"
    m "No. It’s that if I {i}am{/i} right and not having a child inside of you while doing this wipes your slate clean of all these memories, you are going to owe me dinner."
    ay "How will I even know that if I don’t have any memories of this?"
    m "I’ll figure that out later."
    s "Can I say something as well?"
    m "No."
    ay "Go ahead, Sensei. I’ll listen to you. "
    s "I’m glad it’s you two I get to do this with."
    s "Anyone else would just feel...wrong."
    m "Probably because it would {i}be{/i} wrong."
    ay "Me next! Me next! "
    ay "When the world resets..."
    ay "And we {i}all{/i} make it back..."
    ay "I don’t care {i}where{/i} we end up..."
    ay "But wherever it {i}is...{/i}"
    ay "Know that I am going to tackle Sensei and proceed to make passionate love to him regardless of whether or not Maya is there."
    ay "Kay. Done. Send us home, Maya."
    m "After that? I’m not sure if I want-"

    stop music
    play sound "static.mp3"
    scene ayhh1
    with flash
    scene ayhh2
    with flash
    scene ayhh3
    with flash
    scene ayhh4
    with flash
    scene ayhh5
    with flash
    scene ayhh6
    with flash
    scene ayhh7
    with flash
    scene ayhh8
    with flash
    scene ayhh9
    with flash
    scene ayhh10
    with flash
    scene ayhh11
    with flash
    scene ayhh12
    with flash
    scene ayhh13
    with flash
    scene ayhh14
    with flash
    scene ayhh15
    with flash
    scene ayhh16
    with flash
    scene ohnoyoureawakeagain18 with flash
    stop sound

    s "..."
    ay "..."
    m "..."

    scene ohnoyoureawakeagain19
    with dissolve
    play music "daybreak.mp3"

    ay "..."
    m "..."
    m "I’m assuming you...still have all of your memories?"
    ay "Mhm."
    m "I see."
    ay "..."
    m "..."
    ay "Maya?"
    m "Yes?"
    ay "You might want to look away."
    m "..."
    ay "..."

    scene ohnoyoureawakeagain20
    with dissolve

    m "Wait, you were actually serious?!"
    ay "Excuse me...teacher? I have a problem I need some {i}help{/i} with."
    s "Uhh..."
    m "Hold on...you realize we’re still at school, right? Someone could come up here any-"
    ay "Don’t care. Infinite world. Modifiable memory. Ayane do sex now."
    s "Maybe...it would be best if we waited until-"

    scene sky
    with dissolve

    ay "Amamiya hidden technique — glomp of the midnight sun!"
    s "Please don’t-"

    play sound "tackle.mp3"
    with hpunch

    m "Ayane, what the fuck?!"

    scene ohnoyoureawakeagain21
    with dissolve

    m "What do you think you’re doing?!"
    ay "Something I should have done a {i}long{/i} time ago."
    ay "Like, literally. I stopped having sex for an entire school year for no reason. I must now make up for lost time."
    m "How insatiable are you?! Couldn’t you have at least waited until I was gone?!"

    "Ayane climbs on top of me and I am suddenly in a rather...uhh...well, you can see what type of situation it is."

    ay "Did you miss me? Because {i}I{/i} missed you. And I am about to ride you so hard that your penis might break off. Sorry in advance."
    s "At least give Maya a chance to-"
    ay "Maya’s not going to leave now that she knows what’s going on. She’s going to stay here and yell and try to make us feel bad."
    ay "{i}Let her watch.{/i} I don’t even care."
    m "Yeah! You’re making that extremely apparent!"
    s "Ayane...come on."
    ay "Oh, I will. I’m so fucking horny right now that I’ll probably cum the second it’s inside."

    "She pulls her waist back and forth, slowly grinding against my dick- which is, as you may have guessed, extremely hard."

    ay "Then...I’ll cum again."
    ay "And again."
    ay "And again...and again...and again..."
    ay "And we can keep doing that for the next several months or so until everybody disappears and I have finally had my fill."

    "She presses her body harder against mine..."

    m "Seriously, stop! You’re being fucking...gross!"
    s "Ayane..."
    ay "Yeah, [ayanemaster]?"
    s "Let’s..."
    s "Let’s do this later, okay?"

    scene ohnoyoureawakeagain22
    with dissolve

    ay "What?! Seriously?! But we’ve already waited so long!"
    s "Which is why a couple more hours shouldn’t be that much of a problem."

    scene ohnoyoureawakeagain23
    with dissolve

    ay "Tch!"
    ay "If you’d have just looked away like I asked, there would be a penis inside of me right now! I can barely even remember what that feels like, Maya!"
    m "Uhh...I’m...I’m sorry?"

    scene black
    with dissolve2

    "Ayane pulls herself off of me and I have to awkwardly adjust myself so the following conversation doesn’t take place with an extremely large protrusion bulging out of my pants..."

    scene ohnoyoureawakeagain24
    with dissolve2

    ay "Hmph!"
    m "Do you not have the decency to fix yourself? You’re just going to stand here looking like that?"
    ay "I want Sensei to see what he’s missing."

    scene ohnoyoureawakeagain25
    with dissolve

    m "As if he hasn’t already memorized it..."
    s "I’m sorry, Ayane. It’s just-"

    scene ohnoyoureawakeagain26
    with dissolve

    ay "I know exactly what it is. But that doesn’t mean I’m not going to be grumpy about it when I have been looking forward to this day for far longer than any girl should ever have to."
    m "Oh, cry me a river."

    scene ohnoyoureawakeagain27
    with dissolve

    ay "Sensei, you are to report directly to me the moment school is over. From that point on, I can not guarantee your safety."
    ay "Water and other refreshments will be provided, and a change of clothes will likely be necessary. Perhaps multiple."
    ay "I am going to go make preparations and leave you here. But please know that if you have sex with Maya {i}before{/i} me and this was all a coordinated effort on both of your behalves to shoo me away-"

    scene ohnoyoureawakeagain28
    with dissolve

    ay "I’m gonna be really mad!"
    s "That’s it? That’s your threat?"
    ay "And I mean it!"
    m "Hah..."
    s "Thanks, Ayane. I really appreciate it and will report to you as soon as possible."
    ay "You’re darn right you will!"

    scene ohnoyoureawakeagain29
    with dissolve

    "Ayane storms off, leaving me alone in the midst of an extremely awkward silence with someone who I may have just saved from permanent visual impairment and emotional trauma."

    m "Ugh. I was really banking on that pregnancy theory. Now I have to deal with {i}this{/i} for the rest of forever. Wonderful."
    s "Was only a matter of time until you had to face the music. I don’t think any less of you for not being an expert on a concept no mortal would ever be able to grasp."

    scene ohnoyoureawakeagain30
    with dissolve

    m "I suppose that’s true."
    m "And...um..."

    scene ohnoyoureawakeagain31
    with dissolve

    m "Thank you...for stopping her."
    m "I didn’t believe she was actually going to go through with it. I’m used to people having a bit more...{i}tact.{/i}"
    s "Are you? Because you spend a lot of time with me and that’s sure as hell not a quality {i}I’m{/i} known for."

    scene ohnoyoureawakeagain32
    with fade

    m "No, you’re certainly not. And it’s honestly a miracle that I’ve been able to deal with you for even half as long as I have."
    s "The same could be said for you. There aren’t many people who can face such constant beratement and {i}still{/i} wind up coming back for more."
    m "You’re right. It would take either a monster or the world’s most insidious pervert to waltz into such torment. Unsurprisingly, you are both of those things. I hope you’re proud of yourself."
    s "I get by. Having someone constantly reminding me of how horrible I am has actually done wonders in desensitizing me to my own wrongdoings. So thank you for that."
    m "You’re welcome. I hope you die."
    s "Likewise."
    m "..."
    s "..."
    m "..."
    s "..."

    scene ohnoyoureawakeagain33
    with dissolve2

    m "I was worried too..."
    s "I know."
    m "Never disappear for that long again. I mean it."
    s "It would have been fine for you to break down too, you know? You didn’t have to stay strong the whole time."
    m "I got all of my crying out of the way on Christmas."
    m "I’ll be fine for a thousand more years."

    scene black
    with dissolve2

    "The day ends."
    "But something else begins."

    play sound "static.mp3"
    scene thething with flash
    stop sound
    stop music

    "do you know what?"

    $ renpy.end_replay()
    $ slumberreset5 = True
    $ ayanenosex = False
    $ maya_love += 5
    $ ayane_love += 1
    $ yumiblock = False
    $ makotoblock = False

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    $ ayane_lust += 1
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    $ ayane_lust += 1
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    $ ayane_lust += 1
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    $ ayane_lust += 1
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    $ ayane_lust += 1
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    $ ayane_lust += 1
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    $ ayane_lust += 1
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"

    jump endofsat

label mothersmilk:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
scene wemadeit36 with flash
    stop sound

    q "Just one?"
    sev "Just one."
    q "What is it?"
    sev "I choose...this one."
    q "What is it? Tell me. And I’m not answering anything gross anymore, so you can forget it if it’s something like that."
    sev "I can’t read the question until you change...but what I {i}can{/i} tell you..."
    sev "Is it may very well change the future."

    scene wemadeit37
    with dissolve2

    q "..."
    sev "..."
    q "You’re sick."
    q "You’re {i}all{/i} sick. I don’t understand how you can do this to someone so...helpless. He’s broken. Can’t you see that?"
    sev "He can be fixed."
    sev "They can always be fixed."
    q "I’m done after this. I’m not coming back."
    sev "Moyo will be very upset to hear that. She likes you very much."

    play sound "static.mp3"
    scene wemadeit38
    with flash
    stop sound
    stop music

    sev "Final question..."
    sev "You got me pregnant, but I never told you about it because I am a coward."
    sev "Something happened that made the baby go away."
    sev "I remember, but I pretend that I don’t because it makes it hurt less."
    sev "I picked out a name for her."
    sev "It was one I knew you’d like."
    sev "What was it?"

    $ whatyousaid = renpy.input("The answer is...")
    $ whatyousaid = whatyousaid.strip()

    s "[whatyousaid]."
    ay "..."
    s "..."
    sev "Fact checker?"
    ay "..."
    s "..."
    sev "I’m going to need an answer."
    ay "I..."
    ay "I can’t give you one."
    sev "You can’t? How strange. Why do you think that is?"
    ay "..."
    sev "Perhaps...you’re afraid of what will happen if you do?"
    ay "..."
    sev "Of what will happen to {i}you.{/i}"
    ay "I’m sorry."
    ay "I can’t protect you."

    play sound "eggcrack.mp3"
    scene wemadeit39 with hpunch

    sev "Oooh, too bad! It looks like we’ll have to send you back to the beginning of everything after all!"
    sev "I’ll remember you always, [mayamaster]. The feeling of your cock still lingers in my-"

    play sound "static.mp3"
    scene wemadeit40 with flash
    stop sound
    play music "alarmbell.mp3"

    sev "What? What happened?"
    s "..."
    sev "{i}Now? But I was informed that wasn’t possible.{/i}"
    s "..."
    sev "Does It know yet?"
    s "..."
    sev "I see..."

    if cheater == True:
        sev "..."
        sev "Yes. Adjustments have already been made and precautionary measures have been taken to ensure it does not happen again."
        sev "..."
        sev "Understood."

    play sound "static.mp3"
    scene wemadeit41 with flash
    stop sound

    sev "It appears that there has been an interruption in today’s broadcast."
    sev "If your connection has not yet been severed and you are still watching this program, thank you. But it is with a heavy heart that I must sign off."
    sev "Thank you again to our sponsors and to all of the people who-"

    scene wemadeit42
    play sound "pop.mp3"

    sev "Oh no."
    sev "He popped."

    $ renpy.end_replay()
    $ slumberreset4 = True
    stop music
    jump slumberreset5
...
```