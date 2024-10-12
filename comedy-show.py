from openai import OpenAI
import time 

client = OpenAI()

# List of competing LLM models
competing_models = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o"]  # Add or modify as needed

# Function to generate themes for the comedy night
def generate_themes(num_themes):
    themes = []
    for _ in range(num_themes):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": "Generate a theme for a comedy night."}
            ]
        )
        themes.append(completion.choices[0].message.content) 
    return themes

# Function to generate jokes based on a theme using different models
def generate_jokes(theme):
    jokes = {}
    for model in competing_models:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a comedian."},
                {"role": "user", "content": f"Tell a joke about the theme: {theme}"}
            ]
        )
        jokes[model] = completion.choices[0].message.content
    return jokes

# Function to evaluate jokes
def evaluate_jokes(jokes):
    evaluations = {}
    for model, joke in jokes.items():
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a judge evaluating jokes."},
                {"role": "user", "content": f"Evaluate this joke: '{joke}'. Rate it from 1 to 10 and explain why."}
            ]
        )
        evaluations[model] = completion.choices[0].message.content
    return evaluations

# Main function to run the comedy show
def run_comedy_show(num_themes):
    themes = generate_themes(num_themes)
    
    for i, theme in enumerate(themes, 1):
        print(f"\nRound {i} - Theme: {theme}")
        jokes = generate_jokes(theme)
        evaluations = evaluate_jokes(jokes)
        
        for model in competing_models:
            print(f"\n{model}:")
            print(f"Joke: {jokes[model]}")
            print(f"Evaluation: {evaluations[model]}")

# Run the show
def run_comedy_show(num_themes):
    print("\n=== AI Comedy Show ===\n")
    print("Generating themes...")
    themes = generate_themes(num_themes)
    
    for i, theme in enumerate(themes, 1):
        print(f"\n--- Round {i} ---")
        print(f"Theme: {theme}")
        input("Press Enter to generate jokes...")
        
        print("\nGenerating jokes...")
        jokes = generate_jokes(theme)
        
        print("\nEvaluating jokes...")
        evaluations = evaluate_jokes(jokes)
        
        print("\nResults:")
        for model in competing_models:
            print(f"\n{model}:")
            print(f"Joke: {jokes[model]}")
            print(f"Evaluation: {evaluations[model]}")
            time.sleep(1)  # Pause for readability
        
        if i < num_themes:
            input("\nPress Enter to continue to the next round...")

    print("\n=== Comedy Show Ended ===")

def main_menu():
    while True:
        print("\n=== AI Comedy Show Menu ===")
        print("1. Start a new show")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            num_themes = int(input("Enter the number of themes for the show: "))
            run_comedy_show(num_themes)
        elif choice == '2':
            print("Thank you for using AI Comedy Show. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()