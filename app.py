from flask import Flask, render_template_string

app = Flask(__name__)

notes = [
    {"class": "Class 11", "subject": "Physics",
     "chapter": "Units and Measurements", "file": "#"},
    {"class": "Class 11", "subject": "Chemistry",
     "chapter": "Structure of Atom", "file": "#"},
    {"class": "Class 11", "subject": "Biology",
     "chapter": "The Living World", "file": "#"},
    {"class": "Class 12", "subject": "Chemistry",
     "chapter": "Solutions", "file": "#"},
    {"class": "Class 10", "subject": "Mathematics",
     "chapter": "Real Numbers", "file": "#"},
    {"class": "Class 9", "subject": "Science",
     "chapter": "Matter in Our Surroundings", "file": "#"}
]

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Notivexa | Learn Smart</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f5f6ff;
    color: #25254a;
}

header {
    background: #29245c;
    color: white;
    padding: 20px;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 30px;
}

nav {
    background: white;
    padding: 15px;
    text-align: center;
}

nav a {
    text-decoration: none;
    color: #29245c;
    margin: 10px;
    font-weight: bold;
}

.hero {
    text-align: center;
    padding: 55px 15px;
    background: linear-gradient(120deg, #39318a, #8175e8);
    color: white;
}

.hero h2 {
    font-size: 32px;
}

.search {
    margin: 20px auto;
    padding: 13px;
    width: 85%;
    max-width: 450px;
    border: none;
    border-radius: 25px;
}

.container {
    padding: 25px;
    max-width: 1100px;
    margin: auto;
}

.cards {
    display: grid;
    grid-template-columns:
    repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    box-shadow: 0 3px 12px #ddd;
}

.card h3 {
    color: #5146a5;
}

.card a {
    display: inline-block;
    background: #5146a5;
    color: white;
    padding: 10px 18px;
    border-radius: 8px;
    text-decoration: none;
}

footer {
    background: #29245c;
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 40px;
}
</style>
</head>

<body>

<header>
    <h1>NOTIVEXA 📚</h1>
    <p>Learn Smart, Grow Faster!</p>
</header>

<nav>
    <a href="/">Home</a>
    <a href="#classes">Classes</a>
    <a href="#notes">Notes</a>
    <a href="#about">About</a>
</nav>

<section class="hero">
    <h2>Your Learning Journey Starts Here!</h2>
    <p>Explore notes, learn concepts and prepare for success.</p>
    <input class="search" id="search"
    onkeyup="searchNotes()"
    placeholder="Search your subject or chapter...">
</section>

<div class="container" id="classes">
    <h2>Explore Your Classes</h2>
    <div class="cards">
        <div class="card"><h3>📘 Class 9</h3>
        <p>Study materials and notes.</p></div>

        <div class="card"><h3>📗 Class 10</h3>
        <p>Board exam preparation.</p></div>

        <div class="card"><h3>📙 Class 11</h3>
        <p>NCERT notes and important questions.</p></div>

        <div class="card"><h3>📕 Class 12</h3>
        <p>Revision and exam materials.</p></div>
    </div>
</div>

<div class="container" id="notes">
    <h2>Latest Study Notes</h2>
    <div class="cards" id="noteCards">

    {% for note in notes %}
    <div class="card note">
        <h3>{{ note.subject }}</h3>
        <p>{{ note.class }}</p>
        <p>{{ note.chapter }}</p>
        <a href="{{ note.file }}">View PDF</a>
    </div>
    {% endfor %}

    </div>
</div>

<div class="container" id="about">
    <h2>About Notivexa</h2>
    <p>
    Notivexa is a student-friendly educational platform
    for Classes 9–12. Our goal is to make learning simple,
    accessible and enjoyable through useful study resources.
    </p>
</div>

<footer>
    <h3>NOTIVEXA</h3>
    <p>Your Knowledge, Your Future!</p>
    <p>© 2026 Notivexa. All rights reserved.</p>
</footer>

<script>
function searchNotes() {
    let input = document.getElementById("search")
        .value.toLowerCase();

    let cards = document.querySelectorAll(".note");

    cards.forEach(card => {
        card.style.display =
            card.innerText.toLowerCase().includes(input)
            ? "block" : "none";
    });
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, notes=notes)

if __name__ == "__main__":
    app.run(debug=True)