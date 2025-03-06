FROM public.ecr.aws/lambda/python:3.13

COPY requirements.txt ${LAMBDA_TASK_ROOT}

COPY . ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

CMD ["main.handler"]