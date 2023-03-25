# A Day in the Life (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Loggerhead](./yumislumber2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: yumislumber3
* Group: Yumi
* Triggered by label: yumislumber2
* Chain sources: yumislumber2
* Chain sources path: yumislumber2

## Official wiki page

[A Day in the Life](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumislumber3&go=Go) for more details.

## Event code

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label yumislumber3:
    play sound "static.mp3"
    scene thisisgreen1 with flash
    scene thisisgreen2 with flash
    scene thisisgreen3 with flash
    scene thisisgreen4 with flash
    scene thisisgreen5 with flash
    scene thisisgreen1 with flash
    scene thisisgreen2 with flash
    scene thisisgreen3 with flash
    scene thisisgreen4 with flash
    scene thisisgreen5 with flash
    scene yuminightschool1 with flash
    stop sound
    play music "amiawake.mp3"

    s "..."
    y "Welcome back."

    scene yuminightschool2
    with dissolve

    s "Are we at...school? When did we get here?"
    y "Somewhere in the time between your brain clockin’ out and then gettin’ called back in to work, I guess."
    y "Lasted a fuckin’ while this time. Guess it ain’t much compared to two months if that’s really what happened, though."

    scene yuminightschool3
    with dissolve

    s "And you stayed with me?"
    y "Looks that way. Ain’t like I had anything else going on after Chika kicked me out."
    y "But just because I didn’t leave you in some dried-up aqueduct with a decomposing chicken doesn’t mean I suddenly like you."
    s "Really? Because that’s my go-to benchmark for deciding whether or not I’m close to someone."

    scene yuminightschool4
    with dissolve

    y "Ha ha ha. Eat an entire bag of dicks."
    s "Why {i}here?{/i}"
    y "Fuck if I know. You kept sayin’ some shit about a box and, before I knew it, you were draggin’ me all the way across town and unlocking the gate."
    y "Fine by me since there’s food here and shit. But I ain’t sure if it’s a good look for you to be wanderin’ around the halls with a delinquent after hours."
    s "You’re no longer a delinquent, though. Auto-pilot Yumi reformed herself during your two months of absence."
    y "You say that as if you were there."
    s "I kind of wish I was. Prefect Yumi is a sight I don’t think I’d ever be able to see otherwise."
    y "No one said anything about bein’ a prefect. For all we know, I was still an asshole. Just a...more present asshole, I guess."
    s "Did I say anything else about a box?"

    scene yuminightschool5
    with dissolve

    y "You actually have an idea of what that means? Cause I kinda figured it was just mindless blackout shit."
    s "Yes and no. It’s hard to explain."
    y "Yeah, what else is fuckin’ new? This has quickly become the weirdest week ever and that’s in no small part to gettin’ dragged along in a day of the life of the world’s most open sex offender."
    s "This is probably the first full day we’ve spent together, isn’t it?"
    y "Depends on whether or not you count the last three hours as “you.” "
    y "Also, don’t go makin’ it sound like this was enjoyable for either one of us. Woulda had more fun stayin’ at home helpin’ Chika keep her sister alive."
    s "Go do that then. I can survive without a chaperone."

    scene yuminightschool6
    with dissolve

    y "..."
    s "..."
    y "If I go...what’ll happen if you zone out again?"
    s "Are you actually worried about me?"

    scene yuminightschool7
    with dissolve

    y "N-No! Why the fuck would I ever worry about {i}you?!{/i} I just meant I...I don’t really care about us bein’ alone anymore. I can hold my own if you decide to get all fucking...well...you know how you get."

    scene yuminightschool8
    with dissolve

    y "Plus, we...kinda left off at a weird spot and...guess I’m still a little interested in whatever this whole memory shit is."
    y "I’m just hangin’ around ‘cause I want answers. And if anybody’s got answers, it’s you."
    s "What made you change your mind? Because it seemed like you were barely even listening earlier."
    y "You just suck at explainin’ shit. Obviously I’m gonna be interested if weird, supernatural-ish shit starts happenin’ to me. I just ain’t sure if we can, like...do anything about it yet."
    y "But if you’ve got ideas...I can, like...listen or whatever. Even if you’re just fuckin’ with me. Which you probably are. But at least it’s a little...entertaining, I guess."
    s "..."
    y "..."
    s "You’re hungry, right?"
    y "Kind of. Was too busy makin’ sure you didn’t walk into oncoming traffic to stop and eat."
    s "Then how about we continue this conversation in the cafeteria?"

    scene black
    with dissolve2

    "Something feels different."
    "Dangerous, even."
    "But the danger surprisingly does not lie in my own hands and their ability to effortlessly pluck the petals from premature flowers."
    "It lies in the air."
    "I can feel it becoming tangible...twisting into the shape of hands."
    "I can see their fingers elongating...tightly constricting our necks."
    "All that’s left is to patiently wait and see which one of us chokes first."
    "..."
    "I hope it’s her."
    "It would be easier to take her home if she were unconscious."
    "........."
    "......"
    "..."

    scene yuminightschool9
    with dissolve2

    y "This place always feels so different at night..."
    y "Takes a lot to creep me out but, not gonna lie, this shit comes close."
    s "It doesn’t take a lot to creep you out. I successfully creep you out every single day."
    y "Yeah, the thought of getting raped will do that."

    scene yuminightschool10
    with dissolve

    s "I wouldn’t-"
    y "Weirdly enough, shit gets even creepier when you turn the lights {i}on.{/i} "
    y "Think it’s probably cause it feels less like sneakin’ in and more like everybody’s just...gone. Like the whole world’s in the process of vanishing or some shit."
    s "Well, I can definitely relate to that."

    scene yuminightschool11
    with dissolve

    y "You come here often? At night, I mean."
    s "Are you hitting on me?"
    y "No, but I {i}will{/i} hit you if you say that again."
    s "Every once in a while, I’ll show up. I don’t think it’s ever really been intentional, though."
    y "You mean with your blackouts? They lead you here often?"
    s "Either them or a small girl with a ponytail."

    scene yuminightschool12
    with dissolve

    y "Your niece’s friend? The fuck would {i}she{/i} have to do here so late at night?"
    s "Either she has a very strange hobby or it has something to do with why time is stuck-"

    scene yuminightschool13
    with dissolve

    y "Wait. Hold that thought. Do you want food or some shit? Because I’ve gotta feeling this is gonna be a long ass explanation and I ain’t gonna be able to listen without something to eat."
    s "I’m-"
    y "Fuck it. I’ll just pick something out for you. You’ve treated me to dinner during the job search BS, so I’ve got you this one time."
    s "Well, thank you for treating me to a meal that I do not want with money you do not have to use."
    y "You should really say thank you when people do nice things for you, prick. "

    scene yuminightschool14
    with dissolve

    "Yumi disappears into the kitchen, but doesn’t take it upon herself to kill the darkness as the only light I can make out from here is the faint glow of a refrigerator door opening."
    "I can tell from the way she moves that she really has done this before, but I’m not sure if I should be thankful I haven’t bumped into her here or...disappointed? Is that the right word?"
    "If I had crossed paths with her while on one of several trips with Maya, maybe it wouldn’t have taken so long to reel Yumi into this segment of the hidden world?"
    "After all, she does seem at least slightly central to some “deeper” aspect of my life given how frequently I lose my mind around her..."
    "But would that alone have been enough to convince her to hear me out? "
    "And will she hear anything at all when my half-baked attempts at explaining things add up to no more than just “your memory is broken but so is mine. Let’s have a sleepover?”"
    "I have no idea what I’m doing...nor any idea of what I even want Yumi’s role to be if things {i}do{/i} continue to progress like this."
    "All I know is I’d feel a little emptier if the one segment of common ground we’ve found ruptured and split."

    scene yuminightschool15
    with dissolve2

    "When she returns, I think about what I would have done if I never encountered Maya on the rooftop that night so long ago."
    "Would I have felt lonely?"
    "Would I have maintained the steady pursuit of fucking my entire classroom — completely disregarding how empty it would have felt apart from the momentary warmth?"
    "Where would it have ended?"
    "I think for another moment about what would have become of the other {i}me’s{/i} that never felt the first traces of waking up...but I have no reason to brag when I’ve only just begun to open my eyes."
    "When will it end?"
    "..."
    "Just what is the point of all of this?"

    y "Uhh...hello?"

    scene yuminightschool16
    with dissolve

    s "Hi."
    y "Okay, good. Wasn’t sure if you were “there” again or not. "
    s "I am. And thanks again for the free food that I didn’t want."
    y "You sure? Cause you haven’t eaten all day either. Been with you the whole time."
    s "Ami gets mad if I don’t eat the dinner she makes for me every night, so I’ll hold out if it means not getting an earful from her in the morning."
    y "Damn. She’s got you even more whipped than I thought."
    y "She involved in all this weird, time-related stuff too? Or is that reserved for just you and Ponytail?"
    s "Ami’s unrelated. It’s just Maya, Ayane, and me right now."

    scene yuminightschool17
    with dissolve

    y "Huh. Guess that helps explain why the blonde one’s so fuckin’ obsessed with you and shit."
    s "She was like that before- actually, yes. That is why she loves me."
    s "It’s hard not growing close to someone when you live through the apocalypse together."

    scene yuminightschool18
    with dissolve

    y "Apocalypse? The fuck is this about an apocalypse? I thought we just had some disease or that time was, like...glitching out or some shit. Nobody said anything about an apocalypse."
    s "That’s just sort of how we started referring to it. "
    s "You’ll get a more in-depth answer if you decide you really {i}do{/i} want to look more into this, but the bare-bones explanation is that the world is going to end soon and only a few of us are going to remember it."

    scene yuminightschool19
    with dissolve

    y "The fuck do you mean it’s going to {i}end?{/i} How can you stay so calm while saying that shit?"
    s "Because it’s going to start again right afterward. At the same place in the school year, but not the same place in time. Do you understand?"
    y "No. {i}Fuck{/i} no. Am I being Punk’d? Are there cameras here or some shit? "
    s "I really hope not. My job would be in even greater jeopardy than it already is."

    scene yuminightschool20
    with dissolve

    y "Apocalypse...a new world...reliving the same school year?"
    y "How...how the fuck am I supposed to believe that?"
    s "The only way to believe it is to see it for yourself, I think. "
    y "And if I..."
    y "If I sleep with you, I’ll somehow-"
    s "I’m going to stop you right there because that is definitely not what I was getting at when I suggested that you sleep over my house."

    scene yuminightschool21
    with dissolve

    y "Be a little more honest about that next time! Of course I was gonna think that’s what you were tryin’ to get at! What kind of grown man just has a normal sleepover with teenage girls?!"
    s "I’m not the leader of a sex cult, Yumi. I’m just some guy with advanced knowledge of how the world works who is trying to shepherd others into understanding as well."
    y "That sounds exactly like what the leader of a sex cult would say!"
    s "You don’t have to sleep with me. You literally just have to show up and hang out at my place so we can all monitor each other and discuss what’s been going on."
    s "Like I said, you’re one of the only people who has ever been able to grasp that things aren’t exactly as they seem. So we want to use you as a sort of...test subject, I guess."
    y "And that’s supposed to convince me?!"
    s "What {i}would{/i} convince you? Because if honesty doesn’t work, I’m not really sure what else to do. I’m not going to force you."
    y "I-"

    scene yuminightschool22
    with dissolve

    y "Hah..."
    y "How the fuck would I explain that to Chika?"
    y "I get that you ain’t just pervin’ out on me this time, but I’ve got no idea how to tell her that I’m stayin’ at your place even if I {i}do{/i} decide to."
    s "Then don’t tell her."
    y "She’s my best friend and she’s...fuckin’ {i}in love{/i} with you for whatever reason. I can’t just ignore that because it’s convenient."
    s "Convenience doesn’t have anything to do with it, Yumi."
    s "I’m obviously not one to model your priorities after, but I don’t think it’s all that far-fetched to say getting to the bottom of a time loop is a little more important than {i}love.{/i}"
    y "Doubt Chika would agree."
    s "Chika probably won’t even remember once everything is said and done. But I guess I can’t guarantee that as it seems the memories that {i}do{/i} carry over are very...inconsistent."
    y "Inconsistent how?"
    s "Inconsistent like...some memories are just omitted if they have anything to do with time or...events surrounding the whole world-resetting ordeal."
    y "But memories like being sexually assaulted by a teacher get to stay? Sounds fair."

    scene yuminightschool23
    with dissolve

    y "Figures the world would go out of its way to make my life even shittier. Ain’t like it’s done enough of that already."
    y "Whether it be deadbeat parents...or growin’ up too mean to get anybody to like me...or havin’ a teacher who openly admits to beating off to his students..."
    y "Or how I...how despite that, I..."
    s "..."

    scene yuminightschool24
    with dissolve

    s "I get it."
    s "You don’t have to come."
    s "I’ll tell Maya and Ayane that-"
    y "I’ll...do it."

    scene yuminightschool25
    with dissolve

    s "..."
    y "I’ll do it, but...I still ain’t sure what I’m gonna say to Chika. And if you do anything to make me feel even slightly uncomfortable while I’m there, I’m noping the fuck out. Got it?"
    s "...Yeah."
    s "That’s fine."
    y "Cool."
    s "..."
    y "..."
    y "Anyway, I ain’t really hungry anymore, so...I’m gonna, like...get rid of all this shit so nobody knows anyone was here when they weren’t supposed to be."
    y "I’ll be fucked out of a bunch of meals in the future if security suddenly tightens and...yeah. I’ll clear your tray too, I guess."
    s "Yumi-"
    y "How about we just...shut the fuck up for a little while, okay?"

    scene black
    with dissolve2

    "Yumi clears everything off of the table and, for the next ten minutes, we keep our lips sealed."

    play sound "static.mp3"
    scene thisisgreen5 with flash
    scene yuminightschool26 with flash
    stop sound

    "But something we find in the hallway beckons us to part them."

    y "What the...fuck?"
    s "..."
    y "That...wasn’t there the whole time, was it? Didn’t we come down this hallway on the way to the cafeteria?"

    play sound "static.mp3"
    scene thisisgreen5 with flash
    scene yuminightschool27 with flash
    stop sound

    s "We did..."
    y "Are we...not alone in here? "
    y "Somebody’s gotta be playin’ a prank on us, right?"
    s "..."
    y "You said Ponytail or...uhh...{i}Maya{/i} or whatever comes here too, right? Would {i}she{/i} do something like this?"
    y "Cause this ain’t-"

    scene yuminightschool28
    with dissolve

    y "Yo! What are you doing?! There could be, like...a bomb in there or some shit!"
    s "I have to move it."
    s "If I don’t move it, we can’t leave."
    y "We can just walk around it, you fucking idiot! It ain’t like it’s-"

    stop music
    scene bedroom_night
    play sound "cheer1.mp3"

    s "{b}Lucy, I’m hooooooome!{/b}"
    s "{b}And I brought a PRIIIIIIIIIIZE!{/b}"

    scene black
    stop sound

    "THE DAY ENDS"

    $ renpy.end_replay()
    $ yumislumber3 = True
    $ yumi_love += 3

    if day == 4:
        $ totaldays += 1
        $ day = 5
        hide thursday onlayer date
        show friday onlayer date
    if day == 3:
        $ totaldays += 1
        $ day = 4
        hide wednesday onlayer date
        show thursday onlayer date

    "A NEW ONE BEGINS"
    "And I know what it is I have to do."

    jump slumberphonemenu
...
```

## Code that triggers this event

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
y "Though, I guess “the other day” is two months ago at this point."
    y "I was stayin’ at my dad’s place for a while since I didn’t have anywhere else to go and...I guess she caught wind of it and showed up."
    y "And, honestly...it went...kinda good. She wasn’t pissed that I got kicked out of school and didn’t call me a letdown or any of that shit..."
    y "Just told me I was doin’ a good job and that Nodoka probably deserved what she had comin’ to her. Which she did."
    y "Wasn’t just her either. Kaori was there too. Was the first time I talked to her in years."

    scene chickenscene17
    with dissolve

    y "Did you know it was her birthday on Christmas? How fuckin’ wild is that? "
    y "People used to talk about how weird it was that we were both born on such big holidays, but I feel like she’s the one who got the short end of the stick, all things considered."
    y "Ain’t nobody gonna remember someone’s birthday if it’s on fuckin’ Christmas. Halloween’s easy cause it ain’t that big of a deal."
    s "What was it like getting to talk to her after so long? Is she anything like you remember?"

    scene chickenscene18
    with dissolve

    y "She, uhh..."
    y "I was kinda expectin’ it after seein’ her with you that one time, but...she ain’t exactly “all there” anymore."
    y "Wasn’t ever really {i}normal{/i} by any means, but...she’s different now. Don’t think she really remembers me either, which ain’t as hard on me as I expected it to be...but still."
    y "Kinda surreal seein’ somebody you thought was dead just...suddenly alive and full of energy. Almost {i}too{/i} much energy, if you ask me."

    scene chickenscene19
    with dissolve

    s "That is certainly one way to describe her, for sure."
    y "..."
    s "..."
    s "Do you want her number?"
    y "Kaori’s? Why?"
    s "To talk to her, obviously. "
    y "I literally just told you she doesn’t remember me. "
    s "So remind her. That’s what your mom did and the two of them are relatively close now. "
    y "Yuki’s just tryin’ to right all the wrongs she made with me by latchin’ onto somebody else who’s lackin’ a mother figure. Does the same shit with Io if what I’ve heard is true. "
    s "Maybe. But I don’t see why that should prevent you from having a relationship with Kaori."
    y "I don’t need another “relationship.” Chika’s more than enough for me. And that’s not even countin’ whatever the fuck is goin’ on between us."
    s "What {i}is{/i} going on between us?"
    y "Fuckin’...time travel or some shit apparently. Ain’t like {i}I’ve{/i} got a fuckin’ clue."
    s "Take her number, Yumi. I’m obviously not one to tell you what is and {i}isn’t{/i} good for you, but it’s not like I’m asking you to call her."
    s "You’ll just...be able to if you ever feel like it."

    scene chickenscene20
    with dissolve

    y "Hah..."
    y "I guess if it’ll get you off my fuckin’ back, I’ll-"

    scene chickenscene21
    with dissolve
    stop music fadeout 3.0

    y "Huh?..."

    scene chickenscene22
    with dissolve

    s "Is something wrong?"
    y "Do you...see that?"
    s "See what?"
    y "Over there...at the end of the aqueduct. "
    s "I don’t see-"

    scene black
    with dissolve

    s "Wait, where are you going?"
    y "To check out what the fuck that is, obviously. Stay here if you’re gonna be a fuckin’ pussy about it."

    "Yumi takes off toward the end of the aqueduct, and as I lift myself off of the ground to follow her, I notice whatever it is she sees."
    "........."
    "......"
    "..."

    scene chickenscene23
    with dissolve2

    y "..."
    s "..."
    y "How the fuck?..."
    s "..."
    y "Since when do we have wild chickens in Kumon-mi?"

    play sound "static.mp3"
    scene chickenscene24
    with flash
    stop sound
    $ renpy.pause(5, hard=True)

    s "That’s not a wild chicken..."
    s "That’s someone’s pet."

    $ renpy.end_replay()
    $ yumislumber2 = True

    play sound "eggcrack.mp3"
    scene gamechicken
    $ renpy.pause(10, hard=True)

    jump yumislumber3
...
```