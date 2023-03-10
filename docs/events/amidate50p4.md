# Somnambula (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [My Life With You](./amidate50p3.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: amidate50p4
* Group: Ami
* Triggered by label: amidate50p3
* Chain sources: amidate50p3
* Chain sources path: amidate50p3

## Official wiki page

[Somnambula](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidate50p4&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amidate50p4:
    "..."
    "......"
    "........."

    scene tree3
    play music "newhope.mp3"

    "We board a bus that’s moving backwards and all I can think about is the sound the tires make."
    "It’s a low pitched hum, not far dissimilar to the sound of a hummingbird’s wings as they defy what we’ve come to expect of some of the creatures living in the same world as us."
    "Soon, the night will come. "
    "It will replace the sun and shift the tide, dragging many creatures back into the shallowest parts of the ocean- some willing, some not."
    "We take a seat in the back and look into each other’s eyes."
    "I take Ami’s hands in my own and observe the minor gashes she obtained while trying to do something good."
    "They open back up and leak out the only fluid meant to be kept in."
    "I press my tongue to them and drink in her existence."
    "A warmth floods over me like a ray of sunlight made weaker by a bedsheet."

    play sound "static.mp3"
    scene amibus1
    with flash
    stop sound

    a "Do you believe in God, Sensei?"
    s "Do you?"
    a "I do."
    a "Maya makes fun of me for it sometimes, but I think that he’s real."
    a "I don’t know if he’s watching every second of every day, but I think he’s there."
    a "And I think that all of the suffering that you and I have endured is just his way of testing us."
    s "Testing us for what?"
    a "..."
    s "Testing us for wh-"
    a "It is a test to see if we are worthy of Heaven."
    a "To see if we can endure the harshness of reality and overcome adversity in order to gain one of the many limited seats in the giant sky castle all good boys and girls go to when they die."
    a "Will you sit with me, Sensei?"
    a "Will you come to the sky castle with me?"

    play sound "static.mp3"
    scene amibus2
    with flash
    stop sound

    "We talk at length about the afterlife while swapping seats in the classroom."
    "Ami breathes in a sequence that is easily decoded. She is trying to communicate with me in a secret language we devised when we weren’t as tattered."
    "One. Two. One. Four. Eight."
    "The amount of seconds between breaths. It moves from side to side, neglecting all that is in the middle."
    "It’s like an abacus, in that sense."
    "I’m like an abacus in that sense."
    "The parts of me furthest away from the center are the ones that do the most work."
    "Everything in the middle is just blank."

    a "Do you ever wonder where we go when we die?"
    s "Is it not the sky castle you were alluding to in the sentences prior to this?"
    a "Do you ever wonder anything at all?"
    s "I wonder about all sorts of things."
    a "Tell me."
    a "Tell me the things you think about on bus rides backwards."

    "I remove a list from my pocket that I always keep on hand in the event that someone asks me this question."
    "I begin to read from it."

    s "When I was younger, I used to take the tips of my thumb and my index finger and make a ring out of them. "
    s "I’d wrap the ring around my ankle and, as the years went by, I stopped being able to fit all of it inside."
    s "I think it was when I could no longer close the ring anymore that I realized I was unhappy."
    s "It was good to be growing, but what if I was growing too much?"
    s "Tell me the things you think about, Ami."

    play sound "static.mp3"
    scene amibus3
    with flash
    stop sound

    a "On bus rides backwards, I like to think about us."
    s "Us?"

    "I ask her, “Us?”"

    a "Us."

    if amifingered == False:
        a "Like...“is this really working?”"
        s "Is what working?"
        a "You and me at arm’s distance. "
        a "I’ve done almost all I can and yet you’re still so far away."
        a "Is that really going to work?"
        s "Why wouldn’t it?"
        a "Because neither of us are happy."
        s "Would changing the proximity of our physical distance truly work in adjusting that?"
        a "It would bring us closer. Literally."
        a "We’re not meant to be apart."
        a "We’re meant to sit in the sky castle together."
        s "I see."

    else:
        s "I see."

    "One. Two. One. Four. Eight."
    "The pattern stays the same."
    "An onslaught of footsteps approaches from directly behind me, but there’s not enough room in here to move my head."
    "I also fear that it would fall off of my shoulders if I were to try."

    av "Next stop: Somewhere else."

    play sound "static.mp3"
    scene amibus4
    with flash
    stop sound

    a "If I asked you to start reading me bedtime stories before I go to sleep, would you?"
    s "Of course."
    a "Thank you, Sensei."
    a "The sound of your voice always puts me at ease."
    a "I particularly enjoy the way you enunciate わ and how it always sounds as if you are breathing a sigh of relief when saying my name."
    a "Like you are glad that I still exist in a form that you can talk about without slipping your hands into your pockets."
    a "When you grasp at the fabric inside of them, do you ever find holes? "
    a "Does anything ever fall through?"

    "The bus ride continues and I watch the clouds through the windows of a well lit church."
    "I can smell candles scented with something reminiscent of the earliest years of my life, though it could just be dying wax."
    "Ami’s hands open up again, but she smears the blood onto a pew built of concrete before sending signals to her brain that cause her eyes to tilt in the direction of mine."

    scene amibus5
    with dissolve2

    a "I can feel it, Sensei."
    a "I can feel His light."
    a "And though it isn’t mine to hold, I want nothing more than to wrap my arms around it. I want nothing more than to be swallowed by it."
    a "I love you so much."

    play sound "static.mp3"
    scene amibus1 with flash
    scene amibus5 with flash
    stop sound

    a "Will you tell me you love me too?"
    s "Of course. I love you, Ami."
    a "Thank you, Sensei."

    play sound "static.mp3"
    scene amibus6 with flash
    stop sound

    a "Thank you, Sensei."
    a "That was a really random time to say that, but I love you too."
    a "Are you feeling any better now?"
    s "What do you mean?"

    play sound "static.mp3"
    scene amibus7 with flash
    stop sound

    a "What do you mean, “What do you mean?”"
    s "I mean what do you mean?"
    a "I don’t know what you mean."

    "Ami lovingly caresses a giant chicken as the bus begins to move faster."
    "It stops at so many different places and I can’t help but applaud the constant advancement in modern transportation technology."
    "One. Two. One. Four. Eight. Yet the middle parts drop out again as she points me to a chair."

    scene white
    with flash

    "I sit down on it and can’t help but feel like I’m usurping the role of king from an invisible entity who doesn’t want me to sit here."
    "Ami brings herself down to her knees and kisses my feet."

    a "This will help you walk."

    "Her tongue slips out like a clam searching for salt."

    play sound "static.mp3"
    scene amibus8 with flash
    stop sound

    "She laps up the effort I place into tainting sacred grounds and dirties herself in the process, but at least my feet are clean now."
    "Her tongue dissolves into a sludge that seeps back into her throat only to ooze out of every pore and, in that moment, looks more beautiful than I have ever seen before."

    play sound "static.mp3"
    scene amibus9 with flash
    stop sound

    "The ooze seeps back into her flesh before it seizes the opportunity to drip onto the ground of an area undiscovered before its ultimate absorption provokes the budding of a thousand eyes."

    a "Do you believe in God, Sensei?"

    "She asks again, but the beauty before me eliminates any chance I have to deny it once more."
    "I am condemned by an entity unseen- the same one who granted her an ever-abundance of vision."
    "The condemnation carries with it a single letter carved out of wood that fuses to my back the same way my bed in the early morning had been."
    "I fall as I am unable to bear its weight but encounter a moment of tranquility when my path intertwines with that of a REAL HUMAN FEMALE."

    play sound "static.mp3"
    scene amibus10 with flash
    stop sound


    saki "Greetings, you who are highly favored! The Lord is with you."
    s "Where? I can’t see him."
    saki "Greetings, you who are highly favored! The Lord is with you."
    saki "Greetings, you who are highly favored! The Lord is with you."
    saki "Greetings, you who are highly favored! The Lord is with you."

    "The REAL HUMAN FEMALE gets caught on repeat and my journey comes to an untimely demise."

    play sound "static.mp3"
    scene amibus1 with flash
    stop sound

    "We board a bus that’s moving backwards and all I can think about is a spot on the window where the guts of a bug we crashed into are smeared."
    "Dried by the sun and picked partially clean by whatever predators dared to crawl upon an invisible barrier, the spot casts a small shadow upon Ami’s arm."
    "In between the miniature hair follicles covering it, I imagine the bug springing back to life."
    "It’s blurred out, however, as I can not imagine what type of insect it was from just a stain alone."
    "The bus continues on (Or off) and I drift in and out of consciousness at the command of violent glares brought on by the god in the sky."
    "Oh."
    "So I do believe after all."

    a "Sometimes, I wish you knew how to drive."
    a "I think it would be nice to kind of just...drive around with you sometimes. "
    a "We wouldn’t have to go anywhere. Just being with you and taking in the sights would be enough."
    a "We could listen to music on the radio and talk about the things we’re afraid of admitting in front of others."
    a "Sometimes, I wish you knew how to drive."
    a "Because it would give us something to do when everything else disappears."
    s "What do you mean, “When everything else disappears?”"

    scene amibus6
    with dissolve

    a "Hm?"
    a "Did you just wake up?"
    s "If you thought I was asleep, who were you talking to just now?"

    scene amibus11
    with dissolve

    a "Sensei, I haven’t said anything this entire ride. You passed out the second we got on."
    s "What?"
    a "It’s obviously my fault for dragging you around all day, so I’m sorry if it was a little too much."
    s "And your hand?"
    a "What about it?"
    s "Is it okay?"

    play sound "static.mp3"
    scene amibus12 with flash
    stop sound

    a "It's totally fine!"
    a "I guess the cuts from the glass weren’t really that deep since you can barely even see them anymore."

    scene amibus6
    with dissolve

    s "I...see..."
    a "It still stings a little, but I’m sure I’ll feel totally normal by tomorrow."
    a "Oh, which reminds me-"
    s "Ami, I don’t think I have the energy required to go on an outing like this two days in a row."
    a "{i}Actually{/i}, what I was about to tell you is that I’ll be working all day tomorrow and that you won’t need to put up with me {i}at all.{/i}"
    s "All day? Did Uta call out or something?"

    scene amibus13
    with dissolve

    a "That’s the weird part. I got a text from Osako-chan while you were asleep saying that Uta hadn’t answered her phone all day."
    a "She was supposed to work today, too, but she just kinda...didn’t show up. "
    a "So if that happens again tomorrow night and nobody is there to cover for her, the cafe will have to close early or something and that would probably be pretty bad for business."
    a "I really hope she’s okay. She’s never done anything like this before."
    s "Should we maybe go check on her?"

    scene amibus14
    with dissolve

    a "If she’s not in school tomorrow, I think you should. I won’t have time, though, since I’ll have to go straight to work."
    s "It’s fine. I’ll just text Io to- oh."
    s "I guess I don’t get any service here."

    scene amibus11
    with dissolve

    a "Io? Since when do you have {i}her{/i} number? I thought she didn’t talk to anybody except Uta?"
    s "I am one of the very rare exceptions, I guess. But it looks like I’ll have to just ask her when we get home."

    scene amibus1
    with dissolve

    a "I guess so..."
    s "..."
    a "..."
    a "Sensei. Can I ask you something?"
    s "Sure. What’s up?"
    a "..."
    a "Do you believe in God?"

    scene black
    with dissolve2
    stop music fadeout 15.0

    "The bus continues on (Or off) and I drift in and out of consciousness at the command of violent glares brought on by the sky."
    "Ami does the same, collapsing onto my shoulder at several points following a question that would have been better suited for someone else."
    "Her skin feels much colder than normal and I wrap my arm around her to distribute some of my warmth."
    "Her breaths are unsteady. One. Two. One. Four. Eight."
    "Her lungs can’t seem to decide what it is they should be doing."
    "And my mind can’t seem to decide where it is that it should wander."
    "We get off the bus that’s moving backwards."

    stop sound

    "And we bend ourselves until we wind up at our door."

    "///////////////////////USER1 HAS SUCCESSFULLY LOGGED IN"

    $ renpy.end_replay()
    $ amidate50p4 = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump returntosummer1

label aminew1:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
a "A little..."
    a "I wrote this a little while ago, but...when I was going through some of Mom’s stuff last night, I found a bunch of her old poetry and remembered how much you liked it."
    a "I never really understood what the appeal of poems was back then, but reading them now...I think I finally get it."
    a "She had such an...um...eloquent way of writing? Is eloquent the right word?"
    s "..."

    scene amidatecafe26
    with dissolve

    a "You know what? I’ll just read one that I took a picture of and you can let me know if I’m on the right track."
    a "I’m sure that it’ll make my poem sound like, {i}really{/i} bad since she was basically a pro, but-"

    stop music
    play sound "static.mp3"
    scene spiderbug with flash
    scene amidatecafe27 with flash
    play sound "glass.mp3"

    a "Ah."

    "Ami drops her phone and it bounces off the table into the side of an empty glass."
    "The glass once held water, but it will never hold anything again."
    "I watch the shattering as if my world is plunged into slow motion."
    "Each shard moves in a different direction, some moving more distance than others without rhyme or reason as to why."
    "I am sure there is a scientific explanation for it, but I’d prefer to imagine it’s just random chance."
    "A nearby table joins in on the action and watches on, mesmerized as well."
    "There is something beautiful about being broken that attracts all sorts of onlookers."
    "I am glad the glass is what attracted most when there is so much that is broken all around me."

    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."

    scene amidatecafe28
    play music "lifeismostlygood.mp3"

    a "Huh? What happened to my phone? I was just-"

    scene amidatecafe29
    with dissolve

    a "Wait, what happened to that glass?! "
    s "Do you really not remember?"

    scene amidatecafe30
    with dissolve

    a "Remember what? What are you talking about?"
    s "You...literally dropped your phone into the glass just a few seconds ago."
    a "I...did?"
    s "Yeah...are you feeling okay?"

    scene amidatecafe31
    with dissolve

    a "Yeah. I feel totally fine. I...I have to clean that up, though. Somebody could get hurt."
    s "I’ll just flag down our waitress. I’m sure they have someone who-"
    a "No! That’s not fair to them."
    a "It’s my fault this happened. Besides, I’ve cleaned up a lot worse than this."

    scene amidatecafe32
    with dissolve

    a "But I guess I probably don’t have to explain that since my poem probably...reminded you of...anyway, yeah. I’m going to clean up the glass now."
    a "I’m sorry for causing a scene, Sensei. I know how much you hate being the center of attention."
    s "It’s fine..."
    s "Are you really sure you’re okay, though?"
    a "I’m..."
    a "I have to clean up the glass."

    scene black
    stop music

    "Ami bends down and begins to scoop the shards of glass into her hands."
    "I wonder if she, too, appreciates the beauty in how each and every one of them is unique."
    "I wonder if she, too, acknowledges how tragic it is that the object is now devoid of all purpose."
    "She cuts her hands as she cleans up the accident."
    "It reminds me of something."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amidate50p3 = True

    "........."
    "......"
    "..."

    jump amidate50p4
...
```