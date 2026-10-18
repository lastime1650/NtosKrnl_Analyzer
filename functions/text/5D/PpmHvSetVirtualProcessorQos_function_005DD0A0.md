# PpmHvSetVirtualProcessorQos

- RVA: `0x005DD0A0`–`0x005DD0CF` (길이 `47` bytes)
- VA: `0x00000001405DD0A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005DD0C4` → [HvlpSetRegister64](../4D/HvlpSetRegister64_function_004DDA70.md) (function, `0x004DDA70`)

### Direct callers
- [sub_00391AFF](../39/Unknown_function_00391AFF.md) at `0x00391B25`
- [sub_00391D5F](../39/Unknown_function_00391D5F.md) at `0x00391D9F`
- [KeBugCheck2](../5B/KeBugCheck2_function_005B27D0.md) at `0x005B355B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DD0A0  48 83 EC 28                     sub rsp, 0x28
005DD0A4  48 8B 81 B8 8E 00 00            mov rax, qword ptr [rcx + 0x8eb8]
005DD0AB  48 85 C0                        test rax, rax
005DD0AE  74 19                           je 0x1405dd0c9
005DD0B0  89 50 04                        mov dword ptr [rax + 4], edx
005DD0B3  B9 1B 00 09 00                  mov ecx, 0x9001b
005DD0B8  BA FE FF FF FF                  mov edx, 0xfffffffe
005DD0BD  C7 40 0C 01 00 00 00            mov dword ptr [rax + 0xc], 1
005DD0C4  E8 A7 09 F0 FF                  call 0x1404dda70
005DD0C9  48 83 C4 28                     add rsp, 0x28
005DD0CD  C3                              ret
005DD0CE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmHvSetVirtualProcessorQos(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(a1 + 36536);
    if (*(unsigned __int64 *)(a1 + 36536) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 4) = a2;
        a1 = 0x9001BULL;
        a2 = 0xFFFFFFFEULL;
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 12) = 1;
        result = HvlpSetRegister64(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmHvSetVirtualProcessorQos(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(arg1 + 0x8EB8);
    if (*(uint64_t *)(arg1 + 0x8EB8) != 0) {
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0x4) = Arg2;
        Arg1 = 0x9001BULL;
        Arg2 = 0xFFFFFFFEULL;
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0xC) = 1;
        result = HvlpSetRegister64(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8EB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DD0A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DD0A0[BB_005DD0A0]
  bb_005DD0B0[BB_005DD0B0]
  bb_005DD0C9[BB_005DD0C9]
  bb_005DD0CE[BB_005DD0CE]
  bb_005DD0A0 -->|branch| bb_005DD0C9
  bb_005DD0A0 -->|fallthrough| bb_005DD0B0
  bb_005DD0B0 -->|flow| bb_005DD0C9
```
