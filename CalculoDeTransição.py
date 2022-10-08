#Calculo de valores para nutrição animal
#ENN (%) = 100 – (Umidade + PB + EEA + FB + MM)
#EB (kcal/kg) = (5,7 x PBG) + (9,4 x EEAG) + [(ENNG + FBG)]
#CDE (%) = 91,2 - (1,43 x FB na Matéria SECA (Ou seja ( VALOR DE FB/(100-VALOR DE UMIDADE)
#ED (kcal/kg) = EB x CDE/100
#EM(kcal/kg) =  ED - (1,04 x PB)
umidade=float (input("Digite umidade, em % :"))
umidadeg=float(input("Digite valor, de  UMIDADE em gramas por kg :"))
pb= float(input("Digite valor, em % de  PB :"))
pbg=float(input("Digite valor, de  Proteína Bruta em gramas por kg :"))
eea= float(input("Digite valor Extrato Etéreo em % :"))
eeag=float(input("Digite valor, de  Extrato Etéreo em gramas por kg :"))
fb= float(input("Digite valor Fibra Bruta em %:"))
fbg=float(input("Digite valor, de  Fibra Bruta em gramas por kg :"))
mm=float(input("Digite valor Matéria Mineral em % :"))
mmg=float(input("Digite valor, de  Matéria Mineral em gramas por kg :"))
peso= float(input("Digite o peso do animal :"))
nem= (peso**0.67)
valor_final= (75*nem)
enn= 100 -( umidade + pb + eea + fb + mm)
novo_enn= enn*10
eb= (5.7*pbg) + (9.4*eeag) + (4.1 * (novo_enn+fbg))
cde= (91.2) - (1.43*(fb/(100- umidade) *100))
ed= (eb) * (cde/100)
em= (ed) - (1.04*pbg)
novo_em=em/1000
valor_final2=nem/novo_em
print(" O valor NEM DIÁRIA é :", valor_final)