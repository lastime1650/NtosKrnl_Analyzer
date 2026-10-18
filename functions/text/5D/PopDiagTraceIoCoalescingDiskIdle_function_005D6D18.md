# PopDiagTraceIoCoalescingDiskIdle

- RVA: `0x005D6D18`–`0x005D6DB1` (길이 `153` bytes)
- VA: `0x00000001405D6D18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEE48`
- 디코드: `32`개 명령, `153/153` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005D6D47` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005D6D99` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005D6DA6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopScanIdleList](../49/PopScanIdleList_function_00497F04.md) at `0x004980DE`

### Static image references
- `0x005D6D21` → RVA `0x00E0A740` (`.data`; read)
- `0x005D6D30` → RVA `0x00E67858` (`.data`; read)
- `0x005D6D39` → RVA `0x00F0B408` (`.data`; read)
- `0x005D6D40` → RVA `0x00021D88` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D6D18  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005D6D1D  48 83 EC 68                     sub rsp, 0x68
005D6D21  48 8B 05 18 3A 83 00            mov rax, qword ptr [rip + 0x833a18]
005D6D28  48 33 C4                        xor rax, rsp
005D6D2B  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005D6D30  80 3D 21 0B 89 00 00            cmp byte ptr [rip + 0x890b21], 0
005D6D37  74 65                           je 0x1405d6d9e
005D6D39  48 8B 0D C8 46 93 00            mov rcx, qword ptr [rip + 0x9346c8]
005D6D40  48 8D 15 41 B0 A4 FF            lea rdx, [rip - 0x5b4fbf]
005D6D47  E8 04 B7 DB FF                  call 0x140392450
005D6D4C  84 C0                           test al, al
005D6D4E  74 4E                           je 0x1405d6d9e
005D6D50  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
005D6D55  48 8D 44 24 70                  lea rax, [rsp + 0x70]
005D6D5A  48 8B 0D A7 46 93 00            mov rcx, qword ptr [rip + 0x9346a7]
005D6D61  48 8D 15 20 B0 A4 FF            lea rdx, [rip - 0x5b4fe0]
005D6D68  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005D6D6D  45 33 C9                        xor r9d, r9d
005D6D70  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005D6D75  C7 44 24 48 08 00 00 00         mov dword ptr [rsp + 0x48], 8
005D6D7D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005D6D82  45 33 C0                        xor r8d, r8d
005D6D85  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
005D6D8D  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005D6D93  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D6D99  E8 32 83 C8 FF                  call 0x14025f0d0
005D6D9E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
005D6DA3  48 33 CC                        xor rcx, rsp
005D6DA6  E8 95 58 0D 00                  call 0x1406ac640
005D6DAB  48 83 C4 68                     add rsp, 0x68
005D6DAF  C3                              ret
005D6DB0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceIoCoalescingDiskIdle(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 8600088)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 8981281)) == 0) goto loc_005D6D9E;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9651912), v_rip - 5984191, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 9651879);
        a2 = v_rip - 5984224;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 8;
        v_stack_m30 = result;
        a3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceIoCoalescingDiskIdle(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x833A18)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x890B21)) == 0) goto loc_005D6D9E;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x9346C8), v_rip - 5984191, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x9346A7);
        Arg2 = v_rip - 5984224;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 8;
        v_stack_m30 = result;
        Arg3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D6D18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D6D18[BB_005D6D18]
  bb_005D6D39[BB_005D6D39]
  bb_005D6D50[BB_005D6D50]
  bb_005D6D9E[BB_005D6D9E]
  bb_005D6DB0[BB_005D6DB0]
  bb_005D6D18 -->|branch| bb_005D6D9E
  bb_005D6D18 -->|fallthrough| bb_005D6D39
  bb_005D6D39 -->|branch| bb_005D6D9E
  bb_005D6D39 -->|fallthrough| bb_005D6D50
  bb_005D6D50 -->|flow| bb_005D6D9E
```
