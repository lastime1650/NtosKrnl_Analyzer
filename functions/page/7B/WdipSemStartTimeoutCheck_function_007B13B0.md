# WdipSemStartTimeoutCheck

- RVA: `0x007B13B0`–`0x007B142E` (길이 `126` bytes)
- VA: `0x00000001407B13B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `25`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x007B13C4` → [WdipSemSqmInit](WdipSemSqmInit_function_007B1E98.md) (function, `0x007B1E98`)
- `0x007B13D6` → [ExAllocateTimer](../../text/3A/ExAllocateTimer_function_003A30D0.md) (function, `0x003A30D0`)
- `0x007B1421` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [WdipSemCleanStart](../7A/WdipSemCleanStart_function_007AF590.md) at `0x007AF5CD`

### Static image references
- `0x007B13B4` → RVA `0x00EFFC38` (`.data`; read)
- `0x007B13BD` → RVA `0x00EFFC38` (`.data`; write)
- `0x007B13CB` → RVA `0x004BA980` (`WdipTimeoutTimerRoutine`; read)
- `0x007B13DB` → RVA `0x00EFFC70` (`.data`; write)
- `0x007B13E7` → RVA `0x00EFFC60` (`.data`; read/write)
- `0x007B13EF` → RVA `0x00A5B910` (`WdipTimeoutCheckRoutine`; read)
- `0x007B13F6` → RVA `0x00EFFC68` (`.data`; read/write)
- `0x007B13FE` → RVA `0x00EFFC40` (`.data`; read)
- `0x007B1405` → RVA `0x00EFFC58` (`.data`; read/write)
- `0x007B1412` → RVA `0x00EFFC40` (`.data`; read/write)
- `0x007B141A` → RVA `0x00EFFC50` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007B13D6` → [ExAllocateTimer](../../text/3A/ExAllocateTimer_function_003A30D0.md) (`PAGE` → `.text`)
  - `0x007B1421` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B13B0  48 83 EC 28                     sub rsp, 0x28
007B13B4  80 3D 7D E8 74 00 00            cmp byte ptr [rip + 0x74e87d], 0
007B13BB  75 69                           jne 0x1407b1426
007B13BD  C6 05 74 E8 74 00 01            mov byte ptr [rip + 0x74e874], 1
007B13C4  E8 CF 0A 00 00                  call 0x1407b1e98
007B13C9  33 D2                           xor edx, edx
007B13CB  48 8D 0D AE 95 D0 FF            lea rcx, [rip - 0x2f6a52]
007B13D2  44 8D 42 08                     lea r8d, [rdx + 8]
007B13D6  E8 F5 1C BF FF                  call 0x1403a30d0
007B13DB  48 89 05 8E E8 74 00            mov qword ptr [rip + 0x74e88e], rax
007B13E2  48 85 C0                        test rax, rax
007B13E5  74 3F                           je 0x1407b1426
007B13E7  48 83 25 71 E8 74 00 00         and qword ptr [rip + 0x74e871], 0
007B13EF  48 8D 05 1A A5 2A 00            lea rax, [rip + 0x2aa51a]
007B13F6  48 83 0D 6A E8 74 00 FF         or qword ptr [rip + 0x74e86a], 0xffffffffffffffff
007B13FE  48 8D 0D 3B E8 74 00            lea rcx, [rip + 0x74e83b]
007B1405  48 83 25 4B E8 74 00 00         and qword ptr [rip + 0x74e84b], 0
007B140D  BA 01 00 00 00                  mov edx, 1
007B1412  48 83 25 26 E8 74 00 00         and qword ptr [rip + 0x74e826], 0
007B141A  48 89 05 2F E8 74 00            mov qword ptr [rip + 0x74e82f], rax
007B1421  E8 FA 80 B4 FF                  call 0x1402f9520
007B1426  33 C0                           xor eax, eax
007B1428  48 83 C4 28                     add rsp, 0x28
007B142C  C3                              ret
007B142D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdipSemStartTimeoutCheck(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 7661693)) != 0) goto loc_007B1426;
    *(unsigned __int8 *)(v_rip + 7661684) = 1;
    result = WdipSemSqmInit(a1, a2, a3, a4);
    a2 = 0;
    result = ExAllocateTimer(v_rip - 3107410, a2, a2 + 8, a4);
    *(unsigned __int64 *)(v_rip + 7661710) = result;
    if (result != 0) {
        result = v_rip + 2794778;
        a1 = v_rip + 7661627;
        a2 = 1;
        *(unsigned __int64 *)(v_rip + 7661615) = result;
        result = ExQueueWorkItem(a1, a2, a2 + 8, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WdipSemStartTimeoutCheck(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x74E87D)) != 0) goto loc_007B1426;
    *(uint8_t *)(v_rip + 0x74E874) = 1;
    result = WdipSemSqmInit(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    result = ExAllocateTimer(v_rip - 3107410, Arg2, Arg2 + 8, a4);
    *(uint64_t *)(v_rip + 0x74E88E) = result;
    if (result != 0) {
        result = v_rip + 2794778;
        Arg1 = v_rip + 7661627;
        Arg2 = 1;
        *(uint64_t *)(v_rip + 0x74E82F) = result;
        result = ExQueueWorkItem(Arg1, Arg2, Arg2 + 8, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B13B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B13B0[BB_007B13B0]
  bb_007B13BD[BB_007B13BD]
  bb_007B13E7[BB_007B13E7]
  bb_007B1426[BB_007B1426]
  bb_007B142D[BB_007B142D]
  bb_007B13B0 -->|branch| bb_007B1426
  bb_007B13B0 -->|fallthrough| bb_007B13BD
  bb_007B13BD -->|branch| bb_007B1426
  bb_007B13BD -->|fallthrough| bb_007B13E7
  bb_007B13E7 -->|flow| bb_007B1426
```
