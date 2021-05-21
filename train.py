import torch
from torch import nn, optim
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from dataset import Dataset
from model import Model


def train(dataset, model):
    model.train()
    dataloader = DataLoader(dataset, batch_size=128,shuffle=True)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    num_of_epochs = 35
    # Declare lists to store the respective values, inorder to plot graphs later
    epochs = []
    losses = []
    val_losses = []
    # Iterate the loop, for the number of epochs
    for epoch in range(num_of_epochs):
        state_h, state_c = model.init_state(100)
        state_h_val, state_c_val = model.init_state(100)
        cnt = 0
        val_cnt=0
        tot_loss = 0
        tot_val_loss = 0
        for batch, (x, y) in enumerate(dataloader):
            # Training (85% of the dataset)
            if (batch<46):
                # Set the value, zero all of the gradients for the variables
                optimizer.zero_grad()

                y_pred, (state_h, state_c) = model(x, (state_h, state_c))
                # Compute loss (here CrossEntropyLoss)
                loss = criterion(y_pred.transpose(1, 2), y)

                state_h = state_h.detach()
                state_c = state_c.detach()

                # Compute gradient of the loss with respect to all the learnable parameters of the model. 
                loss.backward()
                # update its parameters
                optimizer.step()

                # Calcuate the total loss
                tot_loss = tot_loss + loss
                cnt = cnt + 1

            # Validation using 15% of the dataset
            else:
                with torch.no_grad():
                    y_pred, (state_h_val, state_c_val) = model(x, (state_h_val, state_c_val))
                    # Compute loss (here CrossEntropyLoss)
                    val_loss = criterion(y_pred.transpose(1, 2), y)

                state_h_val = state_h_val.detach()
                state_c_val = state_c_val.detach()

                # Calcuate the total loss
                tot_val_loss = tot_val_loss + val_loss
                val_cnt = val_cnt + 1
        
        # Append the epochs number and the loss in thier lists
        epochs.append(epoch)
        losses.append((tot_loss/cnt))
        val_losses.append((tot_val_loss/val_cnt))
        print("epoch = {}  loss = {} val_loss = {} ".format(epoch, (tot_loss/cnt),(tot_val_loss/val_cnt)))

    # Saving the model
    torch.save(model.state_dict(), "manglish_model-ep" + str(num_of_epochs) + "-bs128.pth")

    # Plot a Validation Loss vs Epochs graph 
    plt.plot(epochs, val_losses, color='green', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=8) 
    plt.xlabel('epochs ---->',color='m',fontsize='xx-large' ) 
    plt.ylabel('valisdation loss ------>',color='m',fontsize='xx-large') 
    axes = plt.gca()        # 'gca' - get current axes
    axes.set_facecolor('c') #'c' - cyan
    axes.tick_params(axis='y', which='both', colors='tomato')
    axes.tick_params(axis='x', which='both', colors='#20ff14')
    plt.title("Val Loss vs Epoch",color='m',fontsize='xx-large')


if __name__ == "__main__":
    dataset = Dataset()
    model = Model()
    train(dataset,model)