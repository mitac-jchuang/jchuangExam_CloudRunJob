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

## Call a existing job with parameters (Python)
```
from google.cloud.run_v2.services import jobs
from google.cloud.run_v2 import RunJobRequest

client = jobs.JobsClient()
job_path = client.job_path('project_id', 'asia-east1', 'cloudRunJobs_name')

container_override = RunJobRequest.Overrides.ContainerOverride(args=['paramter_passed_by_python'])
overrides = RunJobRequest.Overrides(container_overrides=[container_override])

request = RunJobRequest(name=job_path, overrides=overrides)

try:
    operation = client.run_job(request=request)
    print(f"Job triggered with overrides.")
except Exception as e:
    print(f"Failed to trigger job: {e}")


```