@echo off
echo ---------------------------------------
echo Setting up PythonOverflow Environment...
echo ---------------------------------------

REM Step 1: Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Step 2: Activate the virtual environment
call venv\Scripts\activate.bat

REM Step 3: Upgrade pip and install dependencies
echo Installing required packages...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ---------------------------------------
echo Setup complete! To run your app:
echo Activate the environment with: venv\Scripts\activate
echo Then run: python app.py
echo ---------------------------------------
pause
