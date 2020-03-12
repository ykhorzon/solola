# SoloLa python 3.5 Docker Image

> 

We provide an docker image for SoloLa python3.5 . Check out the image on Docker Hub

> https://hub.docker.com/r/ykhorizon/solola-py35/


## Dependency

We use essentia docker image as base images:

- ubuntu:16.04 (latest ubuntu LTS)

Other dependency check out [SoloLa Requirements](https://github.com/SoloLa-Platform/SoloLa/tree/dev_version)


## Usage 
You have to place target_audio under [host_dir] (take [host_dir] as root)
<pre> 
docker run -ti --rm -v [host_dir]:/solola ykhorizon/solola-service:0.1 python3 main.py [path_target_audio_with_mp3_format]

# image: solola-py35:prod
docker run -ti --rm -v [host_input_dir]:/solola/inputs -v [host_output_dir]:/solola/outputs ykhorizon/solola-service:0.1 python3 main.py inputs/test.mp3

# quick test
cd $SOLOLA_HOME/
docker run -ti --rm -v ${PWD}:/solola ykhorizon/solola-service:0.1 python3 main.py inputs/test.mp3

# dive into env.
cd $SOLOLA_HOME/
docker run -ti --rm  -v /e/workplace/projects/solola/solola:/solola -p 5000:5000 ykhorizon/solola-service:0.1 bash
</pre>

## Build
docker build -t ykhorizon/solola-service:0.1 -f docker/dev.Dockerfile  .
