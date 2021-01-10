//
//  DemoPluginPriv.hpp
//  DemoPlugin
//
//  Created by Baijiang Liu on 2021/1/6.
//

#include <DemoPluginUI.hpp>

class DemoDialog : public QDialog {
  Q_OBJECT
  
public:
  DemoDialog();
  ~DemoDialog();
  
private slots:
  void lineEditReturnPressed();
  
protected:
  Ui::Dialog m_ui;
};
