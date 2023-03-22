# This code is just a Pseudocode

my_rnn = RNN()
hidden_state = [0,0,0]
sentence = ["I" , "love", "mathematics"]


# We are iterating through whole sentence word by word
for word in sentence:
    # with the help of rnn function we are updating hidden_state and making prediction also
    prediction , hidden_state = my_rnn(word , hidden_state)

next_word_prediction = prediction

