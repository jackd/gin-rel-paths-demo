import gin
import os


@gin.configurable
def f(x=None):
  return x


os.environ['HERE'] = os.path.realpath(os.path.dirname(__file__))
print('-------------------')
print('  enabling vars    ')
print('-------------------')

try:
  gin.config.parse_config_file('$HERE/config/a.gin')
  print("We won't see this")
except Exception:
  print('Failed to expand $HERE as expected')

gin.config.enable_vars_in_includes()
try:
  gin.config.parse_config_file('$HERE/config/a.gin')
  print("Works after enabling")
except Exception:
  print("We don't fail!")

print('-------------------')
print(' relative includes ')
print('-------------------')

gin.config.parse_config_file('config/a.gin')
print('Without enabling,                 f.x = {}'.format(
    gin.query_parameter('f.x')))

gin.config.enable_relative_includes()
gin.config.parse_config_file('config/a.gin')
print('After enabling, without priority, f.x = {}'.format(
    gin.query_parameter('f.x')))

gin.config.enable_relative_includes(highest_priority=True)
gin.config.parse_config_file('config/a.gin')
print('After enabling, with priority,    f.x = {}'.format(
    gin.query_parameter('f.x')))

gin.config.parse_config_file('$HERE/config/a.gin')

try:
  gin.config.parse_config_file('$HERE/config/a.gin')
  print('path with variables work after enabling.')
except Exception:
  print("We shouldn't see this either")
