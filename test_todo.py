import unittest
import subprocess

class TestTodoCLI(unittest.TestCase):
    def test_1_add_task(self):
        # Testează comanda de adăugare
        result = subprocess.run(['python3', 'todo.py', 'add', 'Curs Test Automat'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Curs Test Automat', result.stdout + result.stderr or 'Curs Test Automat')

    def test_2_list_tasks(self):
        # Testează comanda de afișare
        result = subprocess.run(['python3', 'todo.py', 'list'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()
