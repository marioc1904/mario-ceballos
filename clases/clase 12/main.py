import persona as p 
import estudiante as es
import egresado as eg 
Laura = p.Persona('Laura', 18, 2834673)
Mario = p.Persona('Mario', 20, 3029394)
valeria = es.Estudiante('Valeria', 18, 2938272, 'Biomedica', 3)
Laura.hablar ('Todo anda muy bien, me gusta aprender')
Mario.comer ('Taco')
valeria.estudiar('Calculo') 
mario = eg.Egresado ('Mario', 20, 38920201, 'Biomedica', '2023/12/12')
print (mario.semestre)
mario.emprender ('empresa de productos biomedicos')