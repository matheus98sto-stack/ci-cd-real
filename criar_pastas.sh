#!/bin/bash
mkdir -p .github/workflows && cd .github/workflows && touch ci.yml && touch deploy.yml
cd ../../
mkdir src && cd src
mkdir config && mkdir controllers && mkdir models && mkdir routes && mkdir services && mkdir utils
cd ..
mkdir tests
touch Dockerfile && touch package.json
