from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass
class NavigatorDeps:
    user_name: str
    difficulty: str


class CourseReference(BaseModel):
    path: str = Field(description="The file path to the learning module")
    title: str = Field(description="The title of the module")


class CourseAnswer(BaseModel):
    summary: str = Field(description="A personalized summary of the requested info")
    references: list[CourseReference] = Field(
        description="List of relevant files used",
    )
