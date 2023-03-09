# Rule #1
Yuki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yukidate1&go=Go)



## Event preconditions
✅Yuki love greater than or equal to 0

✅Event "[Yumi: Where the Sidewalk Ends](./streets30.md)" is completed (event=streets30)

✅Event "[Tsuneyo: Blackout](./ramen20.md)" is completed (event=ramen20)

✅yukinumber equal to True (unknown variable)



## Next events
* [Yumi: Walls Too Thick to Hear Through](./yumidorm30.md)
* [Yuki: Better Off Alone](./yukidate5.md)

## Event properties
* ID: yukidate1
* Group: Yuki
* Triggered by label: callyukinight
* Triggered by branch label: callnight

## Event code
File: \game\YukiEvents.rpy
Code:
```python
...
label yukidate1:
    play sound "phonebeep.wav"

    "I tap on Yuki’s name in my phone and wait for her to answer."
    "I haven’t really seen her at all since our last run-in at the bathhouse, and it definitely seemed like she had some things to...discuss with me."
    "Granted, it’s possible she just wants to drag me into an alley and beat me up. "
    "And I’m pretty sure she could since she wears a leather jacket."

    s "…"

    "If you can’t tell, I may be slightly nervous given how horrible I am at dealing with Yumi’s temper...and this is the woman who started it all."

    play sound "phonebeep.wav"

    yu "Yeah?"
    s "Hey. "
    yu "Hey. "
    yu "Who’s this?"
    s "It’s...your daughter’s teacher."
    yu "Oooooh, shit. I was startin’ to think I’d never hear from you."
    yu "You hungry? Dinner offer’s still on the table."
    s "Does accepting make this a date?"
    yu "Pfft. Yeah, right. "
    yu "I haven’t been on a date in ten fuckin’ years. "
    yu "Just think of it as payment for bothering the shit out of you for a little while."
    s "That sounds significantly less fun. But I’m in, I guess."
    s "Tojo Ramen?"
    yu "Yeah. Need a ride?"
    s "You drive?"
    yu "I’ve got a bike I could swing by on."
    s "Oh."
    s "Yeah, I’ll walk. I’m not a fan of motorcycles."
    yu "What?"
    yu "You fuckin’ scared or something?"
    s "Nope. Not scared at all."
    s "See you soon, Yuki."
    yu "Uh-huh. Don't forget to tell your mom you’re going to be out late-"

    play sound "phonebeep.wav"

    "I hang up the phone before Yuki begins to talk about how brave and manly I am, a thing she was definitely about to do."

    scene black
    with dissolve
    play music "kashiwagi.mp3" fadein 10.0

    "I walk deeper into the winter winds, heading toward the old district with my hands buried inside of my pockets."
    "It will be nice not having to pay tonight, sure."
    "But I wonder how a conversation between Yuki and me could possibly go?"
    "………"
    "……"
    "…"

    scene yukifirstdate1
    with dissolve

    yu "Yo. "
    yu "Sure took your sweet ass time gettin’ here."
    yu "The bike probably doesn’t sound so scary now, huh?"
    t "Hello and welcome to Tojo Ramen. Is it your first time here?"
    s "Tsuneyo, I’m here all the time."
    t "Fuck you."
    s "..."

    "Well that's one way to greet someone, I guess."

    yu "So...you two are still {i}fucking{/i} each other, I see."
    s "I am very glad that she cleared up that misunderstanding with you instead of me."
    yu "Same. "
    yu "Weird experience, walkin’ in to get dinner and seeing the waitress and your daughter’s teacher talkin’ about boning."
    t "What is “boning?” This is one more term I am not familiar with."
    s "Don’t worry about it, Tsuneyo. "
    s "In fact, why don’t you stay out of this conversation entirely? I’m here to talk with Yuki."
    yu "Ooooh, look at you sounding all serious."
    s "Well, that’s why we’re meeting up, right?"
    s "Since you made it clear that it’s not a date, I mean."

    scene yukifirstdate2
    with dissolve

    yu "Well, yeah. But that doesn’t mean we’ve gotta act like we're holdin’ a fuckin’ meeting or something."
    yu "Just eat, drink, and talk. "
    yu "Pretend we’re friends or something. I don’t give a shit."
    yu "Long as neither one of us makes this weird, it’ll wind up being easy as hell."
    s "What will wind up being easy, exactly?"

    scene yukifirstdate3
    with dissolve

    yu "Gettin’ a progress report on my daughter, numbnuts. "
    yu "How’s she doing? Beat the shit out of anybody yet? Any teachers?"
    yu "Wait, wait. You’re probably scared of me because she fucked you up already, didn’t she?"
    s "Uhh...no. That is not a thing that has happened."

    if bonus == True:
        yu "Well if you’re not boning her and she ain’t doing shit to you, how come you two are hanging out together after[school]?"
    else:
        yu "Well it could. You're a fucking pussy and she would kick the shit out of you."
        s "That was not necessary, Yuki."

    s "You know, I had a feeling Yumi would be the topic of conversation tonight, but I can’t say I was expecting the world’s most informal PTA meeting."
    t "Your daughter has a very unique attitude. "
    t "I believe she would make an exceptional drill sergeant. "
    s "Tsuneyo."

    scene yukifirstdate4
    with dissolve

    t "Ah-"
    s "Let me handle this, please."

    scene yukifirstdate5
    with dissolve

    yu "I just fuckin’ said that we don’t need to treat this like a meeting."
    yu "I really just want to know how she’s doing."

    if bonus == True:
        yu "And also whether or not we need to have a {i}talk{/i} about you getting closer to her than someone in your “position” probably should be."
    else:
        yu "And also if you're adequately teaching her algebra and shit."

    s "You say that as if I’m not a model teacher."

    scene yukifirstdate6
    with dissolve

    yu "Well, if what Io tells me is true, you definitely aren’t."

    if bonus == False:
        s "Io is a bitch. Don't listen to her."
    else:
        yu "But I also don’t think Yumi would be dumb enough to go after someone your age, so I’m curious about what’s going on."
        yu "And it’s not like I can ask her myself. "
        yu "You saw how she reacted the last time we ran into each other."

    "I sit down at the table and realize that I’m already too deep into this topic to be able to order any food without killing the momentum."
    "I guess I’ll just have to go with the flow until Tsuneyo realizes that I am also a human being who needs to eat in order to stay alive."

    s "Yumi is...definitely a student."
    yu "…"
    s "…"
    yu "Is that it? That’s all you’re gonna give me?"
    yu "Of course she’s a fucking student. What else?"
    s "Can I ask why you want to know all this? "
    s "It just seems a little weird for you to start showing concern out of nowhere after all I’ve heard from her about you."

    scene yukifirstdate7
    with dissolve

    yu "And what did you hear from her?"
    yu "That I’m a shit mother and a junkie and that I used to beat her or something?"
    s "She definitely didn’t mention that last part."
    s "That’s not something you actually did, is it?"

    scene yukifirstdate8
    with dissolve

    yu "No! She’s my kid! I’d never fuckin’ do something like that!"
    yu "Can’t even tell you how many people I had to fuck up for just makin’ her cry."
    yu "It was like, a whole fuckin' thing back when I was still hangin’ around that place."
    yu "The second Yumi would start crying, everyone would book it because they were all afraid they’d have to answer to me."
    s "And the other stuff? The drugs and the...abandonment?"

    scene yukifirstdate9
    with dissolve

    yu "That..."
    yu "Yeah. She wasn’t lyin’ about that."
    yu "Kind of surprised she didn’t start saying anything worse, though."
    yu "Thought for sure she’d make me out to be fuckin’ Satan reincarnated by now."
    s "Well you’re certainly no angel."
    yu "Yeah, yeah. I’m a bad fucking parent. You think I don’t know that?"
    yu "But that doesn’t mean I don’t want to know how she’s doing."
    yu "Just to check in and shit. "

    if bonus == True:
        yu "She’s around the same age I was when everything started fallin' apart, so it’s...nice seeing that she’s not completely fucked up yet."
        s "What exactly happened to you when you were her age?"
    else:
        yu "She's startin' to act like Bigfoot back when I used to track him."
        s "Tell me more about that."

    scene yukifirstdate10
    with dissolve

    yu "That’s a story for another time. "
    yu "You’ve been chill so far, so I wouldn't mind talkin' about it. Just not today."

    if bonus == False:
        s "But I need to know where he is so I can blog about it."

    yu "All you {i}really{/i} need to know is that I ain’t doin’ that shit anymore."
    yu "Not like I expect it to change anything at this point, but yeah."
    yu "Either quit now or wind up in a fuckin' dumpster, you know?"
    s "Not really. I can’t say this is an area I have much experience with. "
    yu "Oh, good. Thanks for reminding me that my life is shit and everyone else’s is so much better."
    s "…"
    yu "…"

    scene yukifirstdate11
    with dissolve

    yu "Dude, it’s a joke."
    s "Your delivery is somehow just as bad as Tsuneyo’s."

    scene yukifirstdate12
    with dissolve

    t "It’s true. But I have only been associating with people for several months now."
    t "You have no excuse. Please stop trying to be funny."
    yu "Jesus Christ, sorry. Didn’t realize everyone here was so dead inside."

    scene yukifirstdate13
    with dissolve

    yu "So, you said before you were helping her find a job or some shit, right?"
    yu "How’s that going? Anyone bite yet?"
    s "Not yet. But it’s not like she’s particularly...adept when it comes to job interviews."
    yu "What’s that mean? She ain’t qualified or some shit?"
    s "More like she threatened to beat the shit out of customers who stole from the store during one of her last interviews."
    yu "…"
    yu "And?"
    s "And that’s not a thing you can really say during a job interview."
    yu "Well, why the fuck not? Think showin’ that level of dedication would be a huge plus for managers and shit."
    yu "I’d hire her."

    "Well, she is definitely Yumi’s mother, if not anything else."

    s "Let’s look at things this way...what was your first job?"
    yu "Uhh...my parents owned a candy shop when I was little. "
    yu "I kind of helped out there until I was a [teenager], I guess."
    s "I don’t think helping out parents really counts. What about the first job you had as a [teenager]?"
    yu "Oh. None."
    s "None?"
    yu "Nah. "
    yu "I was one of those “This town is boring. I’ve gotta get away.” kind of girls."
    yu "So I left when I was in [high_school] and fell in with some gang."
    yu "Just chilled with them for a few years until I met Yumi’s dad and then mooched off of him after that."
    yu "Fucking lowlife, by the way. She tell you about him, too?"
    s "Just that he’s in the yakuza. "
    s "She hasn’t mentioned that much about either one of you, to be honest."
    s "The two of us aren’t exactly friends."
    yu "Does she have {i}any{/i} friends? Can’t imagine it’s easy makin’ any given her upbringing."
    s "One. "
    s "Well, one and a half."
    yu "How the fuck can you have half of a friend?"
    s "It’s her friend’s little sister. Yumi looks after her sometimes."

    scene yukifirstdate14
    with dissolve

    yu "{i}Yumi{/i} does?"
    yu "Like, {i}my{/i} Yumi? Looking after a kid?"
    s "Yeah. "
    s "She’s surprisingly good at it, too."
    yu "Well isn’t that a fuckin’ steaming pile of irony."
    yu "You gonna tell me she’s running a charity next, too?"
    s "No. But she {i}does{/i} steal and resell old TV’s in order to feed herself."

    scene yukifirstdate15
    with dissolve

    yu "There we go. There’s that good ole entrepreneurial spirit."
    yu "Must be takin’ after her grandpa."
    yu "Pretty soon, she’ll have her own fuckin’ candy store for some other little rebel to come steal from."
    yu "The cycle fuckin’ continues."
    s "This is a strange thing to seem proud about."
    yu "Hey, she’s out there trying to build something for herself. ‘Course I’m gonna be proud."
    yu "Think I’d have these bags under my eyes if I did the same thing at her age instead of just fallin’ in with some punks and livin' the easy way?"
    s "That is a weirdly positive way to look at things, but I’m pretty sure I agree."

    scene yukifirstdate16
    with dissolve

    yu "Shit, man. Her own business."
    s "I...don’t know if I’d call it a {i}business{/i}-"

    "Yuki remains silent for a few moments and I get caught up in watching the smoke trail off of her cigarette, only to be sucked up by the hoods of Tojo Ramen."
    "She seems strangely content right now. More content than a normal woman would be after learning her child is a semi-professional shoplifter."
    "But hey, with so many horrible things on this planet, I guess it wouldn’t be right to look down on anyone for managing to siphon some joy out of something slightly {i}less{/i} horrible."
    "I do wish that I didn’t feel compelled to ask things like this, though-"

    s "Do you want to see her again?"

    scene yukifirstdate17
    with dissolve

    yu "Huh?"
    s "If she agreed to it, would you want to meet up with her?"
    yu "…"
    s "I’m pretty sure Yumi doesn’t know you’re sober. "
    s "Maybe it would change things if she figured out you were trying to be a better person?"
    yu "…"

    scene yukifirstdate18
    with dissolve

    yu "That’s not what this was about, man."
    yu "I wasn’t planning on getting to know you so I could find a way back into my daughter’s life or some shit."
    yu "I just wanted to check in on her."
    yu "Make sure she’s not still hangin’ out with all those yakuza punks and shit."
    yu "You can’t just run out on your kid and then expect to walk back into the picture after gettin’ a little better."
    yu "That’ll fuck ‘em up even harder once things get bad again."
    s "Do you think there’s a chance things will get bad again?"

    scene yukifirstdate19
    with dissolve

    yu "Heh."
    yu "You don’t deal with people like me often, do you?"
    s "I can’t say I do, no."
    yu "Rule #1 - Things can {i}always{/i} get bad again. "
    yu "Doesn’t matter how fine I look now or how fine I look tomorrow. "
    yu "The day after that, somethin’ could snap and I could wind up in a bag."
    yu "Goal is just makin’ it through each day so you can start fresh on the next one or whatever other “enlightened” shit they’re preaching in NA nowadays."
    yu "Just the way things work, unfortunately."
    s "And here I thought {i}I{/i} was the one who didn’t want to make an effort to change anything."
    yu "Oh, shit...if only it were as easy as just “making an effort.”"
    yu "Listen, man. You can say whatever the fuck you want. I’ve heard it all before. "
    yu "But I’ll tell you the same thing I tell everybody else-"
    yu "It’s not that simple."
    yu "I really wish it was."
    yu "But it’s not."

    scene yukifirstdate20
    with dissolve

    yu "I’d be happy to meet up with her if she wanted to. "
    yu "But I’m not asking you to try and make shit like that happen when she has bigger fish to fry."

    scene yukifirstdate21
    with dissolve

    t "Did I hear fried fish?"
    t "Are you ready to order?"
    s "Just...give me the same thing Yuki is having. "
    t "There’s no fish in that at all. Are you sure this is what you want?"
    s "Give me literally anything, Tsuneyo. I’m starving."
    t "I understand. "
    t "I will go get you one of everything."
    s "That’s not-"

    scene yukifirstdate22
    with dissolve

    s "And she’s gone."
    yu "You expect anything else? She’s a fuckin’ weird kid."
    s "They all are. Everyone in my class."
    yu "Sorry to put you on the spot, but...you really think Yumi would want to see me again now that I’m not all...fucked up?"
    s "I have no idea what Yumi wants literally ever. But I don’t think it would hurt to ask."
    yu "Well...again, I’m not askin’ you to go out of your way for something like that."
    yu "I’m fine just hearing she’s doing okay. "
    yu "But...I ain’t gonna try and stop you."
    yu "I know how fuckin’ hardheaded guys get when they think about doin’ something."
    yu "And...yeah, I guess I {i}do{/i} kind of want to see that brat."
    yu "Don’t say anything to Io about it, though. Girl’s weirdly attached to me for whatever reason."
    yu "Don’t want her to get jealous and wind up gettin’ the shit kicked out of her after starting something with Yumi."
    s "I will...definitely not mention anything to Io."
    s "And I’ll think more about saying anything to Yumi, too."
    s "It just feels strange meeting up with you to give you a progress report when A: I hate progress reports. And B: This is the first time we’ve ever really {i}talked{/i}."

    scene yukifirstdate23
    with dissolve

    yu "Well, hey. You’ve got my number now, so you can call whenever you want."
    yu "Can’t guarantee you’ll like hangin’ out with me at all. But it’s kinda nice havin’ somebody to talk to in a place like this, you know?"
    yu "Also, the food’s fuckin’ great and Tsu-chan is hilarious."
    t "Ah-"

    "A gasp rings out from the kitchen and the sound of a metal pan being dropped rings throughout the ramen shop."
    "It’s hard to tell if this is the result of Tsuneyo’s name being said (Albeit in short form) or if she’s just shocked that someone has acknowledged her...rare form of comedy."

    scene black
    with dissolve2

    "Tsuneyo reappears and serves me the same bowl of ramen that Yuki has."
    "We eat our respective dinners and, just as she promised, Yuki winds up paying for me."
    "I still have no idea how I should progress with the Yumi situation, but it’s good knowing that things aren’t even half as bad as I thought they were at first."
    "Or, who knows? Maybe they are?"
    "I can’t imagine what it’s like being in either of their shoes."
    "So all I can really do now is just pull on every lever and press every button I can find until something happens."
    "So basically, life."
    "Yuki offers to give me a ride home but, once again, I decline."
    "Not because I am afraid of motorcycles-"
    "But because I am afraid of how much hope I may have given her for something that will likely never happen."

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yukidate1 = True
    stop music fadeout 5.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yukidate5:
...
```

## Code that triggers this event
File: \game\YukiEvents.rpy
Code:
```python
...
label callyukinight:
    if streets30 == False or ramen20 == False:
        "I should probably make sure I'm caught up with Yumi and Tsuneyo before giving Yuki a call."
        jump callnight

    if yuki_love >= 0 and streets30 == True and ramen20 == True and yukidate1 == False:
        jump yukidate1
...
```