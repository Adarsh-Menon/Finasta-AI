import os
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class ModelProvider(str,Enum):
    OLLAMA = "ollama"
    GOOGLE_GENAI = "google_genai"
    
@dataclass
class ModelConfig:
    name:str
    temperature: float
    provider: ModelProvider
    
qwen = ModelConfig("qwen3:8b", temperature=0.0,provider=ModelProvider.OLLAMA)
gemini = ModelConfig(
    "gemini-2.5-flash",temperature=0.0,provider=ModelProvider.GOOGLE_GENAI
)

class config:
    SEED = 42
    MAX_ITERATIONS = 10
    MODEL = gemini
    CONTEXT_WINDOW = 8192
    
    class path:
        APP_HOME = Path(os.getenv("APP_HOME",Path(__file__).parent.parent))
        DATA_DIR = APP_HOME / "data"