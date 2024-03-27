class Job:
    def __init__(self, p, r, d):
        self.process = p
        self.release = r
        self.deadline = d

    def __str__(self):
        return f"p:{self.process},r:{self.release},d:{self.deadline}"


def bubbleSort(job_list):
    n = len(job_list)
    if n <= 1:
        return job_list
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if job_list[j].deadline > job_list[j + 1].deadline:
                (job_list[j], job_list[j + 1]) = (job_list[j + 1], job_list[j])


def edd(job_list):
    time = 0
    excuted_list = []
    latency = 0
    while len(job_list) > 0:
        current_job = job_list.pop(0)
        time += current_job.process
        latency += (time - current_job.deadline)
        excuted_list.append(current_job)
    return latency


j1 = Job(2, 0, -1)
j2 = Job(1, 2, 1)
j3 = Job(4, 1, 10)
job_list = [j2, j1, j3]
bubbleSort(job_list)
for i in job_list:
    print(i)
latency = edd(job_list)
print(latency)
