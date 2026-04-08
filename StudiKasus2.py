#Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Menyiapkan himpunan fuzzy
kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101), 'ketersediaan_sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401), 'kepuasan_pelayanan')

#Menentukan fungsi keanggotaan untuk kejelasan informasi
kejelasan_informasi['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [0, 0, 60, 75])
kejelasan_informasi['Cukup Memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi['Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [75, 90, 100, 100]) 

#Menentukan fungsi keanggotaan untuk kejelasan persyaratan
kejelasan_persyaratan['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [0, 0, 60, 75])
kejelasan_persyaratan['Cukup Memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan['Memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [75, 90, 100, 100])

#Menentukan fungsi keanggotaan untuk kemampuan petugas
kemampuan_petugas['Tidak Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [0, 0, 60, 75])
kemampuan_petugas['Cukup Memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas['Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [75, 90, 100, 100])

#Menentukan fungsi keanggotaan untuk ketersediaan sarpras
ketersediaan_sarpras['Tidak Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [0, 0, 60, 75])
ketersediaan_sarpras['Cukup Memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [60, 75, 90])
ketersediaan_sarpras['Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [75, 90, 100, 100])

#Menentukan fungsi keanggotaan untuk kepuasan pelayanan
kepuasan_pelayanan['Tidak Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50, 75])
kepuasan_pelayanan['Kurang Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan['Cukup Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan['Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan['Sangat Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350, 400, 400])

#Aturan fuzzy
# =====================================================================
# KI = Tidak Memuaskan, KP = Tidak Memuaskan (rule 1-9)
# =====================================================================
rule1 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule2 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule3 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule4 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule5 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule6 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule7 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule8 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule9 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

# =====================================================================
# KI = Tidak Memuaskan, KP = Cukup Memuaskan (rule 10-18)
# =====================================================================
rule10 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule11 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule12 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule13 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule14 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule15 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule16 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule17 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule18 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

# =====================================================================
# KI = Tidak Memuaskan, KP = Memuaskan (rule 19-27)
# =====================================================================
rule19 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule20 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule21 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule22 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule23 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule24 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule25 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule26 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule27 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

# =====================================================================
# KI = Cukup Memuaskan, KP = Tidak Memuaskan (rule 28-36)
# =====================================================================
rule28 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule29 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule30 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule31 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule32 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule33 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule34 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule35 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule36 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

# =====================================================================
# KI = Cukup Memuaskan, KP = Cukup Memuaskan (rule 37-45)
# =====================================================================
rule37 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule38 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule39 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule40 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule41 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule42 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule43 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule44 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule45 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

# =====================================================================
# KI = Cukup Memuaskan, KP = Memuaskan (rule 46-54)
# =====================================================================
rule46 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule47 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule48 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule49 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule50 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule51 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule52 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule53 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule54 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

# =====================================================================
# KI = Memuaskan, KP = Tidak Memuaskan (rule 55-63)
# =====================================================================
rule55 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Tidak Memuaskan'])
rule56 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule57 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule58 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule59 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule60 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule61 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule62 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule63 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

# =====================================================================
# KI = Memuaskan, KP = Cukup Memuaskan (rule 64-72)
# =====================================================================
rule64 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule65 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule66 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule67 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule68 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule69 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule70 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule71 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule72 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

# =====================================================================
# KI = Memuaskan, KP = Memuaskan (rule 73-81)
# =====================================================================
rule73 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule74 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule75 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule76 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule77 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule78 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule79 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule80 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule81 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

pelayanan_ctrl = ctrl.ControlSystem([
    rule1,  rule2,  rule3,  rule4,  rule5,  rule6,  rule7,  rule8,  rule9,
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,
    rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36,
    rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45,
    rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54,
    rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63,
    rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72,
    rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81,
])
pelayanan_sim = ctrl.ControlSystemSimulation(pelayanan_ctrl)

pelayanan_sim.input['kejelasan_informasi'] = 80
pelayanan_sim.input['kejelasan_persyaratan'] = 60
pelayanan_sim.input['kemampuan_petugas'] = 50
pelayanan_sim.input['ketersediaan_sarpras'] = 90
pelayanan_sim.compute()

print(f"Nilai Kepuasan Pelayanan: {pelayanan_sim.output['kepuasan_pelayanan']:.2f}")
kepuasan_pelayanan.view(sim=pelayanan_sim)
input("Tekan ENTER untuk melanjutkan")