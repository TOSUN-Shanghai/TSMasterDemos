program TestLibTSMaster;

{.$DEFINE DETECT_MEMORY_LEAK}

uses
  {$IFDEF DETECT_MEMORY_LEAK}
  FastMM4,
  {$ENDIF}
  Vcl.Forms,
  fTestLibTSMaster in 'fTestLibTSMaster.pas' {frmTestLibTSMaster};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TfrmTestLibTSMaster, frmTestLibTSMaster);
  Application.Run;

end.
