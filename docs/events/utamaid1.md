# Abuse of Power (Uta)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Uta love greater than or equal to 0

* Event [Caterpillar](./day247.md) (Main) is completed)



## Next events

* [Uta: Love Me to Pieces](./utamaid5.md)

## Event properties

* Id: utamaid1
* Group: Uta
* Triggered by label: utamaid
* Triggered by branch label: utamaid
* Triggered by path: utamaid->utamaid1

## Official wiki page

[Abuse of Power](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utamaid1&go=Go) for more details.

## Event code

File: (install folder)\game\UtaEvents.rpy

Code:
```python
...
label utamaid1:
    scene utafirstmaidcafe1
    with dissolve
    play music "maidcafe.mp3"

    "I walk into the maid cafe to find it pretty much deserted- which I guess makes sense considering that they close in around an hour."
    "There’s a little bell near where you walk in that I guess they want you to ring in the event of something like this happening, but..."
    "I am a man."
    "I shall ring no bell."
    "I will remain standing right here until a maid emerges from the kitchen and awkwardly discovers that there is someone waiting to be taken advantage of."

    u "Uta-chan’s maid-senses are tingling! Someone has arrived!"

    "That someone is me. "
    "She could probably sense my unrivaled love for her."

    scene utafirstmaidcafe2
    with dissolve

    u "Ah! Sen- Master! You came to visit me!"
    s "Woah. Did you almost break character just now?"
    u "Uta-chan is the perfect maid who never breaks character and makes all of her masters leave with full hearts and full tummies!"
    u "And, in return, she gets to leave with a full coinpurse!"
    s "That last part didn’t seem like a very maid-like thing to say."

    scene utafirstmaidcafe3
    with dissolve

    u "Sorry, Master. I just feel so comfortable around you that I guess I let a little bit of my true self slip. "
    u "Teehee~"
    s "God, you’re good at this."

    scene utafirstmaidcafe4
    with dissolve

    u "I like taking care of people. "
    u "I talked about it in class but I was looking after my grandpa before coming here."
    u "Most people would probably get bothered by something like that after a while but I thought it was kinda fun!"
    u "Like taking care of a baby except the baby is like four times your age and smokes cigarettes."
    s "Ahh, yes. I can totally see the correlation."

    scene utafirstmaidcafe5
    with dissolve

    u "Good! Cause today, since nobody else is around, Master gets Uta-chan all to himself!"
    u "I’ll be sure to make you even happier than I used to make grandpa before the cancer spread."
    s "…"
    u "…"

    "She doesn’t even realize how dark that was, does she?"

    s "You sure that’s okay? I feel kind of bad for showing up so late in hindsight- like you’re supposed to be cleaning right now or something."
    u "Of course it’s okay! I’m not really supposed to be spending so much time in the back anyway."
    u "I need a stepping stool to reach most of the stuff back there and it’s led to a few more broken glasses and dishes than I’d like to admit."
    u "But it’s no fun talking about things like that when you’re here to unwind! Come take a load off, Master! I’ll sit you down at my favorite table!"

    scene black
    with dissolve

    "Uta breaks the no-contact policy she informed me of the first time I came here and grabs my wrist, pulling me to a table near the window."
    "She doesn’t sit down beside me. But she {i}does{/i} slam her hands down onto the table like some sort of detective interrogating a murder suspect."

    scene utafirstmaidcafe6
    with dissolve

    u "So, Master...how can I make your dreams come true today?"

    if bonus == True:
        s "You can start by calling your parents."
        u "Sorry, Master. I can’t talk about things that frisky while I’m on the clock."
        u "Unfortunately, Uta-chan will have to reject you once again."
        u "But if there is anything slightly more legal that you’re interested in, all you need to do is let me know!"
        s "I can just wait an hour or two until you’re off the clock. It’s fine."
        u "Such determination. You’re really cute when you set your sights on something, Master! "
        u "I’m not weirded out at all!"
        s "Saying that makes me feel like you are..."
        u "Hey, know what’s even better than all of those dirty thoughts you’re having right now, Master? "
        s "...Nothing?"
        u "A nice...hot...plate of dinner!"
        s "That’s not really better but I guess I’ll have to settle for it."
    else:
        s "I am just here for food. I do not wish to converse with you."

    scene utafirstmaidcafe7

    u "Do you need a menu? Or do you want me to just have them make you something I know you’ll fall in love with?"
    u "Besides me, I mean~"

    if bonus == True:
        s "Uta, I want you to know that you make it very hard to not flirt with you when you say things like that."
        u "Of course. That’s the whole point of places like this, silly. "
        u "I say things to make you feel good and, in return, you spend all of your money on little-ole Uta-chan so she can buy more socks and underwear."
        s "And I’m guessing you tacked underwear onto the end of that as another part of the maid-strategy?"
        u "It worked, right? Are you thinking about my panties now? "
        u "It makes you want to spend more money on me, right?"
    else:
        s "The service here is entirely inappropriate and not at all welcome."
        u "Then why are you already trying to tip me?"

    "I look down at the table to find that I’ve already begun subconsciously sliding my wallet toward Uta."

    s "When did this even happen?"

    if bonus == True:
        u "You reached into your pocket the second I said underwear."
        u "Even girls do that sometimes. It’s kinda crazy how well it works."
        u "I guess I’m pretty good at this, huh?"
        s "Yes. You’re going to bankrupt me one day."
    else:
        u "Just now."
        s "Did you use one of your secret maid tactics on me? Is the flavor beam actually a curse?"
        u "Yes."
        s "Why would you do this?"

    scene utafirstmaidcafe8
    with dissolve

    if bonus == True:
        u "Uta-chan can’t help it if Master lets his mind wander. But as long as he’s happy and keeps his hands to himself, he can do whatever he likes."
        u "And, in the meantime, I’ll go put your order in! Try not to stare at my butt as I walk away, okay? "
        u "My skirt’s a little short today so I’m kinda worried you might accidentally catch a peek~"
        s "..."
    else:
        u "Idunno. World domination maybe?"

    s "Are you actually a genius, Uta?"

    scene utafirstmaidcafe9
    with dissolve

    u "Just a maid~ We’re all like this. "
    u "Ami will be exactly like me soon. Just you watch."

    scene utafirstmaidcafe10
    with dissolve

    if bonus == True:
        "Uta walks away and I realize that her skirt isn’t any shorter than normal. I know this for sure because I {i}always{/i} stare at her as she walks away. "
        "I’ve been deceived."
        "And also, now I have to worry that Ami will be using these same tricks on me soon."
        "This is no haven for degenerates. It’s a prison."
        "It sucks us in under the false pretenses of cute girls who will unconditionally care about us-"
        "When in all actuality, it’s just a cash-vacuum that they use and abuse until they can line their pockets with our hard-earned money."
        "I shall not be defeated by a place like this."
        "I am a man."
        "I didn’t even ring the bell."
        "All I have to do is hold out a little while longer..."
    else:
        s "No. Anyone but her."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene utafirstmaidcafe11
    with dissolve

    "Uta comes back several minutes later with a plate of omurice, but instead of blessing it with the ritualistic flavor-beam, she sits across from me and presses her fingers together."
    "This time it feels less like the work of a criminal-investigator and more like some sort of...seductive older woman. "

    u "You know, Master. It just occurred to me while I was in the kitchen that I can {i}really{/i} take advantage of you if I want."
    s "Have you not already been doing that?"
    u "Of course not. Uta-chan’s been nothing but affectionate and attentive toward you. "
    u "She even went as far as infusing all of the love in her little heart into this omelette."
    s "If you’re looking for more money, I don’t know what else I’d even be able to give-"

    scene utafirstmaidcafe12
    with dissolve

    u "Calm down. I’m not actually going to do anything."
    s "You say that, but I have a hard time believing this isn’t part of your scheme as well."

    scene utafirstmaidcafe13
    with dissolve

    u "Heheh~ It’s not. Really."
    u "I was just thinking that it’s a little risky for someone working in public education to even come to a maid cafe this close to the[school] in the first place."
    u "The only reason I got a job here instead of somewhere closer to my old[school] was that I was worried about being caught."

    if bonus == True:
        u "But here you are, an actual teacher, throwing all of his money at Uta-chan and thinking about her underwear and stuff."

        scene utafirstmaidcafe14
        with dissolve

        u "Aren’t you worried about getting caught?"
        u "Like, what if a girl from a different class saw you here and ratted you out to one of the other teachers or something?"
        s "Well...that would probably make me look bad. But I think they’d also be revealing that they have a job in the process, so they’d be effectively ratting themselves out as well."
    else:
        s "That seems like a rational concern. Can you please serve me now?"

    scene utafirstmaidcafe15
    with dissolve

    u "Wait, are we not allowed to have jobs at this[school]?"
    u "My other one was fine with them as long as they were part-time and we kept our grades up."
    u "Oh, wait! You’re actually here to blackmail Uta-chan, aren’t you?!"

    if bonus == True:
        u "You want to get freaky with her so badly that you’re abusing your power because you know you can get her on her back-foot!"
        u "Or even worse- her back!"
        s "...While the desire to “get freaky with you” may almost certainly be true-"
        u "Almost?! Uta-chan’s not even a definite candidate in her ultimate form?!"
        s "...I have no intention of blackmailing you."
        s "You keep my presence here a secret and I’ll keep yours a secret in return."
    else:
        s "I am just here to eat food in peace."

    scene utafirstmaidcafe16
    with dissolve

    u "Ah! Back-scratching! It’s finally shown up!"

    if bonus == True:
        s "That’s right. We’re both breaking rules by being here, so the least we can do is help each other continue to break them instead of abiding by them."
        u "I agree. Rules are dumb. Like, there’s that one rule at the mall where you can’t even bring more than like five things into the dressing room at once."
        u "But what if I wanna try on more than five things? You know?"
        u "And also, what’s the deal with not being able to use your cell-phone on planes? I hate rules."
        s "None of that really has anything to do with what I was trying to say, but I feel you."
    else:
        s "What are you talking about? Go get the manager. This is unacceptable."

    scene utafirstmaidcafe17
    with dissolve

    u "Whaaaat? You want to {i}feel{/i} me? Master! Keep your voice down."

    if bonus == True:
        s "You know, that’s not what I meant, but it’s true so there’s no sense in denying it."
        s "I would like to “feel” you immediately, if at all possible."

        scene utafirstmaidcafe18
        with dissolve

        u "Wait, no. It feels kinda weird if you just go along with it like that."
        u "We’re supposed to keep going back and forth for a little while and then I’m supposed to shoot you down and apologize. "
        u "You’re breakin’ out of the pattern here. Next thing I know, you’re going to be telling me you weren’t even staring at my butt as I walked away."
        s "Oh, I can guarantee that I was doing just that."
        s "Your skirt is also the same size as always."
    else:
        s "What? No."
        s "I have absolutely no idea what you are talking about."
        s "I am so hungry."

    scene utafirstmaidcafe19
    with dissolve

    u "Stooooooooop right there, Master!"
    u "As flattered as I am to hear that you think I’m cute enough to stare at me as I walk away, I’m afraid that I can’t let things go any further."
    u "So I am sorry but, once again, I must reject you. Please do not hold this against me or take it out on my report card."

    if bonus == True:
        u "I am willing to do several special things to increase my grades after hours but probably not the things you want me to do."
        s "What does that even mean? What sort of things would you do to increase your grades?"
        u "I can’t tell you that or you’ll lower them on purpose. Please forget I said anything and enjoy your omurice."
        u "It was made with love. Lots of love. All of the love in my tiny body."
        s "…"
        u "…"
    else:
        s "Someone please help me."

    scene utafirstmaidcafe20
    with dissolve

    u "Heheh~"
    u "Talking to you is fun."
    u "And I’m not just saying that as Uta-chan. "
    u "Did you ever get annoyed with me those first few days I transferred in? How I stuck to your side the whole time?"

    if bonus == True:
        s "Annoyed? Not really. "
        s "You talk a lot but it’s not like you do anything that actually disrupts my day."
        u "Well, that’s good. I’m glad I asked. "
    else:
        s "Yes."

    scene utafirstmaidcafe14
    with dissolve

    u "Question, and you can say no if it makes you feel weird, but did you maybe want to give me a ride back to the dorm after this?"
    u "I’m still new-ish to the area and not totally comfortable going alone yet."
    u "Io was gonna come meet me but I’m pretty sure she fell asleep or something."
    s "I don't have a car, so I can't give you a ride. But we can walk back if you'd like."

    scene utafirstmaidcafe15
    with dissolve

    u "An adult without a car?!"
    s "This is the city. We don’t really {i}need{/i} cars with all the public transportation here."
    u "Oh right. I’m not in the country anymore."
    u "Well then, did you want to walk back with me instead?"
    u "As long as I have some big guy like you next to me, I’ll feel a lot safer."
    u "That crazy brawl with Yumi really gave me a wake-up call about how weak I am."
    s "That crazy brawl was a two-second arm-wrestle, but sure. I’ll walk back with you."

    scene utafirstmaidcafe16
    with dissolve

    u "Yay! "
    u "But remember, no holding my hand unless I ask you to. "
    s "Right. Keep my hands in the vehicle at all times. You’ve said that before."
    u "Yes. Uta-chan is not for sale."
    u "Unless you hire me to come clean your room or your house or something. I’d probably do that for you."
    s "Ami normally handles all of that, but I’ll let you know if she just suddenly...stops for some reason. "
    u "Works for me!"
    u "Now- dig in, Master! Your food’s probably cold by now!"

    scene black
    with dissolve2

    "I hang around the cafe for the next hour until it’s time for Uta to leave."
    "The two of us walk back together and she tells me a little bit more about what life in Nara was like."
    "Apparently, before she came here to take care of her grandfather, she also did all of the cooking and cleaning around the house."
    "She seems a bit worried about how they’re all getting on without her over there, but it doesn’t seem to break her spirit at all."
    "Eventually, we make it back to the dorm and she trots up the stairs, thanking me again for bringing her back."
    "Then, the next thing I know, I’m headed back home to a {i}different{/i} maid."
    "Life sure has gotten interesting lately."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utamaid1 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utamaid5:
...
```

## Code that triggers this event

File: (install folder)\game\UtaEvents.rpy

Code:
```python
...
label utamaid:
    if uta_love >= 0 and day247 == True and utamaid1 == False:
        jump utamaid1
...
```