

class WaitingTime:
    def __init__(self, nCapacity : int, treatmentTime : float, arrivalRate : float) -> None:
        self.nCapacity = nCapacity
        self.treatmentTime = treatmentTime
        self.arrivalRate = arrivalRate
        self.clock = 0.0
        self.patientsInTreatment = 0
        self.patientsInQueue = 0
    
    def arrival(self, numPatient : int, time : float):
        self.clock += time
        self.patientsInQueue += numPatient

    def newTreatment(self):
        self.patientsInQueue -= 1
        self.patientsInTreatment += 1
    
    def expectedWaitingTime(self):
        if self.patientsInTreatment < self.nCapacity:
            return 
        
    
    
        