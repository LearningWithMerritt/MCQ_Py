import os
import subprocess

if os.name == "nt":
    lwm_path = os.path.join(os.environ["LOCALAPPDATA"], "LWM") 
elif os.name == "posix":
    lwm_path = os.path.join(os.environ["HOME"], "LWM") 


repo_path = os.path.join(lwm_path, "MCQ_Py")

os.makedirs(lwm_path, exist_ok=True)


if not os.path.exists(repo_path):
    subprocess.run(["git", "clone", "https://github.com/LearningWithMerritt/MCQ_Py.git", repo_path])
else:
    print("Repository already exists. Skipping clone.")


os.chdir(repo_path)


subprocess.run(["git", "pull"])

if os.name == "nt":
    subprocess.run(["python", "app-cli/main.py"])
elif os.name == "posix":
    subprocess.run(["python3", "app-cli/main.py"])