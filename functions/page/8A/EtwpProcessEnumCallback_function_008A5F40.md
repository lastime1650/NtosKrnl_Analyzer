# EtwpProcessEnumCallback

- RVA: `0x008A5F40`–`0x008A62FC` (길이 `956` bytes)
- VA: `0x00000001408A5F40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F0BC`
- 디코드: `242`개 명령, `956/956` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x008A5F8C` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x008A5FAC` → [EtwpIsProcessZombie](EtwpIsProcessZombie_function_008A6304.md) (function, `0x008A6304`)
- `0x008A601A` → [EtwpEnumerateAddressSpace](EtwpEnumerateAddressSpace_function_008A7590.md) (function, `0x008A7590`)
- `0x008A6056` → [PsEnumProcessThreads](../8C/PsEnumProcessThreads_function_008C9B30.md) (function, `0x008C9B30`)
- `0x008A606E` → [EtwpProcessPerfCtrsRundown](EtwpProcessPerfCtrsRundown_function_008A5E08.md) (function, `0x008A5E08`)
- `0x008A608F` → [EtwpTraceProcessRundown](EtwpTraceProcessRundown_function_008A5024.md) (function, `0x008A5024`)
- `0x008A60A0` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x008A60AC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008A60BB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008A60F6` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x008A610B` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x008A612A` → [EtwpSysModuleRunDown](EtwpSysModuleRunDown_function_008A43C0.md) (function, `0x008A43C0`)
- `0x008A6149` → [EtwpTraceProcessRundown](EtwpTraceProcessRundown_function_008A5024.md) (function, `0x008A5024`)
- `0x008A6172` → [EtwpEnumerateAddressSpace](EtwpEnumerateAddressSpace_function_008A7590.md) (function, `0x008A7590`)
- `0x008A61A8` → [EtwpEnumerateWorkingSet](../7B/EtwpEnumerateWorkingSet_function_007BFFA4.md) (function, `0x007BFFA4`)
- `0x008A61DA` → [EtwpTraceProcessRundown](EtwpTraceProcessRundown_function_008A5024.md) (function, `0x008A5024`)
- `0x008A620B` → [PsEnumProcessThreads](../8C/PsEnumProcessThreads_function_008C9B30.md) (function, `0x008C9B30`)
- `0x008A6228` → [EtwpSysModuleRunDown](EtwpSysModuleRunDown_function_008A43C0.md) (function, `0x008A43C0`)
- `0x008A6235` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x008A6260` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x008A626F` → [EtwpThreadEnumCallback](../8C/EtwpThreadEnumCallback_function_008C9BD0.md) (function, `0x008C9BD0`)
- `0x008A6277` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x008A6289` → [EtwpThreadEnumCallback](../8C/EtwpThreadEnumCallback_function_008C9BD0.md) (function, `0x008C9BD0`)
- `0x008A62AF` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x008A62BE` → [EtwpThreadEnumCallback](../8C/EtwpThreadEnumCallback_function_008C9BD0.md) (function, `0x008C9BD0`)
- `0x008A62D5` → [EtwpEnumerateWorkingSet](../7B/EtwpEnumerateWorkingSet_function_007BFFA4.md) (function, `0x007BFFA4`)
- `0x008A62F2` → [EtwpObjectHandleRundown](../7C/EtwpObjectHandleRundown_function_007C047C.md) (function, `0x007C047C`)

### Direct callers
- [EtwpProcessThreadImageRundown](../9E/EtwpProcessThreadImageRundown_function_009E4568.md) at `0x009E460C`
- [sub_00B3066E](../B3/Unknown_function_00B3066E.md) at `0x00B306AB`

### Static image references
- `0x008A5F54` → RVA `0x00E0A740` (`.data`; read)
- `0x008A5F98` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x008A5FB9` → RVA `0x00FC6B70` (`ALMOSTRO`; read)
- `0x008A604C` → RVA `0x008C9BD0` (`EtwpThreadEnumCallback`; read)
- `0x008A6118` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x008A624C` → RVA `0x00FC6A80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x008A5F8C` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x008A60A0` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x008A60AC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008A60BB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008A60F6` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x008A610B` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x008A6235` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x008A6260` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x008A6277` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x008A62AF` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A5F40  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008A5F45  55                              push rbp
008A5F46  56                              push rsi
008A5F47  57                              push rdi
008A5F48  41 54                           push r12
008A5F4A  41 55                           push r13
008A5F4C  41 56                           push r14
008A5F4E  41 57                           push r15
008A5F50  48 83 EC 60                     sub rsp, 0x60
008A5F54  48 8B 05 E5 47 56 00            mov rax, qword ptr [rip + 0x5647e5]
008A5F5B  48 33 C4                        xor rax, rsp
008A5F5E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008A5F63  4C 8B 72 20                     mov r14, qword ptr [rdx + 0x20]
008A5F67  0F 57 C0                        xorps xmm0, xmm0
008A5F6A  44 8A 62 40                     mov r12b, byte ptr [rdx + 0x40]
008A5F6E  48 8B F2                        mov rsi, rdx
008A5F71  48 8B 1A                        mov rbx, qword ptr [rdx]
008A5F74  48 8B F9                        mov rdi, rcx
008A5F77  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
008A5F7C  45 32 ED                        xor r13b, r13b
008A5F7F  45 32 FF                        xor r15b, r15b
008A5F82  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
008A5F87  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
008A5F8C  E8 4F 5F BA FF                  call 0x14044bee0
008A5F91  49 8B 96 50 05 00 00            mov rdx, qword ptr [r14 + 0x550]
008A5F98  48 3B 15 09 0B 72 00            cmp rdx, qword ptr [rip + 0x720b09]
008A5F9F  0F 85 8D 02 00 00               jne 0x1408a6232
008A5FA5  48 8B CF                        mov rcx, rdi
008A5FA8  44 88 6E 41                     mov byte ptr [rsi + 0x41], r13b
008A5FAC  E8 53 03 00 00                  call 0x1408a6304
008A5FB1  85 C0                           test eax, eax
008A5FB3  0F 85 F9 01 00 00               jne 0x1408a61b2
008A5FB9  48 3B 3D B0 0B 72 00            cmp rdi, qword ptr [rip + 0x720bb0]
008A5FC0  40 B5 01                        mov bpl, 1
008A5FC3  0F 85 10 01 00 00               jne 0x1408a60d9
008A5FC9  44 8A FD                        mov r15b, bpl
008A5FCC  40 32 ED                        xor bpl, bpl
008A5FCF  40 88 6E 41                     mov byte ptr [rsi + 0x41], bpl
008A5FD3  44 88 7E 43                     mov byte ptr [rsi + 0x43], r15b
008A5FD7  48 85 DB                        test rbx, rbx
008A5FDA  0F 84 B4 00 00 00               je 0x1408a6094
008A5FE0  45 84 E4                        test r12b, r12b
008A5FE3  0F 85 4B 01 00 00               jne 0x1408a6134
008A5FE9  F7 43 04 00 00 00 08            test dword ptr [rbx + 4], 0x8000000
008A5FF0  0F 85 D9 02 00 00               jne 0x1408a62cf
008A5FF6  8B 03                           mov eax, dword ptr [rbx]
008A5FF8  A8 04                           test al, 4
008A5FFA  0F 85 18 01 00 00               jne 0x1408a6118
008A6000  48 85 DB                        test rbx, rbx
008A6003  0F 84 8B 00 00 00               je 0x1408a6094
008A6009  F7 03 04 C0 00 00               test dword ptr [rbx], 0xc004
008A600F  74 10                           je 0x1408a6021
008A6011  4C 8B C3                        mov r8, rbx
008A6014  48 8B D6                        mov rdx, rsi
008A6017  48 8B CF                        mov rcx, rdi
008A601A  E8 71 15 00 00                  call 0x1408a7590
008A601F  EB 05                           jmp 0x1408a6026
008A6021  48 85 DB                        test rbx, rbx
008A6024  74 6E                           je 0x1408a6094
008A6026  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
008A6029  A8 40                           test al, 0x40
008A602B  0F 85 AE 02 00 00               jne 0x1408a62df
008A6031  48 85 DB                        test rbx, rbx
008A6034  74 5E                           je 0x1408a6094
008A6036  8B 03                           mov eax, dword ptr [rbx]
008A6038  A8 02                           test al, 2
008A603A  74 21                           je 0x1408a605d
008A603C  48 3B 3D 2D 0B 72 00            cmp rdi, qword ptr [rip + 0x720b2d]
008A6043  0F 84 03 02 00 00               je 0x1408a624c
008A6049  4C 8B C6                        mov r8, rsi
008A604C  48 8D 15 7D 3B 02 00            lea rdx, [rip + 0x23b7d]
008A6053  48 8B CF                        mov rcx, rdi
008A6056  E8 D5 3A 02 00                  call 0x1408c9b30
008A605B  EB 05                           jmp 0x1408a6062
008A605D  48 85 DB                        test rbx, rbx
008A6060  74 32                           je 0x1408a6094
008A6062  8B 03                           mov eax, dword ptr [rbx]
008A6064  A8 08                           test al, 8
008A6066  74 0D                           je 0x1408a6075
008A6068  49 8B D6                        mov rdx, r14
008A606B  48 8B CF                        mov rcx, rdi
008A606E  E8 95 FD FF FF                  call 0x1408a5e08
008A6073  EB 05                           jmp 0x1408a607a
008A6075  48 85 DB                        test rbx, rbx
008A6078  74 1A                           je 0x1408a6094
008A607A  8B 03                           mov eax, dword ptr [rbx]
008A607C  A8 01                           test al, 1
008A607E  74 14                           je 0x1408a6094
008A6080  41 B8 04 03 00 00               mov r8d, 0x304
008A6086  4C 8B CE                        mov r9, rsi
008A6089  49 8B D6                        mov rdx, r14
008A608C  48 8B CF                        mov rcx, rdi
008A608F  E8 90 EF FF FF                  call 0x1408a5024
008A6094  45 84 ED                        test r13b, r13b
008A6097  74 18                           je 0x1408a60b1
008A6099  33 D2                           xor edx, edx
008A609B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
008A60A0  E8 8B 1C 97 FF                  call 0x140217d30
008A60A5  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
008A60AC  E8 CF 3D AA FF                  call 0x140349e80
008A60B1  33 C0                           xor eax, eax
008A60B3  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008A60B8  48 33 CC                        xor rcx, rsp
008A60BB  E8 80 65 E0 FF                  call 0x1406ac640
008A60C0  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
008A60C8  48 83 C4 60                     add rsp, 0x60
008A60CC  41 5F                           pop r15
008A60CE  41 5E                           pop r14
008A60D0  41 5D                           pop r13
008A60D2  41 5C                           pop r12
008A60D4  5F                              pop rdi
008A60D5  5E                              pop rsi
008A60D6  5D                              pop rbp
008A60D7  C3                              ret
008A60D8  CC                              int3
008A60D9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008A60E2  48 39 B8 B8 00 00 00            cmp qword ptr [rax + 0xb8], rdi
008A60E9  0F 84 E0 FE FF FF               je 0x1408a5fcf
008A60EF  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
008A60F6  E8 25 05 97 FF                  call 0x140216620
008A60FB  84 C0                           test al, al
008A60FD  0F 84 C9 FE FF FF               je 0x1408a5fcc
008A6103  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
008A6108  48 8B CF                        mov rcx, rdi
008A610B  E8 F0 06 97 FF                  call 0x140216800
008A6110  44 8A ED                        mov r13b, bpl
008A6113  E9 B7 FE FF FF                  jmp 0x1408a5fcf
008A6118  48 3B 3D 91 09 72 00            cmp rdi, qword ptr [rip + 0x720991]
008A611F  0F 85 E4 FE FF FF               jne 0x1408a6009
008A6125  33 D2                           xor edx, edx
008A6127  49 8B CE                        mov rcx, r14
008A612A  E8 91 E2 FF FF                  call 0x1408a43c0
008A612F  E9 D5 FE FF FF                  jmp 0x1408a6009
008A6134  8B 03                           mov eax, dword ptr [rbx]
008A6136  A8 01                           test al, 1
008A6138  74 14                           je 0x1408a614e
008A613A  41 B8 03 03 00 00               mov r8d, 0x303
008A6140  4C 8B CE                        mov r9, rsi
008A6143  49 8B D6                        mov rdx, r14
008A6146  48 8B CF                        mov rcx, rdi
008A6149  E8 D6 EE FF FF                  call 0x1408a5024
008A614E  8B 03                           mov eax, dword ptr [rbx]
008A6150  A8 02                           test al, 2
008A6152  0F 85 8C 00 00 00               jne 0x1408a61e4
008A6158  48 85 DB                        test rbx, rbx
008A615B  0F 84 33 FF FF FF               je 0x1408a6094
008A6161  F7 03 04 C0 00 00               test dword ptr [rbx], 0xc004
008A6167  74 10                           je 0x1408a6179
008A6169  4C 8B C3                        mov r8, rbx
008A616C  48 8B D6                        mov rdx, rsi
008A616F  48 8B CF                        mov rcx, rdi
008A6172  E8 19 14 00 00                  call 0x1408a7590
008A6177  EB 09                           jmp 0x1408a6182
008A6179  48 85 DB                        test rbx, rbx
008A617C  0F 84 12 FF FF FF               je 0x1408a6094
008A6182  8B 03                           mov eax, dword ptr [rbx]
008A6184  A8 04                           test al, 4
008A6186  0F 85 89 00 00 00               jne 0x1408a6215
008A618C  48 85 DB                        test rbx, rbx
008A618F  0F 84 FF FE FF FF               je 0x1408a6094
008A6195  F7 43 04 00 00 00 08            test dword ptr [rbx + 4], 0x8000000
008A619C  0F 84 F2 FE FF FF               je 0x1408a6094
008A61A2  48 8B D6                        mov rdx, rsi
008A61A5  48 8B CF                        mov rcx, rdi
008A61A8  E8 F7 9D F1 FF                  call 0x1407bffa4
008A61AD  E9 E2 FE FF FF                  jmp 0x1408a6094
008A61B2  48 85 DB                        test rbx, rbx
008A61B5  0F 84 F6 FE FF FF               je 0x1408a60b1
008A61BB  8B 03                           mov eax, dword ptr [rbx]
008A61BD  A8 01                           test al, 1
008A61BF  0F 84 EC FE FF FF               je 0x1408a60b1
008A61C5  45 84 E4                        test r12b, r12b
008A61C8  0F 85 E3 FE FF FF               jne 0x1408a60b1
008A61CE  41 B8 27 03 00 00               mov r8d, 0x327
008A61D4  4C 8B CE                        mov r9, rsi
008A61D7  49 8B D6                        mov rdx, r14
008A61DA  E8 45 EE FF FF                  call 0x1408a5024
008A61DF  E9 CD FE FF FF                  jmp 0x1408a60b1
008A61E4  F6 87 70 01 00 00 01            test byte ptr [rdi + 0x170], 1
008A61EB  0F 85 70 FF FF FF               jne 0x1408a6161
008A61F1  48 3B 3D 78 09 72 00            cmp rdi, qword ptr [rip + 0x720978]
008A61F8  0F 84 9D 00 00 00               je 0x1408a629b
008A61FE  4C 8B C6                        mov r8, rsi
008A6201  48 8D 15 C8 39 02 00            lea rdx, [rip + 0x239c8]
008A6208  48 8B CF                        mov rcx, rdi
008A620B  E8 20 39 02 00                  call 0x1408c9b30
008A6210  E9 4C FF FF FF                  jmp 0x1408a6161
008A6215  48 3B 3D 94 08 72 00            cmp rdi, qword ptr [rip + 0x720894]
008A621C  0F 85 73 FF FF FF               jne 0x1408a6195
008A6222  41 8A D4                        mov dl, r12b
008A6225  49 8B CE                        mov rcx, r14
008A6228  E8 93 E1 FF FF                  call 0x1408a43c0
008A622D  E9 63 FF FF FF                  jmp 0x1408a6195
008A6232  48 8B C8                        mov rcx, rax
008A6235  E8 66 EE 97 FF                  call 0x1402250a0
008A623A  48 39 90 40 03 00 00            cmp qword ptr [rax + 0x340], rdx
008A6241  0F 84 5E FD FF FF               je 0x1408a5fa5
008A6247  E9 65 FE FF FF                  jmp 0x1408a60b1
008A624C  8B 2D 2E 08 72 00               mov ebp, dword ptr [rip + 0x72082e]
008A6252  45 33 FF                        xor r15d, r15d
008A6255  85 ED                           test ebp, ebp
008A6257  0F 84 05 FE FF FF               je 0x1408a6062
008A625D  41 8B CF                        mov ecx, r15d
008A6260  E8 6B 23 A3 FF                  call 0x1402d85d0
008A6265  4C 8B C6                        mov r8, rsi
008A6268  48 8B CF                        mov rcx, rdi
008A626B  48 8B 50 18                     mov rdx, qword ptr [rax + 0x18]
008A626F  E8 5C 39 02 00                  call 0x1408c9bd0
008A6274  41 8B CF                        mov ecx, r15d
008A6277  E8 54 23 A3 FF                  call 0x1402d85d0
008A627C  4C 8B C6                        mov r8, rsi
008A627F  48 8B CF                        mov rcx, rdi
008A6282  48 8B 90 38 38 00 00            mov rdx, qword ptr [rax + 0x3838]
008A6289  E8 42 39 02 00                  call 0x1408c9bd0
008A628E  41 FF C7                        inc r15d
008A6291  44 3B FD                        cmp r15d, ebp
008A6294  72 C7                           jb 0x1408a625d
008A6296  E9 C7 FD FF FF                  jmp 0x1408a6062
008A629B  44 8B 3D DE 07 72 00            mov r15d, dword ptr [rip + 0x7207de]
008A62A2  33 ED                           xor ebp, ebp
008A62A4  45 85 FF                        test r15d, r15d
008A62A7  0F 84 B4 FE FF FF               je 0x1408a6161
008A62AD  8B CD                           mov ecx, ebp
008A62AF  E8 1C 23 A3 FF                  call 0x1402d85d0
008A62B4  4C 8B C6                        mov r8, rsi
008A62B7  48 8B CF                        mov rcx, rdi
008A62BA  48 8B 50 18                     mov rdx, qword ptr [rax + 0x18]
008A62BE  E8 0D 39 02 00                  call 0x1408c9bd0
008A62C3  FF C5                           inc ebp
008A62C5  41 3B EF                        cmp ebp, r15d
008A62C8  72 E3                           jb 0x1408a62ad
008A62CA  E9 92 FE FF FF                  jmp 0x1408a6161
008A62CF  48 8B D6                        mov rdx, rsi
008A62D2  48 8B CF                        mov rcx, rdi
008A62D5  E8 CA 9C F1 FF                  call 0x1407bffa4
008A62DA  E9 17 FD FF FF                  jmp 0x1408a5ff6
008A62DF  48 3B 3D 8A 08 72 00            cmp rdi, qword ptr [rip + 0x72088a]
008A62E6  0F 84 4A FD FF FF               je 0x1408a6036
008A62EC  48 8B D6                        mov rdx, rsi
008A62EF  48 8B CF                        mov rcx, rdi
008A62F2  E8 85 A1 F1 FF                  call 0x1407c047c
008A62F7  E9 3A FD FF FF                  jmp 0x1408a6036
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpProcessEnumCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 5654501)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m78 = v_xmm0;
    v_r13 = 0;
    v_r15 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = PsGetProcessServerSilo(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 1360)) != (*(unsigned __int64 *)(v_rip + 7473929))) goto loc_008A6232;
loc_008A5FA5:
    *(unsigned __int8 *)(a2 + 65) = 0;
    result = EtwpIsProcessZombie(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 1360), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_008A61B2;
    if (a1 != (*(unsigned __int64 *)(v_rip + 7474096))) goto loc_008A60D9;
loc_008A5FCC:
    v_rbp = 0;
loc_008A5FCF:
    *(unsigned __int8 *)(a2 + 65) = 0;
    *(unsigned __int8 *)(a2 + 67) = 1;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_008A6094;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + 64)) != 0) goto loc_008A6134;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2) + 4)) & (0x8000000ULL)) != 0) goto loc_008A62CF;
loc_008A5FF6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2))))) & (4)) != 0) goto loc_008A6118;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_008A6094;
loc_008A6009:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2))) & (0xC004ULL)) == 0) goto loc_008A6021;
    result = EtwpEnumerateAddressSpace(a1, a2, *(unsigned __int64 *)(a2), a4);
    goto loc_008A6026;
loc_008A6021:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_008A6094;
loc_008A6026:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 16)))) & (64)) != 0) goto loc_008A62DF;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_008A6094;
loc_008A6036:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2))))) & (2)) == 0) goto loc_008A605D;
    if (a1 == (*(unsigned __int64 *)(v_rip + 7473965))) goto loc_008A624C;
    result = PsEnumProcessThreads(a1, v_rip + 146301, a2, a4);
    goto loc_008A6062;
loc_008A605D:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_008A6094;
loc_008A6062:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2))))) & (8)) == 0) goto loc_008A6075;
    result = EtwpProcessPerfCtrsRundown(a1, *(unsigned __int64 *)(a2 + 32), a2, a4);
    goto loc_008A607A;
loc_008A6075:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_008A6094;
loc_008A607A:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2))))) & (1)) != 0) {
        a3 = 772;
        a4 = a2;
        a2 = *(unsigned __int64 *)(a2 + 32);
        a1 = a1;
        result = EtwpTraceProcessRundown(a1, a2, a3, a4);
    }
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = KiUnstackDetachProcess(a1, a2, a3, a4);
        a1 = a1 + 488;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = 0;
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
loc_008A60D9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == a1) goto loc_008A5FCF;
    result = ExAcquireRundownProtection(a1 + 488, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008A5FCC;
    result = KeStackAttachProcess(a1, v_stack_p20, a3, a4);
    goto loc_008A5FCF;
loc_008A6118:
    if (a1 != (*(unsigned __int64 *)(v_rip + 7473553))) goto loc_008A6009;
    a2 = 0;
    result = EtwpSysModuleRunDown(*(unsigned __int64 *)(a2 + 32), a2, a3, a4);
    goto loc_008A6009;
loc_008A6134:
    result = (unsigned int)(*(unsigned int *)(v_stack_p18));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (1)) != 0) {
        a3 = 771;
        a4 = 0;
        a2 = *(unsigned __int64 *)(a2 + 32);
        a1 = a1;
        result = EtwpTraceProcessRundown(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (2)) != 0) goto loc_008A61E4;
    if (v_stack_p18 == 0) goto loc_008A6094;
loc_008A6161:
    if (((*(unsigned int *)(v_stack_p18)) & (0xC004ULL)) == 0) goto loc_008A6179;
    result = EtwpEnumerateAddressSpace(a1, a2, v_stack_p18, a4);
    goto loc_008A6182;
loc_008A6179:
    if (v_stack_p18 == 0) goto loc_008A6094;
loc_008A6182:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (4)) != 0) goto loc_008A6215;
    if (v_stack_p18 == 0) goto loc_008A6094;
loc_008A6195:
    if (((*(unsigned int *)(v_stack_p18 + 4)) & (0x8000000ULL)) == 0) goto loc_008A6094;
    result = EtwpEnumerateWorkingSet(a1, a2, v_stack_p18, a4);
    goto loc_008A6094;
loc_008A61B2:
    if (v_stack_p18 == 0) goto loc_008A60B1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (1)) == 0) goto loc_008A60B1;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + 64)) != 0) goto loc_008A60B1;
    result = EtwpTraceProcessRundown(a1, *(unsigned __int64 *)(a2 + 32), 807, a2);
    goto loc_008A60B1;
loc_008A61E4:
    if (((*(unsigned __int8 *)(a1 + 368)) & (1)) != 0) goto loc_008A6161;
    if (a1 == (*(unsigned __int64 *)(v_rip + 7473528))) goto loc_008A629B;
    result = PsEnumProcessThreads(a1, v_rip + 145864, a2, a2);
    goto loc_008A6161;
loc_008A6215:
    if (a1 != (*(unsigned __int64 *)(v_rip + 7473300))) goto loc_008A6195;
    result = EtwpSysModuleRunDown(*(unsigned __int64 *)(a2 + 32), (unsigned __int8)(*(unsigned __int8 *)(a2 + 64)), a2, a2);
    goto loc_008A6195;
loc_008A6232:
    result = PsGetServerSiloGlobals(result, (unsigned __int8)(*(unsigned __int8 *)(a2 + 64)), a2, a2);
    if ((*(unsigned __int64 *)(result + 832)) == ((unsigned __int8)(*(unsigned __int8 *)(a2 + 64)))) goto loc_008A5FA5;
    goto loc_008A60B1;
loc_008A624C:
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7473198))) == 0) goto loc_008A6062;
loc_008A625D:
    result = KeGetPrcb(0, (unsigned __int8)(*(unsigned __int8 *)(a2 + 64)), a2, a2);
    result = EtwpThreadEnumCallback(a1, *(unsigned __int64 *)(result + 24), a2, a2);
    result = KeGetPrcb(0, *(unsigned __int64 *)(result + 24), a2, a2);
    result = EtwpThreadEnumCallback(a1, *(unsigned __int64 *)(result + 14392), a2, a2);
    v_r15 = (unsigned int)((v_r15) + 1);
    if (((unsigned int)(v_r15)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7473198))))) goto loc_008A625D;
    goto loc_008A6062;
loc_008A629B:
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7473118))) == 0) goto loc_008A6161;
loc_008A62AD:
    result = KeGetPrcb(0, *(unsigned __int64 *)(result + 14392), a2, a2);
    result = EtwpThreadEnumCallback(a1, *(unsigned __int64 *)(result + 24), a2, a2);
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((unsigned int)(v_rbp)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7473118))))) goto loc_008A62AD;
    goto loc_008A6161;
loc_008A62CF:
    result = EtwpEnumerateWorkingSet(a1, a2, a2, a2);
    goto loc_008A5FF6;
loc_008A62DF:
    if (a1 == (*(unsigned __int64 *)(v_rip + 7473290))) goto loc_008A6036;
    result = EtwpObjectHandleRundown(a1, a2, a2, a2);
    goto loc_008A6036;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpProcessEnumCallback(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x5647E5)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m78 = v_xmm0;
    local_r13 = 0;
    local_r15 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = PsGetProcessServerSilo(Arg1, Arg2, a3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x550)) != (*(uint64_t *)(v_rip + 0x720B09))) goto loc_008A6232;
loc_008A5FA5:
    *(uint8_t *)(arg2 + 0x41) = 0;
    result = EtwpIsProcessZombie(Arg1, *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x550), a3, a4);
    if ((uint32_t)(result) != 0) goto loc_008A61B2;
    if (Arg1 != (*(uint64_t *)(v_rip + 0x720BB0))) goto loc_008A60D9;
loc_008A5FCC:
    local_rbp = 0;
loc_008A5FCF:
    *(uint8_t *)(arg2 + 0x41) = 0;
    *(uint8_t *)(arg2 + 0x43) = 1;
    if (*(uint64_t *)(arg2) == 0) goto loc_008A6094;
    if ((uint8_t)(*(uint8_t *)(arg2 + 0x40)) != 0) goto loc_008A6134;
    if (((*(uint32_t *)(*(uint64_t *)(arg2) + 0x4)) & (0x8000000ULL)) != 0) goto loc_008A62CF;
loc_008A5FF6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2))))) & (4)) != 0) goto loc_008A6118;
    if (*(uint64_t *)(arg2) == 0) goto loc_008A6094;
loc_008A6009:
    if (((*(uint32_t *)(*(uint64_t *)(arg2))) & (0xC004ULL)) == 0) goto loc_008A6021;
    result = EtwpEnumerateAddressSpace(Arg1, Arg2, *(uint64_t *)(arg2), a4);
    goto loc_008A6026;
loc_008A6021:
    if (*(uint64_t *)(arg2) == 0) goto loc_008A6094;
loc_008A6026:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x10)))) & (64)) != 0) goto loc_008A62DF;
    if (*(uint64_t *)(arg2) == 0) goto loc_008A6094;
loc_008A6036:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2))))) & (2)) == 0) goto loc_008A605D;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x720B2D))) goto loc_008A624C;
    result = PsEnumProcessThreads(Arg1, v_rip + 146301, Arg2, a4);
    goto loc_008A6062;
loc_008A605D:
    if (*(uint64_t *)(arg2) == 0) goto loc_008A6094;
loc_008A6062:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2))))) & (8)) == 0) goto loc_008A6075;
    result = EtwpProcessPerfCtrsRundown(Arg1, *(uint64_t *)(arg2 + 0x20), Arg2, a4);
    goto loc_008A607A;
loc_008A6075:
    if (*(uint64_t *)(arg2) == 0) goto loc_008A6094;
loc_008A607A:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2))))) & (1)) != 0) {
        a3 = 772;
        a4 = Arg2;
        Arg2 = *(uint64_t *)(arg2 + 0x20);
        Arg1 = Arg1;
        result = EtwpTraceProcessRundown(Arg1, Arg2, a3, a4);
    }
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = KiUnstackDetachProcess(Arg1, Arg2, a3, a4);
        Arg1 = Arg1 + 488;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = 0;
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (96);
    return result;
loc_008A60D9:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == Arg1) goto loc_008A5FCF;
    result = ExAcquireRundownProtection(Arg1 + 488, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_008A5FCC;
    result = KeStackAttachProcess(Arg1, v_stack_p20, a3, a4);
    goto loc_008A5FCF;
loc_008A6118:
    if (Arg1 != (*(uint64_t *)(v_rip + 0x720991))) goto loc_008A6009;
    Arg2 = 0;
    result = EtwpSysModuleRunDown(*(uint64_t *)(arg2 + 0x20), Arg2, a3, a4);
    goto loc_008A6009;
loc_008A6134:
    result = (uint32_t)(*(uint32_t *)(v_stack_p18));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (1)) != 0) {
        a3 = 771;
        a4 = 0;
        Arg2 = *(uint64_t *)(arg2 + 0x20);
        Arg1 = Arg1;
        result = EtwpTraceProcessRundown(Arg1, Arg2, a3, a4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (2)) != 0) goto loc_008A61E4;
    if (v_stack_p18 == 0) goto loc_008A6094;
loc_008A6161:
    if (((*(uint32_t *)(v_stack_p18)) & (0xC004ULL)) == 0) goto loc_008A6179;
    result = EtwpEnumerateAddressSpace(Arg1, Arg2, v_stack_p18, a4);
    goto loc_008A6182;
loc_008A6179:
    if (v_stack_p18 == 0) goto loc_008A6094;
loc_008A6182:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (4)) != 0) goto loc_008A6215;
    if (v_stack_p18 == 0) goto loc_008A6094;
loc_008A6195:
    if (((*(uint32_t *)(v_stack_p18 + 0x4)) & (0x8000000ULL)) == 0) goto loc_008A6094;
    result = EtwpEnumerateWorkingSet(Arg1, Arg2, v_stack_p18, a4);
    goto loc_008A6094;
loc_008A61B2:
    if (v_stack_p18 == 0) goto loc_008A60B1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (1)) == 0) goto loc_008A60B1;
    if ((uint8_t)(*(uint8_t *)(arg2 + 0x40)) != 0) goto loc_008A60B1;
    result = EtwpTraceProcessRundown(Arg1, *(uint64_t *)(arg2 + 0x20), 807, Arg2);
    goto loc_008A60B1;
loc_008A61E4:
    if (((*(uint8_t *)(Arg1 + 0x170)) & (1)) != 0) goto loc_008A6161;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x720978))) goto loc_008A629B;
    result = PsEnumProcessThreads(Arg1, v_rip + 145864, Arg2, Arg2);
    goto loc_008A6161;
loc_008A6215:
    if (Arg1 != (*(uint64_t *)(v_rip + 0x720894))) goto loc_008A6195;
    result = EtwpSysModuleRunDown(*(uint64_t *)(arg2 + 0x20), (uint8_t)(*(uint8_t *)(arg2 + 0x40)), Arg2, Arg2);
    goto loc_008A6195;
loc_008A6232:
    result = PsGetServerSiloGlobals(result, (uint8_t)(*(uint8_t *)(arg2 + 0x40)), Arg2, Arg2);
    if ((*(uint64_t *)(result + 0x340)) == ((uint8_t)(*(uint8_t *)(arg2 + 0x40)))) goto loc_008A5FA5;
    goto loc_008A60B1;
loc_008A624C:
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x72082E))) == 0) goto loc_008A6062;
loc_008A625D:
    result = KeGetPrcb(0, (uint8_t)(*(uint8_t *)(arg2 + 0x40)), Arg2, Arg2);
    result = EtwpThreadEnumCallback(Arg1, *(uint64_t *)(result + 0x18), Arg2, Arg2);
    result = KeGetPrcb(0, *(uint64_t *)(result + 0x18), Arg2, Arg2);
    result = EtwpThreadEnumCallback(Arg1, *(uint64_t *)(result + 0x3838), Arg2, Arg2);
    local_r15 = (uint32_t)((local_r15) + 1);
    if (((uint32_t)(local_r15)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x72082E))))) goto loc_008A625D;
    goto loc_008A6062;
loc_008A629B:
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7207DE))) == 0) goto loc_008A6161;
loc_008A62AD:
    result = KeGetPrcb(0, *(uint64_t *)(result + 0x3838), Arg2, Arg2);
    result = EtwpThreadEnumCallback(Arg1, *(uint64_t *)(result + 0x18), Arg2, Arg2);
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((uint32_t)(local_rbp)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7207DE))))) goto loc_008A62AD;
    goto loc_008A6161;
loc_008A62CF:
    result = EtwpEnumerateWorkingSet(Arg1, Arg2, Arg2, Arg2);
    goto loc_008A5FF6;
loc_008A62DF:
    if (Arg1 == (*(uint64_t *)(v_rip + 0x72088A))) goto loc_008A6036;
    result = EtwpObjectHandleRundown(Arg1, Arg2, Arg2, Arg2);
    goto loc_008A6036;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x40` | `8` | `R` |
| `Arg2` | `+ 0x41` | `8` | `W` |
| `Arg2` | `+ 0x43` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A5F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
