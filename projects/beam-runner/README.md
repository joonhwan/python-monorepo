## beam runner

Sample to run apache beam in multi project


## Usage

`for running local`

```shell script
poetry sync
poetry run python -m beam_runner
```

`for running cloud`

use docker
```shell script
docker build -t beam_runner -f Dockerfile ../../
docker run -it --rm beam_runner
```

use docker-compose
```shell script
docker-compose up --build
```

