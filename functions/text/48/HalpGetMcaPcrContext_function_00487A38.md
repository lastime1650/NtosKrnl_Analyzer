# HalpGetMcaPcrContext

- RVA: `0x00487A38`–`0x00487A81` (길이 `73` bytes)
- VA: `0x0000000140487A38`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000841D0`
- 디코드: `20`개 명령, `73/73` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00487A69` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpCmciInitializeErrorPacket](HalpCmciInitializeErrorPacket_function_00487010.md) at `0x0048702C`
- [HalpMcaStuckErrorCheck](HalpMcaStuckErrorCheck_function_00487554.md) at `0x00487566`
- [HalpCmciInitProcessor](HalpCmciInitProcessor_function_004875E4.md) at `0x00487647`
- [HalpCmciPollProcessor](HalpCmciPollProcessor_function_00487A88.md) at `0x00487AA0`
- [HalpHvInitMcaPcrContext](../4D/HalpHvInitMcaPcrContext_function_004D7D88.md) at `0x004D7ED8`
- [HalpHvInitMcaPcrContext](../4D/HalpHvInitMcaPcrContext_function_004D7D88.md) at `0x004D7F25`
- [HalpHvInitMcaPcrContext](../4D/HalpHvInitMcaPcrContext_function_004D7D88.md) at `0x004D7F6C`
- [HalpMceHandlerCore](../54/HalpMceHandlerCore_function_00542038.md) at `0x005420A9`
- [HalpMceInitializeErrorPacket](../../pagelk/B7/HalpMceInitializeErrorPacket_function_00B7D4BC.md) at `0x00B7D514`

### Static image references
- `0x00487A51` → RVA `0x00E100D8` (`.data`; read)
- `0x00487A5E` → RVA `0x00FC1D20` (`.data`; read)
- `0x00487A78` → RVA `0x00E10370` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00487A38  48 83 EC 28                     sub rsp, 0x28
00487A3C  48 8B C1                        mov rax, rcx
00487A3F  48 C1 E8 20                     shr rax, 0x20
00487A43  A8 01                           test al, 1
00487A45  75 17                           jne 0x140487a5e
00487A47  8B C1                           mov eax, ecx
00487A49  48 8D 04 40                     lea rax, [rax + rax*2]
00487A4D  48 C1 E0 06                     shl rax, 6
00487A51  48 03 05 80 86 98 00            add rax, qword ptr [rip + 0x988680]
00487A58  48 83 C4 28                     add rsp, 0x28
00487A5C  C3                              ret
00487A5D  CC                              int3
00487A5E  48 8B 05 BB A2 B3 00            mov rax, qword ptr [rip + 0xb3a2bb]
00487A65  0F BA F1 1F                     btr ecx, 0x1f
00487A69  E8 62 30 23 00                  call 0x1406baad0
00487A6E  8B C8                           mov ecx, eax
00487A70  48 8D 04 49                     lea rax, [rcx + rcx*2]
00487A74  48 C1 E0 06                     shl rax, 6
00487A78  48 03 05 F1 88 98 00            add rax, qword ptr [rip + 0x9888f1]
00487A7F  EB D7                           jmp 0x140487a58
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpGetMcaPcrContext(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (a1) >> (32);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00487A5E;
    result = ((unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 2) << (6);
    result = (result) + (*(unsigned __int64 *)(v_rip + 9995904));
loc_00487A58:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00487A5E:
    result = guard_dispatch_icall(a1, a2, a3, a4);
    result = ((unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2) << (6);
    result = (result) + (*(unsigned __int64 *)(v_rip + 9996529));
    goto loc_00487A58;
}
```

## 5. (Beta) C Style

```c
int64_t HalpGetMcaPcrContext(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (Arg1) >> (32);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00487A5E;
    result = ((uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 2) << (6);
    result = (result) + (*(uint64_t *)(v_rip + 0x988680));
loc_00487A58:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00487A5E:
    result = guard_dispatch_icall(Arg1, a2, a3, a4);
    result = ((uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2) << (6);
    result = (result) + (*(uint64_t *)(v_rip + 0x9888F1));
    goto loc_00487A58;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00487A38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00487A38[BB_00487A38]
  bb_00487A47[BB_00487A47]
  bb_00487A58[BB_00487A58]
  bb_00487A5D[BB_00487A5D]
  bb_00487A5E[BB_00487A5E]
  bb_00487A38 -->|branch| bb_00487A5E
  bb_00487A38 -->|fallthrough| bb_00487A47
  bb_00487A47 -->|flow| bb_00487A58
  bb_00487A5D -->|flow| bb_00487A5E
  bb_00487A5E -->|branch| bb_00487A58
```
