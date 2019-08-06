To run docker image use this command:
'''
docker run --name container-name -v volume-name:/app/plarforms_branches -p port:port -e PORT=port -e PLATFORMS=list-of-platforms image-name
'''
for example:
'''
docker run --name swagger -v swagger-volume:/app/platforms_branches -p 5000:5000 -e PLATFORMS="web gift" swagger-image
'''
BY DEFAULT
PORT = 5000
PLATFORMS = "web server mobile gift"

