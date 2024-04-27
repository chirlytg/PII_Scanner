from burp import IBurpExtender, IHttpListener

# Basado en: https://github.com/everythingishacked/burpsuite-custom-extension/blob/master/cloud2butt.py

class BurpExtender(IBurpExtender, IHttpListener):
    # Define the BurpExtender class implementing IBurpExtender and IHttpListener interfaces.
  def registerExtenderCallbacks(self, callbacks):
    # Method to register extension callbacks.
    self._callbacks = callbacks
    self._helpers = callbacks.getHelpers()
    callbacks.registerHttpListener(self)
    callbacks.setExtensionName("PII Scanner")
    print("Loading Extension 1")

  def getResponseHeadersAndBody(self, content):
    # Method to retrieve headers and body from an HTTP response.
    response = content.getResponse()
    response_data = self._helpers.analyzeResponse(response)
    headers = list(response_data.getHeaders() or '')
    body = response[response_data.getBodyOffset():].tostring()
    return headers, body

  def processHttpMessage(self, tool, is_request, content):
    # Method to process an HTTP message (either request or response).
    if is_request:
      return
    headers, body = self.getResponseHeadersAndBody(content)
    # If the response body contains "CPF", print a message indicating PII detection.
    if "CPF" in body:
      print("Se ha detectado un CPF")
      #print(body)