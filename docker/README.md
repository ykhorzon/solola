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
docker run -ti --rm -p 5000:5000 -v E:\workplace\projects\solola\solola\:/solola solola_api/pipenv:1.0 bash
pipenv shell

# run script
python
# start API service
python3 services/API/api.py
```

```
docker run -ti --rm -p 5000:5000 -v E:\workplace\projects\solola\solola\:/solola solola_api/pipenv:1.0 bash
cd /solola
pipenv install
```


### Build Image
<pre>
cd [project_root]
docker build -t solola_api/pipenv:[tag] -f docker/Dockerfile.pipenv.dev .
</pre>