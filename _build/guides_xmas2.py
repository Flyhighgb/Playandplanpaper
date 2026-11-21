"""Christmas guides, batch 2 (added 21 Nov 2026): large groups and Boxing Day."""
from guides_xmas import pack, sec, ul, ol

DATE = "2026-11-21"

BIG_GAMES = [
    ("Christmas quiz in teams", "Split into tables of 4 to 6, read ten questions a round and swap answer sheets to mark. Works for 10 people or 100.", "christmas-family-quiz"),
    ("Who's Most Likely To", "Read a card out loud. On the count of three everyone points at the person most likely to do it. No props, no teams, instant laughs.", "christmas-party-games"),
    ("Christmas bingo", "Everyone gets a different card and one person calls. It needs no skill, so children and grandparents can win together.", "christmas-bingo"),
    ("The Left Right gift game", "Everyone holds a wrapped gift while you read a story. Each time you say left or right, the gifts move that way. Whoever holds a gift at the end keeps it.", None),
    ("Beat the minute challenges", "Teams take turns at 60-second challenges like stacking cups or flicking a bauble into a bowl. Everyone else cheers, which is half the fun.", "beat-the-minute-christmas-games"),
    ("Christmas charades", "Two teams, a pile of cards and a one-minute timer. Films, songs and Christmas jobs like untangling the lights.", "christmas-party-games"),
    ("Guess the price", "Show a list of Christmas favourites and everyone guesses what they cost. Closest guess wins the round. Great for mixed ages.", "christmas-guess-the-price"),
    ("Emoji song and film quiz", "Put emoji puzzles on the TV or hand out sheets. Teams race to name the Christmas song or film.", "christmas-emoji-games"),
    ("Gift exchange dice game", "Everyone brings one wrapped gift. Roll a die each turn: swap, steal, unwrap or pass. Gifts change hands until the timer runs out.", "gift-exchange-dice-game"),
    ("Christmas Would You Rather", "Read a question and everyone moves to one side of the room. Quick, silly and good for breaking the ice.", "christmas-party-games"),
    ("Pass the parcel with forfeits", "Add a forfeit card under each layer: sing a carol, do your best reindeer, tell a cracker joke.", None),
    ("Christmas word search race", "Pin a giant word search on the wall and let teams hunt in turns. It keeps a big room busy for an hour.", "giant-christmas-word-search"),
]

BIG = dict(
    slug="christmas-games-for-large-groups", cat="Christmas", date=DATE, mins=6,
    title="12 Christmas games for large groups (10 to 50 people)",
    seo_title="12 Christmas Games for Large Groups (10 to 50 People)",
    meta="12 Christmas games for large groups that work for 10 to 50 people: team quizzes, bingo, Who's Most Likely To, gift games and quick-fire challenges. Easy to print and run.",
    teaser="Team quizzes, bingo and gift games that work for a full room.",
    image="christmas-party-games-1.jpg",
    answer="The best Christmas games for large groups are ones where everyone plays at once: a team quiz, Christmas bingo, Who's Most Likely To, the Left Right gift game and quick 60-second challenges. They need little setup, work for 10 to 50 people and suit mixed ages.",
    html="<p>With a big group, the games that work are the ones where nobody waits for a turn. Everything below either plays in teams or gets the whole room involved at once. Each one needs a printer and a pen at most.</p>"
         + sec("games", "12 games that work for a crowd", "<ol>" + "".join(
             f"<li><b>{n}.</b> {d}" + (f' <a href="/p/{s}/">Printable version →</a>' if s else "") + "</li>" for n, d, s in BIG_GAMES) + "</ol>")
         + pack("ultimate-christmas-games-bundle-1.jpg", "Ultimate Christmas Games Bundle", "30+ games in one download: quiz, bingo, charades, Who's Most Likely To, hunt and more.", "4607015011", "ultimate-christmas-games-bundle")
         + sec("plan", "How to run games for a big group", ol([
             "Pick three or four games and plan about 20 minutes for each.",
             "Make teams before people arrive. Mix ages and mix people who don't know each other.",
             "Print everything the night before, and keep one spare copy of each sheet.",
             "Give one person a microphone or a loud voice. Running a game is easier than playing it.",
             "Have a small prize for each game. Chocolate coins work well."]))
         + sec("which", "Which game for which group?", '<div class="tbl-wrap"><table><thead><tr><th>Group</th><th>Start with</th></tr></thead><tbody>'
             + "<tr><td>Family Christmas Day, all ages</td><td>Bingo, then a team quiz</td></tr>"
             + "<tr><td>Work Christmas party</td><td>Who's Most Likely To, then the gift dice game</td></tr>"
             + "<tr><td>Friends with drinks</td><td>Beat the minute, then charades</td></tr>"
             + "<tr><td>School class or club</td><td>Bingo, then the word search race</td></tr>"
             + "</tbody></table></div>"
             + '<p>Planning a work do? See our <a href="/ideas/office-christmas-party-games/">office Christmas party games</a>. For a smaller table, try these <a href="/ideas/christmas-dinner-table-games/">Christmas dinner table games</a>.</p>'),
    toc=[("games", "12 games"), ("plan", "How to run them"), ("which", "Which game for which group")],
    faq=[("What is a good Christmas game for 20 people?", "A team Christmas quiz is the easiest. Split into four tables of five and read ten questions per round. Christmas bingo and Who's Most Likely To also work well for 20."),
         ("What Christmas games need no equipment?", "Who's Most Likely To, Would You Rather and charades need nothing but the cards or a list of prompts."),
         ("How long should Christmas party games last?", "About 20 minutes per game, and three or four games in an evening, keeps the energy up without dragging.")],
)

BOXING = [
    ("Leftovers bake-off judging", "Everyone makes a sandwich from the leftovers and a panel scores it. Points for taste, looks and the silliest name."),
    ("Boxing Day quiz", "Ten questions on the year, ten on Christmas films and ten on the family. Mark them over a cup of tea."),
    ("Christmas film charades", "Act out a Christmas film with no talking. Works brilliantly with a mix of ages."),
    ("New toy tournament", "Turn the new board games and gadgets into a family tournament with a score sheet on the fridge."),
    ("Walk and spot", "Head out for a Boxing Day walk with a spotting sheet: a robin, a dog in a Christmas jumper, a wreath on a door."),
    ("Emoji puzzle race", "Put emoji song and film puzzles on the TV and race in teams."),
    ("Year in review", "Everyone answers the same questions about the year: best day, funniest moment, a goal for next year. Seal them away to open next Christmas."),
    ("Beat the minute", "Quick 60-second challenges using things in the house: stack the chocolates, flick the bauble, wrap a present one-handed."),
]

BOXINGDAY = dict(
    slug="boxing-day-games", cat="Christmas", date=DATE, mins=5,
    title="8 Boxing Day games for the whole family",
    seo_title="8 Boxing Day Games for the Whole Family (Easy, No Prep)",
    meta="8 easy Boxing Day games for the whole family: a Boxing Day quiz, film charades, a leftovers bake-off, a year in review and quick 60-second challenges.",
    teaser="Easy games for the lazy day after Christmas, with nothing to buy.",
    image="beat-the-minute-christmas-games-1.jpg",
    answer="Good Boxing Day games are easy and low effort: a Boxing Day quiz, Christmas film charades, a leftovers sandwich contest, a family walk with a spotting sheet, and quick 60-second challenges. Most use things you already have in the house.",
    html="<p>Boxing Day is for staying in pyjamas and eating leftovers. These games fit right in, because none of them need a trip to the shops and most need only a pen.</p>"
         + sec("games", "8 Boxing Day games", "<ol>" + "".join(f"<li><b>{n}.</b> {d}</li>" for n, d in BOXING) + "</ol>")
         + pack("beat-the-minute-christmas-games-1.jpg", "Beat the Minute Christmas Games", "36 quick-fire challenges using things you already have.", "4611838190", "beat-the-minute-christmas-games")
         + pack("christmas-emoji-games-1.jpg", "Christmas Emoji Games", "60 emoji puzzles with a TV edition for big screens.", "4611319989", "christmas-emoji-games")
         + sec("year", "Start a year in review tradition", "<p>A year in review is a lovely Boxing Day habit. Everyone fills in the same short sheet, you read them out, then seal them in an envelope to open next Christmas. Children love seeing how much they've changed.</p>")
         + pack("nye-time-capsule-1.jpg", "New Year Time Capsule", "Year-in-review dice game, About Me pages and predictions for all ages.", "4611838688", "nye-time-capsule")
         + sec("more", "More ideas", ul([
             'Still got a crowd? Try our <a href="/ideas/christmas-games-for-large-groups/">Christmas games for large groups</a>.',
             'Children bored of new toys? Set up a <a href="/ideas/christmas-scavenger-hunt-clues-for-kids/">Christmas scavenger hunt</a>.',
             'Want a quiz ready to read? Use our <a href="/ideas/christmas-quiz-questions-and-answers/">Christmas quiz questions and answers</a>.'])),
    toc=[("games", "8 games"), ("year", "Year in review"), ("more", "More ideas")],
    faq=[("What do families do on Boxing Day?", "Many families eat leftovers, go for a walk, watch films and play games together. A quiz or charades is a Boxing Day tradition in lots of UK homes."),
         ("What games can you play on Boxing Day with no prep?", "Charades, Would You Rather, a leftovers sandwich contest and 60-second challenges all need no preparation."),
         ("Is Boxing Day celebrated in the US?", "Boxing Day on 26 December is a holiday in the UK, Canada, Australia and New Zealand. It isn't a public holiday in the US, but these games work for any lazy day after Christmas.")],
)

XMAS_GUIDES2 = [BIG, BOXINGDAY]
