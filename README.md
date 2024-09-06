# CGPI to Percentage Converter

This is a simple web application built using Streamlit that converts your Cumulative Grade Point Index (CGPI) to Percentage based on the University of Mumbai's formula.

## Features

- Allows input for multiple semesters' CGPI.
- Converts CGPI to Percentage based on the following conditions:
  - If CGPI is less than 7, the formula used is: `Percentage = 7.1 * CGPI + 12`
  - If CGPI is greater than or equal to 7, the formula used is: `Percentage = 7.4 * CGPI + 12`
- Automatically rounds the percentage to the nearest full integer.
- The application keeps previously entered CGPI values pre-filled when interacting with the app.

## Formula

The percentage is calculated using the following rules:
- If CGPI < 7: 
  ```plaintext
  Percentage = 7.1 * CGPI + 12
  ```
- If CGPI >= 7:
  ```plaintext
  Percentage = 7.4 * CGPI + 12
  ```

## Prerequisites

- Python 3.x installed
- `streamlit` package installed. You can install it by running:
  ```bash
  pip install streamlit
  ```

## How to Run the Application

1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the following command in your terminal:
   ```bash
   streamlit run cgpi_conversion.py
   ```
4. Your web browser will automatically open the app. If not, go to the URL displayed in the terminal (usually `http://localhost:8501/`).

## Usage

1. Enter the number of semesters.
2. Input the CGPI for each semester.
3. Click on the **Calculate Overall Percentage** button.
4. The overall percentage will be displayed as the result.

## Example

If the CGPI for Semester 1 is 6.8 and for Semester 2 is 7.2, the application will calculate the percentage using the appropriate formula for each CGPI and display the overall percentage.

## Author

**Amey Mali**  
Contact: [ameymali54@icloud.com](mailto:ameymali54@icloud.com)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Instructions for Use:
1. Save this as `README.md` in your project folder.
2. You can add a `screenshot.png` if you'd like to include a visual representation of your app.

Let me know if you'd like to make any changes!
