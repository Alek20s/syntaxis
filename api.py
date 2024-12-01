from fastapi import FastAPI

app = FastAPI()

@app.get("/search_name/{word}")
async def search_game(word: str):
    return "Hello   " + word



# --- HOW  TO  RUN  THIS FILE ----------------
# wget -qO- http://127.0.0.1:8000/search_name/star
#  wget -qO- http://127.0.0.1:8000/search_name/Suns | jq -c '.[]'
# uvicorn api_search_keybin:app --reload
