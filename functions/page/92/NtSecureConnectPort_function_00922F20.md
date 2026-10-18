# NtSecureConnectPort

- RVA: `0x00922F20`–`0x00923536` (길이 `1,558` bytes)
- VA: `0x0000000140922F20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D2D8`
- 디코드: `335`개 명령, `1,558/1,558` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00922FAE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009230A3` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x009230C5` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009230DE` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00923165` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0092319E` → [SeCaptureSid](SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x00923225` → [AlpcpCreateClientPort](AlpcpCreateClientPort_function_009270AC.md) (function, `0x009270AC`)
- `0x009232AF` → [AlpcpFormatConnectionRequest](AlpcpFormatConnectionRequest_function_00922A40.md) (function, `0x00922A40`)
- `0x009232FD` → [AlpcpDispatchConnectionRequest](AlpcpDispatchConnectionRequest_function_0092353C.md) (function, `0x0092353C`)
- `0x0092334C` → [AlpcpReceiveLegacyConnectionReply](AlpcpReceiveLegacyConnectionReply_function_00921CA0.md) (function, `0x00921CA0`)
- `0x009233FA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00923411` → [AlpcpDereferenceBlobEx](../88/AlpcpDereferenceBlobEx_function_0088AF00.md) (function, `0x0088AF00`)
- `0x0092341E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00923430` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009234B2` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x009234CE` → [AlpcpLogConnectFail](../74/AlpcpLogConnectFail_function_0074D0D8.md) (function, `0x0074D0D8`)
- `0x009234E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00923501` → [AlpcpLogConnectRequest](../74/AlpcpLogConnectRequest_function_0074D14C.md) (function, `0x0074D14C`)
- `0x00923510` → [AlpcpLogConnectFail](../74/AlpcpLogConnectFail_function_0074D0D8.md) (function, `0x0074D0D8`)
- `0x0092351A` → [AlpcpLogConnectSuccess](../74/AlpcpLogConnectSuccess_function_0074D1BC.md) (function, `0x0074D1BC`)
- `0x0092352C` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)

### Direct callers
- [IopConnectLinkTrackingPort](../71/IopConnectLinkTrackingPort_function_0071B050.md) at `0x0071B0F8`
- [NtConnectPort](NtConnectPort_function_009229F0.md) at `0x00922A2C`

### Static image references
- `0x00922F32` → RVA `0x00E0A740` (`.data`; read)
- `0x009232CD` → RVA `0x00E66D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00922FAE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009230C5` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00923165` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009233FA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0092341E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00923430` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009234E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00922F20  40 56                           push rsi
00922F22  57                              push rdi
00922F23  41 54                           push r12
00922F25  41 55                           push r13
00922F27  41 56                           push r14
00922F29  41 57                           push r15
00922F2B  48 81 EC 98 01 00 00            sub rsp, 0x198
00922F32  48 8B 05 07 78 4E 00            mov rax, qword ptr [rip + 0x4e7807]
00922F39  48 33 C4                        xor rax, rsp
00922F3C  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
00922F44  49 8B F1                        mov rsi, r9
00922F47  4D 8B F8                        mov r15, r8
00922F4A  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00922F52  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
00922F5A  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
00922F62  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00922F6A  4C 8B B4 24 F8 01 00 00         mov r14, qword ptr [rsp + 0x1f8]
00922F72  4C 8B A4 24 10 02 00 00         mov r12, qword ptr [rsp + 0x210]
00922F7A  4C 89 A4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r12
00922F82  4C 8B AC 24 F0 01 00 00         mov r13, qword ptr [rsp + 0x1f0]
00922F8A  48 8B 84 24 08 02 00 00         mov rax, qword ptr [rsp + 0x208]
00922F92  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00922F97  48 83 A4 24 80 00 00 00 00      and qword ptr [rsp + 0x80], 0
00922FA0  33 D2                           xor edx, edx
00922FA2  44 8D 42 40                     lea r8d, [rdx + 0x40]
00922FA6  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00922FAE  E8 8D 3C DA FF                  call 0x1406c6c40
00922FB3  48 83 A4 24 90 00 00 00 00      and qword ptr [rsp + 0x90], 0
00922FBC  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
00922FC2  48 83 A4 24 A0 00 00 00 00      and qword ptr [rsp + 0xa0], 0
00922FCB  0F 57 C0                        xorps xmm0, xmm0
00922FCE  33 C0                           xor eax, eax
00922FD0  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
00922FD8  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
00922FE0  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
00922FE8  21 44 24 64                     and dword ptr [rsp + 0x64], eax
00922FEC  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
00922FF4  89 84 24 78 01 00 00            mov dword ptr [rsp + 0x178], eax
00922FFB  48 21 84 24 88 00 00 00         and qword ptr [rsp + 0x88], rax
00923003  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0092300C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00923013  90                              nop
00923014  33 C0                           xor eax, eax
00923016  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
0092301E  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00923026  0F 57 C9                        xorps xmm1, xmm1
00923029  0F 11 8C 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm1
00923031  0F 11 8C 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm1
00923039  0F 11 8C 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm1
00923041  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0092304A  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00923050  88 44 24 60                     mov byte ptr [rsp + 0x60], al
00923054  84 C0                           test al, al
00923056  0F 84 EC 03 00 00               je 0x140923448
0092305C  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
00923066  48 8B CF                        mov rcx, rdi
00923069  48 39 BC 24 A8 00 00 00         cmp qword ptr [rsp + 0xa8], rdi
00923071  48 0F 42 8C 24 A8 00 00 00      cmovb rcx, qword ptr [rsp + 0xa8]
0092307A  48 8B 01                        mov rax, qword ptr [rcx]
0092307D  48 89 01                        mov qword ptr [rcx], rax
00923080  4D 85 E4                        test r12, r12
00923083  74 23                           je 0x1409230a8
00923085  48 8B C7                        mov rax, rdi
00923088  4C 3B E7                        cmp r12, rdi
0092308B  49 0F 42 C4                     cmovb rax, r12
0092308F  90                              nop
00923090  8B 00                           mov eax, dword ptr [rax]
00923092  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00923096  8B D0                           mov edx, eax
00923098  41 B8 01 00 00 00               mov r8d, 1
0092309E  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009230A3  E8 18 61 FC FF                  call 0x1408e91c0
009230A8  48 85 F6                        test rsi, rsi
009230AB  74 4B                           je 0x1409230f8
009230AD  48 8B D7                        mov rdx, rdi
009230B0  48 3B F7                        cmp rsi, rdi
009230B3  48 0F 42 D6                     cmovb rdx, rsi
009230B7  41 B8 30 00 00 00               mov r8d, 0x30
009230BD  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
009230C5  E8 06 99 D9 FF                  call 0x1406bc9d0
009230CA  83 BC 24 C0 00 00 00 30         cmp dword ptr [rsp + 0xc0], 0x30
009230D2  0F 85 A3 00 00 00               jne 0x14092317b
009230D8  40 F6 C6 03                     test sil, 3
009230DC  74 06                           je 0x1409230e4
009230DE  E8 ED 6E F7 FF                  call 0x140899fd0
009230E3  CC                              int3
009230E4  48 8B CF                        mov rcx, rdi
009230E7  48 3B F7                        cmp rsi, rdi
009230EA  48 0F 42 CE                     cmovb rcx, rsi
009230EE  8A 01                           mov al, byte ptr [rcx]
009230F0  88 01                           mov byte ptr [rcx], al
009230F2  8A 41 2F                        mov al, byte ptr [rcx + 0x2f]
009230F5  88 41 2F                        mov byte ptr [rcx + 0x2f], al
009230F8  4D 85 F6                        test r14, r14
009230FB  74 30                           je 0x14092312d
009230FD  48 8B C7                        mov rax, rdi
00923100  4C 3B F7                        cmp r14, rdi
00923103  49 0F 42 C6                     cmovb rax, r14
00923107  90                              nop
00923108  8B 00                           mov eax, dword ptr [rax]
0092310A  83 F8 18                        cmp eax, 0x18
0092310D  0F 85 9F 00 00 00               jne 0x1409231b2
00923113  41 F6 C6 03                     test r14b, 3
00923117  75 C5                           jne 0x1409230de
00923119  48 8B CF                        mov rcx, rdi
0092311C  4C 3B F7                        cmp r14, rdi
0092311F  49 0F 42 CE                     cmovb rcx, r14
00923123  8A 01                           mov al, byte ptr [rcx]
00923125  88 01                           mov byte ptr [rcx], al
00923127  8A 41 17                        mov al, byte ptr [rcx + 0x17]
0092312A  88 41 17                        mov byte ptr [rcx + 0x17], al
0092312D  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00923135  48 85 C0                        test rax, rax
00923138  74 0E                           je 0x140923148
0092313A  48 8B CF                        mov rcx, rdi
0092313D  48 3B C7                        cmp rax, rdi
00923140  48 0F 42 C8                     cmovb rcx, rax
00923144  8B 01                           mov eax, dword ptr [rcx]
00923146  89 01                           mov dword ptr [rcx], eax
00923148  4D 85 FF                        test r15, r15
0092314B  74 1D                           je 0x14092316a
0092314D  4C 3B FF                        cmp r15, rdi
00923150  49 0F 42 FF                     cmovb rdi, r15
00923154  41 B8 0C 00 00 00               mov r8d, 0xc
0092315A  48 8B D7                        mov rdx, rdi
0092315D  48 8D 8C 24 70 01 00 00         lea rcx, [rsp + 0x170]
00923165  E8 66 98 D9 FF                  call 0x1406bc9d0
0092316A  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
0092316F  44 8A 64 24 60                  mov r12b, byte ptr [rsp + 0x60]
00923174  4D 85 ED                        test r13, r13
00923177  75 10                           jne 0x140923189
00923179  EB 45                           jmp 0x1409231c0
0092317B  BF 0D 00 00 C0                  mov edi, 0xc000000d
00923180  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
00923184  E9 95 02 00 00                  jmp 0x14092341e
00923189  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0092318E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00923193  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00923198  41 8A D4                        mov dl, r12b
0092319B  49 8B CD                        mov rcx, r13
0092319E  E8 31 45 00 00                  call 0x1409276d4
009231A3  8B F8                           mov edi, eax
009231A5  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
009231A9  85 C0                           test eax, eax
009231AB  79 13                           jns 0x1409231c0
009231AD  E9 6C 02 00 00                  jmp 0x14092341e
009231B2  BF 0D 00 00 C0                  mov edi, 0xc000000d
009231B7  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
009231BB  E9 5E 02 00 00                  jmp 0x14092341e
009231C0  EB 0B                           jmp 0x1409231cd
009231C2  8B F8                           mov edi, eax
009231C4  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
009231C8  E9 51 02 00 00                  jmp 0x14092341e
009231CD  49 F7 DF                        neg r15
009231D0  48 1B C0                        sbb rax, rax
009231D3  48 8D 8C 24 70 01 00 00         lea rcx, [rsp + 0x170]
009231DB  48 23 C1                        and rax, rcx
009231DE  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
009231E3  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009231E8  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
009231ED  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
009231F2  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
009231F8  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
009231FE  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00923204  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0092320A  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
00923212  45 33 C0                        xor r8d, r8d
00923215  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
0092321D  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00923225  E8 82 3E 00 00                  call 0x1409270ac
0092322A  8B F8                           mov edi, eax
0092322C  4D 3B FD                        cmp r15, r13
0092322F  0F 85 A3 02 00 00               jne 0x1409234d8
00923235  85 FF                           test edi, edi
00923237  0F 88 E1 01 00 00               js 0x14092341e
0092323D  0F B7 44 24 64                  movzx eax, word ptr [rsp + 0x64]
00923242  66 89 84 24 08 01 00 00         mov word ptr [rsp + 0x108], ax
0092324A  48 8B C6                        mov rax, rsi
0092324D  48 F7 D8                        neg rax
00923250  48 1B C0                        sbb rax, rax
00923253  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
0092325B  48 23 C1                        and rax, rcx
0092325E  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00923266  44 88 64 24 48                  mov byte ptr [rsp + 0x48], r12b
0092326B  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00923270  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00923278  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0092327D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00923282  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00923288  48 8D 84 24 08 01 00 00         lea rax, [rsp + 0x108]
00923290  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00923295  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0092329A  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
009232A2  4D 8B C7                        mov r8, r15
009232A5  33 D2                           xor edx, edx
009232A7  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
009232AF  E8 8C F7 FF FF                  call 0x140922a40
009232B4  8B F8                           mov edi, eax
009232B6  85 C0                           test eax, eax
009232B8  0F 88 39 01 00 00               js 0x1409233f7
009232BE  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
009232C6  45 8B A5 08 01 00 00            mov r12d, dword ptr [r13 + 0x108]
009232CD  80 3D 2C 3A 54 00 00            cmp byte ptr [rip + 0x543a2c], 0
009232D4  0F 85 24 02 00 00               jne 0x1409234fe
009232DA  4C 89 BC 24 30 01 00 00         mov qword ptr [rsp + 0x130], r15
009232E2  4C 89 AC 24 38 01 00 00         mov qword ptr [rsp + 0x138], r13
009232EA  C7 84 24 60 01 00 00 00 00 02 00  mov dword ptr [rsp + 0x160], 0x20000
009232F5  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
009232FD  E8 3A 02 00 00                  call 0x14092353c
00923302  8B F8                           mov edi, eax
00923304  85 C0                           test eax, eax
00923306  0F 88 9A 01 00 00               js 0x1409234a6
0092330C  49 8B C6                        mov rax, r14
0092330F  48 F7 D8                        neg rax
00923312  48 1B C9                        sbb rcx, rcx
00923315  48 8D 84 24 F0 00 00 00         lea rax, [rsp + 0xf0]
0092331D  48 23 C8                        and rcx, rax
00923320  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00923325  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0092332D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00923332  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
0092333A  4C 8D 44 24 64                  lea r8, [rsp + 0x64]
0092333F  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00923344  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
0092334C  E8 4F E9 FF FF                  call 0x140921ca0
00923351  8B F8                           mov edi, eax
00923353  85 C0                           test eax, eax
00923355  0F 85 61 01 00 00               jne 0x1409234bc
0092335B  38 05 9F 39 54 00               cmp byte ptr [rip + 0x54399f], al
00923361  0F 85 B0 01 00 00               jne 0x140923517
00923367  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0092336F  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00923377  48 89 01                        mov qword ptr [rcx], rax
0092337A  48 85 F6                        test rsi, rsi
0092337D  74 23                           je 0x1409233a2
0092337F  0F 10 84 24 C0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xc0]
00923387  0F 11 06                        movups xmmword ptr [rsi], xmm0
0092338A  0F 10 8C 24 D0 00 00 00         movups xmm1, xmmword ptr [rsp + 0xd0]
00923392  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
00923396  0F 10 84 24 E0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xe0]
0092339E  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
009233A2  4D 85 F6                        test r14, r14
009233A5  74 1B                           je 0x1409233c2
009233A7  0F 10 84 24 F0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xf0]
009233AF  41 0F 11 06                     movups xmmword ptr [r14], xmm0
009233B3  F2 0F 10 84 24 00 01 00 00      movsd xmm0, qword ptr [rsp + 0x100]
009233BC  F2 41 0F 11 46 10               movsd qword ptr [r14 + 0x10], xmm0
009233C2  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009233CA  48 85 C9                        test rcx, rcx
009233CD  74 06                           je 0x1409233d5
009233CF  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
009233D3  89 01                           mov dword ptr [rcx], eax
009233D5  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
009233DD  48 85 C9                        test rcx, rcx
009233E0  74 09                           je 0x1409233eb
009233E2  41 8B 87 10 01 00 00            mov eax, dword ptr [r15 + 0x110]
009233E9  89 01                           mov dword ptr [rcx], eax
009233EB  EB 0A                           jmp 0x1409233f7
009233ED  8B F8                           mov edi, eax
009233EF  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
009233F7  49 8B CF                        mov rcx, r15
009233FA  E8 51 5F 9D FF                  call 0x1402f9350
009233FF  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00923407  48 85 C9                        test rcx, rcx
0092340A  74 0A                           je 0x140923416
0092340C  BA 01 00 00 00                  mov edx, 1
00923411  E8 EA 7A F6 FF                  call 0x14088af00
00923416  85 FF                           test edi, edi
00923418  0F 85 06 01 00 00               jne 0x140923524
0092341E  E8 8D A4 93 FF                  call 0x14025d8b0
00923423  8B C7                           mov eax, edi
00923425  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
0092342D  48 33 CC                        xor rcx, rsp
00923430  E8 0B 92 D8 FF                  call 0x1406ac640
00923435  48 81 C4 98 01 00 00            add rsp, 0x198
0092343C  41 5F                           pop r15
0092343E  41 5E                           pop r14
00923440  41 5D                           pop r13
00923442  41 5C                           pop r12
00923444  5F                              pop rdi
00923445  5E                              pop rsi
00923446  C3                              ret
00923447  CC                              int3
00923448  4D 85 E4                        test r12, r12
0092344B  0F 85 A0 00 00 00               jne 0x1409234f1
00923451  48 85 F6                        test rsi, rsi
00923454  74 23                           je 0x140923479
00923456  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00923459  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
00923461  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
00923465  0F 11 8C 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm1
0092346D  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
00923471  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00923479  4D 85 FF                        test r15, r15
0092347C  74 19                           je 0x140923497
0092347E  F2 41 0F 10 07                  movsd xmm0, qword ptr [r15]
00923483  F2 0F 11 84 24 70 01 00 00      movsd qword ptr [rsp + 0x170], xmm0
0092348C  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00923490  89 84 24 78 01 00 00            mov dword ptr [rsp + 0x178], eax
00923497  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
0092349C  44 8A 64 24 60                  mov r12b, byte ptr [rsp + 0x60]
009234A1  E9 27 FD FF FF                  jmp 0x1409231cd
009234A6  80 3D 53 38 54 00 00            cmp byte ptr [rip + 0x543853], 0
009234AD  75 5C                           jne 0x14092350b
009234AF  49 8B CD                        mov rcx, r13
009234B2  E8 29 46 F7 FF                  call 0x140897ae0
009234B7  E9 3B FF FF FF                  jmp 0x1409233f7
009234BC  80 3D 3D 38 54 00 00            cmp byte ptr [rip + 0x54383d], 0
009234C3  0F 84 2E FF FF FF               je 0x1409233f7
009234C9  8B D0                           mov edx, eax
009234CB  41 8B CC                        mov ecx, r12d
009234CE  E8 05 9C E2 FF                  call 0x14074d0d8
009234D3  E9 1F FF FF FF                  jmp 0x1409233f7
009234D8  41 80 FC 01                     cmp r12b, 1
009234DC  0F 87 53 FD FF FF               ja 0x140923235
009234E2  33 D2                           xor edx, edx
009234E4  49 8B CF                        mov rcx, r15
009234E7  E8 84 F3 25 00                  call 0x140b82870
009234EC  E9 44 FD FF FF                  jmp 0x140923235
009234F1  41 8B 04 24                     mov eax, dword ptr [r12]
009234F5  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
009234F9  E9 53 FF FF FF                  jmp 0x140923451
009234FE  49 8B CD                        mov rcx, r13
00923501  E8 46 9C E2 FF                  call 0x14074d14c
00923506  E9 CF FD FF FF                  jmp 0x1409232da
0092350B  8B D0                           mov edx, eax
0092350D  41 8B CC                        mov ecx, r12d
00923510  E8 C3 9B E2 FF                  call 0x14074d0d8
00923515  EB 98                           jmp 0x1409234af
00923517  41 8B CC                        mov ecx, r12d
0092351A  E8 9D 9C E2 FF                  call 0x14074d1bc
0092351F  E9 43 FE FF FF                  jmp 0x140923367
00923524  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0092352C  E8 3F 53 F4 FF                  call 0x140868870
00923531  E9 E8 FE FF FF                  jmp 0x14092341e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSecureConnectPort(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m164;
    unsigned __int8 v_stack_m168;
    unsigned __int8 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int8 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p170;
    unsigned int v_stack_p178;
    unsigned __int8 v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pE0;

    v_rsp = (v_rsp) - (408);
    result = (*(unsigned __int64 *)(v_rip + 5142535)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m130 = a2;
    v_stack_m120 = a1;
    v_stack_m118 = a7;
    v_stack_m110 = a9;
    v_stack_m150 = a8;
    a2 = 0;
    result = memset(v_stack_m98, a2, a2 + 64, a4);
    result = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = 0;
    v_stack_m58 = 0;
    v_stack_m50 = 0;
    result = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = 0;
    v_stack_m108 = v_xmm1;
    v_stack_mF8 = v_xmm1;
    v_stack_mE8 = v_xmm1;
    v_stack_m168 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00923448;
    a1 = v_rdi;
    if (v_stack_m120 < v_rdi) { a1 = v_stack_m120; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    result = *(unsigned __int64 *)(a1);
    if (a9 != 0) {
        result = v_rdi;
        if (a9 < v_rdi) { result = a9; }
        result = *(unsigned int *)(result);
        v_stack_m164 = (unsigned int)(result);
        a2 = (unsigned int)(result);
        a3 = 1;
        a1 = v_stack_m150;
        result = ProbeForWrite(a1, a2, a3, a4);
    }
    if (a4 == 0) goto loc_009230F8;
    a2 = v_rdi;
    if (a4 < v_rdi) { a2 = a4; }
    result = RtlCopyVolatileMemory(v_stack_m108, a2, 48, a4);
    if (v_stack_m108 != 48) goto loc_0092317B;
    if ((((unsigned __int8)(a4)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m108, a2, 48, a4);
    }
    a1 = v_rdi;
    if (a4 < v_rdi) { a1 = a4; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 47) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 47));
loc_009230F8:
    if (a6 == 0) goto loc_0092312D;
    result = v_rdi;
    if (a6 < v_rdi) { result = a6; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) != 24) goto loc_009231B2;
    if ((((unsigned __int8)(a6)) & (3)) != 0) goto loc_009230DE;
    a1 = v_rdi;
    if (a6 < v_rdi) { a1 = a6; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 23) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 23));
loc_0092312D:
    result = v_stack_m118;
    if (v_stack_m118 != 0) {
        a1 = v_rdi;
        if (v_stack_m118 < v_rdi) { a1 = v_stack_m118; }
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    if (a3 != 0) {
        if (a3 < v_rdi) { v_rdi = a3; }
        a3 = 12;
        a2 = v_rdi;
        a1 = v_stack_m58;
        result = RtlCopyVolatileMemory(a1, a2, a3, a4);
    }
    v_stack_m158 = a5;
    if (a5 != 0) goto loc_00923189;
    goto loc_009231C0;
loc_0092317B:
    v_stack_m160 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0092341E;
loc_00923189:
    v_stack_m198 = v_stack_m158;
    v_stack_m1A0 = 1;
    result = SeCaptureSid(a5, (unsigned __int8)(v_stack_m168), a3, a4);
    v_stack_m160 = (unsigned int)(result);
    if (!sign_flag) goto loc_009231C0;
    goto loc_0092341E;
loc_009231B2:
    v_stack_m160 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0092341E;
loc_009231C0:
    goto loc_009231CD;
loc_009231CD:
    v_r15 = -(a3);
    result = (result) & (v_stack_m58);
    v_stack_m178 = 1;
    v_stack_m180 = result;
    v_stack_m188 = v_stack_m158;
    a3 = 0;
    result = AlpcpCreateClientPort(v_stack_m138, v_stack_m148, a3, v_stack_m130);
    if (v_stack_m158 != a5) goto loc_009234D8;
loc_00923235:
    if (sign_flag) goto loc_0092341E;
    v_stack_mC0 = (unsigned __int16)(v_stack_m164);
    result = -(a4);
    result = (result) & (v_stack_m108);
    v_stack_m130 = result;
    v_stack_m180 = (unsigned __int8)(v_stack_m168);
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m140;
    v_stack_m198 = result;
    v_stack_m1A8 = v_stack_mC0;
    a2 = 0;
    result = AlpcpFormatConnectionRequest(v_stack_m128, a2, v_stack_m148, v_stack_m150);
    if (sign_flag) goto loc_009233F7;
    if ((*(unsigned __int8 *)(v_rip + 5519916)) != 0) goto loc_009234FE;
loc_009232DA:
    v_stack_m98 = v_stack_m148;
    v_stack_m90 = v_stack_m128;
    v_stack_m68 = 0x20000ULL;
    result = AlpcpDispatchConnectionRequest(v_stack_m98, a2, v_stack_m148, v_stack_m150);
    if (sign_flag) goto loc_009234A6;
    result = -(a6);
    a1 = (v_stack_m98) & (v_stack_mD8);
    v_stack_m1A0 = a1;
    v_stack_m1A8 = v_stack_m130;
    result = AlpcpReceiveLegacyConnectionReply(v_stack_m98, v_stack_m150, v_stack_m164, v_stack_m140);
    if ((unsigned int)(result) != 0) goto loc_009234BC;
    if ((*(unsigned __int8 *)(v_rip + 5519775)) != ((unsigned __int8)(result))) goto loc_00923517;
loc_00923367:
    *(unsigned __int64 *)(v_stack_m120) = v_stack_m138;
    if (a4 != 0) {
        *(unsigned __int64 *)(a4) = v_xmm0;
        *(unsigned __int64 *)(a4 + 16) = v_xmm1;
        *(unsigned __int64 *)(a4 + 32) = v_xmm0;
    }
    if (a6 != 0) {
        *(unsigned __int64 *)(a6) = v_xmm0;
        *(unsigned __int64 *)(a6 + 16) = v_xmm0;
    }
    result = v_stack_m138;
    if (v_stack_m110 != 0) {
        result = v_stack_m164;
        *(unsigned int *)(v_stack_m110) = (unsigned int)(result);
    }
    if (v_stack_m118 != 0) {
        result = *(unsigned int *)(v_stack_m148 + 272);
        *(unsigned int *)(v_stack_m118) = (unsigned int)(result);
    }
    goto loc_009233F7;
loc_009233F7:
    result = ObfDereferenceObject(v_stack_m148, v_stack_m150, v_stack_m164, v_stack_m140);
    if (v_stack_m140 != 0) {
        a2 = 1;
        result = AlpcpDereferenceBlobEx(v_stack_m140, a2, v_stack_m164, v_stack_m140);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_00923524;
loc_0092341E:
    result = KeLeaveCriticalRegion(v_stack_m140, a2, v_stack_m164, v_stack_m140);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m164, v_stack_m140);
    v_rsp = (v_rsp) + (408);
    return result;
loc_00923448:
    if ((unsigned int)(*(unsigned int *)(v_stack_m128 + 264)) != 0) goto loc_009234F1;
loc_00923451:
    if (a4 != 0) {
        v_stack_pC0 = v_xmm0;
        v_stack_pD0 = v_xmm1;
        v_stack_pE0 = v_xmm0;
    }
    if (v_stack_m148 != 0) {
        v_stack_p170 = v_xmm0;
        result = *(unsigned int *)(v_stack_m148 + 8);
        v_stack_p178 = (unsigned int)(result);
    }
    v_stack_p70 = v_stack_m128;
    goto loc_009231CD;
loc_009234A6:
    if ((*(unsigned __int8 *)(v_rip + 5519443)) != 0) goto loc_0092350B;
loc_009234AF:
    result = AlpcpUnlockMessage(v_stack_m128, a2, v_stack_m164, v_stack_m140);
    goto loc_009233F7;
loc_009234BC:
    if ((*(unsigned __int8 *)(v_rip + 5519421)) == 0) goto loc_009233F7;
    result = AlpcpLogConnectFail((unsigned int)((unsigned int)(v_stack_p60)), (unsigned int)((unsigned int)(result)), v_stack_m164, v_stack_m140);
    goto loc_009233F7;
loc_009234D8:
    if (((unsigned __int8)(v_stack_p60)) > 1) goto loc_00923235;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m148, a2, v_stack_m164, v_stack_m140);
    goto loc_00923235;
loc_009234F1:
    v_stack_p64 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60)));
    goto loc_00923451;
loc_009234FE:
    result = AlpcpLogConnectRequest(v_stack_m128, a2, v_stack_m164, v_stack_m140);
    goto loc_009232DA;
loc_0092350B:
    result = AlpcpLogConnectFail((unsigned int)((unsigned int)(v_stack_p60)), (unsigned int)((unsigned int)(result)), v_stack_m164, v_stack_m140);
    goto loc_009234AF;
loc_00923517:
    result = AlpcpLogConnectSuccess((unsigned int)((unsigned int)(v_stack_p60)), (unsigned int)((unsigned int)(result)), v_stack_m164, v_stack_m140);
    goto loc_00923367;
loc_00923524:
    result = NtClose(v_stack_p90, (unsigned int)((unsigned int)(result)), v_stack_m164, v_stack_m140);
    goto loc_0092341E;
}
```

## 5. (Beta) C Style

```c
int64_t NtSecureConnectPort(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m164;
    uint8_t v_stack_m168;
    uint8_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint8_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p170;
    uint32_t v_stack_p178;
    uint8_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p70;
    uint64_t v_stack_p90;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pE0;

    local_rsp = (local_rsp) - (408);
    result = (*(uint64_t *)(v_rip + 0x4E7807)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m130 = Arg2;
    v_stack_m120 = Arg1;
    v_stack_m118 = Arg7;
    v_stack_m110 = Arg9;
    v_stack_m150 = Arg8;
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, Arg2 + 64, Arg4);
    result = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = 0;
    v_stack_m58 = 0;
    v_stack_m50 = 0;
    result = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = 0;
    v_stack_m108 = v_xmm1;
    v_stack_mF8 = v_xmm1;
    v_stack_mE8 = v_xmm1;
    v_stack_m168 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00923448;
    Arg1 = local_rdi;
    if (v_stack_m120 < local_rdi) { Arg1 = v_stack_m120; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    result = *(uint64_t *)(Arg1);
    if (Arg9 != 0) {
        result = local_rdi;
        if (Arg9 < local_rdi) { result = Arg9; }
        result = *(uint32_t *)(result);
        v_stack_m164 = (uint32_t)(result);
        Arg2 = (uint32_t)(result);
        Arg3 = 1;
        Arg1 = v_stack_m150;
        result = ProbeForWrite(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg4 == 0) goto loc_009230F8;
    Arg2 = local_rdi;
    if (Arg4 < local_rdi) { Arg2 = Arg4; }
    result = RtlCopyVolatileMemory(v_stack_m108, Arg2, 48, Arg4);
    if (v_stack_m108 != 48) goto loc_0092317B;
    if ((((uint8_t)(Arg4)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m108, Arg2, 48, Arg4);
    }
    Arg1 = local_rdi;
    if (Arg4 < local_rdi) { Arg1 = Arg4; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x2F) = (uint8_t)(*(uint8_t *)(Arg1 + 0x2F));
loc_009230F8:
    if (Arg6 == 0) goto loc_0092312D;
    result = local_rdi;
    if (Arg6 < local_rdi) { result = Arg6; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) != 24) goto loc_009231B2;
    if ((((uint8_t)(Arg6)) & (3)) != 0) goto loc_009230DE;
    Arg1 = local_rdi;
    if (Arg6 < local_rdi) { Arg1 = Arg6; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x17) = (uint8_t)(*(uint8_t *)(Arg1 + 0x17));
loc_0092312D:
    result = v_stack_m118;
    if (v_stack_m118 != 0) {
        Arg1 = local_rdi;
        if (v_stack_m118 < local_rdi) { Arg1 = v_stack_m118; }
        result = *(uint32_t *)(Arg1);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
    }
    if (Arg3 != 0) {
        if (Arg3 < local_rdi) { local_rdi = Arg3; }
        Arg3 = 12;
        Arg2 = local_rdi;
        Arg1 = v_stack_m58;
        result = RtlCopyVolatileMemory(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m158 = Arg5;
    if (Arg5 != 0) goto loc_00923189;
    goto loc_009231C0;
loc_0092317B:
    v_stack_m160 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0092341E;
loc_00923189:
    v_stack_m198 = v_stack_m158;
    v_stack_m1A0 = 1;
    result = SeCaptureSid(Arg5, (uint8_t)(v_stack_m168), Arg3, Arg4);
    v_stack_m160 = (uint32_t)(result);
    if (!sign_flag) goto loc_009231C0;
    goto loc_0092341E;
loc_009231B2:
    v_stack_m160 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0092341E;
loc_009231C0:
    goto loc_009231CD;
loc_009231CD:
    local_r15 = -(Arg3);
    result = (result) & (v_stack_m58);
    v_stack_m178 = 1;
    v_stack_m180 = result;
    v_stack_m188 = v_stack_m158;
    Arg3 = 0;
    result = AlpcpCreateClientPort(v_stack_m138, v_stack_m148, Arg3, v_stack_m130);
    if (v_stack_m158 != Arg5) goto loc_009234D8;
loc_00923235:
    if (sign_flag) goto loc_0092341E;
    v_stack_mC0 = (uint16_t)(v_stack_m164);
    result = -(Arg4);
    result = (result) & (v_stack_m108);
    v_stack_m130 = result;
    v_stack_m180 = (uint8_t)(v_stack_m168);
    v_stack_m188 = 1;
    v_stack_m190 = v_stack_m140;
    v_stack_m198 = result;
    v_stack_m1A8 = v_stack_mC0;
    Arg2 = 0;
    result = AlpcpFormatConnectionRequest(v_stack_m128, Arg2, v_stack_m148, v_stack_m150);
    if (sign_flag) goto loc_009233F7;
    if ((*(uint8_t *)(v_rip + 0x543A2C)) != 0) goto loc_009234FE;
loc_009232DA:
    v_stack_m98 = v_stack_m148;
    v_stack_m90 = v_stack_m128;
    v_stack_m68 = 0x20000ULL;
    result = AlpcpDispatchConnectionRequest(v_stack_m98, Arg2, v_stack_m148, v_stack_m150);
    if (sign_flag) goto loc_009234A6;
    result = -(Arg6);
    Arg1 = (v_stack_m98) & (v_stack_mD8);
    v_stack_m1A0 = Arg1;
    v_stack_m1A8 = v_stack_m130;
    result = AlpcpReceiveLegacyConnectionReply(v_stack_m98, v_stack_m150, v_stack_m164, v_stack_m140);
    if ((uint32_t)(result) != 0) goto loc_009234BC;
    if ((*(uint8_t *)(v_rip + 0x54399F)) != ((uint8_t)(result))) goto loc_00923517;
loc_00923367:
    *(uint64_t *)(v_stack_m120) = v_stack_m138;
    if (Arg4 != 0) {
        *(uint64_t *)(Arg4) = v_xmm0;
        *(uint64_t *)(Arg4 + 0x10) = v_xmm1;
        *(uint64_t *)(Arg4 + 0x20) = v_xmm0;
    }
    if (Arg6 != 0) {
        *(uint64_t *)(Arg6) = v_xmm0;
        *(uint64_t *)(Arg6 + 0x10) = v_xmm0;
    }
    result = v_stack_m138;
    if (v_stack_m110 != 0) {
        result = v_stack_m164;
        *(uint32_t *)(v_stack_m110) = (uint32_t)(result);
    }
    if (v_stack_m118 != 0) {
        result = *(uint32_t *)(v_stack_m148 + 0x110);
        *(uint32_t *)(v_stack_m118) = (uint32_t)(result);
    }
    goto loc_009233F7;
loc_009233F7:
    result = ObfDereferenceObject(v_stack_m148, v_stack_m150, v_stack_m164, v_stack_m140);
    if (v_stack_m140 != 0) {
        Arg2 = 1;
        result = AlpcpDereferenceBlobEx(v_stack_m140, Arg2, v_stack_m164, v_stack_m140);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_00923524;
loc_0092341E:
    result = KeLeaveCriticalRegion(v_stack_m140, Arg2, v_stack_m164, v_stack_m140);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m164, v_stack_m140);
    local_rsp = (local_rsp) + (408);
    return result;
loc_00923448:
    if ((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x108)) != 0) goto loc_009234F1;
loc_00923451:
    if (Arg4 != 0) {
        v_stack_pC0 = v_xmm0;
        v_stack_pD0 = v_xmm1;
        v_stack_pE0 = v_xmm0;
    }
    if (v_stack_m148 != 0) {
        v_stack_p170 = v_xmm0;
        result = *(uint32_t *)(v_stack_m148 + 0x8);
        v_stack_p178 = (uint32_t)(result);
    }
    v_stack_p70 = v_stack_m128;
    goto loc_009231CD;
loc_009234A6:
    if ((*(uint8_t *)(v_rip + 0x543853)) != 0) goto loc_0092350B;
loc_009234AF:
    result = AlpcpUnlockMessage(v_stack_m128, Arg2, v_stack_m164, v_stack_m140);
    goto loc_009233F7;
loc_009234BC:
    if ((*(uint8_t *)(v_rip + 0x54383D)) == 0) goto loc_009233F7;
    result = AlpcpLogConnectFail((uint32_t)((uint32_t)(v_stack_p60)), (uint32_t)((uint32_t)(result)), v_stack_m164, v_stack_m140);
    goto loc_009233F7;
loc_009234D8:
    if (((uint8_t)(v_stack_p60)) > 1) goto loc_00923235;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m148, Arg2, v_stack_m164, v_stack_m140);
    goto loc_00923235;
loc_009234F1:
    v_stack_p64 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60)));
    goto loc_00923451;
loc_009234FE:
    result = AlpcpLogConnectRequest(v_stack_m128, Arg2, v_stack_m164, v_stack_m140);
    goto loc_009232DA;
loc_0092350B:
    result = AlpcpLogConnectFail((uint32_t)((uint32_t)(v_stack_p60)), (uint32_t)((uint32_t)(result)), v_stack_m164, v_stack_m140);
    goto loc_009234AF;
loc_00923517:
    result = AlpcpLogConnectSuccess((uint32_t)((uint32_t)(v_stack_p60)), (uint32_t)((uint32_t)(result)), v_stack_m164, v_stack_m140);
    goto loc_00923367;
loc_00923524:
    result = NtClose(v_stack_p90, (uint32_t)((uint32_t)(result)), v_stack_m164, v_stack_m140);
    goto loc_0092341E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00922F20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
