# MinCrypK_VerifySignedDataKModeEx

- RVA: `0x00838568`–`0x00838A08` (길이 `1,184` bytes)
- VA: `0x0000000140838568`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DAF24`
- 디코드: `294`개 명령, `1,184/1,184` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008385F7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0083860C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0083863C` → [MinAsn1ParseSignedData](MinAsn1ParseSignedData_function_00838F24.md) (function, `0x00838F24`)
- `0x0083866A` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x008386BD` → [MinAsn1SignedDataGetContent](MinAsn1SignedDataGetContent_function_0083A3EC.md) (function, `0x0083A3EC`)
- `0x008386EB` → [MinAsn1ParseSignedDataCertificatesEx](MinAsn1ParseSignedDataCertificatesEx_function_00838F68.md) (function, `0x00838F68`)
- `0x00838712` → [I_MinCryptFindSignerCertificateByIssuerAndSerialNumber](I_MinCryptFindSignerCertificateByIssuerAndSerialNumber_function_00837DE8.md) (function, `0x00837DE8`)
- `0x0083876C` → [MinCryptVerifyCertificateWithPolicy2](MinCryptVerifyCertificateWithPolicy2_function_008368A8.md) (function, `0x008368A8`)
- `0x008387A0` → [I_MinCryptGetPlatformManifestBinaryIDAttribute](I_MinCryptGetPlatformManifestBinaryIDAttribute_function_00837E9C.md) (function, `0x00837E9C`)
- `0x008387E3` → [MinCryptDecodeHashAlgorithmIdentifier](MinCryptDecodeHashAlgorithmIdentifier_function_008361A0.md) (function, `0x008361A0`)
- `0x0083880B` → [MinAsn1ExtractContent](MinAsn1ExtractContent_function_0083A00C.md) (function, `0x0083A00C`)
- `0x00838849` → [MinCryptHashMemory](../../text/6A/MinCryptHashMemory_function_006A5F04.md) (function, `0x006A5F04`)
- `0x0083887F` → [I_MinCryptVerifySignerAuthenticatedAttributes](I_MinCryptVerifySignerAuthenticatedAttributes_function_00838430.md) (function, `0x00838430`)
- `0x008388BD` → [MinCryptVerifySignedHash2](MinCryptVerifySignedHash2_function_008362A0.md) (function, `0x008362A0`)
- `0x00838908` → [I_MinCryptGetSigningTime](I_MinCryptGetSigningTime_function_00837F2C.md) (function, `0x00837F2C`)
- `0x00838967` → [MincryptIsTimestampBeforeRevocation](MincryptIsTimestampBeforeRevocation_function_00837A68.md) (function, `0x00837A68`)
- `0x008389A7` → [I_MinCryptBuildErrorPolicy](I_MinCryptBuildErrorPolicy_function_008391DC.md) (function, `0x008391DC`)
- `0x008389C0` → [I_MincryptFreeChainInfo](I_MincryptFreeChainInfo_function_008395E8.md) (function, `0x008395E8`)
- `0x008389ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MinCrypK_VerifySignedDataKMode](MinCrypK_VerifySignedDataKMode_function_00838524.md) at `0x00838555`

### Static image references
- `0x00838663` → RVA `0x00B4B658` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x008385F7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0083860C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0083866A` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00838849` → [MinCryptHashMemory](../../text/6A/MinCryptHashMemory_function_006A5F04.md) (`PAGE` → `.text`)
  - `0x008389ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00838568  4C 8B DC                        mov r11, rsp
0083856B  53                              push rbx
0083856C  56                              push rsi
0083856D  57                              push rdi
0083856E  41 54                           push r12
00838570  41 55                           push r13
00838572  41 56                           push r14
00838574  41 57                           push r15
00838576  48 81 EC C0 00 00 00            sub rsp, 0xc0
0083857D  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
00838582  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00838587  44 8B E2                        mov r12d, edx
0083858A  4C 8B F9                        mov r15, rcx
0083858D  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00838595  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0083859A  4C 8B B4 24 28 01 00 00         mov r14, qword ptr [rsp + 0x128]
008385A2  4D 89 73 C0                     mov qword ptr [r11 - 0x40], r14
008385A6  48 8B BC 24 30 01 00 00         mov rdi, qword ptr [rsp + 0x130]
008385AE  C7 44 24 30 28 04 00 C0         mov dword ptr [rsp + 0x30], 0xc0000428
008385B6  33 F6                           xor esi, esi
008385B8  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008385BD  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
008385C1  8B DE                           mov ebx, esi
008385C3  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
008385C7  0F 57 C0                        xorps xmm0, xmm0
008385CA  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
008385CF  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
008385D3  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
008385D7  41 0F 11 43 88                  movups xmmword ptr [r11 - 0x78], xmm0
008385DC  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
008385E1  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
008385E6  C7 44 24 40 0A 00 00 00         mov dword ptr [rsp + 0x40], 0xa
008385EE  33 D2                           xor edx, edx
008385F0  44 8D 46 50                     lea r8d, [rsi + 0x50]
008385F4  48 8B CF                        mov rcx, rdi
008385F7  E8 44 E6 E8 FF                  call 0x1406c6c40
008385FC  BA D0 0A 00 00                  mov edx, 0xad0
00838601  B9 02 01 00 00                  mov ecx, 0x102
00838606  41 B8 43 49 63 72               mov r8d, 0x72634943
0083860C  E8 DF 9A 34 00                  call 0x140b820f0
00838611  4C 8B E8                        mov r13, rax
00838614  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00838619  48 85 C0                        test rax, rax
0083861C  75 0E                           jne 0x14083862c
0083861E  BF 17 00 00 C0                  mov edi, 0xc0000017
00838623  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00838627  E9 6F 03 00 00                  jmp 0x14083899b
0083862C  48 8D B0 60 09 00 00            lea rsi, [rax + 0x960]
00838633  4C 8B C6                        mov r8, rsi
00838636  41 8B D4                        mov edx, r12d
00838639  49 8B CF                        mov rcx, r15
0083863C  E8 E3 08 00 00                  call 0x140838f24
00838641  85 C0                           test eax, eax
00838643  79 0A                           jns 0x14083864f
00838645  BB 00 00 05 00                  mov ebx, 0x50000
0083864A  E9 3F 03 00 00                  jmp 0x14083898e
0083864F  83 7E 20 09                     cmp dword ptr [rsi + 0x20], 9
00838653  0F 85 30 03 00 00               jne 0x140838989
00838659  41 B8 09 00 00 00               mov r8d, 9
0083865F  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
00838663  48 8D 0D EE 2F 31 00            lea rcx, [rip + 0x312fee]
0083866A  E8 01 20 E8 FF                  call 0x1406ba670
0083866F  48 83 F8 09                     cmp rax, 9
00838673  0F 85 10 03 00 00               jne 0x140838989
00838679  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0083867D  85 C9                           test ecx, ecx
0083867F  74 21                           je 0x1408386a2
00838681  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00838686  48 85 C0                        test rax, rax
00838689  74 17                           je 0x1408386a2
0083868B  83 7E 50 00                     cmp dword ptr [rsi + 0x50], 0
0083868F  74 08                           je 0x140838699
00838691  0F 10 46 50                     movups xmm0, xmmword ptr [rsi + 0x50]
00838695  F3 0F 7F 07                     movdqu xmmword ptr [rdi], xmm0
00838699  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0083869D  89 4F 10                        mov dword ptr [rdi + 0x10], ecx
008386A0  EB 30                           jmp 0x1408386d2
008386A2  83 7E 50 00                     cmp dword ptr [rsi + 0x50], 0
008386A6  74 9D                           je 0x140838645
008386A8  83 7E 60 00                     cmp dword ptr [rsi + 0x60], 0
008386AC  74 97                           je 0x140838645
008386AE  0F 10 46 50                     movups xmm0, xmmword ptr [rsi + 0x50]
008386B2  F3 0F 7F 07                     movdqu xmmword ptr [rdi], xmm0
008386B6  48 8D 57 10                     lea rdx, [rdi + 0x10]
008386BA  48 8B CE                        mov rcx, rsi
008386BD  E8 2A 1D 00 00                  call 0x14083a3ec
008386C2  85 C0                           test eax, eax
008386C4  0F 8E BF 02 00 00               jle 0x140838989
008386CA  C7 44 24 50 01 00 00 00         mov dword ptr [rsp + 0x50], 1
008386D2  83 BE A0 00 00 00 00            cmp dword ptr [rsi + 0xa0], 0
008386D9  0F 84 66 FF FF FF               je 0x140838645
008386DF  48 8D 4E 70                     lea rcx, [rsi + 0x70]
008386E3  4D 8B C5                        mov r8, r13
008386E6  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
008386EB  E8 78 08 00 00                  call 0x140838f68
008386F0  85 C0                           test eax, eax
008386F2  78 30                           js 0x140838724
008386F4  44 8B 7C 24 40                  mov r15d, dword ptr [rsp + 0x40]
008386F9  45 85 FF                        test r15d, r15d
008386FC  74 26                           je 0x140838724
008386FE  48 8D 96 D0 00 00 00            lea rdx, [rsi + 0xd0]
00838705  48 8D 8E C0 00 00 00            lea rcx, [rsi + 0xc0]
0083870C  4D 8B CD                        mov r9, r13
0083870F  45 8B C7                        mov r8d, r15d
00838712  E8 D1 F6 FF FF                  call 0x140837de8
00838717  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0083871F  48 85 C0                        test rax, rax
00838722  75 0A                           jne 0x14083872e
00838724  BB 00 00 06 00                  mov ebx, 0x60000
00838729  E9 60 02 00 00                  jmp 0x14083898e
0083872E  0F 10 40 10                     movups xmm0, xmmword ptr [rax + 0x10]
00838732  F3 0F 7F 47 20                  movdqu xmmword ptr [rdi + 0x20], xmm0
00838737  4C 8D A6 F0 00 00 00            lea r12, [rsi + 0xf0]
0083873E  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00838743  F3 0F 7F 47 30                  movdqu xmmword ptr [rdi + 0x30], xmm0
00838748  0F 10 8E 20 01 00 00            movups xmm1, xmmword ptr [rsi + 0x120]
0083874F  F3 0F 7F 4F 40                  movdqu xmmword ptr [rdi + 0x40], xmm1
00838754  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00838759  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0083875E  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
00838763  4D 8B C5                        mov r8, r13
00838766  41 8B D7                        mov edx, r15d
00838769  48 8B C8                        mov rcx, rax
0083876C  E8 37 E1 FF FF                  call 0x1408368a8
00838771  8B F8                           mov edi, eax
00838773  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00838777  85 C0                           test eax, eax
00838779  79 18                           jns 0x140838793
0083877B  3D 03 06 00 C0                  cmp eax, 0xc0000603
00838780  0F 85 15 02 00 00               jne 0x14083899b
00838786  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
0083878B  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
00838793  41 83 3C 24 00                  cmp dword ptr [r12], 0
00838798  74 19                           je 0x1408387b3
0083879A  49 8B D6                        mov rdx, r14
0083879D  49 8B CC                        mov rcx, r12
008387A0  E8 F7 F6 FF FF                  call 0x140837e9c
008387A5  8B F8                           mov edi, eax
008387A7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008387AB  85 C0                           test eax, eax
008387AD  0F 88 E8 01 00 00               js 0x14083899b
008387B3  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008387B8  48 85 C0                        test rax, rax
008387BB  74 07                           je 0x1408387c4
008387BD  8B 40 04                        mov eax, dword ptr [rax + 4]
008387C0  A8 10                           test al, 0x10
008387C2  75 18                           jne 0x1408387dc
008387C4  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
008387C8  48 85 C9                        test rcx, rcx
008387CB  74 0F                           je 0x1408387dc
008387CD  33 C0                           xor eax, eax
008387CF  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008387D3  3B 41 30                        cmp eax, dword ptr [rcx + 0x30]
008387D6  73 04                           jae 0x1408387dc
008387D8  FF C0                           inc eax
008387DA  EB F3                           jmp 0x1408387cf
008387DC  48 8D 8E E0 00 00 00            lea rcx, [rsi + 0xe0]
008387E3  E8 B8 D9 FF FF                  call 0x1408361a0
008387E8  44 8B F8                        mov r15d, eax
008387EB  85 C0                           test eax, eax
008387ED  0F 84 96 01 00 00               je 0x140838989
008387F3  83 7C 24 50 00                  cmp dword ptr [rsp + 0x50], 0
008387F8  74 1F                           je 0x140838819
008387FA  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
008387FF  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00838804  8B 56 60                        mov edx, dword ptr [rsi + 0x60]
00838807  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
0083880B  E8 FC 17 00 00                  call 0x14083a00c
00838810  85 C0                           test eax, eax
00838812  79 17                           jns 0x14083882b
00838814  E9 70 01 00 00                  jmp 0x140838989
00838819  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0083881D  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00838821  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00838826  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0083882B  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
00838830  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00838835  4C 8D 8E 30 01 00 00            lea r9, [rsi + 0x130]
0083883C  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00838841  BA 01 00 00 00                  mov edx, 1
00838846  41 8B CF                        mov ecx, r15d
00838849  E8 B6 D6 E6 FF                  call 0x1406a5f04
0083884E  8B F8                           mov edi, eax
00838850  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00838854  85 C0                           test eax, eax
00838856  79 0A                           jns 0x140838862
00838858  BB 00 00 04 00                  mov ebx, 0x40000
0083885D  E9 35 01 00 00                  jmp 0x140838997
00838862  41 83 3C 24 00                  cmp dword ptr [r12], 0
00838867  74 25                           je 0x14083888e
00838869  4C 8D 8E F0 00 00 00            lea r9, [rsi + 0xf0]
00838870  4C 8D 44 24 3C                  lea r8, [rsp + 0x3c]
00838875  48 8D 96 30 01 00 00            lea rdx, [rsi + 0x130]
0083887C  41 8B CF                        mov ecx, r15d
0083887F  E8 AC FB FF FF                  call 0x140838430
00838884  8B F8                           mov edi, eax
00838886  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0083888A  85 C0                           test eax, eax
0083888C  78 CA                           js 0x140838858
0083888E  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00838896  48 05 B0 00 00 00               add rax, 0xb0
0083889C  4C 8D 8E 10 01 00 00            lea r9, [rsi + 0x110]
008388A3  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
008388A9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008388AE  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
008388B3  48 8D 96 30 01 00 00            lea rdx, [rsi + 0x130]
008388BA  41 8B CF                        mov ecx, r15d
008388BD  E8 DE D9 FF FF                  call 0x1408362a0
008388C2  8B F8                           mov edi, eax
008388C4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008388C8  85 C0                           test eax, eax
008388CA  78 8C                           js 0x140838858
008388CC  83 7C 24 38 00                  cmp dword ptr [rsp + 0x38], 0
008388D1  0F 84 C4 00 00 00               je 0x14083899b
008388D7  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
008388DC  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
008388E2  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008388E7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008388EC  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008388F1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008388F6  4C 8D 8C 24 80 00 00 00         lea r9, [rsp + 0x80]
008388FE  4D 8B C5                        mov r8, r13
00838901  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
00838905  48 8B CE                        mov rcx, rsi
00838908  E8 1F F6 FF FF                  call 0x140837f2c
0083890D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00838911  85 C0                           test eax, eax
00838913  78 2A                           js 0x14083893f
00838915  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0083891A  48 85 C0                        test rax, rax
0083891D  7E 2A                           jle 0x140838949
0083891F  48 3B 84 24 A0 00 00 00         cmp rax, qword ptr [rsp + 0xa0]
00838927  7C 16                           jl 0x14083893f
00838929  48 3B 84 24 A8 00 00 00         cmp rax, qword ptr [rsp + 0xa8]
00838931  7F 0C                           jg 0x14083893f
00838933  49 3B 46 20                     cmp rax, qword ptr [r14 + 0x20]
00838937  7C 06                           jl 0x14083893f
00838939  49 3B 46 28                     cmp rax, qword ptr [r14 + 0x28]
0083893D  7E 07                           jle 0x140838946
0083893F  33 C0                           xor eax, eax
00838941  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00838946  48 85 C0                        test rax, rax
00838949  75 0C                           jne 0x140838957
0083894B  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
0083894F  0F BA E8 1A                     bts eax, 0x1a
00838953  41 89 46 08                     mov dword ptr [r14 + 8], eax
00838957  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
0083895F  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00838964  49 8B CE                        mov rcx, r14
00838967  E8 FC F0 FF FF                  call 0x140837a68
0083896C  8B F8                           mov edi, eax
0083896E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00838972  85 C0                           test eax, eax
00838974  78 25                           js 0x14083899b
00838976  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
0083897A  0F BA F0 15                     btr eax, 0x15
0083897E  41 89 46 08                     mov dword ptr [r14 + 8], eax
00838982  33 FF                           xor edi, edi
00838984  E9 9A FC FF FF                  jmp 0x140838623
00838989  BB 00 00 04 00                  mov ebx, 0x40000
0083898E  BF 28 04 00 C0                  mov edi, 0xc0000428
00838993  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00838997  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
0083899B  85 FF                           test edi, edi
0083899D  79 0F                           jns 0x1408389ae
0083899F  44 8B C3                        mov r8d, ebx
008389A2  49 8B D6                        mov rdx, r14
008389A5  8B CF                           mov ecx, edi
008389A7  E8 30 08 00 00                  call 0x1408391dc
008389AC  8B F8                           mov edi, eax
008389AE  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
008389B6  74 28                           je 0x1408389e0
008389B8  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
008389C0  E8 23 0C 00 00                  call 0x1408395e8
008389C5  0F 57 C0                        xorps xmm0, xmm0
008389C8  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
008389D0  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
008389D8  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
008389E0  4D 85 ED                        test r13, r13
008389E3  74 0D                           je 0x1408389f2
008389E5  BA 43 49 63 72                  mov edx, 0x72634943
008389EA  49 8B CD                        mov rcx, r13
008389ED  E8 7E 9E 34 00                  call 0x140b82870
008389F2  8B C7                           mov eax, edi
008389F4  48 81 C4 C0 00 00 00            add rsp, 0xc0
008389FB  41 5F                           pop r15
008389FD  41 5E                           pop r14
008389FF  41 5D                           pop r13
00838A01  41 5C                           pop r12
00838A03  5F                              pop rdi
00838A04  5E                              pop rsi
00838A05  5B                              pop rbx
00838A06  C3                              ret
00838A07  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MinCrypK_VerifySignedDataKModeEx(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;

    v_rsp = (v_rsp) - (192);
    v_stack_mB0 = a4;
    v_stack_m98 = a3;
    v_stack_mA0 = a5;
    *(unsigned __int64 *)(v_rsp - 64) = a6;
    v_stack_mC8 = 0xC0000428ULL;
    v_rsi = 0;
    v_stack_m90 = 0;
    v_stack_mBC = 0;
    v_stack_mC4 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_mC0 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    v_stack_mB8 = 10;
    a2 = 0;
    result = memset(a7, a2, v_rsi + 80, a4);
    result = ExAllocatePool2(258, (unsigned int)(0xAD0ULL), (unsigned int)(0x72634943ULL), a4);
    v_stack_m90 = result;
    if (result != 0) goto loc_0083862C;
loc_00838623:
    v_stack_mC8 = (unsigned int)((unsigned int)(0xC0000017ULL));
    goto loc_0083899B;
loc_0083862C:
    result = MinAsn1ParseSignedData(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), result + 2400, a4);
    if (!sign_flag) goto loc_0083864F;
loc_00838645:
    goto loc_0083898E;
loc_0083864F:
    if ((*(unsigned int *)(result + 2400 + 32)) != 9) goto loc_00838989;
    result = RtlCompareMemory(v_rip + 3223534, *(unsigned __int64 *)(result + 2400 + 40), 9, a4);
    if (result != 9) goto loc_00838989;
    if ((unsigned int)((unsigned int)(v_stack_mB0)) == 0) goto loc_008386A2;
    if (v_stack_m98 == 0) goto loc_008386A2;
    if ((*(unsigned int *)(result + 2400 + 80)) != 0) {
        *(unsigned __int64 *)((unsigned int)(0xC0000017ULL)) = v_xmm0;
    }
    *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 24) = v_stack_m98;
    *(unsigned int *)((unsigned int)(0xC0000017ULL) + 16) = (unsigned int)((unsigned int)(v_stack_mB0));
    goto loc_008386D2;
loc_008386A2:
    if ((*(unsigned int *)(result + 2400 + 80)) == 0) goto loc_00838645;
    if ((*(unsigned int *)(result + 2400 + 96)) == 0) goto loc_00838645;
    *(unsigned __int64 *)((unsigned int)(0xC0000017ULL)) = v_xmm0;
    result = MinAsn1SignedDataGetContent(result + 2400, (unsigned int)(0xC0000017ULL) + 16, 9, a4);
    if (condition_is_less_or_equal) goto loc_00838989;
    v_stack_mA8 = 1;
loc_008386D2:
    if ((*(unsigned int *)(result + 2400 + 160)) == 0) goto loc_00838645;
    result = MinAsn1ParseSignedDataCertificatesEx(result + 2400 + 112, v_stack_mB8, result, a4);
    if (sign_flag) goto loc_00838724;
    if ((unsigned int)((unsigned int)(v_stack_mB8)) == 0) goto loc_00838724;
    result = I_MinCryptFindSignerCertificateByIssuerAndSerialNumber(result + 2400 + 192, result + 2400 + 208, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8))), result);
    v_stack_m48 = result;
    if (result != 0) goto loc_0083872E;
loc_00838724:
    goto loc_0083898E;
loc_0083872E:
    *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 32) = v_xmm0;
    *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 48) = v_xmm0;
    *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 64) = v_xmm1;
    v_stack_mD0 = result + 2400 + 240;
    v_stack_mD8 = a6;
    result = MinCryptVerifyCertificateWithPolicy2(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8))), result, v_stack_mA0);
    v_stack_mC8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00838793;
    if (((unsigned int)(result)) != 0xC0000603ULL) goto loc_0083899B;
    v_stack_mC0 = 1;
loc_00838793:
    if ((*(unsigned int *)(result + 2400 + 240)) == 0) goto loc_008387B3;
    result = I_MinCryptGetPlatformManifestBinaryIDAttribute(result + 2400 + 240, a6, result, v_stack_mA0);
    v_stack_mC8 = (unsigned int)(result);
    if (sign_flag) goto loc_0083899B;
loc_008387B3:
    if (v_stack_mA0 == 0) goto loc_008387C4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 4)))) & (16)) != 0) goto loc_008387DC;
loc_008387C4:
    if (*(unsigned __int64 *)(a6 + 16) == 0) goto loc_008387DC;
    result = 0;
loc_008387CF:
    v_stack_mA4 = 0;
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(a6 + 16) + 48))) goto loc_008387DC;
    result = (unsigned int)((result) + 1);
    goto loc_008387CF;
loc_008387DC:
    result = MinCryptDecodeHashAlgorithmIdentifier(result + 2400 + 224, a6, result, v_stack_mA0);
    if ((unsigned int)(result) == 0) goto loc_00838989;
    if (v_stack_mA8 == 0) goto loc_00838819;
    result = MinAsn1ExtractContent(*(unsigned __int64 *)(result + 2400 + 104), (unsigned int)(*(unsigned int *)(result + 2400 + 96)), v_stack_m88, v_stack_m80);
    if (!sign_flag) goto loc_0083882B;
    goto loc_00838989;
loc_00838819:
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_mB0));
    v_stack_m80 = v_stack_m98;
loc_0083882B:
    v_stack_mD8 = v_stack_mBC;
    result = MinCryptHashMemory((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 1, v_stack_m88, result + 2400 + 304);
    v_stack_mC8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00838862;
loc_00838858:
    goto loc_00838997;
loc_00838862:
    if ((*(unsigned int *)(result + 2400 + 240)) == 0) goto loc_0083888E;
    result = I_MinCryptVerifySignerAuthenticatedAttributes((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result + 2400 + 304, v_stack_mBC, result + 2400 + 240);
    v_stack_mC8 = (unsigned int)(result);
    if (sign_flag) goto loc_00838858;
loc_0083888E:
    result = (v_stack_m48) + (176);
    v_stack_mD8 = result;
    result = MinCryptVerifySignedHash2((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result + 2400 + 304, (unsigned int)(v_stack_mBC), result + 2400 + 272);
    v_stack_mC8 = (unsigned int)(result);
    if (sign_flag) goto loc_00838858;
    if (v_stack_mC0 == 0) goto loc_0083899B;
    v_stack_mD0 = v_stack_mC0;
    v_stack_mD8 = v_stack_mB0;
    result = I_MinCryptGetSigningTime(result + 2400, (unsigned int)(v_stack_mB8), result, v_stack_m78);
    v_stack_mC8 = (unsigned int)(result);
    if (sign_flag) goto loc_0083893F;
    if (condition_is_less_or_equal) goto loc_00838949;
    if (v_stack_mB0 < v_stack_m58) goto loc_0083893F;
    if (v_stack_mB0 > v_stack_m50) goto loc_0083893F;
    if (v_stack_mB0 < (*(unsigned __int64 *)(a6 + 32))) goto loc_0083893F;
    result = v_stack_mB0;
    if (v_stack_mB0 >= = (*(unsigned __int64 *)(a6 + 40))) {
        result = 0;
        v_stack_mB0 = 0;
    }
loc_00838949:
    if (0 == 0) {
        result = *(unsigned int *)(a6 + 8);
        *(unsigned int *)(a6 + 8) = (unsigned int)(result);
    }
    result = MincryptIsTimestampBeforeRevocation(a6, v_stack_mB0, v_stack_m78, v_stack_m78);
    v_stack_mC8 = (unsigned int)(result);
    if (sign_flag) goto loc_0083899B;
    *(unsigned int *)(a6 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a6 + 8)));
    v_rdi = 0;
    goto loc_00838623;
loc_00838989:
loc_0083898E:
    v_stack_mC8 = (unsigned int)((unsigned int)(0xC0000428ULL));
loc_00838997:
    v_stack_mC4 = (unsigned int)((unsigned int)(0x40000ULL));
loc_0083899B:
    result = (unsigned int)(*(unsigned int *)(a6 + 8));
    v_rdi = (unsigned int)(0xC0000428ULL);
    if (sign_flag) {
        a3 = (unsigned int)((unsigned int)(0x40000ULL));
        a2 = a6;
        a1 = (unsigned int)((unsigned int)(0xC0000428ULL));
        result = I_MinCryptBuildErrorPolicy(a1, a2, a3, v_stack_m78);
        v_rdi = (unsigned int)(result);
    }
    if (v_stack_m78 != 0) {
        a1 = v_stack_m68;
        result = I_MincryptFreeChainInfo(a1, a2, a3, v_stack_m78);
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        v_stack_m58 = v_xmm0;
    }
    if (result != 0) {
        a2 = 0x72634943ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_m78);
    }
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)(v_rdi));
}
```

## 5. (Beta) C Style

```c
int64_t MinCrypK_VerifySignedDataKModeEx(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, void *Arg6, void *Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;

    local_rsp = (local_rsp) - (192);
    v_stack_mB0 = Arg4;
    v_stack_m98 = Arg3;
    v_stack_mA0 = Arg5;
    *(void **)(local_rsp - 0x40) = Arg6;
    v_stack_mC8 = 0xC0000428ULL;
    local_rsi = 0;
    v_stack_m90 = 0;
    v_stack_mBC = 0;
    v_stack_mC4 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_mC0 = 0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    v_stack_mB8 = 10;
    Arg2 = 0;
    result = memset(Arg7, Arg2, local_rsi + 80, Arg4);
    result = ExAllocatePool2(258, (uint32_t)(0xAD0ULL), (uint32_t)(0x72634943ULL), Arg4);
    v_stack_m90 = result;
    if (result != 0) goto loc_0083862C;
loc_00838623:
    v_stack_mC8 = (uint32_t)((uint32_t)(0xC0000017ULL));
    goto loc_0083899B;
loc_0083862C:
    result = MinAsn1ParseSignedData(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), result + 2400, Arg4);
    if (!sign_flag) goto loc_0083864F;
loc_00838645:
    goto loc_0083898E;
loc_0083864F:
    if ((*(uint32_t *)(result + 0x960 + 0x20)) != 9) goto loc_00838989;
    result = RtlCompareMemory(v_rip + 3223534, *(uint64_t *)(result + 0x960 + 0x28), 9, Arg4);
    if (result != 9) goto loc_00838989;
    if ((uint32_t)((uint32_t)(v_stack_mB0)) == 0) goto loc_008386A2;
    if (v_stack_m98 == 0) goto loc_008386A2;
    if ((*(uint32_t *)(result + 0x960 + 0x50)) != 0) {
        *(uint64_t *)((uint32_t)(0xC0000017ULL)) = v_xmm0;
    }
    *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x18) = v_stack_m98;
    *(uint32_t *)((uint32_t)(0xC0000017ULL) + 0x10) = (uint32_t)((uint32_t)(v_stack_mB0));
    goto loc_008386D2;
loc_008386A2:
    if ((*(uint32_t *)(result + 0x960 + 0x50)) == 0) goto loc_00838645;
    if ((*(uint32_t *)(result + 0x960 + 0x60)) == 0) goto loc_00838645;
    *(uint64_t *)((uint32_t)(0xC0000017ULL)) = v_xmm0;
    result = MinAsn1SignedDataGetContent(result + 2400, (uint32_t)(0xC0000017ULL) + 16, 9, Arg4);
    if (condition_is_less_or_equal) goto loc_00838989;
    v_stack_mA8 = 1;
loc_008386D2:
    if ((*(uint32_t *)(result + 0x960 + 0xA0)) == 0) goto loc_00838645;
    result = MinAsn1ParseSignedDataCertificatesEx(result + 2400 + 112, v_stack_mB8, result, Arg4);
    if (sign_flag) goto loc_00838724;
    if ((uint32_t)((uint32_t)(v_stack_mB8)) == 0) goto loc_00838724;
    result = I_MinCryptFindSignerCertificateByIssuerAndSerialNumber(result + 2400 + 192, result + 2400 + 208, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8))), result);
    v_stack_m48 = result;
    if (result != 0) goto loc_0083872E;
loc_00838724:
    goto loc_0083898E;
loc_0083872E:
    *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x20) = v_xmm0;
    *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x30) = v_xmm0;
    *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x40) = v_xmm1;
    v_stack_mD0 = result + 2400 + 240;
    v_stack_mD8 = Arg6;
    result = MinCryptVerifyCertificateWithPolicy2(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8))), result, v_stack_mA0);
    v_stack_mC8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00838793;
    if (((uint32_t)(result)) != 0xC0000603ULL) goto loc_0083899B;
    v_stack_mC0 = 1;
loc_00838793:
    if ((*(uint32_t *)(result + 0x960 + 0xF0)) == 0) goto loc_008387B3;
    result = I_MinCryptGetPlatformManifestBinaryIDAttribute(result + 2400 + 240, Arg6, result, v_stack_mA0);
    v_stack_mC8 = (uint32_t)(result);
    if (sign_flag) goto loc_0083899B;
loc_008387B3:
    if (v_stack_mA0 == 0) goto loc_008387C4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x4)))) & (16)) != 0) goto loc_008387DC;
loc_008387C4:
    if (*(uint64_t *)(arg6 + 0x10) == 0) goto loc_008387DC;
    result = 0;
loc_008387CF:
    v_stack_mA4 = 0;
    if (0 >= (*(uint32_t *)(*(uint64_t *)(arg6 + 0x10) + 0x30))) goto loc_008387DC;
    result = (uint32_t)((result) + 1);
    goto loc_008387CF;
loc_008387DC:
    result = MinCryptDecodeHashAlgorithmIdentifier(result + 2400 + 224, Arg6, result, v_stack_mA0);
    if ((uint32_t)(result) == 0) goto loc_00838989;
    if (v_stack_mA8 == 0) goto loc_00838819;
    result = MinAsn1ExtractContent(*(uint64_t *)(result + 0x960 + 0x68), (uint32_t)(*(uint32_t *)(result + 0x960 + 0x60)), v_stack_m88, v_stack_m80);
    if (!sign_flag) goto loc_0083882B;
    goto loc_00838989;
loc_00838819:
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_mB0));
    v_stack_m80 = v_stack_m98;
loc_0083882B:
    v_stack_mD8 = v_stack_mBC;
    result = MinCryptHashMemory((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 1, v_stack_m88, result + 2400 + 304);
    v_stack_mC8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00838862;
loc_00838858:
    goto loc_00838997;
loc_00838862:
    if ((*(uint32_t *)(result + 0x960 + 0xF0)) == 0) goto loc_0083888E;
    result = I_MinCryptVerifySignerAuthenticatedAttributes((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result + 2400 + 304, v_stack_mBC, result + 2400 + 240);
    v_stack_mC8 = (uint32_t)(result);
    if (sign_flag) goto loc_00838858;
loc_0083888E:
    result = (v_stack_m48) + (176);
    v_stack_mD8 = result;
    result = MinCryptVerifySignedHash2((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result + 2400 + 304, (uint32_t)(v_stack_mBC), result + 2400 + 272);
    v_stack_mC8 = (uint32_t)(result);
    if (sign_flag) goto loc_00838858;
    if (v_stack_mC0 == 0) goto loc_0083899B;
    v_stack_mD0 = v_stack_mC0;
    v_stack_mD8 = v_stack_mB0;
    result = I_MinCryptGetSigningTime(result + 2400, (uint32_t)(v_stack_mB8), result, v_stack_m78);
    v_stack_mC8 = (uint32_t)(result);
    if (sign_flag) goto loc_0083893F;
    if (condition_is_less_or_equal) goto loc_00838949;
    if (v_stack_mB0 < v_stack_m58) goto loc_0083893F;
    if (v_stack_mB0 > v_stack_m50) goto loc_0083893F;
    if (v_stack_mB0 < (*(uint64_t *)(arg6 + 0x20))) goto loc_0083893F;
    result = v_stack_mB0;
    if (v_stack_mB0 >= = (*(uint64_t *)(arg6 + 0x28))) {
        result = 0;
        v_stack_mB0 = 0;
    }
loc_00838949:
    if (0 == 0) {
        result = *(uint32_t *)(arg6 + 0x8);
        *(uint32_t *)(arg6 + 0x8) = (uint32_t)(result);
    }
    result = MincryptIsTimestampBeforeRevocation(Arg6, v_stack_mB0, v_stack_m78, v_stack_m78);
    v_stack_mC8 = (uint32_t)(result);
    if (sign_flag) goto loc_0083899B;
    *(uint32_t *)(arg6 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x8)));
    local_rdi = 0;
    goto loc_00838623;
loc_00838989:
loc_0083898E:
    v_stack_mC8 = (uint32_t)((uint32_t)(0xC0000428ULL));
loc_00838997:
    v_stack_mC4 = (uint32_t)((uint32_t)(0x40000ULL));
loc_0083899B:
    result = (uint32_t)(*(uint32_t *)(arg6 + 0x8));
    local_rdi = (uint32_t)(0xC0000428ULL);
    if (sign_flag) {
        Arg3 = (uint32_t)((uint32_t)(0x40000ULL));
        Arg2 = Arg6;
        Arg1 = (uint32_t)((uint32_t)(0xC0000428ULL));
        result = I_MinCryptBuildErrorPolicy(Arg1, Arg2, Arg3, v_stack_m78);
        local_rdi = (uint32_t)(result);
    }
    if (v_stack_m78 != 0) {
        Arg1 = v_stack_m68;
        result = I_MincryptFreeChainInfo(Arg1, Arg2, Arg3, v_stack_m78);
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        v_stack_m58 = v_xmm0;
    }
    if (result != 0) {
        Arg2 = 0x72634943ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_m78);
    }
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)(local_rdi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x8` | `32` | `R` |
| `Arg6` | `+ 0x8` | `32` | `W` |
| `Arg6` | `+ 0x10` | `64` | `R` |
| `Arg6` | `+ 0x20` | `64` | `R` |
| `Arg6` | `+ 0x28` | `64` | `R` |
| `Arg7` | `+ 0x0` | `128` | `W` |
| `Arg7` | `+ 0x10` | `32` | `W` |
| `Arg7` | `+ 0x10` | `64` | `R` |
| `Arg7` | `+ 0x18` | `64` | `W` |
| `Arg7` | `+ 0x20` | `128` | `W` |
| `Arg7` | `+ 0x30` | `128` | `W` |
| `Arg7` | `+ 0x40` | `128` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00838568&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
