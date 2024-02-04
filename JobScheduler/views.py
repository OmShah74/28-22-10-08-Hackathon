from django.shortcuts import render

def rank(jobs):
    for job in jobs:
        job.append((job[1] + job[2] - job[3]) / 3)

    jobs.sort(key=lambda x: x[4], reverse=True)

    return [job[0] for job in jobs]

def job_form(request):
    num_jobs_range = range(1, 6)  # Adjust the range according to your needs
    return render(request, 'JobScheduler/job_form.html', {'num_jobs_range': num_jobs_range})

def submit_jobs(request):
    if request.method == 'POST':
        n = int(request.POST.get('num_jobs'))
        jobs = []

        for i in range(1, n + 1):
            profit = int(request.POST.get(f'job_{i}_profit'))
            importance = int(request.POST.get(f'job_{i}_importance'))
            duration = int(request.POST.get(f'job_{i}_duration'))
            jobs.append([i, profit, importance, duration])

        ranked_jobs = rank(jobs)

        return render(request, 'JobScheduler/result.html', {'ranked_jobs': ranked_jobs})

    return render(request, 'JobScheduler/job_form.html', {'num_jobs_range': range(1, 6)})  # Adjust the range according to your needs
