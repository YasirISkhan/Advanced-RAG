from typing import Optional, Annotated, Literal
from pydantic import BaseModel, EmailStr, Field
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'CohereLabs/tiny-aya-global',
    task = 'text-generation'
)

class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive, or neutral.")
    pros: Optional[list[str]] = Field(description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

model = ChatHuggingFace(llm=llm)

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I bought this smartphone last week, and honestly, it’s a total mixed bag. Let's start with the positives: the design is absolutely stunning, and the battery life is a beast—it easily lasts me two full days of heavy usage without needing a charge. The camera takes beautiful daylight photos too. BUT, the actual user experience is where everything falls apart completely. The operating system is incredibly laggy right out of the box, and it is choked with ridiculous bloatware that you cannot uninstall. Every time I open the camera app, it freezes for three seconds before taking a picture, causing me to miss the shot. Aggravating! If you only care about aesthetics and battery, you might look past these flaws, but for me, a phone has to actually run smoothly. I’m seriously considering returning it before my 14-day window closes.""")


print(result)