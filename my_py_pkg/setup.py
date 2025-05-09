from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kali',
    maintainer_email='kali@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_py_pkg.1_my_first_node:main",
            "py_oop_node = my_py_pkg.2_my_node_oop:main",
            "robot_news_station = my_py_pkg.3_publisher:main",
            "smartphone = my_py_pkg.4_subscriber:main",
            "add_int_service = my_py_pkg.5_service:main",
            "add_int_clint = my_py_pkg.6_service_clint:main",
            "add_int_clint_oop = my_py_pkg.7_clint_oop:main",
        ],
    },
)
