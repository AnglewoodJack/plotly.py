import _plotly_utils.basevalidators


class RowValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='row', parent_name='layout.mapbox.domain', **kwargs
    ):
        super(RowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            min=0,
            role='info',
            **kwargs
        )