# I Died With You (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 35

* Event [Ten Steps Forward](./rindorm35.md) (Rin) is completed)

* rininvite equal to True (unknown variable)



## Next events

None

## Event properties

* Id: cafe35
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe
* Triggered by path: cafe->cafe35

## Official wiki page

[I Died With You](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe35&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe35:
    scene firstotoha1
    with dissolve
    play music "justbehappy.mp3" fadein 4.0

    "I wind up showing up to the cafe after taking an obnoxiously long detour."
    "The path I normally take here was completely blocked off for construction or something so, after an extra fifteen minutes of finding an alternate route, I’m finally here."

    scene firstotoha2
    with dissolve

    f "Oh, good morning."
    f "We were just wondering when you were going to show up."
    s "Oh, right. Rin’s post-heartbreak excursion is today."
    s "I may or may not have forgotten about that."

    scene firstotoha3
    with dissolve

    f "So you just happened to show up at the cafe at the exact time we were supposed to go out on accident?"
    s "Yeah, kind of. "
    s "I would have shown up fifteen minutes earlier but I think they’re building something nearby."

    scene firstotoha4
    with dissolve

    f "Is that what all of that traffic was about? I had no idea. "
    f "We came from the opposite direction, but some of the roads were backed up over there as well. "
    f "I wonder what they’re building?"
    s "Beats me."

    "I look around the cafe, expecting to see Rin behind the counter or something, but can’t seem to find her at all."

    s "So, where’s our leader?"

    scene firstotoha2
    with dissolve

    f "In the bathroom doing her makeup. "
    f "She’s feeling much better today."
    s "Really? What happened?"

    scene firstotoha3
    with dissolve

    f "If anyone should know what happened, it’s you."
    f "Rin told me you were the one who let Chika into the room the other night so the two of them could talk."

    scene firstotoha2
    with dissolve

    f "Well, apparently that talk went really well."
    f "And even though nothing has really changed since then, she’s definitely held her head up a little higher."
    r "Hm? Who you guys talkin’ about?"

    scene firstotoha5
    with dissolve

    "Rin rounds the corner and stops in front of me, playfully punching me in the arm and feigning obliviousness to the fact that we're talking about her."

    s "Welcome back to the world of the living."
    r "Thank ya! Glad to be here!"
    r "And thanks again for all of your help since the beach. "
    r "I already thanked Futaba like six million times, but I really don’t think I would have gotten over this so quickly if it weren’t for you two."
    f "There’s no need to thank us. We’re just happy you don’t look like a zombie anymore."

    scene firstotoha6
    with dissolve

    r "As am I, dearest Futaba. "
    r "I can finally venture forth and be among normal people once again. It feels great to be alive."

    scene firstotoha7
    with dissolve

    r "Do you know the plan, Sensei?"
    s "Nope. I honestly still don’t even know where we’re going."
    r "Ohohoh, then you’re in for a treat."
    r "We’re returning to our native land at the far reaches of the outer-barrier."
    s "The what?"
    f "She means the area where our old school is. "
    f "Some people call it the outer-barrier because of the wall that was erected to prevent people from leaving the city."
    s "Is there an...inner barrier?"
    r "Nope. Just the outer one. But that’s beside the point."
    r "All you need to know is that you’ll be seeing our old stomping-ground for the first time."
    r "I haven’t been there ever since we moved, so I might be a little lost. But Futaba is there pretty often so she’ll be able to show us around."
    s "Why do you still go over there, Futaba?"

    scene firstotoha8
    with dissolve

    f "Oh, a good friend of mine still goes to the [high_school] in that part of town."
    s "Wait...if there is a [high_school] over there, why did you two wind up coming here?"
    s "You didn't move for the sole purpose of coming to this[school], did you?"

    scene firstotoha9
    with dissolve

    f "Oh...Well, um...That’s-"
    r "N-Nevermind that! It’s old news and doesn’t matter at all. "

    scene firstotoha10
    with dissolve

    r "What {i}does{/i} matter is getting this show on the road!"
    r "The last stage of fixing a broken heart is buying a bunch of stuff to get yourself over the final hurdle."
    s "So is that what we’re doing? Shopping?"
    r "Shopping. Eating. Enjoying life. You name it."

    "I really didn’t expect to be spending the majority of my day tagging along with girls while they buy clothes, but..."
    "Hey, maybe they’ll be willing to sample outfits for me or something?"
    "There’s got to be a bright side to this, right?..."

    scene black
    with dissolve2

    "…"
    "Okay, so there was no brightside."
    "We went into roughly fifteen stores and I did not get to see them sample even one article of clothing for me."
    "What is it with girls?"
    "How are they able to do things like spending hours upon hours in department stores without buying anything?"
    "I’ll never understand it."

    scene firstotoha11
    with dissolve

    "After department store number 20 or 21 (I’ve honestly lost count), we begin to make our way to some dessert place that Rin and Futaba know about."

    r "Look at this trooper, still standin’ tall after chaperoning two [young]lasses into half of the clothing stores in the city."
    f "Sorry for not buying anything. I just haven’t really been able to find anything that looks good on me..."
    r "Yeah, same here. But hey, that just means more money for food, am I right?"
    s "Another bright side to the fact that you two haven’t bought anything is that it's actually a huge plus for me."
    r "Why? Cause you think you’d end up carrying it?"
    s "Because I {i}know{/i} I’d end up carrying it."
    r "Excuse me, good sir, but who did most of the heavy lifting when Molly was moving into her dorm?"
    s "Me."

    scene firstotoha12
    with dissolve

    r "Heck no you didn’t! I carried like, triple the amount of boxes you did!"
    s "Yeah, but they were all light. Who’s the one who carried her eight hundred gaming chairs upstairs?"

    scene firstotoha13
    with dissolve

    r "Bad homie! You’re supposed to only say nice things about me today. I’m wounded."
    s "Sorry, Rin. I’ll make sure to give you any leftover compliments after you drain my wallet at the dessert buffet."

    scene firstotoha14
    with dissolve

    f "Oh, you don’t have to worry about that. I’m treating Rin today."
    r "What, really? You don’t have to do that. Sensei can pay."

    "Why is it okay for {i}me{/i} to do it?..."

    scene firstotoha15
    with dissolve

    f "Mhm. My parents gave me an advance on my allowance, so I have some extra money to spare."
    r "They still give you an allowance even though you don’t work for it or anything?"
    f "Well, it’s not like there’s really anything I can do for them when they’re thousands of miles away..."
    r "True, true. But you don’t have to use that on me, you know. I’m perfectly fine with Sensei paying."
    s "Is paying for yourself a thing that has even crossed your mind today?"

    scene firstotoha16
    with dissolve

    r "Hm? Did you say something? I can’t really hear you over the sound of the guitar."

    scene firstotoha17
    with dissolve

    r "Wait, guitar? "
    r "What’s going on down there?"

    scene firstotoha18
    with dissolve

    "I turn around to see a girl around the same age as Rin and Futaba playing guitar in the center of a small park."
    "It’s hard to hear from all the way over here, but it looks like she’s singing as well."

    scene firstotoha17
    with dissolve

    r "…"

    "Rin stops dead in her tracks as she watches the girl play. "
    "It’s hard to tell what she’s thinking, but she becomes absorbed within a matter of seconds."

    scene firstotoha19
    with dissolve

    f "We have time to stop and watch for a little while, right?"
    f "I think it would make Rin really happy."
    s "Hey, this isn’t my day. It’s hers. If she wants to go watch guitar-girl for a little while, that’s fine by me."
    r "Woah..."
    r "She’s really good."
    r "Do you guys hear her?"
    s "It’s kind of hard to from up here."
    s "Did you want to get closer?"

    scene firstotoha20
    with dissolve

    r "Yes! Please! "
    r "Come with me!"

    scene black
    with dissolve

    "Rin nearly jumps down the entire flight of stairs and dashes over to the park. "
    "I worry that something like that might make a scene because it’s rather busy around here but, somehow or another, no one seems to notice..."

    scene firstotoha21
    with dissolve

    "We wind up stopping a decent distance away from the girl, who’s busy playing and singing to a small and mostly inattentive group of people."
    "But despite the lack of attention she’s getting from the crowd, she’s surprisingly good."
    "Her words are clear and emotional. And even though I don’t know much about music, her guitar playing seems pretty good as well."

    r "…"

    "Rin stands still, taking in every ounce of the performance. It's almost like she's getting lost in it. "
    "Futaba stands to her side, gently tapping her foot and nodding her head along with the music."

    gg "...{i}Untie the knot around your finger set me loose again{/i}-"
    gg "{i}I'm longing for a chance to breathe and-{/i}"

    scene firstotoha22
    with dissolve

    gg "{i}A chance to make amends-{/i}"

    scene firstotoha23
    with dissolve

    r "Oh my God, she looked at me."
    s "She’s still looking at you."
    r "What? Why?"
    s "Probably because you seemed interested."
    s "No one else was really paying attention."
    r "Is it safe to look back?"
    s "Why wouldn’t it be?"
    r "I don’t know, dude. It’s embarrassing. She’s pretty and talented and I...have a ponytail!"
    s "Is there something wrong with ponytails that I'm not aware of?"

    scene firstotoha24
    with dissolve

    r "I DON’T KNOW! LEAVE ME ALONE!"

    scene firstotoha25
    with dissolve

    "The girl with the guitar goes through the chorus one more time before finishing her song and staring at the ground."
    "She takes a few moments to catch her breath before beginning to pack her things up."
    "The music that had seamlessly blended in with car horns and sidewalk chatter fades into nothingness and, once again, we’re left without a clear goal in mind."

    scene firstotoha26
    with dissolve

    r "Sensei."
    r "I call upon you for help."

    "Well, one of us seems to have a goal, apparently."

    s "What’s up?"
    r "I want to talk to her."
    s "Are you in love again?"
    r "Of course not. But...she’s really cool and really pretty and...maybe we could play together or something."

    if bonus == True:
        r "Like, guitar I mean. Not sexually."
    else:
        r "Like, guitar I mean. We are not children and we will not be confined to the sandboxes of playgrounds."

    r "Unless she wanted to."

    scene firstotoha27
    with dissolve

    r "AHHH! Just help me!"

    "I wonder how vulnerable Rin is at a time like this?"
    "I suppose now is as good a time as any to find out..."

    s "Okay, okay. Just look at her and repeat after me. Got it?"

    scene firstotoha26
    with dissolve

    r "Got it."
    s "First, tell her...{i}I love your music! I came running the second I heard it!{/i}"
    r "Roger!"

    scene firstotoha28
    with dissolve

    r "Uh...ummm! I love your music! I came running the second I heard it!"
    gg "Wow, really?! Thank you so much!"
    gg "You have no idea how much it means for me to hear that!"
    s "Now tell her, {i}You’re very pretty. Like...supermodel-pretty.{/i}"
    r "A-Also! You’re very pretty! Like a supermodel!"

    scene firstotoha29
    with dissolve

    gg "Oh, come on...that's not true. You’re just trying to make me blush."
    s "Okay, ready for the final move?"
    r "Hit me, wingman."
    s "With every ounce of confidence in your body, shout...{i}I would give anything just to kiss you!{/i}"
    r "I-I would give anything just to kiss you!"

    scene firstotoha30
    with dissolve

    r "Wait, what?! What are you making me say?!"
    gg "Uhh..."
    gg "..."
    gg "Cool?..."
    f "Okay...Futaba to the rescue."

    scene black
    with dissolve

    "Futaba pushes both myself and Rin toward the girl, who carefully places her guitar back in her case and comes to stand next to us."

    scene firstotoha31
    with dissolve

    f "Hey! We just wanted to say we really liked your performance."
    r "And {i}I{/i} want to say that I am so, SO sorry for that...last thing I said."
    gg "You mean the part about kissing me?"

    scene firstotoha32
    with dissolve

    r "Yuuuuup...That’s the one..."
    gg "Don’t sweat it...I’ve heard much weirder stuff playing out here. Trust me."
    f "Do you perform here often?"

    scene firstotoha33
    with dissolve

    gg "Every weekend, pretty much. So if you ever get bored and want to come watch, feel free."
    gg "I don’t ask for money or anything. I’m just kind of doing this for fun."
    r "Do you...go to[school] around here?"
    gg "Mhm. I’m a first-year at the [high_school] a couple miles away."
    f "So you’re in the same grade as us then."
    f "Do you know Nodoka Nagasawa by any chance?"

    scene firstotoha34
    with dissolve

    gg "Ah! Nodoka! I {i}do{/i} know her!"
    gg "I’m always going to her for writing tips and stuff."
    gg "That girl’s like...a pillar of infinite wisdom."

    scene firstotoha35
    with dissolve

    f "Yeah...She definitely knows a little too much for her own good at times..."
    r "Umm...Is it cool if I ask you for your name?"

    scene firstotoha36
    with dissolve

    gg "Why? Need it for your next pickup line?"

    scene firstotoha37
    with dissolve

    r "Okay. Time to go back into depression-mode."
    r "It’s been a good day, everyone. Rin Rokuhara is signing off."

    scene firstotoha38
    with dissolve

    o "Otoha. Otoha Okakura."
    o "It’s nice to meet you, Rin. You don't have to sign off yet."

    scene firstotoha39
    with dissolve

    r "Y-Yeah! It’s really nice to meet you too!"
    r "I promise to be less weird in the future!"

    scene firstotoha40
    with dissolve

    o "Speaking of weird, who’s this guy?"
    o "Boyfriend for one of you two?"
    r "Oh, no. That’s just some guy. He’s been following us around for like two miles now."
    r "I thought about calling the police, but my phone died."
    s "She’s lying. I’m their teacher."

    scene firstotoha41
    with dissolve

    o "Their teacher?"
    o "Then what are you doing out with them on the weekend?"
    f "He’s not exactly a normal teacher..."
    s "I’m really not."

    scene firstotoha42
    with dissolve

    o "Well, uhh...Okay then."

    "Yeah, that’s pretty much the reaction I’d expect out of any [high_school] girl who {i}isn’t{/i} in my class."

    scene firstotoha43
    with dissolve

    o "Anywho, I need to be getting a move on. I’ve got some stuff I need to take care of before tonight."
    o "It was really nice meeting you all, though!"

    scene firstotoha44
    with dissolve

    o "Oh! And Nodoka’s friend- I didn’t get your name! Tell me who you are and I’ll tell her I ran into you."
    f "Oh, Futaba Fukuyama. You don’t need to tell her, though. I’m sure I’ll be seeing her again soon anyway."
    o "Nah, nah. Totally telling her first thing Monday morning. We have science together."

    scene firstotoha45
    with dissolve

    o "And you! Make sure you take good care of these girls."
    o "You’re a lot older, so people might get the wrong idea if they see you out and about with them after dark."
    s "They’re in good hands..."

    "Kind of."

    o "Well, I don’t really have any reason to distrust you right now. So I guess they are."

    scene firstotoha43
    with dissolve

    o "Anyway, I’ll see you later! Thanks for listening to me play!"
    o "I’m here every weekend if you ever want to come say hi!"

    scene firstotoha46
    with dissolve

    r "W-We will!"
    r "..."
    r "...See ya."
    f "…"
    s "…"

    scene black
    with dissolve2

    "Shortly after that, the three of us make our way over to the dessert buffet."
    "We spend almost three hours there as Rin apparently has seventeen stomachs when it comes to dessert."
    "And even though Futaba offers to foot the bill for both her and Rin, I ultimately wind up paying for everyone."
    "I figure it’s the least I can do to thank them for a surprisingly fun day in a part of town I’ve never seen before."
    "And hey, we even managed to meet someone new."
    "I wonder if Rin and Futaba will wind up going back to see her again sometime soon?"
    "I can’t imagine myself ever wanting to go {i}that{/i} far away just to spend time with a girl, so there’s no guarantee I’ll ever see Otoha again."
    "But even if I don’t, I’m glad that she was able to make Rin smile."
    "That was the happiest I’ve seen her in quite some time..."

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe35 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label cafe40:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
    if rin_love >= 20 and ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False:
        jump cafe20
    if rin_love >= 15 and cafe15 == True and day63 == False:
        jump rincafegone
    if rin_love >= 25 and rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False:
        jump cafe25
    if rin_love >= 30 and beachvacation16 == True and cafe30 == False:
        jump cafe30
    if rin_love >= 35 and rindorm35 == True and rininvite == True and cafe35 == False:
        jump cafe35
...
```