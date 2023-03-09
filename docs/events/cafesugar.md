# The Flavor of Love
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafesugar&go=Go)



## Event preconditions
✅Rin love greater than or equal to 5



## Next events
* [Main: Drowning](./day30.md)
* [Ayane: Imprinting](./ayanenew1.md)
* [Rin: Skulls](./rinfirstvisit.md)

## Event properties
* ID: cafesugar
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe

## Event code
File: \game\RinEvents.rpy
Code:
```python
...
label cafesugar:
    play music "cafe.mp3"
    scene cafe_day
    with dissolve

    r "Next customer!"

    scene cafe1
    with dissolve

    r "Oh! Morning, Sensei! What'll you be having today?"
    s "Rin, why do you even bother taking my order if you're just going to give me some random concoction instead?"

    scene cafe2
    with dissolve

    r "Hey, it won't be random! I put a lot of thought and love into the drinks I make."
    s "Then I guess I will order one cup of thought and love, please."

    scene cafe4
    with dissolve

    r "Excellent choice, Sensei! I’ve got a really good one for you today, I swear."
    s "They've all been good so I guess I'll just, once again, trust the judgement of the self-proclaimed best barista ever."
    r "Nuh-uh-uh. It's not just self-proclaimed anymore since you wrote it on a card. Now, there is written proof that I am the best barista ever."
    s "I don't think I'm really fit to be making the final decision on that, but I'm glad you're happy."
    s "So, what's so different about today's drink?"

    scene cafe1
    with dissolve

    r "The one today is made with {i}extra{/i} love."
    s "Can I have extra {i}thought{/i} instead? Love is a little too sweet for me."
    r "No. Because love tastes like vanilla and we ordered extra vanilla syrup that I am now responsible for getting rid of."
    s "There's no actual love in this drink at all, is there?"

    scene cafe4
    with dissolve

    r "There is love in {i}everything{/i} I make for you, Sensei."
    s "The barista isn't the one who's supposed to initiate the flirting. I think there's some sort of code against that."
    r "There's a code against a lot of things. But then there are cheat codes that let you ignore them."
    r "My love is but one more bug in the system. A bug that just happens to taste like vanilla."
    s "Well, I'm glad that you've at least confirmed it won't be anything with the potential to kill me."

    scene cafe3
    with dissolve

    r "Kill you? Of course not. If you die, who will I have to experiment on?"
    s "Is your need for a guinea pig all that is keeping me tethered to this world?"

    scene cafe1
    with dissolve

    r "Probably. So it would be in your best interest if you'd just leave all this stuff to me and go take a seat while I pour you a nice cup of love."
    r "With maybe a {i}little{/i} bit of arsenic for added flavor."
    s "..."
    r "..."
    s "Is your manager around? I'd like to inquire about a refund."
    r "Sorry, no returns. Tough luck."

    scene black
    with dissolve

    "I sigh to myself and slide a 500 yen coin across the counter to Rin, who picks it up and shoots it into a register like it's a basketball."
    "Unfortunately, she does not appear to be very good at basketball as she misses completely and it bounces off the counter and right back over to me."
    "But, being the gentleman I am, I give her the money {i}again{/i} and go to find a table as she starts preparing my drink."
    "........."
    "......"
    "..."

    scene sugarredux1
    with dissolve

    r "Alrighty, here you go. I brought some extra pastries and stuff too."
    s "I...see that. Not like I care, but is it really okay for you to be taking this much stuff from work?"
    r "Totes. All this stuff needs to get thrown out anyway since we can't hold stuff for more than two days."
    s "Well, thank you very much for the expired pastries."

    "I take a sip of the drink Rin slid across the counter to me and, just like always, it's...good."
    "A bit on the sugary side due to the amount of {i}love{/i} in it, but still good."

    s "I give it a seven out of ten."

    scene sugarredux2
    with dissolve

    r "Wait, a seven?! That's it?!"
    r "But I put so much love into it!"
    s "I think that's exactly the problem. All I can taste is the love."
    r "But the love is good! The love is great! Love the love, Sensei!"
    s "Do you want to give it a try? Because I'm fine for now, but I have no idea if I'll be able to drink the whole thing."
    r "Is it really that sweet?"
    s "Shouldn't you be testing things before handing them off to me?"
    r "Do scientists test chemicals on themselves before pumping rodents full of them, Sensei? You are my guinea pig for a reason."
    s "As the person responsible for establishing the footing of your new drink platform, you should really value me more."

    scene sugarredux3
    with dissolve

    "Rin looks down at my mug for a few seconds, contemplating whether or not she wants to become a rodent of her own, before sighing to herself and admitting defeat."

    r "Okay, fine. I'll take your word. Some people are really into the super sugary stuff, though."
    r "Like, we get customers all the time who order coffee and then proceed to dump like, 50%% of it out and fill the rest with cream and sugar."
    s "That's not even coffee at that point."

    scene sugarredux4
    with dissolve

    r "I know! Like, why are you even ordering coffee if you don't like the taste of coffee? Do you just like the {i}idea{/i} of coffee? Do you think it will make people like you or something?"
    r "I don't get it. Especially those customers who are like...{i}umm...the place near my house uses extra syrup.{/i}"
    r "Like, whoopdy-fucking-do, Karen. Why not just go there instead if you like them so much?"

    scene sugarredux5
    with dissolve

    r "I'm gonna punch somebody in the face one day, Sensei. I just know it."
    s "Is it really okay to be saying things like that while you're still in uniform?"
    r "Yeah, I clocked out for my break so it's no big deal."
    r "I get what you're saying about the less sugar thing, though. I guess my mind was just tainted by all of the customers with shittier tastebuds than yours."
    r "Anyway, rant over. Let's order pizza."
    s "You sure you're done? Because it looked like you were enjoying yourself just now."
    s "It almost might be good to find out if there is anything that I, as a customer, should be doing to avoid invoking your wrath."

    scene sugarredux6
    with dissolve

    r "You’re fine, Sensei. I like you as a customer."
    s "That’s just because I let you experiment on me."
    r "The experimenting part definitely helps. But even without that, I'd like you."
    s "I think you're breaking the flirting code again, Rin."

    scene sugarredux7
    with dissolve

    r "This isn't flirting! I seriously do."
    r "We get a lot of customers in here and I'm never really {i}excited{/i} to deal with any of them."
    r "But with you, it's like...not like that."
    r "I don't know. It's hard to explain. But I'm going to ask that you keep showing up whenever possible as it definitely makes my mornings a little better."

    scene sugarredux8
    with dissolve

    r "But, now that I've gotten that embarassing piece of information out of the way, I should probably be getting back to work."
    s "Already? But you just clocked out for your break a few minutes ago, didn't you?"

    scene sugarredux6
    with dissolve

    r "Yeah. I get a few breaks because of labor laws and stuff like that, though. What you just experienced was one of the short ones."
    r "But hey, time your visits better and you might be able to catch me on a full-length break one day."
    s "I'll do my best. Sorry your entire mini-break was wasted on me."
    r "It's not a waste at all."
    r "Do you want an actual drink now? Or are you going to force yourself to finish that one for my sake?"
    s "The plan was to tell you I'd finish this so I could look cool, then drop it into a trash can a few blocks away from here."
    s "Now that I know a replacement is possible, I will graciously accept."
    r "Roger that. But, just so you know, it's gonna be another patented Rin Rokuhara creation."
    r "Easy on the love this time."

    scene black
    with dissolve

    "Rin steps away from the table before swiftly spinning around and skipping over to the counter, starting on my new drink as soon as she arrives."
    "As is customary, another wave of customers crashes into the store and prevents the two of us from being able to actually say goodbye to one another-"
    "But I do get my replacement drink."
    "And go figure, but it's much more enjoyable without all of the love."

    $ renpy.end_replay()
    $ cafesugar = True
    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0
    "........."
    "......"
    "..."
    jump saturdayafternoon

label cafe6to9:
    scene cafe1
    with dissolve
    play music "cafe.mp3"

    "Once again, I find myself killing time at the cafe with Rin."
    "She takes my order and promptly discards it before dumping a bunch of random ingredients into a cup and handing it over."
    "Despite my initial skepticism, it actually tastes pretty good and I finish the entire thing."
    "Rin smiles from ear to ear and tells me that she can't wait to rub this in her manager's face."

    scene black
    with dissolve2

    "Things get busy and I wind up having to leave before the two of us can start up a new conversation, but at least we managed to get a little bit closer."

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe10:
...
```

## Code that triggers this event
File: \game\RinEvents.rpy
Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
...
```