"""
Example: Data Extraction Agent

This example demonstrates extracting structured data from unstructured text.
"""
import asyncio
from typing import List

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from loguru import logger


class Person(BaseModel):
    """Structured person information."""
    name: str
    age: int
    occupation: str
    skills: List[str] = Field(default_factory=list)


class DataExtractionExample:
    """Extract structured data from text."""
    
    def __init__(self):
        """Initialize the data extraction agent."""
        self.agent = Agent(
            "openai:gpt-4",
            result_type=Person,
            system_prompt="""Extract person information from the text.
            Be accurate and only extract information that is present."""
        )
        logger.info("Data extraction agent initialized")
    
    async def extract(self, text: str) -> Person:
        """Extract person data from text.
        
        Args:
            text: The text to extract from
            
        Returns:
            Structured Person data
        """
        logger.debug(f"Extracting data from: {text}")
        result = await self.agent.run(text)
        logger.debug(f"Extracted: {result.data}")
        return result.data


async def main():
    """Run the data extraction example."""
    extractor = DataExtractionExample()
    
    # Example texts
    examples = [
        "John Smith is a 35-year-old software engineer who specializes in Python, AI, and cloud computing.",
        "Meet Sarah Johnson, age 28. She works as a data scientist and has expertise in machine learning and statistics.",
    ]
    
    print("=" * 60)
    print("Data Extraction Example")
    print("=" * 60)
    
    for text in examples:
        print(f"\n📄 Input Text:\n{text}")
        person = await extractor.extract(text)
        print(f"\n✅ Extracted Data:")
        print(f"   Name: {person.name}")
        print(f"   Age: {person.age}")
        print(f"   Occupation: {person.occupation}")
        print(f"   Skills: {', '.join(person.skills)}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
