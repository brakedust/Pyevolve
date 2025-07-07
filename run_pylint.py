import subprocess

subprocess.call("pylint --rcfile=pylintrc.conf pyevolve >errors.html")
