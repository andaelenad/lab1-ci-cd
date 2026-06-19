import subprocess
import time

def ruleaza_simulare(prompt_natural, comanda_asteptata):
    print(f"\n👤 Utilizator: {prompt_natural}")
    time.sleep(1) # Simulam timpul de gandire al modelului
    print(f"🤖 Ollama a tradus si a decis comanda: {comanda_asteptata}")
    print("⚙️  Se executa...\n")
    time.sleep(0.5)
    
    # Rulam comanda reala din aplicatia ta
    subprocess.run(comanda_asteptata.split())

if __name__ == "__main__":
    # Simulam interogari in limbaj natural si spunem scriptului ce comanda reala sa execute
    ruleaza_simulare("Adauga te rog cursul de Programare Orientata pe Obiecte", "python3 todo.py add Programare Orientata pe Obiecte")
    
    print("\n" + "-"*50)
    
    ruleaza_simulare("Arata-mi lista de cursuri pe care le am", "python3 todo.py list")
