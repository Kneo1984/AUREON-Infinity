from fastapi import FastAPI 
app = FastAPI() 
 
@app.get("/") 
def root(): 
    return {"message": "QuantumShield Infinity Core aktiviert."} 
