# The River Styx (Yasu)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Things That Hurt](./nodokaspecial15p3.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: yasuspecial20
* Group: Yasu
* Triggered by label: nodokaspecial15p3
* Chain sources: nodokaspecial15p3
* Chain sources path: nodokaspecial15p3

## Official wiki page

[The River Styx](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yasuspecial20&go=Go) for more details.

## Event code

File: (install folder)\game\YasuEvents.rpy

Code:
```python
...
label yasuspecial20:
    scene calmbeforethestorm1
    with dissolve2
    play music "phantomthief.mp3"

    "I find myself in my office after what could only be referred to as...one of the most {i}interesting{/i} nights of my new life thus far."
    "Not interesting in the way that involves dodging the end of the world with two of my niece’s closest friends, though."
    "Interesting in the fact that someone other than me was finally able to get Yumi to crumble, albeit in a much more...intentionally cynical and harmful way than my underlying compulsions of the past."
    "What that means for the future, I have no idea. Which is probably why I’ve taken it upon myself to seek shelter in here and let Imani handle homeroom for the day."
    "Even if my current thoughts on Nodoka are a bit “off” compared to how they were last week, I still don’t think I want to watch her get murdered."
    "And I can’t say I want to see Yumi, a girl that I feel I’ve been genuinely helping in many ways lately, throw all of that away because I preemptively got to see her naked."

    if nodokaspecial15p3 == True:
        "Naked and...attempting to pleasure herself while I looked on and did nothing, sure. "
        "But, like Nodoka said back then...that was going to happen eventually, right?"

        s "..."

        "I don’t know. Maybe I’m just grasping at straws in hopes of being able to pull myself out of the River Styx."
        "But seeing as I’m already on my way to Hades, I should probably just shut up and drown myself in its waters already."

    "Either way, the safest place for me right now is behind these doors."
    "For when I tear myself away from the harsh rays of the sun and slink back into the dark, I am somehow at my brightest and warmest."
    "And there is nothing that can or {i}will{/i} take that away from me."

    play sound "knock.mp3"

    to "Sensei, are you in there right now?"
    s "..."

    "I think for a moment that remaining silent will create one more barrier between what goes on out there and me."
    "But as a master of second guessing myself, I tear the barrier down in hopes that someone else will build one in my stead. "
    "And that the person at my door is only here to slink into the dark with me."

    s "Yeah..."
    s "I’m here."

    play sound "dooropen.mp3"
    scene calmbeforethestorm2
    with dissolve

    to "Wonderful. Please do something about Yasu."
    s "That’s a vague demand, but I think I get it."
    to "You do? So you’ve already been informed that she refuses to set foot in the classroom today?"
    s "I meant “get it” in the sense that there are many things that should probably be done regarding Yasu’s well being, but no. That is not something I was aware of."
    to "Well, now that you have been made aware, I will take my leave and pawn the rest of this problem off on you."
    s "But dealing with Yasu is {i}your{/i} thing. The last time I tried to do anything for her, she..."
    to "..."
    s "..."
    to "She what?"
    s "I just realized I should probably keep that to myself. "

    scene calmbeforethestorm3
    with dissolve

    to "Sensei, I have already agreed to assist Ms. Watabe with cleaning up the archery range this morning and can not afford to be late to something I {i}personally{/i} assured her I would be on time for."
    to "I may be Yasu’s current caretaker and...probably her legal guardian as well, but you are her teacher. Which means it is {i}your{/i} job to get her to go to class."
    s "Okay, sure. But what if {i}I{/I} was also planning on not going to class today?"

    scene calmbeforethestorm4
    with dissolve

    to "Did you hear that, Yasu? You get to spend the whole day in this delightfully drab room with Sensei. Oh, how fun."
    s "Touka-"

    play sound "dooropen.mp3"
    scene calmbeforethestorm5
    with dissolve

    to "Farewell! I have things to do and places to be!"
    to "And if she tells you she does not have lunch money, she is lying."
    ya "To lie would be one step short of a cardinal sin. I can not lie, for I have already incurred more of His wrath than I am able to handle."

    "Welp, I guess this is a thing I am dealing with now."
    "Here’s hoping she doesn’t climb on top of anything and start speaking in tongues again."
    "Though, I suppose if she’s going to have an orgasm anywhere in the school building, this is probably the safest room to do it."

    s "So...what’s going on? Why aren’t you going to class?"

    scene calmbeforethestorm6
    with dissolve

    ya "There are some doors that must remain closed. For the more people that set foot inside the areas they conceal, the closer those doors come to disappearing entirely."
    s "Can you say that again, but without the cryptic metaphor?"
    ya "Something bad is going to happen today."
    s "Something bad happens almost every day. But, based on what I experienced yesterday, you’re probably right."

    "How she can sense this beforehand is another question entirely, though."

    ya "This is different."
    ya "This is not His word, but the word of the world itself."
    ya "It speaks through the wind, backwards and under the cover of the shadows. The same language the cicadas speak. "
    s "Right. And how long have you been able to speak to bugs?"

    scene calmbeforethestorm7
    with dissolve

    ya "Bugs are my friends."
    s "Well, I don’t know what your friends told you, but premonitions aren’t really a viable excuse for not going to class."
    s "Besides, if you try to live your entire life avoiding confrontation, what are you going to do when said confrontation becomes unavoidable?"
    s "Face your fears now so they’ll be less scary later. Also, don’t you have, like...divine protection or whatever?"

    scene calmbeforethestorm8
    with dissolve

    ya "..."

    "Yasu grows silent (Something I can rarely say when I am alone with her) and stares at the corner of the room."
    "I imagine she’s mentally sorting through memorized religious texts pertaining to which sin “conflict” is and-"

    ya "I have not heard His voice since you last left my room."
    ya "I believe He is angry with me. But I do not understand what it is I did that would have angered Him."
    s "..."

    scene calmbeforethestorm9
    with dissolve

    ya "That...That is why I can not go to class!"
    ya "I will not know what the bad thing is until it happens! And if I am the one endangered and something bad happens to {i}me,{/i} what will become of Him when His voice returns?!"
    ya "It is my duty to protect the world! Mine alone! I can not do this if I am forced off of this plane before I am ready to leave!"
    s "You really can’t think of anything you did that would have angered your god?"

    scene calmbeforethestorm10
    with dissolve

    ya "All I remember about that night is the feeling of His warmth as it flooded my undeserving body. An outpouring of holy pleasure that I-"
    s "Okay, yeah. Let’s just leave it at “an outpouring of holy pleasure” and not think any more about it. "
    s "That night aside, though, I can’t imagine there is anyone in class that wants to hurt you, Yasu."
    s "You may be weird, but I don’t think you have any enemies. So if anything bad {i}were{/i} to happen, which it probably will, I doubt you’d be directly involved."
    s "I guess that {i}would{/i} call into question why the...wind and bugs informed you about it, though."

    scene calmbeforethestorm11
    with dissolve

    ya "The world did not speak to me directly- it was conversing with itself. Speaking alone for it has no one else to talk to. "
    ya "How lonely it must be to be the last of your kind."
    ya "I have felt the urge on many occasions to try and speak back to it, but I worry of what God would do to me if I shared my inner voice with anyone but Him."

    "I sigh to myself and try to figure out how I am going to deal with an entire day's worth of this."
    "It dawns on me after a moment or two of quiet contemplation that such a feat is impossible, and that this is probably why I have a student teacher in the first place. "
    "If I can get Yasu back to class, I can pawn the responsibility off on her and then leave before anyone is killed and go back to spending my time alone."
    "It’s not the most responsible of strategies, but it’s the easiest and least likely to result in a bout of mental exhaustion that will put me out of commission for the entire weekend."

    s "You have to go back to class, Yasu."

    scene calmbeforethestorm9
    with dissolve

    ya "But...the bad thing!"
    s "I’m sure that whatever “the bad thing” is will come to pass."
    s "At the very least, Imani and Makoto will be able to handle it a lot better than I can."
    ya "But-"
    s "No excuses. Go."
    ya "But-"
    s "Yasu-"
    ya "But I don’t know which way the classroom is!"
    s "What? You’ve been here for months."
    ya "Touka always grabs my collar and pulls me to where I am supposed to be. Without her, I am nothing. A worthless, discarded husk of a human- stuck to the side of a fence and waiting for the wind to blow me away."
    s "Ugh..."
    s "Fine. I’ll walk you back. But I’m not hanging around for long, got it?"

    scene calmbeforethestorm11
    with dissolve

    ya "Yes. Thank you. "
    ya "I am sorry for filling your day with these wasted words of mine that do less for your mind than the act of watching paint dry."
    s "That sounds like something you’d be into, given your tendency to stare at walls and whatnot."
    ya "I do not stare {i}at{/i} the walls. I stare {i}through{/i} them."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Okay. It’s time to leave."
    ya "Wait! My collar! "
    s "I’m not grabbing your collar, Yasu. It will make me look bad."

    "........."
    "......"
    "..."

    scene calmbeforethestorm12
    with dissolve2

    s "..."
    ya "..."
    s "Is the world speaking to you again?"
    ya "It speaks, but I can not discern the words."
    ya "Its tone is one of excitement...like it is anticipating what will soon befall us."
    ya "But what reason would one have to look forward to something that both sounds and feels like a bed of heated nails?"
    s "Some people just...like watching the world burn, I guess. "
    ya "The world is not who will burn. It is all of us who live inside of it that will."
    s "Well, at least we get to die together. That’s a plus, right?"
    ya "There is no death. Just-"

    scene calmbeforethestorm13
    with dissolve

    s "Oh, look. We’re here. And not a second too late."
    s "It’s been fun. But I’ll see you later, Yasu. Tell Touka that the next time she wants me to do her dirty work, she should-"

    scene calmbeforethestorm14
    with dissolve
    stop music fadeout 20.0

    ya "Wait. You have to come inside."
    s "That was not the deal."
    ya "The deal was that you will not hang around for long. You have not done any hanging at all."
    s "Does this not count as hanging?"
    ya "I am not an expert, but I don’t think it does."
    s "..."
    ya "..."
    s "Five minutes."

    scene calmbeforethestorm15
    with dissolve

    ya "Yay! Praise be!"

    scene black
    with dissolve2
    play sound "slidedoor.mp3"
    play music "10c.mp3"

    "Well, somehow or another, it looks like I have failed the only goal I put in place for myself today."
    "I slide the door open for Yasu in an attempt to let her in first. However, still being a little...uneasy about the fact that she’s about to come face to face with “the bad thing,” she clings to my arm for support."
    "And while walking into the class with anyone {i}else{/i} around my arm would probably be cause for concern, I can’t imagine it will be much of a problem with Yasu."
    "People will probably just see her without Touka and think that she needed some other body to absorb the life force of or something."

    scene calmbeforethestorm16
    with dissolve2

    f "..."
    ya "..."
    s "..."

    "Strike that."
    "If even {i}Futaba{/i} is looking at us with an air of skepticism about her, I’m sure it’s only a matter of time until someone else points this out as well."

    f "Umm..."
    s "If it helps clear the air at all, I didn’t want this either."
    s "Yasu is worried that something bad is going to happen today and...I guess she thinks I can protect her from that?"

    scene calmbeforethestorm17
    with dissolve

    f "Something bad? Like...what, exactly? It’s seemed like a mostly normal day so far."
    ya "Something that will shake the foundation of all that we know to its very core...An undeniable, horrible turn of events that will flip the world on its head, pouring all of us into the abyss in the process."
    ya "You should run while you still have the chance. You should wrap your arms around those you cherish and escape to an area outside the grasp of the sky’s mighty tendrils-"
    ya "For the moment they begin to extend in your direction, it is already too late. "
    ya "We are already doomed."
    s "So, yeah. This has been my morning so far."
    f "I’m...beginning to understand why you left Miss- Uhh...Why you left Imani in charge of the class."
    no "These...{i}tendrils{/i} that you speak of..."
    no "Can you tell me more about them?"

    $ renpy.end_replay()
    $ yasu_love += 1
    $ yasuspecial20 = True

    jump nodokaspecial20
...
```

## Code that triggers this event

File: (install folder)\game\NodokaEvents.rpy

Code:
```python
...
scene thematador24
    with dissolve2

    y "..."
    s "..."
    y "..."
    s "..."

    scene thematador25
    with dissolve

    "Yumi leaves the room without saying anything to me."
    "She doesn’t need to."
    "The way she looked made her feelings clear enough."
    "When I turn around to watch her leave, I step on the shards of a broken cellphone and almost slip because of it."
    "I kind of wish I did."
    "For even though I did not intend to hurt anyone tonight, my inaction spoke volumes in reminding her of who I really am at the end of the day."
    "I’m not someone who cares."
    "I’m not someone who’s here to help her succeed."
    "I’m just {i}someone.{/i}"
    "And she deserves a little more than that."

    scene thematador26
    with dissolve

    no "Why the solemn gaze? You’re the first person to ever ejaculate on me. You should be smiling."
    s "Why did you do that?..."
    s "Since when are you the type of person who blackmails someone?"
    no "Since when do you care?"
    no "You got what you wanted. I got what I wanted. Isn’t that really all that matters?"
    no "You know better than anyone that sometimes people need to be hurt in order for others to benefit. Today, {i}we{/i} are those beneficiaries."
    no "So what if {i}Yumi{/i} suffers after all the suffering she’s put other people through? This is sure to do more for her future cooperation than any detention or stern lecturing would."
    s "She was already {i}changing,{/i} though. She’s come a long way since I’ve met her. And she’s already apologized to Futaba and-"
    no "That’s not good enough."
    s "What?"
    no "I said that’s not good enough."
    no "This likely won’t come as a surprise, but there aren’t many people I care about in this world."
    no "And while one of the main reasons for that is that there just aren’t many people who {i}interest{/i} me, a {i}second{/i} main reason is that it’s just far too exhausting."
    no "You see, I {i}protect{/i} the people I care about. And sometimes, protecting someone means cutting down the person they must be protected {i}from.{/i}"
    no "And other times, if that person doesn’t {i}need{/i} protection anymore, I simply...avenge them instead."
    s "I don’t think Futaba wanted revenge."
    no "She didn’t."
    no "But I did."
    no "And so I got it...because I am a freethinking, powerful girl who takes what she wants {i}when{/i} she wants it."
    no "If doing that means hurting someone that matters less to me than the dirt I walk on, I really don’t care."
    no "All I have to lose is the favor of others. "
    no "That said, do {i}you{/i} think any less of me now?"
    s "Would you care if I did?"
    no "Of course. If I didn’t like you, I wouldn’t have let you cum on my face. "
    s "I..."
    s "I don’t really know how I feel."
    no "I think the fact that you {i}don’t{/i} know just confirms that your opinion of me hasn’t changed at all."
    no "If you can watch me engage in something as morally reprehensible as blackmailing someone into masturbating and then fellating the person they like in front of them...and {i}not{/i} be mad about it-"
    no "Well, let’s just say most traditionally “good” people would put their foot down then and there."
    no "But you let it happen. Albeit with a few “No, stop”s sprinkled in. But I think that was just you doing your best impression of someone with a moral compass."
    no "The truth is that you only feel bad about certain things because you think that you’re {i}supposed{/i} to feel bad."
    no "Why not just live your life surrounded by the people you care about? Why not build a moat to keep everyone else out?"
    s "..."
    no "..."
    s "Isn’t it lonely keeping everyone else out?"

    scene thematador27
    with dissolve

    no "Not to me."
    no "But I suppose we should end things there for today. Especially since I now need to take a {i}second{/i} shower when I just took one a couple hours ago."
    no "Hopefully, your relationship with Yumi isn’t {i}too{/i} badly damaged based on what just happened. It would be a crying shame if you had to live the rest of your life without seeing her tits again."
    no "Fortunately, I believe all of her anger is directed at me right now. And that you should be okay for the immediate future."
    s "What about you, then? Aren’t you worried about what she’ll do to get back at you?"
    no "Right now? Not really."
    no "Right now, all of my serious thoughts are blocked by the intoxicating scent of your cum. "
    no "Thank you for that, Sensei. I’m sure my dreams tonight will be spectacular."
    s "I think the fact that you can sleep at all is something to be proud of."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Nodoka and I walk out of the locker room together."
    "We walk back to the dorms together. "
    "And all the while, we somehow manage to not despise each other’s presence despite the constant entanglement of our shadows and our thoughts."
    "When she returns to her room, she takes a piece of me with her."
    "When I return to mine, I take a handful of sleeping pills. "

    $ renpy.end_replay()
    $ nodokaspecial15p3 = True

    "{i}Nodoka’s affection has increased by 5!{/i}"
    "........."
    "......"
    "..."

    $ day = 5
    $ totaldays += 1

    hide thursday onlayer date
    show friday onlayer date

    jump yasuspecial20
...
```