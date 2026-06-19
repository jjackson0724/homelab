import os
import requests
import json

# Path to your cybersecurity skills
SKILLS_PATH = r"C:\Users\Jarron\.claude\skills\cybersecurity\skills"

# Ollama settings
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def list_skills():
    """List all available skills"""
    skills = [f for f in os.listdir(SKILLS_PATH) if os.path.isdir(os.path.join(SKILLS_PATH, f))]
    return sorted(skills)

def load_skill(skill_name):
    """Read the SKILL.md file for a given skill"""
    skill_path = os.path.join(SKILLS_PATH, skill_name, "SKILL.md")
    if not os.path.exists(skill_path):
        return None
    with open(skill_path, "r", encoding="utf-8") as f:
        return f.read()

def ask_ollama(skill_content, question):
    """Send skill content + question to Ollama"""
    prompt = f"""You are a cybersecurity expert. Use the following skill documentation to answer the question.

SKILL DOCUMENTATION:
{skill_content}

QUESTION: {question}

Answer based on the skill documentation above. Be specific and practical."""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    print("\nThinking...\n")
    response = requests.post(OLLAMA_URL, json=payload)
    
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}"

def main():
    print("=== Matrix Homelab Skill Query ===\n")
    
    # List available skills
    skills = list_skills()
    print(f"Found {len(skills)} skills.\n")
    print("Enter part of a skill name to search (or press Enter to list first 20):")
    
    search = input("> ").strip().lower()
    
    if search:
        matches = [s for s in skills if search in s]
    else:
        matches = skills[:20]
    
    if not matches:
        print("No skills found matching that search.")
        return
    
    print("\nMatching skills:")
    for i, skill in enumerate(matches):
        print(f"  [{i+1}] {skill}")
    
    print("\nEnter the number of the skill you want to load:")
    choice = int(input("> ")) - 1
    
    selected_skill = matches[choice]
    print(f"\nLoading: {selected_skill}")
    
    skill_content = load_skill(selected_skill)
    if not skill_content:
        print("Could not load skill file.")
        return
    
    print("Skill loaded. Ask your question (or type 'quit' to exit):\n")
    
    while True:
        question = input("You: ").strip()
        if question.lower() == "quit":
            break
        if not question:
            continue
        
        answer = ask_ollama(skill_content, question)
        print(f"\nOllama: {answer}\n")

if __name__ == "__main__":
    main()