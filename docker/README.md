# SoloLa docker Image
> 

We provide an docker image for SoloLa python3.5 . Check out the image on Docker Hub

> https://hub.docker.com/r/ykhorizon/solola-py35/

## Solola script
### Dependency

We use essentia docker image as base images:

- ubuntu:16.04 (latest ubuntu LTS)

Other dependency check out [SoloLa Requirements](https://github.com/SoloLa-Platform/SoloLa/tree/dev_version)


### Usage 
You have to place target_audio under [host_dir] (take [host_dir] as root)
<pre> 
docker run -ti --rm -v [host_dir]:/solola ykhorizon/solola-py35:prod python3 main.py [path_target_audio_with_mp3_format]
</pre>




## Service

### Introduction
If you want to use integrated service(Flask), you use follow usage instructions


### Usage
```bash
# run script
python
# start API service without docker(transcription)
python3 services/API/api.py
```

development
```bash
docker run -it --name test -p 5000:5000 solola_api:0.9.3
```

testing entry.sh
```bash
docker run -it --rm -p 5000:5000 -v [wsl_project_path]:/home/solola solola_api:0.9.3
```
### Build Image
<pre>
cd [project_root]
docker build -t solola_api:[tag] -f docker/Dockerfile.pipenv.dev 
</pre>