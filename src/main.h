//---------------------------------------------------------------------------

#ifndef mainH
#define mainH
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include "SHDocVw_OCX.h"
#include <OleCtrls.hpp>
#include <ExtCtrls.hpp>
//---------------------------------------------------------------------------
class TMainForm : public TForm
{
__published:	// IDE-managed Components
        TCppWebBrowser *Browser;
        TTimer *Startup;
        TMemo *config;
        TTimer *load_config;
        TTimer *check_reload;
        TMemo *url_saver;
        void __fastcall StartupTimer(TObject *Sender);
        void __fastcall load_configTimer(TObject *Sender);
        void __fastcall check_reloadTimer(TObject *Sender);
        void __fastcall BrowserBeforeNavigate2(TObject *Sender,
          LPDISPATCH pDisp, Variant *URL, Variant *Flags,
          Variant *TargetFrameName, Variant *PostData, Variant *Headers,
          VARIANT_BOOL *Cancel);
        void __fastcall FormCloseQuery(TObject *Sender, bool &CanClose);
private:	// User declarations
public:		// User declarations
        __fastcall TMainForm(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TMainForm *MainForm;
//---------------------------------------------------------------------------
#endif
