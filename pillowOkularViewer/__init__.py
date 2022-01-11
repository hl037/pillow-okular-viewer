from PIL.ImageShow import Viewer, register

class OkularViewer(Viewer):
  """
  Okular image viewer for PIL
  """
  format = 'PNG'

  def get_command(self, file, title=None, **options):
    if title :
      return f'okular --title "{title}" "{file}"'
    return f'okular {file}'

register(OkularViewer(), order=0)
    




