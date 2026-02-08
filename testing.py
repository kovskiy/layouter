import toml

config = toml.load('config.toml')

#sigma = config['layouts']['2'][1]
#print(sigma)

for k, v in config['layouts'].items():
    print(k, v)

test_trigger = "vesktop"

#user_keyboard = str(input("Enter your device name (you can get it using 'hyprctl devices' command!): "))
user_keyboard = config['keyboards'][0]

layout = None

for index, windows in config['layouts'].items():
    if test_trigger in windows:
        layout = index

print(f"class {test_trigger} likes {layout}")