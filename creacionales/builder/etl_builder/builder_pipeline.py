from pipeline import PipelineETL
import pandas as pd
class BuilderPipeline:

    def __init__(self):

        self.pipeline = PipelineETL()

    def build_read(self):
        raise NotImplementedError

    def build_transform(self):
        raise NotImplementedError

    def build_validate(self):
        raise NotImplementedError

    def get_result(self):
        return self.pipeline.df
    


class BuilderColombia(BuilderPipeline):

    def build_read(self):

        data = {

            "NOMBRE": ["Bryan", "Ana"],
            "TELEFONO": ["300-1234567", "301-9998888"],
            "FECHA_NACIMIENTO": ["1998/01/10", "2000/05/20"]
        }

        self.pipeline.df = pd.DataFrame(data)

    def build_transform(self):

        df = self.pipeline.df

        # columnas minúsculas
        df.columns = df.columns.str.lower()

        # limpiar teléfonos
        df["telefono"] = df["telefono"].str.replace("-", "")

        # convertir fechas
        df["fecha_nacimiento"] = pd.to_datetime(
            df["fecha_nacimiento"]
        )

        self.pipeline.df = df

    def build_validate(self):

        df = self.pipeline.df

        # validar teléfonos 10 dígitos
        df = df[
            df["telefono"].str.len() == 10
        ]

        self.pipeline.df = df
class BuilderPeru(BuilderPipeline):

    def build_read(self):

        data = {

            "nombre_completo": ["Carlos", "Lucía"],
            "celular": ["987654321", "999111222"],
            "fecha_registro": ["2024-01-10", "2024-02-15"],
            "ubigeo": ["150101", "150102"]
        }

        self.pipeline.df = pd.DataFrame(data)

    def build_transform(self):

        df = self.pipeline.df

        # renombrar columnas
        df = df.rename(columns={

            "nombre_completo": "nombre",
            "celular": "telefono"
        })

        # eliminar ubigeo
        df = df.drop(columns=["ubigeo"])

        # convertir fecha
        df["fecha_registro"] = pd.to_datetime(
            df["fecha_registro"]
        )

        self.pipeline.df = df

    def build_validate(self):

        df = self.pipeline.df

        # validar celulares 9 dígitos
        df = df[
            df["telefono"].str.len() == 9
        ]

        self.pipeline.df = df

class BuilderMexico(BuilderPipeline):

    def build_read(self):

        data = {

            "nombre": ["Luis", "Sofía"],
            "telefono": ["55-1234-5678", "55-9876-5432"],
            "fecha_nacimiento": ["1995/03/15", "1997/07/25"]
        }

        self.pipeline.df = pd.DataFrame(data)

    def build_transform(self):

        df = self.pipeline.df

        # limpiar teléfonos
        df["telefono"] = df["telefono"].str.replace("-", "")

        # convertir fechas
        df["fecha_nacimiento"] = pd.to_datetime(
            df["fecha_nacimiento"]
        )

        self.pipeline.df = df

    def build_validate(self):

        df = self.pipeline.df

        # validar teléfonos 10 dígitos
        df = df[
            df["telefono"].str.len() == 10
        ]

        self.pipeline.df = df