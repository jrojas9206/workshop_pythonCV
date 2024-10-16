class SimpleBike:

    OBJECT_NAME = 'sBike'

    def __init__(self):
        self._colorFrame = '#000000' # RRGGBB R = red B = Blue G = Green
        self._colorWheels = '#00FF00' # Green Weels 
        self._weight = 1 # Kg
        self._frame = [] # Points to draw 
        self._wheels = 2.0 # Inches  
        self._maxSpeed = 20 # Km/sec
        self._minSpeed = 1/2.0 # Km/sec  
        self._position = [0,0] # x,y
        self._trajectory = {'speed':[], 
                            'time':[],
                            'positions':[]}
    
    def move(self, speed, period):
        '''
            Do something
        '''
        return {}
    
    def breakOn(self):
        '''
            Do something
        '''

    def turn(self):
        '''
            Do something
        '''
        