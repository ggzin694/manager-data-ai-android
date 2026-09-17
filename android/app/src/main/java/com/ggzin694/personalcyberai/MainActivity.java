package com.ggzin694.personalcyberai;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;
import org.json.JSONObject;

public class MainActivity extends Activity {
    private WebView web;
    @Override protected void onCreate(Bundle state) { super.onCreate(state); build(); handle(getIntent()); }
    private void build() {
        web = new WebView(this);
        WebSettings s=web.getSettings(); s.setJavaScriptEnabled(true); s.setDomStorageEnabled(true); s.setDatabaseEnabled(false); s.setAllowFileAccess(true); s.setAllowContentAccess(false); s.setBuiltInZoomControls(false); s.setDisplayZoomControls(false); s.setTextZoom(100); s.setSupportZoom(false);
        web.setWebViewClient(new WebViewClient(){ @Override public void onPageFinished(WebView v,String url){ handle(getIntent()); } });
        web.setWebChromeClient(new WebChromeClient()); web.setBackgroundColor(0xFF070B16); setContentView(web); web.loadUrl("file:///android_asset/index.html");
    }
    private void handle(Intent intent) { if(web==null||intent==null)return; String value=null; if(Intent.ACTION_PROCESS_TEXT.equals(intent.getAction())) value=intent.getStringExtra(Intent.EXTRA_PROCESS_TEXT); else if(Intent.ACTION_SEND.equals(intent.getAction())) value=intent.getStringExtra(Intent.EXTRA_TEXT); if(value==null){Uri u=intent.getData();if(u!=null)value=u.toString();} if(value!=null&&!value.trim().isEmpty()){try{web.evaluateJavascript("window.setIncoming("+JSONObject.quote(value.trim())+")",null);}catch(Exception ignored){}} }
    @Override protected void onNewIntent(Intent intent){super.onNewIntent(intent);setIntent(intent);handle(intent);}
    @Override public void onBackPressed(){if(web!=null&&web.canGoBack())web.goBack();else super.onBackPressed();}
    @Override protected void onDestroy(){if(web!=null)web.destroy();super.onDestroy();}
}
