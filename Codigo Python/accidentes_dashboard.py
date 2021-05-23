import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from connection import Connection
import bucaramangaSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

con = Connection()

# Costos totales
con.openConnection()
query_c = pd.read_sql_query(sql.CostosTotales(), con.connection)
con.closeConnection()

# Numero de accidentes
con.openConnection()
query_n = pd.read_sql_query(sql.NumeroAccidentes(), con.connection)
con.closeConnection()


# Accidentes por genero
con.openConnection()
query = pd.read_sql_query(sql.VictimasPorGenero(), con.connection)
con.closeConnection()
dfGenero = pd.DataFrame(query, columns=["sexo", "accidentes"])
figPieGenero = px.pie(dfGenero, values="accidentes", names="sexo")

# Accidentes por grupo etario
con.openConnection()
query = pd.read_sql_query(sql.AccidentesPorGrupo(), con.connection)
con.closeConnection()
dfGrupo = pd.DataFrame(query, columns=["grupo_etario", "accidentes"])
figPieGrupo = px.pie(dfGrupo, values="accidentes", names="grupo_etario")


# Costos por EPS
con.openConnection()
query = pd.read_sql_query(sql.CostosPorEPS(), con.connection)
con.closeConnection()
dfEPS = pd.DataFrame(query, columns=["nombre_eps", "costo_total"])
figBarEps = px.bar(dfEPS.tail(20), y="nombre_eps", x="costo_total", orientation='h')


# Costos por EPS por año
con.openConnection()
query = pd.read_sql_query(sql.CostosAnualesPorEPS(), con.connection)
con.closeConnection()
dfEPS_anio = pd.DataFrame(query, columns=["nombre_eps","costo_total", "2018", "2019", "2020", "2021"])
figBarEpsAnios = px.bar(dfEPS_anio.tail(20),  y="nombre_eps", x=["2018", "2019", "2020", "2021"], orientation='h') 


# Accidentes por vehiculo
con.openConnection()
query = pd.read_sql_query(sql.AccidentesPorVehiculo(), con.connection)
con.closeConnection()
dfVeh = pd.DataFrame(query, columns=["nombre", "accidentes"])
figBarVeh = px.bar(dfVeh.head(11), x ="nombre", y="accidentes")


#Accidentes por vehiculo y genero
con.openConnection()
query = pd.read_sql_query(sql.AccidentesVehiculoGenero(), con.connection)
con.closeConnection()
dfVehGen = pd.DataFrame(query, columns=["nombre", "accidentes", "hombres", "mujeres"])
figBarVehGen = px.bar(dfVehGen.head(11), x ="nombre", y=["hombres", "mujeres"], barmode="group")


# Total de accidentes por dia
con.openConnection()
query = pd.read_sql_query(sql.AccidentesPorDia(), con.connection)
con.closeConnection()
dfDia = pd.DataFrame(query, columns=["dia","total_acc", "2018", "2019", "2020", "2021"])
figBarDia = px.bar(dfDia.head(7), x="dia", y="total_acc")


# Numero accidentes por dia en los 4 años
con.openConnection()
query = pd.read_sql_query(sql.AccidentesPorDia(), con.connection)
con.closeConnection()
dfDia_anio = pd.DataFrame(query, columns=["dia","total_acc", "2018", "2019", "2020", "2021"])
figBarDiaAnios = px.bar(dfDia_anio,  x="dia", y=["2018", "2019", "2020", "2021"])


#Layout
app.layout = html.Div(children=[
    html.H1(children="Accidentalidad Bucaramanga Dashboard", className="text-center"),
    
    html.Div(className="container-fluid", children=[
        html.Div(className="row mt-4", children=[
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="alert alert-dark", children=[
                    html.H3(children=["Costos totales: " + str(query_c["sum"].values[0])]),
                    ]),
                ]),
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="alert alert-dark", children=[
                    html.H3(children=["Numero de accidentes: " + str(query_n["count"].values[0])]),
                    ]),
                ]),
            ]),
        html.Div(className="row mt-4", children=[
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Accidentes por género"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="pieAccidentesPorGenero",
                            figure=figPieGenero
                            ),
                        ]),
                    ]),
                ]),
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Accidentes por grupo etario"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="pieAccidentesPorGrupo",
                            figure = figPieGrupo
                            ),
                        ]),
                    ]),
                ]),
            ]),
        html.Div(className="row mt-4", children=[
            html.Div(className="col-12 col-xl-12", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Costos por año"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="BarCostosEps",
                            figure = figBarEps
                            ),
                        ]),
                    ]),
                ]),
            ]),
        html.Div(className="row mt-4", children=[
            html.Div(className="col-12 col-xl-12", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Costos de EPS por año"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="BarCostosEpsPorAño",
                            figure = figBarEpsAnios
                            ),
                        ]),
                    ]),
                ]),
            ]),
        html.Div(className="row mt-4", children=[
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Accidentes por vehiculo"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Vehiculos",
                            figure = figBarVeh
                            ),
                        ]),
                    ]),
                ]),
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Accidentes por vehiculo y género"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Vehiculos y genero",
                            figure = figBarVehGen
                            ),
                        ]),
                    ]),
                ]),
            ]),
        html.Div(className="row mt-4", children=[
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Accidentes por dia"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="BarAccidentesDia",
                            figure = figBarDia
                            ),
                        ]),
                    ]),
                ]),
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-primary", children=[
                    html.Div(className="card-header bg-primary text-light", children=[
                        html.H3(children="Accidentes por dia  por año"),
                        ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="BarAccidentesDiaPorAño",
                            figure = figBarDiaAnios
                            ),
                        ]),
                    ]),
                ]),
            ]),
        ]),         
    ])


if __name__ == "__main__":
    app.run_server(debug=True)
