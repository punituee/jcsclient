# Copyright (c) 2016 Jiocloud.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

import argparse
from jcsclient import utils
from jcsclient import mon_utils
from jcsclient import requestify


###
#   list-metrics
# [--namespace <value>]
# [--metric-name <value>]
# [--dimensions <value>]
# [--cli-input-json <value>]
# [--starting-token <value>]
# [--max-items <value>]
# [--generate-cli-skeleton]
###
def list_metrics(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--metric-name', nargs='?', required=False)
    parser.add_argument('--starting-token', nargs='?', required=False,
                        dest='next_token')
    parser.add_argument('--max-items', nargs='?', type=int, required=False)
    parser.add_argument('--namespace', nargs='?', required=False)
    parser.add_argument('--dimensions', nargs='+', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)


###
#   get-metric-statistics
# --namespace <value>
# --metric-name <value>
# [--dimensions <value>]
# --start-time <value>
# --end-time <value>
# --period <value>
# --statistics <value>
# [--unit <value>]
# [--cli-input-json <value>]
# [--generate-cli-skeleton]
###
def get_metric_statistics(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--metric-name', nargs='?', required=True)
    parser.add_argument('--namespace', nargs='?', required=True)
    parser.add_argument('--start-time', nargs='?', required=True)
    parser.add_argument('--end-time', nargs='?', required=True)
    parser.add_argument('--period', nargs='?', type=int, required=True)
    parser.add_argument('--unit', nargs='?',
                        choices=['Seconds', 'Microseconds', 'Milliseconds',
                                 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes',
                                 'Terabytes', 'Bits', 'Kilobits', 'Megabits',
                                 'Gigabits', 'Terabits', 'Percent', 'Count',
                                 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second',
                                 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second',
                                 'Kilobits/Second', 'Megabits/Second',
                                 'Gigabits/Second', 'Terabits/Second', 'Count/Second',
                                 'None'], required=False)
    parser.add_argument('--statistics', nargs='+',
                        choices=['SampleCount', 'Average', 'Sum',
                                 'Minimum', 'Maximum'], required=True)
    parser.add_argument('--dimensions', nargs='+', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)


###
#   put-metric-alarm
# --alarm-name <value>
# [--alarm-description <value>]
# [--actions-enabled | --no-actions-enabled]
# [--ok-actions <value>]
# [--alarm-actions <value>]
# [--insufficient-data-actions <value>]
# --metric-name <value>
# --namespace <value>
# --statistic <value>
# [--dimensions <value>]
# --period <value>
# [--unit <value>]
# --evaluation-periods <value>
# --threshold <value>
# --comparison-operator <value>
# [--cli-input-json <value>]
# [--generate-cli-skeleton]
###
def put_metric_alarm(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--actions-enabled', nargs='?', type=bool, required=False)
    parser.add_argument('--alarm-actions', nargs='+', required=False)
    parser.add_argument('--alarm-description', nargs='?', required=False)
    parser.add_argument('--alarm-name', nargs='?', required=True)
    parser.add_argument('--comparison-operator', nargs='?',
                        choices=['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold',
                                 'LessThanThreshold', 'LessThanOrEqualToThreshold'],
                        required=True)
    parser.add_argument('--dimensions', nargs='+', required=False)
    parser.add_argument('--evaluation-periods', nargs='?', type=int, required=True)
    parser.add_argument('--insufficient-data-actions', nargs='+', required=False)
    parser.add_argument('--metric-name', nargs='?', required=True)
    parser.add_argument('--namespace', nargs='?', required=True)
    parser.add_argument('--ok-actions', nargs='?', required=False, dest='OK_actions')
    parser.add_argument('--period', nargs='?', required=True)
    parser.add_argument('--statistic', nargs='?',
                        choices=['SampleCount', 'Average', 'Sum',
                                 'Minimum', 'Maximum'], required=True)
    parser.add_argument('--threshold', nargs='?', type=float, required=True)
    parser.add_argument('--unit', nargs='?', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)


###
#   disable-alarm-actions
# --alarm-names <value>
# [--cli-input-json <value>]
# [--generate-cli-skeleton]
###
def disable_alarm_actions(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--alarm-names', nargs='+', required=True)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)


###
#   enable-alarm-actions
# --alarm-names <value>
# [--cli-input-json <value>]
# [--generate-cli-skeleton]
###
def enable_alarm_actions(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--alarm-names', nargs='+', required=True)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)


###
#  describe-alarms
# [--alarm-names <value>]
# [--alarm-name-prefix <value>]
# [--state-value <value>]
# [--action-prefix <value>]
# [--cli-input-json <value>]
# [--starting-token <value>]
# [--page-size <value>]
# [--max-items <value>]
# [--generate-cli-skeleton]
###
def describe_alarms(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--alarm-names', nargs='+')
    group.add_argument('--alarm-name-prefix', nargs='?')
    parser.add_argument('--state-value', nargs='?', required=False)
    parser.add_argument('--action-prefix', nargs='?', required=False)
    parser.add_argument('--starting-token', nargs='?', required=False,
                        dest='next_token')
    parser.add_argument('--max-items', nargs='?', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)

###
# describe-alarms-for-metric
# --metric-name <value>
# --namespace <value>
# [--statistic <value>]
# [--dimensions <value>]
# [--period <value>]
# [--unit <value>]
# [--cli-input-json <value>]
# [--generate-cli-skeleton]
###
def describe_alarms_for_metric(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--metric-name', nargs='?', required=True)
    parser.add_argument('--namespace', nargs='?', required=True)
    parser.add_argument('--statistic', nargs='?',
                        choices=['SampleCount', 'Average', 'Sum',
                                 'Minimum', 'Maximum'], required=False)
    parser.add_argument('--period', nargs='?', type=int, required=False)
    parser.add_argument('--unit', nargs='?',
                        choices=['Seconds', 'Microseconds', 'Milliseconds',
                                 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes',
                                 'Terabytes', 'Bits', 'Kilobits', 'Megabits',
                                 'Gigabits', 'Terabits', 'Percent', 'Count',
                                 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second',
                                 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second',
                                 'Kilobits/Second', 'Megabits/Second',
                                 'Gigabits/Second', 'Terabits/Second', 'Count/Second',
                                 'None'], required=False)
    parser.add_argument('--dimensions', nargs='+', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)

###
#   delete-alarms
# --alarm-names <value>
# [--cli-input-json <value>]
# [--generate-cli-skeleton]
###
def delete_alarms(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--alarm-names', nargs='+', required=True)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)


###
#  set-alarm-state
#--alarm-name <value>
#--state-value <value>
#--state-reason <value>
#[--state-reason-data <value>]
#[--cli-input-json <value>]
#[--generate-cli-skeleton]
###
def set_alarm_state(url, verb, headers, version, args):
    params = dict()
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--alarm-name', nargs='?', required=True)
    parser.add_argument('--state-value', nargs='?', required=True)
    parser.add_argument('--state-reason', nargs='?', required=True)
    parser.add_argument('--state-reason-data', nargs='?', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)
