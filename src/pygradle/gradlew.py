from types import MethodType

from src.pygradle import system


_BASIC_GRADLE_TASKS = ['assemble', 'build', 'buildDependents', 'buildNeeded',
                      'classes', 'compileJava', 'processResources', 'clean',
                      'jar', 'testClasses', 'compileTestJava',
                      'processTestResources', 'init', 'javadoc', 'components',
                      'dependencies', 'dependencyInsight', 'help', 'model',
                      'projects', 'properties', 'tasks', 'check', 'test']


class GradleFactory(object):

    @staticmethod
    def create(gradle_cmd='gradle'):
        cmd = ' '.join([gradle_cmd, 'task', '--all'])
        result = system.call_system_command(cmd)
        gradle_tasks = GradleFactory.get_gradle_tasks(result.split('\n'))

        gradle = Gradle(gradle_cmd)
        for new_task in set(_BASIC_GRADLE_TASKS) - set(gradle_tasks):
            setattr(gradle, new_task,
                    MethodType(MethodType(Gradle.execute_task, gradle),
                               new_task))

        return gradle

    @staticmethod
    def get_gradle_tasks(lines):
        return list(filter(None,
                           [line.split('-')[0].strip().replace(':', '_')
                            for line in lines
                            if len(line.split('-')) > 1]))


class Gradle(object):
    def __init__(self, gradle_cmd):
        self._gradle_cmd = gradle_cmd
        self._tasks = []
        for basic_task in _BASIC_GRADLE_TASKS:
            setattr(self, basic_task,
                    MethodType(MethodType(Gradle.execute_task, self),
                               basic_task))

    def execute_task(self, name):
        return system.call_system_command(
            self._create_cmd([self._gradle_cmd, name]))

    def add_task(self, name):
        self._tasks.append(name)

    def execute(self):
        pass

    def _create_cmd(self, args):
        return ' '.join(args)
