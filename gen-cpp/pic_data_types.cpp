/**
 * Autogenerated by Thrift Compiler (0.11.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "pic_data_types.h"

#include <algorithm>
#include <ostream>

#include <thrift/TToString.h>




Image::~Image() throw() {
}


void Image::__set_data(const std::string& val) {
  this->data = val;
}

void Image::__set_width(const int32_t val) {
  this->width = val;
}

void Image::__set_height(const int32_t val) {
  this->height = val;
}

void Image::__set_channel(const int32_t val) {
  this->channel = val;
}
std::ostream& operator<<(std::ostream& out, const Image& obj)
{
  obj.printTo(out);
  return out;
}


uint32_t Image::read(::apache::thrift::protocol::TProtocol* iprot) {

  ::apache::thrift::protocol::TInputRecursionTracker tracker(*iprot);
  uint32_t xfer = 0;
  std::string fname;
  ::apache::thrift::protocol::TType ftype;
  int16_t fid;

  xfer += iprot->readStructBegin(fname);

  using ::apache::thrift::protocol::TProtocolException;


  while (true)
  {
    xfer += iprot->readFieldBegin(fname, ftype, fid);
    if (ftype == ::apache::thrift::protocol::T_STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readBinary(this->data);
          this->__isset.data = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 2:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          xfer += iprot->readI32(this->width);
          this->__isset.width = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 3:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          xfer += iprot->readI32(this->height);
          this->__isset.height = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 4:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          xfer += iprot->readI32(this->channel);
          this->__isset.channel = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      default:
        xfer += iprot->skip(ftype);
        break;
    }
    xfer += iprot->readFieldEnd();
  }

  xfer += iprot->readStructEnd();

  return xfer;
}

uint32_t Image::write(::apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  ::apache::thrift::protocol::TOutputRecursionTracker tracker(*oprot);
  xfer += oprot->writeStructBegin("Image");

  xfer += oprot->writeFieldBegin("data", ::apache::thrift::protocol::T_STRING, 1);
  xfer += oprot->writeBinary(this->data);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("width", ::apache::thrift::protocol::T_I32, 2);
  xfer += oprot->writeI32(this->width);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("height", ::apache::thrift::protocol::T_I32, 3);
  xfer += oprot->writeI32(this->height);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("channel", ::apache::thrift::protocol::T_I32, 4);
  xfer += oprot->writeI32(this->channel);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(Image &a, Image &b) {
  using ::std::swap;
  swap(a.data, b.data);
  swap(a.width, b.width);
  swap(a.height, b.height);
  swap(a.channel, b.channel);
  swap(a.__isset, b.__isset);
}

Image::Image(const Image& other0) {
  data = other0.data;
  width = other0.width;
  height = other0.height;
  channel = other0.channel;
  __isset = other0.__isset;
}
Image& Image::operator=(const Image& other1) {
  data = other1.data;
  width = other1.width;
  height = other1.height;
  channel = other1.channel;
  __isset = other1.__isset;
  return *this;
}
void Image::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "Image(";
  out << "data=" << to_string(data);
  out << ", " << "width=" << to_string(width);
  out << ", " << "height=" << to_string(height);
  out << ", " << "channel=" << to_string(channel);
  out << ")";
}


