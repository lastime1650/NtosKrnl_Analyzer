# PopDiagTraceDebuggerTransitionRequirements

- RVA: `0x005D6430`–`0x005D6507` (길이 `215` bytes)
- VA: `0x00000001405D6430`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC818`
- 디코드: `47`개 명령, `215/215` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005D6476` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005D64E4` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005D64F0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPepInitializeDebuggerMasks](PopPepInitializeDebuggerMasks_function_005DCB94.md) at `0x005DCC5C`

### Static image references
- `0x005D644A` → RVA `0x00E0A740` (`.data`; read)
- `0x005D6458` → RVA `0x00E67858` (`.data`; read)
- `0x005D6468` → RVA `0x00F0B408` (`.data`; read)
- `0x005D646F` → RVA `0x00021400` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D6430  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005D6435  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
005D643A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005D643F  55                              push rbp
005D6440  48 8B EC                        mov rbp, rsp
005D6443  48 81 EC 80 00 00 00            sub rsp, 0x80
005D644A  48 8B 05 EF 42 83 00            mov rax, qword ptr [rip + 0x8342ef]
005D6451  48 33 C4                        xor rax, rsp
005D6454  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005D6458  80 3D F9 13 89 00 00            cmp byte ptr [rip + 0x8913f9], 0
005D645F  48 8B DA                        mov rbx, rdx
005D6462  0F 84 81 00 00 00               je 0x1405d64e9
005D6468  48 8B 0D 99 4F 93 00            mov rcx, qword ptr [rip + 0x934f99]
005D646F  48 8D 15 8A AF A4 FF            lea rdx, [rip - 0x5b5076]
005D6476  E8 D5 BF DB FF                  call 0x140392450
005D647B  84 C0                           test al, al
005D647D  74 6A                           je 0x1405d64e9
005D647F  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
005D6483  48 8D 45 10                     lea rax, [rbp + 0x10]
005D6487  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
005D648B  48 8D 15 6E AF A4 FF            lea rdx, [rip - 0x5b5092]
005D6492  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
005D6496  45 33 C9                        xor r9d, r9d
005D6499  48 8B 0D 68 4F 93 00            mov rcx, qword ptr [rip + 0x934f68]
005D64A0  45 33 C0                        xor r8d, r8d
005D64A3  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
005D64A7  48 8D 45 20                     lea rax, [rbp + 0x20]
005D64AB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
005D64AF  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
005D64B2  89 45 E8                        mov dword ptr [rbp - 0x18], eax
005D64B5  48 8D 45 C0                     lea rax, [rbp - 0x40]
005D64B9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005D64BE  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
005D64C6  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005D64CC  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D64D2  C7 45 C8 08 00 00 00            mov dword ptr [rbp - 0x38], 8
005D64D9  C7 45 D8 04 00 00 00            mov dword ptr [rbp - 0x28], 4
005D64E0  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
005D64E4  E8 E7 8B C8 FF                  call 0x14025f0d0
005D64E9  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
005D64ED  48 33 CC                        xor rcx, rsp
005D64F0  E8 4B 61 0D 00                  call 0x1406ac640
005D64F5  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
005D64FD  48 81 C4 80 00 00 00            add rsp, 0x80
005D6504  5D                              pop rbp
005D6505  C3                              ret
005D6506  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceDebuggerTransitionRequirements(__int64 a1, __int64 a2, int a3, int a4)
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
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 8602351)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 8983545)) == 0) goto loc_005D64E9;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9654169), v_rip - 5984374, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 5984402;
        a4 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 9654120);
        a3 = 0;
        v_stack_m48 = result;
        result = v_stack_p18;
        v_stack_m38 = result;
        result = v_stack_p18;
        v_stack_m20 = (unsigned int)(result);
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m40 = 8;
        v_stack_m30 = 4;
        v_stack_m28 = a2;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceDebuggerTransitionRequirements(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x8342EF)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x8913F9)) == 0) goto loc_005D64E9;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x934F99), v_rip - 5984374, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 5984402;
        Arg4 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x934F68);
        Arg3 = 0;
        v_stack_m48 = result;
        result = v_stack_p18;
        v_stack_m38 = result;
        result = v_stack_p18;
        v_stack_m20 = (uint32_t)(result);
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m40 = 8;
        v_stack_m30 = 4;
        v_stack_m28 = Arg2;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D6430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D6430[BB_005D6430]
  bb_005D6468[BB_005D6468]
  bb_005D647F[BB_005D647F]
  bb_005D64E9[BB_005D64E9]
  bb_005D6506[BB_005D6506]
  bb_005D6430 -->|branch| bb_005D64E9
  bb_005D6430 -->|fallthrough| bb_005D6468
  bb_005D6468 -->|branch| bb_005D64E9
  bb_005D6468 -->|fallthrough| bb_005D647F
  bb_005D647F -->|flow| bb_005D64E9
```
