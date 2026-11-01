from fastapi import FastAPI

app = FastAPI(
    title="employee-service",
    description="Sample employee API with static demo data",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "UP", "application": "employee-service"}

@app.get("/api/employees")
def employees():
    return [
        {"id": 101, "name": "Asha", "role": "Platform Engineer"},
        {"id": 102, "name": "Rahul", "role": "Python Developer"},
        {"id": 103, "name": "Maya", "role": "QA Engineer"},
    ]

