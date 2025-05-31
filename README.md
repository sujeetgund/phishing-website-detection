# PhishDetector: Phishing Website Detection

PhishDetector is a machine learning-based web security project that aims to detect phishing websites using features extracted from URLs and site metadata. It leverages a structured ML pipeline for data ingestion, validation, preprocessing, model training, and inference.



## 🚀 Project Features

* Data ingestion and validation from UCI Phishing Websites Dataset
* Preprocessing and feature engineering
* Model training and evaluation pipeline
* Inference API to detect phishing from new website data
* Modular and scalable ML codebase
* Dockerized for consistent deployment



## 📊 Dataset

- **Source**: [UCI Machine Learning Repository - Phishing Websites Data Set](https://archive.ics.uci.edu/dataset/327/phishing+websites)
- **File**: `data/raw/phisingData.csv`
- **Features**: 30 website attributes (e.g., URL length, presence of IP, HTTPS usage, etc.)
- **Target**: `Result` column (1 = Phishing, -1 = Legitimate)



## 🚧 Project Structure

```bash
.
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── main.py
├── data/
│   └── raw/phisingData.csv
├── src/phishdetector/
│   ├── api/v1/endpoints.py
│   ├── components/
│   │   ├── data_ingestion.py
│   │   └── data_validation.py
│   ├── config/
│   ├── pipelines/
│   │   ├── inference/infer.py
│   │   ├── preprocessing/preprocess.py
│   │   └── training/train_model.py
```



## ⚖️ Tech Stack

* **Language**: Python 3.10+
* **Libraries**: pandas, scikit-learn, fastapi
* **Models**: Random Forest, Support Vector Machines, KNeighbours, Logistic Regression, and Ridge
* **API**: FastAPI
* **Packaging**: Docker



## 📚 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sujeetgund/phishing-website-detection.git
cd phishing-website-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run API Server

```bash
uvicorn run_api:app
```



## 🐳 Docker Usage

### Build the Image

```bash
docker build -t phishdetector .
```

### Run the Container

```bash
docker run -p 8000:8000 phishdetector
```



## 📆 Project Roadmap

* [X] Dataset ingestion and validation
* [X] Feature preprocessing and model training
* [X] Inference pipeline
* [X] API integration
* [ ] Add Streamlit frontend for usability
* [ ] CI/CD integration with GitHub Actions



## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit and push (`git push origin feature-branch`)
5. Open a Pull Request



## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## ℹ️ Author
If you have questions, suggestions, opportunities, or encounter any issues with this repository, feel free to reach out to **Sujeet Gund**.

[LinkedIn](https://linkedin.com/in/sujeetgund) • [Email](mailto:sujeetgund@gmail.com) • [X (formerly Twitter)](https://x.com/Sujeet_Gund)

