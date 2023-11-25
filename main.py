from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def f_index():
    return {"ФИО": "Головизина Е.В."}

@app.get('/users')
async def f_indexU():
    return {"№ телефона": "+7(923)727-**-**"}

@app.get('/tools')
async def f_indexT():
    return {"О себе": "Прохожу обучение по направлению Прикладная информатика"}
