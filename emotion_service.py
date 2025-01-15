from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

emotion_analyzer = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

class EmotionRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_emotions(request: EmotionRequest):
    try:
        results = emotion_analyzer(request.text)
        # Flatten the results to ensure a consistent structure
        flattened_results = results[0] if isinstance(results, list) and len(results) > 0 else []
        return {"emotions": flattened_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

