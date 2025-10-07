from cereal import car  
from opendbc.car.common.conversions import Conversions as CV  
  
class FixedCarState:  
    def __init__(self):  
        self.fixed_speed_ms = 120 * CV.KPH_TO_MS  # 120 km/h to m/s  
          
    def update(self, CS: car.CarState) -> car.CarState:  
        # Inject fixed values for hardware without Panda  
        CS.vEgo = self.fixed_speed_ms  
        CS.vEgoRaw = self.fixed_speed_ms    
        CS.vEgoCluster = 120.0  # Display speed in km/h  
        CS.standstill = False  
          
        # No braking  
        CS.brake = 0.0  
        CS.brakePressed = False  
        CS.regenBraking = False  
        CS.brakeHoldActive = False  
          
        # Blinkers off  
        CS.leftBlinker = False  
        CS.rightBlinker = False  
          
        # Ensure CAN validity for system operation  
        CS.canValid = True  
        CS.canTimeout = False  
          
        return CS
