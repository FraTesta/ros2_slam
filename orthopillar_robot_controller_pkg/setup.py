import os # Operating system library
from glob import glob # Handles file path names
from setuptools import setup # Facilitates the building of packages

package_name = 'orthopillar_robot_controller_pkg'

# Path of the current directory
cur_directory_path = os.path.abspath(os.path.dirname(__file__))


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    # Path to the launch file      
        (os.path.join('share', package_name,'launch'), glob('launch/*.launch.py')),
    ],    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andrea',
    maintainer_email='andrea.tiranti97gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'robot_estimator = orthopillar_robot_controller_pkg.robot_estimator:main',
        'robot_controller = orthopillar_robot_controller_pkg.robot_controller:main'
        ],
    },
)
