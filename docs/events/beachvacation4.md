# Extra French Fries (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [My Heart is Full](./beachvacation3.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation4
* Group: Main
* Triggered by label: makotoinnx
* Chain sources: beachvacation3
* Chain sources path: beachvacation3->beachvacation3

## Official wiki page

[Extra French Fries](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation4&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation4:
    scene mikuvac1
    with dissolve

    "Makoto and I split apart as soon as we get back to the beach. "
    "She said something about wanting to go get lunch but, not being particularly hungry myself, I elect to put on my swim trunks and walk around instead of tagging along with her."

    mi "Hey! You there! With the legs!"

    play music "highspeedprinter.mp3"

    "Being a person with legs, I instinctively respond and turn around to see Miku waving me over to the water."
    "She’s alone at the moment, so I imagine she needs someone to talk to or all of that energy welling up within her will cause her to explode and destroy Kumon-mi."
    "I live in Kumon-mi, so it would be bad if I were to sit back and let it explode."
    "I must do my duty to defend the city."

    scene mikuvac2
    with dissolve

    mi "Ahoy there matey!"
    s "Yo."

    scene mikuvac3
    with dissolve

    mi "Whatcha doin’? You and Makoto have fun doin’ cabin stuff?"

    if bonus == True:
        s "Sure. She had a little more fun than I did, though."
        mi "Makes sense. She’s always talkin’ about how cool and handsome and smart ya are."

        "That’s not really what I meant, but I’ll allow Miku to think whatever she wants since telling her I just fingered her best friend might scare her off."
    else:
        s "Yeah, it was actually really nice until she started talking about depression."

    s "What about you, Miku? What are you doing?"
    s "And why are you all alone in the water?"
    mi "Cause I like water! Duh."
    mi "Plus, there's nothin’ wrong with a little alone time every now and then."
    mi "I was playin’ with Ami and Ayane before but they went to get lunch and now I’m all like “Gahhhh woe is me” and stuff."
    s "Are you not hungry?"

    scene mikuvac4
    with dissolve

    mi "Nah. I had a huge breakfast this morning and if I eat more than 1300 calories in a day I’ll get fat and undesirable."

    scene mikuvac5
    with dissolve

    mi "It’s hard enough gettin’ people to look at me as a girl to begin with."
    mi "I’ve gotta keep up this tomboy thing as long as I can or I’ll just fade into the abyss."
    s "Hey, the tomboy thing works for you at least. "

    scene mikuvac6
    with dissolve

    if bonus == True:
        mi "Not as good as it works for Karin. Know any tips for your pal Miku to grow some big ole' melons like her?"
        s "…"
        mi "…"
        s "I could massage them for you?"
    else:
        mi "Not as good as it works for Karin."
        s "Shhh don't say that. There are a lot of people that don't consider her one of those and we don't want to make them angry."

    scene mikuvac7
    with dissolve

    if bonus == True:
        mi "Does that actually work?!"
        s "No idea. But I’m cool with it either way."
        mi "Is that even legal?!"
        s "…"
        mi "You know, cause we’re like student and teacher."
        s "Right. Yeah I don’t think there are any specific laws against teachers...massaging their students' breasts."
        s "It's just kind of...frowned upon."
    else:
        mi "Wait, are we bein' watched right now?!"
        mi "This ain't some sorta Truman Show thing, is it?!"

    scene mikuvac4
    with dissolve

    if bonus == True:
        "It doesn’t hit me how ridiculous that notion is until I get it out of me."
        "Miku doesn’t seem to mind, though."
        "If anything, she actually looks like she’s thinking about it."

        mi "Hmm...Idunno. Doesn’t that sound a little sketchy to you?"
        mi "Obviously I don’t know much about girl-on-guy contact and stuff, but I’m pretty sure that sorta thing is saved for boyfriends and girlfriends."

        scene mikuvac8
        with dissolve

        mi "Wait! Is this a confession?!"
        mi "I didn’t think the lewd stuff would come right off the bat!"
        mi "Oh! And I have like, zero boobs to begin with! It would be like massagin’ a countertop!"
        s "Calm down, Miku. It’s not like I’d be able to do it out in the open anyway. "
        s "There are several girls I can think of off the top of my head that would kill me if I came anywhere close to doing something like that."

        scene mikuvac9
        with dissolve

        mi "Phew. That’s a relief. "
        mi "I was startin’ to feel stuff I’ve never felt before."
        mi "Kinda like when you finish ‘yer french fries but, oh look! There are more in the bag!"

        scene mikuvac10
        with dissolve

        mi "Know what I’m talkin’ about?"

        "That is the strangest way I have ever heard arousal being described, but I guess I see where Miku is coming from."
        "Extra french fries are always a magical feeling."
        "…"
        "What the fuck am I even talking about?"

        s "Yeah, I know what you mean. "
        s "I’m not banned from thighs, though, am I? That was one of the key reasons I decided to coach your team."

        scene mikuvac11
        with dissolve

        mi "You didn’t decide anything. I had to force ya to join because you were takin’ too heckin’ long to agree."
        mi "I thought I had ya at soccer thighs but I guess adults are too mature to be swayed by things like that."
        s "I just needed some time to think it over. That’s all."
        s "I’ll gladly massage your thighs right now if you want. "

        scene mikuvac10
        with dissolve

        mi "But they’re not sore right now. "
        mi "And I’m gonna be here all weekend so I don’t have to worry about practice makin' 'em all tight either."
        s "I can’t just do it because I want to?"
        mi "Hm? Why on Earth would ya wanna do somethin’ like that?"
        s "Because you’re cute and I want to touch your thighs."
        mi "…"
        s "…"
        mi "…"
        s "…"

        scene mikuvac12
        with dissolve

        mi "Where the heck did that come from?!"
        s "Did I say something wrong?"
        mi "Heck yeah ya did! Ya can’t just come out and call a girl cute and tell her ya wanna touch her thighs! That’s like...adult stuff!"
        mi "Ya have to use the soccer thing as an excuse first! Yer skippin’ like eight steps here!"

        "Realistically, I’m only skipping one. Two at most."
        "But fine. I’ll play along."

        s "Okay. I’ll just wait until you’re {i}ready{/i} to get to the massaging."

        scene mikuvac13
        with dissolve

        mi "Good. Feels kinda weird when you’re not wearin’ a shirt anyway."
        mi "I knew you were muscley but like, geez. You and Karin should wrestle or somethin’ with bodies like that."

        "I will gladly wrestle Karin any day of the week."

        ka "Hm? What’s that about Karin?"
        s "Hm?"
    else:
        s "Hey, maybe it is! And maybe people will look back on this line in ten years and think {i}Darn that Selebus guy for telling us everything way beforehand.{/i}"
        mi "That's just the beauty of Lessons in Love, Sensei! No one ever knows what parts they're supposed to take seriously!"

        ka "Hello."

    scene mikuvac14
    with dissolve

    if bonus == True:
        "I turn around to find the Kanda sisters standing right beside me."
        "I had no idea they were coming, but I’m not about to complain."
        "Seeing the two of them in swimsuits is just as welcome as seeing the other twelve girls who tagged along for the trip."
    else:
        ka "We are also here now."

    ka "Hey, Sensei..."
    s "Hey. How long have you two been there?"

    if bonus == True:
        ki "Since the part where you were trying to touch Miku’s thighs."
    else:
        ki "Since the Truman show part."

    scene mikuvac15
    with dissolve

    if bonus == True:
        ki "I am quite sorry for your loss."
        mi "Woah! I didn’t even see you two walk over!"
    else:
        ki "It is no Seinfeld season three, but-"

    mi "I thought you couldn’t make it?"

    scene mikuvac7
    with dissolve

    s "You knew they were coming?"
    mi "Heh? You listenin’ to me? I literally just said I thought they couldn’t make it."
    s "Yeah but that implies that you knew they were planning on coming."
    mi "Well yeah, I invited them. The more the merrier and all that."
    s "We barely have enough room for everyone as-is."

    scene mikuvac16
    with dissolve

    ka "Should we not have come?..."
    ka "I had a feeling Miku wasn’t being entirely honest when she said she talked it over with everyone, but I thought that at least {i}you{/i} knew about it."
    ki "You’re not gonna make us go all the way home, are you?"
    ki "I’ve been doing crunches for weeks trying to get my tummy looking nice and tight for you."
    s "…"

    scene mikuvac17
    with dissolve

    ki "Oh, whoops! Did I say for {i}you{/i}? "
    ki "Hahahah! I meant for the beach. Silly me."
    ka "Really?..."

    if bonus == True:
        "I am suddenly faced with the challenge of not getting an erection in the middle of a conversation."
        "Game on."
    else:
        "I sure wish Kirin would stop flirting with me all the time. I never enjoy hugging her, and I'm pretty sure she doesn't like it either."

    s "I mean, we do have an extra room if you can't fit in the first one, so I guess it’s fine."
    s "I just feel kind of bad for Ayane and Makoto since neither of them knew about this."

    scene mikuvac18
    with dissolve

    ki "Ayane knows. I texted her on the way here."
    s "And she said she’s okay with it?"
    ki "Yeah. She even offered to buy us our own room if we wanted."

    "Just how much money does Ayane have to spare?..."

    s "Well, I guess it’s fine then. "
    s "Just try not to cause any problems."

    scene mikuvac19
    with dissolve

    ki "Problems? Just what kind of people do you think we are?"
    ka "We’ll be good. We wouldn’t want to make any trouble for you guys. "
    ka "And if you need help preparing dinner or anything like that, you can count on me."
    ka "It’s only fair that we do our part if we’re going to be staying with you."
    s "That won’t be necessary, but thanks for the offer."
    s "You look really cute by the way, Karin. That swimsuit fits you really well."

    scene mikuvac20
    with dissolve

    ka "C-C-C-C-C-C..."
    ki "…"

    "Karin breaks and Kirin looks at me with a growing sense of...probably jealousy or something."

    ki "Um..."
    s "...What?"
    ki "Where’s my compliment?"
    ki "Sorry if I’m {i}not your type{/i} or whatever but if you’re going to compliment my sister you should at least {i}acknowledge{/i} me. "
    s "Oh, my bad."
    s "You look cute, too, Kirin."

    scene mikuvac21
    with dissolve

    ki "No. Now you’re just saying that."
    ka "C...C...C...C..."
    ki "After all that work I did and everything. So annoying."
    ki "Actually, you know what? I’ll {i}make{/i} you appreciate me."
    ki "Here. Touch my tummy."

    if bonus == True:
        scene mikuvac22
        with fade

        "Kirin steps forward and grabs my hand, pulling it toward her stomach and pressing it against her."

        mi "Wha-?!"
        ki "Do you feel that? That’s weeks of hard work and you’re going to appreciate it, mister."
        s "Have I done something to offend you?"
        ki "What do you think? You complimented the one who’s just naturally great at everything and left the girl who worked her ass off in the dust."
        ki "Now appreciate my tummy."

        "Kirin locks eyes with me in a manner that is actually quite discomforting, especially with her sister and Miku right next to us."
        "It feels almost like she’s ready to assault me."
        "Now, I don’t know if it would technically be classified as assault because I’d be totally into it, but still."
        "This level of aggression is...intimidating, if not anything else."

        mi "Kirin, calm the heck down! And let go of Sensei’s hand! He’s like two inches away from ‘yer you-know-what!"
        ki "Don’t worry, Miku. It’s not like he’d ever touch it anyway since he’s so grossed out by the sheer thought of me."
        s "I think you might be taking this a little too far."

        scene mikuvac23
        with dissolve

        ki "And I think you aren’t taking it far enough."
        s "What does that even mean?"
        ki "I don’t know. Shut up. Just keep touching me."
        s "Are you sure that’s a good idea? Your face is starting to get red."

        scene mikuvac24
        with dissolve

        ki "It’s cause of the heat."
        s "…"
        ki "…"

        "No matter how long I stand here, Kirin refuses to let go of my hand."
        "I’ll just need to tell her what she wants to hear, I guess."

        s "Kirin, your body is extremely fit and the epitome of both femininity and eroticism. I wish I could stay in this moment forever."

        scene mikuvac25
        with dissolve

        ki "Aw~ How sweet. I had no idea you felt that way about me, Sensei~"
        mi "Kirin’s friggin’ scary..."

        scene mikuvac26
        with dissolve

        ki "You know, Sensei...My tummy’s not the only part of me that’s super tight."
        mi "AH! MY EYES!"

        "Kirin begins to pull my hand downward and sparks an immediate reaction from Miku."
        "But before I can pull away, the ace of the soccer team springs into action and leaps out of the water, running over to me and pushing Kirin to the ground."

        scene black
        with dissolve

        mi "OKAY! THAT’S ENOUGH!"
        mi "It’s my turn to get all touchy-feely with Sensei before anything Rated-M happens!"
        ki "Miku! What the fuck?! Did you really just push me over?!"

        "Miku hugs me from behind and pulls her body against mine, bringing one of her hands to my abdomen."

        scene mikuvac27
        with dissolve

        mi "Holy guacamole! You’re outright chiseled!"
        mi "Why the heck were you keepin’ these things hidden for so long?!"
        mi "If I had abs like this I’d be friggin’ crackin’ eggs on ‘em or somethin’."
        s "Weird compliment but I’ll accept it."

        "Miku’s hand trails back and forth across my body, poking and pressing nearly everywhere she can reach."
        "It isn’t long before Kirin gets jealous again and also hops on the bandwagon..."

        scene mikuvac28
        with dissolve

        ki "Holy shit, you’re right."
        ki "It feels like I have my hand on a rock right now."

        "Kirin follows suit and also allows her hormones to take control of her mind."
        "Both of their hands wander all over, Kirin’s often poking into my waistband, while Miku drags hers upward."

        mi "I think...I could do this all day."
        ki "Same. I want my own Sensei to take home and play with."
        s "There is only one of me and something unforgivable is bound to happen if the two of you keep touching me like this."

        scene mikuvac29
        with dissolve

        mi "Hm? What do ya mean ‘unforgivable’? Do ya not like bein’ touched or somethin’?"
        ki "Yeah, tell us Sensei~ What will happen if the two of us keep touching you like this?"
        s "Karin, why are you just letting this happen?"
        ka "C-C-C-C-C-C-C-"
        s "Oh, right. She’s broken."

        scene black
        with dissolve2

        "I’m able to last another ten seconds or so before I need to pull the plug and back away from the two of them."

        mi "Hey! Where do you think you’re goin’?"
        mi "We’re not done with you yet!"
        ki "Sensei! Come back! I wanna feel how hard it is!"

        "Kirin’s words are obviously packed with a double-meaning. "
        "Miku, I can forgive for not fully understanding what's going on, but Kirin-"
        "She knows what she’s doing."
        "It’s intimidating."
        "…"
        "I retreat to behind the restroom and press my back against the wall, waiting for a certain part of my body to calm down before I reveal myself again."
    else:
        scene black
        with dissolve

        s "No! You can't make me!"
        ki "Why are you running away from my stomach?!"
        s "This is not the right game for that!"
        s "I apologize to Miku and Karin for cutting the conversation short, but I must remain in compliance with Patreon's community guidelines no matter what the cost!"
        ki "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

    $ renpy.end_replay()
    $ beachvacation4 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

label beachvacation5:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
"And also it’s really funny seeing how desperate she gets when she’s about to cum."

    scene makotoinn15
    with dissolve

    mak "Nnf~ Fuck...[makotomaster]...that feels so good..."
    mak "I’m sorry for how...wet it is down there..."
    mak "We went swimming earlier and-"
    s "Again, just be quiet and accept your reward."

    scene makotoinn16
    with dissolve

    mak "How...hah...am I supposed to be quiet with your fingers so deep inside of me?"
    mak "Do you have any idea...how that feels for a girl?..."
    s "I don’t. But I’m assuming it’s pretty great based on your reactions."
    mak "So...great..."
    mak "It’s like...my heart is full..."
    mak "And knowing that you’re the one making me feel this way is...enough to get me to cum..."
    mak "But...but..."

    scene makotoinn17
    with dissolve

    mak "I don’t...want to cum just yet..."
    mak "Because then...it will be over...and I’ll have to do boring stuff like...make sure Miku doesn’t hit her head on things..."

    "I keep my motions steady, exploring Makoto’s insides with two of my fingers as she quakes and grinds against my hand."
    "What she says is true."
    "Once she cums, this {i}will{/i} be over."
    "Everyone’s waiting for us."
    "But that doesn’t mean it won’t ever happen again."
    "So for now, I just need to make her feel as good as possible."

    mak "[makotomaster]...[makotomaster]..."
    mak "Right there..."
    mak "Are you... really sure you don’t want to fuck me?"
    mak "I know you can fit two fingers in now, but I promise it’s still tight...probably..."
    mak "Boys like that right? Tight...pussies that...squeeze their big cocks..."
    s "You’re about to cum, aren’t you?"

    scene makotoinn18
    with dissolve

    mak "Ugh...yes...unfortunately..."
    mak "You’re too good at this...it’s...hah...annoying..."
    s "Just do it then. "
    mak "Ngh...fine...but..."
    mak "Next time...you’re putting it inside...whether you like it or not..."
    s "Whatever you say, Makoto..."

    scene makotoinn17
    with dissolve

    mak "[makotomaster]...[makotomaster]..."

    "Her breaths grow heavier and her hips begin to rock harder against me, pushing my fingers inside of her as deep as they’ll go."

    mak "Right there...just like that..."
    mak "I’m..."
    mak "I’m going to..."

    scene makotoinn19
    with dissolve

    mak "Oh god...oh god...yeah...yeah..."
    mak "[makotomaster]! I’m...I’m-"

    with sexfade
    with sexfade
    scene makotoinn20
    with cumflash
    with hpunch

    mak "AAAAAAAAAHHHHHHHNNNNNNN~~~~!!!!!!!!"

    "A violent climax consumes Makoto’s mind. The bed shakes as her back arches."
    "I lift her up from the inside, pulling her toward the headboard and letting her cum on my fingers, now tightly squeezed by her vaginal muscles."
    "Tears begin to flow from her eyes, but not because she’s upset."
    "At least I don’t think that’s the reason for them."
    "But who even knows at this point?"
    "I’m just here to have fun with cute girls."
    "That’s all there is to this life."

    scene black
    with dissolve2

    "And that’s all there will ever be."

    $ renpy.end_replay()
    $ makoto_love += 3
    $ beachvacation3 = True
    stop music fadeout 6.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    jump beachvacation4
...
```