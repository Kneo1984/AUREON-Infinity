�
    K�hR  �                   �  � d dl Z d dlZd dlZd dlmZ  e j
                  �       Z ej                  �       Z ej                   ej                  �       �      Zdev r
dev rdZndZn	dev rdZnd	Z ed
e� ��        ede� ��       y)�    N)�	plattform�Linuxz
com.termuxzANDROID (Termux)zLINUX-PC�Windowsz
WINDOWS-PCzUNBEKANNTES SYSTEMu   
🧭 Plattform erkannt: u   🌐 Lokale IP-Adresse: )�platform�socket�os�system_checkr   �system�system_type�getcwd�current_path�gethostbyname�gethostname�	device_ip�print� �    �Hc:\Users\denni\OneDrive\Dokumente\Venv\QuantumShield 3.0\system_check.py�<module>r      s�   �� � � 	� "� �h�o�o����r�y�y�{�� �F� � �!3��!3�!3�!5�6�	�
�k���|�#�&�	��	��+���I�$�I� �"�9�+�.� /� � ���,� -r   