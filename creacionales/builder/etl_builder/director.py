from builder_pipeline import BuilderPipeline
class ETLDirector:

    def construct_pipeline(self, builder):

        builder.build_read()
        builder.build_transform()
        builder.build_validate()

        return builder.get_result()
    