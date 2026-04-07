from flask import Flask, request, render_template
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import os

app = Flask(__name__)

# ====== CONFIG ======
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ====== LOAD MODEL ======
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, 2)

model.load_state_dict(torch.load(r"model_catdog.pt", map_location="cpu"))
model.eval()

# ====== TRANSFORM ======
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ====== ROUTE DUY NHẤT ======
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    image_path = None

    if request.method == "POST":
        file = request.files["file"]

        # lưu ảnh
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # xử lý ảnh
        img = Image.open(filepath).convert("RGB")
        img = transform(img).unsqueeze(0)

        # predict
        with torch.no_grad():
            output = model(img)
            _, predicted = torch.max(output, 1)

        result = "Cat 🐱" if predicted.item() == 0 else "Dog 🐶"
        image_path = filepath

    return render_template("index.html", result=result, image_path=image_path)

# ====== RUN ======
if __name__ == "__main__":
    app.run(debug=True)