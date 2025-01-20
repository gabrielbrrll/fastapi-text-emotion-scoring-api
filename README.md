# fastapi-text-emotion-scoring-api

# Emotion Analyzer API

A lightweight and simple API for analyzing emotions in text using a pre-trained model from the Hugging Face `transformers` library.

## Features

- Accepts a text input and returns detected emotions with associated confidence scores.
- Utilizes the `j-hartmann/emotion-english-distilroberta-base` model for emotion classification.
- Built with **FastAPI** for fast, reliable, and easy-to-use RESTful API endpoints.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/emotion-analyzer-api.git
cd emotion-analyzer-api
```

### Install Dependencies

It’s recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Requirements File Example

If not included, here’s the `requirements.txt`:

```plaintext
fastapi==0.95.1
uvicorn==0.23.0
transformers==4.29.1
pydantic==1.10.5
```

### Run the Application

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## Usage

### Endpoint: `/analyze`

**Method**: `POST`  
**Request Body**:
```json
{
  "text": "I feel amazing today!"
}
```

**Response**:
```json
{
  "emotions": [
    {"label": "joy", "score": 0.95},
    {"label": "anger", "score": 0.03},
    {"label": "sadness", "score": 0.02}
  ]
}
```

### Example with `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/analyze" -H "Content-Type: application/json" -d '{"text": "I feel amazing today!"}'
```

## Model Information

This API uses the `j-hartmann/emotion-english-distilroberta-base` model, a fine-tuned DistilRoBERTa model for emotion classification. It can detect multiple emotions with confidence scores.

## Error Handling

- **500 Internal Server Error**: Returned when the model fails to process the input.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.
```
