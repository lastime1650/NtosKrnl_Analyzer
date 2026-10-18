# MiGetAweVadPartition

- RVA: `0x002A94E8`–`0x002A9538` (길이 `80` bytes)
- VA: `0x00000001402A94E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068E00`
- 디코드: `18`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002A9528` → [MiLocateLockedVadEvent](MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x002A9531` → [MiGetAweInfoPartition](MiGetAweInfoPartition_function_002AA2CC.md) (function, `0x002AA2CC`)

### Direct callers
- [MiQueryAddressState](../32/MiQueryAddressState_function_0032C380.md) at `0x0032D10D`
- [MmQueryVirtualMemory](../../page/9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D9FAC`

### Static image references
- `0x002A950B` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A94E8  48 83 EC 28                     sub rsp, 0x28
002A94EC  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
002A94EF  25 00 00 20 0C                  and eax, 0xc200000
002A94F4  3D 00 00 20 08                  cmp eax, 0x8200000
002A94F9  75 28                           jne 0x1402a9523
002A94FB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002A9504  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002A950B  48 8B 05 76 6B B8 00            mov rax, qword ptr [rip + 0xb86b76]
002A9512  0F B7 91 AE 04 00 00            movzx edx, word ptr [rcx + 0x4ae]
002A9519  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
002A951D  48 83 C4 28                     add rsp, 0x28
002A9521  C3                              ret
002A9522  CC                              int3
002A9523  BA 00 01 00 00                  mov edx, 0x100
002A9528  E8 DF E4 FF FF                  call 0x1402a7a0c
002A952D  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
002A9531  E8 96 0D 00 00                  call 0x1402aa2cc
002A9536  EB E5                           jmp 0x1402a951d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetAweVadPartition(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (0xC200000ULL));
    if (((unsigned int)(result)) != 0x8200000ULL) goto loc_002A9523;
loc_002A951D:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12086134) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8);
loc_002A9523:
    result = MiLocateLockedVadEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 256, a3, a4);
    result = MiGetAweInfoPartition(*(unsigned __int64 *)(result + 40), 256, a3, a4);
    goto loc_002A951D;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetAweVadPartition(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (0xC200000ULL));
    if (((uint32_t)(result)) != 0x8200000ULL) goto loc_002A9523;
loc_002A951D:
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(*(uint64_t *)(v_rip + 0xB86B76) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8);
loc_002A9523:
    result = MiLocateLockedVadEvent(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 256, a3, a4);
    result = MiGetAweInfoPartition(*(uint64_t *)(result + 0x28), 256, a3, a4);
    goto loc_002A951D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A94E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A94E8[BB_002A94E8]
  bb_002A94FB[BB_002A94FB]
  bb_002A951D[BB_002A951D]
  bb_002A9522[BB_002A9522]
  bb_002A9523[BB_002A9523]
  bb_002A94E8 -->|branch| bb_002A9523
  bb_002A94E8 -->|fallthrough| bb_002A94FB
  bb_002A94FB -->|flow| bb_002A951D
  bb_002A9522 -->|flow| bb_002A9523
  bb_002A9523 -->|branch| bb_002A951D
```
