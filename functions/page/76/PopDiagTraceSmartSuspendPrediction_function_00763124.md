# PopDiagTraceSmartSuspendPrediction

- RVA: `0x00763124`–`0x00763462` (길이 `830` bytes)
- VA: `0x0000000140763124`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC8A4`
- 디코드: `155`개 명령, `830/830` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00763185` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x00763193` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x007631A1` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x007631AF` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x007631BD` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x007631CB` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x007631D8` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x007631E5` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x007631F2` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (function, `0x004C1724`)
- `0x00763215` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0076343C` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0076344B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopSmartSuspendMakePredictions](../AD/PopSmartSuspendMakePredictions_function_00AD9168.md) at `0x00AD93C3`

### Static image references
- `0x00763139` → RVA `0x00E0A740` (`.data`; read)
- `0x007631F7` → RVA `0x00E07748` (`.data`; read)
- `0x00763404` → RVA `0x0004B1DD` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00763185` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x00763193` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x007631A1` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x007631AF` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x007631BD` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x007631CB` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x007631D8` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x007631E5` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x007631F2` → [PopSystemTimeToLocalTime](../../text/4C/PopSystemTimeToLocalTime_function_004C1724.md) (`PAGE` → `.text`)
  - `0x00763215` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0076343C` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0076344B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00763124  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00763129  55                              push rbp
0076312A  48 8D AC 24 E0 FE FF FF         lea rbp, [rsp - 0x120]
00763132  48 81 EC 20 02 00 00            sub rsp, 0x220
00763139  48 8B 05 00 76 6A 00            mov rax, qword ptr [rip + 0x6a7600]
00763140  48 33 C4                        xor rax, rsp
00763143  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
0076314A  33 DB                           xor ebx, ebx
0076314C  4C 8B DA                        mov r11, rdx
0076314F  48 8D 51 18                     lea rdx, [rcx + 0x18]
00763153  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00763158  4C 8B D1                        mov r10, rcx
0076315B  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00763160  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00763165  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
0076316A  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
0076316F  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00763174  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00763179  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
0076317D  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
00763181  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
00763185  E8 9A E5 D5 FF                  call 0x1404c1724
0076318A  49 8D 52 20                     lea rdx, [r10 + 0x20]
0076318E  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00763193  E8 8C E5 D5 FF                  call 0x1404c1724
00763198  49 8D 52 28                     lea rdx, [r10 + 0x28]
0076319C  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007631A1  E8 7E E5 D5 FF                  call 0x1404c1724
007631A6  49 8D 52 30                     lea rdx, [r10 + 0x30]
007631AA  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007631AF  E8 70 E5 D5 FF                  call 0x1404c1724
007631B4  49 8D 52 38                     lea rdx, [r10 + 0x38]
007631B8  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
007631BD  E8 62 E5 D5 FF                  call 0x1404c1724
007631C2  49 8D 53 20                     lea rdx, [r11 + 0x20]
007631C6  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
007631CB  E8 54 E5 D5 FF                  call 0x1404c1724
007631D0  49 8D 53 28                     lea rdx, [r11 + 0x28]
007631D4  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007631D8  E8 47 E5 D5 FF                  call 0x1404c1724
007631DD  49 8D 53 30                     lea rdx, [r11 + 0x30]
007631E1  48 8D 4D 88                     lea rcx, [rbp - 0x78]
007631E5  E8 3A E5 D5 FF                  call 0x1404c1724
007631EA  49 8D 53 38                     lea rdx, [r11 + 0x38]
007631EE  48 8D 4D 90                     lea rcx, [rbp - 0x70]
007631F2  E8 2D E5 D5 FF                  call 0x1404c1724
007631F7  83 3D 4A 45 6A 00 05            cmp dword ptr [rip + 0x6a454a], 5
007631FE  0F 86 3D 02 00 00               jbe 0x140763441
00763204  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
0076320E  48 8D 0D 33 45 6A 00            lea rcx, [rip + 0x6a4533]
00763215  E8 86 B8 CC FF                  call 0x14042eaa0
0076321A  84 C0                           test al, al
0076321C  0F 84 1F 02 00 00               je 0x140763441
00763222  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00763227  48 C7 45 C8 08 00 00 00         mov qword ptr [rbp - 0x38], 8
0076322F  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00763233  41 8B 42 48                     mov eax, dword ptr [r10 + 0x48]
00763237  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0076323B  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00763240  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00763244  41 8B 42 44                     mov eax, dword ptr [r10 + 0x44]
00763248  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0076324C  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
00763251  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00763255  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
00763259  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0076325D  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00763262  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00763266  41 8A 02                        mov al, byte ptr [r10]
00763269  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0076326D  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00763272  48 89 45 00                     mov qword ptr [rbp], rax
00763276  41 8A 42 01                     mov al, byte ptr [r10 + 1]
0076327A  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0076327E  48 8D 44 24 31                  lea rax, [rsp + 0x31]
00763283  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00763287  41 8B 42 08                     mov eax, dword ptr [r10 + 8]
0076328B  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0076328F  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00763294  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00763298  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0076329D  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
007632A1  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007632A6  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
007632AA  41 8A 42 02                     mov al, byte ptr [r10 + 2]
007632AE  88 44 24 32                     mov byte ptr [rsp + 0x32], al
007632B2  48 8D 44 24 32                  lea rax, [rsp + 0x32]
007632B7  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
007632BB  41 8A 42 03                     mov al, byte ptr [r10 + 3]
007632BF  88 44 24 33                     mov byte ptr [rsp + 0x33], al
007632C3  48 8D 44 24 33                  lea rax, [rsp + 0x33]
007632C8  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
007632CC  41 8B 42 0C                     mov eax, dword ptr [r10 + 0xc]
007632D0  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
007632D4  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007632D9  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
007632DD  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007632E2  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
007632E9  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007632EE  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
007632F5  41 8A 03                        mov al, byte ptr [r11]
007632F8  88 44 24 34                     mov byte ptr [rsp + 0x34], al
007632FC  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00763301  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00763308  48 8D 44 24 78                  lea rax, [rsp + 0x78]
0076330D  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00763314  48 8D 45 80                     lea rax, [rbp - 0x80]
00763318  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
0076331F  41 8A 43 02                     mov al, byte ptr [r11 + 2]
00763323  88 44 24 35                     mov byte ptr [rsp + 0x35], al
00763327  48 8D 44 24 35                  lea rax, [rsp + 0x35]
0076332C  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00763333  48 8D 45 88                     lea rax, [rbp - 0x78]
00763337  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
0076333E  48 8D 45 90                     lea rax, [rbp - 0x70]
00763342  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00763349  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00763351  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
00763359  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
00763361  48 C7 45 08 01 00 00 00         mov qword ptr [rbp + 8], 1
00763369  48 C7 45 18 01 00 00 00         mov qword ptr [rbp + 0x18], 1
00763371  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
00763379  48 C7 45 38 08 00 00 00         mov qword ptr [rbp + 0x38], 8
00763381  48 C7 45 48 08 00 00 00         mov qword ptr [rbp + 0x48], 8
00763389  48 C7 45 58 01 00 00 00         mov qword ptr [rbp + 0x58], 1
00763391  48 C7 45 68 01 00 00 00         mov qword ptr [rbp + 0x68], 1
00763399  48 C7 45 78 04 00 00 00         mov qword ptr [rbp + 0x78], 4
007633A1  48 C7 85 88 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x88], 8
007633AC  48 C7 85 98 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x98], 8
007633B7  48 C7 85 A8 00 00 00 01 00 00 00  mov qword ptr [rbp + 0xa8], 1
007633C2  48 C7 85 B8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xb8], 8
007633CD  48 C7 85 C8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xc8], 8
007633D8  48 C7 85 D8 00 00 00 01 00 00 00  mov qword ptr [rbp + 0xd8], 1
007633E3  48 C7 85 E8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xe8], 8
007633EE  48 8D 45 98                     lea rax, [rbp - 0x68]
007633F2  48 C7 85 F8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xf8], 8
007633FD  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00763404  48 8D 15 D2 7D 8E FF            lea rdx, [rip - 0x71822e]
0076340B  48 8D 45 A0                     lea rax, [rbp - 0x60]
0076340F  48 C7 45 98 00 00 00 02         mov qword ptr [rbp - 0x68], 0x2000000
00763417  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0076341C  48 8D 0D 25 43 6A 00            lea rcx, [rip + 0x6a4325]
00763423  45 33 C9                        xor r9d, r9d
00763426  C7 44 24 20 17 00 00 00         mov dword ptr [rsp + 0x20], 0x17
0076342E  45 33 C0                        xor r8d, r8d
00763431  48 C7 85 08 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x108], 8
0076343C  E8 9F 2C CC FF                  call 0x1404260e0
00763441  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
00763448  48 33 CC                        xor rcx, rsp
0076344B  E8 F0 91 F4 FF                  call 0x1406ac640
00763450  48 8B 9C 24 30 02 00 00         mov rbx, qword ptr [rsp + 0x230]
00763458  48 81 C4 20 02 00 00            add rsp, 0x220
0076345F  5D                              pop rbp
00763460  C3                              ret
00763461  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSmartSuspendPrediction(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
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
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned int v_stack_m1E8;
    unsigned int v_stack_m1EC;
    unsigned int v_stack_m1F0;
    unsigned __int8 v_stack_m1F3;
    unsigned __int8 v_stack_m1F4;
    unsigned __int8 v_stack_m1F5;
    unsigned __int8 v_stack_m1F6;
    unsigned __int8 v_stack_m1F7;
    unsigned __int8 v_stack_m1F8;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (544);
    result = (*(unsigned __int64 *)(v_rip + 6977024)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rbx = 0;
    v_stack_m1D8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    v_stack_m198 = 0;
    result = PopSystemTimeToLocalTime(v_stack_m1D8, a1 + 24, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m1D0, a1 + 32, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m1C8, a1 + 40, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m1C0, a1 + 48, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m1B8, a1 + 56, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m1B0, a2 + 32, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m1A8, a2 + 40, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m1A0, a2 + 48, a3, a4);
    result = PopSystemTimeToLocalTime(v_stack_m198, a2 + 56, a3, a4);
    if ((*(unsigned int *)(v_rip + 6964554)) <= 5) goto loc_00763441;
    result = tlgKeywordOn(v_rip + 6964531, a2 + 56, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m1D8;
        v_stack_m160 = 8;
        v_stack_m168 = result;
        result = *(unsigned int *)(a1 + 72);
        v_stack_m1F0 = (unsigned int)(result);
        result = v_stack_m1F0;
        v_stack_m158 = result;
        result = *(unsigned int *)(a1 + 68);
        v_stack_m1EC = (unsigned int)(result);
        result = v_stack_m1EC;
        v_stack_m148 = result;
        result = *(unsigned int *)(a1 + 4);
        v_stack_m1E8 = (unsigned int)(result);
        result = v_stack_m1E8;
        v_stack_m138 = result;
        result = *(unsigned __int8 *)(a1);
        v_stack_m1F8 = (unsigned __int8)(result);
        result = v_stack_m1F8;
        v_stack_m128 = result;
        result = *(unsigned __int8 *)(a1 + 1);
        v_stack_m1F7 = (unsigned __int8)(result);
        result = v_stack_m1F7;
        v_stack_m118 = result;
        result = *(unsigned int *)(a1 + 8);
        v_stack_m1E4 = (unsigned int)(result);
        result = v_stack_m1E4;
        v_stack_m108 = result;
        result = v_stack_m1D0;
        v_stack_mF8 = result;
        result = v_stack_m1C8;
        v_stack_mE8 = result;
        result = *(unsigned __int8 *)(a1 + 2);
        v_stack_m1F6 = (unsigned __int8)(result);
        result = v_stack_m1F6;
        v_stack_mD8 = result;
        result = *(unsigned __int8 *)(a1 + 3);
        v_stack_m1F5 = (unsigned __int8)(result);
        result = v_stack_m1F5;
        v_stack_mC8 = result;
        result = *(unsigned int *)(a1 + 12);
        v_stack_m1E0 = (unsigned int)(result);
        result = v_stack_m1E0;
        v_stack_mB8 = result;
        result = v_stack_m1C0;
        v_stack_mA8 = result;
        result = v_stack_m1B8;
        v_stack_m98 = result;
        result = *(unsigned __int8 *)(a2);
        v_stack_m1F4 = (unsigned __int8)(result);
        result = v_stack_m1F4;
        v_stack_m88 = result;
        result = v_stack_m1B0;
        v_stack_m78 = result;
        result = v_stack_m1A8;
        v_stack_m68 = result;
        result = *(unsigned __int8 *)(a2 + 2);
        v_stack_m1F3 = (unsigned __int8)(result);
        result = v_stack_m1F3;
        v_stack_m58 = result;
        result = v_stack_m1A0;
        v_stack_m48 = result;
        result = v_stack_m198;
        v_stack_m38 = result;
        v_stack_m150 = 4;
        v_stack_m140 = 4;
        v_stack_m130 = 4;
        v_stack_m120 = 1;
        v_stack_m110 = 1;
        v_stack_m100 = 4;
        v_stack_mF0 = 8;
        v_stack_mE0 = 8;
        v_stack_mD0 = 1;
        v_stack_mC0 = 1;
        v_stack_mB0 = 4;
        v_stack_mA0 = 8;
        v_stack_m90 = 8;
        v_stack_m80 = 1;
        v_stack_m70 = 8;
        v_stack_m60 = 8;
        v_stack_m50 = 1;
        v_stack_m40 = 8;
        result = v_stack_m190;
        v_stack_m30 = 8;
        v_stack_m28 = result;
        a2 = v_rip - 7438894;
        result = v_stack_m188;
        v_stack_m190 = 0x2000000ULL;
        v_stack_m200 = result;
        a1 = v_rip + 6964005;
        a4 = 0;
        v_stack_m208 = 23;
        a3 = 0;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (544);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceSmartSuspendPrediction(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
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
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m18;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint32_t v_stack_m1E8;
    uint32_t v_stack_m1EC;
    uint32_t v_stack_m1F0;
    uint8_t v_stack_m1F3;
    uint8_t v_stack_m1F4;
    uint8_t v_stack_m1F5;
    uint8_t v_stack_m1F6;
    uint8_t v_stack_m1F7;
    uint8_t v_stack_m1F8;
    uint64_t v_stack_m20;
    uint64_t v_stack_m200;
    uint32_t v_stack_m208;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (544);
    result = (*(uint64_t *)(v_rip + 0x6A7600)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rbx = 0;
    v_stack_m1D8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    v_stack_m198 = 0;
    result = PopSystemTimeToLocalTime(v_stack_m1D8, Arg1 + 24, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m1D0, Arg1 + 32, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m1C8, Arg1 + 40, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m1C0, Arg1 + 48, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m1B8, Arg1 + 56, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m1B0, Arg2 + 32, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m1A8, Arg2 + 40, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m1A0, Arg2 + 48, Arg3, Arg4);
    result = PopSystemTimeToLocalTime(v_stack_m198, Arg2 + 56, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x6A454A)) <= 5) goto loc_00763441;
    result = tlgKeywordOn(v_rip + 6964531, Arg2 + 56, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m1D8;
        v_stack_m160 = 8;
        v_stack_m168 = result;
        result = *(uint32_t *)(arg1 + 0x48);
        v_stack_m1F0 = (uint32_t)(result);
        result = v_stack_m1F0;
        v_stack_m158 = result;
        result = *(uint32_t *)(arg1 + 0x44);
        v_stack_m1EC = (uint32_t)(result);
        result = v_stack_m1EC;
        v_stack_m148 = result;
        result = *(uint32_t *)(arg1 + 0x4);
        v_stack_m1E8 = (uint32_t)(result);
        result = v_stack_m1E8;
        v_stack_m138 = result;
        result = *(uint8_t *)(arg1);
        v_stack_m1F8 = (uint8_t)(result);
        result = v_stack_m1F8;
        v_stack_m128 = result;
        result = *(uint8_t *)(arg1 + 0x1);
        v_stack_m1F7 = (uint8_t)(result);
        result = v_stack_m1F7;
        v_stack_m118 = result;
        result = *(uint32_t *)(arg1 + 0x8);
        v_stack_m1E4 = (uint32_t)(result);
        result = v_stack_m1E4;
        v_stack_m108 = result;
        result = v_stack_m1D0;
        v_stack_mF8 = result;
        result = v_stack_m1C8;
        v_stack_mE8 = result;
        result = *(uint8_t *)(arg1 + 0x2);
        v_stack_m1F6 = (uint8_t)(result);
        result = v_stack_m1F6;
        v_stack_mD8 = result;
        result = *(uint8_t *)(arg1 + 0x3);
        v_stack_m1F5 = (uint8_t)(result);
        result = v_stack_m1F5;
        v_stack_mC8 = result;
        result = *(uint32_t *)(arg1 + 0xC);
        v_stack_m1E0 = (uint32_t)(result);
        result = v_stack_m1E0;
        v_stack_mB8 = result;
        result = v_stack_m1C0;
        v_stack_mA8 = result;
        result = v_stack_m1B8;
        v_stack_m98 = result;
        result = *(uint8_t *)(Arg2);
        v_stack_m1F4 = (uint8_t)(result);
        result = v_stack_m1F4;
        v_stack_m88 = result;
        result = v_stack_m1B0;
        v_stack_m78 = result;
        result = v_stack_m1A8;
        v_stack_m68 = result;
        result = *(uint8_t *)(Arg2 + 0x2);
        v_stack_m1F3 = (uint8_t)(result);
        result = v_stack_m1F3;
        v_stack_m58 = result;
        result = v_stack_m1A0;
        v_stack_m48 = result;
        result = v_stack_m198;
        v_stack_m38 = result;
        v_stack_m150 = 4;
        v_stack_m140 = 4;
        v_stack_m130 = 4;
        v_stack_m120 = 1;
        v_stack_m110 = 1;
        v_stack_m100 = 4;
        v_stack_mF0 = 8;
        v_stack_mE0 = 8;
        v_stack_mD0 = 1;
        v_stack_mC0 = 1;
        v_stack_mB0 = 4;
        v_stack_mA0 = 8;
        v_stack_m90 = 8;
        v_stack_m80 = 1;
        v_stack_m70 = 8;
        v_stack_m60 = 8;
        v_stack_m50 = 1;
        v_stack_m40 = 8;
        result = v_stack_m190;
        v_stack_m30 = 8;
        v_stack_m28 = result;
        Arg2 = v_rip - 7438894;
        result = v_stack_m188;
        v_stack_m190 = 0x2000000ULL;
        v_stack_m200 = result;
        Arg1 = v_rip + 6964005;
        Arg4 = 0;
        v_stack_m208 = 23;
        Arg3 = 0;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (544);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00763124&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00763124[BB_00763124]
  bb_00763204[BB_00763204]
  bb_00763222[BB_00763222]
  bb_00763441[BB_00763441]
  bb_00763461[BB_00763461]
  bb_00763124 -->|branch| bb_00763441
  bb_00763124 -->|fallthrough| bb_00763204
  bb_00763204 -->|branch| bb_00763441
  bb_00763204 -->|fallthrough| bb_00763222
  bb_00763222 -->|flow| bb_00763441
```
