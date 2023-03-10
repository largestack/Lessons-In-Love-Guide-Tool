# Heartbreak & Harmony (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 25

* Event [Work Less, Not Hard](./bathhouse25.md) (Io) is completed)

* Day of week is not Friday



## Next events

* [Io: 1999 PC Classic, Rollercoaster Tycoon](./iospecial30.md)

## Event properties

* Id: iodorm25
* Group: Io
* Triggered by label: iodorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->iodorm->iodorm25

## Official wiki page

[Heartbreak & Harmony](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=iodorm25&go=Go) for more details.

## Event code

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label iodorm25:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Io’s door and wait for her to answer, but my patience is quickly met by the sounds of the half-hushed humming of an unfamiliar tune halfway between heartbreak and harmony."
    "I do not know what has broken from this side of the door. But if there is anything I know about Io, it is that she likely has the tools to fix it."

    play sound "knock.mp3"

    "I knock again so she knows it’s me."
    "The humming stops and her attention bounces from whatever undeserving plank of wood it previously settled on and back to me where it rightfully belongs."

    i "Sensei?..."
    s "Yup. Can I come in?"
    i "I don’t knooooooww~ You might be kind of boooooored..."

    "Her words are slurred, something I couldn’t pick up from the humming, but the vulnerable state of an already vulnerable girl is not something that would force me back the way it would force others."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "It just brings me closer."
    "........."
    "......"
    "..."

    scene iooutofit1
    with dissolve2
    play music "io.mp3"

    "What I’m closer {i}to{/i} is something I’m not sure of, though. "
    "It’s not heartbreak for the remnants of my cardiovascular system have been worn so thin that “breaking” wouldn’t even suffice in describing the severing of the bits that are left at this point."
    "It’s not harmony either as the two of us inside of this room are almost constantly acting in opposition to whatever the world would have us do to move in unison."
    "I’m just closer to {i}her.{/i}"
    "Whether that’s good for either of us is something that remains to be seen."
    "But, if you want my opinion-"
    "The only thing that would be good for us is if we were left alone and stopped forcing ourselves to find one another."

    i "Heeeeey. Io Ichimonji here, reporting live from the floor. Which is coincidentally exactly where she belongs."
    s "I’m not sure if I’d call this “boring,” Io."
    i "Well, hey! If me being hopped on a medicinal cocktail’s enough to keep you entertained, you might be in for the most exciting night of your life."
    i "Just kind of figured I wouldn’t be as much fun as normal when every word I speak brings me one step closer to passing out."
    i "But then again, I’m not really any fun to begin with. So your taste is already kind of weird."
    i "Anyway, how’re things? Your niece still number one in the harem ranking? Uta says she makes a mean omurice."
    s "If talking is bringing you closer to passing out, maybe it’s best if you just...you know, don’t do that?"
    i "But then you’d {i}really{/i} be bored. And it’s not like I’m actually {i}gonna{/i} pass out. I’m just getting {i}closer{/i} to passing out."
    i "As if I’d waste this precious time with my favorite person in the world on {i}sleeping{/i} when he’s already expressed that he’s cool with me over-medicating myself."
    s "I’m not “cool” with that. You’re kind of weirding me out right now, actually. But at least you don’t look like you’re on the verge of dying this time."
    i "Different pills, different side effects. The endless cycle of targeted drug usage to combat the many things wrong with this stupid brain of mine."
    s "And what exactly were you targeting this time?"
    i "Yes."
    s "Io-"
    i "Why’s it matter what I was targeting? Can’t we just pretend that I’m feeling completely normal so we can have a completely normal conversation?"
    s "Is any conversation with you completely normal?"
    i "No. I like you too much to be able to speak normally. I’ll just wind up messing up again."
    s "Can I help you up? Or do you want to stay down there on the floor?"
    i "Wait wait wait. I just had the best idea."
    s "I somehow doubt that."
    i "No no no. Hear me out."
    i "If things can’t be normal because of how fucked up I am right now..."

    scene iooutofit2
    with dissolve

    i "You just need to get fucked up too!"
    s "How is that “the best” idea? That’s a horrible idea."
    i "Why’s that?"
    s "Because you very clearly need someone to look after you."

    scene iooutofit3
    with dissolve

    i "Nuh-uh. I know my limits when it comes to treating myself. Do I intentionally push those limits sometimes? Hell yeah. But this isn’t one of those times."
    i "I promise this is like, normal loopiness. The kind of stuff you’d be dealing with at least three nights a week if you ever ran away with me."
    i "If it was {i}really{/i} bad, I’d be hunched over my stepladder again and you’d have to carry me over to the kotatsu. But look! I made it here all by myself this time! Woohoo!"
    s "Either way, I’m not taking any of your pills. "
    i "Why not? They might help you."
    s "I don’t need help."
    i "Wish I could think that way."
    i "Either way, I wasn’t talking about pills in the first place. They’re too expensive and I like them too much to share."
    s "What {i}were{/i} you talking about then?"

    scene iooutofit4
    with dissolve

    i "One of our regular customers gifted us a bottle of sake a while back that I was supposed to give to my aunt- but I never did because I’m an asshole."
    i "Also, I thought it would be a fun thing to have in case Uta and I ever got bored one night. But it’s been here ever since and neither one of us has ever touched it."

    scene iooutofit5
    with dissolve

    i "Sensei, I bestow unto you this humble gift. May you partake so that we may {i}both{/i} get fucked up and free ourselves from the endless torment that is life itself."
    s "Well...that’s definitely a better alternative to unidentified medication, but I still don’t think getting drunk around someone so clearly under the influence is a great idea."

    scene iooutofit6
    with dissolve

    i "Why not?"
    s "Because we wouldn’t be ourselves at that point."
    i "If we’re not ourselves, anything that happens isn’t our fault."
    i "It would be more like whatever happens never happened in the first place."
    s "That’s not-"
    i "Just accept the fucking gift, Sensei. "
    i "With how uncertain the future is, {i}not{/i} accepting the gift could lead to Uta or I getting alcohol poisoning one day. And if that ever happened, I bet you’d regret not drinking right now."
    s "My bad. I didn’t realize I was supposed to be thinking ten steps ahead."

    scene iooutofit7
    with dissolve

    i "Why {i}step{/i} at all when jumping is so much more fun?"

    scene black
    with dissolve2

    "Io scrambles to her feet and is able to set her chair back up without much of an issue."
    "I’m not sure if I just caught her at the height of her drug-induced stupor but, fortunately, it appears to be in the early stages of wearing off right now."
    "She grabs her stepladder or, to paraphrase what she said just moments ago, the symbol of whether or not she is “really bad.”"
    "In some ways, though, the Io today seems worse."
    "Sure, she isn’t feverish or struggling to walk, but she seems almost numb to the fact that she’s leaving herself open."
    "I guess some might call that a good thing- that she’s comfortable enough with me to let her guard down in knowing that I won’t do anything to hurt her."
    "It’s just worrying when she lets that guard down before {i}I{/i} do."
    "Because sometimes, I hurt people without even trying."
    "Without even thinking about it."
    "And I do not want a reality where that becomes okay because the two of us decided to be someone else for a night."
    "........."
    "......"
    "..."

    scene iooutofit8
    with dissolve2

    "I am a marsh warbler."
    "I abandon the me from minutes ago and slip into a new reality- one where I don’t feel the need to restrain myself in favor of protecting someone else because the center of this world is {i}me.{/i}"
    "I am the one who needs to be protected. And the subsequent results of my decisions, while serving as occasional preventative measures, very rarely make things worse."
    "Things become worse on their own regardless of the choices I make or the things I do."
    "There are consequences that we face without knowing or understanding what even invokes them at times."
    "If the world is going to break, I am not going to be the one to break it."
    "If Io is going to break, I am not going to be the one to break her."
    "Especially when she’s just like the wires and rods keeping my heart propped up- spread too thin to spread anymore."
    "And so immeasurably shattered from the get-go that her further destruction would be impossible."
    "I jumped not because I thought it would be more fun."
    "I jumped because I knew it wouldn’t hurt me."

    i "See! Aren’t you so much happier now that we’re {i}both{/i} not our normal selves?"
    s "You seem more or less the same to me. Just a shade redder and...more animated with your hand movements."
    i "Heheh. Yeah. The Clonazepam always makes my limbs feel a little numb, so that just kinda happens sometimes. Uta likes making fun of it."
    s "I take it she sees you like this pretty often?"
    i "Oh yeah. It’s like the only time I can kinda keep up with her, too. I think we both kind of enjoy it in a way."
    i "She gets an Io who doesn’t complain about herself as much, and I get an Uta who...well, you know. It’s Uta. She’s always fun."
    i "Hey, what were you guys doing in the tea ceremony room thing the other day? That was weird."
    s "I think it was something about me being sad."
    i "Were you actually sad? Do you wanna talk about it?"
    s "No thanks. I can’t even really remember what it was about."
    i "Do you have depression, Sensei? I wouldn’t normally ask about something that directly because I hate when people do that for me, but this isn’t the {i}real{/i} Io speaking right now, so it’s cool if I do that."
    s "No clue. It wouldn’t surprise me if I did, but it’s not something I think I really need to know."
    i "I mean, {i}I{/i} would wanna know if {i}I{/i} had depression. "
    s "Do you...not?"

    scene iooutofit9
    with dissolve

    i "No! I don’t! That’s like, one of the only things I {i}don’t{/i} have! And it really pisses me off when people just {i}assume{/i} I have it because I don’t act how they {i}want{/i} me to, you know?!"
    i "Kirin asked me the same shit the other day and then started rattling off all this stuff about psychology like she actually {i}knew{/i} what she was talking about and I almost turned her into an art project!"

    scene iooutofit10
    with dissolve

    i "Now, asking if I take drugs that {i}treat{/i} depression is another story entirely since the usage of antidepressants extends far beyond depressive disorder, but do I actually have {i}depression?{/i} Fuck no!"

    scene iooutofit11
    with dissolve

    i "You’d think that shit with that disorder was annoying enough in the fact that everybody and their mother claims to have it now-"
    i "But the fact that it’s extended to the point where undiagnosed people are diagnosing {i}other{/i} people with it despite having zero understanding of how it works is just straight up ridiculous!"

    scene iooutofit12
    with dissolve

    i "Anyway, rant over. I’ve been holding that in for a while and it felt good to let it out, so thanks. Even {i}if{/i} you just did the exact thing that I was complaining about."
    s "Yeah...now I know for next time, I guess."
    s "If you don’t mind me asking, though, exactly what {i}are{/i} all of these medications for then? Besides anxiety, which I think everybody already knows about."

    scene iooutofit13
    with dissolve

    i "Honestly? I don’t even know what they’re trying to treat with some of them. I’m at the point where I just take whatever’s given to me without questioning it and watch as it fucks me up later."
    s "That...is extremely worrying."
    i "Worried my aunt at first too. In fact, I wouldn’t be surprised if it still worries her now. She just doesn’t let it show anymore."
    i "It’s obviously not like that for all of them, though. Some of this stuff I’ve been taking for, like...I don’t know, seven or eight years?"
    i "I just got to a point where I accepted that everything about me is broken and that some of it can be patched up by the shit they shove into orange bottles."

    scene iooutofit14
    with dissolve

    s "Hey, it can’t be {i}everything{/i} if you don’t have depression, right?"
    i "That’s a good point. The TLDR is that there’s a lot of me that hasn’t worked the way it’s supposed to since I was little. "
    s "TLDR?"
    i "Too long, didn’t read. You’re old."
    s "Thanks, Io."
    i "No, like really old. The cap is still on that bottle. And your glass is full."
    s "..."
    i "..."
    s "You don’t have any pills in here that treat dementia, do you?"
    i "I don’t think so. But the clinic I get my Ketamine from is open 24 hours and I can probably cash in a few of my broken girl punch-cards in exchange for a couple free doses. "
    i "I don’t think it helps with dementia, but it feels cool."
    s "I think I’m just...more drunk than I thought."
    i "I bet. I’ve only had sake a couple times, but I remember it being super strong and messing me up like, right away."
    s "Considering that this bottle is probably heavier than you, I’m not surprised."
    i "Can I try?"

    scene iooutofit15
    with dissolve

    s "Aren’t you on like eight hundred medications? There’s no way mixing alcohol with them would be a good idea."
    i "Nothing about tonight has been a good idea by most accounts. Plus, I’ve been watching you drink from that glass all night and I want to ham up the indirect kiss cliche."
    s "Okay. But I’m only agreeing to this because I’m also intoxicated and, if you actually die, I’m going to run away with Uta just to spite you."

    scene iooutofit16
    with dissolve

    i "You say that like it would be a bad thing."
    s "Wouldn’t it?"
    i "You and Uta? Not really. If that made you guys happy, I probably wouldn’t even mind dying."
    s "Io-"
    i "Don’t worry. I’m having too much fun right now to actually die."
    i "I’m just saying that the two people who matter most to me finding joy in the arms of one another wouldn’t ever be {i}bad.{/i}"
    i "I just wish it could be me in your arms instead."

    scene iooutofit17
    with dissolve

    i "Mnh...mm......mnh..."

    scene iooutofit18
    with dissolve

    i "Geh..."
    s "This never happened."
    i "Heheh..."
    i "That stuff...really is strong, huh?"
    s "Did you enjoy it at least?"

    scene iooutofit19
    with dissolve

    i "Yeah..."
    i "I got to taste your lips."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene iooutofit20
    with dissolve2

    "I turn off the lights and rest Io on the bed after she finally passes out."
    "But before you blame me, I didn’t let her have any more alcohol after that."
    "Does that absolve me of the fact that I let her have some in the first place? No. "
    "But it’s something she would have done on her own the moment I left either way. Being able to watch over her as it happens is surely better than the alternative, isn’t it?"
    "Like I said before, things are going to happen whether I want them to or not."

    scene black
    with dissolve2

    "Which is why, despite knowing that I am the last thing she needs, I want to keep seeing her."
    "I want to taste her lips as well."

    $ renpy.end_replay()
    $ iodorm25 = True
    $ io_love += 1
    stop music fadeout 7.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iospecial30:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iodorm:
    if io_love >= 5 and bathhouse5 == True and iodorm5 == False:
        jump iodorm5
    if io_love >= 10 and iodorm5 == True and iofirsthall == True and iodorm10 == False:
        jump iodorm10
    if io_love >= 15 and bathhouse10 == True and day != 5 and iodorm15 == False:
        jump iodorm15
    if io_love >= 25 and bathhouse25 == True and day != 5 and iodorm25 == False:
        jump iodorm25
...
```