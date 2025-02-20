FROM public.ecr.aws/lambda/python:3.13

# copy the requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# copy the app code
COPY /app/* ${LAMBDA_TASK_ROOT}

# install dependencies
RUN pip install -r requirements.txt

# set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.handler" ]