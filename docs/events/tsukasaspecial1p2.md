# Jeeves Tsukioka XIII
Tsukasa event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsukasaspecial1p2&go=Go)


Part of event chain [National Tsukasa Day](./tsukasaspecial1.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Chinami: Death Trap](./chinamidate25.md)

## Event properties
* ID: tsukasaspecial1p2
* Group: Tsukasa
* Triggered by label: tsukasaspecial1

## Event code
File: \game\TsukasaEvents.rpy
Code:
```python
...
label tsukasaspecial1p2:
    if _in_replay:
        play music "10c.mp3"

    scene tsukasaoffice1
    with dissolve2

    "But not without a very special {i}guest...{/i}"

    tk "I’m bored. "
    s "Well, you had the opportunity to leave when that convoy of limos showed up, but you decided to follow me here instead. So you did this to yourself."
    tk "Tsukasa Tsukioka deserves more than just a convoy of limos. If Mother thinks she can buy me off with just that, she is sorely mistaken."
    s "I can’t imagine buying you off {i}at all{/i} is feasible considering how numb you already are to money at your age but, to satisfy my own curiosity, what {i}will{/i} it take for you to leave?"
    tk "I’m making Mother come here to get me on her own. It isn’t fair that I should have to be surrounded by lowly peons on my own national holiday."
    s "I thought your mother was busy?"
    tk "She won’t be if I ask enough. That’s just how important I am."

    "In just seven hours, I have gone from the world’s most sexually active teacher to the world’s most exhausted teacher."
    "Well, after Wakana- who I’m consistently shocked to see roaming the halls despite looking like she is going to drop dead at any moment."
    "Regardless, I must now play babysitter while waiting for someone to come take this brat off of my hands."
    "I guess you can call it practice for when I have to visit Chika’s house and watch both her {i}and{/i} Chinami soon, but at least then I’ll have Chinami to keep her occupied. And Touka to keep {i}me{/i} occupied."

    tk "Jeeves, tell me a story."
    s "No."

    scene tsukasaoffice2
    with dissolve

    tk "But it’s-"
    s "I know what day it is. But I will not be bossed around in my own office by someone I could pick up with one hand. "
    tk "If you’re not going to tell me a story, can you at least do {i}something{/i} to keep me entertained?"
    s "Like what?"
    tk "How am I supposed to know? You’re the adult here. Aren’t you supposed to be full of guidance and wisdom?"
    s "I don’t think you’re old enough for my guidance and wisdom yet."
    tk "What about that game you were playing with the peasant girl at the onsen?"
    s "I really hope your mom gets here within the next thirty seconds because that is a road that even I am not ready to traverse just yet."

    scene tsukasaoffice3
    with dissolve

    tk "Hah...Of course it’s not. This Tsukasa Day sucks. It’s like nobody is appreciating me any more than they normally do. "
    tk "The only difference is I got to go to high school. And even that wasn’t very fun."
    s "I’m not sure what you were expecting, but school isn’t really known for being “fun.”"
    tk "Not like I would know. I’m not allowed to go to school."
    s "Not allowed? Or just not willing to settle for a commoner school?"
    tk "I would settle for a commoner school if I had to. "
    tk "I’m the second in line to inherit the Tsukioka family business, so it’s not like I {i}have{/i} to get the highest form of education when my older sister is going to be the one to take over."
    tk "Unless staying here makes her brain turn into mush. Which, based on what I have seen here today, it might. "
    s "While what you say may be true, I’m not really sure what that has to do with you not being {i}allowed{/i} to go to school."
    tk "Mother says I’m too “advanced” to go to school with girls my age and too young to go to school with Big Sister."
    tk "So all I can do is sit at home and listen to boring old people talk about boring stuff when what I {i}really{/i} want to do is have fun."
    s "I’ve been to your house. I have a hard time believing there isn’t anything fun to do there."

    scene tsukasaoffice4
    with dissolve

    tk "Nothing’s really fun if you do it every day. Which is why I like going out and seeing other stuff that I’m not able to see at home. Like tacos. Or “the subway.” "
    tk "Or that very pale girl with the freckles who kept talking about demons."
    s "That’s Molly and she isn’t really a tourist destination."
    s "In fact, none of the things you listed are tourist destinations and you should probably do a little more research if you really want to see the outside world."
    tk "Maybe."

    scene tsukasaoffice5
    with dissolve

    tk "Or maybe you can officially accept the job as the new Jeeves Tsukioka the Thirteenth and we can go on all sorts of commoner adventures that-"
    s "No."

    scene tsukasaoffice6
    with dissolve

    tk "You are being very rude to me, Jeeves. This sort of behavior will not be tolerated."
    s "Fuck you."

    scene tsukasaoffice7
    with dissolve

    tk "Ah! I’m telling Mother that you cursed at me! "
    s "Do it. I’m pretty sure she’ll understand."
    tk "Nuh-uh! Cursing at a child is something adults should never do! I’ve gotten at least ten other Jeeves fired because of that."
    s "If ten other Jeeves cursed at you, don’t you think the problem might be...I don’t know, {i}you?{/i}"

    scene tsukasaoffice8
    with dissolve

    tk "Tsukasa Tsukioka isn’t a problem. She is gifted and talented and richer than you and everyone else you know combined."
    s "I know your sister, you know. And, unless she is a pathological liar who is only attending this school because she was excommunicated from your family, I’m pretty sure {i}she’s{/i} rich too."
    tk "She might as well be excommunicated with how often she talks about her new fun and exciting commoner life."
    tk "It’s like she doesn’t even remember we’re better than you or something."
    s "Or...she’s just starting to realize you’re not?"

    scene tsukasaoffice9
    with dissolve

    tk "But we are."
    s "How?"
    tk "We’re smarter and cleaner and more sophisticated and cleaner and are trained in a variety of different skillsets that people like you aren’t exposed to. And also, we are cleaner."
    s "I don’t know where this strange fascination with our personal hygiene comes from, but there are plenty of people out here who are just as talented as you and Touka."
    s "Like Tsuneyo. She was a national kendo champion and now she is a...noodle warrior."
    tk "A...noodle warrior?"
    s "And then there’s Otoha who’s, like...some singing prodigy or something. And Nodoka, who is also prodigal in a lot of ways when she isn’t ruining the lives of ex-Yakuza."
    tk "What about the one girl with the ponytail who kept glaring at you all day? What’s she really good at?"
    s "Uhh..."

    scene tsukasaoffice10
    with dissolve

    s "She’s good at..."
    s "..."
    tk "..."
    s "Eating?"
    tk "That doesn’t sound very impressive to me, Jeeves. If you were trying to make me realize how interesting you people can be, you should have stopped at the Yakuza part. "

    scene tsukasaoffice11
    with dissolve

    s "The fact of the matter is that there’s just a lot more to what makes a person good than how talented they are or...how “clean” they are."
    tk "Like what?"
    s "Like how...nice they are. How open to change they are. How adaptable and versatile they can be in all types of situations."
    tk "And who out of all of your students do you think is the best at all of those things?"
    s "..."
    tk "..."

    scene tsukasaoffice12
    with dissolve

    s "Touka."
    tk "See, Jeeves? The Tsukioka family is just flat out better than everybody you know."
    s "Some members at least. Others...I’m not convinced yet. But sure, you win this round, Tsurumi."

    scene tsukasaoffice13
    with dissolve

    tk "Of course I win! A Tsukioka does not pick losing battles. Not that there are many battles we’d lose in the first place, but still. "
    s "You are easily the most prideful person I have ever met and you probably can’t even ride a bike yet."
    tk "I don’t own a bike, but Big Sister lets me ride Morning Glory sometimes and I haven’t fallen off yet."
    s "Look at you, not even owning your own horse yet. And you call me a commoner."
    tk "I own seven horses. They’re just all display pets."
    s "What good is a display horse?"
    tk "You’d know if you could afford one. But sadly, unless you accept my proposition and become a real Jeeves, you never will."
    s "How did you get like this when both of the other Tsukioka women are so approachable and kind?"

    scene tsukasaoffice14
    with dissolve

    tk "Some people are just born with the gift, I suppose."
    s "Is it too late to return it?"
    tk "When you’re as rich as Tsukasarumi Tsukioka, you don’t have to return anything. You can just buy something else."
    s "On second thought, I’m just going to blame your father as I can’t imagine Tsubasa or Touka having this sort of influence on you."

    scene tsukasaoffice15
    with dissolve

    tk "It’s not Papa’s fault I’m like this. It’s probably just a side effect of being the second born in a family that typically only produces one heir."
    tk "Besides, I don’t see him that much anyway. He’s always doing stuff and never has time for me anymore."
    s "Really? With how much you talk about him, I figured you bothered- err...I figured you were {i}with{/i} him all the time."
    tk "Not really. I try to talk to him as much as I can, but I think he forgets to charge his walkie talkie sometimes."
    s "Walkie talkie?"
    tk "Mhm. Santa brought me a walkie talkie a few years ago so I could talk to Papa whenever I wanted. "
    s "Does he not have a cell phone?"
    tk "He does. But he says that it’s for work only and that I’m not allowed to call him on it during the day."
    s "I see..."
    s "What do you spend most of your time at home doing then?"
    tk "Whatever I want. Drawing pictures. Swimming. Shifting all of Big Sister’s furniture that isn’t too heavy slightly to the left and watching her get confused."
    tk "Oh, and getting the staff to do my bidding. Can’t forget about that. I have lots of bidding that needs to be done."
    s "..."

    "Her story reminds me of one I’m much closer to-"
    "Of a girl who can barely speak about her father to me without the joy draining from her eyes as she slips into quiet reflection."
    "And while I feel I should be worrying that something like this may one day happen to Tsukasa as well-"
    "Instead, I find myself wondering if Ayane saw the world through such unfortunate glass."
    "I’m sure that a lot of that is due to the fact that I just don’t really care about Tsukasa yet...but at least it helps me understand her."
    "It’s not at all unique for children to act out when they aren’t getting adequate attention from their parents after all."

    play sound "knock.mp3"
    scene tsukasaoffice16
    with dissolve

    "But Tsukasa {i}is{/i} still getting attention from one of her parents. "
    "Maybe even a little {i}too{/i} much attention if that parent is dropping what they’re doing just to come over here and pick them up despite a whole convoy of cars sent to do just that."
    "It’s just not the parent she wants, I guess."

    tb "Tsukasa, dear...please tell me you are in there..."
    tk "About time, Mother. It’s been almost an hour and this room isn’t even climate controlled. And Jeeves is {i}soooooo{/i} boring."
    tb "Jeeves? But you fired Jeeves last- oh. Oh, Tsukasa! That is so rude for someone who’s done so much for our family in just a short while!"
    tk "All he’s done is get Big Sister to blab about him and the rest of her new friends all day long. Doesn’t that bother you? "
    tb "Not at all, dear. Your sister is finally-"
    s "You know you can come in, right? You don’t have to talk through the door."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    tb "Oh! Silly me. I probably would have stood there all day if you hadn’t said that."

    scene tsukasaoffice17
    with dissolve

    tb "I’m terribly sorry for any trouble my youngest daughter may have caused you. I truly didn’t expect her to refuse {i}all{/i} of our drivers when she knew I was busy, but...Tsukasa will be Tsukasa, I suppose."
    tk "It’s National Tsukasa Day. I didn’t want to go home with someone being paid to care about me."

    scene tsukasaoffice18
    with dissolve

    tb "But what about your sister? Couldn’t you have gone with her instead of burdening her teacher?"
    tk "Burden?"
    s "It’s really no big deal. I’m usually here for an hour or two after class anyway. Tsukasa just sat on the couch. "
    tb "Tsukasa should have been a good girl and left school with one of the drivers {i}like we agreed to this morning.{/i}"
    tk "But I wanted {i}you.{/i} "
    tk "And you told me we could get ice cream after I finished my first day of high school to celebrate."

    scene tsukasaoffice19
    with dissolve

    tb "Darling...that was when I assumed I didn’t have to take an hour away from my meetings just to come and get you. "
    tb "I’m not sure if we’ll have time anymore, dear. "

    scene tsukasaoffice20
    with dissolve

    tk "But...Tsukasa Day..."
    tb "Thank you again for watching over her, Sensei. I really do appreciate it."
    s "Yeah...no worries."

    scene tsukasaoffice21
    with dissolve

    tb "Come along, dear. Sensei’s time is just as valuable as ours and we have taken up enough of it."
    tk "Yes, Mother..."
    tk "Bye bye, Jeeves..."

    play sound "dooropen.mp3"
    scene tsukasaoffice22
    with dissolve

    "Tsukasa exits the office and..."
    "And I somehow feel a little bad for her."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "The feeling fades shortly after, though."
    "Things like that don’t normally last long for me."
    "But the fact that it came at all tells me she’s no longer just an arrogant waste of space in my mind."
    "She’s a girl, just like everyone else, trying to figure out how she best fits into this world."
    "And all things considered, that’s a lot better than just staying put and deciding you don’t belong at all."

    $ renpy.end_replay()
    $ tsukasa_love += 5
    $ tsukasaspecial1p2 = True

    jump afterschoolevent
...
```

## Code that triggers this event
File: \game\TsukasaEvents.rpy
Code:
```python
...
ima "Special game?..."
    ima "Onsen?..."
    c "Hahaha! Kids, right?! Always making up stories!"
    s "Oh, look. A stack of papers way at the...other end of the school that I need you to file."

    scene tsukasaday22
    with fade

    ima "..."
    s "..."
    ima "..."
    s "..."
    ima "You trying to teach Chika how to time travel, Senpai?"
    s "I have no idea what you’re talking about."
    ima "And at an {i}onsen?{/i} What does that mean for all of the other girls who had to stare at your drab-ass wallpaper while you were doin’ ‘em dirty?"
    s "Is that really what you’re most concerned about?"
    ima "I’m an advocate for equality, Senpai. We {i}all{/i} deserve onsens."
    s "Well, I’ll add you to the top of my...prospective onsen visit list now."
    ima "Think saying that might be giving me a little too much attention on National Tsukasa Day, don’t you think?"

    scene tsukasaday23
    with fade

    tk "MMMFMFMFMFMFFHFHFHFFMMFMFM!!!!!!!! MMMMM!!!!!!!"
    to "Tsukasa, what does Mother say about making a racket like that? Quiet down or you’ll attract negative press."
    tk "MMMMMMMMMM!!!!!!!!!!!!"
    c "Tsukasa...I’m gonna let you go now. {i}But I kinda need you to not say anything about the onsen, okay? Nobody is supposed to know about that.{/i}"
    tk "MMMM! MMMMM! MMMM!!!"

    scene tsukasaday24
    with dissolve

    tk "Are you out of your mind?! Do you have any idea who I am?! Do you think it’s okay to just assault a princess?! I will have your head!"
    c "But if you kill me, Chinami won’t want to do business with you anymore, so...your success kinda hinges on me in a way, doesn’t it?"

    scene tsukasaday25
    with dissolve

    tk "While it {i}is{/i} true that an ally like her would certainly take us to the next level, I’m not quite sure if it is worth my own personal safety."
    c "What if I...promise not to grab your face anymore?"
    tk "That would be a start...but I am going to need something a little more than that."
    c "Uhh..."
    c "You can eat...cereal when you come over to my place?"

    scene tsukasaday26
    with dissolve

    tk "C...Cereal? But Mother says cereal is a leading cause of diabetes and that there are much tastier and healthier alternatives."
    c "And while I’m sure she’s right...you {i}do{/i} want a taste of commoner life, don’t you? What better taste than eating the same thing Chinami eats every morning {i}inside{/i} of Chinami’s house?"
    c "Think of it as a...research...project."

    scene tsukasaday27
    with dissolve

    tk "You drive a hard bargain, peasant. That does sound like something that tickles my interest. However, I have one final adjustment I’d like to add to your offer."
    c "And that...adjustment is?"

    scene tsukasaday28
    with dissolve

    tk "Can my sister come too?"
    to "What?"
    tk "It wouldn’t be fair if I got to experience something like that firsthand and she did not. I am simply doing this so that the two of us may remain on equal footing."
    tk "It is the least I can do in exchange for intruding on her personal life by being here."
    to "Tsukasa...I don’t really need to-"
    c "Sure, yeah. That’s actually..."

    scene tsukasaday29
    with dissolve

    c "You know what? Why don’t we invite Sensei too?"
    s "What?"
    tk "That seems unnecessary. Jeeves has no place in the same room as two serious and powerful businesswomen. And also Onee-chan."
    to "Why is Sensei...suddenly a part of this as well, Chika?"
    c "Because I was looking for a good time to go do something lately and kind of need a babysitter since I have no idea how long it will take."
    c "Which isn’t to say I don’t trust you, Touka. I just...don’t really know if you'll be able to grasp any of the, uhh...commoner technology at my place."
    s "I mean...I guess I can come? I doubt I’ll be much help, though."
    tk "Jeeves can wait in the lobby while the rest of us talk. That seems fair to me."
    to "I don’t believe Chika’s home is the type to have a lobby, Tsukasa. Sensei can wait in her rose garden instead."
    s "..."
    c "Sensei? You cool with that?"
    s "Depends. Do you have a rose garden now?"
    c "Who doesn’t?"
    to "Told you so, Tsukasa. You should listen to me more often."
    tk "Stop making so many silly decisions and I will."

    scene black
    with dissolve2

    "Somehow, I wound up getting roped into agreeing to be a babysitter for both Chinami {i}and{/i} Tsukasa soon."
    "That doesn’t sound exhausting at all."
    "Thankfully, I’ll at least have Touka there with me. And while that probably won’t really help either, it will definitely help me feel a little more {i}normal{/i} as there’s at least someone who isn’t..."
    "Well, someone who isn’t a full blown child there."
    "Plus, an environment like that sounds like the perfect place to fuck with her. And that is quickly becoming one of my favorite past times."
    "Anyway, the day comes to an end- and I find myself retreating back to my office."

    $ renpy.end_replay()
    $ tsukasaspecial1 = True

    jump tsukasaspecial1p2
...
```