from setuptools import setup

package_name = 'robot_one'

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
    maintainer='rohit',
    maintainer_email='rohit@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_one = robot_one.robot_1_sub:main',
            'ball_move = robot_one.ball_mover:main',
			'robot_one_twisto = robot_one.robot_1_sub_twisto:main' 
        ],
    },
)
