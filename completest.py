import subprocess

result = subprocess.run (
    "python3 -m unittest discover tests 2>&1",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

output = result.stdout.strip().split('\n')
for line in output:
    print(line)

# Prints the last line separately to see what it looks like
print("\nLast line of the output:")
print(output[-1])
