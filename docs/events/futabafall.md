# Fan Fiction (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 5



## Next events

* [Futaba: Under the Radar](./futabafirstvisit.md)

## Event properties

* Id: futabafall
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library
* Triggered by path: library->futabafall

## Official wiki page

[Fan Fiction](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabafall&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label futabafall:
    scene newfall1
    with fade
    play music "morningmoon.mp3"

    "Another morning means another chance to hang around an attractive girl, and so I find myself where I have found myself on several occasions now-"
    "And probably even {i}more{/i} occasions in a life I can’t remember."
    "The only issue this time around is that the girl in question has yet to notice my presence and I have now been standing here for going on five minutes now."
    "What’s even worse is that there are other people here. And seeing as Futaba is the only working volunteer, it has fallen on me to help all of the people she has ignored."
    "This may come as a surprise to you, but I am not very good at helping people."
    "So I am sorry to everyone who I have misinformed today, but that is simply how things must be until I am able to snap the regular weekend librarian out of her daydream-induced stupor."

    f "..."
    s "Futaba, for the millionth time, good morning."
    f "..."
    s "..."

    "Whatever is going on inside that head of hers must be pretty interesting if even hearing {i}my{/i} voice, the one she adores so much, is not enough to snap her out of it."
    "But, then again, it might not be very interesting at all seeing as how every time I get caught in a daydream like that, one of my hands ends up inside of my pants."
    "Futaba has yet to make such a move, unfortunately. And as much as it pains me to say this, I’d have to break her out of it if she did."
    "I am all for the idea of watching her pleasure herself in the library, but doing so in a room full of other students would very likely not be a good move for me."

    f "..."
    s "..."
    f "..."
    s "..."

    "So, what are some other things I can think about in the time between now and whenever Futaba wakes up?"
    "Oh. The weather is nice today. Clouds are expected in the afternoon, with the morning being a bit on the colder side compared to the norm as of late."
    "The birds are chirping, the sun is shining, and I am still an incorrigible predator waiting to feast upon the flesh of an overly-developed teenage girl."
    "Good morning, world. I am here."

    s "Futaba. Please snap out of it before my thoughts start spiraling even further into the abyss."
    f "..."
    s "Futaba. I really need-"

    scene newfall2
    with hpunch

    f "Huh? Sensei? What’s wrong?"
    f "And...how long have you been there exactly?"
    s "Probably ten minutes now. I was only a few more away from calling an ambulance."

    scene newfall3
    with dissolve

    f "I’m so sorry, Sensei. I started reading a new book last night and...I suppose I may have started thinking about it while waiting for you to show up."
    s "Why not just...keep reading the book?"

    scene newfall4
    with dissolve

    f "Because I left it at home."
    s "Futaba, this is a library. Just get another copy."

    scene newfall5
    with dissolve

    f "I’m okay with waiting until I get back home. It wouldn’t be right for me to spend my time getting absorbed in something when there are people here who need assistance."
    s "Yeah, about that. A bunch of people {i}have{/i} needed assistance and you kind of just ignored them."

    scene newfall6
    with hpunch

    f "I...what?!"
    s "Futaba, don’t yell. This is a library."

    scene newfall7
    with dissolve

    f "How...How many people have I ignored? "
    s "I stopped counting after three."
    f "Why would you stop counting after such a low number? "
    s "Why would you forsake your responsibility as a librarian and neglect your job? This is on you, not me."
    f "Sensei...you...wouldn’t happen to know what time it is, would you?"
    s "Probably somewhere around 10:00 AM. I stopped keeping track of that as well."

    scene newfall6
    with hpunch

    f "10:00 AM?!"
    s "We’re still in the library, you know. People are trying to study and you have done nothing but make things harder for them today."

    scene newfall7
    with dissolve

    f "I...haven’t even started reorganizing the shelves yet. And I promised I’d have the entire library done by noon..."
    f "Sensei...you...wouldn’t mind helping-"
    s "Oh, no. I’ve already helped over three people today. If I wanted to help more than that, I’d just start volunteering here myself."

    scene newfall8
    with dissolve

    f "Hah...I suppose I’ll just have to stay later then. This is the price I must pay for letting my imagination run wild again."
    s "If it’s any consolation, I’m not opposed to standing around and further preventing you from doing your job with continued conversation about what was going on in your head a few minutes ago."

    scene newfall5
    with dissolve

    f "At this point, I think that would be fine...I’m already going to have to stay late anyway, so having you around might actually make time go by a little faster."
    s "Then, by all means, start organizing your shelves or whatever it is you need to do while I transition back into the unhelpful burden of a man I am meant to be."

    scene black
    with dissolve2

    "Futaba tears herself away from the desk, closing a notebook that only has a small handful of words scribbled into it, before making her way across the library."
    "I think to myself about whether or not she’d only gotten sucked into daydreaming because she was attempting to write, but ultimately ignore the thought as it doesn’t really interest me."

    scene newfall9
    with dissolve2

    "Unfortunately, the thought comes back just a few moments later when I can’t think of anything else to talk to Futaba about."

    s "So...is everything okay, Futaba?"
    f "Hm? Of course. Everything is completely fine, Sensei. I just get caught up in little daydreams like that from time to time. It’s nothing to worry over, really."
    s "I saw you close a notebook before we got up. Were you trying to write something?"

    scene newfall10
    with dissolve

    f "That’s...um...well..."
    f "To be honest, I’m not really sure how to put this..."
    s "Are you...embarrassed to be caught writing or something?"

    scene newfall11
    with dissolve

    f "It’s less embarrassment about being caught writing and...more embarrassment about exactly {i}what{/i} I was writing."
    f "I’ve always had problems...coming up with my own stories, so...I often find myself just adding to stories made by other people."
    s "Like...writing unofficial sequels or something like that?"
    f "Kind of?...Not just sequels, but...side stories and...alternate scenarios and...things like that."
    f "There’s a term for it. {i}Fan fiction.{/i} But a lot of people frown upon it since it’s not entirely original and...the quality of a lot of it is...really, really bad."
    f "I’m...sure that nothing I do really helps to...break that stigma, but...it keeps me occupied when I’m not actually reading."

    scene newfall12
    with dissolve

    f "W...What I’d really like to do is eventually come up with my own stories, though! From the ground up!"

    scene newfall13
    with dissolve

    f "A good friend of mine from my old school does that...and she’s found a lot of success in...umm...{i}certain circles.{/i}"
    f "I can’t imagine I’ll ever be anywhere as good as her since she’s always been a sort of prodigy, but...I think it would be really nice to also be able to do something like that one day."
    s "Interesting."
    s "Well, I don’t know anything about this fan fiction stuff, but I’m sure that you’d be able to write an original story if you actually apply yourself. "
    s "You certainly {i}read{/i} enough to know what would make a good book."

    scene newfall14
    with dissolve

    f "I do...But, as I’m sure you know, reading and writing are two completely different beasts."
    f "And just because I read a lot doesn’t mean that I’ll be able to come up with an interesting story."
    s "That doesn’t, no. But what about whatever daydream you were having when I showed up?"
    f "That...daydream was another one of my...umm...alternate timelines ideas again..."
    s "Are they all like that?"
    f "All of them? No. I have plenty of original ones too. I just-"
    s "Then how about writing one of those? "
    s "If they’re interesting enough to tear you away from reality for ten minutes at a time, I’m sure there are plenty of other people who’d enjoy reading them as well."

    scene newfall15
    with dissolve

    f "Well...yes. They’re interesting to me...But who’s to say that someone else will enjoy them as much as I do?"
    s "Who’s to say literally anything in this life? Caring more about what others think about your work means nothing compared to what {i}you{/i} think about it."
    s "So what if no one else enjoys it? As long as you do, isn’t it worth the effort?"

    scene newfall16
    with dissolve

    "Futaba pauses for a moment as blood begins to pool in her cheeks and I think about how strange it is that words alone can influence the fluids inside of a person’s body."
    "I wonder if her words will ever do that for someone else?"
    "And I wonder what type of words they would be."

    f "You’re..."
    f "You’re so cool..."
    s "Thanks, Futaba. I try."

    scene newfall17
    with dissolve

    f "Oh! Uhh...haha! I didn’t really mean to say that out loud...but I guess it just kind of slipped out."

    scene newfall18
    with dissolve

    f "That was...a really inspiring thing to say, though...But I guess if anyone was going to be able to give me the push I needed, it would be you."
    s "I’m sure it won’t be the last time I push you. In fact, what if I give you a little assignment to push you even further?"

    scene newfall19
    with dissolve

    f "An assignment?"
    s "Yeah. Take one of those original daydreams of yours and try turning it into a full-fledged story. The kind without characters who already exist in properties owned by other people."
    s "I’ll read it and give you my honest thoughts along with any criticism I may have. "
    f "You...would really go out of your way for me like that?"
    s "Sure.  Writing is a mutated reflection of a person’s innermost self."
    s "The more you put on paper, the more I’ll understand you."

    "And the more I understand you, the closer we’ll become."

    scene newfall20
    with dissolve

    f "And if it’s not good?..."
    f "If I can’t write something that...serves as a reflection...will that ruin your chances of ever {i}understanding{/i} me?"
    s "No clue. I can’t predict the future."
    s "I just don’t think it’s fair to hold yourself back from something you want to do just because you’re afraid of what other people would think."
    s "Especially when one of those {i}other people{/i} is standing right in front of you, telling you to go for it."

    scene newfall21
    with dissolve

    "Futaba locks eyes with me in disagreement with what the pools of blood inside her cheeks would have her do."
    "She pushes back, but her words do not influence my bodily fluids the way mine influenced hers."

    f "Okay..."
    f "I’ll do it. I’ll start writing something. Something original."
    f "I..."
    f "I want you to understand me a little better, Sensei."
    f "I want to write something you can be proud of."
    s "I had a feeling you’d say that."
    s "I won’t give you a due date or anything, obviously. You’re free to do this at your own leisure. And if you need any suggestions or help with anything, feel free to ask."
    s "Just don’t tell any of the other girls about this since I am absolutely giving you special treatment right now."
    f "Can I...or...umm..."

    scene newfall22
    with dissolve

    f "Is it okay if I ask...{i}why{/i} you’re giving me special treatment?..."

    "Her blood wins out in the end."
    "She turns away."

    s "I don’t really have a reason for it."
    s "I guess I just have a soft spot for girls who write."

    scene black
    with dissolve2

    f "Then..."
    f "I’ll do my best to become one of those girls."

    "I don’t stay around for much longer as Futaba still has a decent amount of work to do and my presence has all but prevented her from getting {i}anything{/i} done at all."
    "As such, I take my leave and begin to look for something else to do with the rest of my day."
    "I have no idea what Futaba will manage to create...or even if it will be any good."
    "But at least she’s going to try."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabafall = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label library6to9:
    scene futabafall1
    with dissolve
    play music "morningmoon.mp3" fadein 2.0

    "I decide to spend my morning in the library with Futaba."
    "Apparently, the senior class has an important exam coming up, so the library
    has been getting a bit more traction than normal lately."
    "Not wanting her to feel overwhelmed by the increased workload, I help her
    clean things up and put away a few books."
    "I’m happy that she finally seems to be getting a little more comfortable with me."

    scene black
    with dissolve

    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    jump saturdayafternoon

label library10:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
...
```