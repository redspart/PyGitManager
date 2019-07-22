 
CONTAINER_NAME=buildMePythoScope
ARTIFACT_DESIRED=unittest.tar
docker build -t builder -f BuildPythoScope.Dockerfile .
docker rm $CONTAINER_NAME
#ßdocker run -it -v /tmp/deploy-ready/:/Build/output builder  
docker run --name $CONTAINER_NAME  builder 
#docker run -it --name buildmecentos -v /tmp/deploy-ready/:/Build/output builder cp switchboard_centos_6_10.tar /Build/output/
rm -rf _unittest/*
mkdir _unittest/
docker cp $CONTAINER_NAME:/$ARTIFACT_DESIRED _unittest/$ARTIFACT_DESIRED
tar -xvf _unittest/$ARTIFACT_DESIRED -C _unittest/ 
# debug docker --rm -it <hash> sh