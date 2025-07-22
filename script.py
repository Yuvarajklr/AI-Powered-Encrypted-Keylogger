from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

# Create a dummy LSTM model (expects input shape: (batch_size, 10, 1))
model = Sequential([
    LSTM(32, input_shape=(10, 1)),
    Dense(4, activation='softmax')  # Output: 4 behavior classes
])

model.compile(optimizer='adam', loss='categorical_crossentropy')
model.save("behavior_model.h5")
print("✅ Dummy model created.")
