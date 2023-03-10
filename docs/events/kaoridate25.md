# Wither (Kaori)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* kaorinumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: kaoridate25
* Group: Kaori
* Triggered by label: callkaorinight
* Triggered by branch label: callnight
* Triggered by path: callnight->callkaorinight->kaoridate25

## Official wiki page

[Wither](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kaoridate25&go=Go) for more details.

## Event code

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label kaoridate25:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer."

    if bonus == True:
        "And, all jokes aside, I hope there’s no giant cock involved this time."

    "It’s one thing to dedicate an entire night of my potentially unending life to finding a lost chicken, but I think two nights spent on that might be pushing it."
    "Not to mention I still have no idea how things really ended up after we found John."
    "Or why he suddenly has an affinity for saying Maya-esque things despite at least my {i}perceived{/i} understanding that he has not been spending lifetimes watching his chicken friends fall for someone else."
    "I wonder if they’ll return along with summer."
    "I wonder if his {i}voice{/i} will as well."
    "But, like many other minor aspects of my existence, that’s something I’m willing to part with."
    "I find that keeping a mental list of those things can be quite beneficial in terms of ensuring you don’t accidentally wind up hurt while stumbling down this ghost town, life."
    "Not all stars become supernovae. But when you find one that will, it’s best to get as far away as possible."
    "Being caught in the blast of anything is risky."
    "But, then again-"
    "So is something as menial and unimportant as dialing the number of a friend. "
    "Something somewhere explodes."

    play sound "phonebeep.wav"

    k "Phone call!"
    s "Hey, Kaori. What are you up to right now?"
    k "I do not know!"
    s "..."
    k "..."
    s "What do you mean you don’t know?"
    k "Well, it all started with a white cat."
    k "I was on my way home from one of my working places when it was using its beanholders to try and capture a bakeryfly. It was very cute!"
    s "Okay?"
    k "So cute that I chased after it and wound up somewhere unfamiliar!"
    k "And now I do not know how to return home!"
    k "Thankfully, I put a special lock on the door that prevents John from leaving, so he can not disappear again."
    k "I will have to hope that my neighbor feeds him when they realize I am deceased."
    s "You are not going to die, Kaori."
    k "We all die, Friend. It is something I learned by spending time with you."
    s "Okay well, that makes it sound like I’m the reason you learned that and that it wasn’t something that you just happened to learn while I was around."
    s "But if you’re actually lost, why not use a navigation app or something?"
    k "My phone is dead!"
    k "Like all things..."
    s "But you’re talking to me on it right now."
    k "Lightbulb! "
    k "What if I describe the things I see and you go on a hunt of the scavenging variety to locate me?"
    s "Fine. Go. "
    k "I spy with my little vision balls...stars! And...buildings!"
    k "But they are not very good buildings. They are brown-ish. And...there is a wall! But there are many walls in many places, and not all of them keep things out!"
    s "..."
    k "There is a...water crossing street extension! And...wires!"
    k "Lots and lots of wires!"
    k "Wires and wires and wires and wires and-"
    s "Wait, are you in the old district?"
    k "I do not know! Is that where cats go?"
    s "“Water crossing street extension” means bridge, right?"
    k "You are very good at learning! Congratulations!"
    s "I think I know where you are, I just have no idea how you made it all the way over there just by chasing an animal."
    k "Animals can be very fast and have large amounts of stamina! Unless you are referring to the cheetah, which is an animal built for speed but {i}not{/i} stamina! "
    k "This cat was not a cheetah, though. It was much smaller. But did you know that cheetahs-"
    s "Just stay where you are, Kaori. I’ll come and find you."
    k "Thank you, Friend! I wanted to ask for help, but I have not yet discovered how to use my arm feet to make your phone go bzzzzzzzzzzz and always have to wait for mine to do that!"
    s "I’ll teach you soon. Just...stay where you are."
    k "Okay! Phone call!"

    play sound "phonebeep.wav"

    "I hang up the phone and sigh to myself, knowing that I’ve got a long way to walk if I’m going to find Kaori."
    "I just hope that she doesn’t wind up wandering off and that she actually stays where I asked her to."
    "The second half of town is the last place anyone like her should put themselves this late at night. "
    "{i}I{/i} don’t even like being there this late at night and I’m probably twice her size in terms of weight."
    "Here goes nothing, I guess."
    "I think of the phrase someone important uttered at some point that goes, “Nothing ventured, nothing gained” and attempt to connect it to my current situation in a meaningful way."
    "The connection is severed once I remember that I am the living antithesis to that quote, who gains everything from doing nothing but has the potential to be wiped clean if those operations were flipped."
    "Instead of thinking at all, I walk."

    play sound "static.mp3"
    scene kaoribridge1
    with flash
    stop sound
    play music "blueair.mp3"

    "And I arrive."
    "Kaori stands at the railing of a bridge where I once met someone she’s forgotten."
    "She looks up at the sky and thinks of something- probably animals. But I think of something else."
    "Something impure, though not the type of impurity you’d typically associate with me."
    "I think of what it would be like to shove both her consciousness and mine into a blender and deliver it unto the people of this place through telephone wires."
    "If those devoid of life could have life itself injected back into them, I wonder what it would do for this place."
    "And I wonder what would become of us, who sacrificed everything so they could do that."
    "I give up the thought as it’s not my choice to dictate what this girl wastes her mind on."
    "Not while it’s still blooming."
    "Not while mine has already withered."

    play sound "static.mp3"
    scene kaoribridge2
    with flash
    stop sound

    "I take my place beside her and gaze up at the same sky."
    "We see different things."

    k "I did as you asked, Friend. I did not move at all."
    k "And it was very hard because I saw a frog. "
    k "Do you like frogs?"
    s "They’re fine, I guess."
    k "Did you know that frogs have nightvision? And that one of the reasons they are so good at hunting tiny bugs is because they are very sensitive to movement?"
    k "When a frog captures its dinner, it will even pull its eyes down to the ceiling of its frog mouth to push the food down its throat! It is a very impressive way to eat!"
    k "Is there anything special you use your eyes for, Friend?"
    s "Nothing as special as sending them down to the roof of my mouth."
    k "You probably can not do that because you have a chicken brain. And chickens just have normal eyes. Which means you probably have chicken eyes too."
    k "Maybe you are just a large chicken who plucks his feathers?"
    k "Did you know that birds will pluck their own feathers to cope with stress when-"
    s "You need to be more careful, Kaori. You getting lost somewhere like this in the middle of the night isn’t really something I want to deal with regularly."
    s "Same goes for John, I guess. But you matter to me a little more than he does."
    k "I am sorry for making you sadburger."
    k "I didn’t know I would get lost."
    k "Recently, my mind has been very {i}zizz zizz{/i} and I thought petting a kitten would make it more {i}pow pow{/i}. Do you understand?"
    s "Nope."
    k "I will try a little harder to keep your life easy, Friend."

    play sound "static.mp3"
    scene spiderbug with flash
    scene kaoribridge3 with flash
    stop sound

    k "Know that I am with you always. To the end of time."
    s "Or at least until I get tired of finding you."
    k "You will always find me, whether you want to or not! I do not want to disappear, but it is something that can happen!"
    s "Make it...not happen, then? It’s fine on nights like tonight when I’m not really doing anything but, if this were to happen again tomorrow, I can’t say I’d really come out searching."
    k "But you would!"
    s "Why do you sound so certain of that when I’m literally telling you that’s not how it would work?"
    k "If a man owns a hundred sheep, and one of them wanders away, will he not leave the ninety-nine on the hills and go to look for the one that wandered off?"
    s "Since when do you know about metaphors?"

    scene kaoribridge4
    with dissolve

    k "I will continue to make trouble for you because that is who I am. I am a troublesome girl. So much trouble. "
    k "But it is you who continues to find me even when you are not looking that makes me so sure you will find me again."
    k "To the end of time, Friend."
    k "And even after that."
    s "..."
    k "..."

    "Kaori stares off at the sky once again and I can’t help but-"

    k "I am hungry."
    s "Okay, I guess I can finish my inner monologue later."
    k "Do you know of any establishments in this strange part of the world that will feed me at this time of night?"
    s "I mean, there’s a ramen shop not far from here that I- wait, haven’t you been there before?"

    scene kaoribridge5
    with dissolve

    k "Noodle building..."
    s "Is that angry face because you hate noodles or because you’re still upset Tsuneyo wouldn’t hire you?"
    k "Yes!"
    k "There is something strange about that building. Strange about this place. It makes my insides buzz like they are full of bees."
    s "Well, if you want food around here, it’s either that or the convenience store. I don’t really want to scout out any new local businesses at this time of night- especially when most of them are probably defunct."

    scene kaoribridge6
    with dissolve

    k "Mmmmmmmmmmmmmmmmmmmmmmmmmmm!"
    k "Okay!"
    k "But you must protect me from the evil that is the attractive ramen girl! She has access to too many sharp objects and an ingrained dislike for spiders!"
    s "Just keep your shirt on and I’m sure there won’t be any problems, then."
    k "If only things were that easy, Friend."
    k "If only things were that easy..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "After another minute or two of silent reflection as we gaze up at the sky, Kaori and I pull ourselves away from the bridge and begin to make our way over to Tojo Ramen."
    "It’s late enough that Tsuneyo should be closing up soon, but there should still be enough time for Kaori and I to get there and order before it becomes too much of a burden."
    "Not like I really care about being a burden anyway."
    "I helped someone tonight, so it’s only fair that I trouble someone else to cancel that out."
    "Kaori and I make our way through the overgrown streets of the second half of town and I notice her forcing herself to not chase after every living creature she spots."
    "The ones with extra legs, at least."
    "The humans who cling to the sides of old houses or tuck themselves into alleyways seem to be nearly invisible to her."
    "The opposite goes for them, however, who pay closer attention to her movements than I’ve seen them pay to anything else for as long as I’ve been coming here."
    "If it means something, I don’t know what. And I’m far too tired to try and figure it out."
    "So I will swallow my tongue and keep quiet until we arrive, locking any lingering thoughts so far in the back of my mind that even you will not be able to find them."
    "........."
    "......"
    "..."

    scene kaoribridge7
    with dissolve2
    play music "kashiwagi.mp3" fadein 3.0

    t "Welcome to Tojo Ramen. Please take a seat wherever you would like. The options are limitless."
    yu "Yo. What are you two doing here this late? Tsu-chan was just about to close up."

    scene kaoribridge8
    with fade

    s "Kaori got lost after chasing a cat. Then she got hungry. Now we’re here."
    yu "Yeah, okay. That tracks. "
    yu "Shoulda told me. I would’ve came and got her if I knew. Would’ve saved you a whole ass trip."
    s "I’ll do that next time now that she’s practically assured me there will be another."

    scene kaoribridge9
    with fade

    t "You look familiar."
    s "This is the {i}other{/i} girl related to Yuki who came in looking for a job that you refused to hire."
    t "What a persistent and irritating family."
    yu "Hey."
    t "Do you require a menu? Or are the many items listed on our walls sufficient in guiding your decision?"
    s "Just make me whatever. I don’t really care."
    k "I will have..."
    k "Tori shio ramen!"
    yu "Tori shio?"
    yu "Ain’t that your old man’s favorite, Tsu-chan? Remember him always makin’ that for himself back in the day."
    t "That dish is not one that is displayed on our wall. How did you know of it?"
    yu "I mean, it ain’t really a weird dish to order, is it?"
    t "I am simply curious. That is all."
    k "I am a friend of chickens! It is my duty to make sure their sacrifices for our sake do not go to waste!"

    scene kaoribridge10
    with fade

    t "Is it truly a sacrifice if they die unwillingly?"
    k "Does terminating the life-contracts of innocent creatures bring joy to your blood muscle?"
    t "The heart can feel no joy. It is the brain that processes emotions. You are clearly not prepared for the dish you ordered."

    scene kaoribridge11
    with dissolve

    s "I didn’t realize there were dishes you needed to pass a test in order to...order here."
    t "Tojo Ramen reserves the right to refuse service to anyone. For the protection of my family’s restaurant, I must ask that you order something else."
    s "I’m no ramen expert but I think fixing your ongoing power issues should be a little higher on the priority list when it comes to defending your family’s restaurant than refusing customers."
    yu "Oh, I think those are taken care of. I helped out with some of the wiring and shit downstairs earlier today and it’s been fine ever since."
    k "Tori shio ramen! Save the chickens!"
    t "You are a confusing individual. Why cling to something you do not understand? Something you have never experienced?"
    s "Tsuneyo, it’s just soup."

    scene kaoribridge12
    with dissolve

    t "First, ah!"
    t "Second, {i}just{/i} soup?! Have you no shame?!"
    yu "I think that dish might just be important to Tsu-chan because of her dad. Ain’t ever really seen somebody else order it."
    k "Do not make me go to the Yelp! I do not know what it is, but I know that these words instill fear in the brainhearts of my managers!"

    scene kaoribridge13
    with dissolve

    t "Tch. So that is how this is going to be."
    t "I should have known you would play dirty when you reek of arachnids."
    s "Do spiders even have a scent?"
    k "Everything has a scent if you close your eyes and imagine it has a scent!"
    s "..."
    t "Very well. I will make you what you ordered. But I bid you fair warning that I have never made this dish before and would highly implore you to order something else."
    k "I will glue that to the inside of my brain with imaginary glue and {i}un{/i}glue it once I have saved all of the chickens in Kumon-mi!"

    scene kaoribridge14
    with dissolve

    t "Why save what is doomed from the start? "
    k "Why abandon those who need us most?"
    s "Why is this conversation still happening?"

    play sound "imscared.mp3"
    scene black
    stop music

    "{i}Why does everything have to hurt so much?{/i}"

    yu "Yo, are you fuckin’ for real?!"
    yu "You’ve gotta call your electric company or some shit, Tsuneyo. This is gettin’ out of hand."
    t "Tojo Ramen sincerely apologizes for the inconvenience. Please remain calm while I attempt to restore the power."
    s "Looks like we probably should have gone to the convenience store after all."
    t "Why would we go there? We have all of the green onions we need and leaving work would not be convenient for anyone."
    s "I wasn’t talking about you, Tsuneyo. I was talking about Kaori and me."
    t "How rude of you to not invite me. I will not forget this."
    yu "Aight, I’m gettin’ outta here. Just put my shit on my tab and I’ll pay you back next-"

    play sound "imscared.mp3"
    scene kaoribridge15
    play music "sanctuary.mp3"

    yu "JESUS fuck, that noise ain’t easy to get used to."
    s "..."
    yu "Wait, where’d Kaori go? She afraid of the dark or something?"
    s "I think she’s said something about that in the past, but...I don’t think she’d really run away because of a five second blackout."
    s "Or how she could even find the door, now that I think about it."
    yu "Tsu-chan, you cool with puttin’ everything on my tab? That girl’s my niece and I probably shouldn’t be lettin’ her wander around in the dark over here."
    yu "No offense but this part of town ain’t exactly the safest thing around."
    t "Tojo Ramen understands and thanks you for your patronage. Please rest assured that these blackouts will no longer happen after today."
    t "For the sake of my business, I can not allow this to continue."
    yu "Yo, you comin’? Should probably help look for her since you’re the one who brought her here and all that shit."
    s "..."
    s "Yeah."
    s "Yeah, I’ll help."

    scene black
    with dissolve2

    "I follow Yuki out of Tojo Ramen burdened by the sensation of a large pit in my stomach."
    "By the time I make my way out into the open air, the pit grows."

    play sound "static.mp3"
    scene kaoribridge16
    with flash
    stop sound

    "I’m unsure of exactly what it grows {i}into{/i}, however."
    "I can feel thin roots sinking into some organs I probably couldn’t name if they were placed on an autopsy table in front of me...and wonder how much of my body’s resources are being siphoned away by them."
    "I wonder if removing them would be as simple as removing weeds from a garden."
    "A plucking motion- followed by a twist. "
    "A lift of the hand to observe the dirt falling off. To observe what wildlife clings to them, acting as yet another siphon."

    yu "Kaori? You around? "
    yu "I’ll give you a ride home. Just need you to like...come out and shit."
    s "..."

    "I look, but I don’t look far."
    "I don’t know how, but I can tell we aren’t going to find her."
    "Of course, I can’t bring myself to say that because I don’t want Yuki to worry."
    "And I guess {i}I{/i} don’t want to worry either."
    "Everything will be okay."
    "Everything is normal."

    play sound "static.mp3"
    scene kaoribridge17
    with flash
    stop sound

    "Everything is normal."

    scene black
    with dissolve2

    "Yuki gives up on searching and decides to go home."
    "I do the same."

    stop music

    "{i}Kaori’s aff____________________xxxxxxxxxxxxxxx{/i}"
    "........."
    "......"
    "..."

    scene kaoribridge18
    with dissolve2

    "Ami was sleeping on the couch when I came home."
    "All of her clothes were off."
    "She is getting so big."

    scene black
    with dissolve2

    "Sleep."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate25 = True

    jump amidate50
...
```

## Code that triggers this event

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label callkaorinight:
    if kaori_love >= 20 and mayafestival4 == True and kaoridate20 == False:
        jump kaoridate20
    if ((totaldays >= 480) and (chap1point + chap2point >= 200) and (happypoint + happymiss >= 13) and (chikapoint + chikamiss >= 24) and
        (yumipoint >= 20) and (ayanepoint + ayanemiss >= 26) and (sanapoint + sanamiss >= 22) and (makotopoint + makotomiss >= 22) and (mikupoint >= 21) and
        (rinpoint + rinmiss >= 24) and (futabapoint + futabamiss >= 27) and (amipoint + amimiss >= 24) and (nikipoint >= 6) and
        (mayapoint + mayamiss >= 20) and (mollypoint >= 14) and (tsuneyopoint >= 14) and (utapoint >= 9) and (iopoint >= 9) and (otohapoint >= 9) and (nodokapoint >= 5)
        and (toukapoint >= 9) and (yasupoint >= 5) and (norikopoint >= 11) and (kirinpoint + kirinmiss >= 19) and (wakanapoint >= 2) and (osakopoint >= 2) and (yukipoint >= 4) and (tsubasapoint >= 2)
        and (sarapoint + saramiss >= 10) and (harukapoint + harukamiss >= 10) and (karinpoint + karinmiss >= 7) and (kaoripoint >= 7) and (makipoint + makimiss >= 7) and (chinamipoint >= 5) and (day == 6) and kaoridate25 == False):
            jump kaoridate25
...
```