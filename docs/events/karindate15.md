# Dying Alone With Ten Cats (Karin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Karin love greater than or equal to 15

* Event [Forty Degrees Below Zero](./day264.md) (Main) is completed)

* karinlied equal to True (unknown variable)

* karinnumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: karindate15
* Group: Karin
* Triggered by label: callkarinafternoon
* Triggered by branch label: callkarinafternoon
* Triggered by path: callkarinafternoon->karindate15

## Official wiki page

[Dying Alone With Ten Cats](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karindate15&go=Go) for more details.

## Event code

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label karindate15:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."
    "It’s that weird part of the afternoon between lunch and dinner where I want to eat, but having four meals in one day is kind of frowned upon."
    "But I’m sure if I told Karin that, she wouldn’t mind."
    "Maybe the two of us could go out for lunch or something?"
    "That sounds like a thing she’d enjoy."
    "Sure, she’ll probably drop her phone when I ask, but I think she’d enjoy it when all is said and done."

    play sound "phonebeep.wav"
    play music "acoustic.mp3" fadein 15.0

    ka "Hello! I mean...hi!"
    ka "Hey!"
    s "All three of those mean the exact same thing, Karin. Any of them will work in the future."
    ka "Okay but “hello” is too formal and “hi” is too informal and if I accidentally added an extra y to “hey” you would have thought I was too clingy."
    s "Are these things that girls actually think of?"
    ka "Greetings! H...How are you today?!"
    s "Hungry."
    ka "Do you..."
    ka "Do you want me to make you lunch?"
    ka "Or...dinner, I guess?"
    ka "It's that weird part of the day between the two, so I don’t really know what to call it."
    s "I was actually wondering if you’d maybe want to go out to a diner or something?"
    ka "Ah! D-Diner?!"

    "A loud bang rings out through my cell-phone, signaling that Karin has, just as I expected, dropped the phone upon being asked out."
    "She’s so pure."

    ka "S-Sorry! My hand slipped! "
    ka "I had a lot of coffee today and...um...hands."
    s "Right..."
    s "So, what do you say?"
    ka "I’d love to!"
    s "Great, then-"
    ka "But..."
    s "Uh-oh."
    ka "My parents are expecting a package and they asked me if I could sign for it when it gets here."
    s "Can’t Kirin do it instead? "
    ka "I..don’t know where she is."
    ka "But, umm..."
    ka "Maybe if..."
    ka "If you wanted to...come over?"
    ka "I...I wasn’t really joking when I offered to make you lunch...or dinner."
    ka "Which one did we decide this was again?"
    s "I don’t think we did. "
    s "But if that’s really okay, I’ll start heading over now."
    ka "Okay! Yeah! I’ll...um..."
    ka "I’m gonna take a shower and get dressed then."
    ka "You...you know where I live, right?"
    s "Yeah. I’ve met Kirin there before."
    ka "Right...right. Yeah. Okay!"
    ka "Umm...just...call me when you get here, then!"
    ka "I’ll see you soon!"

    play sound "phonebeep.wav"

    "The two of us hang up and I begin to make my way over to the Kanda residence."
    "It will be the first time I’m hanging out with Karin alone in the apartment, and I fully expect it to be disastrous in the cutest possible way."
    "………"
    "……"
    "…"

    scene karinsushi1
    with dissolve

    "Karin lets me in after I text her about my arrival. And, before I know it, we’re awkwardly standing in the living room, staring at each other."

    ka "So...umm...did you find the place okay?"
    s "Yup. Didn’t I just tell you earlier that I remembered where you live?"
    ka "Y-Yeah...but my mom always talks about how boys can be forgetful, so...I thought maybe you’d...you know...forget."
    ka "She could just be saying all of that to justify how my dad forgot their anniversary this year, though."
    s "Well, it’s true that my memory is probably one of the worst you’ll ever find, but it’s for reasons entirely unrelated to anniversaries and whatnot."

    scene karinsushi2
    with dissolve

    ka "What’s...what’s wrong with your memory? Is it okay for me to ask that?"
    s "Let’s just say a lot of it disappeared. "
    s "And I guess the rest of it could technically disappear again...but only at several really specific moments."
    s "Like when seasons change or something."
    s "I don’t really understand how it works, to tell you the truth."
    ka "Is that...some sort of...disease?"
    s "No, it’s more like-"

    scene karinsushi3
    with dissolve

    ka "I...I’ll take care of you!"
    ka "You don’t need to worry, Sensei!"
    ka "I’ll wait by your bedside every morning and show you flashcards to remind you of who I am! And who everyone else is!"
    ka "You don’t have to worry! Everything will be okay!"
    s "I appreciate the offer, but I’m pretty sure I’ll be fine."
    s "Please continue to spend your mornings working out or whatever else it is that you do."

    scene karinsushi4
    with dissolve

    ka "I...watch the news sometimes?"
    s "While you’re working out, I’m guessing?"
    ka "...Maybe."
    s "Well, in the event that my memory {i}does{/i} randomly disappear again, I’d love for you to come remind me of who I am."
    s "You’ll probably have to fight off a small girl with red hair who will be attempting to do the same exact thing, though."

    scene karinsushi5
    with dissolve

    ka "But I don’t want to fight Ami...she’s so nice."
    ka "Maybe we can just take turns?"
    ka "Or I can just...cook for you while she reads you the flashcards."
    ka "I still want to make them, though. I have this weird thing where I just really like flashcards for some reason."
    ka "Do you want to talk more about flashcards? That sounds fun, right?"
    s "It sounds...like a thing."
    s "I’m more interested in the part about you cooking."

    scene karinsushi6
    with dissolve

    ka "Oh! Right! That’s why you’re here!"
    ka "I...I..."
    ka "Look! Table!"

    scene karinsushi7
    with dissolve

    "I “Look. Table.” to find that Karin has laid out two surprisingly large sushi platters."
    "And when I say “surprisingly large” I mean both the platters and the actual pieces of sushi are gigantic."
    "I was all about the idea of a fourth meal today, but...this might be a little too much."

    ka "So, umm...I’m sorry for not asking you what you wanted."
    ka "If you hate it, we can just order from somewhere."
    ka "Actually, let’s just do that right now. This clearly isn’t good enough for you."
    s "I’m sure it’s fine, Karin."
    ka "Oh! And...umm...I didn’t know what you would want to drink, so I just got you...one of everything we had."
    s "Is that canned coffee?"
    ka "Yes!"
    s "Do you normally drink canned coffee with sushi?"
    ka "No!"
    s "..."
    ka "..."
    ka "Oh God...I’ve ruined everything."
    ka "I’m so sorry, Sensei. I’ll just get my phone and-"

    scene karinsushi8
    with dissolve

    s "It's fine, Karin. There’s no reason to order takeout when you’ve already done this much."
    s "I’m not drinking the canned coffee, though."
    s "I’m no gourmet, but that doesn’t sound like it would be a good flavor combination."
    ka "Are you sure you don’t want a pizza or something? "
    s "I want to eat what you made."
    ka "…"
    s "…"

    scene karinsushi9
    with dissolve

    ka "Are you sure?"
    s "Of course."
    ka "But what if I’m not good enough?"

    scene karinsushi10
    with dissolve

    ka "Or...the food! I meant the food! What if the food isn’t good enough?"
    ka "You’ll never want to come over again and I’ll be too embarrassed to look at you during practice!"
    ka "Then I’ll have to quit the soccer team and start pursuing another sport full time and it will destroy my future and I’ll lose any scholarship I could have gotten and..."
    ka "And before I know it I’ll wind up severely injuring myself and never being able to play anything ever again!"
    s "I’m not sure how you got to the last part, but I think it might be time for us to sit down and eat."
    ka "Okay! But please...{i}please{/i} stop me if I start rambling again! I mean it!"
    s "Sure..."

    scene black
    with dissolve

    "Karin and I move to our respective spots at the table."
    "I take my place behind a plethora of beverages that she was apparently torn between-"
    "And she takes her place behind..."

    s "…"
    ka "Is...is something wrong?"

    scene karinsushi11
    with dissolve

    s "Is that a glass of wine?"
    ka "Wine?..."

    scene karinsushi12
    with dissolve

    ka "…"
    ka "That’s a glass of wine."
    ka "…"

    if bonus == True:
        ka "I’m not old enough to drink this."
    else:
        ka "I do not want this."

    s "You're not secretly an alcoholic, are you?"

    scene karinsushi13
    with dissolve

    ka "What?! No! I must have poured it by mistake when I was pouring yours!"
    ka "I’m only allowed to drink on special occasions!"
    s "Is today not a special occasion? "
    ka "It is! But...it’s a different kind of special!"
    ka "It has to be a holiday!"
    s "I kind of want to see you drink now."

    scene karinsushi14
    with dissolve

    ka "Wh...why would you want to see that?"
    s "Just curious about how much it changes your personality."
    s "Who knows? Maybe you’re a lot more relaxed with alcohol in your system?"
    ka "Please don’t say things that will lead to me having a drinking problem..."
    ka "If I find out wine is the key to holding a conversation with you, I’ll be sneaking bottles into[school] before I know it."
    s "This conversation never happened."
    ka "But...um..."
    ka "I...I wouldn’t mind if you...maybe came over for a holiday sometime...if you really wanted to see."
    ka "I can’t drink a lot but...it would make me happy having you around for something like that..."
    s "I’m sure it would. I can’t imagine your parents would feel the same way, though."

    scene karinsushi15
    with dissolve

    ka "Oh."
    ka "Right."
    ka "I have parents."
    s "Parents who I imagine wouldn’t be very fond of their daughter dating a staff member at the[school]."
    ka "Yeah...they-"

    scene karinsushi16
    with dissolve

    ka "Wait..."
    ka "Are..."
    ka "Are you saying you would...date me?"
    s "…"

    "Shit."
    "I guess I {i}did{/i} kind of say that."
    "It’s definitely not what I meant, though."
    "I mean, a relationship with Karin does sound like it would be...surprisingly normal-"
    "But a relationship in general isn’t something that I want."
    "Or at least it’s not something I think I want."
    "I don’t know."
    "Maybe in a different life."
    "As far as this one goes, though-"

    s "I’m sorry. I didn’t mean it like that."

    scene karinsushi17
    with dissolve

    ka "Ah, no! You don’t have to apologize! I wasn’t trying to put you on the spot!"
    ka "It just sounded like...you might...l-like me or something...that’s all..."
    ka "I mean, obviously you wouldn’t like someone like me. I don’t even know what kind of drinks you prefer with sushi."
    s "That’s actually the first thing I quiz my prospective girlfriends on."

    scene karinsushi18
    with dissolve

    ka "Hmm..."
    s "…"
    s "What’s that face for?"
    ka "I’m waiting to see which one you drink first in case this ever happens again."
    ka "Also, what other types of questions are on this quiz?"
    s "Look at you getting all serious in the face of romance."

    scene karinsushi19
    with dissolve

    ka "Oh my God! I did it! I flirted with a boy!"
    s "I'm not sure if I'd count something that small as flirting, but at least it was smooth."
    s "At least a lot smoother than openly celebrating your success."

    scene karinsushi20
    with dissolve

    ka "I’m a boy expert now."
    s "You haven’t been sneaking sips of that wine while I’m not looking, have you?"

    scene karinsushi21
    with dissolve

    ka "Of course not..."
    ka "But I’m...finally starting to calm down, I think."
    ka "My heart’s still beating out of my chest, but...I think that “dating” thing gave me a temporary boost to my self-esteem."
    s "Even though I immediately said I didn’t mean anything by it?"
    ka "Weird, right? Maybe that part just hasn’t settled in yet?"
    ka "Or maybe I’m just finally-"

    scene karinsushi22
    with dissolve

    ka "Wait. No. It’s here."
    ka "I’m going to die alone with ten cats."
    s "No one is truly alone with ten cats."

    scene karinsushi23
    with dissolve

    ka "Do you like cats, Sensei?!"
    s "Not really. "

    scene karinsushi24
    with dissolve

    ka "Oh."
    ka "But...their ears."
    ka "And their little noses..."
    s "I just meant that all human beings are inherently alone as a matter of principle, so the only way to properly judge loneliness is by sheer tangibility."
    s "If there are ten other living creatures in the same room as you, whether they be cats or humans, you are not {i}technically{/i} alone. "
    s "But you {i}are{/i} still alone. "
    s "Get it?"
    ka "…"

    scene karinsushi25
    with dissolve

    ka "But...their ears..."
    s "…"
    ka "And their little noses..."
    s "Let’s just eat now..."

    scene black
    with dissolve2

    "I decide to stop being depressing for a moment and enjoy the food Karin prepared for us."
    "I’m surprised she was able to make something as classy as a sushi platter with virtually no mistakes whatsoever."
    "I’m not even sure if Ami can make sushi at this level, and she’s pretty much a personal chef at this point."
    "I guess if anyone was going to be able to, though, it was Karin."
    "Despite her tomboyish hobbies and a physique that would make even professional athletes jealous, she’s a pure, wholesome girl at heart."
    "A wholesome girl who wants to make the people around her happy, and who wants to find happiness of her own without damaging anyone else in the process."
    "I wish her luck in that regard."
    "Personally, I don’t think something like that is possible."
    "But I’d be happy to be proven wrong."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate15 = True
    stop music fadeout 7.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "………"
    "……"
    "…"
    "{i}Thirty minutes later...I leave Karin’s house and decide to get on with my day...{/i}"

    jump saturdaynight

label karinsoccer15:
...
```

## Code that triggers this event

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label callkarinafternoon:
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
    if karin_love >= 5 and day103 == True and karindate5 == False:
        jump karindate5
    if karin_love >= 10 and mollycafe1 == True and karindate10 == False:
        jump karindate10
    if karin_love >= 15 and day264 == True and karinlied == True and karindate15 == False:
        jump karindate15
...
```