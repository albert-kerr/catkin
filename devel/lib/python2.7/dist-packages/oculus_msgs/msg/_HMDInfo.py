# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from oculus_msgs/HMDInfo.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class HMDInfo(genpy.Message):
  _md5sum = "9fd415a6483b21473bf35e7a4b8c2302"
  _type = "oculus_msgs/HMDInfo"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
string display_device_name
string product_name
string manufacturer
uint32 version
uint32 horizontal_resolution
uint32 vertical_resolution
float32 horizontal_screen_size
float32 vertical_screen_size
float32 vertical_screen_center
float32 eye_to_screen_distance
float32 lens_separation_distance
float32 interpupillary_distance
int32 desktop_x
int32 desktop_y
int32 display_id
float32[] distortion_K
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','display_device_name','product_name','manufacturer','version','horizontal_resolution','vertical_resolution','horizontal_screen_size','vertical_screen_size','vertical_screen_center','eye_to_screen_distance','lens_separation_distance','interpupillary_distance','desktop_x','desktop_y','display_id','distortion_K']
  _slot_types = ['std_msgs/Header','string','string','string','uint32','uint32','uint32','float32','float32','float32','float32','float32','float32','int32','int32','int32','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,display_device_name,product_name,manufacturer,version,horizontal_resolution,vertical_resolution,horizontal_screen_size,vertical_screen_size,vertical_screen_center,eye_to_screen_distance,lens_separation_distance,interpupillary_distance,desktop_x,desktop_y,display_id,distortion_K

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HMDInfo, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.display_device_name is None:
        self.display_device_name = ''
      if self.product_name is None:
        self.product_name = ''
      if self.manufacturer is None:
        self.manufacturer = ''
      if self.version is None:
        self.version = 0
      if self.horizontal_resolution is None:
        self.horizontal_resolution = 0
      if self.vertical_resolution is None:
        self.vertical_resolution = 0
      if self.horizontal_screen_size is None:
        self.horizontal_screen_size = 0.
      if self.vertical_screen_size is None:
        self.vertical_screen_size = 0.
      if self.vertical_screen_center is None:
        self.vertical_screen_center = 0.
      if self.eye_to_screen_distance is None:
        self.eye_to_screen_distance = 0.
      if self.lens_separation_distance is None:
        self.lens_separation_distance = 0.
      if self.interpupillary_distance is None:
        self.interpupillary_distance = 0.
      if self.desktop_x is None:
        self.desktop_x = 0
      if self.desktop_y is None:
        self.desktop_y = 0
      if self.display_id is None:
        self.display_id = 0
      if self.distortion_K is None:
        self.distortion_K = []
    else:
      self.header = std_msgs.msg.Header()
      self.display_device_name = ''
      self.product_name = ''
      self.manufacturer = ''
      self.version = 0
      self.horizontal_resolution = 0
      self.vertical_resolution = 0
      self.horizontal_screen_size = 0.
      self.vertical_screen_size = 0.
      self.vertical_screen_center = 0.
      self.eye_to_screen_distance = 0.
      self.lens_separation_distance = 0.
      self.interpupillary_distance = 0.
      self.desktop_x = 0
      self.desktop_y = 0
      self.display_id = 0
      self.distortion_K = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.display_device_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.product_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.manufacturer
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I6f3i.pack(_x.version, _x.horizontal_resolution, _x.vertical_resolution, _x.horizontal_screen_size, _x.vertical_screen_size, _x.vertical_screen_center, _x.eye_to_screen_distance, _x.lens_separation_distance, _x.interpupillary_distance, _x.desktop_x, _x.desktop_y, _x.display_id))
      length = len(self.distortion_K)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.distortion_K))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.display_device_name = str[start:end].decode('utf-8')
      else:
        self.display_device_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.product_name = str[start:end].decode('utf-8')
      else:
        self.product_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.manufacturer = str[start:end].decode('utf-8')
      else:
        self.manufacturer = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.version, _x.horizontal_resolution, _x.vertical_resolution, _x.horizontal_screen_size, _x.vertical_screen_size, _x.vertical_screen_center, _x.eye_to_screen_distance, _x.lens_separation_distance, _x.interpupillary_distance, _x.desktop_x, _x.desktop_y, _x.display_id,) = _struct_3I6f3i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.distortion_K = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.display_device_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.product_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.manufacturer
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I6f3i.pack(_x.version, _x.horizontal_resolution, _x.vertical_resolution, _x.horizontal_screen_size, _x.vertical_screen_size, _x.vertical_screen_center, _x.eye_to_screen_distance, _x.lens_separation_distance, _x.interpupillary_distance, _x.desktop_x, _x.desktop_y, _x.display_id))
      length = len(self.distortion_K)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.distortion_K.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.display_device_name = str[start:end].decode('utf-8')
      else:
        self.display_device_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.product_name = str[start:end].decode('utf-8')
      else:
        self.product_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.manufacturer = str[start:end].decode('utf-8')
      else:
        self.manufacturer = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.version, _x.horizontal_resolution, _x.vertical_resolution, _x.horizontal_screen_size, _x.vertical_screen_size, _x.vertical_screen_center, _x.eye_to_screen_distance, _x.lens_separation_distance, _x.interpupillary_distance, _x.desktop_x, _x.desktop_y, _x.display_id,) = _struct_3I6f3i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.distortion_K = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_3I6f3i = struct.Struct("<3I6f3i")
