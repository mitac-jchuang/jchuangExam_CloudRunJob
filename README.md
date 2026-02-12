# This project is develop mode!!

This project is aims to exam the CI/CD process of cloud run jobs.

## Deploy Manually


## Run with input parameters
```
gcloud run jobs execute JOB_NAME --region="asia-east1" --args="your_argument_value"
# For multiple arguments:
gcloud run jobs execute JOB_NAME --region="asia-east1" --args="arg1","arg2","arg3"
# 如要讓指令等待執行完成，請使用
gcloud run jobs execute JOB_NAME --wait --region="asia-east1"
```

## Call a existing job and overwrite env (Python)
```
from google.cloud import run_v2

client = run_v2.JobsClient()
job_path = client.job_path("project", 'region', 'cloud-run-job_name')

# Giving the enviroment variable list in dictionary
env_data = {
    "file_dir": "filename"
}

# Create the list of EnvVar objects from the dictionary
overridden_env_vars = [
    run_v2.EnvVar(name=name, value=value)
    for name, value in env_data.items()
]

# Create the RunJobRequest with the overrides
request = run_v2.RunJobRequest(
    name=job_path,
    overrides=run_v2.RunJobRequest.Overrides(
        container_overrides=[
            run_v2.RunJobRequest.Overrides.ContainerOverride(
                env=overridden_env_vars
            )
        ]
    )
)

try:
    operation = client.run_job(request=request)
    print(f"Job triggered with overrides.")
except Exception as e:
    print(f"Failed to trigger job: {e}")


```