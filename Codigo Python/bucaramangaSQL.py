# Victimas por genero
def VictimasPorGenero():
    return """select sexo, count(numero) as accidentes
              from accidente_victima
              group by sexo
              order by accidentes desc"""

# Costos anuales por Eps              
def CostosAnualesPorEPS():
    return """select e.nombre_eps, sum(acc.costos) as costo_total, costo_2018, costo_2019, costo_2020, costo_2021
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
              order by costo_total desc"""

# Numero de accidentes por cada tipo de vehiculo
def AccidentesPorVehiculo():
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


# Numero de accidentes por grupo_etario
def AccidentesPorGrupo():
    return """select tip.nombre, count(numero) as accidentes
              from accidente_victima acc join tipo_vehiculo tip on (acc.id_tipo_vehiculo = tip.id)
              group by tip.nombre
              order by accidentes desc"""













