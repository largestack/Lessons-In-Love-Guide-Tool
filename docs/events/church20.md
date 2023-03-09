# Mother Duck
Yasu event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=church20&go=Go)



## Event preconditions
✅Yasu love greater than or equal to 20

❌Event "[Yasu: Sore Thumb](./yasuspecial15.md)" is completed (event=yasuspecial15)



## Next events
* [Yasu: Glossolalia](./yasudorm20.md)

## Event properties
* ID: church20
* Group: Yasu
* Triggered by label: church
* Triggered by branch label: church

## Event code
File: \game\YasuEvents.rpy
Code:
```python
...
label church20:
    scene urbanparadise
    with dissolve2
    play music "undersea.mp3"

    "Despite continuous signs that I should stop coming here in the form of vanishing rabbits and duct taped eyes, I find myself in disagreement with the world and all that’s happened to me once more."
    "Though, this time, instead of my legs moving themselves, it is a conscious decision that I have made."
    "I could turn around at any moment if I truly wanted to."
    "So why don’t I want to?"
    "Where does this subconscious compulsion to meet with a girl—who, despite maintaining constant eye contact, will never see eye to eye with me—come from?"
    "And why is the path to her always so devoid of everything but unwelcome sounds and sweat droplets trickling down my chest before being consumed by my clothing?"
    "I think for a moment that maybe tonight will be different."
    "And that maybe I will find Yasu outside of her church and we’ll leave this place and learn who each other really are."
    "But the chances of that are unlikely."
    "Not because we are predictable creatures who dance on the puppet strings of thoughts or beings we cannot see-"
    "But because we're incapable of being anything {i}but{/i} that."
    "So there is nothing left to learn about one another as we have not yet squeezed our way out of our respective cocoons. "
    "And so long as our shells are wrapped tightly in the invisible threads of our masters, we will not break free."
    "The one who controls Yasu keeps her strings firm and taut."
    "And the one who controls me can’t figure out how to untangle them."

    scene black
    with dissolve2

    "A small hole appears in the wall of my subconscious."
    "I press my hands to its edges and pull it open as wide as I can."
    "Its insides smell like rotting wormwood."
    "........."
    "......"
    "..."

    scene yasuoutsidechurch1
    with dissolve2

    ya "Ngh!"
    ya "Let...me in!"
    ya "I...belong inside! "
    ya "I have no use out here!"
    ya "Let me in! Let me in! Let...me in!"
    s "..."

    "Huh."
    "It appears that maybe tonight {i}will{/i} be different after all."
    "I find Yasu desperately fighting against the handle of the church door, attempting to leverage what little body weight she has to pry it open. But all to no avail."
    "She struggles, much like a fish out of water. "
    "And though she may lack the necessary amount of slits in her neck to take in oxygen, the one she has much further down below is sure to bring her more joy than any amount of released carbon dioxide would."
    "Perhaps this sudden rejection at the hands of her god will be the motivation she needs to finally use it?"

    ya "I will repent for my sins! I will repent for my sins!"
    ya "I did not mean to sully your great name, heavenly Father! I did not mean any harm at all!"
    ya "If I have done wrong, strike me down! For I belong nowhere if not inside!"
    ya "I know you not as a cruel and callous god, but as a forgiving and loving one! And that all who wish to enter, may!"
    ya "So why?! Why must you keep me out here?! "
    ya "Tell me, Father! What must I do?! "
    ya "Scream it loud enough that it pierces the veil! Loud enough to penetrate this plague of locusts with a plague of your own!"
    ya "Let me in! "
    ya "Let...me in!"
    s "Yasu...I don’t think you’re going to be able to get in there if someone locked the door."

    scene yasuoutsidechurch2
    with dissolve

    ya "It can’t be locked! It wouldn’t make sense! "
    ya "The hands of mortals who do not accept Him are not strong enough to move these doors!"
    s "I don’t accept him and I move these doors all the time. "
    s "Someone’s probably just fucking with you."
    ya "No! No, that is not possible!"
    ya "This is divine punishment! I have strayed from my path and am being forced aside!"
    ya "I must repent! I must repent!"

    scene yasuoutsidechurch3
    with dissolve

    ya "Let me in!"
    ya "I will right all of my wrongs! Whatever they may be! Just give me a sign! Let me hear your voice!"

    "While the idea of someone going out of their way to lock these doors seems like the most likely scenario, it’s important to note that I’ve never really {i}seen{/i} anyone around here."
    "And with Yasu spending virtually all of her free time inside of this building, it would mean that they would have had to come in one of the rare windows of time in which she’s absent."
    "But that begs to question- why?"
    "What would someone have to gain from closing off an old church building used by no one but a young girl with knotted hair and several screws loose?"
    "What will become of Yasu when she realizes that prayer alone will not get her what she wants?"
    "And that any time it {i}had{/i} in the past was just a convenient coincidence."
    "The same way this meeting is."

    scene black
    with dissolve2

    "For me and not for her, of course."
    "I got what I wanted and the only thing lost was a sliver of sanity in a girl who does not possess much to begin with."
    "It reminds me of something a rabbit once said about gifts."
    "But if this is a gift from an unlikely sponsor—the same one watched by a girl with blue eyes—why am I the one benefiting when all I have done thus far is doubt?"
    "And why is the one who follows so closely behind the guiding light the one caught in darkness?"
    "........."
    "......"
    "..."

    scene yasuoutsidechurch4
    with dissolve2

    ya "Help me open the door!"
    ya "It may be closed for me, but it would never close for you!"
    s "It’s locked, Yasu. It’s not going to make a difference {i}who{/i} tries to open it right now."
    ya "You don’t know that! You don’t know the way He works!"
    s "This may just be my inner “expert sinner” talking, but wouldn’t it be {i}bad{/i} if you were to sneak back into the church if your god truly is the one locking you out?"

    scene yasuoutsidechurch5
    with dissolve

    ya "He will forgive me! For in His light I walk! And all that I am is the result of all He allows me to be!"
    ya "Though the darkness hath clung to my coattails, I have shaken them off and am ready for His touch of reluctant purification!"
    ya "I will be clean again! I will!"
    s "What did you even do to become {i}unclean?{/i}"

    scene yasuoutsidechurch6
    with dissolve

    ya "I do not know. And I {i}can not{/i} know as His voice has retreated behind these doors."
    ya "The only change to my life that I can recall sprung from the pages of the books that I read!"
    ya "But those books were free from the tainted and misconceived depictions of life that true sinners indulge in!"
    ya "What I did should be allowed! "
    ya "There are no rules against entertainment! There are no rules against fun!"
    ya "And yet I find myself abandoned! "

    play sound "static.mp3"
    scene yasuoutsidechurch7
    with flash
    stop sound

    ya "Do you know what happens to a duckling who loses its mother?"
    s "Doesn’t it just...latch onto whoever it sees next?"
    ya "Yes. But if the replacement animal or human does not understand what the duck requires to survive and grow, then what?"
    s "I don’t-"
    ya "It dies."
    s "I thought that nothing ever “dies” in your religion?"
    ya "That which is abandoned can. For He is the one who binds the planes together with fishing wire."
    ya "And if he willfully decides that one can not fit in the space between them, there is nowhere left for that person to go."
    ya "I am caught, Sensei."
    ya "Tangled up in wires."
    ya "I must-"
    ya "Be-"
    ya "Unraveled."
    s "Well, you’re not going to get “unraveled” by just waiting outside a building you can’t get into. So why don’t we...go for a walk and help you clear your mind or something?"

    scene yasuoutsidechurch8
    with dissolve

    ya "A...walk?"
    ya "But where?"
    ya "The world as we know it has been stripped away from us."
    ya "Everything is already g-"
    s "The world is still here, Yasu. Just because you won’t be able to see your normal hangout spot from wherever we’re going doesn’t mean that everything has vanished."
    ya "But...where {i}are{/i} we going?"
    ya "What sort of place will accept me the way I am?"
    s "Wherever I take you, I guess."
    ya "..."
    s "Is that a problem?"
    ya "I do not know..."
    ya "I have lost my mother duck..."
    s "Then make your own decision for once in your life instead of waiting for someone else to make one for you."
    ya "What you ask of me...is to both lead and follow at the same time."
    s "I think choosing to follow can be its own form of leading."
    ya "But only when it's directed at {i}you{/i} and not the true god?"
    s "..."
    ya "Do you see yourself as an interim deity? Are you truly so elevated?"
    s "I see myself as someone who is about to walk away with or without you."
    s "So follow me or don’t. This choice is yours."
    s "But if you plan on sticking around here and trying to pry those doors open all night, the only thing you’re going to find is further frustration and heartbreak."
    s "At least {i}I{/i} won’t willfully abandon you."

    scene black
    with dissolve2

    "I turn around and, just as expected, Yasu clings to my side like the desperate prey she is- hiding under the cover of someone more powerful just because they have an idea of where they want to go."
    "And so I take her into the darkest alley I can find."
    "Not so I can defile her holy, virgin body-"
    "But so she understands that power does not come from the light alone."
    "And that sometimes, it’s easier to see in the dark."
    "........."
    "......"
    "..."

    scene yasuoutsidechurch9
    with dissolve2

    "Vines sprawl out and make their home on the same damp, concrete wall we press our backs against."
    "The smell of mildew spreads throughout the alley, its scent almost pulsing- coming in waves where it turns from bearable to nauseating in the blink of an eye."
    "I distract myself from the need to vomit by focusing on a girl who’s able to ignore the scent entirely. "
    "I imagine this is not the first time she’s spent the late hours pressed up against a damp concrete wall."
    "In fact, I imagine this feels more like home to her than a warm bed in a locked room."
    "It’s the only thing that makes her lack of fear right now plausible when many others in her position would attempt to distance themselves."
    "Yasu pulls her knees to her chest- not because she is scared and defensive."
    "But because, even in this intense summer heat, the only warmth she will let in is that which belongs to her god."
    "And despite my desire to become that for her, it is still far too soon."

    s "So..."
    ya "..."
    s "I take it nothing like that has ever happened before?"
    ya "I have been the purest of the pure. There was no reason to bar me from entry until recently."
    s "There was no reason to bar you from entry {i}tonight{/i} either, though. Right?"
    ya "There must be something. Something I have yet to understand. "
    ya "Something that I must come to terms with so that I can return home."
    s "You have another home now, though. One significantly warmer and less creepy. Hell, it even comes with an extremely hot and generous rich girl."
    s "That’s where I’d be spending {i}all{/i} of my time if I were you."
    ya "But you are not me."
    ya "You resist the light when I require it to move forward."
    ya "It is the reason I still persist today. The reason I can open my eyes."
    s "..."

    scene yasuoutsidechurch10
    with dissolve

    s "I take it you won’t actually tell me about how things were before that, will you?"
    ya "There is no me before the me I am today."
    ya "I am but a product of Him alone. An angel in training that lives to serve, even while I am falling to the ground."
    s "But you were someone else {i}before{/i} that."
    ya "And so were you. "
    ya "The reasons you do not speak of your past self may not be different from those which belong to me."
    s "In all fairness, you’ve never really given me the opportunity to speak of my past self around you."
    ya "Would you if I did?"
    s "That’s...a little complicated."

    scene yasuoutsidechurch11
    with dissolve

    ya "Yes..."
    ya "It is, isn’t it?"
    ya "You have so many secrets that even the air struggles to hold them."
    ya "It is why I know more about you than you will ever understand about me."
    s "Oh yeah? Then...what do you know?"
    ya "..."
    s "..."

    scene yasuoutsidechurch12
    with dissolve

    ya "I know that tragedy would befall each and every one of us if I were to share that information with you."
    s "That sounds a lot like a convenient excuse to make up for the fact that you’re just bullshitting me right now."
    ya "If that is what you believe, then that is what you believe."
    ya "But that is where our biggest difference lies."
    ya "All you {i}can{/i} do is believe. But all I can do is {i}know.{/i}"

    scene yasuoutsidechurch13
    with dissolve

    ya "The secrets of this world and everyone in it glitter like diamonds."
    ya "The stars are not real. They are the residue of hopes and wishes. Dreams and desires."
    ya "And when we gaze up at them with our undeserving eyes, we are gazing at the past itself and each and every trace left behind during a departure from one plane to the next."
    ya "Would you believe me if I told you of the stars below us as well?"
    s "I wouldn’t believe you no matter what you told me about literally anything."
    ya "Even when that’s all you can do? When I {i}know?{/i}"
    s "Yes. Because we have actual scientific explanations for the stars and I have a hard time believing that the key to everything is the endless rambling of a cult member."

    scene yasuoutsidechurch14
    with dissolve

    ya "A cult is full of members. I am but {i}one{/i} measly soul- filled with nothing but messages too painfully true for those around me to grasp."
    ya "Those unlike you."
    ya "But your palms will open soon enough. And in them, I will place little shards of His truth. A truth that will change the way you perceive your life."
    ya "Soon, you will forget how to swim."
    ya "And as your head falls beneath the surface of the water, you will understand just how much His protection means."
    ya "The tide is rising, Child of Man. A torrential downpour looms on the horizon."
    ya "He can teach you how to swim once more. He can lift you up when the water starts to fill your lungs."
    s "I thought you couldn’t hear him any-"
    ya "I have heard this so many times that it is engraved into the back of my mind like initials on a tree."
    ya "You are popular in more than one plane, Sensei."
    ya "Your entire being transcends that which grounds the world."
    ya "Your failure to accept that would be a sin if it were anyone else."
    ya "But {i}you-{/i}"
    ya "You are His favorite."
    ya "Even though you deny Him so."

    scene yasuoutsidechurch15
    with dissolve

    s "Yeah, well...maybe if gods weren’t such fucking pricks I’d be more inclined to believe in them."
    ya "Do not fear, for I will make you believe."
    ya "And in me, you will find reason to persist. "
    ya "Though the doors may be closed tonight, the quieting of the insects has provided an opportunity for me to catch His whispers once more."
    ya "I do not know if He wants me to have them, but I am His humble servant and would willingly give my life to make His better."
    ya "Soon, I will help you understand."
    ya "Soon, you will have no reason to doubt me."

    scene yasuoutsidechurch16
    with dissolve

    ya "Soon, it will all be revealed!"
    ya "He will rise from the ground! Coated in the thick residue of dreams deterred! With arms spread wide, beckoning us forward!"
    ya "He will take us under his wings and we will return to where we belong! Clinging to his feathers as he reminds us that we are eternally loved so long as we obey!"
    ya "The snow has gone! It quiets his screaming no longer!"
    ya "The light returns! The light returns!"
    ya "And soon-"
    ya "So will we!"

    scene black
    with dissolve2

    "I stop paying attention to everything Yasu says somewhere in the middle of her speech."
    "I had thought this was finally going to be an opportunity to learn more about her."
    "About the {i}real{/i} her."
    "Or, as she would likely put it- the her that isn’t {i}her{/i} anymore."
    "But I guess that’s not going to happen."
    "And I guess that if it ever {i}will{/i}-"
    "It won’t be anywhere near here."
    "I should have taken her to a darker alley, further away."
    "I should have taken her somewhere the wind could not reach."
    "Somewhere underground."
    "Beneath the blanket of dreams deterred."

    $ renpy.end_replay()
    $ church20 = True
    $ yasu_love += 1
    stop music fadeout 7.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasudorm20:
...
```

## Code that triggers this event
File: \game\YasuEvents.rpy
Code:
```python
...
label church:
    if yasu_love >= 0 and ramen20 == True and church1 == False:
        jump church1
    if yasu_love >= 5 and church1 == True and church5 == False:
        jump church5
    if yasu_love >= 10 and yasudorm10 == True and day == 7 and church10 == False:
        jump church10
    if yasu_love >= 15 and chapthree8 == True and church15 == False:
        jump church15
    if yasu_love >= 20 and yasuspecial15 == True and church20 == False:
        jump church20
...
```