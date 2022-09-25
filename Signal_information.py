from Lightpath import Lightpath

class SignalInformation(Lightpath):

    def __init__(self, signal_power, path):
        super().__init__(signal_power, path, 0)
        self._signal_power = signal_power
        self._noise_power = 0
        self._latency = 0
        self._path = path
        self.Rs = 32e9
        self.df = 50e9

    def increase_noise(self, noise_power):
        self._noise_power += noise_power

    def increase_latency(self, latency):
        self._latency += latency

    def next(self):
        self._path = self._path[1:]

    @property
    def path(self):
        return self._path

    def getlatency(self):
        return self._latency

    def getnoisepower(self):
        return self._noise_power

    def getsignalpower(self):
        return self._signal_power