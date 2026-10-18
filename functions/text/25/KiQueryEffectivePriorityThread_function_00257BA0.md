# KiQueryEffectivePriorityThread

- RVA: `0x00257BA0`–`0x00257BCA` (길이 `42` bytes)
- VA: `0x0000000140257BA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063C34`
- 디코드: `10`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiRetireDpcList](../21/KiRetireDpcList_function_0021A0B0.md) at `0x0021AC3E`
- [sub_002574E0](Unknown_function_002574E0.md) at `0x00257573`
- [sub_002579C3](Unknown_function_002579C3.md) at `0x002579C9`
- [KiTransitionSchedulingGroupGeneration](../30/KiTransitionSchedulingGroupGeneration_function_003094C8.md) at `0x00309909`
- [KiCommitRescheduleContextEntry](../30/KiCommitRescheduleContextEntry_function_0030CFD0.md) at `0x0030D387`
- [KiCommitRescheduleContextEntry](../30/KiCommitRescheduleContextEntry_function_0030CFD0.md) at `0x0030D3BC`
- [KeAccumulateTicks](../39/KeAccumulateTicks_function_0039C140.md) at `0x0039C3F7`
- [KeQueryEffectivePriorityThread](../3C/KeQueryEffectivePriorityThread_function_003C7CA0.md) at `0x003C7CD8`
- [KeUpdateTotalCyclesCurrentThread](../3F/KeUpdateTotalCyclesCurrentThread_function_003FA2B0.md) at `0x003FA97B`
- [KiCheckForEffectivePriorityChange](../46/KiCheckForEffectivePriorityChange_function_0046DD94.md) at `0x0046DE2E`
- [KiUpdateThreadSchedulingProperties](../46/KiUpdateThreadSchedulingProperties_function_0046E5DC.md) at `0x0046E732`
- [KiInitializePriorityState](../5C/KiInitializePriorityState_function_005C4480.md) at `0x005C4493`
- [sub_006E0CEA](../6E/Unknown_function_006E0CEA.md) at `0x006E0CF0`
- [sub_006E0CEA](../6E/Unknown_function_006E0CEA.md) at `0x006E0D8F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00257BB7` → [sub_00257C8A](Unknown_function_00257C8A.md) (`tail-transfer`)
  - `0x00257BC4` → [sub_00257C8A](Unknown_function_00257C8A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00257BA0  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00257BA5  57                              push rdi
00257BA6  48 83 EC 20                     sub rsp, 0x20
00257BAA  80 B9 C3 00 00 00 10            cmp byte ptr [rcx + 0xc3], 0x10
00257BB1  48 8B EA                        mov rbp, rdx
00257BB4  48 8B F9                        mov rdi, rcx
00257BB7  0F 8D CD 00 00 00               jge 0x140257c8a
00257BBD  48 8B 41 68                     mov rax, qword ptr [rcx + 0x68]
00257BC1  48 85 C0                        test rax, rax
00257BC4  0F 84 C0 00 00 00               je 0x140257c8a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiQueryEffectivePriorityThread(__int64 a1, __int64 a2)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
int64_t KiQueryEffectivePriorityThread(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (32);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0xC3` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00257BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00257BA0[BB_00257BA0]
  bb_00257BBD[BB_00257BBD]
  bb_00257BA0 -->|fallthrough| bb_00257BBD
```
