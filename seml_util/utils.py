import os


def create_logdir(logdir, ex):
    array_job_id = os.environ.get("SLURM_ARRAY_JOB_ID")
    array_task_id = os.environ.get("SLURM_ARRAY_TASK_ID")
    logdir = os.path.join(logdir, f"{array_job_id}_{array_task_id}")
    os.makedirs(logdir, exist_ok=True)
    ex.current_run.config["logdir"] = logdir
    return logdir
