import tkinter as tk
import random
from PIL import Image, ImageTk
import sqlite3

# Function to analyze mood and generate book recommendations
def analyze_mood():
    mood = 0
    for var in mood_vars:
        if var.get():
            mood += 1

    if mood >= 3:
        mood_label.config(text="Mood: Sad")
        recommended_books.config(text="Recommended Books: Happy Books")
    elif mood == 2:
        mood_label.config(text="Mood: Depressed")
        recommended_books.config(text="Recommended Books: Books to boost your confidence")
    else:
        mood_label.config(text="Mood: Happy")
        recommended_books.config(text="Recommended Books: Inspiration Books")

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Function to update the welcome message
def update_welcome_message():
    name = username_entry.get()
    if name:
        welcome_message = "Welcome, " + name
        save_username(name)  # Save username to the database
    else:
        welcome_message = "Welcome, User"
    welcome_label.config(text=welcome_message, font=("Helvetica", 25))
    show_frame(welcome_frame)

# Function to save username to the database
def save_username(username):
    conn = sqlite3.connect("usernames.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect("usernames.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Function to save username to the database
def save_username(username):
    conn = sqlite3.connect("usernames.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    conn.commit()
    #conn.close()
    print(get_users())

# Create the main application window
root = tk.Tk()
root.title("MOODPAGE MASTER")
root.geometry("400x400")

# Create frames
username_frame = tk.Frame(root)
welcome_frame = tk.Frame(root)
questions_frame = tk.Frame(root)
books_frame = tk.Frame(root)

for frame in (username_frame, welcome_frame, questions_frame, books_frame):
    frame.grid(row=0, column=0,sticky="nsew")

# Username Frame
img = Image.open('assets/book1.png')
img = img.resize((395, 395), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
image_label = tk.Label(username_frame, image=photo)
image_label.grid(row=1,column=0,pady=10)
username_label = tk.Label(username_frame, text = "Enter your username:",font=("Helvetica", 18))
#username_label.pack(pady=10)
username_label.place(x=80,y=100)
username_entry = tk.Entry(username_frame)
#username_entry.pack(pady=20)
username_entry.place(x=80,y=150)
next_button = tk.Button(username_frame, text="Next", font=("Helvetica", 18), command=update_welcome_message)
#next_button.pack()
next_button.place(x=80,y=200)

# Database part
save_username("")  # To create the table if it doesn't exist initially

# Welcome Frame
welcome_label = tk.Label(welcome_frame, text="", pady=10)
welcome_label.pack()
update_welcome_message()  # Initial update

next_button = tk.Button(welcome_frame, text="Next",font=("Helvetica", 12), command=lambda: show_frame(questions_frame))
next_button.pack()
back_button = tk.Button(welcome_frame, text="Back", command=lambda: show_frame(username_frame))
back_button.pack()

# Questions Frame
questions_label = tk.Label(questions_frame, text="Answer the following questions to analyze your mood:")
questions_label.pack(pady=10)
mood_vars = [tk.BooleanVar() for _ in range(4)]
questions = [
    "Do you often feel sad?",
    "Do you find joy in everyday activities?",
    "Do you feel hopeless or worthless?",
    "Do you feel guilty about something?"
]

random.shuffle(questions)  # Randomize the order of questions

for i, question in enumerate(questions):
    check_button = tk.Checkbutton(questions_frame, text=question, variable=mood_vars[i])
    check_button.pack()

analyze_button = tk.Button(questions_frame, text="Analyze Mood", command=analyze_mood)
analyze_button.pack()
back_button = tk.Button(questions_frame, text="Back", command=lambda: show_frame(welcome_frame))
back_button.pack()

mood_label = tk.Label(questions_frame, text="", pady=10)
mood_label.pack()
recommended_books = tk.Label(questions_frame, text="", wraplength=300, justify="left")
recommended_books.pack()

# Books Frame
books_label = tk.Label(books_frame, text="Books Recommendations:", pady=10)
books_label.pack()

books = {
    "Happy Books": ["Little Women", "Suppandi Tales", "Tinkle comics","Anne of Green Gables by L.M. Montgomery - $10.99", "The Secret Garden by Frances Hodgson Burnett - $9.99","Pride and Prejudice by Jane Austen - $12.99"
"Charlie and the Chocolate Factory by Roald Dahl - $8.99",
"Matilda by Roald Dahl - $8.99",
 "The Alchemist by Paulo Coelho - $11.99",
 "To Kill a Mockingbird by Harper Lee - $9.99",
 "The Catcher in the Rye by J.D. Salinger - $10.99",
 "The Little Prince by Antoine de Saint-Exupéry - $7.99",
 "A Man Called Ove by Fredrik Backman - $11.99",
 "Where the Crawdads Sing by Delia Owens - $13.99",
"Eleanor Oliphant is Completely Fine by Gail Honeyman - $12.99",
"The Guernsey Literary and Potato Peel Pie Society by Mary Ann Shaffer and Annie Barrows - $10.99",
 "The Night Circus by Erin Morgenstern - $11.99",
 "The Book Thief by Markus Zusak - $10.99"],
    "Inspiration Books": ["Wings of fire", "Me before you", "Power of your sub-concious mind","The Power of Now by Eckhart Tolle - $13.99",
"The Four Agreements by Don Miguel Ruiz - $11.99",
"Becoming by Michelle Obama - $14.99",
"Educated by Tara Westover - $12.99",
 "Man's Search for Meaning by Viktor E. Frankl - $11.99",
"The Sun Does Shine by Anthony Ray Hinton - $13.99",
"Born a Crime by Trevor Noah - $12.99",
"Option B by Sheryl Sandberg and Adam Grant - $13.99",
"Daring Greatly by Brené Brown - $11.99",
"Untamed by Glennon Doyle - $14.99",
"Big Magic by Elizabeth Gilbert - $12.99",
"Atomic Habits by James Clear - $13.99",
"The Subtle Art of Not Giving a F*ck by Mark Manson - $11.99",
"Year of Yes by Shonda Rhimes - $12.99",
"You Are a Badass by Jen Sincero - $10.99"],
    "Confident Books": ["Think straight", "What confident women do", "The confidence code","Lean In by Sheryl Sandberg - $12.99","Presence by Amy Cuddy - $11.99","Grit by Angela Duckworth - $13.99","Mindset by Carol S. Dweck - $11.99","The 5 Second Rule by Mel Robbins - $12.99",
"The Power of Habit by Charles Duhigg - $13.99", "Quiet by Susan Cain - $11.99","Braving the Wilderness by Brené Brown - $12.99", "Girl, Wash Your Face by Rachel Hollis - $10.99","The Confidence Gap by Russ Harris - $11.99","Start with Why by Simon Sinek - $13.99","High Performance Habits by Brendon Burchard - $14.99","The 7 Habits of Highly Effective People by Stephen R. Covey - $12.99","You Are a Badass at Making Money by Jen Sincero - $10.99","The Magic of Thinking Big by David J. Schwartz - $11.99"]
}
for mood, book_list in books.items():
    tk.Label(books_frame, text=mood, font=("Helvetica", 14, "bold")).pack()
    for book in book_list:
        tk.Label(books_frame, text=book).pack()

# Function to generate a random book recommendation
def generate_book():
    if mood_label.cget("text") == "Mood: Happy":
        recommended_books.config(text="Recommended Book:" + random.choice(books["Happy Books"]))
    elif mood_label.cget("text") == "Mood: Depressed":
        recommended_books.config(text="Recommended Book:" + random.choice(books["Inspiration Books"]))
    else:
        recommended_books.config(text="Recommended Book:" +  random.choice(books["Confident Books"]))

# Generate Book Button
generate_book_button = tk.Button(questions_frame, text="Generate Book",font=("Helvetica", 12), command=generate_book)
generate_book_button.pack()

# Show the initial frame
show_frame(username_frame)
root.mainloop()
