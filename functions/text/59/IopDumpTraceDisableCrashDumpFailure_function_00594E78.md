# IopDumpTraceDisableCrashDumpFailure

- RVA: `0x00594E78`–`0x00594F80` (길이 `264` bytes)
- VA: `0x0000000140594E78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF3A4`
- 디코드: `57`개 명령, `264/264` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00594E97` → [IopDumpIsTracingEnabled](../4F/IopDumpIsTracingEnabled_function_004FC5D0.md) (function, `0x004FC5D0`)
- `0x00594EE4` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x00594F03` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00594F65` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00594F71` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IopDisableCrashDump](IopDisableCrashDump_function_005949A0.md) at `0x005949D2`

### Static image references
- `0x00594E89` → RVA `0x00E0A740` (`.data`; read)
- `0x00594EA8` → RVA `0x00E65EF0` (`.data`; read)
- `0x00594EAF` → RVA `0x000216E0` (`.rdata`; read)
- `0x00594EE9` → RVA `0x00E06DE8` (`.data`; read)
- `0x00594F18` → RVA `0x00045BA3` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00594E78  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00594E7C  55                              push rbp
00594E7D  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00594E82  48 81 EC B0 00 00 00            sub rsp, 0xb0
00594E89  48 8B 05 B0 58 87 00            mov rax, qword ptr [rip + 0x8758b0]
00594E90  48 33 C4                        xor rax, rsp
00594E93  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00594E97  E8 34 77 F6 FF                  call 0x1404fc5d0
00594E9C  84 C0                           test al, al
00594E9E  74 49                           je 0x140594ee9
00594EA0  83 65 03 00                     and dword ptr [rbp + 3], 0
00594EA4  48 8D 45 67                     lea rax, [rbp + 0x67]
00594EA8  48 8B 0D 41 10 8D 00            mov rcx, qword ptr [rip + 0x8d1041]
00594EAF  48 8D 15 2A C8 A8 FF            lea rdx, [rip - 0x5737d6]
00594EB6  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00594EBA  45 33 C9                        xor r9d, r9d
00594EBD  48 8D 45 F7                     lea rax, [rbp - 9]
00594EC1  C7 45 FF 04 00 00 00            mov dword ptr [rbp - 1], 4
00594EC8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00594ECD  45 33 C0                        xor r8d, r8d
00594ED0  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00594ED8  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00594EDE  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00594EE4  E8 E7 A1 CC FF                  call 0x14025f0d0
00594EE9  83 3D F8 1E 87 00 05            cmp dword ptr [rip + 0x871ef8], 5
00594EF0  76 78                           jbe 0x140594f6a
00594EF2  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00594EFC  48 8D 0D E5 1E 87 00            lea rcx, [rip + 0x871ee5]
00594F03  E8 98 9B E9 FF                  call 0x14042eaa0
00594F08  84 C0                           test al, al
00594F0A  74 5E                           je 0x140594f6a
00594F0C  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00594F10  48 8D 45 EF                     lea rax, [rbp - 0x11]
00594F14  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00594F18  48 8D 15 84 0C AB FF            lea rdx, [rip - 0x54f37c]
00594F1F  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00594F23  48 8D 0D BE 1E 87 00            lea rcx, [rip + 0x871ebe]
00594F2A  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
00594F2D  45 33 C9                        xor r9d, r9d
00594F30  89 45 E7                        mov dword ptr [rbp - 0x19], eax
00594F33  45 33 C0                        xor r8d, r8d
00594F36  48 8D 45 E7                     lea rax, [rbp - 0x19]
00594F3A  48 C7 45 EF 00 00 00 01         mov qword ptr [rbp - 0x11], 0x1000000
00594F42  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00594F46  48 8D 45 07                     lea rax, [rbp + 7]
00594F4A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00594F4F  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00594F57  C7 45 2F 08 00 00 00            mov dword ptr [rbp + 0x2f], 8
00594F5E  C7 45 3F 04 00 00 00            mov dword ptr [rbp + 0x3f], 4
00594F65  E8 76 11 E9 FF                  call 0x1404260e0
00594F6A  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00594F6E  48 33 CC                        xor rcx, rsp
00594F71  E8 CA 76 11 00                  call 0x1406ac640
00594F76  48 81 C4 B0 00 00 00            add rsp, 0xb0
00594F7D  5D                              pop rbp
00594F7E  C3                              ret
00594F7F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopDumpTraceDisableCrashDumpFailure(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 8870064)) ^ (v_rsp);
    v_stack_m18 = result;
    result = IopDumpIsTracingEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 9244737);
        a2 = v_rip - 5715926;
        v_stack_m68 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m60 = 4;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 8855288)) <= 5) goto loc_00594F6A;
    result = tlgKeywordOn(v_rip + 8855269, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m70;
        a2 = v_rip - 5567356;
        v_stack_m38 = result;
        a1 = v_rip + 8855230;
        result = v_stack_p8;
        a4 = 0;
        v_stack_m78 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m78;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m90 = result;
        v_stack_m98 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopDumpTraceDisableCrashDumpFailure(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x8758B0)) ^ (local_rsp);
    v_stack_m18 = result;
    result = IopDumpIsTracingEnabled(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x8D1041);
        Arg2 = v_rip - 5715926;
        v_stack_m68 = result;
        Arg4 = 0;
        result = v_stack_m68;
        v_stack_m60 = 4;
        v_stack_m80 = result;
        Arg3 = 0;
        v_stack_m88 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x871EF8)) <= 5) goto loc_00594F6A;
    result = tlgKeywordOn(v_rip + 8855269, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m70;
        Arg2 = v_rip - 5567356;
        v_stack_m38 = result;
        Arg1 = v_rip + 8855230;
        result = v_stack_p8;
        Arg4 = 0;
        v_stack_m78 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m78;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m90 = result;
        v_stack_m98 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00594E78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00594E78[BB_00594E78]
  bb_00594EA0[BB_00594EA0]
  bb_00594EE9[BB_00594EE9]
  bb_00594EF2[BB_00594EF2]
  bb_00594F0C[BB_00594F0C]
  bb_00594F6A[BB_00594F6A]
  bb_00594F7F[BB_00594F7F]
  bb_00594E78 -->|branch| bb_00594EE9
  bb_00594E78 -->|fallthrough| bb_00594EA0
  bb_00594EA0 -->|flow| bb_00594EE9
  bb_00594EE9 -->|branch| bb_00594F6A
  bb_00594EE9 -->|fallthrough| bb_00594EF2
  bb_00594EF2 -->|branch| bb_00594F6A
  bb_00594EF2 -->|fallthrough| bb_00594F0C
  bb_00594F0C -->|flow| bb_00594F6A
```
