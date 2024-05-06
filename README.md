# staticSiteGenerator

Converts markdown to html and injects it into the template.html. Copies it to the public dir for hosting.
running `./main.sh` will process the markdown and serve the site at http://localhost:8888/
Assumes all files in `content` are markdown

Uses Python 3.12+