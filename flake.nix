{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    mach-nix.url = "github:DavHau/mach-nix";
  };
  outputs = { self, nixpkgs, mach-nix, ... }@inp:
    with inp; {
      shell = mach-nix.lib.x86_64-linux.mkPythonShell {
        python = "python310";
        requirements = ''
          absl-py==1.4.0
          albumentations==1.3.0
          asgiref==3.6.0
          astunparse==1.6.3
          cachetools==5.3.0
          certifi==2022.12.7
          charset-normalizer==3.1.0
          contourpy==1.0.7
          cycler==0.11.0
          Django==4.2
          flatbuffers==23.3.3
          fonttools==4.39.2
          gast==0.4.0
          google-auth==2.16.3
          google-auth-oauthlib==0.4.6
          google-pasta==0.2.0
          grpcio==1.51.3
          h5py==3.8.0
          idna==3.4
          imageio==2.26.1
          importlib-metadata==6.1.0
          importlib-resources==5.12.0
          joblib==1.2.0
          keras==2.11.0
          kiwisolver==1.4.4
          lazy_loader==0.2
          libclang==16.0.0
          Markdown==3.4.3
          MarkupSafe==2.1.2
          matplotlib==3.7.1
          networkx==3.0
          numpy==1.24.2
          oauthlib==3.2.2
          opencv-python-headless==4.7.0.72
          opt-einsum==3.3.0
          packaging==23.0
          Pillow==9.4.0
          protobuf==3.19.6
          pyasn1==0.4.8
          pyasn1-modules==0.2.8
          pyparsing==3.0.9
          python-dateutil==2.8.2
          PyWavelets==1.4.1
          PyYAML==6.0
          qudida==0.0.4
          requests==2.28.2
          requests-oauthlib==1.3.1
          rsa==4.9
          scikit-image==0.20.0
          scikit-learn==1.2.2
          scipy==1.9.1
          six==1.16.0
          sqlparse==0.4.3
          tensorboard==2.11.2
          tensorboard-data-server==0.6.1
          tensorboard-plugin-wit==1.8.1
          tensorflow-estimator==2.11.0
          tensorflow==2.11.0
          termcolor==2.2.0
          threadpoolctl==3.1.0
          tifffile==2023.3.21
          typing_extensions==4.5.0
          urllib3==1.26.15
          Werkzeug==2.2.3
          whitenoise==6.4.0
          wrapt==1.15.0
          zipp==3.15.0
          gunicorn==20.1.0
        '';
      };
    };
}
