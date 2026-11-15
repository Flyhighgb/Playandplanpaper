"""Christmas SEO guides (added 15 Nov 2026). Each answers one real search and links to the matching Etsy listings."""

ETSY = "https://playandplanpaper.etsy.com/listing/"
DATE = "2026-11-15"


def pack(img, name, line, etsy_id, site=None):
    """Inline product card. img is a file in /img/p/. site is the product page slug, if the site has one."""
    links = f'<a href="{ETSY}{etsy_id}" rel="noopener" style="font-weight:800">See it on Etsy →</a>'
    if site:
        links = f'<a href="/p/{site}/" style="font-weight:800">See the pack →</a> · ' + links
    return (f'<div class="inline-prod"><img src="/img/p/{img}" alt="{name} printable" width="110" height="110" loading="lazy">'
            f'<div class="stack" style="gap:.3rem"><b>{name}</b><span class="muted-sm">{line}</span><span>{links}</span></div></div>')


def sec(sid, title, body):
    return f'<h2 id="{sid}">{title}</h2>{body}'


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def qa(items):
    """Joke or question list: (setup, punchline)."""
    return "<ol>" + "".join(f"<li><b>{q}</b> {a}</li>" for q, a in items) + "</ol>"


# ---------------------------------------------------------------- 1. Cracker jokes
KIDS_JOKES = [
    ("What's a snowman's favourite drink?", "Iced tea."),
    ("Why did the gingerbread man go to the doctor?", "He was feeling crumby."),
    ("What's a sheep's favourite Christmas song?", "Fleece Navidad."),
    ("Why was the Christmas tree bad at knitting?", "It kept dropping its needles."),
    ("What do reindeer hang on their trees?", "Horn-aments."),
    ("How does a snowman pay for things?", "With cold, hard cash."),
    ("Why don't sprouts ever win at hide and seek?", "You can always smell where they are."),
    ("What do you call a cat on the beach at Christmas?", "Sandy Claws."),
    ("What do snowmen do at the weekend?", "They just chill."),
    ("Why was the advent calendar so nervous?", "Its days were numbered."),
    ("How does a snowman get to school?", "By icicle."),
    ("What did the stamp say to the Christmas card?", "Stick with me and we'll go places."),
    ("Why did Rudolph get a bad school report?", "He went down in history."),
    ("What do you get if you cross a bell with a skunk?", "Jingle smells."),
    ("Why did the tinsel get told off?", "It kept hanging around."),
    ("What's Santa's favourite kind of music?", "Wrap."),
    ("What do elves learn at school?", "The elf-abet."),
    ("Why did the snowman call his dog Frost?", "Because Frost bites."),
    ("What do you call a penguin in the desert?", "Lost."),
    ("Who hides in the bakery at Christmas?", "A mince spy."),
]
ADULT_JOKES = [
    ("What do you call Santa when he stops moving?", "Santa Pause."),
    ("Why does Santa go down the chimney?", "Because it soots him."),
    ("What did the wrapping paper say to the present?", "Don't worry, I've got you covered."),
    ("Why did the turkey say no to pudding?", "It was already stuffed."),
    ("Why was Santa's little helper feeling down?", "Low elf-esteem."),
    ("What's every parent's favourite carol?", "Silent Night."),
    ("How much did Santa pay for his sleigh?", "Nothing. It was on the house."),
    ("What do you call an old snowman?", "Water."),
    ("Why don't crabs give presents?", "They're shellfish."),
    ("What did Adam say on 24 December?", "It's Christmas, Eve."),
    ("Who brings presents to baby sharks?", "Santa Jaws."),
    ("Why did the Christmas jumper need a lie down?", "It was coming apart at the seams."),
    ("What do you call a reindeer with no eyes?", "No idea."),
    ("Why did the snowman go through the bag of carrots?", "He was picking his nose."),
    ("What do you get if you eat the decorations?", "Tinsel-itis."),
    ("Why is it so cold at Christmas?", "Because it's Decemb-brrr."),
    ("What do you call a snowman with a six-pack?", "An abdominal snowman."),
    ("What do you call a broke Santa?", "Saint Nickel-less."),
    ("What do you call a reindeer wearing earmuffs?", "Anything you like. He can't hear you."),
    ("What's the best thing to put into a Christmas dinner?", "Your teeth."),
]

CRACKER = dict(
    slug="christmas-cracker-jokes", cat="Christmas", date=DATE, mins=5,
    title="40 Christmas cracker jokes for kids and adults (clean and groan-worthy)",
    seo_title="40 Christmas Cracker Jokes for Kids and Adults (Clean & Funny)",
    meta="40 clean Christmas cracker jokes for kids and adults, from snowman puns to proper groaners. Perfect for homemade crackers and the Christmas dinner table.",
    teaser="20 for the kids, 20 for the grown-ups, all safe for Grandma.",
    image="ideas-cracker-jokes.jpg",
    answer="The best Christmas cracker jokes are short puns that everyone can get, like \"What do you call Santa when he stops moving? Santa Pause.\" Below are 40 clean ones: 20 for kids and 20 groaners for adults, ready to read out or slip into homemade crackers.",
    html="<p>A cracker joke has one job: making the whole table groan at once. These are all clean, so they're safe to read out in front of children and grandparents alike.</p>"
         + sec("kids", "20 Christmas jokes for kids", qa(KIDS_JOKES))
         + pack("ideas-cracker-jokes.jpg", "Printable cracker joke cards", "24 cut-out joke cards sized for homemade crackers. Instant download.", "4605488040")
         + sec("adults", "20 Christmas cracker jokes for adults", qa(ADULT_JOKES))
         + sec("tips", "How to make your own crackers", ol([
             "Print joke cards and cut them out along the lines.",
             "Roll each joke with a paper hat and a small gift inside an empty kitchen roll tube.",
             "Wrap the tube in Christmas paper, twist both ends and tie them with ribbon.",
             "Add a cracker snap (sold in craft shops) if you want the bang."]))
         + pack("christmas-dinner-table-1.jpg", "Christmas Dinner Table Pack", "Place cards, a menu and games to go with the crackers.", "4603400048", "christmas-dinner-table"),
    toc=[("kids", "Jokes for kids"), ("adults", "Jokes for adults"), ("tips", "Make your own crackers")],
    faq=[("What is the most famous Christmas cracker joke?", "One of the best known is \"What do you call a cat on the beach at Christmas? Sandy Claws.\" It turns up in crackers every year."),
         ("Are these cracker jokes suitable for children?", "Yes. All 40 are clean and safe to read out at a family table."),
         ("How do I put jokes in homemade crackers?", "Print the jokes, cut them out, and roll one into each cracker tube with a paper hat and a small gift before you wrap and tie the ends.")],
)

# ---------------------------------------------------------------- 2. Dinner table games
TABLE_TALK = [
    "What's the best present you've ever been given?",
    "Which Christmas film could you watch every year?",
    "What would your perfect Christmas dinner have on it?",
    "What's the funniest thing that's happened on a Christmas Day?",
    "If you could spend Christmas anywhere in the world, where would it be?",
    "What's one thing you're proud of from this year?",
    "Which Christmas song would you happily never hear again?",
    "What tradition would you add to our Christmas?",
]
DINNER = dict(
    slug="christmas-dinner-table-games", cat="Christmas", date=DATE, mins=6,
    title="10 games to play at the Christmas dinner table",
    seo_title="10 Christmas Dinner Table Games (No Moving, No Mess)",
    meta="10 easy Christmas dinner table games everyone can play without leaving their seat: dinner bingo, table talk questions, cracker joke-off, quick quiz and more.",
    teaser="Keep everyone laughing between courses, without anyone leaving their seat.",
    image="ideas-dinner-bingo.jpg",
    answer="The best Christmas dinner table games need no moving and no mess: Christmas dinner bingo, table talk question cards, a cracker joke-off, Would You Rather and a quick 20-question quiz. Each takes 5 to 15 minutes and works for any age.",
    html="<p>Between the starter and the pudding there's a lot of sitting. These games keep the conversation going while everyone stays put, and none of them need more than a pen.</p>"
         + sec("g1", "1. Christmas dinner bingo", "<p>Hand out bingo cards filled with things that always happen at Christmas dinner: someone pulls a cracker too early, Grandad falls asleep, a sprout rolls off a plate. Tick them off as they happen. The first full line shouts \"Bingo!\" and wins the last roast potato.</p>")
         + pack("ideas-dinner-bingo.jpg", "Christmas Dinner Bingo", "8 different funny bingo cards for the Christmas table.", "4606207413")
         + sec("g2", "2. Table talk questions", "<p>Put a question card at each place setting and go round the table between courses. Some to start with:</p>" + ul(TABLE_TALK) + f'<p>Want them ready to print? Get our <a href="{ETSY}4606852787" rel="noopener">Christmas Table Talk cards</a>.</p>')
         + pack("christmas-dinner-table-1.jpg", "Christmas Dinner Table Pack", "Place cards, a menu and table games for the big day.", "4603400048", "christmas-dinner-table")
         + sec("g3", "3. Cracker joke-off", "<p>Everyone reads their cracker joke aloud, and the table votes for the worst groaner. The winner gets to wear the gold paper hat. Need more jokes? Try our <a href=\"/ideas/christmas-cracker-jokes/\">40 cracker jokes</a>.</p>")
         + sec("g4", "4. Christmas Would You Rather", "<p>\"Would you rather only eat sprouts or only eat Christmas pudding until New Year?\" Everyone answers and explains. It's perfect for getting quieter relatives talking.</p>")
         + sec("g5", "5. Quick Christmas quiz", "<p>Twenty questions read out between courses, scored on the back of a napkin. Use our <a href=\"/ideas/christmas-quiz-questions-and-answers/\">40 Christmas quiz questions with answers</a>.</p>")
         + sec("g6", "6. Guess the turkey time", "<p>Before dinner, everyone writes down when they think the turkey will reach the table. The closest guess wins a chocolate from the tin.</p>")
         + sec("g7", "7. Two truths and a lie", "<p>Each person says three things about their year, and one of them is made up. The table guesses the lie.</p>")
         + sec("g8", "8. Who am I?", "<p>Write a famous Christmas character on a sticky note and stick it on your neighbour's forehead. They ask yes or no questions until they guess who they are.</p>")
         + sec("g9", "9. Christmas categories", "<p>Pick a letter. Everyone writes a Christmas food, film, song and present that start with it in one minute. Score a point for each answer nobody else wrote.</p>")
         + sec("g10", "10. Compliment crackers", "<p>Everyone writes something kind about the person on their left, folds it up and puts it in a bowl. Take turns pulling one out and guessing who it's about.</p>"),
    toc=[(f"g{i}", t) for i, t in enumerate(["1. Dinner bingo", "2. Table talk questions", "3. Cracker joke-off", "4. Would You Rather", "5. Quick quiz", "6. Guess the turkey time", "7. Two truths and a lie", "8. Who am I?", "9. Christmas categories", "10. Compliment crackers"], 1)],
    faq=[("What games can you play at the Christmas dinner table?", "Games that need no moving work best: Christmas dinner bingo, table talk questions, a cracker joke-off, Would You Rather and a quick quiz."),
         ("How do you keep kids entertained at Christmas dinner?", "Christmas dinner bingo and Who am I? keep children busy, and picture-based games work for those who can't read yet."),
         ("When should you play games at Christmas dinner?", "Between courses is best, especially while the main course is being cleared and pudding is on its way.")],
)

# ---------------------------------------------------------------- 3. Office party
AWARDS = ["Most Likely to Reply All", "Biscuit Tin Guardian", "Best Mute Button Fail", "Queen or King of the Spreadsheet",
          "Most Inventive Out of Office", "Tea Round Champion"]
OFFICE = dict(
    slug="office-christmas-party-games", cat="Office", date=DATE, mins=7,
    title="12 office Christmas party games and ideas your team will actually enjoy",
    seo_title="12 Office Christmas Party Games & Ideas (Easy, Inclusive, Fun)",
    meta="12 office Christmas party games and ideas: office bingo, funny staff awards, a work quiz, Secret Santa, Find a Colleague and more. Easy to run, fun for everyone.",
    teaser="Icebreakers, awards and quizzes that work for any team size.",
    image="ideas-office-awards.jpg",
    answer="The best office Christmas party games are easy, quick and include everyone: office party bingo, funny staff awards, a work Christmas quiz, Find a Colleague and Secret Santa. Print them ahead and each one takes 10 to 20 minutes to run.",
    html="<p>A good work Christmas party gets people talking who don't normally sit together. These games and ideas suit any team, from five people in a small office to a full company do, and none of them make anyone feel awkward.</p>"
         + sec("g1", "1. Office Christmas party bingo", "<p>Cards are filled with things that happen at every work party: someone mentions the budget, the boss dances, a colleague wears the same jumper as last year. Small prizes for each full line.</p>")
         + pack("ideas-office-bingo.jpg", "Office Christmas Party Bingo", "10 different bingo cards for coworkers and staff.", "4605489294")
         + sec("g2", "2. Funny staff awards", "<p>Hand out light-hearted certificates at the end of the night. Keep them kind so everyone laughs together. Some ideas:</p>" + ul(AWARDS))
         + pack("ideas-office-awards.jpg", "Office Christmas Awards", "12 funny staff award certificates for the work party.", "4606206755")
         + sec("g3", "3. Office Christmas quiz", "<p>Mix general Christmas questions with a round about your workplace: who has been here longest, which team drinks the most tea. Play in mixed teams so departments get talking.</p>" + f'<p>Short on time? Our <a href="{ETSY}4606851485" rel="noopener">printable Office Christmas Quiz</a> is ready to go, answers included.</p>')
         + sec("g4", "4. Find a Colleague", "<p>Everyone gets a sheet of statements like \"has met a celebrity\" or \"can speak three languages\" and has to find a colleague who fits each one. The best icebreaker for big or mixed teams.</p>")
         + sec("g5", "5. Secret Santa", "<p>Draw names a few weeks before the party, set a budget, and swap gifts on the day. Our <a href=\"/ideas/secret-santa-questions-for-coworkers/\">Secret Santa questions for coworkers</a> help everyone choose a gift people actually want.</p>")
         + sec("g6", "6. The Left Right gift game", "<p>Everyone brings a small wrapped gift, then passes it left or right as a story is read out. Read our <a href=\"/ideas/left-right-christmas-game/\">Left Right game guide and free story</a>.</p>")
         + sec("g7", "7. Work This or That", "<p>Call out pairs like \"tea or coffee\", \"early start or late finish\", \"email or call\". People move to one side of the room or the other. Quick, silly and good for getting people mixing.</p>")
         + sec("g8", "8. Guess the baby photo", "<p>Collect baby photos in advance, number them on a board, and let everyone guess who's who. Ask people to opt in so nobody feels put on the spot.</p>")
         + sec("g9", "9. Desk decorating contest", "<p>Give each team a budget for tinsel and paper chains, and judge the most festive desk on party day.</p>")
         + sec("g10", "10. Christmas jumper day", "<p>Make the party a jumper day, with a small prize for the best, worst and most homemade jumper.</p>")
         + sec("g11", "11. Two truths and a lie", "<p>Each person shares three facts about themselves and the team guesses which one is the lie. It works brilliantly on video calls too.</p>")
         + sec("g12", "12. Reverse advent box", "<p>Instead of opening a door each day, the team adds one item to a box for a local food bank. Hand it over at the party.</p>")
         + pack("office-christmas-party-1.jpg", "Office Christmas Party Pack", "Icebreakers, Secret Santa and party games in one download.", "4603482987", "office-christmas-party"),
    toc=[(f"g{i}", t) for i, t in enumerate(["1. Office bingo", "2. Staff awards", "3. Office quiz", "4. Find a Colleague", "5. Secret Santa", "6. Left Right gift game", "7. Work This or That", "8. Baby photo guess", "9. Desk decorating", "10. Jumper day", "11. Two truths and a lie", "12. Reverse advent box"], 1)],
    faq=[("What are good games for an office Christmas party?", "Office party bingo, funny staff awards, a team quiz, Find a Colleague and Secret Santa are easy to run and include everyone."),
         ("How do you make an office Christmas party fun?", "Mix teams up, keep games short, and choose ones where nobody has to perform alone. Light-hearted awards at the end give everyone something to remember."),
         ("What office Christmas games work on Zoom or Teams?", "Two truths and a lie, a Christmas quiz, bingo and This or That all work well on video calls.")],
)

# ---------------------------------------------------------------- 4. Left Right
STORY = """<div class="story"><p>It was Christmas Eve, and Mrs <b>RIGHT</b> was running late. She grabbed her coat, <b>LEFT</b> the house and then remembered she had <b>LEFT</b> the turkey in the oven. She ran <b>RIGHT</b> back inside.</p>
<p>"Is everything all <b>RIGHT</b>?" called Mr <b>RIGHT</b> from upstairs. "Nearly," she said, turning <b>LEFT</b> into the kitchen. The turkey was golden, the sprouts were <b>RIGHT</b> on time, and only one roast potato was <b>LEFT</b> on the tray because the dog had helped himself.</p>
<p>They loaded the car and set off. At the end of the road they turned <b>LEFT</b>, then <b>RIGHT</b>, then <b>LEFT</b> again, until Mr <b>RIGHT</b> admitted he wasn't sure which way was <b>RIGHT</b>. "Turn <b>LEFT</b> at the big tree," said Mrs <b>RIGHT</b>. "No, the other <b>LEFT</b>!"</p>
<p>At last they arrived. Grandma was waiting <b>RIGHT</b> by the door with mince pies. "You're <b>RIGHT</b> on time," she smiled. "There's nobody <b>LEFT</b> to come but you."</p>
<p>After dinner everyone sat down to open presents. Grandma looked to her <b>LEFT</b>, then to her <b>RIGHT</b>, and said, "Well, I hope you've all got the <b>RIGHT</b> present. Because the game is over, and whatever you're holding now is yours to keep!"</p></div>"""

LEFTRIGHT = dict(
    slug="left-right-christmas-game", cat="Christmas", date=DATE, mins=5,
    title="How to play the Left Right Christmas game (with a free short story)",
    seo_title="Left Right Christmas Game: How to Play + Free Short Story",
    meta="How to play the Left Right Christmas gift exchange game, step by step, plus a free short Left Right story to read aloud. Works for families and office parties.",
    teaser="The gift-passing game everyone can play, plus a story you can read tonight.",
    image="ideas-left-right.jpg",
    answer="To play the Left Right Christmas game, everyone sits in a circle holding a wrapped gift. One person reads a story aloud, and every time they say \"left\" or \"right\", everyone passes their gift that way. When the story ends, you keep the gift you're holding.",
    html="<p>The Left Right game is the easiest gift swap there is. There's no stealing and no arguing, and it takes about five minutes. It works for a family Christmas, a classroom or the office party.</p>"
         + sec("how", "How to play", ol([
             "Everyone brings one small wrapped gift. Agree a budget first, such as £5 or $10.",
             "Sit in a circle, each holding a gift.",
             "One person reads the story aloud, slowly.",
             "Every time the reader says LEFT, pass your gift to the left. Every time they say RIGHT, pass it to the right.",
             "When the story ends, open the gift you're holding."]))
         + sec("story", "Free short Left Right Christmas story", "<p>Read this aloud and pause a moment on each LEFT and RIGHT so people can pass.</p>" + STORY)
         + pack("ideas-left-right.jpg", "Left Right Christmas Game printable", "Longer, funnier stories ready to print and read aloud.", "4605467991")
         + sec("tips", "Tips for a smooth game", ul([
             "Read slowly. The faster you read, the more gifts end up on the floor.",
             "For young children, use a soft toy or a bag of sweets in place of breakable gifts.",
             "For big groups, split into two circles with one reader each.",
             "Want more gift swap ideas? See our <a href=\"/ideas/office-christmas-party-games/\">office Christmas party games</a>."])),
    toc=[("how", "How to play"), ("story", "Free short story"), ("tips", "Tips")],
    faq=[("How many people do you need for the Left Right game?", "It works with as few as 4 people and as many as 30. Above that, split into two circles."),
         ("How long does the Left Right game take?", "About 5 minutes per story, depending on how slowly it's read."),
         ("What gifts work for the Left Right game?", "Small, similar-value gifts work best: chocolates, socks, candles or a novelty mug. Set a budget so everyone brings something similar.")],
)

# ---------------------------------------------------------------- 5. Secret Santa questions
SS_Q = [
    "What's your go-to hot drink, and how do you take it?",
    "Sweet or savoury snacks?",
    "What's your favourite chocolate bar?",
    "Do you have any allergies or foods you avoid?",
    "What do you do to relax at the weekend?",
    "Name a hobby you'd like to try.",
    "Favourite colour?",
    "Candles: love them or leave them?",
    "Are you a book, film or podcast person?",
    "What's your favourite film genre?",
    "Is there an author or series you love?",
    "Desk plant: yes, no, or one you can't kill?",
    "What's on your desk that you couldn't work without?",
    "Mugs: do you have enough already?",
    "Cosy socks or fun socks?",
    "Do you have a favourite sports team?",
    "Coffee shop order?",
    "Any pets? What are their names?",
    "Gin, wine, beer, or alcohol-free?",
    "What's a small thing that always makes your day better?",
    "Are you more of a gadget person or a stationery person?",
    "Would you rather get something useful or something funny?",
    "Is there anything you definitely don't want?",
    "If you won a free afternoon off, what would you do with it?",
    "What's your favourite season of the year?",
]
SECRETSANTA = dict(
    slug="secret-santa-questions-for-coworkers", cat="Office", date=DATE, mins=5,
    title="25 Secret Santa questions to ask your coworkers",
    seo_title="25 Secret Santa Questions to Ask Coworkers (Free List)",
    meta="25 Secret Santa questions to ask coworkers, plus how to run a work Secret Santa: budgets, sign-up sheets, wish lists and gift ideas that people actually want.",
    teaser="Ask these and nobody gets a sixth mug this year.",
    image="ideas-secret-santa.jpg",
    answer="Good Secret Santa questions cover favourite snacks and drinks, hobbies, allergies and anything someone definitely doesn't want. Ask 5 to 10 questions on a sign-up sheet, set a budget, and share the answers only with each person's Secret Santa.",
    html="<p>Most disappointing Secret Santa gifts happen because the giver knew nothing about the person. A short questionnaire fixes that. Here are 25 questions to choose from, and a simple way to run the whole thing.</p>"
         + sec("questions", "25 Secret Santa questions", ol(SS_Q))
         + pack("secret-santa-kit-1.jpg", "Secret Santa Kit", "Sign-up sheets, question cards, gift tags and a reveal game.", "4611106575", "secret-santa-kit")
         + sec("how", "How to run a work Secret Santa", ol([
             "Set a budget everyone is comfortable with. £10 to £15 or $15 to $20 is typical.",
             "Hand out a sign-up sheet with your chosen questions and a deadline.",
             "Draw names in secret. A hat works, or one person can assign them.",
             "Give each Santa only their person's answers.",
             "Pick a swap day, ideally at the Christmas party, and add a guessing game for the reveal."]))
         + pack("ideas-secret-santa.jpg", "Secret Santa Sign Up and Wish List Cards", "Printable sign-up sheet and wish list cards for office or family.", "4605470813")
         + sec("ideas", "Gift ideas that rarely miss", ul([
             "Their favourite chocolate or snack, plus a nice mug only if they said they want one",
             "A book by an author they named",
             "A plant they can't kill, like a succulent",
             "Good stationery for the gadget-shy",
             "A coffee shop gift card for their usual order"])),
    toc=[("questions", "25 questions"), ("how", "How to run it"), ("ideas", "Gift ideas")],
    faq=[("What should I ask for Secret Santa?", "Ask about favourite snacks and drinks, hobbies, allergies, colours and anything they don't want. Five to ten questions is plenty."),
         ("How much should you spend on a work Secret Santa?", "Most workplaces set £10 to £15 or $15 to $20. Agree the amount up front so nobody overspends."),
         ("Is Secret Santa anonymous?", "Usually yes, until the swap. Some teams add a guessing game where everyone tries to work out who their Santa was.")],
)

# ---------------------------------------------------------------- 6. Christmas Eve box
EVEBOX = dict(
    slug="what-to-put-in-a-christmas-eve-box", cat="Christmas", date=DATE, mins=6,
    title="What to put in a Christmas Eve box: ideas for kids, teens and adults",
    seo_title="What to Put in a Christmas Eve Box (Ideas for Kids, Teens & Adults)",
    meta="What to put in a Christmas Eve box: new pyjamas, hot chocolate, a film, a book, a letter from Santa and reindeer food, with ideas for toddlers, kids, teens and adults.",
    teaser="Pyjamas, hot chocolate and a little magic for the night before.",
    image="christmas-eve-box-kit-1.jpg",
    answer="A classic Christmas Eve box holds new pyjamas, hot chocolate and a mug, a Christmas film or book, a snack for Santa, reindeer food and a letter from Santa. Add a small activity for kids, or swap in grown-up treats for adults.",
    html="<p>A Christmas Eve box is a small box opened on the night before Christmas. It sets up a cosy evening and gets everyone in pyjamas and in bed at a sensible time. Here's what to put in one.</p>"
         + sec("classic", "The classic Christmas Eve box", ul([
             "New Christmas pyjamas",
             "Hot chocolate sachets and marshmallows",
             "A Christmas film to watch together",
             "A Christmas book for bedtime",
             "A plate tag and treat for Santa, and a carrot for the reindeer",
             "Reindeer food: oats mixed with a little birdseed. Leave out glitter, which harms wildlife",
             "A letter or a \"nice list\" certificate from Santa",
             "Cosy socks"]))
         + pack("christmas-eve-box-kit-1.jpg", "Christmas Eve Box Kit", "Printable box labels, Santa letter, nice list certificate, plate tags and activities.", "4611107319", "christmas-eve-box-kit")
         + sec("toddlers", "For toddlers", ul(["A soft toy", "A board book", "A bath toy for the Christmas Eve bath", "Bedtime story about Santa"]))
         + sec("kids", "For kids aged 4 to 10", ul(["Colouring pages or a puzzle", "A torch for spotting Santa's sleigh", "A countdown sleep sheet", "A small game for the evening"]))
         + sec("teens", "For teens", ul(["Fancy hot chocolate or a face mask", "A new book or magazine", "Fun socks", "A voucher for the film they choose"]))
         + sec("adults", "For grown-ups", ul(["A good candle", "Posh chocolates", "A mini bottle of something festive", "A crossword or puzzle book for the quiet hour"]))
         + sec("tips", "Tips for putting one together", ul([
             "Any sturdy box works. Wrap the lid separately so it can be opened easily.",
             "Print a label with each child's name on it.",
             "Set a small budget. The magic is in the evening, not the spend."])),
    toc=[("classic", "The classic box"), ("toddlers", "Toddlers"), ("kids", "Kids 4 to 10"), ("teens", "Teens"), ("adults", "Grown-ups"), ("tips", "Tips")],
    faq=[("What is a Christmas Eve box?", "A small box of treats opened on Christmas Eve, usually with new pyjamas, hot chocolate and a film or book, to start a cosy evening before the big day."),
         ("When do you open a Christmas Eve box?", "In the early evening of 24 December, before bath and bedtime."),
         ("What do you put in an adult Christmas Eve box?", "Pyjamas or socks, a candle, posh chocolates, a mini drink and a puzzle book all work well.")],
)

# ---------------------------------------------------------------- 7. Quiz
ROUNDS = [
    ("films", "Round 1: Christmas films and TV", [
        ("In Home Alone, which city do the McCallisters fly to?", "Paris"),
        ("What is the name of the Grinch's dog?", "Max"),
        ("In Elf, what does Buddy pour on his spaghetti?", "Maple syrup"),
        ("What is the name of the snowman in Frozen?", "Olaf"),
        ("In It's a Wonderful Life, what is the name of George Bailey's guardian angel?", "Clarence"),
        ("In The Muppet Christmas Carol, who plays Bob Cratchit?", "Kermit the Frog"),
        ("In The Polar Express, what is the first gift of Christmas?", "A sleigh bell"),
        ("What colour is the Grinch?", "Green"),
        ("In Love Actually, what is the Prime Minister's first name?", "David"),
        ("Which Christmas film features the line \"Keep the change, ya filthy animal\"?", "Home Alone"),
    ]),
    ("music", "Round 2: Christmas music", [
        ("Who sang All I Want for Christmas Is You in 1994?", "Mariah Carey"),
        ("Which band sang Fairytale of New York with Kirsty MacColl?", "The Pogues"),
        ("What was Wham!'s Christmas hit?", "Last Christmas"),
        ("In The Twelve Days of Christmas, how many geese are a-laying?", "Six"),
        ("What did my true love give to me on the first day of Christmas?", "A partridge in a pear tree"),
        ("Which Slade singer shouts \"It's Christmas!\"?", "Noddy Holder"),
        ("Who sang Rockin' Around the Christmas Tree in 1958?", "Brenda Lee"),
        ("In Jingle Bells, what kind of sleigh is it?", "A one-horse open sleigh"),
        ("Which charity single from 1984 asked \"Do They Know It's Christmas?\"", "Band Aid"),
        ("Which reindeer has a very shiny nose?", "Rudolph"),
    ]),
    ("food", "Round 3: Food and traditions", [
        ("What is traditionally poured over a Christmas pudding and set alight?", "Brandy"),
        ("What is the German name for mulled wine?", "Glühwein"),
        ("Brussels sprouts are named after a city in which country?", "Belgium"),
        ("What is the name of the Italian Christmas bread with dried fruit?", "Panettone"),
        ("What were the three gifts of the Wise Men?", "Gold, frankincense and myrrh"),
        ("What is the date of Boxing Day?", "26 December"),
        ("Who sent the first commercial Christmas card in 1843?", "Sir Henry Cole"),
        ("Which country gave us the bûche de Noël, or yule log cake?", "France"),
        ("Which royal helped make Christmas trees popular in Britain?", "Prince Albert"),
        ("What do people traditionally kiss under?", "Mistletoe"),
    ]),
    ("general", "Round 4: General Christmas knowledge", [
        ("Who wrote A Christmas Carol?", "Charles Dickens"),
        ("What is the name of Scrooge's late business partner?", "Jacob Marley"),
        ("How many reindeer pull Santa's sleigh, including Rudolph?", "Nine"),
        ("Which of Santa's reindeer is named after the German word for thunder?", "Donner"),
        ("In which country is Rovaniemi, the official hometown of Santa Claus?", "Finland"),
        ("How many points does a snowflake usually have?", "Six"),
        ("Which London square gets a Christmas tree from Norway every year?", "Trafalgar Square"),
        ("Noël is the French word for what?", "Christmas"),
        ("What colour are mistletoe berries?", "White"),
        ("In which year was the Queen's Christmas message first shown on television?", "1957"),
    ]),
]


def quiz_html():
    out = ""
    for sid, title, qs in ROUNDS:
        out += sec(sid, title, "<ol>" + "".join(f"<li>{q}<br><b>Answer:</b> {a}</li>" for q, a in qs) + "</ol>")
        if sid == "music":
            out += pack("ideas-table-quiz.jpg", "Christmas Table Quiz", "20 questions with answers, printed and ready for the dinner table.", "4605488810")
    return out


QUIZ = dict(
    slug="christmas-quiz-questions-and-answers", cat="Christmas", date=DATE, mins=8,
    title="40 Christmas quiz questions and answers for families",
    seo_title="40 Christmas Quiz Questions and Answers (Family Friendly, 2026)",
    meta="40 Christmas quiz questions with answers in four rounds: films and TV, music, food and traditions, and general knowledge. Family friendly and ready to read out.",
    teaser="Four rounds of ten, answers included, ready to read out tonight.",
    image="christmas-family-quiz-1.jpg",
    answer="Here are 40 family-friendly Christmas quiz questions with answers, in four rounds of ten: films and TV, music, food and traditions, and general knowledge. Play in teams, read one round between courses, and give a point per correct answer.",
    html="<p>A Christmas quiz fills an hour, gets every generation involved and needs nothing but paper and pens. Split into teams, pick a quizmaster, and give a point for each correct answer. The answers sit under each question, so cover them up if you're reading from a screen.</p>"
         + quiz_html()
         + pack("christmas-family-quiz-1.jpg", "Christmas Family Quiz", "A full printable quiz night with answer sheets and a scoreboard.", "4602873720", "christmas-family-quiz"),
    toc=[(sid, title.split(": ")[1]) for sid, title, _ in ROUNDS],
    faq=[("How many questions should a Christmas quiz have?", "Around 40 questions in four rounds of ten fills about an hour, which suits most families and parties."),
         ("What are easy Christmas quiz questions for kids?", "Questions like \"What is the name of the snowman in Frozen?\" or \"Which reindeer has a shiny nose?\" are easy wins for children."),
         ("How do you run a Christmas quiz at home?", "Split into teams, give each an answer sheet, read one round at a time, then swap sheets to mark them.")],
)

# ---------------------------------------------------------------- 8. Scavenger hunt clues
CLUES = [
    ("Fridge", "I'm cold inside but full of treats,<br>with milk and cheese and things to eat."),
    ("Christmas tree", "I'm covered in baubles from top to toe,<br>look under my branches, what's there? Ho ho!"),
    ("Bath", "You fill me with bubbles and climb right in,<br>look inside me, then you'll win."),
    ("Washing machine", "I spin and I swish and I wash all your socks,<br>open my door and you'll find the next box."),
    ("Pillow", "At night you rest your sleepy head<br>on me. I'm soft and on your bed."),
    ("Shoe", "You put your feet in me each day,<br>check inside me straight away."),
    ("Bookshelf", "I'm full of stories, old and new,<br>look between my books for your next clue."),
    ("Sofa", "Sit on me to watch TV,<br>check under my cushions, what do you see?"),
    ("Front door mat", "Wipe your feet before you come in,<br>lift me up and look within."),
    ("Toy box", "I hold your toys when you're done playing,<br>look inside me, no delaying!"),
    ("Sock drawer", "I'm full of pairs, but some have gone,<br>open me up and carry on."),
    ("Biscuit tin", "I'm round and full of crunchy treats,<br>the next clue's hiding with the sweets."),
    ("Mirror", "Look at me and who do you see?<br>Someone clever, as clever as can be!"),
    ("Stairs", "Up and down you climb each day,<br>check my bottom step, then on your way."),
    ("Plant pot", "I hold a plant that's green and tall,<br>look behind me, by the wall."),
]
HUNT = dict(
    slug="christmas-scavenger-hunt-clues-for-kids", cat="Kids", date=DATE, mins=6,
    title="15 Christmas scavenger hunt clues for kids (rhyming, indoor)",
    seo_title="15 Christmas Scavenger Hunt Clues for Kids (Rhyming, Indoors)",
    meta="15 rhyming Christmas scavenger hunt clues for kids to hide around the house, with the answer for each one, plus tips for running an indoor Christmas treasure hunt.",
    teaser="Rhyming clues to hide around the house, with answers for the grown-up.",
    image="ideas-hunt-house.jpg",
    answer="A Christmas scavenger hunt for kids uses rhyming clues hidden around the house, each one leading to the next, with a treat at the end. Below are 15 indoor clues with their hiding places. Pick 8 to 12 for a hunt that takes about 20 minutes.",
    html="<p>A scavenger hunt is the best way to burn off some Christmas energy indoors. Each clue tells children where to find the next one. Start them with the first clue, and hide each of the others in the place the clue before it describes.</p>"
         + sec("clues", "15 rhyming Christmas clues (with answers)", "<ol>" + "".join(f"<li>{c}<br><b>Hide it in or near:</b> {p}</li>" for p, c in CLUES) + "</ol>")
         + pack("ideas-hunt-house.jpg", "Christmas House Scavenger Hunt", "12 printable rhyming clues to hide around the home.", "4606225252")
         + sec("how", "How to set up the hunt", ol([
             "Choose 8 to 12 clues and decide the order.",
             "Hide each clue at the place the clue before it describes. The first clue goes straight into the children's hands.",
             "Put a small treat or present at the final hiding place.",
             "For mixed ages, pair older children with younger ones so everyone can read the clues."]))
         + pack("christmas-scavenger-hunt-1.jpg", "Christmas Scavenger Hunt", "A ready-to-print clue trail with a festive finish.", "4602874126", "christmas-scavenger-hunt")
         + sec("tips", "Tips", ul([
             "Avoid hiding clues near the oven, fire or anything hot.",
             "Take a photo of each hiding place so you remember where they are.",
             "Want more ideas? See our <a href=\"/ideas/christmas-games-for-kids/\">Christmas games for kids</a>."])),
    toc=[("clues", "15 clues"), ("how", "How to set it up"), ("tips", "Tips")],
    faq=[("What age is a Christmas scavenger hunt for?", "Rhyming clue hunts suit children from about 5 to 11. Younger children can play with a grown-up reading the clues."),
         ("How many clues should a scavenger hunt have?", "Eight to twelve clues takes about 20 minutes, which is perfect for most children."),
         ("What do you put at the end of a Christmas scavenger hunt?", "A small treat, a chocolate coin, a Christmas Eve box or a present to open early all make a great finish.")],
)

XMAS_GUIDES = [CRACKER, QUIZ, OFFICE, DINNER, LEFTRIGHT, SECRETSANTA, EVEBOX, HUNT]
