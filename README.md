
# Reverse Complement Tool

This project is a simple **Reverse Complement Tool** built using Flask. It takes a DNA sequence as input, computes the reverse complement of the sequence, and provides an option to download the result. 

## Features
- Input DNA sequences up to 5000 characters.
- Displays the reverse complement of the entered DNA sequence.
- Allows users to download the result as a `.txt` file.
- An "About" page that describes the functionality of the tool.

## Project Structure
```
Reverse-Compliment/
│
├── app.py                  # The main Flask application.

```

## Requirements

To run this project, you need to have the following installed:
- Python 3.x
- Flask (`pip install flask`)
- Flask-Frozen (`pip install Flask-Frozen`)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/jaannawaz/Reverse-Compliment-.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Reverse-Compliment
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## How It Works

- **Input**: The user inputs a DNA sequence in the text area.
- **Processing**: The application reverses the DNA sequence and calculates its complement (A ↔ T, C ↔ G).
- **Output**: The reverse complement is displayed and can be downloaded as a `.txt` file.

## Example

For the DNA sequence `ATTGC`, the reverse complement would be:
```
GCAAT
```

## About

This tool is useful for anyone working with DNA sequences who needs to quickly find the reverse complement of a sequence.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
