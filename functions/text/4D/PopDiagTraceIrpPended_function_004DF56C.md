# PopDiagTraceIrpPended

- RVA: `0x004DF56C`–`0x004DF605` (길이 `153` bytes)
- VA: `0x00000001404DF56C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEE48`
- 디코드: `32`개 명령, `153/153` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004DF59B` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004DF5ED` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004DF5FA` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopFxNotifyPostSIrpCompletion](../5D/PopFxNotifyPostSIrpCompletion_function_005D2F68.md) at `0x005D2F97`
- [PopSystemIrpCompletion](../../pagelk/B7/PopSystemIrpCompletion_function_00B70CC0.md) at `0x00B70E02`

### Static image references
- `0x004DF575` → RVA `0x00E0A740` (`.data`; read)
- `0x004DF584` → RVA `0x00E67858` (`.data`; read)
- `0x004DF58D` → RVA `0x00F0B408` (`.data`; read)
- `0x004DF594` → RVA `0x00020C58` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004DF56C  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
004DF571  48 83 EC 68                     sub rsp, 0x68
004DF575  48 8B 05 C4 B1 92 00            mov rax, qword ptr [rip + 0x92b1c4]
004DF57C  48 33 C4                        xor rax, rsp
004DF57F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004DF584  80 3D CD 82 98 00 00            cmp byte ptr [rip + 0x9882cd], 0
004DF58B  74 65                           je 0x1404df5f2
004DF58D  48 8B 0D 74 BE A2 00            mov rcx, qword ptr [rip + 0xa2be74]
004DF594  48 8D 15 BD 16 B4 FF            lea rdx, [rip - 0x4be943]
004DF59B  E8 B0 2E EB FF                  call 0x140392450
004DF5A0  84 C0                           test al, al
004DF5A2  74 4E                           je 0x1404df5f2
004DF5A4  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
004DF5A9  48 8D 44 24 70                  lea rax, [rsp + 0x70]
004DF5AE  48 8B 0D 53 BE A2 00            mov rcx, qword ptr [rip + 0xa2be53]
004DF5B5  48 8D 15 9C 16 B4 FF            lea rdx, [rip - 0x4be964]
004DF5BC  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004DF5C1  45 33 C9                        xor r9d, r9d
004DF5C4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004DF5C9  C7 44 24 48 08 00 00 00         mov dword ptr [rsp + 0x48], 8
004DF5D1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004DF5D6  45 33 C0                        xor r8d, r8d
004DF5D9  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
004DF5E1  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004DF5E7  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004DF5ED  E8 DE FA D7 FF                  call 0x14025f0d0
004DF5F2  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004DF5F7  48 33 CC                        xor rcx, rsp
004DF5FA  E8 41 D0 1C 00                  call 0x1406ac640
004DF5FF  48 83 C4 68                     add rsp, 0x68
004DF603  C3                              ret
004DF604  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceIrpPended(__int64 a1, __int64 a2, int a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 9613764)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 9994957)) == 0) goto loc_004DF5F2;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10665588), v_rip - 4974915, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 10665555);
        a2 = v_rip - 4974948;
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
int64_t PopDiagTraceIrpPended(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0x92B1C4)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x9882CD)) == 0) goto loc_004DF5F2;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA2BE74), v_rip - 4974915, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0xA2BE53);
        Arg2 = v_rip - 4974948;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004DF56C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004DF56C[BB_004DF56C]
  bb_004DF58D[BB_004DF58D]
  bb_004DF5A4[BB_004DF5A4]
  bb_004DF5F2[BB_004DF5F2]
  bb_004DF604[BB_004DF604]
  bb_004DF56C -->|branch| bb_004DF5F2
  bb_004DF56C -->|fallthrough| bb_004DF58D
  bb_004DF58D -->|branch| bb_004DF5F2
  bb_004DF58D -->|fallthrough| bb_004DF5A4
  bb_004DF5A4 -->|flow| bb_004DF5F2
```
