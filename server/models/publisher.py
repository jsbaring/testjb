from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """Model representing a game publisher.
    
    Publishers create and distribute games seeking crowdfunding. Each publisher
    can have multiple games associated with them on the platform.
    """
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key, name):
        """Validate the publisher name field.
        
        Args:
            key: The field name being validated
            name: The publisher name value
            
        Returns:
            The validated name
            
        Raises:
            ValueError: If name is invalid
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """Validate the publisher description field.
        
        Args:
            key: The field name being validated
            description: The publisher description value
            
        Returns:
            The validated description
            
        Raises:
            ValueError: If description is invalid
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self):
        """Return string representation of the publisher.
        
        Returns:
            A string representation of the publisher
        """
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """Convert the publisher to a dictionary representation.
        
        Returns:
            A dictionary containing the publisher's data including id, name,
            description, and count of associated games
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }