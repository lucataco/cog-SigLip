# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
from PIL import Image
from transformers import pipeline

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        self.pipe = pipeline(task="zero-shot-image-classification", model="google/siglip-base-patch16-224",)

    def predict(
        self,
        image: Path = Input(description="Input image"),
        candidate_labels: str = Input(
            description="Candidate labels separated by commas",
            default="2 cats, a plane, a remote")
    ) -> str:
        """Run a single prediction on the model"""
        # Load the image and handle png images
        pil_image = Image.open(image).convert("RGB")
        # convert canditate labels to list
        labels = candidate_labels.split(",")
        outputs = self.pipe(pil_image, candidate_labels=labels)
        result = [{"score": round(output["score"], 4), "label": output["label"] } for output in outputs]
        return str(result)
