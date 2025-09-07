FROM python:3.9-alpine

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /src/app

COPY requirements.txt .

RUN apk add --no-cache \
    build-base \
    mariadb-dev \
    libjpeg-turbo-dev \
    zlib-dev

RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# 🔧 کپی کردن entrypoint از پوشه جدید
COPY docker_scripts/entrypoint.sh /entrypoint.sh 

# اصلاح فرمت خطوط پایانی و اجرایی کردن فایل
RUN sed -i 's/\r$//' /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]