import json

with open('scrapy-Bayut-Data-Extraction-main/a.json') as f:
  data = json.load(f)
  val=json.dumps(data)
  with open("output.json", "w") as outfile:
    outfile.write(json.dumps(json.loads(val),indent=4))
