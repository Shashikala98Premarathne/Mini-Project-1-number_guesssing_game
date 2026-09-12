import streamlit as st
import random

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Number Guessing Game 🎯",
    page_icon="🎯",
    layout="centered"
)

# -----------------------------
# BACKGROUND COLOR
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF4E6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎯 Number Guessing Game")


# -----------------------------
# SESSION STATE
# -----------------------------

# Generate the secret number only once
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

# Keep track of attempts
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Keep track of whether the game has finished
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Keep track of whether the player quit
if "quit_game" not in st.session_state:
    st.session_state.quit_game = False


# -----------------------------
# USER NAME
# -----------------------------

name = st.text_input("Enter your name:")

if name:
    st.write(
        f"Hello {name}! Welcome to the Number Guessing Game. "
        f"You have 10 attempts. Good luck! 🍀"
    )


# -----------------------------
# GAME
# -----------------------------

if not st.session_state.game_over:

    guess_input = st.text_input(
        "I have a number in my mind. Hint: It's between 1 and 100. 😉 "
        "Please give me your guess:"
    )

    col1, col2 = st.columns(2)

    # -----------------------------
    # SUBMIT GUESS
    # -----------------------------

    with col1:
        submit_guess = st.button("Submit Guess 🎯")

    # -----------------------------
    # QUIT GAME
    # -----------------------------

    with col2:
        quit_button = st.button("Quit Game 👋")

    if quit_button:
        st.session_state.quit_game = True
        st.session_state.game_over = True

        st.warning(
            f"Thanks for playing, {name}! 👋 "
            f"The secret number was {st.session_state.secret_number}."
        )

    elif submit_guess:

        try:
            guess = int(guess_input)

            # Validate range
            if guess < 1 or guess > 100:
                raise ValueError(
                    "Please enter a number between 1 and 100."
                )

            # Count valid attempt
            st.session_state.attempts += 1

            attempts_left = 10 - st.session_state.attempts

            # -----------------------------
            # CORRECT GUESS
            # -----------------------------

            if guess == st.session_state.secret_number:

                if st.session_state.attempts == 1:
                    st.success(
                        f"Congratulations {name}! "
                        f"You nailed it on the first try! 🔥🎯 "
                        f"The number was {st.session_state.secret_number}."
                    )

                else:
                    st.success(
                        f"Congratulations {name}! 🥳 "
                        f"You guessed the number "
                        f"{st.session_state.secret_number} "
                        f"in {st.session_state.attempts} attempts."
                    )

                st.session_state.game_over = True

            # -----------------------------
            # WRONG GUESS
            # -----------------------------

            else:

                difference = abs(
                    guess - st.session_state.secret_number
                )

                if difference <= 5:
                    st.warning(
                        f"🔥 Fire! You're very close! "
                        f"{attempts_left} attempts left."
                    )

                elif difference <= 10:
                    st.warning(
                        f"😮‍💨 Wow! You're close! "
                        f"{attempts_left} attempts left."
                    )

                elif difference <= 20:
                    st.warning(
                        f"😮 You're getting warmer! "
                        f"{attempts_left} attempts left."
                    )

                elif difference <= 30:
                    st.warning(
                        f"😑❄️ You're getting cold! "
                        f"{attempts_left} attempts left."
                    )

                else:
                    st.warning(
                        f"😩🥶 Wrong direction! You're very cold! "
                        f"{attempts_left} attempts left."
                    )

                # -----------------------------
                # OUT OF ATTEMPTS
                # -----------------------------

                if st.session_state.attempts >= 10:
                    st.error(
                        f"Sorry {name}, you've used all your attempts. ☹️ "
                        f"The secret number was "
                        f"{st.session_state.secret_number}. "
                        f"Better luck next time! ✨🧚"
                    )

                    st.session_state.game_over = True

        except ValueError as e:

            if guess_input == "":
                st.error("Please enter a number before submitting.")

            else:
                st.error(
                    "Please enter a whole number between 1 and 100."
                )


# -----------------------------
# GAME FINISHED
# -----------------------------

else:

    if st.session_state.quit_game:
        st.info("Game ended. You can start a new game below.")

    else:
        st.info("🎮 Game finished! Want to play again?")


# -----------------------------
# PLAY AGAIN
# -----------------------------

if st.session_state.game_over:

    if st.button("Play Again 🔄"):

        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.quit_game = False

        st.rerun()