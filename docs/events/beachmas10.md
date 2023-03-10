# Treasured (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Bending of Italics](./beachmas9.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachmas10
* Group: Main
* Triggered by label: beachmas9
* Chain sources: beachmas9
* Chain sources path: beachmas9

## Official wiki page

[Treasured](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas10&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label beachmas10:
    scene twogirlsonabed1
    with dissolve4
    play music "hallelujah.mp3"

    a "{i}Okay, okay! It’s my turn again...{/i}"
    a "{i}Two truths and a lie. I played with dolls until I was ten...I keep a secret journal somewhere in my house that no one has ever seen before...and I once had a crush on Molly.{/i}"
    ki "{i}It’s gotta be the Molly one.{/i}"
    mo "{i}Of course it’s the heckin’ Molly one! Arborea’s had her sights set on the same man since childhood! But she didn’t need to just blatantly rub it in like that!{/i}"
    a "{i}Hey, you don’t know that for sure! What if I’ve just been really good at holding it in? {/i}"
    ay "{i}Don’t tempt her, Ami. She has a track record of kissing people during Christmas parties.{/i}"
    a "{i}So do you! Or have you already forgotten the trauma you inflicted on me?!{/i}"
    ay "{i}As if I’d ever forget kissing you! Come here. Let’s do it again for old time’s sake.{/i}"
    no "{i}My, my. This game is proving to be significantly more exciting than truth or dare was.{/i}"
    ki "{i}No wonder Touka bailed right away. But at least we got- woah. Chika, where are you going? You were up next.{/i}"
    c "{i}Oh, I’m done for now. You guys can play without me. I’m gonna go take a break in the other room.{/i}"
    a "{i}Are you sure? I think Rin’s in-{/i}"
    c "{i}Yup! I’ll just chill with her while you guys have fun.{/i}"
    no "{i}Afraid of revealing too many truths? {/i}"
    c "{i}Pfft, as if. Laters.{/i}"

    play sound "slidedoor.mp3"
    scene twogirlsonabed2
    with dissolve

    c "Hey."
    r "..."
    c "You gonna sulk in here all night? Or do you want to maybe {i}try{/i} having some amount of fun before New Year's rolls around? "
    r "I was planning on sulking...so please feel free to go have fun without me."
    c "Is this depression talking? Or is this “I wish my girlfriend was here” talking?"
    r "I probably wouldn’t be talking at all if it were depression. But it’s a lot more complicated than just wishing Otoha was here."
    c "That so?"
    r "..."
    c "..."
    c "Move over."

    scene twogirlsonabed3
    with dissolve

    r "What?"
    c "I said move over. I’ll lie with you if you’re going to be so much of a buzzkill that you won’t even play party games with your friends."
    r "I don’t really think that’s a good idea, Chika."

    scene twogirlsonabed4
    with dissolve

    c "Why not? Worried you might fall for me again?"
    c "Would it help if I threw a shirt on? Oh- but I left my bag in the other room. "
    c "Could I maybe borrow one of yours? Or would that make us look too much like girlfriends?"

    scene twogirlsonabed5
    with dissolve

    r "Borrow whatever you want. We’re girls. Our clothes are basically made for trading."
    r "Just...don’t lie down. Because if someone comes in and sees us and then Otoha finds out, it’ll be a whole-"
    c "{i}Fuck{/i} Otoha."

    scene twogirlsonabed6
    with dissolve

    r "God, I wish it was that easy."
    c "First, eww. Second, aww. Third, move the fuck over, girl."
    r "Right after talking shit on my girlfriend? I don’t think so."
    c "If your girlfriend is going to make you feel like {i}this,{/i} I think I’ve got the right to say a few mean things about her. Come on. Let me take your mind off of stuff."
    r "Are you still going to want to take my mind off of stuff when I stay glued to my phone the entire time, hoping she texts me?"

    scene twogirlsonabed7
    with dissolve

    c "Yeah."
    r "..."
    c "And do you wanna know why?"
    r "Don’t say it, Chika."
    c "Because I love you."

    scene twogirlsonabed8
    with dissolve

    c "And even if you don’t feel tempted to sniff my hair every time I’m opening my locker now, I know you love me too."
    r "But Otoha-"
    c "I knew you first. "
    r "But that doesn’t make it okay to-"
    c "Platonically share the same bed with a girl who cares about you and wants to make you feel better? Gee, silly me. I can see now why you’re so against the idea."
    r "..."
    c "Rin, either you move over...or I am going to come over there and use my crazy bitch strength to move you myself."
    r "Well, when you put it that way...guess I don’t have much of a choice. "
    c "You never did and you never will. "

    scene black
    with dissolve2

    c "Thanks for having me~"

    "........."
    "......"
    "..."

    scene twogirlsonabed9
    with dissolve2

    c "There. That wasn’t so hard, was it?"
    r "No, obviously not. But that doesn’t mean it doesn’t feel weird for me."
    c "Does it {i}actually{/i} feel weird? Are you {i}actually{/i} tempted to climb on top of me right now? Or are you just {i}saying{/i} it feels weird because you know it would piss off Otoha if she walked in?"
    r "I don’t know...I don’t know anything anymore. "
    c "Ahh, the woes of love. "

    scene twogirlsonabed10
    with dissolve

    c "One minute, it’s like you’ve got the whole world in the palms of your hands. But the next, it’s like all of the water on it’s begun spilling through your fingers."
    c "It’s disorienting and scary and you never know what’s going to happen next. So you start thinking, “Hey...maybe I’m not the right person to hold this thing?”"
    c "But the more you think about someone else holding it, the worse everything starts to feel. "
    c "So you hang on as if your life depends on it...because it’s better than the alternative. Better than never knowing."

    scene twogirlsonabed11
    with dissolve

    c "Sorry. That probably sounded a little cheesy, didn’t it? I know I’m not as good at writing as you or Otoha. "
    r "No, it...it was nice. And it made sense. I think. I don’t know. I could probably make some sort of sense out of pretty much anything right now but that’s just how desperate I am, I guess."
    c "Worried of what will happen if someone else gets to hold her instead of you?"
    r "Of course."
    c "Do you think she’s worried of the same thing?"
    r "Maybe..."

    scene twogirlsonabed12
    with dissolve

    r "I mean...I think so? Why else would she get so jealous any time literally anyone else comes up?"
    c "Maybe cause she’s...possessive? Or jealous? Or trying to overcompensate for something?"
    r "You really don’t like her, do you?"
    c "I have this thing where I get kinda pissed off at people who make my loved ones sad. So yeah, Otoha’s on my shit list until she starts getting her act together."
    c "To be honest, I don’t really know much about the girl. So the majority of my opinion on her comes from the fact that I know you have good taste in women. "

    scene twogirlsonabed13
    with dissolve

    r "Do I?"
    c "Absolutely. But ignoring that blatant pat on the back I just gave myself...I want you to know that I’ll always be here for you...and that anyone who would ever hurt you is fucking insane."
    r "Mhm. And are you counting yourself as one of those people? Or do you want to pat yourself on the back a little bit more?"

    scene twogirlsonabed14
    with dissolve

    c "Of course I count myself as one of those people. "
    c "All “logic” pointed toward you in my relationship with love. Same class. Close to the same age. Close to the same {i}size.{/i} You even live right across the hall from me."
    c "But the heart doesn’t care about logic. Which is probably why you’re still so down over a girl you’ve been fighting with for two months now."
    r "Yeah, but..."
    r "It really doesn’t feel like it’s been that long to me."

    scene twogirlsonabed15
    with dissolve

    r "It’s like I just woke up this morning and all of that time passed by without me even realizing it. "
    r "Maybe if...maybe if it really felt like two months...maybe then I’d be able to wrap my head around this and think more rationally, but-"
    c "But the heart doesn’t care about logic."
    c "It wants what it wants and throws a temper tantrum if it can’t have it."

    scene twogirlsonabed16
    with dissolve

    r "Yeah..."
    c "Do you remember {i}why{/i} I turned you down, Rin?"
    c "It wasn’t because I didn’t like you. It was because-"
    r "Because you already had someone. I know."
    c "But did I ever tell you {i}who{/i} that person was? Or anything about them? Because if you knew, you’d be calling it the least logical decision of all time. And you’d see firsthand just how right I am."
    c "You’re not the only one around here who’s impulsive and lovestruck and powered by desire...I’m all of those things too. Which is why I can lie here next to you right now and see where you’re coming from."
    c "The guy I’m with-"
    r "I know it’s Sensei, Chika."

    scene twogirlsonabed17
    with dissolve

    c "You-"
    r "I’ve known the whole time."
    r "I mean...who else would it be?"
    c "Rin-"
    r "I might have lost the stupid bullshit knowledge contest to Yasu fucking Yasui, but I still know Sensei better than almost anybody."
    r "And I’ll admit that I wasn’t even {i}close{/i} to cheering you guys on in the beginning. "
    r "I was jealous and bitter and mad and every other shitty thing a person can feel."
    r "But you guys managed to make it work, didn’t you? You’re still together all this time later while Otoha and I can’t even celebrate a single holiday together without exploding into a million pieces."
    c "But...why didn’t you ever-"

    scene twogirlsonabed18
    with dissolve

    r "What was I going to say?"
    r "“Hey, Chika. Having a good time dating the teacher?” or “Hey, think I could borrow Sensei later if you guys aren’t busy boning? I need help with math.”"
    c "Rin...nobody else can know about this. It’s serious. He could go to jail."
    r "Th...That’s obvious, yeah. But...uhh...the...the point is that you don’t need to go to all these lengths to explain heart logic and stuff like that to me because I already know."

    scene twogirlsonabed19
    with dissolve

    r "I know pain...and longing...and grief...because I’ve been feeling and experiencing those things in tandem with everyone else."
    r "But none of that changes the position I’m in now or where I’m meant to go from here. The only one who can change any of that is me."

    scene twogirlsonabed20
    with dissolve

    r "I just wish it was a little fucking easier, you know?"
    r "I don’t want to be stuck in here. I want...I want to have fun! And make memories with all of my friends {i}and{/i} Otoha."
    c "I know...I know."

    scene twogirlsonabed21
    with dissolve

    r "Why doesn’t she want that too?! "
    r "Why does it always have to be about someone else when it can just be about us?!"
    r "I’m not the one making things that way! I gave up all she wanted me to give up but I can’t just rip you and Sensei out of my life like it’s nothing! I love you guys!"
    r "Why can’t she just let me love you?!"

    scene twogirlsonabed22
    with dissolve

    c "It’s not up to her or {i}anyone{/i} else to ever tell you what you should and shouldn’t feel. "
    r "That’s what I’ve been saying the whole time! But nope! Fuck Rin! She liked Chika {i}once{/i} so she obviously still likes her now! People never move on! That’s impossible!"
    c "You can’t help what you feel and she can’t help what she feels either. The only options are learning to deal with it or moving on."
    r "But I don’t want to move on and she doesn’t want to learn! So what are we supposed to do now?!"

    scene twogirlsonabed23
    with dissolve

    c "Just cry and hold my hand. The pain will hurt a little less if you have someone to share it with. And I can take it."
    r "I know you can...you’re amazing...you’ve always been amazing...and that’s why you can be happy and mature and know how to function as one half of a couple and all I can do is complain and cry."
    c "I’m not always happy and I’m not always mature. I’m just lucky enough to have someone who’s able to put up with that."
    c "And if Otoha can’t be that person for you, {i}I{/i} will."

    scene twogirlsonabed24
    with dissolve

    r "But we’re not {i}together.{/i} It’s not {i}you{/i} I think of the second I wake up anymore. It’s {i}her.{/i} "
    r "It’s not you who comes to mind when I see an old couple happily eating together through the window of a family restaurant, it’s {i}her.{/i}"
    r "When {i}she{/i} sees things like that...does she think of me at all?..."
    r "Or does she just keep walking?"
    r "How can she ignore me so easily, Chika? How doesn’t it eat away at her? "
    r "What do you do when Sensei won’t look at you? How do you catch his eye?"
    r "Apart from being really hot, I mean. But there’s gotta be more to it than that."

    scene twogirlsonabed25
    with dissolve

    c "Pfft...thank you, Rin."
    c "I wish I had better advice to give you, but...getting someone to look my way isn’t really a strong suit of mine."
    c "Sensei was looking at me before I even knew he was. And without even realizing what was happening, I just started looking at him as well."
    c "And yeah...there are times when his eyes wander somewhere else...but all I can do is sit there on the couch and have faith that he’ll come back home. And you know what?...He always {i}does.{/i} "
    c "But that’s not because of anything {i}I’m{/i} doing. It’s because he loves me. And because I love him enough to wait."
    c "So if you love Otoha...and you’re okay with waiting, do it."
    c "But Rin?...I have to say this...and if you want to hate me for it, that’s fine..."
    c "But you can do better. "
    c "You can do {i}so much{/i} better. You {i}deserve{/i} so much better."
    c "You shouldn’t spend every night on the couch...waiting for someone to come home just to have them leave again a week later."
    c "You shouldn’t have to explain yourself every time you have feelings...and you shouldn’t be turned into a villain just because you have so much love to give. "
    c "You should be treasured. The way {i}I{/i} am treasured."

    scene twogirlsonabed26
    with dissolve

    r "Chika...are you...{i}really{/i} sure you’re being treasured? Because-"
    c "Yes...I’m sure. "
    c "I’m sure."
    r "..."
    c "..."

    scene twogirlsonabed27
    with dissolve

    r "Okay..."
    r "Yeah..."
    r "As long as you’re sure..."
    c "..."
    r "..."
    c "Rin, I’m...I’m not sure what your...pre-established limits for touching are...but you can come a little closer if my hand isn’t enough."
    c "I’d be happy to hold you tighter until you manage to calm down."
    r "{i}*Sniff*{/i} You’re crying too, you know..."
    c "{i}*Sniff*{/i} Mhm. Which is why I made the suggestion..."
    r "I don’t know if I’m allowed to have a platonic cuddle buddy...especially one that I masturbated to for years. "
    c "You can masturbate to me whenever you want. I don’t mind."
    r "..."
    c "..."

    scene twogirlsonabed28
    with dissolve

    r "On second thought, it’s probably better if we just lie like this instead."
    c "Yeah...I probably shouldn’t have said that. My bad."
    r "Thanks. Yeah. Just...gonna forget that happened."
    c "..."
    r "..."
    c "You, uhh...want a glass of water or something? I think I need some...fresh air..."
    r "One gallon of ice water, please. And if you could maybe slap me in the face a couple times too, that would be cool. "
    c "Didn’t realize you liked it rough."
    r "Make that two gallons of ice water, please."
    c "Coming right up."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "We have come to associate places like this with tragedy based on prior experience."
    "Patterns, if you will."
    "Remember when we heard about those just a short while ago?"
    "About how hard it is to judge when a pattern is going to break...and precisely what will happen once it {i}does?{/i}"
    "How many other dark places do you link to tragedy? "
    "How long does it take your eyes to adjust when nearly every trace of light has been killed off...like the limbs of animals in objects far too small or tight to support them?"
    "To die in fragments is a beautiful way to go."
    "But do you know what’s even more beautiful?"

    $ renpy.end_replay()
    $ beachmas10 = True

    jump beachmas11

label beachmas11:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
t "I see now that I was blinded by my own perception of events. And that my ill will was only directed toward you as I had nowhere else to send it."
    s "How can you be so sure I’m not just a good actor? And that I’m lying to you right now to get you off of my case?"
    t "I can’t. And as I mentioned earlier, I can’t ever {i}understand{/i} you either. But I can {i}trust{/i} you — which is something Molly wants me to do."
    s "..."
    t "My father always told me that there are forces in this world that will compel us to act in ways we do not understand. "
    t "When I was younger, I would fall back on this every time I added an incorrect ingredient to a recipe or misjudged a portion size. "
    t "But it wasn’t until meeting you and everyone else that I understood his words stretched far beyond the reach of our restaurant. "
    t "I have a hard time remembering those words when things do not go the way they’re supposed to. And I imagine he’d be laughing right now if he could only see me."

    scene tsuneyobeach13
    with dissolve

    t "But he can not. And you {i}can.{/i}"
    t "So I ask you...do you truly care about us?"
    t "Or is the list of what you love still as empty as your eyes?"
    s "I care..."

    scene tsuneyobeach14
    with dissolve

    s "Just..."
    s "I don’t know if I care the way I’m supposed to. Or what the proper way to “care” even is."
    s "But I would never force that on anyone."
    s "At least..."
    s "Not...willingly..."

    scene tsuneyobeach15
    with dissolve

    t "Good. "
    t "But know that if you are lying to me about this...and you do go on to hurt someone in an unforgivable way...that I will not hesitate to introduce your organs to Gallow’s Edge."
    s "You’d be doing everyone a favor, that’s for sure."
    t "In that case, yes."
    t "But as it currently stands, you are the glue keeping many things in place. And a world without you would be sure to collapse within days."
    s "So I hear."
    t "Hearing and understanding are two different things."
    s "I’m like you — not good at “understanding.”"
    t "What I struggle to understand is people. What you struggle to understand is love."
    t "I can tell when someone cares about me, which is one of the many reasons I have not fallen for you the way the others have. I know that there is no real “love” there."
    t "You are the inverse. You can read everyone...and base each of your actions specifically on what you believe a person needs. "
    t "But you can not even understand the love from those closest to you...can you?"
    s "..."
    t "It would be interesting if we could trade places for a day."
    t "I could finally read rooms better."
    t "And you could feel like there’s some sort of purpose to all of this."
    s "I think you should head back to the inn, Tsuneyo. Molly’s going to get the wrong idea and think you hate her if you just keep avoiding her like this."
    s "But, then again, I have no idea what the hell has happened between you two over the last couple months, so...yeah."
    t "Strange. Neither can I."

    scene tsuneyobeach16
    with dissolve

    s "Hm?"
    t "Perhaps it has something to do with the humidity? Or how busy the shop has been as of late?"
    s "How would the humidity-"
    t "Regardless of the root cause, it is good knowing there is someone who feels the same way. As oftentimes, it seems that things are simply going around in circles."
    s "..."

    scene tsuneyobeach17
    with dissolve

    t "Will you not walk with me back to the inn? It is dangerous out here for a weak man like you, and I may be able to provide some sort of protective assistance. "
    s "Tsuneyo...what if I told you that time really {i}was{/i} moving around in circles? And that the way you feel isn’t necessarily wrong?"
    t "I’d say that you’re starting to sound more like my father. Regardless, if you do not need my protection, I will be on my way. My son is waiting."
    t "But thank you again for clearing up the current status of our relationship and where things stand between us. "
    t "I kindly hope for your continued support hereafter."
    s "Yeah..."

    scene black
    with dissolve2

    s "See you...later..."

    "I watch Tsuneyo for a full ten minutes until she disappears from my sight."
    "And it isn’t until she’s gone that I’m able to really grasp what she said about never being able to understand someone."
    "We all have patterns — things we do on a daily basis that help others predict our next actions or sentences."
    "And it’s funny. Based on dialogue and experience alone...she is perhaps the most predictable person in the entire class."

    s "..."

    "But every time her pattern breaks...she goes so far in another direction that it’s impossible to keep up."

    s "..."

    "I can’t help wanting to chase after her."
    "But it’s dangerous out here for someone as weak as me."
    "So I pick myself up off of the ground and set my sights on anyone weaker."
    "On anyone more predictable."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ beachmas9 = True
    stop music fadeout 7.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump beachmas10
...
```