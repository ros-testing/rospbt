# -*- coding: utf-8 -*-

import re

import pytest


class AssertException(Exception):
    """
    Exception for rostestplus asserts.
    """
    pass


def assert_node_pingable(rosnode_stdout, node):
    """
    Asserts that `rosnode ping` stdout indicates pingable node.
    
    Parameters
    ----------
    rosnode_stdout : String
        Minimal value to generate.
    node : String
        Name of the ROS node (e.g. "talker").

    Raises
    -------
    AssertException
        ROS node is not indicated pingable in rosnode_stdout.
    
    """ 
    NODE_REGEX = r"ping average: (?P<ms>\d{1,6}.\d{1,6})"
    rosnode_stdout_lines = rosnode_stdout.splitlines()
    match = False
    for line in rosnode_stdout_lines:
        match = re.search(NODE_REGEX, line)
        if match:
            match = True
            break
    if not match:
        raise AssertException("should contain at least 1 /{} listing".format(node))
        

def assert_node_listed(rosnode_stdout, node):
    """
    Asserts that `rosnode list` stdout contains a node.
    
    Parameters
    ----------
    rosnode_stdout : String
        Minimal value to generate.
    node : String
        Name of the ROS node (e.g. "talker").

    Raises
    -------
    AssertException
        ROS node is not contained in rosnode_stdout.
    
    """
    NODE_REGEX = r"(?P<node>/" + node + ")"
    rosnode_stdout_lines = rosnode_stdout.splitlines()
    match = False
    for line in rosnode_stdout_lines:
        match = re.search(NODE_REGEX, line)
        if match:
            match = True
            break
    if not match:
        raise AssertException("should contain at least 1 /{} listing".format(node))


def assert_node_listed_on_machine(rosnode_stdout, machine_name, node_name):
    """
    Asserts that `rosnode machine <machine-name>` stdout contains a node.
    
    Parameters
    ----------
    rosnode_stdout : String
        Stdout output of `rosnode node` command.
    node : String
        Name of the ROS node (e.g. "talker-<machine-name>").

    Raises
    -------
    AssertException
        ROS node is not contained in rosnode_stdout.
    
    """
    NODE_REGEX = r"(?P<node>/" + node_name + "-" + machine_name + ")"
    rosnode_stdout_lines = rosnode_stdout.splitlines()
    match = False
    for line in rosnode_stdout_lines:
        match = re.search(NODE_REGEX, line)
        if match:
            match = True
            break
    if not match:
        raise AssertException("should contain at least 1 /{}-{} listing".format(node_name, machine_name))


def assert_service_response_success_true(rosservice_stdout):
    """
    Asserts that `rosservice call <service-name> [service-args]` stdout
    indicates service request was ok.

    Parameters
    ----------
    rosservice_stdout : String
        Stdout output of `rosservice call <service-name> [service-args]` command.

    Raises
    -------
    AssertException
        ROS service request was not successful.
    
    """
    SUCCESS_REGEX = r"success: (?P<success>True)"
    rosservice_stdout_lines = rosservice_stdout.splitlines()
    match = False
    for line in rosservice_stdout_lines:
        match = re.search(SUCCESS_REGEX, line)
        if match:
            match = True
            break
    if not match:
        raise AssertException("node/nodelet should respond with success:True but did not")
