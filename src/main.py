from fastapi import FastAPI, HTTPException, Request
from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is only for testing out that heroku works
@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/translateposttext/")
async def queryTranslatePosttext(request: Request):
    req = await request.body()
    req = json.loads(req)

    translator = Translator()
    # Return if body is empty
    if not req:
        return ''
    try:
        return translator.translate(req).text
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")

@app.post("/translatepostfull/")
async def queryTranslatePostJSON(request: Request):
    req = await request.body()
    req = json.loads(req)

    translator = Translator()
    # Return if body is empty
    if not req:
        return ''
    try:
        return translator.translate(req)
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")




@app.get("/translategetfull/")
async def queryTranslateGetJSON(query=''):
    translator = Translator()
    # Return if query is empty
    if not query:
        return ''
    try:
        return translator.translate(query)
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")



# https://www.tutlinks.com/create-and-deploy-fastapi-app-to-heroku/
# https://fastapi.tiangolo.com/tutorial/first-steps/
@app.get("/translategettext/")
async def queryTranslateGetText(query=''):
    translator = Translator()
    # Return if query is empty
    if not query:
        return ''
    try:
        return translator.translate(query).text
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")
# @app.get("/headers/")
# async def read_items(request: Request):
#    header = dict(request.headers)
#    header.pop("origin", None)
#    header.pop("referer", None)
#    header.pop("host", None)
#    header["accept-encoding"] = "gzip, deflate"
#    del header['referer']
#    return {"User-Agent": header}


#abc = '["1","2","3"]'
#k = json.loads(abc)
# print(k[0])
#    import httpx
#    r = httpx.get('https://www.google.com/search?q=how+to+repair+a+mouse',headers=header)

#    headerz = {'user-agent': header['user-agent']}
#    print("this is headerz", headerz)
# https://www.google.com/search?q=word+based+dictionary


#    r = httpx.get('https://httpbin.org/gzip', headers=header)
# https://www.starlette.io/responses/
#    return Response(content=r.text, headers=r.headers)
#    return Response
#    r.headers['Access-Control-Allow-Origin'] = '*'
# if r.headers['content-type'].startswith('text/'):
#        return Response(content=r.text, media_type="text/html")
#    return ""
#    return Response(r)
#    return {"message": header}

# install brotoli py to support br encoding

# @app.post()
# https://fastapi.tiangolo.com/tutorial/handling-errors/

#import httpx
#r = httpx.get('https://www.google.com/search?q=how+to+repair+a+computer+chair')
# print(r.text)
