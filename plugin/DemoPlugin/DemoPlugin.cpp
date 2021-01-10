//
//  DemoPlugin.cpp
//  DemoPlugin
//
//  Created by Baijiang Liu on 2021/1/6.
//

#include "DemoPlugin.hpp"
#include "DemoPluginPriv.hpp"

static const adp_api_t *api = nullptr;

DemoDialog::DemoDialog() {
  m_ui.setupUi(this);
  connect(m_ui.lineEdit, SIGNAL(returnPressed()), this, SLOT(lineEditReturnPressed()));
}

DemoDialog::~DemoDialog() {}

void DemoDialog::lineEditReturnPressed() {
  QString log = m_ui.lineEdit->text() + "\n";
  m_ui.lineEdit->clear();
  api->log(log.toUtf8().data());
}

adp_error_t adp_main(adp_payload_t *adp) {
  switch (adp->event) {
    case adp_event_loaded: {
      api = adp->api; // save api to a global instance
      return adp_err_ok;
    }
    case adp_event_version: {
      adp->result.str_const = __ADP_VERSION__;
      return adp_err_ok;
    }
    case adp_event_menuname: {
      adp->result.str_const = "DemoPlugin";
      return adp_err_ok;
    }
    case adp_event_main_menu: {
      DemoDialog dlg;
      dlg.exec();
      return adp_err_ok;
    }
    case adp_event_adpinfo: {
      adp->result.ptr.p0 = (void *)"0.1.0";
      adp->result.ptr.p1 = (void *)"This is a very simple GUI based AD plugin.";
      return adp_err_ok;
    }
    default:
      break;
  }
  return adp_err_unimpl;
}
