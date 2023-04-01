
import typing
from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class ChatGPTJailbreakFinderIn(BaseModel):
    url: str
    google_sheet_id: str


class ChatGPTJailbreakFinderOut(BaseModel):
    top_jailbreaks: List[str]


class ChatGPTJailbreakFinder(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: ChatGPTJailbreakFinderIn, callbacks: typing.Any
    ) -> ChatGPTJailbreakFinderOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        top_jailbreaks = results_dict['top_jailbreaks']
        out = ChatGPTJailbreakFinderOut(top_jailbreaks=top_jailbreaks)
        return out

load_dotenv()
chatgpt_jailbreak_finder_app = FastAPI()


@chatgpt_jailbreak_finder_app.post("/transform/")
async def transform(
    args: ChatGPTJailbreakFinderIn,
) -> ChatGPTJailbreakFinderOut:
    chatgpt_jailbreak_finder = ChatGPTJailbreakFinder()
    return await chatgpt_jailbreak_finder.transform(args, callbacks=None)
