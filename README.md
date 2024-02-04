# python_data_science

For this project I use Docker to create a Python 3.10 development environment which I access using VSCode with the DevContainers extension.

docker build -t interactive-container .
docker run -it --mount type=bind,src="$(pwd)",target=/app interactive-container
Attach to Running Container
