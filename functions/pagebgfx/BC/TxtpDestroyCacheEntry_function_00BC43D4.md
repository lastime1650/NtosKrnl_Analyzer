# TxtpDestroyCacheEntry

- RVA: `0x00BC43D4`–`0x00BC43F5` (길이 `33` bytes)
- VA: `0x0000000140BC43D4`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC43E1` → [BgpGxRectangleDestroy](BgpGxRectangleDestroy_function_00BC3F04.md) (function, `0x00BC3F04`)
- `0x00BC43E9` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (function, `0x003E25E0`)

### Direct callers
- [TxtpAddCacheEntry](TxtpAddCacheEntry_function_00BC33FC.md) at `0x00BC348C`
- [TxtpClearCache](TxtpClearCache_function_00BC437C.md) at `0x00BC438E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BC43E9` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC43D4  40 53                           push rbx
00BC43D6  48 83 EC 20                     sub rsp, 0x20
00BC43DA  48 8B D9                        mov rbx, rcx
00BC43DD  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00BC43E1  E8 1E FB FF FF                  call 0x140bc3f04
00BC43E6  48 8B CB                        mov rcx, rbx
00BC43E9  E8 F2 E1 81 FF                  call 0x1403e25e0
00BC43EE  48 83 C4 20                     add rsp, 0x20
00BC43F2  5B                              pop rbx
00BC43F3  C3                              ret
00BC43F4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TxtpDestroyCacheEntry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = BgpGxRectangleDestroy(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    result = BgpFwFreeMemory(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TxtpDestroyCacheEntry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = BgpGxRectangleDestroy(*(uint64_t *)(arg1 + 0x30), a2, a3, a4);
    result = BgpFwFreeMemory(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC43D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC43D4[BB_00BC43D4]
  bb_00BC43F4[BB_00BC43F4]
```
