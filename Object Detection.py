{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRPLeo4+gIe8F5IB7wlKUw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KhangTheKangaroo/AIO-354-Homework/blob/main/Object%20Detection.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KjwNTr59cXHu"
      },
      "outputs": [],
      "source": [
        "!git clone https://github.com/THU-MIG/yolov10.git #Run this to clone the yolov10 files"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd yolov10 #Change Directory to yolov10\n",
        "!pip install -q -r requirements.txt #Install any APis or tools needed to run\n",
        "!pip install -e"
      ],
      "metadata": {
        "id": "fBwG-npTdeMz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt #Get yolov10n.pt file"
      ],
      "metadata": {
        "id": "PwjUBq0LeXEb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install ultralytics import YOLov10 #Download ultralytics (Skip this step if everything below is working as attended)"
      ],
      "metadata": {
        "id": "D9qFxUBqeh2Q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from ultralytics import YOLOv10\n",
        "\n",
        "MODEL_PATH = 'yolov10n.pt'\n",
        "model = YOLOv10(MODEL_PATH)"
      ],
      "metadata": {
        "id": "3hcJHGByetph"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!gdown '1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R' #Download the Safety_Helmet_Data set zip if you haven't already got it from Github\n",
        "!mkdir safety_helmet_dataset\n",
        "!unzip -q '/content/Safety_Helmet_Dataset.zip' -d '/content/safety_helmet_dataset'"
      ],
      "metadata": {
        "id": "8onYCPIkezEX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "YAML_PATH = '/../safety_helmet_data.yaml'\n",
        "EPOCHS = 50 #Number of Epoch/Run per data\n",
        "IMG_SIZE = 640\n",
        "BATCH_SIZE = 256 #Number of batches per Epoch run, Batch size = 256 and Epoch = 50 then tere are 50*256 Amount of Data (N)/Reduce this to multiples of 2 (2n) if you're experiencing RAM/Memory Leak\n",
        "model.train = (path = YAML_PATH, epochs = EPOCHS, img_size = IMG_SIZE, batch_size = BATCH_SIZE) #Train Model"
      ],
      "metadata": {
        "id": "0tNI-eWrfNmw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "TRAINED_MODEL_PATH = 'runs/detect/train/weights/best.pt'\n",
        "model = YOLOv10(TRAINED_MODEL_PATH)\n",
        "\n",
        "model.val = (data = YAML_PATH, imgsz = IMG_SIZE, split = 'test')"
      ],
      "metadata": {
        "id": "bT9cq1-7fs7n"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}