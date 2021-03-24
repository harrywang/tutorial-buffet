# About

Setup JupyterHub Server locally on Mac

Note: I set 6G for Docker

- Make sure docker is running correctly: `docker run hello-world`

```
docker pull jupyterhub/jupyterhub
```



https://www.arhea.net/posts/2020-06-18-jupyterhub-amazon-eks.html

beijing region: cn-north-1


aws ec2 create-key-pair --region us-west-2 --key-name myKeyPair

eksctl create cluster \
--name my-test-cluster \
--region cn-north-1 \
--with-oidc \
--ssh-access \
--ssh-public-key harrywang-tezign \
--managed

create a keypair harrywang-tezign
`aws configure` to make sure the user has the right permissions.