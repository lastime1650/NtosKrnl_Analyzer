# FopFreeMappingTable

- RVA: `0x00BC28AC`–`0x00BC28D2` (길이 `38` bytes)
- VA: `0x0000000140BC28AC`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC28BE` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (function, `0x003E25E0`)
- `0x00BC28C6` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (function, `0x003E25E0`)

### Direct callers
- [FopFreeFontData](FopFreeFontData_function_00BC2800.md) at `0x00BC287B`
- [FopReadMappingTable](../../init/C8/FopReadMappingTable_function_00C80BA4.md) at `0x00C80CEF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00BC28BE` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (`PAGEBGFX` → `.text`)
  - `0x00BC28C6` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC28AC  40 53                           push rbx
00BC28AE  48 83 EC 20                     sub rsp, 0x20
00BC28B2  48 8B D9                        mov rbx, rcx
00BC28B5  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00BC28B9  48 85 C9                        test rcx, rcx
00BC28BC  74 05                           je 0x140bc28c3
00BC28BE  E8 1D FD 81 FF                  call 0x1403e25e0
00BC28C3  48 8B CB                        mov rcx, rbx
00BC28C6  E8 15 FD 81 FF                  call 0x1403e25e0
00BC28CB  48 83 C4 20                     add rsp, 0x20
00BC28CF  5B                              pop rbx
00BC28D0  C3                              ret
00BC28D1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FopFreeMappingTable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        result = BgpFwFreeMemory(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    }
    result = BgpFwFreeMemory(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FopFreeMappingTable(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        result = BgpFwFreeMemory(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    }
    result = BgpFwFreeMemory(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC28AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC28AC[BB_00BC28AC]
  bb_00BC28BE[BB_00BC28BE]
  bb_00BC28C3[BB_00BC28C3]
  bb_00BC28D1[BB_00BC28D1]
  bb_00BC28AC -->|branch| bb_00BC28C3
  bb_00BC28AC -->|fallthrough| bb_00BC28BE
  bb_00BC28BE -->|flow| bb_00BC28C3
```
