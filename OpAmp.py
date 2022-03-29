# **************************************************************************************************************************************************************************************************** #
# ******************************************************************* 8. To study the op amp as an inverting and non-inverting amplifier. ************************************************************ #
# **************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Units of like Physical Quantities are assumed to be in same unit system.
    - All Testings have been logged into the terminal for future debuggings.
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #



n = 5                                                                   # For storing the Number of Observations
Vin = [5, 4, 3, 2, 1]                                                   # For storing the Input Voltages(Vin)
Vout = [10, 8, 6, 4, 2]                                                 # For storing the Output Voltages(Vout)
V = {'Vin': Vin, 'Vout': Vout}                                          # For storing and grouping the 2 Voltages(Vin and Vout) together
R1 = [1, 2, 3, 4, 5]                                                    # For storing the Values of the First Resistance(R1)_ in the OpAmp's Circuit
R2 = [0.5, 1, 1.5, 2, 2.5]                                              # For storing the the Values of the Second Resistance(R2)_ in the OpAmp's Circuit
R = {'R1': R1, 'R2': R2}                                                # For storing and grouping the 2 Voltages(R1 and R2) together



# **************************************************************************************** Section ends here ***************************************************************************************** #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ************************ For Simulating a Virtual OpAmp(Operational Amplifier) and Finding the Readings based on the Theoretical and Experimental Values of the Voltage Gain *********************** #



def calTheoreticalVoltageGain(R, opt = 'n'):                                                           # For Calculating the Theoretical Voltage Gain
    return list(map(lambda o, i: 1 + i / o, list(R.values())[0], list(R.values())[1])) if opt == 'n' else list(map(lambda o, i: -(1 + i / o), list(R.values())[0], list(R.values())[1]))

# Testing-
Av_theoretical = calTheoreticalVoltageGain(R, 'i')
print('Theoretical Reading(s) for Voltage Gain =', end = ' ')
print(*Av_theoretical, sep = ', ')


def calExperimentalVoltageGain(V, opt= 'n'):                                                          # For Calculating the Experimental Voltage Gain
    return list(map(lambda o, i: o / i, list(V.values())[1], list(V.values())[0])) if opt == 'n' else list(map(lambda o, i: -(o / i), list(V.values())[1], list(V.values())[0]))

# Testing-
Av_experimental = calExperimentalVoltageGain(V, 'i')
print('Experimental Reading(s) for Voltage Gain Av =', end = ' ')
print(*Av_experimental, sep = ', ')


def calSignedError(Av_theoretical, Av_experimental):                                                  # For Calculating the Signed Error in the Theoretical and Experimental Readings
    return list(map(lambda theo, exp: theo - exp, Av_theoretical, Av_experimental))

# Testing-
signed_err = calSignedError(Av_theoretical, Av_experimental)
print('Signed Error(s) =', end = ' ')
print(*signed_err, sep = ', ')


def calAbsoluteError(signed_err):                                                                     # For Calculating the Absolute Error in the Theoretical and Experimental Readings
    return list(map(lambda err: abs(err), signed_err))

# Testing-
abs_err = calAbsoluteError(signed_err)
print('Absolute Error(s) =', end = ' ')
print(*abs_err, sep = ', ')

def calRelativeError(abs_err, Av_theoretical):                                                        # For Calculating the Relative Error in the Theoretical and Experimental Readings
    return list(map(lambda err, theo: abs(err / theo), abs_err, Av_theoretical))

# Testing-
rel_err = calRelativeError(abs_err, Av_theoretical)
print('Relative Error(s) =', end = ' ')
print(*rel_err, sep = ', ')


def calPercentageError(rel_err):                                                                      # For Calculating the Percentage Error in the Theoretical and Experimental Readings
    return list(map(lambda rel: abs(rel) * 100, rel_err))

# Testing-
signed_err = calPercentageError(rel_err)
print('Percentage Error(s) =', end = ' ')
print(*list(map(lambda err: str(err) + '%', signed_err)), sep = ', ')



# ********************************************************************************* Section ends here ************************************************************************************************ #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #




