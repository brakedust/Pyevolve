import subprocess


if __name__ == "__main__":
    subprocess.call("pytest --cov=pyevolve tests")
