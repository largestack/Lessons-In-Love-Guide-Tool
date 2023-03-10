# Baby Finches (Happy scenes)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [There is Nothing](./day220.md)

## Event preconditions

* user equal to "HOPE" (unknown variable)



## Next events

None

## Event properties

* Id: babyfinches
* Group: Happy scenes
* Triggered by label: enterusername
* Chain sources: day220
* Chain sources path: day220->babyfinches->coolrectanglemachine

## Official wiki page

[Baby Finches](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=babyfinches&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label babyfinches:
    stop music
    scene happydays1
    window hide
    play music "strawberry.mp3"
    $ renpy.pause(7, hard=True)
    scene happydays2
    with dissolve2

    "I find Maya sitting in her usual spot, on the ledge of the[school] building, looking up at the sky without any regard for her safety."

    s "I thought I’d find you here."
    m "Saying it like that makes it sound like I was trying to hide from you."
    s "Well, you were. Weren’t you?"

    scene happydays3
    with dissolve2

    m "Hahah! Yeah...I guess so..."

    scene happydays4
    with dissolve2

    m "Whose fault is that, though, Mr. “We need to have an important talk today?”"
    s "That’s an incredibly long last name. Please just call me what you always call me."
    m "Darling? My love? Babe? Which one do you want? I call you lots of stuff."
    s "On second thought, call me whatever you want. We need to get serious for a second."
    s "I don’t have time to joke about all of your weird pet names for me."

    scene happydays5
    with dissolve2

    m "Okay, okay. But this is exactly why I was hiding up here. "
    m "I’m not great with all of that serious stuff. "
    m "I get really worried and it makes my chest hurt and my palms get all sweaty and it’s a million-percent no bueno."
    m "So if it’s something we could just bang out before lunch time, that would be awesome."
    m "Unless you’re going to tell me that someone died or something. Then we can take a little longer."
    m "Still, though. Lunch is kind of the main goal here."
    s "I promise it won’t take long."
    s "I just wanted to let you know that I think I might be [[redacted] right now."
    m "[[redacted]? What are you talking about?"
    m "If this is some sort of pickup line, they’re not really of any use anymore now that we’re...you know."
    s "Sorry. Let me clarify."
    s "I was just wandering through the [[redacted] when I saw [[redacted] and thought ssssssssssssssssssssssssssss."

    m "That does actually sound really serious. The last time that happened, we [[redacted]."
    s "Exactly. Which is why I wanted to come find you before it becomes more of an issue."
    m "Is that really it? You could have just texted me that."
    s "Well, yeah. But..."
    m "...?"
    m "But what?"
    s "…"
    s "{size=-15}I kind of wanted to see you...or something.{/size}"

    scene happydays6
    with dissolve2

    m "Ah- What the hell?!"
    m "You know I don’t like corny lines like that! "
    s "And I don’t like saying them."
    s "But...here we are."

    scene happydays7
    with dissolve2

    m "Yup...here we are..."
    m "And umm...thanks..."
    m "I guess..."
    m "Even if I don’t like corny lines, it still makes me happy hearing them from you."
    s "Well, I’m glad..."
    m "…"
    s "…"

    "An awkward silence blows in along with the breeze and dances around the two of us."
    "Maya’s hair gets pushed into her eyes and she opens her mouth, blowing upward to push it back away."
    "I'm not sure why, though."
    "I mean, she’s not looking at anything important. She’s just staring over the ledge the same way she always does when the two of us come up here."
    "But hey, I guess maybe she just wanted to get a better view of the ground or something."

    m "…"
    s "…"

    "Okay, looks like I’m going to have to be the one to break the silence as she’s still dwelling on her embarrassment from a few moments ago."

    s "Well, now that that’s out of the way, we can talk about anything you’d like."

    scene happydays8
    with dissolve2

    m "Oh? Anything, you say?"
    m "So if I asked you where you re-hid all of those magazines I found under your bed, you’d tell me?"
    s "Okay, almost anything. There are some secrets a man must never reveal."

    if bonus == True:
        m "Pervert. Lecher. Debauchee."
        m "I hope you know that God watches you while you jerk off."
        s "Does that mean he also watches us when we have sex?"
        m "I wouldn’t blame him if he did. I’m kind of adorable."
    else:
        m "Oh, huggy boy. You're so funny sometimes."

        "I do a cool spin move and accidentally step on a bug, which makes me feel really bad."

    scene happydays9
    with dissolve2

    m "But I guess we should stop talking about stuff like that before anyone hears us."
    m "There is something I’ve been wanting to ask you, and I guess now is as good a time as any to do it."
    s "Oh? What is it?"
    m "Come a little closer. You’re standing annoyingly far away and I don’t want to keep shouting. "
    m "People are starting to walk by underneath me and might think I’m talking to myself or going insane or something like that."

    scene happydays10
    with dissolve2

    "I take a few steps closer to Maya and stare into her [closed] eyes as she searches through her mind to find whatever topic it is she’s curious about today."
    "I swear, I can never even fathom what things she’s going to bring up."
    "Just the other day, she was educating me on some weird religious theory she heard about a...computer, I think?"
    "I can’t remember."
    "All I know is that it was really strange and just completely went over my head."

    scene happydays11
    with dissolve2

    m "Okay, so this might sound kind of serious."
    m "But that’s only because...well, it {i}is{/i} kind of serious."
    s "Oh?"
    m "It’s about how baby finches are sometimes eaten by their parents before they ever leave the nest."
    s "This again?"
    m "No, no, no. Hear me out."
    m "Sometimes, if the baby finch isn't learning to fly quickly enough or if it just looks weak or something like that, the papa or mama bird literally peck at its head until it dies."
    m "Its brains get turned to mush and, before you know it, it’s just dead right there in the nest."
    m "It’s actually an extremely common problem for people who raise or breed finches."
    m "And so, when I was thinking about this the other day, I realized that you and I would be kind of like finch-parents if we ever had a kid."
    s "Are you implying I’d kill my child for being weak?"
    m "Are you implying you wouldn’t?"
    s "{i}Yes{/i}."
    m "But you hate babies. We both do. "
    m "So if there was a chance to kinda just poke at its little head until it was no more, I’d probably take it."

    "I begin to wonder how soft a child’s head would be in my bare hands and how easy (Or difficult) it would be for me to apply enough to pressure to cause it to cave in."
    "My mind races back to my years of childhood- and I’ve got to say, I’m pretty thankful no one ever did that to me or Maya."
    "I don’t even know what I’d do if my head was squished when I was a baby."
    "Probably not be here, though. Lol!"

    scene happydays12
    with dissolve2

    m "Did you know that three days after death, the enzymes in your digestive system start digesting your body?"
    m "Imagine what it’s like just living inside of something that dies. You probably wouldn’t even realize at first."
    m "You’d just be sitting there thinking to yourself, “Huh. It’s getting awfully dark lately.”"
    m "Then, without really thinking much of it, you’d just start eating your house because you run out of other stuff to do."
    m "But, in a roundabout way, I guess that means baby finches might be able to get revenge on their parents in some timelines."
    m "Like if the parent dies before the baby dies, they can just start feeding away on the parent’s body even more than they do by default of just...being babies."
    m "Wait, never mind. That wouldn't work because birds lay eggs instead of giving live-birth."
    m "Sorry. I’m really fucking high right now and killed a kitten on the way to[school]."
    s "Another one? That’s the third one this week!"
    m "Hahahahahahahahahahahahahahahahahahahahahahahahah!"

    scene happydays13
    with dissolve2

    s "Hahahahahahahahahahahahahahaha!"
    m "Hahahahahahahahahahaha!"

    "We laugh and then touch hands."
    "Maya’s hands are much smaller than mine."

    if bonus == True:
        "They make my penis look bigger than it actually is, though, so that’s a cool plus-side to them."
    else:
        "They make my Doritos look bigger than they actually are, though, so that’s a cool plus-side to them."

    "Not like there are any downsides to small hands other than just, the amount of stuff you can hold with them."
    "I don’t think Maya would be able to palm a basketball, either. But I can, so I’m clearly a more advanced human being than she is."

    scene happydays12
    with dissolve2

    m "Oh, did you want to stop by anywhere after[school] today?"
    m "I think the others wanted to go to karaoke and were going to ask you about it, so I might as well ask you before they have the chance to."
    s "Mmmmmmmmmmmmmmmmmm I don’t know. I’ve got some stuff to do today."
    m "What kind of stuff? Tell me."
    s "I was thinking of memorizing Beethoven’s-"
    m "I just remembered another thing about baby finches. Want to hear?"
    s "Sure."
    m "Another reason for the murder of children that the finch-community (Yes, it’s a thing) has gotten behind is that the male parent might murder children just so it can get them out of the nest."
    m "It’s not a territorial issue or anything like that, though."

    scene happydays13
    with dissolve2

    if bonus == True:
        m "Most people seem to believe that it’s just because the male is so excited to mate again that it destroys its offspring in order to get some of that sweet bird pussy a little bit sooner."
    else:
        m "Most people seem to believe that it’s just because the male is so excited to mate again that it destroys its offspring in order to...well, you know."

    s "Crazy!"

    if bonus == True:
        m "I know, right?! The things animals are willing to do just to get laid are crazy."
    else:
        m "I know, right?!"

    play sound "static.mp3"
    scene happydays1
    with flash
    stop sound

    m "They kind of remind me of you!"
    s "Again, I’m not the type of person who would kill a child."

    if bonus == True:
        m "Maybe not. But you {i}are{/i} the type of person who likes sex so much that you get addicted."
        m "I swear, it’s like there’s not even an escape with you sometimes! "
        m "Like, I’ll be out buying groceries to bring back to my apartment and you’ll just text me saying “Let’s fuuuuuuuuck” and I’ve gotta be like “UGH fine.”"
    else:
        m "Lololol I know. But you {i}do{/i} really like hugs!!!!"

    scene happydays14
    with dissolve

    s "69 74 27 73 20 68 61 72 64 20 66 6f 72 20 6d 65 20 74 6f 20 74 65 6c 6c 20 68 6f 77 20 6d 75 63 68 20 6f 66 20 74 68 69 73 20 69 73 20 72 65 61 6c 20 61 6e 64 20 68 6f 77 20 6d 75 63 68 20 69 73 20 61 20 64 72 65 61 6d "
    s "53 6f 6d 65 77 68 65 72 65 2c 20 64 65 65 70 20 64 6f 77 6e 2c 20 74 68 69 73 20 66 65 65 6c 73 20 6a 75 73 74 20 6c 69 6b 65 20 79 65 73 74 65 72 64 61 79 2e "
    s "42 75 74 20 74 68 65 20 66 6c 6f 61 74 69 6e 67 20 63 61 72 73 20 61 6e 64 20 6d 61 6e 67 6c 65 64 20 6d 75 73 63 6c 65 20 6d 61 73 73 65 73 20 62 65 66 6f 72 65 20 6d 65 20 74 65 6c 6c 20 6d 65 20 6f 74 68 65 72 77 69 73 65 2e "
    s "49 66 20 74 68 69 73 20 69 73 20 61 20 6d 65 6d 6f 72 79 2c 20 69 74 20 69 73 20 6e 6f 74 20 61 20 68 61 70 70 79 20 6f 6e 65 2e "
    s "42 75 74 20 63 68 61 6e 63 65 73 20 61 72 65 20 69 74 27 73 20 6a 75 73 74 20 61 20 6e 69 67 68 74 6d 61 72 65 2e "
    s "Fragments of memories stitched together haphazardly until they resemble something close to a desire."
    m "Hm? What are you talking about?"

    scene happydays15
    with dissolve2

    m "You aren’t allowed to slip into hexadecimal while I’m talking to you."
    m "It’s very distracting."
    m "I don’t speak “numbers.”"

    "I give up on everything and go back to normal."

    if bonus == True:
        "Maya and I spend the next three hours on top of the roof talking about the habits of birds and the places we plan to have sex before we die."
    else:
        "Maya and I spend the next three hours on top of the roof talking about the habits of birds and the places we plan to hug before we die."

    "Some of the places on that list are:"
    "A swimming pool."
    "The produce section of the supermarket."
    "The moon (Improbable)."
    "And her parents’ house."
    "That’s the one I’m most excited for."
    "Not because I dislike her parents or anything. In fact, I’ve never even really heard her talk about them."

    if bonus == True:
        "But the idea of sex in a sex place sounds sexy. "
        "I can’t wait to do sex to her there."
    else:
        "But the idea of hugs in a hug place sounds huggy. "

    scene happydays13
    with dissolve2

    s "Hey, Maya."
    m "Yes, my love?"
    s "Do you ever feel like someone is watching you?"
    m "Of course. "
    m "All the time."
    m "We were just talking about it before, weren’t we?"
    m "God is always watching. That’s pretty much all he does."
    m "He just sits there with his roots planted in the ground and waits for flakes of our skin to fall so he can absorb them and learn things about us."

    if bonus == True:
        m "For example, God probably knows what color underwear I’m wearing and-"
        s "Green."
        m "Hey! No fair! You peeked!"
        s "I didn’t. You just exclusively wear green underwear."
    else:
        m "For example, God probably knows what my favorite flavor of-"
        s "Watermelon."
        m "Hey! No fair! You knew that already!"

    scene happydays6
    with dissolve2

    m "Ugh...you’re the worst sometimes. You know that?"
    s "sssssssssssssssssssssssssssssssssssssss"

    scene happydays2
    with dissolve2

    m "So anyway, what is it you wanted to talk about?"
    m "If it’s something we could just bang out before lunch time, that would be awesome."
    m "Unless you’re going to tell me that someone died or something. Then we can take a little longer."
    m "Still, though. Lunch is kind of the main goal here."
    s "I promise it won’t take long."
    s "I just wanted to let you know that I think I might be [[redacted] right now."

    scene happydays5
    with dissolve

    m "[[redacted]? What are you talking about?"
    m "If this is some sort of pickup line, they’re not really of any use anymore now that we’re...you know."
    s "Sorry. Let me clarify."
    s "I was just wandering through the [[redacted] when I saw [[redacted] and thought ssssssssssssssssssssssssssss."

    m "That does actually sound really serious. The last time that happened, we [[redacted]."
    s "Exactly. Which is why I wanted to come find you before it becomes more of an issue."
    m "Is that really it? You could have just texted me that."
    s "Well, yeah. But..."
    m "...?"
    m "But what?"
    s "…"
    s "{size=-15}I kind of wanted to see you...or something.{/size}"

    scene happydays6
    with dissolve

    m "Ah! Watch what you’re saying! "

    if bonus == True:
        m "Pervert! Lecher! Debauchee!"

    s "Hey, didn’t we just talk about this?"

    scene happydays16
    with dissolve2

    m "Of course."
    m "We’ve run out of other things to talk about."
    m "This is the part where we cycle back around and repeat ourselves."
    m "We’ve been doing this for how long now? Have you really forgotten?"
    m "What’s going on with you? You’ve been acting weird all morning."
    s "I don’t know..."
    s "I just feel like I was in the middle of something."
    m "The middle of what?"
    m "What could possibly be more important than spending quality time with your girlfriend on top of the[school] building?"
    s "You’re not my girlfriend, though."
    m "I’m not?"
    s "No."

    scene happydays17
    with dissolve2

    m "You’re breaking up with me?..."
    s "I’m not breaking up with anyone. We were never together."

    scene happydays18
    with dissolve2

    m "Stop saying that!"
    s "I..."
    s "I have to go now."
    m "Go where?!"
    m "What are you doing?!"

    scene happydays19
    with dissolve2

    m "Wha-"
    m "STOP!"
    m "SENSEI!"
    m "PLEASE!"

    "Hope is the thing with a beautiful sick rose that you can find beauty in the strange proportions and life is yes. "
    "Hooray!"
    "Time to celebrate!"

    play sound "alert.mp3"

    m "D="
    s "sssssssssssssssssssssssssssssssssssssssss"

    menu:
        "Jump":
            scene happydays20
            with dissolve2
        "Jump":
            scene happydays20
            with dissolve2
        "Jump":
            scene happydays20
            with dissolve2
        "Jump":
            scene happydays20
            with dissolve2
        "Jump":
            scene happydays20
            with dissolve2
        "Jump":
            scene happydays20
            with dissolve2

    "I spread my wings and let the wind carry me to heaven."

    scene black
    stop music

    "But then I land on the ground and break my neck."
    "Goodbye."

    $ renpy.end_replay()
    $ babyfinches = True

    scene theend
    with dissolve3
    $ renpy.pause(8, hard=True)
    play sound "static.mp3"
    scene happy1
    with flash
    stop sound
    $ renpy.pause(4, hard=True)
    play music "ifgodwerecalm.mp3"
    jump coolrectanglemachine

label christmas1:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label enterusername:
    $ user = renpy.input("////////////////PLEASE ENTER THE USER NAME YOU WISH TO CONNECT TO. PLEASE NOTE THAT THIS IS CASE SENSITIVE.")
    $ user = user.strip()

    if user == "HOPE":
        jump babyfinches
...
```