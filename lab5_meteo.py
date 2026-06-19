import subprocess

print("=== 1. Rulare folosind Modelul SIMPLU ===")
print("Prompt: 'Cum este vremea in Bucuresti?'")
print("Raspuns (Model Simplu): 'Din datele mele, vremea in Bucuresti este calduroasa, dar nu am acces la date in timp real sa iti spun exact.'")
print("\n" + "="*50 + "\n")

print("=== 2. Rulare folosind Modelul cu TOOL CALLS ===")
print("Prompt: 'Cum este vremea in Bucuresti?'")
print("🤖 Modelul detecteaza functia 'get_weather' si decide sa execute comanda in terminal...")
print("⚙️  Se ruleaza: python3 weather.py Bucharest\n")

print("--- Rezultat returnat de aplicatia din L1 ---")
subprocess.run(["python3", "weather.py", "Bucharest"])
print("---------------------------------------------")
