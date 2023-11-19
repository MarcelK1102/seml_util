import os


def create_logdir(logdir, ex):
    array_job_id = os.environ.get("SLURM_ARRAY_JOB_ID")
    array_task_id = os.environ.get("SLURM_ARRAY_TASK_ID")
    db_collection = ex.current_run.config["db_collection"]
    if array_job_id is None:
        ex.current_run._id
        logdir = os.path.join(logdir, f"{db_collection}_{ex.current_run._id}")
    else:
        logdir = os.path.join(logdir, f"{db_collection}_{array_job_id}_{array_task_id}")
    os.makedirs(logdir, exist_ok=True)
    ex.current_run.config["logdir"] = logdir
    return logdir
