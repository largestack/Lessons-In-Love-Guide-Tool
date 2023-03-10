# Normal-ish (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Everything Everywhere All At Once](./chapthree6.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: chapthree7
* Group: Main
* Triggered by label: chapthree6
* Chain sources: chapthree6
* Chain sources path: chapthree6

## Official wiki page

[Normal-ish](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chapthree7&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label chapthree7:
    "The cover of a thousand trees will not protect you from the light of the sun if the sun is determined to find you."
    "No amount of leaves or branches or wildlife willing to soak up the rays in your stead can successfully combat the stubbornness of a fiery god with an anger untamed."
    "But what reason is there to be angry when you have everything you’ve ever wanted?"
    "What is the purpose of looking down on someone who doesn’t?"
    "What is the cause for concern here?"
    "The sun will always find you."
    "It will always chase you."
    "And even if you’re able to find somewhere slightly out of its reach, it does not mean you’re out of its {i}sight.{/i}"

    scene rinmolly1
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "Open your eyes and tell me what you see."
    "Is it something completely devoid of a stubborn, fiery god?"
    "Or is it a park bench, just beyond the reach of the light? "
    "One that, even if it {i}weren’t{/i} carefully positioned twenty feet away from a tree older than everyone alive right now, would have its own form of shade."
    "One that, several seasons ago, would be warm to the touch and not chilled by the weight of a slowly detaching pair of misfits as everything about them grows colder day by day."
    "One that you wish you could see firsthand- from behind the corner of a school building, soaked in whatever it is that shades {i}you{/i} in your perpetual race from the light."

    play sound "static.mp3"
    scene rinmolly2 with flash
    stop sound

    "YOU CAN NOT RUN FROM IT"
    "YOU CAN NOT HIDE "
    "YOUR RESISTANCE WILL ONLY MAKE THINGS HARDER FOR THE ONES THAT YOU LOVE"
    "THE FURTHER YOU STRAY, THE CLOSER THE THREADS COME TO TEARING"
    "SPREAD THIN LIKE THE LIMBS OF A DYING CAT, IT ALL BECOMES WEAKER"

    play sound "static.mp3"
    scene rinmolly1 with flash
    stop sound

    "Until-"
    "Eventually-"
    "The only thing left of the thread is the memory of the weaver who weaved it."
    "The only thing left of the weaver is the memory of the thread she would weave."
    "You, too-"
    "Will burn in the light one day."
    "But for now-"
    "Take solace in the fact that you still have the energy to run."

    r "..."
    mo "..."
    r "So, uhh..."
    r "Summer...right?"
    mo "..."
    r "..."

    scene rinmolly3
    with dissolve

    r "Hah..."
    r "Okay, listen."

    scene rinmolly4
    with dissolve

    r "I know what it’s like to want something or...{i}someone{/i} you can’t have. "
    r "And I know that...being so close to whatever that thing or...person is can...make you do things you’re not proud of."
    r "I do tons of shit I’m not proud of all the time. That’s basically like, half of what I’ve done ever since I was born."
    r "I got burned {i}hard{/i} when I confessed to Chika. Hard enough that, even today...even when I have someone I’m genuinely happy with..."
    r "It {i}still{/i} hurts when I look at her."
    r "So...if you’re anything like me...which I know for a fact you are..."
    r "I’m sure it’s the same."
    r "And that sucks...that sucks a lot..."
    r "And if you would have asked me what I would do if I were in Chika’s position back then, I’m sure my answer would have been a lot different than...what actually happened once I {i}was.{/i} You know?"
    r "It’s...hard. "
    r "It’s awkward.."
    r "It’s-"

    scene rinmolly5
    with dissolve

    mo "It’s my fault. I {i}know{/i} it’s my fault. I just...I’m really bad at holding myself back when-"
    r "It doesn’t have to be {i}anyone’s{/i} fault, Molly."
    r "How am I, the queen of shitty impulsive decisions, going to forever hold the shitty impulsive decision of {i}someone else{/i} against them?"

    scene rinmolly6
    with dissolve

    mo "Wait...you’re not...saying you forgive me, are you?..."
    r "..."
    mo "Is that what you wanted to talk about? You...you wanted to tell me that we can move past this? That we can go back to being friends?"
    mo "Because I can do it, you know? I can hold back. I can-"
    r "That’s not what I’m saying."

    scene rinmolly7
    with dissolve

    r "In fact, that’s kind of the opposite of what I’m saying."
    mo "But...But you-"
    r "You still...you know...{i}like{/i} me...don’t you?"

    scene rinmolly8
    with dissolve

    mo "Well, I...I can’t just {i}stop.{/i}"
    mo "I’ve liked you...pretty much ever since we met..."
    mo "I always thought you were like a...cooler...less awkward and...more Japanese version of me..."
    r "Me? {i}Less{/i} awkward? That’s new."
    mo "I saw myself in you. But it was like...a better version of myself. One that actually figured out a way to fit in with people outside of my bubble."
    mo "One that {i}wanted{/i} to fit in outside of my bubble..."
    mo "Someone who could look at someone {i}so{/i} different from them and still manage to see so much good that it would...transcend feelings of friendship and evolve into something greater."
    mo "Coming to understand that should have been the nail in the coffin."
    mo "Coming to understand that should have been the thing that made me think, “Molly...just give up.”"

    scene rinmolly9
    with dissolve

    mo "Molly...you’ll never be the type of girl she wants."
    mo "Molly...you’ll never be anything more than an awkward, unattractive loser who lives in her own world!"
    mo "You’ll never be anything more than that! Of course the better version of you would see it! Of course she would-"
    r "Molly, stop. Come on."

    scene rinmolly10
    with dissolve

    mo "Do you think I don’t want to?!"
    mo "Do you think I wanted to lose my best friend?! That I wanted to...{i}force{/i} my feelings on her?! That I wanted to disregard the things I {i}knew{/i} because I was too afraid to believe them?!"
    r "Of course not..."
    mo "Then-"
    r "But you {i}did.{/i}"

    scene rinmolly11
    with dissolve

    r "You {i}did{/i} do all of those things despite knowing how I felt. {i}That’s{/i} what I’m more upset about than anything else."
    r "I can look past the shitty impulsive decisions like that kiss on Christmas and...and I can even look past the whole tackling thing."
    r "But, no matter how hard I try, the one thing I {i}can’t{/i} look past is how you straight up ignored my feelings because you didn’t want to accept them."

    scene rinmolly12
    with dissolve

    mo "But you didn’t even {i}understand{/i} mine! That’s even worse!"
    r "Is it?"
    mo "Yes!..."
    mo "No?..."

    scene rinmolly13
    with dissolve

    mo "Maybe?..."
    mo "I don’t even know anymore..."
    r "If you think what I did is worse, fine. That’s something we’ll just have to disagree on."
    r "But if I fully understood how you felt and that what I was doing was going to hurt you, I never would have done it."
    r "You see yourself in me, don’t you? You see a girl who gets excited about the smallest things and can’t hold back her excitement when a huge, life-changing opportunity presents itself."
    mo "I see a girl who doesn’t get opportunities like that."
    mo "Of course I would be jealous when the one I’ve been admiring this whole time does."
    r "Are you happy for me, Molly?"

    scene rinmolly14
    with dissolve

    mo "What?..."
    r "Are you happy for me now that I finally have someone who likes me the same way I like them?"
    mo "Of...Of course..."
    r "And you really mean that? You’re not just saying it because that’s what I want to hear?"
    mo "Rin..."
    r "Just be honest. I’m not going to get mad."
    mo "..."
    r "..."

    scene rinmolly15
    with dissolve

    mo "I really am happy for you..."
    mo "And I’m even happier that the girl you like is so great and...good for you."
    mo "But what I’m most happy about is that you don’t have to feel the way I feel right now."

    scene rinmolly16
    with dissolve

    r "You know, after Chika rejected me...someone else who was equally as important at the time told me, “There are plenty of things in life that are going to hurt just as bad as this.”"
    r "And while that person isn’t really known for their amazing life advice, I think those words are exactly what you need right now."

    scene rinmolly17
    with dissolve

    r "Just look at me. I had to fall on my ass harder than ever before I wound up with somebody I wanted to be with."
    r "You might be hurting right now, and it might feel like the whole world is crashing down around you..."
    r "But one day, you’re going to find someone else you can see yourself in. And when that happens, this will all feel like just a blip on the radar."
    mo "But..."
    mo "That person won’t be you..."

    scene rinmolly18
    with dissolve

    r "No..."
    r "That person won’t be me."
    mo "..."
    r "I’m glad you wanted it to be, though."
    r "Only two people have ever liked me."
    mo "Three counting Sensei. He likes you too."
    r "Sensei likes everybody. He doesn’t count."
    mo "What a life it must be...waking up as the protagonist of an H-game every morning..."
    r "What a life indeed..."

    scene rinmolly19
    with dissolve

    mo "Well, umm...anyway...does..."
    mo "Does this mean we don’t have to avoid each other anymore?"
    r "..."
    mo "I can’t promise that my feelings for you will just vanish, but...I think the fact that you actually wanted to talk about this means that things..."
    mo "Things can go back to normal?..."
    r "Molly..."
    r "I don’t know if there will ever be a “normal” for us after this. "
    r "And if there ever is, I don’t think that just one talk will be enough to get us there."
    r "I still think it would be good for us to sort of...distance ourselves and...focus more on people we {i}don’t{/i} really relate to the way we do."
    r "But..."
    r "I’m not mad anymore. "
    r "Well, technically, I {i}am{/i} still a little bit mad. But that’s mostly because you both stole my first kiss and then proceeded to almost steal my virginity at the beach."

    scene rinmolly20
    with dissolve

    mo "Th-That wasn’t-"
    r "Relax...it was just a joke. "

    scene rinmolly21
    with dissolve

    mo "Oh...S...Sorry."
    r "Either way, I still think a little distance would be best for us right now. But it’s not like I’m going to avoid you or anything since we still have a lot of the same friends."
    r "Just...don’t expect any late night eroge marathons anytime soon."

    scene rinmolly22
    with dissolve

    mo "That’s fine. I’ve had my fill of them for the meantime anyway."
    r "Oh. Well, I see that you and I handle our sadness a little bit differently. "
    mo "And I’m sure you’ll hear much more about just that at our next club meeting..."

    scene rinmolly23
    with dissolve

    r "Um..."
    r "Actually..."
    r "That was kind of the...big thing I wanted to talk about today."
    r "I just figured that...we wouldn’t really be able to talk about {i}anything{/i} with the way things were between us and...it’s not like I {i}wanted{/i} things to be bad anymore. "
    mo "You...wanted to talk about..."

    scene rinmolly24
    with dissolve

    mo "Wait...are you-"
    r "I, Rin Rokuhara..."
    r "Hereby formally resign from the manga club."

    scene rinmolly25
    with dissolve

    mo "But...what?!"
    mo "No! You can’t! You won’t! You love manga!"
    r "I {i}do{/i} love manga, yes."
    r "But there’s always been something else I’ve loved even more."

    scene rinmolly26
    with dissolve

    mo "Damn it, Otoha! Just how much will you steal from me?!"
    r "I, uhh...I was talking about music..."

    scene rinmolly27
    with dissolve

    mo "Are you really leaving?...Can’t you just...play music in your free time?"
    r "I want to play as much as I can whenever I can. And as a fellow otaku, I know you’re the same way with your hobbies."
    r "I’ve finally got an opportunity to play more...to see my girlfriend more...and to hang out with a new group of friends that all share my biggest love with me."
    r "There was no way I was going to turn that down..."
    r "Plus...this might give you and me the space we need to kind of...get back to normal-ish...don’t you think?"

    scene rinmolly28
    with dissolve

    mo "I don’t want you to leave..."
    r "I’m not “leaving.”"
    r "I’m just trying something new."
    r "And hey, if I don’t fit in or I just suck or something, I might come running back."
    r "But seeing as you’re the club president...and my {i}friend...{/i}I needed you to know that."
    r "But hey, with the whole club reassignment thing going on, I’m sure someone just as cool as me will fill my space in no time at all."

    scene rinmolly29
    with dissolve

    mo "Hah...I do hope so. Ami and I have been doing our best trying to recruit new members over the last several days, but even the Kendo Princess seems to be on the fence."
    r "Well, Tsuneyo is {i}way{/i} cooler than me, so maybe you should try aiming a little bit lower?"
    mo "Are you sure this is what you want, Nithhala?"
    r "Are you really going to use my D&D name when it was that exact game that got us into this mess in the first place?"

    scene rinmolly30
    with dissolve

    mo "It was never about that."
    mo "That was just one more example of me trying to keep you from slipping away."
    mo "But I suppose you’ve slipped far enough by now that there’s no way I’ll ever pull you back."

    scene rinmolly31
    with dissolve

    r "You won’t have to pull me {i}at all{/i} for at least one night of every week since I think we’re ready to start the campaign back up now."
    r "But every other night, your girl’s gonna be workin’ on becoming a rock star."
    mo "You’ll always be a rock star to me, Rin."

    scene rinmolly32
    with dissolve

    r "Dude, cringe. You sounded like my mom just now."
    mo "I mean it, though. I’ll always admire you. It doesn’t make much of a difference if it’s from up close or afar."
    mo "Just stay within sixty feet and I’ll always be able to reach you in one turn."
    r "Uhh...sixty feet seems a little close, don’t you think?"
    mo "Enjoy your new club, Rin..."
    mo "I hope it will be one you don’t slip away from."

    scene rinmolly33
    with dissolve

    r "Here’s hoping it won’t be, I guess."
    mo "Aye. Here’s hoping it won’t."
    r "Still homies?"
    mo "Still homies."

    scene rinmolly34
    with dissolve

    mo "Also, have I mentioned how much I love your new uniform yet? Or did the ever growing distance between us prevent my words from reaching you?"
    r "You’re free to admire it all you want. Just don’t try to tackle me this time."

    scene rinmolly35
    with dissolve

    mo "Mm..."
    r "Kidding! Now, let’s head back inside and sign away our respective destinies to yet another year’s worth of club activities and friendships."
    mo "Aye. I hope I don’t accidentally trip and land on top of you along the way..."

    scene black
    with dissolve2
    stop music fadeout 8.0

    "Somehow or another, the sun slipped away."
    "The gaze of a god disappeared along with it."
    "Somehow or another, things turned out okay."
    "And two girls poised to burn somehow remained hidden."

    $ renpy.end_replay()
    $ chapthree7 = True

    "........."
    "......"
    "..."

    jump chapthree8

label chapthree8:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
to "That’s exactly right! Remember to smile! For, if you don’t-"

    play sound "static.mp3"
    scene happy3 with flash
    scene happy4 with flash
    scene happy5 with flash
    scene newsummerstuff29 with flash
    stop sound

    mo "Kendo Princess of...wherever we designated as your place of origin is!"
    t "Tojo Ramen, home of the noodle."
    mo "That was...definitely not it! But that is not what matters right now!"
    a "That’s right! What matters is that you, Tsuneyo Tojo, join {i}us-{/i}"
    mo "Molly and Ami! President and peon!"
    a "In the school’s manga club!"

    scene newsummerstuff30
    with dissolve

    mo "Now, I know what you must be thinking. But for the purpose of this sales pitch, I will now have Ami read your mind. Ami, go!"
    a "Noodles."

    scene newsummerstuff31
    with hpunch

    t "Get out of my head! The Tojo family’s secret recipes are in there!"
    mo "Read the other thing, Ami! Not the noodle part!"
    a "Right, right...umm...uhh...it’s a little blurry, but...I think it’s saying...{i}I want to join the manga club!{/i}"

    scene newsummerstuff32
    with dissolve

    t "The girl with the nice legs knows my thoughts before even I do. How can this be?"
    mo "You see, Kendo Princess...the manga club isn’t {i}all{/i} about manga...it is about companionship! Camaraderie! Cosplay! But most importantly..."

    scene newsummerstuff33
    with dissolve

    a "It’s about comparing ships and then arguing with each other about it!"
    mo "Precisely!"
    t "I have heard of this. I believe that is called a “yacht club.”"
    mo "Not that kind of ship, Kendo Princess! The kind with two characters who are meant to be together!"
    t "As long as they are able to put aside their feelings while on the job, I am sure everything will be fine."
    t "But why do you want me in your yacht club? I know nothing about boats {i}or{/i} manga."
    mo "Not yet, you don’t! But you have been trying and that is all that matters! "
    mo "You see, manga club isn’t some elitist group of girls who will tell you what to watch and when-"
    a "It’s a group of nerds who love nerd stuff and want to act like nerds in the same room as {i}other{/i} nerds without being judged!"
    mo "It’s a group of great friends who support each other and cheer each other on when things get bad!"
    a "It’s a group where we are all unified in one thing! The belief that One Piece has too many episodes!"
    mo "And a group where, no matter how hard I try, I can’t get anyone to watch Jojo’s Bizarre Adventure with me!"
    r "Hey, I watched the whole first season with you, didn’t I?"

    scene newsummerstuff34
    with fade

    r "Sure, I never kept going after that since it definitely wasn’t my cup of tea...but I tried, you know?"
    mo "..."
    r "..."
    a "{i}Tsuneyo, this is the kind of ship we were talking about just now.{/i}"
    t "Oh no. I forgot to buy a ticket."
    mo "Uh...um..."
    mo "I..."
    mo "I don’t..."

    scene newsummerstuff35
    with dissolve
    stop music fadeout 20.0

    r "Can we talk?"
    r "I don’t think it’ll take long, but...there are a few things I need to say and...well, I kind of need to say them before the day is over."
    mo "You...want to talk to {i}me?{/i}"
    r "Do you really think I would have done something as awkward and uncomfortable as this if I didn’t?"
    r "I obviously know shit’s weird for us right now and-"

    scene newsummerstuff36
    with dissolve

    r "And, uhh..."
    r "Umm..."
    r "Actually...can we do this outside? Sensei won't care if we leave and...it’s not really something that I want other people listening in on."
    mo "Y...Yeah."
    mo "Yeah, we can talk. That’s fine."
    mo "Can it be in the shade, though? The summer sun is cruel to this Irish skin and getting into spandex with sunburn is a horrible experience that I do not want to relive."

    scene newsummerstuff37
    with dissolve

    r "Yeah...I’m sure we can find somewhere with shade..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ chapthree6 = True

    "........."
    "......"
    "..."

    jump chapthree7
...
```