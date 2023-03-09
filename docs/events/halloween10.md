# Samhain
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween10&go=Go)


Part of event chain [At Least It's Not Christmas](./halloween9.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloween10
* Group: Main
* Triggered by label: halloween9

## Event code
File: \game\script.rpy
Code:
```python
...
label halloween10:
    if _in_replay:
        play music "letsfuckingo.mp3"

    scene samhain1
    with dissolve

    mo "Oh?"
    mo "Does my eye deceive me? Or has the Herald of the Adolescents graced us with his presence on this most-deadly of nights?"
    t "Hello."
    s "Hey, you two. "
    s "For the record, I don’t think tonight is any more deadly than the night before it."
    s "Or the night before that, for that matter. I think it’s just an excuse for people to dress up."

    scene samhain2
    with dissolve

    mo "Ohoho~ Is that so?"
    mo "Then I take it you’ve not heard the origin of this wondrous holiday after all?"
    s "Wasn’t the idea to like, celebrate the dead or something?"

    scene samhain3
    with dissolve

    mo "No, Sir. It was not."
    mo "Halloween can be traced back nearly 2,000 years ago to the Celtic festival of Samhain, which was meant to not only ward off ghosts but celebrate the end of Summer and usher in the coming season."
    mo "But given that you grew up in the land of the rising sun and not the land of warm beer and potatoes, I suppose I can’t hold it against you for not knowing that."
    t "Yeah, idiot."
    s "…"
    s "Did you know about Sa-whatever, Tsuneyo?"

    scene samhain4
    with dissolve

    t "Ah-"

    scene samhain5
    with dissolve

    t "...bviously."
    s "Don’t turn your sheltered, surprised gasps into retorts. Answer the question."

    scene samhain6
    with dissolve

    mo "You can’t blame her for not knowing these things either, Sir. Especially when she’s carrying her trusted blade, {i}Gallows...edge.{/i}"
    s "You just came up with that now, didn’t you?"
    mo "Absolutely not. Tell him, Kendo Princess."

    scene samhain7
    with dissolve

    t "I will strike you down with the Hallowed Ledge."
    mo "Gallows Edge."
    t "Gallows Edge."
    s "Right."
    s "Are those swords even real?"
    t "That is a secret, bro."
    t "If you are lucky, you will never have to find out."
    s "...Okay then."
    s "So were you two just going to stand over here being weird the entire night?"
    mo "No, Sir. We were actually looking to conduct a top-secret raid on the Amamiya wine cellar."
    mo "Or beer cooler."
    mo "Anywhere that the elixirs of joy are kept."
    s "But Tsuneyo can’t handle alcohol."
    t "It’s true. I fell asleep immediately after one sip during vacation."
    t "The small soccer girl took advantage of me after that, if the tales I’ve been told are true."
    s "I can’t imagine you’d be able to handle alcohol either given that you’re like...five feet tall, Molly."

    scene samhain8
    with dissolve

    mo "Is this a test, Sir? "
    mo "I’ll have you know that even though I’m just a [young]lass, I’m still from the Emerald Isle."
    mo "Alcohol courses through my veins and beckons me to the promised land."
    s "And the promised land in this case is wherever Ayane’s dad keeps the beer?"
    mo "Or wine, yes."
    mo "What would you say to accompanying the two of us lovely [young]ladies somewhere safe so we can drink in private?"
    s "Does it really need to be in private? I doubt Ayane would care and her butler is stuck in his room sick or something."

    scene samhain9
    with dissolve

    mo "I-It’s no fun if we can do it where everyone can see us!"

    if bonus == True:
        mo "This is my first [high_school] party and I wanna feel like the cool kid who gets drunk and loses her vir...PHONE in a secret room that only a few people know about!"
    else:
        mo "(Incomprehensible Gaelic)"

    s "What were you about to say, Molly?"

    scene samhain10
    with dissolve

    mo "N-Nothing!"
    mo "Did...Did you also know that during Samhain, Druids would create huge bonfires where they could sacrifice animals in the name of the Celtic deities?!"

    if bonus == True:
        t "Why would you want to lose your phone? "
        t "Do you have good insurance?"
        s "She wasn’t actually talking about her phone, Tsuneyo. She was talking about her virginity."
        mo "I was not!"
    else:
        t "I understand Gaelic now. I learned it after the beach."
        s "You {i}learned{/i} something without my help??? Why?!"
        t "I believe she just said something about losing Virginia."

    scene samhain11
    with dissolve

    t "Isn’t that a state in the US?"
    s "Yes."
    t "Then how would she-"

    scene samhain12
    with dissolve

    mo "Do not worry, Tsuneyo. No states will be lost tonight as I am both mentally and physically unprepared for it."
    mo "But the mission remains the same either way."
    mo "When surrounded by social [teens], we must {i}become{/i} social [teens]!"
    mo "We must take our shut-in mentalities and cast them aside! Toss them into the pyres along with our animal sacrifices!"
    t "If I had known there were going to be sacrifices, I would have stopped at a convenience store on the way here to obtain some."
    s "You can’t buy sacrifices from convenience stores, Tsuneyo."
    t "Well that’s not convenient at all."

    scene samhain13
    with dissolve

    mo "How well do you know your way around this place, Sir? Ayane talks about you constantly so I assume you’ve been here before."
    s "Not even once. I’ve only been in this room."
    mo "Then we can explore together! Think of it as a low-level quest."
    mo "As a reward, your social-link with both the Kendo Princess and myself is sure to go up."

    scene samhain14
    with dissolve

    mo "And we all know what happens when you max out a social-link, don’t we?"
    t "Sausage-link, Emerald Guardian. Not social-link. "
    t "You’re Irish. You should know this."

    scene samhain15
    with dissolve

    mo "What? No. That’s...a completely different thing."

    "Molly gets wrapped up in a small tangent about some video game that Tsuneyo and I have clearly never heard about."
    "Our confusion causes Molly’s excitement to fade rather quickly as she changes gears and goes back to focusing on her “mission.”"

    scene samhain16
    with dissolve

    mo "Okay, I’m gonna stop beating around the bush and just ask if you want to come hang out with us for a little while, Sir."
    mo "I have no idea what to do at parties so I’d be more comfortable with you and Tsuneyo by my side."
    t "I also don’t know what to do at parties, but I’m quickly learning that I don’t know what to do anywhere."

    if bonus == True:
        s "How does alcohol tie into this, though? I’m a responsible adult and shouldn’t be letting you two drink unsupervised."
        mo "But you are supervising us right now, aren’t you?"
        s "Good point. Let’s do it."
    else:
        s "How does alcohol tie into this, though? If you don't wind up rationing your consumption of alcohol, you will end up like Sana's mom."
        mo "But we {i}are{/i} rationing our consumption, Sir."
        s "Oh. Then I respect your decision to drink and will accompany you to the courtyard."

    scene samhain17
    with dissolve

    mo "Woo! Phase one accomplished!"

    scene black
    with dissolve
    stop music fadeout 10.0

    "Obviously, I was never going to get between these two and what is obviously a bad idea, but now I’m really locked into it."
    "The three of us manage to slip out of the room unnoticed (At least for now) and make our way into an unattended, commercial-sized kitchen."
    "Molly and I both grab a handful of cans."
    "Tsuneyo grabs one and looks at it for a disturbingly long amount of time, almost like she’s trying to tell it something with her mind."
    "That or she’s just remembering the effects of beer on her body from the beach and is questioning her decision to consume yet another one."

    play sound "slidedoor.mp3"

    "Molly pulls open a sliding door and leads us into a backyard-slash-koi pond type area."
    "A cool breeze blows past us and reminds me, yet again, that Summer is coming to an end."
    "It really is Samhain."
    "We’re having a party to usher in the end of the Summer."
    "And what comes next is something even I’m not sure of."
    "As I sit down on the stone steps with Molly and Tsuneyo, I realize that things are going to change again soon."
    "But what does that mean for them?"

    scene samhain18
    with dissolve
    play music "samhain.mp3"

    mo "To the end of Summer! "
    mo "And the ancient Celts!"
    mo "Though there is no spare wood to be found, let our hearts become the bonfire and let the ghosts of the dead be banished once more!"
    mo "Gods! However many of you are up there! Hear our pleas!"
    mo "Accept our sacrifices and bless us with a wonderful end of the[school] year!"

    scene samhain19
    with dissolve

    mo "And thank {i}you{/i} for blessing us with a wonderful middle of the[school] year, Sir."
    t "I would like to thank you as well."
    t "I have not known you long, but you have given me the confidence I need to continue failing at everything I try."
    s "It’s fine. You’ll succeed in something other than noodles, eventually."
    t "At this point, I find that hard to believe."

    "It hadn’t occurred to me until now that I...didn’t even {i}know{/i} these two prior to the world resetting."
    "That doesn’t mean they’re going to be gone again when I wake up the second time, does it?"
    "I know Maya’s talked about how memories don’t typically change, but-"
    "What sort of reason would there be for these two to just show up halfway through a[school] year on the second loop but not the first one?"

    t "Is something wrong?"

    scene samhain20
    with dissolve

    mo "Yeah, you look really pale all of a sudden."
    mo "Could it be that {i}you{/i} are the one who can’t handle alcohol, Sir?"
    s "Nah. I’m just thinking about what a strange...year it’s been."

    scene samhain21
    with dissolve

    mo "Strange isn’t always a bad thing, though."
    mo "I mean, look at me."
    mo "I’m a weirdo who talks too much and makes everybody uncomfortable all the time, but we’re good friends now, aren’t we?"

    scene samhain22
    with dissolve

    mo "You too, Kendo Princess."
    mo "I feel like all three of us have only known each other for a little while but I’d cry and scream like a mandrake if I lost either of you."
    mo "Which is why I’ve made a pledge to myself to stay close to both of you even if we all get split up next year."
    t "Split up?"
    t "Why would anyone split us up?"
    t "I didn’t even know the[school] year was ending until two minutes ago."
    s "What, did you just think it kept going forever or something?"

    scene samhain23
    with dissolve

    t "Yes, actually."
    s "Nope. In a little less than two months, everything is going to end. "
    s "You’re going to get a new teacher and new classmates."
    s "And you’re going to start over from the beginning."

    "I play my part and tell Tsuneyo how things are {i}supposed{/i} to be when, frankly, it’s a lot more complicated than that."
    "For all I know, I very well {i}could{/i} be her teacher again once everything starts over."
    "I just don’t know."
    "There are millions, if not billions of things I don’t know, which is exactly why I’ve always felt like I should prevent myself from getting attached to...well, anything."
    "But on nights like this, where I’m having real conversations with cute girls illuminated by the glow of moonlight and the shadows of well-trimmed hedges dancing across their faces in the wind-"
    "Well-"
    "It gets pretty hard."

    scene samhain24
    with dissolve2

    t "…"
    t "What?..."

    "Tsuneyo’s eyes widen and fill with tears."
    "I guess even she wouldn’t be able to handle news like that out of absolutely nowhere."
    "It makes me wonder how she’ll look when her father inevitably passes."
    "This is just the start of bad things for her."
    "Welcome to the outside world."
    "Please enjoy your stay."

    t "No."
    s "Yes."
    t "No."
    s "Hey, you could always get lucky and wind up in my class again next year."

    "Or, even better yet, we can just do this entire year over."
    "That sounds much more fun, doesn’t it?"

    t "I will leave[school] if I’m not in your class again."
    s "Why? You don’t even like me that much. You’ve said it yourself."
    t "I don’t dislike you either."

    scene samhain25
    with dissolve

    mo "Looks like it isn’t just me you’ve made a lasting impression on, Sir."
    mo "Here’s hoping I get lucky, too."
    mo "But I guess even if I don’t, I could always just make a lot of noise and annoy everyone until I get kicked out of some other teacher's class."

    scene samhain26
    with dissolve

    t "Is that an option?"
    mo "Wanna find out together if we’re in the same one?"
    t "I do. "
    t "Miss Watabe was a nice person but she felt less human than Sensei does."
    s "I’m sure she’s also a human, Tsuneyo."

    "If anything, I’m probably {i}less{/i} human than Miss Watabe."
    "I’m just a disembodied soul who wandered into the body of a man who didn’t know how great he had it."
    "Or maybe he did."
    "Who knows?"

    scene samhain27
    with dissolve2

    if bonus == True:
        mo "High school really sucks..."
    else:
        mo "College really sucks..."

    mo "This isn’t like an anime at all."
    mo "Everything is ending before it even had a chance to start."
    s "..."

    "Ah, the sweetest lesson of all. "
    "Time."
    "She’s an evil bitch, isn’t she?"
    "High school ends faster than anyone realizes, which is crazy given how long it feels like we’re in there for."
    "But, sooner or later, we all make it out of the labyrinth of [teenage]life and find ourselves trying to feel [young]again in any way we possibly can."

    if bonus == True:
        "It’s probably one of the reasons I let girls this age continuously cry around me."
    else:
        "It’s probably one of the reasons I let girls continuously cry around me."

    "Being needed feels nice."
    "Being wanted feels nice."
    "The only issue is that almost everything else in the world feels horrible."
    "Oh, how wonderful it would be to always feel loved."

    mo "Sir, I believe this is the part where you give us some profound advice that sticks in our heads for the rest of our lives."
    mo "Something we can pass on to our children."
    t "I do not want children, but I will accept your advice and share it with my father."
    t "I’m sure he would be happy to hear something nice for a change."

    "Huh..."
    "Advice."
    "What am I supposed to say during times like this?"
    "Should I just make something up?"
    "Should I quote one of the motivational posters they have hanging in the cafeteria?"
    "Or should I speak from whatever is left of my heart?"

    s "How about this-"
    s "Life is a game."

    scene samhain28
    with dissolve

    mo "Gah. It’s a platformer, isn’t it?"
    mo "I was never good at those."
    mo "It would definitely explain why I suck at fitting in."
    s "It’s not a...whatever you just said. But it’s a game nonetheless."
    s "And all there is to it is to just...try and get through without running out of lives."
    mo "Don’t we only get one life, though?"
    s "Not at all."
    s "You get tons of lives."
    s "And each time something bad happens, one gets taken away."
    s "It could be something like losing a mother."

    scene samhain29
    with dissolve2

    mo "…"
    s "Or a father."

    scene samhain30
    with dissolve2

    t "…"
    s "But all of those horrible things by themselves aren’t enough to kill you."
    s "They’ll just make it harder to keep going."
    s "As long as you have some lives saved up, though, you’ve got a chance."

    scene samhain31
    with dissolve

    t "But then..."
    t "What happens at the end of the game? How do we win?"
    mo "Yeah, what are we supposed to do? What’s the point of it all?"
    s "The point?"

    scene nightsky
    with dissolve2

    s "…"
    mo "…"
    t "…"
    s "Being happy, I guess?"
    mo "Life is..."
    t "A game about...being happy?"
    s "It sounds kind of stupid when you say it like that, doesn’t it?"
    mo "N-No! Not at all!"
    mo "That was like...way better advice than I was expecting you to give us!"
    t "I thought you were going to just tell us to figure it out ourselves."
    s "I mean, I kind of did. Didn’t I?"
    mt "No..."

    "The two of them speak in perfect unison."
    "I’ve found it quite difficult to look at them with tears in their eyes, so I’m focusing on the night sky now."
    "We’ve been gone for a while."
    "People are probably wondering where we-"

    scene samhain32
    with dissolve2

    "The feeling of four unfamiliar arms wrapping around me at the same time breaks my train of thought."
    "It’s strange seeing these two girls, who I’ve only known for a couple months, become so torn up at the thought of a new[school] year."
    "At the thought of losing not only each other, but me."
    "It doesn’t make much sense, to be honest."
    "I mean-"
    "What have I given them? "
    "One life lesson and a few free A’s on tests they probably would have passed in the first place."
    "This reaction is unwarranted."
    "But-"
    "It feels nice."
    "I’d like to feel this again sometime."
    "…"
    "I really hope they’re still around when winter comes."

    t "Don’t...go..."
    s "I’m not going anywhere..."
    mo "Sensei..."
    s "Wow, you’re even calling me Sensei now? You must really be upset."
    s "This is the first time you've hugged me, too."
    mo "I get...*sniff*...really clingy when I cry..."
    mo "And when I don't..."
    mo "I'm actually just clingy all the time...I'm sorry..."
    t "I don’t normally cry...so this is new for me..."
    s "Well you two are free to stay like this for as long as you like."
    mo "Even if it’s...*sniff*...forever?"
    t "I have ten seconds left until I start feeling very embarrassed."
    s "Then Tsuneyo can stop after ten seconds and Molly, you can stop after thirty."

    scene samhain33
    with dissolve

    mo "That’s not even close to forever!"

    scene black
    with dissolve2


    "Tsuneyo leaves first, wiping tears from her eyes as she goes."
    "Molly, I understand. But I didn’t expect to see a reaction like that from Tsuneyo for at least-"
    "Actually, I don’t even know how long I thought that would take."
    "Molly and I walk back into the party together and are promptly questioned by Ami about where we’ve been."
    "Ami ultimately lays off when she sees that Molly is still a little shaken up and, after an awkward and abrupt ending to that conversation-"

    stop music fadeout 8.0

    "I bid the two of them goodbye and head off to find Makoto."
    "I wonder what it is she wanted to talk about?"

    $ renpy.end_replay()
    $ halloween10 = True
    $ tsuneyo_love += 3
    $ molly_love += 3

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

label halloween11:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```