from setuptools import setup
from glob import glob
import os
package_name = 'top_camera'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jakub',
    maintainer_email='jakub.hodek@fs.cvut.cz',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zenith_camera_subscriber = top_camera.zenith_camera_subscriber:main',
            'robot_detector_publisher = top_camera.robot_detector_publisher:main',
            'path_point_publisher = top_camera.path_point_publisher:main',
        ],
    },
)
