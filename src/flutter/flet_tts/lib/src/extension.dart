import 'package:flet/flet.dart';
import 'package:flutter/widgets.dart';

import 'flet_tts.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "FletTts":
        return FletTtsControl(control: control);
      default:
        return null;
    }
  }
}
