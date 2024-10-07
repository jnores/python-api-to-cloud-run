import os
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Union, List, Dict

app = FastAPI()


@app.get("/hello", response_model=str, operation_id="get_clientes")
async def get_clientes():
    return "World"


@app.get("/many_hello", response_model=List[str], operation_id="get_bienes")
async def get_bienes(cant: Optional[str] = Query(None)):
    limit_value = 10 if cant == "" or cant is None else int(cant)
    lst=["world" for i in range(limit_value)]
    return lst

if __name__ == '__main__':
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
