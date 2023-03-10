# The Queen of Spiders (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 5



## Next events

* [Sana: Scouting Mission](./bar20.md)
* [Rin: Good Day, Humans](./cafe25.md)

## Event properties

* Id: amisroom5
* Group: Ami
* Triggered by label: amisroom
* Triggered by branch label: amisroom
* Triggered by path: amisroom->amisroom5

## Official wiki page

[The Queen of Spiders](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amisroom5&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amisroom5:
    scene black
    with dissolve
    play sound "dooropen.mp3"
    play music "normalday.mp3"

    "I guess I’ll see if Ami has any plans today."
    "I woke up feeling a lot more exhausted than normal for some reason, so the idea of going anywhere right now sounds like nothing more than...unnecessary pain."
    "Combine that with the fact that all I'd be doing is searching for another cute girl to hang out with and there's really no reason for me to ever leave at all."
    "Everything I could ever want is right here at home."
    "........"
    "......"
    "..."

    scene amidineredux1
    with dissolve2

    a "Oh, Sensei! Good morning. I was just going to come wake you up and see if you wanted to go out."

    "God damn it."

    s "Nope. I'll just stay here and be miserable."
    a "You're not allowed to be miserable while I'm here. That's one of our house rules, remember?"
    s "I remember no such thing. Where could you possibly want to go this early in the morning?"

    scene amidineredux2
    with dissolve

    a "Some new diner thingy just opened up the other day and I figured the two of us could go together since going to a diner by myself would make me look really lame."
    s "Are Ayane and Maya busy today or something?"

    scene amidineredux3
    with dissolve

    a "I don't think they're {i}busy...{/i}but chances are that both of them are still sleeping."
    s "You...don't want to call them and find out?"

    scene amidineredux4
    with dissolve

    a "Sensei...can you look down, please?"
    s "What? Why?"
    a "It's just that I've dropped so many hints about {i}wanting to do this alone with you{/i} over the last two minutes that they are now making the house look messy."
    s "Don't drop hints. It's best to just speak your mind, Ami."

    scene amidineredux5
    with dissolve

    a "I literally did that and you just said you'd stay here and be miserable!"
    a "Prove that you love me and come have breakfast at the new diner with me or I will throw myself off a bridge and leave a note saying you made me do it!"
    s "It was nice knowing you, Ami."
    a "Sensei!"
    s "I'm obviously kidding. I'll come. Just...give me a minute to get dressed since I was really planning on spending the whole morning here."

    scene amidineredux6
    with dissolve

    a "Really?! You'll go on a date with me?!"
    s "I'll come to the diner with you. I don't think I'm allowed to date my niece."
    a "Says who? There's no rule like that {i}I've{/i} ever heard about before."
    s "Then you haven't been paying much attention to societal norms or values. This place isn't far, is it?"

    scene amidineredux2
    with dissolve

    a "Not super far. Maybe like...a mile or two?"
    s "You're really going to make me walk a whole mile as soon as I wake up?..."
    a "You walk to other places all the time. What's the harm in walking somewhere with a cute relative at your side?"
    a "Besides, the two of us could use a little exercise, don't you think?"
    a "Unless there's some {i}other{/i} sort of physical activity that the two of us could do together in the comfort and privacy of our own home."
    s "Isn't that being a little too suggestive this early in the morning?"

    scene amidineredux3
    with dissolve

    a "I have no idea what you're talking about. I just want to spend some quality time with my uncle."
    s "I am sure you do..."

    scene black
    with dissolve2

    "I head back to the bedroom and change my clothes, wondering how serious Ami was about the whole {i}physical activities{/i} thing and...whether or not {i}I'd{/i} be serious about that as well."
    "But seeing as I don't want to walk one or two miles with an erection pressing up against the inside of my jeans, I decide to abandon the thought and simply think of nothing instead."
    "………"
    "……"
    "…"

    scene amidiner1
    with dissolve2

    "After a decently long walk, we make our way into a relatively old-fashioned, American style diner."
    "The air conditioner in here is turned on full-blast, making it an extremely welcome escape from the sweltering summer heat we were forced to battle on the way over."
    "For being what Ami claims is a new business, the diner is surprisingly empty."
    "Only a few tables are occupied by customers while a single waitress makes her way around the room, checking on each and every table while Ami and I figure out what we want to eat."

    a "Sensei, do you know what you’re gonna get yet?"
    s "I have no clue."
    a "Do you want something sweet? Or do you want something savory? Because I heard online that the doughnuts here are crazy good."
    a "But also, you shouldn't get the doughnuts because that's what I'm getting."
    a "You know what? I'll just choose for you. Get something savory and we can share with each other if it really comes down to it."
    s "Well, that certainly makes things easier for me."
    s "A little more freedom would be nice, though."

    scene amidiner2
    with dissolve

    a "You're free to do whatever you want! As long as what you want to do is love me."
    s "..."

    scene amidiner3
    with dissolve

    a "Kidding."
    a "Maybe."

    "I think my niece might be obsessed with me."

    scene amidiner4
    with dissolve

    wa "Hello, humans! And welcome to food! My name is Kaori Kadowaki and I will now write down the objects you wish to consume on this rectangular book of slaughtered trees."

    if day65 == True:
        "Isn't this the same girl that was working at the bistro where I met up with Sara and Haruka?"
        "Isn't she a little young to be working multiple jobs?"

    scene amidiner5
    with dissolve

    a "That's funny. I don't remember seeing anything online about this diner being themed."
    k "Yes! Themed! The theme here is hunger! And the characters are you and the large, intimidating man with circles of glass in front of his vision balls."
    a "You...said your name was Kaori?"
    k "Yes! That is what I am called. But you may also address me as the Mistress of the Dark or the Queen of Spiders. All of these things are true! I think!"

    scene amidiner7
    with dissolve

    k "Have you been inside of this building before?"
    a "Not yet. I've seen a lot of people talking about it online, though."
    k "On which line?"
    a "The...The Internet?"

    scene amidiner8
    with dissolve

    k "Did you also bring a net? Or did your girlfriend just require moral support for all of the flavors she is going to catch?"

    scene amidiner9
    with dissolve

    a "G-G-G-G-G-Girlfriend?! Is that who you think I am?! Does it really look that way?!"
    k "Was my assumption incorrect? I smelt a heavy dose of romantic pheromones shortly after the two of you entered the store."
    a "Pheromones?!"
    k "So strong that they are almost pulsating! I can feel them surrounding my body and squeezing me the way I long to squeeze small dogs."

    scene amidiner11
    with dissolve

    k "Treat her well or face the consequences."
    s "..."

    scene amidiner9
    with dissolve

    k "What would you like to eat, small girl?"
    a "I-"

    scene amidiner11
    with dissolve

    k "I am serious. Protect this tiny human."

    "Am I wrong for feeling mildly intimidated right now?"

    scene amidiner9
    with dissolve

    k "What is your name and how many muffins have you eaten in your life?"
    k "Please also inform me on the object on our menu that you most want to put inside of your mouth."

    scene amidiner12
    with dissolve

    a "Well, umm..."
    a "My name is Ami..."
    k "An adorable name for an adorable girl. Tell me what your desired food is called, Ami."
    a "Uhh...there's a...doughnut platter thingy, right?"
    k "That is a thing that exists. Yes."

    scene amidiner13
    with dissolve

    k "And for you, mystery man? Please list the objects you are most interested in at this very moment."

    "I'm beginning to think that Ami is right in assuming that this is some sort of themed diner, but...I can't really tell what the theme is by the way the waitress is speaking."

    s "I’ll just have a burger. Thanks."
    k "I understand. One order of fried zeros and a hot meat sandwich coming right up for the cute Ami and her human boyfriend."
    k "Please remain at this specific rectangle and I will return right away."

    scene amidiner15
    with dissolve

    "Kaori or...the mistress of whatever disappears from the table, prompting Ami and I to awkwardly resume where we left off moments ago."

    a "She’s...umm..."
    a "A little-"

    scene amidiner16
    with hpunch
    play sound "thump.mp3"

    k "I have returned with the things you wanted!"
    s "How the hell did you do that so quickly?"
    k "Do not ask questions that you are not yet prepared to hear the answers to!"
    k "For there is one nickname I did not mention when I first introduced myself..."

    scene amidiner17
    with dissolve

    k "You see before you, Kaori...the Goddess of Gluttony...the world’s greatest waitress..."
    a "How...what?..."
    s "If anything, I’m more impressed with the cooks. All you really did was carry everything over."
    s "And we didn’t even order the coffee you gave to Ami."

    scene amidiner18
    with dissolve

    k "The Ami needs the hot bean water to grow strong and develop larger bones!"
    s "I think there might be some misunderstanding on your end about the nutritional value of coffee."
    k "Do not tempt me to return your meat to the cooking zone! I will do it!"

    "Kaori quickly snatches back the burger she had placed in front of me before I’m even able to take a bite."

    s "I am so confused."

    scene amidiner19
    with dissolve

    k "You will eat when I deem you worthy."

    scene amidiner20
    with dissolve

    a "Umm...Miss Kaori?"

    scene amidiner21
    with dissolve

    k "What is wrong? Will your tiny body reject the strength of the hot bean water?"
    a "No, I just...was wondering if that spider on your chest was a real tattoo or not?"
    k "It is. Would you like to touch it?"
    a "I...don't know if I should with where it's located."
    k "I understand. Human customs say that a spider on one's body must not be touched until the seventh date."
    s "I didn’t realize there was a custom for something that specific."
    k "May I ask you a question now, Ami?"
    a "Of course. What do you want to know?"
    k "What is your favorite animal?"
    a "…"
    a "Is that...really what you want to ask?"
    k "Do you not have one?"
    a "Um...I guess...I think cats are really cute?"
    k "I see, I see."
    k "I will remember this."
    a "Okay...umm..."
    a "Thank you?"
    k "You are very welcome."

    scene amidiner22
    with dissolve

    k "As for you..."
    s "What did {i}I{/i} do?"
    k "I will allow you to eat this hot meat sandwich under one condition."
    s "And what condition would that be?"
    k "You must say one nice thing about me."
    s "What? Why?"
    k "Because you have jammed an invisible knife into my feelings and they are now deflating."
    k "Please patch me up immediately."
    s "Uhh..."
    s "You're...really attractive?"

    scene amidiner26
    with dissolve

    k "GUH!"
    k "That...That is not the type of nice thing I thought you would say, boyfriend-man!"
    a "Yeah...me neither."

    scene amidiner27
    with dissolve

    a "And I'm extra annoyed because I actually agree."
    a "You look kinda like a...rock idol or something. And you're super cool and now I'm jealous."
    k "The Ami thinks that too?! Is this what they call a gangbang?!"
    s "Uhh...no. No it's not."

    scene amidiner28
    with dissolve

    k "All I wanted was my role as the greatest waitress in the world to be validated by a large man and his miniature girlfriend!"
    k "Now, I must deal with the extra blood in my face! And all because of you two!"
    a "We...weren't trying to offend you, Miss Kaori. We just-"
    k "I will now depart! The weight of these comments has become too much for me to bear!"
    k "Please remember to like, comment, and subscribe!"

    scene amidiner29
    with dissolve

    "Kaori vanishes into the kitchen, leaving both Ami and me in a state of mild shock."
    "But, on the bright side, the room quickly grows much quieter."

    a "…"
    s "…"
    a "So, uhh...I guess we just...eat breakfast now?"
    s "What just happened?"
    a "I’m not really sure..."
    a "I kind of like her, though."
    s "What? Why?"
    a "I...don't really know."
    a "I just kind of...do."

    scene black
    with dissolve2

    "Ami and I finish up our meals without any further interruption from the diner staff..."
    "Something tells me this isn’t the last we’ve seen of Kaori, though..."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amisroom5 = True
    stop music fadeout 3.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label amisroom10:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amisroom:
    if ami_love >= 0 and firsttimeamisroom == False:
        jump firsttimeamisroom
    if ami_love >= 5 and amisroom5 == False:
        jump amisroom5
...
```