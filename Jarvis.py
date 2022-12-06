# Import necessary libraries
import random
import numpy as np

# Define a function to train the AI
def train_AI(data):
  # Calculate the mean of the data
  mean = np.mean(data)
  
  # Calculate the standard deviation of the data
  std = np.std(data)
  
  # Return the calculated mean and standard deviation
  return mean, std

# Define a function to predict a value based on the trained AI
def predict(value, mean, std):
  # Calculate the probability of the given value
  probability = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(-(value - mean)**2 / (2 * std**2))
  
  # Return the calculated probability
  return probability

# Define a list of greetings
greetings = ["hello", "hi", "how are you", "good to see you"]

# Define a list of responses to greetings
greeting_responses = ["hello!", "hi there!", "I'm doing well, thank you!", "nice to see you too!"]

# Define a function to process user input
def process_input(input, mean, std):
  # Check if the user's input is a greeting
  if input.lower() in greetings:
    # If so, return a random greeting response
    return random.choice(greeting_responses)
  else:
    # If not, predict the probability of the user's input
    probability = predict(input, mean, std)
    
    # Return a response based on the probability
    if probability > 0.5:
      return "That sounds interesting!"
    else:
      return "I'm sorry, I didn't understand that."

# Define some sample data
data = [0, 1, 2, 3, 4, 5]

# Train the AI on the data
mean, std = train_AI(data)

# Define a function to run the chatbot
def run_chatbot():
  # Print a welcome message
  print("Welcome to the chatbot! Type 'quit' to exit.")
  
  # Start an infinite loop to process user input
  while True:
    # Get user input
    user_input = input("User: ")
    
    # Check if the user wants to exit
    if user_input.lower() == "quit":
      # If so, break out of the loop
      break
      
    # Process the user's input
    response = process_input(user_input, mean, std)
    
    # Print the chatbot's response
    print("Chatbot: " + response)

# Run the chatbot
run_chatbot()