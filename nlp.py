import spacy

# Load the spaCy language model
nlp = spacy.load("en")

# Define a function to detect emotions from text
def detect_emotions(text):
    # Tokenize the text
    tokens = nlp(text)

    # Initialize an empty list to store emotions
    emotions = []

    # Iterate over each token in the text
    for token in tokens:
        # Check if the token is a part of speech (POS) tag that is associated with emotion
        if token.pos_ == "ADJ" or token.pos_ == "VERB":
            # Extract the emotion word
            emotion_word = token.text

            # Check if the emotion word is in a list of known emotions
            if emotion_word in known_emotions:
                # Add the emotion to the list of emotions
                emotions.append(emotion_word)

    # Return the list of emotions
    return emotions

# Define a list of known emotions
known_emotions = ["happy", "sad", "angry", "fearful", "surprised"]

# Example usage
text = "I am feeling very happy today!"
emotions = detect_emotions(text)
print(emotions)