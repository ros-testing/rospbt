# -*- coding: utf-8 -*-

import pytest

from rostestplus.ros_comm.asserts import (
    AssertException,
    assert_node_pingable,
    assert_node_listed,
    assert_node_listed_on_machine,
    assert_service_response_success_true,
)


def test_assert_node_pingable_doesnt_raise_exception_for_existing_node():
    fake_stdout = """
rosnode: node is [/rosout]
pinging /rosout with a timeout of 3.0s
xmlrpc reply from http://ann:46635/     time=1.195908ms
ping average: 1.150429ms    
"""
    assert_node_pingable(fake_stdout, 'rosout')
        

def test_assert_node_listed_raises_no_exception_for_existing_node():
    fake_stdout = """
/rosout
/talker
/listener
"""
    assert_node_listed(fake_stdout, 'talker')


def test_assert_node_on_machine_listed_raises_exception_for_non_existing_node():
    fake_stdout = """
/talker-ninja.local-72266-125792
/rosout
/listener-ninja.local-72615-125792
"""
    with pytest.raises(AssertException):
        assert_node_listed_on_machine(fake_stdout, 'non_existing_node', 'ninja.local')


def test_assert_node_on_machine_listed_raises_no_exception_for_existing_node():
    fake_stdout = """
/talker-ninja.local-72266-125792
/rosout
/listener-ninja.local-72615-125792
"""
    assert_node_listed_on_machine(fake_stdout, 'ninja.local', 'talker')


def test_assert_service_response_success_true_raises_no_exception_if_true():
    fake_stdout = """
success: True
"""
    assert_service_response_success_true(fake_stdout)


def test_assert_service_response_success_true_raises_exception_if_falsse():
    fake_stdout = """
success: False
"""
    with pytest.raises(AssertException):
        assert_service_response_success_true(fake_stdout)
