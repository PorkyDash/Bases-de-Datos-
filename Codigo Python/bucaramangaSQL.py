# Victimas por genero
def VictimasPorGenero():
    return """select sexo, count(numero) as accidentes
              from accidente_victima
              group by sexo
              order by accidentes desc"""


# Costos totales por Eps              
def CostosPorEPS():
    return """select e.nombre_eps, sum(acc.costos) as costo_total
              from accidente_victima acc join eps e on (acc.id_eps = e.id)
              group by e.nombre_eps
              order by costo_total asc"""


# Numero de accidentes por cada tipo de vehiculo
def AccidentesPorVehiculo():
    return """select tip.nombre, count(numero) as accidentes
              from accidente_victima acc join tipo_vehiculo tip on (acc.id_tipo_vehiculo = tip.id)
              group by tip.nombre
              order by accidentes desc"""


# Numero de accidentes por grupo_etario
def AccidentesPorGrupo():
    return """select acc.grupo_etario, count(numero) as accidentes
              from accidente_victima acc
              group by acc.grupo_etario
              order by accidentes desc"""



# Costos anuales por EPS
def CostosAnualesPorEPS():
    return """select e.nombre_eps, sum(acc.costos) as costo_total, coalesce(costo_2018,0) as "2018", 
              coalesce(costo_2019,0) as "2019", coalesce(costo_2020, 0) as "2020", coalesce(costo_2021,0) as "2021"
              from accidente_victima acc join eps e on (acc.id_eps = e.id)
              left join (select nombre_eps as eps_2018, sum(acc.costos) as costo_2018 
                         from accidente_victima acc join eps on (acc.id_eps = id)
                         where acc.anio_accidente = 2018
                         group by eps_2018) as gasto_2018 on (e.nombre_eps = eps_2018)
              left join (select nombre_eps as eps_2019, sum(acc.costos) as costo_2019 
                         from accidente_victima acc join eps on (acc.id_eps = id)
                         where acc.anio_accidente = 2019
                         group by eps_2019) as gasto_2019 on (e.nombre_eps = eps_2019)
              left join (select nombre_eps as eps_2020, sum(acc.costos) as costo_2020 
                         from accidente_victima acc join eps on (acc.id_eps = id)
                         where acc.anio_accidente = 2020
                         group by eps_2020) as gasto_2020 on (e.nombre_eps = eps_2020)
              left join (select nombre_eps as eps_2021, sum(acc.costos) as costo_2021 
                         from accidente_victima acc join eps on (acc.id_eps = id)
                         where acc.anio_accidente = 2021
                         group by eps_2021) as gasto_2021 on (e.nombre_eps = eps_2021)
              group by e.nombre_eps, costo_2018, costo_2019, costo_2020, costo_2021
			  order by costo_total asc"""


# Accidentes por vehiculo y genero
def AccidentesVehiculoGenero():
    return """select tip.nombre, count(numero) as accidentes, hombres, mujeres
              from accidente_victima acc join tipo_vehiculo tip on (acc.id_tipo_vehiculo = tip.id)
              left join (select tip.nombre as vehiculo, count(acc.numero) as hombres
		                 from accidente_victima acc join tipo_vehiculo tip on (acc.id_tipo_vehiculo = tip.id)
                         where acc.sexo = 'MASCULINO'
                         group by tip.nombre) as hombres_acc on (tip.nombre = vehiculo)
              left join (select tip.nombre as veh, count(acc.numero) as mujeres
                         from accidente_victima acc join tipo_vehiculo tip on (acc.id_tipo_vehiculo = tip.id)
                         where acc.sexo = 'FEMENINO'
                         group by tip.nombre) as femenino on (tip.nombre = veh)
              group by tip.nombre, hombres, mujeres
              order by accidentes desc"""


# Costos totales
def CostosTotales():
    return """select sum(costos)
              from accidente_victima"""


def NumeroAccidentes():
    return """select count(numero)
              from accidente_victima"""
              

# Accidentes por dia
def AccidentesPorDia():
    return """select acc.dia_semana_accidente as dia, count(acc.numero) as total_acc, num2018 as "2018", num2019 as "2019", num2020 as "2020", num2021 as "2021"
              from accidente_victima acc
              join (select acc.dia_semana_accidente as semana2018, count(acc.numero) as num2018 
                    from accidente_victima acc
                    where acc.anio_accidente = 2018
                    group by semana2018) as acc_2018 on (acc.dia_semana_accidente = semana2018)
              join (select acc.dia_semana_accidente as semana2019, count(acc.numero) as num2019 
                    from accidente_victima acc
                    where acc.anio_accidente = 2019
                    group by semana2019) as acc_2019 on (acc.dia_semana_accidente = semana2019)
              join (select acc.dia_semana_accidente as semana2020, count(acc.numero) as num2020 
                    from accidente_victima acc
                    where acc.anio_accidente = 2020
                    group by semana2020) as acc_2020 on (acc.dia_semana_accidente = semana2020)
              join (select acc.dia_semana_accidente as semana2021, count(acc.numero) as num2021 
                    from accidente_victima acc
                    where acc.anio_accidente = 2021
                    group by semana2021) as acc_2021 on (acc.dia_semana_accidente = semana2021)
              group by dia, "2018", "2019", "2020", "2021"
              order by total_acc desc""" 

