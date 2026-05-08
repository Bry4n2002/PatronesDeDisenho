from director import ETLDirector
from builder_pipeline import *

if __name__ == "__main__":

    director = ETLDirector()


    print("\nCOLOMBIA")

    builder_co = BuilderColombia()

    df_co = director.construct_pipeline(builder_co)

    print(df_co)



    print("\nPERÚ")

    builder_pe = BuilderPeru()

    df_pe = director.construct_pipeline(builder_pe)

    print(df_pe)

    print("\nMÉXICO")
    builder_mx = BuilderMexico()
    df_mx = director.construct_pipeline(builder_mx)
    print(df_mx)