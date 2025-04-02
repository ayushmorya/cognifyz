import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("450x550")  # Slightly larger window
        self.root.configure(bg="#ffffff")  # White background for canvas

        # Game variables
        self.target_number = None
        self.attempts = 0
        self.max_attempts = 0
        self.max_number = 0
        self.remaining_attempts = 0
        self.difficulty = None
        self.confetti_labels = []  # For confetti effect

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas for the gradient background
        self.canvas = tk.Canvas(self.root, width=450, height=550, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Simulate a gradient background (light yellow to light pink)
        for i in range(550):
            color = f"#{int(255 - i*0.2):02x}{int(255 - i*0.1):02x}{int(200 + i*0.1):02x}"  # Gradient from yellow to pink
            self.canvas.create_line(0, i, 450, i, fill=color)

        # Title
        self.title_label = tk.Label(
            self.root, text="🎡 Carnival Number Guessing Game 🎡", 
            font=("Comic Sans MS", 18, "bold"), bg="#fffacd", fg="#ff4500",  # LemonChiffon background, orange text
            borderwidth=2, relief="ridge"
        )
        self.canvas.create_window(225, 40, window=self.title_label)

        # Difficulty selection
        self.difficulty_label = tk.Label(
            self.root, text="🎈 Pick Your Challenge 🎈", 
            font=("Comic Sans MS", 12), bg="#fffacd", fg="#ff69b4"  # Hot pink text
        )
        self.canvas.create_window(225, 100, window=self.difficulty_label)

        self.difficulty_var = tk.StringVar(value="Easy")
        self.difficulty_menu = ttk.Combobox(
            self.root, textvariable=self.difficulty_var, 
            values=["Easy (1-50, 20 attempts)", "Medium (1-100, 15 attempts)", "Hard (1-200, 10 attempts)"],
            state="readonly", width=25, font=("Comic Sans MS", 10)
        )
        self.canvas.create_window(225, 140, window=self.difficulty_menu)

        # Start button with hover effect
        self.start_button = tk.Button(
            self.root, text="🎉 Start the Fun! 🎉", command=self.start_game, 
            font=("Comic Sans MS", 12, "bold"), bg="#ff69b4", fg="white",  # Hot pink button
            activebackground="#ff1493", activeforeground="white", borderwidth=2, relief="raised"
        )
        self.canvas.create_window(225, 190, window=self.start_button)

        # Guess entry and button
        self.guess_label = tk.Label(
            self.root, text="🎯 Enter Your Guess 🎯", 
            font=("Comic Sans MS", 12), bg="#fffacd", fg="#ff69b4"
        )
        self.guess_entry = tk.Entry(self.root, font=("Comic Sans MS", 12), width=10, bg="#e6e6fa")  # Lavender background
        self.guess_button = tk.Button(
            self.root, text="Guess! 🎈", command=self.make_guess, 
            font=("Comic Sans MS", 12, "bold"), bg="#1e90ff", fg="white",  # Dodger blue button
            activebackground="#00b7eb", activeforeground="white", borderwidth=2, relief="raised"
        )

        # Feedback label
        self.feedback_label = tk.Label(
            self.root, text="", font=("Comic Sans MS", 12), bg="#fffacd", fg="#ff4500", wraplength=400
        )

        # Attempts label
        self.attempts_label = tk.Label(
            self.root, text="", font=("Comic Sans MS", 12), bg="#fffacd", fg="#ff69b4"
        )

        # Play again button
        self.play_again_button = tk.Button(
            self.root, text="🎠 Play Again! 🎠", command=self.reset_game, 
            font=("Comic Sans MS", 12, "bold"), bg="#32cd32", fg="white",  # Lime green button
            activebackground="#228b22", activeforeground="white", borderwidth=2, relief="raised"
        )

    def start_game(self):
        # Get difficulty settings
        difficulty = self.difficulty_var.get()
        if "Easy" in difficulty:
            self.max_number, self.max_attempts = 50, 20
            self.difficulty = "Easy"
        elif "Medium" in difficulty:
            self.max_number, self.max_attempts = 100, 15
            self.difficulty = "Medium"
        else:
            self.max_number, self.max_attempts = 200, 10
            self.difficulty = "Hard"

        # Initialize game
        self.target_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.remaining_attempts = self.max_attempts

        # UI
        self.feedback_label.config(
            text=f"🎪 I'm thinking of a number between 1 and {self.max_number}!\nLet's play on {self.difficulty} mode! 🎪"
        )
        self.attempts_label.config(text=f"🎟️ Attempts left: {self.remaining_attempts}")

        # Hide initial elements and show game elements
        self.canvas.delete("all")
        self.create_gradient()  # Redraw gradient
        self.canvas.create_window(225, 40, window=self.title_label)
        self.canvas.create_window(225, 100, window=self.feedback_label)
        self.canvas.create_window(225, 160, window=self.attempts_label)
        self.canvas.create_window(225, 220, window=self.guess_label)
        self.canvas.create_window(225, 260, window=self.guess_entry)
        self.canvas.create_window(225, 310, window=self.guess_button)
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def create_gradient(self):
        for i in range(550):
            color = f"#{int(255 - i*0.2):02x}{int(255 - i*0.1):02x}{int(200 + i*0.1):02x}"
            self.canvas.create_line(0, i, 450, i, fill=color)

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.remaining_attempts -= 1

            # Check if guess is within range
            if guess < 1 or guess > self.max_number:
                self.feedback_label.config(text=f"🎡 Please guess a number between 1 and {self.max_number}!", fg="#ff4500")
                self.remaining_attempts += 1
                self.attempts -= 1
                self.guess_entry.delete(0, tk.END)
                return

            # Check the guess
            if guess == self.target_number:
                score = (self.max_attempts - self.attempts + 1) * 10
                self.feedback_label.config(
                    text=f"🎉 Hooray! You guessed the number {self.target_number} in {self.attempts} attempts!\nScore: {score} 🏆",
                    fg="#32cd32"  # Green for winning
                )
                self.confetti_effect()  # Add confetti animation
                self.end_game()
            elif self.remaining_attempts == 0:
                self.feedback_label.config(
                    text=f"🎢 Game Over! The number was {self.target_number}. Better luck next time! 😢",
                    fg="#ff4500"  # Orange for losing
                )
                self.end_game()
            else:
                # Playful feedback with color animation
                if guess < self.target_number:
                    messages = [
                        "🎈 Too low! Aim higher! 📈",
                        "🎪 Nope, too low! Keep climbing! ⛰️",
                        "🎡 A bit too low! You're getting there! 🌟"
                    ]
                    self.animate_feedback(random.choice(messages), "#1e90ff")  # Blue for too low
                else:
                    messages = [
                        "🎈 Too high! Bring it down! 📉",
                        "🎪 Oops, too high! Lower your guess! 🪂",
                        "🎡 A bit too high! Almost there! ✨"
                    ]
                    self.animate_feedback(random.choice(messages), "#ff4500")  # Orange for too high
                self.attempts_label.config(text=f"🎟️ Attempts left: {self.remaining_attempts}")

            self.guess_entry.delete(0, tk.END)

        except ValueError:
            self.feedback_label.config(text="🎡 Invalid input! Please enter a number.", fg="#ff4500")
            self.guess_entry.delete(0, tk.END)

    def animate_feedback(self, message, color):
        # Simple color animation: flash the feedback label
        for i in range(3):
            self.feedback_label.config(fg=color if i % 2 == 0 else "#ffffff")
            self.feedback_label.config(text=message)
            self.root.update()
            time.sleep(0.2)
        self.feedback_label.config(fg=color)

    def confetti_effect(self):
        # Create "confetti" labels that fall from the top
        colors = ["#ff69b4", "#1e90ff", "#32cd32", "#ff4500", "#ffff00"]  # Pink, blue, green, orange, yellow
        for _ in range(20):  # Create 20 confetti pieces
            x = random.randint(50, 400)
            confetti = tk.Label(
                self.root, text="✨", font=("Comic Sans MS", 12), fg=random.choice(colors), bg="SystemTransparent"
            )
            self.confetti_labels.append(confetti)
            self.canvas.create_window(x, 0, window=confetti)
            self.animate_confetti(confetti, x)

    def animate_confetti(self, confetti, x):
        # Animate confetti falling
        for y in range(0, 600, 10):
            self.canvas.coords(confetti, x, y)
            self.root.update()
            time.sleep(0.05)
        confetti.destroy()  # Remove confetti after it falls

    def end_game(self):
        self.canvas.delete("all")
        self.create_gradient()
        self.canvas.create_window(225, 40, window=self.title_label)
        self.canvas.create_window(225, 150, window=self.feedback_label)
        self.canvas.create_window(225, 300, window=self.play_again_button)

    def reset_game(self):
        # Clear confetti
        for confetti in self.confetti_labels:
            confetti.destroy()
        self.confetti_labels.clear()

        # Reset UI
        self.feedback_label.config(text="", fg="#ff4500")
        self.attempts_label.config(text="")
        self.canvas.delete("all")
        self.create_gradient()
        self.canvas.create_window(225, 40, window=self.title_label)
        self.canvas.create_window(225, 100, window=self.difficulty_label)
        self.canvas.create_window(225, 140, window=self.difficulty_menu)
        self.canvas.create_window(225, 190, window=self.start_button)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()