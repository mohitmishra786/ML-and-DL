import tensorflow as tf
class MyRNNCell(tf.keras.layers.Layer):
    def __init__(self, rnn_units, input_dim, output_dim):
        super(MyRNNCell, self).__init__()

        # Initialisation of weight matrices
        self.W_xh = self.add_weight([rnn_units, input_dim])
        self.W_hh = self.add_weight([rnn_units, rnn_units])
        self.W_hy = self.add_weight([output_dim, rnn_units])

        # Initialization hidden state to zeros
        self.h = tf.zeros([rnn_units , 1])

    def call(self , x):
        # Calculating current hidden state
        self.h = tf.math.tanh(self.W_hh * self.h + self.W_xh * x)

        # Calculation output
        output = self.h * self.W_hy

        # Return the current output and hidden state
        return output, self.h
