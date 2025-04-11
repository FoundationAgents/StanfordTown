#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : MG StanfordTown Env

from metagpt.environment.base_env import Environment
from stanford_town.environment.stanford_town_ext_env import StanfordTownExtEnv


class StanfordTownEnv(StanfordTownExtEnv, Environment):
    pass
