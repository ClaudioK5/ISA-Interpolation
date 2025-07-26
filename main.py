import bisect

class ISAInterpolation:

    #this class method allows you to calculate as realistical as possible all the properties
    #such as temperature, pressure and density at any particular altitude.

    #This calculation is valid only for altitudes between 0 and 20,000 meters.

    def __init__(self):

        self.Altitudes = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000]
        self.Temperatures = [288.2, 281.7, 275.2, 268.7, 262.2, 255.7, 249.2, 242.7, 236.2, 229.7, 223.2, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7]
        self.Pressures = [101.30, 89.85, 79.47, 70.08, 61.61, 53.99, 47.16, 41.04, 35.58, 30.72, 26.42, 22.62, 19.32, 16.50, 14.09, 12.04, 10.28, 8.78, 7.50, 6.40, 5.47]
        self.Densities = [1.225, 1.111, 1.006, 0.909, 0.819, 0.736, 0.659, 0.589, 0.525, 0.466, 0.412, 0.364, 0.311, 0.265, 0.227, 0.194, 0.165, 0.141, 0.121, 0.103, 0.088]

    def interpolation(self,height):

        i = bisect.bisect_left(self.Altitudes, height)

        try:

           T = self.Temperatures[i-1] + ((height - self.Altitudes[i-1])/(self.Altitudes[i] - self.Altitudes[i-1]))*(self.Temperatures[i] - self.Temperatures[i-1])

           P = self.Pressures[i-1] + ((height - self.Altitudes[i-1])/(self.Altitudes[i] - self.Altitudes[i-1]))*(self.Pressures[i] - self.Pressures[i-1])

           D = self.Densities[i-1] + ((height - self.Altitudes[i-1])/(self.Altitudes[i] - self.Altitudes[i-1]))*(self.Densities[i] - self.Densities[i-1])
  
           return  {"Temperature (K)": T, "Pressure (kPa)": P, "Densities kg m^-3": D}
        
        except Exception as e:

           return  print(f"An error has occurred during interpolation: {e}")
        
      

 