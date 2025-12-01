from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

# initialize FastAPI app
app = FastAPI()

@app.post("/add")
def add(a: float, b: float) -> float:
    """
    Add two numbers.
    Parameters:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of the two numbers.
    """
    return a + b

@app.post("/subtract")
def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers.
    Parameters:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The difference of the two numbers.
    """
    return a - b

@app.post("/multiply")
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    Parameters:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The product of the two numbers.
    """
    return a * b

@app.post("/divide")
def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    Parameters:
        a (float): The numerator.
        b (float): The denominator.
    Returns:
        float: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# converting to MCP
mcp = FastApiMCP(app, name="calculator")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)