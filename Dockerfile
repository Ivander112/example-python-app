FROM python:3.8
LABEL Name="ansible_st2_ivan"
LABEL Version="0.1.0"
EXPOSE 4321
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]