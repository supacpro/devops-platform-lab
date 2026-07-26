# devops-platform-lab

ตัวอย่างโปรเจกต์ Python สำหรับเรียนรู้ DevOps และ CI/CD

## โครงสร้าง

- `app/` - โค้ดแอปพลิเคชันหลัก
- `tests/` - ชุดทดสอบ
- `.github/workflows/ci.yml` - กำหนด workflow ของ GitHub Actions

## เครื่องมือ

- Python 3.11+ และ `pytest`

## วิธีใช้งาน

1. ติดตั้ง dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
2. รันทดสอบ:
   ```bash
   python -m pytest
   ```
3. รันแอปตัวอย่าง:
   ```bash
   python -m app.main
   ```
