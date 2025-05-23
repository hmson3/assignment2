import subprocess

# 설정
EXECUTABLE = "../build/my_tsp_exec"
INSTANCES = ["test4", "test18", "test20", "test22", "test24", "a280", "xql662", "kz9976", "mona-lisa_sample"]
DATA_DIR = "../data"

for instance in INSTANCES:
    print(f"▶ Running: {instance}")

    process = subprocess.run(
        [EXECUTABLE, instance],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # 출력 로그 보기
    print(process.stdout.strip())

print("\n✅ All instances executed.")
