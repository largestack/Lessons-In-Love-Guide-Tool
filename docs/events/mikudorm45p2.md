# Chrysalis
Miku event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm45p2&go=Go)


Part of event chain [Acute Love Triangle](./mikudorm45.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Miku: Someone Else's Skin](./mikuspecial50.md)

## Event properties
* ID: mikudorm45p2
* Group: Miku
* Triggered by label: mikudorm45

## Event code
File: \game\MikuEvents.rpy
Code:
```python
...
label mikudorm45p2:
    scene mikuwalksatnight1
    with dissolve2
    play music "retrospect.mp3"

    if bonus == True:
        "Eventually, we {i}do{/i} stop talking about my penis. "
        "Depressing, I know."
        "But seeing as it’s dangerous enough to discuss that in the dorms, it would be even more dangerous to walk the streets of Kumon-mi without trying to move onto other topics."
        "Things that will not ultimately serve as yet another common ground for the two of these girls to sprawl out on."
        "I guess one of them hasn’t done much sprawling yet, though."
        "But it’s only a matter of time- and I’m sure Makoto knows that too."
        "Miku’s grown up in a world filled with competition- she lives for it. And not just to win either. "
        "There are a lot of people out there who will tell you the whole idea of playing sports is to have fun, and there are those who would vehemently disagree."
        "I’d probably be one of those people."
        "And I’m sure that in the right shade of light, Miku would be too. "
        "But I think this is just one of those times where she’s excited to be playing."
        "Especially since it’s a game she’s just learning to play now."
        "But maybe her best friend will be able to help her."
        "And maybe one day, I can have them both sprawled out over that common ground at once."
    else:
        "(Insert SFW monologue here)"

    mi "Oh, Makoto. What’d ya wind up doin’ with that fancy painting Touka gave ya?"
    mak "I wound up giving it to my mother to either hang up at home or sell but, knowing her, I doubt she still has it."
    mi "Yeah, Maki doesn’t really seem like the kind of girl who would be into stuff like that."
    mak "It’s less that she doesn’t care for things like that and {i}more{/i} that she’s just really into...one very specific hobby."
    mak "But that’s not really something I want to discuss right now since I’m going to be surrounded by it in a matter of minutes."
    mak "I’d much prefer to hear about Sensei’s present. "

    scene mikuwalksatnight2
    with dissolve

    s "Oh, I’m involved now?"
    mi "Yeah. Didn’t Molly make somethin’ for ya, Sensei? I remember hearin’ somethin’ about that."
    mi "You two talkin’ again? Cause she seemed really beat up for a while over whatever happened with you two."
    s "We’re on good enough terms for her to make me clothing, at least."
    mak "Are we finally saying goodbye to your trusty thick t-shirt?"
    s "Well, it’s not like I was going to be able to wear it forever. "
    s "Once summer comes, I’ll need something thinner. And I guess Molly just figured that out before I could."

    scene mikuwalksatnight3
    with dissolve

    mak "I supposed we’ll get to see it soon then. The weather’s been rather nice these last few days."
    mi "Fine by me. I’m tired of wearin’ this oversized jacket. Summer Miku’s been rarin’ to go for months."
    s "You wore a hoodie all last summer too, so I was just under the impression you liked being overheated."

    scene mikuwalksatnight4
    with dissolve

    mi "Nah...it ain’t really like that. I just don’t really change up my look that often and that’s what I had lyin’ around."
    mi "But...I’ve been thinkin’ it might be time to maybe try out a few new things and see if any of ‘em stick. You know?"
    mak "Want me to help with your hair again? I’ve noticed that it’s starting to get longer and I actually quite enjoy doing it when the circumstances aren’t utterly horrible."

    scene mikuwalksatnight5
    with dissolve

    mi "Yeah! Just don’t use the scissors to kill me or somethin’. I know how you can be when you get competitive and we {i}are{/i} kinda like rivals now."

    scene mikuwalksatnight6
    with dissolve

    mak "I’m not going to murder you, Miku."
    mi "Sounds like somethin' a murderer would say. "
    mak "God, I really hope this isn’t just how you are now. It’s difficult enough having to use virtually all of my free time teaching you the things Sensei doesn’t."
    s "Don’t worry, Makoto. I’ll make sure to teach Miku everything I know."

    scene mikuwalksatnight7
    with dissolve

    mak "Like hell you will!"
    mi "I think only I’m allowed to joke about stuff like that, Sensei. Makoto’s gonna get mad if you start doin’ it."
    mak "Start?! Our entire relationship is based around him using me however he wants."

    scene mikuwalksatnight8
    with dissolve

    mi "That ain’t true, Makoto. Sensei likes you and doesn’t do that stuff to hurt you on purpose."
    mi "And I ain’t sayin’ I know a lot about all of that adult stuff you and your mom watch together but, from what I’ve heard, it sounds to me like Sensei has done plenty to please you and not just-"

    scene mikuwalksatnight9
    with dissolve

    mak "Oh, look! My family’s store! What an inconvenient moment for this conversation to end. "

    if bonus == True:
        s "The porn shop is still like three blocks-"
    else:
        s "I can smell the DVDs from here."

    scene mikuwalksatnight10
    with dissolve

    mak "Right! Which means it’s the perfect place for us to part ways and not further discuss the horrible things we do {i}with{/i} and {i}to{/i} each other."

    if bonus == True:
        mi "If they’re so horrible, how come you keep-"
    else:
        s "What is so wrong about hugging?"

    mak "CAN’T HEAR YOU! HAVE TO WORK! BYE!"
    s "..."
    mi "..."

    scene mikuwalksatnight11
    with dissolve

    s "I think that Makoto probably would have kept a few more secrets from you if she had known you were going to just bring them up in casual conversation."
    mi "I just don’t get why she’s so embarrassed about it."
    s "I think the easiest way to put it is to just say that Makoto is kind of a different person when she’s doing that kind of stuff."
    mi "Different how?"
    s "..."
    mi "..."
    s "Is that a real question? Because that seems like a weird thing to ask about your best friend."

    scene mikuwalksatnight12
    with dissolve

    mi "Man! I’ve got no idea what’s okay to talk about and what’s {i}not{/i} okay to talk about when it comes to this stuff."
    mi "How come playin’ for two teams is like...twice as hard as playin’ for one?"
    s "Miku, I know you’re not very good at math, but I think that you can handle this problem if you just believe in yourself."

    scene black
    with dissolve2

    "Miku and I walk for a little while longer, and I’m pretty sure it’s aimless as well since it’s in a direction I’ve never gone before."
    "I doubt that either of us care much right now about where we’re headed or what we’re going to do when we get there."
    "We’re just kind of...moving from one place to the next and hoping that existing beside one another isn’t enough to tire the other out."
    "With someone like Miku beside me, that much is always a little uncertain."
    "But it’s been getting better lately."
    "Well, maybe “better” isn’t the right word."
    "But she doesn’t tire me out even half as much as she used to...and that is absolutely a good thing."
    "On the other side of things, though-"
    "It’s clear that she’s the one beginning to get a little exhausted."

    scene mikuwalksatnight13
    with dissolve2

    s "..."
    mi "..."
    s "Everything okay?"
    mi "Yeah, yeah. Everything’s good. Really good, actually."
    mi "I’m just still tryin’ to wrap my head around everything."
    mi "I’m used to stuff movin’ fast since that’s pretty much all I’ve ever known, but...this is a completely different kinda fast."
    mi "My blood’s pumpin’ and my heart is racin’, but my legs are all noodley and I can’t really hold my hands straight."
    mi "They’ve got this thing in sports called “The zone” where an athlete just gets like, mega focused for a little while and it kinda, like...enhances all of their abilities and stuff."
    mi "But I don’t know if this whole...liking you thing has a “zone.”"
    mi "I don’t know when I’m gonna stop being nervous and stuff. Which means I have no idea when I’m gonna be able to go back to {i}normal.{/i}"

    scene mikuwalksatnight14
    with dissolve

    mi "Wait! What if it’s not that?! What if I actually am sick?!"
    s "I’m no doctor, but I’m pretty sure your initial take on the situation is the one you’re looking for."
    s "Besides, there’s no need to go back to normal. Especially when normal with you has always been kind of abnormal to begin with."

    scene mikuwalksatnight15
    with dissolve

    mi "Ya think so? Cause we’ve got some pretty abnormal girls in our class and I was under the assumption that I was kinda one of the more normal ones."
    s "Sometimes, sure. "
    s "You have your moments, though."
    s "Like, I can’t think of anyone else who would have immediately gone against what I asked them to do and told their friend instead of just continuing to make out with me in private."

    scene mikuwalksatnight16
    with dissolve

    mi "You mad about that, Sensei? Cause I understand if you are. "
    mi "Ya gotta remember that you didn’t do anything, though. It was all me. We’d be playin’ a completely different ball game if you made the first move and kissed me instead of me kissin’ you."
    s "That’s true, I guess. I’ve made the first move on several occasions with you before and you never told Makoto about any of those."
    s "Well, until now, I guess."

    scene mikuwalksatnight17
    with dissolve

    mi "That’s not...completely true...and it might be why I still feel like somethin’s kinda...not right."
    mi "Makoto still doesn’t know about what happened at the beach and I kinda...don’t really wanna admit it to her."

    if bonus == True:
        mi "But that makes me feel really bad cause she told me {i}all about{/i} you two goin’ at it. "
        mi "I just don’t get why I’d wanna confess one thing but not confess another if they all fit into the same box, ya know?"
        s "Kissing and dry humping someone to the point of orgasm aren’t really things that fit into the same box, Miku."
        s "You don’t need a reason to not want to tell a person something. You can just...{i}not{/i} want to tell a person something. And that’s completely okay."
        mi "But is it still okay when you’re pretendin’ that everything is out in the open even when there’s still somethin’ buried beneath it all?"
    else:
        mi "But that makes me feel really bad cause she told me {i}all about{/i} how you guys are in the secret hug club. "

    s "Well, let me ask you this- do you think Makoto has really shared {i}everything{/i} with you?"

    scene mikuwalksatnight18
    with dissolve

    mi "I’m pretty friggin’ sure she has because I have no idea what else two people can even do to each other that she didn’t already tell me about."
    mi "Felt like any moment she was gonna start breakin’ out reference material. Certainly knows where to get it."
    s "Oh. Well...I don’t know, then."
    s "I’ve never had a best friend to talk to about things like that, so I’m not really sure what someone would be compelled to share or not."
    s "But I do know that there are things I’d want kept a secret from everyone- and I don’t think you should beat yourself up about it for being in the same boat."

    scene mikuwalksatnight19
    with dissolve

    mi "Yeah...probably not..."
    mi "Everythin’ just seems a little too good to be true right now, I guess. "
    mi "The guy I like’s hangin’ out with me on a bench in some park and my best friend who likes the same person doesn’t seem to mind at all."
    s "I think it’s less that she doesn’t mind and more that she’s just good at dealing with it."
    mi "Then she’s friggin’ stronger than I’ll ever be cause, if I was in her place, I’d be pissed the heck off."
    s "And what place is that? Because you two don’t seem too far off from where I’m standing."
    mi "I mean, she’s basically kinda your girlfriend already, just without the title and...without the kissing. "

    if bonus == True:
        mi "You two see each other all the time...she’s super loyal...you’ve {i}done it{/i} more times than I can even keep track of..."

    mi "What else is missing?"
    s "Love."
    s "On my end, at least."
    mi "Well, I hope you change your mind one day. "
    mi "She deserves it."
    s "And you don’t?"
    mi "Not really. "
    mi "I ain’t a bad person, but I ain’t really a good one either."
    s "I think you’re a good person, Miku."
    mi "Sure don’t feel that way, Sensei. Not while I’m pretendin’ to have a totally clean slate when all I did was use my hand to wipe off the dirt."
    mi "And, you know what? I don’t really want it to be completely clean either. When stuff like that’s clean, ya gotta take more time to look after it and make sure it doesn’t get all messed up."
    mi "But when somethin’s already a little dirty, you don’t have to be as careful. You can be a little reckless from time to time and just hope that nothin’ goes wrong."
    mi "Somethin’ always can, though."
    mi "Somethin’ always does."
    s "..."
    mi "..."
    s "This isn’t just about Makoto, is it?"

    scene mikuwalksatnight20
    with dissolve

    "Miku looks up at me, but doesn’t reply."
    "If she did, she’d be opening herself up. Exposing a weakness."
    "And in true athletic fashion, she’s swapped over to defense in order to weather my attack. "
    "I’m not much of an athlete, though-"
    "So it will be a half-hearted attack that I already know she’ll be able to deflect."
    "And one that won’t break through until she’s been worn down to near nothingness."

    if kirinkill == False:
        s "I know what happened to your parents."

        scene mikuwalksatnight23
        with dissolve

        mi "Don’t..."
        s "I can't tell you who told me, but-"
        mi "No..."
        mi "Not yet..."
        mi "I...ain’t ready..."
        s "Do you think you ever will be?"
        mi "Sensei..."
        mi "I really can’t..."
        s "I won’t force you to."
        s "I implore you to take your own advice sometime, though."
        s "Be a little reckless. Hope that nothing goes wrong."
        s "Maybe even rely on a teammate to make up for the areas you lack in."
        s "I’m not good at sports, but I can listen to whatever it is that happened and give you some half-hearted advice on the matter that’ll likely devolve into some sort of existential monologue."
        mi "..."
        s "I might be getting ahead of myself in saying this, but I think calling me just another average person in your life is a little outdated at this point."
        s "If you want to get closer, get closer. You’re good at that."
        s "And remember that simply talking about things that have happened in the past is perhaps the best way to get over them."

        "Something gets stuck in my throat during that last sentence."
        "Probably the irony."

        mi "..."
        s "..."

    else:
        s "I still don’t know anything about your past."

        scene mikuwalksatnight21
        with dissolve

        mi "My...past?..."
        mi "But...why would you..."
        s "It just might help me understand a little more about why you think the way you do."
        s "It’s a bit of a hobby of mine- staring into the depths of people and trying to attach motives to their actions. Particularly the ones that make the least amount of sense to them."
        s "But that’s hard to do when I can’t see even a single quadrant of the big picture."

        scene mikuwalksatnight22
        with dissolve

        mi "I...uh..."
        mi "It’s...hard..."
        mi "Like...I...."
        mi "I...start freezing up..."
        mi "Whenever I...go back there..."
        s "That bad?"

        scene mikuwalksatnight23
        with dissolve

        mi "I can..."
        mi "Still hear it..."
        mi "See it..."
        mi "I don’t..."
        mi "I...I can’t..."
        s "That’s enough."
        mi "..."

    s "You’ll tell me when you’re able to tell me, I guess."
    s "I just figured that whatever happened back then is probably something I’d know about {i}before{/i} we started taking our relationship in a more exciting direction."
    mi "I just..."
    mi "I want to forget..."
    s "Do you?"
    mi "..."
    s "..."

    "As expected, Miku cocoons herself inside a blanket of fear and waits to metamorphosize into something a little less defenseless."
    "Something more beautiful."
    "But her wings fuse to her chrysalis and she gets stuck inside."
    "As such, it falls on me to free her."
    "Or rather-"
    "I just want to."

    s "Let’s just talk about something else."

    scene mikuwalksatnight24
    with dissolve

    mi "..."
    s "..."
    mi "Yeah."
    mi "Yeah, that sounds good."
    mi "Sorry for-"
    s "Don’t apologize. Just move on."
    s "I’d prefer to not have to drag your screaming, nubile body all the way over to Makoto’s porn sanctuary and have her nurse you back to health."

    scene mikuwalksatnight25
    with dissolve

    mi "I think there were a bunch’a nicer ways to say that, but...yeah. I don’t really want ya doin’ that either."
    mi "‘Sides, bein’ round all those videos makes me feel kinda weird anyway. I’ve got no idea what’s goin’ on in like 90%% of them."

    if bonus == True:
        s "Want to find out?"
    else:
        s "Do you want to braid each other's hair?"

    mi "Jeez, Sensei. At least take me on a date-"

    scene mikuwalksatnight26
    with dissolve

    mi "Ooh! Right! I was gonna ask ya earlier when we were still with Makoto, but..."
    mi "Do you...maybe wanna come to the mall and help me pick out some clothes? I ain’t really sure if that counts as a date or not, but we can call it one if ya want."
    s "I don’t really care what we call it, but I {i}am{/i} interested in helping you find an outfit since that is an area I can now safely say I am slightly experienced in."

    scene mikuwalksatnight27
    with dissolve

    mi "Yeah...I remember you comin’ along with us when we got new swimsuits before the beach trip."
    mi "I guess this’ll be kinda like that, just...with only us two instead of a group of girls."
    s "Did you have an idea of when you’d want to go?"

    scene mikuwalksatnight28
    with dissolve

    mi "Idunno. Just call me after soccer practice on the weekend and we can meet up at the mall or somethin’."
    mi "We can make a whole thing out of it. Somethin’ that’ll get Makoto real jealous when I recap it for her."
    s "For my own personal curiosity, is {i}everything{/i} we do outside the bedroom in a beach inn something that’s going to be immediately forwarded to Makoto?"
    s "Because that would make my life exponentially harder."
    mi "I can probably make some more exceptions if they’re good enough."
    mi "Like ya said, I shouldn’t feel inclined to share {i}everything{/i} all the time."
    mi "You haven’t failed me so far, Sensei. So maybe you’re right about that too."
    s "Good enough for me."
    s "I’ll call you sometime over the weekend, then."
    mi "Sounds good."
    mi "I’m..."
    mi "Really lookin’ forward to it."

    scene black
    with dissolve2

    "Seeing as it’s already late and this park is as close to a halfway point as we're going to get, the two of us decide to split up and head back to our respective residences."
    "There’s no hug or kiss marking the end of the night in a way any different than it would normally be."
    "There’s no anything, really."
    "Just more lingering curiosity about what it is that made Miku {i}Miku{/i}-"

    if bonus == True:
        "And a higher likelihood of her sneaking into my thoughts when I go home to rub one out before bed."
    else:
        "And a really neat bird that lands right next to us on a tree branch."

    $ renpy.end_replay()
    $ mikudorm45p2 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikuspecial50:
...
```

## Code that triggers this event
File: \game\MikuEvents.rpy
Code:
```python
...
mak "Maybe {i}you{/i} should try and be more like Miku! I have done more than enough for you and deserve a reward every once in a while!"
    mi "She {i}does{/i} deserve it, Sensei. "
    s "Correct me if I’m wrong, but...aren’t you supposed to be rooting for yourself right now? "
    s "I figured the whole “Team Makoto” thing would be over with after today and that you’d try a little harder to keep me to yourself."

    scene intervention22
    with dissolve

    mi "Why would I try and keep ya to myself when Makoto likes you too? That ain’t fair at all."
    mi "I don’t see any reason why I can’t stay on Team Makoto {i}and{/i} like you. There some kinda rule against that?"
    mak "I mean...I don’t think there’s a {i}rulebook{/i} we can consult...but that’s not normally how love triangles go..."

    scene intervention23
    with dissolve

    mi "Well, maybe it ain’t really a triangle then?"
    mi "Aren’t you kinda rootin’ for me too, Makoto?"
    mak "Uhh..."
    mak "Not really?"
    mak "I obviously don’t want to hold you back from pursuing the person you admire, but if you’re asking if I’m hoping you and Sensei get closer...absolutely not."
    mi "Oh. "
    mi "Huh."

    scene intervention24
    with dissolve

    mi "Guess I’m the weird one, then."
    s "No surprise there."
    mak "Do {i}you{/i} have any questions, Sensei?"
    s "Just one. Was this really necessary?"
    mak "Probably not. But I’m sure it made Miku feel a little more comfortable and, strangely enough, I think I feel that way as well."
    s "Well, I don’t. This was weird and I’d prefer that we don’t ever do anything like this again in the future."
    mak "If you honestly think you’ll be able to avoid a similar conflict in the future, you’re out of your mind."
    mak "It’s only a matter of time until you’re having this exact conversation with every pair of friends who fall hopelessly in love or...{i}like{/i} with you."
    mak "All things considered, I think Miku and me handled this extremely well."
    s "Miku and I."
    mak "..."
    s "..."

    scene intervention25
    with dissolve

    mak "I changed my mind. You can have him."

    scene black
    with dissolve2

    "The intervention comes to a close as Makoto needs to start getting ready for work."
    "It definitely feels a little later than normal for her to start heading over there, so I initially dismiss it as an excuse to give Miku and me some time alone. "
    "But that notion is immediately quelled when Makoto says this."

    if bonus == True:
        mak "Oh, and you two are going to be walking there with me. I refuse to leave this room knowing that her shirt would immediately come off as soon as the door closes."
        mi "That happened one time! "
        mi "I do kinda wanna walk, though. So I’ll come."
        mak "And you, Sensei?"
        s "..."
        s "Ugh, fine."
    else:
        mak "Yahtzee!"
        s "Congratulations, Makoto."

    scene intervention26
    with dissolve

    mak "Oh, for fuck’s sake! Who keeps turning the number on our door upside down?! It’s getting very tiring!"
    mi "Do you really think it’s weird that I wanna be on Team Makoto {i}and{/i} Team Miku? Cause I just don’t really get why."
    s "That’s something you’ll have to talk to Makoto about. I’m perfectly fine with it."
    s "I do stand to benefit the most, though, so I’m probably biased."

    scene intervention27
    with dissolve

    mak "Why are we talking about that again?! The intervention is over and it’s time to return to reality!"
    mi "Oh, and sorry for lyin’ about Makoto not bein’ around. I figured ya would’ve ran if I told ya she was with me."
    s "It’s whatever. That honestly went a lot better than I was expecting. "
    mi "Yeah, nobody cried at all. And Makoto only got a tiny bit flustered when I brought up her {i}relationship{/i} with “little” Sensei."

    if bonus == True:
        s "Please don’t call it that, Miku."
        mak "Please don’t talk about that at all! And {i}definitely{/i} not in the halls!"
    else:
        s "Who told you about my miniature clone? That was supposed to be a secret."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ mikudorm45 = True
    $ makoto_love += 1
    $ miku_love += 1
    stop music fadeout 8.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump mikudorm45p2
...
```