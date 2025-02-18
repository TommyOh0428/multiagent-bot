FROM public.ecr.aws/lambda/python:3.13

COPY requirements.txt ${LAMBDA_TASK_ROOT}

COPY /app/* ${LAMBDA_TASK_ROOT}
