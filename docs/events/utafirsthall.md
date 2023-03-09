# Far From Home
Uta event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utafirsthall&go=Go)



## Event preconditions
✅Event "[Main: Caterpillar](./day247.md)" is completed (event=day247)



## Next events
None

## Event properties
* ID: utafirsthall
* Group: Uta
* Triggered by label: utahall
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label utafirsthall:
    scene utahall1
    with dissolve

    u "Hey! What are you up to, Sensei?"
    u "Come to hang out with one of your six million girlfriends?"
    s "All of them at once, actually. And what better place to do that than the dorms?"
    u "Hmmm...School, if you can be sneaky enough."
    u "That way, you could even rope some of the other classes into it. You can thank me later for the brilliant idea."
    s "I might just have to do that."
    s "What are {i}you{/i} up to, Uta?"
    u "Me? Was just stopping for a quick drink of water on my way out to do some exploring."
    s "Right. You’re still getting acquainted with the area, aren’t you?"
    u "Slowly but surely. It’s not as confusing as the area I was living in before this."
    u "Over there, since the[school] was {i}in{/i} the actual city part, we didn’t get those cool stretches of nothingness like you have over here."
    u "Reminds me a lot of Nara but with less wildlife and more...tamed life."
    s "Is that a good or bad thing? I don’t think I’ve really asked you how you feel about this place other than the class itself."

    scene utahall2
    with dissolve

    u "It’s not...bad?"
    u "Like yeah the class is awesome and I’m glad to finally have a teacher who doesn’t creep me out-"
    s "Wait, what? Your other teachers creeped you out but I somehow don’t?"

    scene utahall1
    with dissolve

    if bonus == True:
        u "Oh totally. The fact that you’re so up front about how interested you are in [younger_girls] is actually weirdly comforting in a way."
        u "It’s like, “Oh, nothing this guy does will surprise me.”"
        u "My other teachers have all been like, the secret kind of perverts who just stare at everybody from behind their desks and daydream instead of actually acting on anything."
        s "I’m pretty sure that’s just how people are supposed to act, especially in public settings."
    else:
        u "Oh, totally. They kept trying to steal my stuff when I wasn't looking."
        s "You should report that to the principal."

    scene utahall2
    with dissolve

    u "Probably. You’ve been fun so far, though. "
    u "As far as Kumon-mi itself goes, it’s not what I’d call my ideal place to live...but it’s not like I’m dying to get out just yet."
    s "What would your ideal place to live be, then?"

    scene utahall3
    with dissolve

    u "Well, even though it can get kind of boring over there at times, I think I {i}do{/i} prefer the country overall."
    u "Places like this kinda lose their luster once you realize you can just do anything you want whenever you want."
    u "It turns stuff I always viewed as super-special outings into another way of life. "

    scene utahall4
    with dissolve

    u "But, it’s definitely easier finding work over here. Not a lot of maid cafes where I’m from."
    u "And also not a lot of teachers willing to just let us girls teach ourselves. So, thanks!"

    "Interesting."
    "I don’t think I’d particularly enjoy living in the country."
    "But it’s not like Uta and I need to agree on everything in order to become better acquainted."
    "I understand why she’d want to be somewhere closer to what she’s grown used to over the course of her life."
    "Thankfully, I have the advantage (Or disadvantage, depending on how you look at it) of not remembering anything about my childhood-"
    "So somewhere like Kumon-mi is perfect for me."

    s "No need to thank me for being bad at my job. I do that willingly."

    scene utahall5
    with dissolve

    u "Hey! Don’t call yourself bad!"
    u "I’m tryin’ to be serious here, Sensei. I think you’re great."
    u "Even Io has started feeling at home here and I don’t think she even looks at the bathhouse that way."

    scene utahall1
    with dissolve

    u "Plus, I think it’s cool that you’re allowed to come to the dorms and talk to us. "
    u "I feel more inclined to learn if I’m closer to whoever’s teaching me."
    s "Is that code for “Let’s get even closer, Sensei?”"

    scene utahall6
    with dissolve

    if bonus == True:
        u "Ohohoh~ Turnin’ the moves on even though I’m wearing three layers of clothes and a hat that smiles back?"
        s "I wouldn’t have it any other way."

        scene utahall7
        with dissolve

        u "Thank you, Sensei. But as much as I appreciate your advances and unearthly desire to get it on with a girl under five-feet tall, I must once again decline."
        u "It would take far too long to remove all of these clothes and I do not want to get dressed again before embarking on my late-night journey to wherever the cold wind takes me."
        s "I can remove them for you. I don’t mind at all."
        u "But then what would poor Io do? She’s still in the room."
        s "…"
        s "Watch?"

        scene utahall8
        with dissolve

        u "You want to get freaky with me while my friend watches?!"
        s "Kind of, yeah."
        u "But what if we both make really weird faces in the heat of the moment and she laughs at us?"
        u "Would you be able to keep it up if that happened?"
        s "I think I’d be a little too distracted by...what else is going on."
        u "If someone ever made fun of me during a time like that, I’d stop like, immediately."
        u "And then it would be really awkward because, like, I’d have to put all of these layers back on while they just laugh."
        u "And so I will never have sex for the rest of forever. It's simply not safe."
        s "…"
        s "You’re going to run out of excuses one day. And when that day comes-"

        scene utahall9
        with dissolve

        u "Yes. When that day comes, I am ready to join the ever-growing list of names in my soon-to-be best selling novel, Sensei’s Secret Sex Journal."
        s "Finally, a book I actually want to read."

        scene utahall8
        with dissolve

        u "Are you really so self-absorbed that you’d read an entire book about yourself? Sensei, you’re better than this."
        s "I’m really not, Uta. You just don’t realize it yet."

        scene utahall9
        with dissolve

        u "Ah. Well then I apologize."
    else:
        u "Ohohoh~ It's starting to sound like {i}somebody{/i} wants to hug."
        s "That person is me. But I think it still might be too soon."

    u "I shall pay closer attention to how much I am supposed to dislike you and will ignore the wonderful chemistry we have begun to form with each other."
    s "I am sorry things had to end like this."
    u "I understand, Sensei. Things {i}needed{/i} to happen this way before they became too serious and one of us wound up with a broken heart."
    u "Probably me because I get attached too easily and would never leave you since I’m so nice."
    s "I’ve changed my mind. I love you."

    scene utahall10
    with dissolve

    u "I remember...when I loved you..."
    u "It feels so long ago now..."
    u "Goodbye...Sensei..."

    scene utahall11
    with dissolve

    "Uta smiles and walks right past me, closing her eyes and sighing to herself as she forever disappears from my life."
    "The days we shared with one another were brief, but they will echo in the back of my mind for as long as I live."

    scene black
    with dissolve

    "I will never forget you, Uta Ushibori."
    "May you find happiness wherever the cold wind takes you."

    $ renpy.end_replay()
    $ utafirsthall = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utahall:
    if utafirsthall == False:
        jump utafirsthall
    else:
        jump utahallgen

label utahallgen:
    if chapthreeactive == True:
        scene utasummer2hallgen
        with dissolve
    else:
        scene utahall1
        with dissolve

    u "Heya! I'm guessing you're here to see me, Sensei?"
    u "Just can't stay away, can ya?"

    "I spend the night hanging out with Uta in the hall."
    "We take a walk around the dorm to kill time and find that there are a number of empty floors directly above us."
    "I wonder why they stuffed my entire class in here but didn't bother filling up any of the other rooms?"
    "Uta seems to find it strange as well, but we shrug it off and then walk back to her floor together."

    scene black
    with dissolve

    "The night ends anticlimactically as Uta decides to head back into her room a little ahead of schedule."
    "She offers to let me join but it seems like her and Io are just going to be watching some TV series they're into."
    "Figuring they could use a little alone time, I reject the offer and decide to just visit her again another night..."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta's affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label iofirsthall:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label utahall:
    if utafirsthall == False:
        jump utafirsthall
...
```