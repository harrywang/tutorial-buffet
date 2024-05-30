# About
The examples at https://github.com/allegroai/clearml/tree/master/examples/frameworks

# Setup and Run

## Demo Server
By default, the results are logged to the demo server (no authorization configuration needed and all users SHARE all results!!): https://demoapp.demo.clear.ml/

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt 
$ pip install -r matplotlib/requirements.txt
$ python matplotlib/mlp_grouped_errorbar.py
```

Then follow the address in the terminal to view the result:

```
ClearML results page: https://demoapp.demo.clear.ml/projects/7b8167f284e0477389cd1d3701dad113/experiments/395a49ae59b2464299fddc479146fc27/output/log
```
<img width="1272" alt="Screen Shot 2020-12-22 at 7 11 25 PM" src="https://user-images.githubusercontent.com/595772/102944700-8b1bdf00-4489-11eb-9717-b327a2fb2de3.png">

### hyperparameter logging
In `pytorch/pytorch_mnist.py`, hypterparameters are specified using `argparse`:

```
parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--epochs', type=int, default=10, metavar='N',
                        help='number of epochs to train (default: 10)')
    parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                        help='learning rate (default: 0.01)')
    parser.add_argument('--momentum', type=float, default=0.5, metavar='M',
                        help='SGD momentum (default: 0.5)')
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
```
Then, the hypterparameters are used in the training/testing as follows:
```
optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)
```
### Result Logging

Log the results in the following way:

```
Logger.current_logger().report_scalar(
                "train", "loss", iteration=(epoch * len(train_loader) + batch_idx), value=loss.item())
Logger.current_logger().report_scalar(
        "test", "loss", iteration=epoch, value=test_loss)
Logger.current_logger().report_scalar(
        "test", "accuracy", iteration=epoch, value=(correct / len(test_loader.dataset)))
```

Run the example:

```
$ pip install -r pytorch/requirements.txt
$ python pytorch/pytorch_mnist.py
```

The results will show on the server as follows:

<img width="1000" src="https://user-images.githubusercontent.com/595772/104486720-28a29400-559a-11eb-80b4-d0a01d520308.png">

You can choose a number of experiments and compare the results:

<img width="494" alt="Screen Shot 2021-01-13 at 1 30 16 PM" src="https://user-images.githubusercontent.com/595772/104493952-cb134500-55a3-11eb-93fe-2219c7b1552d.png">

## ClearML Server or Self-Hosted Server

You can self host ClearML server by following my note at: https://github.com/harrywang/tutorial-buffet/tree/master/clearml-server

Once the server is up and running, you can login and get to the profile page to get the credentials.

Go to https://app.community.clear.ml/, login and go to profile page, create a new credential, you should see the following page:

<img width="1038" alt="Screen Shot 2020-12-27 at 2 37 40 PM" src="https://user-images.githubusercontent.com/595772/103178498-51fcb980-4851-11eb-9522-fab299acbf87.png">

Create `clearml.conf` with the information from the screen above: `$ vim ~/clearml.conf` or run `clearml-init` to setup the file step by step.

Now, run `$ python matplotlib/mlp_grouped_errorbar.py` again and your result is logged to the community server under your username (login required), e.g., https://app.community.clear.ml/projects/5a0ad99dd5b749d4931dee5da1e47870/experiments/7b9eae9bbd0a42bdbe887bf111c80b13/output/log


# Notes

1. 12/22/2020 - you have to lock PyJWT==1.7.1, the latest 2.0.0 breaks the system
2. when using matplotlib if you have problem with tkinter for certain python version, using agg instead:

```
import matplotlib
matplotlib.use('agg') # use agg instead of tkinter
```

See my example at `matplotlib/mlp_grouped_errorbar.py`, only need to add the following lines:

```
from trains import Task
task = Task.init(project_name='examples', task_name='Matplotlib GroupedBar example by Harry')
```