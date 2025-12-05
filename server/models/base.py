# filepath: server/models/base.py
from . import db

class BaseModel(db.Model):
    """Base model class for all database models.
    
    Provides common validation methods and functionality for all models.
    This is an abstract base class and should not be instantiated directly.
    """
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name, value, min_length=2, allow_none=False):
        """Validate that a string field meets length requirements.
        
        Args:
            field_name: The name of the field being validated (for error messages)
            value: The string value to validate
            min_length: Minimum required length (default: 2)
            allow_none: Whether None values are allowed (default: False)
            
        Returns:
            The validated string value
            
        Raises:
            ValueError: If validation fails
        """
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value