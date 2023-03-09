# Walk Into the Water
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas1&go=Go)


Part of event chain [Redeemer](./dormwartwo19.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: beachmas1
* Group: Main
* Triggered by label: dormwartwo19

## Event code
File: \game\chap3.rpy
Code:
```python
...
label beachmas1:
    "Something is wrong."

    play sound "static.mp3"
    scene scenetransition
    stop sound
    $ renpy.pause(2, hard=True)
    play sound "static.mp3"
    scene beachmasintro1
    with flash
    stop sound

    "Ayane and Maya quickly rush me behind the bathroom after..."
    "After...whatever it was that just happened."
    "And while it certainly is not the {i}first{/i} time I’ve ever seemingly teleported somewhere else in the middle of a conversation, it is...perhaps the most jarring."
    "Especially considering that it was more like the world itself is what teleported rather than just me."
    "But then...that wouldn’t explain all of the outfit changes and-"
    "We didn’t reset, did we?"

    s "Did-"

    play music "notabluearchivesong.mp3"

    m "No. "
    s "But you haven’t even heard what I was going to say yet."
    m "I don’t have to because it was the first thing {i}I{/i} thought as well."
    s "Well, there goes my five seconds of feeling smart. "
    ay "It seems like...we all kind of just went through the same thing then, huh?"
    m "I don’t like this..."

    scene beachmasintro2
    with dissolve

    ay "I mean...yeah, it’s scary. And...shocking. But, on the bright side, at least...we’re at the beach now!"
    m "Your perpetual optimism makes you both an invaluable asset and incredibly annoying. Why is being {i}here{/i} some sort of bright side? We don’t even know how much time we’ve lost yet."
    s "Can we ever really {i}lose{/i} time at this point?"

    scene beachmasintro3
    with dissolve

    m "You know what I mean. "
    s "So...just to recap, you two were also minding your own business when this happened? "
    ay "The two of us and Ami were talking about our plans for Christmas and...all of a sudden, we were just... here."

    scene beachmasintro4
    with dissolve

    ay "And...I guess Maya and I are close enough at this point that we were able to figure out what each other was thinking in just a single glance, so..."
    m "Yes, hooray. Friendship. But what comes {i}next?{/i} What do we do {i}now?{/i}"
    ay "I don’t know. Maybe go play volleyball or something? We {i}are{/i} at the beach."
    m "This isn’t the time to be playing around, Ayane. Not when we should be worrying about {i}how{/i} this happened."
    s "Well, what’s worrying even going to do? It’s not like we can sit down for five minutes and come up with a rational explanation for a sudden...group teleportation."
    s "How do you know it wasn’t a reset? Why are you so sure?"

    scene beachmasintro5
    with dissolve

    m "Oh, I don’t know. Maybe it was the part where I’m always able to feel when they’re coming. Or the part where we weren’t on the roof. Or the part where we didn’t all get annoyingly close to one another."
    m "Or the part where Ayane is still here when I’m almost certain that {i}not{/i} sleeping with you for an entire cycle will get her reverted back to her normal, less-informed self."
    ay "It really hurts when you say things like that about me, Maya."

    scene beachmasintro6
    with dissolve

    m "Oh, please. It’s not as if I’m unaware of the fact that you two talk about me behind my back. At least I’m courteous enough to not hide anything from you."
    ay "You mean other than the fact that you’ve been hiding the true nature of this world from me for what could be millions of years by now?"
    m "Yes, please forgive me for saving you from the countless existential crises I have prevented over the years. I am very sorry. Now, can we get back to formulating a plan that isn’t just playing {i}volleyball?{/i}"
    s "You can be a little nicer to Ayane, you know. It’s not like she wanted to get involved in any of this."
    m "What, and {i}I{/i} did?"
    ay "I don’t think there’s anything we {i}can{/i} do, Maya. "
    m "There has to be something."
    s "Has there ever been something before?"

    scene beachmasintro7
    with dissolve

    m "No, but {i}this{/i} has never happened before! "
    m "I’m sorry if it’s not exactly normal for me to be talking to someone one second, and then in a completely different place the next!"
    s "Well, if it’s any consolation, that sort of thing is pretty par for the course for me."
    m "That’s not-"

    scene beachmasintro8
    with dissolve

    m "Wait...there might actually be something there. I need to think."
    ay "You don’t have your phone on you...do you, Sensei?"

    "I reach into my pockets to find that...no. I do not have my phone. But that’s fine. I probably just left it {i}further back in time.{/i}"
    "Or...forward."
    "Or in a different location. "
    "I have no idea. It’s not everyday that everyone else is just as lost as I am."

    s "I don’t, no."
    ay "I guess we’ll just have to figure out the...circumstances of this trip from the other girls then. "
    ay "But, if it’s anything like our {i}previous{/i} beach trips...wouldn’t that mean that it should be {i}before{/i} Halloween, then?"
    ay "We always do our beach trip around August. Christmas should be our next big holiday and none of this seems very...you know, {i}Christmassy{/i} to me."
    s "Yeah. Bathing suits aren’t normally a thing I associate with that holiday. But I’m open to changing that if everyone else is on board."
    m "Can you maybe tone down the insatiable lust for a moment while I figure out what we’re supposed to do?"
    s "Sure. Am I allowed to have sex with Ayane again?"

    scene beachmasintro9
    with dissolve

    m "Uhhhhhh...no. "
    ay "I think it would be best for all of us if we could make a one time exception."

    scene beachmasintro10
    with dissolve

    m "How would that be best for me?"
    ay "Because you’d get your peace-and-quiet slash lonely pondering time and Sensei and I could finally relieve ourselves of the pent-up feelings we’ve been keeping in for {i}your{/i} sake alone."
    ay "Well, that {i}I’ve{/i} been keeping in for your sake alone. Who {i}knows{/i} what Sensei does behind closed doors?"

    "You do. I literally told you just the other day."

    m "I’ll take a little extra noise over the greater chance of an apocalyptic meltdown and the mental image of whatever sorts of ungodly things you two would do to each other."
    ay "I don’t know. That sounds a little bit like jealousy to me, Maya."

    scene beachmasintro11
    with dissolve

    m "You’re disgusting."
    s "Hey. Those words are supposed to be for me."

    scene beachmasintro12
    with dissolve

    m "Do you really intend to side with Ayane over me in regard to all of this?"
    s "I didn’t even realize there were actual sides yet considering all you’ve done is think. At least Ayane’s plan will get our minds off of stuff. "
    m "We do not have the {i}time{/i} for-"
    ay "Actually, if we {i}did{/i} go back in time and this is all happening prior to Halloween, we {i}would{/i} have the time to goof off for a little while!"
    ay "Maybe. "
    ay "Or we could all die. I never really know anymore."
    s "Maya, can I weigh in without the fear of you yelling at me?"
    m "I can neither confirm nor deny the possibility of that."
    s "Well, I’m going to do it anyway."
    s "I think Ayane is right. I think the best thing we can do right now is just play it cool and not think too much about any of this."

    "There’s also someone I should probably clear things up with if I’m ever able to track her down..."

    s "Point is, we’ll learn a lot more about what’s going on from the other girls than we will from each other. "
    s "And honestly, I need a break following the Dorm Wars. You might not believe it, but all of that attention is actually very exhausting for me."
    m "Yeah, I don’t believe that at all."

    scene beachmasintro13
    with dissolve

    m "But...fine. It does seem like that is the only reasonable course of action for now. But only until we get some sort of lead or...idea of what could have possibly happened."
    ay "I can’t tell if you’re actually paranoid or if you’re just really excited that different things are finally happening in a life that has been extremely repetitive thus far."
    ay "It’s cute. Like you’re trying to be a detective or something."

    scene beachmasintro14
    with dissolve

    m "Ayane, I say this with the utmost sincerity."
    m "Fuck you."
    ay "Now you’re just jealous again because Sensei wants to hang out and relax instead of going all {i}film noire{/i} at the beach with you and discovering the secrets of the universe underneath the stars."

    scene beachmasintro15
    with dissolve

    m "Is it just me or is she actively going out of her way to try and egg me on today?"
    s "I think she’s just fed up with your ingrained need to be controlling."
    m "You think I’m controlling?"
    s "Either that or certain information that was recently revealed to her has somehow made her reevaluate the nature of our relationship. I think it could go either way."
    m "I am not {i}controlling.{/i} I am just smarter and more experienced than you."
    ay "{i}Are you,{/i} though?"
    s "Okay, I think it was the latter of the two things I said. "
    ay "It was a little of both."
    m "I have no idea what is going on. But, before this meeting is adjourned and we split apart to go “act natural” or whatever it was, I have a demand. You know, since I’m so “controlling” and whatnot."
    s "Uh-huh. And that demand is?"
    m "Take me on a date tonight."

    scene beachmasintro16
    with dissolve

    ay "What?"
    s "{i}What?{/i}"
    m "A date. You do know what that is, correct?"
    s "I do, but..."
    m "But what? Is there an issue?"
    s "There are...several. But I figured the fact that Ayane is right there would have been-"
    m "If I had waited any longer, she would have asked you the same thing I did. "
    ay "You’re right...I was just about to ask..."
    m "See? This way, {i}I{/i} win and {i}she{/i} is now the one who is jealous."

    scene beachmasintro17
    with dissolve

    m "Take that, nerd. Thank you for the suggestion that we all utilize our time for the sake of “fun.”"
    s "Uhh..."
    m "Does 8:00 PM sound okay?"
    s "Uhh-"

    scene beachmasintro18
    with dissolve

    m "Wonderful. I’ll see you then."
    s "Wait. Just to clarify, this {i}does{/i} mean what I think it means, right?"
    m "Probably not. But you’re going to think whatever you want to regardless of my response to that. And to that, I say this."
    m "Screw you guys. I’m going to find a melon."

    scene beachmasintro19
    with fade

    m "Oh, and if we actually did somehow go back in time and the second annual Dorm Wars has yet to begin, please make sure Tsuneyo doesn’t participate in stand-up comedy again. That was revolting."
    s "You’re just going to ask me out on a date and leave?"
    m "Yes. That was the climax of our conversation and everything after that will be boring. So I am going to find a melon. Please stop talking to me."
    s "Maya-"
    m "Walking away."

    scene beachmasintro20
    with dissolve

    s "..."
    ay "..."
    s "She shut you up really quick, didn’t she?"
    ay "I didn’t think she was going to come out and just...openly invite you on a date."
    s "Well, it {i}was{/i} more like a demand. But yes, that’s never really happened so...directly before."

    scene beachmasintro21
    with dissolve

    ay "What...{i}are{/i} you two, exactly? Because at first I thought you were secretly seeing each other...and then I changed my mind...and then I thought that {i}again.{/i} And {i}then{/i} you showed me the list and..."
    ay "That was an accurate list, right? You didn’t...maybe forget to add anyone amidst the sea of other girls you’ve been seeing alongside me?"
    s "I’ve never so much as touched Maya."
    ay "But...if you were given the opportunity...which it very much sounds like you will be tonight..."
    s "..."
    ay "..."
    s "I don’t really know if I’d even be {i}able{/i} to."
    ay "That sounds...complicated."
    s "Yeah..."
    s "It really is."
    to "Yasu?"

    scene beachmasintro22
    with fade

    to "What are you doing over here? Didn’t you require my assistance putting your floaties on?"
    ya "I remembered the way water feels when it slides off of my skin and it dragged me closer to the darkness. I’m sorry for betraying your trust."
    to "You haven’t betrayed me at all. I just find it rather concerning seeing you over here...leaning up against a wall as one of our classmates and our teacher engage in what is very obviously a private discussion."
    to "If I didn’t know any better, I’d take you for some sort of peeping tom or eavesdropper."
    ya "Voices bounce off of the water, Touka. Words slip off of them the way {i}it{/i} slips off of me. And sometimes, slipping shows you more than anything else ever could."
    to "Right...and in terms that someone unfamiliar with your ideology would understand?"

    scene beachmasintro23
    with dissolve

    ya "The vines still grow in places we thought they died."
    to "Why are you doing that with your face? Stop it. It’s unbefitting of a lady."
    ya "I am not a lady. I am a droplet of water gliding across the surface of inflated plastic. A blade of grass with holes drilled into it by the mandibles of a grasshopper."
    to "{i}Noooo...{/i}You are Yasu Yasui. A young lady who needs to put her floaties on so she does not drown when she absentmindedly walks too far out into the water."

    scene beachmasintro24
    with dissolve

    ya "And if I tell you I am already happily submerged?"
    to "I would respond with the fact that, whether it be intentional or not, you can be extremely unsettling at times and I really wish you would let me take you to the doctor."
    ya "The only doctor I need is Him."
    to "And yet I question {i}His{/i} qualifications as you grow more and more worrisome by the day."

    scene beachmasintro25
    with dissolve

    to "Come! We only have until the end of Christmas to enjoy our time here!"
    to "Though...I suppose we could always use one of my family’s private beaches if- oh, you get the point. Now, come!"
    ya "He’s here."
    ya "He is on the beach."

    scene black
    with dissolve2
    stop music fadeout 8.0

    $ renpy.end_replay()
    $ beachmas1 = True
    $ maya_love += 1
    $ ayane_love += 1

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump beachmas2

label beachmas2:
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
y "You know what I’m talking about."

    if nodokaspecial15p3 == False:
        y "It’s one thing to just sit there with your dick in your hands while a girl gets harrassed — a {i}shitty{/i} thing, I’ll add — but letting that happen to someone you {i}know?{/i}"
        y "Someone you’ve been actually pretty fuckin’ decent to recently?"
        y "Was that all just for fun? "
        y "Did you ever actually want me to get better? Or was that all just some kind of sick game to you?"

    else:
        s "I don’t have an excuse, Yumi."

        scene endofsecondwar41
        with dissolve

        y "Yeah, how the fuck {i}could{/i} you?!"
        y "What kind of shit do you think you can just say to make it feel like none of that ever happened?! Because if there’s some sorta miracle cure you think you can pull outta thin air, I’d love to hear it!"
        s "Yumi-"
        y "I was finally starting to trust you! I thought you were on my side!"
        y "All that shit with...helping me get a job! Helping me study! Genuinely fucking apologizing for the shitty things you’ve done to me! Was that all fake?! Some kind of plot to get me undressed?! To corner me?!"
        y "Is this just a game to you?! Am I a plaything?!"

    s "Nothing about that was or {i}is{/i} a game. I told you back then that I was just as surprised as you."

    scene endofsecondwar42
    with dissolve

    y "Then why?..."
    y "Why did you just freeze?"
    y "You're a fucking {i}adult...{/i}"
    s "..."
    y "Why didn’t you stand up to her?"
    s "Because I didn’t know {i}how...{/i}"
    y "..."
    s "..."
    s "Or maybe some part of me didn’t want to. "
    s "I don’t know."
    y "..."
    s "I’m disgusting, Yumi. "
    s "You know it. I know it. Everyone knows it. It’s not like I try to keep it a secret."
    s "And I’m not just talking about forcing myself on you either. I’m talking about {i}everything.{/i}"
    s "Do you have {i}any{/i} idea how many times I’ve gotten off while thinking about you? Because the number would make you sick."
    y "Why...are you telling me this? That’s not why I-"

    play sound "static.mp3"
    scene endofsecondwar43
    with flash
    stop sound

    s "Because lying to you doesn’t work. And I’m sure you don’t {i}want{/i} me to lie to you either."
    s "I don’t {i}know{/i} why I froze. But I did. And I can’t go back in time and change that, just like I can’t go back in time and change when I kissed you."
    s "Or, I don’t know. Maybe I can. But I don’t {i}want{/i} to because it’s those things that brought us here."
    s "And even if this world is fucked beyond belief and I’m going to repeatedly destroy any hope you’ll ever have in me, I can’t change."
    s "I {i}won’t{/i} change."
    s "But {i}you{/i} will."

    play sound "static.mp3"
    scene endofsecondwar44 with flash
    stop sound

    s "If you want to keep staying away from me, that’s fine. I don’t blame you. "
    s "You’ve already given me multiple chances to redeem myself and I’ve squandered every single one of them."
    s "You can’t trust me. "
    s "You were an idiot for ever {i}thinking{/i} you could trust me after all I’ve done to you."
    s "And the most disheartening part of all of that is I can’t even remember some of it."

    play sound "static.mp3"
    scene endofsecondwar45 with flash
    stop sound

    s "Or maybe I can...but I {i}don't.{/i}"
    s "Maybe I just {i}choose{/i} not to remember because of the way it makes me feel."
    s "But I’d do it all again in a heartbeat because that’s just who I am."
    s "Never count on me."
    s "Never believe in me."
    s "{s}And run away while you still can.{/s}"
    y "But why?..."
    s "Why what?"

    play sound "static.mp3"
    scene endofsecondwar46
    with flash
    stop sound

    y "Why are you telling me this {i}now?...{/i}"
    s "..."
    y "..."
    ay "Uhh...Sensei?"

    scene endofsecondwar47
    with fade

    ay "I think we’ve got a bit of a problem..."

    $ renpy.end_replay()
    $ dormwartwo19 = True

    play sound "eggcrack.mp3"
    scene black

    jump beachmas1
...
```