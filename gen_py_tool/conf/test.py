#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import yaml

with open("project.yaml") as project_templates:
    templates = yaml.load(project_templates, Loader=yaml.FullLoader)
    print(templates)
    print(templates['templates'][0].keys())

with open("schema_tool.yaml") as tool_project_file:
    tool_project = yaml.load(tool_project_file, Loader=yaml.FullLoader)
    print(tool_project)

with open("schema_generator.yaml") as generator_project_file:
    generator_project = yaml.load(generator_project_file, Loader=yaml.FullLoader)
    print(generator_project)

"""
##############################################################################
############### Templates ####################################################
##############################################################################
{
    'templates': [
        {
            'tool': [
                'run_module.template',
                'tool_process_class.template',
                'tool_configuration.template',
                'tool_configuration_util.template',
                'editorconfig.template'
            ]
        },
        {
            'generator': [
                'run_module.template',
                'tool_process_class.template',
                'tool_configuration.template',
                'tool_configuration_util.template',
                'generator_read_template.template',
                'generator_write_template.template',
                'generator_test.template',
                'editorconfig.template'
            ]
        }
    ],
    'schema': [
        'schema_tool.yaml',
        'schema_generator.yaml'
    ]
}

##############################################################################
############### Tool #########################################################
##############################################################################
{
    'schema_tool': {
        'tool_name': {
            'type': 'package',
            'modules': [
                '__init__.py',
                '.editorconfig',
                {
                    'run': {
                        'type': 'dir',
                        'modules': [
                            'tool_name_run.py',
                            '.editorconfig'
                        ]
                    }
                },
                {
                    'pro': {
                        'type': 'package',
                        'modules': [
                            '__init__.py',
                            '.editorconfig'
                        ]
                    }
                },
                {
                    'conf': {
                        'type': 'dir',
                        'modules': [
                            'tool_name.cfg',
                            'tool_name_util.cfg',
                            '.editorconfig'
                        ]
                    }
                },
                {
                    'log': {
                        'type': 'dir',
                        'modules': [
                            'tool_name.log',
                            '.editorconfig'
                        ]
                    }
                }
            ]
        }
    }
}

##############################################################################
############### Generator ####################################################
##############################################################################
{
    'schema_generator': {
        'generator_name': {
            'type': 'package',
            'modules': [
                '__init__.py',
                '.editorconfig',
                {
                    'run': {
                        'type': 'dir',
                        'modules': [
                            'generator_name_run.py',
                            '.editorconfig'
                        ]
                    }
                },
                {
                    'pro': {
                        'type': 'package',
                        'modules': [
                            '__init__.py',
                            '.editorconfig'
                        ]
                    }
                },
                {
                    'conf': {
                        'type': 'dir',
                        'modules': [
                            'generator_name.cfg',
                            'generator_name_util.cfg',
                            '.editorconfig',
                            {
                                'template': {
                                    'type': 'dir',
                                    'modules': [
                                        'test.template',
                                        '.editorconfig'
                                    ]
                                }
                            }
                        ]
                    }
                },
                {
                    'log': {
                        'type': 'dir',
                        'modules': [
                            'generator_name.log', '.editorconfig'
                        ]
                    }
                }
            ]
        }
    }
}
"""
