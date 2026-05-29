from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

def format_validation_message(error: dict) -> str:
    error_type = error.get("type")
    field = error.get("loc", ["unknown"])[-1]

    if error_type == "literal_error":
        expected_values = error.get("ctx", {}).get("expected")
        return f"Valor inválido para o campo {field}. Valores permitidos: {expected_values}."

    if error_type == "greater_than_equal":
        min_value = error.get("ctx", {}).get("ge")
        return f"O campo {field} deve ser maior ou igual a {min_value}."

    if error_type == "less_than_equal":
        max_value = error.get("ctx", {}).get("le")
        return f"O campo {field} deve ser menor ou igual a {max_value}."

    if error_type == "missing":
        return f"O campo {field} é obrigatório."

    return f"Valor inválido para o campo {field}."

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    formatted_errors = []

    for error in exc.errors():
        location = error.get("loc", ["unknown"])[0]
        field = error.get("loc", ["unknown"])[-1]

        formatted_errors.append({
            "field": field,
            "location": location,
            "message": format_validation_message(error)
        })

    return JSONResponse(
        status_code=422,
        content={
            "message": "Erro de validação",
            "errors": formatted_errors
        }
    )