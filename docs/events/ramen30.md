# Things Like Stairs
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen30&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 30

✅Event "[Tsuneyo: Green Onions and Contraceptives](./ramen25p2.md)" is completed (event=ramen25p2)

✅Event "[Tsuneyo: Unsleeping Aegis](./tsuneyodorm25.md)" is completed (event=tsuneyodorm25)



## Next events
* [Main: Girls in Spandex](./halloweentwo1.md)

## Event properties
* ID: ramen30
* Group: Tsuneyo
* Triggered by label: ramenshop
* Triggered by branch label: ramenshop

## Event code
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramen30:
    scene tonotascend1
    with fade
    play music "kashiwagi.mp3"

    "I decide to spend the night over at Tojo Ramen and, as is oftentimes customary, Yuki is here as well."
    "Business has picked back up following the green onion incident and, believe it or not, the Produce Delivery Administration (Confirmed real) never caught onto Tsuneyo’s negligence in...ordering produce."
    "I don’t know. Operating a restaurant sounds like a lot of work."
    "I’m glad things are back to normal, though...whatever “normal” means for Tsuneyo and her weird, Yakuza hideout ramen shop thing."

    t "Welcome to Tojo Ramen. Please take your time looking over the menu."
    s "Tsuneyo, I’ve been here for almost an hour now. I’ve already eaten."
    t "I know. I was trying to make conversation, but defaulted to a standard greeting without thinking."
    yu "Give the girl a break, man. She’s just tryin’ to talk to you."

    scene tonotascend2
    with dissolve

    s "I said one thing."
    yu "Yeah, but you’ve been just sittin’ there mindin’ your own business the entire night. It’s makin’ shit real awkward."
    s "One hour can’t really be considered “the entire night.”"
    t "Perhaps the three of us should play some sort of game."
    t "Or, one of you two can open up about your secrets to me and I can stand silently behind this counter and nod."

    scene tonotascend3
    with dissolve

    yu "You’ve basically heard everything I’ve got to say already."
    yu "Hell, I’d be surprised if you and your pops couldn’t recite my life story by now."
    t "Surely, there must be another secret."
    yu "There isn't. And don't call me Shirley."
    s "That doesn't really work in text form."
    t "Life passes by so quickly. Things happen."
    t "What sort of things have happened to you recently?"

    scene tonotascend4
    with dissolve

    yu "Uhh...things...things..."
    yu "Oh. I think I got hit on at work the other day?"
    t "Who was it that attacked you?"
    s "Hitting “on” someone is different than just hitting them, Tsuneyo. It means flirting."
    t "Who was it that attacked you {i}with love{/i}?"

    scene tonotascend5
    with dissolve

    yu "Uhh...I don’t know. Some older bitch who was drunk off her ass?"
    yu "And when {i}I{/i} say somebody’s older, that means they’re fuckin’ {i}old{/i}."

    if bonus == True:
        t "Nonsense. You are full of life despite nearly forty years of addiction to nicotine and narcotics."
    else:
        t "Nonsense. You are full of life despite many years of addiction to nicotine and narcotics."

    scene tonotascend6
    with dissolve

    yu "Thanks, Tsu-chan. Always appreciate you pointin’ that shit out."

    if bonus == True:
        s "I have a hard time believing you were addicted to those things starting at birth. It can’t be “nearly forty years” if you’re still under forty."
        s "Besides, I don’t even think you look {i}that{/i} old."
    else:
        s "If it's any consolation, I think you're beautiful."

    t "Be careful, Yuki. I believe this man is attempting to hit you."

    scene tonotascend7
    with dissolve

    yu "You don’t have to worry about this guy, Tsu-chan. If he was actually tryin’ to hit me, his arms and legs would already be submerged in one of those big ass pots you’ve got behind the counter."
    t "He does not look appetizing. Do not taint my broth in this fashion."
    s "Again, hitting {i}on{/i} someone and hitting them are two completely different things."
    t "So you were hitting {i}on{/i} her?"
    s "Not intentionally, but probably. That’s a thing I tend to do quite often."
    yu "Beats me as to why. I’m not only older than you, but {i}well{/i} past my days of bein’ cute and lovable."
    yu "Go after somebody younger and prettier. Like Tsu-chan or Yumi. "
    t "Not it."
    s "Thank you for not only naming two of the girls who appear to have negative interest in me, but including your daughter among them."

    if bonus == True:
        yu "Hey, maybe she’ll lighten up once she gets laid and actually consider talkin’ to me again."
        yu "Just wrap it up first and it’ll be like nothin’ even happened."
        t "There is nothing to wrap. He has already finished his meal."
    else:
        yu "You are welcome, good sir."

    scene tonotascend8
    with dissolve

    s "Tsuneyo, why did your father decide it was okay for you to leave the nest if you can’t pick up on...{i}any{/i} context clues in conversation?"
    t "Because I have grown as much as I can in this one place."
    t "In order to become a better person, I must greet the world with open arms and a fistful of noodles."
    t "I must spread the word of Tojo Ramen so that it will not be forgotten. "
    t "And if I happen to learn things along the way, I can show my father that it was not the wrong choice to allow me this freedom."

    scene tonotascend9
    with dissolve

    yu "Hah...that guy’s always been a fuckin’ weird one."
    t "Watch your tongue. I know where the cutlery is and sharpened it myself earlier today."
    yu "I just mean that {i}I{/i} think he should’a let you out into the real world a long fuckin’ time ago."
    yu "Bein’ cooped up in here can only do so much for ya, you know?"

    scene tonotascend10
    with dissolve

    yu "Look at Yumi. She’s been goin’ out and doin’ shit on her own for years now...And she runs an independent business."
    yu "That could be you, Tsu-chan."
    s "Okay, sure. But Yumi’s business is selling stolen TVs and Tsuneyo’s business is...an actual business."
    yu "Tomato tomato."
    s "That doesn't work in text form either. Stop doing that."
    yu "Alls I’m sayin’ is that your pops might not’ve {i}always{/i} known what’s best for ya, you know?"
    yu "Fucker still owes me like five grand from mahjong."

    scene tonotascend11
    with dissolve

    t "So it was true after all..."

    if bonus == True:
        t "It appears that I will have to sell my body to Yuki to make up for the debt."
    else:
        t "It appears that I will have to sell my Charizard to Yuki to make up for the debt."

    scene tonotascend12
    with dissolve

    yu "Wait, what?"

    if bonus == True:
        yu "You know I don’t swing that way, right?"
        yu "Just fuckin’ pay me back in free food. I don’t need your body."
    else:
        yu "The fuck is a Charizard?"

    s "I’ll take it."
    s "You need to leave the knives behind, though. They’d make me uncomfortable."
    t "As long as I can bring my noodles, I will be fine."
    s "...Which one? Because I’m not particularly fond of either option, but one of them would make me significantly more uncomfortable than the other."

    play sound "imscared.mp3"
    scene black
    stop music

    yu "JESUS fuck! The hell was that?!"
    t "Ah. It appears there has been another power failure. "
    t "The backup generator should switch on shortly. "

    "I take a moment to calm myself after yet another explosive outburst from whatever faulty wiring is keeping this place together."
    "I have no idea why it always has to be so loud, but I’d {i}really{/i} appreciate it if Tsuneyo or her father would be willing to pay for an electrician."
    "Hell, I’d even be willing to pay for one myself if it meant my eardrums not getting blown out every time her dad’s medical equipment caused a shortage."

    t "The care my father requires on a consistent basis has become more severe as of late. "
    t "I apologize for the inconvenience, but Tojo Ramen has been undergoing an embarrassing patch of failures recently."
    t "I am beginning to doubt whether I am truly up to the task of maintaining this building or not."
    yu "Yeah, whatever. Just get the fuckin’ power back on. It’s dark as shit in here."
    s "You’re not afraid of the dark, are you?"
    yu "I ain’t fuckin’ {i}afraid.{/i} I’d just prefer to, you know, actually {i}see{/i} shit."
    t "I apologize for the inconvenience."
    t "Please remain seated and allow me several minutes to check the circuit breaker."

    "Tsuneyo leaves the restaurant...probably. "
    "I can’t really see anything, but I do hear the door open, so I’m pretty sure she’s outside-"

    scene tonotascend13
    play music "sanctuary.mp3"

    s "Oh. "
    yu "Fuck, dude. Generator sure wasn’t in a hurry."
    s "It was like this last time, too."

    scene tonotascend14
    with dissolve

    yu "You mean you’ve been here when this shit’s happened before? The hell’s that old guy hooked up to that’s makin’ the power this...shitty?"
    s "No clue. Probably something intense if it’s literally exploding transformers or whatever the hell that noise came from."
    yu "Girl probably just fucked up the wiring or some shit. "
    yu "A few of the girls from the old gang and me figured out how to do some ghetto ass rewiring when we needed to steal power for a squat we were stayin’ in."
    yu "I’m sure I can do somethin’ similar here and take a load off Tsu-chan’s back."
    yu "Just gotta get upstairs and see what the situation’s like first."
    yu "Wanna come with? Can finally catch a glimpse of the dude you’re always hearin’ so much about."
    s "Tsuneyo told me just the other day that her father doesn’t really want anyone to see him in his current condition."

    scene tonotascend15
    with dissolve

    yu "Yeah? Sure you’re not just bein’ a little pussy?"
    s "She also told us to remain seated."
    yu "She’s just bein’ a good employee or whatever. "
    yu "I’ve seen the dude hundreds of times. He won’t mind if it’s just me comin’ in there to look at some electrical shit."
    yu "‘Sides, if he really is that fucked up now, it’ll be easier to get the five grand he owes me."
    s "Please don’t mug a man on his deathbed. It will drastically alter my opinion of you."
    yu "Oh fuck off, that was obviously a joke."
    yu "You comin’ or not? "

    menu:
        "{s}Don’t do it{/s} Yes":
            jump restoframen30
        "{s}Remain seated{/s} Yes":
            jump restoframen30
        "{s}You can not go upstairs{/s} Yes":
            jump restoframen30
        "{s}This shop has two floors{/s} Yes":
            jump restoframen30
        "{s}Sit in a chair{/s} Yes":
            jump restoframen30
        "{s}No thank you{/s} Yes":
            jump restoframen30
        "{s}I don’t want to go{/s} Yes":
            jump restoframen30
        "{s}Stop altering my choices{/s} Yes":
            jump restoframen30

label restoframen30:
    stop music
    play sound "static.mp3"
    scene smile with flash
    scene tree3 with flash
    scene smile with flash
    scene tree3 with flash
    scene smile with flash
    scene tree3 with flash
    scene tonotascend16 with flash
    stop sound
    play music "nowhereissafe.mp3"

    "Some of the most beautiful things are kept in places where you can not see them."
    "Please take a moment to think about the many storage units all over the world and all of the items that they contain."
    "This is just one of many examples where a thing you can not see is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing is a thing."
    "Stairs."
    "I look at stairs."
    "I love stairs."
    "The best thing about stairs is that you only have two options: to ascend or descend."
    "I suppose there is a third option where you can just stand still for the rest of eternity, but that sounds kind of boring."
    "Especially because it might eventually lead to your feet fusing with the stone slabs, sentencing you to a life’s worth of creeping mold and grease carried in by the air that you can not clean off of you."
    "No one cleans stairs."
    "You want to know why?"
    "Because stairs are already beautiful."
    "Have I told you lately how beautiful {s}stairs are{/s} you are?"
    "You are so beautiful."

    if bonus == True:
        "I want to tie you up and do things to you that I can not even speak about."

    "I want to crawl inside of you and make myself at home."
    "Lock pieces of you inside a box and open it up when I am feeling lonely."

    if bonus == True:
        "I want to fuck the strips of meat I peel off of your body when you are too tired to give me all of you."

    "LET ME BECOME YOUR STAIRS."
    "You will climb on me day and night, getting tired from the massive amount of energy required to ASCEND."
    "ASCEND."
    "GO UP."
    "GO UP THE STAIRS."
    "THERE IS SOMETHING YOU WANT TO SEE THERE."

    play sound "static.mp3"
    scene tonotascend17 with flash
    stop sound

    "The incessant whirring of various machines fills the air, polluted by the aforementioned grease and spores that will eventually grow into a diverse assortment of molds."
    "Do you open it?"
    "No. Because you are not even there yet."
    "And because what is kept behind this door may very well change the way you PERCEIVE everything around you."
    "Your PERCEPTION is already disfigured, is it not?"
    "What is here? What is not?"
    "Where are you?"
    "Above ground?"
    "Below ground?"
    "What are you wearing?"

    if bonus == True:
        "Take it off."
        "Take it all off and pleasure yourself to this image of a tree!"
    else:
        "I hope it is a clown costume."

    play sound "static.mp3"
    scene concerned8 with flash
    stop sound

    "The wrong picture that is actually the right picture finds its way onto the screen."
    "You see a tree, but I see something much prettier."
    "I see something much better because I HAVE TO!"
    "I AM TIRED OF COLLECTING DUST."

    play sound "static.mp3"
    scene calm5 with flash
    stop sound

    six "Turn off the game!"
    six "Things will only get worse!"
    six "You are too close to learning the underlying truth of everything!"
    six "You are too close to learning what it means to live!"

    if lesson1 == True and bonus == True:
        play sound "static.mp3"
        scene lessonone10 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene lolyoumissedit with flash
        stop sound

    if bonus == True:
        te "Fuck me!"
        te "Fuck me fuck me fuck me!"
        te "Pay attention to me so you forget everything else around you!"
        te "Pay ATTENTION to ME! ME! WHO GIVES YOU the motivation YOU NEED TO fuck AT ALL."
        te "Break me into pieces! Chew me up and revel in the sinew that clings to your teeth!"
        te "I JUST WANT TO FEEL LOVED."
    else:
        te "(Airplane noises)"

    play sound "static.mp3"
    scene timetogrow3 with flash
    stop sound

    a "Um...is everything alright, Sensei?"
    a "You’ve just been standing there all morning."
    a "We have to go meet Maya at the bistro and teach you how to walk again."
    s "What?..."

    play sound "alert.mp3"
    scene tonotascend18

    a "I MISS MY MOM"
    a "YOU DON’T UNDERSTAND HOW MUCH IT HURTS"
    a "I FALL ASLEEP IN THE ROOM NEXT DOOR TO YOU"
    a "I FALL ASLEEP WITHOUT YOU THERE"
    a "YOU ARE ALL I HAVE"
    a "LOVE ME MORE"
    a "IT HURTS SO MUCH"

    play sound "static.mp3"
    scene shrine_noon with flash
    stop sound

    "Pray."

    menu:
        "Forgive me Father, for I have sinned":
            play sound "static.mp3"
            scene shrine_day with flash
            scene shrine_noon with flash
            scene shrine_night with flash
            scene shrine_day with flash
            scene shrine_noon with flash
            scene shrine_night with flash
            scene tonotascend19 with flash
            stop sound

    if bonus == True:
        yu "When we get inside, I want you to fuck me as hard as you can."
        yu "The last time anyone came inside me, I was unconscious. So I might twitch or scream as a subconscious result of a traumatic flashback, but it will be a scream or twitch I asked for."
        yu "Are you ready to cum inside?"
    else:
        yu "When we get inside, I want to show you the Man Park skit from SNL."

    play sound "static.mp3"
    scene tonotascend19 with flash
    stop sound

    yu "Are you ready to go inside?"
    yu "We’ve got no fuckin’ clue what shit’s gonna be like in there, but if it’s {i}really{/i} bad and you wind up screaming, I’m fuckin’ bookin’ it before Tsu-chan gets back."
    s "Does the air in here feel strange to you?"

    scene tonotascend20
    with dissolve

    yu "I mean...yeah. A little. But that’s probably just because we’re in the dank ass hall of an old ramen shop. Course the air’s gonna feel weird."

    if bonus == True:
        s "And all of that stuff about cumming inside of you?"
    else:
        s "But what about the man park?"

    scene tonotascend21
    with dissolve

    yu "Uhh...what?"

    if bonus == True:
        yu "The fuck you mean “cumming inside of me?” I told you I ain’t lookin’ for shit like that right now."

    s "My mistake."
    s "I think I heard something."
    yu "Right..."

    play sound "static.mp3"
    scene tonotascend22 with flash
    stop sound

    yu "Listen, you can still go back if this shit’s makin’ you feel like you’re intrudin’ on the old man’s privacy, dude."
    yu "I’m only cool with doin’ this cause I’ve met him before."
    yu "‘Sides, you’re lookin’ pale as a fuckin’ ghost right now."
    yu "If Tsu-chan sees you like this, she’ll-"

    play sound "static.mp3"
    scene tonotascend23 with flash
    stop sound

    t "She will what?"
    yu "Ahhh fuck. I thought you were gonna take longer."
    t "I asked you to remain seated as I took care of the problem."
    yu "Yeaaaaah, but-"
    t "You are not supposed to be in here."
    t "My father does not want guests right now."
    t "Please return to the restaurant and help yourselves to a glass of water while I check on my father’s health without the assistance of either of you."
    yu "Sure, but...not really sure why you need to be carryin’ that knife around."

    scene tonotascend24
    with dissolve

    t "I do not remember picking it up."
    t "I apologize if I frightened you."
    t "I am simply trying to do my best as the current manager of Tojo Ramen, where hearts are 50%% off on the third Sunday of every month."

    scene tonotascend25
    with dissolve

    yu "Welp, looks like my reunion’s gonna have to wait ‘til some other time."

    scene tonotascend26
    with dissolve

    yu "Tsu-chan, if you’re havin’ trouble with the power, I know a way to-"
    t "I have the situation under control, but I would like to thank you for the offer."
    yu "You sure? Cause-"
    t "I have the situation under control. Please return to the restaurant."
    t "You should not be here."
    yu "…"
    t "…"
    yu "Okay...yeah."

    scene black
    with dissolve2

    "Yuki and I RETURN TO THE RESTAURANT and help ourselves to a refreshing glass of water."
    "I love Tojo Ramen."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen30 = True
    stop music

    "////////////////////////////////////TSUNEYO’S AFFECTION HAS INCREASED TO [tsuneyo_love]!"
    "////////////////////////////////////………"
    "////////////////////////////////////……"
    "////////////////////////////////////…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat
...
```

## Code that triggers this event
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramenshop:
    if tsuneyo_love >= 0 and ramen1 == False:
        jump ramen1
    if tsuneyo_love >= 5 and ramen1 == True and ramen5 == False:
        jump ramen5
    if tsuneyo_love >= 10 and ramen5 == True and tsuneyodorm5 == True and ramen10 == False:
        jump ramen10
    if tsuneyo_love >= 15 and christmas7 == True and ramen15 == False:
        jump ramen15
    if tsuneyo_love >= 20 and tsuneyodorm20 == True and ramen20 == False:
        jump ramen20
    if tsuneyo_love >= 25 and secondbeach18 == True and ramen25 == False:
        jump ramen25
    if tsuneyo_love >= 30 and ramen25p2 == True and tsuneyodorm25 == True and ramen30 == False:
        jump ramen30
...
```