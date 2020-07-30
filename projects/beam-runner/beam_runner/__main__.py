import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from lib_one.main import main
from logger.logger import get_logger


def run():
    pipeline_options = PipelineOptions([
        '--runner=DirectRunner'
    ])

    with beam.Pipeline(options=pipeline_options) as p:
        collection = p | beam.Create(['A', 'B', 'C'])

        (collection
         | beam.Fillter(lambda x: x == "A")
         | beam.Map(lambda x: print(x))
         )


if __name__ == '__main__':
    get_logger(__name__).info("start beam_runner!!!!")
    main()
    run()
