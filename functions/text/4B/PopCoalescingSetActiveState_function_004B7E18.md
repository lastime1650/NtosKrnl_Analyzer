# PopCoalescingSetActiveState

- RVA: `0x004B7E18`–`0x004B7EA4` (길이 `140` bytes)
- VA: `0x00000001404B7E18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092CC0`
- 디코드: `31`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x004B7E38` → [KeCancelTimer](../23/KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x004B7E3D` → [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) (function, `0x00A31718`)
- `0x004B7E42` → [PopUpdateDiskIdleTimeoutSetting](../../page/91/PopUpdateDiskIdleTimeoutSetting_function_00912E30.md) (function, `0x00912E30`)
- `0x004B7E47` → [PopDiagTraceIoCoalescingOff](../../page/AC/PopDiagTraceIoCoalescingOff_function_00AC0D50.md) (function, `0x00AC0D50`)
- `0x004B7E87` → [PopCoalescingSetTimer](../48/PopCoalescingSetTimer_function_0048EEC0.md) (function, `0x0048EEC0`)
- `0x004B7E8C` → [PopUpdateDiskIdleTimeoutSetting](../../page/91/PopUpdateDiskIdleTimeoutSetting_function_00912E30.md) (function, `0x00912E30`)
- `0x004B7E9D` → [PopDiagTraceIoCoalescingOn](../../page/76/PopDiagTraceIoCoalescingOn_function_00761AB4.md) (function, `0x00761AB4`)

### Direct callers
- [PopCoalescingCallbackWorker](../../page/A8/PopCoalescingCallbackWorker_function_00A8DA40.md) at `0x00A8DA88`
- [PopCoalescingCallbackWorker](../../page/A8/PopCoalescingCallbackWorker_function_00A8DA40.md) at `0x00A8DAAF`

### Static image references
- `0x004B7E24` → RVA `0x00F0E068` (`.data`; read/write)
- `0x004B7E2B` → RVA `0x00F0E000` (`.data`; read)
- `0x004B7E32` → RVA `0x00FC6CCC` (`ALMOSTRO`; write)
- `0x004B7E53` → RVA `0x00FC6ADF` (`ALMOSTRO`; read)
- `0x004B7E63` → RVA `0x00FC6E38` (`ALMOSTRO`; read)
- `0x004B7E69` → RVA `0x00FC6E3C` (`ALMOSTRO`; read)
- `0x004B7E7A` → RVA `0x00F0E060` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x004B7E3D` → [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) (`.text` → `PAGE`)
  - `0x004B7E42` → [PopUpdateDiskIdleTimeoutSetting](../../page/91/PopUpdateDiskIdleTimeoutSetting_function_00912E30.md) (`.text` → `PAGE`)
  - `0x004B7E47` → [PopDiagTraceIoCoalescingOff](../../page/AC/PopDiagTraceIoCoalescingOff_function_00AC0D50.md) (`.text` → `PAGE`)
  - `0x004B7E8C` → [PopUpdateDiskIdleTimeoutSetting](../../page/91/PopUpdateDiskIdleTimeoutSetting_function_00912E30.md) (`.text` → `PAGE`)
  - `0x004B7E9D` → [PopDiagTraceIoCoalescingOn](../../page/76/PopDiagTraceIoCoalescingOn_function_00761AB4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7E18  40 53                           push rbx
004B7E1A  48 83 EC 20                     sub rsp, 0x20
004B7E1E  33 DB                           xor ebx, ebx
004B7E20  84 C9                           test cl, cl
004B7E22  75 2F                           jne 0x1404b7e53
004B7E24  80 25 3D 62 A5 00 FE            and byte ptr [rip + 0xa5623d], 0xfe
004B7E2B  48 8D 0D CE 61 A5 00            lea rcx, [rip + 0xa561ce]
004B7E32  89 1D 94 EE B0 00               mov dword ptr [rip + 0xb0ee94], ebx
004B7E38  E8 A3 A9 D7 FF                  call 0x1402327e0
004B7E3D  E8 D6 98 57 00                  call 0x140a31718
004B7E42  E8 E9 AF 45 00                  call 0x140912e30
004B7E47  E8 04 8F 60 00                  call 0x140ac0d50
004B7E4C  48 83 C4 20                     add rsp, 0x20
004B7E50  5B                              pop rbx
004B7E51  C3                              ret
004B7E52  CC                              int3
004B7E53  38 1D 86 EC B0 00               cmp byte ptr [rip + 0xb0ec86], bl
004B7E59  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
004B7E63  8B 0D CF EF B0 00               mov ecx, dword ptr [rip + 0xb0efcf]
004B7E69  0F 45 0D CC EF B0 00            cmovne ecx, dword ptr [rip + 0xb0efcc]
004B7E70  80 0D F1 61 A5 00 01            or byte ptr [rip + 0xa561f1], 1
004B7E77  48 8B 00                        mov rax, qword ptr [rax]
004B7E7A  48 89 05 DF 61 A5 00            mov qword ptr [rip + 0xa561df], rax
004B7E81  89 0D 45 EE B0 00               mov dword ptr [rip + 0xb0ee45], ecx
004B7E87  E8 34 70 FD FF                  call 0x14048eec0
004B7E8C  E8 9F AF 45 00                  call 0x140912e30
004B7E91  38 1D 48 EC B0 00               cmp byte ptr [rip + 0xb0ec48], bl
004B7E97  0F 94 C3                        sete bl
004B7E9A  44 8B CB                        mov r9d, ebx
004B7E9D  E8 12 9C 2A 00                  call 0x140761ab4
004B7EA2  EB A8                           jmp 0x1404b7e4c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopCoalescingSetActiveState(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (a1 != 0) goto loc_004B7E53;
    *(unsigned int *)(v_rip + 11595412) = 0;
    result = KeCancelTimer(v_rip + 10838478, a2, a3, a4);
    result = PopCheckResiliencyScenarios(v_rip + 10838478, a2, a3, a4);
    result = PopUpdateDiskIdleTimeoutSetting(v_rip + 10838478, a2, a3, a4);
    result = PopDiagTraceIoCoalescingOff(v_rip + 10838478, a2, a3, a4);
loc_004B7E4C:
    v_rsp = (v_rsp) + (32);
    return result;
loc_004B7E53:
    a1 = (unsigned int)(*(unsigned int *)(v_rip + 11595727));
    if ((*(unsigned __int8 *)(v_rip + 11594886)) != 0) { a1 = *(unsigned int *)(v_rip + 11595724); }
    *(unsigned __int64 *)(v_rip + 10838495) = *(unsigned __int64 *)(result);
    *(unsigned int *)(v_rip + 11595333) = a1;
    result = PopCoalescingSetTimer(a1, a2, a3, a4);
    result = PopUpdateDiskIdleTimeoutSetting(a1, a2, a3, a4);
    v_rbx = ((*(unsigned __int8 *)(v_rip + 11594824)) == 0) ? 1 : 0;
    result = PopDiagTraceIoCoalescingOn(a1, a2, a3, (unsigned int)((unsigned int)(v_rbx)));
    goto loc_004B7E4C;
}
```

## 5. (Beta) C Style

```c
int64_t PopCoalescingSetActiveState(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (Arg1 != 0) goto loc_004B7E53;
    *(uint32_t *)(v_rip + 0xB0EE94) = 0;
    result = KeCancelTimer(v_rip + 10838478, a2, a3, a4);
    result = PopCheckResiliencyScenarios(v_rip + 10838478, a2, a3, a4);
    result = PopUpdateDiskIdleTimeoutSetting(v_rip + 10838478, a2, a3, a4);
    result = PopDiagTraceIoCoalescingOff(v_rip + 10838478, a2, a3, a4);
loc_004B7E4C:
    local_rsp = (local_rsp) + (32);
    return result;
loc_004B7E53:
    Arg1 = (uint32_t)(*(uint32_t *)(v_rip + 0xB0EFCF));
    if ((*(uint8_t *)(v_rip + 0xB0EC86)) != 0) { Arg1 = *(uint32_t *)(v_rip + 0xB0EFCC); }
    *(uint64_t *)(v_rip + 0xA561DF) = *(uint64_t *)(result);
    *(uint32_t *)(v_rip + 0xB0EE45) = Arg1;
    result = PopCoalescingSetTimer(Arg1, a2, a3, a4);
    result = PopUpdateDiskIdleTimeoutSetting(Arg1, a2, a3, a4);
    local_rbx = ((*(uint8_t *)(v_rip + 0xB0EC48)) == 0) ? 1 : 0;
    result = PopDiagTraceIoCoalescingOn(Arg1, a2, a3, (uint32_t)((uint32_t)(local_rbx)));
    goto loc_004B7E4C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7E18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7E18[BB_004B7E18]
  bb_004B7E24[BB_004B7E24]
  bb_004B7E4C[BB_004B7E4C]
  bb_004B7E52[BB_004B7E52]
  bb_004B7E53[BB_004B7E53]
  bb_004B7E18 -->|branch| bb_004B7E53
  bb_004B7E18 -->|fallthrough| bb_004B7E24
  bb_004B7E24 -->|flow| bb_004B7E4C
  bb_004B7E52 -->|flow| bb_004B7E53
  bb_004B7E53 -->|branch| bb_004B7E4C
```
