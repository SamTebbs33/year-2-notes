import Network.HTTP
import Text.JSON

apiUrl = "http://version1.api.memegenerator.net/Instance_Create"
doRequest imageID text1 text2 = simpleHTTP (getRequest (apiUrl ++ ("?username=SamTebbs33&password=vmfqba&languageCode=en&imageID=" ++ imageID ++ "&text0=" ++ text1 ++ "&text1=" ++ text2 ++ "&generatorID=6627881"))) >>= getResponseBody
getMemed = doRequest
