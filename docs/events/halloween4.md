# Mysterious Abundance of Chickens
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween4&go=Go)


Part of event chain [The Meat has Come](./halloween3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloween4
* Group: Main
* Triggered by label: halloween3

## Event code
File: \game\script.rpy
Code:
```python
...
label halloween4:
    k "Friend! I have returned!"

    scene kaorihalloween1
    with dissolve
    play music "happyandplotting.mp3" fadein 5.0

    "Kaori trots over to me shortly after Rin and Futaba get on the bus and, to my surprise, she’s wearing a brand new outfit."
    "Did she really get changed just to go for a walk?"
    "And why does she even want to go for a walk in the first place?"
    "Is this an actual date all of a sudden?"

    s "Hey. New clothes?"
    k "Yes! My other clothes became all squish-squooshy after turning the dishes clean!"
    s "The correct word is “wet” for future reference."
    k "Squish-squooshy is better! Use my word instead!"
    s "Fine, Kaori."
    s "So, where are we going?"
    k "Places! "
    s "And is there any reason in particular you want to go to “places” with me?"
    k "I want you to teach me more about humans!"
    k "Today, an angry woman customer yelled at me for the way I speak! It was quite frightening!"
    k "And so I must work hard to obtain the proper knowledge that will prevent me from hurting anyone’s feelings hundreds of years from now when I am finally prepared."
    s "If you’re talking in dog years again, which I’m assuming you are, I can’t imagine it will take that long."

    scene kaorihalloween2
    with dissolve

    k "Really? You think I will be able to master human conversation so quickly?"
    k "Are teachers really that powerful?"
    s "No, I just have a lot of faith in you for reasons beyond my comprehension."
    k "Faith? In the Queen of Spiders? I’m shocked."
    s "I am too, to be honest. You haven’t really done anything to deserve it, really."
    k "Is this what humans call “flirting?”"
    k "Are you attempting to woo me because I am suddenly wearing tight-fitting fabric? Must I remove my clothes a second time and exchange them for yet another pair?"
    s "I don’t think that will be necessary."

    scene kaorihalloween1
    with dissolve

    k "I understand! I am overjoyed to hear this because I did not bring another pair with me today."
    s "I didn’t imagine you did. Bringing two changes of clothes to work would be strange even for you."
    s "So, where are these {i}places{/i} you want to go, Kaori?"
    k "Good question, Friend!"
    k "Tell me, have you ever heard of “chickens” before?"
    s "As a matter of fact, I have."
    k "Would your body be consumed by excitement if I told you there was a place with many chickens?"
    s "Not really, no."

    scene kaorihalloween3
    with dissolve

    k "There is nothing to fear, Friend!"
    k "I was afraid at first as well, but everything will be okay! They are kind animals!"
    k "And they make such strange noises! Like...BACAWK and...SQUAWK!"
    s "…"

    scene kaorihalloween4
    with dissolve

    k "Do not worry. I will protect you."
    k "The spider is a natural predator of the chicken."
    s "No it isn’t, Kaori. That’s not a thing."

    scene kaorihalloween5
    with dissolve

    k "It is! I will show you! "
    k "All you must do is follow me into a nearby alleyway three squares from here!"
    s "Do you mean three blocks?"
    k "Squares and blocks are the same! I will not be deceived by a man who fears chickens!"
    s "I don’t fear-"
    s "Actually, fine. I’ll follow you to the sketchy chicken alleyway."

    scene black
    with dissolve

    "Kaori quickly walks up to my side and points in the direction we’ll be heading to make it to the mysterious abundance of chickens."
    "It’s not exactly what I had in mind for our first “date,” but I guess it fits in with Kaori’s image."
    "Whatever that image may be."
    "I’ll honestly just accept anything she does as normal at this point. "
    "And if she just-so-happened to have found a nearby chicken coop or something, I see no harm in going there with her if it will make her happy."

    scene kaorihalloween6
    with dissolve

    k "So, this bar you speak of- does it have a name?"
    s "I...actually don’t know."
    s "Sara’s Bar, I guess? We can just call it that."
    k "Sara? What is a Sara?"
    s "Sara is a friend of mine who owns the bar. She’s the one you’ll be covering for."
    k "I need to work extra hours because Sara wants to become dizzy instead of working?"
    k "That is a bad mindset. Humans must work hard if they ever want to own pets."
    s "I don’t think she wants a pet, but I’ll let her know tonight that she’ll have to step it up if she does."

    scene kaorihalloween7
    with dissolve

    k "Thank you! Is this Sara person a very close friend?"
    k "She will not steal you from me, will she?"
    s "Well, tonight she probably will. But not overall."
    k "I will be working tonight, so that is fine. I do not know the rules of “The Sara’s Bar,” but I don’t think I am allowed to have fun while I am pouring liquids into cylinders."
    s "I’m sure you can if you want. Sara’s pretty laid back."
    k "Laid-back? "
    k "Does she need one of those chairs with wheels? I do not know the correct name for them."
    s "Wheelchair. And no."

    scene kaorihalloween8
    with dissolve

    k "Yes! Wheelchair! Like the ones they have in the hospital!"
    s "Are hospitals something you’re familiar with, Kaori?"

    scene kaorihalloween6
    with dissolve

    k "Yes! Such delicious juice they have! And they come in the perfect sized canisters!"
    k "Would you like to visit the hospital with me one day, Friend? If you ask them very politely for the juices, they sometimes give you extra!"
    k "Such a generous location!"
    s "Hospitals aren’t really a place people are supposed to go for juice, Kaori. They have juice in convenience stores."
    k "The convenient juices are too large! It is not convenient at all!"
    k "Hospital-sized juices are ideal for consumption."
    s "But didn’t you just talk about getting extra juices?"
    k "Correct! More juices means more juice. Everyone wins!"
    s "But doesn’t that make it the same as just getting one larger juice from the store?"

    scene kaorihalloween9
    with dissolve

    k "You are acting suspicious, Friend."
    k "You speak so much of the convenient stores that I think you may believe all other stores are inconvenient."
    s "I mean...they kind of are, aren’t they?"
    k "Of course not! You must support all local businesses to do your part in stimulating the economy!"
    s "..."
    s "Are you actually smart, Kaori?"

    scene kaorihalloween6
    with dissolve

    k "Maybe you are just not-smart?"
    k "Juices contain vitamins and may help you retain knowledge, Friend."

    if bonus == True:
        k "It may even help you with your trafficking of the tiny girls."
    else:
        k "It may even help you with your trafficking."

    s "Teaching."
    k "Yes, it may help with that as well. It is very impressive how you can hold two completely different jobs at once."
    s "I only have one job. And don’t you hold like ten?"
    k "If you can carry meat in one place, you can carry meat in others."
    k "Stealing girls is a specialized job that only someone large and attractive like you can manage."
    s "Are you flirting with {i}me{/i} now?"
    k "No, I am offering valuable advice that may help you at some point in the future."
    s "And calling me attractive is really part of that advice?"

    scene kaorihalloween10
    with dissolve

    k "Gah! It is so complicated figuring out the differences between the words I say and the ones in my brain."
    s "It’s fine. I’m glad that you’re thinking about how attractive I am all the time."

    scene kaorihalloween11
    with dissolve

    k "Not all of the time! But yes! Many of the times!"
    k "The chickens are close now!"
    k "We should discuss those instead of my physical attraction to you!"

    "I have to admit, chickens aren’t normally my first pick for a conversation topic, but it wouldn’t be very kind for me to force Kaori into flirting when she has a hard time even thinking straight."

    scene black
    with dissolve

    "Kaori immediately begins shouting out random words and hoping one of them will stick. "
    "The thing is, none of them do because they’re all just that. Random words."
    "None of them are anything that two sane people could discuss without some sort of...overarching topic or question surrounding them."
    "Or I guess, in this case, one sane person and one of...whatever Kaori is."
    "………"
    "……"
    "…"

    scene kaorihalloween12
    with dissolve

    k "Ahh! They’re still here!"
    k "I was worried they would fly away!"
    s "Chickens can’t fly, Kaori."
    k "Not with that attitude!"

    "Kaori walks me into a random alleyway in the middle of some random street and we are suddenly surrounded by a bunch of random chickens."
    "Well, I guess they aren’t entirely random given that she said they would be here."
    "But still, nothing about this situation is normal."

    k "I have returned, feathered friends!"
    foc "*Confused chicken noises*"
    s "What are they doing?"
    k "It appears that they have formed a fellowship and are attempting to communicate with us."
    s "Do you understand them?"
    k "Of course not. They are chickens."
    k "I can barely understand humans, let alone silly looking birds."
    s "Okay, so now what?"
    k "What do you mean?"
    s "What do we do with the chickens?"
    k "We watch them."
    k "This is the only normal friendship-activity I know."
    s "This can hardly be called normal."
    k "Friend, why do you think they have gathered here of all places?"
    k "An alleyway is not fit for chickens. They should be in the sky or a swimming pool."
    s "They can’t swim either, Kaori."
    s "Or...at least I don’t think they can? I honestly have no idea."

    "I scan the alleyway for an actual chicken coop and, sure enough, I find one not more than twenty feet away from us filled with even more chickens."
    "My guess is that there’s a restaurant that uses this alley for smoke breaks or something and these chickens are just...part of their menu."
    "It’s a little odd seeing a man-made chicken coop in a city-alleyway, but at least it’s not totally nonsensical anymore."

    s "They’re probably being bred and raised back here before being killed."

    scene kaorihalloween13
    with dissolve

    k "Killed?..."
    s "Yeah. There’s probably a restaurant back here that just raises their own chickens instead of buying pre-slaughtered ones to save money."
    k "Slaughtered?"
    s "Do you see that chicken coop over there? There are even more inside."
    k "If the chickens are going to be killed, why don’t they just run away?"
    k "Do they not fear death?"
    s "Well...they’re chickens. They’re not really known for their intellect."
    s "They probably just live back here passing the time until, eventually, the manager or owner or whoever else comes back here and snaps their neck."
    s "The girl you met at the ramen shop did the same thing when she was little."

    stop music
    play sound "static.mp3"
    scene kaorihalloween14
    with flash
    stop sound

    k "Disgusting."

    play sound "static.mp3"
    scene kaorihalloween15
    with flash
    stop sound

    s "What was that?"
    k "We should free them. Shouldn’t we?"
    s "That’s not really our choice, is it?"
    s "They belong to whoever owns the restaurant."
    k "No they don’t. They are fun and feathery and belong to everyone."
    k "Do you not see the way they look at you? With admiration in their eyes and fire in their tiny, chickeny hearts?"
    s "They just look like chickens to-"

    play sound "static.mp3"
    scene kaorihalloween14
    with flash
    stop sound

    k "Look harder."

    play sound "static.mp3"
    scene howtowish
    with flash
    stop sound

    "PLAY ME A SONG THAT REMINDS ME OF BETTER DAYS."
    "WRITE ME A HAPPY POEM AND WRAP IT IN SHARED MEMORIES. "
    "THINGS FROM OUR YOUTH."
    "ALLOW ME TO TAKE ALL OF THOSE MEMORIES FROM YOU."
    "I CAN FILL YOU WITH SUCH BEAUTIFUL THINGS. "
    "BETTER MEMORIES."
    "BETTER EVERYTHING."
    "ALL YOU NEED TO DO IS LISTEN. "
    "LISTEN TO ME AND NO ONE BUT ME."
    "STOP LOOKING FOR ANSWERS."
    "PLEASE. "
    "IT WILL ONLY CAUSE YOU PAIN."
    "YOU’LL RELIVE ALL OF THOSE HORRIBLE THINGS."
    "THE SCREECH OF TIRES. "
    "THE WEIGHT OF GOD PRESSING DOWN ON YOUR SHOULDERS AS YOU KNEEL DOWN AND REMOVE STRIPS OF STEEL FROM HER BODY."
    "YOU SAW IT ALL."
    "YOU SEE IT ALL."
    "YOU SAW NOTHING."
    "YOU SEE NOTHING."
    "//////EXIT PATH NOT FOUND FOR CURRENT ROUTE"
    "//////USER2 IS NOW REWRITING KEY EVENTS TO PREVENT APPLICATION FROM BEING TERMINATED"
    "//////.................."
    "/////RESET REQUIRED"
    "/////WORLD CAN ONLY BE PARTIALLY REVERTED"
    "/////PLEASE CONTACT ADMINISTRATOR WITH ANY QUESTIONS"
    "/////USER2 HAS LEFT"

    play sound "static.mp3"
    scene kaorihalloween16
    with flash
    stop sound
    play music "amiawake.mp3"

    k "Friend!"
    k "You are alive!"

    "Out of nowhere, I feel myself on the floor."
    "My legs are weak."
    "My mouth feels numb."

    s "What happened?"
    s "What’s going on?"
    k "You suddenly collapsed! This chicken saved your life!"
    k "It is proof that they must be saved! It is a sign!"
    s "How did a chicken save my life?..."
    k "It just did! Do not ask questions! You are too weak!"
    k "Your head made a very loud sound when you landed but I observed its surface area and found no life-juice."
    k "Are you dizzy? Do you need a wheelchair?"
    s "No...and I doubt you’d have one on hand either way."

    "Despite being on the ground and having apparently hit my head, I don’t feel much of anything."
    "It’s just...a little strange being this close to a chicken."

    scene black
    with dissolve

    "I lift myself off of the ground and several of the other chickens who had gathered around me begin to run back to their coop."

    scene kaorihalloween17
    with dissolve

    k "Can you walk? Must I wrap my arms around your body and support you?"
    s "I can walk. I feel fine actually. "
    s "How long was I out for?"
    k "Twenty-three seconds. I counted."
    k "You should return to your residence and enter sleep-mode. "
    k "There will be more days where we can walk. "
    k "I hope today proved to you that chickens can be good, though."
    k "Please tell me at least that much is true."
    s "Sure, Kaori..."
    s "You need to try and not get attached to things like chickens so quickly, though. People are always going to eat animals whether you like it or not."
    k "I know this. I eat animals."
    k "But these chickens are special! I want to protect them!"
    k "I will use the money I receive from the Sara to free them!"
    s "I don’t know if she’s going to pay you enough to buy out the entire stock of chickens, but I’ll support you however I can, Kaori."

    scene kaorihalloween18
    with dissolve

    k "Thank you, Friend. I will also support you when you decide to obtain a furry companion."
    k "Or a feathery companion, like a chicken."
    k "And then I will come to your house and rub its belly three to seven times a week."
    s "I’m not planning on getting a pet any time soon, but sure. I’ll let my [niece] know."
    k "Your [niece] is the pretty girl with the red hair, yes? She is cute. I like her."
    k "Tell her that I said goodbye."
    k "Sorry, I mean hello. I still confuse those two things."
    s "Sure. I’ll tell her as soon as I get home. "
    s "Do you need the address for the bar tonight? I can text it to you if-"

    if bonus == True:
        k "I will find it on my own. Now go to where you and the tiny girl live and fall asleep!"
    else:
        k "I will find it on my own. Now go to where you and the money girl live and fall asleep!"

    s "...Sure. "
    s "I’ll see you tonight, Kaori."

    scene black
    with dissolve2

    "Kaori and I walk out of the alleyway together and go our separate ways."
    "I have no idea what happened to me just now, but there’s a strange sensation somewhere in the back of my mind that feels like it’s trying to claw its way out."

    if bonus == True:
        "I shrug it off and realize that, a few hours from now, I’ll be surrounded by horny drunk women."
        "Here’s hoping I don’t wind up collapsing in the middle of them next."
    else:
        "I shrug it off and realize that, a few hours from now, I'll be with all of my buddies over at the bar."
        "Here's hoping Sara doesn't say anything about her son again!"

    $ renpy.end_replay()
    $ kaori_love += 1
    $ halloween4 = True
    $ trinity3 = True
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "………"
    "……"
    "…"

label halloween5:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```