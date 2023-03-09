# The Yellow Wallpaper
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach6&go=Go)


Part of event chain [The Next Best Thing](./secondbeach5.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: secondbeach6
* Group: Main
* Triggered by label: secondbeach5

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach6:
    scene ocean
    with dissolve
    play music "icantseeher.mp3"

    "I walk in a strange pattern to avoid the introduction of sand to the insides of my shoes."
    "It’s one of the least satisfying sensations of all."
    "I’m not quite sure where Molly ran off to, but I can only assume that it was somewhere to hide her tears."
    "Perhaps a linen closet or the arms of a close friend. "
    "A close friend other than Rin, that is- since I imagine Molly’s currently fighting back her desire to at least {i}attempt{/i} tongue wrestling her before she has the chance to have her heart broken later."

    if bonus == True:
        "I become slightly erect at the thought of the two of them kissing."
        "Then become completely erect at the thought of Otoha joining in."
        "Then somehow less erect when I add myself into the mix."
        "But that’s probably due to the fact that, at that point, it would become less of a pleasurable act and more of a test to see how I’d handle things in that situation."
        "It seems like too much to focus on and would likely detract from the activity."
        "It’s not like any of those girls would prioritize me anyway, so this is one of the worst fantasies I could have concocted during this spur of the moment stroll down soon-to-be-memory lane."
    else:
        "Man, it's going to be so sad when Molly has her fragile Irish heart broken."

    "At least it’s getting a little warmer, though."
    "Which is strange given the fact that it’s getting later in the day and the tint of the sky has not changed even the slightest."
    "Kumon-mi is weird. Weather is weird."
    "Everything is weird. Everyone is weird."
    "I keep walking until I find someone less weird."

    scene nodokaispretty1
    with dissolve2

    "Or at least that was the plan."
    "Despite how many similarities I share with the character before me, I’d be a fool to not throw her into the “weird” category with...basically everyone else."

    if bonus == True:
        "Which essentially means I’d have to lump myself in there with her-"
        "But I guess I’m not opposed to being locked in a confined space with a girl like her when she’d likely only require some light coercion to jerk me off in a public bathroom."

        no "Are you preparing to mount me, Sensei?"
        no "I am primed and ready. Though, I regret to inform you that it was far too cold for me to remain in my swimsuit for the rest of the day."
        no "Also, your loyal {i}helper{/i} seemed quite opposed to the idea."
        no "She informed me several times as I was attempting to unzip her pants."
        s "You just have to try a little harder. Makoto caves once the pressure gets going."
        s "And you’re a lot like me, so I doubt she’d be entirely opposed to the prospect."
        no "A lot like you, but in a much cuter package and harder to please."
    else:
        no "Are you preparing to  hug me, Sensei?"
        no "I have heard through the grapevine that my ability to teleport short distances makes me an exceptionally difficult hug target."

    s "Is that a challenge?"

    scene nodokaispretty2
    with dissolve

    no "Are you the type who likes being challenged from time to time?"
    s "Not really, no."
    no "I didn’t think so."

    scene nodokaispretty1
    with dissolve

    no "What brings you over here?"

    if bonus == True:
        no "I half expected you to be fist deep inside of my roommate by now, knowing your powers of seduction."
        s "Nah. Otoha just wanted to talk about lesbian stuff."
        no "Without me? How rude."
        no "I presume it was about Rin?"
        s "No. She’s in love with you and was asking for advice on how to get into your pants."
        no "Lies. Otoha knows that all she’d need to do is ask if she truly wanted something like that."
        s "Are you just sexually attracted to everyone? Or..."
        no "Are you?"
        no "At the end of the day, I still lack any real form of sexual experience."
        no "I’m just a rather curious girl with an insatiable appetite for new happenings."
        s "Then I’d like to propose that the two of us venture forth to a public bathroom and I put an earlier thought of mine to the test."
        no "Are there no janitorial closets available?"
        s "I’m sure we can find one if we try hard enough."
    else:
        s "Oh, you know. Just enjoying the feeling of the sand against my...shoes."

    scene nodokaispretty2
    with dissolve

    if bonus == True:
        no "Oh dear. Any more of that and I’ll have to change my underwear. "
        s "Can I take your sarcasm as a yes? Or are you going to send me wandering down the beach walking in an even stranger fashion than I’ve already been walking in?"
        no "Are you afraid of the sensation of sand in your shoes as well?"
        s "I wouldn’t say I’m {i}afraid{/i}. It just kind of sucks."
        no "I see."
        no "I suppose I could stop reading and go on a bit of a journey with you."
        no "Though, something tells me that our first true sexual exploit as a duo is a bit further off."
        s "I feel like we can very easily change that if we’re both up for it."
        no "Can we?"
        no "Is fate truly something so moldable? Or are you the type to believe that it follows a pre-ordained chain of events to some extent?"
        s "I really don’t care. I just want to have sex."
        no "With me?"
        s "Yes, Nodoka."
        no "Why is that?"
        s "Because I find you attractive and think you’d be fun to have sex with. What more do you want?"
    else:
        no "I see."

    scene nodokaispretty3
    with dissolve

    no "Did you know that in ancient times, it wasn’t uncommon for men to be romantically involved with both men {i}and{/i} women?"
    no "And while many of the male on male relationships were sexually exploitative in nature, they weren’t exactly frowned upon until much later when it started becoming a little more...well known."
    no "Women, however, were never as open to the prospect of bedding other women as they were deemed further away from godliness than that of a man."

    if bonus == True:
        no "I think one of the reasons so many women are sexually experimental and more open to the prospect of fingering each other now than they used to be is that they’re making up for lost time."
        s "Cool. Can we have sex now?"
        no "Hmm..."
        no "No."
    else:
        s "Hey. {i}I{/i} am the teacher. Stop teaching me things."
        s "Can we just hug now so I can get back to feeling things through my shoes?"

    no "But we can take a walk if you’d like."
    s "I don’t understand you."

    if bonus == True:
        no "Of course you do. You just aren’t used to having to confront someone so philosophically identical."
        no "What joy would there be in using {i}now{/i} as our first experience with one another when {i}now{/i} seems like such a standard and unexciting choice?"
        no "Wouldn’t something like that proceed to skew our sexual perception of one another to the point where we no longer {i}want{/i} to have sex under standard conditions?"
        no "I’m playing the long game here, Sensei."
        no "Also, you have not accumulated anywhere near the correct amount of Nodoka points."
        no "There is a high price on my V-card, good sir."

        "In some ways, Nodoka is even worse than Uta when it comes to teases like this."
        "But that’s because Nodoka’s obnoxious enough to make it seem like it’s actually a feasible possibility before going off on tangents of...bisexual history or whatever point she was trying to get across just now."
        "And yet, I’m still not finding myself annoyed {i}enough{/i} to wander off in search of someone more likely to swallow my semen."
        "Probably because she’s here now while everyone else is still up in the air- and waiting for any of them to float back down to earth sounds a bit too boring for my liking."

        s "So, to clarify, you will go on a walk with me...but that walk will not result in any act of intimacy?"
    else:
        no "Nobody does. But that's okay because the world is going to end soon anyway."
        s "So, to clarify, you will go on a walk with me...but that walk will not result in a hug?"

    scene nodokaispretty4
    with dissolve

    no "I’d be open to the prospect of watching you [masturbate], if that’s something you’d be interested in."
    s "That’s a bit too humiliating for someone like me. "
    no "Would you like to watch me [masturbate] instead?"
    s "Are you actually going to? Or is this just another personality probe?"
    no "Don’t know. Hard to say without seeing where the wind takes us."
    s "You’re so fucking weird."
    no "As are you. Now, help me up. My legs appear to have fallen asleep."

    if bonus == True:
        no "And if you decide to mount me instead of actually lending your aid, please keep it to soft grinding only as these are my favorite leggings and I do not want them destroyed."
    else:
        s "Oh no. However will you dance with sleeping legs?"

    scene black
    with dissolve2

    if bonus == True:
        "I help Nodoka up (Without mounting her) and she takes a moment to regain her footing."
    else:
        "I help Nodoka up and she takes a moment to regain her footing."

    "Even though her legs are wobbling like that of a newborn deer, she’s careful to not remove her finger from its place in her book."
    "Using my master level of deductive reasoning, I half-confirm in my mind that this is either an important book to Nodoka or one that she’s reading for the first time."

    if bonus == True:
        "Why I’m thinking of this instead of what she looks like underneath the layers of winter clothing, I don’t know."
    else:
        "Why I’m thinking of this instead of what it would feel like to hug her, I don't know."

    "But something inside of me feels compelled to ask."

    scene nodokaispretty5
    with dissolve2

    s "Nodoka."
    no "Yes, my love?"

    if bonus == True:
        s "Are we dating now?"
        no "So long as you don’t mind me seeing other women."
        s "Can I be involved in the event that you do?"
        no "Not every time, but I’ll be sure to include you in a fair deal of my experiments."
        s "Wait, stop. I’m getting distracted. I was about to ask you something."
        no "Were you now?"
        s "Yeah. Just about whatever it is you’re reading, though."

        scene nodokaispretty6
        with dissolve

        no "Oh? I have to say, I’m a bit surprised that you were willing to stray away from the topic at hand when I was certain it was your favorite one."
        s "Having an erection is just a burden when I know it won’t end up inside of anyone."

        scene nodokaispretty7
        with dissolve

        no "And here I was ready to offer you a pity handjob."
        no "There’s no point if it’s not inside of me, though, so I won’t bother."
        s "You are my new least favorite student."
        no "I love you too, darling."
        no "What I’m reading today isn’t all that exciting, though. "
        no "It’s just a collection of short stories I’m rereading for my own personal reasons."
        s "Ah. "
        s "Well, I don’t know much about short stories, so I think this topic is going to fall flat."
        no "I’d highly recommend this one if you’re ever looking to kill six thousand words worth of time."
        s "And what is “this one?”"
        no "The story of a girl forced to spend an unhealthy amount of time confined to a single location."
        no "The onset of hysteria and how isolation itself can be just as deadly a beast as cancer."
        no "It’s called “The Yellow Wallpaper.”"
    else:
        s "First off, don't call me that. Second, I'm just interested in whatever it is you're reading."

        scene nodokaispretty7
        with dissolve

        no "It’s just a collection of short stories I’m rereading for my own personal reasons."
        s "Ah. "
        s "Well, I don’t know much about short stories, so I think this topic is going to fall flat."
        no "I’d highly recommend this one if you’re ever looking to kill six thousand words worth of time."
        s "And what is “this one?”"
        no "The story of a girl forced to spend an unhealthy amount of time confined to a single location."
        no "The onset of hysteria and how isolation itself can be just as deadly a beast as cancer."
        no "It’s called “The Yellow Wallpaper.”"

    scene nodokaispretty8
    with dissolve

    no "How do you think you’d fare in a situation like that, Sensei?"
    no "Being trapped, I mean."
    no "Stuck in one place...unable to venture outside of it."
    s "That’s not really an easy question."
    no "I suppose it isn’t."
    no "Why, that sounds quite familiar to our current situation, doesn’t it?"
    no "If we can not leave Kumon-mi, how can we even confirm if there is a world {i}outside{/i} of it?"
    s "I mean, several of the girls have parents outside of Kumon-mi that they’re in regular contact with. Isn’t that confirmation enough?"

    scene nodokaispretty9
    with dissolve

    no "For some, that would be enough. Yes."
    no "Though, I’m the type of person who has trouble believing anything if I do not see it with my own eyes."
    no "The curse of being a curious realist, I suppose."
    no "If someone is trapped...the most realistic reaction would be for them to attempt to escape, yes?"
    no "And yet some people give up on that entirely."
    no "They fall victim to circumstance and let a horrible reality overtake them when they’re feeling too weak to compete."
    no "‘Tis a shame I tell you."
    no "A god damn fucking shame."
    s "…"
    no "…"

    "Nodoka falls silent for a moment and I can’t really find anything worth adding to the conversation."

    if bonus == True:
        "Even though her story sounds interesting by...short story standards, six thousand words is still time I could be using to crank one out or...asking one of the girls for nudes."
    else:
        "I should read one of those books on how to talk to girls."

    no "Do you have your own room this weekend, Sensei?"
    s "I do. "

    scene nodokaispretty10
    with dissolve

    no "May I see it?"
    s "Do you actually want to see it or are you just fucking with me?"
    no "Why would I be fucking with you?"

    if futabalust15 == True:
        no "I accompanied you to your room during the dorm war and that was a resounding success, wouldn’t you say?"
    else:
        no "It wouldn’t be the first time you’ve taken me to your room during a class-wide event, would it?"
        no "Though, I suppose you might be a little nervous or excited since we’ll be all alone this time."

    s "I mean, I’m fine with taking you there. I just don’t really know {i}which{/i} room is mine, yet."

    scene nodokaispretty9
    with dissolve

    if bonus == True:
        no "Never fear. I may have already gotten that information during a particular strip search earlier."
    else:
        no "Never fear. I may have already gotten that information during a particular yuri police raid earlier."

    s "Your talent is being wasted on all of us, Nodoka. "
    no "Nothing can be called a waste if you have fun in the process."
    no "And, Sensei..."
    no "I’m having a lot of fun all of a sudden."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene nodokaispretty11
    with dissolve2

    w "Oh dear god, no."
    s "Hey, you two. Fancy running into you here."
    os "I honestly forgot you were even going to be at this thing."
    s "Thanks, Osako. I appreciate that."
    w "I was hoping I’d be able to avoid confrontation before going into a self-induced coma for the weekend, but it appears that dream of mine was too good to be true."

    scene nodokaispretty12
    with dissolve

    no "{i}*Sniff sniff*{/i}"
    no "That subtle scent of lilac and earl grey tea..."
    no "You...you really are here..."
    os "Uhhhhhhhhhhhh..."
    w "Do not {i}sniff{/i} me, you mischievous wench. "

    scene nodokaispretty13
    with dissolve

    if bonus == True:
        no "I’m open to threesomes, you know..."
        no "I’ll do anything you want me to..."
        s "…"

        "I bite my tongue and manage to prevent myself from scolding Nodoka for being open to hooking up with a female teacher and not me. "
        "Even though Osako already seems to be aware of my relationship with Ayane and...Wakana has her suspicions as well, incriminating myself like that would probably be a death sentence."
    else:
        no "Let's go charge our iPhones together and talk about bears."

        "I bite my tongue and manage to prevent myself from scolding Nodoka for being open to hooking up her phone with a female teacher and not me. My battery is so low."

    s "Nodoka. Please stop sniffing Wakana."

    scene nodokaispretty14
    with dissolve

    if bonus == True:
        no "In the event that they would like a {i}fourth{/i} participant to even out the numbers, I’d like to rescind my earlier statements regarding the probability of us-"
    else:
        no "But I want to talk about bears with her. How else am I supposed to show that?"

    os "Yeah, no. Hold on a second."

    scene nodokaispretty15
    with dissolve

    os "That’s my girlfriend you’re...inhaling right now."
    no "Hm..."
    no "You touched Miss Watabe without her wincing in disgust."
    no "You two must truly have a deeper connection than I believed at first glance."

    scene nodokaispretty16
    with dissolve

    no "No matter. If you’d prefer to use me as some sort of object or toy instead of an active participant in the bedroom, I’d be open to that as well."
    w "Osako. Do the...karate to her."
    os "It’s not {i}the{/i} karate, babe. It’s just karate."
    os "And I’m pretty sure I could get arrested for hitting someone her age, so...let’s just get to our room so you can take a nap."

    scene nodokaispretty17
    with dissolve

    w "Nagasawa, if you attempt to make contact with me even once before the weekend is over, I will poison you in your sleep."
    no "I’m a reeaaaaaally heavy sleeper, Miss Watabe. You could do all sorts of other things to me as well if you wanted and {i}no one would ever know.{/i}"
    os "Uhh...hi. And bye, I guess."

    if bonus == True:
        os "Please keep your weird pervert friend away from us."
    else:
        os "Please keep your weird friend away from us."

    s "I...will do my best."

    scene nodokaispretty18
    with dissolve

    if bonus == True:
        "Osako pulls Wakana along and the two of them hastily walk down the halls of the inn to the room where I imagine they’ll be quarantining for the weekend on account of a[school]girl lesbian outbreak."

    no "Huh."
    no "You know, I’m going to go out on a limb here and assume that if I still had my swimsuit on that none of this painful rejection would have ever happened."

    if bonus == True:
        no "I have very nice legs. And now they are missing out on a cute, obedient girl in the prime of her sexuality."
        s "Nodoka, harness that energy and take it into {i}my{/i} room."
    else:
        no "I have very nice legs. Like that lamp from A Christmas Story but without the fishnet stockings."

    scene nodokaispretty19
    with dissolve
    stop music fadeout 10.0

    if bonus == True:
        no "But it’s just not the {i}same{/i} with a penis."
        s "How do you know? You have zero experience."
        no "Girls are gentle and delicate like flowers, while you are a torrential downpour looking to flood my insides with your seed when all I want is a light shower."
        s "I..."
        s "{i}What?{/i}"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ secondbeach6 = True
    $ nodoka_love += 1

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "………"
    "……"
    "…"

    jump kirinlust20intro

label kirinlust20intro:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
mi "Yup! Think it was somethin’ Makoto wanted to do to make sure we had enough room for this trip or whatever."
    mi "Can’t actually remember the reason, but I {i}do{/i} remember the three of us were there and it was..."

    scene beachpartyyay30
    with dissolve

    mi "It was..."
    mi "Fun..."
    sa "…"
    mi "…"

    scene beachpartyyay31
    with dissolve

    sa "…"
    mi "…"

    "Two girls in a line on the beach."
    "Seen an undisclosed amount of time before breaking."
    "Could it be tomorrow? "
    "The next day?"
    "The day after that?"
    "A month from now?"
    "A year?"
    "Or perhaps the two of them are already broken."
    "And perhaps they’re not just staring off into the distance right now, but searching the shoreline for the remnants of things they may have lost."
    "Everyone loses something, you know."
    "I bet you’ve lost a fair deal yourself."
    "But how would you compare it to them?"
    "And {i}should{/i} you compare it in the first place?"
    "Two girls in a line on the beach, measuring around the same size as a professional basketball hoop when their heights are combined."
    "But the lack of physical verticality and concealed desire to snatch away the object of their respective best friends’ affection is not the only similarity they share."
    "They share a bond much deeper- "
    "One that very few will understand. "
    "One that very few {i}want{/i} to understand."
    "I will tell you now that they {i}were{/i} looking for the remnants of things they once lost in the sand."
    "Neither of them expected to find anything, of course."
    "I mean, why would they?"
    "But I, just as they do, struggle to think that anyone can walk around a place like this without incessantly gazing down at their feet in hopes of finding something that takes them back."
    "A seashell."
    "A coin with a specific year on it."
    "The sunglasses of a woman who was pulled in by the current."
    "Mementos and mementos and mementos!"
    "Each one left behind with a story of its own."
    "Every object in every place is more than it seems."
    "Just like every downtrodden, longing stare from a girl with A-cups is also more than it seems."
    "They connect."

    sa "Hey..."
    sa "How do you...feel about Sensei?"
    sa "Not...as a teacher, but-"
    mi "I want him to be with Makoto."

    scene beachpartyyay32
    with dissolve

    sa "With...Makoto?"
    mi "Yeah."
    mi "She’s liked him from the moment she met him."
    mi "And she’s my best friend, so I have to root for her."
    sa "…"
    mi "Makoto works harder than anybody and doesn’t have much to show for it other than good grades."
    mi "Her dad was a big part of her life, too...and now he’s up in space. So all she’s really got in terms of a guy figure to look up to is Sensei."
    mi "So I want him to look at her the same way she looks at him."
    mi "That way, everyone can be happy."
    sa "…"
    mi "I..."
    mi "Yeah."
    mi "I want him to end up with Makoto."
    sa "…"
    mi "…"

    scene beachpartyyay33
    with dissolve

    sa "I..."
    sa "I don’t want him to end up with anybody."
    mi "…"
    sa "…"
    mi "I guess that would be the next best thing for me too."

    scene black
    with dissolve2

    "The line remains unmoving on the beach, blending in with thousands more left there by nature or the pointy end of a stick gripped firmly by the slimy fingers of someone’s child."
    "Neither girl ever finds anything they’re looking for."
    "But, on the bright side-"
    "All of the other girls seem to have a good time."

    $ renpy.end_replay()
    $ secondbeach5 = True
    stop music fadeout 5.0

    "{i}There is something buried underneath your feet!{/i}"
    "{i}Could it be here?{/i}"
    "………"
    "……"
    "…"

    jump secondbeach6
...
```