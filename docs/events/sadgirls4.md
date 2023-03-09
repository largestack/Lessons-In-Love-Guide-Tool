# To Anyone Who Passes By
Haruka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls4&go=Go)


Part of event chain [Adulting](./sadgirls3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: sadgirls4
* Group: Haruka
* Triggered by label: sadgirls3

## Event code
File: \game\HarukaEvents.rpy
Code:
```python
...
label sadgirls4:
    scene harukaoutdoor1
    with dissolve2

    "Someone who doesn’t seem to have a problem holding {i}anything{/i} in, though, is Haruka- who is currently sharing her recent fortune with a still noticeably confused Rin."
    "At least she’s not the {i}only{/i} one confused."
    "It’s hard enough figuring out how to deal with a woman who lost her husband. Jumping directly from that to a woman who {i}gained{/i} a husband is just more than I can process this early in the morning."
    "But at least it seems like Haruka isn’t diving headfirst into celebration mode based on her current expression."

    if harukasex == True:
        "I’m sure that our talk last night might have something to do with that, though."

    r "But...wait. If {i}your{/i} husband is okay, what about Makoto’s mom’s husband? "
    r "That’s gotta have something to do with-"
    h "That’s...not really something I think I should be discussing with you. I just wanted to give you an update about {i}my{/i} situation since I know you’ve been, uhh...curious about it."

    scene harukaoutdoor2
    with dissolve

    r "Well, I’m really happy for you. That’s great news."

    if harukasex == True:
        scene harukaoutdoor3
        with dissolve

        r "But, uhh...what exactly does that mean for Sensei?"
        h "Ah..."
        h "I thought you were leaving with Maki. I didn’t realize you were right behind me."
        s "Maki went off to meet up with Sara, I think. What’s this about me?"
        r "Just...well..."
        r "Aren’t you two, like...you know..."

        scene harukaoutdoor4
        with dissolve

        r "Actually, I want to keep my job, so I probably shouldn’t say it right now."
        h "That’s not..."
        h "Things are a lot more complicated than that! "
        s "Wouldn’t flat out denying it work a little better here, Haruka?"

        scene harukaoutdoor5
        with dissolve

        h "I can’t deny it when she already knows. "
        h "Besides, I’m not wrong, am I? You told me just last night that my, uhh...circumstances are all messed up. "
        h "Did you change your mind after a night’s sleep? Or were those just words you used back then to try and soothe me?"
        r "You know what? I just remembered that I have dishes to wash. And that this is something you two should probably figure out without me in the picture."
        h "No..."
        h "You need to stay here and watch the store while he and I have an actual conversation. One where I don’t rip my shirt open and try to get him to screw me."

        scene harukaoutdoor6
        with dissolve

        r "On second thought, maybe this {i}is{/i} something I should be involved in? "
        r "You two basically are my second set of adoptive parents anyway.  And my first set never gave me the sex talk because girls can’t get other girls pregnant. "
        h "I’m going to take your {i}father{/i} outside now, Rin. "

        scene harukaoutdoor7
        with dissolve

        r "Okay, Mom. Don’t press your bodies up against the glass when you inevitably go at it. I’m the one who has to clean them."
        h "Noted. "

    else:
        scene harukaoutdoor8
        with dissolve

        r "But, uhh...what exactly does that mean for Sensei?"
        h "Wha-"
        h "I thought you left with Maki? What are you still doing here?"
        s "Maki ran off to go meet up with Sara. What’s all this about me?"

        scene harukaoutdoor9
        with dissolve

        r "Nothing. Nobody here wants to fuck you. {i}Especially{/i} nobody named Haruka."
        h "Are you fucking kidding me right now? Is this really the time for that?"
        r "Time for what? I’m just here to make coffee and keep secrets. "
        r "Besides, just {i}wanting{/i} to do something isn’t a big deal unless you actually do it, right? "
        r "I figured by now that both of you were well aware of the sexual tension and just not giving into it because you knew it would be fucked up."

        scene harukaoutdoor10
        with dissolve

        r "If you ask me, though- I’m on Team Sensei because at least he is {i}here.{/i}"
        h "Okay...I’m going to go outside now so I can have a real conversation with him. And you’re going to stay {i}here{/i} and watch the store so I can do that."

        scene harukaoutdoor11
        with dissolve

        r "Aye aye, Captain Haruka. You two enjoy your fun adult conversation where you pretend you don’t want to bang."
        h "I’m sorry about her."
        s "It’s fine. I’ve come to accept her the way she is and you should too."
        s "Also, it’s not like she’s {i}wrong.{/i} I know for one that I-"
        h "Please don’t finish that sentence. I can already tell that it’s going to do more harm than good."

    scene black
    with dissolve2

    h "Come on. It’ll be easier to talk without the world’s nosiest teenager getting all up in our business."
    r "Hey! I have a {i}cute{/i} nose! Otoha tells me all the time!"

    "Haruka and I exit the cafe, surveying the surroundings to make sure that no one else is around before we begin what will be my second mature conversation of the day."

    if harukasex == True:
        "Or at least what I {i}hope{/i} will be my second mature conversation of the day."
        "Given what happened the {i}last{/i} time Haruka and I tried to talk, I’m not really sure."
    else:
        "Unless Haruka plans on just excitedly freaking out about her husband being alive again. "
        "Which, based on the brief conversation we had yesterday, seems highly probable."
        "It does seem that I’m actually more involved than I thought, though, if what Rin said has any truth to it."
        "Am I involved enough to have Haruka throw everything else away in an effort to chase me down? Of course not."
        "But one good conversation could disconnect our paths entirely. "
        "And that’s probably why she wants to do this."

    scene sky
    with dissolve2

    "The one good thing about today (Not counting Haruka’s husband, since I have never met and couldn’t care any less about the guy) is that, at least thus far, the sun has shown us mercy."
    "It’s still early, though. And life does prove to be inconvenient in more ways than most of us would like to admit. But if it means dodging tragedy in the form of UV rays, I can pretend to be an optimist for a bit."
    "It’ll be good to have {i}one{/i} of us fulfill that role, at least- as the sigh that escapes Haruka’s lips as she slouches against the wall reveals that it certainly won’t be her."
    "And that this change, albeit one much brighter in color than that of her friend, has drastically altered her life out of nowhere."
    "It remains to be seen if it’s what she wants, though."
    "Or if the last several years of being without him have turned her into something she can’t look at anymore."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    if harukasex == True:
        scene harukaoutdoor12
        with dissolve2

        h "I owe you an apology."
        s "You do."
        h "It was way fucked up for me to place the blame on you like that when this was as much of a decision on my end as it was yours."
        h "Actually, scratch that. It was {i}more{/i} of a decision on my end than yours. {i}You’re{/i} not the one hurting anyone else by sleeping with me."
        h "You’re not tied down the same way I am. Or...{i}was.{/i}"
        h "I guess what I’m saying is that I’m the one who loosened the knot my husband and I tied and that you were just...there to lend me a hand."

        scene harukaoutdoor13
        with dissolve

        h "You know...this whole {i}marriage{/i} thing...it wasn’t anything like I expected it to be."
        s "I don’t think most newlyweds anticipate a space war coming in between them."
        h "No, I guess they don’t. But even something like that is something I figured I was prepared for back when we first found out."
        h "I was still so high on the idea of being with someone I was in love with that there was {i}no{/i} amount of time that I wouldn’t wait for them to come back."
        h "But here I am, three years later...still married...yet trying to salvage my relationship with the man I’m regularly cheating on my husband with."
        h "What does that say about me?"
        s "It says that you’re confused. Which most people would be in your position."
        s "I’m not mad about what happened last night. I’m used to dealing with people at their worst, and I’m sure it felt like your life was falling apart."
        s "It was the contrast between that and something else that coerced me into walking away, I think."

        scene harukaoutdoor14
        with dissolve

        h "I can only imagine. "
        h "If I had known back then that Maki’s..."
        s "..."
        h "..."
        h "Why didn’t you tell me?"
        s "Because I already pissed her off once that day. And I didn’t want to go telling people things she didn’t give me the okay to talk about. Especially someone as close to her as you."
        s "I get that there was a lot going through your head when you called me, but Maki’s your best friend. You’re better than that."

        scene harukaoutdoor15
        with dissolve

        h "I’m not, though. "
        h "Everything I’ve done over the last few years has been mistake after mistake. And a good portion of those mistakes have been {i}repeated{/i} mistakes."
        h "Do you have any idea how many times we’ve had sex? Because I don’t. "
        h "What I do know, though, is that every single one of those times was me jamming a knife further and further into my husband’s back."
        h "I honestly wouldn’t be surprised if it was poking out of his abdomen by now."
        s "Can you think of a metaphor a little less gruesome, please?"

        scene harukaoutdoor16
        with dissolve

        h "No."
        h "I deserve the most disgusting and gruesome metaphors my shitty brain can come up with. Anything less wouldn’t be fair."
        s "I still don’t think that what we’ve done is that big of a deal. "

        scene harukaoutdoor17
        with dissolve

        h "No, it {i}is{/i} a big deal! And I really wish you’d stop saying it’s not!"
        h "This is more than me thinking my husband is gone and emotionlessly using the body of some other man to fill the void he left!"
        h "It’s more than me making a little mistake! More than me trying to hide my loneliness the only way I know how!"
        h "It’s the fact that I {i}know{/i} he’s alive now! That I know he has a chance of coming back!"
        h "And that I still want you despite that!"

        scene harukaoutdoor18
        with dissolve

        s "..."
        h "..."
        h "I don’t want to feel this way anymore...like I’m being forced to choose between two things I want when one of them I can’t even {i}have{/i} and the other is an option I didn’t even realize {i}existed{/i} until I already chose."
        h "And no. This isn’t me saying that I’m thinking of separating with my husband and just devoting myself to you instead."
        h "I just..."
        h "I can’t help but think sometimes that something like that might be nice."
        h "Anyway, I’m sorry for yelling at you and...saying all of the fucked up shit that I said...and blaming you and not listening and...anything else you want me to apologize for."
        h "You didn’t deserve it."
        h "So if you want to go off on me for being selfish and neurotic and just an all around shitty person, you can. Because {i}I{/i} deserve that."
        h "If I didn’t, I wouldn’t keep making the same mistakes."
        s "..."
        h "..."

        scene harukaoutdoor19
        with dissolve

        s "I’m not going to go off on you."
        s "I’d just like some sort of warning beforehand if this winds up happening again. Walking all the way over there just to get yelled at for your shitty behavior kind of sucked."

        scene harukaoutdoor20
        with dissolve

        h "You’re...{i}still{/i} going to come over?"
        s "Well, {i}somebody’s{/i} gotta fuck you, right?"
        h "That’s...That wasn’t really the point I was trying to-"
        s "I know it wasn’t the point you were trying to make."
        s "It’s just easier to talk about it like that."
        h "..."
        s "..."

    else:
        scene harukaoutdoor21
        with dissolve

        h "So, umm..."
        h "Can we avoid the part about the sexual tension? Or is that a thing we actually have to address?"
        s "We can avoid it. I’m just a little upset since I was starting to think you were calling me out here to confess."

        scene harukaoutdoor22
        with dissolve

        h "Ahh, yes. What better time to confess than the 24 hours following the revelation that your husband is still alive?"
        s "Jokes aside, if you didn’t call me out here to talk about that...why {i}did{/i} you call me out here?"

        scene harukaoutdoor23
        with dissolve

        h "To thank you."
        s "Me? For what?"
        h "For also feeling that tension and never giving into it."
        s "I thought we weren’t going to-"
        h "We’re not. It’s...something much bigger than {i}just{/i} that. "
        h "It’s something that’s been an unavoidable part of who I am for years now...a part that I never figured out how to address until meeting {i}you{/i} brought on a whole bunch of new challenges."
        h "You can say it’s due to an overwhelming lack of men or something like that..."
        h "But you are the exact sort of temptation I have always feared I’d face."
        h "I get lonely very easily. I’m sure you know that much about me by now. And it’s that sort of loneliness that makes me think things I shouldn’t sometimes."
        h "And maybe it’s like Rin said. Maybe just thinking things and never actually {i}doing{/i} them is fine...but it sure as shit doesn’t feel that way."
        h "Having you around...made me think a bunch of things all the time. Things that seemed like magic in the moment, but tapeworms once the moment faded."
        h "I found myself trying to appeal to you without even realizing it. "
        h "Unbuttoning my blouse when you walk into the store...{i}forgetting{/i} my wedding ring at home so it would look like I wasn’t committed."
        h "And, honestly...if you’d have pursued something with me...I really think I would have let those compulsions of mine win."

        scene harukaoutdoor24
        with dissolve

        h "But you didn’t."
        h "And sure, you might joke about how you’d be completely fine with throwing all of that away and starting an actual affair with me-"
        h "But you’re the one who held back when I was ready to bend."
        h "{i}That{/i} is why I wanted to thank you."
        h "You protected me from myself when I’ve always been my own worst enemy."
        h "I don’t know if you did it {i}to{/i} protect me...or if you had some other sort of motive in mind...or even if you’re just flat out unattracted to me."
        h "But whatever reason it was that we became what we are today instead of what I fantasized about..."
        h "I’m thankful for that reason."
        h "I’m thankful for you."
        h "And I seriously can’t thank you enough."
        s "..."

        scene harukaoutdoor25
        with dissolve

        h "I feel like I’m going to stop forgetting my ring as much when I leave the house now."
        h "There’s not really anyone I feel the need to appeal to like that anymore."
        h "Because, thanks to a certain close friend of mine, I now understand that there’s more than one way to dispel loneliness."
        h "That there are plenty of ways to feel full without being filled up."
        h "Because at the end of the day...what I already have should be enough for me."
        h "And that reaching for any more would just be greedy."
        s "..."
        h "..."
        s "Want to make out?"
        h "Nope."

        scene harukaoutdoor26
        with dissolve

        s "Wow. You really have turned over a new leaf."
        s "Back in the beginning, you’d just make out with me without even asking."
        h "Okay, first off, that only happened one time and I was extremely drunk."
        h "Second, I’m still kind of upset about it. So don’t joke like that."
        h "Third, do you even {i}want{/i} to make out with me? Or do you just feel weird that I forced you into a sentimental conversation when your biggest goal in life is to avoid those?"
        s "Yes and yes. "
        h "Well, too bad. Because a phone call I received yesterday has reminded me of just how long I am willing to wait."
        h "And no handsome man with a well-defined body and mysterious aura will change that."
        s "If only I was less mysterious."

        scene harukaoutdoor27
        with dissolve

        h "Yes. If only."

    "A moment of silence washes over the two of us as the streets finally begin to fill with people."
    "But seeing as we’ve already passed the points of our conversation that demand secrecy, I don’t see much of an issue with it."
    "To anyone who passes by, we probably just look like lovers."
    "Ironically enough, that’s the one thing we’ll never be."
    "Haruka’s heart belongs to someone else."

    if harukasex == True:
        "I’m just the man who took it."
    else:
        "And it’s not as if I’d take it anyway."

    scene harukaoutdoor25
    with dissolve

    h "Anyway..."
    h "I guess it’s about time we head back in. "
    h "All those people on the street will soon remember they need coffee in order to survive and then turn to me in desperation."
    s "You’re going to stay here?"

    scene harukaoutdoor28
    with dissolve

    h "I mean...yeah. That {i}is{/i} my job."
    s "I just figured you might want to go spend time with Maki or something since she’s already on her way to the bar."
    s "She hasn’t shown any weakness to {i}me{/i} yet, but I’m pretty sure that brave facade she’s putting on won’t last nearly as long as she wants it to."
    s "Having another friend around might be good for her."
    h "I..."
    h "I didn’t realize you cared so much about her."
    s "Who says {i}she’s{/i} the one I care about?"
    h "..."
    s "..."

    scene harukaoutdoor29
    with dissolve

    h "Ahh..."
    s "..."
    h "I’d have to call Molly in."
    h "Do you think she and Rin will be able to get along for the rest of the day? Or are they still on bad terms?"
    s "Beats me. There’s only one way to find out, isn’t there?"
    h "I guess so..."
    h "Here’s hoping I still have a cafe to return to tomorrow."

    scene black
    with dissolve2

    "I leave Haruka’s side and blend in with the crowd as I begin to ponder over what else I can possibly do today."
    "I toy with the idea of showing up to the bar as well, but..."
    "I think that whatever is going on there would probably be best left between the girls."
    "I don’t belong anywhere with that level of uninhibited emotion."
    "Where I do belong is amidst a sea of faceless others, each focusing solely on where the day will bring them."
    "Paying no mind to me."
    "So to anyone who passes by, ignore me."
    "I’ll figure out where to go on my own."
    "Just focus on yourself."
    "Find your own way home."

    $ renpy.end_replay()
    $ sadgirls4 = True
    $ haruka_love += 1

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump sadgirls5

label sadgirls5:
...
```

## Code that triggers this event
File: \game\MakiEvents.rpy
Code:
```python
...
scene makidayafter20
    with dissolve

    maki "But, as of yesterday, I'm the only parent Makoto has left. "
    maki "And if {i}I{/i} start breaking down and forgetting to eat and shower and brush my teeth, there’s no way that she’ll get over this in a healthy way."
    maki "So {i}that{/i} is what I’m worried about right now. Getting {i}her{/i} over this."
    maki "I can cry when that’s done."
    s "..."
    maki "..."

    scene makidayafter21
    with dissolve

    "As if on cue, Haruka walks into the cafe and immediately takes note of the friend she absentmindedly forgot to check on yesterday."

    if harukasex == True:
        "And while Haruka and I certainly have our own share of “issues” that we’ll need to address, that doesn’t matter right now."

    scene makidayafter22
    with dissolve

    "She stops at the counter and grabs a small tray of drinks and assorted pastries that Rin prepared for us but likely refrained from delivering on account of the conversation heating up."
    "With Maki’s eyes still closed in either reflection or avoidance at the sound of the door opening, I find no other space to rest {i}my{/i} eyes than in Haruka’s."
    "In that moment, hers rest in mine as well."
    "And they become congruent not in the fact that they share the same level of concern for someone that we enjoy the company of-"
    "But in the fact that they share in mutual pity."
    "For we may {i}think{/i} that we can connect with Maki in this moment."
    "But truly no one can without having experienced what she has."

    scene makidayafter23
    with dissolve

    "Haruka puts the tray down and fills her arms with something else before saying what any reasonable person in this situation would."

    h "I’m so sorry for your loss..."

    "But what does saying something like that even do?"
    "What good is the apology of an uninvolved party in the face of having your life ripped away from you?"
    "Are we not meant to mask our pity in situations like these?"
    "Are we not meant to scrounge up more genuine responses than we’d be able to find at the bottom of a barrel?"
    "Are we truly supposed to say we’re {i}sorry?{/i}"
    "Why?"
    "It doesn’t make sense."
    "But I suppose most things in this life don’t."
    "And I suppose that sometimes a genuinely sorrowful canned response can work as serviceable acknowledgment of that."

    maki "Thanks, Haruka. "
    maki "I’m really happy for you."
    h "Maki...if I knew that your husband-"
    maki "Don’t worry about it. You were excited and...wanted to share the news with someone."
    maki "You had no way of knowing."
    h "But if I did, I-"
    maki "It doesn’t matter."
    maki "So...thanks for your apology. I really appreciate it. But if you don’t mind, I’d like to finish up my conversation with Sensei. "
    maki "You and I can talk later."

    scene black
    with dissolve2

    "Maki tells me more about what she expects from Makoto going forward."
    "She has no idea when she’ll be able to return to school, but assured me that it wouldn’t be a problem as Miku would be taking all of her work directly to her."
    "As if that would even matter right now."
    "I’m not just saying this because I am a horrible teacher, but the last thing I expect out of a girl whose father just died is {i}schoolwork.{/i}"
    "Regardless, I nod and tell Maki not to worry about it- going so far as even offering to deliver Makoto’s “schoolwork” myself."
    "But of course, she in her unwavering devotion to not burdening anyone, refuses such a gesture before getting up from the table and straightening out her clothes."

    scene makidayafter24
    with dissolve2

    maki "Thanks again for meeting with me. I didn’t want the Maki from yesterday ruining your thoughts about the Maki from the future."
    s "I like all Makis equally. Though, I could do with this one being a little more selfish when it comes to her personal feelings."
    maki "Psht. Who needs feelings anyway? All they ever do is get in the way."
    maki "I’ve got a genius to take care of, Sensei. If she stays upset, she’ll never develop the cure for whatever the next big pandemic is."
    maki "I am doing this to save the world. My tears mean nothing in the face of the greater good."
    s "Well, whatever the case, good luck. And if you need any help with Makoto, don’t hesitate to ask."

    scene makidayafter25
    with dissolve

    maki "Leave it to me, Sensei!"
    maki "There’s no problem that Maki Miyamura can’t handle!"

    scene black
    with dissolve2

    "Maki says goodbye and wanders off to meet up with Sara and give her what I imagine will be a very similar speech."
    "I watch from the opposite side of the window, expecting to see her break down now that she’s no longer faced with a situation where she feels obligated to keep her tears in."
    "But she’s an adult."
    "So she probably holds it in until she’s at least a few blocks away."

    $ renpy.end_replay()
    $ sadgirls3 = True
    $ maki_love += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "........."
    "......"
    "..."

    jump sadgirls4
...
```