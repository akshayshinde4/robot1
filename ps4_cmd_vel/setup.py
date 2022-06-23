from setuptools import setup

package_name = 'ps4_cmd_vel'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aaryan',
    maintainer_email='aaryan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
		'console_scripts': [
			'robot_1_cmd_vel=ps4_cmd_vel.cmd_R1_vel:main',
        ],
    },
)
