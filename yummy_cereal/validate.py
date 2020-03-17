from dataclasses import dataclass
from typing import Any, Callable, NoReturn, Optional

from multi_job.models.exceptions import ParserValidationError


@dataclass
class Result:
    success: bool
    details: Optional[str] = None


@dataclass
class Validator:
    category: str
    subcategory: str
    check: Callable[..., Result]

    def validate(self, config: Any) -> None:
        """
        Apply the validator's check method and call its reject method if the
        result is a failure
        
        Args:
            config (Any): Validation target
        """
        result = self.check(config)
        if not result.success:
            self.reject(result.details)

    def reject(self, details: Optional[str]) -> NoReturn:
        """
        Raise a ParserValidationError with a formatted error message
        
        Args:
            details (Optional[str]): The specific case of failure reported in the check's result
        
        Raises:
            ParserValidationError:
 
        Returns:
            NoReturn:
        """
        msg = f"The config file failed validation.\nIssue catagory: {self.category}\nIssue subcatagory: {self.subcategory}\nDetails: {details}"
        raise ParserValidationError(msg)


def validate(config_path: str) -> dict:
    """Apply all validation functions to the given configuration
    
    Args:
        config_path (str): Path to the configuration file
    
    Returns:
        Any: Validated configuration
    """
    config = read(config_path)

    # Validate structure first to allow simpler validator designs
    for validator in []:
        validator.validate(config)
    return config
