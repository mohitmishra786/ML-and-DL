class MyDenserLayer(tf.keras.layers.layer):
    def __init__(self, input_dim, output_dim) -> None:
        super(MyDenserLayer, self).__init__()


        # Initialization of weights and bias
        self.W = self.add_weight([input_dim, output_dim])
        self.b = self.add_weight([1, output_dim])

    def call(self, inputs):

        # Forward Propagation
        z = tf.matmul(inputs, self.W) + self.b

        # Feeding through a non-linear equation
        output = tf.math.sigmoid(z)

        return output