#Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Menyiapkan himpunan fuzzy
barang_terjual = ctrl.Antecedent(np.arange(0,101), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0,301), 'permintaan')
harga_item = ctrl.Antecedent(np.arange(0,100001), 'harga_item')
profit = ctrl.Antecedent(np.arange(0,4000001), 'profit')
stok_makanan = ctrl.Consequent(np.arange(0,1001), 'stok_makanan')

#Menentukan fungsi keanggotaan untuk barang terjual
barang_terjual['Rendah'] = fuzz.trimf(barang_terjual.universe, [0, 0, 40])
barang_terjual['Sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['Tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 100, 100])

#Menentukan fungsi keanggotaan untuk permintaan
permintaan['Rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['Sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['Tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

#Menentukan fungsi keanggotaan untuk harga item
harga_item['Murah'] = fuzz.trimf(harga_item.universe, [0, 0, 40000])
harga_item['Sedang'] = fuzz.trimf(harga_item.universe, [30000, 50000, 80000])
harga_item['Mahal'] = fuzz.trimf(harga_item.universe, [60000, 100000, 100000])

#Menentukan fungsi keanggotaan untuk profit
profit['Rendah'] = fuzz.trimf(profit.universe, [0, 0, 1000000])
profit['Sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['Tinggi'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

#Menentukan fungsi keanggotaan untuk stok makanan
stok_makanan['Sedang'] = fuzz.trimf(stok_makanan.universe, [100, 500, 900])
stok_makanan['Banyak'] = fuzz.trimf(stok_makanan.universe, [600, 1000, 1000])

#Aturan fuzzy
rule1 = ctrl.Rule(barang_terjual['Tinggi'] & permintaan['Tinggi'] & harga_item['Murah'] & profit['Tinggi'], stok_makanan['Banyak'])
rule2 = ctrl.Rule(barang_terjual['Tinggi'] & permintaan['Tinggi'] & harga_item['Murah'] & profit['Sedang'], stok_makanan['Sedang'])
rule3 = ctrl.Rule(barang_terjual['Tinggi'] & permintaan['Sedang'] & harga_item['Murah'] & profit['Sedang'], stok_makanan['Sedang'])
rule4 = ctrl.Rule(barang_terjual['Sedang'] & permintaan['Tinggi'] & harga_item['Murah'] & profit['Sedang'], stok_makanan['Sedang'])
rule5 = ctrl.Rule(barang_terjual['Sedang'] & permintaan['Tinggi'] & harga_item['Murah'] & profit['Tinggi'], stok_makanan['Banyak'])
rule6 = ctrl.Rule(barang_terjual['Rendah'] & permintaan['Rendah'] & harga_item['Sedang'] & profit['Sedang'], stok_makanan['Sedang'])
stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
stok_sim = ctrl.ControlSystemSimulation(stok_ctrl)

stok_sim.input['barang_terjual'] = 80
stok_sim.input['permintaan'] = 255
stok_sim.input['harga_item'] = 25000
stok_sim.input['profit'] = 3500000
stok_sim.compute()

print(f"Stok Makanan: {stok_sim.output['stok_makanan']}")
stok_makanan.view(sim=stok_sim)
input("Tekan ENTER untuk melanjutkan")