# 1. IMPORT necessary libraries:
#    - google.genai (for interacting with the Gemini API)
#    - config (for API key management)
from google import genai
from google.genai import types
import config 

client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API."""

    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
category = input("Enter a category (e.g., animal, food, city): ")
item = input(f"Enter a specific {category} to classify: ")

print("\n--- ZERO-SHOT LEARNING ---")

zero_shot = f"Is {item} a {category}? Answer yes or no."

print(f"Prompt: {zero_shot}")

print(f"Response: {generate_response(zero_shot)}")

print("\n--- ONE-SHOT LEARNING ---")

one_shot = f"""Determine if the item belongs to the category.

Example:

Category: fruit

Item: apple

Answer: Yes, apple is a fruit.

Now you try:

Category: {category}

Item: {item}

Answer:"""

print(f"Response: {generate_response(one_shot)}")

print("\n--- FEW-SHOT LEARNING ---")

few_shot = f"""Determine if the item belongs to the category.

Example 1:

Category: fruit

Item: apple

Answer: Yes, apple is a fruit.

Example 2:

Category: fruit

Item: carrot

Answer: No, carrot is not a fruit. It's a vegetable.
"""

few_shot = f"""Determine if the item belongs to the category.

Example 1:

Category: fruit

Item: apple

Answer: Yes, apple is a fruit.

Example 2:

Category: fruit

Item: carrot

Answer: No, carrot is not a fruit. It's a vegetable.

Example 3:

Category: vehicle

Item: bicycle

Answer: Yes, bicycle is a vehicle.

Now you try:

Category: {category}

Item: {item}

Answer:"""

print(f"Response: {generate_response(few_shot)}")

print("\n--- CREATIVE FEW-SHOT EXAMPLE ---")

creative_prompt = f"""Write a one-sentence story about the given word.

Example 1:

Word: moon

Story: The moon winked at the lovers as they shared their first kiss.

Example 2:

Word: computer

Story: The computer sighed as another cup of coffee was spilled on its keyboard.
"""
Word: {item}

#Story:"""

print(f"Response:{generate_response(creative_prompt, temperature=0.7)}")


print("\n--- REFLECTION QUESTIONS ---")

print("1. How did the responses differ between zero-shot, one-shot, and few-shot approaches?")

print("2. Which approach gave the most helpful or accurate response?")

print("3. How did the examples in the few-shot prompt influence the model's output?")

#if __name__ == "__main__":
#run_activity()
    
# 2. DEFINE function generate_response(prompt, temperature=0.3):
#    - Initialize the genai client using the API key from config
#    - Create the content structure based on the user's prompt
#    - Configure the temperature and generate the response from Gemini API
#    - Return the response text

# 3. DEFINE function run_activity():
#    - PRINT introductory message explaining zero-shot, one-shot, and few-shot learning
#    - Step 1: Get user input for category and specific item (e.g., animal, food, city)
   
#    - Part 1: Zero-Shot Learning
#      - Generate a zero-shot learning prompt (e.g., "Is X a Y?")
#      - Display the AI's response to this prompt

#    - Part 2: One-Shot Learning
#      - Provide a one-shot learning prompt with a single example
#      - Display the AI's response to this one-shot prompt

#    - Part 3: Few-Shot Learning
#      - Provide a few-shot learning prompt with multiple examples
#      - Display the AI's response to the few-shot prompt

#    - Part 4: Creative Few-Shot Learning Example
#      - Create a creative prompt (e.g., a one-sentence story)
#      - Display the AI's creative response with a slightly higher temperature (0.7)

#    - Part 5: Reflection
#      - Ask reflection questions to encourage users to think about the differences between the learning approaches and the model's output

# 4. IF __name__ == "__main__":
#    - Call the run_activity() function to run the activity
