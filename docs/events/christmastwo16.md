# No Escape (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [A Way's Away](./christmastwo15.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmastwo16
* Group: Main
* Triggered by label: christmastwo15
* Chain sources: christmastwo15
* Chain sources path: christmastwo15

## Official wiki page

[No Escape](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo16&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo16:
    scene clearnightsky
    with dissolve2
    play music "retrospect.mp3"

    "I make my way through an empty lobby and out into the open air. "
    "It’s not every day that I go to the effort of seeking someone out for the sole purpose of doing something nice for them, but...{i}tis the season{/i} or whatever else you’re supposed to say here."
    "What a life I lead where I must justify acts of kindness with seasonal phrases at the risk of seeming a little more human to whoever or whatever is watching me at all hours of the day."
    "Or night now, I suppose."
    "Which isn’t to say that someone {i}is{/i} watching me."
    "I’m no more paranoid than anyone else."
    "But, in the event that one of thousands of religions might have sturdy enough hands to grab hold of the elusive truths of the world- I will remain careful."
    "I will remain vigilant."
    "Because those elusive truths would imply that there is more to simply being than {i}being.{/i}"
    "I will walk into the night with a purpose in every step, keeping close to the walls to avoid the prying eyes of imaginary (Or unimaginary) gods. "
    "Or...anyone else who might see me alone with a small girl in the middle of the night."
    "I’m sure I look incredibly suspicious right now."
    "But I’m an incredibly suspicious person, so that’s rightfully deserved."
    "I look down at the stuffed bear in my hands and wonder why it was that I picked this of all things."
    "Was this {i}really{/i} just a spur of the moment decision brought on by an overwhelming lack of care?"
    "Or is there something more to it?"
    "I search my mind for the answer but am unable to sneak past an ever-growing wall of apathy thirty one years in the making."
    "To think it’s been in construction for so long and is not even close to finished is a bit disheartening."
    "And while I should hate that such an obstacle exists at all, especially in the place where it does-"
    "All I’m really curious about is whether or not I’ll live to see it completed."
    "What a wonderful wall it will be."

    s "..."

    "Oh, right."
    "The bear."
    "I need to give this to Miku."

    scene black
    with dissolve2

    "My legs begin to tremble for reasons beyond my comprehension."
    "The glow of electric billboards dyes my clothes."
    "I revel in the light, yet move further into the dark in hopes of pulling out a girl drenched in it."

    play sound "static.mp3"
    scene help5 with flash
    scene mikubear1 with flash
    stop sound

    if chikalust10 == True:
        "I find her on a familiar bench in a familiar place."
    else:
        "I find her easily."

    "She does not notice my presence at first, for I am just one more shadow in a world filled to the brim with them."
    "I do not exist until she accepts my existence."
    "And I make no sound because there are no sounds left to make."

    if bonus == True:
        play sound "static.mp3"
        scene help5 with flash
        scene mikubear2 with flash
        stop sound

        "Her shirt comes off, but only in my mind."
        "I’m sure that things are different outside of it. "
        "They always are."

        s "..."

        "As I {s}sit{/s} stand and stare at the budding chest of the school’s star soccer player, I struggle to subconsciously slide off her pants."
        "How shameful that even the images I conjure up are incapable of giving me more than I already have. "
        "Or had. "
        "Or will have. "
        "Or am currently having."
        "Or possessed at one point only to be pushed back to the beginning."
        "But for what?"
        "The sensation of flower petals falling off of my fingertips infuriates me."
        "I long to return to the memory of this young girl, nervously grinding up against my-"

        play sound "static.mp3"
        scene help5 with flash
        scene mikubear1 with flash
        stop sound

        "No."
        "That’s not why I-"

        play sound "static.mp3"
        scene help5 with flash
        scene mikubear2 with flash
        stop sound

        "I wonder how often she thinks of that night."
        "I bet it’s more than I do."

        scene mikubear3
        with dissolve

        mi "Hm?"
        mi "Sensei?"

    play sound "static.mp3"
    scene mikubear4 with flash
    stop sound

    s "Hey. "
    mi "What’re you doin’ out here? Figured you’d be fist deep in a whole room full of girls by now."
    s "I think you might be misunderstanding the usage of “fist deep” seeing as I only have two of them and could not possibly-"
    s "Actually, that doesn’t matter. I’m here to see you."

    scene mikubear5
    with dissolve

    mi "Me? But...Wait, did Makoto tell you I was here? "
    s "Was she not supposed to do that?"

    scene mikubear6
    with dissolve

    mi "Well, I...didn’t tell her not to tell ya. I just think there are a lot better ways of spendin’ your Christmas than worrying about me."
    mi "I’ll go back up soon. Just needed a little break from all of the noise."
    mi "Turns out I wasn't doin' as good as I thought I was."
    mi "Can only handle so much at once, ya know?"
    s "Don’t worry about rushing to go back up there. Almost half of the class is missing at this point, so it’s not like you’re the odd man out or anything."

    scene mikubear7
    with dissolve

    mi "Yeah, I noticed that. And Kirin left without even sayin’ bye to me. D’ya think havin’ so many people in our class now is like...separatin’ everybody into factions or something?"
    s "No, but I wouldn’t be surprised if the two day long event where you all literally separated into factions did that."

    scene mikubear8
    with dissolve

    mi "Don’t bring that up. I’m still embarrassed about how my part of the contest ended up."
    s "You...won, though?"

    scene mikubear5
    with dissolve

    mi "But at what cost?! It wasn’t a sweep {i}and{/i} I got licked by a girl! It may as well have just been a flat out loss."
    s "Then...make up for it next time. I don’t know. "

    scene mikubear9
    with dissolve

    mi "You feelin’ okay, Sensei? You look fine but you seem a little more...{i}blah{/i} than usual."
    mi "Anything your buddy Miku can do to perk you up a bit?"

    if bonus == True:
        s "Nothing legal."
        mi "Legal? You tryin’ to rob a bank or something?"
        s "Yup. That is exactly what I was implying."
        mi "Then take a seat and draft up some heist plans with me. I had to use up the last of my money buyin’ a present for Io so I’m basically flat out broke."
    else:
        s "No. Now tell me who you had for Secret Santa or I will kill you."
        mi "Io."

    s "You had to get something for Io? What did you buy?"

    scene mikubear10
    with dissolve

    mi "Hehehe...I ain’t tellin’ you. You’ll just have to see it for yourself the next time you visit her room."

    if bonus == True:
        mi "Now, come on. Tell me more about this heist. Me and you’ll be the best bank robbers Kumon-mi’s ever seen."

    scene black
    with dissolve2

    "Miku slides over on the bench and makes room for me."
    "I awkwardly place the stuffed bear in my lap and have to choke back vomit as it causes me to imagine a life in which it is replaced by a child."
    "And while I’m sure the image of that would make several girls I know very, {i}very{/i} happy- it makes me feel sick."
    "........."
    "......"
    "..."

    scene mikubear11
    with dissolve2

    mi "I ain’t gonna lie to you, Sensei...you look pretty friggin’ creepy right now. Kinda like some...baby thief or something."
    s "I’m glad that at least you acknowledge that I would be a horrible father. That means a lot."
    mi "Wasn’t really tryin’ to compliment you, but I’m glad I could help."
    mi "What’re carryin’ that thing around for anyway? I wasn’t gonna say anything at first, but now that it’s in your lap, I kinda can’t ignore it anymore."

    scene mikubear12
    with dissolve

    mi "Wait, isn’t that the same bear Touka was luggin’ around earlier? She give that to you or something? "
    mi "I know ya told me I wasn't supposed to look at her, but I kinda failed at that right away."
    mi "Pretty crappy present if ya ask me."
    s "Well, that is going to make the next few minutes very awkward because {i}I{/i} actually bought this for you."

    scene mikubear13
    with dissolve

    mi "...huh?"
    mi "No. No you didn’t. That’s..."

    scene mikubear14
    with dissolve

    mi "That’s not something that..."
    mi "Because...I’m..."

    "Guess I should have just added another piece to her soccer ball collection after all."

    s "If you’re worried about upsetting me, don’t be. It’s fine to dislike it. "
    s "I kind of just bought it on a whim anyway, so it’s not like there was any real thought put into it."
    mi "You bought...{i}that{/i} on a whim...for me?"

    scene mikubear15
    with dissolve

    mi "You’re just pullin’ my leg, right? You probably bought that for Ami or Uta or somethin’ and are just messin’ around right now."
    s "Why would I be messing around?"

    scene mikubear16
    with dissolve

    mi "Because that’s definitely not the kinda thing I’d expect ya to buy for me when you can get some kinda...sports thingy at pretty much any store you walk into!"
    mi "I don’t have anything that...girly! I just don’t keep that kind of stuff around! So you’d have no reason to choose that over somethin’ more...Miku-ish."
    s "Well, it’s yours now. So if you want to pretend it’s a basketball and just shoot it into the trash can behind us, we can do that."
    s "I get to go first, though, because I used my money to buy it and that would only be fair."
    mi "What? No...I..."

    scene mikubear17
    with dissolve

    "Miku snatches the bear out of my hands and stares at it for a few moments."
    "I recall a short while ago when Makoto mentioned something about Miku going to the place “furthest away from the noise” or however it was she worded it-"
    "But the lack of conversation, as temporary as it may be, makes me acutely aware that there is no escape at all."
    "And that even in this place, as far away from her fears as possible, they’re still lingering in the background."
    "As is everything in a world full of shadows."

    mi "..."
    s "..."
    mi "..."
    s "So, remember when you said {i}I{/i} was creepy a couple minutes ago? You’re really not making a good case for yourself by just silently staring at a toy right now."
    mi "Oh no..."

    scene mikubear18
    with dissolve

    s "Miku?"
    mi "No no no no no no...this is bad. "
    mi "This is really, really bad."
    s "Wow. You must really hate bears."

    scene mikubear19
    with dissolve

    mi "This is the single worst thing you could have gotten me..."
    s "Yeah, you’ve made that pretty apparent."
    mi "No...Sensei...You don’t understand..."
    mi "I love it..."
    s "..."
    s "You’re right. I don’t understand."

    scene mikubear20
    with dissolve

    mi "I love it so much! I...I need to give him a name!"
    s "You really don’t-"
    mi "I do!"
    mi "And..."
    mi "{i}And...{/i}"

    scene mikubear21
    with dissolve

    mi "I’m sorry!"
    s "Sorry for-"

    play sound "static.mp3"
    scene help5 with flash
    scene mikubear22 with flash
    stop sound

    mi "Mm~"
    s "..."

    "Oh. Okay."
    "I get it now."
    "It’s {i}exactly{/i} what she wanted."
    "Perhaps there {i}was{/i} a reason I bought this after all."
    "And perhaps things simply stop being {i}whims{/i} when you’ve existed long enough to experience every outcome."
    "Is this a new path?"
    "Or am I just sticking as close to someone else’s shadow as I possibly can?"

    mi "..."
    s "..."

    "There’s obviously no point in thinking about that right now, though."
    "Not when I can do this."

    scene mikubear23
    with dissolve

    mi "Mm! Mm...mnh...mm..."
    mi "Chu...mm~"
    mi "Thank you...mnch...thank...you..."
    mi "Sensei..."

    "Miku clumsily kisses me back and clearly has no idea what she’s doing."
    "She likes it, though."
    "Which, all things considered, I’m not that surprised about."
    "I’ve obviously known for a while that she’s been interested in me on at least {i}some{/i} level."
    "I just figured that level was going to remain a bit more dubious until she came to terms with pining after the man her best friend loves."
    "That’s why this present was so horrible."
    "Because it’s jeopardizing one of the purest, truest friendships I have ever known."

    if bonus == True:
        "And it’s doing so in a way much more calculated than drowsily grinding against my cock in the middle of the night."
        "{i}This{/i} is something we meant to do."
        "No. This is something {i}Miku{/i} meant to do."

    "She can’t hide anymore."
    "There truly is no escape."

    scene mikubear24
    with dissolve

    mi "{i}Haah...{/i}"
    mi "Hah........ah.......hah......"
    mi "I have to tell Makoto..."
    s "Why?"
    mi "Because she loves you..."
    s "Makoto must know how you feel about me by now. "
    mi "I don't know, Sensei. She did bust into the room that one time, but..."
    mi "But I told her it didn't mean anything. I {i}promised{/i} her it didn't mean anything."
    s "Stop suffering for her."
    mi "It’s not {i}suffering{/i}, Sensei. If she’s happy, I’m happy."
    s "Then shouldn’t the same go for her?"

    scene mikubear25
    with dissolve

    mi "What do you mean?..."
    s "If being with me makes {i}you{/i} happy, shouldn’t {i}she{/i} be happy knowing that you are?"
    mi "She’s liked you forever. I can’t just cut the line no matter {i}how{/i} much I want to."
    s "But you can blur it."
    mi "You’ve gotta remember who you’re talkin’ to right now, Sensei. I ain’t good at pickin’ up on fancy metaphors like that."
    mi "That...{i}was{/i} a metaphor, right? "
    s "Just keep this a secret. You don’t {i}have{/i} to tell Makoto everything because there’s no way {i}she’s{/i} telling you everything."

    scene mikubear26
    with dissolve

    mi "She does, though..."
    mi "But that’s not sayin’ I like hearin’ it...It’s really hard sometimes, you know?..."
    mi "I’m happy that she gets to...do all sorts of stuff with you...but it makes me feel all...gross inside hearin’ about it..."
    s "And your solution is to just keep letting that happen?"
    mi "I told you already...I’m on Team Makoto..."
    mi "I can’t be-"

    scene mikubear23
    with dissolve

    mi "Mmm! Mm..."
    mi "I...can’t be...mnch...doing this..."
    mi "It’s bad...it’s...really...really...bad..."

    scene mikubear27
    with dissolve

    s "You seem to be enjoying this quite a bit for someone who allegedly doesn’t want it."
    mi "I doubt {i}you’re{/i} havin’ any fun, though. I’ve got no friggin’ idea what to do with my tongue. I’m still new to this. "
    s "That’s fine. We can practice."
    mi "..."
    s "..."
    mi "I’ve gotta tell her, Sensei..."
    s "You don’t."
    mi "I do..."
    s "You don’t. "
    mi "I do. Every time I look at that bear, it’s gonna remind me of this. "
    s "Then get rid of the bear."

    scene mikubear28
    with dissolve

    mi "You kidding?! No way! This is the first time anyone’s ever given me somethin’ like that! And it was friggin’ {i}you{/i} of all people."
    mi "I’m gonna treasure it forever!"
    s "Then don’t complain about how it makes you feel when you look at it. "
    s "Accept what happened here tonight and take solace in the fact that the person you’re interested in is interested in you."
    s "Makoto doesn’t need to know that. No one does."

    scene mikubear24
    with dissolve

    mi "Sensei...thank you again for the present, but..."
    mi "I kinda...think I need a little time to myself to...figure out what to do."
    s "I’m assuming that means we’re done making out then?"
    mi "I guess so..."
    mi "Sorry again for attacking you like that..."
    s "You can attack me as often as you want so long as we’re not in public."
    mi "Stop sayin’ such...dangerous things, Sensei..."
    mi "It’ll only make it harder for me..."

    scene black
    with dissolve2

    "Miku and I break apart. "
    "But she breaks a little bit more."

    scene mikubear29
    with dissolve2

    if bonus == True:
        "{i}Welcome to Lessons in Love!{/i}"
        "{i}A game where you get to put your penis inside of girls dealing with trauma, no matter how bad of an idea they may think it is!{/i}"
        "{i}Occasionally, your actions will cause things like this to happen.{/i}"
        "{i}But that’s okay! Because, most of the time, it won’t even be your fault.{/i}"
        "{i}You are a shadow, after all.{/i}"
        "{i}You are everything I want you to be.{/i}"
        "{i}And slowly, but surely, you are becoming even more.{/i}"
        "{i}There is something buried underneath your feet.{/i}"
        "{i}And something above as well.{/i}"
    else:
        "{i}Welcome to The Legend of the Huggy Boy, a completely uncensored video game that has absolutely nothing to do with Lessons in Love!{/i}"
        "{i}There is nothing here!{/i}"
        "{i}It's all just empty.{/i}"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ christmastwo16 = True
    $ miku_love += 10

    "{i}Miku’s affection has increased to [miku_love]!{/i}"

    stop music

    "/////////////////////////////EVENT COMPLETE"
    "/////////////////////////////ATTEMPTING TO DOWNLOAD CARE PACKAGE"
    "/////////////////////////////..."
    "/////////////////////////////..."
    "/////////////////////////////..."
    "/////////////////////////////DOWNLOAD SUCCESSFUL"
    "/////////////////////////////PLEASE CONTINUE WALKING. YOU ARE VERY GOOD AT IT."

    play sound "static.mp3"
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    stop sound

    jump christmastwo17

label christmastwo17:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
ima "Nothing?! Not even an innuendo for me to feed off of?!"
    s "I’m busy right now. Just let me drop this thing off and {i}then{/i} we can practice our...innuendo trading."

    scene secretsantatime30
    with dissolve

    ima "Fine. Give it here. "
    ima "I’m a little too old for stuffed animals, but I guess this’ll have to do. "
    s "Imani."
    ima "What, dude? You said you needed to drop that thing off. I’ve got arms. I can handle the drop."

    scene black
    with dissolve2

    s "Maybe next year."

    "If she’s even still around next year."
    "Based on my current track record, though, I think it’s probably safe to assume she will be."
    "Unless tonight ends with another dramatic turn of events, of course."
    "But I should probably find a tomboy to give this bear to before that winds up being the case."

    scene secretsantatime31
    with dissolve2

    s "Makoto, where-"
    s "Woah. What’s wrong?"
    mak "What am I supposed to do with this, Sensei?!"
    s "It’s a picture, so...I think you’re supposed to hang it up?"

    scene secretsantatime32
    with dissolve

    mak "It’s worth a million yen! I’ve never even touched anything this expensive before!"
    s "That is well over the $20 spending limit."
    mak "I knew something like this might happen when we set the limit in US dollars! Touka barely understands the value of {i}our{/i} currency, let alone a foreign one!"
    s "You know, I was wondering what the reasoning behind that was when I saw it written on the board the other day, but I decided against asking."
    mak "I need your help! I don’t know what to do with this thing!"
    s "I will gladly take it off your hands."

    scene secretsantatime33
    with dissolve

    mak "Not that kind of help! I need your help returning it! I can barely even hold this thing up! It’s too heavy!"
    s "Yeah, it must be really tough having all of that wealth in the palms of your hands. Poor you."

    scene secretsantatime34
    with dissolve

    mak "Ugh...why did she think something like this was okay?"
    s "That aside, have you seen Miku? I have to give her this present."

    scene secretsantatime35
    with dissolve

    mak "Miku? Yeah. She went outside to get some air a little while ago when things started getting loud."
    mak "Is that...stuffed animal you’re carrying for her?"
    s "Yeah. I didn’t really know what else to get and it kind of just jumped out at me."
    mak "And you...didn’t think she was too {i}boyish{/i} to enjoy something like that?"

    scene secretsantatime36
    with dissolve

    s "I have no idea if she’ll enjoy it or not. It’s just what I bought. If she likes it, she likes it. If she doesn’t-"
    mak "..."
    s "..."
    s "Makoto?"

    scene secretsantatime37
    with dissolve

    mak "She’s probably somewhere on the side of the hotel, where you can’t see any of the other buildings or cars or anything."
    mak "So...as far away from everything that she can possibly be right now without completely abandoning the party."
    s "Oh. Uhh, okay. "
    s "I guess I’ll just head out there now then."
    mak "And I’ll...be here. Stuck standing in place with this extremely valuable painting."
    s "I believe in you, Makoto. If there’s anyone good at not being crushed by the weight of responsibility and obligation, it’s you."

    scene secretsantatime38
    with dissolve

    mak "Okay. You can leave now."
    s "And I will do just that. See you later."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ christmastwo15 = True
    $ makoto_love += 1
    $ molly_love += 1
    stop music fadeout 7.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo16
...
```