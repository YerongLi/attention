import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import copy
import math
import time
from torch.autograd import Variable
import matplotlib.pyplot as plt
import seaborn
seaborn.set_context(context='talk')
class EncoderDecoder(nn.Module):
    '''
        encoder: 
        decoder:

    '''
    def __init(self, encoder, decoder):
        self.encoder = encoder
        self.decoder = decoder