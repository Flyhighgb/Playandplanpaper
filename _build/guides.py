"""Blog guides. Each guide answers one search people really make, then points to the matching pack."""


def prod(slug, name, line):
    return (f'<div class="inline-prod"><img src="/img/p/{slug}-1.jpg" alt="" width="110" height="110" loading="lazy">'
            f'<div class="stack" style="gap:.3rem"><b>{name}</b><span class="muted-sm">{line}</span>'
            f'<a href="/p/{slug}/" style="font-weight:800">See the pack →</a></div></div>')


def games(items):
    out, toc = [], []
    for i, (title, text) in enumerate(items, 1):
        sid = f"g{i}"
        toc.append((sid, f"{i}. {title}"))
        out.append(f'<h2 id="{sid}">{i}. {title}</h2><p>{text}</p>')
    return out, toc


ADULT = [
    ("Who's Most Likely To", "Read a card out, such as \"Who's most likely to fall asleep before the King's speech?\", and everyone points on three. Whoever gets the most fingers reads the next card. It needs no explaining and works with any number of people."),
    ("Christmas Would You Rather", "Two choices, no sitting on the fence. \"Would you rather eat only sprouts on Christmas Day or only Christmas pudding?\" Great for getting quieter guests talking, and it works around the dinner table."),
    ("The Left Right Christmas story", "Everyone brings a small wrapped gift. One person reads a funny story out loud, and every time they say \"left\" or \"right\" the gifts move that way. Whatever you're holding at the end is yours to keep."),
    ("Christmas charades", "Split into two teams and act out films, songs and Christmas traditions. Printed cards stop the \"I can't think of one\" pause and keep it fair."),
    ("This or That", "Fast-fire pairs: Elf or Home Alone? Real tree or fake? Stand on one side of the room or the other. Good for a big group because everyone moves at once."),
    ("Draw It!", "Pictionary with Christmas words. One person draws, their team guesses, and a timer keeps it moving. Bad drawings make it funnier."),
    ("Find Someone Who", "Guests mingle to find someone who has, say, worn a Christmas jumper to work. The first to fill their sheet wins. The best icebreaker when guests don't all know each other."),
    ("Christmas Categories", "Pick a letter and fill in a Christmas food, film, song and gift that start with it in two minutes. Score points for answers nobody else wrote."),
    ("Christmas Word Scramble", "Unscramble festive words against the clock. Quiet enough to play with a drink in hand while the turkey rests."),
    ("A Christmas quiz", "A proper quiz with rounds on films, songs, food and traditions. Play in teams with answer sheets and a quizmaster. It fills an hour easily."),
    ("Christmas bingo", "Works for 4 people or 40. Use the word cards for grown-ups and the picture cards when children join in. Small prizes help."),
    ("Christmas A to Z", "Teams race to write something Christmassy for every letter of the alphabet. X and Z cause the most arguments."),
]

KIDS = [
    ("A Christmas scavenger hunt", "Hide clue cards around the house. Each clue rhymes and leads to the next, with a treat at the end. Children can read the clues themselves from about age 6, and younger ones can hunt with a grown-up."),
    ("Picture bingo", "Picture cards mean children who can't read yet can still play and win. Call out the pictures, cover them with sweets or buttons, and shout \"Bingo!\""),
    ("Christmas charades", "Act out a snowman, a reindeer or wrapping a present. Little ones love being the actor, and there is no reading needed if you whisper the word."),
    ("Write a letter to Santa", "A printed letter with prompts makes it easy for children to write their wish list. Add a reply from Santa on Christmas Eve for extra magic."),
    ("Advent activity cards", "One small family activity for every day of December, like hot chocolate and a film, or making paper snowflakes. Pop a card in each advent door."),
    ("Mazes and spot the difference", "Perfect for quiet time while dinner is cooking, or in a restaurant on the run-up to Christmas."),
    ("Christmas colouring pages", "Colouring is calm, easy and works for every age. Print a stack and leave them on the table with crayons."),
    ("Draw It! with Christmas words", "Kids draw a word while their team guesses. Easy words like \"star\" and \"present\" keep it fun for younger players."),
]

g1, t1 = games(ADULT)
g1.insert(1, prod("christmas-party-games", "Most of these are in our Christmas Party Games pack", "12 printable games with answer keys. Instant download."))
g1.insert(12, prod("christmas-family-quiz", "Christmas Family Quiz", "Ready-made rounds for every age, answers included."))
g1.append(prod("ultimate-christmas-games-bundle", "Want the lot?", "The Ultimate Christmas Games Bundle has more than 30 games across six packs."))

g2, t2 = games(KIDS)
g2.insert(1, prod("christmas-scavenger-hunt", "Christmas Scavenger Hunt", "Printable rhyming clue trail for indoors."))
g2.append(prod("kids-christmas-bundle", "Kids' Christmas Fun Bundle", "Activities, advent cards and a Santa kit in one download."))

GUIDES = [
    dict(slug="printable-christmas-games-for-adults", cat="Christmas", date="2026-11-03", mins=7,
         title="12 printable Christmas games for adults that get everyone laughing",
         seo_title="12 Printable Christmas Games for Adults (Easy, Funny, No Setup)",
         meta="12 printable Christmas games for adults that work for 4 to 40 people: Who's Most Likely To, Would You Rather, the Left Right game, charades, quiz and more.",
         teaser="What works for 4 people, what works for 20, and what to print tonight.",
         image="christmas-party-games-1.jpg",
         answer="The best printable Christmas games for adults are Who's Most Likely To, Would You Rather, the Left Right gift game and charades. They need nothing but a printer, work for 4 to 20 people and take 10 to 30 minutes each.",
         html='<p>Grown-up Christmas games have one job: getting people talking who haven\'t seen each other since last year. These are the ones that keep working, whether it is six of you after dinner or a full house on Boxing Day.</p>' + "".join(g1),
         toc=t1,
         faq=[("How many games do I need for a Christmas party?", "Plan about one game for every 20 to 30 minutes, starting with a quick icebreaker such as Find Someone Who."),
              ("What is a good Christmas game for a big group?", "Bingo, This or That and Who's Most Likely To all work for 30 people or more."),
              ("What Christmas games can you play at the dinner table?", "Would You Rather, Who's Most Likely To and a Christmas quiz all work without anyone leaving their seat.")]),
    dict(slug="christmas-games-for-kids", cat="Kids", date="2026-11-03", mins=5,
         title="8 printable Christmas games and activities for kids",
         seo_title="8 Printable Christmas Games for Kids (Ages 3 to 11)",
         meta="Printable Christmas games and activities for kids: a rhyming scavenger hunt, picture bingo, charades, letter to Santa, advent activity cards and more.",
         teaser="Screen-free ideas for the school holidays, from age 3 upwards.",
         image="christmas-scavenger-hunt-1.jpg",
         answer="Great printable Christmas games for kids are a rhyming scavenger hunt, picture bingo, charades and a letter to Santa. Picture-based games suit children who can't read yet, and clue hunts work best from about age 6.",
         html='<p>The school holidays are long, and children get restless by about the 22nd. These printable games and activities keep them busy without a screen, and most need nothing more than paper and a pencil.</p>' + "".join(g2),
         toc=t2,
         faq=[("What age are printable Christmas games for?", "Picture bingo and colouring suit ages 3 and up. Scavenger hunts and word games work best from about age 6."),
              ("Can I use these games in a classroom?", "Yes. Our Classroom Christmas Pack has 30 different bingo cards so a whole class can play at once.")]),
]
