# EtwpApplyEventNameFilter

- RVA: `0x003F10B8`–`0x003F140C` (길이 `852` bytes)
- VA: `0x00000001403F10B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00096CF8`
- 디코드: `229`개 명령, `852/852` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003F11D6` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x003F11F2` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003F1204` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003F1295` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003F12B5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003F12D8` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003F1324` → [EtwpIsEventNameFilterEnabled](EtwpIsEventNameFilterEnabled_function_003F1414.md) (function, `0x003F1414`)
- `0x003F1340` → [EtwpGetEventNameFromEventMetadata](EtwpGetEventNameFromEventMetadata_function_003F1590.md) (function, `0x003F1590`)
- `0x003F1361` → [EtwpEventNameFilterSearch](EtwpEventNameFilterSearch_function_003F1620.md) (function, `0x003F1620`)
- `0x003F13A3` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x003F13C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003F13F1` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [EtwpEventWriteFull](../22/EtwpEventWriteFull_function_00225C10.md) at `0x00226131`
- [EtwpEventWriteFull](../22/EtwpEventWriteFull_function_00225C10.md) at `0x00226571`
- [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF33A7`
- [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF3620`

### Static image references
- `0x003F10D4` → RVA `0x00E0A740` (`.data`; read)
- `0x003F126B` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x003F1204` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x003F13A3` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x003F13C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003F13E4` → [sub_006EAED0](../6E/Unknown_function_006EAED0.md) (`tail-transfer`)
  - `0x003F13F7` → [sub_006EAED0](../6E/Unknown_function_006EAED0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003F10B8  40 55                           push rbp
003F10BA  56                              push rsi
003F10BB  57                              push rdi
003F10BC  41 54                           push r12
003F10BE  41 55                           push r13
003F10C0  41 56                           push r14
003F10C2  41 57                           push r15
003F10C4  48 83 EC 70                     sub rsp, 0x70
003F10C8  48 8D 6C 24 30                  lea rbp, [rsp + 0x30]
003F10CD  48 89 9D 90 00 00 00            mov qword ptr [rbp + 0x90], rbx
003F10D4  48 8B 05 65 96 A1 00            mov rax, qword ptr [rip + 0xa19665]
003F10DB  48 33 C5                        xor rax, rbp
003F10DE  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
003F10E2  44 8B E2                        mov r12d, edx
003F10E5  4C 8B E9                        mov r13, rcx
003F10E8  33 DB                           xor ebx, ebx
003F10EA  66 89 5D 04                     mov word ptr [rbp + 4], bx
003F10EE  48 89 5D 08                     mov qword ptr [rbp + 8], rbx
003F10F2  0F 57 C0                        xorps xmm0, xmm0
003F10F5  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
003F10F9  8B F3                           mov esi, ebx
003F10FB  48 89 5D 10                     mov qword ptr [rbp + 0x10], rbx
003F10FF  44 8A FB                        mov r15b, bl
003F1102  88 5D 01                        mov byte ptr [rbp + 1], bl
003F1105  C6 45 00 01                     mov byte ptr [rbp], 1
003F1109  38 9D A0 00 00 00               cmp byte ptr [rbp + 0xa0], bl
003F110F  0F 85 5C 02 00 00               jne 0x1403f1371
003F1115  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
003F111F  8B CB                           mov ecx, ebx
003F1121  89 5D 18                        mov dword ptr [rbp + 0x18], ebx
003F1124  41 3B C8                        cmp ecx, r8d
003F1127  72 11                           jb 0x1403f113a
003F1129  BF 02 00 00 00                  mov edi, 2
003F112E  44 8A B5 A8 00 00 00            mov r14b, byte ptr [rbp + 0xa8]
003F1135  E9 07 01 00 00                  jmp 0x1403f1241
003F113A  8B C1                           mov eax, ecx
003F113C  48 03 C0                        add rax, rax
003F113F  41 80 7C C1 0C 01               cmp byte ptr [r9 + rax*8 + 0xc], 1
003F1145  74 07                           je 0x1403f114e
003F1147  FF C1                           inc ecx
003F1149  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
003F114C  EB D6                           jmp 0x1403f1124
003F114E  8B F1                           mov esi, ecx
003F1150  48 C1 E6 04                     shl rsi, 4
003F1154  49 03 F1                        add rsi, r9
003F1157  44 8A B5 A8 00 00 00            mov r14b, byte ptr [rbp + 0xa8]
003F115E  BF 02 00 00 00                  mov edi, 2
003F1163  44 3A F7                        cmp r14b, dil
003F1166  0F 83 AF 00 00 00               jae 0x1403f121b
003F116C  0F 10 06                        movups xmm0, xmmword ptr [rsi]
003F116F  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
003F1173  48 8D 75 20                     lea rsi, [rbp + 0x20]
003F1177  48 89 75 10                     mov qword ptr [rbp + 0x10], rsi
003F117B  4C 8B D6                        mov r10, rsi
003F117E  66 0F 73 D8 08                  psrldq xmm0, 8
003F1183  66 0F 7E C1                     movd ecx, xmm0
003F1187  81 F9 FF FF 00 00               cmp ecx, 0xffff
003F118D  0F 83 95 00 00 00               jae 0x1403f1228
003F1193  38 9D A0 00 00 00               cmp byte ptr [rbp + 0xa0], bl
003F1199  74 18                           je 0x1403f11b3
003F119B  85 C9                           test ecx, ecx
003F119D  74 14                           je 0x1403f11b3
003F119F  44 8B C9                        mov r9d, ecx
003F11A2  4C 8B 45 20                     mov r8, qword ptr [rbp + 0x20]
003F11A6  4D 03 C8                        add r9, r8
003F11A9  4C 3B CA                        cmp r9, rdx
003F11AC  77 7F                           ja 0x1403f122d
003F11AE  4D 3B C8                        cmp r9, r8
003F11B1  72 7A                           jb 0x1403f122d
003F11B3  41 8B 52 08                     mov edx, dword ptr [r10 + 8]
003F11B7  81 F9 00 01 00 00               cmp ecx, 0x100
003F11BD  77 3A                           ja 0x1403f11f9
003F11BF  48 8D 42 0F                     lea rax, [rdx + 0xf]
003F11C3  48 3B C2                        cmp rax, rdx
003F11C6  77 0A                           ja 0x1403f11d2
003F11C8  48 B8 F0 FF FF FF FF FF FF 0F   movabs rax, 0xffffffffffffff0
003F11D2  48 83 E0 F0                     and rax, 0xfffffffffffffff0
003F11D6  E8 85 97 2C 00                  call 0x1406ba960
003F11DB  48 2B E0                        sub rsp, rax
003F11DE  48 8D 44 24 30                  lea rax, [rsp + 0x30]
003F11E3  48 89 45 08                     mov qword ptr [rbp + 8], rax
003F11E7  44 8B C1                        mov r8d, ecx
003F11EA  48 8B 55 20                     mov rdx, qword ptr [rbp + 0x20]
003F11EE  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
003F11F2  E8 49 56 2D 00                  call 0x1406c6840
003F11F7  EB 48                           jmp 0x1403f1241
003F11F9  B9 42 00 00 00                  mov ecx, 0x42
003F11FE  41 B8 45 74 77 74               mov r8d, 0x74777445
003F1204  E8 E7 0E 79 00                  call 0x140b820f0
003F1209  48 89 45 08                     mov qword ptr [rbp + 8], rax
003F120D  48 85 C0                        test rax, rax
003F1210  74 29                           je 0x1403f123b
003F1212  C6 45 01 01                     mov byte ptr [rbp + 1], 1
003F1216  8B 4D 28                        mov ecx, dword ptr [rbp + 0x28]
003F1219  EB CC                           jmp 0x1403f11e7
003F121B  48 89 75 10                     mov qword ptr [rbp + 0x10], rsi
003F121F  48 8B 06                        mov rax, qword ptr [rsi]
003F1222  48 89 45 08                     mov qword ptr [rbp + 8], rax
003F1226  EB 19                           jmp 0x1403f1241
003F1228  88 5D 00                        mov byte ptr [rbp], bl
003F122B  EB 75                           jmp 0x1403f12a2
003F122D  8A 02                           mov al, byte ptr [rdx]
003F122F  8B 4D 28                        mov ecx, dword ptr [rbp + 0x28]
003F1232  48 8B 75 10                     mov rsi, qword ptr [rbp + 0x10]
003F1236  E9 78 FF FF FF                  jmp 0x1403f11b3
003F123B  C6 45 00 01                     mov byte ptr [rbp], 1
003F123F  EB 61                           jmp 0x1403f12a2
003F1241  EB 08                           jmp 0x1403f124b
003F1243  C6 45 00 01                     mov byte ptr [rbp], 1
003F1247  33 DB                           xor ebx, ebx
003F1249  EB 57                           jmp 0x1403f12a2
003F124B  48 85 F6                        test rsi, rsi
003F124E  0F 84 AF 01 00 00               je 0x1403f1403
003F1254  48 39 5D 08                     cmp qword ptr [rbp + 8], rbx
003F1258  0F 84 A5 01 00 00               je 0x1403f1403
003F125E  44 3A F7                        cmp r14b, dil
003F1261  73 11                           jae 0x1403f1274
003F1263  45 0F 20 C7                     mov r15, cr8
003F1267  44 0F 22 C7                     mov cr8, rdi
003F126B  83 3D AE 5A BD 00 00            cmp dword ptr [rip + 0xbd5aae], 0
003F1272  75 5E                           jne 0x1403f12d2
003F1274  49 8B 8D 80 02 00 00            mov rcx, qword ptr [r13 + 0x280]
003F127B  48 85 C9                        test rcx, rcx
003F127E  75 5F                           jne 0x1403f12df
003F1280  44 3A F7                        cmp r14b, dil
003F1283  73 1D                           jae 0x1403f12a2
003F1285  83 3D 94 5A BD 00 00            cmp dword ptr [rip + 0xbd5a94], 0
003F128C  74 0C                           je 0x1403f129a
003F128E  44 0F 20 C1                     mov rcx, cr8
003F1292  41 8A D7                        mov dl, r15b
003F1295  E8 FE 43 10 00                  call 0x1404f5698
003F129A  41 0F B6 C7                     movzx eax, r15b
003F129E  44 0F 22 C0                     mov cr8, rax
003F12A2  38 5D 01                        cmp byte ptr [rbp + 1], bl
003F12A5  0F 85 13 01 00 00               jne 0x1403f13be
003F12AB  8A 45 00                        mov al, byte ptr [rbp]
003F12AE  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
003F12B2  48 33 CD                        xor rcx, rbp
003F12B5  E8 86 B3 2B 00                  call 0x1406ac640
003F12BA  48 8B 9D 90 00 00 00            mov rbx, qword ptr [rbp + 0x90]
003F12C1  48 8D 65 40                     lea rsp, [rbp + 0x40]
003F12C5  41 5F                           pop r15
003F12C7  41 5E                           pop r14
003F12C9  41 5D                           pop r13
003F12CB  41 5C                           pop r12
003F12CD  5F                              pop rdi
003F12CE  5E                              pop rsi
003F12CF  5D                              pop rbp
003F12D0  C3                              ret
003F12D1  CC                              int3
003F12D2  40 8A D7                        mov dl, dil
003F12D5  41 8A CF                        mov cl, r15b
003F12D8  E8 1F 44 10 00                  call 0x1404f56fc
003F12DD  EB 95                           jmp 0x1403f1274
003F12DF  49 6B F4 68                     imul rsi, r12, 0x68
003F12E3  8A 85 C0 00 00 00               mov al, byte ptr [rbp + 0xc0]
003F12E9  84 C0                           test al, al
003F12EB  0F 85 DD 00 00 00               jne 0x1403f13ce
003F12F1  48 8B 74 0E 60                  mov rsi, qword ptr [rsi + rcx + 0x60]
003F12F6  48 85 F6                        test rsi, rsi
003F12F9  74 85                           je 0x1403f1280
003F12FB  44 3A F7                        cmp r14b, dil
003F12FE  45 0F B6 C6                     movzx r8d, r14b
003F1302  77 03                           ja 0x1403f1307
003F1304  44 8B C7                        mov r8d, edi
003F1307  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003F130B  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
003F1312  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003F1317  44 8A 8D B0 00 00 00            mov r9b, byte ptr [rbp + 0xb0]
003F131E  41 8B D4                        mov edx, r12d
003F1321  49 8B CD                        mov rcx, r13
003F1324  E8 EB 00 00 00                  call 0x1403f1414
003F1329  84 C0                           test al, al
003F132B  0F 84 4F FF FF FF               je 0x1403f1280
003F1331  4C 8D 45 04                     lea r8, [rbp + 4]
003F1335  48 8B 55 10                     mov rdx, qword ptr [rbp + 0x10]
003F1339  8B 52 08                        mov edx, dword ptr [rdx + 8]
003F133C  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
003F1340  E8 4B 02 00 00                  call 0x1403f1590
003F1345  48 85 C0                        test rax, rax
003F1348  0F 84 8A 00 00 00               je 0x1403f13d8
003F134E  0F B7 55 04                     movzx edx, word ptr [rbp + 4]
003F1352  66 85 D2                        test dx, dx
003F1355  0F 84 A1 00 00 00               je 0x1403f13fc
003F135B  4C 8B C6                        mov r8, rsi
003F135E  48 8B C8                        mov rcx, rax
003F1361  E8 BA 02 00 00                  call 0x1403f1620
003F1366  38 06                           cmp byte ptr [rsi], al
003F1368  0F 94 45 00                     sete byte ptr [rbp]
003F136C  E9 0F FF FF FF                  jmp 0x1403f1280
003F1371  41 8B C0                        mov eax, r8d
003F1374  48 C1 E0 04                     shl rax, 4
003F1378  48 85 C0                        test rax, rax
003F137B  74 2B                           je 0x1403f13a8
003F137D  41 F6 C1 03                     test r9b, 3
003F1381  75 20                           jne 0x1403f13a3
003F1383  4A 8D 0C 08                     lea rcx, [rax + r9]
003F1387  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
003F1391  48 3B CA                        cmp rcx, rdx
003F1394  77 05                           ja 0x1403f139b
003F1396  49 3B C9                        cmp rcx, r9
003F1399  73 17                           jae 0x1403f13b2
003F139B  8A 02                           mov al, byte ptr [rdx]
003F139D  48 8B 75 10                     mov rsi, qword ptr [rbp + 0x10]
003F13A1  EB 0F                           jmp 0x1403f13b2
003F13A3  E8 28 8C 4A 00                  call 0x140899fd0
003F13A8  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
003F13B2  E9 68 FD FF FF                  jmp 0x1403f111f
003F13B7  32 C0                           xor al, al
003F13B9  E9 F0 FE FF FF                  jmp 0x1403f12ae
003F13BE  33 D2                           xor edx, edx
003F13C0  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
003F13C4  E8 A7 14 79 00                  call 0x140b82870
003F13C9  E9 DD FE FF FF                  jmp 0x1403f12ab
003F13CE  48 8B 74 0E 38                  mov rsi, qword ptr [rsi + rcx + 0x38]
003F13D3  E9 1E FF FF FF                  jmp 0x1403f12f6
003F13D8  44 3A F7                        cmp r14b, dil
003F13DB  73 26                           jae 0x1403f1403
003F13DD  83 3D 3C 59 BD 00 00            cmp dword ptr [rip + 0xbd593c], 0
003F13E4  0F 84 E6 9A 2F 00               je 0x1406eaed0
003F13EA  44 0F 20 C1                     mov rcx, cr8
003F13EE  41 8A D7                        mov dl, r15b
003F13F1  E8 A2 42 10 00                  call 0x1404f5698
003F13F6  90                              nop
003F13F7  E9 D4 9A 2F 00                  jmp 0x1406eaed0
003F13FC  38 1E                           cmp byte ptr [rsi], bl
003F13FE  E9 65 FF FF FF                  jmp 0x1403f1368
003F1403  C6 45 00 01                     mov byte ptr [rbp], 1
003F1407  E9 96 FE FF FF                  jmp 0x1403f12a2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpApplyEventNameFilter(__int64 a1, int a2, int a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6, unsigned __int8 a7, __int64 a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int16 v_stack_m74;
    unsigned __int8 v_stack_m77;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;

    v_rsp = (v_rsp) - (112);
    v_stack_p18 = v_rbx;
    result = (*(unsigned __int64 *)(v_rip + 10589797)) ^ (v_stack_m78);
    v_stack_m48 = result;
    v_rbx = 0;
    v_stack_m74 = 0;
    v_stack_m70 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m77 = 0;
    v_stack_m78 = 1;
    if (a5 != 0) goto loc_003F1371;
loc_003F111F:
    v_stack_m60 = 0;
loc_003F1124:
    if (0 < a3) goto loc_003F113A;
    goto loc_003F1241;
loc_003F113A:
    result = (0) + (0);
    if ((*(unsigned __int8 *)(a4 + result * 8 + 12)) == 1) goto loc_003F114E;
    a1 = (unsigned int)((0) + 1);
    v_stack_m60 = (unsigned int)(a1);
    goto loc_003F1124;
loc_003F114E:
    v_rsi = ((unsigned int)((unsigned int)(a1))) << (4);
    v_rsi = (v_rsi) + (a4);
    if (a6 >= 2) goto loc_003F121B;
    v_stack_m58 = v_xmm0;
    v_stack_m68 = v_stack_m58;
    if (((unsigned int)(a1)) >= 0xFFFFULL) goto loc_003F1228;
    if (a5 == 0) goto loc_003F11B3;
    if ((unsigned int)(a1) == 0) goto loc_003F11B3;
    a4 = ((unsigned int)((unsigned int)(a1))) + (v_stack_m58);
    if (a4 > a2) goto loc_003F122D;
    if (a4 < v_stack_m58) goto loc_003F122D;
loc_003F11B3:
    if (((unsigned int)(a1)) > 256) goto loc_003F11F9;
    if (((unsigned int)(*(unsigned int *)(v_stack_m58 + 8)) + 15) <= ((unsigned int)(*(unsigned int *)(v_stack_m58 + 8)))) {
    }
    result = ((unsigned int)(*(unsigned int *)(v_stack_m58 + 8)) + 15) & (-16);
    result = _chkstk(a1, (unsigned int)(*(unsigned int *)(v_stack_m58 + 8)), v_stack_m58, a4);
    v_rsp = (v_rsp) - (result);
    v_stack_m70 = v_stack_m78;
loc_003F11E7:
    result = memcpy(v_stack_m70, v_stack_m58, (unsigned int)((unsigned int)(a1)), a4);
    goto loc_003F1241;
loc_003F11F9:
    result = ExAllocatePool2(66, v_stack_m58, (unsigned int)(0x74777445ULL), a4);
    v_stack_m70 = result;
    if (result == 0) goto loc_003F123B;
    v_stack_m77 = 1;
    goto loc_003F11E7;
loc_003F121B:
    v_stack_m68 = v_stack_m58;
    v_stack_m70 = *(unsigned __int64 *)(v_stack_m58);
    goto loc_003F1241;
loc_003F1228:
    v_stack_m78 = 0;
    goto loc_003F12A2;
loc_003F122D:
    goto loc_003F11B3;
loc_003F123B:
    v_stack_m78 = 1;
    goto loc_003F12A2;
loc_003F1241:
    goto loc_003F124B;
loc_003F124B:
    if (v_stack_m68 == 0) goto loc_003F1403;
    if (v_stack_m70 == 0) goto loc_003F1403;
    if (a6 >= 2) goto loc_003F1274;
    if ((*(unsigned int *)(v_rip + 12409518)) != 0) goto loc_003F12D2;
loc_003F1274:
    if (*(unsigned __int64 *)(a1 + 640) != 0) goto loc_003F12DF;
loc_003F1280:
    if (a6 >= 2) goto loc_003F12A2;
    result = *(unsigned __int8 *)(v_stack_m58);
    if ((*(unsigned int *)(v_rip + 12409492)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(0x74777445ULL), a4);
    }
loc_003F12A2:
    if (v_stack_m77 != 0) goto loc_003F13BE;
loc_003F12AB:
loc_003F12AE:
    a1 = (v_stack_m48) ^ (v_stack_m78);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x74777445ULL), a4);
    return result;
loc_003F12D2:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 2, (unsigned int)(0x74777445ULL), a4);
    goto loc_003F1274;
loc_003F12DF:
    v_rsi = (v_stack_m68) * ((unsigned int)(a2));
    if (a9 != 0) goto loc_003F13CE;
loc_003F12F6:
    if (*(unsigned __int64 *)(v_rsi + (unsigned __int8)(v_cr8) * 1 + 96) == 0) goto loc_003F1280;
    if (a6 <= 2) {
        a3 = 2;
    }
    v_stack_p28 = a9;
    v_stack_p20 = a8;
    result = EtwpIsEventNameFilterEnabled(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a7);
    if ((unsigned __int8)(result) == 0) goto loc_003F1280;
    result = EtwpGetEventNameFromEventMetadata(v_stack_m70, (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)), v_stack_m74, a7);
    if (result == 0) goto loc_003F13D8;
    if ((unsigned __int16)(v_stack_m74) == 0) goto loc_003F13FC;
    result = EtwpEventNameFilterSearch(result, v_stack_m74, *(unsigned __int64 *)(v_rsi + (unsigned __int8)(v_cr8) * 1 + 96), a7);
loc_003F1368:
    goto loc_003F1280;
loc_003F1371:
    result = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsi + (unsigned __int8)(v_cr8) * 1 + 96)))) << (4);
    if (result == 0) goto loc_003F13A8;
    if (((a7) & (3)) != 0) goto loc_003F13A3;
    if ((result + a7 * 1) > v_stack_m74) goto loc_003F139B;
    if ((result + a7 * 1) >= a7) goto loc_003F13B2;
loc_003F139B:
    goto loc_003F13B2;
loc_003F13A3:
    result = ExRaiseDatatypeMisalignment(result + a7 * 1, v_stack_m74, *(unsigned __int64 *)(v_rsi + (unsigned __int8)(v_cr8) * 1 + 96), a7);
loc_003F13A8:
loc_003F13B2:
    goto loc_003F111F;
loc_003F13BE:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, a2, *(unsigned __int64 *)(v_rsi + (unsigned __int8)(v_cr8) * 1 + 96), a7);
    goto loc_003F12AB;
loc_003F13CE:
    goto loc_003F12F6;
loc_003F13D8:
    if (a6 >= 2) goto loc_003F1403;
    result = KiLowerIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), (unsigned __int8)(v_cr8), *(unsigned __int64 *)(v_rsi + (unsigned __int8)(v_cr8) * 1 + 96), a7);
loc_003F13FC:
    goto loc_003F1368;
loc_003F1403:
    v_stack_m78 = 1;
    goto loc_003F12A2;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpApplyEventNameFilter(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint8_t Arg5, uint8_t Arg6, uint8_t Arg7, int64_t Arg8, uint8_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint16_t v_stack_m74;
    uint8_t v_stack_m77;
    uint64_t v_stack_m78;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;

    local_rsp = (local_rsp) - (112);
    v_stack_p18 = local_rbx;
    result = (*(uint64_t *)(v_rip + 0xA19665)) ^ (v_stack_m78);
    v_stack_m48 = result;
    local_rbx = 0;
    v_stack_m74 = 0;
    v_stack_m70 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m77 = 0;
    v_stack_m78 = 1;
    if (Arg5 != 0) goto loc_003F1371;
loc_003F111F:
    v_stack_m60 = 0;
loc_003F1124:
    if (0 < Arg3) goto loc_003F113A;
    goto loc_003F1241;
loc_003F113A:
    result = (0) + (0);
    if ((*(uint8_t *)(Arg4 + result * 8 + 0xC)) == 1) goto loc_003F114E;
    Arg1 = (uint32_t)((0) + 1);
    v_stack_m60 = (uint32_t)(Arg1);
    goto loc_003F1124;
loc_003F114E:
    local_rsi = ((uint32_t)((uint32_t)(Arg1))) << (4);
    local_rsi = (local_rsi) + (Arg4);
    if (Arg6 >= 2) goto loc_003F121B;
    v_stack_m58 = v_xmm0;
    v_stack_m68 = v_stack_m58;
    if (((uint32_t)(Arg1)) >= 0xFFFFULL) goto loc_003F1228;
    if (Arg5 == 0) goto loc_003F11B3;
    if ((uint32_t)(Arg1) == 0) goto loc_003F11B3;
    Arg4 = ((uint32_t)((uint32_t)(Arg1))) + (v_stack_m58);
    if (Arg4 > Arg2) goto loc_003F122D;
    if (Arg4 < v_stack_m58) goto loc_003F122D;
loc_003F11B3:
    if (((uint32_t)(Arg1)) > 256) goto loc_003F11F9;
    if (((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x8)) + 15) <= ((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x8)))) {
    }
    result = ((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x8)) + 15) & (-16);
    result = _chkstk(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x8)), v_stack_m58, Arg4);
    local_rsp = (local_rsp) - (result);
    v_stack_m70 = v_stack_m78;
loc_003F11E7:
    result = memcpy(v_stack_m70, v_stack_m58, (uint32_t)((uint32_t)(Arg1)), Arg4);
    goto loc_003F1241;
loc_003F11F9:
    result = ExAllocatePool2(66, v_stack_m58, (uint32_t)(0x74777445ULL), Arg4);
    v_stack_m70 = result;
    if (result == 0) goto loc_003F123B;
    v_stack_m77 = 1;
    goto loc_003F11E7;
loc_003F121B:
    v_stack_m68 = v_stack_m58;
    v_stack_m70 = *(uint64_t *)(v_stack_m58);
    goto loc_003F1241;
loc_003F1228:
    v_stack_m78 = 0;
    goto loc_003F12A2;
loc_003F122D:
    goto loc_003F11B3;
loc_003F123B:
    v_stack_m78 = 1;
    goto loc_003F12A2;
loc_003F1241:
    goto loc_003F124B;
loc_003F124B:
    if (v_stack_m68 == 0) goto loc_003F1403;
    if (v_stack_m70 == 0) goto loc_003F1403;
    if (Arg6 >= 2) goto loc_003F1274;
    if ((*(uint32_t *)(v_rip + 0xBD5AAE)) != 0) goto loc_003F12D2;
loc_003F1274:
    if (*(uint64_t *)(arg1 + 0x280) != 0) goto loc_003F12DF;
loc_003F1280:
    if (Arg6 >= 2) goto loc_003F12A2;
    result = *(uint8_t *)(v_stack_m58);
    if ((*(uint32_t *)(v_rip + 0xBD5A94)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(0x74777445ULL), Arg4);
    }
loc_003F12A2:
    if (v_stack_m77 != 0) goto loc_003F13BE;
loc_003F12AB:
loc_003F12AE:
    Arg1 = (v_stack_m48) ^ (v_stack_m78);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x74777445ULL), Arg4);
    return result;
loc_003F12D2:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 2, (uint32_t)(0x74777445ULL), Arg4);
    goto loc_003F1274;
loc_003F12DF:
    local_rsi = (v_stack_m68) * ((uint32_t)(Arg2));
    if (Arg9 != 0) goto loc_003F13CE;
loc_003F12F6:
    if (*(uint64_t *)(local_rsi + (uint8_t)(v_cr8) * 1 + 0x60) == 0) goto loc_003F1280;
    if (Arg6 <= 2) {
        Arg3 = 2;
    }
    v_stack_p28 = Arg9;
    v_stack_p20 = Arg8;
    result = EtwpIsEventNameFilterEnabled(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg7);
    if ((uint8_t)(result) == 0) goto loc_003F1280;
    result = EtwpGetEventNameFromEventMetadata(v_stack_m70, (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)), v_stack_m74, Arg7);
    if (result == 0) goto loc_003F13D8;
    if ((uint16_t)(v_stack_m74) == 0) goto loc_003F13FC;
    result = EtwpEventNameFilterSearch(result, v_stack_m74, *(uint64_t *)(local_rsi + (uint8_t)(v_cr8) * 1 + 0x60), Arg7);
loc_003F1368:
    goto loc_003F1280;
loc_003F1371:
    result = ((uint32_t)((uint32_t)(*(uint64_t *)(local_rsi + (uint8_t)(v_cr8) * 1 + 0x60)))) << (4);
    if (result == 0) goto loc_003F13A8;
    if (((Arg7) & (3)) != 0) goto loc_003F13A3;
    if ((result + Arg7 * 1) > v_stack_m74) goto loc_003F139B;
    if ((result + Arg7 * 1) >= Arg7) goto loc_003F13B2;
loc_003F139B:
    goto loc_003F13B2;
loc_003F13A3:
    result = ExRaiseDatatypeMisalignment(result + Arg7 * 1, v_stack_m74, *(uint64_t *)(local_rsi + (uint8_t)(v_cr8) * 1 + 0x60), Arg7);
loc_003F13A8:
loc_003F13B2:
    goto loc_003F111F;
loc_003F13BE:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, Arg2, *(uint64_t *)(local_rsi + (uint8_t)(v_cr8) * 1 + 0x60), Arg7);
    goto loc_003F12AB;
loc_003F13CE:
    goto loc_003F12F6;
loc_003F13D8:
    if (Arg6 >= 2) goto loc_003F1403;
    result = KiLowerIrqlProcessIrqlFlags((uint8_t)(v_cr8), (uint8_t)(v_cr8), *(uint64_t *)(local_rsi + (uint8_t)(v_cr8) * 1 + 0x60), Arg7);
loc_003F13FC:
    goto loc_003F1368;
loc_003F1403:
    v_stack_m78 = 1;
    goto loc_003F12A2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x280` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F10B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
