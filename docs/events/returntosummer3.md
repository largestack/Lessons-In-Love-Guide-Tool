# Utinam Ne Illum Numquam Conspexissem (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [A Life of Prizes](./returntosummer2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: returntosummer3
* Group: Main
* Triggered by label: returntosummer2
* Chain sources: returntosummer2
* Chain sources path: returntosummer2

## Official wiki page

[Utinam Ne Illum Numquam Conspexissem](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=returntosummer3&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label returntosummer3:
    scene black
    with dissolve2

    "I spread all ten key pieces I’ve collected on the ground and use the tiny attachments at the end of each one to put them back together."
    "I don’t know what asshole broke such a pretty key into so many pieces, but I guess it doesn’t matter anymore since I was able to restore it to its former glory."
    "I take the key and place it in my mouth to make sure that all of the parts taste right before using it on the door."
    "It tastes like what you would probably imagine a key tastes like, so I assume everything is correct and make my way to the handle."

    if bonus == True:
        "I place the key inside and wiggle it around until the door cums. "
        "Sorry, I mean “opens.”"
        "But unlocking a door with a key is kind of like door sex and the unlocking part is kind of like an orgasm."
        "At least that’s what I’ve always thought."
        "Anyway, I probably shouldn’t stay in here anymore for it is clearly and negatively affecting my mental health."

    scene endofthefourth1
    with dissolve2

    "I walk into my completely normal and not at all lopsided living room. But before exiting my home and going on another journey, I peer outside of the window."
    "I see a melting world, packed to the brim with collapsing buildings and more colors than you could fit into ten rainbows if all of them had different colors or something."
    "My ability to make metaphors always suffers during times like this, but I can guarantee you that some crazy shit is going down right now."
    "I breathe onto the window and draw my initials on the glass."
    "I forget them the moment I turn away."
    "I’ll remember again when the time is right."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene endofthefourth2
    play sound "pop.mp3"
    stop music

    achoir "CONGRATULATIONS!"
    s "What’s this?!"

    play sound "static.mp3"
    scene endofthefourth3 with flash
    stop sound
    play music "letsfuckingo.mp3"

    achoir "A CELEBRATION JUST FOR YOU!"
    achoir "YOU’VE SURVIVED THE WINTER! EVERYONE IS VERY IMPRESSED!"
    s "Oh, you guys! Have you been waiting out here this whole time?"
    achoir "WHERE ELSE WOULD WE GO RIGHT NOW? YOU SAW THE WORLD FROM THE WINDOWS, DID YOU NOT?"
    blue "Okay, okay. That’s enough yelling."
    green "Yeah, my throat was starting to hurt."
    pink "I’m the pink one!"
    red "In all seriousness, congratulations. And, in even more seriousness, yes. We’ve been waiting out here the entire time. But do you know {i}why?{/i}"
    s "Because it’s my birth-"
    pink "Because we knew you could do it!"
    blue "We’ve never had more faith in you succeeding before, Sensei! We all knew you were going to pull through this time!"
    green "I had my doubts, but I {i}am{/i} glad to see you did it."
    s "And everybody else???"
    red "Who is everyone else?"

    scene endofthefourth4 with fade

    s "The hundreds of other mysterious figures lining both the streets and the skies."
    red "Oooooooh, them."
    red "Yeah, they’ve been waiting too."
    achoir "YOU DID IT!"

    "I did it!"

    a "You did it!"

    scene endofthefourth5
    with fade

    s "Ami! You’re alive!"
    a "Of course I’m alive! What’s a trip to school in the middle of the night without your doting and mildly obsessive [niece]?"
    s "Did you see me solve the puzzle? I was very smart and only needed a little bit of help."
    a "I did! You {i}really{/i} like rice!"
    s "We should hit the town to celebrate."

    if bonus == True:
        a "I was going to suggest the same exact thing! I was just kinda hoping we could maybe do it a few times first."
        s "But with your body all twisted, I wouldn’t even know where to put it."
        a "Anywhere you want! I’m up for anything!"
    else:
        a "I say we HUG first!"

    green "Right here? Really?"
    pink "Shut up, Green! We all know you would do the same!"
    blue "So would-"
    a "[amimaster], I can’t believe I’m saying this, but it would probably be for the best if we {i}didn’t{/i} do it right now."
    a "We’re still ahead of schedule, though! So we’ll have plenty of time to do it once we get to the school."
    red "Remember to look both ways when crossing the street! You never know when someone might let go of the wheel!"
    s "I am ready for school! But there is just one problem."
    a "What’s wrong, [mayamaster]?"

    if bonus == True:
        s "How am I supposed to walk with this huge string tied around my penis???"

        "I point to the string in case Ami isn’t able to see it. Her eyes have always been bad."
    else:
        s "How am I supposed to walk with my crippling sciatica???"

    a "Beats me! It hasn’t stopped you so far."
    a "Now shut up and move through the choir of angels, Sensei! And if any of them don’t want to step aside for you, feel free to push them over."
    a "We might get in trouble for it later, but it’s the right thing to do in the moment."
    s "Can I at least say goodbye to all of my new friends, first?"
    a "Nope!"
    s "Darn it!"

    play sound "laugh3.mp3"
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene street_night
    with dissolve2
    show amihappyyay with dissolve

    a "Hey, is it okay if I change the song? It feels weird to be doing this with normal music instead of the backwards kind."
    s ".ekil d'uoy revetahw od nac uoY .imA ,yako s'ti esruoc fO"

    "I decide to answer in reverse because it’s topical and I’m able to."

    stop music

    a "Thanks, Sensei! Now, let’s see what we’ve- oh!"

    play music "undoitall.mp3"

    a "This one’s probably still fresh in everyone’s memories!"
    a "{i}And{/i} it will heighten the impact of the current scene and the way it ultimately has to end."
    a "That was such a cute little date you and Maya had. I really wish I could have been there for it."
    a "How come you never invite me anywhere anymore?"
    s "What are you talking about? We went on a cool bus ride just yesterday."
    a "{i}You{/i} went on a bus ride. All {i}I{/i} did was dream. That’s totally different, Sensei."
    s "My bad. It seems so long ago at this point."
    a "Hey, would you like me more if there was a mini Maya with an engorged head that followed me around everywhere?"
    s "I wouldn’t like you any {i}less!{/i} But where would you obtain such a thing on such short notice?"

    if bonus == True:
        a "Oh, I already have one. I’ve just been keeping her in my pocket since I was afraid you’d mistake her for an onahole and I am perpetually in need of your semen."
    else:
        a "Oh, I already have one."

    a "Maya 2, come! Just not literally!"

    hide amihappyyay with dissolve
    show amihappyyay at left with dissolve
    show mayadoll at right with dissolve

    a "There she is! Are you in love with me yet???"
    m "..."
    s "Wow. She looks just like the real Maya but with an engorged head and the ability to float."
    s "Can she speak?"
    m "Cha cha cha."
    a "Kind of. That’s all she can say."
    a "It’s a weird default setting, but I haven’t really had the time to see if she can do anything else since I’ve been so busy trying to drown her in the bathtub."
    s "You should treat your toys better, Ami."
    a "You should treat {i}me{/i} better."

    if bonus == True:
        a "I overheard you talking to Maya about how getting pregnant gives people a chance to make it up to the roof, and I always disappear before I reach the top step! It’s not fair!"
        a "So yeah, if you would just keep trying to breed me, I wouldn’t have to get all squiggly and milk you dry while you’re sleeping anymore."
        s "I’m going to need a new lock for my door."
        a "That’s rude! If you didn’t like it, you wouldn’t cum so much!"
        s "No, like I literally need a new lock for my door. I put my fancy puzzle key inside of it too many times on the way out today and I think it might have broken."
        a "Oh."
        a "I guess we can pick one up on the way to school then."
        s "Yay! Best [niece] ever!"
    else:
        s "I will try. I promise."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene endofthefourth6
    with dissolve2

    "Ami and I make it to the hardware store and search around for locks, but keep getting blocked by stock image watermarks that the staff forgot to clean up."

    s "What kind of lock do you think would work best for a bedroom door?"

    "There are no associates around so I have to ask Ami, who may or may not know anything about hardware."

    a "Hmm...maybe one of those touch pad type ones? The ones where it needs your fingerprint."
    s "But what if someone chops off my finger and uses it to make it into my room? There are things I need to protect in there."
    a "Like the door to the attic where all of my mom’s things are?"
    s "There are things I need to protect in there."

    if bonus == True:
        a "Like the secret folder of nude photos you have of Maya?"
        s "There are-"
        a "How old is she in those, Sensei?"
        s "There-"
        a "Stuck on loop? Right now? What are you, Kumon-mi?"
    else:
        a "Like what? Your Roblox account?"

    play sound "laugh1.mp3"

    "The staff of the hardware store laughs and I get a little embarrassed."
    "I pick the first lock (As in {i}select{/i}. Not like, lockpick) I can find and quickly ring myself up at the self-checkout register."
    "I forget to grab a bag and also forget to grab the lock and then run out of the store."

    scene black
    with dissolve2

    if bonus == True:
        "The Maya doll is fast, so it is able to keep up with me and tie a second lasso around my penis that she squeezes really tight, giving Ami the time to catch up."
        "I curse the day I bought her that special outfit."

    "........."
    "......"
    "..."

    scene lockers_night
    with dissolve2
    show amihappyyay at left with dissolve
    show mayadoll at right with dissolve

    a "Jeez. I forgot how good you are when it comes to running away from stuff."
    m2 "Cha cha cha."
    a "You tell him, Maya 2."
    s "Why did we come here again?"
    s "I feel like there’s a thing I’m supposed to do."
    a "You probably haven’t remembered yet because we're so ahead of schedule. We’ve still got plenty of time left until {i}she{/i} gets here."

    "Ami stares at-"

    m2 "Cha cha cha."

    "Ami stares at Maya 2 and her scribbles bend into a giant pair of angry eyebrows that poke into her scalp and cause her to bleed, but not as much as her hand{s}s{/s} bled at the cafe yesterday."
    "I can see that they’ve healed all but entirely now."

    a "So...what do you want to do since we have so much time to kill?"
    a "Play with the Maya doll? She is annoyingly durable."
    m2 "Cha cha cha."
    s "I’m hungry."
    a "Still? After all of that rice?"
    s "I want something rounder with a solid white covering on the outside of it."
    a "Oh! Well, I know just the place to go, then!"

    hide amihappyyay with dissolve

    a "Follow me, guys!"
    a "It is egg time!"
    m2 "Cha cha cha."

    hide mayadoll with dissolve

    "Ami and Maya 2 float down the hallway and I’m angrier than ever that I have to use my stupid legs again."

    ll "Yo you better be fucking kidding me right now."
    s "Sorry, Left Leg. I forgot you were sentient."
    ll "Yeah no shit you forgot. Always walking on me and shit. Some fucking nerve you’ve got."
    s "In my defense, walking is literally your only job."
    ll "You think that’s all I do?! Bro. You don’t even {i}know.{/i}"
    ll "If it wasn’t the end of the fucking world right now, I’d be so fucking gone, dude. Holy shit."
    a "Sensei! Stop talking to your leg and get over here! There is round food!"

    scene black
    with dissolve2

    s "Coming, Ami!"

    "My leg shuts up when I pinch him, but I get a tiny bruise as a result."
    "I ignore the slow transition of the color of my skin as the ruptured blood vessels underneath it begin to leak."

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene endofthefourth7 with flash
    stop sound

    "And I take my place in a room full of friends."

    m2 "Cha cha cha."

    "Our plates cover themselves in the purest of all foods, some even pipping before we have the chance to dig in."
    "The cafeteria comes alive with laughter and discussion, teleporting me back in time to when everything was simpler."
    "Before cursed birds and fireworks."
    "Before watermelons and violin."
    "Before the world began to melt into a puddle of refuse that I would scoop up with my hands and coat myself in."
    "If I had never seen it, this would not have happened."
    "If I had never heard it, this could have been avoided."
    "But I did."
    "And so here we are."
    "If only I was stronger."
    "If only she was here."

    a "Wow! The lunch room is really packed today!"
    a "Everyone must have known you were coming, Sensei!"
    a "But it was like that back at the house as well."
    a "If you keep this up, you might have a {i}second{/i} harem comprised of more than just cute, innocent schoolgirls like me!"
    m2 "Cha cha cha."
    a "Yes I am, Maya 2. Shut up."
    s "..."
    a "Sensei, what’s wrong? You’ve barely touched your eggs."
    s "There’s a little bird trying to escape from one of them. I can see its beak."
    a "So what? That just means there’s like, more protein or something."
    m2 "Cha cha cha."
    a "Even Maya 2 agrees and we {i}never{/i} see eye to eye."
    a "It probably doesn’t really help that her eyes are literally empty, but you know what I’m saying, don’t you?"
    s "..."

    "I lift up the egg in my hand and the chirping of the small creature becomes audible, even with all of the noise in this room."
    "The laughter and the conversations grow louder as if to distract me from what is in front of me, but-"

    play sound "static.mp3"
    scene endofthefourth7 with flash
    stop sound

    s "Yum! Egg!"

    play sound "glass.mp3"

    "I bite down on the egg. It feels a little like glass."
    "It leaves a sour taste in my mouth and something gets stuck in my throat."
    "After picking the shards of FOOD out of my teeth, I flick them at the table behind me and direct my full attention to Ami Arakawa, my loving [niece], and her best friend, Maya 2."

    a "So...I..."
    a "I wrote you another poem, Sensei..."
    a "And I’m really nervous about reading it to you..."
    a "But if you could find it in your heart to listen to me for a second, I-"

    stop music
    play sound "bell.mp3"
    scene endofthefourth8

    a "AAAAAHHHHH!!!!!!!!!!!!!!!!!!"
    a "DON’T INTERRUPT ME WHEN I AM TRYING TO TAAAAAAAAAAALK!!!!!!!!!!!!"
    m2 "Cha cha cha."

    "The sound of the school’s PA system turns on immediately after the bell, but no one seems to be paying any attention but me."
    "Who would have known that all my friends are such terrible students?"

    a "DO NOT LISTEN TO THE ANNOUNCEMENT, SENSEI!"
    a "LISTEN TO MY POEM!"
    a "I MADE IT JUST FOR YOU!"
    s "..."

    play music "sensei.mp3"

    ay "Um...hello?"
    ay "Is this thing- yeah. Okay. It’s on. Uhh..."
    a "SENSEI! PAY ATTENTION TO ME!"
    s "Ayane?..."
    ay "Uhh..."
    ay "Sensei, if you’re here...please come to the staff room."
    ay "Everyone else is gone and...my phone isn’t working and..."
    ay "I’m really scared..."
    ay "I’m...{i}really{/i} scared..."
    s "..."
    a "THE POEM GOES LIKE THIS."
    a "A ROOM FULL OF SUN-"
    s "I...think I need to go, Ami."
    a "YOU DON’T NEED TO DO ANYTHING EXCEPT LISTEN TO MY POEM!"
    a "SHE GETS ATTENTION WHENEVER SHE WANTS. I GET NOTHING."
    a "I GET NOTHING, SENSEI! STAY HERE AND LISTEN TO MY POEM!"
    s "..."
    a "SENSEI!!!"
    m2 "Cha cha-"

    scene black
    play sound "pop.mp3"

    a "YOU WORTHLESS FUCKING DOLL!"
    a "YOU WERE SUPPOSED TO MAKE HIM LOVE ME MORE!"
    a "NOW I HAVE TO WAIT EVEN LONGER!"
    a "LOOK WHAT YOU HAVE DONE!"

    "Ami begins to beat on the secondary version of Maya while the main one lingers somewhere on the roof of the school."
    "I doubt there will be another picnic on account of my arrival no longer being much cause for celebration...but I need to go regardless."
    "Not before stopping at the staff room, though."
    "I have no idea how Ayane managed to make it here {i}again{/i}, but I know that I’m not going to find the answer to that in an empty cafeteria."
    "As I move through the halls of the school and peer out of the windows, I notice that the world isn’t melting at all."
    "But the last surviving evidences of winter are."
    "........."
    "......"
    "..."

    scene endofthefourth9
    with dissolve2

    ay "Oh my god! You’re here! You’re really here! I was so worried! I had no idea what else to do!"
    ay "You weren’t at your house! You weren’t at the dorms! I even checked the dojo and the cafe and-"
    s "I’m here."
    s "It’s okay."

    scene endofthefourth10
    with dissolve

    ay "Sensei...what in the world is going on? Where did everyone go?"
    s "They’re gone."
    ay "What do you mean they’re gone? Where’d they go {i}to{/i}? And why didn’t they take us with them?"
    s "Because they couldn’t. And we wouldn’t want to go with them anyway."
    s "Maya will explain it better than I can, but you don’t have to worry about everyone else. They’ll come back soon."
    ay "Maya?...Is she here too?"
    s "She’s probably up on the roof watching shooting stars and eating melons or something."
    s "This is actually a situation I’ve found myself in a few times now. And, believe it or not, it’s {i}your{/i} second."
    ay "My second what? What are you talking about?"
    s "Your second trip to the end of the world."

    scene endofthefourth11
    with dissolve

    ay "The...end of the world?..."
    s "Or...{i}this{/i} world? It’ll start over once the three of us are together and, before you know it, your beloved summer will have returned."

    scene endofthefourth12
    with dissolve

    ay "Fuck summer! If it’s the end of the world, all that matters is that I’m with you! I don’t care about anything else!"
    s "Well...like I said, the world is going to start over."
    ay "That’s obviously just a thing you’re saying to me so I don’t have to worry! This is the only world we have!"
    s "Ayane, breathe."

    scene endofthefourth13
    with dissolve

    ay "Hah......hah......hah......"
    s "Do you remember the conversation we had earlier tonight? The one where Maya invaded your personal space and you {i}confirmed{/i} that you’re not pregnant?"
    s "Well, apparently you are."

    scene endofthefourth14
    with dissolve

    ay "What? No I’m not. I already told you that. Why don’t you believe me?"
    s "How confident are you, though? Because if you’re here-"
    ay "I am 100%% confident and I’m not going to tell you any of the details because they are embarrassing and I don’t want you to think I’m disgusting in our last ten minutes on earth."
    ay "Sensei...what is happening? For real..."
    s "Well, to reiterate Maya’s summary..."
    s "All of us are caught in an infinite time loop and, up until recently, she was the only one aware of it."
    s "Now, we all have to go up to the roof and hug and then she’ll pray or something and we’ll all wake up in a different place at a different time."
    s "If you don’t believe me now, which of course you wouldn’t because it sounds fucking insane, you will when we get up there."

    scene endofthefourth15
    with dissolve

    ay "You're..."
    ay "You’re...really not kidding...are you?"
    s "This would absolutely not be the time for me to tell jokes. And I’m horrible with them anyway, so you’d know if I was messing around."
    ay "Is this..."
    ay "You asked me something like this at the Christmas party, right?"
    ay "And...that thing with the rooftop you asked me months ago..."
    ay "This...really is happening."
    ay "This has {i}been{/i} happening..."
    ay "But...that doesn’t make sense."
    s "You’re accepting it a lot easier than I thought you would, all things considered."

    scene endofthefourth16
    with dissolve

    ay "It’s just...why would you lie? And why would there be so many instances of you giving me hints about it?"
    ay "You’ve wanted me to find out all along, haven’t you?..."
    s "I wouldn’t say I’ve {i}wanted{/i} you to-"
    s "But I definitely don’t mind having someone else around who thinks it’s as weird as I do."
    s "I have no idea how Maya is going to feel, though."

    scene endofthefourth17
    with dissolve

    ay "R-Right! Maya."
    ay "You said she’s on the roof, right?"
    s "Yeah. I think that’s where we need to be for the ritual thing to work."
    ay "And...she’s the one who knows how to teleport us into the future or something?"
    s "I don’t really think that’s exactly what’s happening, but sure."
    ay "And she’s been doing this for how long exactly?"
    s "No clue. A long time- that’s all I know."
    ay "And...everyone else is okay? And we’ll get to see them again?"
    s "Yes. And I’d hate to interrupt you while you obviously have so many questions, but we should probably head up now and-"
    ay "Wait, no. I only have one more question. I’ll let Maya explain the rest."
    s "..."
    ay "I promise."
    s "Fine."
    s "What’s your last question, Ayane?"
    ay "Well..."
    ay "Uhh..."

    if bonus == True:
        ay "What..."
        ay "What happened to your clothes?"
        s "..."
        ay "..."

        scene endofthefourth18
        with fade

        s "..."
        ay "..."
        s "Well, this has never happened before."
        ay "Umm..."
        ay "Is...Maya going to be naked too?..."
        ay "Do I...need to..."
        s "I think I have an extra pair of clothes in my office, but you can take your clothes off if you don’t mind."
        s "It will probably make me showing up with you significantly funnier and less stress-inducing for her at least."
        ay "No, I...think I’ll keep my clothes on if taking them off is optional..."
        s "I see..."
        ay "..."
        s "..."
        ay "So...are we gonna go to your office now?..."
    else:
        ay "..."
        ay "Do you want to make bone necklaces together?"
        s "Right now?"
        ay "It seems like the best possible time. No one will try to stop us."
        s "..."
        ay "..."
        s "Okay..."

    scene black
    with dissolve2

    if bonus == True:
        s "Yeah. My bad."
        s "I’ll make sure to put a note on my door so this doesn’t happen again in the future."
        ay "I mean...{i}I{/i} obviously don’t mind. Especially with almost everyone else being gone and stuff. I just always figured you’d have your clothes on for the apocalypse."
        s "I’m glad to see that you’ve already imagined this situation in the past."
        ay "Doesn’t everybody think about what they’ll do during the apocalypse? Am I really weird for doing that? Probably not, right? Like...since we’re actually experiencing it right now and stuff."
        s "..."
        ay "Wow, that thing really flops around a lot when it’s not hard, huh?"

        "Ayane and I make our way over to my office so I can get a change of clothes and not surprise Maya by revealing my penis to her for the first time in presumably millions of years."
        "It feels strange to be walking around the school naked but, somehow, it feels even stranger to be walking around in the middle of a reset with someone other than Maya by my side."
        "I don’t normally come-to until I’m on the roof, so...I guess it could have been Ayane’s voice that snapped me out of it?"
        "I have no idea."
        "And it looks like it’s time to go back to the drawing board in a multitude of ways considering Maya’s pregnancy theory is now all but confirmed a bust."
        "I throw on a shirt I haven’t adorned in quite some time and turn around to face Ayane, who refuses to leave my side for even a second."
        "I don’t blame her."
        "Imagine {i}you{/i} woke up one day and everyone you loved was gone?"
        "Assuming there {i}is{/i} anyone like that."
        "If there’s not-"
        "Well, maybe you wouldn’t do all that bad here."
    else:
        "Ayane and I make sweet bone necklaces together and then hide them in a secret club room that only we know about."

    "........."
    "......"
    "..."

    scene endofthefourth19
    with dissolve2

    ay "Um...Sensei?..."
    s "Yeah?"
    ay "I just..."
    ay "Do we really need to go up there?"
    s "What do you mean? Of course we do."
    ay "It’s just...I’ve got this weird feeling in my stomach that’s getting worse the closer we get."
    ay "And no, it’s not a baby."
    s "We don’t really have a choice, unfortunately."
    ay "What...happens if we don’t go up, though?"
    ay "Do we just...die?..."
    s "It’s a little more complicated than that, I think."
    s "We’ll still be there after the world starts over. It’s just our memories that won’t."

    scene endofthefourth20
    with dissolve

    ay "Our..."
    s "..."
    ay "I get it now..."
    ay "{i}That’s{/i} why you can’t remember anything..."
    ay "But, then..."
    ay "No..."
    ay "No no no no no...."
    ay "That can’t be true."
    ay "Our...entire past with one another..."
    ay "Are you saying that’s..."
    ay "That’s already gone?..."
    s "..."

    scene endofthefourth21
    with dissolve

    ay "No..."
    ay "I think I’m gonna be sick..."
    s "We can talk about that later, Ayane. “Our past” can still come back. But if we wait around for too long, there’s a chance it never will."
    ay "I can’t do it..."
    ay "No..."
    ay "I can handle the world ending..."
    ay "I can handle the time loops and the disappearances and...all sorts of things..."

    scene endofthefourth22
    with dissolve

    ay "But not that..."
    ay "Not losing the moments and memories that brought me closer to you..."
    ay "That’s all I have to hold onto, Sensei..."
    ay "That’s all I-"

    scene endofthefourth23
    with fade

    s "If you’re going to cry, cry on me."
    s "Regardless of whatever happened in the past, we’re together now. And that’s not going to change because of some weird...time loop rules or something."
    ay "I’m so scared, Sensei...I don’t want to go up there anymore..."
    ay "I want to forget about all of this...I can’t do it..."

    scene endofthefourth24
    with dissolve

    s "You don’t mean that. I know you."
    s "Being scared is part of life, Ayane. You’ve dealt with a lot worse than the man you’re {i}basically{/i} dating forgetting some stuff from the past."

    scene endofthefourth25
    with dissolve

    ay "...dating?"
    s "Fuck."
    ay "You’ve never called it that before."
    s "I didn’t call it that now either."

    scene endofthefourth26
    with dissolve

    ay "Yes you did! I heard it! We’re basically dating!"
    s "Ayane, there are more important matters to deal with right now."
    ay "Fine!"

    scene endofthefourth27
    with dissolve

    ay "Fine..."
    s "..."
    ay "Even if the world does end when we step onto that roof..."
    ay "At least it will end on a good note."
    ay "I love you."
    s "..."
    ay "Say it or I’m not taking another-"
    s "I love you too."
    s "Now, let’s go..."

    scene black
    with dissolve2

    "Ayane locks her fingers with mine as we take on the last flight of stairs separating us from summer."
    "No."
    "Not just separating us from summer..."
    "Separating us from the girl with the worst luck in the world."
    "The one who’s witnessed the end of everything over and over again."
    "The one who, even after all this time, persists just so {i}I{/i} can live."
    "I should thank her."

    scene clearnightsky
    with dissolve2

    "I should tell her I appreciate all that she does for me."
    "I should let her say what she wants without giving her any problems."
    "But, most importantly-"
    "I should admit to her the same thing I’ve already admitted to her two closest friends."

    s "..."

    "I should do that."

    stop music

    "But I can’t."

    play sound "static.mp3"
    scene endofthefourth28 with flash
    stop sound

    s "..."
    s "..."
    s "..."
    s "Maya?"

    $ renpy.end_replay()
    $ returntosummer3 = True
    $ mollysad = False

    play sound "jackpot.mp3"
    scene chap2end
    $ renpy.pause(4, hard=True)
    play sound "static.mp3"
    scene chap3 with flash
    stop sound
    $ renpy.pause(7, hard=True)
    scene black
    with dissolve4

    jump chap4intro

label chap4intro:
    "There is nothing."

    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop10 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    jump chapthree1
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label returntosummer2:
    scene resetfour6
    play music "11c.mp3"
    $ renpy.pause(10, hard=True)
    play sound "jackpot.mp3"
    scene resetfour7

    s "こんにちは！先生です！"
    s "今日はゲームをします。"
    s "ARE YOU READY???"
    s "で わ。。。"
    s "START!!!"

    play sound "static.mp3"
    scene resetfour6 with flash
    stop sound

    "THE RULES OF THE GAME ARE SIMPLE"
    "FILL OUT MAGAZINE SWEEPSTAKES AND TRY TO WIN DIFFERENT PARTS OF A KEY"
    "ONCE YOU HAVE WON ALL THE PARTS OF THE KEY, YOU WILL BE ABLE TO ASSEMBLE IT AND ESCAPE YOUR ROOM"
    "BUT BE CAREFUL!!!"
    "STAYING IN ONE PLACE FOR TOO LONG COULD CAUSE YOU TO GO INSANE!!!"
    "HAVE FUN AND ENJOY!!!"
    "WELCOME HOME"

    s "What do I want to do?"

    menu resetfourmenu:
        "ESCAPE (For Real)" if keypoint == 10:
            $ renpy.end_replay()
            $ returntosummer2 = True

            jump returntosummer3
...
```