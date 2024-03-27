def bubbleSort(job_list):
    n = len(job_list)
    if n <= 1:
        return job_list
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if job_list[j] < job_list[j + 1]:
                (job_list[j], job_list[j + 1]) = (job_list[j + 1], job_list[j])


job_list = [3, 5, 7, 2, 4, 9, 14, 12, 1, 18, 16, 21]
bubbleSort(job_list)
print("排序后的任务序列：",job_list)


def lpt(job_list, m):
    machine = [[] for i in range(m)]
    T = [0 for i in range(m)]
    while len(job_list) > 0:
        current_job = job_list.pop(0)
        best_machine = T.index(min(T))
        machine[best_machine].append(current_job)
        T[best_machine] += current_job
    print(f"机器数为：{m}，时间序列：{T}")


lpt(job_list, 4)