# HalalLens

HalalLens is a Python-based application designed to help users identify whether a food product is Halal, Haram, or Doubtful by analyzing its ingredient list. The project uses Optical Character Recognition (OCR) to extract text from product labels and compares the detected ingredients with a predefined dataset to determine the product's status.

## Features

- Extracts ingredient text from food labels using OCR
- Analyzes ingredients against a dataset
- Classifies products as Halal, Haram, or Doubtful
- Simple and user-friendly workflow
- Built using Python

## Technologies Used

- Python
- Optical Character Recognition (OCR)
- CSV Dataset
- Machine Learning Concepts

## Project Structure

```
HalalLens/
├── src/
│   ├── main.py
│   ├── ocr.py
│   ├── dataset.py
│   └── constants.py
├── input/
│   ├── dataset.csv
│   └── test.jpg
```

## How It Works

1. Upload an image of a food ingredient label.
2. The application extracts the text using OCR.
3. The extracted ingredients are compared with the dataset.
4. The system classifies the product as Halal, Haram, or Doubtful.

## Future Improvements

- Develop a Flutter-based mobile application
- Improve classification accuracy using AI models
- Support real-time camera scanning
- Expand the ingredient database

## Author

**Isha Saleem**

BS Computer Science Student  
The Shaikh Ayaz University, Shikarpur
