Create a IAM Role for EKS Service Role. It should have the following policies

AmazonEKSClusterPolicy

AmazonEKSServicePolicy

AmazonEC2ContainerRegistryReadOnly

(From the user interface, select EKS as the service, then follow the default steps)

<img width="975" alt="Screen Shot 2021-02-19 at 4 02 37 PM" src="https://user-images.githubusercontent.com/595772/108561437-44e9cd00-72cc-11eb-9ea5-282f4e8486aa.png">
<img width="970" alt="Screen Shot 2021-02-19 at 4 05 09 PM" src="https://user-images.githubusercontent.com/595772/108561443-46b39080-72cc-11eb-9d2c-bd143f8586bf.png">



Create a VPC if you don’t already have one. This step has a lot of variability so it is left to the user. However, one deployment can be found at Getting Started with Amazon EKS, under Create your Amazon EKS Cluster VPC

used the default one

Create a Security Group for the EKS Control Plane to use You do not need to set any permissions on this. The steps below will automatically define access control between the EKS Control Plane and the individual nodes
<img width="1201" alt="Screen Shot 2021-02-19 at 3 58 40 PM" src="https://user-images.githubusercontent.com/595772/108560862-5da5b300-72cb-11eb-8d0d-60fb95f0a186.png">


Create your EKS cluster (using the user interface) Use the IAM Role in step 1 and Security Group defined in step 3. The cluster name is going to be used throughout. We’ll use Z2JHKubernetesCluster as an example.
<img width="916" alt="Screen Shot 2021-02-19 at 3 59 41 PM" src="https://user-images.githubusercontent.com/595772/108560969-7f9f3580-72cb-11eb-8abf-b0276724ebd7.png">

<img width="908" alt="Screen Shot 2021-02-19 at 4 05 44 PM" src="https://user-images.githubusercontent.com/595772/108561585-837f8780-72cc-11eb-952d-685c9555d36b.png">
<img width="752" alt="Screen Shot 2021-02-19 at 4 06 14 PM" src="https://user-images.githubusercontent.com/595772/108561586-84b0b480-72cc-11eb-9a69-d8870aa46269.png">

Install kubectl and aws-iam-authenticator Refer to Getting Started with Amazon EKS on Configure kubectl for Amazon EKS
https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html

https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html



`curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.18.9/2020-11-02/bin/darwin/amd64/kubectl`
Configure kubeconfig Also see Getting Started with Amazon EKS Step 2: Configure kubectl for Amazon EKS

From the user interface on AWS you can retrieve the endpoint-url, base64-encoded-ca-cert. cluster-name is the name given in step 4. If you are using profiles in your AWS configuration, you can uncomment the env block and specify your profile as aws-profile.: