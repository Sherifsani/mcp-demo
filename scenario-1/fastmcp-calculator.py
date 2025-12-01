from fastmcp import FastMCP

mcp = FastMCP(name = "calculator")

@mcp.tool()
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

@mcp.tool(
    name = "subtract",
    description = "Subtract two numbers.",
    tags = ["math", "arithmetic"]
)
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

@mcp.tool()
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

@mcp.tool()
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

if __name__ == "__main__":
    mcp.run() #STDIO default
    # mcp.run(transport="http", host="localhost", port=8000) #HTTP transport example