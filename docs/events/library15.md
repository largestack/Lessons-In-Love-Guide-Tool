# Self-Insert
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library15&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 15

✅Event "[Futaba: Cutting Through Cocoons](./futabadorm10.md)" is completed (event=futabadorm10)



## Next events
* [Futaba: Broken Flowers](./futabanew1.md)

## Event properties
* ID: library15
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library

## Event code
File: \game\FutabaEvents.rpy
Code:
```python
...
label library15:
    scene insertredux1
    with fade
    play music "morningmoon.mp3"

    "I have once again returned to the library to be fawned upon by a busty librarian- a thing that most people in life will, unfortunately, never get to experience."
    "Our last meeting here was a bit...unusual, so I’m hoping today is at least slightly more grounded in reality and doesn't involve any more strange notebooks."
    "Just...what was that thing we read?"
    "I can’t remember much of it on account of how quick I was to just toss it aside, but what I do remember is-"

    play sound "static.mp3"
    scene insertredux2 with flash
    scene insertredux3 with flash
    scene insertredux2 with flash
    scene insertredux3 with flash
    scene insertredux1 with flash
    stop sound

    "I can't remember anything about it."
    "Time for girl."

    f "Good morning, Sensei. You’re here a little early today."
    s "I don't think that's true. I left around the same time as always and checked my phone right before coming in here."

    scene insertredux4
    with dissolve

    f "Wait...really? But there’s no one else here yet and you're never the first person in the library after me."
    f "And I know that for a fact because I always judge the time based on how many people show up before you."
    s "What happens if I don’t show up?"

    scene insertredux5
    with dissolve

    f "Hmm...I guess-"

    stop music
    scene tree3

    "TIME STANDS STILL"

    scene insertredux1
    play music "morningmoon.mp3"

    s "Did you bring your story?"

    scene insertredux6
    with dissolve

    f "Oh! Yes! And I even made sure it was the right one just a few minutes ago, so we don't have to worry about any other...strange stories appearing in its place."
    f "I still have to make a few minor changes here and there...but I think it should be at least partially readable by now."
    s "That's great news. I tend to find that most of the best literary works out there are at least partially readable."

    scene insertredux7
    with dissolve

    f "Well, I'm certain this is nowhere near the best, but...I tried my hardest."
    s "So, give me the run-down of your story. Did you try drawing upon any of those daydreams of yours like we talked about?"
    f "Well...kind of. But I can't really draw upon the ones that have already happened since I've always just...forgotten them once they end."
    f "I’ve started keeping track of some of the newer ones, though...so the story you’ll read today is about one of those. And-"

    "Futaba pauses for a moment as she glances over at what I'm assuming is her bag."

    scene insertredux8
    with dissolve

    f "I'm sorry...I’m just suddenly feeling really nervous all of a sudden..."
    s "There's no need to be nervous. This is no different than handing over an assignment in class...Probably."
    s "I haven't really accepted any assignments {i}lately,{/i} but I imagine this is kind of like that."
    s "All things considered, I'm happy with it just being partially readable. The fact that you're comfortable with it is more than enough for me."
    f "Well...okay."
    f "But just...try not to hate it, please..."

    scene black
    with dissolve2

    "Futaba timidly pulls a notebook from her bag and hands it over to me with trembling fingers."
    "I lean my back against the window and begin to read what seems like a fairly typical story."
    "A girl sits at home alone in a room full of stuffed animals, wondering what it is about life that leaves her so unfulfilled."
    "She doesn’t have many friends- just one. A cat named Pedro who walks with a limp."
    "It’s a minor detail, but it’s little things like this that make the world more believable."

    scene story1
    with dissolve2

    f "…"
    s "…"

    "I can tell that Futaba is nervous simply by the way she’s standing next to me."
    "Every once in a while, she lets out a deep breath, as if she’s counting down from ten in order to calm her nerves."
    "Whatever it is, it doesn't seem to be working as she's done it continuously throughout my entire reading session thus far."

    s "…"
    f "…"

    "I continue reading Futaba’s story and, as expected, it goes exactly where I imagined it would."
    "Eventually, the girl meets a boy who doesn’t see her the way everyone else does."
    "He’s not popular or an athlete or anything like that- just an average guy with no discernible traits or characteristics."
    "Things progress and the two of them start dating."
    "It’s a story that appears to be about overcoming self-perception or...allowing yourself to lean on others when that doesn't seem possible."
    "It’s clearly parallel to how I imagine Futaba feels in real life."
    "I do have one question, though..."

    scene story2
    with dissolve

    s "Why did you kill Pedro?"

    scene story3
    with dissolve

    f "Was that part...bad?"
    s "It wasn’t {i}bad.{/i} It just felt...uncalled for? It didn’t really add anything to the story and felt like it was just...more of a shock value thing."

    scene story4
    with dissolve

    f "It was...supposed to symbolize hardship since...he was her only friend at first."
    s "There were symbols of hardship all over the place and the cat was essentially abandoned as a character as soon as the guy came along."
    f "So...I’m...a failure then?"
    s "You're not a failure. It was actually a pretty solid story apart from that."
    s "Maybe a little basic, but a great first attempt. I’m impressed."

    scene story5
    with dissolve

    f "Wait...You mean that? You liked it?"
    s "Sure. Great job, Futaba. Another A+ in the grade book that I totally keep and am not making up."

    scene story6
    with dissolve

    f "Then...umm...What did you think about the main character?..."
    f "Was she...likeable?"
    f "Is that...the kind of person you'd want to spend time with in real life?"

    "Ahh, there we go. Futaba wants me to grade her self-insert character that ends up alongside the insert-version of me."
    "The honest answer would be that the girl in her notebook is just as unremarkable as the man she ultimately falls for."
    "But I’ll let that slide for today since the one in real life is better and...significantly more tangible."

    s "I think she was really interesting, Futaba."

    scene story7
    with dissolve

    f "Really?! You think so?!"
    s "I do. It's unfortunate the story ended where it did."
    s "I'd really like to learn a little more about her."

    scene story8
    with dissolve

    f "You'd like to...learn more about her, huh?..."
    f "If only...we knew who the writer was...Hahaha...Hah..."
    s "Right. {i}If only.{/i}"

    scene story9
    with dissolve

    f "Umm...Sensei?..."
    f "I just want to say thank you for always being around and...giving me positive encouragement and all that."
    f "I was really nervous about today and...you made me feel really calm..."
    f "So, umm...I wouldn't mind telling you a little more some time..."

    scene story10
    with dissolve

    f "About the character, I mean..."
    s "Oh yeah? I think I might have to take you up on that. I’ve been meaning to stop by your dorm again anyway."
    f "Well...You know which room I’m in, so..."
    f "I'll be there...whenever you want..."

    scene black
    with dissolve2

    "The two of us chat for a few more minutes before it comes time for me to head out."
    "Her story was a lot longer than I expected a first-try to be...but I’m honestly really impressed, all flaws aside."
    "For someone who doesn’t normally write, she definitely has potential."
    "I’m sure all the reading she does helps, but that sort of thing can only carry you so far."
    "Eventually, we part ways- but not before making plans with Futaba to meet up again soon."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ library15 = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    jump saturdayafternoon

label library20:
...
```

## Code that triggers this event
File: \game\FutabaEvents.rpy
Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
    if futaba_love >= 15 and futabadorm10 == True and library15 == False:
        jump library15
...
```