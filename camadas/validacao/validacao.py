from typing import Any, Dict, Type

class Validacao:
    def validar(self, campo: str, valor: Any):
        raise NotImplementedError(
            "Este método deve ser implementado pelas subclasses.")

# Specific Validators (Subclasses of Validacao)

class CpfValidator(Validacao):
    def validar(self, campo: str, valor: str):
        valor = str(valor).replace(".", "").replace("-", "").replace(" ", "")
        if len(valor) != 11 or not valor.isnumeric():
            raise ValueError("CPF deve ter 11 dígitos numéricos.")


class NomeValidator(Validacao):
    def validar(self, campo: str, valor: str):
        if not valor:
            raise ValueError("Nome é obrigatório.")


class DataNascimentoValidator(Validacao):
    def validar(self, campo: str, valor: str):
        if not valor:
            raise ValueError("Data de nascimento é obrigatória.")
        try:
            dia, mes, ano = map(int, valor.split("/"))
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900):
                raise ValueError(
                    "Data de nascimento deve estar no formato DD/MM/AAAA.")
        except ValueError:
            raise ValueError(
                "Data de nascimento deve estar no formato DD/MM/AAAA.")
        if valor.count("/") != 2:
            raise ValueError(
                "Data de nascimento deve estar no formato DD/MM/AAAA.")


class TelefoneValidator(Validacao):
    def validar(self, campo: str, valor: str):
        valor = str(valor).replace("(", "").replace(")",
                                                    "").replace("-", "").replace(" ", "")
        if len(valor) > 11 or len(valor) < 8:
            raise ValueError("Telefone deve ter até 11 dígitos (com DDD).")


class EmailValidator(Validacao):
    def validar(self, campo: str, valor: str):
        if "@" not in valor:
            raise ValueError("Email é inválido.")


class SexoValidator(Validacao):
    def validar(self, campo: str, valor: str):
        if valor not in ["M", "F", "Outro"]:
            raise ValueError("Sexo deve ser 'M', 'F' ou 'Outro'.")
        

class IgnorarValidator(Validacao):
    def validar(self, campo: str, valor: Any):
        pass

# Validator Factory

class ValidatorFactory:
    VALIDATORS: Dict[str, Type[Validacao]] = {
        "cpf": CpfValidator,
        "nome": NomeValidator,
        "data_nascimento": DataNascimentoValidator,
        "telefone": TelefoneValidator,
        "email": EmailValidator,
        "sexo": SexoValidator,
        "endereco": IgnorarValidator,
        "id": IgnorarValidator,
    }

    @staticmethod
    def get_validator(campo: str) -> Validacao:
        validator_class = ValidatorFactory.VALIDATORS.get(campo)
        if not validator_class:
            raise ValueError(
                f"Nenhum validador disponível para o campo: {campo}")
        return validator_class()
